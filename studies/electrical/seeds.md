# Silver Cymbal: electrical and fire-prevention seeds

Channel: **Silver Cymbal** (@SilverCymbal, `UC67dKTEwpAhKv2oYDATwR8g`), 1.09M subscribers, 539 videos (YT channel page and NexLev youtube_channel_about, 2026-10-23). On-camera DIY homeowner (NexLev check_faceless_channel: isFaceless=false, 97%). Helper 1, round 1, pulled 2026-10-23.

## How this was pulled

- Full Videos tab (Latest), 18 pages, **538 of 539 videos** listed (one missing; probably private/members or counted differently). Raw: `data/silver-cymbal/videos-latest.json`. Popular tab, 3 pages (90 videos): `data/silver-cymbal/videos-popular.json`; all 90 are in the Latest pull (cross-check passed). The Videos tab holds no Shorts.
- `yt.py channel ... latest` stopped after page 1 (its last continuation token on the first page is a sort chip, not the next page). I paged with yt.py's own functions, taking the first `continuationItemRenderer` token (scratch script, yt.py itself not changed). Worth fixing in yt.py for other helpers (main session's call).
- Exact views and upload dates: `yt.py video <id>` for every picked video (and the 50 newest uploads, for the multiple basis), 2026-10-23. Lengths: Videos-tab list page.
- **Multiple basis:** median of SC long-form (5:00+) uploads 2025-10-23..2026-10-23, all topics, n=18, median=79807 views (exact views, yt.py video, 2026-10-23). List of the 18 basis videos at the bottom.
- Labels (sub-niche, format, emotions, villain) are **my reading** of title + thumbnail. I looked at the thumbnail of **every** picked video (149, as contact sheets). Not watched.
- Format **`other:review`** (product review / first look) and **`other:explainer`** are not in labels.md; most of his power-station and generator videos are plain reviews and fit no existing format. Proposed as NEW labels for the main session to decide; labels.md not edited.

## Count: re-checked

The earlier "about 44 electrical videos" is too low for the full scope. **149 videos** are in the electrical / fire-prevention scope: **96 long-form (5:00+)** and **53 under 5:00** (short reference, not counted). Plus 31 borderline videos listed at the end and not counted.

| Group | Long-form | Under 5:00 | Total |
|---|---|---|---|
| Core electrical and fire (wiring, outlets/switches, breakers, connectors, GFCI, lighting, explainers, cords, space heater, dryer vent, holiday lights, outage tip, shower head) | 19 | 29 | 48 |
| Home power (power stations, gas generators and hook-ups, solar, chargers) | 77 | 24 | 101 |
| **All** | **96** | **53** | **149** |

My reading of the "44": the core electrical group alone is 48 videos, close to 44, so the earlier chat probably counted wiring/outlet/connector videos and left out power stations and generators. Not verified.

Important for the length rule: much of his best core-electrical work is **under 5:00** and so not counted: "What Happens When You Plug a SUICIDE CORD in a LIVE OUTLET?" (H-4mvK2FW78, 11,640,927 views, 2:42), "Why Do Electric Plugs Have Holes? Answered" (Db-dt5U3MCc, 8,646,225, 3:17), "What REALLY HAPPENS WHEN YOU SPILL WATER in an OUTLET?" (1tfvtJyucHc, 7,414,841, 4:21), "Never use Wire Nuts Again" (rMlI7qOm8hM, 5,966,495, 3:54).

## Long-form electrical / fire videos (96), sorted by views

Multiple = views / 79,807 (basis above). Labels are readings.

Caution (my reading): his last-12-months median (79,807) is far below his long-run level (NexLev get_batch_channel_metrics_v2 average views per video: 864,480), so old videos (2019-2023) show very large multiples. Older videos have also had years to collect views. Compare multiples within the same era; the 12-month basis is the rule from labels.md and was kept.

