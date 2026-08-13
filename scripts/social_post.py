#!/usr/bin/env python3
"""
Posts a new blog entry's title/summary/link to X, LinkedIn, and Instagram.

Four modes, selected by CLI arg:
  find-missing <dir> [<dir> ...]     Prints .md files under the given dirs that
                                      have no summary (or an empty one) and
                                      aren't drafts, one per line.

  generate  <file> [<file> ...]      Writes a Gemini summary into front matter
                                      for files that don't have one yet. Does
                                      NOT post anywhere. Used by the
                                      gemini-summaries workflow, which commits
                                      the result to a branch for PR review.

  sync      <before_sha> <after_sha> Diffs the two commits and posts a file if
                                      either (a) it's newly added and already
                                      has a summary, or (b) it existed before
                                      with no summary and now has one (i.e. its
                                      gemini-summaries PR was just merged).
                                      Never generates a summary itself, so
                                      posting only ever happens with a summary
                                      that's already landed on main. Requires
                                      `social: true` front matter.

  dispatch  <file>                   Manual rerun via Actions UI. Always
                                      posts; generates a summary inline (and
                                      writes it back) if the file has none.

Required env vars:
  SITE_URL                       e.g. https://blog.example.com (no trailing slash)
  X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
  LINKEDIN_ACCESS_TOKEN, LINKEDIN_PERSON_URN
  IG_ACCESS_TOKEN, IG_USER_ID
  GEMINI_API_KEY                 optional - generates `summary` when a post has none

Any platform whose secrets are missing is skipped (logged, not fatal), so you
can wire these up one platform at a time.
"""
import os
import re
import sys
import yaml
import glob
import datetime
import subprocess
import requests
from requests_oauthlib import OAuth1

SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
GEMINI_MODEL = "gemini-3.6-flash"

FEATURE_GLOB_PATTERNS = ["*feature*", "*cover*", "*thumbnail*"]
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif"}

FRONT_MATTER_RE = re.compile(r"^---\n(.*?\n)---\n?", re.DOTALL)


