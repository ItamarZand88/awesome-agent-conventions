# Kiro steering files 🟢 Adopted

> Kiro's always-on steering docs - product, structure, and tech files that give the agent persistent project context outside of any single spec.

- **Read by:** AWS Kiro, and Kiro-compatible agents
- **Location:** .kiro/steering/*.md (or ~/.kiro/steering/ for global)
- **Spec:** [https://kiro.dev/docs/steering](https://kiro.dev/docs/steering)
- **Files:** `product.md`, `structure.md`, `tech.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `product.md`

What the product is and who it's for.

| Source | File | Provenance |
| --- | --- | --- |
| `fame2` | [`fame2.product.md`](examples/fame2.product.md) | [source](https://raw.githubusercontent.com/HimangshuPronoy/fame2/main/.kiro/steering/product.md) |

### `structure.md`

File organization and architectural conventions.

| Source | File | Provenance |
| --- | --- | --- |
| `fame2` | [`fame2.structure.md`](examples/fame2.structure.md) | [source](https://raw.githubusercontent.com/HimangshuPronoy/fame2/main/.kiro/steering/structure.md) |

### `tech.md`

Allowed frameworks, libraries, and technical constraints.

| Source | File | Provenance |
| --- | --- | --- |
| `fame2` | [`fame2.tech.md`](examples/fame2.tech.md) | [source](https://raw.githubusercontent.com/HimangshuPronoy/fame2/main/.kiro/steering/tech.md) |

## Field notes

### Composition
Three always-on files, each a tight single concern:
- **`product.md`** - what the product is and who it's for.
- **`structure.md`** - file organization and architectural conventions.
- **`tech.md`** - the stack plus **Common Commands**. The fame2 example goes further and encodes a real guardrail: *"`supabaseAdmin` (bypasses RLS) - ONLY use in Server Actions/API routes"* - exactly the kind of standing rule steering exists to carry.

### Anti-patterns
- Collapsing all three into one file, which loses the always-on/per-topic clarity.
- Duplicating per-feature spec content into steering (steering is for what's true *across* features).
- A `tech.md` that lists versions and then rots - an agent will trust "Next.js 15 / React 19" literally.

### Edge cases
- Steering supports four **inclusion modes** via front-matter - `always`, `fileMatch` (with a `fileMatchPattern`), `manual` (pulled in by a `#name` reference), and `auto` (matched against the file's `description`) - use them to keep large or niche guidance out of every prompt.
- Steering is project-scoped (`.kiro/steering/`) or global (`~/.kiro/steering/`), project winning on conflict; neither is limited to the three default files - teams add custom steering docs.