| # | Title | ID | Views | Date | Length | Sub-niche | Format | Emotions | Villain | Multiple |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | How to SOLDER WIRES TOGETHER - PRO TIPS for WATERPROOF CONNECTIONS | uj_PbRBirkQ | 15,647,092 | 2021-06-06 | 5:39 | connectors | how-to | E13 E8 E10 | none | 196.06x |
| 2 | Ultimate Home Generator? - Ecoflow Delta / Portable Backup Power | YyMonPCxzog | 4,750,418 | 2019-10-15 | 8:46 | backup-power-stations | other:review | E5 E13 E3 | none | 59.52x |
| 3 | BEWARE Of These 3 Common Wiring Mistakes On Outlets & Switches | irK7l3eyB8g | 4,486,163 | 2022-03-29 | 5:12 | wiring-mistakes | mistakes | E9 E17 E10 | own habit | 56.21x |
| 4 | How To Replace or Change a Circuit Breaker in your Electrical Panel & Why it's Tripping | ta0CvuSGQgY | 4,001,200 | 2020-12-05 | 6:11 | breakers-panels | how-to | E6 E13 E2 | none | 50.14x |
| 5 | Cheap Inverter Generator - Generac GP2200i Review - Alternative to Honda EU2200i | EXuP6tQACa8 | 2,338,108 | 2019-09-08 | 7:33 | generators-backfeed | x-vs-y | E3 E12 E8 | maker / shelf | 29.3x |
| 6 | Yamaha EF2200is Generator VS Honda EU2200i - Best Portable Generator? | iugI8dGS39A | 2,012,056 | 2019-09-28 | 6:59 | generators-backfeed | x-vs-y | E10 E3 | none | 25.21x |
| 7 | Easiest Electric Outlet to Install in 100 Years - Safest too! | nr5gPJQuLic | 1,846,248 | 2023-04-06 | 5:45 | outlets-switches | other:review | E10 E13 E17 | none | 23.13x |
| 8 | BIGGEST Harbor Freight Generator Predator 9500 Review & TEST | TfnMW1jwQEs | 1,719,155 | 2021-11-01 | 8:05 | generators-backfeed | other:review | E3 E10 | none | 21.54x |
| 9 | NEW HONDA BLUETOOTH Generator EU2200i Exposed! CO Minder Review / 2021 Model | CLqSPvvO_8U | 1,598,703 | 2020-09-12 | 8:57 | generators-backfeed | other:review | E10 E17 E3 | none | 20.03x |
| 10 | NO MORE GAS Generators? ECOFLOW DELTA PRO Review | bfWzPPDh2Yg | 1,535,025 | 2021-07-15 | 10:38 | backup-power-stations | other:review | E10 E5 E13 | none | 19.23x |
| 11 | MOST RUGGED Power Station in the WORLD! 8000 Watts - Hybrid Power Solutions Review | Wzb8OQJNDnc | 1,369,292 | 2021-09-08 | 6:48 | backup-power-stations | other:review | E10 E5 | none | 17.16x |
| 12 | Testing the CHEAPEST HARBOR FREIGHT INVERTER GENERATOR Predator 1400 | ksl4WAB3B0U | 1,305,213 | 2021-05-09 | 5:34 | generators-backfeed | test | E3 E10 | maker / shelf | 16.35x |
| 13 | Cheap & Easy Way to Connect a Generator to Your House - Legal Too! | pPMm0reEBPM | 1,205,397 | 2023-12-21 | 8:19 | generators-backfeed | cheap-hack | E2 E13 E18 | service call | 15.1x |
| 14 | BIGGEST 2400Wh Power Station & Solar Generator - NEW Bluetti EB240 -  Portable Backup Power | A9MVTWGvPho | 1,125,875 | 2020-02-04 | 7:39 | backup-power-stations | other:review | E5 E10 | none | 14.11x |
| 15 | What Happens When You Use a SUICIDE SHOWER HEAD in the US | E5Vs4Zsvo04 | 1,103,433 | 2022-10-30 | 6:31 | other:electric-shower-head | test | E17 E10 E18 | maker / shelf | 13.83x |
| 16 | Lightest 1000 Watt Power Station & Solar Generator - Jackery Explorer 1000 | W90DZ8uYzEo | 1,092,985 | 2020-03-06 | 5:06 | backup-power-stations | other:review | E14 E5 E13 | none | 13.7x |
| 17 | How to power your Whole House with a battery generator - Ecoflow Delta pro | yNBXE3BszEM | 982,861 | 2023-01-11 | 7:23 | backup-power-stations | how-to | E5 E13 E10 | none | 12.32x |
| 18 | Easy DIY Generator Transfer Switch Install - Works with ANY Portable Gas or Battery Generator | BACQ3167pkA | 810,090 | 2022-01-24 | 7:54 | generators-backfeed | how-to | E13 E5 E17 | none | 10.15x |
| 19 | What Wire Connector is the Best? Wire Nut VS Wago TESTED | B1pmuRsf1co | 768,182 | 2021-02-21 | 5:51 | connectors | x-vs-y | E12 E10 E3 | maker / shelf | 9.63x |
| 20 | Ecoflow Delta Max & Solar Tracker Review | DWjlQ4jNio4 | 693,563 | 2021-08-07 | 7:58 | backup-power-stations | other:review | E10 E13 | none | 8.69x |
| 21 | Honda Generator EU7000is Full Review - Best Home Backup Generator 2020 | _KCUVtXJCrI | 653,910 | 2017-12-16 | 9:34 | generators-backfeed | other:review | E5 E10 | none | 8.19x |
| 22 | How I built my SOLAR Powered Workshop - Power Anywhere | HhbKRWesOY8 | 601,817 | 2021-10-11 | 6:09 | solar | how-to | E13 E8 E1 | bill-sender | 7.54x |
| 23 | How To Install A 240V Outlet Start to Finish -  EV Car Charger - Welder 14-50 Explained | Yj_QUYuKgWw | 542,112 | 2025-09-14 | 17:43 | outlets-switches | how-to | E13 E18 E2 | none | 6.79x |
| 24 | How to Legally Mount Your TV & Hide the Wires - Adding an Outlet | Qwk1rER_EFM | 498,392 | 2024-09-03 | 9:44 | outlets-switches | how-to | E8 E13 E18 | none | 6.24x |
| 25 | BEST SOLAR LIGHT REVIEW - Just as bright as WIRED Lights! | LdCU-PPryEY | 490,104 | 2022-05-11 | 5:57 | lighting-led | other:review | E8 E3 E13 | none | 6.14x |
| 26 | Ultimate Power Station & Solar Generator - Jackery Explorer 500 Review | Q0JmZDRxE80 | 472,680 | 2019-12-22 | 5:58 | backup-power-stations | other:review | E5 E10 | none | 5.92x |
| 27 | ⚡️Honda Generator EU2200i Full Review - Upgrade to Honda EU2000i Best Generator 2019 | hqnR7WK9UeU | 468,174 | 2018-09-23 | 13:43 | generators-backfeed | other:review | E10 | none | 5.87x |
| 28 | Ultimate USB Outlet Install - No More Chargers! | xuj-sEJryxw | 429,966 | 2021-02-12 | 6:49 | outlets-switches | how-to | E8 E13 | none | 5.39x |
| 29 | Dirty Secret about the New 2024 Romex Wire Colors | taxobtIQwx4 | 424,465 | 2024-10-28 | 5:34 | electrical-explainer | dont-want-you | E10 E18 E3 | maker / shelf | 5.32x |
| 30 | Ecoflow River 600 Portable Battery Generator Review - R600 | FUnlW7gXsJQ | 390,622 | 2020-05-22 | 8:17 | backup-power-stations | other:review | E10 E14 | none | 4.89x |
| 31 | Ecoflow Delta PRO 3 with 120 & 240v BUILT IN!  4000 Watt Solar Generator | YlJk9Ua9lSM | 369,970 | 2024-06-25 | 5:11 | backup-power-stations | other:review | E5 E10 | none | 4.64x |
| 32 | BIG POWER! 5100Wh Bluetti EP500 Battery Generator TEST & Review | WSB3bnoe7tY | 368,375 | 2021-03-25 | 7:26 | backup-power-stations | other:review | E10 E5 | none | 4.62x |
| 33 | BIG BOY Honda EU7000is 7000 Watt Bluetooth Generator Review | OzKWqf1b0to | 365,450 | 2021-02-27 | 7:43 | generators-backfeed | other:review | E10 E5 | none | 4.58x |
| 34 | Waterproof 1000 Watt Battery Generator CHEAP & Solar Power Station - Montek X-1000 Review | j711uxbw5ow | 352,679 | 2020-12-20 | 8:31 | backup-power-stations | other:review | E3 E10 | none | 4.42x |
| 35 | BEST Generator Cord is the One you Can Make Yourself | OVpKizAQLr4 | 350,660 | 2022-02-07 | 6:29 | generators-backfeed | how-to | E13 E3 E8 | maker / shelf | 4.39x |
| 36 | BIGGEST 2000 WATT Bluetti AC200 Battery Generator & Solar Power Station | Gm-SoM_whkE | 342,787 | 2020-07-01 | 5:49 | backup-power-stations | other:review | E10 E5 | none | 4.3x |
| 37 | ULTIMATE Home Generator just got BIGGER with 240V \| Ecoflow Delta Pro ULTRA | 2K9mlryo8lI | 334,737 | 2024-01-09 | 8:22 | backup-power-stations | other:review | E5 E10 | none | 4.19x |
| 38 | How to Strip Electrical Wire like a Pro 6 Ways | d8O57J1d2o4 | 327,620 | 2018-12-22 | 6:37 | connectors | how-to | E9 E10 E13 | own habit | 4.11x |
| 39 | Westinghouse Dual Fuel Propane Generator iGEN4500DF | er9TmHg7QMw | 319,409 | 2019-11-03 | 6:25 | generators-backfeed | other:review | E5 E10 | none | 4.0x |
| 40 | BIG Backup Power Small Price - Pecron E3000 Solar Generator Review | EcZ6iX_kOGo | 319,274 | 2022-01-27 | 5:22 | backup-power-stations | other:review | E3 E5 | none | 4.0x |
| 41 | INSTANT Lightswitch installs ANYWHERE | L9G21_0Jpzs | 310,083 | 2023-01-31 | 10:40 | outlets-switches | how-to | E13 E8 E10 | none | 3.89x |
| 42 | How to Fix Damaged Buried Electric Wire - Cheap & Easy | 4xopIgWVcPM | 308,039 | 2022-01-19 | 5:26 | connectors | how-to | E13 E8 E4 | none | 3.86x |
| 43 | If Your Circuit Breaker Makes a Buzzing Sound 🔥 Fix It Quick! | UxXtfFfMzRA | 307,331 | 2023-01-01 | 5:32 | breakers-panels | how-to | E4 E17 E5 | none | 3.85x |
| 44 | Better than GAS Generator? First 240V Battery Backup - Anker SOLIX F3800 | PKNENRY26Og | 293,250 | 2023-10-11 | 5:08 | backup-power-stations | other:review | E5 E10 | none | 3.67x |
| 45 | Don't Buy a Rooftop Solar System Before Seeing my Disaster | Roz9OXl5uEU | 277,080 | 2023-04-02 | 11:43 | solar | story | E1 E3 E4 | company | 3.47x |
| 46 | PLUG & PLAY SOLAR FOR OFF-GRID & VANLIFE - ECOFLOW Modular POWER KIT REVIEW | ZN2H_I37RUg | 264,855 | 2022-07-08 | 12:48 | solar | other:review | E13 E10 | none | 3.32x |
| 47 | What Ecoflow Delta Pro Battery Generator is the Best Value? | 5o_RVXnk2J8 | 261,296 | 2024-08-17 | 6:54 | backup-power-stations | x-vs-y | E3 E10 | none | 3.27x |
| 48 | How to get Wifi in the woods - DIY Solar Internet Station | tXf8opZCQdk | 240,255 | 2023-07-23 | 8:47 | solar | how-to | E13 E8 | none | 3.01x |
| 49 | Easy BACKUP POWER - Ecoflow River 2 First Look | YlQKePD6jl8 | 209,196 | 2022-12-23 | 5:29 | backup-power-stations | other:review | E5 E10 | none | 2.62x |
| 50 | Milwaukee FAILED Attempt at a Generator Carry-On MX-Fuel Battery Power Station | gFwP-0oQwMY | 208,097 | 2021-02-13 | 6:45 | backup-power-stations | other:review | E3 E12 | maker / shelf | 2.61x |
| 51 | AUTOMATIC Battery Backup for your ENTIRE HOUSE! - Ecoflow Smart Home Panel | UfxsvqbeO84 | 201,716 | 2022-06-28 | 5:47 | backup-power-stations | other:review | E5 E14 E13 | none | 2.53x |
| 52 | TESTING the BEST CAMPING GENERATORS for $299 - EcoFlow RIVER & Jackery 300 | z2M0CVzs5xM | 163,370 | 2021-05-23 | 5:30 | backup-power-stations | x-vs-y | E10 E13 | none | 2.05x |
| 53 | STEALTH GENERATOR $999 - LEOCH 2048 Next Generation Battery Power Station 2000 Watts! Review | Jc4-SYH5IW4 | 156,831 | 2020-11-15 | 5:27 | backup-power-stations | other:review | E10 | none | 1.97x |
| 54 | Cheapest 240V Whole House Battery Generator - ANKER SOLIX F3800 & Home Power Panel | tYEuYB8FGDA | 150,394 | 2024-03-27 | 6:11 | backup-power-stations | other:review | E5 E3 | none | 1.88x |
| 55 | Electric Panel Full?  Try This Simple Fix | s0aRduXcUKs | 147,925 | 2023-01-15 | 7:34 | breakers-panels | cheap-hack | E2 E13 E10 | upsell | 1.85x |
| 56 | ANKER 521 Power Station- CHEAPEST Lithium IRON Phosphate! LiFePO4 | SWhM_ZjzUX4 | 140,825 | 2021-11-29 | 5:31 | backup-power-stations | other:review | E10 | none | 1.76x |
| 57 | Bluetti EB70 vs Ecoflow River Pro - Which is Better? | paYfM8Ni_jk | 131,944 | 2021-04-30 | 7:04 | backup-power-stations | x-vs-y | E10 E3 | none | 1.65x |
| 58 | What can a Battery/Solar Generator Run? | 7hVFM8U2hWk | 125,044 | 2021-06-16 | 5:02 | backup-power-stations | other:review | E10 E5 | none | 1.57x |
| 59 | New MONSTER Jackery 3000 Watt Solar Generator - Explorer 3000 Pro | 4FDXXrpeyQw | 122,632 | 2023-03-28 | 8:51 | backup-power-stations | other:review | E10 | none | 1.54x |
| 60 | Honda Generator Oil Change - Honda EU7000 How To | j7QChedMD9U | 118,403 | 2017-12-26 | 11:05 | generators-backfeed | how-to | E13 | none | 1.48x |
| 61 | How to CONNECT Solar & Battery Generators to Circuit Breakers | _-fc2gb1kmA | 109,359 | 2020-11-24 | 5:53 | backup-power-stations | how-to | E13 E5 E17 | none | 1.37x |
| 62 | Reviewing a 1965 Honda Generator | UBblPogHqvk | 109,314 | 2021-03-06 | 6:54 | generators-backfeed | story | E15 E10 | none | 1.37x |
| 63 | Wago Gelbox - Instant Waterproof High Voltage Connections | caT0JBkiGm8 | 109,288 | 2023-11-20 | 5:41 | connectors | other:review | E13 E8 E10 | none | 1.37x |
| 64 | TESLA Powerwall Alternative - WATTS Battery Power Array & Solar Generator | VM6HfDC0LGk | 108,972 | 2021-04-11 | 5:39 | backup-power-stations | other:review | E3 E13 E10 | maker / shelf | 1.37x |
| 65 | Desktop Sized Power Station - Ecoflow River Mini Review | FNWKrxfzVJU | 104,717 | 2021-10-29 | 5:19 | backup-power-stations | other:review | E10 | none | 1.31x |
| 66 | PORTABLE PROPANE Dual Fuel GENERATOR 2000 Watt - Pulsar Review | DuDNPiKYlw8 | 102,175 | 2023-04-10 | 6:36 | generators-backfeed | other:review | E13 E5 | none | 1.28x |
| 67 | Yamaha Inverter Generator EF2000is V2 Review 2000 Watt - Portable Generator | 2-AhUNRSXBk | 97,631 | 2018-09-23 | 7:20 | generators-backfeed | other:review | E10 | none | 1.22x |
| 68 | Most Powerful USB Outlet you can buy that won't burn your house down - Leviton 60 Watt | Zbq5pBaXWOc | 97,318 | 2023-10-22 | 7:10 | outlets-switches | other:review | E17 E16 E10 | maker / shelf | 1.22x |
| 69 | How Safe are DREO Electric Space Heaters? | ZJQjKOnbLKU | 94,700 | 2025-01-07 | 5:27 | space-heaters | test | E17 E16 E14 | maker / shelf | 1.19x |
| 70 | ANKER SOLIX F3800+ 120v/240v - In Depth Review & Test - Big Update! | rBCmecPQ0qg | 90,924 | 2025-04-02 | 8:14 | backup-power-stations | other:review | E10 E12 | none | 1.14x |
| 71 | Testing Amazon's Cheapest Generator | BdW_a9SIUIM | 83,876 | 2023-12-30 | 5:27 | generators-backfeed | test | E3 E10 | maker / shelf | 1.05x |
| 72 | Finally a Power Station that Can Outlive GAS Generators - Anker SOLIX S2000 | iyQk6K8ABlw | 80,878 | 2026-05-26 | 6:26 | backup-power-stations | other:review | E10 E14 | none | 1.01x |
| 73 | Installing My BIGGEST Battery Backup System Yet! (62kWh EcoFlow DPUX) | VuQwtq7v0pk | 78,736 | 2026-08-03 | 11:01 | backup-power-stations | story | E5 E13 E10 | none | 0.99x |
| 74 | EcoFlow Just Made Whole House Backup WAY More Affordable! ALL NEW TITAN | XJdrUmHkjIs | 76,904 | 2026-10-13 | 9:32 | backup-power-stations | other:review | E5 E10 E14 | none | 0.96x |
| 75 | Honda EU7000is Generator Oil Change / Spark Plug Replacement & Air Cleaner | W6TWKPX5oXM | 76,118 | 2018-11-18 | 27:49 | generators-backfeed | how-to | E13 | none | 0.95x |
| 76 | ULTIMATE Home Generator Reinvented - ECOFLOW Delta 2 | PwCwlDkTggE | 75,695 | 2022-09-17 | 5:21 | backup-power-stations | other:review | E10 E5 | none | 0.95x |
| 77 | RUGGED Klein Tools Power Station for Electricians & Pros - KTB1000 | aOZBV_U5ddc | 74,577 | 2021-11-17 | 5:16 | backup-power-stations | other:review | E13 E10 | none | 0.93x |
| 78 | Which 240V Power Station Is the Best? Ecoflow Delta Pro 3 or Anker Solix F3800 Plus | UvGZzlLEU90 | 73,696 | 2025-07-23 | 6:07 | backup-power-stations | x-vs-y | E10 E3 | none | 0.92x |
| 79 | Best Budget Inverter Generator - Champion 2000watt | _i0xLiOhNRg | 73,359 | 2019-11-09 | 6:09 | generators-backfeed | other:review | E3 E10 | none | 0.92x |
| 80 | Ecoflow just made a Battery MORE Powerful than 90% of Gas Generators - Ultra X | n3JOHMlrQQQ | 65,108 | 2025-10-31 | 6:39 | backup-power-stations | other:review | E10 E5 | none | 0.82x |
| 81 | NO CABLES! INERGY FLEX 1500 Modular Solar Generator REVIEW | sn7V9dTq30A | 59,226 | 2022-03-26 | 6:09 | backup-power-stations | other:review | E5 E10 | none | 0.74x |
| 82 | First Whole-House WEATHERPROOF 240V Power Backup Station - Anker SOLIX E10 | feHQ4g72DZc | 57,352 | 2026-02-03 | 9:11 | backup-power-stations | other:review | E5 E10 | none | 0.72x |
| 83 | MOST RUGGED Power Station in the WORLD! 10,000 Watts - Hybrid Power Solutions Review | mzd9vJ_3Pzc | 57,264 | 2024-01-25 | 5:29 | backup-power-stations | other:review | E10 | none | 0.72x |
| 84 | GENERARK Home Power 2 Power Generator Review | XoM3fdZAvis | 55,387 | 2021-06-21 | 5:05 | backup-power-stations | other:review | E5 E10 | none | 0.69x |
| 85 | You will be SHOCKED at what a 1000 Watt Generator Can Run | _iwtjBK1TTE | 54,345 | 2018-12-29 | 5:42 | generators-backfeed | test | E10 E8 | none | 0.68x |
| 86 | Ecoflow Recession Buster $615 Delta 3 Plus Power Station | jOdz-E94uYQ | 53,445 | 2024-10-09 | 6:37 | backup-power-stations | other:review | E10 E3 | none | 0.67x |
| 87 | SUNGZU 1000 Watt Battery Generator & Solar Power Station | 34wHS7eHhoU | 52,608 | 2020-07-21 | 5:05 | backup-power-stations | other:review | E3 E10 | none | 0.66x |
| 88 | Yoshino B2000 SST Power Station | sLP7jMeGgvg | 49,208 | 2023-09-25 | 5:32 | backup-power-stations | other:review | E10 | none | 0.62x |
| 89 | The Truth About the Anker SOLIX S2000 - FULL TESTS Revealed | hd6tJMsJ1ac | 47,148 | 2026-06-24 | 6:15 | backup-power-stations | test | E10 E3 | none | 0.59x |
| 90 | Hands On with the MOST Powerful Portable Solar Generator Anker Has Made - S5000 | K8F2R1gDSkg | 46,778 | 2026-10-09 | 7:12 | backup-power-stations | other:review | E5 E10 | none | 0.59x |
| 91 | Storm Prep: How to Power Your House with a Battery Almost Indefinitely - Anker SOLIX | IgeexSKIEOQ | 36,806 | 2025-06-27 | 6:20 | backup-power-stations | how-to | E5 E13 E16 | none | 0.46x |
| 92 | Yoshino INVESTIGATION - Are Their Solid State Batteries REAL? | WToukRDZjJo | 36,070 | 2024-10-14 | 6:20 | backup-power-stations | test | E3 E10 E12 | maker / shelf | 0.45x |
| 93 | Ecoflow DELTA 2 Max BEATS Gas Honda! Clean Power Solar Generator | 5oEB5CNs9xU | 34,879 | 2023-05-25 | 5:06 | backup-power-stations | x-vs-y | E10 E12 | none | 0.44x |
| 94 | Disaster Readiness WITHOUT GAS - How to Choose the RIGHT Battery Generator - Beginner's Guide | Z3C-b2OTEbA | 31,963 | 2023-09-15 | 9:51 | backup-power-stations | how-to | E5 E16 E10 | none | 0.4x |
| 95 | Unraveling the New Ecoflow DELTA 3 Series Ultra & Max Solar Power Generators | J7GY5q36IKY | 31,506 | 2025-09-29 | 6:04 | backup-power-stations | other:review | E10 | none | 0.39x |
| 96 | How to change a spark plug on a Honda generator | Rv2O5Eg8hR8 | 30,171 | 2017-12-22 | 11:52 | generators-backfeed | how-to | E13 | none | 0.38x |