def load_doc(path):
    """Returns (meta_dict, body_text) for a content file's front matter."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def write_doc(path, meta, body):
    # YAML auto-parses date-like fields into datetime objects; re-dumping those
    # would flip Hugo's RFC3339 "T" separator into a space. Keep them as the
    # ISO string Hugo already wrote.
    for key, value in meta.items():
        if isinstance(value, (datetime.date, datetime.datetime)):
            meta[key] = value.isoformat()
    front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"---\n{front}\n---\n{body}")


def page_url(path):
    """content/education/nebula/nebula-level-00/index.md -> /education/nebula/nebula-level-00/"""
    rel = os.path.relpath(path, "content")
    rel = re.sub(r"(^|/)(_?index)\.md$", "", rel)
    rel = rel.strip("/")
    url_path = f"/{rel}/" if rel else "/"
    return f"{SITE_URL}{url_path}"


def resolve_image(path, meta):
    """Mirrors the theme's feature-image lookup: explicit `featureimage` front
    matter, else a *feature*/*cover*/*thumbnail* file next to the content file."""
    bundle_dir = os.path.dirname(path)
    if meta.get("featureimage"):
        candidate = os.path.join(bundle_dir, meta["featureimage"])
        if os.path.isfile(candidate):
            return candidate
    for pattern in FEATURE_GLOB_PATTERNS:
        for candidate in glob.glob(os.path.join(bundle_dir, pattern)):
            if os.path.splitext(candidate)[1].lower() in IMAGE_EXTS:
                return candidate
    return None


def image_url(path, meta):
    image_path = resolve_image(path, meta)
    if not image_path:
        return None
    bundle_dir = os.path.dirname(path)
    filename = os.path.relpath(image_path, bundle_dir)
    return f"{page_url(path)}{filename}"


def strip_markdown(text):
    if not text:
        return ""
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)  # headings
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links -> text
    text = re.sub(r"`([^`]+)`", r"\1", text)  # inline code
    for _ in range(3):  # nested emphasis, a couple passes is enough
        text = re.sub(r"(?<!\w)[*_]{1,3}(?!\s)(.+?)(?<!\s)[*_]{1,3}(?!\w)", r"\1", text)
    return text.strip()


def truncate(text, max_len):
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


PROMPT_PATH = os.path.join(os.path.dirname(__file__), "prompts", "summary.md")


def generate_summary(title, body):
    """Gemini writes a Nebula-card-style summary, per the rules in
    scripts/prompts/summary.md. Falls back to a plain excerpt if no
    GEMINI_API_KEY is set or the request fails, so a missing summary never
    blocks a post."""
    api_key = os.environ.get("GEMINI_API_KEY")
    plain_body = strip_markdown(re.sub(r"```.*?```", "", body, flags=re.DOTALL))
    if not api_key:
        print("  [gemini] no GEMINI_API_KEY set, falling back to a plain excerpt")
        return truncate(re.sub(r"\s+", " ", plain_body), 200)

    with open(PROMPT_PATH, encoding="utf-8") as f:
        system_settings = f.read()
    prompt = (
        f"{system_settings}\n\n"
        f"Title: {title}\n\nPost body:\n{truncate(re.sub(r'[ \\t]+', ' ', body), 6000)}"
    )
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        interaction = client.interactions.create(model=GEMINI_MODEL, input=prompt)
        return interaction.output_text.strip().strip('"')
    except Exception as e:
        print(f"  [gemini] request failed ({e}), falling back to a plain excerpt")
        return truncate(re.sub(r"\s+", " ", plain_body), 200)


def post_x(title, summary, url):
    keys = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    if not all(os.environ.get(k) for k in keys):
        print("  [x] skipped - missing X_* secrets")
        return
    auth = OAuth1(*(os.environ[k] for k in keys))
    # X counts any URL as 23 chars (t.co wrapping) regardless of real length.
    budget = 280 - 23 - len("\n\n\n\n") - len(title)
    body = f"{title}\n\n{truncate(summary, max(budget, 0))}\n\n{url}"
    resp = requests.post("https://api.x.com/2/tweets", auth=auth, json={"text": body}, timeout=30)
    if resp.status_code >= 300:
        raise RuntimeError(f"X post failed: {resp.status_code} {resp.text}")
    print(f"  [x] posted: {resp.json()['data']['id']}")


def post_linkedin(title, summary, url):
    token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    person_urn = os.environ.get("LINKEDIN_PERSON_URN")
    if not (token and person_urn):
        print("  [linkedin] skipped - missing LINKEDIN_* secrets")
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }
    body = {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": title},
                "shareMediaCategory": "ARTICLE",
                "media": [
                    {
                        "status": "READY",
                        "originalUrl": url,
                        "title": {"text": title},
                        "description": {"text": truncate(summary, 256)},
                    }
                ],
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    resp = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=body, timeout=30)
    if resp.status_code >= 300:
        raise RuntimeError(f"LinkedIn post failed: {resp.status_code} {resp.text}")
    print(f"  [linkedin] posted: {resp.headers.get('x-restli-id', 'ok')}")


def post_instagram(title, summary, url, img_url):
    token = os.environ.get("IG_ACCESS_TOKEN")
    ig_user_id = os.environ.get("IG_USER_ID")
    if not (token and ig_user_id):
        print("  [instagram] skipped - missing IG_* secrets")
        return
    if not img_url:
        print("  [instagram] skipped - post has no feature image (Instagram requires one)")
        return
    caption = truncate(f"{title}\n\n{summary}\n\n{url}", 2200)
    api = f"https://graph.facebook.com/v21.0/{ig_user_id}"
    create = requests.post(
        f"{api}/media", data={"image_url": img_url, "caption": caption, "access_token": token}, timeout=30
    )
    if create.status_code >= 300:
        raise RuntimeError(f"Instagram media create failed: {create.status_code} {create.text}")
    creation_id = create.json()["id"]
    publish = requests.post(
        f"{api}/media_publish", data={"creation_id": creation_id, "access_token": token}, timeout=30
    )
    if publish.status_code >= 300:
        raise RuntimeError(f"Instagram publish failed: {publish.status_code} {publish.text}")
    print(f"  [instagram] posted: {publish.json()['id']}")


def find_missing_summaries(dirs):
    """Walks `dirs` and returns .md files with no summary - treating a present
    but empty `summary: ""` the same as a missing key, since a plain text
    grep for `^summary:` can't tell those apart."""
    paths = []
    for d in dirs:
        for root, _, files in os.walk(d):
            for name in files:
                if not name.endswith(".md"):
                    continue
                path = os.path.join(root, name)
                meta, _ = load_doc(path)
                if meta.get("draft"):
                    continue
                if not meta.get("summary"):
                    paths.append(path)
    return sorted(paths)


