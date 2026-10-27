# HVAC round 5: thumbnails of the top 100 and the recent winners

Built 2026-10-26 by a round 5 helper. **Not checked yet by a second helper** (I re-read a sample of 10 thumbnails at full size myself; all 10 matched, but that is not an independent check).

## Method

- **Which videos.** All 100 rows of `../top-100.csv` plus every video ID in the four tables of `../recent-winners.md` (last 90 days by views, top 30; last 90 days by multiple, top 30; last 12 months by views, top 50; last 12 months by multiple, top 50). 160 recent rows deduplicate to 120 recent videos; 6 of them are also in the top 100, so there are **214 different thumbnails**.
- **Download.** `https://i.ytimg.com/vi/<id>/maxresdefault.jpg` first, then `hqdefault.jpg` when maxres was missing: 205 maxres (1280x720) and 9 hqdefault (480x360, 4:3 with black bars). Pulled 2026-10-26. Saved as `../thumbnails/img/<id>.jpg` (about 88 MB in total). These are today's thumbnails; a channel may have swapped a thumbnail since upload.
- **Reading.** Every thumbnail was viewed with the Read tool on contact sheets of 6 (each tile 640x360), and single images or crops were opened where the text was small (`rE4QQRNaEn8`, `H8-QNBd7MIo`, `2ydQNz5O4I4`, and a full-size re-check of `HVd1qlorPJw`, `1hpJt_mxbOE`, `Y0teFh7cVrA`, `hqaImbFVwAM`, `H8-QNBd7MIo`, `QoC8R3KHk8E`, `auUvh-k5ja4`, `C82HvbvP08E`, `pSBR5A6oR70`, `1P4H0oly778`).
- **Labels are readings,** made by eye: face, the person (real / AI / cartoon / none, age and look), the object, the text (word count, colours, the exact words in quotes, spelling kept, "(sic)" where misspelt), arrows and circles, before-and-after, red or green marks, background, overall look, and a style group. "Real person" versus "AI person" and "realistic photo" versus "AI image" are the hardest calls: where unsure the cell says "(reading)" or "could be AI". Several 2024-2026 build thumbnails labelled "realistic photo" may be AI-made (marked "possibly AI-polished" or "possibly AI-made").
- **Word count** counts the overlay words (numbers such as "$4" or "-64°C" count as words; channel logos, watermarks, printing on the product and chart axis labels do not). Two This Old House rows show only the show logo and count 0.
- **Views and multiples** are copied from `top-100.csv` and `recent-winners.md` (exact views pulled 2026-10-26; multiple = views / channel baseline). Old videos' multiples are inflated by age, so multiples are compared within the recent lists only.
- **Style groups** were given by a fixed order of rules on the labels (cut-away claim houses first, then cartoon/animation, diagram/render, before/after split, store front, AI history, then look x person x text), then checked by eye. The rule script is not in the repo (it is in the helper's scratch folder); the CSV holds every label it used.
- Output: `../thumbnails/labels-top-winners.csv` (one row per thumbnail; `list` and `rank` list every list the video is in, e.g. `top100#15; 12m-views#2; 12m-mult#10`).

## Style groups: counts, median views, median multiple

"Top 100" and "Recent" overlap by 6 videos, so their counts add to 220, not 214.

| Style group | All: n | Top 100: n | Recent: n | All: median views | All: median multiple | Top 100: median views | Recent: median views | Recent: median multiple |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| real build/product photo + text | 38 | 36 | 3 | 3,744,084 | 69.1x | 3,766,384 | 725,527 | 140.7x |
| real face + text | 29 | 17 | 12 | 2,918,198 | 29.4x | 3,554,704 | 1,195,615 | 6.3x |
| AI persona + bold text (+ red arrow) | 25 | 2 | 23 | 566,976 | 153.5x | 3,914,594 | 545,458 | 192.7x |
| AI object/build + bold text | 22 | 2 | 20 | 737,098 | 213.3x | 4,772,786 | 578,540 | 213.3x |
| real build/product photo, no text | 18 | 17 | 1 | 4,536,928 | 555.6x | 4,869,487 | 197,372 | 179.4x |
| AI object/build, no headline | 18 | 5 | 15 | 1,522,540 | 126.8x | 3,214,841 | 1,338,882 | 118.7x |
| before/after or hot-vs-cold split | 11 | 3 | 9 | 1,683,340 | 271.9x | 3,270,731 | 1,183,500 | 321.3x |
| real person on the job, no text | 10 | 10 | 0 | 4,188,232 | 140.5x | 4,188,232 | - | - |
| AI persona + object, no text | 10 | 2 | 10 | 1,315,786 | 320.4x | 9,738,106 | 1,315,786 | 320.4x |
| cartoon / sketch / 3D animation | 10 | 2 | 8 | 957,976 | 616.0x | 6,050,012 | 708,420 | 1,038.0x |
| AI cut-away house / buried pipe + claim text | 8 | 0 | 8 | 966,400 | 429.8x | - | 966,400 | 429.8x |
| AI store front + list text | 6 | 0 | 6 | 243,492 | 421.4x | - | 243,492 | 421.4x |
| diagram / 3D render explainer | 4 | 3 | 1 | 2,942,776 | 6.6x | 2,998,544 | 260,585 | 351.2x |
| bold text panel + product cut-out | 3 | 1 | 2 | 1,852,699 | 40.3x | 12,954,600 | 1,772,778 | 38.5x |
| AI history scene + red banner | 2 | 0 | 2 | 1,119,046 | 74.6x | - | 1,119,046 | 74.6x |
| **Total** | 214 | 100 | 120 | 1,991,480 | 172.4x | 3,794,726 | 884,890 | 203.2x |

Readings from the table:

- **The all-time top 100 is mostly real photos** (81 of 100 look like real photos): a home-made build or product with short text (36) or no text (17), a real person at work with no text (10), or a real YouTuber face with text (17).
- **The recent winners are mostly AI images** (92 of 120): an AI build or object (35, with or without words), an AI persona with bold words and usually a red arrow (23), an AI persona beside a stove with no words (10), AI cut-away houses with a buried-pipe claim (8) and AI store fronts with a list (6).
- Look follows upload year (measured on these 214): uploads to 2023: 66 of 74 real photos, 3 AI; 2024: 10 of 10 real; 2025: 8 real, 19 AI of 32; 2026: 12 real, 77 AI of 98. So "real photo versus AI" in this table is largely "old versus new", not a test of which style wins.
- Within the recent lists, the highest median multiples are the cartoon / sketch group (1,038x, n=8), the AI cut-away claim houses (430x, n=8), AI store fronts (421x, n=6, but low views: median 243,492) and the AI persona beside a stove with no text (320x, n=10). Real faces with text have the lowest recent multiple (6.3x, n=12), because they are mostly big channels (Linus Tech Tips, Guy Martin, Project Farm). These are small groups; read them as leads, not proof.

## Which styles go with the biggest videos

### All-time top 100, by rank

| Style group | Ranks 1-10 | Ranks 11-25 | Ranks 26+ |
|---|---:|---:|---:|
| real build/product photo + text | 2 | 7 | 27 |
| real face + text | 1 | 1 | 15 |
| AI persona + bold text (+ red arrow) | 0 | 0 | 2 |
| AI object/build + bold text | 0 | 1 | 1 |
| real build/product photo, no text | 3 | 4 | 10 |
| AI object/build, no headline | 0 | 0 | 5 |
| before/after or hot-vs-cold split | 0 | 0 | 3 |
| real person on the job, no text | 1 | 1 | 8 |
| AI persona + object, no text | 1 | 1 | 0 |
| cartoon / sketch / 3D animation | 1 | 0 | 1 |
| diagram / 3D render explainer | 0 | 0 | 3 |
| bold text panel + product cut-out | 1 | 0 | 0 |
| **Total** | 10 | 15 | 75 |

The all-time top 10:

| Rank | Video | Channel | Views | Multiple | Style group | Thumbnail words |
|---:|---|---|---:|---:|---|---|
| 1 | `ITtlxjvLQis` | desertsun02 | 15,266,541 | 2,135.2x | real build/product photo, no text | none |
| 2 | `UawMGmg87ho` | Creative inventions LMTN | 14,880,633 | 2,807.7x | real build/product photo, no text | none |
| 3 | `DzVJiSQNbew` | alpinehomeair | 13,034,823 | 129.7x | real person on the job, no text | none |
| 4 | `7LV5wY-iM34` | Zen Garden Oasis | 12,954,600 | 281.6x | bold text panel + product cut-out | "UNLIMITED HEAT WITH NO ELECTRICITY" + badge "POWER OUTAGE" |
| 5 | `OEdzXsloZ7I` | DIY | 12,478,319 | 367.0x | real build/product photo + text | "ROOM HEATER" |
| 6 | `RotAhlS7LQ4` | Creation Daily | 11,941,053 | 1,243.9x | AI persona + object, no text | none |
| 7 | `I9Td5uMB_vQ` | CrazyRussianHacker | 10,743,855 | 199.0x | real build/product photo, no text | none (small channel logo only) |
| 8 | `_-mBeYC2KGc` | Technology Connections | 10,392,115 | 5.6x | real build/product photo + text | "These suck (no, really)" |
| 9 | `6CE72U92R-I` | WINNI | 9,166,055 | 247.7x | real face + text | "Continues Insulation" |
| 10 | `gVLhrLTF878` | Sabin Civil Engineering | 8,246,301 | 37.3x | cartoon / sketch / 3D animation | "COLD AIR" "HEAT OUT" "Animation!" |

### Last 12 months, top 50 by views

| Style group | Ranks 1-10 | Ranks 11-25 | Ranks 26+ |
|---|---:|---:|---:|
| real build/product photo + text | 1 | 0 | 0 |
| real face + text | 1 | 3 | 4 |
| AI persona + bold text (+ red arrow) | 0 | 1 | 3 |
| AI object/build + bold text | 1 | 1 | 5 |
| AI object/build, no headline | 2 | 4 | 4 |
| before/after or hot-vs-cold split | 1 | 3 | 1 |
| AI persona + object, no text | 3 | 0 | 3 |
| cartoon / sketch / 3D animation | 0 | 0 | 2 |
| AI cut-away house / buried pipe + claim text | 1 | 1 | 2 |
| bold text panel + product cut-out | 0 | 2 | 0 |
| AI history scene + red banner | 0 | 0 | 1 |
| **Total** | 10 | 15 | 25 |

The 12-month top 10:

| Rank | Video | Channel | Views | Multiple | Style group | Thumbnail words |
|---:|---|---|---:|---:|---|---|
| 1 | `RotAhlS7LQ4` | Creation Daily | 11,941,053 | 1,243.9x | AI persona + object, no text | none |
| 2 | `7BvS13bvegY` | Unknowns Lab 101 | 7,605,364 | 1,000.7x | real build/product photo + text | "WASTE OIL HEATER!" |
| 3 | `H2SrcFJ8g6s` | Creative DIY365 | 7,535,159 | 627.9x | AI persona + object, no text | none |
| 4 | `dP2PCqUanu0` | Creative DIY365 | 5,546,111 | 462.2x | AI object/build, no headline | none |
| 5 | `H514-w6ttNo` | Why Am I Green | 3,708,639 | 608.0x | before/after or hot-vs-cold split | "COLDER AIR!" "95°F" "62°F" |
| 6 | `2kEXIAsOAMM` | Creative DIY365 | 2,757,322 | 229.8x | AI object/build, no headline | none |
| 7 | `JZ4vlMZlCj8` | JDub Adventures | 2,619,713 | 609.2x | real face + text | "WHAT'S INSIDE THE BREEZAMAX?" "SCAM" "EXPOSED!" |
| 8 | `FGQmj5oA_oY` | Creation Daily | 2,459,044 | 256.2x | AI persona + object, no text | none |
| 9 | `XJzM-fcrFck` | Construction Odyssey with Eddie | 2,227,816 | 795.6x | AI cut-away house / buried pipe + claim text | "ILLEGAL COOLING" |
| 10 | `SVuQqEXaWdw` | Wild Line | 2,139,032 | 50.9x | AI object/build + bold text | "37°F" "FREE COOLING" |

### Last 90 days, top 30 by views

| Style group | Ranks 1-10 | Ranks 11-25 | Ranks 26+ |
|---|---:|---:|---:|
| real build/product photo + text | 0 | 1 | 0 |
| real face + text | 2 | 3 | 0 |
| AI persona + bold text (+ red arrow) | 3 | 5 | 1 |
| AI object/build + bold text | 0 | 2 | 0 |
| AI object/build, no headline | 2 | 1 | 2 |
| AI persona + object, no text | 0 | 0 | 2 |
| cartoon / sketch / 3D animation | 1 | 1 | 0 |
| AI store front + list text | 0 | 1 | 0 |
| bold text panel + product cut-out | 1 | 0 | 0 |
| AI history scene + red banner | 1 | 1 | 0 |
| **Total** | 10 | 15 | 5 |

The 90-day top 10:

| Rank | Video | Channel | Views | Multiple | Style group | Thumbnail words |
|---:|---|---|---:|---:|---|---|
| 1 | `1H20xp8Brnc` | Linus Tech Tips | 1,981,054 | 1.5x | real face + text | "DIY Heat Pump" |
| 2 | `KphunxyIbKM` | Zen Garden Oasis | 1,692,856 | 36.8x | bold text panel + product cut-out | "$4" "DEHUMIDIFIER WORKS FOREVER" |
| 3 | `lC4HeSA5bwU` | GRENY | 1,588,457 | 3,460.7x | cartoon / sketch / 3D animation | "HOW?! 50°C" |
| 4 | `sHL4lBAhklA` | Silver Cymbal | 1,529,886 | 19.0x | AI persona + bold text (+ red arrow) | "BETTER THAN SPRAY FOAM" "SEALS INSTANTLY - NO WASTE" "WRONG" |
| 5 | `9tbUFAocp5A` | Creative DIY365 | 1,424,588 | 118.7x | AI object/build, no headline | none |
| 6 | `rX4eyZaHAjw` | Lost Survival Knowledge | 1,327,280 | 132.7x | AI persona + bold text (+ red arrow) | "CHEAP WINTER LIFESAVERS" |
| 7 | `dOZ-8__G4uU` | Ray Dutton's Garage | 1,229,174 | 81.9x | AI persona + bold text (+ red arrow) | "BIG FALL MISTAKE!" |
| 8 | `9-eQiEQOhyo` | Secret State Files | 1,224,700 | 81.6x | AI history scene + red banner | "BEFORE CENTRAL HEATING" "HOW DID THEY STAY WARM?" |
| 9 | `mP0IjyvQtxw` | The DIY HVAC Guy | 1,220,217 | 29.4x | real face + text | "THEY HOPE YOU MISS THIS" |
| 10 | `hm08rD9vrxo` | Creative DIY365 | 1,131,701 | 94.3x | AI object/build, no headline | none |

### By multiple (recent lists)

Last 12 months, top 50 by multiple:

| Style group | Ranks 1-10 | Ranks 11-25 | Ranks 26+ |
|---|---:|---:|---:|
| real build/product photo + text | 1 | 0 | 0 |
| real face + text | 1 | 1 | 0 |
| AI persona + bold text (+ red arrow) | 0 | 3 | 6 |
| AI object/build + bold text | 2 | 2 | 4 |
| AI object/build, no headline | 0 | 0 | 2 |
| before/after or hot-vs-cold split | 0 | 1 | 4 |
| AI persona + object, no text | 2 | 2 | 1 |
| cartoon / sketch / 3D animation | 4 | 1 | 3 |
| AI cut-away house / buried pipe + claim text | 0 | 2 | 3 |
| AI store front + list text | 0 | 3 | 1 |
| diagram / 3D render explainer | 0 | 0 | 1 |
| **Total** | 10 | 15 | 25 |

Last 90 days, top 30 by multiple:

| Style group | Ranks 1-10 | Ranks 11-25 | Ranks 26+ |
|---|---:|---:|---:|
| real build/product photo + text | 0 | 1 | 0 |
| AI persona + bold text (+ red arrow) | 5 | 6 | 1 |
| AI object/build + bold text | 1 | 6 | 1 |
| real build/product photo, no text | 0 | 1 | 0 |
| AI object/build, no headline | 0 | 0 | 2 |
| cartoon / sketch / 3D animation | 3 | 0 | 0 |
| AI store front + list text | 1 | 1 | 1 |
| **Total** | 10 | 15 | 5 |

### Features by tier

| Feature | Top 100 (n=100) | Top 100 ranks 1-10 (n=10) | Top 100 ranks 1-25 (n=25) | Top 100 ranks 26-100 (n=75) | Recent (all lists) (n=120) | 12m views ranks 1-10 (n=10) | 12m views ranks 1-25 (n=25) | 12m views ranks 26-50 (n=25) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Face shown | 33 (33%) | 4 (40%) | 7 (28%) | 26 (35%) | 57 (48%) | 4 (40%) | 9 (36%) | 13 (52%) |
| Real person | 27 (27%) | 2 (20%) | 4 (16%) | 23 (31%) | 12 (10%) | 1 (10%) | 4 (16%) | 4 (16%) |
| AI person | 4 (4%) | 1 (10%) | 2 (8%) | 2 (3%) | 39 (32%) | 3 (30%) | 5 (20%) | 7 (28%) |
| Cartoon person | 2 (2%) | 1 (10%) | 1 (4%) | 1 (1%) | 6 (5%) | 0 (0%) | 0 (0%) | 2 (8%) |
| Look: realistic photo | 81 (81%) | 7 (70%) | 19 (76%) | 62 (83%) | 16 (13%) | 2 (20%) | 5 (20%) | 4 (16%) |
| Look: AI image | 12 (12%) | 1 (10%) | 3 (12%) | 9 (12%) | 92 (77%) | 8 (80%) | 18 (72%) | 19 (76%) |
| Look: cartoon/animation | 2 (2%) | 1 (10%) | 1 (4%) | 1 (1%) | 8 (7%) | 0 (0%) | 0 (0%) | 2 (8%) |
| Look: graphic/diagram/render | 5 (5%) | 1 (10%) | 2 (8%) | 3 (4%) | 4 (3%) | 0 (0%) | 2 (8%) | 0 (0%) |
| Any headline text | 66 (66%) | 5 (50%) | 14 (56%) | 52 (69%) | 92 (77%) | 5 (50%) | 15 (60%) | 17 (68%) |
| Median words (when text) | 3.0 | 4 | 3.5 | 3.0 | 5.0 | 4 | 4 | 5 |
| Arrow or circle | 21 (21%) | 1 (10%) | 4 (16%) | 17 (23%) | 53 (44%) | 2 (20%) | 11 (44%) | 11 (44%) |
| Red arrow or circle | 13 (13%) | 1 (10%) | 4 (16%) | 9 (12%) | 35 (29%) | 0 (0%) | 6 (24%) | 6 (24%) |
| Before/after or split | 3 (3%) | 0 (0%) | 0 (0%) | 3 (4%) | 17 (14%) | 1 (10%) | 5 (20%) | 2 (8%) |
| Red X / crossed out | 2 (2%) | 0 (0%) | 0 (0%) | 2 (3%) | 6 (5%) | 0 (0%) | 0 (0%) | 1 (4%) |
| Check mark | 2 (2%) | 0 (0%) | 0 (0%) | 2 (3%) | 3 (2%) | 0 (0%) | 1 (4%) | 0 (0%) |

Readings:

- **The very biggest videos use less text, not more.** All-time top 10: 5 of 10 have no headline text (an ice-chest cooler, a waste-oil burner, a real installer with a mini-split, an AI old man at a stove, a bucket cooler); 12-month top 10: 5 of 10 have none. The three biggest 12-month videos by views include two thumbnails with no words at all: an AI old man warming his hands at a home-made stove (`RotAhlS7LQ4`, 11.9M; `H2SrcFJ8g6s`, 7.5M).
- **The no-text winners are "show the thing working":** a flame, a glowing coil, mist, a cut-away. Of the 18 real no-text photos, 17 are in the all-time top 100 (median 4.9M views).
- **Lower down the recent lists, the AI persona + bold words + red arrow style takes over:** 23 of 120 recent thumbnails, 9 of the 90-day top 30 by views and 12 of the 90-day top 30 by multiple, but none in the 12-month top 10 by views. Its median views are lower (545,458 recent) but its median multiple is high (193x): it does well for new, small channels.
- **Red arrows and circles** rise from 13% of the top 100 to 29% of the recent set; **before/after or split** from 3% to 14%.
- **Faces:** a third of the top 100 show a face (27 real, 4 AI); about half of the recent set do, and those are mostly AI (39 AI, 12 real, 6 cartoon).

## Text length and colour

| Words | Top 100: n | Top 100: median views | Recent: n | Recent: median views | Recent: median multiple |
|---|---:|---:|---:|---:|---:|
| 0 (no headline) | 34 | 4,714,882 | 28 | 1,283,488 | 152.9x |
| 1-3 | 35 | 3,554,704 | 30 | 915,496 | 173.1x |
| 4-6 | 24 | 3,718,651 | 33 | 727,226 | 305.3x |
| 7-10 | 4 | 4,232,807 | 17 | 672,609 | 226.6x |
| 11+ | 3 | 3,107,097 | 12 | 306,194 | 354.1x |

Text colour (a thumbnail with several colours counts under each):

| Text colour (mentioned) | Top 100 with text | Recent with text |
|---|---:|---:|
| white | 53 of 66 (80%) | 75 of 92 (82%) |
| yellow | 15 of 66 (23%) | 46 of 92 (50%) |
| red | 16 of 66 (24%) | 41 of 92 (45%) |
| black | 26 of 66 (39%) | 38 of 92 (41%) |
| blue / cyan | 8 of 66 (12%) | 9 of 92 (10%) |
| green | 1 of 66 (2%) | 6 of 92 (7%) |
| orange | 2 of 66 (3%) | 2 of 92 (2%) |

Readings:

- **Short text is the norm:** median 3 words in the top 100, 5 in the recent set (when there is text). Most top 100 headlines are 1-6 words ("ROOM HEATER", "These suck (no, really)", "Stop Buying These", "$5 FIX").
- **Recent thumbnails carry more words** (29 of 92 with text have 7+ words, against 7 of 66 in the top 100): stacked claims such as "ATTIC IS A TRAP" / "75°F YEAR ROUND" / "160°F DEADLY HEAT" / "BURIED SINCE 1824" / "$4 TO BUILD" / "NASA HID THIS" (19 words, `H8-QNBd7MIo`). In the recent lists, more words go with fewer views (11+ words: median 306,194) but a higher multiple (354x): long text is a small-channel style.
- **White is the base colour** (about 80% of thumbnails with text in both sets). **Yellow and red double in the recent set** (yellow 23% to 50%, red 24% to 45%). White plus yellow together: 7 of 66 top 100 thumbnails with text, 33 of 92 recent. Text on a coloured box or banner (red brush stroke, black bar, yellow box): 11 of 66 top 100, 40 of 92 recent.
- The recent house style (my reading): big white condensed capitals, one key word in yellow, a red brush-stroke or red bar under a second line, and a red curved arrow to the object.

## The style groups, with 3 example IDs each

The three biggest videos in each group (views pulled 2026-10-26; list: top100 / 12m / 90d).

- **real build/product photo + text** (38): `OEdzXsloZ7I` (DIY, 12,478,319 views, 367.0x, top100, text: "ROOM HEATER"); `_-mBeYC2KGc` (Technology Connections, 10,392,115 views, 5.6x, top100, text: "These suck (no, really)"); `dHKD-9uI24I` (Google Nest, 8,011,020 views, 16.1x, top100, text: "Connect the wires")
- **real face + text** (29): `6CE72U92R-I` (WINNI, 9,166,055 views, 247.7x, top100, text: "Continues Insulation"); `xZotuV1qkvA` (Kiun B, 6,660,835 views, 1.3x, top100, text: "HOW WE KEEP WARM -71°C"); `k7PSzi7NSyc` (How To Home, 5,633,462 views, 28.2x, top100, text: "What Nobody Tells You")
- **AI persona + bold text (+ red arrow)** (25): `TcZebLi8VsQ` (Kiun B, 5,034,024 views, 0.9x, top100, text: "-64°C" "HOW WE HEAT"); `s-41UF02vrU` (Tech Ingredients, 2,795,163 views, 18.4x, top100, text: "GeoThermal Air Conditioner"); `FsmLvHuA96M` (Japan with Nao, 2,001,906 views, 62.6x, 12m, text: "WINTER HACK")
- **AI object/build + bold text** (22): `WHLuimGVzBA` (The Liberty Engine Project, 5,650,993 views, 154.8x, top100, text: "DIY PORTABLE AIR CONDITIONER!" (plus readout "10 °C 14.7")); `1l4jg_FJ5Yc` (Gem Webb, 3,894,579 views, 819.9x, top100, text: "Power Outage Heat" "NO POWER? Here's the solution."); `SVuQqEXaWdw` (Wild Line, 2,139,032 views, 50.9x, 12m, text: "37°F" "FREE COOLING")
- **real build/product photo, no text** (18): `ITtlxjvLQis` (desertsun02, 15,266,541 views, 2,135.2x, top100, no text); `UawMGmg87ho` (Creative inventions LMTN, 14,880,633 views, 2,807.7x, top100, no text); `I9Td5uMB_vQ` (CrazyRussianHacker, 10,743,855 views, 199.0x, top100, no text)
- **AI object/build, no headline** (18): `h9KS-fcXFjI` (DIY mr.T, 5,618,575 views, 2,043.1x, top100, no text); `dP2PCqUanu0` (Creative DIY365, 5,546,111 views, 462.2x, 12m/top100, no text); `fclBeOvI7FA` (Holic Creation, 3,214,841 views, 229.6x, top100, no text)
- **before/after or hot-vs-cold split** (11): `H514-w6ttNo` (Why Am I Green, 3,708,639 views, 608.0x, 12m/top100, text: "COLDER AIR!" "95°F" "62°F"); `NzjmnIv89Ls` (Fix This House, 3,270,731 views, 251.6x, top100, text: "1970" "2021" "MOTION & HUMIDITY SENSOR!"); `Wejop_Rjpv0` (Silver Cymbal, 3,087,340 views, 38.4x, top100, text: "Old" "4 Hours Later" "DIY")
- **real person on the job, no text** (10): `DzVJiSQNbew` (alpinehomeair, 13,034,823 views, 129.7x, top100, no text); `7WC-gGb0YNY` (Missouri Wind and Solar, 5,827,989 views, 20,377.6x, top100, no text); `ozaw9QhxkQU` (This Old House, 5,272,557 views, 167.4x, top100, no text)
- **AI persona + object, no text** (10): `RotAhlS7LQ4` (Creation Daily, 11,941,053 views, 1,243.9x, 12m/top100, no text); `H2SrcFJ8g6s` (Creative DIY365, 7,535,159 views, 627.9x, 12m/top100, no text); `FGQmj5oA_oY` (Creation Daily, 2,459,044 views, 256.2x, 12m, no text)
- **cartoon / sketch / 3D animation** (10): `gVLhrLTF878` (Sabin Civil Engineering, 8,246,301 views, 37.3x, top100, text: "COLD AIR" "HEAT OUT" "Animation!"); `nVTdukNJdtM` (Mscope, 3,853,724 views, 4.5x, top100, text: "Easy explanation"); `zn5IiwhAxgU` (Sketchy Survival, 1,592,258 views, 1,326.9x, 12m, text: "YOUR AC IS A SCAM")
- **AI cut-away house / buried pipe + claim text** (8): `XJzM-fcrFck` (Construction Odyssey with Eddie, 2,227,816 views, 795.6x, 12m, text: "ILLEGAL COOLING"); `H8-QNBd7MIo` (Elias Yoder, 1,939,171 views, 213.1x, 12m, text: "ATTIC IS A TRAP" "75°F YEAR ROUND" "160°F DEADLY HEAT" "BUR); `--bKaRdZGO4` (Eli Yoder Secrets, 1,275,389 views, 280.3x, 12m, text: "ILLEGAL COOLING" "NASA HID THIS" "55°F" "$300 TOTAL SYSTEM")
- **AI store front + list text** (6): `H1qCDI9DJmY` (Rhett Callahan Prepping, 870,926 views, 128.1x, 90d, text: "11 DOLLAR TREE HEATING ITEMS THAT'LL BE WORTH GOLD IN WINTE); `0AZw4BlV_3Q` (Prep Life Hacks, 440,213 views, 762.9x, 12m, text: "15 HEATING SOURCES" "THAT DON'T NEED ELECTRICITY" "STOCKPIL); `PWAU0mE9R9c` (Prep Life Hacks, 280,332 views, 485.8x, 12m, text: "11 DOLLAR TREE HEATING ITEMS" "THAT'LL BE WORTH GOLD" "IN W)
- **diagram / 3D render explainer** (4): `PI45yUhUWgk` (Undecided with Matt Ferrell, 3,682,492 views, 7.2x, top100, text: "Worth The Cost?"); `qcscUoP8FNk` (Undecided with Matt Ferrell, 2,998,544 views, 5.9x, top100, text: "No Refrigerant?"); `QykwWs3L1W8` (The Engineering Mindset, 2,887,008 views, 3.3x, top100, text: "HEAT PUMPS" "EXPLAINED" (label "R410A"))
- **bold text panel + product cut-out** (3): `7LV5wY-iM34` (Zen Garden Oasis, 12,954,600 views, 281.6x, top100, text: "UNLIMITED HEAT WITH NO ELECTRICITY" + badge "POWER OUTAGE"); `475x-ql8kpw` (Zen Garden Oasis, 1,852,699 views, 40.3x, 12m, text: "MONTHS OF HEAT WITH NO ELECTRICITY"); `KphunxyIbKM` (Zen Garden Oasis, 1,692,856 views, 36.8x, 12m/90d, text: "$4" "DEHUMIDIFIER WORKS FOREVER")
- **AI history scene + red banner** (2): `9-eQiEQOhyo` (Secret State Files, 1,224,700 views, 81.6x, 12m/90d, text: "BEFORE CENTRAL HEATING" "HOW DID THEY STAY WARM?"); `y5kjluBWlEo` (Secret State Files and 4 more, 1,013,392 views, 67.6x, 90d, text: "BEFORE AIR CONDITIONING" "HOW DID THEY SURVIVE?")

Short descriptions (readings):

- **real build/product photo + text:** a real photo of a build or product with a short headline, often white with a black outline or red ("WASTE OIL HEATER!"). Technology Connections (9) is the biggest user.
- **real face + text:** a real YouTuber's face (shocked, pointing, sceptical) beside the equipment, with 2-6 words; contractor channels (How To Home, The DIY HVAC Guy) and big creators.
- **AI persona + bold text (+ red arrow):** an AI-made older tradesman or homemaker (often grey hair, navy work shirt, name patch such as "RAY" or "Mike", or an Amish or Asian persona) pointing at the object; bold white/yellow text on a red brush stroke; red arrow or circle.
- **AI object/build + bold text:** an AI picture of a build or product with a claim ("NASA SECRET", "FREE COOLING", "OIL FILLTER HACK!").
- **real build/product photo, no text:** a real photo of a home-made heater or cooler working, or a real product, and nothing else. The biggest all-time group by median views.
- **AI object/build, no headline:** an AI build glowing or flaming on a table or outdoors (Creative DIY365 made 11 of 18).
- **before/after or hot-vs-cold split:** a split frame, old/new, wrong/right (red X, green check) or hot/cold with temperature readouts.
- **real person on the job, no text:** a real person installing or using equipment; no words (This Old House, Alpine Home Air).
- **AI persona + object, no text:** an AI old man (white beard, flat cap, sherpa jacket) or Amish/Viking figure warming his hands at a home-made stove; no words.
- **cartoon / sketch / 3D animation:** cartoon Egyptians or Vikings, ink sketches with one colour highlight, 3D teaching animations.
- **AI cut-away house / buried pipe + claim text:** an AI cut-away of a house and the ground, a glowing buried pipe or cool air, with a forbidden-knowledge claim ("ILLEGAL COOLING", "NASA HID THIS").
- **AI store front + list text:** a snowy Dollar Tree or Walmart front with a list headline ("11 DOLLAR TREE HEATING ITEMS THAT'LL BE WORTH GOLD IN WINTER BLACKOUT"); prepper channels.
- **diagram / 3D render explainer:** a clean diagram or 3D render with a 2-4 word question ("Worth The Cost?").
- **bold text panel + product cut-out:** big black-and-red text stacked on white beside a product photo (all three from Zen Garden Oasis).
- **AI history scene + red banner:** a sepia AI history scene with a portrait and "BEFORE ... HOW DID THEY ...?" on a red banner (Secret State Files).

## Caveats

- Every label is a reading by one helper; the real/AI calls are the weakest. A second helper should re-check a sample against the images before the operator sees this.
- The style is mixed up with the upload year and with the channel: some groups are mostly one channel (Creative DIY365, Zen Garden Oasis, Technology Connections, Secret State Files), so a group's views partly measure that channel.
- Thumbnails are as of 2026-10-26; old videos may have new thumbnails.
- Channel top-5 thumbnails (the brief's third set) are not in this file.
