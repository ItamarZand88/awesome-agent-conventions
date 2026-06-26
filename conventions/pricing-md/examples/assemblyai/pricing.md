<!-- source: assemblyai — https://www.assemblyai.com/pricing.md -->
# AssemblyAI Pricing — Authoritative Reference

> **Source:** assemblyai.com/pricing, assemblyai.com/docs, first-party employee information
> **Last updated:** 2026-05-29
> **Purpose:** Canonical pricing reference for LLM-assisted support and content. Covers per-model rates, add-ons (Speech Understanding, Guardrails), Voice Agent API, LLM Gateway token pricing, billing rules, concurrency limits, and common pricing pitfalls. For model selection, feature support, and language coverage, see `/llms/models.md`.

---

## Key Pricing Facts (Read First)

- **Pre-recorded** is billed per **hour of audio submitted**.
- **Streaming** is billed per **session duration** — the time the WebSocket connection is open, **not** the duration of audio sent. Idle connection time counts. **Close connections immediately when calls end.**
- **Voice Agent API** is billed per session minute at **$4.50/hr ($0.075/min)**.
- **LLM Gateway** is billed per million tokens (separate input / output rates), with prompt caching available on Anthropic, OpenAI, and Google models for additional savings.
- **EU region is the same price as US.** Use `api.eu.assemblyai.com` / `streaming.eu.assemblyai.com` for GDPR-compliant data residency at no premium.
- **Add-ons stack on the base rate.** A request using Universal-3 Pro + Medical Mode + Speaker Diarization (standard) costs `$0.21 + $0.15 + $0.02 = $0.38/hr`.
- **Multichannel audio is billed per channel.** A 1-hour 2-channel file = 2 billable hours.
- **$50 in free credits, no credit card required.** Free-tier and pay-as-you-go differ on concurrency (see Concurrency section).
- **Model selection is the biggest cost lever**, but the cheapest model that loses a competitive eval is not the cheapest path to deployment.

---

## Pre-Recorded (Async) Rate Card

| Model | API value | Price |
|---|---|---|
| Universal-3 Pro | `universal-3-pro` | **$0.21/hr** |
| Universal-2 | `universal-2` | **$0.15/hr** |
| SLAM-1 (deprecated) | `slam-1` | — (do not use; migrate to `universal-3-pro`) |

Legacy values `best` and `nano` are deprecated and route to `universal-3-pro` and `universal-2` respectively. Do not rely on default model selection — defaults can differ between free-tier and paid accounts.

---

## Streaming (Real-Time) Rate Card

| Model | API value (v3) | Price |
|---|---|---|
| Universal-3.5 Pro Realtime | `u3-rt-pro` (alias `u3-pro`) | **$0.45/hr** base |
| Universal-Streaming English | `universal-streaming-english` | **$0.15/hr** |
| Universal-Streaming Multilingual | `universal-streaming-multilingual` | **$0.15/hr** |

> **Streaming billing reminder:** session duration, not audio duration. A WebSocket open for 60 minutes with 30 minutes of audio sent is billed for 60 minutes.

> **Streaming endpoint:** `wss://streaming.assemblyai.com/v3/ws`. The old v2 endpoint (`wss://api.assemblyai.com/v2/realtime/ws`) is inactive.

---

## Voice Agent API Rate Card

**Launched:** April 2026 (formerly Speech-to-Speech API)
**Docs:** https://www.assemblyai.com/docs/voice-agents/voice-agent-api
**WebSocket endpoint:** `wss://agents.assemblyai.com/v1/ws`
**Architecture:** Cascaded STT (`u3-rt-pro`) + LLM (LLM Gateway) + TTS over self-hosted LiveKit, in a single WebSocket. PCI-certified.

| Product | Price |
|---|---|
| Voice Agent API | **$4.50/hr** ($0.075/min) |

