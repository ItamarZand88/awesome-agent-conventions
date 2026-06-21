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
