# Third-party examples

This repository vendors small, representative examples so readers can inspect the
actual files AI agents read and write. Those examples are evidence and teaching
material, not a relicensing of upstream work.

## What MIT covers

The root [MIT license](LICENSE) covers this repository's original curation,
scripts, metadata, generated prose, and maintainer-written notes.

## What MIT does not cover

Files under `conventions/*/examples/` are fetched from public upstream sources by
[`scripts/extract.py`](scripts/extract.py). Each file starts with a provenance
comment that links to its source. Copyright, license, trademark, and terms for
those example files remain with the upstream owner.

Before reusing an example outside this catalog, follow the provenance link and
check the upstream repository license or website terms.

To generate a current local summary, run:

```bash
make license-report
```

## Current upstream license mix

The catalog intentionally samples the real ecosystem, so the upstream sources
are mixed:

| Source type | Examples in this repo |
| --- | --- |
| Permissive or public-domain repos | Apache-2.0, MIT, MIT-0, and CC0 projects such as OpenAI Codex, Apache Airflow, Microsoft VS Code, GitHub Spec Kit, and A2A samples. |
| Copyleft repos | AGPL/GPL projects such as Warp, Gitpod, and WordPress Calypso. |
| No license detected / unavailable via GitHub API | Some public examples from repos such as `modelcontextprotocol/servers`, `getsentry/sentry`, `ag-grid/ag-grid`, `holochain/holochain`, `inspec/inspec`, and a few archived or inaccessible sources. |
| Direct website pages | `llms.txt`, `pricing.md`, and `auth.md` examples fetched from public site URLs. |

That mix is why this notice exists: the catalog can be MIT while individual
examples keep their own upstream rights.

## Contributor rule

When adding an extracted example, include enough evidence in the PR for a
maintainer to evaluate reuse risk: upstream URL, detected license or terms, and
why vendoring the file is preferable to linking it as a pattern. If in doubt,
use a pattern entry with live links instead of copying the file into `examples/`.
