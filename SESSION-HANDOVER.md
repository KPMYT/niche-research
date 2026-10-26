# Session handover

The live note passed from chat to chat. A new chat reads `CLAUDE.md`, then this file, then `RESEARCH-BRIEF.md` and `README.md`, and carries on from its section's "Next actions". Each chat rewrites only its own section.

**Last updated:** 2026-10-26, electrical section by the electrical research chat (branch `claude/zealous-ptolemy-lxtx6t`). Other sections as the setup chat left them on 2026-10-23.

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

- **Owns:** `studies/electrical/`. Last branch: `claude/zealous-ptolemy-lxtx6t` (merged into `main` 2026-10-26 at handover).
- **Status (2026-10-26):** all six research rounds done and checked (checkers A-H; every fix in `studies/electrical/log.md`). **The operator has not read the findings yet** ("i have read none of this yet"). Everything they need is in **`studies/electrical/REPORT-2026-10-26.md`**: what was done, the findings in plain words with tables, and 4 questions.
- **Next chat, start here:**
  1. Read `CLAUDE.md`, this section, then `studies/electrical/REPORT-2026-10-26.md` (and `log.md` for detail if needed).
  2. Walk the operator through the report in short messages: the topics table, the title shapes, who presents, thumbnails (page: https://claude.ai/artifact/4ZPp2yNMNRvQccsNo3yyet, private), then the 4 questions (1 electrical-first with fire as payoff; 2 Frederick's background, suggested a retired electrical inspector; 3 the AI-persona risk; 4 long-form only). Answer their questions from the files; don't re-run research unless they ask.
  3. Record their answers in `studies/electrical/log.md`, then write `studies/electrical/CONCLUSIONS.md` (deliverable 9: what to make, emotions and villains, titles and thumbnails, gaps, how to stand apart, what the scripting pack should take).
- **Deliverables:** `channels.md`/`.csv`, `new-channels.md`, `subniches.md`, `emotions.md`, `thumbnails/thumbnail-styles.html`, `recent-winners.md`, `top-100.md`/`.csv`, `keyword-sweep.md`, `formats.md`; `studies/electrical/README.md` maps every file. They're built by scripts in `studies/electrical/data/tools/` (`build_docs.py`, `build_channels.py`, `build_thumb_page.py`); re-run them after any data fix.
- **Operator decisions so far:** (2026-10-26) run rounds straight through with a check after each, stop only for real decisions. (2026-10-24) narrow scope: core electrical and fire prevention; not winter blackouts (maybe later, for the stopped generator channel Jack Redfield), not seniors' home safety; no money framing; Frederick's old channel isn't a guide ("full pivot"); the tiny fire inspector/marshal field "could mean we have a gap". (2026-10-23) 5-minute rule, under-5:00 hits in `short-reference.md`; Frederick's channel in the census as "ours"; find new channels.
- **Method notes for anyone re-running:** YouTube search's "upload date" sort no longer sorts and there's no "oldest" search sort (date windows used; see `data/tools/yt.py`). NexLev's batch tool has no monthly views; 30-day views come from `get_daily_analytics`, impossible values blanked. Search-based multiples run high (compare topics, not absolutes). Only some emotion labels are robust (`labels.md`). Helpers can't write `.md` files; the main session saves their reports.

---

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
