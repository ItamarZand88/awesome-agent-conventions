<!-- source: argus-session-dashboard — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/001-session-dashboard/tasks.md -->
# Tasks: Session Dashboard

**Branch**: `001-session-dashboard` | **Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)
**Input**: Design documents from `specs/001-session-dashboard/`

**Tests**: Included per constitution (Principles IV & V — Test-First, Testing Requirements).

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- **Test tasks**: Written FIRST; must FAIL before implementation begins

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize monorepo structure, tooling, and test runners. All Phase 1 tasks can run in parallel after T001.

- [X] T001 Create monorepo directory structure: `backend/`, `frontend/`, root `package.json` workspace config
- [X] T002 [P] Initialize backend `package.json` with TypeScript 5, Fastify 4, ws, better-sqlite3, chokidar, pino, js-yaml, ps-list at `backend/package.json`
- [X] T003 [P] Initialize frontend with Vite + React 18 + TypeScript: `frontend/package.json` and `frontend/vite.config.ts`
- [X] T004 [P] Configure backend `tsconfig.json` for Node 22, strict mode, ESM output at `backend/tsconfig.json`
- [X] T005 [P] Configure frontend `tsconfig.json` for Vite + React at `frontend/tsconfig.json`
- [X] T006 [P] Configure ESLint + Prettier for backend at `backend/.eslintrc.json` and `backend/.prettierrc`
- [X] T007 [P] Configure ESLint + Prettier for frontend at `frontend/.eslintrc.json` and `frontend/.prettierrc`
- [X] T008 [P] Configure Vitest for backend at `backend/vitest.config.ts` with coverage reporting
- [X] T009 [P] Configure Playwright for E2E tests at `playwright.config.ts` (targets `http://localhost:7411`)

**Checkpoint**: Project structure exists, all tooling configured. `npm install` runs clean across both workspaces.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure required by ALL user stories. No story work begins until this phase is complete.

**⚠️ CRITICAL**: These tasks BLOCK all user stories.

- [X] T010 Define TypeScript model interfaces: `Repository`, `Session`, `SessionOutput`, `ControlAction`, `ArgusConfig` at `backend/src/models/index.ts`
- [X] T011 [P] Implement `ArgusConfig` loader (read/write `~/.argus/config.json`, create with defaults if absent) at `backend/src/config/config-loader.ts`
- [X] T012 Implement SQLite schema (tables: `repositories`, `sessions`, `session_output`, `control_actions`) at `backend/src/db/schema.ts`
- [X] T013 Implement database connection, query helpers, and migration runner at `backend/src/db/database.ts`
- [X] T014 Implement Fastify server entry point bound to `127.0.0.1`, pino structured logging, graceful shutdown at `backend/src/server.ts`
- [X] T014b Implement Fastify `requestIdHeader` and inject `requestId` into all pino log entries; return `X-Request-Id` header in all error responses for failure traceability at `backend/src/server.ts`
- [X] T015 Implement WebSocket event dispatcher (register clients, broadcast typed events) at `backend/src/api/ws/event-dispatcher.ts`
- [X] T016 [P] Implement frontend WebSocket client with exponential backoff reconnection at `frontend/src/services/socket.ts`
- [X] T017 [P] Implement frontend REST API client with TanStack Query base configuration (queryClient, axios instance) at `frontend/src/services/api.ts`

**Checkpoint**: Server starts, connects to SQLite, serves WebSocket upgrades at `ws://localhost:7411/ws`. Frontend compiles and connects.

---

## Phase 3: User Story 1 — Repository & Session Overview (Priority: P1) 🎯 MVP

**Goal**: Developer opens Argus and sees all registered repositories with active session counts, updating in real time.

**Independent Test**: Register 2 repos, start Copilot CLI in one and Claude Code in the other. Open dashboard → both repos appear within 5s; sessions are labeled with correct type; no manual refresh needed (SC-001, SC-005).

### Tests for User Story 1

> **Write these tests FIRST. Verify they FAIL before writing any implementation.**

- [X] T018 [P] [US1] Write contract tests for `GET /api/v1/repositories`, `POST /api/v1/repositories`, `DELETE /api/v1/repositories/:id` at `backend/tests/contract/repositories.test.ts`
- [X] T019 [P] [US1] Write contract test for `GET /api/v1/sessions` (with `repositoryId`, `status`, `type` filters) at `backend/tests/contract/sessions.test.ts`
- [X] T020 [P] [US1] Write integration test for `CopilotCliDetector`: mock `~/.copilot/session-state/` directory with fixture files; assert sessions detected with correct PID, CWD, status at `backend/tests/integration/copilot-cli-detector.test.ts`
- [X] T021 [P] [US1] Write integration test for `ClaudeCodeDetector`: simulate hook POST payload; assert session record created with correct repo association at `backend/tests/integration/claude-code-detector.test.ts`

### Implementation for User Story 1

- [X] T022 [P] [US1] Implement `RepositoryScanner` service: scan configured directories for `.git` repos, persist to SQLite, detect new/removed repos at `backend/src/services/repository-scanner.ts`
- [X] T023 [P] [US1] Implement `CopilotCliDetector`: scan `~/.copilot/session-state/`, parse `inuse.{PID}.lock` + `workspace.yaml`, map CWD to registered repo. **Validate each PID against running processes via `ps-list`** — if process is gone but lock file exists, mark session as `ended` (stale lock) at `backend/src/services/copilot-cli-detector.ts`
- [X] T024 [P] [US1] Implement `ClaudeCodeDetector`: inject hooks into `~/.claude/settings.json`, receive `POST /hooks/claude` payloads, create/update session records at `backend/src/services/claude-code-detector.ts`
- [X] T025 [US1] Implement `SessionMonitor` orchestrator: coordinate detectors, manage session lifecycle, emit typed domain events at `backend/src/services/session-monitor.ts`
- [X] T026 [US1] Implement `GET`, `POST`, `DELETE /api/v1/repositories` route handlers with input validation at `backend/src/api/routes/repositories.ts`
- [X] T027 [US1] Implement `GET /api/v1/sessions` route handler with filter support at `backend/src/api/routes/sessions.ts`
- [X] T028 [US1] Implement `POST /hooks/claude` event receiver route at `backend/src/api/routes/hooks.ts`
- [X] T029 [US1] Wire `repository.added`, `repository.removed`, `session.created`, `session.updated`, `session.ended` events through `event-dispatcher.ts` at `backend/src/api/ws/event-dispatcher.ts`
- [X] T030 [P] [US1] Implement frontend `DashboardPage` with repository list, session count badges, and loading states at `frontend/src/pages/DashboardPage.tsx`
- [X] T031 [P] [US1] Implement frontend `SessionCard` component: session type badge, status indicator, `startedAt` timestamp at `frontend/src/components/SessionCard/SessionCard.tsx`
- [X] T032 [US1] Connect `session.created`, `session.updated`, `session.ended`, `repository.added`, `repository.removed` WebSocket events to `DashboardPage` live state at `frontend/src/services/socket.ts` *(extends T016 — must be implemented after T016 is complete)*

**Checkpoint**: US1 fully functional. Open dashboard, see repos and sessions, watch live updates without refresh.

---

## Phase 4: User Story 2 — Session State & Results (Priority: P1)

**Goal**: Select a session and see its current state, activity, and output stream updating in real time.

**Independent Test**: Start an active Copilot CLI session. Open its detail view. Type a prompt in the terminal. Confirm new output events appear in the dashboard within 2 seconds (SC-002, SC-003).

### Tests for User Story 2

> **Write these tests FIRST. Verify they FAIL before writing any implementation.**

- [X] T033 [P] [US2] Write contract tests for `GET /api/v1/sessions/:id` and `GET /api/v1/sessions/:id/output` (pagination with `limit`, `before` params) at `backend/tests/contract/sessions.test.ts`
- [X] T034 [P] [US2] Write unit test for `events.jsonl` parser: assert each Copilot CLI event type maps to correct `SessionOutput.type` at `backend/tests/unit/events-parser.test.ts`
- [X] T035 [P] [US2] Write integration test for `OutputStore`: persist 200 output records, assert paginated reads and size-limit pruning (oldest removed when limit exceeded) at `backend/tests/integration/output-store.test.ts`

### Implementation for User Story 2

