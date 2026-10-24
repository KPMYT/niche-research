# Old-house heat: how big is the pool? (round 2, 2026-10-24)

> **Checker notes (2026-10-24, `check-round2.md`):** 0 mismatches in a 10-video sample. Outside it: the on-topic rule missed "How To Remove Air From Your Heating System" (`z80WspC4Nmg`, TheDIYGuyDOTnet, US, 2,050,577 views, 5:24, about 12 years old), which would be the #1 US video in the top 20 (the conclusions don't change; the tables are not yet re-run). Halden Row is probably "faceless, AI images" rather than a persona (no named character). The analysis scripts are now in `data/tools/oldheat/`.

**Question tested.** An earlier chat suggested Roger the HVAC Guy stand apart from the crowded AC / "retired HVAC pro" field (led by Ray Dutton's Garage) through "old-house heat": boilers, hot-water and steam radiators, steam heat, oil furnaces and oil boilers, baseboard hydronic heat and the winter heat bill. It warned that the pool "may be smaller than AC, so validate" (`findings/2026-10-22-hvac-and-electrical.md`, section 1). This file measures that pool and compares it with AC like for like.

**Short answer (measured):** the old-house heat pool is much smaller than AC. On 10 matched keywords per side, it has 135 kept videos against 315. Its median video has 26,413 views against 212,313 (AC is about 8x). In the last 12 months it has 2 videos at 100K+ against 72. The biggest old-house heat videos are mostly British central-heating videos. US old-house heat is held by on-camera working plumbers and heating techs. The faceless AI personas in this space all launched in 2025-2026 and get under about 1,100 views a video. My reading of what this means is in the last section.

NexLev RPM and revenue are not used anywhere in this file (operator decision "ignore nexlev rpm its wrong").

---

## 1. Method

- **Pulled:** 2026-10-24. YouTube searches 06:58-07:08 UTC; original titles 07:06-07:17; About panels 07:09-07:12; channel Videos tabs 07:09; upload dates about 07:20-07:28 (UTC timestamps are on every record in the raw file).
- **Search:** logged out, `hl=en&gl=US`, with `studies/hvac/data/tools/oldheat_search.py` (its `search()` is copied from `sweep_round2.py`). There are 2 result pages per search (often only the first page came back, as in the main sweep: 20-40 rows a search). Each keyword ran under 4 sorts: **relevance**, **views** (view count), **year** (view count, this year) and **month** (view count, this month). That makes 48 keywords x 4 sorts = 192 searches; 2 failed the first time and were re-run at 07:08 (circulator pump / views, old house heating cost / views). I did not read rows from the main session's `priority.jsonl`: when I started, its boiler/radiator/oil rows were not in it yet, so every row here comes from my own pull.
- **Old-house heat keywords (38):** how to bleed radiators; bleeding radiators old house; banging radiator; steam radiator banging; steam radiator not getting hot; steam radiator hissing; steam radiator air vent; one pipe steam system; steam heat; steam boiler maintenance; boiler pressure low; boiler pressure too high; boiler not firing; boiler no heat; old house boiler; boiler vs furnace; boiler replacement cost; boiler expansion tank; circulator pump; zone valve not working; hot water baseboard heat; hydronic heating; baseboard heat not working; cast iron radiators; radiator reflector; radiator covers; old house heating cost; oil furnace no heat; oil burner not firing; oil furnace maintenance; oil boiler; oil tank replacement; heating oil cost; heating oil vs gas; convert oil to gas; oil to heat pump; gravity furnace; octopus furnace.
- **Matched set for the AC comparison (10 a side).**
  - Old-house heat: how to bleed radiators, banging radiator, steam radiator not getting hot, boiler pressure low, boiler no heat, hot water baseboard heat, oil furnace maintenance, heating oil vs gas, old house heating cost, boiler vs furnace.
  - AC: ac not cooling, ac maintenance, ac capacitor, clean ac coils, ac filter, central ac cost, ac freezing up, thermostat settings summer, mini split install, best ac brands.
- **Filters**, in order:
  1. **Long-form:** length 5:00 or more.
  2. **English:** logged-out `hl=en` search **auto-translates foreign titles into English**. For example KlimaClemens's "Heizkörper gluckert? SO entlüftest du ihn richtig!" shows as "Radiator gurgling? How to bleed it properly!" (797,747 views). So I pulled each long-form video's original title from `youtube.com/oembed`, and kept a video only when the original title, the search title and the channel name all read as English (a script, accent and foreign-word check). Of 1,219 long-form heat videos, 82 had a translated title, and 34 of them would have passed as English on the search title alone. For AC the figures are 458, 27 and 15. *This affects any sweep that judges language from search titles.*
  3. **On topic:** title rules. For heat: radiators, boilers, steam heat, hydronic, hot-water baseboard, circulators, zone valves, boiler expansion tanks, oil furnaces, burners, boilers and tanks, heating oil, gravity and octopus furnaces, and old-house heating. Out: car and motorbike radiators, sleep-sound videos, industrial and power-plant boilers, waste-oil and off-grid DIY heaters, wood boilers, radiant floors and slabs, garage, shop and van heat, electric baseboard, water-heater expansion tanks, gaming and music. AC has the same kind of rules (car AC and electronics capacitors out). The full rules are in the raw file under `filters`. These are my rules, so treat the kept counts as **my classification**.
- **Country:** from each channel's About panel (448 channels pulled; "not stated" when the channel gives none).
- **Last 12 months:** the age text is in hours, days, weeks or months. YouTube shows 12 months and older as "1 year ago".
- **Views:** the full view counts in search results. **Check:** I re-pulled the top 20 heat videos through innertube `/next` at about 07:20-07:28. All 20 view counts were within 0.02% of the search figure (table in section 7).

### Funnel

| Set | Rows pulled | Distinct videos | Long-form | + English | + on topic (kept) |
|---|---|---|---|---|---|
| Old-house heat, 38 keywords | 2,844 | 1,982 | 1,219 | 1,107 | **380** |
| Old-house heat, matched 10 | 739 | 593 | 388 | 359 | **135** |
| AC, matched 10 | 919 | 669 | 458 | 407 | **315** |

Reading: about 1 in 3 long-form English results for heat keywords is actually about home heating (380 of 1,107). For AC it is 315 of 407. Heat searches pull in car radiators, waste-oil burners, industrial boilers and so on, and that alone says the home-heating supply per keyword is thinner.

---

## 2. The pool, and the AC comparison

| Set | Keywords | Videos | Channels | Median views | 75th pct | 90th pct | >=100K | >=1M | Last 12 mo: videos | Last 12 mo: median | Last 12 mo: >=100K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Old-house heat, all | 38 | 380 | 213 | 15,504 | 84,099 | 332,115 | 85 | 15 | 164 | 3,779 | 6 |
| Old-house heat, matched 10 | 10 | 135 | 83 | 26,413 | 213,544 | 930,473 | 45 | 14 | 58 | 6,196 | 2 |
| AC, matched 10 | 10 | 315 | 191 | 212,313 | 1,078,894 | 2,492,356 | 191 | 85 | 176 | 42,090 | 72 |
| Old-house heat, all - US-listed channels only |  | 222 | 102 | 12,839 | 50,447 | 220,810 | 39 | 3 | 107 | 5,845 | 1 |
| Old-house heat, matched 10 - US-listed channels only |  | 80 | 41 | 17,944 | 99,958 | 409,219 | 20 | 3 | 40 | 7,546 | 0 |
| AC, matched 10 - US-listed channels only |  | 193 | 103 | 308,456 | 1,366,610 | 2,512,093 | 129 | 58 | 88 | 31,160 | 39 |

Measured ratios, AC to old-house heat, matched 10:
- **Median views:** 212,313 / 26,413 = 8.0x (US-listed channels only: 308,456 / 17,944 = 17.2x).
- **Median views, last 12 months:** 42,090 / 6,196 = 6.8x (US-listed only: 31,160 / 7,546 = 4.1x).
- **Videos at 100K+:** 191 against 45. Over the last 12 months: **72 against 2.**

**Where the channels are (About panel, share of kept videos):**

| Set | Countries (videos, share) |
|---|---|
| Old-house heat, all 38 | United States 222 (58%); United Kingdom 84 (22%); not stated 58 (15%); Italy 4 (1%); Canada 4 (1%); Ireland 3 (1%) |
| Old-house heat, matched 10 | United States 80 (59%); United Kingdom 34 (25%); not stated 18 (13%); Lithuania 1; France 1; Ireland 1 |
| AC, matched 10 | United States 193 (61%); India 61 (19%); not stated 36 (11%); Canada 8 (3%); Pakistan 5 (2%); Indonesia 3 (1%) |

Both pools have about 60% US-listed videos. The non-US part is British on the heat side (combi boilers, panel radiators) and Indian on the AC side (split-AC buying guides). The "US-listed only" rows above are the fairer comparison for Roger's audience.

### Per keyword (all 48; "kept" = long-form, English, on topic, all 4 sorts merged)

| Side | Keyword | Rows pulled (4 sorts) | Distinct videos | Kept (long, English, on topic) | Channels | Median views | Top views | >=100K | Last 12 mo kept | Last 12 mo median |
|---|---|---|---|---|---|---|---|---|---|---|
| heat | banging radiator (matched) | 49 | 36 | 12 | 10 | 61,740 | 2,404,182 | 4 | 4 | 11,300 |
| heat | baseboard heat not working | 60 | 58 | 13 | 10 | 236,480 | 1,246,905 | 9 | 3 | 464 |
| heat | bleeding radiators old house | 47 | 34 | 12 | 9 | 740,527 | 2,404,182 | 10 | 2 | 486 |
| heat | boiler expansion tank | 80 | 73 | 21 | 14 | 8,593 | 2,283,663 | 4 | 14 | 6,540 |
| heat | boiler no heat (matched) | 80 | 69 | 28 | 17 | 26,078 | 2,479,340 | 10 | 16 | 15,474 |
| heat | boiler not firing | 73 | 61 | 18 | 14 | 14,344 | 1,150,095 | 5 | 10 | 8,114 |
| heat | boiler pressure low (matched) | 80 | 70 | 10 | 9 | 492,960 | 2,404,191 | 7 | 3 | 1,232 |
| heat | boiler pressure too high | 52 | 47 | 12 | 10 | 269,774 | 2,404,191 | 6 | 4 | 493 |
| heat | boiler replacement cost | 75 | 73 | 22 | 16 | 28,574 | 624,597 | 3 | 12 | 28,574 |
| heat | boiler vs furnace (matched) | 61 | 53 | 11 | 11 | 95,661 | 380,552 | 4 | 2 | 242 |
| heat | cast iron radiators | 74 | 63 | 12 | 12 | 14,464 | 930,473 | 5 | 5 | 6,053 |
| heat | circulator pump | 80 | 79 | 7 | 6 | 11,041 | 497,971 | 2 | 3 | 7,632 |
| heat | convert oil to gas | 76 | 75 | 8 | 8 | 10,966 | 343,511 | 1 | 0 | not found |
| heat | gravity furnace | 60 | 44 | 2 | 2 | 7,842 | 7,915 | 0 | 0 | not found |
| heat | heating oil cost | 160 | 124 | 9 | 9 | 9,188 | 343,511 | 1 | 8 | 5,830 |
| heat | heating oil vs gas (matched) | 112 | 97 | 7 | 7 | 10,807 | 343,511 | 1 | 4 | 2,268 |
| heat | hot water baseboard heat (matched) | 63 | 60 | 19 | 18 | 97,786 | 1,625,468 | 9 | 6 | 450 |
| heat | how to bleed radiators (matched) | 80 | 69 | 12 | 9 | 1,427,722 | 2,656,757 | 8 | 3 | 97 |
| heat | hydronic heating | 80 | 71 | 16 | 14 | 45,792 | 930,473 | 5 | 5 | 1,098 |
| heat | octopus furnace | 51 | 36 | 3 | 3 | 7,770 | 7,915 | 0 | 1 | 48 |
| heat | oil boiler | 88 | 78 | 17 | 13 | 27,229 | 2,283,663 | 4 | 11 | 4,509 |
| heat | oil burner not firing | 62 | 57 | 20 | 13 | 16,495 | 1,043,525 | 9 | 11 | 2,009 |
| heat | oil furnace maintenance (matched) | 80 | 72 | 31 | 13 | 16,163 | 1,043,525 | 6 | 17 | 8,170 |
| heat | oil furnace no heat | 62 | 59 | 19 | 10 | 30,549 | 1,043,525 | 8 | 5 | 12,519 |
| heat | oil tank replacement | 71 | 67 | 10 | 8 | 41,866 | 380,552 | 2 | 1 | 9,167 |
| heat | oil to heat pump | 92 | 77 | 11 | 8 | 68,289 | 922,523 | 4 | 7 | 68,289 |
| heat | old house boiler | 79 | 69 | 11 | 9 | 62,558 | 738,253 | 3 | 6 | 8,289 |
| heat | old house heating cost (matched) | 80 | 68 | 2 | 2 | 18,688 | 21,673 | 0 | 1 | 15,703 |
| heat | one pipe steam system | 54 | 44 | 24 | 17 | 38,214 | 536,527 | 5 | 8 | 3,722 |
| heat | radiator covers | 84 | 71 | 19 | 18 | 50,148 | 1,499,165 | 7 | 5 | 4,368 |
| heat | radiator reflector | 71 | 53 | 15 | 14 | 1,076 | 1,499,165 | 3 | 10 | 280 |
| heat | steam boiler maintenance | 80 | 75 | 26 | 11 | 23,388 | 821,099 | 6 | 14 | 6,412 |
| heat | steam heat | 160 | 98 | 3 | 2 | 13,791 | 117,642 | 1 | 2 | 10,536 |
| heat | steam radiator air vent | 80 | 69 | 34 | 29 | 1,530 | 1,608,538 | 7 | 17 | 82 |
| heat | steam radiator banging | 47 | 34 | 19 | 11 | 15,188 | 64,797 | 0 | 5 | 9,105 |
| heat | steam radiator hissing | 44 | 27 | 4 | 4 | 32,526 | 2,404,182 | 1 | 2 | 228 |
| heat | steam radiator not getting hot (matched) | 54 | 41 | 24 | 17 | 180,158 | 2,479,340 | 13 | 6 | 210 |
| heat | zone valve not working | 63 | 57 | 19 | 15 | 24,194 | 1,246,905 | 7 | 6 | 4,016 |
| ac | ac capacitor | 88 | 72 | 25 | 18 | 313,974 | 4,863,494 | 20 | 10 | 138,039 |
| ac | ac filter | 92 | 77 | 24 | 19 | 85,211 | 3,178,486 | 12 | 14 | 30,796 |
| ac | ac freezing up | 73 | 62 | 32 | 28 | 473,770 | 5,631,712 | 21 | 9 | 15,439 |
| ac | ac maintenance | 160 | 100 | 47 | 31 | 589,312 | 6,134,983 | 30 | 26 | 330,461 |
| ac | ac not cooling | 80 | 77 | 40 | 31 | 208,800 | 10,388,788 | 28 | 21 | 109,459 |
| ac | best ac brands | 104 | 77 | 48 | 28 | 477,143 | 10,772,005 | 31 | 30 | 106,526 |
| ac | central ac cost | 88 | 73 | 43 | 39 | 115,319 | 4,863,494 | 22 | 26 | 31,505 |
| ac | clean ac coils | 80 | 75 | 50 | 37 | 225,742 | 6,134,983 | 31 | 28 | 44,036 |
| ac | mini split install | 88 | 69 | 47 | 34 | 318,757 | 13,032,752 | 35 | 26 | 110,944 |
| ac | thermostat settings summer | 66 | 62 | 13 | 12 | 292,884 | 3,463,248 | 9 | 6 | 2,483 |

What I see in the per-keyword table (measured; the "why" is my reading):
- Several heat keywords have high medians on few videos: how to bleed radiators (12 kept, median 1,427,722), bleeding radiators old house (12, 740,527), boiler pressure low (10, 492,960). These rest on old UK videos (plumberparts, The DIY Guy, Allen Hart). Their last-12-month medians are 97, 486 and 1,232.
- **US old-house heat words are thin.** Steam heat gave 3 kept out of 98 distinct, gravity furnace 2 out of 44, octopus furnace 3 out of 36, old house heating cost 2 out of 68, heating oil vs gas 7 out of 97, convert oil to gas 8 out of 75.
- Every AC keyword except "thermostat settings summer" keeps 24-50 videos, with a last-12-month median of 15,439-330,461.

---

## 3. Top old-house heat videos (all 38 keywords, kept pool)

### Top 20 by views

| # | ID | Title | Channel | Country (About tab) | Views | Age | Length |
|---|---|---|---|---|---|---|---|
| 1 | `o2Y9elh24wc` | How to Change a Thermostatic Radiator Valve Without Draining The System | The DIY Guy | United Kingdom | 2,656,757 | 4y ago | 14:53 |
| 2 | `wqku_Rc_YuI` | How to Fix One Radiator Not Working - Plumbing Tips | plumberparts | United Kingdom | 2,479,340 | 15y ago | 5:54 |
| 3 | `tbLz8icLr2U` | How To Bleed A Radiator - Don’t try it until you watch this | Allen Hart | United Kingdom | 2,404,191 | 6y ago | 9:25 |
| 4 | `4meZgMAUecw` | BOILER KEEPS LOSING PRESSURE - WHY AND HOW TO FIX - Plumbing tips | plumberparts | United Kingdom | 2,283,663 | 10y ago | 9:13 |
| 5 | `7NsZ2d2Oups` | How to Balance Your Radiators / Save Money and Increase Heat | The DIY Guy | United Kingdom | 2,059,661 | 4y ago | 9:34 |
| 6 | `U2CY4rHr7nA` | How to Fix a Cold Radiator 4 Easy Ways / DIY Plumbing | The DIY Guy | United Kingdom | 1,949,546 | 3y ago | 11:52 |
| 7 | `wG-CqFr6FLM` | How to remove the air from your boiler / heater | askmediy | United States | 1,625,468 | 16y ago | 9:51 |
| 8 | `PAo6yG89vyM` | RADIATORS EXPLAINED How to fix balance bleed panel radiator How radiators work flow & return valves | How2D2 | United Kingdom | 1,608,538 | 6y ago | 8:17 |
| 9 | `0Oa5UBiZ6W0` | £15 Radiator Upgrades That Heat Your Room Fast! | The DIY Guy | United Kingdom | 1,499,165 | 9mo ago | 10:07 |
| 10 | `UR9wSU-I2O8` | Combi Boiler Too Much Pressure - How to reduce the water pressure - Central Heating | Allen Hart | United Kingdom | 1,412,130 | 7y ago | 8:08 |
| 11 | `UmfKzbsQxKE` | Radiator NOT Heating Up? Expert DIY Fixes | Skill Builder | United Kingdom | 1,246,905 | 8y ago | 9:35 |
| 12 | `voS7Url50M4` | Remove Air from your Boiler and Heating System / How To | Fix It With Zim | not stated | 1,153,868 | 7y ago | 16:25 |
| 13 | `Ftj67dIh1ZI` | Vaillant Ecotec Mk 1 - Resetting the boiler. | K. S. Engineering and Exeter City Council | not stated | 1,150,095 | 12y ago | 5:05 |
| 14 | `cog7MaShR7M` | Troubleshoot the oil furnace part 1. Burner won't start. | grayfurnaceman | United States | 1,043,525 | 12y ago | 6:21 |
| 15 | `TfPnLUz1Vh4` | Oil furnace troubleshoot part 2 No flame | grayfurnaceman | United States | 1,012,924 | 12y ago | 11:47 |
| 16 | `CGLAl6nGeo8` | How to Remove and Replace a Radiator For Decorating - No Draining Required! | The DIY Guy | United Kingdom | 930,473 | 2y ago | 11:19 |
| 17 | `kGs_biFA87Q` | Is It Better To Leave The Heating On Constantly? Boilers & Heat Pumps / Consumer Advice | Heat Geek | United Kingdom | 922,523 | 4y ago | 16:15 |
| 18 | `5GbXgEYw5TE` | Oil Heat 🔥 Boilers - How it works - Understand the Basics | Silver Cymbal | United States | 821,099 | 8y ago | 22:18 |
| 19 | `6t6QnYkXuXA` | VAILLANT ECOTEC BOILER. How to use, and change temperatures on the LCD display | Mark Ray | United Kingdom | 781,083 | 6y ago | 6:06 |
| 20 | `LyHy2En9iF0` | Troubleshoot the oil furnace part 3.  Fire comes on but shuts down. | grayfurnaceman | United States | 760,474 | 12y ago | 8:35 |

13 of the top 20 come from UK-listed channels, 5 from US-listed ones and 2 give no country (one is a Vaillant boiler, a UK brand). The only US videos in the top 20 are 7 to 16 years old: askmediy, grayfurnaceman's three oil-furnace troubleshooting videos (November 2013; corrected by the checker, 2012 is the year the channel joined) and Silver Cymbal's "Oil Heat Boilers" (8 years).

### Top 20, US-listed channels only

| # | ID | Title | Channel | Views | Age | Length |
|---|---|---|---|---|---|---|
| 1 | `wG-CqFr6FLM` | How to remove the air from your boiler / heater | askmediy | 1,625,468 | 16y ago | 9:51 |
| 2 | `cog7MaShR7M` | Troubleshoot the oil furnace part 1. Burner won't start. | grayfurnaceman | 1,043,525 | 12y ago | 6:21 |
| 3 | `TfPnLUz1Vh4` | Oil furnace troubleshoot part 2 No flame | grayfurnaceman | 1,012,924 | 12y ago | 11:47 |
| 4 | `5GbXgEYw5TE` | Oil Heat 🔥 Boilers - How it works - Understand the Basics | Silver Cymbal | 821,099 | 8y ago | 22:18 |
| 5 | `LyHy2En9iF0` | Troubleshoot the oil furnace part 3.  Fire comes on but shuts down. | grayfurnaceman | 760,474 | 12y ago | 8:35 |
| 6 | `gOZWyZMOASA` | How to Diagnose Problems with a Hot Water Heating System / Ask This Old House | This Old House | 738,253 | 9y ago | 7:29 |
| 7 | `es478xgCHEw` | How to Repair a Leaking Boiler Relief Valve Easy DIY | DIYeasycrafts | 624,597 | 10y ago | 7:04 |
| 8 | `3qNwCd8LO7k` | How to remove the air from your hot water heating system | Your Hunting Buddy | 612,283 | 13y ago | 9:47 |
| 9 | `HNnUO3-fj8Q` | How to Replace a Steam Radiator / Ask This Old House | This Old House | 536,527 | 8y ago | 8:30 |
| 10 | `yCZqfnlBYW8` | Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT | Silver Cymbal | 470,689 | 8y ago | 5:18 |
| 11 | `gZcPUH83S10` | How to bleed oil burner how to restart the burner how to relight the furnace | Kevin Bergeron | 454,561 | 7y ago | 6:27 |
| 12 | `0l_j1m5KIuw` | Boiler Training Class, Parts, Operation, Zoning, Explained! | AC Service Tech LLC | 449,588 | 4y ago | 22:49 |
| 13 | `Y-8EWK1Moh0` | Hydronics System Components | Tec Tube | 447,543 | 8y ago | 12:31 |
| 14 | `oyq4gTWVRhA` | How to Quiet Noisy Baseboard Heat / Ask This Old House | This Old House | 409,219 | 7y ago | 5:44 |
| 15 | `yx9g9P_z5So` | How to Replace An Oil Filter For Your Oil Fired Boiler Or Furnace | TheDIYGuyDOTnet | 380,552 | 11y ago | 7:20 |
| 16 | `GdTOl1WcHV0` | Why Heating Oil is BETTER than GAS - Explained | Silver Cymbal | 343,511 | 4y ago | 5:12 |
| 17 | `VFLPhENA24E` | How to Diagnose Leaks in a Steam Boiler / Ask This Old House | This Old House | 310,171 | 10y ago | 5:55 |
| 18 | `OSZTmsmjGxg` | Oil Burner Primary Control and CAD Cell Operation and Troubleshooting! | AC Service Tech LLC | 300,467 | 6y ago | 11:13 |
| 19 | `u-_9TEF1k7M` | How to Move Baseboard Heating / Ask This Old House | This Old House | 278,701 | 5y ago | 6:55 |
| 20 | `g2nTv1NRuY4` | OIL BURNER YEARLY SERVICE & CLEAN (Honest Jardys plumbing) | Mike Haduck - Travel - Mechanics - Music | 244,244 | 7y ago | 19:54 |

The US top 20 is all 4 years old or older. It is mostly how-to work: This Old House, grayfurnaceman, Silver Cymbal, AC Service Tech LLC.

---

## 4. Last 12 months: what was uploaded and how it did

- **All 38 keywords:** 164 kept videos from the last 12 months, from 92 channels. Median 3,779 views; **6 at 100K+**, and all 6 are British-topic videos (5 from UK-listed channels, plus Ripped Off Britain, which lists the US but covers British boilers).
- **US-listed channels only:** 107 videos, median 5,845 views, **1 at 100K+** (that same British-topic Ripped Off Britain video). Mikey Pipes (33) and steven lavimoniere (20) made 53 of the 107.

### Top 10, last 12 months (all countries)

| # | ID | Title | Channel | Country | Views | Age | Length |
|---|---|---|---|---|---|---|---|
| 1 | `0Oa5UBiZ6W0` | £15 Radiator Upgrades That Heat Your Room Fast! | The DIY Guy | United Kingdom | 1,499,165 | 9mo ago | 10:07 |
| 2 | `PHXdfLjwtXM` | BOOST Your Home Heating with SIMPLE Radiator Upgrades! | Fix it with Fowler | United Kingdom | 315,682 | 10mo ago | 14:02 |
| 3 | `WfXTAcRNPzk` | This New Heat Pump Could Finish Boilers | Heatable | United Kingdom | 260,426 | 1mo ago | 17:23 |
| 4 | `Nc5trKJvcjg` | Could This Battery Boiler Replace Gas AND Heat Pumps? | Everything Electric TECH | United Kingdom | 213,560 | 11mo ago | 17:10 |
| 5 | `CFSZViBzlIQ` | We RIPPED Out Our Gas Boiler And Installed A £2,150 Heat Pump. Here’s What Happened… | Everything Home | United Kingdom | 184,227 | 3mo ago | 14:45 |
| 6 | `zf-1Zkog5Co` | Why Smart British Homeowners Are Refusing New Boilers — 5 Brands Robbing You Blind And 3 That Last | Ripped Off Britain | United States | 107,815 | 5mo ago | 21:11 |
| 7 | `58syFyq7H1A` | Heat Pumps Need One Thing to BEAT Gas Boilers (Most Homes Don't Have It) | Heatable | United Kingdom | 79,385 | 5mo ago | 20:11 |
| 8 | `hoNNKMSdWsU` | Starmer announces £53m heating oil support as Iran war drives up energy costs | Sky News | United Kingdom | 78,013 | 7mo ago | 7:16 |
| 9 | `urReHw0tx5k` | This Battery Boiler Could Replace Gas! | Heatable | United Kingdom | 76,057 | 7mo ago | 15:29 |
| 10 | `pegUvCXapU8` | Turn Your Gas Boiler Down? Here’s What It Actually Saves | Mick Wall (Energy Stats UK) | United Kingdom | 68,289 | 3w ago | 17:36 |

### Top 10, last 12 months, US-listed channels

| # | ID | Title | Channel | Views | Age | Length |
|---|---|---|---|---|---|---|
| 1 | `zf-1Zkog5Co` | Why Smart British Homeowners Are Refusing New Boilers — 5 Brands Robbing You Blind And 3 That Last | Ripped Off Britain | 107,815 | 5mo ago | 21:11 |
| 2 | `iUdTZM41qaQ` | Homeowner’s Boiler Installed WRONG – Mikey Pipes Explains the Fix! | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 54,879 | 11mo ago | 8:21 |
| 3 | `C48QR-c-Ilw` | Emergency Oil Boiler Repair - No Heat Situation | steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | 30,298 | 10mo ago | 20:05 |
| 4 | `AXGmso3kLAw` | Steam Boiler Disaster: No Hartford Loop, No Equalizer… Here’s Why It Matters | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 27,879 | 9mo ago | 17:13 |
| 5 | `llviLztcDLo` | Oil Burner Blowing Black Soot? Here's Why | steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | 26,413 | 8mo ago | 27:18 |
| 6 | `WR-psuq1mwU` | We ELIMINATED Home Heating Oil With THIS 5-Ton ACiQ Heat Pump! (Full Install) | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 24,502 | 4mo ago | 1:02:16 |
| 7 | `0vNHIvf8zzE` | No Heat! Burnham Boiler Pilot Won’t Stay Lit — Watch Mikey Pipes & Derek Diagnose and Fix It LIVE | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 24,277 | 11mo ago | 23:11 |
| 8 | `E6mVH8b2Ldw` | Watch Mikey Pipes Replace a 50-Year-Old Boiler with a Modern Weil-McLain CGa5 (Full Walkthrough) | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 22,056 | 11mo ago | 20:21 |
| 9 | `K87lcdKa9yk` | Whole House FREEZING! Burnham Boiler Dead – The Real Cause Will Shock You | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 21,699 | 10mo ago | 16:39 |
| 10 | `vuSQ7P0NgtU` | OIL BOILER NEVER SERVICED IN 13 YEARS FULL OF BLACK SOOT | steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | 21,167 | 7mo ago | 58:48 |

For scale, in the AC pool from the same pull, Ray Dutton's Garage, the faceless "retired HVAC pro", has "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" at 1,212,929 (1 month old), "The 5 Thermostat Habits That Wear Out Your AC Years Early" at 1,127,505 (2 months), "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" at 767,290 (2 months) and "5 AC Mistakes HVAC Companies Hope You Keep Making" at 589,312 (2 months). The best US old-house heat upload of the last 12 months has 54,879.

---

## 5. Who owns the space

The type column is my reading from 2 thumbnails per channel (the channel's top 2 in the pool, viewed on 2026-10-24) and its titles. It is not a measurement.

### Top 15 channels by number of kept videos

| Channel | Country | Subs (About) | Joined | Videos in pool | Total views in pool | Median in pool | Last 12 mo in pool | Top video in pool | Type (my reading) |
|---|---|---|---|---|---|---|---|---|---|
| Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | United States | 207K subscribers | Joined Sep 21, 2012 | 47 | 1,038,970 | 11,055 | 33 | Annual Burnham Gas Steam Boiler Step by Step Maintenance & T | on camera |
| steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | United States | 213K subscribers | Joined Dec 6, 2011 | 33 | 557,405 | 11,451 | 20 | OLD CASTIRON RADIATOR BOILER JOB NOT HEATING PROPERLY | on camera (job footage; no face in the 2 thumbnails checked) |
| This Old House | United States | 2.34M subscribers | Joined Jun 7, 2006 | 7 | 2,466,896 | 310,171 | 0 | How to Diagnose Problems with a Hot Water Heating System / A | on camera (TV show) |
| The DIY Guy | United Kingdom | 778K subscribers | Joined Nov 26, 2020 | 6 | 9,186,050 | 1,724,356 | 1 | How to Change a Thermostatic Radiator Valve Without Draining | on camera |
| Heating Help | not stated | 8.99K subscribers | Joined Jun 23, 2016 | 6 | 321,701 | 50,179 | 0 | Steam Boiler Piping Tips | faceless (diagrams) |
| dereton33 Plumbing and heating, DIY and blogging. | United Kingdom | 161K subscribers | Joined Oct 15, 2007 | 5 | 522,282 | 41,609 | 0 | How to stop kettling and banging noises from your central he | faceless (job footage, text) |
| Heatable | United Kingdom | 28.8K subscribers | Joined Apr 23, 2019 | 5 | 461,347 | 76,057 | 3 | This New Heat Pump Could Finish Boilers | on camera |
| Boiler Room Detective | United States | 3.18K subscribers | Joined Jun 21, 2022 | 5 | 3,814 | 763 | 5 | Why steam heat worked in morning but didnt after. Understand | faceless (text cards; illustrated mascot man) |
| plumberparts | United Kingdom | 421K subscribers | Joined Apr 27, 2010 | 4 | 5,131,291 | 1,298,060 | 0 | How to Fix One Radiator Not Working - Plumbing Tips | on camera |
| Allen Hart | United Kingdom | 166K subscribers | Joined Feb 23, 2011 | 4 | 4,429,924 | 971,080 | 0 | How To Bleed A Radiator - Don’t try it until you watch this | on camera |
| grayfurnaceman | United States | 167K subscribers | Joined Feb 3, 2012 | 4 | 2,824,693 | 886,699 | 0 | Troubleshoot the oil furnace part 1. Burner won't start. | faceless (job footage) |
| Silver Cymbal | United States | 1.09M subscribers | Joined Jun 26, 2012 | 4 | 1,851,832 | 407,100 | 0 | Oil Heat 🔥 Boilers - How it works - Understand the Basics | faceless (hands and equipment) |
| Skill Builder | United Kingdom | 749K subscribers | Joined Nov 6, 2013 | 4 | 1,780,041 | 226,394 | 0 | Radiator NOT Heating Up? Expert DIY Fixes | on camera |
| Heat Geek | United Kingdom | 78.7K subscribers | Joined Dec 21, 2016 | 4 | 1,068,789 | 65,282 | 2 | Is It Better To Leave The Heating On Constantly? Boilers & H | on camera |
| BobsPlumbingVideos | United States | 67.3K subscribers | Joined Mar 3, 2012 | 4 | 259,170 | 37,808 | 0 | Steam Radiator Not Working | on camera |

### Top 15 channels by total views of kept videos

| Channel | Country | Subs (About) | Joined | Videos in pool | Total views in pool | Median in pool | Last 12 mo in pool | Top video in pool | Type (my reading) |
|---|---|---|---|---|---|---|---|---|---|
| The DIY Guy | United Kingdom | 778K subscribers | Joined Nov 26, 2020 | 6 | 9,186,050 | 1,724,356 | 1 | How to Change a Thermostatic Radiator Valve Without Draining | on camera |
| plumberparts | United Kingdom | 421K subscribers | Joined Apr 27, 2010 | 4 | 5,131,291 | 1,298,060 | 0 | How to Fix One Radiator Not Working - Plumbing Tips | on camera |
| Allen Hart | United Kingdom | 166K subscribers | Joined Feb 23, 2011 | 4 | 4,429,924 | 971,080 | 0 | How To Bleed A Radiator - Don’t try it until you watch this | on camera |
| grayfurnaceman | United States | 167K subscribers | Joined Feb 3, 2012 | 4 | 2,824,693 | 886,699 | 0 | Troubleshoot the oil furnace part 1. Burner won't start. | faceless (job footage) |
| This Old House | United States | 2.34M subscribers | Joined Jun 7, 2006 | 7 | 2,466,896 | 310,171 | 0 | How to Diagnose Problems with a Hot Water Heating System / A | on camera (TV show) |
| Silver Cymbal | United States | 1.09M subscribers | Joined Jun 26, 2012 | 4 | 1,851,832 | 407,100 | 0 | Oil Heat 🔥 Boilers - How it works - Understand the Basics | faceless (hands and equipment) |
| askmediy | United States | 110K subscribers | Joined Jan 10, 2008 | 2 | 1,845,544 | 922,772 | 0 | How to remove the air from your boiler / heater | on camera |
| Skill Builder | United Kingdom | 749K subscribers | Joined Nov 6, 2013 | 4 | 1,780,041 | 226,394 | 0 | Radiator NOT Heating Up? Expert DIY Fixes | on camera |
| How2D2 | United Kingdom | 121K subscribers | Joined Oct 9, 2016 | 1 | 1,608,538 | 1,608,538 | 0 | RADIATORS EXPLAINED How to fix balance bleed panel radiator  | faceless (diagrams) |
| Proper DIY | United Kingdom | 636K subscribers | Joined Dec 2, 2018 | 2 | 1,396,606 | 698,303 | 0 | How to Bleed Radiators 'Properly' | faceless (hands) |
| Fix It With Zim | not stated | 41.4K subscribers | Joined Mar 8, 2011 | 1 | 1,153,868 | 1,153,868 | 0 | Remove Air from your Boiler and Heating System / How To | faceless (text and equipment) |
| K. S. Engineering and Exeter City Council | not stated | 965 subscribers | Joined Feb 21, 2014 | 1 | 1,150,095 | 1,150,095 | 0 | Vaillant Ecotec Mk 1 - Resetting the boiler. | faceless (hands) |
| Heat Geek | United Kingdom | 78.7K subscribers | Joined Dec 21, 2016 | 4 | 1,068,789 | 65,282 | 2 | Is It Better To Leave The Heating On Constantly? Boilers & H | on camera |
| Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | United States | 207K subscribers | Joined Sep 21, 2012 | 47 | 1,038,970 | 11,055 | 33 | Annual Burnham Gas Steam Boiler Step by Step Maintenance & T | on camera |
| AC Service Tech LLC | United States | 689K subscribers | Joined Feb 26, 2016 | 3 | 913,702 | 300,467 | 0 | Boiler Training Class, Parts, Operation, Zoning, Explained! | on camera |

### Channels most active in the last 12 months (kept videos uploaded in the last 12 months)

| Channel | Country | Subs (About) | Joined | Videos in pool | Total views in pool | Median in pool | Last 12 mo in pool | Top video in pool | Type (my reading) |
|---|---|---|---|---|---|---|---|---|---|
| Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | United States | 207K subscribers | Joined Sep 21, 2012 | 33 | 404,418 | 7,864 | 33 | Homeowner’s Boiler Installed WRONG – Mikey Pipes Explains th | on camera |
| steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | United States | 213K subscribers | Joined Dec 6, 2011 | 20 | 253,378 | 9,514 | 20 | Emergency Oil Boiler Repair - No Heat Situation | on camera (job footage; no face in the 2 thumbnails checked) |
| Boiler Room Detective | United States | 3.18K subscribers | Joined Jun 21, 2022 | 5 | 3,814 | 763 | 5 | Why steam heat worked in morning but didnt after. Understand | faceless (text cards; illustrated mascot man) |
| Heatable | United Kingdom | 28.8K subscribers | Joined Apr 23, 2019 | 3 | 415,868 | 79,385 | 3 | This New Heat Pump Could Finish Boilers | on camera |
| Handyman Hints | United States | 193 subscribers | Joined Dec 11, 2024 | 3 | 3,643 | 1,170 | 3 | How to Unclog Oil Burner Fuel Lines / Clear Sludge & Airlock | faceless (text slides) |
| Everything Home | United Kingdom | 12.1K subscribers | Joined Sep 4, 2019 | 2 | 196,145 | 98,072 | 2 | We RIPPED Out Our Gas Boiler And Installed A £2,150 Heat Pum | not checked |
| Mick Wall (Energy Stats UK) | United Kingdom | 2.92K subscribers | Joined Oct 18, 2006 | 2 | 79,096 | 39,548 | 2 | Turn Your Gas Boiler Down? Here’s What It Actually Saves | not checked |
| Heat Geek | United Kingdom | 78.7K subscribers | Joined Dec 21, 2016 | 2 | 44,184 | 22,092 | 2 | £3,000 Heat Pump vs £3,300 Oil Boiler | on camera |
| Jumper man Tech | United States | 130K subscribers | Joined Dec 24, 2018 | 2 | 17,737 | 8,868 | 2 | HVAC: Boiler Making Noise & Not Firing Up? Step By Step Trou | not checked |
| Mikey Pipes Uncensored | United States | 26.2K subscribers | Joined Apr 13, 2019 | 2 | 8,635 | 4,318 | 2 | I Walked Away From a Two-Pipe Steam Job — Here’s Why (Keepin | not checked |
| VideoParliament Ireland | Ireland | 51.6K subscribers | Joined Sep 18, 2018 | 2 | 4,594 | 2,297 | 2 | Michael Cahill urges action on home heating oil costs | not checked |
| Jay Of All Trades | United States | 5.87K subscribers | Joined May 7, 2024 | 2 | 2,540 | 1,270 | 2 | How to Replace an Oil Burner Nozzle / One Year Later | not checked |
| Drewdriskle | United States | 9.75K subscribers | Joined Jun 3, 2011 | 2 | 922 | 461 | 2 | Crown Boiler Not Working (pt.1) / Boilers | not checked |
| The Home Problem Solver | Italy | 1.17K subscribers | Joined Nov 16, 2024 | 2 | 749 | 374 | 2 | How to Reset an Immergas Boiler   Step by Step Guide and Com | not checked |
| Arthur Weber | United States | 15 subscribers | Joined Apr 28, 2026 | 2 | 375 | 188 | 2 | Why Don’t More Seniors Put This $8 Foil Behind Their Radiato | faceless persona (AI old man) |

Who owns what (counts measured, labels my reading):
- **Views** belong to old UK on-camera how-to channels (The DIY Guy, plumberparts, Allen Hart, Skill Builder) and old US how-to (grayfurnaceman, This Old House, Silver Cymbal). None of these US channels has an old-house heat upload in the last 12 months in this pull.
- **Current US activity** belongs to two on-camera working pros: Mikey Pipes (steam and boilers, 142 long-form uploads in 12 months, tab median 6,000) and steven lavimoniere (oil burners and boilers, 141, tab median 9,800).
- **Faceless footage and diagram channels** (no narrator persona) hold old views: How2D2 1,608,538, grayfurnaceman 1,043,525, Silver Cymbal 821,099, Heating Help 82,434. All of these videos are 6+ years old.
- **Newer faceless narrated or AI-persona channels:** none has more than about 1,200 views on any kept video, apart from a few general money, history or British-topic channels (next table).

### Faceless and faceless-persona channels found in the old-house heat pool

| Channel | Subs (About) | Joined | Title (original) | Views | Age | Length | Type (my reading, from thumbnail) |
|---|---|---|---|---|---|---|---|
| Ripped Off Britain | 10K subscribers | Jan 31, 2026 | Why Smart British Homeowners Are Refusing New Boilers — 5 Brands Robbing You Blind And 3 That Last | 107,815 | 5mo ago | 21:11 | faceless, graphics (no persona) |
| Fred - Money Historian | 12.6K subscribers | Sep 27, 2014 | The Home Heating Crisis No One Is Talking About | 13,758 | 1d ago | 39:14 | faceless, cartoon mascot; money/news |
| Weirdward Bound | 63.1K subscribers | Apr 9, 2026 | Why 1920s Steam Radiators Were Engineered to Boil You Alive | 13,495 | 1mo ago | 25:38 | faceless, AI-illustrated old craftsman; history story |
| WiseMoney | 22K subscribers | Dec 16, 2025 | Heating Oil Costs Just Jumped 40% - Only Use THESE 20 Non Electric Heaters This Winter! | 1,907 | 2w ago | 27:13 | faceless, AI-made presenter image |
| Boiler Room Detective | 3.18K subscribers | Jun 21, 2022 | Why steam heat worked in morning but didnt after. Understanding air vent drop away pressure | 1,177 | 10mo ago | 7:25 | faceless; mix of text cards and an illustrated cap-wearing man with a detective mascot logo |
| Sylvie Mercer and 3 more | not found | not found | Why Putting Aluminum Foil Behind Your Radiator is Genius | 1,076 | 3w ago | 27:58 | faceless persona, AI woman at a radiator |
| Sketchy Survival | 41.7K subscribers | Aug 11, 2025 | Your Radiator Is Heating the Street | 947 | 2w ago | 12:44 | faceless, illustration |
| The Old House Fix | 341 subscribers | Jun 9, 2026 | How To Bleed An Old Radiator - Don't try it until you watch this | 875 | 12d ago | 15:02 | faceless persona, AI old man bleeding a radiator |
| Boiler Room Detective | 3.18K subscribers | Jun 21, 2022 | Should I replace the steam system with forced air? | 783 | 1mo ago | 6:54 | faceless; mix of text cards and an illustrated cap-wearing man with a detective mascot logo |
| Boiler Room Detective | 3.18K subscribers | Jun 21, 2022 | 🔥 Why Raising Steam Boiler Pressure Is a HUGE Mistake (Costs You Money & Causes Banging!) | 763 | 9mo ago | 6:56 | faceless; mix of text cards and an illustrated cap-wearing man with a detective mascot logo |
| Boiler Room Detective | 3.18K subscribers | Jun 21, 2022 | Hydronic boiler won't start? Check these 7 things first. | 676 | 4w ago | 5:44 | faceless; mix of text cards and an illustrated cap-wearing man with a detective mascot logo |
| Boiler Room Detective | 3.18K subscribers | Jun 21, 2022 | Boiler Is Hot but Building Is Cold? Here's What to Check! | 415 | 7d ago | 6:13 | faceless; mix of text cards and an illustrated cap-wearing man with a detective mascot logo |
| Handy Leo and Leo Bennett | not found | not found | $20 Radiator Upgrades That Heat Your Room Fast | 281 | 4w ago | 12:24 | faceless persona, AI man (copies The DIY Guy's title) |
| Arthur Weber | 15 subscribers | Apr 28, 2026 | Why Don’t More Seniors Put This $8 Foil Behind Their Radiators? (The German Way) | 278 | 2w ago | 11:18 | faceless persona, AI old man in work clothes, '(The German Way)' |
| Faded Labels | 9 subscribers | Jul 19, 2026 | The Fascinating Story of the Steam Radiator, How One Hissing Valve Heated Every Apartment | 254 | 1mo ago | 23:11 | faceless, AI image; history story |
| Building Secrets | 286 subscribers | Sep 20, 2017 | How Building Supers Keep 1920s Radiators Warm All Winter With a $5 Fix | 166 | 4mo ago | 15:10 | faceless persona, AI old man in a 'Steam Heating Pro' cap |
| Prime Energy UK | 1 subscriber | Aug 31, 2026 | He Hid This Behind His Boiler for 52 Years / THE LAST FLAME Ep 1 | 98 | 3w ago | 10:00 | faceless, AI old man; drama story series |
| Arthur Weber | 15 subscribers | Apr 28, 2026 | Most People Are Bleeding Radiators Wrong! Try These 3 Old Tricks for Even Heat in Every Room | 97 | 5d ago | 10:50 | faceless persona, AI old man in work clothes, '(The German Way)' |
| Forgotten Survival | 1.93K subscribers | Sep 30, 2025 | Discover the 1940s Radiator Trick That Warms Homes Better Than New Systems | 92 | 10mo ago | 8:38 | faceless, AI image |
| Underwritten | 2 subscribers | Oct 8, 2026 | Why Heating Oil Is $6 a Gallon This Winter, and Who Pays Most | 73 | 5d ago | 8:31 | faceless, graphics; money/news |
| Quarter Turn | 90 subscribers | Jul 7, 2026 | The "Air" in Your Radiator Often Isn't Air | 60 | 3w ago | 8:36 | faceless, graphic |
| Halden Row | 4 subscribers | Apr 8, 2006 | Before Fans, This Octopus Furnace Heated a House by Itself | 48 | 4w ago | 14:49 | faceless persona, AI old man |
| brother Q | 9 subscribers | Jul 17, 2012 | Short Cycling — Why Your Boiler Keeps Turning On and Off | 25 | 11d ago | 11:50 | faceless, icon graphic |
| Simple Savings at Home | 3 subscribers | Oct 12, 2026 | Heating Oil Up 21%, Gas Down 9%: What Your Winter Bill Will Be | 21 | 3d ago | 11:57 | faceless persona, AI woman |
| Walt's Workshop | 1 subscriber | Jan 9, 2026 | STOP Heating Your Walls — This $0 Foil Trick Doubles Your Radiator Heat | 11 | 8d ago | 12:00 | faceless persona, AI old man in flannel |
| brother Q | 9 subscribers | Jul 17, 2012 | Boiler Not Working? The No-Heat Call Playbook | 2 | 11d ago | 11:32 | faceless, icon graphic |

Notes:
- Fred - Money Historian's video showed in search as "Heating Oil Just Hit $6.11. February Is the Real Problem." while oEmbed gives "The Home Heating Crisis No One Is Talking About". The two titles differ, possibly a title test (my reading).
- Arthur Weber's channel (16 videos, all uploaded within the last month) is a faceless AI "old German tradesman" doing home tips: radiators, drains, water heaters, drafts, several marked "(The German Way)". Its median is 135 views (tab counts).

**Is there a faceless persona doing old-house heat?** Yes, several: Arthur Weber, Building Secrets, The Old House Fix, Walt's Workshop, Halden Row, Sylvie Mercer and Handy Leo. All have AI-image "old expert" thumbnails, and every one of them started or went active in 2025-2026. None has a video above 1,076 views in this pull. The faceless channels that did reach 13K-108K are a British consumer channel (Ripped Off Britain), a history-story channel (Weirdward Bound) and money/news channels (Fred - Money Historian). Nothing found in this pull is the size of Ray Dutton's Garage for heat.

---

## 6. Seasonality

### Upload month of the top heat videos (exact dates)

Dates come from innertube `/next` (`dateText`) for the top 120 heat and top 60 AC videos by views. The watch-page method (`vid_exact.py`) returned LOGIN_REQUIRED for all 180, so I used `vid.py`'s `/next` call instead. 114 of the 120 heat videos had a date, as did all 60 AC videos.

| Pool | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heat, top 120 (114 dated) | 14 | 10 | 11 | 7 | 5 | 7 | 3 | 2 | 11 | 10 | **20** | 14 |
| AC, top 60 | 0 | 3 | 4 | 10 | 10 | **11** | 8 | 6 | 1 | 5 | 1 | 1 |

- **Heat:** 55 of 114 (48%) were uploaded Sept-Dec (an even spread would give 33%). Their median is 234,315 views, against 188,740 for the other 59. Sept-Jan together hold 69 of 114.
- **AC:** 39 of 60 were uploaded Apr-Jul, and 8 of 60 (13%) Sept-Dec.

### Last 12 months, from the age text (rough)

These months are approximate, worked back from the age text ("3w ago", "5mo ago") from 2026-10-24, so they can be a month off. October 2026 is over-represented, because the "month" sort only returns this month's uploads, and those uploads have had only days or weeks to gather views.

| Approx. upload month | Videos | Median views | Top views |
|---|---|---|---|
| 2025-11 | 19 | 6,547 | 213,560 |
| 2025-12 | 17 | 7,792 | 315,682 |
| 2026-01 | 12 | 765 | 1,499,165 |
| 2026-02 | 11 | 11,451 | 28,670 |
| 2026-03 | 14 | 5,720 | 78,013 |
| 2026-04 | 2 | 580 | 1,136 |
| 2026-05 | 2 | 93,600 | 107,815 |
| 2026-06 | 3 | 7,107 | 24,502 |
| 2026-07 | 3 | 9,065 | 184,227 |
| 2026-08 | 1 | 11,275 | 11,275 |
| 2026-09 | 13 | 1,098 | 260,426 |
| 2026-10 | 67 | 1,232 | 68,289 |

- Sept-Dec (approx.): 116 videos, median 2,731. Jan-Aug: 48 videos, median 6,687.
- Leaving out uploads under 1 month old, Sept-Dec is 45 videos with a median of 7,415.

Reading: creators upload heat videos in the cold months (only 11 kept uploads in Apr-Aug 2026), and the big heat winners were mostly published Sept-Jan. AC is the mirror image. A heat lane would be a fall and winter lane.

---

## 7. Channel multiples (5 old-house heat channels)

**Rule:** a video's multiple is its views divided by the channel's own median. The median is that of the channel's **long-form (5:00 or more) uploads in the last 12 months** on its Videos tab (Latest, up to 150 videos). The fallback was the last 30 long-form uploads if a channel had fewer than 10; no channel needed it. Tab view counts are rounded by YouTube ("6K views"). "Heat videos" means videos that pass the same on-topic rule as the pool. Tabs were pulled at 07:09 UTC with `yt_allsorts.py` (5 pages per chip).

| Channel | Type (my reading) | Subs | Median basis | Median (views) | Heat videos in the same 12 months: n, median views, median multiple, 2x or more | All heat videos found on the tab (incl. older, Popular/Oldest): n, median multiple, 2x or more |
|---|---|---|---|---|---|---|
| Mikey Pipes - Pipe Doctor | on camera | 207K | 142 long-form, last 12 mo | 6,000 | 22, 5,950, 0.99x, 4/22 | 22, 0.99x, 4/22 (Popular/Oldest chips not returned) |
| steven lavimoniere | on camera (job footage) | 213K | 141 long-form, last 12 mo | 9,800 | 22, 8,300, 0.85x, 0/22 | 70, 4.34x, 40/70 |
| Silver Cymbal | faceless-ish (hands, equipment) | 1.09M | 18 long-form, last 12 mo | 79,500 | 0 (no heat upload in 12 months) | 5, 2.97x, 4/5 |
| Boiler Room Detective | faceless | 3.18K | 38 long-form, last 12 mo | 478 | 25, 479, 1.0x, 4/25 | 71, 1.56x, 22/71 |
| Arthur Weber | faceless persona | 15 | 16 long-form, last 12 mo | 135 | 2, 188, 1.39x, 1/2 | 2, 1.4x, 1/2 |

Best heat multiples (all measured from the tab):
- **Silver Cymbal:** "Oil Heat Boilers - How it works - Understand the Basics" 821K, 10.33x; "Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" 470K, 5.91x (both 8 years old).
- **steven lavimoniere:** "Gas Boiler/ pilot on, but will not fire" 324K, 33.06x (8 years); "beckett AF oil burner tripping out every day or so" 296K, 30.2x (11 years).
- **Boiler Room Detective:** "How to set & adjust steam boiler pressure controls" 44K, 92.05x (3 years).
- **Mikey Pipes:** "The ONE Thing Every Tankless Combi Boiler MUST Have!" 29K, 4.83x (1 month); "We ELIMINATED Home Heating Oil With THIS 5-Ton ACiQ Heat Pump!" 24K, 4.0x (4 months).
- **Arthur Weber:** "Why Don't More Seniors Put This $8 Foil Behind Their Radiators? (The German Way)" 279 views, 2.07x.

Reading of the multiples:
- In the same 12 months, heat videos do about the same as each channel's other videos (0.85x-1.0x on the three channels with enough of them).
- The large multiples all belong to videos 3-12 years old, measured against a recent median. They show old heat how-tos piling up views over years (search traffic), not a current premium. Silver Cymbal posted no heat video in the last 12 months.

### Check of the top 20 heat videos (search figure, then innertube `/next` re-pull 07:20-07:28 UTC)

| ID | Search views | Re-pull views | Difference | Owner text from re-pull |
|---|---|---|---|---|
| `o2Y9elh24wc` | 2,656,757 | 2,656,773 | +0.00% | The DIY Guy |
| `wqku_Rc_YuI` | 2,479,340 | 2,479,363 | +0.00% | plumberparts |
| `tbLz8icLr2U` | 2,404,191 | 2,404,207 | +0.00% | Allen Hart |
| `4meZgMAUecw` | 2,283,663 | 2,283,670 | +0.00% | plumberparts |
| `7NsZ2d2Oups` | 2,059,661 | 2,059,772 | +0.01% | Save Money and Increase Heat |
| `U2CY4rHr7nA` | 1,949,546 | 1,949,579 | +0.00% | DIY Plumbing |
| `wG-CqFr6FLM` | 1,625,468 | 1,625,465 | -0.00% | askmediy |
| `PAo6yG89vyM` | 1,608,538 | 1,608,549 | +0.00% | How2D2 |
| `0Oa5UBiZ6W0` | 1,499,165 | 1,499,435 | +0.02% | The DIY Guy |
| `UR9wSU-I2O8` | 1,412,130 | 1,412,148 | +0.00% | Allen Hart |
| `UmfKzbsQxKE` | 1,246,905 | 1,246,929 | +0.00% | Skill Builder |
| `voS7Url50M4` | 1,153,868 | 1,153,872 | +0.00% | How To |
| `Ftj67dIh1ZI` | 1,150,095 | 1,150,096 | +0.00% | K. S. Engineering and Exeter City Council |
| `cog7MaShR7M` | 1,043,525 | 1,043,534 | +0.00% | grayfurnaceman |
| `TfPnLUz1Vh4` | 1,012,924 | 1,012,940 | +0.00% | grayfurnaceman |
| `CGLAl6nGeo8` | 930,473 | 930,489 | +0.00% | The DIY Guy |
| `kGs_biFA87Q` | 922,523 | 922,530 | +0.00% | Consumer Advice |
| `5GbXgEYw5TE` | 821,099 | 821,105 | +0.00% | Silver Cymbal |
| `6t6QnYkXuXA` | 781,083 | 781,077 | -0.00% | Mark Ray |
| `LyHy2En9iF0` | 760,474 | 760,465 | -0.00% | grayfurnaceman |

All 20 view counts agree within 0.02%. Some owner fields show part of the title instead of the channel (for example "Save Money and Increase Heat" or "Consumer Advice"). That is a parsing quirk of `vid.py`'s owner pattern on titles that contain "|", not a different channel.

---

## 8. What this says (my reading, not measured)

1. **The pool is real but small, and in the US it is mostly old.** Like for like, old-house heat has fewer than half the videos AC has, about 1/8 of the typical views (1/17 on US channels), and almost no recent breakouts: 2 against 72 at 100K+ in 12 months. The earlier chat's warning holds. As a whole-channel lane, old-house heat is much smaller than AC.
2. **Most of the big numbers are British.** Radiator bleeding, boiler pressure and radiator upgrades are UK central-heating topics (combi boilers, panel radiators, £). They do not carry over to Roger's US older-home audience. US steam and oil heat is a narrower niche again: the US top 20 is all 4+ years old.
3. **No faceless persona owns it, and none is winning it yet.** The US space is held by on-camera working pros (Mikey Pipes, steven lavimoniere; channel medians 6,000-9,800). About seven faceless "old expert" personas started in 2025-2026 with radiator and foil tips, and all are under about 1,100 views. That is an open seat, but none of these entrants has yet shown that the seat pays.
4. **What does work recently is money and upgrade framing,** not repair. "£15 Radiator Upgrades That Heat Your Room Fast!" got 1,499,165; "BOOST Your Home Heating with SIMPLE Radiator Upgrades!" 315,682; "Why Smart British Homeowners Are Refusing New Boilers — 5 Brands Robbing You Blind" 107,815; heat pump against boiler cost videos 28-260K. This matches the earlier "a cheap fix plus a lower bill works" finding (findings section 1), even though most of these examples are British.
5. **It is seasonal.** Heat winners cluster Sept-Jan and AC winners Apr-Jul. Ray Dutton's own heat hit ("Before You Turn On Your Heat This Fall...", 926K in the 2026-10-22 findings) is general heating, not old-house heat.
6. **Put together:** old-house heat looks better as a **seasonal sub-lane inside Roger** (Sept-Feb), framed on the winter bill and cheap fixes for old radiators, boilers and oil heat, than as the channel's main point of difference. The main volume stays in AC and general heating, where Ray Dutton's Garage shows a faceless retired-pro format already pulling 0.6-1.2M views a video. This is one helper's reading of one day's pull. The choice is the operator's.

**Gaps:** the matched comparison uses my on-topic rules, and different rules would move the counts. Search returns 20-40 rows per sort, so this is a sample of what YouTube shows, not every video that exists. Exact upload dates were found for the top 120 heat and top 60 AC videos only (6 heat dates not found).

---

## Files

- `studies/hvac/round2/old-house-heat.md`: this file.
- `studies/hvac/data/raw/round2-oldheat-2026-10-24.json`: raw data. It holds all 192 searches with every row, the original oEmbed titles, About panels for 448 channels, the kept pools (with keywords, sorts and country per video), the 5 channel Videos tabs, the multiples, the upload-date lines and the filter rules.
- `studies/hvac/data/tools/oldheat_search.py`: the search script (copied from `sweep_round2.py`, with the side tag and ~1 s pacing added).
- The analysis scripts (filters, tables, oEmbed and About pulls) are in this helper's scratch folder, `/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/` (`build.py`, `tables.py`, `tables2.py`, `season.py`, `mult.py`, `oembed.py`, `about.py`), and are not in the repo.
