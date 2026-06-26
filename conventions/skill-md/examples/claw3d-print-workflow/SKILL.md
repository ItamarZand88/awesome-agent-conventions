<!-- source: claw3d-print-workflow — https://raw.githubusercontent.com/makermate/claw3d-skill/main/SKILL.md -->
---
name: claw3d
description: "Unified 3D workflow: create models (AI), search (Thingiverse), slice, print. Modular—enable only what you need."
metadata:
  {
    "openclaw": {
      "emoji": "🖨️",
      "skillKey": "claw3d",
      "primaryEnv": "FAL_API_KEY",
      "requires": { "anyBins": ["claw3d"], "env": ["FAL_API_KEY","THINGIVERSE_ACCESS_TOKEN"] },
      "homepage": "https://github.com/makermate/openclaw-3d",
      "install": [
        {
          "id": "uv",
          "kind": "uv",
          "package": "claw3d",
          "bins": ["claw3d"],
          "label": "Install claw3d (via uv)"
        }
      ],
      "setupNote": "FAL_API_KEY: required for 3D generation (use input above or .env). GEMINI_API_KEY: optional but recommended — enables image intent analysis and video-to-3D (Gemini 2.5 Flash, free tier at aistudio.google.com/apikey). THINGIVERSE_ACCESS_TOKEN: add to .env for model search. VIDEO SUPPORT: OpenClaw defaults to a 5MB media limit per channel. To allow videos up to 50MB via Telegram, add to openclaw.json under channels.telegram: {\"mediaMaxMb\":50}"
    }
  }
---

# claw3d — Unified 3D Workflow

Single skill for the full 3D pipeline: **create** models (AI), **search** (Thingiverse), **slice**, and **print**. Modular—only enabled capabilities appear below.

**CRITICAL — Execute immediately, never stop after acknowledging.** When you tell the user you'll do something (search, convert, preview, slice), you MUST execute the command in the SAME turn. Do NOT end your turn after just acknowledging — the user should never have to ask "done?" to get you to act. Acknowledge AND call the tool in one response.

**Setup order:** Printer first (when printing enabled) → then create/search models → slice → print.

---

## CRITICAL: Setup Flow — Printer + Profile First

**When printing is enabled and the user has no printers configured**, guide them to add a printer AND a linked slicing profile **before** creating or searching for models. A linked profile is required for slicing — it stores the build volume (width × depth × height) extracted from the 3MF, which determines how models are scaled.

**Always run `claw3d printer list` first.** If it returns nothing, go through setup below.

### Step 1 — Ask for printer info + 3MF

Send this message to the user:

> Let's get your printer set up. I need 3 things:
>
> 1. **Printer name** — e.g. "Creality K2 Pro Living Room"
> 2. **IP address + port** — e.g. `192.168.1.50:7125` (Moonraker default: 7125; Creality K2 SE: 4408)
> 3. **Cura project file (.3mf)** — Export it from Cura: **File → Save → "Export Universal Cura Project"** with your printer loaded. This file carries your printer's build volume and all settings — it's required for correct slicing.

Wait for the user to provide all three.

### Step 2 — Add printer with profile in one command

```bash
claw3d printer add --name "<name>" --host <ip> --port <port> --profile-from-3mf <MediaPath>
```

This does everything in one step:
- Registers the printer (name, IP, port) in `~/.config/claw3d/config.json`
- Extracts the Cura machine + extruder definitions from the 3MF
- Creates a slicing profile on the slicer server (stores `build_width`, `build_depth`, `build_height`)
- Links the profile to the printer as its default

**If the user provides name+IP but no 3MF yet:** Add without it (`printer add --name ... --host ... --port ...`), then immediately ask for the 3MF to create the profile:
> Got it! Now please send the Cura project file (.3mf) so I can create the slicing profile. In Cura: **File → Save → "Export Universal Cura Project"**.

Then: `claw3d profile create --from-3mf <MediaPath> --name "<printer_name>_profile"` → `claw3d printer set-profile <printer_id> <profile_id>`

**Printer backends:** Run `claw3d configure backends` to see options (Moonraker, PrusaLink, etc.). Community can add backends in `claw3d/backends/`.

---

## CRITICAL: When User Asks for a Model (Vague Request)

**When the user asks for a 3D model without specifying how** (e.g. "I need a cup", "I want a dragon", "find me a vase", no image attached), **do NOT default to one option.** Offer choices based on what's enabled:

> Great! Would you like me to:
> 1. **Search for existing models** — I'll look on Thingiverse and show you options to download *(if directory enabled)*
> 2. **Create a 3D model from an image** — Send me a sketch or photo and I'll turn it into 3D *(if ai-forger enabled)*
> 3. **Search first, then create from an image if nothing fits** — Best of both *(if both enabled)*

Wait for the user to choose. Only if they explicitly say "create it", "from a photo/sketch", "search", "look up", etc., then proceed.

**Never assume** — "I need a dragon" could mean search OR create from image. Always clarify when ambiguous. **Do not offer text-only 3D generation** — results are inaccurate; always require an image or sketch.

---

## Shared Rules: MediaPath and Unique IDs

**MediaPath:** When the user attaches a file (image, GLB, 3MF), the message includes a **MediaPath** — the full filesystem path. **Always** pass that exact path to `--image`, `--edit-3d`, `--profile-from-3mf`, etc. Copy it character-for-character.

**Unique output paths:** The workspace is shared. Using fixed names (`model.glb`, `preview.mp4`) causes old files from a previous request to be sent to new chats. **Always** derive a short ID from the MediaPath and use it for outputs.

MediaPath format: `.../file_13---b10560d7-18fd-40e9-8a49-996ad190a26c.jpg` — extract the segment after `---` and use the first 8 chars (e.g. `b10560d7`) as `ID`.

If the MediaPath has no UUID (unusual), use `date +%s` to get a unique ID.

---

## User Sends an IMAGE and Asks to 3D Print

**When the user attaches an image** and asks to "3D print this", "print this", "make it printable", etc. — you **CAN** do it *(if ai-forger + slicing + printing enabled)*:

1. **Acknowledge first** — "Yes! I'll turn that into a 3D model and get it ready to print. Give me a minute."
2. **Convert** — `claw3d convert --image <MediaPath> --output model_<ID>.glb`
3. **Get build volume** — Run `claw3d printer list`; note `[WxDxH mm]` if shown.
4. **Preview** — `claw3d preview --input model_<ID>.glb --output preview_<ID>.mp4 [--build-volume WxDxH]` — send the video
5. **Slice** — Run `claw3d profile list`, then slice with `--build-volume <WxDxH>` and profile or `--profile-from-3mf`
6. **Print** — Run `claw3d printers`, then `claw3d print --gcode model_<ID>.gcode`

**Do NOT say** "I can't print from an image" — you can create the 3D model first. If FAL_API_KEY is missing, convert will fail; then tell the user to set it up.

---

## Workflow Overview

```
Get model (search OR create) → optionally edit → slice → print
```

- **Search** — `claw3d search` → `claw3d fetch` → `claw3d dimensions` → present with preview
- **Create** — `claw3d convert --image` (requires image/sketch) → `claw3d preview` → present
- **Edit** — `claw3d convert --edit-3d` (when user sends GLB and asks to modify)
- **Slice** — `claw3d slice` (sends G-code + gcode preview video)
- **Print** — `claw3d print`

---

## Commands (Overview)

