<!-- source: agentmap — https://raw.githubusercontent.com/remorses/agentmap/main/MEMORY.md -->
# Memory

- `@agentmap/opencode` must treat `experimental.chat.system.transform` as the authoritative session boundary for prompt-cached state. In OpenCode, `chat.message` runs after system prompt construction, so clearing per-session caches there can leak the previous session's system prompt into the first turn of the next session.
- In OpenCode source-mode, CommonJS-ish packages like `ignore` and `picomatch` can show up as either `default` or a callable module namespace, and top-level `require()` can also fail. In `agentmap`, lazy `await import()` plus a minimal `module.default || module` fallback is the safe path.
