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
- Steering supports **inclusion modes** (always-on vs file-match vs manual) via front-matter - use them to keep large or niche guidance out of every prompt.
- `.kiro/steering/` isn't limited to the three default files; teams add custom steering docs there.
