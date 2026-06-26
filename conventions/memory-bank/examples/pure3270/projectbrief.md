<!-- source: pure3270 — https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/projectbrief.md -->
# Project Brief

Pure3270 aims to be a pure Python, dependency‑light, RFC‑compliant drop‑in replacement for `p3270.P3270Client` / s3270 tooling, adding async support and simplified distribution (no external binaries). Current strategic focus: achieving behavioral parity against real public TN3270 hosts (e.g. pub400.com) including hybrid NVT (ASCII/VT100) + TN3270 negotiation flows, while maintaining clean attribution for any future code references to the x3270 (s3270) project.

## Core Goals
- Full Telnet + TN3270/TN3270E negotiation per RFCs 854, 855, 856, 857, 858, 1091, 1576, 1646, 2355.
- Accurate 3270 data stream parsing & screen field management.
- Seamless ASCII / VT100 (NVT) fallback when server does not proceed to TN3270 data.
- Native `P3270Client` class providing API parity with `p3270.P3270Client`.
- RFC 1572 NEW_ENVIRON parsing implemented; standards‑compliant responses (e.g., TERM).
- Configurable terminal model selection with dynamic screen sizing and capability reporting.
- Zero runtime dependencies (stdlib only). Optional dev tooling isolated.
- Clean licensing & attribution for any borrowed logic (BSD‑3-Clause expected for x3270).

## Non‑Goals
- Reintroduction of macro DSL / scripting (explicitly removed).
- Heavy external dependencies or compiled extensions.

## Key Constraints
- Must behave identically enough for existing automation that expects legacy s3270 semantics.
- Network variability: some public hosts may exhibit non‑standard negotiation. Implementation follows RFCs first (including RFC 1572 NEW_ENVIRON), while degrading gracefully and documenting deviations when encountered.
