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

**Census gap and fill (2026-10-26):** NexLev's batch tool returns no monthly views, earnings, outlier score or join date (census chunk 2's helper); subs, views and join date come from YouTube About pages. Main session tested NexLev `get_daily_analytics` (dayCount 30): it gives last-7/30/90/365-day views and subscriber gains (How To Home: 3,589,938 views in 30 days, 2026-10-26). A helper is filling this for all 298 census channels into `data/census/nexlev-daily.csv`; monthly earnings will be estimated as 30-day views × NexLev RPM and labelled an estimate.

**Round 3 landed (2026-10-26):** top 100 and recent winners (`data/top100/`), investigator look (`data/investigator/`), census chunks 1-3 (`data/census/`, 298 channels; reports saved by the main session). Unnarrated "hack" channels (BEEE Works, Handcraft, Inventor J, DIYTechTrends, DIY Hacks and others) hold #1, #2 and #7 of the top 100: kept, flagged; the final top 100 will be shown with and without them (main session's call: a narrated persona can't copy that format).

**Launched:** checker E (round 3: every top-100 row, recent winners, census sample, investigator sample, medians and multiples recomputed) and, in parallel, round 4.

## Round 4 (2026-10-26): emotions, villains, formats

Labelling set (`data/labels/to-label-*.csv`, 1,007 videos): the top 100, both recent lists, and per sub-niche the top 30 by views plus 10 random from the rest (to show the typical video, not just winners). Three labellers by sub-niche group (A wiring and panels 338; B cords and devices 407; C explainers and fire 262), working from the full plumbing emotion definitions; title plus thumbnail for the top 100 and recent winners, title only for the rest. Each also writes per-sub-niche emotion and villain summaries. A checker will re-label a sample blind.

**Round 4 labels landed (2026-10-26):** groups A (338), B (407), C (262) in `data/labels/` (reports saved by the main session). Group C proposed N1 nuisance irritation, N2 how-it-works curiosity, N3 spectacle and thrill; the main session passed them to A and B for consistency (A re-coded 98 rows; B used them and added N4 comeuppance, 2 rows). All four and the round 2 formats are now defined in `labels.md`. Checker F launched: 90 rows (30 per group) re-labelled blind, then compared.

## Round 5 (2026-10-26): thumbnails

`data/census/census-all.csv` (the three chunks merged: 298 rows; core 136, partial 148, out 14). Thumbnail set: the top 100 and both recent lists (about 180) and the top 5 long-form of 50 main channels (`data/labels/thumb-channels.csv`: the 30 biggest core channels by subs, the 10 biggest new core channels, ours, and the main homeowner and persona channels: How To Home, Everyday Home Repairs, Silver Cymbal, LRN2DIY, Technology Connections, Practical Engineering, The Engineering Mindset, The DIY Guy, Weirdward Bound, Home Hazard; Walt Brennan and Roy Dalton were already in). Two labellers: face, expression, subject, exact text, word count, colours, arrows, circles, before/after, red/green marks, fire, numbers, background, look, style group. Output `thumbnails/labels-*.csv`; the page comes next.

**Checker E (round 3, 2026-10-26):** all 100 top-100 rows re-pulled (views, dates, lengths, original titles, ranking: all match); recent lists 40 rows, census 45 channels (figures 0 wrong, scope readings about 13% disagreement), investigator 20, medians 20 re-pulled plus all empties, multiples formula on all 3,101 rows (0 mismatches). Fixed by the main session:
- Top 100 → `data/top100/top100-final.csv` (`data/tools/top100_final.py`): one rule for theory and experiments (in = home electrical work, household device safety, or shock/fire danger to people; out = pure theory): ElectroBOOM "Why Use AC Instead of DC at Home??" out; TKOR battery explosion demos in (consistent with the kept lithium experiment); Techquickie volts/amps/watts stays out. Added checker E's misses: "How To Install Pot Lights in Kitchen Ceiling" (WOK_EH5YHjM, 4,269,106), "How To Convert T8 Fluorescent Lights to LED" (mmR5iEEP9q8, 3,123,310), ElectroBOOM "Tripping Every Breaker in Italy" (A3Dblph1fig, 4,000,997). Cut-off now 2,680,400. `top100-narrated.csv` leaves out the unnarrated hack / hands-only channels (cut-off 2,508,755). A first build missed the helper's search finds; fixed before use.
- Medians: `channel_medians.py` now counts a blank page as an error; 15 empty medians re-pulled (1,275 of 1,277 now have one; GEN3 genuinely has no long-form, Kuenzer Homesteading still fails). `subniche_map.py` leaves out channels whose median is under 200 views (brand/agency channels; e.g. Puget Sound Energy, median 21) from multiples: 2,674 videos now have a multiple. Known limit: basis A loads at most 90 videos, so for 108 very active channels "12 months" is really the newest ~90.
- Census (`census-all.csv`): ELECTRICAL VALLEY → out; Future Briefing → faceless persona.
**Checker F (round 4, 2026-10-26):** blind re-label of 90 rows: first emotion 78% same, any emotion shared 98%, villain 92%, format 84% (A 83/97/93/87, B 80/100/90/87, C 70/97/93/80). Summary arithmetic: 0 errors on all rows. Systematic differences and a robustness list written into `labels.md` (insider villain decided by the title; E6 vs N1; E13/N2 mirror the format; which emotions can be reported as counts).

