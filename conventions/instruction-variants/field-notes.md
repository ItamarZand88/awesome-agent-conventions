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
- **Singular vs plural:** Amp's `AGENT.md` is deliberately distinct from `AGENTS.md` - don't conflate them.
