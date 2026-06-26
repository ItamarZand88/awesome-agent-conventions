<!-- source: pure3270 — https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/systemPatterns.md -->
# System Patterns

## Architecture Overview
- `Session` / `AsyncSession` orchestrate lifecycle; internally use `TN3270Handler`.
- `TN3270Handler` performs I/O reads, Telnet IAC parsing, delegates negotiation to `Negotiator`, and routes payload to either `DataStreamParser` (3270) or VT100 parser when ASCII mode active.
- `Negotiator` manages Telnet option WILL/DO/WONT/DONT and TN3270E subnegotiations (DEVICE-TYPE, FUNCTIONS, RESPONSE-MODE, USABLE-AREA) plus compatibility fallbacks.
- `ScreenBuffer` stores either EBCDIC (default) or raw ASCII bytes when ASCII mode toggled.

## Key Flows
1. Connect -> perform Telnet negotiation (initial WILL TTYPE) -> respond to DOs (BINARY, EOR, TTYPE, {misused NEW-ENVIRON}) -> TTYPE SEND triggers IS reply -> optionally TN3270E negotiation -> data phase.
2. ASCII Detection: During `_process_telnet_stream`, VT100 sequences or high printable ASCII density triggers `set_ascii_mode()`. Handler then exclusively uses VT100 path.

## Detection Heuristics
- VT100 sequences: ESC '[' / '(', ')' '#', 'D', 'M', 'c', '7', '8'.
- Density heuristic: length ≥ 32 and ≥ 70% printable ASCII.

## Compatibility Adjustments
- NEW_ENVIRON (0x27) now fully implemented per RFC 1572: variable/value parsing and proper IS/SEND/INFO handling. TERM reflects configured terminal type.
- Accept legacy TN3270E option (0x1B) though RFC defines 0x28.

## Mode Switching Guarantees
- Once ASCII mode set: no further 3270 parsing attempted for that handler instance.
- ScreenBuffer converts existing EBCDIC spaces (0x40) to ASCII spaces (0x20) when switching.

## Trace & Diagnostics
- Recorder hooks in Negotiator: telnet(command, option), decision(requested, chosen, fallback), error(message).

## Extensibility Points
- Additional Telnet options can be inserted in `_handle_do` / `_handle_will`.
- Terminal type is configurable via `Session`/`AsyncSession(terminal_type=...)` and propagated through `TN3270Handler` → `Negotiator`.

## Pending Enhancements
- Snapshot-based screen parity tests vs reference host.