- [X] T036 [US2] Implement `OutputStore` service: persist `SessionOutput` to SQLite, paginated reads, enforce per-session size limit with oldest-first pruning at `backend/src/services/output-store.ts`
- [X] T037 [P] [US2] Implement `events.jsonl` event parser: map Copilot CLI event types (`tool.execution_start`, `assistant.message`, etc.) to `SessionOutput` records at `backend/src/services/events-parser.ts`
- [X] T038 [US2] Add `chokidar` file watcher to `CopilotCliDetector` to tail `events.jsonl` on active sessions and feed `OutputStore` at `backend/src/services/copilot-cli-detector.ts`
- [X] T039 [US2] Add `GET /api/v1/sessions/:id` and `GET /api/v1/sessions/:id/output` route handlers to `backend/src/api/routes/sessions.ts`
- [X] T040 [US2] Wire `session.output` WebSocket broadcast in `event-dispatcher.ts` triggered by `OutputStore` writes at `backend/src/api/ws/event-dispatcher.ts`
- [X] T041 [P] [US2] Implement frontend `SessionPage`: session metadata header (type, status, PID, duration), navigation back to dashboard at `frontend/src/pages/SessionPage.tsx`
- [X] T042 [P] [US2] Implement frontend `SessionDetail` component: virtualized scrollable output stream with type labels and timestamps at `frontend/src/components/SessionDetail/SessionDetail.tsx`
- [X] T043 [US2] Connect `session.output` WebSocket events to live-append `SessionDetail` feed; integrate TanStack Query for initial output load with pagination at `frontend/src/services/socket.ts` *(extends T016 and T032 — must be implemented after T032 is complete)*

**Checkpoint**: US2 fully functional. Session detail view shows live output stream, status, and paginated history.

---

## Phase 5: User Story 3 — Session Control (Priority: P2)

**Goal**: Stop a running session or send it a prompt directly from the dashboard.

**Independent Test**: Open detail view for an active Copilot CLI session. Click Stop → confirm session terminates within 5s and status updates to `ended` (SC-004). Attempt stop on an already-ended session → error message shown.

### Tests for User Story 3

> **Write these tests FIRST. Verify they FAIL before writing any implementation.**

- [X] T044 [P] [US3] Write contract tests for `POST /api/v1/sessions/:id/stop` (202, 404, 409) at `backend/tests/contract/sessions.test.ts`
- [X] T045 [P] [US3] Write contract tests for `POST /api/v1/sessions/:id/send` (202, 404, 409, 501 for copilot-cli) at `backend/tests/contract/sessions.test.ts`
- [X] T046 [P] [US3] Write unit test for `SessionController`: mock `process.kill` and `exec('taskkill')`; assert `ControlAction` records created with correct status transitions at `backend/tests/unit/session-controller.test.ts`

### Implementation for User Story 3

- [X] T047 [US3] Implement `SessionController`: stop via `process.kill(pid, 'SIGTERM')` (Unix) or `taskkill /PID {pid} /T` (Windows); persist `ControlAction` records at `backend/src/services/session-controller.ts`
- [X] T048 [US3] Implement `POST /api/v1/sessions/:id/stop` route handler using `SessionController` at `backend/src/api/routes/sessions.ts`
- [X] T049 [US3] Implement `POST /api/v1/sessions/:id/send` route handler: `501` for `copilot-cli` with message "Prompt injection not supported for Copilot CLI in v1", `202` accepted for `claude-code`; persist `ControlAction` at `backend/src/api/routes/sessions.ts`
- [X] T050 [US3] Wire `action.updated` WebSocket broadcast in `event-dispatcher.ts` triggered by `ControlAction` status changes at `backend/src/api/ws/event-dispatcher.ts`
- [X] T051 [P] [US3] Implement frontend `ControlPanel` component: Stop button with confirmation dialog, Send Prompt form with disabled state for `copilot-cli` at `frontend/src/components/ControlPanel/ControlPanel.tsx`
- [X] T052 [US3] Integrate `ControlPanel` into `SessionPage`; wire TanStack Query mutations to `POST /api/sessions/:id/stop` and `POST /api/sessions/:id/send` at `frontend/src/pages/SessionPage.tsx`

**Checkpoint**: US3 fully functional. Can stop any active session from the dashboard; send-prompt works for Claude Code, shows clear unsupported message for Copilot CLI.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Health, resilience, retention, empty states, and acceptance validation.

- [X] T053 [P] Implement `GET /api/health` route (status, version, uptime) at `backend/src/api/routes/health.ts`
- [X] T053b [P] Implement `GET /api/metrics` route (counters: `sessions_active`, `sessions_ended`, `output_records_written`, `control_actions_total`) at `backend/src/api/routes/metrics.ts`
- [X] T053c [P] Configure `@fastify/swagger` and `@fastify/swagger-ui` to auto-generate OpenAPI spec from route schemas; serve at `GET /api/docs` at `backend/src/server.ts`
- [X] T054 [P] Implement global Fastify error handler middleware with pino-structured error logging at `backend/src/server.ts`
- [X] T055 Implement background pruning job: purge expired sessions (past `expiresAt`) and over-limit output records on a configurable interval at `backend/src/services/pruning-job.ts`
- [X] T056 [P] Add frontend empty-state screens (no repos registered, no sessions on a repo, loading skeleton) at `frontend/src/components/EmptyState/EmptyState.tsx`
- [X] T057 [P] Write Playwright E2E test for SC-001: register 2 repos with active sessions, open dashboard, assert both visible within 5s at `frontend/tests/e2e/sc-001-repo-overview.spec.ts`
- [X] T058 [P] Write Playwright E2E test for SC-002: observe active session, trigger output, assert it appears in dashboard within 2s at `frontend/tests/e2e/sc-002-real-time-output.spec.ts`
- [X] T059 [P] Write Playwright E2E test for SC-004: click Stop on active session, assert status changes to `ended` within 5s at `frontend/tests/e2e/sc-004-stop-session.spec.ts`
- [X] T060 Run all quickstart.md acceptance scenarios manually and confirm SC-001 through SC-005 pass
  > **Note**: T060 requires manual validation with live sessions. See quickstart.md for steps.

### Addendum: Remove axios dependency

- [X] T061 Remove `axios` from `frontend/package.json` and replace all usages in `frontend/src/services/api.ts` with native `fetch`; ensure all existing TypeScript types are preserved and no behaviour changes

### Addendum: Test isolation

- [X] T062 Fix integration and contract tests to use an isolated test DB (via `ARGUS_DB_PATH` env var) instead of `~/.argus/argus.db`; add afterAll cleanup in `output-store.test.ts` at `backend/tests/integration/output-store.test.ts`, `backend/src/db/database.ts`, `backend/vitest.config.ts`

### Addendum: Folder navigation UX for Add Repository

- [X] T063 Add `GET /api/v1/fs/browse` route: accepts `?path=` query param (defaults to `homedir()`), returns `{ current: string, parent: string|null, entries: { name, path, isGitRepo }[] }` listing immediate subdirectories only at `backend/src/api/routes/fs.ts`; register in `backend/src/server.ts`
- [X] T064 [P] Create `frontend/src/components/FolderBrowser/FolderBrowser.tsx`: shows current path as breadcrumb, lists subdirs (git repos highlighted with a badge), click to navigate into subdir, "Select" button emits chosen path to parent via `onSelect(path: string)` callback; uses `GET /api/v1/fs/browse`
- [X] T065 Wire `FolderBrowser` into the Add Repository modal in `frontend/src/pages/DashboardPage.tsx`: replace text input with FolderBrowser; keep manual path input as a fallback below the browser; pre-populate input when user clicks Select

### Addendum: Scan parent folder for git repositories

- [X] T067 Add `GET /api/v1/fs/scan` route: accepts `?path=` query param, walks immediate subdirectories (non-recursive) checking for `.git` folder, returns `{ scannedPath: string, repos: { name: string, path: string }[] }`; register handler in `backend/src/api/routes/fs.ts` alongside T063's browse route
- [X] T068 Add "Scan Folder" tab to the Add Repository modal in `frontend/src/pages/DashboardPage.tsx`: user picks a parent folder via `FolderBrowser` (T064), clicks "Scan", modal shows a checklist of discovered git repos, user selects any subset, "Add Selected" calls `POST /api/v1/repositories` for each; existing single-repo tab unchanged

### Addendum: Detect pre-existing sessions on startup

- [X] T066 On startup, scan `~/.claude/projects/` for Claude Code sessions that were already running before Argus started: for each project subdir check for active `claude` process via ps-list, map `cwd` to a registered repo, and upsert a `claude-code` session with `status: active`; add this scan to `ClaudeCodeDetector` as `scanExistingSessions()` called from `SessionMonitor.start()` at `backend/src/services/claude-code-detector.ts`

### Addendum: Bug — session not marked ended when process stops

