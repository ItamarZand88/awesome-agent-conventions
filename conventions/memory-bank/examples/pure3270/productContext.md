<!-- source: pure3270 — https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/productContext.md -->
# Product Context

Pure3270 replaces external 3270 emulator binaries with pure Python so environments (containers, serverless, restricted hosts) can script mainframe interactions without installing s3270 packages.

## Problems Solved
- Eliminates platform‑specific binary dependency (s3270).
- Provides asyncio support for concurrent screen/session workflows.
- Simplifies CI by enabling in‑process negotiation & parsing.
- Adds configurable terminal model selection to match host expectations (screen sizes, color).
- Implements RFC‑compliant NEW_ENVIRON handling for robust environment negotiation.

## Users / Personas
- DevOps / automation engineers migrating legacy scripts.
- Test harness builders needing deterministic screen parsing.
- Integration developers requiring both sync and async APIs.

## Experience Goals
- Simple: `from pure3270 import P3270Client` and use identical method names.
- Transparent: Optional trace recorder for negotiation diagnostics.
- Robust: Graceful fallback to ASCII/VT100 mode when TN3270E not negotiated.

## Key Differentiators
- Pure Python (no subprocess management, no binary distribution).
- Built‑in hybrid (VT100 + 3270) handling.
- Extensible screen buffer abstraction (fields, attributes, ASCII mode toggle).
- Standards‑first protocol behavior with documented deviations.
