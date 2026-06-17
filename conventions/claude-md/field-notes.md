### Composition
- The canonical opener is literal: *"# CLAUDE.md - This file provides guidance to Claude Code when working with code in this repository"* (modelcontextprotocol/servers), followed by **Project Overview → repo map → exact build/test commands**.
- Topic-led variants work too: the playwright-mcp file leads with its **Commit Convention**.
- Keep it short. CLAUDE.md is injected into *every* session, so its length is a recurring context tax - Anthropic targets **under ~200 lines**, with longer or path-specific guidance pushed into `.claude/rules/` files. Block-level HTML comments are stripped before injection, so they make free maintainer notes.

### Anti-patterns
- **The bloated CLAUDE.md** - pages of prose that re-explain the codebase burn tokens on every turn.
- **Stale commands** - an agent will trust and run them; wrong commands are worse than none.

### Edge cases
- **`@path` imports:** the Cline example is essentially just `@.clinerules/general.md @.clinerules/network.md` - CLAUDE.md as an include manifest rather than content.
- **Layering:** `~/.claude/CLAUDE.md` (user-global), the repo file (root `CLAUDE.md` or `.claude/CLAUDE.md`), subdir files, and enterprise-managed policy files merge down the tree. `CLAUDE.local.md` still loads but is no longer the recommended personal overlay - it doesn't span git worktrees, so Anthropic now points to importing `@~/.claude/...` instead.
- **The pointer pattern:** some repos (Airflow, Vercel AI) ship a one-line CLAUDE.md that just says `AGENTS.md` - a deliberate redirect to the cross-tool file.
