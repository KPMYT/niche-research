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

- **Owns:** `studies/hvac/`. Branch `claude/adoring-galileo-wqloxp`.
- **Status (2026-10-24):** rounds 1 (seeds) and 2 (spread) done and checked; round 2 reported to the operator (`studies/hvac/round2/round2-report.md`). Operator decisions so far are in `studies/hvac/README.md` (among them: NexLev RPM is not used; off-grid heat is its own sub-niche; E19 comfort and E20 new-gadget wonder added).
- **Next actions:**
  1. Get the operator's answers on the round 2 questions, then run round 3: pull every tier A-D channel's own Videos tab, re-tier with the rule in `round2/check-master.md`, then the census, the top 100, recent winners and the sub-niche map.
  2. Rounds 4-7 as in `RESEARCH-BRIEF.md` section 4, then `CONCLUSIONS.md` after the back and forth.
- **For the electrical chat (passed on via the operator):** logged-out YouTube search translates foreign titles into English, so check English on the original title (oEmbed); Weirdward Bound's electrical explainers sit beside almost every Silver Cymbal HVAC video.

## Electrical and fire prevention research chat

- **Owns:** `studies/electrical/`.
- **Status:** not started.
- **Next actions:**
  1. Read `CLAUDE.md`, `RESEARCH-BRIEF.md`, `findings/2026-10-22-hvac-and-electrical.md`, and Frederick's baseline in `script-system/studies/home-diy/frederick-baseline-2026-10/`.
  2. Show the operator the round 1 plan, then run the rounds.
  3. Include the presenter-background evidence (electrician, lineman, firefighter, inspector, none) for the open decision.
  4. Report the findings, go back and forth, then write `CONCLUSIONS.md`.

---

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
