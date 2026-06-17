### Composition
- **Modern (`.mdc`)** carries frontmatter that *scopes* the rule: the awesome-cursorrules Angular example uses `description`, `globs: **/*`, `alwaysApply: false` - so the rule attaches by file pattern instead of being on for everything.
- **Legacy (`.cursorrules`, `.windsurfrules`)** is a flat prose file. The well-known devin.cursorrules is structured as *Instructions / Lessons / Scratchpad*.

### Anti-patterns
- Large `alwaysApply: true` rule files - they're prepended to every request and quietly inflate token cost.
- Affirmation prose that doesn't change behavior - the Angular `.mdc` opens with *"you are a genius at reasoning… double check your work"*, which reads well but steers little. Concrete rules ("do not nest code more than 2 levels deep") earn their place.
- Keeping a flat `.cursorrules` when glob-scoped `.cursor/rules/*.mdc` would target the rule precisely.

### Edge cases
- Three activation modes coexist: **always**, **glob-scoped**, and **agent-requested** (by description) - pick the narrowest that works.
- `.cursorrules` is deprecated in favor of `.cursor/rules/*.mdc`, and `.windsurfrules` is the legacy single-file form (superseded by `.windsurf/rules/`); both Cursor and Windsurf now also accept a plain `AGENTS.md` as a simpler alternative. `.clinerules` can be a single file *or* a directory of rules.