## Short reference (under 5:00, not counted) (53)

Same columns; multiple uses the same long-form basis, for reference only.

| # | Title | ID | Views | Date | Length | Sub-niche | Format | Emotions | Villain | Multiple |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | What Happens When You Plug a SUICIDE CORD in a LIVE OUTLET? Do Not Try This Ever | H-4mvK2FW78 | 11,640,927 | 2022-09-20 | 2:42 | cords-strips-surge | test | E17 E10 E18 | maker / shelf | 145.86x |
| 2 | Why Do Electric Plugs Have Holes? Answered | Db-dt5U3MCc | 8,646,225 | 2021-02-06 | 3:17 | electrical-explainer | other:explainer | E10 E17 | none | 108.34x |
| 3 | What REALLY HAPPENS WHEN YOU SPILL WATER in an OUTLET? | 1tfvtJyucHc | 7,414,841 | 2021-05-01 | 4:21 | outlets-switches | test | E17 E10 E16 | none | 92.91x |
| 4 | Never use Wire Nuts Again - Wago is Better Electrical Connector | rMlI7qOm8hM | 5,966,495 | 2021-01-17 | 3:54 | connectors | x-vs-y | E12 E13 E3 | maker / shelf | 74.76x |
| 5 | Never Solder Again - How to Connect Wires the EASY Way | NZtwD_F7lTA | 4,474,145 | 2021-03-28 | 4:25 | connectors | cheap-hack | E13 E10 E8 | none | 56.06x |
| 6 | Why 50% of All Crimp Connections Fail - Up or Down? | U9ZQ96hbmIY | 4,297,620 | 2024-03-09 | 4:57 | connectors | mistakes | E9 E10 E6 | own habit | 53.85x |
| 7 | #1 DIY Electric Mistake - Can you use Romex Wire in Conduit? | PZFJkXfThUg | 2,720,570 | 2024-03-31 | 3:44 | wiring-mistakes | mistakes | E18 E9 E10 | own habit | 34.09x |
| 8 | Worst Electrical Mistake You Can Make - Backfeeding Generators | 9kjpS1vfGio | 2,371,256 | 2022-02-10 | 4:15 | generators-backfeed | mistakes | E17 E16 E18 | own habit | 29.71x |
| 9 | Lightswitch So GOOD They Made it ILLEGAL | y59h-9rXALY | 2,119,351 | 2022-10-03 | 3:51 | outlets-switches | dont-want-you | E18 E15 E10 | none | 26.56x |
| 10 | Homeowners are Destroying Generators Skipping 1 Step During a Power Outage | sX442FodiT4 | 1,695,017 | 2025-01-28 | 4:07 | generators-backfeed | mistakes | E9 E1 E5 | own habit | 21.24x |
| 11 | STOP Connecting Stranded Wire Like an Animal - Do it LIKE A PRO! | u9jJqSGMB5g | 1,600,837 | 2021-04-24 | 3:39 | connectors | mistakes | E9 E13 E10 | own habit | 20.06x |
| 12 | Sneaky Reason LED Bulbs are Dying Faster than Advertised | dVjg_BK3G3s | 1,332,557 | 2024-11-11 | 3:29 | lighting-led | dont-want-you | E3 E10 E12 | maker / shelf | 16.7x |
| 13 | Testing the Cheapest Harbor Freight Generator $99 Tailgator | ehkIA38Zm2s | 1,225,584 | 2020-12-16 | 4:45 | generators-backfeed | test | E3 E10 | maker / shelf | 15.36x |
| 14 | Most ILLEGAL CAMERA OUTLET you will never See | UToWV2ZN9h4 | 1,098,898 | 2022-11-27 | 4:39 | outlets-switches | test | E18 E10 E16 | none | 13.77x |
| 15 | How to Connect a Small Generator to Your House - Safe & Legal - Run Heat, Fridge & More! | ydRveyXkf4M | 1,021,421 | 2018-11-13 | 4:18 | generators-backfeed | how-to | E5 E13 E18 | none | 12.8x |
| 16 | How to Fix Flickering Lights in Your House - Blinking - Flashing | atPvvDDE4OM | 865,756 | 2018-03-25 | 4:32 | lighting-led | how-to | E6 E4 E13 | none | 10.85x |
| 17 | EASY WAY to CLEAN a Dryer Vent FAST! | Pe-L2pbQjoY | 842,811 | 2022-06-19 | 2:53 | dryer-vents | how-to | E8 E13 E17 | none | 10.56x |
| 18 | New Wago Electric Connector is SHOCKING everyone - Inline 221 has arrived! | heyEr8agVFA | 824,573 | 2023-03-21 | 4:20 | connectors | other:review | E10 E13 | none | 10.33x |
| 19 | How to Replace a GFCI Outlet - Not Working? | CpCoOoTRIQ0 | 591,887 | 2021-09-25 | 4:16 | gfci-afci | how-to | E6 E13 | none | 7.42x |
| 20 | END of GAS Generators? Milwaukee MX Fuel Carry-On Changes EVERYTHING 3600 Watts! | Yie1zCVx7Yk | 570,976 | 2021-01-24 | 4:29 | backup-power-stations | other:review | E10 E12 | none | 7.15x |
| 21 | WORST MISTAKE Homeowners make upgrading a 15AMP to 20AMP Circuit Breaker | iNE3txnyjLk | 518,705 | 2022-09-12 | 3:30 | breakers-panels | mistakes | E17 E9 E18 | own habit | 6.5x |
| 22 | AC Polarity Explained - Electricity 101 | d6Eq2KRtE90 | 500,432 | 2021-03-01 | 4:22 | electrical-explainer | other:explainer | E10 E17 | none | 6.27x |
| 23 | Harbor Freight is going after Wago! But is their Electric Connector any Good? | Nr7ai7cDgxI | 400,175 | 2024-10-13 | 4:31 | connectors | x-vs-y | E3 E10 | none | 5.01x |
| 24 | Foot Pedal & Hand Crank Generators - K-TOR Pocket Socket & Power Box 50 | WQSKPGmy0v0 | 328,489 | 2021-01-30 | 4:48 | backup-power-stations | test | E10 E5 | none | 4.12x |
| 25 | How to Turn 2 Outlets Into 4 - Leviton QUADRAPLEX | T5QLSZCyPak | 294,167 | 2023-05-28 | 3:28 | outlets-switches | cheap-hack | E10 E13 | none | 3.69x |
| 26 | ECOFLOW SMART HYBRID GAS GENERATOR | uNXsC_592kI | 281,060 | 2021-08-28 | 4:13 | generators-backfeed | other:review | E10 | none | 3.52x |
| 27 | Deadly Outlet Hack House Flippers Are Scamming Buyers With | BYvM8hkO_-E | 277,966 | 2025-01-05 | 4:44 | wiring-mistakes | mistakes | E17 E18 E4 | last owner / flipper | 3.48x |
| 28 | The "Deadly" Bubble Christmas Light Explained | NEsMHTgXf54 | 275,073 | 2024-12-15 | 4:56 | holiday-lights | myth-bust | E17 E15 E12 | none | 3.45x |
| 29 | WORST Electric Connection Made Easy STRANDED & SOLID Wire | wPUkj4hYIEk | 260,607 | 2022-02-26 | 4:24 | connectors | how-to | E13 E10 | none | 3.27x |
| 30 | Now I Understand Why Costco is Selling Out of These Power Stations | FcXPl3aOxHY | 231,849 | 2025-06-09 | 4:09 | backup-power-stations | other:review | E10 E3 | none | 2.91x |
| 31 | How to Get some FREE WAGOS Samples | KWBx5BFtQ0o | 164,462 | 2023-04-23 | 2:20 | connectors | cheap-hack | E13 | none | 2.06x |
| 32 | 3 AMAZING Light Bulbs You Never Knew Existed | KSpaznsOwb0 | 149,751 | 2021-10-25 | 3:34 | lighting-led | other:review | E10 E5 | none | 1.88x |
| 33 | Anker's FIRST Whole House Power Backup - SOLIX X1 Overview & Teardown | xJR_P9CKrtU | 142,051 | 2024-06-13 | 4:24 | backup-power-stations | other:review | E5 E10 | none | 1.78x |
| 34 | Generator Interlock - Using it & Connecting a Generator to your House | F5fP7biZ2aQ | 117,497 | 2018-11-14 | 4:44 | generators-backfeed | how-to | E13 E5 E18 | none | 1.47x |
| 35 | Jackery 1800 WATT Battery & Solar Generator - Jackery Explorer 1500 Review | bbRKmJkhvKs | 117,346 | 2021-04-12 | 4:47 | backup-power-stations | other:review | E5 E10 | none | 1.47x |
| 36 | Ecoflow River 3 is SHOCKINGLY Affordable with Big Power Features | FGyQKYyqtaQ | 113,479 | 2024-09-25 | 3:30 | backup-power-stations | other:review | E10 E3 | none | 1.42x |
| 37 | What REALLY HAPPENS when you Install OUTLETS UPSIDE DOWN | X3J3XwC2vhk | 95,052 | 2023-11-19 | 3:57 | outlets-switches | myth-bust | E12 E17 E10 | none | 1.19x |
| 38 | How to Fix a Loose Outlet In 2 Minutes - No Tools | D8Dpwbl5PBw | 86,025 | 2025-08-10 | 3:12 | outlets-switches | cheap-hack | E13 E8 E2 | none | 1.08x |
| 39 | Clash of the Titans - Anker Solix F3000 vs Ecoflow Delta Pro Power Stations | OsJ7QPSl6JE | 85,868 | 2025-07-07 | 4:55 | backup-power-stations | x-vs-y | E10 | none | 1.08x |
| 40 | ANKER 500 Watt Lithium Iron Phosphate Mini Power Station 535 | JkJyBHvgJZA | 79,650 | 2022-03-10 | 3:53 | backup-power-stations | other:review | E10 | none | 1.0x |
| 41 | Best Deal 3500 Watt Inverter RV / Home Generator Review - Tomahawk | Eu9YRCR4yro | 77,392 | 2019-11-24 | 4:17 | generators-backfeed | other:review | E10 E3 | none | 0.97x |
| 42 | Mini Solar Power Station Kit with LED Lights VERY COOL - LiFePo4 | uOh6NrzUsJU | 77,003 | 2020-10-23 | 3:41 | solar | other:review | E3 E13 | none | 0.96x |
| 43 | Honda Generator Running in Hurricane LIVE for 5 days on Backup Power EU7000is | zHfIqAiUM-s | 76,295 | 2018-03-04 | 1:44 | generators-backfeed | story | E5 E14 | none | 0.96x |
| 44 | 1400 Watt Solar Power Station - ECOFLOW DELTA MINI | NrjHxU7XcTQ | 74,908 | 2021-10-02 | 4:24 | backup-power-stations | other:review | E10 | none | 0.94x |
| 45 | You Won’t Believe These Yard Lights Are Solar Powered | eLc3eUOsNWU | 61,623 | 2025-07-18 | 3:43 | lighting-led | other:review | E8 E10 | none | 0.77x |
| 46 | The Best Electric Box is the type you have never heard of | _BkYht1CwDo | 53,531 | 2025-03-12 | 4:49 | outlets-switches | x-vs-y | E10 E3 | none | 0.67x |
| 47 | UNIVERSAL BATTERY CHARGER - Hulkman Sigma 5 Charger & Maintainer | n7Nd4M8I-jg | 45,947 | 2022-04-02 | 3:52 | batteries-lithium | other:review | E13 E10 | none | 0.58x |
| 48 | BIG Jackery 2200 Watts! Explorer Pro 2000 Battery Generator & Power Station | YqIAsyujHa8 | 45,175 | 2022-05-20 | 4:57 | backup-power-stations | other:review | E10 | none | 0.57x |
| 49 | Best Kept Secret for Staying Warm When the Power is Out | SIyntnwE7O8 | 43,932 | 2021-12-15 | 4:18 | storms-outages | cheap-hack | E5 E10 E16 | none | 0.55x |
| 50 | LIGHTEST SOLAR PANEL in the WORLD! Carbon Fiber uLeaf Canada | SuS2sJfwVec | 38,561 | 2022-01-15 | 4:07 | solar | other:review | E10 | none | 0.48x |
| 51 | How Long Can a Single Power Station Run a Fridge? | GmOOH_JPKpo | 35,603 | 2025-12-29 | 3:59 | backup-power-stations | test | E5 E10 E14 | none | 0.45x |
| 52 | How to CERAMIC COAT your Solar Panels | QZqAwG-azMU | 31,997 | 2022-03-17 | 3:42 | solar | how-to | E13 E10 | none | 0.4x |
| 53 | Ecoflow vs Jackery - Which 240V Power Station is the BEST DEAL? DeltaPro 3 or HomePower 3600 Pro Max | crWFk9Da9_4 | 28,192 | 2026-08-20 | 4:56 | backup-power-stations | x-vs-y | E10 E3 | none | 0.35x |

