# MCP server config 🟢 Adopted

> A JSON file that tells an agent which Model Context Protocol servers to launch and how (command, args, env) - making a project's tool and data integrations portable, shareable, and version-controlled across every MCP-capable client.

- **Read by:** Claude Code, Claude Desktop, Cursor, VS Code / Copilot - any MCP host
- **Location:** Repo root (.mcp.json), .vscode/mcp.json, or the app config dir (claude_desktop_config.json)
- **Spec:** [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)
- **Evidence:** MCP hosts including Claude Code, Claude Desktop, Cursor, and VS Code document project or app-level MCP server config files.
- **Last verified:** 2026-06-18
- **Files:** `.mcp.json`

## Examples

_Every file below was fetched from a public source by [`scripts/extract.py`](../../scripts/extract.py) - none are hand-written._

### `.mcp.json`

Project-scoped MCP servers. The same { "mcpServers": {...} } schema also appears as .vscode/mcp.json (VS Code / Copilot) and claude_desktop_config.json (Claude Desktop).

| Source | File | Provenance |
| --- | --- | --- |
| `inspec-vscode` | [`examples/inspec-vscode/.mcp.json`](examples/inspec-vscode/.mcp.json) | [source](https://raw.githubusercontent.com/inspec/inspec/main/.vscode/mcp.json) |
| `wp-calypso` | [`examples/wp-calypso/.mcp.json`](examples/wp-calypso/.mcp.json) | [source](https://raw.githubusercontent.com/Automattic/wp-calypso/trunk/.mcp.json) |

## Field notes

### Fields (schema)
The three hosts share the *idea* but differ in keys - this is the part people get wrong.

**Claude Code `.mcp.json`** - top level `{ "mcpServers": { "<name>": {...} } }`:

| Field | Notes |
| --- | --- |
| `type` | `stdio` (default) / `http` / `sse` / `ws`; `streamable-http` aliases to `http` |
| `command`, `args` | required for stdio |
| `env` | `{VAR: value}`; supports `${VAR}` and `${VAR:-default}` expansion |
| `url`, `headers` | required for remote servers (`headers` also expands `${VAR}`) |

Scopes: `local` (per-project, in `~/.claude.json`), `project` (committed `.mcp.json`), `user` (global).

**VS Code `.vscode/mcp.json`** - top level is **`servers`** (not `mcpServers`), plus an optional **`inputs`** array for prompted/secret values. Stdio servers add `cwd` and `envFile`; remote servers use `type: http|sse` + `url` + `headers`. References: `${input:id}`, `${workspaceFolder}`, `${env:VAR}`.

**Claude Desktop `claude_desktop_config.json`** - `{ "mcpServers": {...} }`, historically **stdio-only** (`command`/`args`/`env`); remote servers are added via Connectors / an `mcp-remote` proxy.

### Composition
- A committed config is how a team shares one tool surface - every contributor's agent launches the same servers with the same settings.

### Anti-patterns
- Hardcoding API keys or tokens in `env`/`headers` instead of referencing environment variables (or VS Code `inputs`). The file is checked in - treat it as public.
- Per-developer absolute paths in `command` / `args` that break on every other machine.

### Edge cases
- **Same idea, different keys:** Claude Code/Desktop use `mcpServers`; VS Code uses `servers` + `inputs`. A `.mcp.json` schema is not drop-in for `.vscode/mcp.json`.
- A malformed entry can fail silently or block startup; hosts vary in how loudly they report a server that won't launch.
- The two examples here pair a root `.mcp.json` with a `.vscode/mcp.json` to make the cross-tool shape concrete.

### Adoption / maturity
- MCP config is adopted because the protocol is widely supported, but the on-disk config shape is host-specific. The convention here is "project-shared MCP server configuration," not one universal JSON schema.
- Remote HTTP is the direction of travel for cloud services; SSE remains supported in some clients but is increasingly legacy. Stdio remains the right fit for local tools that need filesystem/process access.

### Related conventions
- MCP config tells the agent what tools to connect. AGENTS.md / CLAUDE.md should explain when to use those tools and any safety expectations.
- Never put credentials directly in committed config; use environment expansion, host secret prompts, or VS Code `inputs`.

### Sources checked
- [Claude Code MCP docs](https://code.claude.com/docs/en/mcp)
- [VS Code MCP server docs](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification)
