<!-- source: filesystem-mcp — https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/projectbrief.md -->
<!-- Version: 4.6 | Last Updated: 2025-07-04 | Updated By: Sylph -->

# Project Brief: Filesystem MCP Server

## 1. Project Goal

The primary goal of this project is to create a Model Context Protocol (MCP)
server specifically designed for filesystem operations. This server should allow
an AI agent (like Cline) to interact with the user's filesystem in a controlled
and secure manner, operating relative to a defined project root directory.

## 2. Core Requirements

- **MCP Compliance:** The server must adhere to the Model Context Protocol
  specifications for communication.
- **Relative Pathing:** All filesystem operations must be strictly relative to
  the project root directory. Absolute paths should be disallowed, and path
  traversal attempts must be prevented.
- **Core Filesystem Tools:** Implement a comprehensive set of tools for common
  filesystem tasks:
  - `list_files`: List files/directories within a specified directory (options
    for recursion, stats).
  - `stat_items`: Get detailed status information for multiple specified paths.
  - `read_content`: Read content from multiple specified files.
  - `write_content`: Write or append content to multiple specified files
    (creating directories if needed).
  - `delete_items`: Delete multiple specified files or directories.
  - `create_directories`: Create multiple specified directories (including
    intermediate ones).
  - `chmod_items`: Change permissions for multiple specified files/directories.
  - `chown_items`: Change owner (UID) and group (GID) for multiple specified
    files/directories.
  - `move_items`: Move or rename multiple specified files/directories.
  - `copy_items`: Copy multiple specified files/directories.
  - `search_files`: Search for regex patterns within files in a specified
    directory.
  - `replace_content`: Search and replace content within files across multiple
    specified paths (files or directories).
    - `apply_diff`: Applies multiple search/replace diff blocks to multiple files atomically per file.
- **Technology Stack:** Use Node.js and TypeScript. Leverage the
  `@modelcontextprotocol/sdk` for MCP implementation and `glob` for file
  searching/listing.
- **Efficiency:** Tools should be implemented efficiently, especially for
  operations involving multiple files or large directories.
- **Security:** Robust path resolution and validation are critical to prevent
  access outside the designated project root.

## 3. Scope

- **In Scope:** Implementation of the MCP server logic, definition of tool
  schemas, handling requests, performing filesystem operations via Node.js `fs`
  and `path` modules, and using `glob`. Basic error handling for common
  filesystem issues (e.g., file not found, permissions).
- **Out of Scope:** Advanced features like file watching, complex permission
  management beyond basic `chmod`, handling extremely large files requiring
  streaming (beyond basic read/write), or integration with version control
  systems.

## 4. Success Criteria

- The server compiles successfully using TypeScript.
- The server connects and responds to MCP requests (e.g., `list_tools`).
- All implemented tools function correctly according to their descriptions,
  respecting relative path constraints.
- Path traversal attempts are correctly blocked.
- The server handles basic errors gracefully (e.g., file not found).
