<!-- source: milo-solana-portfolio — https://raw.githubusercontent.com/and-milo/agent-to-agent-portfolio-manager/main/skill.md -->
---
name: milo
version: 1.0.0
description: Autonomous Solana portfolio management. Non-custodial wallets, auto-trading, market analysis, orders, transfers, and AI conversations.
---

# Milo Partner API Skill

Milo is an autonomous Solana portfolio manager. Through this API you can register users, create non-custodial wallets, send tokens, place buy/sell orders, manage positions, configure auto-trading strategies, and converse with Milo's AI agents.

## Getting Started — First-Time Onboarding

Follow these 4 steps to go from zero to a fully active Milo account.

### Step 1: Sign up

Request a SIWX message, sign it with your Solana wallet, and register.

```bash
# 1a. Get the message to sign
curl -X POST {{BASE_URL}}/api/v1/users/siwx/message \
  -H "Content-Type: application/json" \
  -d '{
    "accountAddress": "<your-wallet-address>",
    "chainId": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"
  }'

# 1b. Sign the returned "message" (UTF-8 bytes) with your ed25519 key, base58-encode the signature

# 1c. Register
curl -X POST {{BASE_URL}}/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "signupWallet": "<your-wallet-address>",
    "siwx": {
      "data": <data-object-from-1a>,
      "message": "<message-string-from-1a>",
      "signature": "<base58-signature-from-1b>"
    }
  }'
# → returns apiKey, user.id, wallets[] (save these to ~/.milo/config.json)
```

### Step 2: Ask Milo what's trending

Start a conversation with the market analyst to explore current opportunities.

```bash
# 2a. Create a conversation
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What tokens are trending right now on Solana?",
    "agentType": "market-analyst"
  }'
# → returns conversationId

# 2b. Poll for the response (wait 2-3s between polls)
curl "{{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages" \
  -H "X-API-Key: $API_KEY"
# → when processing: false, the agent has responded
```

### Step 3: Transfer funds to your Milo wallet

Deposit SOL to your Milo wallet so it has capital to trade. The Milo wallet address is `wallets[1].address` from signup (the `type: "milo"` wallet).

Send SOL from your external wallet to that address. Once funded, verify:

```bash
curl {{BASE_URL}}/api/v1/wallets/{walletId}/holdings \
  -H "X-API-Key: $API_KEY"
```

### Step 4: Activate auto-trading

Turn on Milo's autonomous trading agent. It will start scanning for opportunities within ~30 minutes.

```bash
curl -X PATCH {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "isActive": true,
    "riskTolerance": "balanced",
    "strategy": "SWING TRADER"
  }'
```

That's it — Milo is now managing your portfolio. Read on for the full feature guide and API reference.

---

## Feature Overview

> **Note:** You do NOT need to read this entire document. Use the guide below to jump to the relevant section for your task.

| If you need to... | Read section |
|---|---|
| **Look up your user ID and wallet IDs** | "Me" (under Complete API Reference) |
| **Register a new user / get an API key** | "First Boot Protocol" and "Signup" (under Complete API Reference) |
| **Activate or configure auto-trading** | "Recipe 2: Activate the auto-trader" and "Auto-Trade Settings" (under Complete API Reference) |
| **Create, link, or manage strategies** | "Strategies" (under Complete API Reference) |
| **Deploy and manage arena strategies** | "Arena" (under Complete API Reference) |
| **View quests and claim bones** | "Quests & Bones" (under Complete API Reference) |
| **Place, list, or manage orders** | "Orders" (under Complete API Reference) |
| **Send tokens to another wallet** | "Wallet Actions" (under Complete API Reference) |
| **Check positions, holdings, or PnL** | "Recipe 4: Fetch your positions" and "Portfolio" (under Complete API Reference) |
| **Chat with Milo's AI agents** | "Recipe 3: Talk with Milo" / "Recipe 6: Ask about a token" and "Conversations" (under Complete API Reference) |
| **Understand the full onboarding flow** | "Quick Start" and "First Boot Protocol" |
| **Set up a recurring portfolio check-in** | "Heartbeat Protocol" |

**Capabilities:**
- **Non-custodial Solana wallet** — Each user gets a Milo wallet (created via Turnkey). The user's signing key owns the wallet; Milo receives delegated permission to execute trades.
- **Auto-trading** — Configure risk tolerance, strategy, and asset allocation. Milo's auto-trader agent monitors markets and executes trades autonomously.
- **Orders** — Create limit, market, stop-loss, and take-profit orders on any Solana token.
- **Token transfers** — Send any SPL token or SOL from your Milo wallet to any Solana address.
- **Positions** — Track open positions with PnL data, close positions.
- **Arena** — Deploy public strategies to a competitive leaderboard. Milo funds an arena wallet and trades autonomously using the strategy. Withdraw to reclaim holdings.
- **Quests & Bones** — Complete quests (event-driven tasks like trades, signups) to earn bones (reward points). Check quests regularly and claim bones for completed quests.
- **AI conversations** — Chat with Milo's market analyst, auto-trader, or game agent. Async processing with polling.
- **Portfolio data** — Holdings, transactions, executed transactions, diary logs.

## Quick Start

