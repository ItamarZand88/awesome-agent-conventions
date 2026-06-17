<!-- Thanks for contributing! This list lives or dies on two things: a strict
     inclusion filter and an honest maturity tier. Please confirm both. -->

## What this PR adds or changes

<!-- One or two sentences. Which convention, and why it belongs. -->

## Inclusion filter

- [ ] This is an **agent convention file** — a file an AI agent **reads, writes, or acts on** (not a human doc like `README.md` / `CONTRIBUTING.md`).
- [ ] I can name **which agent reads or writes it and what it does with it**.

## Maturity tier

- [ ] I set exactly one tier and can evidence it: 🟢 Adopted · 🟠 Emerging · 🔵 Proposed
- [ ] When in doubt I labelled **down, not up**. (Overstating a tier is the one thing that breaks this list.)

## Mechanics

- [ ] I edited **`scripts/targets.json`** (the single source of truth) — not the generated `README.md` files directly.
- [ ] Example sources are **real, public URLs** (I did not hand-write example files).
- [ ] I ran the generators and committed the result:
      `python scripts/extract.py && python scripts/build_readme.py`
- [ ] `python scripts/check_links.py` passes (all new links resolve).

<!-- New observations? Drop them in conventions/<slug>/field-notes.md — that
     sidecar survives every regeneration and is where the list earns its depth. -->
