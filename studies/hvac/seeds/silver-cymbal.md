# Silver Cymbal: HVAC seed videos

**Channel:** Silver Cymbal, [@SilverCymbal](https://www.youtube.com/@SilverCymbal), channel ID `UC67dKTEwpAhKv2oYDATwR8g`. On-camera home DIY. Header on 2026-10-23: 1.09M subscribers, 539 videos (measured, channel page).

**Pulled:** 2026-10-23 by the Round 1 seed helper. Not yet re-checked by a second helper (working rule 3).

## How this list was made

| Item | Value | Source |
|---|---|---|
| Videos on the Videos tab | 538 | YouTube channel Videos tab, logged-out curl + innertube continuations, all 18 pages (`data/tools/yt_allsorts.py`) |
| Shorts | 1 (`EpGDf1jp0vA`, on the Shorts tab, not on the Videos tab) | YouTube Shorts tab; header count 539 = 538 + 1 Short |
| Live streams | none found (no Live tab on the channel) | YouTube channel tabs: Home, Videos, Shorts, Playlists, Posts |
| Long-form (>= 300 s) | 321 | tab duration text; seed lengths re-checked with NexLev `lengthSeconds` |
| Dropped as under 5 minutes | 217 (plus the 1 Short) | same |
| Baseline rule used | last-12-months rule: long-form uploaded 2025-10-23 to 2026-10-23, n = 18 (>= 10, so the last-30 fallback was not needed) | exact dates from innertube /next |
| Baseline median views | **79,807** | median of those 18 exact view counts (mean of the 9th and 10th: 78,736 and 80,878) |
| His all-time long-form median, for context | 243,780 (= 3.05x the baseline) | same data |
| Multiple | views / 79,807 | calculated |

**Sorts checked (measured, 2026-10-23):**

- **Popular** works: 538 videos, view counts never go up from one video to the next (0 breaks in order); starts with `TofHP1moT78` "NEVER SOLDER PIPE AGAIN" at 21M.
- **Oldest** works: 538 videos, the age text never gets newer down the list (0 breaks); starts with `KZL7tt3culs` "World's ONLY Factory Built GLASS ENGINE" (2015-08-29), ends with the newest upload.
- **Latest** works only through its chip: the default page plus its own continuation stopped at 30 videos (the old `yt.py` method). Loading the "Latest" chip and paging gave all 538, exactly the Oldest list reversed.
- All three sorts return the same 538 IDs.

**Where each figure comes from:**

- **Views:** exact counts from the YouTube video page data (innertube `/next`), pulled 2026-10-23 at about 03:30 UTC. NexLev `youtube_video_details` was called for every seed; its counts are a few views higher on most (pulled minutes later; largest gap +107 on `DSNUyxZtrmo`, and -53 on `yCZqfnlBYW8`). Both are in the CSV.
- **Upload date:** YouTube `/next` date text. It matches NexLev `publishDate` on all 24 videos checked (the 22 seeds, `sHL4lBAhklA` and `JyZgGSmtCRY`).
- **Length:** NexLev `lengthSeconds`. The Videos-tab text is the same or 1 second longer (of 24 checked: 13 identical, 11 one second longer), so the tab rounds up. The 5-minute filter used the tab text; the two edge videos (tab 5:00 and 5:01) were checked in NexLev: 300 s each, so both stay long-form.
- **Thumbnail:** `https://i.ytimg.com/vi/<id>/hqdefault.jpg`; the maxres URL NexLev returned is in the CSV (`yCZqfnlBYW8` has none: not found).
- **Topic group, borderline calls, lean:** my reading from titles and, where unsure, the video description. Not measured.

**Problems found:**

- The watch page (`/watch?v=`) and the `/player` endpoint are blocked from the cloud (Google 'sorry' redirect, LOGIN_REQUIRED), so exact length came from NexLev, not YouTube.
- NexLev `youtube_channel_videos` dates are guessed from the rounded '1 month ago' text, not real: it gives `sHL4lBAhklA` 2026-09-23, the real date is 2026-08-30. Its views are rounded (1.5M). Don't use its listing dates.
- NexLev's channel listing said `videosCount: 31` for this channel, which is wrong (the tab has 538).

## Seed videos (22), sorted by views

Long-form only. Sub-niche, format, emotions and villain were filled on 2026-10-23 by the labelling helper, using the definitions in `../labels.md`. They are **readings** (title first, then thumbnail text; the description only to confirm), not measurements. Emotions: up to 3, strongest first. Not yet re-checked by a second helper.

| # | Video ID | Title | Views | Upload date | Length | Multiple | Topic group (reading) | Thumbnail | Sub-niche (reading) | Format (reading) | Emotions (reading) | Villain (reading) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `_b6p0fkWhCY` | "#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" | 4,307,728 | 2018-07-20 | 8:52 | 53.98x | AC (central) - not cooling / condenser + filter | https://i.ytimg.com/vi/_b6p0fkWhCY/hqdefault.jpg | AC: central | symptom-fix | E19, E10, E13 | none |
| 2 | `qAxJb0J1HH0` | "How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling? or in the Pan" | 3,772,025 | 2019-07-31 | 8:09 | 47.26x | AC (central) - condensate drain | https://i.ytimg.com/vi/qAxJb0J1HH0/hqdefault.jpg | AC: central | symptom-fix | E4, E8, E13 | none |
| 3 | `Wejop_Rjpv0` | "Install your own AIR CONDITIONING in 4 HOURS!  DIY Mini Split MR COOL" | 3,087,177 | 2021-06-12 | 10:13 | 38.68x | mini-split - DIY install | https://i.ytimg.com/vi/Wejop_Rjpv0/hqdefault.jpg | mini-split | install/DIY project | E13, E8 | none |
| 4 | `o8KQu_MlpoY` | "Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" | 2,363,606 | 2020-06-08 | 6:09 | 29.62x | AC (window) - not cooling / cleaning | https://i.ytimg.com/vi/o8KQu_MlpoY/hqdefault.jpg | AC: window | symptom-fix | E19, E8, E13 | none |
| 5 | `DSNUyxZtrmo` | "How to Clean Your Mini Split AC Condenser - Make it Cold Again" | 1,859,343 | 2023-06-23 | 7:06 | 23.30x | mini-split - condenser cleaning | https://i.ytimg.com/vi/DSNUyxZtrmo/hqdefault.jpg | mini-split | how-to | E19, E8, E10 | none |
| 6 | `nsRHhU6q5RY` | "Central Air Conditioner Condenser Cleaning - How To - Make it COLD again!" | 1,454,183 | 2019-07-26 | 8:04 | 18.22x | AC (central) - condenser cleaning | https://i.ytimg.com/vi/nsRHhU6q5RY/hqdefault.jpg | AC: central | how-to | E19, E13, E8 | none |
| 7 | `zvFKD95z7IM` | "How to Install a Mr Cool 18,000 BTU AC in Just 1 Day!" | 1,296,956 | 2022-07-10 | 9:57 | 16.25x | mini-split - DIY install | https://i.ytimg.com/vi/zvFKD95z7IM/hqdefault.jpg | mini-split | install/DIY project | E13, E8 | none |
| 8 | `5GbXgEYw5TE` | "Oil Heat 🔥 Boilers - How it works - Understand the Basics" | 820,639 | 2018-02-10 | 22:18 | 10.28x | boiler (oil heat) - how it works | https://i.ytimg.com/vi/5GbXgEYw5TE/hqdefault.jpg | boilers and old-house heat | explainer | E13, E10 | none |
| 9 | `leEsPGaaru8` | "EcoFlow Wave PORTABLE Battery Powered Air Conditioner 4000 BTU" | 698,976 | 2022-05-17 | 6:29 | 8.76x | AC (portable, battery) - product review | https://i.ytimg.com/vi/leEsPGaaru8/hqdefault.jpg | AC: portable | review | E20 | none |
| 10 | `BP1iDvKpNZA` | "Why Heat Pumps are now leaving people COLD" | 631,905 | 2024-01-17 | 5:30 | 7.92x | heat pump - cold-climate failure | https://i.ytimg.com/vi/BP1iDvKpNZA/hqdefault.jpg | heat pumps | news-warning | E19, E3, E10 | the maker and the store shelf |
| 11 | `NsPBamTmOPM` | "This Tiny Portable AC can Keep Anyone COOL - 14,000 BTU Dreo - Single Hose Trigger Warning!" | 527,951 | 2025-05-30 | 5:08 | 6.62x | AC (portable) - product review | https://i.ytimg.com/vi/NsPBamTmOPM/hqdefault.jpg | AC: portable | review | E20, E19, E12 | none |
| 12 | `uObGbs4sGQY` | "Say Goodbye to BIG Air Conditioners - This Tiny Portable AC Blows them Away!" | 503,681 | 2024-05-08 | 5:00 | 6.31x | AC (portable heat pump) - product review | https://i.ytimg.com/vi/uObGbs4sGQY/hqdefault.jpg | AC: portable | review | E20, E19 | none |
| 13 | `yCZqfnlBYW8` | "Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" | 470,352 | 2017-12-31 | 5:18 | 5.89x | boiler - circulator pump repair (no heat) | https://i.ytimg.com/vi/yCZqfnlBYW8/hqdefault.jpg | boilers and old-house heat | before you do X | E5, E1, E13 | none |
| 14 | `ED3bfesbE_Y` | "Furnace Filter - How to Change it the Right Way & SAVE Money" | 388,617 | 2023-01-18 | 5:18 | 4.87x | filter - furnace filter | https://i.ytimg.com/vi/ED3bfesbE_Y/hqdefault.jpg | filters | how-to | E1, E12, E13 | your own habit |
| 15 | `GdTOl1WcHV0` | "Why Heating Oil is BETTER than GAS - Explained" | 343,444 | 2021-11-16 | 5:11 | 4.30x | heating fuel - oil vs gas | https://i.ytimg.com/vi/GdTOl1WcHV0/hqdefault.jpg | heating fuel and fuel choice | X vs Y | E12, E17, E14 | none |
| 16 | `flpbqJu2sT8` | "How to Replace a Circulator Pump on a Boiler" | 236,222 | 2017-12-17 | 23:20 | 2.96x | boiler - circulator pump replace | https://i.ytimg.com/vi/flpbqJu2sT8/hqdefault.jpg | boilers and old-house heat | how-to | E13 | none |
| 17 | `kEWzIfnIhUw` | "How To install Split Ductless AC & Heating System // Start to Finish - 1 PERSON!" | 221,217 | 2021-09-05 | 9:10 | 2.77x | mini-split - DIY install (heat + AC) | https://i.ytimg.com/vi/kEWzIfnIhUw/hqdefault.jpg | mini-split | install/DIY project | E13, E8 | none |
| 18 | `Xd-Og809TUo` | "Top 10 Heating Problems EASY Fixes for No HEAT - Boiler / Furnace Troubleshooting OIL HEAT" | 216,421 | 2018-11-23 | 10:44 | 2.71x | boiler/furnace - no-heat troubleshooting | https://i.ytimg.com/vi/Xd-Og809TUo/hqdefault.jpg | boilers and old-house heat | symptom-fix | E5, E13, E14 | none |
| 19 | `yZavrHJsBAw` | "Ecoflow Wave 2 Solar Battery Powered Portable Air Conditioner Heater Review" | 163,415 | 2023-05-17 | 7:33 | 2.05x | AC (portable heat pump) - product review | https://i.ytimg.com/vi/yZavrHJsBAw/hqdefault.jpg | AC: portable | review | E20 | none |
| 20 | `S8XO4wFhrPU` | "First Look at the NEW ECOFLOW Glacier Classic & Wave 3 Portable AC" | 117,116 | 2025-04-25 | 6:06 | 1.47x | AC (portable) + portable fridge - product first look | https://i.ytimg.com/vi/S8XO4wFhrPU/hqdefault.jpg | AC: portable | review | E20, E19 | none |
| 21 | `OGVXmIZtEG8` | "The BEST Portable Air Conditioner Just Got BETTER for 2026" | 65,273 | 2026-08-06 | 5:39 | 0.82x | AC (portable) - product review | https://i.ytimg.com/vi/OGVXmIZtEG8/hqdefault.jpg | AC: portable | the only X I'd buy | E20, E19, E1 | none |
| 22 | `cC-J0ZCUH28` | "3 Unknown Features on Mr Cool Mini Split Air Conditioners" | 32,326 | 2025-08-06 | 5:01 | 0.41x | mini-split - hidden features | https://i.ytimg.com/vi/cC-J0ZCUH28/hqdefault.jpg | mini-split | Y doesn't want you to know | E10, E13 | the maker and the store shelf |

## Summary

- **Count:** 22 long-form seeds (out of 321 long-form videos, 6.9%).
- **Median views:** seeds 515,816 vs his long-form median 243,780 (all time) and 79,807 (last 12 months).
- **Median multiple:** seeds 6.46x vs 3.05x for all his long-form videos (both against the 79,807 baseline).
- **Share at 2x or more:** seeds 19 of 22 (86%) vs 195 of 321 (61%) for all his long-form.
- **Upload years of the seeds:** 2017: 2, 2018: 3, 2019: 2, 2020: 1, 2021: 3, 2022: 2, 2023: 3, 2024: 2, 2025: 3, 2026: 1. Only 1 seed (`OGVXmIZtEG8`) is inside the 12-month baseline window.
- **Reading (not measured):** the multiples are high partly because most seeds are years old and the baseline is his last 12 months, when his output turned to power-station reviews (7 of the 18 baseline videos have generator, power-station or battery-backup titles). Treat the multiples as 'this beat his current typical video', not as a fair same-age comparison. The seeds' strongest group by views is AC cleaning/fixing (central, window, drain, condenser); product reviews of portable ACs sit at the bottom.

**Top 5 seeds:**

1. "#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" (`_b6p0fkWhCY`): 4,307,728 views, 54.0x, 2018-07-20
1. "How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling? or in the Pan" (`qAxJb0J1HH0`): 3,772,025 views, 47.3x, 2019-07-31
1. "Install your own AIR CONDITIONING in 4 HOURS!  DIY Mini Split MR COOL" (`Wejop_Rjpv0`): 3,087,177 views, 38.7x, 2021-06-12
1. "Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" (`o8KQu_MlpoY`): 2,363,606 views, 29.6x, 2020-06-08
1. "How to Clean Your Mini Split AC Condenser - Make it Cold Again" (`DSNUyxZtrmo`): 1,859,343 views, 23.3x, 2023-06-23

**Bottom 5 seeds:**

1. "Top 10 Heating Problems EASY Fixes for No HEAT - Boiler / Furnace Troubleshooting OIL HEAT" (`Xd-Og809TUo`): 216,421 views, 2.71x, 2018-11-23
1. "Ecoflow Wave 2 Solar Battery Powered Portable Air Conditioner Heater Review" (`yZavrHJsBAw`): 163,415 views, 2.05x, 2023-05-17
1. "First Look at the NEW ECOFLOW Glacier Classic & Wave 3 Portable AC" (`S8XO4wFhrPU`): 117,116 views, 1.47x, 2025-04-25
1. "The BEST Portable Air Conditioner Just Got BETTER for 2026" (`OGVXmIZtEG8`): 65,273 views, 0.82x, 2026-08-06
1. "3 Unknown Features on Mr Cool Mini Split Air Conditioners" (`cC-J0ZCUH28`): 32,326 views, 0.41x, 2025-08-06

## Label summary (reading)

Added 2026-10-23 by the labelling helper. The labels are readings (definitions in `../labels.md`); the views and multiples are the measured figures in the seed table above, and the medians were computed from that table by script. Each row gives n (how many of the 22 seeds carry the label), the median views and the median multiple of those videos.

**Read this first:**

- **n is tiny.** 22 videos in all, and most labels have 1 to 6. A label on 1 video is one video, not a pattern.
- **These are an on-camera DIY channel's numbers** (Silver Cymbal, a real man doing the work on camera, 1.09M subscribers), **not Roger's audience.** They say what this channel's viewers clicked, not what a faceless "retired pro" will get.
- **Age is mixed in.** The multiples use his last-12-months baseline (79,807), and older videos have had years to collect views. The symptom-fix seeds are all from 2018 to 2020 and the central-AC seeds from 2018 to 2019; the portable-AC reviews are from 2022 to 2026. Some of the gap between labels is age, not the label.
- All 22 seeds: median 515,816 views, median multiple 6.46x (as in the Summary above).

**By sub-niche**

| Sub-niche (reading) | n | Median views | Median multiple |
|---|---|---|---|
| AC: portable | 6 | 333,548 | 4.18x |
| mini-split | 5 | 1,296,956 | 16.25x |
| boilers and old-house heat | 4 | 353,287 | 4.42x |
| AC: central | 3 | 3,772,025 | 47.26x |
| AC: window | 1 | 2,363,606 | 29.62x |
| heat pumps | 1 | 631,905 | 7.92x |
| filters | 1 | 388,617 | 4.87x |
| heating fuel and fuel choice | 1 | 343,444 | 4.30x |

AC of every kind (central, window, portable, mini-split) is 15 of the 22. None of the seeds is about furnaces alone, thermostats, ducts, capacitors and parts, seasonal maintenance, the energy bill, humidity or brand verdicts (0 each).

**By format**

| Format (reading) | n | Median views | Median multiple |
|---|---|---|---|
| review | 5 | 503,681 | 6.31x |
| symptom-fix (new) | 4 | 3,067,816 | 38.44x |
| how-to | 4 | 921,400 | 11.54x |
| install/DIY project (new) | 3 | 1,296,956 | 16.25x |
| explainer (new) | 1 | 820,639 | 10.28x |
| news-warning (new) | 1 | 631,905 | 7.92x |
| before you do X | 1 | 470,352 | 5.89x |
| X vs Y | 1 | 343,444 | 4.30x |
| the only X I'd buy | 1 | 65,273 | 0.82x |
| Y doesn't want you to know | 1 | 32,326 | 0.41x |
| mistakes, cheap hack, myth-bust, story, test | 0 | not found | not found |

**By emotion** (a video counts under every emotion it carries, so the n add up to more than 22)

| Emotion (reading) | n (any of its 3) | n as the strongest | Median views (any) | Median multiple (any) |
|---|---|---|---|---|
| E13 pride in self-reliance | 13 | 5 | 820,639 | 10.28x |
| E19 comfort (NEW) | 9 | 5 | 631,905 | 7.92x |
| E8 satisfaction of the clear payoff | 7 | 0 | 1,859,343 | 23.30x |
| E20 new-gadget wonder (NEW) | 6 | 6 | 333,548 | 4.18x |
| E10 insider curiosity | 5 | 1 | 820,639 | 10.28x |
| E1 fear of the big bill | 3 | 1 | 388,617 | 4.87x |
| E12 vindication and the myth-bust | 3 | 1 | 388,617 | 4.87x |
| E5 emergency dread and urgency | 2 | 2 | 343,386 | 4.30x |
| E14 relief and reassurance | 2 | 0 | 279,932 | 3.50x |
| E4 dread of silent, hidden damage | 1 | 1 | 3,772,025 | 47.26x |
| E3 distrust of the store shelf | 1 | 0 | 631,905 | 7.92x |
| E17 safety fear | 1 | 0 | 343,444 | 4.30x |
| E2, E6, E7, E9, E11, E15, E16, E18 | 0 | 0 | not found | not found |

**By villain**

| Villain (reading) | n | Median views | Median multiple |
|---|---|---|---|
| none | 19 | 527,951 | 6.62x |
| the maker and the store shelf | 2 | 332,116 | 4.17x |
| your own habit | 1 | 388,617 | 4.87x |
| the HVAC company, the service call, the upsell, the bill-sender, the last owner or the flipper, insider | 0 | not found | not found |

**What I read from this (reading, not measured):** his HVAC hits are plain "fix it yourself and feel it work" videos (symptom-fix, how-to, install; E13, E8, E19) with no villain at all. 19 of 22 seeds name no villain, so this channel gives no evidence either way on the villains Roger would use. The product reviews (E20) sit at the bottom by multiple, but they are also the newest, so age and label can't be separated here.

## Borderline and excluded (long-form)

**Operator decision 2026-10-24:** the pellet stove video (`9d9TL02idO4`) counts as a seed (off-grid heat sub-niche). The rest of this table stays out. The seed table and summary above still show the 22; round 3 rebuilds the counts with 23.

Not counted as seeds. 'Lean' is my reading, for the operator to decide. The four label columns on the right were added on 2026-10-23 by the labelling helper (readings, same definitions as the seeds); they are not in the label summary above.

| Video ID | Title | Views | Upload date | Length (tab) | Multiple | Why borderline | Lean | Sub-niche (reading) | Format (reading) | Emotions (reading) | Villain (reading) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `sHL4lBAhklA` | "Spray Foam is Expensive. Use THIS Instead!" | 1,519,132 | 2026-08-30 | 5:34 | 19.04x | Spray foam alternative (duct seal) for sealing gaps around wires/pipes (description). Title is about the cost of spray foam, not heating, cooling or the bill. | operator call | drafts, insulation and air sealing | cheap hack | E1, E3, E12 | the maker and the store shelf |
| `9d9TL02idO4` | "Everyone will be buying pellet stoves after learning this news" | 1,399,618 | 2023-11-26 | 8:47 | 17.54x | Pellet stove install + US tax credit 'to help pay for heating your home' (description). Home heating and cost, but a stove is not in the brief's HVAC list. | lean include | alternative and supplemental heat | news-warning | E10, E1, E13 | none |
| `pPMm0reEBPM` | "Cheap & Easy Way to Connect a Generator to Your House - Legal Too!" | 1,205,390 | 2023-12-21 | 8:19 | 15.10x | Generator inlet/interlock hookup; description mentions running 'heating systems'. Generator how-to (backfeed safety = electrical study). | lean exclude | heat and power in an outage | cheap hack | E1, E18, E13 | none |
| `yNBXE3BszEM` | "How to power your Whole House with a battery generator - Ecoflow Delta pro" | 982,861 | 2023-01-11 | 7:23 | 12.32x | Whole-house battery backup (EcoFlow); description mentions heat. Product/power-station video. | exclude (rule) | heat and power in an outage | install/DIY project | E20, E13 | none |
| `EjLJm0g4whg` | "How to Make Your Garage Door SEAL TIGHT as a Fridge" | 906,215 | 2026-05-17 | 6:36 | 11.36x | Garage-door weatherstripping. Description says 'hot, humid, drafty' but also bugs and mice; garage, not living space; title not about heat/bill. | operator call | drafts, insulation and air sealing | how-to | E8, E7, E13 | none |
| `BACQ3167pkA` | "Easy DIY Generator Transfer Switch Install - Works with ANY Portable Gas or Battery Generator" | 810,090 | 2022-01-24 | 7:54 | 10.15x | Generator transfer switch install. Generator how-to. | exclude (rule) | heat and power in an outage | install/DIY project | E13, E14 | none |
| `_G7ZPjmR5ck` | "Surviving a 36 Hour Power Outage with the BIGGEST ECOFLOW DELTA PRO ULTRA - 30KWH!!!!" | 664,772 | 2024-04-23 | 7:37 | 8.33x | 36-hour outage on an EcoFlow battery. Power-station product video. | exclude (rule) | heat and power in an outage | test | E5, E20 | none |
| `3x5t4Zvkqms` | "How to Heat a Small shop with a BUILT IN Diesel Wall Heater" | 353,981 | 2024-01-07 | 8:26 | 4.44x | Diesel heater for a shop (description: vans, sheds, tents, RVs). Not the house. | lean exclude | alternative and supplemental heat | install/DIY project | E13, E20 | none |
| `CRTh8fIhV5E` | "How to Restore a WOOD STOVE the EASY WAY - Like New in Minutes" | 334,374 | 2022-01-08 | 5:39 | 4.19x | Wood stove restoration (cosmetic). Heating appliance, not HVAC system. | lean exclude | alternative and supplemental heat | how-to | E8, E13, E15 | none |
| `Roz9OXl5uEU` | "Don't Buy a Rooftop Solar System Before Seeing my Disaster" | 277,080 | 2023-04-02 | 11:43 | 3.47x | Rooftop solar contractor disaster. Energy, but not the bill or HVAC. | lean exclude | out of scope: solar | before you do X | E4, E1, E2 | the HVAC company (here: the solar contractor) |
| `r31vJXrZD3Y` | "Make your BATHROOM FAN LIKE NEW without Attic Access" | 275,264 | 2021-09-18 | 5:43 | 3.45x | Bathroom exhaust fan refresh. Ventilation, often filed as electrical. | lean exclude | humidity, ventilation and indoor air | how-to | E8, E7, E13 | the service call |
| `CXjNHwFg0aQ` | "MINDBLOWING Crawlspace Transformation - Next Level ENCAPSULATION" | 242,232 | 2023-08-27 | 7:13 | 3.04x | Crawlspace encapsulation; description: humidity, mold, dehumidifier. Humidity is in scope, but this is a building-envelope project. | operator call | humidity, ventilation and indoor air | install/DIY project | E8, E12, E7 | the last owner or the flipper (read as: the old builders) |
| `zMSWKLvDFTc` | "How to Install a Kitchen Range Hood that VENTS OUTSIDE" | 236,038 | 2026-08-16 | 12:28 | 2.96x | Kitchen range hood vented outside. Ventilation install. | lean exclude | humidity, ventilation and indoor air | install/DIY project | E8, E13 | none |
| `KV4tWIPLFc8` | "NEW Way to remove GROSS FIBERGLASS INSULATION - Full Batts!" | 163,677 | 2023-08-06 | 7:01 | 2.05x | Removing fiberglass insulation. Insulation, but title not about heating, cooling or the bill (rule 5). | exclude (rule) | drafts, insulation and air sealing | how-to | E7, E8, E20 | none |
| `k8hK9duZIGo` | "How to PREVENT Pipes Freezing in your House or RV - HEAT TAPE" | 123,405 | 2021-11-27 | 5:54 | 1.55x | Heat tape to stop pipes freezing. Plumbing freeze protection. | plumbing | adjacent: plumbing (freeze) | how-to | E4, E5, E13 | none |
| `OYM8aSESAY8` | "SURVIVING the Worst Snow Storm in 30 Years" | 110,378 | 2023-03-15 | 6:05 | 1.38x | Snowstorm with no power (description: 'what I did to make it through'). Outage, but heat not named in title or description. | operator call | heat and power in an outage | story | E5, E13 | none |
| `ZJQjKOnbLKU` | "How Safe are DREO Electric Space Heaters?" | 94,700 | 2025-01-07 | 5:27 | 1.19x | Space-heater safety. Space heaters sit in the electrical/fire study's scope. | electrical study | alternative and supplemental heat (space heater; electrical study) | test | E17, E3, E16 | the maker and the store shelf |
| `TVkQ_aU2cWQ` | "When Your Cars Interior Smells Funky - Check This First" | 36,871 | 2025-10-22 | 6:52 | 0.46x | Car interior smell (cabin filter, ozone). Car, not house. | exclude | out of scope: car | symptom-fix | E7, E9, E10 | none |
| `IgeexSKIEOQ` | "Storm Prep: How to Power Your House with a Battery Almost Indefinitely - Anker SOLIX" | 36,806 | 2025-06-27 | 6:20 | 0.46x | Storm prep with an Anker battery. Power-station product video. | exclude (rule) | heat and power in an outage | how-to | E5, E14, E20 | none |

Also excluded without listing one by one: **73 long-form generator / power-station / battery-backup videos** (title keyword count, my reading of the rule 'generator and power-station product reviews are OUT'). IDs are in the raw file.

## Adjacent: water heaters (plumbing, not seeds)

| Video ID | Title | Views | Upload date | Length (tab) | Multiple |
|---|---|---|---|---|---|
| `YNBdtC9jjLA` | "How To Clean & Flush Tankless Hot Water Heaters with VINEGAR!" | 606,755 | 2020-10-17 | 5:39 | 7.60x |
| `e1TpseQATTw` | "EASY Way to Flush Your Hot Water Heater using AIR - Sediment Buster" | 260,090 | 2024-02-11 | 6:02 | 3.26x |
| `R5lfB2G8fnQ` | "How to Replace Hot Water Tank Pressure Relief Valve - T&P" | 126,340 | 2017-12-11 | 17:44 | 1.58x |

## HVAC-type videos dropped by the 5-minute rule (for reference)

Under 300 seconds on the tab, so not seeds. Listed because they are a real part of his HVAC output (10 of the 12 are HVAC proper), and the window-AC install (2,861,907 views) would rank 4th among the seeds. Topic is my reading.

| Video ID | Title | Views | Upload date | Length (tab) | Topic (reading) |
|---|---|---|---|---|---|
| `M-pa_vUNGl4` | "Midea 8,000 BTU U Shaped Smart Inverter Window AC Installation & Review" | 2,861,907 | 2020-02-17 | 4:53 | AC (window) install/review |
| `ydRveyXkf4M` | "How to Connect a Small Generator to Your House - Safe & Legal - Run Heat, Fridge & More!" | 1,021,421 | 2018-11-13 | 4:18 | generator hookup to 'run heat' (borderline) |
| `Lw9awU9xehE` | "EASY WAY to FLUSH your HOT WATER HEATER TANK" | 655,722 | 2022-06-25 | 3:35 | water heater flush (adjacent) |
| `NI-KNyp9tdQ` | "BEST Portable Air Conditioner I have ever tested -  DUAL HOSE" | 519,566 | 2022-08-20 | 4:43 | AC (portable) |
| `NqFgelKaQvc` | "Is the Midea DUO Smart Inverter Portable Air Conditioner Worth It?" | 376,989 | 2025-06-19 | 3:35 | AC (portable) |
| `dgpGsszbF4E` | "This Portable Air Conditioner BLEW me Away - 14,000 BTU Midea Smart Inverter" | 296,156 | 2023-07-31 | 4:42 | AC (portable) |
| `JDq4i_lT8YI` | "TESTING the CHEAPEST AIR CONDITIONER on Amazon" | 174,583 | 2021-08-11 | 3:58 | AC (cheapest on Amazon) |
| `biNdfKcxaqE` | "Ultimate Home Dehumidifier Midea CUBE Review" | 145,332 | 2020-11-19 | 4:06 | dehumidifier |
| `k8PlPcKGENw` | "How to Change a Furnace Filter the RIGHT Way" | 139,492 | 2025-03-18 | 4:26 | filter - furnace filter |
| `xuswKBmauI4` | "No Heat? How to Replace & Troubleshoot a Taco Zone Valve" | 136,871 | 2017-12-28 | 3:26 | boiler - zone valve (no heat) |
| `5cvAHDqpgUY` | "WHY Sony's Pocket Sized Air Conditioner Failed?" | 68,702 | 2020-11-14 | 4:21 | AC (Sony pocket AC) |
| `SIyntnwE7O8` | "Best Kept Secret for Staying Warm When the Power is Out" | 43,932 | 2021-12-15 | 4:18 | outage heat |

## Files

- Full list: `data/raw/silver-cymbal-all-2026-10-23.json` (538 videos: id, title, exact views, date, duration, Popular and Latest rank, source of each field)
- Seed CSV: `data/raw/silver-cymbal-seeds-2026-10-23.csv`
- Raw pulls: `data/raw/silver-cymbal/` (tab pull for all three sorts, `/next` results, NexLev seed details)
- Tools: `data/tools/yt_allsorts.py`, `vid_next_batch.py`, `sc_build.py`, `sc_seeds.py` (`vid_exact.py` is the watch-page attempt that was blocked)
