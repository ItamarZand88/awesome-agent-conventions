# Tool-specific instruction files 🟢 Adopted

> Per-tool instruction files that predate or coexist with AGENTS.md. Many tools now fall back to or symlink AGENTS.md, but these named variants are still read in the wild.

- **Read by:** Each file is read by its namesake tool - Gemini CLI, Amp, Qwen Code, Warp, Aider, GitHub Copilot
- **Location:** Repository root (or .github/ for copilot-instructions.md)
- **Spec:** [https://agents.md](https://agents.md)
- **Files:** `GEMINI.md`, `AGENT.md`, `QWEN.md`, `WARP.md`, `CONVENTIONS.md`, `copilot-instructions.md`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `GEMINI.md`

Google Gemini CLI.

| Source | File | Provenance |
| --- | --- | --- |
| `gemini-cli` | [`gemini-cli.GEMINI.md`](examples/gemini-cli.GEMINI.md) | [source](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/GEMINI.md) |

### `AGENT.md`

Amp (Sourcegraph) - legacy singular form; Amp now reads AGENTS.md (plural).

| Source | File | Provenance |
| --- | --- | --- |
| `dagger` | [`dagger.AGENT.md`](examples/dagger.AGENT.md) | [source](https://raw.githubusercontent.com/dagger/container-use/main/AGENT.md) |

### `QWEN.md`

Qwen Code.

| Source | File | Provenance |
| --- | --- | --- |
| `qwen-code` | [`qwen-code.QWEN.md`](examples/qwen-code.QWEN.md) | [source](https://raw.githubusercontent.com/QwenLM/qwen-code/main/packages/cli/src/commands/extensions/examples/context/QWEN.md) |

### `WARP.md`

Warp terminal - backwards-compat; Warp now defaults to AGENTS.md.

| Source | File | Provenance |
| --- | --- | --- |
| `warp` | [`warp.WARP.md`](examples/warp.WARP.md) | [source](https://raw.githubusercontent.com/warpdotdev/warp/master/WARP.md) |

### `CONVENTIONS.md`

Aider.

| Source | File | Provenance |
| --- | --- | --- |
| `aider` | [`aider.CONVENTIONS.md`](examples/aider.CONVENTIONS.md) | [source](https://raw.githubusercontent.com/Aider-AI/conventions/main/golang/CONVENTIONS.md) |

### `copilot-instructions.md`

GitHub Copilot (lives under .github/).

| Source | File | Provenance |
| --- | --- | --- |
| `vscode` | [`vscode.copilot-instructions.md`](examples/vscode.copilot-instructions.md) | [source](https://raw.githubusercontent.com/microsoft/vscode/main/.github/copilot-instructions.md) |

## Field notes

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