## Counts by sub-niche (long-form only)

| subniche | Videos | Median views | Median multiple | Share at 2x+ |
|---|---|---|---|---|
| backup-power-stations | 52 | 123,838 | 1.56x | 21/52 (40%) |
| generators-backfeed | 21 | 350,660 | 4.39x | 12/21 (57%) |
| outlets-switches | 6 | 464,179 | 5.81x | 5/6 (83%) |
| connectors | 5 | 327,620 | 4.11x | 4/5 (80%) |
| solar | 4 | 270,967 | 3.40x | 4/4 (100%) |
| breakers-panels | 3 | 307,331 | 3.85x | 2/3 (67%) |
| wiring-mistakes | 1 | 4,486,163 | 56.21x | 1/1 (100%) |
| other:electric-shower-head | 1 | 1,103,433 | 13.83x | 1/1 (100%) |
| lighting-led | 1 | 490,104 | 6.14x | 1/1 (100%) |
| electrical-explainer | 1 | 424,465 | 5.32x | 1/1 (100%) |
| space-heaters | 1 | 94,700 | 1.19x | 0/1 (0%) |

## Counts by format (long-form only)

| format | Videos | Median views | Median multiple | Share at 2x+ |
|---|---|---|---|---|
| other:review | 54 | 179,273 | 2.25x | 27/54 (50%) |
| how-to | 20 | 318,851 | 4.00x | 14/20 (70%) |
| x-vs-y | 8 | 212,333 | 2.66x | 5/8 (62%) |
| test | 7 | 83,876 | 1.05x | 2/7 (29%) |
| story | 3 | 109,314 | 1.37x | 1/3 (33%) |
| cheap-hack | 2 | 676,661 | 8.47x | 1/2 (50%) |
| mistakes | 1 | 4,486,163 | 56.21x | 1/1 (100%) |
| dont-want-you | 1 | 424,465 | 5.32x | 1/1 (100%) |