**Deliverables drafted (main session, 2026-10-26):** `data/tools/build_docs.py` builds `top-100.md` and `top-100.csv`, `recent-winners.md` (incl. rising and falling by sub-niche and format), `subniches.md`, `emotions.md`, `keyword-sweep.md`, `formats.md` from the checked CSVs (re-run after any fix). Still to come: `channels.md` and `new-channels.md` (after the monthly-views fill), the thumbnail page (round 5), the round 6 cross-check, then the report.

**Census fill landed (2026-10-26):** `data/census/nexlev-daily.csv`: 203 channels with current NexLev 30-day figures, 37 stale (NexLev stopped tracking), 58 not found; 43 impossible values flagged (negative 30-day views for This Old House and Everything Home Guide, negative 365-day for Starving Electrician and Kidde, 30-day above 90-day on newly tracked channels…). Not yet checked by a second helper: round 6.
**Channels built:** `data/tools/build_channels.py` → `channels.md` and `channels.csv` (298 channels; monthly views from NexLev 30-day where current and possible: 206; estimated earnings = 30-day views × NexLev RPM: 164) and `new-channels.md` (128 new in 12 months among core and partial; taking off = a video over 100K, or 100K+ views in 30 days, or a median at least 2x subs and 1K+).

**Round 5 landed (2026-10-26):** `thumbnails/labels-top-recent.csv` (177) and `labels-channel-top5.csv` (247; reports saved by the main session). The two labellers named style groups differently; `data/tools/build_thumb_page.py` maps both to 11 shared groups and builds `thumbnails/thumbnail-styles.html` (399 unique thumbnails, shrunk and embedded, 5.8 MB). Published as a private Artifact: https://claude.ai/artifact/4ZPp2yNMNRvQccsNo3yyet

## Round 6 (2026-10-26): final cross-check

Checker G: every deliverable file against its source CSVs (numbers, ranks, labels), internal consistency between files, and a re-check of `findings/2026-10-22-hvac-and-electrical.md` section 2 against this study's data. Checker H: a blind sample of thumbnail labels, channel types in `channels.md`, and a sample of NexLev 30-day figures.

**Checker H (round 6, 2026-10-26):** 414 checks, 0 wrong, 31 minor. Thumbnails (40 blind): face 100%, text words 95%, arrows 95%, circles, red/green, fire 97.5%, look 80% (all 8 borderline: mixed vs photo, AI vs cartoon/3D); the AI-image yes/no split 92.5% (kappa about 0.82); AI faces 16 of 16 agreed. Caveat: real presenters placed in AI-made scenes are probably undercounted as AI (e.g. eagOP0bRePM). Uneven calls: lightning as sparks, red stamp boxes as red marks. Channel types: 24 of 25; TheRenderQ corrected to faceless (hands only), scope doubtful; Devin Hollis persona typo fixed (`census-all.csv`). NexLev 30-day figures: 15 of 15 copied correctly (same cached snapshot); 5 stale/not-found flags confirmed.

