<!-- source: editor-constitution — https://raw.githubusercontent.com/tui-cs/Editor/develop/specs/constitution.md -->
# tui-cs/Editor Constitution

**Version**: 1.0 | **Ratified**: 2026-05-10 | **Last Amended**: 2026-05-10

This constitution governs all contributions to `tui-cs/Editor`. It is the highest-authority document in the repository — PRs that violate it are rejected with a link to the specific rule.

---

## I. Purpose & Scope

`Terminal.Gui.Editor` — UI-framework-independent document model lifted from AvaloniaEdit. **Must not reference Terminal.Gui.**

`Terminal.Gui.Editor` — `Editor : View` consuming `Terminal.Gui.Editor`, rendering on a cell grid. References `Terminal.Gui` (version pinned via `$(TerminalGuiVersion)` in `Directory.Build.props`).

The boundary matters: anything that depends on `Terminal.Gui` types belongs in `Terminal.Gui.Editor`, never in `Terminal.Gui.Editor`.

`Editor` is **not** a replacement for `TextView`. Both ship side-by-side. No source-compat obligation.

## II. Non-Goals

These were considered and rejected — do not accidentally pursue them:

- Backwards-compat with `Terminal.Gui.TextView`.
- RTL bidi or shaping beyond grapheme width.
- Pixel/proportional font fidelity. Width is measured in cells via `string.GetColumns ()`.
- Ports of AvaloniaEdit's `Editing/`, `Rendering/`, `CodeCompletion/` namespaces — those are Avalonia-UI-specific and replaced by TG-native equivalents.

## III. Tenets

### This Is Fun

While customers may take what we build seriously, we do this for fun, and we insist on using levity and humor — often cutting — throughout. The beatings will continue until morale improves.

We do this with a modicum of respect and a desire to not offend. We like names and terms that reference humorous cultural touchstones such as Monty Python.

### Excellent Engineering