## Counts by sub-niche, short reference (under 5:00, not counted)

| subniche | Videos | Median views | Median multiple | Share at 2x+ |
|---|---|---|---|---|
| backup-power-stations | 12 | 99,673 | 1.25x | 3/12 (25%) |
| connectors | 8 | 1,212,705 | 15.20x | 8/8 (100%) |
| generators-backfeed | 8 | 651,240 | 8.16x | 5/8 (62%) |
| outlets-switches | 7 | 294,167 | 3.69x | 4/7 (57%) |
| lighting-led | 4 | 507,753 | 6.37x | 2/4 (50%) |
| solar | 3 | 38,561 | 0.48x | 0/3 (0%) |
| electrical-explainer | 2 | 4,573,328 | 57.30x | 2/2 (100%) |
| wiring-mistakes | 2 | 1,499,268 | 18.79x | 2/2 (100%) |
| cords-strips-surge | 1 | 11,640,927 | 145.86x | 1/1 (100%) |
| dryer-vents | 1 | 842,811 | 10.56x | 1/1 (100%) |
| gfci-afci | 1 | 591,887 | 7.42x | 1/1 (100%) |
| breakers-panels | 1 | 518,705 | 6.50x | 1/1 (100%) |
| holiday-lights | 1 | 275,073 | 3.45x | 1/1 (100%) |
| batteries-lithium | 1 | 45,947 | 0.58x | 0/1 (0%) |
| storms-outages | 1 | 43,932 | 0.55x | 0/1 (0%) |

