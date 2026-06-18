### Fields (frontmatter)
**Cursor `.mdc`** (in `.cursor/rules/`; a plain `.md` there is ignored): `description`, `globs` (**comma-separated string, not a YAML array**), `alwaysApply` (bool). The combination selects one of **four rule types**:

| Type | `alwaysApply` | `description` | `globs` |
| --- | --- | --- | --- |
| Always | `true` | - | - |
| Auto Attached | `false` | - | set |
| Agent Requested | `false` | **required** | - |
| Manual (`@rule`) | `false` | - | - |

**Devin Desktop / legacy Windsurf rules**: preferred workspace path is now `.devin/rules/*.md`; `.windsurf/rules/*.md` remains a fallback. Frontmatter uses `trigger` (`always_on` / `model_decision` / `glob` / `manual`), `description` (for `model_decision`), and `globs` (for `glob`). Limits: **12,000 chars** per workspace rule file, **6,000** for the global rules file.

**Cline `.clinerules/`**: primary workspace rules directory at the project root. Cline processes all `.md` and `.txt` files inside it, combines workspace and global rules, and gives workspace rules precedence when they conflict. Legacy `.clinerules` single-file rules are still detected.

**Legacy single-file forms** - `.cursorrules`, `.clinerules`, `.windsurfrules` - are plain prose, always injected, no frontmatter.

### Composition
- **Modern (`.mdc`)** carries frontmatter that *scopes* the rule by glob or description instead of being on for everything.
- **Legacy** is a flat prose file; the well-known devin.cursorrules is structured as *Instructions / Lessons / Scratchpad*.

### Anti-patterns
- Large `alwaysApply: true` / `always_on` rule files - prepended to every request, quietly inflating token cost.
- Affirmation prose that doesn't change behavior ("you are a genius... double-check your work") - concrete rules ("do not nest code more than 2 levels deep") earn their place.
- Keeping a flat `.cursorrules` when a glob-scoped `.cursor/rules/*.mdc` would target the rule precisely.

### Edge cases
- **Four activation modes**, not three: Always, Auto-Attached (glob), Agent-Requested (by description), and **Manual** (`@rule` mention) - pick the narrowest that works. Windsurf mirrors these via its `trigger` field.
- `.cursorrules` is superseded by `.cursor/rules/*.mdc`, `.clinerules` by `.clinerules/`, and `.windsurfrules` by `.devin/rules/*.md` / `.windsurf/rules/*.md`; these tools increasingly also accept a plain `AGENTS.md`. `.cursor/rules/` can be **nested** per subdirectory, and rules reference files with `@filename`.
- Root-level AGENTS.md in Devin/Cascade is processed by the same rules engine as always-on context, while subdirectory AGENTS.md files act like location-scoped glob rules. Do not duplicate the same guidance in both a rule and AGENTS.md.

### Adoption / maturity
- Rules files are adopted, but fragmented. Cursor, Cline, Devin/Cascade/Windsurf, and legacy tools all have slightly different names and activation semantics.
- The safest repo policy is "narrow by default": keep global/always-on rules short, move language-specific or workflow-specific instructions into glob/model/manual rules, and keep one canonical source for cross-tool instructions.

### Sources checked
- [Cursor Rules docs](https://cursor.com/docs/rules)
- [Devin/Cascade Memories & Rules docs](https://docs.devin.ai/desktop/cascade/memories)
- [Cline Rules docs](https://docs.cline.bot/customization/cline-rules)
- [Warp rules docs](https://docs.warp.dev/agent-platform/capabilities/rules/)
