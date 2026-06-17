### Composition
Two files, two jobs:
- **`llms.txt`** is a *map* - an H1, a blockquote summary, then curated, linked sections of the key docs (the Anthropic and Stripe files both follow this shape).
- **`llms-full.txt`** is the *payload* - the entire docs concatenated into one file for direct ingestion (Anthropic's runs to a very large single document).

### Anti-patterns
- **Serving HTML at the `.txt` URL.** Several sites (e.g. Cursor's `llms-full.txt`) return a rendered HTML shell instead of plain text - which defeats the entire point for a fetching agent. Verify the response is actually `text/plain`.
- Dumping everything into `llms.txt` instead of curating - the index should *select*, not mirror.
- Letting either file drift out of sync with the live docs.

### Edge cases
- `llms.txt` (curated map) vs `llms-full.txt` (full dump) are complementary, not alternatives - ship the map always, the full file when ingestion is the goal.
- `llms-full.txt` can blow past a model's context window; some sites paginate or offer per-section full files.
- Both live at the **site root**, discoverable by convention (`/llms.txt`).
