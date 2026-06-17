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
