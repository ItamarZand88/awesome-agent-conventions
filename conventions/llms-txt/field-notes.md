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
