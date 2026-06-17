### Composition
Three always-on files, each a tight single concern:
- **`product.md`** - what the product is and who it's for.
- **`structure.md`** - file organization and architectural conventions.
- **`tech.md`** - the stack plus common commands, and often a standing guardrail (e.g. "use the admin client that bypasses row-level security *only* in server code") - exactly the kind of always-true rule steering exists to carry.

### Anti-patterns
- Collapsing all three into one file, which loses the always-on/per-topic clarity.
- Duplicating per-feature spec content into steering (steering is for what's true *across* features).
- A `tech.md` that lists versions and then rots - an agent will trust "Next.js 15 / React 19" literally.

### Edge cases
- Steering supports four **inclusion modes** via front-matter - `always`, `fileMatch` (with a `fileMatchPattern`), `manual` (pulled in by a `#name` reference), and `auto` (matched against the file's `description`) - use them to keep large or niche guidance out of every prompt.
- Steering is project-scoped (`.kiro/steering/`) or global (`~/.kiro/steering/`), project winning on conflict; neither is limited to the three default files - teams add custom steering docs.
