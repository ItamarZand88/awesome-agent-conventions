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
| `vibetunnel` | [`vibetunnel.AGENT.md`](examples/vibetunnel.AGENT.md) | [source](https://raw.githubusercontent.com/amantus-ai/vibetunnel/main/AGENT.md) |

### `QWEN.md`

Qwen Code.

| Source | File | Provenance |
| --- | --- | --- |
| `MapDownload` | [`MapDownload.QWEN.md`](examples/MapDownload.QWEN.md) | [source](https://raw.githubusercontent.com/Hxy1992/MapDownload/main/QWEN.md) |

### `WARP.md`

Warp terminal - backwards-compat; Warp now defaults to AGENTS.md.

| Source | File | Provenance |
| --- | --- | --- |
| `Zafiro.Avalonia` | [`Zafiro.Avalonia.WARP.md`](examples/Zafiro.Avalonia.WARP.md) | [source](https://raw.githubusercontent.com/SuperJMN/Zafiro.Avalonia/master/WARP.md) |

### `CONVENTIONS.md`

Aider.

| Source | File | Provenance |
| --- | --- | --- |
| `phel-lang` | [`phel-lang.CONVENTIONS.md`](examples/phel-lang.CONVENTIONS.md) | [source](https://raw.githubusercontent.com/phel-lang/phel-lang/master/resources/agents/skills/aider/CONVENTIONS.md) |

### `copilot-instructions.md`

GitHub Copilot (lives under .github/).

| Source | File | Provenance |
| --- | --- | --- |
| `vscode` | [`vscode.copilot-instructions.md`](examples/vscode.copilot-instructions.md) | [source](https://raw.githubusercontent.com/microsoft/vscode/main/.github/copilot-instructions.md) |

## Field notes

### Composition
All of these share the AGENTS.md shape - title, tech stack, build/test commands, conventions - and several announce their reader explicitly:
- **WARP.md** opens *"This file provides guidance to WARP (warp.dev) when working with code in this repository."*
- **AGENT.md** (Amp) leads with **Build/Test Commands** and a single-test recipe.
- **CONVENTIONS.md** (Aider) is loaded *explicitly* - *"Pass to Aider via `--read CONVENTIONS.md`"* - and itself documents a load order of further `.agents/*.md` files.
- **QWEN.md** / **GEMINI.md** mirror CLAUDE.md, including `@`-imports.

### Anti-patterns
- Hand-maintaining six near-identical files until they drift. The common fix is to keep one source (usually AGENTS.md) and symlink the rest.
- Putting tool-specific paths in the wrong place - `copilot-instructions.md` lives under `.github/`, not the repo root.

### Edge cases
- **Discovery differs:** most are auto-loaded by their tool, but Aider's `CONVENTIONS.md` is opt-in via `--read` / `.aider.conf.yml`.
- **Convergence on `AGENTS.md` (plural):** Amp now reads `AGENTS.md`, and Warp defaults to `AGENTS.md` with `WARP.md` kept only for backwards-compatibility. The singular `AGENT.md` and the standalone `WARP.md` are now legacy - the ecosystem moved toward the shared file, not away from it.