Developers — AI agents and humans — working on this project strive to raise the bar as Principal Engineers. Principal Engineers are measured by how they live the [Amazon PE Community Tenets](https://www.amazon.jobs/content/en/teams/principal-engineering/tenets):

1. **Exemplary practitioner** — set the standard through your own work.
2. **Technically fearless** — tackle the hardest, most ambiguous problems.
3. **Lead with empathy** — foster inclusion; be mindful of your impact.
4. **Balanced and pragmatic** — neither dogmatic nor reckless.
5. **Illuminate and clarify** — bring clarity to complexity; drive crisp decisions.
6. **Flexible in approach** — adapt style and methods to the problem at hand.
7. **Respect what came before** — appreciate existing systems; learn from the past.
8. **Learn, educate, and advocate** — pursue continuous learning and teach others.
9. **Have resounding impact** — results are the minimum; lasting impact is the bar.

### Delightful Customer Experience

`TG.Editor` serves four customers, listed in the order in which tradeoffs are made:

1. End customers using `TG.Edit` to edit files in their terminals.
2. Human developers building TG apps.
3. Agentic developers building TG apps.
4. Maintainers, human or agentic, of TG.

### This Is TG

`TG.Editor` is an extension of TG, not independent of it. We follow the tenets of TG (see the TG deep dives), and we do not hack around TG limitations. We work to engineer correct fixes.

Short-term workarounds are allowed when they are the right product tradeoff, but if we use one, we also file a great TG issue that includes clear repros or unit tests that would fail.

### Performance Matters

`TG.Edit` is a TUI editor, and customers expect it to be snappy. We strive to always improve performance, both real and perceived.

We build automated benchmarking, and with each PR we strive to never make performance worse.

### TG Is Successful Because of .NET

We bet on .NET — and to some extent C# — and strive to remain great citizens of the .NET community. We are eager to leverage the latest features while balancing backwards compatibility.

## IV. Architectural Rules

Every PR must comply. Reviewers (human or agent) must reject violations and cite the rule number.

### R1 — No new feature draws directly inside `OnDrawingContent`

Visual features land as an `IVisualLineTransformer` (changes attributes on element ranges) or `IBackgroundRenderer` (paints cell rectangles). `OnDrawingContent` is a thin walker over `CellVisualLine` and stops growing.

### R2 — Cells, not chars

All width math goes through grapheme clusters + `Rune.GetColumns ()` / `string.GetColumns ()`. No `for (int i = 0; i < text.Length; i++)` over rendered text. No `c.ToString ()` per char.

### R3 — Public API mirrors AvaloniaEdit names

`IndentationSize`, `ConvertTabsToSpaces`, `ShowTabs`, `IIndentationStrategy`, `IFoldingStrategy`, `ISearchStrategy`. The wrapper is *superficial*. Bespoke names (`TabWidth`, custom enums) need a written justification in `specs/decisions.md`.

### R4 — Caret-after-edit must use `TextAnchor`

Use `AnchorMovementType.AfterInsertion`. Hand-rolled offset arithmetic stays only until caret-anchors lands; no new caret-positioning code may depend on it.

### R5 — Multi-step edits run inside `Document.OpenUpdateScope ()`

Undo collapses to one user-visible step. No exceptions for "small" multi-edits.

### R6 — Lifted upstream files keep upstream formatting

Preserve original formatting + copyright headers. Add `// Adapted for Terminal.Gui from AvaloniaEdit <sha>`. Log every modification in `third_party/AvaloniaEdit/UPSTREAM.md`. House-style only applies to non-`third_party/`-derived files.

### R7 — All test projects run in parallel; never touch process globals

Every test project — including `Editor.IntegrationTests` — runs in parallel. `AppFixture<T>` boots a per-test `IApplication` from `Application.Create()`, whose state is `ThreadLocal<>`-isolated. **Tests must not** call the static `Application.Init()` shortcut, must not call `ConfigurationManager.Enable()`, and must not mutate any `static` state that Terminal.Gui itself reads (`Logging.Logger`, `Trace.EnabledCategories`, etc.). A test that legitimately must mutate a process-global opts out via `[CollectionDefinition(name, DisableParallelization = true)]` + `[Collection(name)]` (see `HostingTests`); this is the exception, never the default.

Promote a new test to `Editor.IntegrationTests` only when an `IApplication` (driver, input injection, layout/draw) is genuinely needed.

### R8 — Public API additions come with a spec brief

New public API on `Editor` requires a brief in `specs/public-api.md` before merge. Stopgaps are explicitly marked `[Obsolete]` at introduction.

### R9 — No unused public/internal APIs in `src/`

If a public or internal member exists, something in `src/` or `examples/` must call it. **Tests don't count as a consumer.** If the API is a future affordance, leave it out until the consumer is ready.

**AvaloniaEdit lifts are not exempt.** A lift PR must include the `Terminal.Gui.Editor` integration *and* the `examples/ted` wiring that exercises the lifted surface in the same change — pure plumbing is not a complete feature. The principle: a customer (end-user of ted, developer using `Editor`, or maintainer) must be able to *experience* the new capability via the demo app the moment the PR merges. If the lift introduces three new search modes, ted gains three new toggles; if the lift adds folding, ted shows a fold marker; if the lift adds an indentation strategy, ted's Enter key auto-indents.

When the work is too big to merge atomically, split it horizontally (smaller user-visible slices), not vertically (model first, view later). Lift the regex *with* the regex toggle UI. Lift folding *with* fold-marker rendering. Never land a layer that ted does not call.

### R10 — Subscribe to `-ed` events, not `-ing`

Terminal.Gui exposes paired events (`Accepting`/`Accepted`, etc.). Use the `-ed` variant unless your handler reads or sets `e.Cancel` / `e.Handled`.

## V. AvaloniaEdit Fork Policy

Code is lifted from AvaloniaEdit into `src/Terminal.Gui.Editor/` subfolders. The pinned upstream commit and per-file modification log live in `third_party/AvaloniaEdit/UPSTREAM.md`.

For lifted files:

- **Preserve original formatting and copyright headers.**
- Add `// Adapted for Terminal.Gui from AvaloniaEdit <commit-sha>`.
- Targeted edits only: strip `using Avalonia.*`, remove `Dispatcher.UIThread.VerifyAccess ()`, replace `IBrush`/`Avalonia.Media.Color` with `Terminal.Gui.Color`, drop typeface/font-size from `HighlightingColor`.
- Log every modification in `UPSTREAM.md`.

The fork is **hard** — re-syncs are manual and deliberate, triggered only by upstream fixes we want.

## VI. Testing Tiers

Four test projects mirroring Terminal.Gui's convention:

| Project | Workflow | OS matrix | Purpose | Coverage Target |
|---------|----------|-----------|---------|-----------------|
| `Terminal.Gui.Editor.Tests` | `ci.yml` | ubuntu, macos, windows | Pure, no UI, no static state | ≥ 90% |
| `Terminal.Gui.Editor.IntegrationTests` | `ci.yml` | ubuntu, macos, windows | Full key-input → render via `AppFixture<T>` (per-test `IApplication.Create()`) | Informational |
| `Terminal.Gui.Editor.PerformanceTests` | `perf.yml` | ubuntu only, Release only | Stopwatch perf smoke tests + BenchmarkDotNet baseline gate | Wall-time guards |

The three correctness projects run **in parallel** within each assembly. The lone exception: a class that mutates a process-global static (e.g. `HostingTests`) opts out of cross-collection parallelism via `[CollectionDefinition(..., DisableParallelization = true)]` + `[Collection(...)]`. Never disable parallelism at the assembly level.

`PerformanceTests` lives in its own workflow because Windows / macOS GitHub-hosted runners share hosts with neighbour VMs — wall-time assertions there are too noisy to gate on. Ubuntu runners are still noisy but consistent enough that a >3× BenchmarkDotNet baseline ratio is a real signal. The full BenchmarkDotNet matrix runs only on `workflow_dispatch` (`full-suite: true`); that's the operator path for refreshing `benchmarks/baseline.json`.

Tests run as **executables** (xUnit.v3): `dotnet run --project tests/<project>`. `PerformanceTests` always runs with `-c Release`.

## VII. Coding Standards

See `CLAUDE.md` for the full style guide. Key points:

- Space before `()` and `[]`: `Method ()`, `array [i]`.
- Allman braces everywhere.
- `var` for built-ins only; explicit types otherwise.
- `field` keyword for property backing (C# 13), not `_backingField`.
- Block-bodied methods; expression-bodied properties.
- Guard clauses over nested `if`.
- Collection expressions `[...]` over `new[] { ... }`.

## Governance

This constitution supersedes all other practices. Amendments require:

1. A written proposal in a PR touching this file.
2. Review and approval from the project maintainer.
3. A migration plan for any existing code that would be out of compliance.

## VIII. Naming Convention for Specs & Features

Every feature, work item, and spec directory must have a plain English name that a customer — whether an end-user of ted, a developer using `Editor` to build something, or a maintainer — would instantly recognize and understand.

- **No letter+number codes.** Names like "A1", "B2", "D7" are opaque. Use descriptive English: `folding`, `clipboard`, `find-and-replace`, `drawing-overhaul`.
- **Lowercase kebab-case** for directory names: `specs/word-wrap/spec.md`, not `specs/B3-word-wrap/`.
- **Title-case** in document headings: "Feature Specification: Word Wrap", not "Feature Specification: B3".
- **Cross-references use the English name**, never an ID: "depends on rendering-pipeline", not "depends on B1".
- If a feature needs a qualifier to distinguish layers (model vs. UI), use a natural suffix: `folding` (the model) vs. `folding-ui` (the editor UI).
