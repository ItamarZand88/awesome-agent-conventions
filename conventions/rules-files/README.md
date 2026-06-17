# Rules files 🟢 Adopted

> Per-tool rule files that scope agent behavior - older single-file forms (.cursorrules, .windsurfrules) and newer directory-based, glob-scoped forms (.cursor/rules/*.mdc).

- **Read by:** Cursor (.cursorrules / .mdc), Cline (.clinerules), Windsurf (.windsurfrules)
- **Location:** Repo root, or a rules directory (.cursor/rules/*.mdc, .clinerules/)
- **Spec:** [https://cursor.com/docs/rules](https://cursor.com/docs/rules)
- **Files:** `.cursorrules`, `.mdc`, `.clinerules`, `.windsurfrules`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.cursorrules`

Cursor - legacy single-file form (superseded by .cursor/rules/*.mdc).

| Source | File | Provenance |
| --- | --- | --- |
| `devin` | [`devin.cursorrules`](examples/devin.cursorrules) | [source](https://raw.githubusercontent.com/grapeot/devin.cursorrules/master/.cursorrules) |

### `.mdc`

Cursor - modern rule file with frontmatter and glob scoping, under .cursor/rules/.

| Source | File | Provenance |
| --- | --- | --- |
| `awesome-cursorrules` | [`awesome-cursorrules.angular-typescript-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules.angular-typescript-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/angular-typescript-cursorrules-prompt-file.mdc) |

### `.clinerules`

Cline - a rules file or a directory of rules.

| Source | File | Provenance |
| --- | --- | --- |
| `raycast` | [`raycast.clinerules`](examples/raycast.clinerules) | [source](https://raw.githubusercontent.com/raycast/extensions/main/extensions/1bookmark/.clinerules) |

### `.windsurfrules`

Windsurf - project rules.

| Source | File | Provenance |
| --- | --- | --- |
| `snyk` | [`snyk.windsurfrules`](examples/snyk.windsurfrules) | [source](https://raw.githubusercontent.com/snyk/vscode-extension/main/.windsurfrules) |

## Field notes

### Fields (frontmatter)
**Cursor `.mdc`** (in `.cursor/rules/`; a plain `.md` there is ignored): `description`, `globs` (**comma-separated string, not a YAML array**), `alwaysApply` (bool). The combination selects one of **four rule types**:

| Type | `alwaysApply` | `description` | `globs` |
| --- | --- | --- | --- |
| Always | `true` | - | - |
| Auto Attached | `false` | - | set |
| Agent Requested | `false` | **required** | - |
| Manual (`@rule`) | `false` | - | - |

**Windsurf `.windsurf/rules/*.md`**: `trigger` (`always_on` / `model_decision` / `glob` / `manual`), `description` (for `model_decision`), `globs` (for `glob`). Limits: **12,000 chars** per workspace rule file, **6,000** global.

**Cline `.clinerules`** (file or directory): optional frontmatter `paths` (glob[]), `alwaysApply` (bool), `description`; a file with no frontmatter is always active; toggleable in the UI.

**Legacy single-file forms** - `.cursorrules`, `.windsurfrules` - are plain prose, always injected, no frontmatter.

### Composition
- **Modern (`.mdc`)** carries frontmatter that *scopes* the rule by glob or description instead of being on for everything.
- **Legacy** is a flat prose file; the well-known devin.cursorrules is structured as *Instructions / Lessons / Scratchpad*.

### Anti-patterns
- Large `alwaysApply: true` / `always_on` rule files - prepended to every request, quietly inflating token cost.
- Affirmation prose that doesn't change behavior ("you are a genius... double-check your work") - concrete rules ("do not nest code more than 2 levels deep") earn their place.
- Keeping a flat `.cursorrules` when a glob-scoped `.cursor/rules/*.mdc` would target the rule precisely.

### Edge cases
- **Four activation modes**, not three: Always, Auto-Attached (glob), Agent-Requested (by description), and **Manual** (`@rule` mention) - pick the narrowest that works. Windsurf mirrors these via its `trigger` field.
- `.cursorrules` is superseded by `.cursor/rules/*.mdc` and `.windsurfrules` by `.windsurf/rules/`; both tools now also accept a plain `AGENTS.md`. `.cursor/rules/` can be **nested** per subdirectory, and rules reference files with `@filename`.
