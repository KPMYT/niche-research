# HVAC study: Roger the HVAC Guy

The research for the new channel Roger the HVAC Guy, following `RESEARCH-BRIEF.md`. Owned by the HVAC research chat.

**Status (2026-10-27):** conclusions written (`CONCLUSIONS.md`); batch 1 greenlit with fact-checked briefs; next, the scripting chat in `KPMYT/script-system` (`scripting-chat-starter.md`). Earlier status (2026-10-23): round 1 (seeds) done and checked; round 2 (spread) done and checked 2026-10-24; rounds 3-6 done and checked 2026-10-26; round 7 report written (`round7-report.md`); the back and forth with the operator next, then `CONCLUSIONS.md`.

## Scope decisions (operator, 2026-10-23)

- Generator videos count only when they are about keeping the house warm in an outage; generator and power-station product reviews are out.
- Drafts, weatherstripping, spray foam, windows and attic insulation count when the title is about heating, cooling or the bill.
- Round 1 also starts finding channels ("go and find more channels too").

## Operator decisions, 2026-10-24 (on the round 1 report)

- New emotions E19 comfort and E20 new-gadget wonder: yes. New formats (symptom-fix, install/DIY project, review, explainer, news-warning): yes. See `labels.md`.
- **NexLev RPM is not used:** "ignore nexlev rpm its wrong". RPM and NexLev's RPM-based figures are not used for any finding or comparison in this study. (NexLev monthly earnings are RPM-based too, so they are kept in the raw data but marked as NexLev estimates and not relied on.)
- Off-grid heat (wood and pellet stoves, diesel heaters, "free heat" tricks) is mapped as its own sub-niche (my reading of the answer to question 4).
- Silver Cymbal borderline videos: the pellet stove video (`9d9TL02idO4`) counts as a seed; spray foam, garage-door seal, crawlspace and snowstorm videos stay out.
- Search sorts: "this month" and "this year" filters replace the broken "upload date" sort; old videos come from each channel's Oldest tab, as YouTube search has no "oldest" sort.

## Operator decisions, 2026-10-26

