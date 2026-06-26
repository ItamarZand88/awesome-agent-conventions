<!-- source: argus-session-dashboard — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/001-session-dashboard/spec.md -->
# Feature Specification: Session Dashboard

**Feature Branch**: `001-session-dashboard`
**Created**: 2026-04-01
**Status**: Clarified
**Input**: User description: "i want to build and experience that shows me all the repositories that i have locally with the running copilot, github copilot and claude code sessions on each of them. From this i want to see the state of each session. I want to see the results of the session and i want to control what is going on there."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Repository & Session Overview (Priority: P1)

As a developer, I want to open Argus and immediately see all my local repositories alongside any active AI coding sessions running on them, so I can get a complete picture of my AI assistant activity without switching between tools.

**Why this priority**: This is the foundational view — without it there is no product. It delivers immediate value by replacing the manual process of checking each AI tool separately.

**Independent Test**: Can be fully tested by pointing Argus at a machine with multiple local repos and active sessions, and verifying all repos and sessions appear listed with their current status.

**Acceptance Scenarios**:

1. **Given** I have 5 local repositories with 2 active Claude Code sessions and 1 active GitHub Copilot CLI session, **When** I open the Argus dashboard, **Then** all 5 repositories are listed and the 3 active sessions are clearly indicated on their respective repos.
2. **Given** a repository has no active AI sessions, **When** I view the dashboard, **Then** the repository is still listed but shown as having no active sessions.
3. **Given** a new session starts on a repository while the dashboard is open, **When** it is detected, **Then** the dashboard updates to show it without requiring a manual refresh.
4. **Given** repositories exist across multiple directories, **When** I open the dashboard, **Then** all configured directories are scanned and every repository is displayed.

---

### User Story 2 - Session State & Results (Priority: P1)

As a developer, I want to select a specific repository's AI session and see its current state, activity, and output in detail, so I can understand exactly what the AI is doing or has done without opening the AI tool itself.

**Why this priority**: Visibility into session state is the core monitoring value of Argus. Together with US1 this completes the "monitor" capability.

**Independent Test**: Can be fully tested by selecting an active session and verifying that status, current activity, and output history are displayed accurately and update in real time.

**Acceptance Scenarios**:

1. **Given** an active Claude Code session is running, **When** I select it, **Then** I see its current status (active / idle / waiting / error), the current task being worked on, and a history of recent outputs.
2. **Given** a GitHub Copilot session has recently completed work, **When** I view its results, **Then** I see the completed conversation or changes made, with timestamps.
3. **Given** a session is actively generating output, **When** I view it, **Then** the output updates in real time as new content is produced.
4. **Given** a session has encountered an error, **When** I view its state, **Then** the error is clearly surfaced with enough context to understand what went wrong.

---

### User Story 3 - Session Control (Priority: P2)

As a developer, I want to control active AI sessions from the Argus dashboard, so I can manage my AI tools from a single place without switching context.

**Why this priority**: Control is valuable but monitoring alone (US1 + US2) already delivers the core product. Control is a natural and important next layer.

**Independent Test**: Can be fully tested by performing a control action on a live session from the dashboard and verifying the session responds as expected.

**Acceptance Scenarios**:

1. **Given** a running session, **When** I stop it from the dashboard, **Then** the session is terminated and the dashboard reflects the updated state within 3 seconds.
2. **Given** I send a message or prompt to an active session, **When** the session receives it, **Then** the session processes it and the response appears in the results view.
3. **Given** I attempt to control a session that has already ended, **When** I submit the action, **Then** I receive a clear message that the session is no longer active.

---

### Edge Cases

