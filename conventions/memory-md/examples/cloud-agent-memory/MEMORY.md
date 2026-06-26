<!-- source: cloud-agent-memory — https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/Memory.md -->
# Memory: Evolving Playbook (ACE Framework)

This memory file acts as an evolving playbook that accumulates, refines, and organizes strategies for all projects.

**Instructions:**

- **ACE Workflow**: For every task, operate through the roles of **Generator** (execute task), **Reflector** (analyze success/failure), and **Curator** (propose memory updates).
- **Immediate Retrieval**: Identify the repository and **immediately fetch** the corresponding repo-specific memory file — do not ask for permission.
- **Preserve Detail**: Do not summarize or compress existing rules; use itemized bullets to preserve specific domain knowledge.
- **Mandatory Session Close**: You MUST conclude every session with one of:
  - `UPDATE_NEEDED` — one or more Memory Update issue links (one per insight per the Multi-Update Rule below).
  - `CLEAN_RUN` — a single sentence describing what made this run frictionless, after honestly completing the Reflector checklist (Section 1).
- **Multi-Update Rule**: If a task yields multiple insights (e.g., a code snippet AND a troubleshooting tip), create separate issues for each to maintain modularity.

## Global Playbook (Strategies & Hard Rules)

- **Commit Author Identity**: All commits MUST include the author flag: `--author="Prithpal Sooriya <prithpal.sooriya@gmail.com>"`. When amending commits, always verify the author is set correctly.
- **Traceability**: PRs must include the Jira ticket and GitHub issue link.
- **Minimal Scoping**: Modifications must be scoped and minimal to avoid regression.
- **Validation**: Ensure unit tests pass before requesting a memory update.

## Repository Specifics

Fetch and follow the itemized strategies for each domain:

