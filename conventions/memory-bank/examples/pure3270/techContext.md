<!-- source: pure3270 — https://raw.githubusercontent.com/dtg01100/pure3270/main/memory-bank/techContext.md -->
# Tech Context

## Languages & Versions
- Python 3.11+ targeted; README references 3.10 minimum. Dev container includes Python 3.12.

## Dependencies
- Runtime: Standard library only.
- Dev/Test (optional): pytest, pytest-asyncio, black, flake8, coverage. Not always installable in restricted environment; quick smoke script used as fallback.

## Key Modules
- `pure3270/protocol/negotiator.py`: Telnet + TN3270E option handling, subnegotiations, ASCII mode flag bridging.
- `pure3270/protocol/tn3270_handler.py`: Stream processing, IAC parsing, VT100 detection, dispatch.
- `pure3270/emulation/screen_buffer.py`: Unified buffer for EBCDIC or ASCII. Fields & attributes for 3270 mode.
- `pure3270/p3270_client.py`: Native p3270-compatible facade.

## Testing Strategy
- `quick_test.py`: Always runnable, covers imports, native client, navigation methods, mock connectivity, ASCII detection.
- Pytest suite (optional) includes fuzz, negotiation, emulation, protocol, VT100 offline tests.

## Negotiation Edge Cases
- Host sends repeated TTYPE SEND until client replies with IS (now uses configured `terminal_type`).
- NEW_ENVIRON implemented per RFC 1572: TERM and env var parsing handled correctly.

## Limitations
- No persistent snapshot of actual host login screen yet.
