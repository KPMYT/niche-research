# Log: electrical and fire prevention study

## Round 1 (2026-10-23): starting videos and new-channel hunt

**Operator's answers to the plan (2026-10-23):**
1. Keep the 5-minute rule for every count and the top 100; keep Silver Cymbal's (and others') under-5-minute hits in a separate "short reference" list: yes.
2. Just Stop Fire gets a census row, marked "ours": yes.
3. "we alos need you to find new channels. that fit the niche or niche adjacent": two discovery helpers added to round 1.

**Method checks before the helpers ran:**
- Silver Cymbal is `@SilverCymbal` (`UC67dKTEwpAhKv2oYDATwR8g`), 1.09M subscribers, 539 videos (Videos tab, 2026-10-23).
- Channel Videos tab: Latest, Popular and Oldest sorts all work (checked on Silver Cymbal).
- YouTube search: relevance works; most viewed works roughly; **"upload date" no longer sorts by date**, so "newest" uses the date windows (this week, month, year), which filter correctly; **search has no "oldest" sort**, so "oldest" comes from channels' Oldest tabs. This differs from the brief's four sorts; the operator is told.
- Video pages (`/next`) give the exact view count, the exact upload date and the up-next list. The player page is blocked logged out ("confirm you're not a bot"), so lengths come from list pages.
- NexLev's upload dates are rounded from "5 years ago" (every date lands on 10-23); exact dates come from the video pages.

**Helpers launched (6, in parallel, 2026-10-23):** shared brief in each prompt (rules, loader, columns, sub-niche codes).

