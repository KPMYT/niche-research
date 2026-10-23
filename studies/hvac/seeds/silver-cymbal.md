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

Long-form only. Sub-niche, format, emotions and villain are left blank for the labelling round.

| # | Video ID | Title | Views | Upload date | Length | Multiple | Topic group (reading) | Thumbnail | Sub-niche | Format | Emotions | Villain |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `_b6p0fkWhCY` | "#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" | 4,307,728 | 2018-07-20 | 8:52 | 53.98x | AC (central) - not cooling / condenser + filter | https://i.ytimg.com/vi/_b6p0fkWhCY/hqdefault.jpg |  |  |  |  |
| 2 | `qAxJb0J1HH0` | "How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling? or in the Pan" | 3,772,025 | 2019-07-31 | 8:09 | 47.26x | AC (central) - condensate drain | https://i.ytimg.com/vi/qAxJb0J1HH0/hqdefault.jpg |  |  |  |  |
| 3 | `Wejop_Rjpv0` | "Install your own AIR CONDITIONING in 4 HOURS!  DIY Mini Split MR COOL" | 3,087,177 | 2021-06-12 | 10:13 | 38.68x | mini-split - DIY install | https://i.ytimg.com/vi/Wejop_Rjpv0/hqdefault.jpg |  |  |  |  |
| 4 | `o8KQu_MlpoY` | "Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" | 2,363,606 | 2020-06-08 | 6:09 | 29.62x | AC (window) - not cooling / cleaning | https://i.ytimg.com/vi/o8KQu_MlpoY/hqdefault.jpg |  |  |  |  |
| 5 | `DSNUyxZtrmo` | "How to Clean Your Mini Split AC Condenser - Make it Cold Again" | 1,859,343 | 2023-06-23 | 7:06 | 23.30x | mini-split - condenser cleaning | https://i.ytimg.com/vi/DSNUyxZtrmo/hqdefault.jpg |  |  |  |  |
| 6 | `nsRHhU6q5RY` | "Central Air Conditioner Condenser Cleaning - How To - Make it COLD again!" | 1,454,183 | 2019-07-26 | 8:04 | 18.22x | AC (central) - condenser cleaning | https://i.ytimg.com/vi/nsRHhU6q5RY/hqdefault.jpg |  |  |  |  |
| 7 | `zvFKD95z7IM` | "How to Install a Mr Cool 18,000 BTU AC in Just 1 Day!" | 1,296,956 | 2022-07-10 | 9:57 | 16.25x | mini-split - DIY install | https://i.ytimg.com/vi/zvFKD95z7IM/hqdefault.jpg |  |  |  |  |
| 8 | `5GbXgEYw5TE` | "Oil Heat 🔥 Boilers - How it works - Understand the Basics" | 820,639 | 2018-02-10 | 22:18 | 10.28x | boiler (oil heat) - how it works | https://i.ytimg.com/vi/5GbXgEYw5TE/hqdefault.jpg |  |  |  |  |
| 9 | `leEsPGaaru8` | "EcoFlow Wave PORTABLE Battery Powered Air Conditioner 4000 BTU" | 698,976 | 2022-05-17 | 6:29 | 8.76x | AC (portable, battery) - product review | https://i.ytimg.com/vi/leEsPGaaru8/hqdefault.jpg |  |  |  |  |
| 10 | `BP1iDvKpNZA` | "Why Heat Pumps are now leaving people COLD" | 631,905 | 2024-01-17 | 5:30 | 7.92x | heat pump - cold-climate failure | https://i.ytimg.com/vi/BP1iDvKpNZA/hqdefault.jpg |  |  |  |  |
| 11 | `NsPBamTmOPM` | "This Tiny Portable AC can Keep Anyone COOL - 14,000 BTU Dreo - Single Hose Trigger Warning!" | 527,951 | 2025-05-30 | 5:08 | 6.62x | AC (portable) - product review | https://i.ytimg.com/vi/NsPBamTmOPM/hqdefault.jpg |  |  |  |  |
| 12 | `uObGbs4sGQY` | "Say Goodbye to BIG Air Conditioners - This Tiny Portable AC Blows them Away!" | 503,681 | 2024-05-08 | 5:00 | 6.31x | AC (portable heat pump) - product review | https://i.ytimg.com/vi/uObGbs4sGQY/hqdefault.jpg |  |  |  |  |
| 13 | `yCZqfnlBYW8` | "Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" | 470,352 | 2017-12-31 | 5:18 | 5.89x | boiler - circulator pump repair (no heat) | https://i.ytimg.com/vi/yCZqfnlBYW8/hqdefault.jpg |  |  |  |  |
| 14 | `ED3bfesbE_Y` | "Furnace Filter - How to Change it the Right Way & SAVE Money" | 388,617 | 2023-01-18 | 5:18 | 4.87x | filter - furnace filter | https://i.ytimg.com/vi/ED3bfesbE_Y/hqdefault.jpg |  |  |  |  |
| 15 | `GdTOl1WcHV0` | "Why Heating Oil is BETTER than GAS - Explained" | 343,444 | 2021-11-16 | 5:11 | 4.30x | heating fuel - oil vs gas | https://i.ytimg.com/vi/GdTOl1WcHV0/hqdefault.jpg |  |  |  |  |
| 16 | `flpbqJu2sT8` | "How to Replace a Circulator Pump on a Boiler" | 236,222 | 2017-12-17 | 23:20 | 2.96x | boiler - circulator pump replace | https://i.ytimg.com/vi/flpbqJu2sT8/hqdefault.jpg |  |  |  |  |
| 17 | `kEWzIfnIhUw` | "How To install Split Ductless AC & Heating System // Start to Finish - 1 PERSON!" | 221,217 | 2021-09-05 | 9:10 | 2.77x | mini-split - DIY install (heat + AC) | https://i.ytimg.com/vi/kEWzIfnIhUw/hqdefault.jpg |  |  |  |  |
| 18 | `Xd-Og809TUo` | "Top 10 Heating Problems EASY Fixes for No HEAT - Boiler / Furnace Troubleshooting OIL HEAT" | 216,421 | 2018-11-23 | 10:44 | 2.71x | boiler/furnace - no-heat troubleshooting | https://i.ytimg.com/vi/Xd-Og809TUo/hqdefault.jpg |  |  |  |  |
| 19 | `yZavrHJsBAw` | "Ecoflow Wave 2 Solar Battery Powered Portable Air Conditioner Heater Review" | 163,415 | 2023-05-17 | 7:33 | 2.05x | AC (portable heat pump) - product review | https://i.ytimg.com/vi/yZavrHJsBAw/hqdefault.jpg |  |  |  |  |
| 20 | `S8XO4wFhrPU` | "First Look at the NEW ECOFLOW Glacier Classic & Wave 3 Portable AC" | 117,116 | 2025-04-25 | 6:06 | 1.47x | AC (portable) + portable fridge - product first look | https://i.ytimg.com/vi/S8XO4wFhrPU/hqdefault.jpg |  |  |  |  |
| 21 | `OGVXmIZtEG8` | "The BEST Portable Air Conditioner Just Got BETTER for 2026" | 65,273 | 2026-08-06 | 5:39 | 0.82x | AC (portable) - product review | https://i.ytimg.com/vi/OGVXmIZtEG8/hqdefault.jpg |  |  |  |  |
| 22 | `cC-J0ZCUH28` | "3 Unknown Features on Mr Cool Mini Split Air Conditioners" | 32,326 | 2025-08-06 | 5:01 | 0.41x | mini-split - hidden features | https://i.ytimg.com/vi/cC-J0ZCUH28/hqdefault.jpg |  |  |  |  |

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

