# MEMORY.md 🟢 Adopted

> A persistent, agent-maintained index of durable facts - written and re-read across sessions so an agent accumulates project memory instead of relearning each time.

- **Read by:** Claude Code's auto-memory, and agent frameworks that persist a memory index
- **Location:** Claude Code: ~/.claude/projects/<project>/memory/MEMORY.md (the index), with detail offloaded to topic files beside it
- **Spec:** [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- **Files:** `MEMORY.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `MEMORY.md`

| Source | File | Provenance |
| --- | --- | --- |
| `learn-likecc` | [`learn-likecc.MEMORY.md`](examples/learn-likecc.MEMORY.md) | [source](https://raw.githubusercontent.com/Harzva/learn-likecc/main/MEMORY.md) |
| `soul.md` | [`soul.md.MEMORY.md`](examples/soul.md.MEMORY.md) | [source](https://raw.githubusercontent.com/aaronjmars/soul.md/main/MEMORY.md) |

## Field notes

### Composition
- **An index, not a store.** The Harzva/learn-likecc file is a `# Memory Index` of one-line links grouped by type (User / Project / Feedback / Reference) into `.claude/memory/*.md` - the facts live in the linked files, not here.
- **Or an append log.** The soul.md file is a `# Memory` with an HTML-comment header that instructs the agent: *"The agent appends to this file during sessions… continuity across sessions."*

### Anti-patterns
- Inlining the actual facts instead of linking out - that re-bloats the context the index was meant to keep small.
- Unbounded growth with no curation/compaction pass.
- Recording what the repo or git already says (structure, past fixes) instead of the non-obvious.

### Edge cases
- This file is both **read and written** by the agent - the format has to be one the model can reliably append to. In Claude Code it lives at `~/.claude/projects/<project>/memory/MEMORY.md`, only the first ~200 lines / 25 KB load per session, and it's treated as an index with topic files read on demand - which is exactly why it must stay an index, not a store. (Built-in auto-memory, on by default since Claude Code v2.1.59.)
- Two live shapes coexist: a **curated index** (re-read, hand-tended) vs an **append-only log** (chronological). Pick one and be consistent.
- Links are relative into a memory directory; a moved file breaks recall silently.
