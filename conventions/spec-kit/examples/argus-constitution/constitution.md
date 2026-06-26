<!-- source: argus-constitution — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/.specify/memory/constitution.md -->
<!--
## Sync Impact Report
**Version change**: 1.2.0 → 1.3.0 (minor — added §XII Error Handling principle)
**Added sections**: §XII Error Handling
**Rationale**: Errors in logs/server responses must carry full technical context for debuggability (§I, §VII).
UX-facing errors must be human-readable without leaking internal details. Two distinct contracts.
**Templates reviewed**: plan-template.md ✅ spec-template.md ✅ tasks-template.md ✅
-->

# Argus Constitution

## Core Principles

### I. Engineering
- Systems MUST be reliable, observable, and debuggable.
- Prefer simple solutions; every abstraction requires justification.
- All functionality MUST be testable in isolation.
- All changes MUST be reversible (feature flags, migrations, rollback).
- Design for scale from the beginning.

### II. Architecture
- All services MUST have clear, versioned API boundaries.
- No service MAY directly access another service's database.
- All inter-service communication MUST happen via APIs.
- All long-running work MUST be asynchronous with observable status.

### III. Code Standards
- Code MUST be readable and self-documenting (comments explain *why*, not *what*).
- Functions MUST be < 50 lines.
- All public APIs MUST have documentation.
- Use structured logging (JSON/key-value) — no unstructured logs in production.

### IV. Test-First (NON-NEGOTIABLE)
- Tests MUST be written before implementation. No exceptions.
- Follow Red-Green-Refactor strictly.
- No PR may be submitted without tests written first.

### V. Testing Requirements
- All features MUST have unit tests.
- All APIs MUST have integration tests.
- All critical flows MUST have end-to-end tests.
- All AI-generated code MUST be reviewed by a human before merge.
- Test coverage MUST NOT decrease with any PR.

### VI. Security & Compliance
- All endpoints MUST enforce authentication and authorization.
  - **Exception**: Services bound exclusively to `127.0.0.1` that serve a single local user MAY use network isolation in lieu of auth/authz. This exception MUST be explicitly declared in the feature specification and is only valid for v1 of local developer tools. Post-v1 network exposure requires full auth.
- No secrets in source code, config files, or logs.
- All actions MUST be audit-logged (actor, timestamp, outcome).
- Follow least-privilege access for all services and users.

### VII. Observability
- All services MUST emit structured logs, metrics, and a health check endpoint.
- All failures MUST be traceable via correlation IDs or distributed tracing.

### VIII. Performance
- APIs MUST respond within 500ms at p95.
- System MUST support 10,000 concurrent users.
  - **Exception**: Single-user localhost developer tools are exempt from the 10,000 user target. Such tools MUST instead define their actual concurrency target explicitly in the feature specification (e.g., "≥10 concurrent sessions").
- System MUST degrade gracefully under overload.

### IX. AI Usage
- AI MAY generate implementation code but MUST NOT make architecture decisions.
- AI MUST NOT handle security-critical code without explicit human review.
- All AI-generated outputs MUST be validated with tests before merge.

### X. Definition of Done
A feature is complete only when ALL are satisfied:
- [ ] Code written and reviewed
- [ ] Tests written test-first and passing
- [ ] Documentation written
- [ ] README.md updated to reflect the change
- [ ] Metrics and logs added
- [ ] Security reviewed

### XI. Documentation
- `README.md` MUST be updated with every user-facing or architectural change.
- Documentation updates MUST be included in the same PR as the code change — not deferred.
- README MUST always reflect the current state of the project: setup instructions,
  configuration options, and any behaviour changes since the last release.
- Outdated documentation is treated as a bug.

### XII. Error Handling
- Server-side errors and log entries MUST include full technical context: error code,
  stack trace (in development), request ID, affected resource, and any relevant state.
- API error responses MUST use a structured contract: `{ error: ERROR_CODE, message: string, requestId: string }`.
- UX-facing error messages MUST be human-friendly: plain language, actionable where possible,
  and MUST NOT expose internal error codes, stack traces, raw paths, or JSON blobs.
- The frontend MUST extract and display only the `message` field from API error responses —
  never the raw response body or HTTP status prefix.
- Errors that can be recovered by the user MUST suggest a corrective action (e.g., "Please
  choose a folder that contains a .git directory.").

## Governance

Amendments require a dedicated PR (not a feature branch), a migration plan, and a version bump. Run `/speckit.constitution` to propagate changes to templates. Constitution violations found by `/speckit.analyze` are **CRITICAL** and block merge.

**Versioning**: MAJOR = principle removed/redefined · MINOR = new principle · PATCH = clarification

**Version**: 1.3.0 | **Ratified**: 2026-04-01 | **Last Amended**: 2026-04-01
