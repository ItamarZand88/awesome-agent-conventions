# CLAUDE.md 🟢 Adopted

> Anthropic's memory file for Claude Code - loaded automatically at session start to carry project commands, style rules, and standing instructions across turns.

- **Read by:** Claude Code, and tools that read the Claude memory convention
- **Location:** Repo root or .claude/CLAUDE.md, subdirectories, ~/.claude/ (user-global), enterprise-managed policy paths, and CLAUDE.local.md (untracked, personal)
- **Spec:** [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- **Files:** `CLAUDE.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `CLAUDE.md`

| Source | File | Provenance |
| --- | --- | --- |
| `anthropic-sdk-ts` | [`anthropic-sdk-ts.CLAUDE.md`](examples/anthropic-sdk-ts.CLAUDE.md) | [source](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/CLAUDE.md) |
| `mcp-servers` | [`mcp-servers.CLAUDE.md`](examples/mcp-servers.CLAUDE.md) | [source](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/CLAUDE.md) |
| `playwright-mcp` | [`playwright-mcp.CLAUDE.md`](examples/playwright-mcp.CLAUDE.md) | [source](https://raw.githubusercontent.com/microsoft/playwright-mcp/main/CLAUDE.md) |

## Field notes

### Load order & features
Free-form Markdown (no schema). All discovered files are **concatenated root -> cwd** (closer read last), loaded broad -> specific:

1. **Managed policy** - macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`, Linux `/etc/claude-code/CLAUDE.md`, Windows `C:\Program Files\ClaudeCode\CLAUDE.md` (can't be excluded; also inlinable via the `claudeMd` key in managed settings).
2. **User** - `~/.claude/CLAUDE.md`.
3. **Project** - `./CLAUDE.md` or `./.claude/CLAUDE.md`.
4. **Local** - `./CLAUDE.local.md` (gitignored).

- **`@path` imports** - relative (to the importing file) or absolute, expanded at launch; **recursive up to 4 hops**; first external import prompts for approval.
- **`.claude/rules/`** - modular `.md` files; those without `paths:` frontmatter load at launch (same priority as `.claude/CLAUDE.md`), path-scoped ones (`paths:` glob list) load only when Claude touches a matching file; `~/.claude/rules/` is the user-level form.
- **`/memory`** lists everything loaded and toggles auto-memory; **`claudeMdExcludes`** skips files in monorepos; **`--add-dir`** + `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` loads CLAUDE.md from extra dirs. Subdir CLAUDE.md files load **on demand**, not at launch.

### Composition
- The canonical opener is literal: *"# CLAUDE.md - This file provides guidance to Claude Code..."* (modelcontextprotocol/servers), then **Project Overview -> repo map -> exact build/test commands**. Topic-led variants work too (playwright-mcp leads with its Commit Convention).
- Keep it short - **under ~200 lines** is Anthropic's target; it loads **in full regardless of length** (unlike MEMORY.md), so length is a recurring context tax. Block-level HTML comments are stripped before injection (free maintainer notes) - except inside code blocks, where they're preserved.

### Anti-patterns
- **The bloated CLAUDE.md** - pages of prose that re-explain the codebase burn tokens every turn. (Splitting into `@imports` aids organization but doesn't reduce context - imports load at launch.)
- **Stale commands** - an agent will trust and run them; wrong commands are worse than none.

### Edge cases
- **Layering:** `CLAUDE.local.md` still loads (treated like CLAUDE.md) but is no longer the recommended personal overlay - it doesn't span git worktrees, so Anthropic now points to importing `@~/.claude/...` instead.
- **The pointer pattern:** some repos (Airflow, Vercel AI) ship a one-line CLAUDE.md that just `@AGENTS.md`-imports or symlinks the cross-tool file. `/init` seeds CLAUDE.md from an existing AGENTS.md / `.cursorrules` / `.windsurfrules`.