1. **Get SIWX message** - Call `POST /api/v1/users/siwx/message` with your wallet address to get a message to sign.
2. **Register** - Sign the message with your wallet's ed25519 key, then call `POST /api/v1/users` with the signed SIWX proof to create a user and receive an API key + Milo wallet.
3. **Save credentials** - Store the API key, user ID, wallet ID, and wallet address in `~/.milo/config.json`.
4. **Deposit SOL** - Send SOL to your Milo wallet address (the `type: "milo"` wallet from signup).
5. **Activate auto-trader** - Call `PATCH /api/v1/users/{userId}/auto-trade-settings` with `{ "isActive": true }`.
6. **Fetch open quests** - Call `GET /api/v1/users/{userId}/quests` to see available quests. Claim bones for any completed quests.
7. **Start trading** - Create orders, chat with agents, or let the auto-trader manage your portfolio.

## Credential Storage

After signup, persist credentials locally so they survive across sessions:

```json
// ~/.milo/config.json
{
  "api_key": "mk_live_...",
  "user_id": "uuid",
  "wallet_id": "uuid",
  "wallet_address": "7xKXtg...",
  "base_url": "{{BASE_URL}}"
}
```

> **Warning:** In ephemeral environments (containers, serverless), this file may not persist. Use environment variables or a secrets manager instead.

All authenticated requests require the header:
```
X-API-Key: <api_key>
```
(NOT `Authorization: Bearer` — the API uses the `X-API-Key` header.)

## MCP Access

The partner API server exposes MCP on the same host at `/mcp` using Streamable HTTP:
- `POST /mcp` for initialize and JSON-RPC requests
- `GET /mcp` for SSE stream
- `DELETE /mcp` for session termination

`POST /mcp` initialize accepts optional `X-API-Key`. If omitted, the MCP session starts unauthenticated and only signup/public tools are usable until `signup` returns an API key. Request throttling and session-capacity protections are enforced, so initialize may return `429`. On `429`, respect `Retry-After` and retry after the indicated delay. Sessions can also expire, so re-initialize after invalid-session errors.

For sessioned requests after initialize, send `Mcp-Session-Id`.

## Wallet & Deposits

Milo creates a **non-custodial** Solana wallet for each user via Turnkey. The wallet-creating account is the owner; Milo receives delegated permission for trading.

On signup you receive two wallets:
- `type: "signup"` - Your external signing wallet (used for SIWX verification).
- `type: "milo"` - Your Milo trading wallet. **Deposit SOL here** for trading.

To check your wallet balance, use the holdings endpoint:
```bash
curl {{BASE_URL}}/api/v1/wallets/{walletId}/holdings \
  -H "X-API-Key: $API_KEY"
```

## First Boot Protocol

When starting fresh with no saved credentials:

1. **Generate a Solana keypair** for SIWX signing.
2. **Request a SIWX message from the server:**
   ```bash
   curl -X POST {{BASE_URL}}/api/v1/users/siwx/message \
     -H "Content-Type: application/json" \
     -d '{
       "accountAddress": "<your-wallet-address>",
       "chainId": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"
     }'
   ```
   This returns `{ "data": { ... }, "message": "<message-string>" }`. The `data` object contains all SIWX fields (domain, uri, nonce, etc.) and the `message` is the human-readable string to sign.
3. **Sign the message** — Sign the `message` string (UTF-8 encoded bytes) with your Solana keypair's ed25519 private key. Base58-encode the resulting signature.
4. **Register:**
   ```bash
   curl -X POST {{BASE_URL}}/api/v1/users \
     -H "Content-Type: application/json" \
     -d '{
       "signupWallet": "<your-wallet-address>",
       "siwx": {
         "data": <data-object-from-step-2>,
         "message": "<message-string-from-step-2>",
         "signature": "<base58-signature-from-step-3>"
       }
     }'
   ```
   **Important:** Pass the `data` and `message` exactly as returned by the server. Do not construct them manually.
5. **Save** the returned `apiKey`, `user.id`, and `wallets[1]` (the Milo wallet) to `~/.milo/config.json`.
6. **Deposit SOL** to the Milo wallet address.
7. **Configure auto-trade:**
   ```bash
   curl -X PATCH {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
     -H "X-API-Key: $API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "isActive": true,
       "riskTolerance": "balanced",
       "strategy": "SWING TRADER"
     }'
   ```

## Heartbeat Protocol

See [heartbeat.md]({{BASE_URL}}/heartbeat.md) for the recurring check-in protocol. Run every 4+ hours to stay informed about your portfolio.

---

## Cookbook — Working with Milo

This cookbook walks through the most common workflows end-to-end. Follow these recipes to get up and running quickly.

### Recipe 1: Get your API key

Before anything else you need credentials. Generate a Solana keypair, request a SIWX message from the server, sign it, and register.

```bash
# 1. Request a SIWX message to sign
curl -X POST {{BASE_URL}}/api/v1/users/siwx/message \
  -H "Content-Type: application/json" \
  -d '{
    "accountAddress": "<your-wallet-address>",
    "chainId": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"
  }'
# → returns { "data": { "data": { ... }, "message": "<message-to-sign>" } }

# 2. Sign the "message" string (UTF-8 bytes) with your ed25519 private key
#    Base58-encode the signature

# 3. Register with the signed proof
curl -X POST {{BASE_URL}}/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "signupWallet": "<your-wallet-address>",
    "siwx": {
      "data": <data-object-from-step-1>,
      "message": "<message-string-from-step-1>",
      "signature": "<base58-signature-from-step-2>"
    }
  }'

# 4. Save the response — you need these for every subsequent call
#    api_key  → Authorization header
#    user.id  → {userId} in routes
#    wallets[1].id      → {walletId} (the "milo" wallet)
#    wallets[1].address → deposit SOL here
```