## Borderline and excluded (long-form)

Not counted as seeds. 'Lean' is my reading, for the operator to decide.

| Video ID | Title | Views | Upload date | Length (tab) | Multiple | Why borderline | Lean |
|---|---|---|---|---|---|---|---|
| `sHL4lBAhklA` | "Spray Foam is Expensive. Use THIS Instead!" | 1,519,132 | 2026-08-30 | 5:34 | 19.04x | Spray foam alternative (duct seal) for sealing gaps around wires/pipes (description). Title is about the cost of spray foam, not heating, cooling or the bill. | operator call |
| `9d9TL02idO4` | "Everyone will be buying pellet stoves after learning this news" | 1,399,618 | 2023-11-26 | 8:47 | 17.54x | Pellet stove install + US tax credit 'to help pay for heating your home' (description). Home heating and cost, but a stove is not in the brief's HVAC list. | lean include |
| `pPMm0reEBPM` | "Cheap & Easy Way to Connect a Generator to Your House - Legal Too!" | 1,205,390 | 2023-12-21 | 8:19 | 15.10x | Generator inlet/interlock hookup; description mentions running 'heating systems'. Generator how-to (backfeed safety = electrical study). | lean exclude |
| `yNBXE3BszEM` | "How to power your Whole House with a battery generator - Ecoflow Delta pro" | 982,861 | 2023-01-11 | 7:23 | 12.32x | Whole-house battery backup (EcoFlow); description mentions heat. Product/power-station video. | exclude (rule) |
| `EjLJm0g4whg` | "How to Make Your Garage Door SEAL TIGHT as a Fridge" | 906,215 | 2026-05-17 | 6:36 | 11.36x | Garage-door weatherstripping. Description says 'hot, humid, drafty' but also bugs and mice; garage, not living space; title not about heat/bill. | operator call |
| `BACQ3167pkA` | "Easy DIY Generator Transfer Switch Install - Works with ANY Portable Gas or Battery Generator" | 810,090 | 2022-01-24 | 7:54 | 10.15x | Generator transfer switch install. Generator how-to. | exclude (rule) |
| `_G7ZPjmR5ck` | "Surviving a 36 Hour Power Outage with the BIGGEST ECOFLOW DELTA PRO ULTRA - 30KWH!!!!" | 664,772 | 2024-04-23 | 7:37 | 8.33x | 36-hour outage on an EcoFlow battery. Power-station product video. | exclude (rule) |
| `3x5t4Zvkqms` | "How to Heat a Small shop with a BUILT IN Diesel Wall Heater" | 353,981 | 2024-01-07 | 8:26 | 4.44x | Diesel heater for a shop (description: vans, sheds, tents, RVs). Not the house. | lean exclude |
| `CRTh8fIhV5E` | "How to Restore a WOOD STOVE the EASY WAY - Like New in Minutes" | 334,374 | 2022-01-08 | 5:39 | 4.19x | Wood stove restoration (cosmetic). Heating appliance, not HVAC system. | lean exclude |
| `Roz9OXl5uEU` | "Don't Buy a Rooftop Solar System Before Seeing my Disaster" | 277,080 | 2023-04-02 | 11:43 | 3.47x | Rooftop solar contractor disaster. Energy, but not the bill or HVAC. | lean exclude |
| `r31vJXrZD3Y` | "Make your BATHROOM FAN LIKE NEW without Attic Access" | 275,264 | 2021-09-18 | 5:43 | 3.45x | Bathroom exhaust fan refresh. Ventilation, often filed as electrical. | lean exclude |
| `CXjNHwFg0aQ` | "MINDBLOWING Crawlspace Transformation - Next Level ENCAPSULATION" | 242,232 | 2023-08-27 | 7:13 | 3.04x | Crawlspace encapsulation; description: humidity, mold, dehumidifier. Humidity is in scope, but this is a building-envelope project. | operator call |
| `zMSWKLvDFTc` | "How to Install a Kitchen Range Hood that VENTS OUTSIDE" | 236,038 | 2026-08-16 | 12:28 | 2.96x | Kitchen range hood vented outside. Ventilation install. | lean exclude |
| `KV4tWIPLFc8` | "NEW Way to remove GROSS FIBERGLASS INSULATION - Full Batts!" | 163,677 | 2023-08-06 | 7:01 | 2.05x | Removing fiberglass insulation. Insulation, but title not about heating, cooling or the bill (rule 5). | exclude (rule) |
| `k8hK9duZIGo` | "How to PREVENT Pipes Freezing in your House or RV - HEAT TAPE" | 123,405 | 2021-11-27 | 5:54 | 1.55x | Heat tape to stop pipes freezing. Plumbing freeze protection. | plumbing |
| `OYM8aSESAY8` | "SURVIVING the Worst Snow Storm in 30 Years" | 110,378 | 2023-03-15 | 6:05 | 1.38x | Snowstorm with no power (description: 'what I did to make it through'). Outage, but heat not named in title or description. | operator call |
| `ZJQjKOnbLKU` | "How Safe are DREO Electric Space Heaters?" | 94,700 | 2025-01-07 | 5:27 | 1.19x | Space-heater safety. Space heaters sit in the electrical/fire study's scope. | electrical study |
| `TVkQ_aU2cWQ` | "When Your Cars Interior Smells Funky - Check This First" | 36,871 | 2025-10-22 | 6:52 | 0.46x | Car interior smell (cabin filter, ozone). Car, not house. | exclude |
| `IgeexSKIEOQ` | "Storm Prep: How to Power Your House with a Battery Almost Indefinitely - Anker SOLIX" | 36,806 | 2025-06-27 | 6:20 | 0.46x | Storm prep with an Anker battery. Power-station product video. | exclude (rule) |

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
