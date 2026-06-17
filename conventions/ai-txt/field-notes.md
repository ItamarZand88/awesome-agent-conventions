### Directives
Mirrors `robots.txt` grouping. Spawning's generator emits:

| Directive | Meaning |
| --- | --- |
| `# Spawning AI` | preamble comment |
| `User-Agent: *` | the only user-agent the canonical file emits |
| `Disallow: <pattern>` | opt the listed paths/extensions **out** of AI training/TDM |
| `Allow: <pattern>` | opt them **in** |
| `Disallow: /` / `Disallow: *` | global opt-out (the whole site) |
| `Allow: /` | global opt-in |

**Default = everything opted out** (Disallow); a category becomes `Allow` only if the owner toggles it on. Rules are keyed off file-extension globs grouped into **five media categories**: **Images, Audio, Video, Text, Code**. The **Text** category is special (`globalFlag`): allowing it flips the site-wide rule to `Allow: /`.

### Composition
- A short, robots.txt-shaped file: a `User-Agent` line plus `Allow`/`Disallow` lines carrying comma-separated extension lists per media category, declaring training and data-mining consent.

### Anti-patterns
- Treating it as enforcement. It's a *declaration* of consent, not a technical block - crawlers can ignore it, and most do.
- Hand-rolling a schema that diverges from Spawning's; live files vary widely. The canonical shape is best taken from Spawning's own generator config, not from any one adopter.

### Edge cases
- **🔵 Proposed, labelled down on purpose.** There's a real org (Spawning) and a real spec tied to the EU DSM Article 4 TDM opt-out, but adoption is thin: Spawning's own docs concede most bots don't honor it, and live files disagree on format. Until consumption is demonstrable, it sits below 🟠.
- Read at **media-download** time, not crawl time. Orthogonal to the files it's confused with: `robots.txt` AI user-agents (`GPTBot`...) restrict *crawling*; `llms.txt` *exposes* docs; `ai.txt` restricts *training* use. Placement is still unsettled - site root vs `/.well-known/ai.txt`.
