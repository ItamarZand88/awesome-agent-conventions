# llms.txt 🟢 Adopted

> A proposed-turned-widely-published standard: a root-level Markdown file giving LLMs a curated, link-rich map of a site's docs. Published across hundreds of developer-docs sites - though whether the major LLM providers actually read it remains unproven.

- **Read by:** Docs sites publish it for LLM tools and crawlers - though no major provider has confirmed reading it
- **Location:** Site root: /llms.txt (and optionally /llms-full.txt)
- **Spec:** [https://llmstxt.org](https://llmstxt.org)
- **Evidence:** llms.txt is published by many developer-docs sites, including Anthropic and Stripe, even though major-provider consumption is unconfirmed.
- **Last verified:** 2026-06-18
- **Files:** `llms.txt`, `llms-full.txt`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `llms.txt`

Curated index: short description plus linked sections of the key docs.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `docs.anthropic.com` | [`docs.anthropic.com`](https://docs.anthropic.com) | [`examples/docs-anthropic/llms.txt`](examples/docs-anthropic/llms.txt) | [source](https://docs.anthropic.com/llms.txt) |
| `docs.stripe.com` | [`docs.stripe.com`](https://docs.stripe.com) | [`examples/docs-stripe/llms.txt`](examples/docs-stripe/llms.txt) | [source](https://docs.stripe.com/llms.txt) |

### `llms-full.txt`

The full docs concatenated into one file for direct ingestion.

**Pattern - not an extracted file.**

Every documentation page concatenated into a single plain-text file for direct ingestion - routinely multiple megabytes. Structurally it's `llms.txt` with each linked page inlined in full; nothing instance-specific is worth vendoring, so this entry links live instances rather than copying a dump.

Live instances (fetch directly - too large or instance-specific to vendor):

- [docs.anthropic.com/llms-full.txt](https://docs.anthropic.com/llms-full.txt)
- [prisma.io/docs/llms-full.txt](https://www.prisma.io/docs/llms-full.txt)

## Field notes

### Format
Strict element order (only the H1 is required):

1. **H1** - the project/site name. **The one required element.**
2. **Blockquote** (`>`) - optional short summary.
3. **Zero+ free-prose sections** - optional Markdown paragraphs/lists; **must not contain headings**.
4. **Zero+ H2 "file-list" sections** - each `## Section` holds a bullet list of links: `[name](url): optional notes` (the link is required, the `: notes` suffix optional).
5. **`## Optional`** - a special H2 whose links may be **skipped when a shorter context is needed** (lowest priority).

`llms-full.txt` is the whole docs concatenated into one file (same H1 + blockquote + H2 shape). Both live at the **site root** (`/llms.txt`, `/llms-full.txt`). The `llms_txt2ctx` CLI expands an `llms.txt` into `llms-ctx.txt` (excludes Optional) / `llms-ctx-full.txt` (includes it).

### Composition
- **`llms.txt`** is a *map* - H1, blockquote summary, then curated linked sections (the Anthropic and Stripe files both follow this shape).
- **`llms-full.txt`** is the *payload* - the entire docs concatenated for direct ingestion.

### Anti-patterns
- **Serving HTML at the `.txt` URL.** Several sites return a rendered HTML shell instead of plain text - which defeats the point for a fetching agent. Verify the response is actually `text/plain`.
- Dumping everything into `llms.txt` instead of curating - the index should *select*, not mirror. (Free-prose sections also can't carry headings - those start the file-list sections.)
- Letting either file drift out of sync with the live docs.

### Edge cases
- **Published is not the same as read.** Hundreds of sites ship `llms.txt`, but consumption is unproven: Google has publicly said it doesn't use it, and studies find most files draw little or no crawler traffic. Treat it as making docs *available* to agents that choose to fetch it, not a channel the major providers read by default.
- `llms-full.txt` can blow past a model's context window; some sites paginate or offer per-section full files.

### Adoption / maturity
- The format is adopted as a publishing pattern: developer-docs sites such as Anthropic and Stripe expose it, and docs tooling can generate it. The consumer side is weaker: no major model provider has made a durable, public commitment that its production retrieval or training systems obey `llms.txt`.
- The honest use case is "give agents a clean map they can fetch," not "control crawler behavior" and not "force AI search visibility." For control/consent, look at robots.txt, AI Preferences drafts, or `ai.txt` proposals instead.

### Related conventions
- `llms.txt` is an index. `llms-full.txt` is the expanded payload. `pricing.md` is a page-level Markdown twin that can be linked from either.
- A site can publish all three, but each answers a different question: "where is the useful docs context?", "give me the full docs text", and "give me this page in parseable Markdown."

### Sources checked
- [llms.txt proposal](https://llmstxt.org/)
- [Anthropic docs llms.txt](https://docs.anthropic.com/llms.txt)
- [Stripe docs llms.txt](https://docs.stripe.com/llms.txt)
- [llms_txt2ctx parser / CLI](https://github.com/AnswerDotAI/llms-txt)