## Recent uploads (last 12 months, 2025-10-23 to 2026-10-23): is he still making electrical?

Exact dates (yt.py video). In the last 12 months he uploaded 18 long-form videos (Videos tab, all topics); **7 are in scope, and all 7 are power-station reviews** (EcoFlow / Anker), plus 2 under-5:00 power-station videos. **No wiring, outlet, breaker or connector video in the last 12 months.**

| Title | ID | Views | Date | Length | Multiple |
|---|---|---|---|---|---|
| EcoFlow Just Made Whole House Backup WAY More Affordable! ALL NEW TITAN | XJdrUmHkjIs | 76,904 | 2026-10-13 | 9:32 | 0.96x |
| Hands On with the MOST Powerful Portable Solar Generator Anker Has Made - S5000 | K8F2R1gDSkg | 46,778 | 2026-10-09 | 7:12 | 0.59x |
| Ecoflow vs Jackery - Which 240V Power Station is the BEST DEAL? DeltaPro 3 or HomePower 3600 Pro Max | crWFk9Da9_4 | 28,192 | 2026-08-20 | 4:56 (short ref) | 0.35x |
| Installing My BIGGEST Battery Backup System Yet! (62kWh EcoFlow DPUX) | VuQwtq7v0pk | 78,736 | 2026-08-03 | 11:01 | 0.99x |
| The Truth About the Anker SOLIX S2000 - FULL TESTS Revealed | hd6tJMsJ1ac | 47,148 | 2026-06-24 | 6:15 | 0.59x |
| Finally a Power Station that Can Outlive GAS Generators - Anker SOLIX S2000 | iyQk6K8ABlw | 80,878 | 2026-05-26 | 6:26 | 1.01x |
| First Whole-House WEATHERPROOF 240V Power Backup Station - Anker SOLIX E10 | feHQ4g72DZc | 57,352 | 2026-02-03 | 9:11 | 0.72x |
| How Long Can a Single Power Station Run a Fridge? | GmOOH_JPKpo | 35,603 | 2025-12-29 | 3:59 (short ref) | 0.45x |
| Ecoflow just made a Battery MORE Powerful than 90% of Gas Generators - Ultra X | n3JOHMlrQQQ | 65,108 | 2025-10-31 | 6:39 | 0.82x |

