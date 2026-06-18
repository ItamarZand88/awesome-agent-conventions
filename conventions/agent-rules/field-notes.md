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
