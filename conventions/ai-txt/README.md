# ai.txt 🔵 Proposed

> A text file declaring machine-readable consent for AI training and data-mining of a site's content - a robots.txt analogue for the training era. A real spec from a real org (Spawning, tied to the EU TDM opt-out), but adoption is thin and live files use divergent schemas - labelled down to 🔵 until consumption is demonstrable.

- **Read by:** AI training-data crawlers that honor Spawning's opt-out (early adopters)
- **Location:** Site root or /.well-known/ai.txt
- **Spec:** [https://site.spawning.ai/spawning-ai-txt](https://site.spawning.ai/spawning-ai-txt)
- **Files:** `ai.txt`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `ai.txt`

| Source | File | Provenance |
| --- | --- | --- |
| `zenonel` | [`zenonel.ai.txt`](examples/zenonel.ai.txt) | [source](https://raw.githubusercontent.com/ZenonEl/zenonel.github.io/main/.well-known/ai.txt) |

## Field notes

### Composition
- Mirrors `robots.txt`: `User-Agent` lines plus per-media-type allow/disallow directives (Text / Images / Audio / Video) declaring training and data-mining consent. Spawning ships a generator that emits the canonical form.

### Anti-patterns
- Treating it as enforcement. It's a *declaration* of consent, not a technical block - crawlers can ignore it, and most do.
- Hand-rolling a schema that diverges from Spawning's. The live example vendored here is itself a community variant - which is the cautionary tale.

### Edge cases
- **🔵 Proposed, labelled down on purpose.** There's a real org (Spawning) and a real spec tied to the EU TDM opt-out, but adoption is thin: Spawning's own docs concede most bots don't honor it, and live files disagree on format. Until consumption is demonstrable, it sits below 🟠.
- Orthogonal to the files it gets confused with: `robots.txt` AI user-agents (`GPTBot`, etc.) restrict *crawling*; `llms.txt` *exposes* docs to agents; `ai.txt` restricts *training* use. Placement is still unsettled - site root vs `/.well-known/ai.txt`.
