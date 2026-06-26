<!-- source: argus-session-dashboard — https://raw.githubusercontent.com/aarthi-ntrjn/argus/master/specs/001-session-dashboard/plan.md -->
# Implementation Plan: Session Dashboard

**Branch**: `001-session-dashboard` | **Date**: 2026-04-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-session-dashboard/spec.md`

## Summary

Build a web-based dashboard (local server + browser UI) that monitors all local git repositories for active Claude Code, GitHub Copilot CLI, and GitHub Copilot sessions. The dashboard displays real-time session state and output, and allows the developer to stop sessions or send prompts to them. Session history is persisted to disk. The backend runs as a local server bound to `127.0.0.1`; the frontend is a React SPA served from the same process.

## Technical Context

**Language/Version**: TypeScript 5.x + Node.js 22 (LTS)
**Primary Dependencies**:
- Backend: Fastify 4, ws, better-sqlite3, chokidar, pino, js-yaml, ps-list
- Frontend: React 18, Vite, Tailwind CSS, shadcn/ui, TanStack Query

**Storage**: SQLite (better-sqlite3) for session output history + JSON config file (`~/.argus/config.json`) for repository registration

**Testing**: Vitest (unit + integration), Supertest (API contract), Playwright (E2E)

**Target Platform**: Windows 10+, macOS 13+, Linux (Ubuntu 22+); accessed via web browser (localhost)

**Project Type**: Web service (local) — Fastify backend + React SPA frontend bundled and served from the same process

**Performance Goals**: API p95 < 500ms; session state refresh < 2s; dashboard load < 5s; control action reflected < 3s

**Constraints**: Bound to 127.0.0.1 only (no auth required for v1); no elevated permissions; must not modify AI tool installations

**Scale/Scope**: ≥10 concurrent monitored sessions; single developer; local machine only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Status | Notes |
|---|---|---|
| I. Engineering | ✅ PASS | TypeScript + simple layered architecture; all components independently testable |
| II. Architecture | ✅ PASS | Backend/frontend split; WebSocket for real-time; clear REST API boundary |
| III. Code Standards | ✅ PASS | ESLint + Prettier enforced; TypeScript provides self-documentation; pino structured logging |
| IV. Test-First | ✅ PASS | Enforced via tasks phase — tests written before implementation |
| V. Testing Requirements | ✅ PASS | Vitest (unit + integration), Supertest (API), Playwright (E2E) |
| VI. Security | ✅ PASS | Localhost binding approved in spec for v1; no secrets; audit log for control actions |
| VII. Observability | ✅ PASS | pino structured logging; health check endpoint; metrics endpoint |
| VIII. Performance | ✅ PASS | Targets defined in Technical Context above |
| IX. AI Usage | ✅ PASS | Enforced in tasks |
| X. Definition of Done | ✅ PASS | Tracked per task in tasks.md |

**No violations. Gate passes.**

## Project Structure

### Documentation (this feature)

```text
specs/001-session-dashboard/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   ├── rest-api.md      # REST endpoint contracts
│   └── websocket.md     # WebSocket event contracts
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── config/
│   │   └── config-loader.ts       # Reads/writes ~/.argus/config.json
│   ├── db/
│   │   ├── schema.ts              # SQLite schema definitions
│   │   └── migrations/            # Schema migration files
│   ├── models/                    # TypeScript interfaces (no implementation)
│   ├── services/
│   │   ├── repository-scanner.ts  # Discovers git repos from config directories
│   │   ├── session-monitor.ts     # Orchestrates all detectors; emits events
│   │   ├── copilot-cli-detector.ts  # Reads ~/.copilot/session-state/
│   │   ├── claude-code-detector.ts  # Reads ~/.claude/ + process detection
│   │   ├── session-controller.ts  # Executes stop/send-prompt control actions
│   │   └── output-store.ts        # Persists session output to SQLite
│   ├── api/
│   │   ├── routes/                # Fastify REST route handlers
│   │   └── ws/                    # WebSocket event dispatcher
│   └── server.ts                  # Entry point; binds to 127.0.0.1
└── tests/
    ├── unit/
    ├── integration/
    └── contract/

frontend/
├── src/
│   ├── components/
│   │   ├── Dashboard/             # Repository list with session badges
│   │   ├── SessionCard/           # Per-session status and summary
│   │   ├── SessionDetail/         # Full output stream + metadata
│   │   └── ControlPanel/          # Stop / send-prompt actions
│   ├── pages/
│   │   ├── DashboardPage.tsx
│   │   └── SessionPage.tsx
│   └── services/
│       ├── api.ts                 # REST client (TanStack Query)
│       └── socket.ts              # WebSocket client + event dispatcher
└── tests/
    └── e2e/                       # Playwright tests
```

**Structure Decision**: Web application split (Option 2). Backend is a Fastify server; frontend is a React SPA built by Vite and served as static files from the same Fastify process. Single repo, two top-level directories (`backend/`, `frontend/`).

## Complexity Tracking

> No constitution violations to justify.
