### Composition
- **`.prompty` / `.prompt`** = YAML frontmatter over a templated body. Genkit's `countries.prompt` declares `model: googleai/gemini-2.5-flash`, `config`, and an inline **output JSON schema**, then the prompt text — so the contract (model + I/O shape) travels with the prompt.
- **`system_prompt.txt`** = plain text, no metadata. Diffbot's defines a whole tool/function namespace in TypeScript-like syntax as the system message.

### Anti-patterns
- Hardcoding the prompt inside application source, where it can't be diffed or edited without a code change.
- A templated prompt with no declared inputs/outputs — callers then guess the shape.
- Burying model/config choices in code while the text lives in a file (or vice-versa) — keep them together.

### Edge cases
- **`.prompty` (Prompty / Azure / Semantic Kernel) vs `.prompt` (Genkit dotprompt)** look alike but are different toolchains with different templating — don't assume one parser reads both.
- `system_prompt.txt` carries no version metadata, so provenance relies entirely on git history.