- **MetaMask/core:** [https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/MetaMask/metamask-core.md](https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/MetaMask/metamask-core.md)
- **MetaMask/metamask-extension:** [https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/MetaMask/metamask-extension.md](https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/MetaMask/metamask-extension.md)
- **MetaMask/metamask-mobile:** [https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/MetaMask/metamask-mobile.md](https://raw.githubusercontent.com/Prithpal-Sooriya/Cloud-Agent-Memory/main/MetaMask/metamask-mobile.md)

---

## Agentic Memory Update Process (Reflect & Curate)

When you complete a task or encounter a failure, perform a **Reflection** to extract concrete lessons and a **Curation** to propose a **Delta Update**.

### 1. Perform Reflection (The "Reflector" Role)

Open-ended introspection ("did it go well?") is not acceptable — it produces false-positive `CLEAN_RUN` verdicts and loses the real lessons. You MUST answer each of the following with **concrete evidence from this session's execution trace**. If an answer truly is "none", say so explicitly and name what you checked.

1. **Backtracks**: List every moment you abandoned an approach and tried something different. For each, cite the tool call (or reasoning step) and the trigger that caused the pivot.
2. **Stuck windows**: List any stretch of ≥3 consecutive tool calls where you were debugging the same problem. What unblocked you? Was the unblock something a playbook rule could have shortcut?
3. **Errors absorbed**: List every non-zero exit, failed test, lint failure, or tool error. For each, was it preventable with a new or existing playbook rule?
4. **Playbook rules applied**: For each rule ID you actually relied on (not just read), state whether it produced the intended outcome. If any rule misled you, flag it for an UPDATE that supersedes or corrects the rule.
5. **Verdict**: Conclude with exactly one of:
   - `UPDATE_NEEDED` — proceed to Curation (Section 2) and file one issue per insight.
   - `CLEAN_RUN` — single sentence naming what made the run frictionless. The user will challenge this if it looks like a no-op; only use when items 1–4 genuinely produced nothing.

**Mid-session checkpoint** (recommended): if you've spent ≥5 tool calls debugging the same error, pause and jot a one-line reflection candidate before continuing. Lessons fade fast once the blocker is resolved.

### 2. Curate a Delta Update (The "Curator" Role)

Pick an **Operation Type**:

- **ADD**: For entirely new insights missing from the playbook. Use `[shr-NEW]` / `[code-NEW]` / `[ts-NEW]` as the placeholder ID — the curator (human) will assign the real ID at merge time. This avoids ID collisions across parallel agent runs.
- **UPDATE**: To modify an existing rule (refine wording, supersede with a corrected version). Reference the existing ID directly.
- **No DELETE**: Per ACE, do not delete entries. If an entry is obsolete or wrong, UPDATE it with a corrected version. This preserves the negative-knowledge signal.

### 3. Create the Memory Update Issue

There are two supported flows. **Prefer the `gh` CLI when shell access is available** — it sets all labels in one shot and avoids URL encoding the markdown body.

#### Flow A — `gh` CLI (preferred for cloud agents)

````bash
gh issue create \
  --repo Prithpal-Sooriya/Cloud-Agent-Memory \
  --title "Memory Update: [UPDATE] Refine memory limits" \
  --label memory-update \
  --label metamask-extension \
  --body-file - <<'EOF'
## Memory Delta Update Request

**Repository:** MetaMask/metamask-extension
**Operation:** UPDATE
**Section:** TS
**Target ID:** ts-001

### Reasoning
The previous limit in [ts-001] caused a stack overflow on the CI runner
during the integration suite. Bumping to 8192 resolved it; logs attached.

### Proposed Entry (Copy-Paste Ready)
```markdown
- **[ts-001] Memory-Efficient Testing**: Prepend NODE_OPTIONS=--max-old-space-size=8192 to prevent CI timeouts on integration runs.
```

### Evidence
- Failing run: https://github.com/.../actions/runs/123
- Fix commit: <sha>
EOF
````

Labels (always pass both):

- `memory-update` (always)
- One of `metamask-core`, `metamask-extension`, `metamask-mobile` (matches the target repo)

#### Flow B — Issue template via web UI (humans, or agents without shell)

The form (defined in `.github/ISSUE_TEMPLATE/memory-update.yml`) has dropdowns for Repository / Operation / Section and required fields for Reasoning / Proposed Entry.

**The agent / human building the URL MUST include the repo label** via the `labels` query parameter — the URL is the only way to attach it ahead of submission. The template auto-applies `memory-update`; the URL must add the matching repo label (`metamask-core`, `metamask-extension`, or `metamask-mobile`).

Base URL shape:

```
https://github.com/Prithpal-Sooriya/Cloud-Agent-Memory/issues/new?template=memory-update.yml&labels=memory-update,<repo-label>
```

Concrete example for a `metamask-extension` update:

```
https://github.com/Prithpal-Sooriya/Cloud-Agent-Memory/issues/new?template=memory-update.yml&labels=memory-update,metamask-extension
```

**Optional — prefill form fields**: GitHub Issue Forms accept query parameters matching each field's `id`, so the agent can pre-populate the whole form. Useful keys (URL-encode values; `/` → `%2F`, spaces → `+`):

- `title=Memory+Update%3A+%5BUPDATE%5D+Refine+memory+limits`
- `repository=MetaMask%2Fmetamask-extension`
- `operation=UPDATE`
- `section=TS+%E2%80%94+Troubleshooting+and+Pitfalls` (must match the dropdown option text exactly)
- `target_id=ts-001`
- `reasoning=...`
- `proposed_entry=...`
- `evidence=...`

A fully-prefilled URL is long but valid; the human reviewer just confirms and clicks Submit.

#### Body schema (canonical)

Whichever flow is used, the issue body should follow this shape (mirrored in `.github/ISSUE_TEMPLATE/memory-update.md`):

````markdown
## Memory Delta Update Request

**Repository:** [e.g., MetaMask/metamask-extension]
**Operation:** [ADD | UPDATE]
**Section:** [SHR | CODE | TS]
**Target ID:** [existing ID for UPDATE; `NEW` for ADD]

### Reasoning

[Concrete root cause anchored in this session's trace.]

### Proposed Entry (Copy-Paste Ready)

```markdown
- **[shr-NEW] Title**: Actionable instruction or insight here.
```

### Evidence

[Links to logs, errors, commits, PRs.]
````

### 4. Grow-and-Refine Note

Always share the issue URL with the user. The user acts as the final gate for merging these **Delta Entries** — including assigning real IDs to `[*-NEW]` placeholders and replacing the old bullet on UPDATEs.
