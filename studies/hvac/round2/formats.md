# HVAC round 2: formats in the keyword sweep

Built 2026-10-24 by a round 2 helper with `studies/hvac/data/tools/sweep_build.py` from the keyword sweep (`keyword-sweep.md` has the method, sources and filters). Deliverable 8 of `RESEARCH-BRIEF.md`.

**Status:** not yet re-checked by a second helper. **Every format tag here is rule-based** (regular expressions on the title), not a reading of the video. The hand-check below is the helper's reading.

## How titles were tagged

- One main format per video, from the title only (no thumbnails), following the ordered rules in `labels.md` section 3: test, X vs Y, the only X, review, myth-bust, Y doesn't want you to know, mistakes, before you do X, news-warning, cheap hack, symptom-fix, install/DIY project, how-to, explainer, story. The **first** rule that matches wins; a title that matches none is "plain topic/other". (The helper brief listed the formats in a different order; the labels.md order was used, as the brief asked.)
- The rules are `FORMAT_RULES` in the script. A trailing "| channel name" is stripped before matching. A list shape ("Top 10", "5 things") is not a format, as labels.md says.
- Thumbnail text is not read here, so a title that is only a topic label ("Furnace Filters") stays "plain topic/other" even where labels.md would read the thumbnail.
- **Above their search median** (a within-search relative measure): each time a video showed up in a search (with at least 5 kept long-form English results), did its views beat that search's median? The figure is the share of the format's appearances that did (counts in brackets). The all-videos row is the baseline (a little under 50% by construction); a format above it beats the other videos returned for the same keywords. Full definition in `keyword-sweep.md`.
- **Last 12 months** = age text below "1y ago" (approximate). 7,902 of 25,618 videos.

## Format table

### All time (25,618 videos)