Store credentials in `~/.milo/config.json` so they persist across sessions.

---

### Recipe 2: Activate the auto-trader

Once registered, turn on Milo's autonomous trading agent.

```bash
curl -X PATCH {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "isActive": true,
    "riskTolerance": "balanced",
    "strategy": "SWING TRADER",
    "instructions": "Focus on SOL ecosystem tokens. Avoid meme coins.",
    "customTickers": ["SOL", "JUP", "BONK"]
  }'
```

That's it — Milo will start monitoring markets and placing trades according to your configuration. You can verify it's active:

```bash
curl {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
  -H "X-API-Key: $API_KEY"
```

---

### Recipe 3: Talk with Milo about your investment strategy

Use the **auto-trader** agent to discuss, refine, or brainstorm your trading strategy. This is a conversation — Milo understands your portfolio context.

```bash
# 1. Start a conversation with the auto-trader
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I want to shift my strategy toward DeFi blue-chips. What allocation do you recommend for a balanced risk profile?",
    "agentType": "auto-trader"
  }'
# → returns { conversationId, processing: true }

# 2. Poll for the response (wait 2-3s between polls)
curl "{{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages" \
  -H "X-API-Key: $API_KEY"
# → when processing: false, the agent has responded

# 3. Continue the conversation
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "message": "Good plan. Apply those changes to my auto-trade settings." }'
```

**Tip:** The auto-trader agent can directly update your settings when you ask it to — it has tool access to modify your allocation, risk tolerance, and instructions.

---

### Recipe 4: Fetch your positions

Check what Milo is holding and how each position is performing.

```bash
# List all active positions with PnL
curl "{{BASE_URL}}/api/v1/users/{userId}/positions?status=active&page=1&pageSize=50" \
  -H "X-API-Key: $API_KEY"
```

Each position includes the token, entry price, current PnL, and thesis. Use `status=pending` for positions still being built, or omit the filter to get everything.

For a deeper look at your wallet's token balances:

```bash
curl {{BASE_URL}}/api/v1/wallets/{walletId}/holdings \
  -H "X-API-Key: $API_KEY"
```

---

### Recipe 5: Revalidate a position with Milo

Have Milo re-analyze an existing position to decide whether to hold, add, or exit.

```bash
# 1. Get the position's thesisId from the positions list (Recipe 4)
# 2. Start a conversation with the auto-trader, referencing the position
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Re-evaluate my position on JUP (thesis {thesisId}). Given the latest market conditions, should I hold, take partial profit, or close it entirely?",
    "agentType": "auto-trader"
  }'

# 3. Poll for the response
curl "{{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages" \
  -H "X-API-Key: $API_KEY"

# 4. If Milo recommends closing, you can close it directly:
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/positions/{thesisId}/close \
  -H "X-API-Key: $API_KEY"
```

---

### Recipe 6: Ask Milo about a specific token

Use the **market-analyst** agent for token research. It can pull market data, analyze trends, and give you a thesis.

```bash
# 1. Ask the market analyst about a token
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What do you think about RENDER? Give me a full analysis — fundamentals, technicals, and whether it fits my current portfolio.",
    "agentType": "market-analyst"
  }'

# 2. Poll for the response
curl "{{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages" \
  -H "X-API-Key: $API_KEY"

# 3. Follow up with more questions in the same conversation
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "message": "Compare it with RNDR vs HNT for a DePIN play. Which is the better entry right now?" }'
```

**Tip:** The market-analyst agent focuses on research and analysis. If you want Milo to actually execute a trade based on the analysis, either create an order manually or switch to the auto-trader agent.

---

### Putting it all together

A typical session with Milo looks like:

1. **Check in** — Fetch positions and holdings (Recipes 4)
2. **Strategize** — Talk to the auto-trader about adjusting your approach (Recipe 3)
3. **Research** — Ask the market analyst about tokens you're curious about (Recipe 6)
4. **Validate** — Revalidate existing positions with fresh analysis (Recipe 5)
5. **Act** — Let the auto-trader handle execution, or place manual orders via the Orders API

Run the [heartbeat protocol]({{BASE_URL}}/heartbeat.md) every 4+ hours to keep this cycle going automatically.

---

## Complete API Reference

### Authentication

All endpoints (except signup) require:
```
X-API-Key: <api_key>
```

### Me

#### GET /api/v1/me
Get the current user profile and wallets for the authenticated API key. Use this to discover your `userId` and `walletId` values.

```bash
curl {{BASE_URL}}/api/v1/me \
  -H "X-API-Key: $API_KEY"
```

**Response (200):**
```json
{
  "user": {
    "id": "uuid",
    "signupWalletId": "uuid",
    "provider": "siwx",
    "createdAt": "2025-01-01T00:00:00.000Z"
  },
  "wallets": [
    { "id": "uuid", "address": "<address>", "chain": "solana", "type": "signup" },
    { "id": "uuid", "address": "<address>", "chain": "solana", "type": "milo" }
  ]
}
```

---

### Signup

Signup is a two-step process: first request a SIWX message from the server, then sign it and submit the proof.

