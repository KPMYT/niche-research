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
