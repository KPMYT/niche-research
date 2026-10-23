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
- **Status (2026-10-23):** round 1 running (6 helpers): Silver Cymbal's electrical videos, the six known channels re-checked, Just Stop Fire, the first spread from the seeds, and two new-channel hunts (core and adjacent; the operator asked for this).
- **Operator decisions so far:** keep the 5-minute rule for counts and the top 100, with under-5-minute hits in a separate `short-reference.md` (not counted); Just Stop Fire gets a census row marked "ours".
- **Method notes:** YouTube search's "upload date" sort no longer sorts and there's no "oldest" search sort; the loader uses date windows instead (`studies/electrical/data/tools/yt.py`). NexLev upload dates are rounded; exact dates come from video pages.
- **Next actions:**
  1. When round 1 lands: commit, run the checker on a sample, report to the operator.
  2. Rounds 2-6 per `RESEARCH-BRIEF.md` section 4, including the presenter-background count (electrician, lineman, firefighter, inspector, none).
  3. Report the findings, go back and forth, then write `CONCLUSIONS.md`.

---

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
