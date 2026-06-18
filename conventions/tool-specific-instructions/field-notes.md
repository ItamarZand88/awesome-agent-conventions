### Per-tool reference
| File | Tool | Location & loading |
| --- | --- | --- |
| `GEMINI.md` | Gemini CLI | Hierarchical context file; default filename is configurable via `context.fileName` as a string or array; supports `@` imports and `/memory show|reload` |
| `QWEN.md` | Qwen Code | Hierarchical context file; default filename is configurable via `context.fileName`; `includeDirectories` can add up to 5 extra roots; `/memory show|refresh` inspects/reloads context |
| `AGENT.md` | Amp | **legacy singular fallback** - Amp now reads `AGENTS.md` first and falls back to `AGENT.md` or `CLAUDE.md` when no AGENTS.md exists |
| `WARP.md` | Warp | Backwards-compatible project rules file; Warp also supports rules and AGENTS.md, with same-directory WARP.md still relevant for older projects |
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

### Adoption / maturity
- The direction of travel is convergence on AGENTS.md, but the old tool-specific names are still important in audits because many public repositories created guidance before AGENTS.md existed or before their tool added support.
- Treat these files as compatibility shims unless a tool still exposes unique behavior through the file name. One canonical source plus symlinks/imports is safer than six copies that drift.

### Sources checked
- [Gemini CLI project context docs](https://geminicli.com/docs/cli/gemini-md/)
- [Qwen Code configuration docs](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/)
- [Amp AGENTS.md manual section](https://ampcode.com/manual)
- [Warp rules docs](https://docs.warp.dev/agent-platform/capabilities/rules/)
- [Aider conventions docs](https://aider.chat/docs/usage/conventions.html)
- [GitHub Copilot repository instructions docs](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