Median of the 7 recent in-scope long-form: **65,108 views (0.82x)**. Median of the 11 recent long-form NOT in scope: **330,010 views (4.14x)**, led by "Spray Foam is Expensive. Use THIS Instead!" (sHL4lBAhklA, 1,519,132) and "Mosquito Spraying is Expensive. Do This Instead!" (KLtlE41cTOI, 1,051,510). Measured.

My reading: the recent power-station videos are sponsored launches (description of XJdrUmHkjIs carries an EcoFlow early-bird link; NexLev get_channel_promotions lists EcoFlow and Jackery sponsorships, scraped 2026-08-21). They sit at or below his median; they look like sponsor income, not view drivers. His view drivers now are the "X is Expensive. Do THIS Instead!" money-saving format on other topics.

Most recent core-electrical uploads (any length):

| Title | ID | Views | Date | Length | Multiple |
|---|---|---|---|---|---|
| How To Install A 240V Outlet Start to Finish -  EV Car Charger - Welder 14-50 Explained | Yj_QUYuKgWw | 542,112 | 2025-09-14 | 17:43 | 6.79x |
| How to Fix a Loose Outlet In 2 Minutes - No Tools | D8Dpwbl5PBw | 86,025 | 2025-08-10 | 3:12 | 1.08x |
| You Won’t Believe These Yard Lights Are Solar Powered | eLc3eUOsNWU | 61,623 | 2025-07-18 | 3:43 | 0.77x |
| The Best Electric Box is the type you have never heard of | _BkYht1CwDo | 53,531 | 2025-03-12 | 4:49 | 0.67x |
| How Safe are DREO Electric Space Heaters? | ZJQjKOnbLKU | 94,700 | 2025-01-07 | 5:27 | 1.19x |
| Deadly Outlet Hack House Flippers Are Scamming Buyers With | BYvM8hkO_-E | 277,966 | 2025-01-05 | 4:44 | 3.48x |

The last core-electrical long-form video, "How To Install A 240V Outlet Start to Finish" (Yj_QUYuKgWw, 2025-09-14, 542,112 views, 17:43), did ~6.8x his current median, just outside the 12-month window. Measured.

## Borderline (not counted)

Views and length from the Videos-tab list page (rounded), 2026-10-23.

