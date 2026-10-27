# Session handover

The live note passed from chat to chat. A new chat reads `CLAUDE.md`, then this file, then `RESEARCH-BRIEF.md` and `README.md`, and carries on from its section's "Next actions". Each chat rewrites only its own section.

**Last updated:** 2026-10-27: HVAC section by the HVAC research chat (branch `claude/loving-einstein-htwt5s`) at its handover. Electrical section by the electrical research chat (branch `claude/zealous-ptolemy-lxtx6t`). Other sections as the setup chat left them on 2026-10-23.

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
- **Since that handover (2026-10-27, branch `claude/hvac-research-czb2hy`, pushed, not yet merged into `main`: the operator calls this repo's handover):**
  - Batch 1 signed off as `ideation/batch1-final-2026-10-27.{html,md,xlsx}` (idea, thumbnail instructions, brief for each of the 16; Artifact https://claude.ai/artifact/XcqJ2ZTkd7NnXDbYEvjwVh). The approved skill changes are applied and packaged (`ideation/hvac-ideation.skill`, `ideation/thumbnails-upload/thumbnails.skill`, script-system's `dist/ideation-core`), waiting to be uploaded.
  - **Corrected briefs:** `ideation/batch1-briefs-2026-10-27-corrected.tsv` / `.xlsx` and `batch1-brief-corrections-2026-10-27.md`: 35 figures in 15 briefs fixed from the HVAC price research in script-system (four researchers, four checkers); the signed-off briefs are kept. **Use the corrected briefs for scripting.** The sign-off pack still shows the old figures (rebuild it on the operator's yes).
  - The scripting side is built in script-system: the `hvac-scripts` pack, Roger the HVAC Guy's profile (ready), the HVAC price guide, and two rounds of test scripts (`tests/iterations/iter-06/`).
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

- **Owns:** `studies/electrical/`. Last branch: `claude/epic-maxwell-ty7jnr` (merged into `main` 2026-10-27 at handover).
- **Status (2026-10-27):** research finished, conclusions written, first ideation done. **17 initial video ideas are confirmed** with titles, thumbnail words, reference videos and thumbnail advice: `studies/electrical/ideation/initial-ideas.csv` and the page https://claude.ai/artifact/QnG8dP83G7LZ84rpat3Qek (private). The channel is still pinned (see decisions).
- **What this chat did (detail in `studies/electrical/log.md`, from "Walkthrough with the operator"):**
  1. Walked the operator through `REPORT-2026-10-26.md`; recorded every answer. Corrected one report figure: inspection walkthroughs are 73 videos at typically 20K, not 39K.
  2. Thumbnail text study of the 82 recent winners (`thumbnails/thumbnail-text.html`; page https://claude.ai/artifact/DU5qu4MruAiEVR5B2eY4Rg).
  3. Wrote `CONCLUSIONS.md` (deliverable 9), channel-neutral.
  4. Ideation in `studies/electrical/ideation/` (its `README.md` maps every file): round 1 (34 ideas), topic heat for 47 topics (`topic-heat.csv`, helper-checked), recent winning formats, the proof check under the operator's rule (`topic-proof.csv`, `proven-formats.csv`), Silver Cymbal's 1M+ electrical videos re-titled, 50 titles (v1 and v2), round 2, then the 17 initial ideas.
- **Next chat, start here:**
  1. Read `CLAUDE.md`, this section, `studies/electrical/CONCLUSIONS.md`, `studies/electrical/ideation/README.md` and the end of `studies/electrical/log.md`.
  2. Ask the operator which comes next: thumbnail prompts for the 17 (the `thumbnails` skill; each idea's look, words and advice are in `initial-ideas.csv`), the channel decision, or more ideas. Don't decide for them.
  3. On the operator's yes: build the electrical ideation skill, base ideation plan and thumbnail plan here (`RESEARCH-BRIEF.md` step 4), modelled on `script-system/ideation/plumbing-ideation`; the scripting pack is a separate chat in `KPMYT/script-system` (`CONCLUSIONS.md` section 8 lists what it should take).
- **Operator decisions (2026-10-26, quoted in `log.md`):**
  - Lead with everyday electrical problems; fire is the stakes, never the topic ("we dont want any more fire type vids for now").
  - Background mostly unspoken; a retired electrician when needed.
  - Formats: how-to and "why does X keep doing Y" yes; take the test/demonstration topics but explain, never demonstrate; mistakes and "dangerous" work but are crowded; no real inspections or real stories; no "NEVER leave plugged in" lists for now; fire investigator not the lane. Also borrow viral formats from other personas; mainly "take and improve on the top vids in our chosen formats from our niche".
  - Thumbnails: a character with a blue blueprint explainer board for education; otherwise a person reacting or pointing at the problem; may add the character to winning close-ups. Track thumbnail text on recent winners.
  - Long-form only. No money framing (2026-10-24).
  - **Proof rule:** a topic (and format) counts only with a video of 300K+ views on a faceless channel or 1M+ on a real one.
  - Script-level emotion study (how scripts voice each emotion) deferred to the script SOP work.
  - **Channel pinned:** Frederick Barnes or Jack Redfield (stopped generator channel, 4.2K subs), maybe both as two test lanes; "neither one has viewers". Generator ideas suit Jack.
  - Picks: round 1 ideas 1, 2, 7, 12, 14, 29, 30, 31, 33; Silver Cymbal copies 3, 6, 7, 10, 11; 50-title v2 numbers 2, 12, 15. All 17 titles confirmed; five reworded by the operator.
- **Method notes:** `data/tools/topic_heat.py` (search + channel pulls; some page loads fail under load, so run with few threads), `clean_heat.py`, `topic_proof.py` and the page builders (`build_ideas_page.py`, `build_titles_page.py`, `build_round2_page.py`, `build_initial_page.py`) rebuild everything from the CSVs. Keyword matching is noisy: helpers judged every matched title (about half were off topic). Search counts are a floor; 14 topics are marked "partial count" (the operator declined a re-run). Channel types outside the census come from NexLev `check_faceless_channel` (`ideation/channel-types.csv`).

---

## Notes for both chats

- **Your section here and your folder are yours.** Shared files get one row or line per change; when merging into `main`, keep both sides.
- **The operator can't see your context use.** Hand over when they say so (`CLAUDE.md` rule 8).
- **Ideation skills today live in `script-system/ideation/`** (`ideation-core`, `plumbing-ideation`, `woodworking-ideation`). The new ones will be built here, modelled on those. Ask the operator before moving or changing any existing one.
