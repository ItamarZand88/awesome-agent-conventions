# ai.txt 🔵 Proposed

> A text file declaring machine-readable consent, licensing, or policy preferences for AI training and data-mining. Spawning popularized the deployed root-file pattern, and a 2026 Internet-Draft now proposes a well-known URI; adoption and crawler obedience are still thin, so it stays 🔵.

- **Read by:** AI training/data-mining crawlers that voluntarily honor AI usage preferences; crawler support is not yet reliable
- **Location:** Site root /ai.txt in Spawning's deployed pattern; /.well-known/ai.txt in the newer Internet-Draft
- **Spec:** [https://datatracker.ietf.org/doc/draft-car-ai-txt-wellknown/](https://datatracker.ietf.org/doc/draft-car-ai-txt-wellknown/)
- **Evidence:** Spawning popularized deployed ai.txt files and a 2026 Internet-Draft proposes /.well-known/ai.txt, but crawler obedience and adoption remain unproven.
- **Last verified:** 2026-06-26
- **Files:** `ai.txt`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `ai.txt`

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `fuhi-timebaibai` | [`FUHI12342/NewFUHI`](https://github.com/FUHI12342/NewFUHI) | [`examples/fuhi-timebaibai/ai.txt`](examples/fuhi-timebaibai/ai.txt) | [source](https://raw.githubusercontent.com/FUHI12342/NewFUHI/main/static/ai.txt) |
| `hyperpolymath-standards` | [`hyperpolymath/standards`](https://github.com/hyperpolymath/standards) | [`examples/hyperpolymath-standards/ai.txt`](examples/hyperpolymath-standards/ai.txt) | [source](https://raw.githubusercontent.com/hyperpolymath/standards/main/.well-known/ai.txt) |
| `in8finity-codex-formal` | [`in8finity/codex-formal-plugin`](https://github.com/in8finity/codex-formal-plugin) | [`examples/in8finity-codex-formal/ai.txt`](examples/in8finity-codex-formal/ai.txt) | [source](https://raw.githubusercontent.com/in8finity/codex-formal-plugin/main/plugins/formal-methods/ai.txt) |
| `intruvurt-aivis` | [`intruvurt/aivis`](https://github.com/intruvurt/aivis) | [`examples/intruvurt-aivis/ai.txt`](examples/intruvurt-aivis/ai.txt) | [source](https://raw.githubusercontent.com/intruvurt/aivis/main/ai.txt) |
| `koji-blog` | [`koji/blog`](https://github.com/koji/blog) | [`examples/koji-blog/ai.txt`](examples/koji-blog/ai.txt) | [source](https://raw.githubusercontent.com/koji/blog/master/public/ai.txt) |
| `laura-esteves` | [`lauralesteves/quecoreagora.lauraesteves.com`](https://github.com/lauralesteves/quecoreagora.lauraesteves.com) | [`examples/laura-esteves/ai.txt`](examples/laura-esteves/ai.txt) | [source](https://raw.githubusercontent.com/lauralesteves/quecoreagora.lauraesteves.com/main/public/ai.txt) |
| `manujdixit-resumio` | [`Manujdixit/resumio`](https://github.com/Manujdixit/resumio) | [`examples/manujdixit-resumio/ai.txt`](examples/manujdixit-resumio/ai.txt) | [source](https://raw.githubusercontent.com/Manujdixit/resumio/master/apps/web/public/ai.txt) |
| `openverse` | [`WordPress/openverse`](https://github.com/WordPress/openverse) | [`examples/openverse/ai.txt`](examples/openverse/ai.txt) | [source](https://raw.githubusercontent.com/WordPress/openverse/main/frontend/src/static/ai.txt) |
| `reserve-protocol-register` | [`reserve-protocol/register`](https://github.com/reserve-protocol/register) | [`examples/reserve-protocol-register/ai.txt`](examples/reserve-protocol-register/ai.txt) | [source](https://raw.githubusercontent.com/reserve-protocol/register/master/public/.well-known/ai.txt) |
| `smirakle-art-guardian` | [`smirakle/art-guardian-ai`](https://github.com/smirakle/art-guardian-ai) | [`examples/smirakle-art-guardian/ai.txt`](examples/smirakle-art-guardian/ai.txt) | [source](https://raw.githubusercontent.com/smirakle/art-guardian-ai/main/public/ai.txt) |
| `vic-k-y-portfolio` | [`vic-k-y/new-portfolio`](https://github.com/vic-k-y/new-portfolio) | [`examples/vic-k-y-portfolio/ai.txt`](examples/vic-k-y-portfolio/ai.txt) | [source](https://raw.githubusercontent.com/vic-k-y/new-portfolio/main/ai.txt) |
| `vladikk-modularity` | [`vladikk/modularity`](https://github.com/vladikk/modularity) | [`examples/vladikk-modularity/ai.txt`](examples/vladikk-modularity/ai.txt) | [source](https://raw.githubusercontent.com/vladikk/modularity/main/ai.txt) |

## Field notes

### Directives
Two shapes now matter:

- **Spawning root-file pattern** - the deployed examples this catalog vendors.
  It mirrors `robots.txt` grouping.
- **2026 Internet-Draft** - `draft-car-ai-txt-wellknown`, which proposes
  `/.well-known/ai.txt` with site fields such as `Spec-Version`, `Site-Name`,
  `Site-URL`, and `Training`.

Spawning's generator emits:

| Directive | Meaning |
| --- | --- |
| `# Spawning AI` | preamble comment |
| `User-Agent: *` | the only user-agent the canonical file emits |
| `Disallow: <pattern>` | opt the listed paths/extensions **out** of AI training/TDM |
| `Allow: <pattern>` | opt them **in** |
| `Disallow: /` / `Disallow: *` | global opt-out (the whole site) |
| `Allow: /` | global opt-in |

**Default = everything opted out** (Disallow); a category becomes `Allow` only if the owner toggles it on. Rules are keyed off file-extension globs grouped into **five media categories**: **Images, Audio, Video, Text, Code**. The **Text** category is special (`globalFlag`): allowing it flips the site-wide rule to `Allow: /`. The Internet-Draft uses a different key-value vocabulary, so do not assume all `ai.txt` files share one schema yet.

### Composition
- A short, robots.txt-shaped file: a `User-Agent` line plus `Allow`/`Disallow` lines carrying comma-separated extension lists per media category, declaring training and data-mining consent.

### Anti-patterns
- Treating it as enforcement. It's a *declaration* of consent, not a technical block - crawlers can ignore it, and most do.
- Hand-rolling a schema and calling it standard. Live files vary widely, and the new Internet-Draft is still work-in-progress material.

### Edge cases
- **🔵 Proposed, labelled down on purpose.** There's real work here (Spawning's deployed pattern, an IETF AI Preferences WG vocabulary/attachment effort, and a June 2026 individual Internet-Draft for `/.well-known/ai.txt`), but adoption is thin and crawler obedience is not demonstrable. Until consumption is reliable, it sits below 🟠.
- Read at **media-download / usage-policy** time, not plain crawl discovery time. Orthogonal to the files it's confused with: `robots.txt` AI user-agents (`GPTBot`...) restrict *crawling*; `llms.txt` *exposes* docs; `ai.txt` declares *training / usage preference*. Placement is still unsettled - Spawning uses `/ai.txt`, while the Internet-Draft proposes `/.well-known/ai.txt`.
- **Adjacent draft:** `agents.txt` / `agents.json` now has its own Internet-Draft for site-level capability declarations. It is related, but not listed as a full convention here until there are live examples or demonstrated readers beyond the draft.

### Adoption / maturity
- The label stays 🔵 because there are multiple competing shapes and no clear consumption contract. Spawning's original root-file syntax exists in public examples; the June 2026 Internet-Draft proposes `/.well-known/ai.txt` and `/.well-known/ai.json` with a different structured vocabulary.
- The IETF AI Preferences work is adjacent but not identical: it defines vocabulary for expressing use preferences over digital assets, while `ai.txt` is one possible discovery/container file shape.

### Related conventions
- Use robots.txt for crawl access preferences, `llms.txt` for inference-time content maps, and `ai.txt` only as a policy declaration whose enforcement depends on reader cooperation.
- Do not present `ai.txt` as a legal or technical blocker unless a consuming crawler explicitly documents support.

### Sources checked
- [Spawning ai.txt announcement](https://spawning.substack.com/p/aitxt-a-new-way-for-websites-to-set)
- [IETF draft-car-ai-txt-wellknown-00](https://datatracker.ietf.org/doc/html/draft-car-ai-txt-wellknown-00)
- [IETF AI Preferences vocabulary draft](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/03/)
- [Openverse ai.txt example](https://raw.githubusercontent.com/WordPress/openverse/main/frontend/src/static/ai.txt)
