# Watchlist

These are adjacent conventions, drafts, or protocol surfaces that are not full
entries yet. A watchlist item is not a rejection; it means the project needs
live examples, demonstrated readers, or a more stable spec before cataloging it
as a convention.

Last reviewed: 2026-06-21.

## Strong candidates

### `agents.txt` / `agents.json`

- Status: Internet-Draft / proposed site-level capability declaration.
- Why watch: It overlaps with agent-web discovery and may complement `ai.txt`,
  `llms.txt`, and A2A Agent Cards.
- Why not listed yet: Need live site examples and evidence that real agents
  fetch it before acting.
- Promotion bar: at least two independent public deployments plus one reader or
  tool that documents consumption.

### MCP server cards

- Status: Emerging discovery surface for MCP servers.
- Why watch: It could become the MCP equivalent of an Agent Card.
- Why not listed yet: The committed-file convention and client behavior need
  clearer, stable public examples.
- Promotion bar: published spec plus public examples served from real MCP
  providers.

### AIPREF vocabulary and attachment

- Status: IETF AI Preferences Working Group drafts.
- Why watch: It may supersede or sit beside root-file AI preference files.
- Why not listed yet: It is a protocol/vocabulary layer rather than a committed
  file convention in this repo's current sense.
- Promotion bar: stable attachment mechanism with visible deployment and crawler
  handling.

### Agent Identity Discovery (AID)

- Status: Internet-Draft / DNS and well-known discovery proposal.
- Why watch: It may become a useful identity layer for agents and protocols.
- Why not listed yet: The primary mechanism is DNS TXT, not a repo/site file, and
  adoption evidence is early.
- Promotion bar: real providers publishing records plus consuming clients.

## Lower-confidence items

### `agent-manifest.txt`

- Status: Community proposal with namespace overlap.
- Why watch: It tries to declare AI-agent capabilities for websites.
- Why not listed yet: Naming is crowded and the relationship to `agents.txt` is
  unsettled.

### AI usage headers

- Status: Drafts and vendor-specific approaches.
- Why watch: Headers may be a stronger fit than files for content-use
  preferences.
- Why not listed yet: This repo catalogs files an agent reads, writes, or acts
  on; headers are adjacent but outside the current inclusion filter.

### `PLAYBOOK.md`

- Status: Single-team, in-production convention (surfaced via community feedback).
- Why watch: A procedures/runbook file paired with `CLAUDE.md`-style policy. Same
  read-only, enforced role, but a distinct function: how to run the cycle (call
  order, dedup logic, crash recovery) rather than identity and rules.
- Why not listed yet: No adoption evidence beyond one team's system, and no tool
  reads it by name.
- Promotion bar: a few independent public repos committing `PLAYBOOK.md`, or a
  tool that reads it by name.

## How to promote an item

Open an issue with:

- The proposed file name or path.
- Public examples, preferably raw URLs.
- A spec or canonical documentation URL.
- Evidence of readers: which agent/tool fetches it and when.
- License/permission notes for any example to be vendored.