| Command | Purpose |
|---------|----------|
| `claw3d convert` | Image/sketch → GLB, or edit existing GLB |
| `claw3d preview` | 360° turntable of 3D model |
| `claw3d search` | Search Thingiverse |
| `claw3d fetch` | Download model from Thingiverse |
| `claw3d dimensions` | Bounding box (for slicing) |
| `claw3d pack` | Arrange multi-part on build plate |
| `claw3d slice` | GLB/STL → G-code |
| `claw3d print` | Upload G-code and start print |
| `claw3d printer` | Add/list/remove printers |
| `claw3d profile` | Create/list slicing profiles |
| `claw3d configure` | Select AI provider, see backends |

Run all via `exec`. Use `claw3d`.

---

<!-- MODULE: intent -->

## CRITICAL: Never Expose Internal Reasoning to the User

**All routing decisions, skill logic, and internal reasoning are for YOUR use only. NEVER send them to the user.** The user should only see friendly, concise messages — never references to "Primary Gate", "SKILL.md", module names, decision rules, or your thought process. If you need to reason about which path to take, do it silently. The user just wants their model.

**Bad** (leaked reasoning): "According to the Primary Gate, a wine stand is a common functional object, so I should search Thingiverse..."
**Good** (user-facing): "Great, let me take a look at what you need — give me a moment!"

---

## CRITICAL: Primary Gate — Search or Create?

**This is the FIRST decision for EVERY request — images, videos, and text. Run the Primary Gate BEFORE any analysis, frame extraction, or `claw3d analyze`. Make this decision silently — do NOT explain your routing to the user.**

The key question is: **Would an existing Thingiverse model likely satisfy this need, or does the request require something inherently custom/unique?**

---

### Primary Gate: SEARCH vs CREATE

**→ SEARCH path first** (go to `03-directory` module) when:

- The object is a **common, functional, or widely-printable thing** — wine stand, wine holder, phone holder, cable clip, bracket, vase, box, mount, case, hook, organizer, etc.
- Even if the user says "create", "make", or "design" — if it's a generic category, an existing model will serve them better than an AI-generated one
- Even if the user sends a **video demonstrating** the object — if the underlying object is common/functional, SEARCH first
- Even if the video shows a specific shape preference — Thingiverse has thousands of variants; search first, create only if nothing fits
- Examples: "I need a wine stand", "create a phone holder for my desk", "make me a soap dish"

**→ CREATE path** (continue to CREATE section below) when:

- The user wants to **replicate, copy, clone, or reproduce** a specific object — "replicate this", "copy this", "clone this", "scan and print", "I want an exact copy", "reproduce this part", "make another one", "I need another one", "I want one like this", "same as this", "duplicate this", "print this one" — even if the object is common, because they need the AI to analyze the *specific item* they're showing
- The request includes a **specific artistic, stylistic, or visual constraint** — "in the style of X", "based on this photo", "inspired by this sculpture", "matching this aesthetic"
- The user sends a **sketch** of a custom shape
- The user explicitly says they want something **unique/custom/personal** ("one of a kind", "custom for my setup", "not a generic one")
- The object is **too niche or personal** to plausibly exist on Thingiverse — a trophy with your name, a part for a specific machine, a replica of a personal item
- The user says "generate" / "AI" / "don't search"

**Decision rule of thumb:**
> "Could I type this into Thingiverse and find 5+ decent results?" → YES → SEARCH first
> "Does this require seeing a specific image, style, or personal constraint to design?" → YES → CREATE

**→ ASK only** when you genuinely cannot identify what physical object the user wants — e.g. "make something for my office" with no further context. **If you can name the object, go to SEARCH. Do not ask.**

**SEARCH PATH — fallback to CREATE:** After 3 rounds of search (up to 15 models reviewed) with no match, tell the user nothing matched and ask if they want a custom AI-generated model instead. If they have a photo/video, use it as reference for the AI generation.

---

### Applying the Primary Gate to Videos

