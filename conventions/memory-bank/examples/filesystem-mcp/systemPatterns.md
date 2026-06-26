<!-- source: filesystem-mcp — https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/systemPatterns.md -->
<!-- Version: 4.6 | Last Updated: 2025-07-04 | Updated By: Sylph -->

# System Patterns: Filesystem MCP Server

## 1. Architecture Overview

The Filesystem MCP server is a standalone Node.js application designed to run as
a child process, communicating with its parent (the AI agent host) via standard
input/output (stdio) using the Model Context Protocol (MCP).

```mermaid
graph LR
    A[Agent Host Environment] -- MCP over Stdio --> B(Filesystem MCP Server);
    B -- Node.js fs/path/glob --> C[User Filesystem (Project Root)];
    C -- Results/Data --> B;
    B -- MCP over Stdio --> A;
```

## 2. Key Technical Decisions & Patterns

- **MCP SDK Usage:** Leverages the `@modelcontextprotocol/sdk` for handling MCP
  communication (request parsing, response formatting, error handling). This
  standardizes interaction and reduces boilerplate code.
- **Stdio Transport:** Uses `StdioServerTransport` from the SDK for
  communication, suitable for running as a managed child process.
- **Asynchronous Operations:** All filesystem interactions and request handling
  are implemented using `async/await` and Node.js's promise-based `fs` module
  (`fs.promises`) for non-blocking I/O.
- **Strict Path Resolution:** A dedicated `resolvePath` function is used for
  _every_ path received from the agent.
  - It normalizes the path.
  - It resolves the path relative to the server process's current working
    directory (`process.cwd()`), which is treated as the `PROJECT_ROOT`.
    **Crucially, this requires the process launching the server (e.g., the agent
    host) to set the correct `cwd` for the target project.**
  - It explicitly checks if the resolved absolute path still starts with the
    `PROJECT_ROOT` absolute path to prevent path traversal vulnerabilities
    (e.g., `../../sensitive-file`).
  - It rejects absolute paths provided by the agent.
  - **Enhanced Error Reporting:** Throws `McpError` with detailed messages on
    failure, including the original path, resolved path (if applicable), and
    project root to aid debugging. Includes console logging for diagnostics.
- **Zod for Schemas & Validation:** Uses `zod` library to define input schemas
  for tools and perform robust validation within each handler. JSON schemas for
  MCP listing are generated from Zod schemas.
- **Tool Definition Aggregation:** Tool definitions (name, description, Zod
  schema, handler function) are defined in their respective handler files and
  aggregated in `src/handlers/index.ts` for registration in `src/index.ts`.
  - **Description Updates:** Descriptions (e.g., for `write_content`, `apply_diff`) are updated based on user feedback and best practices.
- **`apply_diff` Logic:**
  - Processes multiple diff blocks per file, applying them sequentially from bottom-to-top based on `start_line` to minimize line number conflicts.
  - Verifies that the content at the specified `start_line`/`end_line` exactly matches the `search` block before applying the `replace` block.
  - Ensures atomicity at the file level: if any block fails (e.g., content mismatch, invalid lines), the entire file's changes are discarded.
  - Returns detailed success/failure status per file, including context on error.
- **Error Handling:**
  - Uses `try...catch` blocks within each tool handler.
  - Catches specific Node.js filesystem errors (like `ENOENT`, `EPERM`,
    `EACCES`) and maps them to appropriate MCP error codes (`InvalidRequest`) or returns detailed error messages in the result object.
  - **Enhanced `ENOENT` Reporting:** Specifically in `readContent.ts`, `ENOENT` errors now include the resolved path, relative path, and project root in the returned error message for better context.
  - Uses custom `McpError` objects for standardized error reporting back to the
    agent (including enhanced details from `resolvePath`).
  - Logs unexpected errors to the server's console (`stderr`) for debugging.
- **Glob for Listing/Searching:** Uses the `glob` library for flexible and
  powerful file listing and searching based on glob patterns, including
  recursive operations and stat retrieval. Careful handling of `glob`'s
  different output types based on options (`string[]`, `Path[]`, `Path[]` with
  `stats`) is implemented.
- **TypeScript:** Provides static typing for better code maintainability, early
  error detection, and improved developer experience. Uses ES module syntax
  (`import`/`export`).
- **Dockerfile:** Uses a multi-stage build. The first stage (`deps`) installs _only_ production dependencies. The final stage copies `node_modules` and `package.json` from the `deps` stage, and copies the pre-built `build/` directory from the CI artifact context. This avoids rebuilding the project inside Docker and keeps the final image smaller.
- **CI/CD (GitHub Actions - Single Workflow):**
  - A single workflow file (`.github/workflows/publish.yml`) handles both CI checks and releases.
  - **Triggers:** Runs on pushes to the `main` branch and pushes of tags matching `v*.*.*`.
  - **Conditional Logic:**
    - The `build` job runs on both triggers but _only uploads artifacts_ (including `build/`, `package.json`, `package-lock.json`, `Dockerfile`, etc.) when triggered by a tag push.
    - The `publish-npm`, `publish-docker`, and `create-release` jobs depend on the `build` job but run _only_ when triggered by a version tag push.
  - **Structure & Artifact Handling:**
    - `build`: Checks out, installs, builds. Archives and uploads artifacts _if_ it's a tag push. Outputs version and archive filename.
    - `publish-npm`: Needs `build`. Downloads artifact, extracts using correct filename (`build-artifacts.tar.gz`), publishes to npm.
    - `publish-docker`: Needs `build`. Downloads artifact, extracts using correct filename, includes diagnostic `ls -la` steps, sets up Docker, builds (using pre-built code from artifact), and pushes image.
    - `create-release`: Needs `build`, `publish-npm`, `publish-docker`. Downloads artifact, extracts using correct filename, creates GitHub Release.
  - This simplified structure avoids workflow interdependencies while still preventing duplicate publishing actions and unnecessary artifact uploads during CI checks on `main`. Includes diagnostic steps for debugging artifact issues.

## 3. Component Relationships

- **`index.ts`:** Main entry point. Sets up the MCP server instance, defines
  tool schemas, registers request handlers, and starts the server connection.
- **`Server` (from SDK):** Core MCP server class handling protocol logic.
- **`StdioServerTransport` (from SDK):** Handles reading/writing MCP messages
  via stdio.
- **Tool Handler Functions (`handleListFiles`, `handleEditFile`, etc.):**
  Contain the specific logic for each tool, including Zod argument validation,
  path resolution, filesystem interaction, and result formatting (including enhanced error details).
- **`resolvePath` Helper:** Centralized security function for path validation with enhanced error reporting.
- **`formatStats` Helper:** Utility to create a consistent stats object
  structure.
- **Node.js Modules (`fs`, `path`):** Used for actual filesystem operations and
  path manipulation.
- **`glob` Library:** Used for pattern-based file searching and listing.
- **`zod` Library:** Used for defining and validating tool input schemas.

- **`Dockerfile`:** Defines the multi-stage build process for the production Docker image.
- **`.github/workflows/publish.yml`:** Defines the combined CI check and release process using conditional logic within a single workflow.
