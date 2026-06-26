<!-- source: argus-security-review — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/009-security-review/tasks.md -->
# Tasks: Security Review & Hardening

**Input**: Design documents from `/specs/009-security-review/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/security-hardening.md ✅

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Which user story this task belongs to (US1–US5)
- Exact file paths included in all descriptions

---

## Phase 1: Setup

**Purpose**: No new project or dependency setup required — this is a hardening PR on an existing TypeScript/Fastify project. The only structural addition is a new `backend/src/utils/` directory for `path-sandbox.ts`.

- [x] T001 Create directory `backend/src/utils/` (create placeholder if needed) and confirm `backend/tests/unit/` and `backend/tests/contract/` exist per plan structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Two new modules — `pid-validator.ts` and `path-sandbox.ts` — must exist before US1 and US4 can be implemented. Both are pure functions with no DB or external-process side effects, making them independently testable.

**⚠️ CRITICAL**: US1 (T007) and US4 (T015–T016) cannot begin until T003 and T004 are complete respectively.

- [x] T002 [P] Write unit tests for `pid-validator` covering: valid PID passes both checks, PID not in registry rejected, PID not in OS process list rejected, PID belongs to non-AI-tool process rejected, non-integer PID rejected — in `backend/tests/unit/pid-validator.test.ts` (new file; mock `psList` and `getSessionByPid` DB helper)
- [x] T003 [P] Write unit tests for `path-sandbox` covering: path within home dir allowed, path equal to boundary allowed, path outside home dir rejected, `../` traversal sequences resolved and rejected, Windows system paths (e.g. `C:\Windows`) rejected, boundary separator guard (`/home/user` does not allow `/home/userother`) — in `backend/tests/unit/path-sandbox.test.ts` (new file)
- [x] T004 Implement `pid-validator.ts` — export `validatePidOwnership(pid: number, sessionType: 'claude-code' | 'copilot-cli'): Promise<{ valid: boolean; reason?: 'not_in_registry' | 'process_not_found' | 'process_not_ai_tool' }>` using `psList` and a DB lookup by PID; allowlist: claude-code → `name/cmd.includes('claude')`, copilot-cli → `name/cmd.includes('gh') || cmd.includes('copilot')` — in `backend/src/services/pid-validator.ts` (new file)
- [x] T005 Implement `path-sandbox.ts` — export `isPathWithinBoundary(inputPath: string, allowedBoundaries: string[]): boolean` using `path.resolve()` for canonicalization and `resolved === boundary || resolved.startsWith(boundary + path.sep)` for boundary check — in `backend/src/utils/path-sandbox.ts` (new file)

**Checkpoint**: Run `npm test` in `backend/` — T002 and T003 tests must be green before proceeding.

---

## Phase 3: User Story 1 — Process Control Cannot Be Weaponized (Priority: P1) 🎯 MVP

**Goal**: Stop/interrupt requests that cannot verify PID ownership are rejected; hook payloads cannot overwrite an existing session's PID.

**Independent Test**: Send a stop request for a session whose PID does not pass the ownership check → expect 422/403. Send a hook payload with a `pid` field for a session that already has a different PID stored → expect 409.

- [x] T006 [P] [US1] Write contract tests for PID ownership validation in stop and interrupt routes: (a) session with no PID → 422 `PID_NOT_SET`, (b) session PID not found in OS process list → 422 `PID_NOT_FOUND`, (c) session PID belongs to non-AI-tool → 403 `PID_NOT_AI_TOOL`, (d) valid PID passes through — extend `backend/tests/contract/sessions.test.ts`
- [x] T007 [P] [US1] Write contract test for 409 conflict when hook payload includes a `pid` field that differs from the existing session's stored PID — create `backend/tests/contract/hooks.test.ts` (new file)
- [x] T008 [US1] Update `stopSession` and `interruptSession` in `backend/src/services/session-controller.ts` to call `validatePidOwnership(session.pid, session.type)` before issuing any signal; throw typed errors (`PID_NOT_SET`, `PID_NOT_FOUND`, `PID_NOT_AI_TOOL`) that the error handler maps to 422/403 responses
- [x] T009 [US1] Add 409 guard to `/hooks/claude` handler in `backend/src/api/routes/hooks.ts`: after UUID validation, if the incoming payload contains a `pid` field and the existing session for that `session_id` has a non-null `pid` that differs, return `409 { error: 'SESSION_PID_CONFLICT', message: 'Session already has an established PID', requestId }`

---

## Phase 4: User Story 2 — Hook Endpoint Rejects Malformed and Oversized Payloads (Priority: P1)

**Goal**: The `/hooks/claude` endpoint enforces a 64 KB body limit, validates `session_id` as UUID v4, and silently discards unrecognized `cwd` values (already implemented — test coverage added).

**Independent Test**: POST with (a) 10 MB body → 413, (b) `session_id: "../../etc/passwd"` → 400, (c) unrecognized `cwd` → 200 `{ ok: true }` with no watcher started.

- [x] T010 [P] [US2] Write contract tests for hook validation — extend `backend/tests/contract/hooks.test.ts`: (a) body > 64 KB → 413, (b) `session_id` not UUID v4 (traversal string, empty string, numeric, missing) → 400 `INVALID_SESSION_ID`, (c) valid UUID with unrecognized `cwd` → 200 with no side effects (mock detector to confirm `handleHookPayload` not called), (d) confirm FR-007 cwd registry check is exercised
- [x] T011 [US2] Add `{ bodyLimit: 64 * 1024 }` to the `app.post('/hooks/claude', ...)` route options in `backend/src/api/routes/hooks.ts`
- [x] T012 [US2] Add UUID v4 regex validation for `session_id` in the `/hooks/claude` handler (before calling the detector) in `backend/src/api/routes/hooks.ts`; return `400 { error: 'INVALID_SESSION_ID', message: 'session_id must be a valid UUID v4', requestId }` on mismatch

---

## Phase 5: User Story 3 — Shell Commands Use Safe APIs (Priority: P2)

**Goal**: Both `killProcess` and `interruptProcess` in `session-controller.ts` use `spawnSync` with an explicit args array on Windows — no shell string interpolation.

**Independent Test**: Code inspection and unit test confirm `execAsync` is absent from process control paths; `spawnSync('taskkill', ['/PID', String(pid), ...])` is present.

- [x] T013 [P] [US3] Write unit tests confirming `spawnSync` is used (not `exec`/`execAsync`) in `killProcess` and `interruptProcess` on Windows — extend `backend/tests/unit/session-controller.test.ts`; mock `spawnSync` and assert it is called with `['taskkill', ['/PID', expect.any(String), ...]]`
- [x] T014 [US3] Replace both `execAsync('taskkill /PID ${pid} /T /F')` and `execAsync('taskkill /PID ${pid}')` with `spawnSync('taskkill', ['/PID', String(pid), '/T', '/F'])` and `spawnSync('taskkill', ['/PID', String(pid)])` respectively in `backend/src/services/session-controller.ts`; remove `execAsync`/`promisify` imports if no longer used

---

## Phase 6: User Story 4 — Filesystem Routes Cannot Traverse to Sensitive Paths (Priority: P2)

**Goal**: All three path-accepting fs routes reject paths outside `homedir()` and registered repo paths; `findGitRepos` skips symlinks.

**Independent Test**: POST to `/api/v1/fs/scan-folder` with `path: "C:\\Windows\\System32"` → 403. GET `/api/v1/fs/browse?path=../../../../etc` → 403. `findGitRepos` returns without hanging when a symlink-to-parent is present in the test directory.

- [x] T015 [P] [US4] Write contract tests for path boundary enforcement — extend `backend/tests/contract/fs.test.ts`: (a) `/browse?path=<outside-home>` → 403 `PATH_OUTSIDE_BOUNDARY`, (b) `/scan?path=<traversal>` → 403, (c) `/scan-folder` with `path: "C:\\Windows\\System32"` → 403, (d) valid home subdir path → 200
- [x] T016 [US4] Apply `isPathWithinBoundary(input, [homedir(), ...getRepositories().map(r => r.path)])` to `/api/v1/fs/browse` and `/api/v1/fs/scan` GET routes in `backend/src/api/routes/fs.ts`; return `403 { error: 'PATH_OUTSIDE_BOUNDARY', message: 'Path is outside the allowed directory boundary', requestId: request.id }` on rejection
- [x] T017 [US4] Apply `isPathWithinBoundary` to `/api/v1/fs/scan-folder` POST route in `backend/src/api/routes/fs.ts` with same 403 response
- [x] T018 [US4] Fix `findGitRepos` in `backend/src/api/routes/fs.ts`: replace `statSync(fullPath).isDirectory()` with `lstatSync(fullPath)` followed by an `isSymbolicLink()` guard that skips symlink entries before recursing

---

## Phase 7: User Story 5 — Security Headers Protect the Local Web Interface (Priority: P3)

**Goal**: Every HTTP response includes `X-Content-Type-Options: nosniff` and `X-Frame-Options: DENY`; no `Server` version header is present.

**Independent Test**: Inspect response headers on health, sessions, hooks, and fs endpoints — confirm required headers present and `Server` header absent.

- [x] T019 [P] [US5] Write contract tests for security headers — create `backend/tests/contract/security-headers.test.ts` (new file): assert `X-Content-Type-Options: nosniff` and `X-Frame-Options: DENY` are present and `Server` header is absent on responses from `/health`, `/api/v1/sessions`, `/hooks/claude` (OPTIONS or GET), and `/api/v1/fs/browse`
- [x] T020 [US5] Add `reply.header('X-Content-Type-Options', 'nosniff')` and `reply.header('X-Frame-Options', 'DENY')` to the existing `onSend` hook in `backend/src/server.ts`

---

## Phase 8: Polish & Cross-Cutting Concerns

- [x] T021 Update `README.md` to document the security model: localhost-only binding, PID ownership validation, hook endpoint constraints (body limit, UUID validation), filesystem path boundary enforcement, and security headers (§XI requirement)

---

## Dependencies

```
T001
  └─ T002 [P], T003 [P]   (unit test files, independent)
       └─ T004 (impl pid-validator, after T002)
       └─ T005 (impl path-sandbox, after T003)
            └─ T006 [P], T007 [P]   (US1 tests, independent of each other)
                 └─ T008 (session-controller PID check, after T006 + T004)
                 └─ T009 (hooks 409 guard, after T007; same file as T011/T012 — sequential)
                      └─ T010 [P], T013 [P]   (US2 + US3 tests, independent)
                           └─ T011 (hooks bodyLimit, after T010, same file as T009)
                           └─ T012 (hooks UUID validation, after T011)
                           └─ T014 (session-controller spawnSync, after T013 + T008)
                                └─ T015 [P], T019 [P]   (US4 + US5 tests, independent)
                                     └─ T016 (fs browse/scan boundary, after T015 + T005)
                                     └─ T017 (fs scan-folder boundary, after T016)
                                     └─ T018 (fs symlink fix, after T017)
                                     └─ T020 (security headers, after T019)
                                          └─ T021 (README, final)