- [X] T069 Fix `SessionMonitor.runScan()` in `backend/src/services/session-monitor.ts` to detect sessions that were active but are no longer returned by `CopilotCliDetector.scan()` (e.g., because the session directory was cleaned up on process exit): after each scan, diff the set of currently-returned active session IDs against a `Map<string, Session>` of previously-active sessions; for any session that has disappeared or now has `status: 'ended'`, call `updateSessionStatus(id, 'ended', endedAt)` in `backend/src/db/database.ts` and emit `session.ended`; add `updateSessionStatus` export to `database.ts` if not present

### Addendum: Bug — Copilot CLI session not detected (path mismatch)

- [X] T070 Fix `getRepositoryByPath` in `backend/src/db/database.ts` and `CopilotCliDetector.processSessionDir` in `backend/src/services/copilot-cli-detector.ts` to handle path variations on Windows (case, trailing separator, forward vs backslash): normalize both the registered repo path and the `workspace.cwd` to lowercase with `path.normalize()` before comparing; update `getRepositoryByPath` to perform a case-insensitive lookup using `LOWER(path) = LOWER(?)` so sessions whose `cwd` differs only in case or separators are correctly matched to their repo

### Addendum: Fix README

- [X] T071 Rewrite `README.md` at repo root to be crisp, concise and accurate: include a one-line description, what Argus does (monitors Copilot CLI + Claude Code sessions, real-time output, remote stop), how to run it (`npm run dev` from repo root + `npm run build` in frontend/), how to add a repo, key features list (folder browser, scan-folder bulk-add, pre-existing session detection), and a brief tech stack note (Node/Fastify backend, React frontend, SQLite); remove all placeholder text ("Coming soon", etc.)

### Addendum: Bug — stale active sessions persist across restarts

- [X] T072 On startup, reconcile stale sessions in `SessionMonitor.start()` at `backend/src/services/session-monitor.ts`: query `getSessions({ status: 'active' })` from the DB, fetch current running PIDs via ps-list, and call `updateSessionStatus(id, 'ended', now)` for any session whose `pid` is not in the running PID set (or whose `pid` is null); this must run before the first `runScan()` so the frontend never sees stale `active` sessions

### Addendum: Bug — Copilot CLI sessions not detected (js-yaml Date coercion)

- [X] T073 Fix `CopilotCliDetector.processSessionDir` in `backend/src/services/copilot-cli-detector.ts`: `js-yaml` silently coerces ISO timestamp strings (e.g. `created_at`, `updated_at`) into JavaScript `Date` objects; passing these to `upsertSession` throws "SQLite3 can only bind numbers, strings, bigints, buffers, and null" which is caught and swallowed, making every `processSessionDir` return `null`; fix by converting date fields to ISO strings when constructing the Session: `startedAt: workspace.created_at ? new Date(workspace.created_at as string | Date).toISOString() : new Date().toISOString()` and same for `endedAt`/`lastActivityAt`; update `WorkspaceYaml` interface to type these fields as `string | Date` to make the coercion visible

### Addendum: Bug — Claude Code sessions marked ended on server restart

- [X] T074 Fix `reconcileStaleSessions()` in `backend/src/services/session-monitor.ts`: the condition `if (!session.pid || ...)` evaluates `!null` as `true`, so every Claude Code session created via hooks (which always have `pid: null`) is incorrectly marked `ended` on every server restart; fix by changing the condition to `if (session.pid != null && !runningPids.has(session.pid))` so sessions without a known PID are skipped — their lifecycle is managed by hooks, not by PID presence

### Addendum: Bug — Claude Code sessions not re-detected on restart (scanExistingSessions broken on Windows)

- [X] T075 Fix `ClaudeCodeDetector.scanExistingSessions()` in `backend/src/services/claude-code-detector.ts`: two bugs: (1) it requires `psList` to return a process `cwd` to match the project path, but on Windows psList never returns `cwd`, so `matchedProcess` is always `undefined` and the entire method is a no-op; (2) even if a process is matched, it creates a new `claude-startup-{repo.id}-{pid}` session rather than re-activating an existing `ended` session — so already-ended hook sessions (e.g. incorrectly ended by the pre-T074 bug) are never restored. Fix: (a) remove the per-process `cwd` match — instead check if ANY `claude` process is running at all (`processes.some(p => p.name.toLowerCase().includes('claude'))`); (b) for each project directory matching a registered repo, if no `active` claude-code session exists for that repo: find the most recently ended claude-code session and call `updateSessionStatus(id, 'active', null)` to re-activate it, or create a new startup session if none exists. Import `getSessions` and `updateSessionStatus` from `../db/database.js`

### Addendum: Feature — Remove Repository

- [X] T076 Add cascade delete for sessions and session output when a repository is removed: update `deleteRepository` in `backend/src/db/database.ts` to first `DELETE FROM session_output WHERE session_id IN (SELECT id FROM sessions WHERE repository_id = ?)`, then `DELETE FROM sessions WHERE repository_id = ?`, then `DELETE FROM repositories WHERE id = ?`; this ensures no orphaned session or output records remain after a repo is removed
- [X] T077 Add Claude hook cleanup on repository removal: add a `removeHooksForRepo(repoPath: string)` method to `ClaudeCodeDetector` in `backend/src/services/claude-code-detector.ts` that reads `~/.claude/settings.json`, removes any hook entries whose `cwd` or script arguments reference the given repo path, and writes the file back; call this method from the `DELETE /api/v1/repositories/:id` handler in `backend/src/api/routes/repositories.ts` before calling `deleteRepository`
- [X] T078 Add "Remove" button to each repository card in `frontend/src/pages/DashboardPage.tsx`: render a small remove/trash icon button on the repo card header; clicking it shows a confirmation dialog ("Remove [repo name]? This will also delete all associated sessions."); on confirm, call the existing `removeRepository(id)` from `frontend/src/services/api.ts` (already implemented but never used), handle loading and error states, and close the dialog on success

### Addendum: Feature — Native OS Folder Picker

Replace the custom `FolderBrowser` web component (hard to navigate, poor UX) with a native OS folder selection dialog triggered via a backend endpoint.

- [X] T079 Add `POST /api/v1/fs/pick-folder` endpoint to `backend/src/api/routes/fs.ts`: spawn a platform-appropriate native folder picker dialog using `child_process.spawnSync` — on Windows use PowerShell `Add-Type -AssemblyName System.Windows.Forms; $d = New-Object System.Windows.Forms.FolderBrowserDialog; $d.ShowNewFolderButton = $true; if ($d.ShowDialog() -eq 'OK') { $d.SelectedPath }`, on macOS use `osascript -e 'POSIX path of (choose folder)'`, on Linux use `zenity --file-selection --directory`; wait for the subprocess to exit and return `{ path: string | null }` (null if user cancelled or dialog unavailable); if the platform command is not found, return `{ path: null, error: "not_supported" }` gracefully without throwing
- [X] T080 [P] Replace `FolderBrowser` component usage in `frontend/src/pages/DashboardPage.tsx` with a single "Browse…" button that calls `POST /api/v1/fs/pick-folder` via a new `pickFolder()` function in `frontend/src/services/api.ts`; on success, populate the path input with the returned path; on `null` result (user cancelled), do nothing; on error, show a small inline message "Folder picker not available — enter path manually"; remove all `showBrowser`, `showScanBrowser` state and `FolderBrowser` imports from `DashboardPage.tsx`; keep the manual text input as-is for fallback

### Addendum: Feature — Simplify Add Repository UX

Remove all modal complexity (tabs, scan folder, manual path input, FolderBrowser tree). "Add Repository" should directly invoke the native OS folder picker and register the selected path — zero intermediate UI.

- [ ] T081 Simplify "Add Repository" in `frontend/src/pages/DashboardPage.tsx`: clicking "Add Repository" calls `pickFolder()` directly (no modal); on a path being returned, immediately call `addRepository(path)` and invalidate queries; on cancel (null), do nothing; on error, show a brief inline toast/banner at the top of the dashboard; delete all modal state (`showAddModal`, `addTab`, `newRepoPath`, `adding`, `addError`, `pickingFolder`, `scanPath`, `scannedRepos`, `scanning`, `removeConfirmId` stays), all modal JSX, the `ScannedRepo` interface, `handleAddRepo`, `handleBrowse`, `handleBrowseForScan`, `handleScan`, `handleAddSelected`, `closeModal`; delete unused imports (`apiFetch`); also delete `frontend/src/components/FolderBrowser/FolderBrowser.tsx` and `frontend/src/components/FolderBrowser/index.ts` entirely since they are no longer used anywhere

### Addendum: Bug — model not detected for Claude Code sessions