def generate_only(path):
    """Writes a Gemini summary into `path`'s front matter if it doesn't have
    one. Does not post anywhere - used by the gemini-summaries workflow."""
    if not os.path.isfile(path):
        print(f"skip {path}: file not found")
        return
    meta, body = load_doc(path)
    if meta.get("draft"):
        print(f"skip {path}: draft")
        return
    if meta.get("summary"):
        print(f"skip {path}: already has a summary")
        return
    title = meta.get("title", "").strip()
    meta["summary"] = generate_summary(title, body)
    write_doc(path, meta, body)
    print(f"[gemini] generated summary for {path}")


def git_show(ref, path):
    """Returns the file's content at `ref`, or None if it didn't exist there."""
    result = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None


def had_summary(text):
    if text is None:
        return False
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return False
    meta = yaml.safe_load(m.group(1)) or {}
    return bool(meta.get("summary"))


def changed_content_files(before, after):
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", before, after, "--", "content"],
        capture_output=True, text=True, check=True,
    )
    return [p for p in result.stdout.splitlines() if p.endswith(".md")]


def sync(before, after):
    """Posts newly-added files that already have a summary, and existing
    files that just gained one (their gemini-summaries PR was merged).
    Leaves everything else alone - in particular, never generates a summary
    itself, and never reposts a file whose summary merely changed."""
    success = True
    for path in changed_content_files(before, after):
        if not os.path.isfile(path):
            continue  # deleted in this diff

        before_text = git_show(before, path)
        is_new = before_text is None
        if is_new:
            print(f"{path}: newly added")
        elif had_summary(before_text):
            print(f"skip {path}: already had a summary before this push, not a new-summary event")
            continue
        else:
            print(f"{path}: existing post that just gained a summary")

        if not process(path, require_flag=True, auto_generate=False):
            success = False
    return success


def process(path, require_flag, auto_generate=True):
    if not os.path.isfile(path):
        print(f"skip {path}: file not found")
        return True
    meta, body = load_doc(path)
    if meta.get("draft"):
        print(f"skip {path}: draft")
        return True
    if require_flag and not meta.get("social"):
        print(f"skip {path}: no `social: true` front matter")
        return True

    title = meta.get("title", "").strip()
    if not meta.get("summary"):
        if not auto_generate:
            print(f"skip {path}: no summary yet (waiting on its gemini-summaries PR to be merged)")
            return True
        meta["summary"] = generate_summary(title, body)
        write_doc(path, meta, body)
        print(f"  [gemini] generated summary, wrote back to {path}")
    summary = strip_markdown(meta.get("summary", ""))
    url = page_url(path)
    img = image_url(path, meta)

    print(f"posting {path} -> {url}")
    ok = True
    for name, fn in (("X", post_x), ("LinkedIn", post_linkedin), ("Instagram", None)):
        try:
            if name == "Instagram":
                post_instagram(title, summary, url, img)
            else:
                fn(title, summary, url)
        except Exception as e:
            ok = False
            print(f"  [{name.lower()}] ERROR: {e}")
    return ok


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    mode, rest = sys.argv[1], sys.argv[2:]

    if mode == "find-missing":
        for path in find_missing_summaries(rest):
            print(path)
        sys.exit(0)

    if mode == "generate":
        for path in rest:
            generate_only(path)
        sys.exit(0)

    if mode == "sync":
        if len(rest) != 2:
            print("usage: social_post.py sync <before_sha> <after_sha>")
            sys.exit(2)
        sys.exit(0 if sync(rest[0], rest[1]) else 1)

    if mode == "dispatch":
        success = True
        for path in rest:
            if not process(path, require_flag=False, auto_generate=True):
                success = False
        sys.exit(0 if success else 1)

    print(f"unknown mode: {mode}")
    sys.exit(2)


if __name__ == "__main__":
    main()
