# llms.txt 🟢 Adopted

> A proposed-turned-widely-shipped standard: a root-level Markdown file giving LLMs a curated, link-rich map of a site's docs. Adopted across hundreds of developer-docs sites.

- **Read by:** LLM-powered docs tools, agents, and crawlers that look for /llms.txt
- **Location:** Site root: /llms.txt (and optionally /llms-full.txt)
- **Spec:** [https://llmstxt.org](https://llmstxt.org)
- **Files:** `llms.txt`, `llms-full.txt`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `llms.txt`

Curated index: short description plus linked sections of the key docs.

| Source | File | Provenance |
| --- | --- | --- |
| `docs.anthropic.com` | [`docs.anthropic.com.llms.txt`](examples/docs.anthropic.com.llms.txt) | [source](https://docs.anthropic.com/llms.txt) |
| `docs.stripe.com` | [`docs.stripe.com.llms.txt`](examples/docs.stripe.com.llms.txt) | [source](https://docs.stripe.com/llms.txt) |

### `llms-full.txt`

The full docs concatenated into one file for direct ingestion.

| Source | File | Provenance |
| --- | --- | --- |
| `docs.anthropic.com` | [`docs.anthropic.com.llms-full.txt`](examples/docs.anthropic.com.llms-full.txt) | [source](https://docs.anthropic.com/llms-full.txt) |
| `www.prisma.io` | [`www.prisma.io.llms-full.txt`](examples/www.prisma.io.llms-full.txt) | [source](https://www.prisma.io/docs/llms-full.txt) |

## Field notes

### Composition
Two files, two jobs:
- **`llms.txt`** is a *map* — an H1, a blockquote summary, then curated, linked sections of the key docs (the Anthropic and Stripe files both follow this shape).
- **`llms-full.txt`** is the *payload* — the entire docs concatenated into one file for direct ingestion (Anthropic's runs to a very large single document).

### Anti-patterns
- **Serving HTML at the `.txt` URL.** Several sites (e.g. Cursor's `llms-full.txt`) return a rendered HTML shell instead of plain text — which defeats the entire point for a fetching agent. Verify the response is actually `text/plain`.
- Dumping everything into `llms.txt` instead of curating — the index should *select*, not mirror.
- Letting either file drift out of sync with the live docs.

### Edge cases
- `llms.txt` (curated map) vs `llms-full.txt` (full dump) are complementary, not alternatives — ship the map always, the full file when ingestion is the goal.
- `llms-full.txt` can blow past a model's context window; some sites paginate or offer per-section full files.
- Both live at the **site root**, discoverable by convention (`/llms.txt`).
