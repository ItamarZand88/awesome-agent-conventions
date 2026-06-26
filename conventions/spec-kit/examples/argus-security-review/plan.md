<!-- source: argus-security-review — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/009-security-review/plan.md -->
# Implementation Plan: Security Review & Hardening

**Branch**: `009-security-review` | **Date**: 2026-04-02 | **Spec**: `specs/009-security-review/spec.md`
**Input**: Feature specification from `/specs/009-security-review/spec.md`

## Summary

Harden the Argus backend against five vulnerability classes identified in the security review: PID injection via the hook endpoint, shell command injection in process control, hook payload resource exhaustion, unrestricted filesystem path traversal, and missing HTTP security headers. All changes are to existing backend source files; no new routes or data migrations are required.

## Technical Context

**Language/Version**: TypeScript 5.5, Node.js 22 (ESM)
**Primary Dependencies**: Fastify 4, better-sqlite3, chokidar, ps-list, pino
**Storage**: SQLite via better-sqlite3 (no schema changes)
**Testing**: Vitest 1.6 + supertest (existing test infrastructure)
**Target Platform**: Windows 11 / macOS / Linux localhost (`127.0.0.1:7411`)
**Project Type**: Local web service (single-user developer tool)
**Performance Goals**: No regressions; `psList()` call in PID validation adds <50ms to stop/interrupt paths (acceptable)
**Constraints**: Localhost-only; no auth layer changes; no new npm dependencies
**Scale/Scope**: Single user, ≤20 concurrent sessions

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked post-design — no violations found.*

| Principle | Status | Notes |
|-----------|--------|-------|
| §IV Test-First | **REQUIRED** — all tasks below follow Red-Green-Refactor | Tests written before implementation in every task |
| §V Testing | **REQUIRED** — unit + integration + e2e coverage for all changes | See task breakdown |
| §VI Security | **SATISFIED** — localhost exception declared in spec Assumptions | Audit logging: security rejection events are logged via Fastify's structured logger (`request.log.warn`) |
| §VII Observability | **SATISFIED** — existing pino logger; rejections logged with structured context | |
| §IX AI Usage | **NOTE** — security-critical code (PID validator, path sandbox) MUST have explicit human review before merge | |
| §XI Documentation | **REQUIRED** — README.md update task included (Phase D) | |
| §XII Error Handling | **REQUIRED** — all new 4xx/409 responses use `{ error, message, requestId }` contract | Verified against existing fs.ts pattern |

**Complexity Tracking**: No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/009-security-review/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── contracts/
│   └── security-hardening.md   # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (files modified by this feature)

```text
backend/
├── src/
│   ├── api/routes/
│   │   ├── hooks.ts             # Add bodyLimit, UUID validation, 409 conflict guard
│   │   └── fs.ts                # Add path boundary enforcement, fix lstatSync
│   ├── services/
│   │   ├── session-controller.ts  # Fix exec→spawnSync, call pid-validator
│   │   └── pid-validator.ts       # NEW — two-stage PID ownership check
│   ├── utils/
│   │   └── path-sandbox.ts        # NEW — path boundary helper
│   └── server.ts                  # Add security headers to onSend hook
└── tests/
    ├── unit/
    │   ├── pid-validator.test.ts   # NEW
    │   └── path-sandbox.test.ts    # NEW
    └── integration/
        ├── hooks.test.ts           # Extend with security scenarios
        ├── fs.test.ts              # Extend with boundary scenarios
        ├── sessions.test.ts        # Extend with PID validation scenarios
        └── security-headers.test.ts  # NEW
```

**Structure Decision**: Web application layout (Option 2 from template). New utility files go under `backend/src/utils/` to distinguish them from service-layer code that interacts with the database or external processes.

---

## Phase 0: Research

**Status: Complete** — see `research.md`.

All NEEDS CLARIFICATION items resolved:

| Unknown | Resolution |
|---------|-----------|
| Windows process kill without shell interpolation | `spawnSync('taskkill', ['/PID', String(pid), '/T', '/F'])` — no shell |
| PID ownership check mechanism | Two-stage: registry + `psList()` name/cmd heuristic (matches existing pattern in codebase) |
| `session_id` valid character set | UUID v4 regex — confirmed from real Copilot CLI session data |
| Symlink loop detection | Use `lstatSync` + skip `isSymbolicLink()` entries |
| Security headers approach | Manual `reply.header()` in existing `onSend` hook — no new plugin |
| Concurrent hook conflict resolution | First write wins — 409 if existing session's PID is overwritten |

---

## Phase 1: Design & Contracts

**Status: Complete**

### New Services

#### `backend/src/services/pid-validator.ts`

Single exported async function:

```typescript
export async function validatePidOwnership(
  pid: number,
  sessionType: 'claude-code' | 'copilot-cli'
): Promise<{ valid: boolean; reason?: 'not_in_registry' | 'process_not_found' | 'process_not_ai_tool' }>
```

Logic:
1. Guard: `pid` must be a positive integer — return `{ valid: false, reason: 'not_in_registry' }` if not.
2. Look up session in DB by PID — if no session has this PID, return `{ valid: false, reason: 'not_in_registry' }`.
3. Call `psList()`, find entry with `p.pid === pid`.
4. If not found: return `{ valid: false, reason: 'process_not_found' }`.
5. Check name/cmd against type-specific allowlist. If no match: `{ valid: false, reason: 'process_not_ai_tool' }`.
6. Return `{ valid: true }`.

> Note: The session registry is the authoritative source. A PID not in the registry is rejected before any OS call.

#### `backend/src/utils/path-sandbox.ts`

