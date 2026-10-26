# Session handover

The live note passed from chat to chat. A new chat reads `CLAUDE.md`, then this file, then `RESEARCH-BRIEF.md` and `README.md`, and carries on from its section's "Next actions". Each chat rewrites only its own section.

**Last updated:** 2026-10-23, by the setup chat ("Two-channel YouTube strategy", branch `claude/amazing-lamport-08irk0`).

---

## Where things stand (2026-10-23)

- **The operator chose two new channels** (also in `script-system/HANDOFF.md`, "Operator decisions, 2026-10-23"):
  - **Roger the HVAC Guy:** a new channel; Roger the Pipe Guy carries on. Persona and niche rules close to Roger's, with the same triggers.
  - **Frederick Barnes, a new brand:** electrical DIY, staying safe with electricity, avoiding electrical mistakes, and fire prevention. Different emotions; the focus is emotion. His background is "up for debate"; his book changes from *Prevent The Burning*.
- **The 2026-10-22 research was recovered** into `recovered/` (its chat never pushed). The parts that matter are quoted in `findings/2026-10-22-hvac-and-electrical.md`, not re-checked.
- **The plan:**
  1. Two research chats in this repository, one per niche, following `RESEARCH-BRIEF.md`.
  2. Back and forth with the operator, then conclusions.
  3. Then, on the operator's call, each niche's ideation skill, base ideation plan and thumbnail plan here.
  4. Then two scripting chats in `KPMYT/script-system`, which build the niche packs from the plumbing pack.
- **Nothing is studied yet.** `studies/` is empty.

---

## HVAC research chat

- **Owns:** `studies/hvac/`.
- **Status:** not started.
- **Next actions:**
  1. Read `CLAUDE.md`, `RESEARCH-BRIEF.md` and `findings/2026-10-22-hvac-and-electrical.md`.
  2. Show the operator the round 1 plan (helpers, sources), then run the rounds in `RESEARCH-BRIEF.md` section 4.
  3. Report the findings, go back and forth, then write `CONCLUSIONS.md`.

## Electrical and fire prevention research chat

- **Owns:** `studies/electrical/`. Branch `claude/zealous-ptolemy-lxtx6t` (not yet merged into `main`: the operator says when to hand over).
- **Status (2026-10-26):** all six rounds done and checked (helpers' work re-checked by checkers A-H; every fix in `studies/electrical/log.md`). The research report was given to the operator; waiting on their answers before `CONCLUSIONS.md`.
- **Deliverables:** `channels.md`/`.csv`, `new-channels.md`, `subniches.md`, `emotions.md`, `thumbnails/thumbnail-styles.html` (private Artifact https://claude.ai/artifact/4ZPp2yNMNRvQccsNo3yyet), `recent-winners.md`, `top-100.md`/`.csv`, `keyword-sweep.md`, `formats.md`. Built by scripts in `studies/electrical/data/tools/` (`build_docs.py`, `build_channels.py`, `build_thumb_page.py`); re-run them after any data fix.
- **Operator decisions so far:** (2026-10-26) run rounds straight through with a check after each, stop only for real decisions. (2026-10-24) narrow scope: core electrical and fire prevention; not winter blackouts (maybe later for the stopped generator channel Jack Redfield), not seniors' home safety; no money framing; Frederick's old channel isn't a guide ("full pivot"); the tiny fire inspector/marshal field "could mean we have a gap". (2026-10-23) 5-minute rule, under-5:00 hits in `short-reference.md`; Frederick's channel in the census as "ours"; find new channels.
- **Headline findings (checked):** outlets and switches, ceiling fans, lighting, connectors and testers pull far more than the classic fire-safety topics (space heaters, cords, "what starts fires", kitchen fires: medians 400-1,700); tests, inspection walkthroughs and "why does X keep doing Y" titles beat mistakes lists and "NEVER" lists (median about 200-1,600); real presenters dominate; AI-persona channels in the niche are tiny (thumbnail median 5K vs 368K for real on-camera); no fire investigator/inspector channel is big, and persona "investigator" titles don't lift views.
- **Method notes:** YouTube search's "upload date" sort no longer sorts and there's no "oldest" search sort (date windows used; `yt.py`). NexLev batch metrics lack monthly views; 30-day views come from `get_daily_analytics`, with impossible values blanked. Search-based multiples run high (compare topics, not absolutes). Emotion labels: only some are robust (see `labels.md`).
- **Next actions:**
  1. Go through the report with the operator; record their answers in `log.md`.
  2. Write `CONCLUSIONS.md` (deliverable 9) from the findings and their answers.
  3. At handover (operator's call): rewrite this section, log, commit, merge the branch into `main`, push `main`.

---

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