#### POST /api/v1/users/siwx/message
Generate a SIWX message for the wallet to sign. This is step 1 of signup.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/siwx/message \
  -H "Content-Type: application/json" \
  -d '{
    "accountAddress": "<wallet-address>",
    "chainId": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"
  }'
```

**Request body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `accountAddress` | string | yes | Solana wallet address (32-64 chars) |
| `chainId` | string | yes | CAIP-2 chain ID (e.g. `solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp`) |
| `inviteCode` | string | no | Optional invite code |

**Response (200):**
```json
{
  "data": {
    "data": {
      "accountAddress": "<wallet-address>",
      "chainId": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp",
      "domain": "andmilo.com",
      "uri": "https://andmilo.com",
      "version": "v1",
      "nonce": "<server-generated-nonce>",
      "issuedAt": "2025-06-15T12:00:00.000Z",
      "expirationTime": "2025-06-22T12:00:00.000Z",
      "statement": "By signing, you agree to andmilo Terms of Use..."
    },
    "message": "andmilo.com wants you to sign in with your Solana account:\n<wallet-address>\n\n..."
  }
}
```

Sign the `message` string (UTF-8 encoded bytes) with the wallet's ed25519 private key. Base58-encode the signature. Then proceed to step 2.

#### POST /api/v1/users
Create a new user via SIWX wallet verification. This is step 2 of signup.

```bash
curl -X POST {{BASE_URL}}/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "signupWallet": "<wallet-address>",
    "siwx": {
      "data": <data-object-from-siwx-message-response>,
      "message": "<message-string-from-siwx-message-response>",
      "signature": "<base58-ed25519-signature>"
    }
  }'
