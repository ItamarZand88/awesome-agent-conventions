# Prompt asset files 🟢 Adopted

> Externalized prompt files — Prompty's YAML-front-mattered .prompty, plain .prompt templates, and system_prompt.txt — that pull the prompt out of source code so it can be versioned and edited on its own.

- **Read by:** Prompty tooling, Azure AI / Semantic Kernel, and apps that load externalized prompts
- **Location:** Alongside application code (e.g. prompts/*.prompty)
- **Spec:** [https://prompty.ai](https://prompty.ai)
- **Files:** `.prompty`, `.prompt`, `system_prompt.txt`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) — none are hand-written._

### `.prompty`

Prompty — YAML frontmatter (model + inputs) over a templated prompt body.

| Source | File | Provenance |
| --- | --- | --- |
| `prompty` | [`prompty.basic.prompty`](examples/prompty.basic.prompty) | [source](https://raw.githubusercontent.com/microsoft/prompty/main/web/src/content/docs/assets/code/basic.prompty) |
| `prompty` | [`prompty.chat-basic.prompty`](examples/prompty.chat-basic.prompty) | [source](https://raw.githubusercontent.com/microsoft/prompty/main/web/docs-examples/prompts/chat-basic.prompty) |

### `.prompt`

Generic templated prompt file (Genkit dotprompt and similar).

| Source | File | Provenance |
| --- | --- | --- |
| `genkit` | [`genkit.countries.prompt`](examples/genkit.countries.prompt) | [source](https://raw.githubusercontent.com/firebase/genkit/main/go/samples/prompts/prompts/countries.prompt) |

### `system_prompt.txt`

A plain-text externalized system prompt.

| Source | File | Provenance |
| --- | --- | --- |
| `diffbot` | [`diffbot.system_prompt.txt`](examples/diffbot.system_prompt.txt) | [source](https://raw.githubusercontent.com/diffbot/diffbot-llm-inference/main/system_prompt.txt) |

## Field notes

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
