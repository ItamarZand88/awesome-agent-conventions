### Composition
All of these share the AGENTS.md shape - title, tech stack, build/test commands, conventions - and several announce their reader explicitly:
- **WARP.md** (now Warp's backwards-compat file) follows the standard *"This file provides guidance to WARP..."* shape.
- **AGENT.md** (Amp's legacy singular form) leads with build/test commands.
- **CONVENTIONS.md** (Aider) is loaded *explicitly* - via `--read CONVENTIONS.md` or a `read:` entry in `.aider.conf.yml`, not auto-discovered.
- **QWEN.md** / **GEMINI.md** mirror CLAUDE.md, including `@`-imports.

### Anti-patterns
- Hand-maintaining six near-identical files until they drift. The common fix is to keep one source (usually AGENTS.md) and symlink the rest.
- Putting tool-specific paths in the wrong place - `copilot-instructions.md` lives under `.github/`, not the repo root.

### Edge cases
- **Discovery differs:** most are auto-loaded by their tool, but Aider's `CONVENTIONS.md` is opt-in via `--read` / `.aider.conf.yml`.
- **Convergence on `AGENTS.md` (plural):** Amp now reads `AGENTS.md`, and Warp defaults to `AGENTS.md` with `WARP.md` kept only for backwards-compatibility. The singular `AGENT.md` and the standalone `WARP.md` are now legacy - the ecosystem moved toward the shared file, not away from it.
