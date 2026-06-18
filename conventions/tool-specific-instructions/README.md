# Tool-specific instruction files 🟢 Adopted

> Per-tool instruction files that predate or coexist with AGENTS.md. Some tools now default to AGENTS.md while keeping legacy filenames alive, so these variants still matter when auditing real repositories.

- **Read by:** Each file is read by its namesake tool - Gemini CLI, Amp, Qwen Code, Warp, Aider, GitHub Copilot - often alongside or as a bridge to AGENTS.md
- **Location:** Repository root (or .github/ for copilot-instructions.md)
- **Spec:** [https://agents.md](https://agents.md)
- **Evidence:** Gemini, Qwen, Warp, Amp, Aider, and Copilot each document or ship named instruction files, while several now bridge to AGENTS.md.
- **Last verified:** 2026-06-18
- **Files:** `GEMINI.md`, `AGENT.md`, `QWEN.md`, `WARP.md`, `CONVENTIONS.md`, `copilot-instructions.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `GEMINI.md`

Google Gemini CLI.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `gemini-cli` | [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli) | [`examples/gemini-cli/GEMINI.md`](examples/gemini-cli/GEMINI.md) | [source](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/GEMINI.md) |

### `AGENT.md`

Amp (Sourcegraph) - legacy singular form; Amp now reads AGENTS.md (plural).

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `dagger` | [`dagger/container-use`](https://github.com/dagger/container-use) | [`examples/dagger/AGENT.md`](examples/dagger/AGENT.md) | [source](https://raw.githubusercontent.com/dagger/container-use/main/AGENT.md) |

### `QWEN.md`

Qwen Code.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `qwen-code` | [`QwenLM/qwen-code`](https://github.com/QwenLM/qwen-code) | [`examples/qwen-code/QWEN.md`](examples/qwen-code/QWEN.md) | [source](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/cli/src/commands/extensions/examples/context/QWEN.md) |

### `WARP.md`

Warp terminal - backwards-compatible with project rules; Warp now defaults new projects to AGENTS.md, but WARP.md still takes same-directory priority.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `warp` | [`warpdotdev/warp`](https://github.com/warpdotdev/warp) | [`examples/warp/WARP.md`](examples/warp/WARP.md) | [source](https://raw.githubusercontent.com/warpdotdev/warp/master/WARP.md) |

### `CONVENTIONS.md`

Aider.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `aider` | [`Aider-AI/conventions`](https://github.com/Aider-AI/conventions) | [`examples/aider/CONVENTIONS.md`](examples/aider/CONVENTIONS.md) | [source](https://raw.githubusercontent.com/Aider-AI/conventions/main/golang/CONVENTIONS.md) |

### `copilot-instructions.md`

GitHub Copilot (lives under .github/).

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `vscode` | [`microsoft/vscode`](https://github.com/microsoft/vscode) | [`examples/vscode/copilot-instructions.md`](examples/vscode/copilot-instructions.md) | [source](https://raw.githubusercontent.com/microsoft/vscode/main/.github/copilot-instructions.md) |

## Field notes

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