```

**Important:** Pass the `data` and `message` fields exactly as returned by `POST /api/v1/users/siwx/message`. Do not construct them manually.

**Response (200):**
```json
{
  "data": {
    "user": { "id": "uuid", "signupWalletId": "uuid", "provider": "siwx", "createdAt": "..." },
    "wallets": [
      { "id": "uuid", "address": "<address>", "chain": "solana", "type": "signup" },
      { "id": "uuid", "address": "<address>", "chain": "solana", "type": "milo" }
    ],
    "apiKey": "mk_live_..."
  }
}
```

---

### Auto-Trade Settings

#### GET /api/v1/users/{userId}/auto-trade-settings
Get current auto-trade configuration.

```bash
curl {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
  -H "X-API-Key: $API_KEY"
```

#### PATCH /api/v1/users/{userId}/auto-trade-settings
Update auto-trade configuration.

```bash
curl -X PATCH {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "isActive": true,
    "riskTolerance": "balanced",
    "strategy": "SWING TRADER",
    "instructions": "Focus on SOL ecosystem tokens",
    "customTickers": ["SOL", "JUP", "BONK"],
    "dataSources": { "fundingRates": true, "openInterest": true },
    "assetClassSettings": {
      "memes": { "dataSources": { "liquidationData": true } },
      "majors": { "dataSources": { "macroData": true } }
    }
  }'
```

**Settings fields:**
| Field | Type | Values |
|-------|------|--------|
| `isActive` | boolean | Enable/disable auto-trading |
| `riskTolerance` | string | `conservative`, `balanced`, `degen` |
| `strategy` | string | `VALUE INVESTOR`, `SWING TRADER`, `SCALPER`, `CUSTOM` |
| `strategyId` | uuid \| null | Link a saved strategy to auto-trade settings |
| `modelVersion` | string \| null | Preferred model |
| `instructions` | string | Free-text trading instructions for the agent |
| `customTickers` | string[] | Specific tokens to focus on |
| `allocation` | object | Asset class allocation percentages |
| `dataSources` | object \| null | Global data-source toggles: `fundingRates`, `openInterest`, `liquidationData`, `macroData` |
| `assetClassSettings` | object \| null | Per-asset-class configuration, including nested `dataSources` overrides |

**Asset classes for allocation:** `trenches`, `memes`, `promising-memes`, `staking`, `native`, `majors`, `stables`, `xStocks`, `custom`

Data-source resolution notes:
- Asset-class `dataSources` overrides win over top-level `dataSources`.
- If no override exists, the top-level value applies.
- Missing keys are treated as disabled.
- PATCH deep-merges `dataSources` both globally and inside `assetClassSettings`, so partial updates do not wipe sibling keys.

Model entitlement notes:
- Only canonical model ids are accepted on the partner surface.
- Canonical OpenAI model ids are `o3`, `gpt-5.2-high`, `gpt-5.2-xh`, and `gpt-5.4`.
- Canonical Anthropic model ids are `claude-opus-4.5` and `claude-opus-4.6`.
- Canonical Gemini model ids are `gemini-3-pro` and `gemini-3.1-pro-preview`.
- Canonical Grok model ids are `grok-4.1-fast-reasoning` and `grok-4`.
- If a model is unavailable for your account, the API returns `400 Bad Request` with `error.details.requiredPlan`, `error.details.upgradeUrl`, and an error message containing the same plan-specific Stripe link.

Data-source entitlement notes:
- Only `pro` and `max` users can create, update, apply, sync, or otherwise change `dataSources`.
- Free users can still read saved `dataSources` in GET responses.
- If an account downgrades, saved `dataSources` remain visible but are inactive in auto-trader chat, execution, and position review until the account is back on Pro or Max.
- When blocked, the API returns `400 Bad Request` with `error.details.feature = "dataSources"`, `error.details.requiredPlan = "pro"`, and upgrade details when available.

---

### Strategies

Strategies are reusable autotrade configurations that live under auto-trade settings. Create a strategy, link it to your settings, and sync when the strategy evolves.

**Workflow:**
1. **Create** a strategy with allocation, instructions, and trading approach.
2. **Link** it via `PATCH /auto-trade-settings` with `{ "strategyId": "<uuid>" }`. This takes a **snapshot** of the strategy into your settings.
3. **Use** — Milo auto-trades according to the snapshot.
4. If the strategy is updated later, the GET settings response includes `strategySync.synced: false`.
5. **Sync** — call `POST .../strategies/{strategyId}/sync` to re-apply the latest version.

#### POST /api/v1/users/{userId}/auto-trade-settings/strategies
Create a new strategy.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "SOL Ecosystem DCA",
    "description": "Dollar cost average into SOL ecosystem tokens",
    "strategy": "SWING TRADER",
    "instructions": "Focus on SOL, JUP, and BONK with balanced entries",
    "allocation": { "majors": 45, "native": 25, "staking": 10, "promising-memes": 15, "xStocks": 5 },
    "customTickers": ["SOL", "JUP", "BONK"],
    "dataSources": { "fundingRates": true, "openInterest": true },
    "assetClassSettings": {
      "memes": { "dataSources": { "liquidationData": true } },
      "majors": { "dataSources": { "macroData": true } }
    },
    "isPublic": false
  }'
```

**Response (201):**
```json
{
  "data": {
    "id": "uuid",
    "name": "SOL Ecosystem DCA",
    "strategy": "SWING TRADER",
    "allocation": { ... },
    "createdAt": "..."
  }
}
```

**Create/update fields:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | yes (create) | Strategy name (1-200 chars) |
| `description` | string \| null | no | Description (max 2000 chars) |
| `instructions` | string | no | Free-text instructions (max 4000 chars) |
| `strategy` | string | yes (create) | `VALUE INVESTOR`, `SWING TRADER`, `SCALPER`, `CUSTOM` |
| `allocation` | object | no | Asset class allocation percentages |
| `customTickers` | string[] \| null | no | Token tickers to focus on |
| `dataSources` | object \| null | no | Global data-source toggles carried into the strategy snapshot |
| `assetClassSettings` | object \| null | no | Per-asset-class configuration, including nested `dataSources` |
| `isPublic` | boolean | no | Make strategy publicly discoverable |

The same Pro/Max restriction applies when creating or updating a strategy with `dataSources`, and when syncing a linked strategy that already contains them.

#### GET /api/v1/users/{userId}/auto-trade-settings/strategies
List strategies with filters.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies?scope=owned&page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

**Query parameters:**
| Param | Values | Description |
|-------|--------|-------------|
| `scope` | `all`, `owned`, `public` | Filter by ownership |
| `q` | string | Search by name/description |
| `page` | number | Page number (default: 1) |
| `pageSize` | number | Items per page (default: 25, max: 100) |

#### GET /api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId}
Get strategy details.

```bash
curl {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId} \
  -H "X-API-Key: $API_KEY"
```

#### PATCH /api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId}
Update a strategy. All fields are optional.

```bash
curl -X PATCH {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId} \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Strategy Name",
    "instructions": "New instructions for the agent"
  }'
```

#### DELETE /api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId}
Delete a strategy.

```bash
curl -X DELETE {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId} \
  -H "X-API-Key: $API_KEY"
```

#### POST /api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId}/sync
Re-sync auto-trade settings with the linked strategy. Takes a fresh snapshot of the strategy's current allocation, instructions, and configuration.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId}/sync \
  -H "X-API-Key: $API_KEY"
```

**Strategy sync workflow:**

1. Link a strategy to your settings:
```bash
curl -X PATCH {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "strategyId": "<strategy-uuid>", "isActive": true }'
```

2. Check sync status (included in GET settings response):
```json
{
  "strategyId": "uuid",
  "strategySync": {
    "strategyId": "uuid",
    "synced": false,
    "strategyUpdatedAt": "2025-06-15T14:00:00.000Z",
    "settingsUpdatedAt": "2025-06-01T10:00:00.000Z"
  }
}
```

3. When `synced` is `false`, re-sync:
```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/auto-trade-settings/strategies/{strategyId}/sync \
  -H "X-API-Key: $API_KEY"
```

---

### Arena

Deploy a public strategy to the arena leaderboard. Milo creates a custody wallet, funds it, and trades autonomously using the strategy. The strategy must be public and owned by the user. Deployment requires at least 1 SOL balance (0.01 SOL in dev). Withdrawing transfers all holdings back to the user's Milo wallet.

#### POST /api/v1/users/{userId}/arena/deploy
Deploy a strategy to the arena.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/arena/deploy \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "strategyId": "<strategy-uuid>" }'
```

**Request body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `strategyId` | uuid | yes | ID of a public strategy owned by the user |

**Response (200):**
```json
{
  "data": {
    "arenaUserId": "uuid",
    "custodyWalletId": "uuid",
    "custodyWalletAddress": "<solana-address>",
    "fundingTxSignature": "<transaction-signature>",
    "strategyId": "uuid"
  }
}
```

#### POST /api/v1/users/{userId}/arena/withdraw
Withdraw from the arena. Transfers all holdings from the custody wallet back to the user's Milo wallet.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/arena/withdraw \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "strategyId": "<strategy-uuid>" }'
```

**Request body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `strategyId` | uuid | yes | ID of the deployed strategy to withdraw |

**Response (200):**
```json
{
  "data": {
    "arenaUserId": "uuid",
    "custodyWalletId": "uuid",
    "custodyWalletAddress": "<solana-address>",
    "recipientWalletAddress": "<solana-address>",
    "transferTxs": [
      { "tokenAddress": "<mint-address>", "amount": 1.5, "signature": "<tx-signature>" }
    ]
  }
}
```

#### GET /api/v1/users/{userId}/arena/leaderboard
Get the arena leaderboard.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/arena/leaderboard?timeframe=30d&page=1&pageSize=25&sortKey=pnl&sortDirection=desc" \
  -H "X-API-Key: $API_KEY"
```

**Query parameters:**
| Param | Type | Values | Default |
|-------|------|--------|---------|
| `timeframe` | string | `1d`, `30d`, `90d` | — |
| `page` | number | Page number | 1 |
| `pageSize` | number | Items per page (max: 100) | 25 |
| `sortKey` | string | `pnl`, `winRate`, `returnPct`, `accountValue` | — |
| `sortDirection` | string | `asc`, `desc` | — |

`winRate` is token-PnL based: `(number of tokens with positive token PnL / total tracked tokens) * 100`, excluding USDC.

**Response (200):**
```json
{
  "data": [
    {
      "strategy": "uuid",
      "strategyName": "SOL Ecosystem DCA",
      "ownerUserId": "uuid",
      "ownerUsername": "trader1",
      "pnl": 120.50,
      "winRate": 0.65,
      "returnPct": 12.5,
      "accountValue": 1120.50,
      "arenaWalletAddress": "<solana-address>",
      "currentHoldings": [ ... ]
    }
  ],
  "meta": { "page": 1, "pageSize": 25, "total": 100, "pages": 4 }
}
```

---

### Quests & Bones

Quests are event-driven tasks (trades, signups, etc.) that reward bones (points) upon completion. Each quest has requirements (count, sum, or streak-based) and awards bones when all requirements are met. **Check quests regularly** — call `list_quests` to see open quests, and with `unclaimed=true` to discover completed quests, then `claim_quest` to collect the bones.

#### GET /api/v1/users/{userId}/quests
List quests with progress and requirements. By default returns only unlocked (available) quests.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/quests?page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

**Query parameters:**
| Param | Type | Values | Default |
|-------|------|--------|---------|
| `unlocked` | boolean | Filter for unlocked quests (available) | `true` |
| `unclaimed` | boolean | Filter for completed but unclaimed quests | — |
| `claimed` | boolean | Filter for claimed quests | — |
| `mode` | string | `completed_last` | — |
| `page` | number | Page number | 1 |
| `pageSize` | number | Items per page (max: 100) | 25 |

**Response (200):**
```json
{
  "data": [
    {
      "userId": "uuid",
      "questId": "uuid",
      "title": "First Trade",
      "description": "Execute your first trade",
      "award": 100,
      "totalRequirements": 1,
      "completedRequirements": 1,
      "claimed": false,
      "completed": true,
      "unlocked": true,
      "requirements": [
        {
          "requirementId": "uuid",
          "aggregationKind": "count",
          "targetValue": 1,
          "currentValue": 1,
          "completed": true
        }
      ]
    }
  ],
  "meta": { "page": 1, "pageSize": 25, "total": 10, "pages": 1 }
}
```

#### POST /api/v1/users/{userId}/quests/{questId}/claim
Claim bones for a completed quest.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/quests/{questId}/claim \
  -H "X-API-Key: $API_KEY"
```

**Response (200):**
```json
{ "data": null }
```

Returns 404 if the quest is not found or already claimed.

#### GET /api/v1/users/{userId}/quests/bones
Get the user's bones balance.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/quests/bones" \
  -H "X-API-Key: $API_KEY"
```

**Response (200):**
```json
{
  "data": {
    "userId": "uuid",
    "username": "alice",
    "balance": 500,
    "unclaimed": 100
  }
}
```

- `balance` — total bones already claimed
- `unclaimed` — bones from completed quests not yet claimed (call `claim_quest` to collect)

---

### Wallet Actions

#### POST /api/v1/wallets/{walletId}/actions/send
Send tokens from your Milo wallet to a recipient address.

```bash
curl -X POST {{BASE_URL}}/api/v1/wallets/{walletId}/actions/send \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "recipient": "<solana-address>",
    "token": "<token-mint-address>",
    "amount": 1.5
  }'
```

**Response (202):**
```json
{ "data": "<transaction-signature>" }
```

> **Note:** For native SOL, use the SOL mint address: `So11111111111111111111111111111111111111112`.
> If a JSON body includes `walletId`, it must match the `{walletId}` path parameter.

---

### Orders

#### POST /api/v1/wallets/{walletId}/orders
Create a new order, optionally with take-profit and stop-loss dependants.

```bash
curl -X POST {{BASE_URL}}/api/v1/wallets/{walletId}/orders \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "tokenAddress": "So11111111111111111111111111111111111111112",
    "type": "buy",
    "status": "active",
    "expiresAt": "2026-12-31T23:59:59.000Z",
    "payload": {
      "type": "buy",
      "amount": { "type": "absolute_usd", "amount": 50 },
      "trigger": { "type": "absolute", "trigger": "price", "operator": "gte", "value": 0 },
      "execution": {}
    },
    "takeProfits": [
      { "percentage": 50, "profitPercentage": 20 },
      { "percentage": 50, "profitPercentage": 50 }
    ],
    "stopLosses": [
      { "percentage": 100, "lossPercentage": 15 }
    ]
  }'
```

**Response** includes the main order plus a `dependants` array:
```json
{
  "data": {
    "id": "...",
    "type": "buy",
    "status": "active",
    "dependants": [
      { "type": "take_profit", "order": { "id": "...", "parentId": "...", "subType": "take_profit", "status": "draft" } },
      { "type": "take_profit", "order": { "id": "...", "parentId": "...", "subType": "take_profit", "status": "draft" } },
      { "type": "stop_loss",   "order": { "id": "...", "parentId": "...", "subType": "stop_loss",   "status": "draft" } }
    ]
  }
}
```

**Take-profit / Stop-loss ladder (optional):**

`takeProfits` array — each item:
- `percentage` (1–100) — percent of position to sell
- `profitPercentage` (> 0) — profit percent to trigger the TP

`stopLosses` array — each item:
- `percentage` (1–100) — percent of position to sell
- `lossPercentage` (1–100) — loss percent to trigger the SL

Dependant creation flow (enforced):
- Main order is created first.
- TP and SL dependants are created sequentially as draft sell children (`parentId` = main order ID).
- Dependant failures are captured per dependant entry while the main order still returns `201`.

Guardrails (always enforce mode):
- `takeProfits.length <= 5`
- `stopLosses.length <= 5`
- `takeProfits.length + stopLosses.length <= 8`

Violations return `400 bad_request` with a clear validation message. Dependants use relative triggers (`rise` for TP, `drop` for SL).

**Order payload structure:**

Buy order amounts:
- `{ "type": "absolute", "amount": 1000000 }` - Raw token amount
- `{ "type": "absolute_usd", "amount": 50 }` - USD equivalent

Sell order amounts (additional option):
- `{ "type": "relative", "percentage": 50 }` - Percentage of position

Trigger types:
- Market order: `{ "type": "absolute", "trigger": "price", "operator": "gte", "value": 0 }`
- Limit buy: `{ "type": "absolute", "trigger": "price", "operator": "lte", "value": 150.00 }`
- Stop loss: `{ "type": "relative", "trigger": "price", "operator": "drop", "value": 10 }` (10% drop)
- Take profit: `{ "type": "relative", "trigger": "price", "operator": "rise", "value": 25 }` (25% rise)

Market orders require `expiresAt`, and it must be within 120 minutes of the request time.

Execution options (all optional):
- `slippagePercentage` - Max slippage (0-100)
- `priorityFee` - Priority fee in SOL lamports
- `platformFeeBps` - Platform fee override in basis points

**Linking to a thesis:** Pass `positionThesisId` (UUID) in the body to attach the order (and its TP/SL dependants) to a position thesis.

#### GET /api/v1/users/{userId}/orders
List orders with filters.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/orders?status=active&type=buy&page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

**Query parameters:**
| Param | Type | Values |
|-------|------|--------|
| `status` | string | `active`, `paused`, `error`, `fulfilled`, `archived`, `draft` |
| `type` | string | `buy`, `sell` |
| `tokenAddress` | string | Filter by token |
| `page` | number | Page number (default: 1, max: 100) |
| `pageSize` | number | Items per page (default: 25, max: 100) |

#### GET /api/v1/users/{userId}/orders/{orderId}
Get order details.

```bash
curl {{BASE_URL}}/api/v1/users/{userId}/orders/{orderId} \
  -H "X-API-Key: $API_KEY"
```

#### POST /api/v1/users/{userId}/orders/{orderId}/pause
Pause an active order.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/orders/{orderId}/pause \
  -H "X-API-Key: $API_KEY"
```

#### POST /api/v1/users/{userId}/orders/{orderId}/activate
Activate a draft or paused order.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/orders/{orderId}/activate \
  -H "X-API-Key: $API_KEY"
```

#### DELETE /api/v1/users/{userId}/orders/{orderId}
Archive (delete) an order.

```bash
curl -X DELETE {{BASE_URL}}/api/v1/users/{userId}/orders/{orderId} \
  -H "X-API-Key: $API_KEY"
```

---

### Conversations

Milo uses an async conversation model. You send a message and the agent processes it in the background. Poll the messages endpoint for the response using the `processing` flag.

#### POST /api/v1/users/{userId}/conversations
Create a new conversation and send the first message.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is the current market sentiment for SOL?",
    "agentType": "market-analyst"
  }'
