### Composition
Two files, two jobs:
- **`llms.txt`** is a *map* - an H1, a blockquote summary, then curated, linked sections of the key docs (the Anthropic and Stripe files both follow this shape).
- **`llms-full.txt`** is the *payload* - the entire docs concatenated into one file for direct ingestion (Anthropic's runs to a very large single document).

### Anti-patterns
- **Serving HTML at the `.txt` URL.** Several sites (e.g. Cursor's `llms-full.txt`) return a rendered HTML shell instead of plain text - which defeats the entire point for a fetching agent. Verify the response is actually `text/plain`.
- Dumping everything into `llms.txt` instead of curating - the index should *select*, not mirror.
- Letting either file drift out of sync with the live docs.

### Edge cases
- **Published is not the same as read.** Hundreds of sites ship `llms.txt`, but consumption is unproven: Google has publicly said it doesn't use it, and studies find most `llms.txt` files draw little or no crawler traffic. Treat it as making docs *available* to agents that choose to fetch it, not a channel the major providers read by default.
- `llms.txt` (curated map) vs `llms-full.txt` (full dump) are complementary, not alternatives - ship the map always, the full file when ingestion is the goal.
- `llms-full.txt` can blow past a model's context window; some sites paginate or offer per-section full files.
- Both live at the **site root**, discoverable by convention (`/llms.txt`).