| # | Helper | Output |
|---|---|---|
| 1 | Silver Cymbal: full Videos tab, every electrical/fire video, exact dates and views, labels, thumbnails, census row | `seeds.md`, `data/silver-cymbal/` |
| 3 | The six known channels re-checked against the 2026-10-22 figures, census rows, videos, top-5 thumbnails | `data/known-channels/` |
| 4 | Just Stop Fire (ours): census row, every video with exact dates, labels, thumbnails, the 434K hit's neighbours and comments | `data/just-stop-fire/` |
| 5 | First spread: up-next (two hops) and NexLev similar videos/channels from 15 Silver Cymbal seeds; channel candidates | `data/seed-spread/` |
| 6 | New-channel hunt, NexLev side (niche finder, 25+ phrasings, faceless discoveries, small-channel viral videos), core and adjacent | `data/new-channels-nexlev/` |
| 7 | New-channel hunt, YouTube search side (40+ keywords, this year's most viewed, this month), core and adjacent | `data/new-channels-search/` |

(Helper 2, "Silver Cymbal labels", was folded into helper 1 to avoid a wait. The checker runs once all six land.) Web search budget given: 25 of about 200.

**Landed (2026-10-23):**
- Helper 4, Frederick Barnes channel (ours): `data/just-stop-fire/` (census row, 21 videos with exact dates, labels, thumbnails, report). The channel is named "Frederick Barnes" (@FrederickBarnesYT), not "Just Stop Fire". Report saved by the main session (helpers can't write report files).
- Helper 3, the six known channels: `data/known-channels/` (6 census rows, 175 videos, 30 thumbnails, report saved by the main session). All 2026-10-22 view counts match (grown); Walt Brennan is an AI avatar, not faceless; Rational Buyer's 24.8x was NexLev's score (828x on our basis) and it isn't an electrical channel.
- Helper 1, Silver Cymbal: `seeds.md`, `data/silver-cymbal/` (149 in-scope videos: 96 long-form, 53 under 5:00; 31 borderline; 149 thumbnails). "About 44" matches only the core electrical/fire group (48).

**Fixes:**
- `data/tools/yt.py`: channel lists stopped at 30 videos (the code took a panel's continuation token, not the grid's). Fixed 2026-10-23; latest, popular and oldest checked to 120 videos on Silver Cymbal. Helpers 1 and 3 had paged with their own scratch scripts, so their pulls are complete; the three running helpers were told to re-pull any multi-page list.
- `labels.md`: new labels review, explainer (formats) and recalls (sub-niche).
- Helper 5, first spread: `data/seed-spread/` (385 candidate channels: 128 in scope, 157 adjacent, 100 out; report saved by the main session). How To Home and the new faceless Weirdward Bound are paired most with Silver Cymbal's electrical hits; Home Hazard is the closest fire-safety match; a wave of tiny 2026 retired-tradesman personas. NexLev's faceless check marks AI-image personas "not faceless", so types need eyes on thumbnails.
- Helper 6, new-channel hunt (NexLev): `data/new-channels-nexlev/` (134 channels: 28 core, 106 adjacent; 101 new in 12 months; 52 faceless personas; report saved by the main session with a note that the flagged "Frederick Barnes" channel is ours). No fire marshal or fire inspector persona found; two retired-firefighter personas, one lineman persona.
- Helper 7, new-channel hunt (YouTube search): `data/new-channels-search/` (50 keywords, 563 channels of which 122 checked, 1,740 long-form videos; report saved by the main session). 107 of 121 checked channels are new; 79 faceless personas; 24 reused accounts. Core niche: 2 channels taking off (Home Hazard, SHOCKPROOF LIVING); adjacent: 28 (blackouts, heat without power, backup power, tradition keys).

**Conflicts for the checker:** fire inspector/marshal personas (helper 6: none; helper 7: Earl Whitaker, Chief Reardon, Chief Miller); Ray Sutter (31.5K subs, 1 month) against Ray Dutton's Garage (31.5K) — same or different?; Home Hazard's start (joined 2022 per NexLev; first visible upload Jun 9 2026); Weirdward Bound core or adjacent.

**Checker A (2026-10-23):** re-pulled 80 sampled rows (Silver Cymbal 33, known channels 40, ours 7) and every row's length, 5:00 flag and multiple; re-checked all 8 census rows against NexLev and thumbnails. No data errors. Fixed by the main session: added the missed `_G7ZPjmR5ck` to `seeds.csv` (noted in `seeds.md`); Rational Buyer has 2 electrical videos of 31, not 1 (`FomUMo2Z7Rg` labelled; `known-channels/report.md` corrected). Verdicts: Silver Cymbal and known channels usable with those fixes; ours usable. Details: `data/checks/checker-A.csv`.

**Checker B (2026-10-23):** re-checked 85 sampled channels across the three discovery files (subs, first upload, English, type by thumbnail, persona and claimed background), re-pulled all 72 named "taking off" videos (all within ±1%, all on the named channel, all 5:00+ except one already-noted 4:52 video), and settled the four conflicts. Error rates: seed-spread 4.8% wrong (persona guesses), NexLev census 1.8%, search channels 1.0%. Fixed by the main session: Builds With Eli Yoder and four seed-spread channels relabelled; three reused accounts flagged; Zenthral Code's start date; the "plugged in" count (39 videos on 23 channels, not 65 on 36). Conflicts: fire inspector/marshal personas exist but are tiny (none over 1K subs; not in NexLev); Ray Sutter and Ray Dutton are different channels; Home Hazard's account is from 2022, first visible upload Jun 9 2026. Corrections appended to each report. Details: `data/checks/checker-B.csv`.

**Operator's answers to the round 1 summary (2026-10-24):**
- Frederick's own channel "wont be a strong representation of what will and wont work here we pretty much need a full pivot". So his channel stays a census row (ours), not a guide to what works.
- Fire inspector / marshal personas being tiny: "thats fine … but it could mean we have a gap". Noted as a possible gap, to be tested in later rounds.
- "we dont really need to use money in electrical."
- Scope: "lets keep the scrope narrow". Winter blackouts maybe as a test only, and possibly not: "that could be a different chanenl i have called jack redfield who i stopped that does generators". Seniors' home safety: "definitely not … completley unrelated".
- "go with round 2".

**Scope from round 2 on (main session's reading of the above):** core electrical and fire prevention as `RESEARCH-BRIEF.md` lists them, including generator *safety* (backfeed, CO, cords), which the brief names. Out: winter blackout survival, heat without power, power-station and generator buying reviews (Jack Redfield's lane, a stopped channel), seniors' home security, "free energy". Round 1 files keep their adjacent rows (history isn't deleted); later counts use the narrow scope.

## Round 2 (2026-10-24): keyword sweep and the master channel list

**Helpers launched (7, in parallel):** shared rules (narrow scope) and one sweep task for the six sweep helpers (20+ keywords each; relevance 2 pages, views 3, views this year 2, this month 1, over-20-minutes for the top 5; exact dates for each group's top 40; sub-niche and format labels; formats and sub-niche counts).

| Helper | Topic group | Output |
|---|---|---|
| sweep: wiring | wiring mistakes, outlets and switches, GFCI/AFCI, connectors | `data/sweep/wiring/` |
| sweep: panels | breakers and panels, FPE/Zinsco, aluminium and knob-and-tube, inspectors | `data/sweep/panels/` |
| sweep: cords | cords, power strips, surge, "never leave plugged in", LED, ceiling fans, holiday lights | `data/sweep/cords/` |
| sweep: devices | lithium batteries, space heaters, generator safety, testers, the electric bill, EV/240V | `data/sweep/devices/` |
| sweep: fire | smoke and CO alarms, dryer vents, kitchen and grease, extinguishers and escape, fire habits | `data/sweep/fire/` |
| sweep: explainers | explainers and tests; plus the presenter-background search (electrician, lineman, firefighter, investigator, inspector/marshal, home inspector) | `data/sweep/explainers/` (+ `presenters.csv`) |
| channel list | round 1's channel lists merged, checker fixes applied, re-scoped (core / partial / out) | `data/channel-list/` |

Web search budget given: 30.

**Landed (2026-10-24):** all 7 helpers. Reports saved by the main session in each folder's `report.md`.
- `sweep/devices/` 1,022 long-form (28 keywords); `sweep/wiring/` 1,018 (31); `sweep/panels/` 988 (30); `sweep/fire/` 745 (41); `sweep/cords/` 681 (29); `sweep/explainers/` 1,321 (53, incl. 28 presenter-trade keywords; `presenters.csv` 122 counted channels). Groups overlap (a video can surface in several); the round 3 merge dedupes.
- `channel-list/`: 957 deduped channels: 142 core, 158 partial, 657 out.
- New format labels proposed by helpers: problem-fix, insider-never / never-list, reaction, inspection-walk(through), danger-warning, job-vlog, best-list, number-one, the-x-way, banned-2026. To be defined in `labels.md` after the checkers.

**Fix:** `data/tools/yt.py` now also reads the Popular/Oldest sort from the new drop-down menu (73 channels had no sort chip; the explainers helper found it and used its own wrapper). Checked on Walt Brennan, Weirdward Bound, Home Hazard, Roy Dalton Electric and Silver Cymbal.

**Merge (main session, 2026-10-24):** `data/tools/merge_sweeps.py` → `data/merged/videos-all.csv`: the six sweeps' videos.csv deduped by video ID (keeps the exact-views row; records every group that surfaced it). 5,070 unique long-form rows; 4,896 after dropping rows the helpers marked out. Not yet filtered for language (e.g. the German IFS dryer video, 15.8M) or re-scoped; that's round 3, after the checkers.

**Checker C (2026-10-24):** re-pulled 135 rows (wiring, panels, cords: 30 random plus each top-15): all 135 match on views, title, channel and length. Recomputed counts: match except minor slips (wiring 1M+ 118 not 117; panels home-inspection median 13,490 not 12,651; inspection-walk 35,183 not 34,659; cords dont-want-you 1,450.5, left blank). Keyword sorts: same #1 on all 18 re-runs, top-20 overlap 17-20. Channel list: core 13% and partial 25% disagreement (wrong or minor), out 0%. Scope leakage: wiring 1-2%, panels about 8%, cords 2-3%.
Fixed by the main session:
- `data/merged/corrections.csv` (84 rows): videos marked out in the merge: the 68 general home-inspection videos (helper's own note), HAXMAN whole-home generator alternative (mlCcvozgYfE, 3.85M), two unpublished premieres, fake bill and bulb hacks, Powerwall, Generac installs, HVAC, EMP Shield, car wiring, a yacht, an HOA story. The merge script applies it; helper files unchanged.
- Recomputed without the general inspections: electrical inspection walkthroughs 41 videos, median 46,299 (was 82, 35,183); home-inspection sub-niche 50 videos, median 37,515.
- Channel list: Wired Wonders and HSE STUDY GUIDE → out; The Excellent Laborer → partial.

**Checker D (2026-10-24):** re-pulled 133 videos (devices, fire, explainers): views, channel, title and length all match (views 0 to +0.4%). Labels and scope are where the errors are: devices 18% wrong of 45 rows, fire 9%, explainers 11%; presenters 10 of 52 channels with the wrong background. Recomputed counts and medians match the CSVs (once helpers' own exclusions applied). Keyword re-runs: top-20 overlap 14-20.
Fixed by the main session:
- `data/merged/corrections.csv` now 224 rows: checker D's named rows (phone battery-life tips, generator sizing, solar and home batteries, a laptop battery, an EV-charger buying list, firefighter entertainment incl. Doctor Mike collabs, a video game, a comedy vlog, Bosnian/Malay/Hindi/German videos, the Veritasium Smith chart) and a title scan (solar; backup power / generator buying; phone or laptop battery life without a fire angle; firefighter entertainment). The top 45 title-scan drops were read by hand; 2 false drops restored ("Electricity Explained: Volts, Amps, Watts…" and "BEST Generator Cord is the One you Can Make Yourself").
- `data/checks/presenters-summary-corrected.csv`: the presenter-background table with checker D's corrections (lineman 13 channels, 3 over 10K; firefighter 20, 2 over 10K; fire inspector/marshal 4, none over 10K; electrician 34, 18 over 10K; home inspector 35, 16 over 10K) and the big real channels the sweep missed.
- Merged in-scope long-form after both checkers: see the count in the next round's files.

**Operator, 2026-10-26:** "why do you need me inbetween each round, cant you do urself and check urself after aech round?" Standing instruction: run rounds 3-6 straight through, a checker after each round, fixes logged; stop only for a real decision; report at the end. The fire investigator / inspector deep look is added to round 3 (main session's call; it bears on the open presenter decision).

## Round 3 (2026-10-26): census, channel medians and multiples, top 100, recent winners, investigator deep look

**Launched (2026-10-26):**
- Channel medians for the multiple: `data/tools/channel_medians.py` run by the main session in the background on 1,277 channels (every census channel plus every channel with an in-scope video of 10K+ in the merge; covers 3,125 of the 4,758 merged videos). Basis A = median of long-form uploads in the last 12 months (10 or more); else B = last 30 long-form. List-page views. Output `data/medians/`.
- Census, 3 helpers (298 core and partial channels in 3 chunks): NexLev batch metrics, first upload, pace, top 3, type by thumbnails, persona and background, sub-niches, what it sells, scope re-judged. Output `data/census/`.
- Top 100 and recent winners, 1 helper: the top 250 of the merge re-pulled, English and narrow scope re-judged, plus 15 broad keywords for misses; top 50 of the last 90 days and of the last 12 months. Output `data/top100/`.
- Fire investigator / inspector deep look, 1 helper: every investigator-angle video and channel, top 10 described, compared with the "retired firefighter would NEVER" lists and electrician-angle videos. Output `data/investigator/`.

**Channel medians done (main session, 2026-10-26):** 1,262 of 1,277 channels have a median (`data/medians/channel-medians.csv`; basis A for 686+, B for the rest; 26 failed loads retried, 1 still failing; 14 had no long-form). `data/tools/subniche_map.py` joined them: 3,101 of the 4,758 merged videos have a multiple (`data/merged/videos-with-multiples.csv`), and the first sub-niche and format maps are in `data/merged/subniche-map.csv` and `format-map.csv`.
**Caveat (reading):** search results favour each channel's winners, so multiples run high across the board (most sub-niches median 3-8x). Use them to compare topics with each other, not as absolute figures. Small groups with tiny-channel medians (e.g. best-list, 35.9x) are unreliable. Two helpers' labels for the same format (inspection-walk / inspection-walkthrough; explainer / explainer fallback) are merged in round 4.
