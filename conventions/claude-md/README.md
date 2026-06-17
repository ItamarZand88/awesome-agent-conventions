# CLAUDE.md 🟢 Adopted

> Anthropic's memory file for Claude Code — loaded automatically at session start to carry project commands, style rules, and standing instructions across turns.

- **Read by:** Claude Code, and tools that read the Claude memory convention
- **Location:** Repo root, subdirectories, ~/.claude/ (user-global), and CLAUDE.local.md (untracked, personal)
- **Spec:** [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- **Files:** `CLAUDE.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `CLAUDE.md`

| Source | File | Provenance |
| --- | --- | --- |
| `anthropic-sdk-ts` | [`anthropic-sdk-ts.CLAUDE.md`](examples/anthropic-sdk-ts.CLAUDE.md) | [source](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/CLAUDE.md) |
| `mcp-servers` | [`mcp-servers.CLAUDE.md`](examples/mcp-servers.CLAUDE.md) | [source](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/CLAUDE.md) |
| `playwright-mcp` | [`playwright-mcp.CLAUDE.md`](examples/playwright-mcp.CLAUDE.md) | [source](https://raw.githubusercontent.com/microsoft/playwright-mcp/main/CLAUDE.md) |

## Field notes

### Composition
- The canonical opener is literal: *"# CLAUDE.md — This file provides guidance to Claude Code when working with code in this repository"* (modelcontextprotocol/servers), followed by **Project Overview → repo map → exact build/test commands**.
- Topic-led variants work too: the playwright-mcp file leads with its **Commit Convention**.
- Keep it short. CLAUDE.md is injected into *every* session, so its length is a recurring context tax.

### Anti-patterns
- **The bloated CLAUDE.md** — pages of prose that re-explain the codebase burn tokens on every turn.
- **Stale commands** — an agent will trust and run them; wrong commands are worse than none.

### Edge cases
- **`@path` imports:** the Cline example is essentially just `@.clinerules/general.md @.clinerules/network.md` — CLAUDE.md as an include manifest rather than content.
- **Layering:** `~/.claude/CLAUDE.md` (user-global) + repo `CLAUDE.md` + subdir files merge down the tree; `CLAUDE.local.md` is the untracked personal overlay.
- **The pointer pattern:** some repos (Airflow, Vercel AI) ship a one-line CLAUDE.md that just says `AGENTS.md` — a deliberate redirect to the cross-tool file.
