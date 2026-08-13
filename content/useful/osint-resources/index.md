---
title: "OSINT Resources"
date: 2026-02-02T18:50:00+01:00
draft: false
tags: ["osint"]
categories: ["Hacking"]
summary: "A curated toolbox for OSINT investigations — username/email/IP lookups, social graph mapping, metadata, and reverse-image search, organized around **verification questions** instead of a flat link dump."
---

## It's easy to chase the narrative you want, not the truth.
### Username/Email/IP
Username / handle reuse – search same handle on other sites; record all matches in one sheet

| Link/Name                                                                          | Comment                             | Type     |
| ---------------------------------------------------------------------------------- | ----------------------------------- | -------- |
| [UserSearch](http://usersearch.org/)                     | Cross-platform username search      | SaaS     |
| [Holehe](https://github.com/megadose/holehe) | Email-based site registration check | Software |
| [osint.rocks](https://osint.rocks/)                        | Automated username search           | SaaS     |
| [BreachDirectory](https://breachdirectory.org/)    | Breached username check             | SaaS     |
| [Censys](https://search.censys.io/)                   | IP Search                           | SaaS     |
| [Shodan](https://www.shodan.io/)                         | Internet General Search             | SaaS     |
| [Have I been Pwned](https://haveibeenpwned.com/)    | Email-based leak check              | SaaS     |
| [MailCat](https://github.com/sharsil/mailcat)                                      | Find existing email addresses       | Software |

### Social Media Tools 
Social graph signals > single posts – pull top 10 interactors and scan for repeated overlap  

| Link/Name                                                                                                                                    | Comment                   | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------- |
| [InsE](https://chromewebstore.google.com/detail/inse-instagram-email-find/hboikjnbkhkjmllgdcflmbcojbpklcca?pli=1) | Instagram Email Extractor | Chrome Plugin |
| [Castrick](https://castrickclues.com/)                                                                         | Connections Mapper        | SaaS          |
| [GHunt](https://github.com/mxrch/GHunt)                                                                    | Google Account            | Software      |
### Metadata
download file/photo, check EXIF or doc properties for names/emails

| Link/Name                                                  | Comment                      | Type     |
| ---------------------------------------------------------- | ---------------------------- | -------- |
| [ExifTool](https://exiftool.org/) | Read, write, edit metadata   | Software |
| [LeakIX](https://leakix.net)            | Public Leak Detection/Finder | SaaS     |

Temporal & location patterns – log 10 most recent post times, compare to timezone map  

### Cross-platform redundancy
collect job titles from LinkedIn, Instagram captions, GitHub bio and compare 

| Link/Name                                                       | Comment                                   | Type |
| --------------------------------------------------------------- | ----------------------------------------- | ---- |
| [Epieos](https://epieos.com/)            | Profile aggregation by email              | SaaS |
| [That’s them](https://thatsthem.com/) | Reverse lookup for employment cross-check | SaaS |
| [Skymem](https://skymem.com/)            | Email-based public data search            | SaaS |
  
### Common recurring keypoints  
Reuse of elements – see if matches appear elsewhere

| Link/Name                                                        | Comment                      | Type |
| ---------------------------------------------------------------- | ---------------------------- | ---- |
| [DorkSearch](https://dorksearch.com/) | Pattern-based Google dorking | SaaS |
| [UserSearch](http://usersearch.org/)   | Keyword-based username scan  | SaaS |
  
### Visual overlaps
match objects/backgrounds in photos, save side-by-side for reference  

| Link/Name                                                                 | Comment                            | Type |
| ------------------------------------------------------------------------- | ---------------------------------- | ---- |
| [TinEye](https://tineye.com/)                      | External duplicate image detection | SaaS |
| [Google Images](https://images.google.com/) |                                    | SaaS |
| [Yandex](https://yandex.com/)                      | External reverse image search      | SaaS |
  
### Public records fill gaps
check local registry to confirm address; screenshot results with source date  

| Link/Name                                                       | Comment                   | Type |
| --------------------------------------------------------------- | ------------------------- | ---- |
| [CriminalIP](https://criminalip.io/)   | Asset/risk correlation    | SaaS |
| [That’s them](https://thatsthem.com/) | Public records validation | SaaS |

### Social media OSINT – essential questions  
What other accounts are linked? – search email/phone in reverse lookup; note matches

| Link/Name                                                                          | Comment                             | Type     |
| ---------------------------------------------------------------------------------- | ----------------------------------- | -------- |
| [Epieos](https://epieos.com/)                               | Profile aggregation by email        | SaaS     |
| [Holehe](https://github.com/megadose/holehe) | Email-based site registration check | Software |
| [MailCat](https://github.com/sharsil/mailcat)                                      | Find existing email addresses       | Software |
### Who are the top interactors?
pull top 10 interactors and note overlaps in multiple posts 

| Link/Name                                                                                                                                    | Comment                   | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------- |
| [InsE](https://chromewebstore.google.com/detail/inse-instagram-email-find/hboikjnbkhkjmllgdcflmbcojbpklcca?pli=1) | Instagram Email Extractor | Chrome Plugin |
  
### Which accounts are frequently co-tagged?
list all tagged accounts in last 20 posts and rank by frequency 

### Do mutual connections span same domains?
tag each mutual as work, school, or hobby; see dominant group

| Link/Name                                                                             | Comment            | Type |
| ------------------------------------------------------------------------------------- | ------------------ | ---- |
| [Castrick](https://castrickclues.com/)                  | Connections Mapper | SaaS |
| [FullHunt](https://fullhunt.io/)                              | Domain Map         | SaaS |
| [Subdomain Finder](https://subdomainfinder.c99.nl/) | Subdomain Mapper   | SaaS |
  
### Are posts geotagged or show landmarks?
cross-check location tag with Google Maps Street View 

| Link/Name                                                          | Comment                        | Type |
| ------------------------------------------------------------------ | ------------------------------ | ---- |
| [FOFA](https://en.fofa.info/)             | Geolocated asset mapping       | SaaS |
| [Google Maps](https://maps.google.com/) | External location verification | SaaS |
  
### Do timestamps show routines?
plot post times on a simple chart to find regular posting windows  
  
### Are there employment or education cues?
collect company names, logos, school crests from images 

| Link/Name                                                                                  | Comment                      | Type |
| ------------------------------------------------------------------------------------------ | ---------------------------- | ---- |
| [Hunter Domain Search](https://hunter.io/domain-search) | Company role verification    | SaaS |
| [Netlas](https://netlas.io/)                                         | Organization-based discovery | SaaS |
  
### Do reverse-image searches find duplicates?
run top 5 profile pics through reverse image search, log matches 

| Link/Name                                                                 | Comment                 | Type |
| ------------------------------------------------------------------------- | ----------------------- | ---- |
| [ZoomEye](https://www.zoomeye.ai/)             | Device mapping/finder   | SaaS |
| [Onyphe](https://search.onyphe.io/)          | Image metadata analysis | SaaS |
| [Google Images](https://images.google.com/) |                         | SaaS |

## All tools/links:

| Link/Name                                                                                                                                    | Comment                                   | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------- |
| [CyberSec Tools](https://cybersectools.com/)                                                                                                 |                                           | Tools         |
| [Binary Edge](https://binaryedge.io/)                                                                              | Threat intelligence platform              | SaaS          |
| [BreachDirectory](https://breachdirectory.org/)                                                              | Breached username check                   | SaaS          |
| [Castrick](https://castrickclues.com/)                                                                         | Connections Mapper                        | SaaS          |
| [Censys](https://search.censys.io/)                                                                             | IP Search                                 | SaaS          |
| [CriminalIP](https://criminalip.io/)                                                                                | Asset/risk correlation                    | SaaS          |
| [DorkSearch](https://dorksearch.com/)                                                                             | Pattern-based Google dorking              | SaaS          |
| [Epieos](https://epieos.com/)                                                                                         | Profile aggregation by email              | SaaS          |
| [ExifTool](https://exiftool.org/)                                                                                   | Read, write, edit metadata                | Software      |
| [FOFA](https://en.fofa.info/)                                                                                       | Geolocated asset mapping                  | SaaS          |
| [FullHunt](https://fullhunt.io/)                                                                                     | Domain Map                                | SaaS          |
| [GHunt](https://github.com/mxrch/GHunt)                                                                    | Google Account                            | Software      |
| [Google Images](https://images.google.com/)                                                                    |                                           | SaaS          |
| [Google Maps](https://maps.google.com/)                                                                           | External location verification            | SaaS          |
| [Grey Noise](https://www.greynoise.io/)                                                                         | Scan noise intelligence                   | SaaS          |
| [Have I been Pwned](https://haveibeenpwned.com/)                                                              | Email-based leak check                    | SaaS          |
| [Holehe](https://github.com/megadose/holehe)                                                           | Email-based site registration check       | Software      |
| [Hunter Domain Search](https://hunter.io/domain-search)                                                   | Company role verification                 | SaaS          |
| [InsE](https://chromewebstore.google.com/detail/inse-instagram-email-find/hboikjnbkhkjmllgdcflmbcojbpklcca?pli=1) | Instagram Email Extractor                 | Chrome Plugin |
| [LeakIX](https://leakix.net)                                                                                              | Public Leak Detection/Finder              | SaaS          |
| [MailCat](https://github.com/sharsil/mailcat)                                                                                                | Find existing email addresses             | Software      |
| [Netlas](https://netlas.io/)                                                                                           | Organization-based discovery              | SaaS          |
| [Onyphe](https://search.onyphe.io/)                                                                             | Image metadata analysis                   | SaaS          |
| [osint.rocks](https://osint.rocks/)                                                                                  | Automated username search                 | SaaS          |
| [Packet Storm News](https://www.packetstorm.news/)                                                          | Security tools and exploits               | News          |
| [Shodan](https://www.shodan.io/)                                                                                   | Internet General Search                   | SaaS          |
| [Skymem](https://skymem.com/)                                                                                         | Email-based public data search            | SaaS          |
| [Subdomain Finder](https://subdomainfinder.c99.nl/)                                                        |                                           | SaaS          |
| [That’s them](https://thatsthem.com/)                                                                              | Reverse lookup for employment cross-check | SaaS          |
| [TinEye](https://tineye.com/)                                                                                         | External duplicate image detection        | SaaS          |
| [UserSearch](http://usersearch.org/)                                                                               | Cross-platform username search            | SaaS          |
| [UserSearch](http://usersearch.org/)                                                                               | Keyword-based username scan               | SaaS          |
| [VX Underground](https://vx-underground.org/)                                                                 | Malware Library                           | Tools         |
| [Yandex](https://yandex.com/)                                                                                         | External reverse image search             | SaaS          |
| [ZoomEye](https://www.zoomeye.ai/)                                                                                | Device mapping/finder                     | SaaS          |