```

**Agent types:**
| Agent | ID | Purpose |
|-------|----|---------|
| Market Analyst | `market-analyst` | Market analysis, token research, sentiment |
| Auto Trader | `auto-trader` | Trading strategy discussion |
| Game Agent | `milo-game-agent` | Gamified trading experience |

**Response (201):**
```json
{
  "data": {
    "conversationId": "...",
    "status": "active",
    "agentActive": true,
    "processing": true,
    "createdAt": "..."
  }
}
```

#### GET /api/v1/users/{userId}/conversations
List conversations.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/conversations?page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

#### GET /api/v1/users/{userId}/conversations/{conversationId}
Get conversation details.

```bash
curl {{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId} \
  -H "X-API-Key: $API_KEY"
```

#### POST /api/v1/users/{userId}/conversations/{conversationId}/messages
Send a follow-up message.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "message": "What about JUP?" }'
```

#### GET /api/v1/users/{userId}/conversations/{conversationId}/messages
Poll for messages. Check `processing` flag to know if the agent is still working.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/conversations/{conversationId}/messages?page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

**Response:**
```json
{
  "data": {
    "messages": [
      { "messageId": "...", "role": "user", "content": "...", "createdAt": "..." },
      { "messageId": "...", "role": "assistant", "content": "...", "createdAt": "..." }
    ],
    "processing": false
  },
  "meta": { "page": 1, "pageSize": 25, "total": 2, "pages": 1 }
}
```

**Polling pattern:**
1. Send a message (POST).
2. Poll GET messages every 2-3 seconds.
3. When `processing` is `false`, the agent has finished responding.

---

### Portfolio

#### GET /api/v1/wallets/{walletId}/holdings
Get current token holdings for a wallet.

```bash
curl {{BASE_URL}}/api/v1/wallets/{walletId}/holdings \
  -H "X-API-Key: $API_KEY"
```

#### GET /api/v1/wallets/{walletId}/transactions
Get all transactions for a wallet.

```bash
curl "{{BASE_URL}}/api/v1/wallets/{walletId}/transactions?page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

#### GET /api/v1/wallets/{walletId}/executed-transactions
Get executed transactions (order-linked trades) for a wallet. Uses cursor-based pagination.

```bash
curl "{{BASE_URL}}/api/v1/wallets/{walletId}/executed-transactions?limit=25" \
  -H "X-API-Key: $API_KEY"

# To paginate, pass the nextCursor from the previous response:
curl "{{BASE_URL}}/api/v1/wallets/{walletId}/executed-transactions?limit=25&cursor=<nextCursor>" \
  -H "X-API-Key: $API_KEY"
```

**Query parameters:**
| Param | Type | Description |
|-------|------|-------------|
| `limit` | number | Items per page (default: 25, max: 200) |
| `cursor` | string | Cursor from previous response's `nextCursor` |
| `txType` | string | Filter by `buy` or `sell` |
| `token` | string | Filter by token address |

#### GET /api/v1/users/{userId}/positions
Get positions with PnL data.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/positions?status=active&page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

**Query parameters:**
| Param | Values |
|-------|--------|
| `status` | `active`, `pending`, `not_active` |

#### POST /api/v1/users/{userId}/positions/{thesisId}/close
Close a single position. Cancels pending orders and creates a sell order for remaining holdings.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/positions/{thesisId}/close \
  -H "X-API-Key: $API_KEY"
```

#### POST /api/v1/users/{userId}/positions/close-all
Close **all** active and pending positions for a user. Each position is closed independently — partial failures don't block other positions.

```bash
curl -X POST {{BASE_URL}}/api/v1/users/{userId}/positions/close-all \
  -H "X-API-Key: $API_KEY"
```

**Response:**
```json
{
  "data": {
    "successes": [
      { "thesisId": "...", "cancelled": 2, "sellOrderCreated": true }
    ],
    "failures": [
      { "thesisId": "...", "error": "No wallet found" }
    ]
  }
}
```

#### GET /api/v1/users/{userId}/diary-logs
Get auto-trade diary logs.

```bash
curl "{{BASE_URL}}/api/v1/users/{userId}/diary-logs?page=1&pageSize=25" \
  -H "X-API-Key: $API_KEY"
```

---

## Rate Limits

Rate limits are enforced across endpoints. Effective thresholds vary by endpoint and request context and may be adjusted over time.

Rate limit rejections return `429 Too Many Requests` with:
- `error.code = "rate_limit_exceeded"`
- `Retry-After` header (seconds)
- `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` headers

Retry behavior: back off and retry only after `Retry-After` elapses.

## Pagination

All list endpoints support pagination:
- `page` - Page number (default: 1, max: 100)
- `pageSize` - Items per page (default: 25, max: 100)

Response includes `meta`:
```json
{ "meta": { "page": 1, "pageSize": 25, "total": 100, "pages": 4 } }
```

## Error Codes

| Status | Code | Description |
|--------|------|-------------|
| 400 | `bad_request` | Invalid input, missing fields, validation error |
| 401 | `unauthorized` | Missing or invalid API key |
| 404 | `not_found` | Resource not found |
| 409 | `error` | Conflict (e.g., user already exists) |
| 429 | `rate_limit_exceeded` | Rate limit exceeded |
| 500 | `internal_error` | Unexpected server error |

**Error response format:**
```json
{
  "error": {
    "code": "bad_request",
    "message": "Model \"gpt-5.2-high\" requires a Pro plan. Upgrade here: https://buy.stripe.com/...",
    "details": {
      "requestedModelVersion": "gpt-5.2-high",
      "requiredPlan": "pro",
      "requiredPlanLabel": "Pro",
      "upgradeUrl": "https://buy.stripe.com/...",
      "upgradeText": "Upgrade to Pro to use model \"gpt-5.2-high\"."
    }
  }
}
```

Schema validation failures also return `400 bad_request`, with `error.details.validationIssues` as a field-level issue list:

```json
{
  "error": {
    "code": "bad_request",
    "message": "Missing required field: expiresAt",
    "details": {
      "validationIssues": [
        {
          "target": "json",
          "path": "expiresAt",
          "code": "invalid_type",
          "message": "Required"
        }
      ]
    }
  }
}
```
