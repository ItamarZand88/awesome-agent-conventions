### Per-tool reference
| File | Tool | Location & loading |
| --- | --- | --- |
| `GEMINI.md` | Gemini CLI | `~/.gemini/` global + project tree; `@`-imports; `contextFileName` accepts a string **or array**; `/memory show|refresh|add` |
| `QWEN.md` | Qwen Code | like Gemini; `@`-imports with a configurable **max depth (default 5)**; also reads `AGENTS.md` |
| `AGENT.md` | Amp | **legacy** - Amp now reads `AGENTS.md` (plural) and falls back to `CLAUDE.md`; nearest wins |
| `WARP.md` | Warp | repo root + cwd; filename **must be ALL-CAPS**; supports Global Rules |
| `CONVENTIONS.md` | Aider | **opt-in only**: `--read CONVENTIONS.md` or `read:` in `.aider.conf.yml` (single or list); marks the file read-only + cached; filename is arbitrary |
| `copilot-instructions.md` | GitHub Copilot | `.github/copilot-instructions.md`; path-scoped variants in `.github/instructions/*.instructions.md` (`applyTo` glob, optional `excludeAgent`) |

### Composition
All share the AGENTS.md shape - title, tech stack, build/test commands, conventions:
- **WARP.md** (Warp's backwards-compat file) follows the standard *"This file provides guidance to WARP..."* shape.
- **AGENT.md** (Amp's legacy singular form) leads with build/test commands.
- **CONVENTIONS.md** (Aider) is loaded *explicitly* - via `--read` or `.aider.conf.yml read:`, not auto-discovered.
- **QWEN.md** / **GEMINI.md** mirror CLAUDE.md, including `@`-imports.

### Anti-patterns
- Hand-maintaining six near-identical files until they drift. The common fix: keep one source (usually AGENTS.md) and symlink/import the rest.
- Putting tool-specific paths in the wrong place - `copilot-instructions.md` lives under `.github/`, not the repo root.

### Edge cases
- **WARP.md takes priority over AGENTS.md** when both exist in the same directory (Warp defaults new projects to AGENTS.md, but does not let it override an existing WARP.md). Amp is the opposite - it converged onto AGENTS.md and treats singular `AGENT.md` as legacy.
- **Copilot precedence** is combine-not-override: Personal > Repository > Organization instructions all apply together. Copilot also reads `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` as alternatives.
- Import-depth differs per tool: Claude = 4 hops, Qwen = 5 (configurable), Gemini undocumented - they are not identical despite sharing `@`-import syntax.