- [X] T082 Fix `readNewJsonlLines` in `backend/src/services/claude-code-detector.ts`: the `updateModel` boolean parameter is `false` for all incremental file-change reads (chokidar `change` event calls `this.readNewJsonlLines(sessionId, jsonlPath, false)`), so model extraction is never attempted on new lines; if the initial load had no assistant entries yet (JSONL had only user messages or was empty at the time `watchJsonlFile` was called), the model stays `null` forever; fix by removing the `updateModel` parameter and instead computing `let needsModel = !(getSession(sessionId)?.model)` at the start of each call so model extraction runs whenever the session still lacks a model, and stop once found by setting `needsModel = false`; update both call sites to drop the boolean argument

### Addendum: Bug — Claude Code sessions not appearing as active on dashboard

- [ ] T083 Fix `handleHookPayload` in `backend/src/services/claude-code-detector.ts`: when a Claude Code hook fires (`SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`), the method calls `upsertSession(session)` to write to the DB but emits **no WebSocket event**; `SessionMonitor.runScan()` only iterates `CopilotCliDetector.scan()` results so Claude Code sessions are never included in the broadcast loop; the frontend's TanStack Query cache is never invalidated so the dashboard never updates; fix by importing `broadcast` from `../api/ws/event-dispatcher.js` (already imported for model updates) and calling `broadcast({ type: isNew ? 'session.created' : 'session.updated', timestamp: now, data: session })` immediately after `upsertSession` in `handleHookPayload`, where `isNew = !existing`; similarly broadcast `session.updated` (or `session.created` for new startup sessions) from `scanExistingSessions` after each `upsertSession` call so reactivated sessions appear immediately on startup

### Addendum: Bug — timestamp displays in hardcoded PST instead of browser timezone

- [X] T084 Fix `formatTime` in `frontend/src/components/SessionDetail/SessionDetail.tsx`: T021 incorrectly hardcoded `timeZone: 'America/Los_Angeles'` — all users see PST regardless of their local timezone; fix by removing the explicit `timeZone` option and passing `undefined` as the locale so `toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit', second: '2-digit' })` uses the browser's detected local timezone automatically

### Addendum: Bug — Copilot CLI tool events show raw JSON in output stream

- [X] T085 Fix `parseJsonlLine` in `backend/src/services/events-parser.ts` line 36: when a Copilot CLI event has no `content` field (e.g. `tool.execution_start`, `tool.execution_complete`, `session.start`), the fallback `JSON.stringify(event)` dumps the entire raw event object into `content`; the frontend renders this as unreadable JSON; fix by replacing the fallback with a helper that strips fields already shown elsewhere (`type`, `timestamp`, `tool_name`, `content`) from the event, then JSON.stringifies only the remaining meaningful fields — if no remaining fields exist, use an empty string; this ensures tool parameter/result data is shown without the redundant metadata clutter

### Addendum: Bug — Copilot CLI sessions never show model name

- [X] T086 Fix model detection for Copilot CLI sessions — three problems: (1) `processSessionDir` in `backend/src/services/copilot-cli-detector.ts` always sets `model: null` with no attempt to read the model from events.jsonl; (2) `upsertSession` in `backend/src/db/database.ts` uses `model = excluded.model` in the ON CONFLICT clause which overwrites any previously-detected model with null on every scan cycle — fix by changing to `model = COALESCE(excluded.model, model)` so a non-null model is never clobbered; (3) `readNewLines` in `copilot-cli-detector.ts` parses output events but never extracts the model; fix by: adding `parseModelFromEvent(line: string): string | null` to `events-parser.ts` that returns `event.model` (string) when `event.type === 'assistant.message'` and the field is a string; adding an `extractModelFromEventsFile(path: string): string | null` helper in the detector that reads the file and returns the first model found via `parseModelFromEvent`; calling `extractModelFromEventsFile` in `processSessionDir` and passing the result as `model` instead of `null`; and in `readNewLines`, scanning new lines for a model and calling `upsertSession` with the found model if the session currently has none

### Addendum: Bug — send prompt keystrokes to copilot-cli PTY work inconsistently

- [X] T116 Fix `backend/src/cli/launch.ts` `onSendPrompt` callback for copilot-cli: the Win32 input sequence loop calls `process.stdin.push()` for every character synchronously in a single event-loop tick. The Copilot CLI PTY reads these events and drops or merges them when they all arrive at once. Adding log lines (which have I/O overhead) incidentally creates inter-character timing gaps that make it work, revealing a race. Fix: (1) change `PromptCallback` in `backend/src/cli/argus-launch-client.ts` from `() => void` to `() => void | Promise<void>` to allow async callbacks; (2) make the `onSendPrompt` callback in `launch.ts` async; (3) add a `const KEYSTROKE_DELAY_MS = 10` constant and `await` a `setTimeout`-based delay of that duration after each character's key-down/key-up pair is pushed, so characters are delivered across separate event-loop ticks mimicking real keystroke timing.

### Addendum: Bug — Copilot CLI not detected on Ubuntu

- [ ] T117 Fix Copilot CLI availability and launch command resolution on Linux in `backend/src/api/routes/tools.ts` and `backend/src/launch-pty/launch-command-resolver.ts`: the dashboard's `/api/v1/tools` route only checks `which copilot`, but Ubuntu installs GitHub Copilot CLI as the `gh copilot` subcommand, so Argus reports `copilot: false` and hides Launch Copilot even when the CLI is installed; update the tools route to treat either a standalone `copilot` binary or a working `gh copilot --help` subcommand as installed, build `copilotCmd` from the detected command form, and update the launch command resolver so `node .../launch.js gh copilot ...` is classified as a `copilot-cli` session; add regression coverage proving `/api/v1/tools` and launch-terminal both work when only `gh copilot` is available

### Addendum: Bug — tool install status stays stale after install

- [X] T118 Fix installed-tool detection for the launch menu in `backend/src/api/routes/tools.ts` and `frontend/src/components/LaunchDropdown/LaunchDropdown.tsx`: `/api/v1/tools` only trusts the backend process PATH from startup, so a Copilot CLI installed later at `~/.local/bin/copilot` is invisible until the server restarts; `LaunchDropdown` then caches that false result for the lifetime of the page (`staleTime: 60_000`, `refetchOnWindowFocus: false`), so the menu keeps showing "No supported tools installed" even after install. Fix by making `tools.ts` fall back to the Linux user-local binary path and emit the detected absolute command, updating `backend/src/launch-pty/launch-command-resolver.ts` to classify absolute copilot paths as `copilot-cli`, and refreshing `/api/v1/tools` whenever the menu opens; add regression coverage in `backend/tests/unit/tools-launch-id.test.ts`, `backend/tests/launch-command-resolver.test.ts`, and `frontend/src/__tests__/LaunchDropdown.test.tsx`

**Checkpoint**: All acceptance criteria met. `npm test` passes. E2E suite green.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 completion — **BLOCKS all user stories**
- **Phase 3 (US1)**: Depends on Phase 2 — can start once foundational is complete
- **Phase 4 (US2)**: Depends on Phase 2 + T036 output store — builds on US1 session records
- **Phase 5 (US3)**: Depends on Phase 2 + US1 session detection (T025) — needs active sessions to control
- **Phase 6 (Polish)**: Depends on all desired user stories complete

### User Story Dependencies

| Story | Depends On | Notes |
|---|---|---|
| US1 (P1) | Phase 2 complete | Fully independent — delivers repo + session listing |
| US2 (P1) | Phase 2 + T025 (SessionMonitor) | Needs session records to display output for |
| US3 (P2) | Phase 2 + T025 (SessionMonitor) | Needs session records to control |

US2 and US3 can proceed in parallel once US1's SessionMonitor (T025) is complete.

### Within Each User Story

1. Tests written and **FAIL** verified before implementation begins
2. Models / services before route handlers
3. Route handlers before frontend pages
4. Core implementation before WebSocket integration
5. Story complete and checkpoint validated before moving on

### Parallel Opportunities

- All Phase 1 tasks after T001 can run in parallel
- T018–T021 (US1 tests) all run in parallel
- T022–T024 (US1 detectors) all run in parallel
- T030–T031 (US1 frontend) run in parallel
- T033–T035 (US2 tests) all run in parallel
- T041–T042 (US2 frontend) run in parallel
- T044–T046 (US3 tests) all run in parallel
- T053–T059 (Polish) mostly run in parallel

---

## Parallel Example: User Story 1

```bash
# Run all US1 tests in parallel:
Task T018: Contract tests for /api/repositories
Task T019: Contract test for GET /api/sessions
Task T020: Integration test for CopilotCliDetector
Task T021: Integration test for ClaudeCodeDetector

# Run all US1 detectors in parallel (after tests written):
Task T022: RepositoryScanner service
Task T023: CopilotCliDetector service
Task T024: ClaudeCodeDetector service
```

## Parallel Example: User Story 2

