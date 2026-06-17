### Fields (schema)
The three hosts share the *idea* but differ in keys - this is the part people get wrong.

**Claude Code `.mcp.json`** - top level `{ "mcpServers": { "<name>": {...} } }`:

| Field | Notes |
| --- | --- |
| `type` | `stdio` (default) / `sse` / `http` |
| `command`, `args` | required for stdio |
| `env` | `{VAR: value}`; supports `${VAR}` and `${VAR:-default}` expansion |
| `url`, `headers` | required for sse/http remote servers (`headers` also expands `${VAR}`) |

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
