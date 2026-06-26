<!-- source: rapid7-bulk-export-mcp — https://raw.githubusercontent.com/rapid7/rapid7-bulk-export-mcp/main/.kiro/steering/structure.md -->
# Project Structure

```
rapid7-bulk-export-mcp/
├── src/                          # Main package (installed as 'src')
│   ├── __init__.py               # Package metadata
│   ├── mcp_server.py             # FastMCP server — tool definitions and entry point
│   ├── config.py                 # Environment config loading (API key, region, endpoint)
│   ├── graphql_client.py         # GraphQL HTTP client for Rapid7 API
│   ├── export_manager.py         # Export lifecycle (create, poll, status, date chunking)
│   ├── export_tracker.py         # DuckDB-based export metadata tracker (reuse same-day exports)
│   ├── download.py               # Parquet file downloading from Rapid7 URLs
│   └── duckdb_loader.py          # DuckDB table management, Parquet loading, querying
├── tests/                        # Test suite (pytest)
│   ├── test_config.py
│   ├── test_download.py
│   ├── test_duckdb_loader.py
│   ├── test_export_integration.py
│   ├── test_export_manager.py
│   ├── test_export_tracker.py
│   ├── test_graphql_client.py
│   └── test_setup.py
├── rapid7-bulk-export-skill/     # Agent Skill content (SKILL.md + README)
├── power-rapid7-bulk-export/     # Kiro Power (POWER.md + mcp.json + steering/)
├── docs/                         # Demo GIFs for README
├── run_server.py                 # Thin entry point for MCPB/uv direct execution
├── pyproject.toml                # Package metadata, dependencies, tool config
├── manifest.json                 # MCPB manifest (canonical version source)
├── Makefile                      # Build, lint, test, release automation
├── cortex.yaml                   # Rapid7 service metadata
└── .kiro/steering/               # AI assistant steering rules
```

## Architecture Patterns

- **Single-package layout**: All source lives in `src/` and is installed as the `src` package.
- **Entry point**: `rapid7-mcp-server` console script maps to `src.mcp_server:main`.
- **Global state**: The MCP server uses a module-level `db` variable (VulnerabilityDatabase instance) initialized on first use.
- **Two databases**:
  - `rapid7_bulk_export.db` — main DuckDB with vulnerability/asset/policy data
  - `rapid7_bulk_export_tracking.db` — export metadata tracker for same-day reuse
- **Prefix-based routing**: Parquet files from the API are routed to DuckDB tables based on their prefix (e.g., `asset_vulnerability` → `vulnerabilities` table).
- **Tool annotations**: Each MCP tool uses `ToolAnnotations` to declare read-only, destructive, and idempotent hints.

## Conventions

- Test files mirror source files: `src/config.py` → `tests/test_config.py`
- Tests use class-based grouping (`class TestXxx`) with descriptive method names
- Mocking via `unittest.mock.patch` and the `responses` library for HTTP
- Property-based tests use `hypothesis` with the `@pytest.mark.property` marker
- All user-facing output goes to `sys.stderr`; MCP communication uses stdio
- Security-sensitive SQL uses `# nosec B608` annotations where dynamic queries are safe by design
