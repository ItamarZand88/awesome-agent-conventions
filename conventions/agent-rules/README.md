# Rules files 🟢 Adopted

> Per-tool rule files that scope agent behavior - older single-file forms (.cursorrules, .clinerules, .windsurfrules) and newer directory-based, glob-scoped forms (.cursor/rules/*.mdc, .clinerules/, .windsurf/rules/*.md).

- **Read by:** Cursor (.cursorrules / .mdc), Cline (.clinerules/ and legacy .clinerules), Windsurf (.windsurfrules)
- **Location:** Repo root, or a rules directory (.cursor/rules/*.mdc, .clinerules/, .windsurf/rules/*.md)
- **Spec:** [https://docs.cline.bot/customization/cline-rules](https://docs.cline.bot/customization/cline-rules)
- **Evidence:** Cursor, Cline, and Windsurf document and/or detect project rule files, including both legacy single files and directory-based rules.
- **Last verified:** 2026-06-18
- **Files:** `.cursorrules`, `.mdc`, `.clinerules`, `.clinerules/`, `.windsurfrules`

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

Cline - legacy single-file form, still detected.

| Source | File | Provenance |
| --- | --- | --- |
| `raycast` | [`raycast.clinerules`](examples/raycast.clinerules) | [source](https://raw.githubusercontent.com/raycast/extensions/main/extensions/1bookmark/.clinerules) |

### `.clinerules/`

Cline - primary workspace rules directory; Markdown/text files are combined and can be toggled.

**Pattern - not an extracted file.**

A project-root directory containing focused Markdown or text rule files such as `coding.md`, `testing.md`, and `architecture.md`. Cline combines the files into one workspace rule set, while the UI can toggle individual rules.

Live instances (fetch directly - too large or instance-specific to vendor):

- [Cline docs example](https://docs.cline.bot/customization/cline-rules)
- [wjmuse/mcp_daily_life .clinerules directory](https://github.com/wjmuse/mcp_daily_life/tree/main/.clinerules)

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

**Cline `.clinerules/`**: primary workspace rules directory at the project root. Cline processes all `.md` and `.txt` files inside it, combines workspace and global rules, and gives workspace rules precedence when they conflict. Legacy `.clinerules` single-file rules are still detected.

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
- `.cursorrules` is superseded by `.cursor/rules/*.mdc`, `.clinerules` by `.clinerules/`, and `.windsurfrules` by `.windsurf/rules/`; these tools increasingly also accept a plain `AGENTS.md`. `.cursor/rules/` can be **nested** per subdirectory, and rules reference files with `@filename`.
