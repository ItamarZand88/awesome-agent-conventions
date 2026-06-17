### Composition
- Mirrors `robots.txt`: `User-Agent` lines plus per-media-type allow/disallow directives (Text / Images / Audio / Video) declaring training and data-mining consent. Spawning ships a generator that emits the canonical form.

### Anti-patterns
- Treating it as enforcement. It's a *declaration* of consent, not a technical block - crawlers can ignore it, and most do.
- Hand-rolling a schema that diverges from Spawning's. Live files vary widely: adopters that get it right (WordPress's Openverse uses the canonical Spawning shape) sit beside ad-hoc variants elsewhere.

### Edge cases
- **🔵 Proposed, labelled down on purpose.** There's a real org (Spawning) and a real spec tied to the EU TDM opt-out, but adoption is thin: Spawning's own docs concede most bots don't honor it, and live files disagree on format. Until consumption is demonstrable, it sits below 🟠.
- Orthogonal to the files it gets confused with: `robots.txt` AI user-agents (`GPTBot`, etc.) restrict *crawling*; `llms.txt` *exposes* docs to agents; `ai.txt` restricts *training* use. Placement is still unsettled - site root vs `/.well-known/ai.txt`.