| Format (rule-based) | Videos | Channels | Median views | Above their search median | 3 biggest (title, channel, views, ID) |
|---|---:|---:|---:|---:|---|
| test | 375 | 316 | 29,285 | 50% (630 of 1,265 appearances) | "Experiments with fan capacitor" (Let's See Inside, 10,449,175, `wRiNTWB3hrE`)<br>"Primitive Technology: 2.5 m Natural draft furnace experiment" (Primitive Technology, 4,570,107, `XD4jvdjAMA8`)<br>"As Seen On TV Money-Saving Gadgets TESTED!" (Household Hacker, 4,543,626, `g6gzXaozevE`) |
| X vs Y | 1,101 | 791 | 35,249 | 42% (1,151 of 2,749 appearances) | "HOT VS COLD Challenge Ryan vs Daddy 1hr Kids Show" (Ryan's World, 116,259,579, `SCyFBeIgaDc`)<br>"FULL MATCH: Roman Reigns vs. Randy Orton vs. Kane vs. John Cena –Title Match: WWE Battleground 2014" (WWE, 94,521,566, `wk5EeNzH17o`)<br>"HOT VS COLD ROOM Challenge with Emma and Kate!!" (Kaji Family, 57,986,505, `j6MHN1TPlFA`) |
| the only X | 1,504 | 955 | 11,532 | 42% (1,874 of 4,502 appearances) | "Masha And The Bear 🌞🏖 Summer Holidays🏖🌞 Best episodes cartoon collection 🎬" (Masha and The Bear, 435,536,745, `jCvSEuHms5M`)<br>"স্কুল জীবন \|\| School Jibon \|\| Bengali Best Funny Video 2025 \|\| Baccha Party School" (Baccha Party School , 40,677,948, `8YyoNcjqq-M`)<br>"1st January \|\| পয়লা জানুয়ারি \|\| Bengali Best Funny Video 2025 \|\| Baccha Party School " (Baccha Party School , 30,314,679, `3QYVojJAz6w`) |
| review | 679 | 577 | 18,303 | 43% (627 of 1,465 appearances) | "Mini Fan Humidifier - Air Conditioner Water Spray Fashion Fan \| Unboxing And Review" (Unboxing TV, 14,259,602, `aQ4tLjPelrE`)<br>"Are Aftermarket Intakes Even Worth It?" (Donut, 9,328,614, `q9ZcPtvTKpY`)<br>"Mini Air Conditioner Fan - Cheap Air Cooler Fan USB, Spray Humidifier Water \| Unboxing & Review" (Unboxing TV, 5,064,028, `Lve3CHhypII`) |
| myth-bust | 149 | 132 | 12,989 | 42% (209 of 496 appearances) | "Electric SuperChargers Mythbusted" (Mighty Car Mods, 8,284,574, `cbGWgvJN1_8`)<br>"Did Jamie Enjoy Making MythBusters?" (Adam Savage’s Tested, 3,207,462, `awNKlpxvdrI`)<br>"Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,719, `SVuQqEXaWdw`) |
| Y doesn't want you to know | 788 | 573 | 23,506 | 53% (1,336 of 2,542 appearances) | "Oil change scams: Hidden camera investigation on what really happens to your car (CBC Marketplace)" (CBC News, 48,175,189, `-avpx8UTakI`)<br>"32 Secret Combinations on Your Keyboard" (BRIGHT SIDE, 24,275,215, `WGuFofNF1Pk`)<br>"The Secret Caulking Tip That Will Transform Your Ability!" (The Funny Carpenter, 16,789,508, `cQNIv2QqP00`) |
| mistakes | 407 | 334 | 8,914 | 50% (509 of 1,024 appearances) | "10 Beginner Mistakes Installing Vinyl Plank Flooring" (Fix This Build That, 15,713,486, `kvo-n2AYZnA`)<br>"The ONE Big Mistake That's Making You Colder" (MyLifeOutdoors, 6,818,822, `-Ogv5_xT6S4`)<br>"10 Ways You're Using Your Computer WRONG!" (ThioJoe, 6,269,112, `IbuKffs7wmg`) |
| before you do X | 205 | 182 | 10,547 | 55% (420 of 759 appearances) | "Thinking About Finishing Your Basement? Watch This First!" (Home RenoVision DIY, 1,643,771, `kxMLd3LNwcQ`)<br>"Mini Split - 3 Things I Wish I Knew Before Installing" (LRN2DIY, 1,526,472, `b67w0gEqHe8`)<br>"Watch This Before You Renovate a Mobile Home - Weight and Structure" (DIYfferent, 1,262,129, `sCx_6a3kYyg`) |
| news-warning | 156 | 144 | 44,664 | 70% (337 of 484 appearances) | "Big & Deadly ELECTRIC EELS - Amazon River Monsters" (billschannel, 11,553,950, `GomeIaCmQPw`)<br>"Why India's Air is So Deadly (And Getting Worse!) \| Dhruv Rathee" (Dhruv Rathee, 9,820,522, `Fzs5fEbT4ic`)<br>"Why Cocaine Is So Incredibly Dangerous" (Institute of Human Anatomy, 7,000,173, `pu5AaVqYuP4`) |
| cheap hack | 1,156 | 906 | 34,302 | 50% (1,842 of 3,713 appearances) | "INCREDIBLE ROOM MAKEOVER IDEAS \|\| Low-Budget Decor Crafts" (5-Minute Crafts, 76,850,950, `OGvhmFZwY0s`)<br>"UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,348, `7LV5wY-iM34`)<br>"how to lower your electric bill ... Oncor said I was meter tampering Really !" (ranchitout, 9,461,124, `OgKQihUEFA0`) |
| symptom-fix | 2,513 | 1,484 | 29,733 | 46% (4,206 of 9,103 appearances) | "How to Fix a Car with No Heat (Easy)" (ChrisFix, 9,796,051, `-XjXTVJhFLM`)<br>"Why Didn’t I Know This! Spray WD-40 on Foam and Fix Any Broken Plastic in Your Home!" (Inventor Hacks, 8,776,083, `pXWAABQj0-g`)<br>"Crazy Heat Wave & Broken Air Conditioning! The Big Chill \| The Casagrandes" (The Loud House, 8,414,606, `xcoJAg8ncSU`) |
| install/DIY project | 2,017 | 1,452 | 58,390 | 51% (2,988 of 5,824 appearances) | "Outdoor wood stove from red brick and cement" (Creative Cement, 38,516,965, `EElfn2tYqmA`)<br>"Outdoor multifunctional wood stove _ Creative ideas from cement and non iron barrels" (Creative Project, 35,431,524, `l8Dly23Ey3I`)<br>"How to make a 2 in 1 wood stove from red brick and cement is simple and beautiful" (Creative Cement, 31,536,711, `PJARXm7UG5Y`) |
| how-to | 6,251 | 4,061 | 42,259 | 48% (8,241 of 17,003 appearances) | "Winter Survival Shelter, Stay Warm Overnight With No Fire" (Scavenger Survival, 19,456,552, `lwv-vKYJV1o`)<br>"How to SUPER FLUSH your Cars Cooling System" (ChrisFix, 19,323,840, `s--5ft5YiHg`)<br>"DIY wonderful wood stove (2 in 1) from old gas stove # 157" (Penpen vn 1, 17,864,140, `lGdv_nMzVo4`) |
| explainer | 1,508 | 997 | 39,162 | 53% (2,441 of 4,637 appearances) | "Why Are 96,000,000 Black Balls on This Reservoir?" (Veritasium, 112,818,293, `uxPdPpi5W4o`)<br>"30 minute fat burning home workout for beginners. Achievable, low impact results." (Body Project, 59,983,836, `gC_L9qAHVJ8`)<br>"Could Solar Storms Destroy Civilization? Solar Flares & Coronal Mass Ejections" (Kurzgesagt – In a Nutshell, 15,421,439, `oHHSSJDJ4oo`) |
| story | 283 | 235 | 41,325 | 54% (370 of 688 appearances) | "Dugout Shelter Under 10ft (3m) of Snow - Solo Camping in Survival Shelter During Snow Storm" (Outdoor Boys, 97,243,887, `wcDFgir_jgY`)<br>"I Turned My House Into a Trampoline Park!" (Unspeakable, 79,772,408, `lSSWH4NOdgE`)<br>"HOT ROCKS in my Bushcraft Cot - Winter Camping in Alaska with a Survival Shelter" (Outdoor Boys, 29,993,901, `FtdIcmgfy_w`) |
| plain topic/other | 6,526 | 4,524 | 33,156 | 46% (5,458 of 11,885 appearances) | "Ice Cube - It Was A Good Day" (Ice Cube / Cubevision, 396,896,882, `h4UqMyldS7Q`)<br>"White Noise Black Screen \| Sleep, Study, Focus \| 10 Hours" (Relaxing White Noise, 384,357,623, `nMfPqeZjc2c`)<br>"AC/DC - Thunderstruck (Live At River Plate, December 2009)" (AC/DC, 378,894,765, `n_GFN3a0yj0`) |
| **all** | **25,618** | **13,708** | **33,924** | **48%** (32,639 of 68,139) | |

### Last 12 months (7,902 videos)

| Format (rule-based) | Videos | Channels | Median views | Above their search median | 3 biggest (title, channel, views, ID) |
|---|---:|---:|---:|---:|---|
| test | 157 | 142 | 9,823 | 38% (213 of 564 appearances) | "Primitive Technology: Grate furnace, wood fired smelting experiment" (Primitive Technology, 2,750,290, `eIBEK-_NMJc`)<br>"We Tested Every Air Purifier! One Clear Winner!" (Project Farm, 1,141,385, `sQGfO4hNb60`)<br>"Linux vs. Windows 11 Speed Test (Lab Tested)" (PhoneBuff, 1,136,349, `KqtlpqeYhjM`) |
| X vs Y | 414 | 310 | 10,866 | 28% (265 of 940 appearances) | "Mac vs Windows - It's not close in 2026!" (Mrwhosetheboss, 9,746,912, `aJSK3HZlvnU`)<br>"Learn Colors with Escape Room \| Cold VS Hot \| Nursery Rhyme & Kids Songs \| BabyBus" (BabyBus - Preschool Songs & Learning Cartoons, 4,991,413, `whag0zYhlUU`)<br>"MARK vs SCHOOL BULLIES \| Funniest School Compilation" (Comedy Dose, 3,187,146, `Efg9e3_wF8I`) |
| the only X | 772 | 507 | 2,964 | 27% (501 of 1,884 appearances) | "1st January \|\| পয়লা জানুয়ারি \|\| Bengali Best Funny Video 2025 \|\| Baccha Party School " (Baccha Party School , 30,314,679, `3QYVojJAz6w`)<br>"স্কুলে ক্রাশ \|\| School e Crush \|\| Bengali Best Funny Video 2026 \|\| Baccha Party School " (Baccha Party School , 29,873,643, `oX99q8Www74`)<br>"স্কুল জীবন \|\| School Jibon \|\| Bengali Best Funny Video 2025 \|\| Baccha Party School " (Baccha Party School , 10,428,573, `lSpVw_tYIj0`) |
| review | 192 | 174 | 4,206 | 25% (94 of 376 appearances) | "Portable Mini Viral AC Review Hindi \| Scam or Useful?" (Tanu Superstar, 1,382,659, `M3MC5bb13UU`)<br>"Crawlspace Dehumidifier Review: AlorAir 70 PPD Helios D35 – Is it Right for Your 1000 sq ft Space?" (DailyTested, 1,002,301, `4tmKS-GY2tQ`)<br>"MINI AC For Room Cooling ₹2000😱🥶 Unboxing & Review I Small AC" (Neerazz Tech, 644,660, `xZDn9J6BZY0`) |
| myth-bust | 53 | 50 | 5,746 | 40% (46 of 114 appearances) | "Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,719, `SVuQqEXaWdw`)<br>"Proof That Most Water Purifiers Don’t Work!" (Project Farm, 2,066,106, `3g14JtDrkNY`)<br>"Stop Running Your AC This Summer. Build This $40 Underground Pipe in One Weekend." (Builds With Eli Yoder, 726,882, `nPf7eZfpVxw`) |
| Y doesn't want you to know | 450 | 358 | 4,828 | 42% (568 of 1,347 appearances) | "FREE Heat All Winter😱!! Millions of people don't know this secret! No Gas, No Electricity" (Creation Daily, 11,838,449, `RotAhlS7LQ4`)<br>"Millions Don’t Know That Waste Oil Is a Gold Mine! DIY 3-in-1 Heating Stove" (Creative inventions LMTN, 7,559,944, `ZVlv3r1KQyo`)<br>"AI Whistleblower: We Are Being Gaslit By AI Companies, They’re Hiding The Truth! - Karen Hao" (The Diary Of A CEO, 5,567,669, `Cn8HBj8QAbk`) |
| mistakes | 255 | 211 | 1,668 | 41% (232 of 565 appearances) | "Aliens Are Making Contact 3,000 Years Ahead; Warning We’re Making BIG Mistakes. Darryl Anka \| Bashar" (Dr. Mayim Bialik, 2,594,568, `QBk2MQ1MVZo`)<br>"Stop Wasting Money! Most Homeowners Are Insulating Walls Wrong" (Everyday Home Repairs and Everyday Shed, 1,695,722, `2DuwMoezQLA`)<br>"The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,507, `K2jCz3D5z_0`) |
| before you do X | 115 | 101 | 1,303 | 39% (144 of 365 appearances) | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,971, `dOZ-8__G4uU`)<br>"Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,114, `mP0IjyvQtxw`)<br>"Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night)" (Ray Dutton's Garage, 934,752, `fHAlfm21vYw`) |
| news-warning | 85 | 82 | 9,275 | 45% (76 of 169 appearances) | "I Bought a Banned Chinese Car From a Rental Company for $2,000" (Rich Rebuilds, 2,741,910, `Jdm8qnlnzqc`)<br>"The $4 Amish Fix for a Deadly Hot House (Save $3000 This Summer)" (Elias Yoder, 1,937,923, `H8-QNBd7MIo`)<br>"FLORIDA HIT BY HURRICANE ISAIAS — Severe Flooding, Widespread Power Outages & Dangerous Conditions" (US Housing Report, 1,554,357, `FmruBdrbiQs`) |
| cheap hack | 561 | 452 | 7,077 | 44% (726 of 1,635 appearances) | "No Gas, No Wood 😱!! This Simple DIY Stove Heats for FREE All Winter" (Creative DIY365, 7,514,245, `H2SrcFJ8g6s`)<br>"UNLIMITED Heat For Your Home Or Greenhouse \| No Electric Needed" (Zen Garden Oasis, 4,010,110, `kO3rWyULVYY`)<br>"Drywall Is Dead. Do This Instead." (HAXMAN, 3,227,936, `ji5UfRIVAvI`) |
| symptom-fix | 609 | 434 | 3,275 | 19% (276 of 1,436 appearances) | "The Windows Laptop Problem" (Marques Brownlee, 6,045,597, `eXa2ndhmatI`)<br>"OUR ROOMMATE WON’T STOP GROWING!" (Spy Ninjas Crew and Vy Qwaint, 3,325,462, `ubO_hrwhfpM`)<br>"Broken Bone Healing Process \| How Plaster Helps in Fracture? \| Bone Fractures \| Dr. Binocs Show" (Peekaboo Kidz, 2,092,927, `51rdY8554SU`) |
| install/DIY project | 348 | 303 | 10,047 | 29% (238 of 821 appearances) | "I Built an Insane 260W LASER That Cuts Metal !" (Skill Make, 2,172,097, `mNP-5Oo2aTo`)<br>"Building a Heat System for the Garage Apron to Stay Ice-Free in Arctic Winter" (M. Bjoernstroem, 1,465,767, `OGokIsjjuB4`)<br>"Sculpting a Life Size Alien in 20 Days" (Jon Laymon Studios, 1,435,080, `eIqLN6zGff0`) |
| how-to | 1,135 | 897 | 4,959 | 22% (508 of 2,321 appearances) | "I Bought Costco's CHEAPEST Solar Setup" (Footprint Hero with Alex Beale, 4,820,056, `RUOzvpwy8-8`)<br>"Why I left Linus Tech Tips" (jakkuh, 4,811,814, `gqVxgcKQO2E`)<br>"Turn Any Fan Into an Air Conditioner with 2 Ice Bottles ($0 DIY AC)" (Why Am I Green, 3,707,998, `H514-w6ttNo`) |
| explainer | 454 | 352 | 4,467 | 25% (233 of 914 appearances) | "Steve Ballmer Explains The Cost of Oil" (USAFacts, 10,751,181, `KEiKy6mf2Ew`)<br>"Why HMRC Doesn’t Want You to Understand This" (Your Accountant, 2,854,341, `tcpBWjAikxM`)<br>"Why Buy A Generator? You Have One Parked In Your Driveway." (The DIY HVAC Guy, 2,447,759, `Qx3cC1y23JY`) |
| story | 152 | 143 | 24,802 | 44% (151 of 347 appearances) | "I Secretly Hid a Viral Toy Store In My House!" (Zhong, 4,323,830, `3hXzig1a9XQ`)<br>"EXTREME Carpathian Bushcraft Yurt Build! Warm Survival Shelter in the Snow" (Lost in Mountains: Carpathians, 1,785,137, `E3nh4XCoxSE`)<br>"Surviving Power Outages \| Storm Prep \| EcoFlow Home Backup Solutions \| Delta Pro Ultra X" (HOBOTECH, 1,691,697, `3jPucpWphR0`) |
| plain topic/other | 2,150 | 1,674 | 12,131 | 35% (1,310 of 3,691 appearances) | "Funny Kids Adventures with Magic Air Conditioner" (Vlad and Niki, 23,456,370, `BbhASJOsWms`)<br>"Happy Valentine's Day 2026 \|\| হ্যাপি ভ্যালেন্টাইনস ডে 2026 \|\| Baccha Party School " (Baccha Party School , 16,559,743, `NJRFtHSgjVI`)<br>"6-MIN IMMERSIVE CARDIO WARM-UP – FULL BODY INTERACTIVE WORKOUT" (Immersive Fit, 15,133,806, `GnY20VHLxAg`) |
| **all** | **7,902** | **4,939** | **6,206** | **32%** (5,581 of 17,489) | |

