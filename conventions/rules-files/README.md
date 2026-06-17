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
| `devin` | [`devin..cursorrules`](examples/devin..cursorrules) | [source](https://raw.githubusercontent.com/grapeot/devin.cursorrules/master/.cursorrules) |

### `.mdc`

Cursor - modern rule file with frontmatter and glob scoping, under .cursor/rules/.

| Source | File | Provenance |
| --- | --- | --- |
| `awesome-cursorrules` | [`awesome-cursorrules.angular-typescript-cursorrules-prompt-file.mdc`](examples/awesome-cursorrules.angular-typescript-cursorrules-prompt-file.mdc) | [source](https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/angular-typescript-cursorrules-prompt-file.mdc) |

### `.clinerules`

Cline - a rules file or a directory of rules.

| Source | File | Provenance |
| --- | --- | --- |
| `raycast` | [`raycast..clinerules`](examples/raycast..clinerules) | [source](https://raw.githubusercontent.com/raycast/extensions/main/extensions/1bookmark/.clinerules) |

### `.windsurfrules`

Windsurf - project rules.

| Source | File | Provenance |
| --- | --- | --- |
| `Terminal.Gui` | [`Terminal.Gui..windsurfrules`](examples/Terminal.Gui..windsurfrules) | [source](https://raw.githubusercontent.com/gui-cs/Terminal.Gui/develop/.windsurfrules) |

## Field notes

### Composition
- **Modern (`.mdc`)** carries frontmatter that *scopes* the rule: the awesome-cursorrules Angular example uses `description`, `globs: **/*`, `alwaysApply: false` - so the rule attaches by file pattern instead of being on for everything.
- **Legacy (`.cursorrules`, `.windsurfrules`)** is a flat prose file. The well-known devin.cursorrules is structured as *Instructions / Lessons / Scratchpad*.

### Anti-patterns
- Large `alwaysApply: true` rule files - they're prepended to every request and quietly inflate token cost.
- Affirmation prose that doesn't change behavior - the Angular `.mdc` opens with *"you are a genius at reasoning… double check your work"*, which reads well but steers little. Concrete rules ("do not nest code more than 2 levels deep") earn their place.
- Keeping a flat `.cursorrules` when glob-scoped `.cursor/rules/*.mdc` would target the rule precisely.

### Edge cases
- Three activation modes coexist: **always**, **glob-scoped**, and **agent-requested** (by description) - pick the narrowest that works.
- `.cursorrules` is deprecated in favor of `.cursor/rules/*.mdc`; `.clinerules` can be a single file *or* a directory of rules.