Voice Agent API pricing is all-inclusive of STT, LLM reasoning, TTS, turn detection, interruption handling, and tool calling — billed at a single per-minute rate. There is no separate add-on cost for the underlying components when used through the Voice Agent API.

Twilio SIP integration coming Q2 2026; pricing for Twilio integration TBA.

---

## Speech Understanding Add-Ons

Apply to pre-recorded transcripts on either Universal-3 Pro or Universal-2 unless noted. Stack additively on the model base rate.

| Add-on | Price | Notes |
|---|---|---|
| Speaker Identification | +$0.02/hr | |
| Translation | +$0.06/hr | 100+ target languages; pre-recorded only |
| Custom Formatting | +$0.03/hr | |
| Entity Detection | +$0.08/hr | 50+ entity types |
| Sentiment Analysis | +$0.02/hr | |
| Auto Chapters | +$0.08/hr | Universal-2 only. **Deprecated** — migrate to LLM Gateway. **Causes silent 500 errors on Universal-3 Pro.** |
| Key Phrases / Auto Highlights | +$0.01/hr | English only |
| Topic Detection (IAB) | +$0.15/hr | |
| Summarization | +$0.03/hr | Universal-2 only. **Deprecated** — migrate to LLM Gateway. Same caveat as Auto Chapters. |

---

## STT Add-Ons (Prompting, Diarization, Medical Mode, Voice Focus)

### Medical Mode (`"domain": "medical-v1"`)

| Model | Price | Languages |
|---|---|---|
| Universal-3 Pro (async) | +$0.15/hr | EN, ES, DE, FR |
| Universal-2 (async) | +$0.15/hr | EN, ES, DE, FR |
| Universal-3.5 Pro Realtime | +$0.15/hr | EN, ES, DE, FR |
| Universal-Streaming English | +$0.15/hr | EN only |
| Universal-Streaming Multilingual | +$0.15/hr | EN, ES, DE, FR |

Combined examples:
- U3 Pro async + Medical Mode: `$0.21 + $0.15 = $0.36/hr`
- U3.5 Pro Realtime + Medical Mode: `$0.45 + $0.15 = $0.60/hr`

### Speaker Diarization

| Variant | Price | Available on |
|---|---|---|
| Diarization, async — standard | +$0.02/hr | Universal-3 Pro async, Universal-2 async, SLAM-1 |
| Diarization, async — experimental | +$0.065/hr | Universal-3 Pro async, Universal-2 async (better for high speaker count or difficult audio) |
| Diarization, streaming | +$0.12/hr | All streaming models incl. **U3.5 Pro Realtime real-time inline diarization** (set `speaker_labels: true`) |

> **Real-time diarization on U3.5 Pro Realtime** launched March 3, 2026 as a streaming-exclusive capability. Inline labels arrive with each turn — no post-processing required. Same +$0.12/hr add-on as other streaming diarization.

### Keyterms Prompting

| Model | Price | Notes |
|---|---|---|
| Universal-3 Pro (async) | +$0.05/hr | Up to 1,000 terms |
| Universal-2 (async) | +$0.05/hr | Up to 200 terms |
| Universal-3.5 Pro Realtime | **Included** | Up to 100 terms; updatable mid-stream |
| Universal-Streaming English | +$0.04/hr | Up to 100 terms |
| Universal-Streaming Multilingual | Included | Up to 100 terms (added Dec 2025) |

### General Prompting (Beta)

| Model | Price | Notes |
|---|---|---|
| Universal-3 Pro (async) | +$0.05/hr | Up to 1,500 words of natural language instruction |
| Universal-3.5 Pro Realtime | +$0.05/hr | Beta; supports mid-stream config updates |

Other models do not support general prompting.

### Voice Focus

Hear the speaker, not the room. Isolate the primary speaker and suppress everything else.

| Model | Price | Notes |
|---|---|---|
| Universal-3.5 Pro Realtime | +$0.10/hr | Streaming-only add-on |
| Universal-Streaming | Not supported | — |