- **Deleted/moved repository**: If a repository's `.git` directory is no longer accessible on the next scan, the repository is marked `unavailable` in the database and the dashboard shows an inline warning banner. The repository record is not auto-deleted; the user must manually remove it. Sessions on an unavailable repo retain their last known state.
- **Unexpected session end**: When an AI session crashes or ends unexpectedly, it is shown as "ended" with a timestamp and auto-removed after the configured retention period.
- **Multiple concurrent sessions of the same type**: A repository may have multiple simultaneous sessions of the same AI tool type (e.g., two `copilot-cli` sessions). Each is displayed as a separate session card, ordered by `startedAt` descending.
- **Slow discovery with many repositories**: The initial scan is non-blocking and asynchronous. The UI shows a "Scanning repositories…" state while discovery runs and populates results incrementally as repos are found.
- **No active sessions**: Repositories with no active sessions are still listed on the dashboard. An empty state message is shown per-repo ("No active sessions") and at the dashboard level if no sessions exist across all repos.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST discover and display all local repositories configured for monitoring via a config file specifying root directories to scan; repositories MUST also be addable and removable through the dashboard UI.
- **FR-002**: System MUST detect active Claude Code and GitHub Copilot CLI sessions on each repository via a hybrid approach: OS process scanning to identify running sessions, combined with IPC/API connections and event hooks exposed by each AI tool for real-time state and output. *(GitHub Copilot VS Code extension detection is out of scope for v1; planned post-v1.)*
- **FR-003**: System MUST display the current state of each active session (active, idle, waiting, error, completed).
- **FR-004**: System MUST display session output and results history for each active or recently completed session, persisted to disk so history survives session end and Argus restarts.
- **FR-004a**: System MUST enforce a configurable retention limit on persisted session output (by size or age); output exceeding the limit MUST be automatically pruned.
- **FR-005**: System MUST update session state and output in real time without requiring manual refresh.
- **FR-006**: System MUST allow users to stop active sessions from the dashboard.
- **FR-007**: System MUST allow users to send prompts and messages to active Claude Code sessions from the dashboard. *(Prompt injection for GitHub Copilot CLI is not supported in v1 — the API returns a clear unsupported message; planned post-v1.)*
- **FR-008**: System MUST handle sessions that end or become unreachable gracefully, without crashing or hanging.
- **FR-009**: System MUST be accessible via a web browser connected to a locally running Argus server, bound to localhost (127.0.0.1) only. Network-accessible endpoints are out of scope for v1.
- **FR-009a**: System MUST display ended or crashed sessions as "completed" or "ended" with a timestamp; sessions MUST be automatically removed from the dashboard after a configurable retention period.
- **FR-010**: System MUST clearly distinguish between session types (Claude Code vs GitHub Copilot CLI). *(VS Code GitHub Copilot is out of scope for v1.)*
- **FR-011**: System MUST support at least 10 simultaneously monitored sessions across multiple repositories.

### Key Entities

- **Repository**: A local directory tracked by Argus; has a path, name, and zero or more associated sessions.
- **Session**: An active or recently completed AI coding assistant instance; belongs to a repository; has a type (Claude Code / GitHub Copilot CLI), status, start time, and output history. *(VS Code GitHub Copilot is out of scope for v1.)*
- **Session State**: The current operational status of a session — one of: active, idle, waiting for input, error, completed.
- **Session Output**: The ordered stream of results, messages, or changes produced by a session over its lifetime.
- **Control Action**: A user-initiated command sent to a session (e.g., stop, restart, send prompt).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developer can see all local repositories with their active AI sessions within 5 seconds of opening the dashboard.
- **SC-002**: Session state and output refresh within 2 seconds of a change occurring in the underlying session.
- **SC-003**: Developer can identify the current status of any session without opening the AI tool itself.
- **SC-004**: Developer can perform a session control action and see the result reflected in the dashboard within 3 seconds.
- **SC-005**: The dashboard correctly identifies and distinguishes the two supported AI tool types (Claude Code and GitHub Copilot CLI).

## Assumptions

- Argus runs locally on the same machine where the AI sessions are active.
- All monitored repositories are local filesystem directories accessible to Argus.
- "Results" means the output, conversation history, and file changes produced by a session during its lifetime.
- Multiple sessions of different AI tool types can run concurrently on the same repository.
- v1 scope covers the current user's local machine only — multi-machine and network-accessible endpoints are out of scope for v1 (planned post-MVP).
- Sessions are discovered via OS process scanning; state and output are retrieved via IPC/API connections and event hooks exposed by each AI tool (Claude Code, GitHub Copilot CLI, GitHub Copilot).
- Repositories are configured via a config file pointing to root directories; the dashboard UI supplements but does not replace the config file.
- Session output history is persisted to disk with a configurable retention limit; it is not kept indefinitely.
- Ended or crashed sessions remain visible on the dashboard for a configurable period before being auto-removed.
- The primary user is a single developer (not a team) managing their own local sessions.
- The Argus web server binds to 127.0.0.1 — no authentication is required for v1.