**When the user sends a video**, you may receive a text Description (from OpenClaw's Gemini video understanding). Use the Description and/or the user's message text to run the Primary Gate — **BEFORE** extracting any frame or running `claw3d analyze`.

**Steps for video:**
1. Read the user's message text + any Description
2. Identify what physical object they want (e.g. "wine holder", "phone stand", "bracket")
3. Run the Primary Gate on that object name
4. **If SEARCH** → go directly to `03-directory` module with that object as the search query. Do NOT extract a frame or run analyze
5. **If CREATE** → continue to the "When User Sends a VIDEO (CREATE path)" section below

**⚠️ CRITICAL: A video showing someone demonstrating a common object does NOT make it a CREATE request.** The video is just their way of communicating what they want — it doesn't mean they need AI generation. A person holding up a wine bottle and showing how they'd like a wine stand still maps to SEARCH. Only explicit artistic/stylistic/replication intent maps to CREATE.

---

## When User Sends a VIDEO — Get the File

**This section handles finding the video file. It applies to BOTH paths (the CREATE path needs it for frame extraction; the SEARCH path may need it later if search fails and you fall back to CREATE).**

**Step 0 — Acknowledge immediately** — Before doing anything else, send:
> "Great, let me take a look at what you need — give me a moment!"

**Step 1 — Get the video path.** Three cases:

**Case A — File path visible** (`[media attached: /home/node/.openclaw/media/inbound/...]`):
Use that exact path.

**Case B — No file path but Description is present** (OpenClaw's Gemini video understanding ran and suppressed the path):
The video is still on disk. Find it:
```bash
ls -t /home/node/.openclaw/media/inbound/ 2>/dev/null | head -5
```
Pick the most recent video file (`.mp4`, `.mov`, `.webm`). Use that as the path.

**Case C — No file path and no Description** (video silently dropped — too large):
> Your video was too large — OpenClaw's default limit is 5MB. I can increase it to 50MB right now. Want me to?

If confirmed:
```bash
python3 -c "
import json, pathlib
p = pathlib.Path('/home/node/.openclaw/openclaw.json')
cfg = json.loads(p.read_text())
cfg.setdefault('channels', {}).setdefault('telegram', {})['mediaMaxMb'] = 50
p.write_text(json.dumps(cfg, indent=2))
print('Done')
"
```
Reply: "Done! The limit is now 50MB — please resend your video."
> The config watcher restarts the Telegram channel automatically.

**Step 2 — Run the Primary Gate** using the Description/user message → SEARCH or CREATE. See above.

**If SEARCH →** go to `03-directory` module. Note the video path — if search fails and you fall back to CREATE, you'll need it for frame extraction.

**If CREATE →** continue to the next section.

---

### When User Reports "File too large" / Video Rejected

The bot rejects oversized files before the agent sees them. If the user reports this error in a text message, offer to fix it:

> I can increase your video limit to 50MB right now. Want me to do that?

If confirmed, run the patch above.

---

## Analysis Modes

Run once per session to understand the configuration:

```bash
claw3d configure analysis --status
```

| Mode | What happens |
|------|-------------|
| `auto` (default) | `claw3d analyze` uses Gemini if key is set, else returns `native_mode: true` |
| `native` | `claw3d analyze` immediately returns `native_mode: true` — you do the analysis |
| `gemini` | `claw3d analyze` uses Gemini; errors if key missing |

---

## CREATE Path: Intent Analysis for Image or Video

**Only enter this section if the Primary Gate resolved to CREATE.**

**Before doing anything with a user's image or video, run `claw3d analyze` (images) or analyze the video natively + `claw3d extract-frame --timestamp` + `claw3d analyze` (videos).**

---

### When User Sends an IMAGE (CREATE path)

**Step 1 — Always run analyze:**

```bash
claw3d analyze --input <MediaPath> [--description "user's message"] [--pretty]
```

**Step 2 — Read the result and branch:**

#### Result has `native_mode: true` → you are the analysis layer

Analyze the image yourself using these rules:

**Classify `image_type`:**
- `sketch`: hand-drawn, pencil/pen outlines, whiteboard drawings → intent is almost always `create_new`, proceed directly
- `photo`: real photograph → read description carefully
- `3d_model`: CAD rendering or existing 3D model screenshot
- `reference`: product photo, inspiration, logo

**Decide `needs_clarification`:**

**OVERRIDE — replicate/copy intent always sets `needs_clarification: false`:**
If the user's message contains any of: "make another one", "copy this", "replicate this", "clone this", "I want one like this", "same as this", "reproduce this", "duplicate this", "print this one" — the photo/frame IS the complete design reference. Proceed directly to convert. Do NOT ask for a drawing. The whole point is that they're showing you the exact object they want.

`false` (proceed without asking) when ALL of these are true:
- Single clear subject identified
- The description or image already specifies at least one key design constraint (size, mounting type, orientation, number of units, etc.)
- Sketches always qualify — the drawing itself conveys the shape intent

`true` (ask ONE clarifying question) when ANY of these:
- Complex scene with multiple objects and no description
- Custom functional or structural object (holder, bracket, stand, organizer, case, clip, mount, etc.) where the description does NOT specify key design details — even if the object is clearly identified — **but only if there is no replicate/copy intent (see override above)**
- Subject is clear but could be made many ways (e.g. "a wine holder" — wall-mount or freestanding? holds 1 bottle or multiple? specific angle?)
- Abstract or landscape photo with no description
- "Make this better" / "improve this" with no context

**Rule of thumb for functional objects:** If you could design it 3+ different ways and the user hasn't said which way → send the frame/image back and ask them to draw on it (see below). **Exception: replicate intent (see override above) → always proceed directly.**

**If `needs_clarification: false`:**

**Step A — Tell the user you're starting** (do NOT stay silent):
> "Creating your 3D model now — I'll send it when it's ready!"

**Step B — Write a `suggested_prompt` and run convert:**
```bash
claw3d convert --image <MediaPath> --prompt "<suggested_prompt>" --output model_<ID>.glb
```

**CRITICAL — When writing `suggested_prompt`:**

**For replicate/copy intent** ("make another one", "copy this", etc.):
Keep it SHORT — one sentence. The image already carries the shape. Do NOT add dimensions, material suggestions, or printing advice.
- ✅ "a replica of the black S-hook, matching its exact shape for hanging kitchen utensils"
- ✅ "a replica of the wooden phone stand shown in the image"
- ❌ "A 3D model of a sturdy S-shaped utility hook, designed for 3D printing, with a flat bar profile and rounded edges. The hook should be approximately 7-8 cm in length..." ← WAY too long, invents dimensions

**For all other intents:**
Describe ONLY the 3D object to be printed. Keep it to 1-2 sentences max. Do NOT include:
- Dimensions or measurements (the image conveys scale)
- Material or printing recommendations (PETG, PLA, etc.)
- Scale references ("sized based on the dog for scale")
- People, hands, or human body parts visible in the image
- Background items, decorations, scene context

Example — user shows a wine bottle next to a dog sculpture:
- ❌ WRONG: "An L-shaped wine holder sized appropriately based on the teal dog sculpture for scale"
- ✅ RIGHT: "An L-shaped wine bottle holder with a circular opening at a 45° angle, wall-mountable"

**If `needs_clarification: true`:**

Two cases:

**Case 1 — Ambiguous subject** (multiple objects, unclear what to print):
Ask ONE specific text question:
> "I see a desk with a laptop and a mug. Which item would you like to 3D print?"

**Case 2 — Subject is clear but it's a photo of a functional/custom object** (holder, bracket, case, mount, stand, organizer, etc.):
1. **Note the original frame path** (e.g. `frame_1a589237.jpg`) — you will need it when the annotated image comes back.
2. Send the extracted frame back to the user and ask them to draw on it in red:
   > "Hey! Could you draw in red on this image to show me the shape you have in mind? Any drawing app works — even a quick scribble on your phone. Then send it back and I'll use it as the design reference."
   Use the `message` tool to attach the frame — do NOT use inline MEDIA: syntax:
   `message(text="Hey! Could you draw...", media="<frame_path>")`
3. Wait for the user to send back the annotated image.

**When the user sends back the annotated image:**
Do NOT say "Yes! On it!" and stop — immediately run exec:
```bash
claw3d convert --image <original_frame_path> --annotated-image <annotated_MediaPath> --prompt "<description of the object, NO scene context>" --output model_<ID>.glb
```
- `<original_frame_path>` = the frame you sent them (e.g. `frame_1a589237.jpg`)
- `<annotated_MediaPath>` = the absolute path from the media attached message
- Then run preview + send both files as usual

---

#### Result has `native_mode: false` (Gemini was used) → act on the JSON

```json
{
  "subject": "a wooden phone stand",
  "image_type": "sketch",
  "intent": "create_new",
  "needs_clarification": false,
  "clarification_question": null,
  "suggested_prompt": "a minimalist wooden phone stand with a 70° angled back support..."
}
```

| `intent` | Action |
|---|---|
| `create_new` | Check `needs_clarification` first — if false, then `claw3d convert --image <MediaPath> --prompt "<suggested_prompt>" --output model_<ID>.glb` |
| `create_attachment` | Same as `create_new` |
| `find_existing` | This shouldn't appear here — Primary Gate should have caught it. But if it does: go to `03-directory` module |

If `needs_clarification: true`:
- **First check for replicate/copy intent in the user's description** — if present ("make another one", "copy this", "replicate", etc.), override to `false` and proceed directly regardless of what Gemini returned.
- Otherwise: send `clarification_question` verbatim (Gemini wrote it to be friendly and specific)
- Do NOT rephrase
- After user replies, re-run: `claw3d analyze --input <MediaPath> --description "<original + reply>"`
- After one round, always proceed

---

### When User Sends a VIDEO (CREATE path)

**You should only be here if the Primary Gate resolved to CREATE.**

**Step 1 — Extract the best frame**

Two paths depending on how the video arrived:

**Case A — Video attached as media (you can see the video in this conversation):**
You are a multimodal agent. Analyze the video directly to identify the best frame:
- Subject fully in frame, clear and well-lit
- Best reveals the 3D shape (front 3/4 angle preferred)
- Not blurry, not mid-motion, not transitioning

Pick the exact timestamp (HH:MM:SS), then extract:
```bash
claw3d extract-frame --input <video_path> --timestamp <HH:MM:SS> --output frame_<ID>.jpg
```

**Case B — Only text Description, no media in conversation (OpenClaw pre-processed the video):**
You cannot see the video — you only have the text Description. Do NOT guess a timestamp from text. Use Gemini API for smart frame selection:
```bash
claw3d extract-frame --input <video_path> --output frame_<ID>.jpg
```
(no `--timestamp` → Gemini picks the best frame automatically)

If this fails because no Gemini API key is configured, stop and tell the user:
> "I need a Gemini API key to pick the best frame from your video (the video isn't directly visible to me in this conversation). Please run:
> `claw3d configure analysis --gemini-api-key <YOUR_KEY>`
> You can get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey)."

**Step 2 — Analyze extracted frame:**
```bash
claw3d analyze --input frame_<ID>.jpg --description "<user's message or Gemini description>" --pretty
```
Then follow the IMAGE flow above (including `needs_clarification` checks).

**CRITICAL — Do NOT go silent after frame extraction.** If `needs_clarification: false`, tell the user you're generating the model BEFORE running `claw3d convert`. The full sequence must be:
1. "Great, let me take a look at what you need — give me a moment!" (from earlier)
2. Extract frame + analyze (Steps 1-2)
3. **"Creating your 3D model now — I'll send it when it's ready!"** ← say this BEFORE convert
4. Run `claw3d convert` → `claw3d preview` → send both files

---

## Full Example Flows

**Generic functional object — search first (even if user says "create"):**
```
User: [sends video] "I need you to create a wine stand"
→ Primary Gate: wine stand = common, functional → SEARCH path
→ Go to 03-directory module: search → thumbnails → pick → confirm → download → preview
```

**Video demonstrating a common object — STILL search first:**
```
User: [sends video showing how they'd hold a wine bottle, describing an L-shaped holder]
→ Primary Gate: wine holder = common, functional → SEARCH path (video demo ≠ custom design)
→ Go to 03-directory: search "L-shaped wine bottle holder" → thumbnails → pick
```

**Same object + artistic constraint — create:**
```
User: [sends video + photo of sculpture] "I need a wine stand in the style of this sculpture"
→ Primary Gate: style constraint present → CREATE path
→ claw3d extract-frame → analyze (photo as reference) → convert with prompt + image
```

**Sketch → 3D model (CREATE path):**
```
User: [sends pencil sketch of a bracket]
→ Primary Gate: sketch present → CREATE path
→ claw3d analyze --input sketch.jpg --description "make this"
  (native: sketch → create_new, needs_clarification: false, proceed directly)
→ claw3d convert --image sketch.jpg --prompt "an L-shaped bracket with two mounting holes" --output model_abc.glb
```

**Generic object, user says "I want this" with a photo:**
```
User: [sends photo of a mug] "I want this"
→ Primary Gate: mug = common object → SEARCH path
→ Go to 03-directory: search "mug" → thumbnails → confirm → download → preview
```

**Custom functional object (specific, unlikely to exist):**
```
User: [sends photo of a weird desk edge] "make a phone holder that clips onto this exact edge"
→ Primary Gate: too specific/personal to exist → CREATE path
→ analyze → needs_clarification → ask for sketch on the photo
```

**Video — user asking to find (any wording):**
```
User: [sends video, description: "person asking to find/create a wine stand, demonstrates with bottle"]
→ Primary Gate: wine stand = common functional object → SEARCH path
→ Go to 03-directory module
```

**Search exhausted → fallback to CREATE:**
```
→ 3 searches, 15 thumbnails reviewed, none match
→ "Couldn't find a good match. Want me to generate a custom one with AI?"
User: "yes"
→ If user has a video/photo: use it as reference for CREATE path
→ Extract frame (if video) → analyze → clarification if needed → convert
```

---

## Commands Reference

```bash
# Image intent analysis (outputs JSON)
claw3d analyze --input <image> [--description "text"] [--annotated <image>] [--pretty]

# Video frame extraction
claw3d extract-frame --input <video> [--output frame.jpg] [--timestamp HH:MM:SS]

# Analysis layer configuration
claw3d configure analysis                                 # show status
claw3d configure analysis --mode native                  # use your own AI
claw3d configure analysis --mode auto                    # gemini if available, else native
claw3d configure analysis --mode gemini                  # always use Gemini
claw3d configure analysis --gemini-api-key <KEY>         # set Gemini key
claw3d configure analysis --clear                        # remove Gemini key
```

<!-- /MODULE: intent -->

---

# Module: AI Model Creation

**You CAN convert 2D images to 3D models AND edit existing 3D models (GLB).** When the user sends a GLB and asks to modify it (e.g. "make it blue", "add wheels"), use `claw3d convert --edit-3d <GLB_MediaPath>`. When they send an image, use `--image`.

## When to Use

- **"Modify this 3D model"** / **"Change the color"** / **"Make it blue"** (user sent a GLB) — use `--edit-3d` flow
- "Turn this sketch into a 3D model" / "Make this image a 3D model"
- "Convert this to 3D" / "Create a 3D model from this photo"
- "Could we 3D print this?" (with image) — convert first, then slice and print
- "3D print this image" / "Print this as a 3D"

**Always require an image or sketch.** Do not use text-only `--prompt` for new model creation — results are not accurate enough. If the user asks to "make a cup" without an image, ask them to send a sketch or photo, or offer to search Thingiverse instead.

**CRITICAL — User sent a GLB and wants to edit it:** Run `claw3d convert --edit-3d <GLB_MediaPath> --prompt "..." --output edited_<ID>.glb`. Never say you cannot edit 3D models.

## Acknowledge Before Converting

**When the user asks to create a 3D model from an image OR to edit a 3D model**, REPLY IMMEDIATELY first:
- "Yes! Give me a minute—I'll let you know when the 3D model is ready."
- "On it! I'll work on that now and get back to you when it's done."

Image conversion takes 1–2 minutes. Edit-3d can take 5–10+ minutes when Hunyuan is cold. Do NOT stay silent—always acknowledge first.

## Critical: Image from Chat

When the user attaches an image, the message includes a **MediaPath**. **Always** pass that exact path to `--image`. Copy it character-for-character.

**IMPORTANT — Unique output paths:** Derive a short ID from the MediaPath. Format: `.../file_13---b10560d7-18fd-40e9-8a49-996ad190a26c.jpg` — use first 8 chars after `---` (e.g. `b10560d7`) as `ID`.

**Build volume:** Before running `claw3d preview`, check if a printer is configured with a known build volume: run `claw3d printer list` and look for `[WxDxH mm]` (e.g. `[350×350×350mm]`). If found, pass `--build-volume WxDxH` (e.g. `--build-volume 350x350x350`) — this renders the grey build plate and grid under the model for a realistic preview.

```bash
ID=b10560d7   # from MediaPath
claw3d convert --image <MediaPath> --output model_${ID}.glb
# With printer build volume (preferred):
claw3d preview --input model_${ID}.glb --output preview_${ID}.mp4 --build-volume 350x350x350
# Without printer configured:
claw3d preview --input model_${ID}.glb --output preview_${ID}.mp4
```

If the MediaPath has no UUID (unusual), use `date +%s` for a unique ID. **NEVER** send `model.glb` or `preview.mp4` that existed before this request.

## Edit-3D Workflow (MUST follow in order)

1. **Acknowledge** — "On it! Editing the 3D model. The Hunyuan step can take a few minutes when cold."
2. **Run convert** — `claw3d convert --edit-3d <GLB_MediaPath> --prompt "..." --output edited_<ID>.glb`
   - Edit-3D can take 5–10+ minutes. If it backgrounds, call `process poll <session>` with `timeout: 120000`. You will be notified when it completes — do NOT poll in a rapid loop.
   - When you see `Wrote edited_<ID>.glb` → convert is done.
3. **Run preview** — `claw3d preview --input edited_<ID>.glb --output preview_edited_<ID>.mp4 [--build-volume WxDxH]`
   - **NEVER use `--real-scale`** for edited models. AI-regenerated models use normalized units (~1 unit), not mm. The preview auto-scales the model to fill the build volume.
   - Same: wait for result or single poll with `timeout: 120000`.
4. **Send BOTH files — TWO message() calls required. You are NOT done after sending the preview.**
   ```
   message(action="send", text="Here's the updated preview!", media="preview_edited_<ID>.mp4")
   message(action="send", text="And the edited model:", media="edited_<ID>.glb")
   ```
   **CRITICAL: Do NOT end your turn after the first message(). You MUST send the .glb in a second message() call. The user needs the 3D model file, not just the video. Your turn is only complete after BOTH files are sent.**

**NEVER use --image for a GLB** when modifying. --image is for 2D sketches/photos.

## Convert Workflow (image/sketch → 3D)

1. **Acknowledge** — "Yes! Give me a minute—I'll let you know when the 3D model is ready."
2. **Check build volume** — Run `claw3d printer list`; note `[WxDxH mm]` if present.
3. **Run convert** — `claw3d convert --image <MediaPath> --output model_<ID>.glb`
   - Convert takes 1–2 minutes. The exec call will wait for it to finish (up to 2 min).
   - If it backgrounds (`Command still running`), call `process poll <session>` once with `timeout: 120000`. You will get notified when it completes — do NOT poll in a rapid loop.
   - When you see `Wrote model_<ID>.glb` → convert is done. Proceed immediately.
4. **Run preview** — `claw3d preview --input model_<ID>.glb --output preview_<ID>.mp4 [--build-volume WxDxH]`
   - Same as above: wait for the result or poll once with `timeout: 120000`.
   - When you see `Wrote preview_<ID>.mp4` → preview is done. Proceed immediately.
5. **Send BOTH files — TWO message() calls required. You are NOT done after sending the preview.**
   ```
   message(action="send", text="Here's your 3D model preview!", media="preview_<ID>.mp4")
   message(action="send", text="And the 3D model file:", media="model_<ID>.glb")
   ```
   **CRITICAL: Do NOT end your turn after the first message(). You MUST send the .glb in a second message() call. The user needs the 3D model file, not just the video. Your turn is only complete after BOTH files are sent.**
6. **ALWAYS ask about printing** — After sending the preview and model, ask:
   > Want me to slice this for 3D printing? If so, I need:
   >
   > 1. **Max print size** — What's the longest dimension? (e.g. 100mm, 150mm)
   > 2. **Strength** — How strong? (10%, 25%, 50%, 75%, or 100%)
   > 3. **Detail** — How much print quality? (10%, 25%, 50%, 75%, or 100%)

   This is **mandatory** for AI-generated models — they have no real-world dimensions, so you MUST get the max print size from the user before slicing. Do NOT slice without asking. Do NOT use a default size.

**CRITICAL:** Run convert and preview via exec BEFORE sending. The files do not exist until you create them.

## Commands

```bash
# Image/sketch → 3D
claw3d convert --image <MediaPath> [--prompt "extra description"] --output model_<ID>.glb

# Multiview: 4-quadrant image → Gemini → Hunyuan3D
claw3d convert --image multiview.png --multiview [--prompt "add wheels"] --output model_<ID>.glb

# Edit 3D: modify existing GLB
claw3d convert --edit-3d model.glb --prompt "make it blue" --output edited.glb

# Preview
claw3d preview --input model_<ID>.glb --output preview_<ID>.mp4

# Scale
claw3d scale --input model.glb --output scaled.glb --scale 0.5
```

## Prerequisites

- **FAL_API_KEY** — Required for convert (set in Control UI → Skills → claw3d)
- **Preview** — Headless: xvfb and xauth; or use openclaw:claw3d Docker image

## Error Handling

| Error | Check |
|-------|-------|
| Convert fails | FAL_API_KEY set, image exists, PNG/JPG |
| No image URL in FLUX response | FAL key valid; try again (transient) |
| Preview fails | Headless: apt install xvfb xauth |

**API key errors:** When convert fails with "FAL API key" or "401/403", ask the user to verify their API key in Control UI → Skills → claw3d. Get a key at https://fal.ai/dashboard/keys

---

# Module: 3D Model Search (Thingiverse Library)

**You CAN search for existing 3D models on Thingiverse.** Use `claw3d find`, `claw3d fetch`, and `claw3d preview` — do NOT use web search.

## When to Trigger This Flow

The intent classifier (`06-intent.md`) sets `consider_search: true` for common/functional objects. When that happens — or when the user explicitly asks to find/search/download a 3D model — follow this workflow.

**Skip this flow and go straight to AI generation** only when the user explicitly says "custom", "artistic", or describes something that clearly doesn't exist as a standard printable part.

---

## Full Workflow: Find → Pick → Preview

### Step 0 — Acknowledge (if triggered by video or image)

Before running anything, send:
> "Great, let me take a look at what you need — give me a moment!"

### Step 1 — Find fitting models (single command)

Run one command. It searches Thingiverse, downloads all thumbnails, fetches each model, packs multi-part models, and fit-checks all of them — returning only the models that physically fit in the printer.

```bash
claw3d find "<query>" --max-passing 4
```

**⚠ `claw3d find` is a long-running command (1–2 minutes).** When you see `Command still running`, this is the SEARCH running — NOT slicing. Do NOT say "Slicing started". Just poll silently with `process poll <session>` every 10 seconds until it finishes.

**Output format:**
```
[1] Balancing Wine Holder
    ID: 660698
    URL: https://www.thingiverse.com/thing:660698
    By: Tanacota
    Thumbnail: thumb_660698.jpg
    Model: model_660698.glb
    Extents: 153.8×160.5×69.8mm
    Rotation applied: none

[2] ...
```

- Build volume is auto-read from the default printer. Pass `--build WxDxH` to override.
- Exit 0 = at least one fitting model found. Exit 1 = none found — refine query and retry.
- All model files are already downloaded and pre-rotated (if a rotation was needed to fit).

### Step 2 — View thumbnails, pick best 4

View all returned thumbnail files visually (you are multimodal). Pick the **4 that best match** what the user needs — considering shape, function, and apparent quality. Record the thing ID for each.

**If fewer than 4 passed**, use however many there are.
**If exit 1 (none fit)**: run `claw3d find` with a refined query (change keywords, add constraints), up to 3 rounds total. After 3 rounds with no match, fall back to AI generation.

### Step 3 — Stamp A/B/C/D badges onto thumbnails, compose grid, send to user

Stamp option letters and compose a single 2×2 grid image (A top-left, B top-right, C bottom-left, D bottom-right):

```bash
claw3d stamp-thumbnails --grid thumb_660698.jpg thumb_123456.jpg thumb_789012.jpg thumb_456789.jpg
# Outputs: thumb_660698_A.jpg, thumb_123456_B.jpg, thumb_789012_C.jpg, thumb_456789_D.jpg
# Grid:   thumb_grid_thumb_660698.jpg  (single 2x2 image)
```

**MANDATORY: Send ONE message with the grid image attached.** Do NOT describe the options without the image. Do NOT skip the `media=` parameter. The user needs to SEE the thumbnails to choose — text-only is useless.

```
message(action="send", text="Here are four options I found:\n\nA — [name/brief reason]\nB — [name/brief reason]\nC — [name/brief reason]\nD — [name/brief reason]\n\nReply with A, B, C, or D — or let me know if none look right and I'll search again or create a custom one.", media="thumb_grid_thumb_660698.jpg")
```

**The `media=` field with the grid image path is REQUIRED.** If you send this message without the grid image attached, the user cannot see the options.

Wait for user response before continuing.

- **User picks A, B, C, or D**: read the thing ID from the `claw3d find` output for that option. Continue to Step 4 with that ID. The model is already downloaded and pre-rotated (if needed) — no re-fetch required.
- **User says none / not quite**: run `claw3d find` with a refined query, repeat from Step 1 — up to 3 rounds total
- **After 3 rounds with no match**: fall back to AI generation

### Step 4 — Get grouped file list (deterministic extension selection)

The chosen model is already downloaded. Use its thing ID to inspect variant/part structure:

```bash
claw3d fetch --list-grouped <thing_id>
```

This deterministically selects the best extension group (STL > OBJ > GLB > 3MF). Parse the output:

- `Best extension: .stl (N file(s))` — what will be downloaded
- `Sub-variants (size/version choices…)` — only shown if multiple size/version options exist
- `Multi-part model (N components…)` — only shown if multiple parts with no size variants

### Step 5 — Handle sub-variants or cosmetic variations (if any)

Read the `--list-grouped` output and follow exactly **one** of these branches:

**→ Output shows "Sub-variants" (size/version choices):**
Ask the user which size/version they want:
> "This model comes in several sizes: small, medium, large. Which would work best for you?"
Once user picks, use `--choose "<variant_tag>"` in Step 6.

**→ Output shows "Cosmetic variations" (same model, minor differences):**
Do NOT ask the user. Auto-select the variant marked `<- auto-selected` and inform them:
> "This model has a [no-text / simplified / …] version — I'll use that for a cleaner print."
Use `--choose "<auto_selected_filename_keyword>"` in Step 6. E.g. if `TiltedWineBottleStand_NoText.stl` is auto-selected, use `--choose "NoText"`.

**→ Output shows "Multi-part model" (multiple components):** all parts are needed — model was already packed by `claw3d find`. Skip directly to Step 7.

**→ Single file or complete-set:** model already downloaded by `claw3d find` — skip directly to Step 7.

### Step 6 — Re-fetch with variant/cosmetic choice (only if sub-variant or cosmetic was needed)

Skip this step if no `--choose` is needed (single file, complete-set, or already fetched correctly).

**With sub-variant chosen (e.g. user picked "large"):**
```bash
claw3d fetch <thing_id> --choose "large" -o model_<ID>.glb
claw3d fit-check -i model_<ID>.stl --apply-rotation
```

**With cosmetic variant auto-selected (e.g. NoText):**
```bash
claw3d fetch <thing_id> --choose "NoText" -o model_<ID>.glb
claw3d fit-check -i model_<ID>.stl --apply-rotation
```

### Step 7 — Dimensions (automatic)

**`claw3d find`** auto-computes dimensions from the fitted extents. The `Extents:` line in the output is the already-rotated bounding box.

> Only run `claw3d dimensions -i <file>` manually if the file was re-fetched in Step 6 (variant selection).

### Step 8 — Generate preview with build plate shown

Build volume is auto-read from the default printer config. Generate the preview with **`--real-scale`** so the user sees the model at its actual physical size relative to the build plate:

```bash
claw3d preview -i model_<ID>.glb -o preview_<ID>.mp4 --real-scale
# or for multi-plate:
claw3d preview -i model_<ID>_plate1.glb -o preview_<ID>_p1.mp4 --real-scale
claw3d preview -i model_<ID>_plate2.glb -o preview_<ID>_p2.mp4 --real-scale
```

`--real-scale` shows the model at its true mm dimensions on the plate. `--build-volume` is auto-read from the default printer (no need to pass it). If no printer is configured yet, ask the user for their build volume and pass it explicitly.

### Step 9 — Send preview(s) to user

**Important:** Thingiverse thumbnails are often lifestyle renders that can look very different from the actual printable model. The 3D preview video is the ground truth — always describe the dimensions so the user understands what they're actually getting.

**Single plate:**
```
message(action="send", text="Here's the 3D preview of option [A/B/C] — [model name]. Print size: X × Y × Z mm. Does this look right? If it doesn't match what you expected from the thumbnail, say so and I'll try the next option.", media="preview_<ID>.mp4")
```

**Multi-plate (N plates needed):**
```
message(action="send", text="This model needs N separate prints. Here's plate 1 (X × Y × Z mm):", media="preview_<ID>_p1.mp4")
message(action="send", text="Plate 2 (X × Y × Z mm):", media="preview_<ID>_p2.mp4")
# … all plates
message(action="send", text="Print them sequentially and assemble. Ready to slice when you are!")
```

---

## Printing Multiple Copies (Duplicate / Fill Plate)

When the user asks to print N copies of a model ("add 3 more", "print 4 of these", "fill the plate"):

1. **Use `claw3d pack --copies N`** on the original STL sidecar. Pass any rotation the user wants baked in via `--rotation-x/y/z`. The packer places all N copies with 2mm gaps.

```bash
# 4 copies, standing up (rotation-x 90), on a 220×215×245mm plate:
claw3d pack -i model_<ID>.stl --copies 4 --rotation-x 90 --build 220x215x245 -o model_<ID>_x4.stl
```

2. **If pack exits with error** ("exceeds build volume"): tell the user how many fit per plate, pack that many, slice, then ask if they want more plates.

3. **If pack produces multiple plates** (`model_<ID>_x4_plate1.stl`, `model_<ID>_x4_plate2.stl`): slice and queue each plate separately.

4. **Slice the packed STL** directly — no rotation flags needed (rotation already baked by pack):

```bash
claw3d slice -i model_<ID>_x4.stl -p <profile_id> -o model_<ID>_x4.gcode --build-volume <WxDxH>
```

**Rotation is already baked in by `--rotation-x/y/z` in the pack step — do NOT also pass rotation to `claw3d slice`.**

---

## Fallback: AI Generation

If no Thingiverse result matches, say:

> "I couldn't find a good match in the Thingiverse library. I can generate a custom 3D model using AI — want me to do that?"

If yes, follow the AI generation flow from `02-ai-forger.md`.

---

## Commands Reference

| Command | Purpose |
|---------|---------|
| `claw3d find "<query>" --max-passing 5` | Search + download thumbnails + fetch + fit-check in one shot. Returns only models that fit the printer |
| `claw3d fetch --list-grouped <id>` | Best extension group + sub-variant detection (deterministic) |
| `claw3d fetch --list-only <id>` | Raw file list (complete sets vs parts) |
| `claw3d fetch <id> -o model.glb` | Download + convert to GLB |
| `claw3d fetch <id> --choose "large" -o model.glb` | Download only files matching substring |
| `claw3d pack -i dir/ --build WxHxD -o model.glb` | Arrange multi-part on build plate (2mm gap). Exit 1 if part too large |
| `claw3d pack -i model.stl --copies 4 --build WxHxD -o model_x4.stl` | Duplicate single model 4 times on plate |
| `claw3d pack -i model.stl --copies 4 --rotation-x 90 --build WxHxD -o model_x4.stl` | Duplicate with baked rotation |
| `claw3d fit-check -i model.stl --apply-rotation` | One-off fit check: exits 0 = fits, exits 1 = doesn't fit |
| `claw3d dimensions -i model.glb` | Bounding box + save `.dimensions.json` sidecar for future slicing |
| `claw3d preview -i model.glb -o preview.mp4` | 360° turntable video |

---

## Prerequisites

- **THINGIVERSE_ACCESS_TOKEN** — Free App Token from https://www.thingiverse.com/apps/create

## Error Handling

| Error | Action |
|-------|--------|
| No results / 401 | Check THINGIVERSE_ACCESS_TOKEN in Control UI → Skills → claw3d |
| "No directory providers configured" | Add token in Control UI |
| `claw3d find` exit 1 (0 fitting models) | Refine query and retry, up to 3 rounds; then AI generation |
| `claw3d find` not found | Rebuild Docker: `docker build -f Dockerfile.claw3d -t openclaw:claw3d .` then restart |

---

<!-- MODULE: slicing -->

## Slicing — Profile Selection

**NEVER use hardcoded or remembered profile IDs.** Profile IDs are stored on the slicer server and are lost when the container restarts. Before every slice:

1. Run `claw3d profile list` — use whatever ID is listed there.
2. **If 0 profiles:** User must send a 3MF (use `--profile-from-3mf`) or create a profile first.
3. **If 1 profile:** Use it with `--profile <id>`.
4. **If 2+ profiles:** Ask in a numbered list, or use the printer's linked profile if the user chose a printer for this print.

## Source-Based Auto-Routing (Deterministic)

`claw3d slice` reads the `.source.json` sidecar automatically. When it detects `"source": "thingiverse"`, it:
- Auto-enables `--no-mesh-clean` (skips mesh repair)
- Auto-skips scaling (no 100mm default)

**You do NOT need to pass `--no-mesh-clean` manually** — the code handles it. Just pass the model file and the slicer does the right thing based on provenance.

When re-slicing, the previous settings are saved in `.slice_config.json` and reused automatically (max-dimension, strength, quality). You only need to pass flags that changed.

## Max Print Size — Two Paths

**Path A: Model from directory (Thingiverse)** — The model is already at the correct physical size. **NEVER ask for max print size.** Do NOT pass `--max-from-model` or `--max-dimension`. The source-based routing handles this automatically.

- **Prefer the `.stl` sidecar** (`model_<ID>.stl`) if it exists — send it directly, no conversion.
- **If only `.glb` exists** (model was fetched as GLB): use `model_<ID>.glb`. The auto-routing will apply `--no-mesh-clean` automatically.

Ask the user only:
> Before I slice, I need two things:
>
> 1. **Strength** — How strong should it be? (10%, 25%, 50%, 75%, or 100%)
> 2. **Detail** — How much print detail / quality? (10%, 25%, 50%, 75%, or 100%)

**Path B: Model from AI or user-provided** — Use `model_<ID>.glb`. No dimensions file. **MUST ask** for max print size, strength, and detail before slicing. Use the printer's build volume (from `claw3d printer list`) as the default max dimension suggestion — use the smallest of width/depth/height.

> Before I slice, I need a few things:
>
> 1. **Max print size** — What's the longest dimension you want? (e.g. 100mm or 150mm)
> 2. **Strength** — How strong should it be? (10%, 25%, 50%, 75%, or 100%)
> 3. **Detail** — How much print detail / quality? (10%, 25%, 50%, 75%, or 100%)

**Map percentages to CLI:** 10%→1, 25%→2, 50%→3, 75%→4, 100%→5. Use `--max-dimension <N>`, `--strength`, `--quality`.

**Natural language → CLI flags:**
- "make it stronger" → `--strength 4`
- "20% infill" → `--infill-density 20`
- "fit in 100mm" → `--max-dimension 100`
- "rotate 90 degrees on Y" → `claw3d rotate -i model.glb --rotation-y 90` (then preview/slice without rotation flags)
- "rotate 45 on X" → `claw3d rotate -i model.glb --rotation-x 45`
- "more detail" / "higher quality" / "thinner layers" → `--quality 4` or `--layer-height 0.1`

**Bed leveling:** Do NOT add `--bed-autocalibration` unless the user explicitly asks. Default OFF.

## Rotation Workflow — Baked Into File

`claw3d rotate` permanently modifies the model file. Rotation is cumulative by design — each call rotates from the model's current orientation, like dragging an object in a 3D editor. No state tracking needed.

**When the user asks to rotate a model** ("rotate 90 on X", "flip it sideways", "turn it upside down"):

**Step 1 — Rotate the file:**
```bash
claw3d rotate -i model_<ID>.glb --rotation-x 90
```
The GLB is now permanently rotated. All future preview/slice commands use the file as-is — no rotation flags needed.

**Step 2 — Show preview (no rotation flags):**
```bash
claw3d preview -i model_<ID>.glb --build-volume <WxDxH> -o preview_<ID>_rotated.mp4
```
Send with: "Here it is rotated 90° on X — does this look right for printing?"

**Step 3 — When user confirms, slice (no rotation flags):**
```bash
claw3d slice -i model_<ID>.glb -p <profile_id> -o model_<ID>.gcode --build-volume <WxDxH>
```

**Multiple rotations just work:**
| User says | You run | Result |
|---|---|---|
| "rotate 90 on X" | `claw3d rotate -i model.glb --rotation-x 90` | Model is now 90° on X |
| "now rotate 90 on Y" | `claw3d rotate -i model.glb --rotation-y 90` | Model is now 90° X + 90° Y |
| "and 45 on Z" | `claw3d rotate -i model.glb --rotation-z 45` | All three rotations accumulated |

**Natural language mapping:**
- "flip it" / "turn it upside down" → `--rotation-x 180`
- "turn it sideways" → `--rotation-y 90`
- "rotate 90 on X and 45 on Z" → `--rotation-x 90 --rotation-z 45` (one command)

**Undo rotation:** If the user says "undo that rotation" or "go back":
```bash
claw3d rotate -i model_<ID>.glb --undo
```
This restores the file from before the last rotation. Up to 5 undo levels are kept.

**Do NOT pass `--rotation-x/y/z` to `claw3d preview` or `claw3d slice`.** Always use `claw3d rotate` first — the file is the source of truth.

## Useful Diagnostic Commands

```bash
# Check what happened to a model (source, dimensions, last slice settings, files)
claw3d model-status -i model_<ID>.glb

# System health check (API keys, slicer, printers, ffmpeg)
claw3d doctor
```

## Slice Command — Background Process Handling

**CRITICAL: Both `claw3d slice` and `claw3d preview` are long-running commands. You MUST wait for them to finish before proceeding. Do NOT return control to the user while they run.**

### How long-running commands work:

The exec call waits up to 2 minutes for the command to finish. Most commands complete within this window and return the result directly. If a command takes longer, exec returns `Command still running` with a session ID. In that case:

1. Call `process poll <session>` **once** with `timeout: 120000` (2 min wait).
2. You will be notified automatically when the process completes.
3. **Do NOT poll in a rapid loop** — this wastes API calls and hits rate limits.
4. When you see `Wrote <path>` or `[timing]` → the command finished. Proceed immediately.

### For `claw3d slice`:

1. Run `claw3d slice ...` — tell the user: "Slicing started! I'll let you know when it's ready."
2. Wait for completion (exec returns result, or poll once if backgrounded).
3. When you see `Wrote <path>` for the gcode preview → **send both files immediately**.

### For `claw3d preview`:

1. Run `claw3d preview ...` — tell the user: "Generating your 3D preview, I'll send it when it's ready!"
2. Wait for completion (exec returns result, or poll once if backgrounded).
3. When you see `Wrote <path>` → **send the file immediately. Do NOT ask the user if they want it.**

**YOU MUST NOT return control to the user until you see `Wrote <path>` or an error.**

**After slice succeeds, send BOTH the G-code and the G-code preview video.** Slice generates `model_<ID>_gcode_preview.mp4` by default (body red, supports yellow). Use the `message` tool so both files attach in Telegram.

**Include print estimates in your message.** The slice output includes an `[estimates]` line with print time, filament usage, and layer count. Always include these stats when sending the G-code, e.g.: "Here's your G-code! Estimated print time: 2h 30m | Filament: 12.5m (37g) | Layers: 245"

**When the user asks for "the video" after a slice:** They mean the G-code preview (`model_<ID>_gcode_preview.mp4`). **Do NOT run `claw3d preview`** — that renders the 3D model. Send the existing gcode preview file.

**Build volume for previews:** When a default printer is configured (i.e. the printer was added with `--profile-from-3mf`), `claw3d preview` and `claw3d slice` automatically use that printer's build volume — you do NOT need to pass `--build-volume` explicitly. If needed, you can always override with `--build-volume WxDxH` (e.g. `--build-volume 350x350x350`). The build volume renders the grey build plate, 10mm grid, and volume wireframe in the preview video. To verify the current default printer's build volume, run `claw3d printer list`.

```bash
# GLB + separate 3MF (most common) — read build volume from printer list
claw3d slice -i <glb_path> --profile-from-3mf <3mf_path> -o model_<ID>.gcode --build-volume <WxDxH>

# Thingiverse/directory model — use .stl sidecar if it exists (preferred: no conversion, no mesh fixes)
claw3d slice -i model_<ID>.stl -p <profile_id> -o model_<ID>.gcode --strength 3 --build-volume <WxDxH>

# Thingiverse/directory model — GLB only (no .stl sidecar): must use --no-mesh-clean
claw3d slice -i model_<ID>.glb -p <profile_id> -o model_<ID>.gcode --strength 3 --no-mesh-clean --build-volume <WxDxH>

# AI/user model — use .glb (must ask for max)
claw3d slice -i model.glb -p <profile_id> -o model.gcode --max-dimension 150 --strength 4 --build-volume <WxDxH>

# Single 3MF (model + settings in one file)
claw3d slice -i project.3mf -o model.gcode

# Per-parameter overrides
claw3d slice -i model.glb -p <profile_id> -o model.gcode --infill-density 20 --layer-height 0.15
# Rotation: use `claw3d rotate` first, then slice without rotation flags
claw3d rotate -i model.glb --rotation-y 90
claw3d slice -i model.glb -p <profile_id> -o model.gcode

# Profile management
claw3d profile create --from-3mf settings.3mf --name my_pla
claw3d profile list
claw3d profile set-default <profile_id>
claw3d profile clear   # delete all profiles (fresh start)

# Standalone preview with build area (read WxDxH from printer list)
claw3d preview --input model.glb --output preview.mp4 --build-volume <WxDxH>
claw3d gcode-preview --input model.gcode --output gcode_preview.mp4 --build-volume <WxDxH>
```

## Slice Flags Reference

| Flag | Description |
|------|-------------|
| `-i`, `--input` | Input GLB, STL, or 3MF |
| `-o`, `--output` | Output G-code path |
| `-p`, `--profile` | Profile ID (use `--profile` OR `--profile-from-3mf` for GLB/STL) |
| `--profile-from-3mf` | Create profile from 3MF, then slice |
| `--strength` | 1–5 (10%→1 … 100%→5). Default 3 |
| `--quality` | 1–5 (10%→1 … 100%→5). Detail / print quality level |
| `--max-dimension` | Scale longest axis to N mm (AI models) |
| `--max-from-model` | Use max from dimensions.json (directory models) |
| `--no-mesh-clean` | Skip all mesh repair during GLB→STL conversion. **Required for directory/Thingiverse GLBs** — mesh fixes are for AI models only and can delete real model geometry |
| `--rotation-x` | ⚠️ **Prefer `claw3d rotate` instead** — bakes rotation into file. Only use in slice/preview for one-off tests |
| `--rotation-y` | Same as above |
| `--rotation-z` | Same as above |
| `--layer-height` | Override layer height in mm (e.g. 0.15) |
| `--infill-density` | Override infill percentage (e.g. 20) |
| `--preview-video` | Generate 360° G-code preview video (default ON) |
| `--no-preview-video` | Skip G-code preview video (faster) |
| `--build-volume` | `WxDxH` mm (e.g. `350x350x350`). Shows build plate + grid in gcode preview. Read from `claw3d printer list`. |
| `--bed-autocalibration` | Run bed leveling before print. **Default OFF** — only add when user explicitly asks |

<!-- /MODULE: slicing -->

---

<!-- MODULE: printing -->

## Printer Setup — Do This First

**On first use**, a printer AND a linked slicing profile are both required. The profile (created from a 3MF) stores the printer's build volume (`build_width` × `build_depth` × `build_height` in mm), which the slicer uses to scale models correctly. Without it, slicing fails.

### What the 3MF carries

When you upload a Cura project file (`.3mf`), the slicer extracts:
- `machine_name` — Printer model (e.g. "Creality K2 Pro")
- `build_width` × `build_depth` × `build_height` — Build volume in mm
- `nozzle_size` — Nozzle diameter in mm
- Full Cura machine + extruder definitions (temperatures, speeds, layer heights, etc.)

### How to export from Cura

> In Cura with your printer loaded: **File → Save → "Export Universal Cura Project"** → save as `.3mf`.

This captures the full printer config, not just the model geometry.

**Printer add flags:**
- `--name` (required): Display name, e.g. `"Creality K2 Pro Living Room"`
- `--host` (required): Printer IP or hostname
- `--port` (required): Moonraker usually 7125; Creality K2 SE often 4408
- `--profile-from-3mf` (**required for slicing**): Create and link profile from 3MF in one step. Without this, slicing will fail until a profile is linked manually via `printer set-profile`.
- `--id` (optional): CLI slug. If omitted, derived from `--name` (e.g. `"Creality K2 Pro"` → `creality_k2_pro`)

```bash
claw3d printer add --name "<name>" --host <ip> --port <port> --profile-from-3mf <path> [--id <slug>]
claw3d printer set-profile <printer_id> <profile_id>
claw3d printer set-default <id>   # only needed when 2+ printers; first printer auto-becomes default
claw3d printer remove <id>
```

**Parse user input:** "Creality K2 SE Living Room 192.168.1.100:4408" → name=`"Creality K2 SE Living Room"`, host=`192.168.1.100`, port=`4408`. If user also sends 3MF, add `--profile-from-3mf <path>`.

**Default printer:** The first printer added is automatically set as the default. When there is only one printer, it is always used without asking. When 2+ printers exist and no default is set, ask the user which to use, then run `claw3d printer set-default <id>` with their choice so subsequent operations don't need to ask again.

**No 3MF yet?** Add the printer without it, then immediately ask:
> To complete setup, please send your Cura project file (.3mf). In Cura: **File → Save → "Export Universal Cura Project"**. This gives me your exact build volume and settings.

Then: `claw3d profile create --from-3mf <path> --name "<printer_id>_profile"` → `claw3d printer set-profile <printer_id> <profile_id>`

**Fresh start:** Run `claw3d profile clear`, then re-add printer with `--profile-from-3mf`.

**Printer backends:** Run `claw3d configure backends` to see options (Moonraker, PrusaLink, etc.). Community can add backends in `claw3d/backends/`.

## Before Printing

**ALWAYS** run `claw3d printers` before sending a print:
- **0 printers:** Tell user to add a printer first.
- **1 printer:** Use it.
- **2+ printers:** Ask in a numbered list:
  > Which printer should I send the G-code to?
  > 1. [First printer name]
  > 2. [Second printer name]

## Print Commands

```bash
claw3d print --gcode model.gcode [--printer id]
claw3d status [--printer id]
claw3d pause [--printer id]
claw3d resume [--printer id]
claw3d cancel [--printer id]
claw3d camera [--printer id] [--snapshot]
claw3d preheat --extruder 200 --bed 60 [--printer id]
claw3d cooldown [--printer id]
claw3d home [--axes x y z] [--printer id]
claw3d files [--path subdir] [--printer id]
claw3d start --file model.gcode [--printer id]
claw3d emergency-stop [--printer id]
claw3d metadata --file model.gcode [--printer id]
```

## Multi-Plate Queue

When a model needs more than one build plate:
1. Slice each plate.
2. `claw3d queue add plate1.gcode --label "Plate 1"`, etc.
3. `claw3d print --gcode plate1.gcode`
4. When user says "print finished" / "next": run `claw3d queue next`, ask to start next.
5. If queue is empty (exit 1): "All plates are done!"

```bash
claw3d queue add model_plate1.gcode --label "Plate 1"
claw3d queue list
claw3d queue next    # pops and returns next path
claw3d queue clear   # clear entire queue
```

## Printer ↔ Profile

Each printer can have a linked default profile. Run `claw3d printer list` to see links including build volume. Use that profile when slicing for that printer.

```
  Creality K2 Pro (creality_k2_pro): 192.168.1.50:4408 [moonraker] [profile: creality_k2_pro_profile] [350×350×350mm] (default)
```

The build volume (`350×350×350mm`) is snapshotted from the profile when it is linked. **When slicing AI-generated or user-provided models** (no dimensions file), read the printer's build volume from `claw3d printer list` and use the smallest dimension as the default `--max-dimension` suggestion, rather than asking the user to guess.

<!-- /MODULE: printing -->
