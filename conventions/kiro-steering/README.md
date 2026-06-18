# Kiro steering files 🟢 Adopted

> Kiro's always-on steering docs - product, structure, and tech files that give the agent persistent project context outside of any single spec.

- **Read by:** AWS Kiro, and Kiro-compatible agents
- **Location:** .kiro/steering/*.md (or ~/.kiro/steering/ for global)
- **Spec:** [https://kiro.dev/docs/steering](https://kiro.dev/docs/steering)
- **Evidence:** Kiro docs define .kiro/steering files and public Kiro projects commit the standard product, structure, and tech files.
- **Last verified:** 2026-06-18
- **Files:** `product.md`, `structure.md`, `tech.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `product.md`

What the product is and who it's for.

| Source | File | Provenance |
| --- | --- | --- |
| `spirit-of-kiro` | [`examples/spirit-of-kiro/product.md`](examples/spirit-of-kiro/product.md) | [source](https://raw.githubusercontent.com/kirodotdev/spirit-of-kiro/main/.kiro/steering/product.md) |

### `structure.md`

File organization and architectural conventions.

| Source | File | Provenance |
| --- | --- | --- |
| `spirit-of-kiro` | [`examples/spirit-of-kiro/structure.md`](examples/spirit-of-kiro/structure.md) | [source](https://raw.githubusercontent.com/kirodotdev/spirit-of-kiro/main/.kiro/steering/structure.md) |

### `tech.md`

Allowed frameworks, libraries, and technical constraints.

| Source | File | Provenance |
| --- | --- | --- |
| `spirit-of-kiro` | [`examples/spirit-of-kiro/tech.md`](examples/spirit-of-kiro/tech.md) | [source](https://raw.githubusercontent.com/kirodotdev/spirit-of-kiro/main/.kiro/steering/tech.md) |

## Field notes

### Fields (frontmatter)
| Field | Notes |
| --- | --- |
| `inclusion` | `always` (default) / `fileMatch` / `manual` / `auto` |
| `fileMatchPattern` | required for `fileMatch`; a glob string or an array of globs |
| `description` | required for `auto` (Kiro semantically matches it against the request) |
| `name` | required for `auto`; also the handle for `manual` |

**File reference:** `#[[file:<relative_path>]]` inlines a live workspace file (e.g. `#[[file:api/openapi.yaml]]`) so steering stays in sync with source. **Default files:** `product.md`, `tech.md`, `structure.md` - but custom files (`api-standards.md`, `testing-standards.md`...) are fully supported. **Scope:** workspace `.kiro/steering/`, global `~/.kiro/steering/`, and a team scope (MDM/central-repo distribution); workspace wins on conflict.

### Composition
- Three default always-on files, each a tight single concern:
  - **`product.md`** - what the product is and who it's for.
  - **`structure.md`** - file organization and architectural conventions.
  - **`tech.md`** - the stack plus common commands, and often a standing guardrail (e.g. "use the admin client that bypasses row-level security *only* in server code") - exactly the kind of always-true rule steering exists to carry.

### Anti-patterns
- Collapsing all three into one file, which loses the always-on/per-topic clarity.
- Duplicating per-feature spec content into steering (steering is for what's true *across* features).
- A `tech.md` that lists versions and then rots - an agent will trust "Next.js 15 / React 19" literally.

### Edge cases
- `auto` mode needs **both** `name` and `description`; `manual` is pulled in via a `#steering-file-name` reference (also works as a slash command).
- Kiro also reads the **`AGENTS.md`** standard in steering, but AGENTS.md files don't support inclusion modes - they're always included when at the workspace root or in `~/.kiro/steering/`.
- Steering is project-scoped (`.kiro/steering/`) or global (`~/.kiro/steering/`); neither is limited to the three default files.

### Adoption / maturity
- Kiro steering is an official AWS Kiro feature with documented workspace, global, and team deployment scopes. The three foundation files are the default starting point, but custom steering files are first-class.
- The inclusion mode is the key differentiator from AGENTS.md: `always`, `fileMatch`, `manual`, and `auto` let teams keep context narrow instead of putting everything into one always-on file.

### Related conventions
- AGENTS.md is supported by Kiro, but it does not support Kiro's inclusion modes.
- Spec Kit files are per-feature execution artifacts; steering files are the persistent baseline that every feature should respect.

### Sources checked
- [Kiro steering docs](https://kiro.dev/docs/steering/)
- [Spirit of Kiro steering examples](https://github.com/kirodotdev/spirit-of-kiro/tree/main/.kiro/steering)
