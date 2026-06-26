<!-- source: filesystem-mcp — https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/techContext.md -->
<!-- Version: 4.9 | Last Updated: 2025-07-04 | Updated By: Sylph -->

# Tech Context: Filesystem MCP Server

## Playbook Guideline Versions Checked

- `guidelines/typescript/style_quality.md`: 9d56a9d6626ecc2fafd0b07033220a1282282236

# Tech Context: Filesystem MCP Server

## 1. Core Technologies

- **Runtime:** Node.js (MUST use latest LTS version, currently v22 - `~22.0.0` specified in `package.json`)
- **Language:** TypeScript (Compiled to JavaScript for execution)
- **Package Manager:** pnpm (Preferred package manager as per guidelines)
- **Testing Framework:** Vitest (using v8 for coverage)

## 2. Key Libraries/Dependencies

- **`@modelcontextprotocol/sdk`:** The official SDK for implementing MCP servers and clients.
- **`glob`:** Library for matching files using glob patterns.
- **`typescript`:** TypeScript compiler (`tsc`).
- **`@types/node`:** TypeScript type definitions for Node.js built-in modules.
- **`@types/glob`:** TypeScript type definitions for the `glob` library.
- **`zod`:** Library for schema declaration and validation.
- **`zod-to-json-schema`:** Utility to convert Zod schemas to JSON schemas.

- **`vitest`:** Testing framework.
- **`@vitest/coverage-v8`:** Coverage provider for Vitest.
- **`uuid`:** For generating unique IDs (used in testUtils).
- **`@types/uuid`:** TypeScript type definitions for uuid.

## 3. Development Setup

- **Source Code:** Located in the `src` directory.
- **Tests:** Located in the `__tests__` directory.
- **Main File:** `src/index.ts`.
- **Configuration:**
  - `tsconfig.json`: Configures the TypeScript compiler options.
  - `vitest.config.ts`: Configures Vitest (test environment, globals, coverage).
  - `package.json`: Defines project metadata, dependencies, and pnpm scripts. - `dependencies`: `@modelcontextprotocol/sdk`, `glob`, `zod`, `zod-to-json-schema`. - `devDependencies`: `typescript`, `@types/node`, `@types/glob`, `vitest`, `@vitest/coverage-v8`, `uuid`, `@types/uuid`, `husky`, `lint-staged`, `@commitlint/cli`, `@commitlint/config-conventional`, `prettier`, `eslint`, `typescript-eslint`, `eslint-plugin-prettier`, `eslint-config-prettier`, `standard-version`, `typedoc`, `typedoc-plugin-markdown`, `vitepress`, `rimraf`, `@changesets/cli`. (List might need verification against actual `package.json`)
    - `scripts`: (Uses `pnpm run ...`)
      - `build`: Compiles TypeScript code. - `watch`: Runs `tsc` in watch mode. - `clean`: `rimraf dist coverage` - `inspector`: `npx @modelcontextprotocol/inspector dist/index.js`
      - `test`: Runs Vitest tests.
      - `test:cov`: Runs Vitest tests with coverage.
      - `validate`: Runs format check, lint, typecheck, and tests.
      - `docs:build`: Builds documentation. - `start`: `node dist/index.js` - `prepare`: `husky` - `prepublishOnly`: `pnpm run clean && pnpm run build` - (Other scripts as defined in `package.json`)
- **Build Output:** Compiled JavaScript code is placed in the `dist` directory.
- **Execution:** The server is intended to be run via `node dist/index.js`.

## 4. Technical Constraints & Considerations

- **Node.js Environment:** Relies on Node.js runtime and built-in modules.
- **Permissions:** Server process permissions limit filesystem operations.
- **Cross-Platform Compatibility:** Filesystem behaviors differ. Code uses `path` module and normalizes slashes.
- **Error Handling:** Relies on Node.js error codes and `McpError`.
- **Security Model:** Relies on `resolvePath` function.
- **Project Root Determination:** Uses `process.cwd()`. Launching process must set correct `cwd`.
- **ESM:** Project uses ES Modules. Vitest generally handles ESM well, including mocking.
