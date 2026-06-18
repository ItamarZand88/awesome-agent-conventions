# MEMORY.md 🟢 Adopted

> A persistent, agent-maintained index of durable facts - written and re-read across sessions so an agent accumulates project memory instead of relearning each time.

- **Read by:** Claude Code's auto-memory, and agent frameworks that persist a memory index
- **Location:** Claude Code: ~/.claude/projects/<project>/memory/MEMORY.md (the index), with detail offloaded to topic files beside it
- **Spec:** [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- **Evidence:** Claude Code auto-memory docs describe MEMORY.md as the per-project memory index loaded every session, with public examples of the pattern.
- **Last verified:** 2026-06-18
- **Files:** `MEMORY.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `MEMORY.md`

| Source | File | Provenance |
| --- | --- | --- |
| `learn-likecc` | [`examples/learn-likecc/MEMORY.md`](examples/learn-likecc/MEMORY.md) | [source](https://raw.githubusercontent.com/Harzva/learn-likecc/main/MEMORY.md) |
| `soul.md` | [`examples/soul/MEMORY.md`](examples/soul/MEMORY.md) | [source](https://raw.githubusercontent.com/aaronjmars/soul.md/main/MEMORY.md) |

## Field notes

### How Claude Code auto-memory works
- **Path:** `~/.claude/projects/<project>/memory/MEMORY.md`. `<project>` is keyed to the **git repo**, so all worktrees/subdirs of one repo **share** the memory dir; outside git it's the project root. **Machine-local** (not synced). Relocatable via `autoMemoryDirectory`.
- **Structure:** `MEMORY.md` is a concise **index**; detail lives in topic files beside it (`debugging.md`, ...) that are **read on demand**, not at launch.
- **Load cap:** only the **first 200 lines or 25 KB** of `MEMORY.md` (whichever comes first) loads each session. This cap applies **only to MEMORY.md** (CLAUDE.md loads in full).
- **Enable/disable:** on by default since **v2.1.59**; toggle via `/memory`, `autoMemoryEnabled: false`, or env `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`. "Remember X" routes here; "add this to CLAUDE.md" routes to CLAUDE.md. Subagents can keep their own auto-memory.

### Composition
- **An index, not a store.** The Harzva/learn-likecc file is a `# Memory Index` of one-line links grouped by type (User / Project / Feedback / Reference) - the facts live in the linked files. Claude Code's own auto-memory uses this index-plus-topic-files shape.
- **Or an append log.** The soul.md file is a `# Memory` whose HTML-comment header tells the agent to append across sessions.

### Anti-patterns
- Inlining the actual facts instead of linking out - that re-bloats the context the index was meant to keep small (and past the 200-line cap, content simply isn't loaded).
- Unbounded growth with no curation/compaction pass.
- Recording what the repo or git already says (structure, past fixes) instead of the non-obvious.

### Edge cases
- This file is both **read and written** by the agent - the format must be one the model can reliably append to.
- Two live shapes coexist: a **curated index** (re-read, hand-tended) vs an **append-only log** (chronological). Claude Code's built-in form is the curated index. Pick one and be consistent.
- Links are relative into the memory directory; a moved file breaks recall silently.

### Adoption / maturity
- Claude Code documents auto-memory as a first-class mechanism distinct from CLAUDE.md: it is written by Claude, scoped per repository, shared across worktrees, and capped when loaded into a fresh session.
- Public `MEMORY.md` examples are less uniform than `CLAUDE.md`; some are hand-maintained indexes and some are append logs. The maturity rating reflects the mechanism, not a single strict schema.

### Related conventions
- Use `CLAUDE.md` for project facts that every Claude Code session should read in full.
- Use Memory Bank when a team wants a version-controlled, multi-file memory system that is deliberately reviewed and updated in the repo.

### Sources checked
- [Claude Code memory docs](https://code.claude.com/docs/en/memory)
- [learn-likecc MEMORY.md example](https://raw.githubusercontent.com/Harzva/learn-likecc/main/MEMORY.md)
- [soul.md MEMORY.md example](https://raw.githubusercontent.com/aaronjmars/soul.md/main/MEMORY.md)
