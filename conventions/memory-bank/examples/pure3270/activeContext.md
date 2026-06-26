<!-- source: pure3270 — https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/activeContext.md -->
# Active Context (as of 2025-10-13)

## Recently Completed
- Implemented TTYPE SEND -> IS reply (removed malformed extra NUL) enabling host to proceed after terminal type negotiation.
- Added hybrid VT100/TN3270 handling improvements: exclusive ASCII activation, handler-level flag, quick smoke ASCII detection.

## Recently Completed (October 2025)
- **✅ Attribution & Porting Infrastructure**: All tasks completed (TASK004, TASK005, TASK006)
  - THIRD_PARTY_NOTICES.md created with x3270 BSD-3-Clause license
  - PORTING_GUIDELINES.md enhanced with RFC-first development philosophy
  - Attribution scaffolding system validated (27/27 tests passing)
- **✅ P3270Client API Compatibility**: Full parity achieved (TASK003)

## Recently Completed (January 2025 - Latest)
- **✅ NEW_ENVIRON Proper Parsing**: RFC 1572 compliant implementation completed (TASK008)
 - **✅ Configurable Terminal Models**: Terminal model registry, public API parameter (`terminal_type`), dynamic sizing and negotiation updates, docs and examples (TASK009 completed).
  - Replaced NAWS hack with proper environment variable parsing
  - Added complete NEW_ENVIRON constants and subnegotiation handling
  - Implemented escape sequence processing and IS/SEND/INFO commands
  - Full test coverage with validation against quick smoke test
- **✅ Screen Parity Regression Scaffold**: Comprehensive snapshot system verified as complete and functional
  - Snapshot tools working: capture, compare, validate
  - Multiple baseline scenarios covering different screen states
  - Quick smoke test integration providing continuous regression protection
  - Complete documentation in README.md

## Current Focus
All planned October work items are complete. Next focus will be on printer enhancements and extended attributes per TODO backlog.

## Key Decisions
- ✅ NEW_ENVIRON now RFC 1572 compliant with proper environment variable parsing (replaced previous NAWS hack).
- Default terminal type: `IBM-3278-2` (baseline); now publicly configurable.
- ASCII mode once enabled is irreversible per handler lifecycle (simplifies parsing logic, avoids mixed-mode complexity for now).

 ## Known Gaps / Risks
 - No automated regression test capturing real host negotiation trace.

## Next Planned Steps
1. Evaluate transparent printing support and extended attributes implementation.
2. Plan regression capture for real host negotiation traces.

## Metrics / Validation Hooks
- `quick_test.py` now includes ASCII detection PASS criteria.
- Future: add `python tools/validate_screen_snapshot.py` to assert snapshot fidelity.