| Title | ID | Views (rounded) | Length | Why borderline |
|---|---|---|---|---|
| Not Sure You Can Still Call this an Air Duster - BIG Wolfbox First Look | W-iM-xNJj9E | 57,000 | 5:30 | Wolfbox cordless air duster (battery gadget); not electrical safety or home power |
| 9,000 Sold in 7 Days - Why is this NEW Wolfbox Duster is Going Viral | XFkcIlbX-R4 | 119,000 | 3:09 | Wolfbox cordless air duster (battery gadget) |
| Dust Bunnies HATE Me for Showing You This - WolfBox Duster | My79ZnAyrqY | 79,000 | 3:51 | Wolfbox cordless air duster (battery gadget) |
| Why this WolfBox Jumpstarter will NEVER leave your stranded | xgD05FuF3Xw | 105,000 | 7:16 | car jump starter (lithium pack); automotive, not home electrical |
| Why Jumpstarters are now leaving people stranded | 4SROjWwGVvo | 1,700,000 | 3:51 | car jump starters; automotive. Title shape ("Why X are now leaving people stranded") is worth noting |
| NEVER NEED JUMPER CABLES Again - Fanttik Apex T8 Digital Jump Starter | m7ttligefCo | 281,000 | 4:05 | car jump starter; automotive |
| First Look at the NEW ECOFLOW Glacier Classic & Wave 3 Portable AC | S8XO4wFhrPU | 117,000 | 6:06 | EcoFlow battery fridge + portable AC; cooling product that happens to be battery-powered |
| Ecoflow Wave 2 Solar Battery Powered Portable Air Conditioner Heater Review | yZavrHJsBAw | 163,000 | 7:33 | EcoFlow battery-powered portable AC/heater; cooling product |
| EcoFlow Wave PORTABLE Battery Powered Air Conditioner 4000 BTU | leEsPGaaru8 | 698,000 | 6:29 | EcoFlow battery-powered portable AC; cooling product |
| Starlink MINI In-Depth Setup & Review - Powered by Milwaukee Battery | DGoPeyKQhZQ | 406,000 | 7:46 | Starlink Mini powered by a Milwaukee battery; internet setup |
| The Secret to Outdoor Waterproof Ethernet Connections (Anyone Can Do This!) | TESgNqKAX5g | 45,000 | 5:45 | outdoor waterproof Ethernet connections; low-voltage data cable, not mains wiring |
| How to Run Fiber Optic Cable in Your Backyard - My 10 Gig Install for Starlink | pOKZlwB-lKQ | 426,000 | 7:03 | running fibre-optic cable in the yard; data cabling |
| BEST All in ONE SCREWDRIVER - Klein vs Milwaukee | pyXo3lUDx5U | 127,000 | 4:18 | Klein vs Milwaukee screwdriver; electrician's hand tool, no electrical topic |
| RUGGED eBIKE for BIG BOYS - Heybike Explore | pu29nmLsBKc | 104,000 | 6:12 | e-bike review; vehicle, no battery-safety angle |
| 25MPH Electric Bike looks like a REGULAR Bicycle - Vanpowers City Vanture | 2QXI2ViGTgw | 59,000 | 4:29 | e-bike review; vehicle, no battery-safety angle |
| Sold My Gas Yamaha TW200 Motorcycle for an Electric 2WD UBCO | 3oiBTaLPu_s | 321,000 | 5:49 | electric motorcycle; vehicle |
| How to Install a Kitchen Range Hood that VENTS OUTSIDE | zMSWKLvDFTc | 236,000 | 12:28 | kitchen range hood that vents outside; ventilation (could touch kitchen-grease / wiring; not watched) |
| How to PREVENT Pipes Freezing in your House or RV - HEAT TAPE | k8hK9duZIGo | 123,000 | 5:54 | electric heat tape on pipes; plumbing freeze topic |
| Make your BATHROOM FAN LIKE NEW without Attic Access | r31vJXrZD3Y | 275,000 | 5:43 | bathroom exhaust fan clean-up; appliance cleaning |
| What Happens When You get 6 Inches of RAIN IN ONE HOUR | z33lluiKg9I | 81,000 | 6:29 | 6 inches of rain in one hour; flooding, no outage angle in title |
| SURVIVING the Worst Snow Storm in 30 Years | OYM8aSESAY8 | 110,000 | 6:05 | surviving the worst snow storm in 30 years; storm, outage not named in title |
| Everyone will be buying pellet stoves after learning this news | 9d9TL02idO4 | 1,300,000 | 8:47 | pellet stoves; fuel heating (HVAC study) |
| How to Restore a WOOD STOVE the EASY WAY - Like New in Minutes | CRTh8fIhV5E | 334,000 | 5:39 | restoring a wood stove; fuel heating, fire-adjacent |
| How to Heat a Small shop with a BUILT IN Diesel Wall Heater | 3x5t4Zvkqms | 353,000 | 8:26 | diesel wall heater for a shop; fuel heating |
| Turn TRASH into FIRESTARTERS you can make yourself | 9bHTxnVeeXs | 47,000 | 3:50 | home-made firestarters; fire-making, not prevention |
| Dakota Fire Hole Backyward Smokeless Firepit - Done it in 30 Minutes EASY | 4uZuRNzvYMg | 29,000 | 9:03 | smokeless firepit; fire-making, not prevention |
| How to Store & Stabilize Gasoline for Super Long Periods of Time | KwfAEGZiE2I | 313,000 | 5:24 | storing / stabilising gasoline; generator fuel, no fire-safety angle in title |
| How to Winterize Lawnmowers & Generators in 1 Step | _Uc_NMJ8BNk | 33,000 | 2:59 | winterize lawnmowers & generators; thumbnail shows only a lawn mower |
| Verizon Fios Battery Replacement Free - Stop The Beeping Battery | YVPpruxt4yM | 111,000 | 2:40 | Verizon Fios backup battery replacement; telecom box battery |
| How to Replace a Car Battery | KtrmHkJmZ88 | 65,000 | 5:23 | replacing a car battery; automotive |
| DIY BACKYARD WELL with ELECTRIC PUMP - FREE Water | ybbEK482cg8 | 3,300,000 | 9:15 | DIY backyard well with electric pump; plumbing/water |

## Basis videos for the multiple (18 long-form, last 12 months, all topics)

| Title | ID | Views | Date | Length |
|---|---|---|---|---|
| EcoFlow Just Made Whole House Backup WAY More Affordable! ALL NEW TITAN | XJdrUmHkjIs | 76,904 | 2026-10-13 | 9:32 |
| Hands On with the MOST Powerful Portable Solar Generator Anker Has Made - S5000 | K8F2R1gDSkg | 46,778 | 2026-10-09 | 7:12 |
| Not Sure You Can Still Call this an Air Duster - BIG Wolfbox First Look | W-iM-xNJj9E | 57,990 | 2026-10-07 | 5:30 |
| Lawn Care is Expensive. Try THIS Instead! | VW_bhZt3IpM | 330,010 | 2026-09-13 | 5:25 |
| Spray Foam is Expensive. Use THIS Instead! | sHL4lBAhklA | 1,519,132 | 2026-08-30 | 5:34 |
| How to Install a Kitchen Range Hood that VENTS OUTSIDE | zMSWKLvDFTc | 236,038 | 2026-08-16 | 12:28 |
| The BEST Portable Air Conditioner Just Got BETTER for 2026 | OGVXmIZtEG8 | 65,273 | 2026-08-06 | 5:39 |
| Installing My BIGGEST Battery Backup System Yet! (62kWh EcoFlow DPUX) | VuQwtq7v0pk | 78,736 | 2026-08-03 | 11:01 |
| The Truth About the Anker SOLIX S2000 - FULL TESTS Revealed | hd6tJMsJ1ac | 47,148 | 2026-06-24 | 6:15 |
| First Robot Lawn Mower with a BUILT-IN String Trimmer - Worx Landroid Vision Cloud | ggxTdCjKBjI | 107,072 | 2026-06-15 | 10:53 |
| Lawn Care Just Got Easier - Why this new Fertilizer is a Home Run | rIMsBWXS7UE | 71,052 | 2026-05-31 | 5:05 |
| Finally a Power Station that Can Outlive GAS Generators - Anker SOLIX S2000 | iyQk6K8ABlw | 80,878 | 2026-05-26 | 6:26 |
| How I Stopped Getting Tick Bites Completely - Everything You NEED to Know | e2vsJxyGJtQ | 637,780 | 2026-05-24 | 12:15 |
| How to Make Your Garage Door SEAL TIGHT as a Fridge | EjLJm0g4whg | 906,215 | 2026-05-17 | 6:36 |
| Mosquito Spraying is Expensive.  Do This Instead! Honey Bee Safe Too | KLtlE41cTOI | 1,051,510 | 2026-04-19 | 6:45 |
| First Whole-House WEATHERPROOF 240V Power Backup Station - Anker SOLIX E10 | feHQ4g72DZc | 57,352 | 2026-02-03 | 9:11 |
| A Ridiculously Easy Way to Fix Your Tire Light (Dealers Hate This) | uitpUH742oE | 968,311 | 2026-02-01 | 5:38 |
| Ecoflow just made a Battery MORE Powerful than 90% of Gas Generators - Ultra X | n3JOHMlrQQQ | 65,108 | 2025-10-31 | 6:39 |

Sources: YT Videos tab (Latest 18 pages, Popular 3 pages) and YT watch page via `yt.py`, NexLev get_channel_analytics, check_faceless_channel, get_batch_channel_metrics_v2, get_channel_promotions, youtube_channel_about, youtube_video_details; all pulled 2026-10-23. Thumbnails: `thumbnails/images/<id>.jpg`. Row data: `data/silver-cymbal/seeds.csv`.