**Checker G (round 6, 2026-10-26):** 243 checks (190 ok, 46 minor, 7 wrong) across every deliverable, plus the 2026-10-22 findings re-check (`data/checks/findings-recheck.csv`). All 100 top-100 rows, both recent lists, 5 sub-niches and 3 emotion blocks recomputed from scratch, all 27 format rows, and the earnings arithmetic on all 298 channels matched. Fixed by the main session:
- `build_docs.py`: "Dec 28, 2025"-style dates were counted as older in the rising/falling tables (99 videos); now read.
- `build_channels.py`: top-3 text in "(id) 123,456 views" form was read as 0 views, so DeviceDeep and Eric Explains were missed and 7 channels lost their "video over 100K" reason (taking off now 28, was 26); monthly views also blanked where 30 days exceed 90 or 365 days (14 more; 107 of 298 now blank); the "43 flagged" sentence now states the real count; a note that hack/general channels in the top 100 sit outside the census.
- Scope split: the 47 videos ruled out in the top-250 check (theory, car wiring, wall anchors, non-English originals, networking…) were still in the maps; now in `data/merged/corrections.csv` (269 rows; the TKOR battery demos stay in under checker E's rule). Merged in-scope videos: 4,713; with a multiple: 2,629.
- The 4 top-100 videos added after checker E had no labels: labelled by the main session (`data/labels/labelled-extra.csv`, `thumbnails/labels-extra.csv`); the thumbnail page now has 403 cards.
- README: listed `search-candidates-checked.csv`, `blind-sample.csv`, `wiring/tools/`, `.gitignore`; fixed the sentence about helper folders.
Not changed (reading or design): 67 channels in the top 100 or recent lists aren't in the census (general and hack channels, by design); 14 channels' impossible NexLev figures now blanked.

## Handover (2026-10-26)

The operator: "i have read none of this yet. chat context is too large, so we do a handover and you explain and give me everything there". Wrote `REPORT-2026-10-26.md` (the full report in plain words, with the 4 questions; two figures corrected against `format-map.csv` before saving: mistakes titles have 28 videos over 1M, and the tests example is a counted video). Rewrote the electrical section of `SESSION-HANDOVER.md` so the next chat walks the operator through the report, then merged the branch into `main`.

## Walkthrough with the operator (2026-10-26, chat `claude/epic-maxwell-ty7jnr`)

**Correction to the report (section 2):** the "real inspection walkthroughs" row (39 videos, 39K typical) counted only one helper's label. With both labels (`other:inspection-walk` 39 + `other:inspection-walkthrough` 34, from `data/merged/videos-with-multiples.csv`): 73 videos, typical 20,317, 0 over 1M, 19 over 100K. The "NEVER" lists checked the same way: 143 videos, typical 225, 1 over 1M, 5 over 100K (matches the report). The report file is left as written; this entry supersedes the figure. Question 2's suggestion (retired electrical inspector) leaned on the 39K figure.

**Operator on title shapes (2026-10-26):**
- Tests and demonstrations: "we cannot really do tests and demonstrations. we can take their topics and apply them into a different format or reword slightly. but we cannot do exact demonstrations. WE STILL TAKE THE BEST TOPICS"
- How-to: "how to is good"
- "Why does X keep doing Y": "why does x keep doing y is good"
- Real inspections and real stories: "real inspections real stories wont work"
- Mistakes lists and "this is dangerous": "work but obviuosly high competition"
- "NEVER leave plugged in" lists: "we dont really want to proceed for now"

**Operator on emotions (2026-10-26):** "these are all important the emotions, we must track them but also track how the script makes them sound". Gap: this study labelled emotions from titles (and thumbnails for the top 100 and recent winners) only; no transcripts were read. To do (operator's call on when): a script-level look, i.e. transcripts of top videos per emotion and how the script voices each one (the opening lines, where the fear or pride comes in, the words used), for `CONCLUSIONS.md` and the scripting pack.

**Operator on script emotions and fire (2026-10-26):**
- The transcript look at how scripts voice each emotion is deferred: "we can do that when developing script SOPs on script emotions. for now its good what we do".
- "we dont want any more fire type vids for now. the fire investigtor is interesting but not rly education. not our current lane". Fire investigator ruled out as a lane and a background. Reading (to confirm at question 1): no fire-prevention topic videos (space heaters, cords, "what starts fires", kitchen fires); fire and shock may still be the stakes inside electrical topics.

**Operator on thumbnails (2026-10-26),** after two Hormozi thumbnails ("FULL GUIDE" blueprint, 4M; "YOUR PATH" blueprint, 2.3M): "I have a great idea how we can proceed for anything education like this. character and blue explainer and then the rest will be real person reacting or pointing at the problem. ... we could even place character over winnin thumbnails that dont have character or take in spiration from closeup non character ones and add a character to them. those are the only ones i really want to look at". And: "I also want you to study the text useed on the recent winners in thumbs. those are important".

**Thumbnail text study (main session, 2026-10-26):** `data/thumb-text/recent-thumb-text.csv`: the 82 recent winners (top 50 of 90 days and of 12 months, deduplicated) with their thumbnail words (from `thumbnails/labels-top-recent.csv`; the main session viewed all 82 images on contact sheets and found the words correct), a text type (reading), a lane flag (reading: out = electric bill, space heaters, fire habits, dryer vents, kitchen, lithium batteries, smoke alarms, cords/NEVER lists; one HVAC video) and, for in-lane videos, whether the text repeats the title or adds to it. Blind check: a second helper sorted the 73 texts without seeing the main session's types (`blind-check.csv`): 65 of 73 agree, 40 of 43 in lane; with its calls the order barely moves. Findings (in lane, 49 videos, raw views, small samples): typical 4 words; command 6 videos, typical 531K; question 9, 520K (406K with the checker's calls); topic label 15, 211K (241K); tease 4, 209K; mistake 3, 357K; no text 6, 4.2M (hack channels). Repeats the title 18, 332K; adds to it 25, 289K: no clear difference.
On the operator's looks: no thumbnail in the 403 labelled pairs a presenter with a blueprint board like the Hormozi ones. Nearest: The Wiring Guide "Live Neutral Ground EXPLAINED" (real man + drawn wire lines, 1.04M); Sparky Steve (AI man beside panel diagrams: 17K, 2.6K). Diagram-only thumbnails: 30 labelled. Person reacting or pointing: 31 labelled; among recent winners AI personas in this look did 375-710K (Bertha's Clean Home 710K, Frederick 439K, Ray Dutton's Garage 406K, Ramón Delgado 375K). Page: `thumbnails/thumbnail-text.html`, published privately: https://claude.ai/artifact/DU5qu4MruAiEVR5B2eY4Rg
