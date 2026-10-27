# Session handover

The live note passed from chat to chat. A new chat reads `CLAUDE.md`, then this file, then `RESEARCH-BRIEF.md` and `README.md`, and carries on from its section's "Next actions". Each chat rewrites only its own section.

**Last updated:** 2026-10-27: HVAC section by the HVAC research chat (branch `claude/loving-einstein-htwt5s`) at its handover. Electrical section by the electrical chat (branch `claude/intelligent-ride-v1at70`) at its handover, 2026-10-27. Other sections as the setup chat left them on 2026-10-23.

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

- **Owns:** `studies/hvac/` and `ideation/hvac-ideation/` (plus `ideation/thumbnails-upload/`). Last branch: `claude/loving-einstein-htwt5s` (merged into `main` at the 2026-10-27 handover). Earlier: `claude/adoring-galileo-wqloxp`.
- **Status (2026-10-27, handover):** research done (rounds 1-7), conclusions written, batch 1 greenlit with fact-checked briefs and the thumbnail artist's brief, the HVAC ideation skill built as a draft. **Next is scripting, in `KPMYT/script-system`.** Read `studies/hvac/CONCLUSIONS.md` first, then `studies/hvac/log.md` (the "After round 7" part: every ask, decision and check of 2026-10-26/27).
- **Operator decisions (2026-10-26/27):** copy Ray Dutton's thinking and his top outliers; Roger the HVAC Guy runs **45 years, "same as rogers pipe guy in most aspects"**; **thumbnails show a person: "ray dutton style mixed with rogers"** (Roger's own character, never Ray's face or navy "RAY" shirt); batch 1 = 16 titles for November; "build the hvac ideation skill… we will very much adapt as time goes on"; no image prompts, plain artist instructions with reference links.
- **What's done (all in `studies/hvac/` unless noted):**
  - `ray-dutton-sources.md`: where all 53 of Ray's videos came from (8 of his 10 hits are his own templates or reruns; 2 copy HVAC Exposed; persona predecessor HVAC Mike), checked.
  - `ideation/2026-10-26-batch-1.md`: 68 titles (the 31 real-person 2M+ videos of 3 years and titles from them; the plumbing channels' current winning formats on HVAC, from 712 own videos; Ray's top 5 remade; the source channels' gaps, brand verdicts above all). `ideation/november-titles.html` is the picking page (Artifact https://claude.ai/artifact/QnQAoRFvFsWukjUkSkXkCB).
  - `ideation/greenlit-log.md`: the 16 greenlit titles. `ideation/batch1-briefs-2026-10-26.xlsx`: Title / Reference / Brief, fact-checked (47 fixes, 5 safety gaps closed).
  - `ideation/batch1-thumbnail-brief.html` / `.md`: for the artist, one card per title with reference thumbnails (YouTube links), keep / change / text / don't (Artifact https://claude.ai/artifact/3cBbzYAUQK37jU7bVaVv7t). `ideation/batch1-thumbnail-plans.md`: the same concepts with SEED lines.
  - `CONCLUSIONS.md` (deliverable 9) and `scripting-chat-starter.md` (the message that opens the scripting chat).
  - `ideation/hvac-ideation/` (repo root): the HVAC ideation skill, a thin overlay on ideation-core; `core-proposals.md` lists the 8 changes to ideation-core, plumbing-ideation and the thumbnails skill it needs.
- **Waiting on the operator:**
  1. Roger's thumbnail character image and his HVAC shirt (anything but navy with a name patch); the artist brief says "[to confirm]".
  2. Yes or no to the 8 changes in `ideation/hvac-ideation/core-proposals.md` (registry, scoreboard, kinship, format bank evidence, Werner's probe lane, the thumbnails-skill files in `ideation/thumbnails-upload/`, installing the skill).
  3. Collab credit with Roger the Pipe Guy on Roger the HVAC Guy's uploads.
  4. The five filing calls in `studies/hvac/round7-report.md` §4 (suggested yes to all; none changes batch 1).
- **Next actions:**
  1. The operator opens the scripting chat in `KPMYT/script-system` with `studies/hvac/scripting-chat-starter.md` (it builds the HVAC niche pack and Roger the HVAC Guy's persona from Roger the Pipe Guy's, then scripts the 16).
  2. In this repository: apply the operator's answers to the waiting items above; once batch 1 has views (from mid-November), read them against the channel's normal, update `ideation/hvac-ideation/references/steering.md` and `produced-log.md`, and build batch 2 for December with one or two brand verdicts (the biggest gap, not in batch 1).
- **Method notes:** YouTube's watch page and player are blocked from the cloud; innertube `/next` works (`studies/hvac/data/tools/vid_next_batch.py`; its `owner` field is sometimes wrong, so match channels by id). `ytsearch.py … views` sorts by views. Census dates are rounded ("N months ago"); pull exact dates before claiming who came first. NexLev publish dates are off by weeks. Give each helper its own scratch subfolder, and have a second helper check every list and every set of briefs (the brief fact-check caught 5 safety gaps).

## Electrical and fire prevention research chat

- **Owns:** `studies/electrical/` and `ideation/electrical-ideation/` (+ `ideation/electrical-ideation-build/`, `ideation/dist/electrical-ideation.skill`). Last branch: `claude/intelligent-ride-v1at70` (merged into `main` at the 2026-10-27 handover).
- **Channel: Frederick Barnes** (operator, 2026-10-27: "we will do frederick for this"): retired electrician, **35 years**, **Talking Head**, **no book** (one very short subscribe ask, then a comment ask that says he reads every comment). Jack Redfield stays pinned as a possible second lane.
- **Status (2026-10-27):** research, conclusions and the first ideation are finished; the **17 initial ideas are complete** (titles, thumbnail instructions with reference links, briefs); the **electrical ideation skill is built, checked and packaged**; the **script skills (pack + Frederick's profile) are built in `KPMYT/script-system`** and reviewed (see that repository's `SESSION-HANDOVER.md`).
- **What this chat did:**
  1. **Thumbnail instructions** for the 17: `studies/electrical/ideation/thumb-instructions.xlsx` (A1 per the operator: the reference with its 2 arrows, only the text and character changed, the logo removed). Sent to the operator.
  2. **Briefs** for the 17 (house spec: talking points only, one paragraph, 200-300 words; no money; fire as stakes; nothing claimed as tested): `studies/electrical/ideation/briefs-2026-10-27.xlsx`. Three helpers drafted from the reference transcripts, three more re-checked: 14 of 17 corrected, 40 issues (`ideation/briefs-work/`). The operator accepted the three open points ("good").
  3. **The ideation skill** `ideation/electrical-ideation/` (overlay on `ideation-core`, modelled on plumbing): SKILL.md + 9 references (steering with the base ideation plan, audience, demand map, formats with examples, reference titles, word bank, thumbnail niche pack, produced log with the 17, dead list). A checker verified about 800 figures and fixed 17. Packaged as `ideation/dist/electrical-ideation.skill`; **the operator installed it** (it shows on the account). Frederick named as the channel, tenure 35.
  4. **Registry proposal** for `ideation-core` (registry, scoreboard column, kinship line): `ideation/electrical-ideation-build/registry-proposal.md`. **Not applied**: the operator asked for "the option to register"; asked, no answer yet.
- **Open with the operator (ideation side):**
  1. Register the skill in `ideation-core`? (proposal above)
  2. The ideation skill still lists "after all the houses I've worked in" as allowed (`references/audience.md`, `word-bank.md`); the operator banned it for scripts on 2026-10-27. Change it here too? (asked)
  3. From the skill checker: A29's "I Find in Almost Every Older House" wording; whether videos under 5 minutes count as format proof; topic 26's fire burn-test proof; P-codes awaiting F-numbers.
  4. Two titles in `titles-50.csv` say "30 years" (ids 29, 33): if one is picked, it needs 35 (script-system P13 item 7).
- **Next actions:**
  1. Read `CLAUDE.md`, this section, `studies/electrical/ideation/README.md` and the end of `studies/electrical/log.md`.
  2. The script work continues in `KPMYT/script-system` (its handover lists the operator's six open questions). Ideation work here only on the operator's call: more ideas, the registry, the skill's banned line.
- **Method notes:** as before (`data/tools/`), plus `build_thumb_instructions.py` and `build_briefs.py` rebuild the two sheets from `initial-ideas.csv` and `briefs-work/`.

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
