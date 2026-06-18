# Open-source launch checklist

Use this once, right before flipping the repository from private to public.

## Local verification

- [ ] Run `make install`.
- [ ] Run `make open-source-check`.
- [ ] Run `make license-report` and review copyleft / unclear / website rows.
- [ ] Run a final secret scan with your preferred scanner if available
      (`gitleaks`, GitHub secret scanning, or equivalent).
- [ ] Check `git status --short` and make sure only intended launch changes are present.

## GitHub settings

- [ ] Make the repository public from GitHub's UI.
- [ ] Enable private vulnerability reporting.
- [ ] Enable Dependabot alerts and security updates.
- [ ] Add a default branch ruleset for `main`:
      require the `verify` workflow, block force-pushes, and block deletions.
- [ ] Keep Discussions enabled.
- [ ] Keep "Automatically delete head branches" enabled.
- [ ] Confirm labels exist: `new-convention`, `outdated`, `dependencies`,
      `documentation`, `enhancement`, `good first issue`, `help wanted`.

## Public profile

- [ ] Confirm the repository description is specific and search-friendly.
- [ ] Confirm topics include `awesome-list`, `agents-md`, `ai-agents`,
      `coding-agents`, `llms-txt`, `mcp`, and `prompt-engineering`.
- [ ] Confirm README badges render after the repo is public.
- [ ] Confirm GitHub's Community Standards page detects README, license,
      code of conduct, contributing, issue templates, PR template, and security policy.

## First public moments

- [ ] Create a `v0.1.0` release after the first green public CI run.
- [ ] Pin the launch discussion or issue for feedback.
- [ ] Invite reports for outdated conventions and missing adoption evidence.
- [ ] Avoid submitting to `sindresorhus/awesome` until the list is intentionally
      compatible with its stricter format rules.