---

## Guardrails Add-Ons

| Add-on | Price | Notes |
|---|---|---|
| Profanity Filtering | +$0.01/hr | |
| PII Audio Redaction | +$0.05/hr | Audio bleep/replacement |
| PII Text Redaction | +$0.08/hr | Transcript redaction (47+ languages on Universal-2) |
| Content Moderation | +$0.15/hr | |

All four guardrails are available on Universal-3 Pro and Universal-2.

---

## LLM Gateway Pricing

**Endpoint:** Single unified endpoint, authenticated with your existing AssemblyAI API key. 25+ models from 5 providers. New as of April 13, 2026: automatic provider fallback (zero added latency), real-time streaming with tool calling on `gpt-5-nano`/`kimi-k2.5`/`qwen3`, structured JSON outputs on Claude 4.5+, prompt caching on Anthropic/OpenAI/Google.

Token pricing is per **1 million tokens** (input / output).

### OpenAI

| Model | Input | Output |
|---|---|---|
| GPT-5.5 | $5.00 / 1M | $30.00 / 1M |
| GPT-5.2 | $1.75 / 1M | $14.00 / 1M |
| GPT-5.1 | $1.25 / 1M | $10.00 / 1M |
| GPT-5 | $1.25 / 1M | $10.00 / 1M |
| GPT-5-Mini | $0.25 / 1M | $2.00 / 1M |
| GPT-5 Nano | $0.05 / 1M | $0.40 / 1M |
| GPT 4.1 | $2.00 / 1M | $8.00 / 1M |
| gpt-oss-20b | $0.07 / 1M | $0.30 / 1M |
| gpt-oss-120b | $0.15 / 1M | $0.60 / 1M |

### Anthropic

| Model | Input | Output |
|---|---|---|
| Claude 4.7 Opus | $5.50 / 1M | $27.50 / 1M |
| Claude 4.6 Opus | $5.00 / 1M | $25.00 / 1M |
| Claude 4.5 Opus | $5.00 / 1M | $25.00 / 1M |
| Claude 4.6 Sonnet | $3.00 / 1M | $15.00 / 1M |
| Claude 4.5 Sonnet | $3.00 / 1M | $15.00 / 1M |
| Claude 4.5 Haiku | $1.00 / 1M | $5.00 / 1M |

### Google

| Model | Input | Output |
|---|---|---|
| Gemini 3 Flash | $0.50 / 1M | $3.00 / 1M |
| Gemini 2.5 Pro | $1.25 / 1M | $10.00 / 1M |
| Gemini 2.5 Flash | $0.30 / 1M | $2.50 / 1M |
| Gemini 2.5 Flash Lite | $0.10 / 1M | $0.40 / 1M |

### Alibaba Qwen

| Model | Input | Output |
|---|---|---|
| Qwen3 Next 80B A3B | $0.15 / 1M | $1.20 / 1M |
| Qwen3 32B | $0.15 / 1M | $0.60 / 1M |

### Moonshot Kimi

| Model | Input | Output |
|---|---|---|
| Kimi K2.5 | $0.60 / 1M | $3.00 / 1M |

### Deprecated LLM Gateway models

