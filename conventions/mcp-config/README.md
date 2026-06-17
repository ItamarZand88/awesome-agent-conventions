# MCP server config 🟢 Adopted

> A JSON file that tells an agent which Model Context Protocol servers to launch and how (command, args, env) - making a project's tool and data integrations portable, shareable, and version-controlled across every MCP-capable client.

- **Read by:** Claude Code, Claude Desktop, Cursor, VS Code / Copilot - any MCP host
- **Location:** Repo root (.mcp.json), .vscode/mcp.json, or the app config dir (claude_desktop_config.json)
- **Spec:** [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)
- **Files:** `.mcp.json`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.mcp.json`

Project-scoped MCP servers. The same { "mcpServers": {...} } schema also appears as .vscode/mcp.json (VS Code / Copilot) and claude_desktop_config.json (Claude Desktop).

| Source | File | Provenance |
| --- | --- | --- |
| `inspec-vscode` | [`inspec-vscode.mcp.json`](examples/inspec-vscode.mcp.json) | [source](https://raw.githubusercontent.com/inspec/inspec/main/.vscode/mcp.json) |
| `wp-calypso` | [`wp-calypso.mcp.json`](examples/wp-calypso.mcp.json) | [source](https://raw.githubusercontent.com/Automattic/wp-calypso/trunk/.mcp.json) |

## Field notes

### Composition
- **One object, one job:** `{ "mcpServers": { "<name>": { "command", "args", "env" } } }`. A stdio server gives a `command` + `args`; a remote server gives a `url` / `type`. Secrets flow through `env` (often `${VAR}` expansion), not inline.
- A committed `.mcp.json` is how a team shares one tool surface - every contributor's agent launches the same servers with the same config.

### Anti-patterns
- Hardcoding API keys or tokens in `env` instead of referencing environment variables. The file is checked in - treat it as public.
- Per-developer absolute paths in `command` / `args` that break on every other machine.

### Edge cases
- **Same schema, different homes and scopes:** project `.mcp.json` (Claude Code), `.vscode/mcp.json` (VS Code / Copilot), and `claude_desktop_config.json` (Claude Desktop), plus user/global variants - precedence and merge rules differ per host.
- A malformed entry can fail silently or block startup; hosts vary in how loudly they report a server that won't launch.
- The two examples here pair a root `.mcp.json` with a `.vscode/mcp.json` to make the cross-tool shape concrete - same `mcpServers` schema, different file.
