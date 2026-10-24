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

- **Owns:** `studies/electrical/`. Branch `claude/zealous-ptolemy-lxtx6t`.
- **Status (2026-10-24):** rounds 1 and 2 done and checked. Round 2: 212 keywords across 6 topic sweeps; 4,758 unique in-scope long-form videos after the checkers' corrections (`studies/electrical/data/merged/`); master channel list 957 (142 core, 158 partial); corrected presenter-background table (`data/checks/presenters-summary-corrected.csv`). Round 2 summary given to the operator; waiting on the go for round 3.
- **Operator decisions so far:** (2026-10-24) narrow scope: core electrical and fire prevention; not winter blackouts (maybe a test; possibly for the stopped generator channel Jack Redfield), not seniors' home safety; no money framing needed in electrical; Frederick's old channel isn't a guide ("we pretty much need a full pivot"); the tiny fire inspector/marshal field "could mean we have a gap". (2026-10-23) 5-minute rule for counts and the top 100, with under-5:00 hits in `short-reference.md` (not counted); Frederick's channel gets a census row marked "ours"; find new channels in the niche and next to it.
- **What round 1 found (checked):** Frederick's channel is named "Frederick Barnes" (@FrederickBarnesYT), 97.7% of views on one video; the "never leave plugged in" list broke out on only 3 of 23 channels using it; persona channels in the core niche are all tiny (fire inspector/marshal personas: a few, none over 1K subs; firefighter, lineman and electrician personas mostly under 2K); the big new-channel winners are next door (winter blackouts, heat without power, backup power, seniors' safety).
- **Method notes:** YouTube search's "upload date" sort no longer sorts and there's no "oldest" search sort; the loader uses date windows (`studies/electrical/data/tools/yt.py`, paging fixed 2026-10-23). NexLev dates are rounded; its faceless check marks AI-image personas "not faceless", so channel types need thumbnails. Helpers can't write `.md` report files; the main session saves their reports.
- **Next actions:**
  1. Round 3 on the operator's go: census metrics and checked types for the core/partial channels, channel medians and multiples, the top 100, recent winners, the sub-niche map.
  2. Rounds 2-6 per `RESEARCH-BRIEF.md` section 4: keyword sweep, census metrics, top 100, sub-niche map, labelling, thumbnails, checking.
  3. Report the findings, go back and forth, then write `CONCLUSIONS.md`.

---

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
