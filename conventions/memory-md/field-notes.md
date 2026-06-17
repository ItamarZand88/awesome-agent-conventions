### Composition
- **An index, not a store.** The Harzva/learn-likecc file is a `# Memory Index` of one-line links grouped by type (User / Project / Feedback / Reference) into `.claude/memory/*.md` - the facts live in the linked files, not here.
- **Or an append log.** The soul.md file is a `# Memory` with an HTML-comment header that instructs the agent: *"The agent appends to this file during sessions… continuity across sessions."*

### Anti-patterns
- Inlining the actual facts instead of linking out - that re-bloats the context the index was meant to keep small.
- Unbounded growth with no curation/compaction pass.
- Recording what the repo or git already says (structure, past fixes) instead of the non-obvious.

### Edge cases
- This file is both **read and written** by the agent - the format has to be one the model can reliably append to.
- Two live shapes coexist: a **curated index** (re-read, hand-tended) vs an **append-only log** (chronological). Pick one and be consistent.
- Links are relative into a memory directory; a moved file breaks recall silently.