### The same, only videos with a home-HVAC word in the title

Broad EXTENDED keywords pull in many off-topic videos (games, sports, car AC, Indian-market TV). As a rough cut, this keeps only titles that pass the round 1 keyword filter (`is_hvac` in `tools/autocomplete.py`: a strong HVAC word, or a weak one plus a home word, and no excluded word such as car, game, hours, Hindi). Rule-based and strict: it also drops some on-topic titles (for example any title with "hours"). 16,270 of 25,618 videos pass; 4,880 in the last 12 months. The above-median share still compares each video with all the long-form English videos in its searches.

### HVAC-word titles, all time (16,270 videos)

| Format (rule-based) | Videos | Channels | Median views | Above their search median | 3 biggest (title, channel, views, ID) |
|---|---:|---:|---:|---:|---|
| test | 251 | 210 | 19,805 | 48% (479 of 998 appearances) | "Experiments with fan capacitor" (Let's See Inside, 10,449,175, `wRiNTWB3hrE`)<br>"Primitive Technology: 2.5 m Natural draft furnace experiment" (Primitive Technology, 4,570,107, `XD4jvdjAMA8`)<br>"Testing The Burn Ability Of Insulation In Wall" (post 10, 3,153,216, `CdItsso3ur0`) |
| X vs Y | 675 | 522 | 20,694 | 40% (845 of 2,112 appearances) | "HOT VS COLD ROOM Challenge with Emma and Kate!!" (Kaji Family, 57,986,505, `j6MHN1TPlFA`)<br>"Diana and Roma play Hot vs Cold Challenge" (Diana and Roma World, 27,257,093, `hkdTSZzARZw`)<br>"Bug's Hot vs Cold Roommate" (Little Big Toys, 23,029,697, `jeatQUn03-o`) |
| the only X | 1,080 | 687 | 5,918 | 40% (1,529 of 3,790 appearances) | "Best fan placement to move air through the house" (Matthias random stuff, 11,467,376, `1L2ef1CP-yw`)<br>"Best Water Filter? Brita, ZeroWater, PUR, Berkey, Aquaphor, AquaTrue" (Project Farm, 4,374,897, `ja0ioX6GSz0`)<br>"Top 5 Things AC Companies Don't Want You To Know How To Do!" (How To Home, 2,980,017, `AQQH9QwC46A`) |
| review | 414 | 360 | 17,074 | 42% (448 of 1,061 appearances) | "Free heating fuel but it's illegal - £120 8kw Diesel parking heater review from VEVOR" (Joshua De Lisle , 4,997,239, `KyiUpFjwtlU`)<br>"(1 YEAR REVIEW) black & decker “portable air conditioner” 12000 btu" (Live Free, 3,720,902, `RJQyCq9R6Cs`)<br>"Basic Vent Modes MADE EASY - Ventilator Settings Reviewed" (ICU Advantage, 2,132,742, `E5uLM41URmE`) |
| myth-bust | 88 | 84 | 6,560 | 39% (154 of 393 appearances) | "Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,719, `SVuQqEXaWdw`)<br>"Why You Need To Stop Using These Filters To Purify Your Air!  What To Use Instead" (How To Home, 1,901,852, `6PcBk2umEWA`)<br>"Stop Cleaning Your A/C Coils The Hard Way! Do This To Get Colder Air From Your Vents." (The DIY HVAC Guy, 1,394,646, `6APa3OUc0RI`) |
| Y doesn't want you to know | 551 | 402 | 9,106 | 53% (1,114 of 2,116 appearances) | "Millions of people do not know this knowledge! 3 in 1 waste oil heater! Warm for winter 2024" (Creative inventions LMTN, 14,876,623, `UawMGmg87ho`)<br>"FREE Heat All Winter😱!! Millions of people don't know this secret! No Gas, No Electricity" (Creation Daily, 11,838,449, `RotAhlS7LQ4`)<br>"Millions Don’t Know That Waste Oil Is a Gold Mine! DIY 3-in-1 Heating Stove" (Creative inventions LMTN, 7,559,944, `ZVlv3r1KQyo`) |
| mistakes | 269 | 213 | 2,648 | 50% (423 of 838 appearances) | "5 Furnace Filter Mistakes That Will Cost You Money!" (The Funny Carpenter, 2,871,907, `_g8gQ1gg1FM`)<br>"7 Backup Generator Mistakes. (Have You Made One?)" (Backyard Maine, 2,557,104, `jNuVsFeL7vY`)<br>"Insulation: 5 steps to a more efficient building and why I don't use spray foam" (RR Buildings, 2,208,868, `OUYCbQSErAU`) |
| before you do X | 147 | 136 | 7,456 | 56% (362 of 644 appearances) | "Mini Split - 3 Things I Wish I Knew Before Installing" (LRN2DIY, 1,526,472, `b67w0gEqHe8`)<br>"Think Twice Before Buying Reusable Air Filters: Here is Why" (FordTechMakuloco, 1,235,340, `NJKlb61_kXU`)<br>"Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,114, `mP0IjyvQtxw`) |
| news-warning | 95 | 88 | 16,238 | 74% (289 of 389 appearances) | "Heat Pumps: the Future of Home Heating" (Technology Connections, 4,844,784, `7J52mDjZzto`)<br>"The clever feature that makes cheap heaters safe — and why they're actually dangerous" (Technology Connections, 2,949,072, `HnMuNCl7tZ8`)<br>"Dangerous Old Radiator - Restoration" (TysyTube Restoration, 2,474,355, `LAIPnLQnmQw`) |
| cheap hack | 846 | 677 | 23,176 | 49% (1,481 of 3,043 appearances) | "UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,348, `7LV5wY-iM34`)<br>"how to lower your electric bill ... Oncor said I was meter tampering Really !" (ranchitout, 9,461,124, `OgKQihUEFA0`)<br>"Easy, Cheap, POWERFUL Bow (NO Power Tools or Heat Needed)" (ZNA Productions, 8,540,160, `0XofhpYmaEU`) |
| symptom-fix | 1,836 | 1,056 | 24,144 | 46% (3,560 of 7,785 appearances) | "Crazy Heat Wave & Broken Air Conditioning! The Big Chill \| The Casagrandes" (The Loud House, 8,414,606, `xcoJAg8ncSU`)<br>"EASY - How to STOP CONDENSATION - Get Rid of Black Mold and Clean Mould" (Fixmyroof, 6,835,028, `Oj99RNY55Es`)<br>"THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,898, `J95l9Ue4224`) |
| install/DIY project | 1,556 | 1,110 | 59,099 | 52% (2,613 of 5,044 appearances) | "Outdoor wood stove from red brick and cement" (Creative Cement, 38,516,965, `EElfn2tYqmA`)<br>"Outdoor multifunctional wood stove _ Creative ideas from cement and non iron barrels" (Creative Project, 35,431,524, `l8Dly23Ey3I`)<br>"How to make a 2 in 1 wood stove from red brick and cement is simple and beautiful" (Creative Cement, 31,536,711, `PJARXm7UG5Y`) |
| how-to | 4,028 | 2,646 | 37,902 | 48% (6,476 of 13,398 appearances) | "Winter Survival Shelter, Stay Warm Overnight With No Fire" (Scavenger Survival, 19,456,552, `lwv-vKYJV1o`)<br>"DIY wonderful wood stove (2 in 1) from old gas stove # 157" (Penpen vn 1, 17,864,140, `lGdv_nMzVo4`)<br>"How To Make An Electrical Arc Furnace" (TKOR, 14,668,783, `VTzKIs19eZE`) |
| explainer | 973 | 664 | 27,294 | 53% (1,950 of 3,679 appearances) | "Capacitors Explained - The basics how capacitors work working principle" (The Engineering Mindset, 11,078,060, `X4EUwTwZ110`)<br>"Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`)<br>"DON'T SUBSCRIBE \| How does your AIR CONDITIONER work?" (Sabin Civil Engineering, 8,245,248, `gVLhrLTF878`) |
| story | 146 | 116 | 42,654 | 58% (284 of 491 appearances) | "HOT ROCKS in my Bushcraft Cot - Winter Camping in Alaska with a Survival Shelter" (Outdoor Boys, 29,993,901, `FtdIcmgfy_w`)<br>"Ceiling fans in my house running on all speeds" (Warrenfanguy205, 5,220,030, `NPhsWRXt9LU`)<br>"I Made a BIG Furnace to Melt Metals" (Black Beard Projects, 4,651,936, `yDBTageZeM0`) |
| plain topic/other | 3,315 | 2,379 | 16,760 | 43% (3,005 of 6,984 appearances) | "Jason plays the Hot and Cold Challenge" (Jason Vlogs, 65,645,927, `o1cW9Cv3rWM`)<br>"Ac Ac Ac Dance \|\| New Bhojpuri Dance \|\| लहंगा AC खोजता \|\| Superhit Stage Dance 2024 \|\| @BubunMusic" (Bubun Music, 49,832,001, `8yu27pUBtmA`)<br>"Thermal Power Plant \| Boiler \| Economizer \| Turbine \| Khan GS Research Centre" (Khan GS Research Centre, 46,262,120, `m4CwaKTQikw`) |
| **all** | **16,270** | **8,793** | **24,330** | **47%** (25,012 of 52,765) | |

### HVAC-word titles, last 12 months (4,880 videos)

| Format (rule-based) | Videos | Channels | Median views | Above their search median | 3 biggest (title, channel, views, ID) |
|---|---:|---:|---:|---:|---|
| test | 108 | 97 | 4,632 | 38% (182 of 479 appearances) | "We Tested Every Air Purifier! One Clear Winner!" (Project Farm, 1,141,385, `sQGfO4hNb60`)<br>"Coldest and Quietest Air Conditioner Ever Tested!" (Project Farm, 1,100,040, `BSTkKiJPeaQ`)<br>"Heat Pumps Explained — And Tested \| Guy Martin" (Guy Martin , 819,256, `jbWQV2DTb3Q`) |
| X vs Y | 247 | 206 | 3,100 | 22% (146 of 673 appearances) | "Mac vs Windows - It's not close in 2026!" (Mrwhosetheboss, 9,746,912, `aJSK3HZlvnU`)<br>"Extreme HOT vs COLD Room Survival Challenge \| Mad Brothers" (Mad Brothers and 2 more, 1,364,079, `Bqs_w-gY32c`)<br>"Mac vs Windows in 2026 - It's a Disaster" (Just Josh, 1,167,282, `Paj0IAIHxDM`) |
| the only X | 545 | 377 | 1,442 | 24% (368 of 1,537 appearances) | "SIDEMEN FIGHT TO BUILD THE BEST $20 DRAFT" (SidemenReacts, 2,160,949, `B9BrzofcYd8`)<br>"Latest Laminate flooring price 2026 \| Wooden flooring cost labour, material cost \| best brand AC1,AC" (Construction Zone, 1,036,201, `JhyKThgi51Q`)<br>"Best AC Under 30000 \| Best AC 2026 \| AC Buying Guide 2026" (Vineet Malhotra, 904,812, `Ax_ivx5AOGw`) |
| review | 116 | 105 | 2,364 | 22% (57 of 256 appearances) | "Crawlspace Dehumidifier Review: AlorAir 70 PPD Helios D35 – Is it Right for Your 1000 sq ft Space?" (DailyTested, 1,002,301, `4tmKS-GY2tQ`)<br>"Mitsubishi MXZ-2D20NL Outdoor Unit Review \| Multi Zone Ductless Mini Split Heat Pump" (Got Ductless, 432,288, `7zQ1Y3lc3NI`)<br>"Mitsubishi MXZ-4D30NL Review \| Multi Zone Ductless Mini Split Heat Pump System" (Got Ductless, 395,227, `CpH4j-cJh0g`) |
| myth-bust | 38 | 37 | 856 | 40% (34 of 86 appearances) | "Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,719, `SVuQqEXaWdw`)<br>"Stop Running Your AC This Summer. Build This $40 Underground Pipe in One Weekend." (Builds With Eli Yoder, 726,882, `nPf7eZfpVxw`)<br>"Stop Running Your AC This Summer. Bury This $60 Cool Loop in Your Yard in One Weekend." (The Passive House Files, 534,591, `kB1hjHgr_y4`) |
| Y doesn't want you to know | 314 | 252 | 2,148 | 41% (453 of 1,093 appearances) | "FREE Heat All Winter😱!! Millions of people don't know this secret! No Gas, No Electricity" (Creation Daily, 11,838,449, `RotAhlS7LQ4`)<br>"Millions Don’t Know That Waste Oil Is a Gold Mine! DIY 3-in-1 Heating Stove" (Creative inventions LMTN, 7,559,944, `ZVlv3r1KQyo`)<br>"Don’t Throw Away Your Old Electric Fan Motor! Billions Don't Know THIS SECRET!" (Hack & Craft, 2,086,314, `cZ12B1tTyEI`) |
| mistakes | 184 | 143 | 752 | 43% (208 of 482 appearances) | "Stop Wasting Money! Most Homeowners Are Insulating Walls Wrong" (Everyday Home Repairs and Everyday Shed, 1,695,722, `2DuwMoezQLA`)<br>"The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,507, `K2jCz3D5z_0`)<br>"The Generator Mistake Everyone Makes!" (Backyard Maine, 1,049,146, `gchq6G5Wc8M`) |
| before you do X | 86 | 79 | 1,220 | 38% (115 of 299 appearances) | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,114, `mP0IjyvQtxw`)<br>"Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night)" (Ray Dutton's Garage, 934,752, `fHAlfm21vYw`)<br>"Watch This Before Buying a Cheap Electric Heater" (Proper DIY - Tools & Effect, 877,592, `5NyK6Aoz2Vw`) |
| news-warning | 49 | 48 | 2,712 | 48% (59 of 122 appearances) | "The $4 Amish Fix for a Deadly Hot House (Save $3000 This Summer)" (Elias Yoder, 1,937,923, `H8-QNBd7MIo`)<br>"FLORIDA HIT BY HURRICANE ISAIAS — Severe Flooding, Widespread Power Outages & Dangerous Conditions" (US Housing Report, 1,554,357, `FmruBdrbiQs`)<br>"This Home Costs $300 to Build and $0 to Heat FOREVER. Why Is It Banned?" (Lost Build Archives, 1,452,778, `5fe3rP92hjY`) |
| cheap hack | 442 | 362 | 5,320 | 44% (611 of 1,385 appearances) | "No Gas, No Wood 😱!! This Simple DIY Stove Heats for FREE All Winter" (Creative DIY365, 7,514,245, `H2SrcFJ8g6s`)<br>"Small plug-in solar panels gain traction as an affordable way to cut electricity bills" (PBS NewsHour and KQED, 3,057,508, `yVO9GcNlkLQ`)<br>"No Central Heating? Here's What Japanese Homes Do Instead" (Japan with Nao, 1,916,239, `FsmLvHuA96M`) |
| symptom-fix | 439 | 301 | 2,148 | 17% (201 of 1,190 appearances) | "Why Scandinavian Cabins Stayed Warm At -30°F While Modern Homes Freeze" (Medieval Way, 1,402,893, `eVqwiMtoDhk`)<br>"frozen log cabin in wilderness, -18 winter overnight with new wooden stove" (Life and Craft in wilderess, 1,189,737, `MNE6vDO3qeQ`)<br>"Before Central Heating, How Did Americans Survive Freezing Winters?" (Secret State Files, 1,174,167, `9-eQiEQOhyo`) |
| install/DIY project | 269 | 233 | 6,603 | 28% (201 of 707 appearances) | "Building a Heat System for the Garage Apron to Stay Ice-Free in Arctic Winter" (M. Bjoernstroem, 1,465,767, `OGokIsjjuB4`)<br>"Winter Is Coming — I’m Starting to Build a STOVE for My Log Cabin" (Bjorn Brenton, 1,193,994, `pcwYevp32xs`)<br>"I Built a $30 Air Purifier That Beats Them All" (Sidney Explains , 1,110,782, `DXya56NIaVM`) |
| how-to | 698 | 562 | 3,874 | 19% (311 of 1,679 appearances) | "Turn Any Fan Into an Air Conditioner with 2 Ice Bottles ($0 DIY AC)" (Why Am I Green, 3,707,998, `H514-w6ttNo`)<br>"2 in 1 DIY Mini Air Conditioner with a Fan – Cools Instantly Like a Real AC" (Holic Creation, 1,968,935, `XXBuzbGRDqk`)<br>"£15 Radiator Upgrades That Heat Your Room Fast!" (The DIY Guy, 1,499,165, `0Oa5UBiZ6W0`) |
| explainer | 287 | 236 | 2,561 | 21% (130 of 614 appearances) | "Why Put A Capacitor Across The Diode? Here's Why!" (Mr Carlson's Lab, 1,237,056, `MUVLHRaYilU`)<br>"This Home Survives EF5 Tornadoes, Wildfires, and Costs $0 to Heat. Why Aren't We Using It?" (Wild Line, 961,240, `B-WJqqw5GcE`)<br>"Why Don't Seniors Try This $10 Bucket of Salt That Heats a Room All Winter With No Power?" (Jhon Construction, 580,885, `fX4qYS3lQqY`) |
| story | 70 | 64 | 27,778 | 47% (109 of 231 appearances) | "Surviving Power Outages \| Storm Prep \| EcoFlow Home Backup Solutions \| Delta Pro Ultra X" (HOBOTECH, 1,691,697, `3jPucpWphR0`)<br>"Tearing apart the high-temperature furnace (it was kind of a disaster)" (NileRed Extra, 1,192,104, `ynlVJ8WxDL4`)<br>"I’ve Never Seen A Space Heater This Good!" (Project Farm, 1,166,104, `ND2mrzPnBic`) |
| plain topic/other | 988 | 803 | 3,284 | 34% (708 of 2,112 appearances) | "Alice’s Fun Adventures with a Magic Air Conditioner!" (Alice, 7,841,415, `ipvABY4cO_8`)<br>"Primitive Technology: Hut with Underfloor Heating (Ondol/Hypocaust)" (Primitive Technology, 4,305,441, `UkQfhwrlfJ4`)<br>"How to Sleep in a Freezing Minivan Without a Heater" (Overland Minivan, 3,998,115, `x7q1NcHCYNQ`) |
| **all** | **4,880** | **3,071** | **2,911** | **30%** (3,893 of 12,945) | |

### Which formats the keyword framings return (all time)

Share of each keyword framing's returned videos in each format (a video counts once per framing that returned it). Framing is the keyword list's rule-based label.

| Framing | Videos | test | X vs Y | the only X | review | myth-bust | Y doesn't want you to know | mistakes | before you do X | news-warning | cheap hack | symptom-fix | install/DIY project | how-to | explainer | story | plain topic/other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| plain topic | 14,732 | 1% | 3% | 7% | 3% | 0% | 2% | 1% | 1% | 1% | 3% | 6% | 8% | 23% | 7% | 1% | 32% |
| how-to | 6,931 | 1% | 1% | 3% | 2% | 0% | 2% | 1% | 1% | 0% | 4% | 7% | 15% | 45% | 4% | 0% | 12% |
| problem symptom | 3,899 | 1% | 1% | 2% | 1% | 1% | 2% | 1% | 1% | 0% | 3% | 45% | 1% | 19% | 4% | 0% | 18% |
| cheap hack | 2,614 | 2% | 3% | 8% | 2% | 0% | 4% | 1% | 1% | 1% | 24% | 3% | 10% | 17% | 4% | 1% | 17% |
| X vs Y | 1,848 | 7% | 33% | 5% | 4% | 1% | 2% | 1% | 2% | 1% | 2% | 1% | 3% | 7% | 10% | 1% | 20% |
| cost | 1,071 | 3% | 8% | 13% | 10% | 1% | 4% | 2% | 2% | 1% | 4% | 2% | 9% | 11% | 12% | 2% | 16% |
| the only X | 796 | 3% | 8% | 43% | 3% | 1% | 3% | 1% | 1% | 1% | 4% | 1% | 3% | 10% | 5% | 1% | 13% |
| they don't want you to know | 652 | 1% | 2% | 4% | 2% | 1% | 46% | 1% | 1% | 1% | 5% | 2% | 1% | 7% | 4% | 2% | 20% |
| mistakes | 646 | 1% | 1% | 4% | 1% | 1% | 7% | 36% | 3% | 0% | 2% | 8% | 3% | 7% | 3% | 2% | 21% |
| myth | 387 | 4% | 5% | 5% | 6% | 10% | 7% | 2% | 2% | 1% | 4% | 2% | 3% | 21% | 12% | 2% | 13% |
| before you | 191 | 0% | 2% | 3% | 0% | 2% | 9% | 3% | 21% | 0% | 5% | 16% | 1% | 23% | 3% | 0% | 13% |

## Hand-check of the rules

**Method.** 100 videos drawn at random (Python `random.Random(24).sample` over the sorted video IDs, on 2026-10-24, from the sweep's video list before all original titles were checked; 6 of the 150 sampled videos were later dropped as not English and are scored on their stored title). Each title was read by the helper against `labels.md` section 3, in its rule order, title only. "My reading" is a **reading**. The rules were then fixed and a **fresh** sample of 50 (seed 25, excluding the first 100) was read to see whether the fixes held on titles they were not tuned on.

| Check | Titles | Rule tag = my reading |
|---|---:|---:|
| Seed 24, first-pass rules | 100 | **72** |
| Seed 24, rules after the fixes (in-sample, so flattering) | 100 | 87 |
| Fresh sample (seed 25), rules after the first fixes (out-of-sample) | 50 | **37** |
| Fresh sample, after four more small fixes (in-sample) | 50 | 39 |

**Reading of the accuracy:** about three titles in four get the format a careful reader would give (72 of 100 first pass; 37 of 50 on the fresh sample). Treat format counts as approximate, good for spotting big differences between formats, not small ones.

**Common errors (reading):**
1. **Words that were too broad** (fixed): "troubleshooting" with no symptom read as symptom-fix; "problems" in a question ("What problems are most common...") read as symptom-fix; "avoid" ("Avoid plumber") read as mistakes; "should know" read as Y-doesn't-want-you-to-know; "prices" read as explainer; any "install" read as install/DIY project even for a small part ("How to Install a Flange Isolation Kit"); "replace an AC compressor" read as installing a whole system; "Tested & Reviews" on a best-of list read as test; "Mythbusters" missed by `myths?`.
2. **Missing cue words** (some fixed): "deception", "overlooked", "forgotten", "the foil" trick, "how warm can I get", "before trying", "filter change", "annual service". Adding "forgotten" to Y-doesn't-want-you-to-know is my reading of labels.md rule 6 ("unknown" knowledge).
3. **What a title-only rule can't see** (not fixable here): a title that only names a product ("Klein Carbon Monoxide Tester and Detector...") is a review in labels.md, but the rule needs the word "review"; stories without a first-person cue ("They Said He Wasn't built for HVAC. Now He Runs 20 Techs."); "How to heat your home" in a "101" explainer (labels.md puts how-to before explainer).
4. **Off-topic videos** (games, sports, music) get a format from stray words ("Heat vs Timberwolves" = X vs Y; "cheap and quick farm" = cheap hack). Their formats are counted but say nothing about HVAC; see the HVAC-word cut above.
5. The fresh sample also found one Indonesian title the English rule had missed; its words were added to the rule.

First-pass disagreements in the seed-24 sample (rule tag -> my reading, count):

- plain topic/other -> how-to: 3
- plain topic/other -> review: 2
- plain topic/other -> story: 2
- plain topic/other -> myth-bust: 2
- how-to -> explainer: 2
- install/DIY project -> how-to: 2
- plain topic/other -> Y doesn't want you to know: 2
- explainer -> plain topic/other: 2
- symptom-fix -> how-to: 1
- Y doesn't want you to know -> explainer: 1
- plain topic/other -> cheap hack: 1
- mistakes -> symptom-fix: 1
- test -> the only X: 1
- cheap hack -> before you do X: 1
- explainer -> test: 1
- cheap hack -> plain topic/other: 1
- plain topic/other -> explainer: 1
- symptom-fix -> explainer: 1
- explainer -> story: 1

Titles in the seed-24 sample where the current rules still disagree with my reading:

| ID | Title | Rule tag now | My reading | Note |
|---|---|---|---|---|
| `tC8OfhxqBv8` | "Change this setting and stick on the foil! Your radiator will heat 2x stronger" | plain topic/other | cheap hack | foil trick on a radiator ('2x stronger'); no rule word |
| `y08xbbVcwAA` | "Klein Carbon Monoxide Tester and Detector with Exposure Limit Alarm" | plain topic/other | review | one named product; title only names it (thumbnail would be needed) |
| `YRLzndAx08U` | "We Investigated OUR Haunted House UNCUT (ft. Sturniolo Triplets)" | plain topic/other | story | first-person event ('we investigated'); off-topic |
| `uSObJFzdW2g` | "Spaceships Are Not Covered In Gold Foil - The Cool Engineering Behind Multi-Layer Insulation" | plain topic/other | myth-bust | says a common belief is wrong ('are not covered in gold foil') |
| `vvN3YJXFcuY` | "Mr. Heater Buddy to a 20 lb. Propane Tank \| Preparedness 2023" | plain topic/other | how-to | connecting a heater to a tank; no rule word |
| `BfmRaXbHcss` | "What Do They Do On An AC Tune Up at Fox Family HVAC?" | how-to | explainer | what happens in a tune-up, not a procedure to follow |
| `wEHDng7LxOo` | "He Saved His Uncle’s Dying Fish Shop, Got Kicked Out, Built an Empire, and Won His Beauty!" | plain topic/other | story | third-person saga; off-topic |
| `6NZCnuoCb4o` | "$10 Nozzle The IK Foamer Needs! \| IK Precision Foam Nozzle \| Stainless Alternative Nozzle" | plain topic/other | review | one product judged; off-topic |
| `9aiQS0pmbfc` | "Arc Raiders Frigate Inductor : easy, cheap and quick farm." | cheap hack | plain topic/other | video game |
| `H5PA3CBWvTY` | "HVAC License No Needed In These States of US" | plain topic/other | explainer | which states need no licence; no rule word |
| `5gmFk_TgLrw` | "Geothermal 101 - How to Heat Your Home with 400% Efficiency" | how-to | explainer | 'Geothermal 101'; 'how to heat your home' is not a procedure |
| `NuSgmJ8hDms` | "Why I'm Ditching Apple Notes... (You Might Want To Switch Too!)" | explainer | story | first-person switch; off-topic |
| `o9lWaVzwLb8` | "Rep. Miller-Meeks Q&A During HVAC Hearing on VA’s HR Office" | explainer | plain topic/other | news footage of a hearing; 'Q&A' wrongly read as explainer |

Titles in the fresh sample where the current rules still disagree with my reading:

| ID | Title | Rule tag now | My reading | Note |
|---|---|---|---|---|
| `TCPAgS3F47c` | "Can Solar Power Heat Your Home All Winter? Our Experience and Data Revealed!" | how-to | test | a stated trial with data ('our experience and data revealed') |
| `NK5RhNKA2-k` | "How I Cooled My Attic Using Solar + a Car Fan \| Passive Cooling That Actually Makes Sense" | how-to | install/DIY project | 'How I cooled my attic using solar + a car fan': a build |
| `xemHMVsxCWM` | "7 Best Ceiling Fan Recommendations 2026" | plain topic/other | the only X |  |
| `1oyUUzPbyMk` | "They Said He Wasn't built for HVAC . Now He Runs 20 Techs." | plain topic/other | story | a saga ('they said he wasn't built for HVAC. Now he runs 20 techs') |
| `mo2gHbC4EMw` | "Turn Your Patio Into a Cool Oasis 🌴 \| Parrot Uncle F6015 Ceiling Fan Upgrade" | plain topic/other | install/DIY project | a ceiling fan upgrade project |
| `OEdzXsloZ7I` | "How to Make Room Heater At home" | how-to | install/DIY project | making a heater at home |
| `eR5gagSZMGo` | "Is There Really an HVAC Tech Shortage?" | news-warning | myth-bust | doubts a claim ('is there really a shortage?') |
| `RZCa5BpE7Xc` | "Liberator Rocket Stove -- Hyper Efficient, USA Made Wood Burning Stove / Mass Heater" | plain topic/other | review | one named product; title only names it |
| `RIy-isS73Uw` | "What is a Refrigeration Ton + CALCULATIONS chiller hvac btu kw" | how-to | explainer | 'what is a refrigeration ton'; 'calculations' wrongly read as how-to |
| `hcwqB6c5Pv8` | "The HVAC Scam That Backfired" | Y doesn't want you to know | story | the story of a scam that backfired |
| `4XBGxUih138` | "old capacitor repair at home \|\| only 2 minutes \|\| now before throwing it away..." | how-to | before you do X |  |

Every row (title, first-pass rule tag, my reading, note) is in `data/raw/format-handcheck-2026-10-24.csv` and `data/raw/format-handcheck-fresh-2026-10-24.csv`.

