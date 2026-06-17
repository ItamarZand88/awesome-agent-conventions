### Composition
- The canonical opener is literal: *"# CLAUDE.md - This file provides guidance to Claude Code when working with code in this repository"* (modelcontextprotocol/servers), followed by **Project Overview → repo map → exact build/test commands**.
- Topic-led variants work too: the playwright-mcp file leads with its **Commit Convention**.
- Keep it short. CLAUDE.md is injected into *every* session, so its length is a recurring context tax.

### Anti-patterns
- **The bloated CLAUDE.md** - pages of prose that re-explain the codebase burn tokens on every turn.
- **Stale commands** - an agent will trust and run them; wrong commands are worse than none.

### Edge cases
- **`@path` imports:** the Cline example is essentially just `@.clinerules/general.md @.clinerules/network.md` - CLAUDE.md as an include manifest rather than content.
- **Layering:** `~/.claude/CLAUDE.md` (user-global) + repo `CLAUDE.md` + subdir files merge down the tree; `CLAUDE.local.md` is the untracked personal overlay.
- **The pointer pattern:** some repos (Airflow, Vercel AI) ship a one-line CLAUDE.md that just says `AGENTS.md` - a deliberate redirect to the cross-tool file.