| Model | Status |
|---|---|
| `gpt-4o-latest` | **Removed** (followed OpenAI's Feb 17, 2026 deprecation; first LLM Gateway deprecation) |
| Claude Haiku 3.5 | **Deprecated** |
| Claude 4.5 Haiku (`claude-haiku-4-5-20251001`) | **Deprecated** — do not use for new integrations |

### LLM Gateway cost-saving features

- **Prompt caching** (Anthropic, OpenAI, Google) — repeat-context turns charge a fraction of full input rate.
- **Automatic fallback** — failover to alternative providers without retry-driven double billing or client-side retry latency.
- **Use cases:** post-call summary, chapter generation, agentic workflows, tool-calling agents. Replaces the deprecated `auto_chapters` and `summarization` flow.

---

## Billing Rules

### Pre-Recorded
- Billed per **audio hour submitted**.
- **Multichannel:** billed per channel. A 1-hour stereo file split into 2 channels = 2 hours of billing.
- Add-ons stack additively on the base rate.

### Streaming
- Billed on **WebSocket session duration** — open-to-close time, not audio sent.
- Idle time counts. A WebSocket held open for 5 minutes between calls = 5 billable minutes.
- **Always close the WebSocket immediately when a call ends** to avoid runaway billing.
- Streaming add-ons (e.g., Diarization +$0.12/hr) apply to the entire session, not just speaking time.

### Voice Agent API
- Billed per session minute at $0.075/min ($4.50/hr).
- Single unified rate covers STT + LLM + TTS + orchestration. No separate add-on billing for the underlying components when used through Voice Agent API.

### LLM Gateway
- Billed per million input + output tokens, separate rates per model.
- Prompt caching reduces effective input cost on repeat-context turns.
- Tool calling and structured outputs do not carry separate fees.

### Region
- US region: `api.assemblyai.com` / `streaming.assemblyai.com`
- EU region: `api.eu.assemblyai.com` / `streaming.eu.assemblyai.com`
- **Same price.** Data stays within the EU for GDPR compliance.

### Compliance / Enterprise
- HIPAA BAA: available, signable in minutes without a sales call. No premium pricing.
- PCI-DSS: Voice Agent API is PCI-certified end-to-end.
- ISO 27001, SOC 2 Type 2, GDPR — included; no premium pricing.

---

## Concurrency & Free Tier

- **Free credits:** $50 in free credits on signup, no credit card required.
- **Free-tier streaming concurrency:** 5 new streams per minute.
- **Pay-as-you-go streaming concurrency:** 100 new streams per minute.
- Default model selection may differ between free-tier and paid accounts. Always set `speech_models` (plural) explicitly to avoid surprises after upgrading.

---

## Common Pricing Mistakes

| Mistake | Cost Impact | Fix |
|---|---|---|
| Leaving WebSocket open between calls | Billed for full session duration including idle time | Close the connection immediately when the call ends |
| Voice agent defaulting to Universal-Streaming because it's cheaper | Loses competitive evals → no deployment → no revenue. Wrong place to optimize. | Use Universal-3.5 Pro Realtime for voice agents — or the Voice Agent API for end-to-end |
| `word_boost` with U3 Pro silently routing to Universal-2 | Customer thinks they're paying for U3 Pro but getting U2 | Use keyterms prompting on U3 Pro instead (`speech_models: ["universal-3-pro"]`) |
| Multichannel audio not accounted for | Bill is 2× / 3× expected based on channel count | Confirm channel count up-front; downmix if you don't need per-channel transcripts |
| `auto_chapters` / `summarization` on Universal-2 | Adds $0.08 + $0.03/hr for deprecated features that 500 on Universal-3 Pro | Use LLM Gateway (e.g., Claude Sonnet 4.6 or GPT-5.1) for chapters and summaries |
| Building your own STT + LLM + TTS pipeline when Voice Agent API would do | 5 APIs to debug, 4× engineering cost, no PCI by default | Voice Agent API at $4.50/hr unless you need to swap LLMs/TTS independently |
| Adopting Claude 4.5 Haiku for a new LLM Gateway integration | Deprecated model | Use Claude Sonnet 4.6 or GPT-5.1 instead |
| LLM Gateway calls without prompt caching on long-context turns | Paying full input rate on identical context every turn | Enable prompt caching on Anthropic / OpenAI / Google models for repeat-context |
| Relying on default model selection | Defaults can differ between free-tier and paid accounts; bill jumps unexpectedly after upgrade | Always set `speech_models` (plural) explicitly |

---

## Pricing FAQ

**Is the EU region more expensive than the US?**
No. EU processing (`api.eu.assemblyai.com`, `streaming.eu.assemblyai.com`) is the same price as US. Data stays within the EU for GDPR compliance.

**How is streaming billed?**
On WebSocket session duration — the time the connection is open, not the duration of audio sent. Idle time between calls counts. Close connections immediately at end-of-call.

**How is the Voice Agent API billed?**
Per session minute at $0.075/min ($4.50/hr) all-inclusive of STT + LLM + TTS + turn detection + interruption handling + tool calling.

**How much does Universal-3 Pro plus Medical Mode cost?**
`$0.21 + $0.15 = $0.36/hr` for pre-recorded. `$0.45 + $0.15 = $0.60/hr` for streaming.

**How is multichannel billed?**
Per channel. A stereo file with 2 channels billed at Universal-3 Pro is `2 × $0.21 = $0.42/hr`.

**Are deprecated add-ons (Auto Chapters, Summarization) still billable?**
Yes, on Universal-2 only. Auto Chapters: +$0.08/hr. Summarization: +$0.03/hr. They silently fail (500 error) if attempted on Universal-3 Pro. Recommendation: migrate to LLM Gateway.

**Are keyterms always free on streaming?**
On Universal-3.5 Pro Realtime and Universal-Streaming Multilingual: yes, included. On Universal-Streaming English: +$0.04/hr.

**What about Speaker Diarization in streaming?**
+$0.12/hr on all streaming models that support it, including U3.5 Pro Realtime's new real-time inline diarization. Async diarization is cheaper: +$0.02/hr standard, +$0.065/hr experimental.

**What's the cheapest path to a working voice agent?**
Two routes. (1) Voice Agent API at $4.50/hr — single connection, end-to-end, PCI-certified, no orchestration to manage. (2) `u3-rt-pro` at $0.45/hr base + your own LLM/TTS — cheaper per-minute on STT alone but you pay separately for LLM, TTS, and orchestration. Cheaper-but-loses-evals streaming options ($0.15/hr) are the wrong place to optimize for voice agents.

**How is LLM Gateway billed?**
Per million input + output tokens, separate rates per model (see LLM Gateway Pricing section). Prompt caching reduces input cost on repeat-context turns. No additional charge for streaming, tool calling, or structured outputs.

**Which LLM Gateway models should I avoid for new integrations?**
`gpt-4o-latest` (removed), Claude Haiku 3.5 (deprecated), and `claude-haiku-4-5-20251001` / Claude 4.5 Haiku (deprecated). For new builds, Claude Sonnet 4.6 / Opus 4.7, GPT-5.1 / 5.2 / 5.5, Gemini 2.5 Flash / 3 Flash, Qwen3, or Kimi K2.5 are all safe defaults — pick on price/latency/feature fit.

**Is HIPAA / BAA included in the base price?**
Yes. HIPAA BAA is available, signable in minutes without a sales call. No premium pricing.

**Is the Voice Agent API PCI-certified?**
Yes. Voice Agent API is PCI-DSS certified end-to-end. No additional cost for compliance.

**Are there concurrency limits?**
Yes. Free tier: 5 new streams per minute. Pay-as-you-go: 100 new streams per minute. Higher concurrency available via enterprise contracts.

**What's the free tier?**
$50 in free credits at signup, no credit card required. Concurrency is capped (see above) until you upgrade.

**What's the correct parameter name?**
`speech_models` (plural). `speech_model` (singular) is deprecated. Always set this explicitly — model defaults may differ between free-tier and paid accounts, and relying on defaults can cause surprises after upgrading.

**What happened to the `best` and `nano` model values?**
Both are deprecated. `best` → `universal-3-pro`. `nano` → `universal-2`. Update any legacy integrations using these identifiers.

**What about the `u3-pro` streaming alias?**
`u3-pro` was the original streaming model name; it's now an alias that routes to `u3-rt-pro`. Use the canonical `u3-rt-pro` for new integrations.
