# Prompt asset files 🟢 Adopted

> Externalized prompt files - Prompty's YAML-front-mattered .prompty, plain .prompt templates, and system_prompt.txt - that pull the prompt out of source code so it can be versioned and edited on its own. Only .prompty has a formal spec (prompty.ai); .prompt and system_prompt.txt are ad-hoc externalized-prompt filenames.

- **Read by:** Prompty tooling, Azure AI / Semantic Kernel, and apps that load externalized prompts
- **Location:** Alongside application code (e.g. prompts/*.prompty)
- **Spec:** [https://prompty.ai](https://prompty.ai)
- **Evidence:** Prompty, Genkit, and application repos publish external prompt files that tools load independently of source code.
- **Last verified:** 2026-06-18
- **Files:** `.prompty`, `.prompt`, `system_prompt.txt`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.prompty`

Prompty - YAML frontmatter (model + inputs) over a templated prompt body.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `prompty` | [`microsoft/prompty`](https://github.com/microsoft/prompty) | [`examples/prompty/basic.prompty`](examples/prompty/basic.prompty) | [source](https://raw.githubusercontent.com/microsoft/prompty/main/web/src/content/docs/assets/code/basic.prompty) |
| `prompty` | [`microsoft/prompty`](https://github.com/microsoft/prompty) | [`examples/prompty/chat-basic.prompty`](examples/prompty/chat-basic.prompty) | [source](https://raw.githubusercontent.com/microsoft/prompty/main/web/docs-examples/prompts/chat-basic.prompty) |

### `.prompt`

Generic templated prompt file (Genkit dotprompt and similar).

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `genkit` | [`firebase/genkit`](https://github.com/firebase/genkit) | [`examples/genkit/countries.prompt`](examples/genkit/countries.prompt) | [source](https://raw.githubusercontent.com/firebase/genkit/main/go/samples/prompts/prompts/countries.prompt) |

### `system_prompt.txt`

A plain-text externalized system prompt.

| Example | Upstream | File | Exact source |
| --- | --- | --- | --- |
| `diffbot` | [`diffbot/diffbot-llm-inference`](https://github.com/diffbot/diffbot-llm-inference) | [`examples/diffbot/system_prompt.txt`](examples/diffbot/system_prompt.txt) | [source](https://raw.githubusercontent.com/diffbot/diffbot-llm-inference/main/system_prompt.txt) |

## Field notes

### Fields (frontmatter)
**Prompty `.prompty`** (YAML frontmatter + role-marked body):

| Field | Req | Notes |
| --- | --- | --- |
| `name` | yes | display name |
| `description`, `version`, `authors`, `tags` | no | metadata |
| `model` | yes | object: `api` (`chat`/`completion`), `configuration` (`type` + connection: `azure_deployment`/`azure_endpoint`/`api_version`/`api_key`/`name`/`base_url`...), `parameters` (`temperature`, `max_tokens`, `top_p`, `stop`, `response_format`, `tools`, `tool_choice`...), `response` (`first`/`full`/`all`) |
| `sample` | no | inline dict of test inputs, or a filename to load |
| `inputs` / `outputs` | no | per-name specs (`type`, `default`, `description`); `outputs` needs `response_format: json_object` |
| `template` / `template_format` | no | engine: `jinja2` (default), `mustache`, `nunjucks` |

Values support `${env:VAR}`. (A TypeSpec-based **Prompty 2.0** schema is in development; the above is the stable format.)

**Genkit dotprompt `.prompt`** (YAML + Handlebars body): `name?`, `variant?`, `version?`, `description?`, `model`, `config` (camelCase: `temperature`, `maxOutputTokens`, `topK`, `topP`, `stopSequences`...), `tools` (string[]), `toolChoice` (`auto`/`required`/`none`), `input` {`schema`, `default`}, `output` {`format` (`json`/`text`), `schema`}, `metadata`, `raw` (passthrough), `ext` (namespaced extension keys). Schemas can be **Picoschema** (compact YAML), full JSON Schema, or a registered schema name.

**`system_prompt.txt`** = plain UTF-8, no schema, no frontmatter - the whole file is the system message.

### Composition
- **`.prompty` / `.prompt`** put the contract (model + I/O shape) beside the prompt text. Genkit's `countries.prompt` declares `model: googleai/gemini-2.5-flash`, a `config`, and an inline output schema.
- **`system_prompt.txt`** carries the prompt only; Diffbot's defines a whole tool namespace as the system message.

### Anti-patterns
- Hardcoding the prompt inside application source, where it can't be diffed or edited without a code change.
- A templated prompt with no declared inputs/outputs - callers then guess the shape.
- Splitting model/config from the text (or vice-versa) - keep them together.

### Edge cases
- **`.prompty` (Prompty / Azure / Semantic Kernel) vs `.prompt` (Genkit dotprompt)** look alike but are different toolchains with different templating (Jinja2 vs Handlebars) - don't assume one parser reads both.
- dotprompt's `ext` collects any dotted-key frontmatter (`myext.foo: bar`) so non-standard keys don't collide with the reserved schema.
- `system_prompt.txt` carries no version metadata, so provenance relies entirely on git history.

### Adoption / maturity
- Prompt assets are adopted as a family rather than one single standard. Prompty, Genkit Dotprompt, and plain prompt text files all externalize prompt behavior into files that can be versioned and reviewed.
- The portability boundary is the parser: a `.prompty` file can carry model, inputs, tools, and template metadata, while Genkit `.prompt` uses Dotprompt semantics and Handlebars. The same extension shape does not imply compatible runtimes.

### Related conventions
- Use `*.prompt.md` when the file is a VS Code/Copilot slash-command prompt. Use `.prompty` or `.prompt` when application code loads the prompt at runtime.
- Use `SKILL.md` when the prompt needs a reusable agent capability with resources and activation logic.

### Sources checked
- [Prompty file format docs](https://prompty.ai/core-concepts/file-format/)
- [microsoft/prompty repository](https://github.com/microsoft/prompty)
- [Genkit Dotprompt docs](https://genkit.dev/docs/js/dotprompt/)
- [Diffbot system_prompt.txt example](https://raw.githubusercontent.com/diffbot/diffbot-llm-inference/main/system_prompt.txt)
