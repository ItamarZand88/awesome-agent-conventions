<!-- source: argus-security-review — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/009-security-review/spec.md -->
# Feature Specification: Security Review & Hardening

**Feature Branch**: `009-security-review`
**Created**: 2026-04-02
**Status**: Draft
**Input**: User description: "do a security review of this project"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Process Control Cannot Be Weaponized (Priority: P1)

A developer runs Argus on their machine. A separate local process (malicious script, compromised npm package) attempts to use Argus's unauthenticated REST API to stop or interrupt processes by injecting a crafted PID via the hook endpoint, then calling the stop/interrupt API. The attack should fail.

**Why this priority**: Session control endpoints can kill arbitrary OS processes. A compromised local tool exploiting this could terminate critical system processes or other developer tools. This is the most direct harm vector.

**Independent Test**: Send a POST to `/hooks/claude` with a crafted `pid` pointing to a known non-AI process, then call `/api/v1/sessions/{id}/stop`. Verify the target process is not affected and the request is rejected or the PID is validated against running Claude/Copilot processes only.

**Acceptance Scenarios**:

1. **Given** the Argus backend is running, **When** a caller sends a hook payload with a `pid` that does not belong to a Claude Code or Copilot CLI process, **Then** the session's PID field is not set to that value and process control cannot target it.
2. **Given** a session exists with a stored PID, **When** a caller POSTs to `/api/v1/sessions/:id/stop`, **Then** the system verifies the PID still belongs to a Claude/Copilot process before sending a signal.
3. **Given** a caller injects a `session_id` that matches an existing session via the hook endpoint, **Then** the hook cannot overwrite the existing session's PID with a new value.

---

### User Story 2 - Hook Endpoint Rejects Malformed and Oversized Payloads (Priority: P1)

A developer's Argus instance receives a crafted POST to `/hooks/claude` — either from a malicious local process or a misconfigured Claude hook — containing an extremely large payload, unexpected field types, or a `cwd` path designed to trigger a file watcher on a sensitive system path. The endpoint should validate and reject bad input without crashing or being exploited.

**Why this priority**: The hook endpoint is the primary external input surface. It receives unstructured data from Claude Code and triggers file system watchers. Unrestricted input here can cause resource exhaustion or watcher abuse.

**Independent Test**: POST to `/hooks/claude` with (a) a 10 MB body, (b) `cwd` set to `C:\Windows\System32`, (c) a `session_id` with path traversal characters. Verify each is rejected with a 400 and no watcher is started.

**Acceptance Scenarios**:

1. **Given** a POST to `/hooks/claude` with a body larger than a defined maximum, **When** received, **Then** the server returns 400 and does not process the payload.
2. **Given** a `cwd` in the hook payload that does not match any registered repository, **When** processed, **Then** no file watcher is started and no session is created.
3. **Given** a `session_id` containing path traversal sequences (e.g., `../../`), **When** received, **Then** the server rejects it with a 400 before any file path is constructed.

---

### User Story 3 - Shell Commands Use Safe APIs Instead of String Interpolation (Priority: P2)

When Argus stops or interrupts a session on Windows, it currently constructs a `taskkill` shell command by embedding a PID directly into a string passed to `exec()`. This should be replaced with a safe API call that does not involve shell interpretation.

**Why this priority**: String interpolation into shell commands is a well-known injection class. Even if PIDs are numeric today, the pattern is fragile and should be eliminated before the codebase grows.

**Independent Test**: Code review and automated linting confirms no `exec()` or `execSync()` calls with interpolated session data in session-controller.ts. All process signals use native OS APIs.

**Acceptance Scenarios**:

1. **Given** a stop request for a session on Windows, **When** processed, **Then** the process is terminated using a native API call with a numeric PID argument, not a shell command string.
2. **Given** a stop request for a session on Unix/macOS, **When** processed, **Then** `process.kill(pid, 'SIGTERM')` is used directly, with no shell invocation.
3. **Given** any PID-based operation where the PID value is not a valid positive integer, **When** attempted, **Then** the operation is rejected before any API or shell call is made.

---

### User Story 4 - Filesystem Routes Cannot Traverse to Sensitive Paths (Priority: P2)

A developer uses the folder picker or scan-folder feature. A malicious caller (or confused frontend bug) sends a path like `C:\Windows` or `../../../../etc` to the filesystem API. The scan should be rejected or sandboxed to the user's home directory and configured watch paths.

**Why this priority**: The filesystem routes expose real directory listings and recursive repo scanning. While localhost-only, they should not allow disclosure of arbitrary filesystem structure.

**Independent Test**: POST to `/api/fs/scan-folder` with `path: "C:\\Windows\\System32"`. Verify it returns a 403, not a directory listing.

**Acceptance Scenarios**:

1. **Given** a scan-folder request with a path outside the user's home directory and configured watch directories, **When** received, **Then** the server returns a 403 rather than a directory listing.
2. **Given** a scan-folder request with a path containing `..` sequences, **When** received, **Then** the server normalizes and rejects the path before any filesystem access.
3. **Given** a folder scan that recurses into a symlink loop, **When** processed, **Then** the server detects the loop and terminates traversal safely without hanging.

---

### User Story 5 - Security Headers Protect the Local Web Interface (Priority: P3)

When a browser connects to the Argus frontend, HTTP responses include standard security headers that prevent clickjacking, MIME sniffing, and other browser-level attacks — even in a localhost context.

**Why this priority**: The Argus frontend is served from a local HTTP server opened in a real browser. Browser security policies apply regardless of the host being localhost.

