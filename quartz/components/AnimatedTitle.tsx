import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { i18n } from "../i18n"

const AnimatedTitle: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
  const title = cfg?.pageTitle ?? i18n(cfg.locale).propertyDefaults.title
  const baseDir = pathToRoot(fileData.slug!)
  return (
    <h2 class={classNames(displayClass, "page-title")}>
      <a href={baseDir}><span class="title-text">{title}</span></a>
    </h2>
  )
}

AnimatedTitle.css = `
.page-title {
  font-size: 1.75rem;
  margin: 0;
  font-family: var(--titleFont);
}

.page-title .title-text {
  color: white; /* Default color for scrambled text */
}

.original-char {
  color: red;
}

.typing-cursor {
  color: white; /* Ensure cursor is visible */
  animation: blink 1s step-end infinite;
}

@keyframes blink {
  from, to {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}
`

AnimatedTitle.afterDOMLoaded = `
document.addEventListener("DOMContentLoaded", () => {
  const titleElement = document.querySelector('.page-title .title-text');
  if (!titleElement) return;

  // --- Timer Variables ---
  const animationSpeed = 60;
  const flickerSpeed = 60;
  const flickerDuration = 1000;
  const pauseDuration = 4000;
  // -----------------------

  const originalText = titleElement.textContent || "";
  const chars = '!@#$%^&*()_+-=[]{}|;:,.<>?';
  let intervalId = null;
  let flickerIntervalId = null;
  let targetScrambledText = [];

  const wrapOriginal = (text) => text.split('').map(char => \`<span class="original-char">\${char}</span>\`).join('');

  const animate = (direction, onComplete) => {
    let iteration = 0;
    clearInterval(intervalId);

    if (direction === 'encrypt') {
      targetScrambledText = originalText.split('').map(() => chars[Math.floor(Math.random() * chars.length)]);
    }

    intervalId = setInterval(() => {
      if (direction === 'decrypt') {
        const revealedPart = wrapOriginal(originalText.substring(0, iteration));
        const cursor = '<span class="typing-cursor">|</span>';
        const scrambledPart = targetScrambledText.slice(iteration).join('');
        titleElement.innerHTML = revealedPart + cursor + scrambledPart;
      } else { // Encrypt
        const newText = originalText.split("").map((letter, index) => {
          if (index >= originalText.length - iteration) {
            return targetScrambledText[index];
          } else {
            return \`<span class="original-char">\${originalText[index]}</span>\`;
          }
        }).join("");
        titleElement.innerHTML = newText;
      }

      if (iteration >= originalText.length) {
        clearInterval(intervalId);
        titleElement.innerHTML = direction === 'decrypt' ? wrapOriginal(originalText) : targetScrambledText.join('');
        if (onComplete) onComplete();
      }

      iteration += 1;
    }, animationSpeed);
  };

  const runAnimationCycle = () => {
    animate('encrypt', () => {
      let flickerTimeout;
      flickerIntervalId = setInterval(() => {
        const randomText = originalText.split('').map(() => chars[Math.floor(Math.random() * chars.length)]).join('');
        titleElement.innerHTML = randomText;
      }, flickerSpeed);

      flickerTimeout = setTimeout(() => {
        clearInterval(flickerIntervalId);
        clearTimeout(flickerTimeout);

        targetScrambledText = (titleElement.textContent || "").split('');
        animate('decrypt', () => {
          const cursor = '<span class="typing-cursor">|</span>';
          titleElement.innerHTML = wrapOriginal(originalText) + cursor;
          setTimeout(runAnimationCycle, pauseDuration);
        });
      }, flickerDuration);
    });
  };

  runAnimationCycle();
});
`


export default (() => AnimatedTitle) satisfies QuartzComponentConstructor