```

**Same-file sequential constraints** (cannot parallelize):
- `hooks.ts`: T009 → T011 → T012
- `session-controller.ts`: T008 → T014
- `fs.ts`: T016 → T017 → T018

---

## Parallel Execution Examples

**Sprint start (all independent)**:
```
T002 ∥ T003   (unit test scaffolds for both new modules)
```

**After T002/T003 complete**:
```
T004 ∥ T005   (implement pid-validator and path-sandbox independently)
```

**After T004/T005 complete (US1 + US4 start)**:
```
T006 ∥ T007 ∥ T015 ∥ T019   (all are test-only tasks on different files)
```

**After US1 tests complete (T006, T007)**:
```
T008 → T009   (sequential: same hooks.ts file)
T013 can start in parallel while T008/T009 are in progress (different file)
```

---

## Implementation Strategy

**MVP** (US1 + US2 — both P1): T001–T012. Delivers the two highest-severity fixes: PID injection prevention and hook endpoint hardening. These changes eliminate the direct process weaponization attack surface.

**Increment 2** (US3 + US4 — P2): T013–T018. Eliminates shell injection pattern and filesystem traversal. Safe to ship independently after MVP.

**Increment 3** (US5 + Polish — P3): T019–T021. Security headers and documentation. Lowest risk, can be deferred if timeline is tight.

---

## Summary

| Phase | User Story | Tasks | Priority |
|-------|-----------|-------|----------|
| Foundational | — | T001–T005 | — |
| Phase 3 | US1: Process Control Safety | T006–T009 | P1 |
| Phase 4 | US2: Hook Endpoint Validation | T010–T012 | P1 |
| Phase 5 | US3: Shell Command Safety | T013–T014 | P2 |
| Phase 6 | US4: Filesystem Path Safety | T015–T018 | P2 |
| Phase 7 | US5: Security Headers | T019–T020 | P3 |
| Polish | Cross-cutting | T021 | — |
| **Total** | | **21 tasks** | |

**Parallel opportunities identified**: 8 (T002∥T003, T004∥T005, T006∥T007∥T015∥T019, T010∥T013)

**Format validation**: All 21 tasks follow `- [ ] [ID] [P?] [Story?] Description with file path` ✅