**Independent Test**: Inspect HTTP response headers from the Argus backend. Verify presence of `X-Content-Type-Options`, `X-Frame-Options`, and absence of server version disclosure.

**Acceptance Scenarios**:

1. **Given** any response from the Argus backend API, **When** inspected, **Then** `X-Content-Type-Options: nosniff` and `X-Frame-Options: DENY` are present.
2. **Given** a response from any API endpoint, **When** inspected, **Then** no server version or runtime information is disclosed in response headers.

---

### Edge Cases

- What happens if two hook payloads arrive simultaneously with the same `session_id` but different `pid` values?
- What happens if a `session_id` is a valid UUID but also a valid file path segment that resolves to an existing directory under `~/.claude/projects/`?
- What happens if the Argus process's own PID is sent in a stop request?
- What happens if a scan-folder request is sent while a previous scan is still running on the same path?
- What happens if `~/.claude/settings.json` is a symlink pointing to a sensitive file when hook injection attempts to write to it?

## Requirements *(mandatory)*

### Functional Requirements

**Process Control Safety**

- **FR-001**: The system MUST validate that a session's PID belongs to a running Claude Code or Copilot CLI process before executing any stop, interrupt, or signal operation. Validation MUST apply two checks in order: (1) the PID is present in the internal session registry (set via internal session-creation flow, never from hook input), and (2) the OS-reported executable name for that PID matches a known-safe allowlist (e.g., `claude.exe`, `gh.exe` on Windows; `claude`, `gh` on Unix). Both checks must pass.
- **FR-002**: The system MUST NOT construct OS shell commands by interpolating PID or session data into strings; all process signals MUST use native OS APIs with typed numeric arguments.
- **FR-003**: The system MUST reject stop/interrupt requests where the stored PID fails either the registry check or the OS executable name check.
- **FR-004**: The system MUST NOT allow a hook payload to overwrite the `pid` of an already-active session with a different value. If a hook payload arrives for an existing `session_id` with a conflicting `pid`, the server MUST return 409 and leave the existing session unchanged.

**Hook Endpoint Validation**

- **FR-005**: The system MUST enforce a maximum request body size on the `/hooks/claude` endpoint and return 400 for oversized payloads.
- **FR-006**: The system MUST validate that `session_id` in hook payloads matches the UUID format (`[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`, exactly 36 characters) before constructing any file path from it. Both Claude Code and Copilot CLI use UUIDs for session identifiers.
- **FR-007**: The system MUST only start a file watcher for a `cwd` path that matches a registered repository — unrecognized `cwd` values MUST NOT trigger any filesystem activity.

**Filesystem Route Safety**

- **FR-008**: The system MUST reject scan-folder and browse requests for paths outside the user's home directory and configured watch directories, returning a 403 response.
- **FR-009**: The system MUST normalize and validate all user-supplied paths to remove traversal sequences before any filesystem operation.
- **FR-010**: The system MUST detect and terminate symlink loops during recursive directory traversal without hanging.

**Security Headers**

- **FR-011**: All HTTP responses from the backend MUST include `X-Content-Type-Options: nosniff` and `X-Frame-Options: DENY`.
- **FR-012**: The backend MUST NOT expose server version or runtime information in response headers.

### Key Entities

- **Hook Payload**: Input received at `/hooks/claude` — validated against a strict schema (session_id format, cwd registry membership, body size) before any processing.
- **Process Signal**: An OS-level operation targeting a PID — only issued after verifying PID belongs to a Claude/Copilot process.
- **Watched Path**: A filesystem path registered for file watching — derived only from registered repository paths, never directly from user input.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Zero shell-command-with-string-interpolation patterns remain in process control code — verified by code review and automated linting rule.
- **SC-002**: 100% of hook payloads with invalid `session_id` characters, oversized bodies, or unrecognized `cwd` values are rejected with 4xx before any filesystem or database write occurs — verified by unit tests.
- **SC-003**: 100% of stop/interrupt requests verify PID ownership before issuing any signal — verified by unit tests covering both valid and invalid PID scenarios.
- **SC-004**: All backend HTTP responses include the required security headers — verified by integration tests inspecting response headers on every route.
- **SC-005**: Filesystem route requests with paths outside safe boundaries return 403 in 100% of test cases covering home-dir boundary, traversal sequences, and Windows system paths.

## Assumptions

- Argus is a single-user local tool; multi-user access control (roles, per-user sessions) is out of scope.
- The server binding to `127.0.0.1` is already in place and is not changing — this review hardens within that constraint.
- Teams integration auth token handling is out of scope for this review (separate auth surface addressed in branch 008).
- Rate limiting is out of scope — the localhost constraint is the accepted primary DoS mitigation.
- Claude Code's JSONL files on disk are considered trusted input (written by Claude Code itself, not by users).
- WebSocket broadcast authentication (filtering events per client) is out of scope for this review given the localhost constraint.

## Clarifications

### Session 2026-04-02

- Q: How should the system verify a PID belongs to a Claude Code or Copilot process? → A: Both checks required — registry membership first, then OS executable name match against a known allowlist.
- Q: What is the valid character set for `session_id` in hook payloads? → A: UUID format only (`[a-f0-9-]{36}`). Confirmed from real Copilot CLI session data — both tools use UUIDs.
- Q: When two hook payloads arrive with the same `session_id` but different `pid` values, which wins? → A: First write wins; subsequent conflicting payloads return 409 and the existing session is unchanged.
