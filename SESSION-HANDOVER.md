# Session handover

The live note passed from chat to chat. A new chat reads `CLAUDE.md`, then this file, then `RESEARCH-BRIEF.md` and `README.md`, and carries on from its section's "Next actions". Each chat rewrites only its own section.

**Last updated:** 2026-10-26: HVAC section by the HVAC research chat (branch `claude/adoring-galileo-wqloxp`) at its handover; electrical section by the electrical research chat (branch `claude/zealous-ptolemy-lxtx6t`). Other sections as the setup chat left them on 2026-10-23.

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

- **Owns:** `studies/hvac/`. Branch `claude/adoring-galileo-wqloxp` (merged into `main` at the 2026-10-26 handover).
- **Status (2026-10-26, handover):** rounds 1-6 done and each checked by second helpers; round 7 reported to the operator. Start with `studies/hvac/round7-report.md` (findings, caveats, the default calls), then `studies/hvac/README.md` (operator decisions and the file map) and `studies/hvac/log.md` (every round, every check and fix).
- **The deliverables (all in `studies/hvac/`):** 1 `channels.md`/`.csv` (764 channels in tiers A-D; tier A 254, of which 61 faceless personas); 2 `new-channels.md` (221 new, 58 well above); 3 `subniches.md`; 4 `emotions.md`; 5 `thumbnails/thumbnail-styles.html` (private Artifact https://claude.ai/artifact/NmxFR6D24eSFyQ9hSpB8Vz); 6 `recent-winners.md`; 7 `top-100.md`/`.csv`; 8 `round2/keyword-sweep.md` plus `formats.md`. 9 `CONCLUSIONS.md` is not written yet.
- **Operator decisions so far** (also in `studies/hvac/README.md`): NexLev RPM and earnings are not used ("ignore nexlev rpm its wrong"); run the rounds without stopping and check after each; off-grid heat is its own sub-niche; E19 comfort and E20 new-gadget wonder added; generator videos only when about outage heat; insulation only when about heat, cooling or the bill; "newest" = the this-month / this-year filters.
- **Waiting on the operator** (round 7 report section 4): confirm the five default calls (contractors = competitors; mostly-HVAC outage channels in tier A; stove-craft channels moved to the off-grid lane and craft stoves out of the top 100; four channel types plus a company column; add the four proposed sub-niche codes to `labels.md`?).
- **Next actions:**
  1. The back and forth with the operator on the round 7 report; then write `studies/hvac/CONCLUSIONS.md` (deliverable 9: what Roger makes, emotions and villains, titles and thumbnails, gaps, standing apart from Ray Dutton's Garage, what the scripting pack takes).
  2. Then, on the operator's call, the ideation skill, base ideation plan and thumbnail plan in this repository.
- **What a new chat needs to know (method):**
  - The YouTube watch page and player endpoint are blocked from the cloud; the innertube `/next` endpoint works (`data/tools/vid.py`, `vid_next_batch.py`). Logged-out search translates foreign titles, so English is checked on the original title from oEmbed. The search "upload date" sort is broken.
  - Channel Videos tabs: `data/tools/yt_allsorts.py` (patched for channels whose sorts sit in a dropdown). The census is rebuilt by `data/tools/census_build.py`; the label tables by `data/tools/round4_build.py`; the thumbnail page by `data/tools/thumb_page.py`.
  - The multiple flatters old videos (lifetime views against a recent baseline): read the last-12-months tables; multiples use only channels with a 100+ view baseline.
  - Helpers share the scratchpad and once overwrote each other's scripts: give each helper its own scratch subfolder.

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
