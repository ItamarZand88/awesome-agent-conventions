<!-- source: rapid7-bulk-export-mcp — https://raw.githubusercontent.com/rapid7/rapid7-bulk-export-mcp/main/.kiro/steering/product.md -->
# Product Overview

Rapid7 Bulk Export MCP is an MCP (Model Context Protocol) server that exports vulnerability, asset, policy, and remediation data from the Rapid7 Command Platform via the Bulk Export API, loads it into a local DuckDB database, and exposes SQL query tools for AI-powered security analysis.

## Key Capabilities

- Export data from Rapid7 InsightVM (vulnerabilities, policies, remediation)
- Load Parquet files into a local DuckDB database
- Query data via SQL through MCP tool interface
- Reuse same-day exports to avoid redundant API calls
- Automatic date-range chunking for remediation exports (31-day API limit)

## Users

Security analysts and engineers who use AI assistants (Kiro, Claude Desktop, GitHub Copilot) to analyze vulnerability data from Rapid7 InsightVM via natural language or SQL queries.

## Distribution

- Published as a pip-installable Python package
- Also distributed as an MCPB bundle with an accompanying Agent Skill zip
- Versioned via `manifest.json` (source of truth), synced to `pyproject.toml` and `SKILL.md`
