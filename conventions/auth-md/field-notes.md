### Composition
The WorkOS example is the clearest live instance and worth studying:
- **Addressed to the agent**, in the second person: *"You are an agent. This document tells you how to register a credential…"* — and it forks immediately: *"Not an agent? You might be looking for workos.com/auth-md."*
- **Ordered steps** ("Follow the steps in order; do not skip ahead") with a named flow (anonymous provision → later user-claim).
- **A CLI shortcut *and* a raw-HTTP fallback**, so it works whether or not Node is present.
- Concrete machine affordances: agent-context detection (`CLAUDECODE`, `CURSOR_AGENT`, `CODEX_SANDBOX`), structured JSON output, and `gh`-style exit codes (`0/1/2/4`).

### Anti-patterns
- Assuming a human reader — WorkOS explicitly branches instead.
- Offering only a CLI with no HTTP fallback for environments without Node.
- Unordered or branchy instructions an agent can't follow deterministically.

### Edge cases
- **🟠 Emerging:** strong spec, essentially one polished live example. Treat the shape as indicative, not settled.
- Flows vary (user-claimed vs verified registration); placement (`/auth.md` vs `.well-known/`) is still converging.
