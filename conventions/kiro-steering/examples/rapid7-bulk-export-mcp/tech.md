<!-- source: rapid7-bulk-export-mcp — https://raw.githubusercontent.com/rapid7/rapid7-bulk-export-mcp/main/.kiro/steering/tech.md -->
# Tech Stack & Build System

## Language & Runtime

- Python >= 3.10

## Build System

- **Hatchling** as the build backend (`pyproject.toml`)
- **uv** as the package manager and task runner (lockfile: `uv.lock`)

## Core Dependencies

| Library | Purpose |
|---------|---------|
| fastmcp | MCP server framework (stdio transport) |
| duckdb | Local analytical database for Parquet data |
| pyarrow | Parquet file reading |
| requests | HTTP client for Rapid7 GraphQL API |

## Dev Dependencies

| Library | Purpose |
|---------|---------|
| pytest | Test framework |
| hypothesis | Property-based testing |
| responses | HTTP request mocking |
| ruff | Linter and formatter |
| bandit | Security static analysis |

## Common Commands

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest --tb=short

# Lint (check only)
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/

# Lint (auto-fix)
uv run ruff check --fix src/ tests/
uv run ruff format src/ tests/

# Security scan
uv run bandit -r src/ -c pyproject.toml

# Run the MCP server locally
uv run rapid7-mcp-server

# Version check (all files in sync)
make check-version

# Bump version
make bump-version V=x.y.z

# Build release artifacts
make package

# Full release (verify + build + publish)
make release
```

## Configuration

The server requires two environment variables:
- `RAPID7_API_KEY` — Rapid7 InsightVM API key
- `RAPID7_REGION` — Region identifier (`us`, `us2`, `us3`, `eu`, `ca`, `au`, `ap`)

## Code Quality Rules

- **Ruff** config: target Python 3.10, line length 120, rules E/F/W/I (isort)
- **Bandit** skips: B110 (bare except pass), B112 (try-except-continue)
- **Pytest** markers: `property`, `unit`, `integration`
- **Hypothesis** max examples: 100