- **Run the rounds without stopping:** "cant you do urself and check urself after aech round?" Rounds 3-6 run straight through, each checked by a second helper; the operator gets the full report at round 7. Only genuine operator calls stop the run.
- Taken as the default, to be confirmed in the round 7 report (the operator didn't answer the two round 2 questions and asked to go on): contractor channels that teach homeowners count as competitors (tier A, marked "contractor"); outage or off-grid channels whose videos are mostly HVAC count as tier A, marked with their lane.

## Operator decisions, 2026-10-26 and 2026-10-27

- On the round 7 findings: copy Ray Dutton's thinking and his top outliers; keep the best and worst lists in mind; thumbnails and selling later.
- Batch 1 (16 titles) greenlit for November uploads (`ideation/greenlit-log.md`).
- **Roger the HVAC Guy's persona:** "45 years, same as rogers pipe guy in most aspects" (2026-10-27). Tenure 45, the same constant number as Roger the Pipe Guy.

## Files

| Path | What it is |
|---|---|
| `README.md` | This file: what's here, the status, the dates pulled. |
| `log.md` | Every round: what ran, how many helpers, what changed. |
| `labels.md` | Label definitions (emotions, villains, formats, sub-niches, types, the multiple), including proposed new ones marked NEW. |
| `seeds/` | Round 1: `silver-cymbal.md` (22 HVAC seed videos, labelled; borderline and adjacent tables), `known-channels-recheck.md` (the 8 known channels re-checked), `leads-channels.md` (up-next and similar-video leads), `channel-finds-round1.md` (174 channels found), `keywords-round2.md` (round 2 keyword list), `check-round1.md` (the round 1 check), `round1-report.md` (what was reported to the operator). |
| `data/raw/` | Raw pulls (JSON, CSV), one file per pull, named with the date. |
| `data/tools/` | The small scripts used. Copied from `recovered/2026-10-22-roger-sub-brands/tools/` on 2026-10-23, then adapted where noted. |
| `round2/` | Round 2 working files: `keyword-sweep.md`, `formats.md`, `nexlev-channels.md`, `old-house-heat.md`, `channels-master.md` (the master channel list), the checks `check-round2.md` and `check-master.md`, and `round2-report.md` (what was reported to the operator). |
| `channels.md`, `channels.csv` | Deliverable 1: the channel census (tiers A-D, 764 channels): tier, HVAC share, subs, views, joined, pace, baseline, top videos, sub-niches, type, persona, what it sells. |
| `new-channels.md` | Deliverable 2: channels started (or pivoted) in the last 12 months, the 58 "well above", their takeoff videos, and the Ray Dutton copycats. |
| `subniches.md` | Deliverable 3: the sub-niche map from the round 4 hand labels (all time, last 12 months, by tier, by type, faceless personas only). |
| `emotions.md` | Deliverable 4: emotions across the niche and sub-niche by sub-niche, with lift and examples; faceless personas only. |
| `thumbnails/` | Deliverable 5: `thumbnail-styles.html` (the page, also a private Artifact), `labels-top-winners.csv`, `labels-channel-top5.csv`, `img/` (the images), `census-sheets/` (contact sheets used for channel types). |
| `recent-winners.md` | Deliverable 6: top videos of the last 90 days and 12 months by views and by multiple, rising and falling. |
| `top-100.md`, `top-100.csv` | Deliverable 7: the all-time top 100 long-form English HVAC videos. |
| `formats.md` | Deliverable 8 (formats and villains): from the round 4 hand labels. The keyword sweep itself is `round2/keyword-sweep.md` (rule-based formats: `round2/formats.md`). |
| `round3/` | Round 3 working files: `types-A/B/C.md`, `sells.md`, `subniches-rule-based-2026-10-26.md`, `check-round3.md` (with the fixes applied). |
| `round4/` | Round 4: `LABEL-GUIDE.md` (the labelling codes) and `labels-summary.md` (agreement and counts). |
| `round5/` | Round 5: `thumbs-top-winners.md`, `thumbs-channel-top5.md`. |
| `round6/` | Round 6 checks: `check-labels.md`, `check-thumbnails.md`, `check-fixes.md`. |
| `round7-report.md` | Round 7: the report to the operator. |
| `CONCLUSIONS.md` | Deliverable 9 (2026-10-27): what Roger the HVAC Guy makes, emotions and villains, titles and thumbnails, gaps, standing apart from Ray Dutton, what the scripting pack should take, open items. |
| `scripting-chat-starter.md` | The opening message for the HVAC scripting chat in `KPMYT/script-system`. |
| `ray-dutton-sources.md` | Where Ray Dutton's Garage got his topics and titles: source videos for all 53 of his videos, his templates, the persona's predecessors, his method (operator's ask, 2026-10-26; checked). Raw data in `data/raw/ray-sources-2026-10-26/` and `data/raw/ray-dutton-videos-2026-10-26.jsonl`. |
| `ideation/` | Title batches for Roger the HVAC Guy, drafts for the operator's picks (not banked): `2026-10-26-batch-1.md` (64 titles: real-person HVAC videos over 2M in 3 years and titles from them; plumbing formats applied to HVAC; Ray Dutton's best 5 remade; the source channels' top videos Ray never made). `batch1-thumbnail-plans.md` (one faceless thumbnail concept and a SEED line per batch 1 title, 2026-10-27); `greenlit-log.md` (every greenlit title, batch 1 = 16 titles, 2026-10-26); `batch1-briefs-2026-10-26.xlsx`/`.tsv` (Title, Reference, Brief; built by `data/tools/briefs/batch1_briefs.py`); `november-titles.html`: the 55 heating-season titles with their reference videos' thumbnails and views, for picking (private Artifact https://claude.ai/artifact/QnQAoRFvFsWukjUkSkXkCB; built by `data/tools/november-page/build.py`). Raw: `data/raw/plumbing-own-channels-2026-10-26/`, `data/raw/top-real-person-3y-2026-10-26.csv`, `top-3y-candidates-exact-2026-10-26.jsonl`, `top-real-person-3y-thumbsheet-2026-10-26.jpg`. |
