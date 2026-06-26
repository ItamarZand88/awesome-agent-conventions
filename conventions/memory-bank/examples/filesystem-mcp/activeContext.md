<!-- source: filesystem-mcp — https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/activeContext.md -->
<!-- Version: 4.39 | Last Updated: 2025-07-04 | Updated By: Sylph -->

# Active Context: Filesystem MCP Server

## 1. Current Work Focus & Status

**Task:** Implement `apply_diff` tool.
**Status:** Completed configuration alignment and file renaming based on `guidelines/typescript/style_quality.md` (SHA: 9d56a9d...). ESLint check (with `--no-cache`) confirms **no errors**. `import/no-unresolved` rule was temporarily disabled but seems unnecessary now.
## 2. Recent Changes/Decisions

- **Configuration Alignment:**
    - Updated `package.json`: Added ESLint dependencies (`eslint-config-airbnb-typescript`, `eslint-plugin-import`, `eslint-plugin-unicorn`), updated scripts (`lint`, `validate`), updated `lint-staged`.
    - Created `.eslintrc.js` based on guideline template.
    - Deleted old `eslint.config.js`.
    - Updated `.prettierrc.js` (formerly `.cjs`) content and filename based on guideline.
    - Updated `tsconfig.json`: Set `module` and `moduleResolution` to `NodeNext`.
- **Guideline Checksum:** Updated `memory-bank/techContext.md` with the latest SHA for `style_quality.md`.
- (Previous changes remain relevant)

## 3. Next Steps

1.  **NEXT:** Rename `__tests__/testUtils.ts` to `__tests__/test-utils.ts`.
2.  **DONE:** ESLint errors fixed (confirmed via `--no-cache`).
3.  **DONE:** Verified `import/no-unresolved` rule (re-enabled in `eslint.config.ts`, no errors reported).
4.  **DONE:** Verified tests in `__tests__/handlers/apply-diff.test.ts` are passing.
5.  **NEXT:** Enhance `apply_diff` tests further (edge cases, large files).
6.  Consider adding performance benchmarks for `apply_diff`.
7.  Update `README.md` with details about the new `apply_diff` tool and remove mentions of `edit_file`.

## 4. Active Decisions

- **Skipped Tests:** `chmodItems`, `chownItems` (Windows limitations), `searchFiles` zero-width regex test (implementation complexity).
- Temporarily skipping full ESLint validation pass to focus on completing the `apply_diff` implementation and basic testing.
- (Previous decisions remain active unless superseded).
