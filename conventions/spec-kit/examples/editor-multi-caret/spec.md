<!-- source: editor-multi-caret — https://raw.githubusercontent.com/tui-cs/Editor/develop/specs/multi-caret/spec.md -->
# Feature Specification: Multi-Caret Editing

**Status**: Done — shipped in PR #105 + selection fix PR #121 (merged into `develop` 2026-05-14); issue #103 closed. Vertical extension shipped separately — see [vertical-multi-caret](../vertical-multi-caret/spec.md).
**Created**: 2026-05-10
**Last updated**: 2026-05-17
**Depends on**: caret-anchors ✅
**Blocked by**: —

## Overview

Add multi-caret support to the Editor. Expose `IReadOnlyList<int> AdditionalCaretOffsets` alongside the primary caret. All editing commands run inside a single `Document.OpenUpdateScope ()` so that undo collapses multi-caret edits into one step. Each additional caret has its own selection. The rendering pipeline paints all carets and selections via `IBackgroundRenderer` and `UpdateCursor ()`.

## User Scenarios

### Scenario 1 — Ctrl+Click adds a caret

**Given** the editor has a single caret at line 3, **When** the user Ctrl+Clicks on line 7, **Then** a second caret appears at the clicked position on line 7 and the original caret remains on line 3.

### Scenario 2 — Typing inserts at every caret

**Given** two carets at offsets 10 and 50, **When** the user types "abc", **Then** "abc" is inserted at both positions and both carets advance by 3.

### Scenario 3 — Undo collapses multi-caret edits

**Given** a multi-caret edit that typed "xyz" at 3 carets, **When** the user presses Ctrl+Z, **Then** all three insertions are undone in a single undo step.

### Scenario 4 — Selection per caret survives editing

**Given** two carets, each with an independent selection, **When** the user types a character, **Then** each selection is replaced by the typed character at its respective position.

## Requirements

- **FR-001**: `Editor` exposes `IReadOnlyList<int> AdditionalCaretOffsets`.
- **FR-002**: Editing commands run inside `Document.OpenUpdateScope ()` to collapse undo.
- **FR-003**: Ctrl+Click adds/removes additional carets.
- **FR-004**: Each additional caret has its own independent selection.
- **FR-005**: `IBackgroundRenderer` paints all carets and selections.
- **FR-006**: `UpdateCursor ()` accounts for multiple carets.
- **FR-007**: R5 (multi-caret rule from the plan) enforceable.

## Files in Scope

- `src/Terminal.Gui.Editor/Editor.cs`
- `src/Terminal.Gui.Editor/Editor.Commands.cs`
- `src/Terminal.Gui.Editor/Editor.MultiCaret.cs` (new)
- `src/Terminal.Gui.Editor/Rendering/` (background renderer updates)

## Definition of Done

- [ ] Ctrl+Click adds a caret (demonstrated in ted)
- [ ] Typing inserts at every caret position
- [ ] Undo collapses multi-caret edits into a single step
- [ ] Selection per caret survives editing
- [ ] ted demo can demonstrate Ctrl+Click multi-caret typing + undo

## Out of Scope

- Sticky Column Selection Mode — VS Code's modal toggle where ordinary clicks/arrows keep column-select behavior until disabled. The drag and keyboard column-selection gestures are in scope for `specs/vertical-multi-caret/spec.md`; the persistent mode with menu/status UI is a separate follow-up.
- Multi-caret find/replace

## Notes

- Blocked on caret-anchors (anchor-backed caret) — multi-caret is meaningfully simpler when the primary caret is already an anchor.
- All additional carets should also be `TextAnchor` instances.