```bash
# Run all US2 tests in parallel:
Task T033: Contract tests for /api/sessions/:id and output
Task T034: Unit test for events.jsonl parser
Task T035: Integration test for OutputStore

# Run in parallel after tests:
Task T037: events.jsonl parser
Task T041: SessionPage frontend
Task T042: SessionDetail component
```

---

## Implementation Strategy

### MVP First (User Story 1 + 2 — full monitoring, no control)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (**CRITICAL**)
3. Complete Phase 3: User Story 1 → **STOP & VALIDATE**: repos and sessions appear on dashboard
4. Complete Phase 4: User Story 2 → **STOP & VALIDATE**: real-time output visible in detail view
5. Ship MVP: full read-only monitoring capability

### Full Feature (add control)

6. Complete Phase 5: User Story 3 → **STOP & VALIDATE**: stop session from dashboard
7. Complete Phase 6: Polish → run quickstart.md, confirm SC-001–SC-005

### Incremental Delivery

Each phase checkpoint delivers independently demonstrable value:
- After Phase 3: "I can see all my sessions at a glance"
- After Phase 4: "I can watch any session's output live"
- After Phase 5: "I can stop sessions without leaving the dashboard"

---

## Notes

- `[P]` tasks operate on different files — safe to parallelize
- `[Story]` label maps each task to its user story for traceability
- Constitution principle IV (Test-First): test tasks precede implementation in every story phase
- Commit after each completed checkpoint or logical group of tasks
- On Windows, use `taskkill /PID {pid} /T` for session stop; `process.kill` on macOS/Linux
- Claude Code `send-prompt` returns `501 Not Implemented` for `copilot-cli` sessions — UI must show "Not supported for Copilot CLI in v1"
- Hook injection modifies `~/.claude/settings.json` — must be idempotent (don't duplicate hooks on restart)
- All versioned REST routes use the `/api/v1/` prefix; `/api/health`, `/api/metrics`, `/api/docs`, and `/hooks/claude` are unversioned
- `frontend/src/services/socket.ts` is built incrementally across 3 phases: T016 (base) → T032 (US1 handlers) → T043 (US2 handlers). Each task MUST complete before the next begins.
- VS Code GitHub Copilot extension detection is **out of scope for v1**; `copilot-vscode` type is reserved in constitution but not implemented. Post-v1 work item.

### Addendum: Bug  Copilot CLI events use nested data object, not flat fields

- [X] T088 Fix vents-parser.ts to read content from vent.data: real Copilot CLI events nest ALL payload under vent.data (not flat top-level fields). vent.content is always undefined, causing xtractContent() to fall back to serializing data, id, parentId as raw JSON. Also vent.tool_name is always undefined (real field is vent.data.toolName). Fix: (1) Update JsonlEvent to add data?: Record<string, unknown>; (2) In xtractContent, check data.content (string) first for messages, use data.arguments for 	ool.execution_start, use data.result.content for 	ool.execution_complete; (3) Update 	oolName extraction to use vent.data?.toolName; (4) Update parseModelFromEvent to also check vent.data?.model (model appears on 	ool.execution_complete events in real CLI output)
### Addendum: Bug  Claude Code session ID mismatch causes phantom session on each command

### Addendum: Bug — Claude Code Stop hook incorrectly introduced idle status instead of reusing active/ended like Copilot CLI

- [X] T092 Fix `backend/src/services/claude-code-detector.ts` `handleHookPayload`: T090 replaced `status: 'ended'` on Stop with `status: 'idle'`, but `idle` is a new intermediate status that doesn't exist in Copilot CLI's model and duplicates what the frontend already handles time-based via `isInactive()` (20-min `lastActivityAt` threshold). The UI shows "resting" (moon icon) for any non-ended session whose `lastActivityAt` is >20 min old — no backend status change needed. Fix: remove the `if (hook_event_name === 'Stop')` special branch entirely; collapse to a single path that sets `session.status = 'active'` and `session.lastActivityAt = now` for ALL hook events including Stop. Also update `reconcileClaudeCodeSessions()` and `reconcileStaleSessions()` in `session-monitor.ts` to remove the `idle` queries — only `active` Claude Code sessions need liveness checks. Update the T090 regression tests in `claude-code-detector-scan.test.ts` that now incorrectly assert `Stop → idle` to assert `Stop → active` instead.

### Addendum: Bug — Claude Code sessions not marked ended when process exits while Argus is running

- [X] T091 Fix `backend/src/services/session-monitor.ts`: Three compounding problems prevent Claude Code sessions from ever being marked ended: (1) `reconcileStaleSessions()` only runs once at startup — there is no periodic liveness check while Argus is running; (2) it only queries `status: 'active'` sessions — after T090, sessions go `idle` on Stop hook so they are invisible to this check even at startup; (3) hook-created sessions have `pid: null`, so the PID-based guard (`session.pid != null`) never fires for them. Fix: (a) in `reconcileStaleSessions()`, also fetch and process `idle` sessions alongside `active` ones (replace the single `getSessions({ status: 'active' })` call with two calls merged); (b) add a new private `reconcileClaudeCodeSessions()` method that fetches all `active`+`idle` Claude Code sessions, calls `psList()`, ends any with a known dead PID, and also ends all null-PID Claude Code sessions if no `claude` process is running at all; (c) call `reconcileClaudeCodeSessions()` from `runScan()` so it runs every 5 seconds; (d) emit `session.ended` for every session ended in (b) so the WebSocket broadcast fires and the frontend updates immediately.

### Addendum: Bug — Claude Code session transitions to ended after every response instead of only on exit

- [X] T090 Fix handleHookPayload in `backend/src/services/claude-code-detector.ts`: the `Stop` hook event fires at the end of every AI response turn — it does NOT mean the session has exited. The current code sets `status: 'ended'` on `Stop`, causing the session card to show "ended" after every reply. Session end is already handled by `reconcileStaleSessions()` via PID check on startup, and by the Copilot CLI scan loop for CLI sessions. Fix: in the `if (hook_event_name === 'Stop')` branch, set `status: 'idle'` and do NOT set `endedAt` — leave it null. The session should remain alive (idle) until the actual Claude process exits.

- [X] T089 Fix ClaudeCodeDetector.scanExistingSessions() in ackend/src/services/claude-code-detector.ts: (1) The lse branch creates fake IDs (claude-startup-{repo.id}-{timestamp}) when no prior ended session exists  when real hooks fire with the real Claude session_id, getSession(realId) returns undefined and a NEW session is created, causing duplicate sessions; (2) The mostRecentEnded path reuses the OLD session ID, but the new Claude invocation has a new ID  same duplicate problem; (3) Active sessions on restart are skipped entirely (if (activeSessions.length > 0) continue) so their JSONL watchers are never restarted. Root cause: the real session ID is always the JSONL FILENAME (basename without .jsonl). Fix: replace the entire per-repo block with: (a) scan project dir for *.jsonl files sorted by mtime descending, (b) skip if most recent JSONL is older than ACTIVE_JSONL_THRESHOLD_MS, (c) use the JSONL filename (without .jsonl) as the session ID, (d) check if that ID already has status='active' and just restart its watcher via watchJsonlFile  do not re-upsert; (e) otherwise upsert with the real ID using existing session data (if any) or a fresh session struct; remove the claude-startup-* fake-ID branch entirely.

### Addendum: Bug  Preview strip light theme inconsistent, user wants dark consistently

- [X] T093 Fix `frontend/src/components/SessionCard/SessionCard.tsx` preview strip: T108 changed the preview strip from dark (`bg-gray-900 text-gray-300`) to light (`bg-gray-100 text-gray-600`), but the user wants a consistently dark code-preview aesthetic across all session cards regardless of selection state. The light `bg-gray-100` on a white/blue-50 card background has poor contrast and loses the "code output" feel. Fix: change the preview `<p>` classes back to `bg-gray-900 text-gray-300` (and keep the rest: `text-xs mt-1 px-2 py-1 rounded line-clamp-2 whitespace-pre-wrap break-words font-mono`).



### Addendum: Bug  Stale null-PID Claude Code sessions never cleaned up while any Claude process is running

- [X] T094 Fix `reconcileClaudeCodeSessions()` in `backend/src/services/session-monitor.ts`: For null-PID sessions the current condition `session.pid == null && !claudeRunning` never fires if any Claude process is running (even a different session). Stale sessions linger indefinitely. Fix: for null-PID sessions, check the JSONL file freshness instead  stat `~/.claude/projects/{projectDirName(repo.path)}/{session.id}.jsonl` and end the session if the file is missing OR its mtime is older than `ACTIVE_JSONL_THRESHOLD_MS` (30 min). Requires: (a) export `ACTIVE_JSONL_THRESHOLD_MS` from `claude-code-detector.ts`; (b) make `claudeProjectDirName` a `static projectDirName` public method on `ClaudeCodeDetector` so `session-monitor.ts` can use it; (c) import `existsSync`/`statSync` from `fs`, `join` from `path`, `homedir` from `os`, `getRepositories` (already imported) and `ACTIVE_JSONL_THRESHOLD_MS`/`ClaudeCodeDetector` in `session-monitor.ts`; (d) rewrite the null-PID branch to do the JSONL staleness check.

### Addendum: Bug — Branch badge does not update until window refocus

- [X] T095 Fix `frontend/src/pages/DashboardPage.tsx`: Both `useQuery` calls (for `repositories` and `sessions`) have no `refetchInterval`, so React Query only re-fetches on window focus/mount. The backend already refreshes branch names in the DB every 5 seconds via `SessionMonitor.refreshRepositoryBranches()`, but the frontend never polls for the updated data — users see the stale branch until they switch away and back to the browser. Fix: add `refetchInterval: 5000` to both the `repositories` useQuery and the `sessions` useQuery in DashboardPage.tsx.

### Addendum: Bug — Folder selection dialog shows old Win32 tree-view UI

- [ ] T110 Fix `backend/src/api/routes/fs.ts` `pick-folder` Windows branch: currently spawns `powershell` with `System.Windows.Forms.FolderBrowserDialog` which renders the ancient Win32 SHBrowseForFolder tree-view (unchanged since Windows XP). Fix: replace the PowerShell command with inline C# via `Add-Type` that calls `IFileOpenDialog` COM interface (CLSID `DC1C5A9C-E88A-4dde-A5A1-60F82A20AEF7`) with option `FOS_PICKFOLDERS | FOS_FORCEFILESYSTEM` — this renders the modern Vista-style Explorer dialog. No frontend changes needed.

### Addendum: Bug — PTY session stays "running" after /exit because process.exit() kills launcher before WebSocket flushes

- [X] T111 Fix `backend/src/cli/argus-launch-client.ts` `notifySessionEnded` and `backend/src/cli/launch.ts` `pty.onExit`: when Claude exits via /exit, `pty.onExit` calls `client.notifySessionEnded()` which calls `ws.send()` (async, only queues the data) then `ws.close()`, and then `launch.ts` immediately calls `process.exit()`. The process dies before the WebSocket message is flushed to the Argus backend, so the server never receives `session_ended` and the session stays "running". Fix: (a) change `notifySessionEnded` to return a Promise that resolves after `ws.close()` completes by listening for the `close` event; (b) in `launch.ts`, `await` the returned promise before calling `process.exit()`, with a safety timeout so the launcher never hangs indefinitely.

### Addendum: Bug — Adding a reminder does not appear in the list

- [X] T109 Fix `frontend/src/hooks/useTodos.ts`: After `createTodo`, `toggleTodo`, and `deleteTodo` mutations succeed, `queryClient.invalidateQueries` is called on the `queryClient` exported from `services/api.ts` — a **different** QueryClient instance from the one provided by `<QueryClientProvider>` in `App.tsx`. React Query's `useQuery` in `useTodos` is subscribed to the provider's QueryClient, so the invalidation has no effect and the list never refreshes. Fix: replace the direct import of `queryClient` from `services/api.ts` with `useQueryClient()` from `@tanstack/react-query` inside each mutation hook (useCreateTodo, useToggleTodo, useDeleteTodo), so invalidation targets the correct QueryClient instance that the queries are subscribed to.

### Addendum: Bug — GHCP launched via argus launch shows as read-only instead of live PTY session

- [X] T112 Fix `backend/src/services/copilot-cli-detector.ts` `processSessionDir()`: the method always sets `launchMode: null` on every upserted session. When `argus launch copilot` registers a pending WS in `ptyRegistry.registerPending()`, the subsequent scan never calls `ptyRegistry.claimForSession()`, so the WS connection is never promoted and `launchMode` stays null. Fix: (a) add `import { ptyRegistry } from './pty-registry.js'` to `copilot-cli-detector.ts`; (b) in `processSessionDir()`, after resolving `repo`, call `getSession(sessionId)` to check if the session is already claimed — if `existingSession?.launchMode === 'pty'` preserve `launchMode: 'pty'` and the existing pid/pidSource; otherwise call `ptyRegistry.claimForSession(sessionId, repo.path)` and if it returns a claim set `launchMode: 'pty'`, `pid: claimed.pid`, `pidSource: 'pty_registry'`; (c) add a regression test to `backend/tests/integration/copilot-cli-detector.test.ts` that mocks `ptyRegistry` with a pending connection for `testRepoCwd` and verifies `scan()` returns a session with `launchMode: 'pty'`.

### Addendum: Bug — sending a prompt to a GHCP PTY session fails after Argus backend restart

### Addendum: Bug — T113 regression: PTY launchMode wiped when session ends

### Addendum: Bug — ended sessions stealing pending PTY WS claim

- [X] T115 Fix `backend/src/services/copilot-cli-detector.ts` `processSessionDir()`: in the `else` branch (not yet claimed), `claimForSession(sessionId, repo.path)` is called unconditionally even when `isRunning = false`. GHCP creates a new session directory for each launch; old ended directories with the same `cwd` are processed during the scan and steal the pending WS registration from the new running session, leaving the active session without a claimed WS (`launchMode: null`). Fix: wrap the `claimForSession` call in the `else` branch with `if (isRunning)` so only active sessions can claim a pending launcher WS. Update the existing test "sets launchMode=pty when ptyRegistry has a pending connection for the same cwd" to add `mockPsList.mockResolvedValueOnce([{ pid: testPid, name: 'test', ppid: 1 }])` so the session appears running. Add a new test "does not claim pending PTY connection for a non-running (ended) session" that verifies `claimForSession` is NOT called when `isRunning = false`.

- [X] T114 Fix regression in `backend/src/services/copilot-cli-detector.ts` `processSessionDir()` introduced by T113: the T113 change `if (alreadyClaimed && ptyRegistry.has(sessionId))` causes the `else` branch to run when a PTY session's WS closes on normal process exit. `claimForSession` fails (no pending reconnect for an ended process), so `launchMode` is set to `null` — incorrectly erasing the historical PTY launch mode. Fix: restore `launchMode:'pty'` unconditionally when `alreadyClaimed=true`; separately try `claimForSession` only when `!ptyRegistry.has(sessionId) && isRunning` (process still alive, so WS disconnect is a backend-restart scenario not a normal exit). This preserves T113's restart re-linking behaviour while preventing launchMode from being wiped on session end. Also update the test for `preserves launchMode=pty without re-claiming when alreadyClaimed=true and WS is still live` and the test `downgrades to launchMode=null when alreadyClaimed=true but WS gone and no pending reconnect` — the latter should now expect `launchMode:'pty'` (not null) since an ended session keeps its historical launchMode. (a) In `copilot-cli-detector.ts` `processSessionDir()`, change `if (alreadyClaimed)` to `if (alreadyClaimed && ptyRegistry.has(sessionId))` — only preserve `launchMode:'pty'` when the WS is still live; when the WS is gone, fall through to `claimForSession()` to attempt re-linking to a freshly reconnected launcher, and if that also fails let `launchMode` remain `null` so the UI correctly shows the session as not launcher-connected; (b) In `argus-launch-client.ts`, add a `close` event handler inside `connect()` that calls `setTimeout(() => this.connect(), 2000)` when `!this.isClosing`, so the launcher process auto-reconnects to Argus after a backend restart and re-sends its `register` message on the new connection; add an `isClosing` flag set to `true` inside `notifySessionEnded()` to prevent reconnect after an intentional shutdown; (c) In `pty-registry.ts` `sendPrompt()`, add a `readyState` guard before `ws.send()` that rejects with the "not connected" error and removes the stale entry from `connections` if the socket is not open, preventing a thrown `WebSocket is not open` exception from escaping as an unhandled error; (d) add regression tests: in `copilot-cli-detector.test.ts` add tests for re-claim on `alreadyClaimed+WS-gone`, downgrade to `null` when no pending reconnect, and stable preserve when WS is live; in `argus-launch-client.test.ts` add tests that verify reconnect fires after close and that `notifySessionEnded` sets `isClosing` to block reconnect.

### Addendum: Bug — TODO toggle button state not preserved on remount

- [X] T117 Fix `frontend/src/components/TodoPanel/TodoPanel.tsx`: the three header toggle states (`showDone`, `showTimestamps`, `wrapText`) are plain `useState` with hardcoded defaults (`true`, `true`, `false`). They reset on every remount — e.g. switching mobile tabs away from the tasks tab and back, or toggling the Todo panel visibility in settings. Fix: initialise each state by reading from `localStorage` (keys `argus.todo.showDone`, `argus.todo.showTimestamps`, `argus.todo.wrapText`), falling back to the current defaults when the key is absent. Add a `useEffect` for each state that writes the new value back to `localStorage` whenever it changes.

### Addendum: Bug — conversation history not shown when adding a repository with an active session

- [X] T116 Fix `frontend/src/services/socket.ts` `applyOutputBatchEvent`: when `session.output.batch` fires before the `SessionCard` has mounted (and therefore before the React Query cache for `['session-output-last', sessionId]` and `['session-output', sessionId]` is populated), the guard `if (!old) return old` silently drops the batch. The `SessionCard` then mounts and fires an API call that can race the DB write from `insertOutput` in `readNewLines`. If the API returns before `insertOutput` completes (outputs not in DB yet), the result is cached as empty with `staleTime: Infinity`, permanently hiding the conversation. Fix: in `applyOutputBatchEvent`, replace `if (!old) return old` with a seed path that creates a valid `OutputQueryData` entry from the batch when `old` is undefined: for `['session-output', sessionId]` seed with `{ items: outputs.slice(-100), nextBefore: outputs.length > 0 ? String(outputs[outputs.length - 100 < 0 ? 0 : outputs.length - 100].sequenceNumber) : null, total: outputs.length }`; for `['session-output-last', sessionId]` seed with `{ items: outputs.slice(-10), nextBefore: null, total: outputs.length }`. Add a unit test in `frontend/tests/unit/socket.test.ts` that calls `applyOutputBatchEvent` with `old = undefined` and asserts the returned value is not undefined and contains the correct items.

### Addendum: Bug — Copilot session summary reset to autogenerated title on every scan

- [X] T119 Fix `backend/src/services/copilot-cli-detector.ts` `processSessionDir()`: the summary field is always set from `workspace.summary` (Copilot's autogenerated title), so every 5-second scan overwrites any user-message-derived summary that `readNewLines` wrote. Root cause: line 109 passes `summary: workspace.summary ?? null` unconditionally to `upsertSession`, and the SQL (`summary = excluded.summary`) applies it without guard. Fix: change line 109 to `summary: existingSession?.summary ?? workspace.summary ?? null` so the DB summary is preserved once set (whether from a user message or a prior workspace.yaml read), and workspace.yaml is only used as the initial fallback. Add a regression test in `backend/tests/integration/copilot-cli-detector.test.ts` that: (1) scans once (sets summary from workspace.yaml), (2) manually upserts the session with a user-message summary, (3) scans again, (4) asserts the session summary is still the user-message value, not the workspace.yaml value.

### Addendum: Bug — pid=null after backend restart reconnect

- [X] T121 Fix `backend/src/cli/argus-launch-client.ts` `updatePid()`: when the WS is open, `updatePid()` sends `update_pid` immediately but never writes the resolved pid back to `this.registerInfo.pid`. On backend restart, `handleOpen()` replays the `register` message using `this.registerInfo` (still has `pid: null`) and only replays `update_pid` if `this.pendingPid !== null` — but `pendingPid` is only set when the WS is closed at the time `updatePid` is called. So after reconnect the session is re-linked with `pid: null` permanently. Fix: at the top of `updatePid()`, before the `isOpen` check, add `if (this.registerInfo) { this.registerInfo = { ...this.registerInfo, pid }; }` so `registerInfo.pid` is always kept current and the reconnect register replay carries the correct pid.

### Addendum: Bug — Copilot model/summary updates not broadcast over WebSocket; dashboard polls unnecessarily

- [X] T120 Two related issues. (1) In `backend/src/services/copilot-cli-detector.ts` `readNewLines()`: the model-detection block (around line 241) and the summary-update block (around line 246) both call `upsertSession()` but never call `broadcast()`, so Copilot model and summary changes are written to the DB but not pushed to connected frontends. The frontend compensates with a 5-second `refetchInterval` poll. Fix: import `broadcast` from `../api/ws/event-dispatcher.js` in `copilot-cli-detector.ts` and add `broadcast({ type: 'session.updated', timestamp: new Date().toISOString(), data: updated as unknown as Record<string, unknown> })` immediately after each `upsertSession(updated)` call in those two blocks. (2) In `frontend/src/pages/DashboardPage.tsx` lines 76 and 82: both `useQuery` calls for `['repositories']` and `['sessions']` have `refetchInterval: 5000`. All repository and session lifecycle events are already pushed via WebSocket (`session.created`, `session.updated`, `session.ended`, `repository.added`, `repository.removed`), making the poll redundant. Fix: remove `refetchInterval: 5000` from both queries.

### Addendum: Bug — Kill session toggles output stream visibility

- [X] T118 Fix `frontend/src/components/KillSessionDialog/KillSessionDialog.tsx`: clicking Confirm, Cancel, or the backdrop in the kill dialog incorrectly triggers the `SessionCard` outer div's `onClick` handler, toggling the output stream pane. Root cause: `KillSessionDialog` uses `createPortal` to render to `document.body`, but React's synthetic event system still propagates events up the virtual component tree; since the dialog is a React child of `SessionCard`, button clicks bubble up to the card's `onClick={() => onSelect?.(session.id)}`. Fix: add `e.stopPropagation()` to the backdrop div's `onClick` handler so all clicks within the dialog are contained: change `onClick={(e) => { if (e.target === e.currentTarget && !isPending) onCancel(); }}` to `onClick={(e) => { e.stopPropagation(); if (e.target === e.currentTarget && !isPending) onCancel(); }}`.

### Addendum: Bug — Copilot sessions show "resting" despite active responses

- [X] T122 Fix `backend/src/services/copilot-cli-detector.ts`: Copilot sessions incorrectly show the "resting" badge even when responses are actively flowing. Two root causes: (1) `readNewLines()` never updates `lastActivityAt` when output arrives — unlike `ClaudeJsonlWatcher.applyActivityUpdate()` which does this correctly for Claude. (2) `processSessionDir()` always sets `lastActivityAt: toIso(workspace.updated_at)` on every 5-second scan, so even if fix (1) updates the field, the scan immediately overwrites it with the stale `workspace.updated_at` timestamp. Fix: (1) In `readNewLines()`, after `this.outputStore.insertOutput(sessionId, outputs)`, add an activity update: fetch the existing session, set `lastActivityAt` to `now`, `upsertSession`, and broadcast `session.updated`. (2) In `processSessionDir()`, change `lastActivityAt: toIso(workspace.updated_at)` to `lastActivityAt: existingSession?.lastActivityAt && existingSession.lastActivityAt > toIso(workspace.updated_at) ? existingSession.lastActivityAt : toIso(workspace.updated_at)` so a fresher in-memory value is never clobbered by the scan.

### Addendum: Bug — Copilot CLI ask_user question not shown in Argus UX

- [X] T124 Fix `backend/src/services/copilot-jsonl-watcher.ts` and `backend/src/services/jsonl-watcher-base.ts`: when Copilot CLI calls the `ask_user` tool, the `tool.execution_start` event is written to `events.jsonl` with `data.toolName: "ask_user"` and `data.arguments: {question, choices}`. The `CopilotJsonlWatcher` processes this via `readNewLines()` and stores it as a `tool_use` SessionOutput. However, the backend never broadcasts `session.pending_choice` for Copilot CLI sessions (unlike Claude Code, which fires it via an HTTP hook). The frontend's `detectPendingChoice(items)` fallback in `SessionCard` is unreliable because it depends on the `session-output-last` React Query cache being up to date. Fix: (1) Add a `protected onNewOutputs(sessionId: string, outputs: SessionOutput[]): void {}` hook in `JsonlWatcherBase` and call it with the inserted outputs at the end of `readNewLines()`. (2) Override `onNewOutputs` in `CopilotJsonlWatcher`: when a `tool_use` output with `toolName === 'ask_user'` is detected, parse `output.content` as `{question, choices}` and broadcast `session.pending_choice` (matching the shape emitted by `handlePreAskQuestion` in `claude-code-detector.ts`); track the `toolCallId` in a per-session map; when a `tool_result` output with a matching `toolCallId` is found, broadcast `session.pending_choice.resolved`.

### Addendum: Bug — branch name not updated on dashboard

- [X] T123Fix `backend/src/services/session-monitor.ts` `refreshRepositoryBranches()`: when a branch change is detected and `updateRepositoryBranch(repo.id, branch)` is called, no WebSocket event is broadcast. T120 removed the 5-second `refetchInterval` poll from the frontend, so the UI has no way to learn of the change. The frontend `socket.ts` also has no `repository.updated` handler. Fix: (1) In `refreshRepositoryBranches()`, after `updateRepositoryBranch(repo.id, branch)`, call `getRepository(repo.id)` and broadcast `{ type: 'repository.updated', timestamp: now, data: updatedRepo }`. `getRepository` is already exported from `../db/database.js`. (2) In `frontend/src/services/socket.ts`, add `onEvent('repository.updated', () => { qc.invalidateQueries({ queryKey: ['repositories'] }); })` alongside the existing `repository.added` and `repository.removed` handlers.


### Addendum: Bug — historical JSONL outputs re-sent to Slack/Teams on session detection

- [X] T124 Fix `backend/src/services/claude-jsonl-watcher.ts` `watchFile()` and `backend/src/services/output-store.ts` `insertOutput()`: when `watchFile()` is first called for a session, it sets `filePositions` to 0 and immediately calls `readNewLines()`, which reads the entire JSONL history and calls `outputStore.insertOutput()`. `insertOutput()` unconditionally fires output listeners (Teams) and emits `session.output.batch` (Slack), causing every historical message to be re-sent as a new notification. Fix: add an optional `options?: { skipNotifications?: boolean }` parameter to `OutputStore.insertOutput()`. When `skipNotifications` is true, skip the listener loop, `broadcast()` call, and `outputEvents.emit()` call (still persist to DB). In `watchFile()`, pass `{ skipNotifications: true }` to the `readNewLines()` invocation at line 33 by adding an `options` parameter to `readNewLines()` that is forwarded to `insertOutput()`. Subsequent `chokidar` change events call `readNewLines()` without the flag, so live output continues to notify normally.

### Addendum: Bug — @homebridge/node-pty-prebuilt-multiarch dead dependency breaks Node 25

- [X] T125 Remove dead dependency `@homebridge/node-pty-prebuilt-multiarch` from `package.json` (root) and `backend/package.json`: the package is listed as a dependency in both files but is never imported anywhere in the codebase (all PTY usage imports from `node-pty` directly). Its engine constraint `>=18.0.0 <25.0.0` causes `npm warn EBADENGINE` on Node 25.x. Fix: delete the `"@homebridge/node-pty-prebuilt-multiarch": "^0.13.1"` entry from the `dependencies` section of both `package.json` and `backend/package.json`, then run `npm install` to remove it from `package-lock.json`.

### Addendum: Bug — Copilot ask_user question text not shown when no choices provided

- [X] T126 Fix `backend/src/services/copilot-jsonl-watcher.ts` `onNewOutputs()`: when Copilot CLI calls `ask_user` with only a `question` argument and no `choices`, `copilot-cli-jsonl-parser.ts` `extractContent()` returns the raw question string (not JSON-wrapped) because the single-value shortcut `vals.length === 1` triggers. In `onNewOutputs()`, `JSON.parse(output.content)` then throws a SyntaxError. The catch block says "content may not be JSON when choices is absent" but leaves `question = ''`, so an empty question is broadcast and the UI renders no question text. Fix: in the catch block of `onNewOutputs()`, set `question = output.content` so the raw string is used as the question directly instead of being silently discarded.

### Addendum: Bug — WebSocket-driven queries refetch unnecessarily on window focus

- [X] T128 Fix seven `useQuery` calls that have no `refetchOnWindowFocus: false` despite being fully kept up to date by WebSocket push. On every tab focus React Query treats them as stale (staleTime=0 default) and fires an HTTP request that duplicates what the WebSocket already delivered. The affected queries and files: (1) `['sessions']` in `frontend/src/pages/DashboardPage.tsx` (covered by `session.created/updated/ended` WS events); (2) `['repositories']` in `frontend/src/pages/DashboardPage.tsx` (covered by `repository.added/updated/removed` WS events); (3) `['session', id]` in `frontend/src/pages/SessionPage.tsx` (covered by `session.updated` WS event); (4) `['repositories']` in `frontend/src/pages/SessionPage.tsx` (same WS events); (5) `['update-status']` in `frontend/src/hooks/useUpdateStatus.ts` (covered by `update.status` WS event added in T127); (6) `['session-output', session.id]` in `frontend/src/components/OutputPane/OutputPane.tsx` (covered by `session.output.batch` WS event); (7) `['session-output', session.id]` in `frontend/src/components/SessionPromptBar/SessionPromptBar.tsx` (same WS event). Fix: add `refetchOnWindowFocus: false` to each of these seven `useQuery` calls. Do NOT add it to `['integration-status']`, `['todos']`, `['argus-settings']`, `['available-tools']`, or `['health']` — those have no WebSocket push and benefit from focus refetch.

### Addendum: Bug — integration status has no WebSocket push so frontend polls on window focus

- [X] T130 Fix integration status so state changes are pushed via WebSocket instead of relying on focus-refetch. Two root causes: (1) `backend/src/api/routes/integrations.ts` start/stop route handlers never broadcast after changing state, so the frontend has no push signal. (2) `frontend/src/hooks/useIntegrationControl.ts` `useQuery` for `['integration-status']` has no `refetchOnWindowFocus: false`. Fix: (a) In `backend/src/api/ws/event-dispatcher.ts`, add `'integration.status'` to `WsEventType` and add `{ type: 'integration.status'; timestamp: string; data: IntegrationStatusPayload }` to the `WsEvent` union, where `IntegrationStatusPayload` is exported from `integrations.ts` and matches the shape of `GET /api/v1/integrations`. (b) In `backend/src/api/routes/integrations.ts`, extract the status-building logic from the GET handler into a private `buildStatusPayload()` helper so both the GET response and the broadcast use identical logic; import `broadcast` from `event-dispatcher.ts`; call `broadcast({ type: 'integration.status', timestamp: new Date().toISOString(), data: buildStatusPayload() })` at the end of each of the four start/stop route handlers (slack/start, slack/stop, teams/start, teams/stop). (c) In `frontend/src/services/socket.ts` `initSocketHandlers()`, add `onEvent('integration.status', (data) => { qc.setQueryData(['integration-status'], data); })`. (d) In `frontend/src/hooks/useIntegrationControl.ts`, add `refetchOnWindowFocus: false` to the `useQuery` call.

### Addendum: Bug — argus-settings refetches on window focus despite mutations keeping cache current

- [X] T129 Fix `frontend/src/hooks/useArgusSettings.ts`: the `useQuery` for `['argus-settings']` has `staleTime: 30_000` but no `refetchOnWindowFocus: false`. Settings have no external source of change and no WebSocket push — every write goes through `patchSetting`, which calls `queryClient.setQueryData(ARGUS_SETTINGS_QUERY_KEY, updated)` on success, keeping the cache permanently current. A tab-focus refetch 30+ seconds after the last write just re-fetches the same value already in cache. Fix: add `refetchOnWindowFocus: false` to the `useQuery` call at line 17 of `useArgusSettings.ts`.

### Addendum: Bug — update status polled every 60 s instead of being pushed via WebSocket

- [X] T127 Fix two related issues in the auto-update flow: (1) `frontend/src/hooks/useUpdateStatus.ts` line 8 has `refetchInterval: 60_000`, causing the frontend to poll `/api/v1/update/status` every 60 seconds even though the backend only checks npm every 4 hours (240 unnecessary HTTP requests per check cycle). (2) `backend/src/services/update-service.ts` `checkForUpdates()` never broadcasts a WebSocket event after completing a check, so the frontend had no push alternative. Fix: (a) In `backend/src/api/ws/event-dispatcher.ts`, add `'update.status'` to `WsEventType` and add `{ type: 'update.status'; timestamp: string; data: UpdateStatus }` to the `WsEvent` union (import `UpdateStatus` from `../../services/update-service.js`). (b) In `backend/src/services/update-service.ts`, add `private broadcastFn: ((status: UpdateStatus) => void) | null = null;` and a `setBroadcastCallback(fn: (status: UpdateStatus) => void): void` setter; at the end of `checkForUpdates()` (after setting `this.lastChecked`), call `this.broadcastFn?.(this.getStatus())`. (c) In `backend/src/server.ts`, after `updateService.scheduleChecks(...)`, call `updateService.setBroadcastCallback((status) => broadcast({ type: 'update.status', timestamp: new Date().toISOString(), data: status }))`. (d) In `frontend/src/services/socket.ts` `initSocketHandlers()`, add `onEvent('update.status', (data) => { qc.setQueryData(['update-status'], data); })`. (e) In `frontend/src/hooks/useUpdateStatus.ts`, remove `refetchInterval: 60_000` and `staleTime: 55_000` so the hook only fetches once on mount (initial cached state from backend) and relies on WebSocket push for subsequent updates.
