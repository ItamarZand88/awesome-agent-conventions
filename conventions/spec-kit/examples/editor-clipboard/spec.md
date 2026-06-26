<!-- source: editor-clipboard — https://raw.githubusercontent.com/tui-cs/Editor/develop/specs/clipboard/spec.md -->
# Feature Specification: Clipboard (Cut / Copy / Paste)

**Status**: Done — shipped in PR #107 (merged into `develop` 2026-05-13); issue #101 closed
**Created**: 2026-05-10
**Last updated**: 2026-05-17
**Depends on**: None
**Blocked by**: None

## Overview

Implement Cut (Ctrl+X), Copy (Ctrl+C), and Paste (Ctrl+V) in the Editor using Terminal.Gui's `Clipboard` API. Operations are selection-aware: Copy and Cut operate on the current selection (or the current line if no selection). Cut and Paste use `Document.OpenUpdateScope ()` so each operation produces a single undo step.

## User Scenarios

### Scenario 1 — Copy selected text

**Given** text is selected, **When** the user presses Ctrl+C, **Then** the selected text is placed on the clipboard and the selection/document remain unchanged.

### Scenario 2 — Cut selected text

**Given** text is selected, **When** the user presses Ctrl+X, **Then** the selected text is placed on the clipboard and removed from the document in a single undo step.

### Scenario 3 — Paste replaces selection

**Given** text is selected and the clipboard has content, **When** the user presses Ctrl+V, **Then** the selection is replaced with the clipboard content.

### Scenario 4 — Paste with no selection

**Given** no text is selected and the clipboard has content, **When** the user presses Ctrl+V, **Then** the clipboard content is inserted at the caret position.

### Scenario 5 — Paste multi-line text

**Given** the clipboard contains multi-line text, **When** the user presses Ctrl+V, **Then** the text is inserted with correct line breaks.

### Scenario 6 — Cut produces one undo step

**Given** text is selected and cut, **When** the user presses Ctrl+Z, **Then** the cut is fully undone in a single step (text restored, selection restored).

## Requirements

- **FR-001**: Ctrl+C copies selected text to `Clipboard`.
- **FR-002**: Ctrl+X cuts selected text to `Clipboard` and removes it from the document.
- **FR-003**: Ctrl+V pastes clipboard content at caret or replacing selection.
- **FR-004**: Cut and Paste use `Document.OpenUpdateScope ()` for single-step undo.
- **FR-005**: When no selection exists, Copy/Cut operate on the current line (or are no-ops — [NEEDS CLARIFICATION]).
- **FR-006**: Multi-line paste inserts with correct line endings.

## Files in Scope

- `src/Terminal.Gui.Editor/Editor.Commands.cs`
- `src/Terminal.Gui.Editor/Editor.Keyboard.cs`
- Tests in `tests/Terminal.Gui.Editor.Tests/`

## Definition of Done

- [ ] Round-trip tests: copy → paste across selection cases
- [ ] Paste with multi-line text test passes
- [ ] Cut emits one undo step (single Ctrl+Z restores)
- [ ] ted demo Edit menu wires Cut/Copy/Paste commands

## Out of Scope

- Multi-caret clipboard behavior
- Rich text / format-preserving clipboard
- System clipboard fallbacks beyond Terminal.Gui's `Clipboard`

## Notes

- No dependencies — can be implemented at any time.
- FR-005 (no-selection behavior for Copy/Cut) is marked [NEEDS CLARIFICATION] — common editors copy the current line, but this should be a deliberate design choice.