```typescript
export function isPathWithinBoundary(inputPath: string, allowedBoundaries: string[]): boolean
```

Logic:
1. `resolved = path.resolve(inputPath)` — canonicalizes and makes absolute.
2. For each boundary in `allowedBoundaries`: return `true` if `resolved === boundary` OR `resolved.startsWith(boundary + path.sep)`.
3. Return `false`.

Boundaries passed in from routes: `[homedir(), ...getRepositories().map(r => r.path)]`.

### Modified Services

#### `backend/src/services/session-controller.ts`

- `killProcess(pid)`: Replace `execAsync('taskkill /PID ${pid} /T /F')` with `spawnSync('taskkill', ['/PID', String(pid), '/T', '/F'])`.
- `interruptProcess(pid)`: Replace `execAsync('taskkill /PID ${pid}')` with `spawnSync('taskkill', ['/PID', String(pid)])`.
- `stopSession(sessionId)`: Before calling `killProcess`, call `validatePidOwnership(session.pid, session.type)`. Throw typed error on failure.
- `interruptSession(sessionId)`: Same.

#### `backend/src/api/routes/hooks.ts`

- Add `{ bodyLimit: 64 * 1024 }` to the POST route options.
- In `handleHookPayload` (called by detector): validate `session_id` against UUID v4 regex before any path construction or DB access.
- Add 409 guard: if existing session has non-null `pid` and incoming payload carries a different `pid`, return 409.

> Note: Current hook payloads do not carry `pid` — this guard is defensive and enforces FR-004 contractually.

#### `backend/src/api/routes/fs.ts`

- All three path-accepting routes (`/browse`, `/scan`, `/scan-folder`): call `isPathWithinBoundary(input, boundaries)` after `normalize` but before any filesystem access. Return 403 on failure.
- `findGitRepos`: replace `statSync(fullPath).isDirectory()` with `lstatSync(fullPath)` — if `isSymbolicLink()`, skip the entry.

#### `backend/src/server.ts`

- `onSend` hook: add `reply.header('X-Content-Type-Options', 'nosniff')` and `reply.header('X-Frame-Options', 'DENY')`.

### Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| `pid-validator.ts` as a standalone module, not a method on `SessionController` | Keeps validation logic independently testable without constructing a full controller; aligns with §I "testable in isolation" |
| `path-sandbox.ts` in `utils/` not `services/` | No DB or external process interaction; pure function belongs in utils |
| No new npm dependencies | All required capabilities available via existing `ps-list`, `child_process`, and Node.js `path`/`os` built-ins |
| `spawnSync` not `spawn` for taskkill | The kill operation is fire-and-forget; synchronous avoids needing to thread a promise through what is already an awaited function |

---

## Implementation Phases (for /speckit.tasks)

### Phase A — Process Control Safety (FR-001, FR-002, FR-003, FR-004)

Tasks in this phase address the highest-severity vulnerabilities: PID injection and shell command injection.

1. **[A1]** Write unit tests for `pid-validator.ts` (mock `psList`, DB lookup) — test-first
2. **[A2]** Implement `pid-validator.ts`
3. **[A3]** Write unit tests for `session-controller.ts` stop/interrupt with PID validation (mock validator)
4. **[A4]** Update `session-controller.ts`: call validator in `stopSession` and `interruptSession`
5. **[A5]** Replace `execAsync` taskkill calls with `spawnSync` in `session-controller.ts`
6. **[A6]** Write integration test for 409 on conflicting PID in hook payload
7. **[A7]** Add 409 guard to hook handler in `hooks.ts`

### Phase B — Hook Endpoint Validation (FR-005, FR-006, FR-007)

8. **[B1]** Write integration tests for hook body size limit, UUID validation, cwd rejection
9. **[B2]** Add `bodyLimit: 64 * 1024` to `/hooks/claude` route
10. **[B3]** Add UUID v4 validation for `session_id` in hook handler

> FR-007 (cwd registry check): already implemented — `handleHookPayload` returns early if `getRepositoryByPath` returns null. Test coverage to be added in B1.

### Phase C — Filesystem Route Safety (FR-008, FR-009, FR-010)

11. **[C1]** Write unit tests for `path-sandbox.ts` (home dir boundary, traversal, Windows paths)
12. **[C2]** Implement `path-sandbox.ts`
13. **[C3]** Write integration tests for fs routes: boundary rejection, traversal sequences, Windows system paths
14. **[C4]** Apply `isPathWithinBoundary` to `/browse`, `/scan`, `/scan-folder` routes
15. **[C5]** Fix `findGitRepos` to use `lstatSync` and skip symlinks

### Phase D — Security Headers & Documentation (FR-011, FR-012, §XI)

16. **[D1]** Write integration test for security headers on all routes
17. **[D2]** Add `X-Content-Type-Options` and `X-Frame-Options` headers to `onSend` hook
18. **[D3]** Update `README.md` to document security model

---

## Post-Design Constitution Re-check

| Principle | Status |
|-----------|--------|
| §IV Test-First | Every implementation task (A2, A4, A5, A7, B2, B3, C2, C4, C5, D2) has a preceding test task |
| §V Coverage | Unit tests for both new modules; integration tests for all modified routes; security header test for all routes |
| §IX AI Usage | Security-critical new files (`pid-validator.ts`, `path-sandbox.ts`) flagged for explicit human review |
| §XI Documentation | D3 task covers README update |
| §XII Error Handling | All new 4xx responses use `{ error: ERROR_CODE, message, requestId }` — verified against §XII contract |

**Gate result**: PASS. Proceed to `/speckit.tasks`.
