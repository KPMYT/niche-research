# Roger the Water Guy: view demand by sub-topic (2026-10-22)

## Method, and what to trust

- **NexLev was unavailable.** Every NexLev call returned "Too Many Requests" for about 30 minutes, retried several times. That covered youtube_search, search_videos, faceless_outliers_videos and search_viral_videos_small_channels.
- **Data source instead:** I pulled YouTube's own search results pages directly (geo US, English) and parsed them. This was about 70 queries, each run in two or three modes:
  - views-sorted and limited to the last 12 months (YouTube's "this year" filter, which is rolling)
  - views-sorted all-time
  - views-sorted last month
  - Videos under 3 minutes were dropped, which removes Shorts and ads.
  - Raw dumps: `/tmp/claude-0/-home-user/d5acabeb-7481-55ab-bfba-e93a497d3593/scratchpad/w2data/`
- **Subscriber counts** come from YouTube channel search on 2026-10-22.
- **"xN"** means views ÷ the channel's *current* subscribers. It's a rough outlier proxy, not NexLev's outlier score (which divides by average views). Anything at 5x or more on a channel under 150K is flagged as a small-channel outlier.
- **Channel type is inferred, not tool-verified.** NexLev check_faceless_channel was also rate-limited, so I judged type from the channel name, its description and its title style. Categories:
  - face: a real person on camera
  - faceless: voiceover over b-roll
  - AI-avatar "doctor": the faceless senior-health channels with generated presenters
  - brand/dealer
  - news
- Age is as YouTube displays it ("7mo" = about 7 months ago).
- **Indian, kids, gaming and Shorts results were excluded.** "Water purifier" search is dominated by Indian RO content (Kent, Aquaguard, Native/Urban Company), which isn't Roger's audience.
- **Correction to the earlier research.** Hidden Homestead's "two cheap metals" hit isn't a water video. YouTube now shows "Two Cheap Metals Eliminate ANY Bug Forever — The Discovery They Tried to Bury" at 1,358,988 views (6mo), Hidden Homestead (110K subs). It's about bugs. The water version of that hook belongs to Historia Prime and Caleb Greer (see (a) and (e)).

---

## (a) Water filters / pitchers / under-sink / RO / whole-house

### Last 12 months, US/English, top by views

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | Don't Buy a Whole House Water Filter! DIY Water Treatment Innovation 2026 from Natural Materials | 3,188,881 | 3mo | Holic Creation (688K) | faceless DIY build (no narration) | 4.6 |
| 2 | Proof That Most Water Purifiers Don’t Work! | 2,064,753 | 7mo | Project Farm (3.94M) | face/hands tester | 0.5 |
| 3 | Connecting Two Metals Purifies ANY Water — The "Earth Filter" Secret They Buried | 1,632,756 | 7mo | Historia Prime (103K) | faceless "forgotten knowledge" | **15.9** |
| 4 | I Made My Own Wastewater Filtration System at Home! A 65-Year-Old Plumber’s Secret Using PVC Update! | 1,310,677 | 5mo | Holic Clever (273K) | faceless DIY build | 4.8 |
| 5 | How to Choose a Reverse Osmosis System \| Waterdrop X16 Review | 1,186,625 | 7mo | The Q (13.1M) | face/brand-sponsored | 0.1 |
| 6 | Stop Buying Water Filters - This WWII Ceramic Method Purifies Forever | 708,933 | 10mo | Apocalypse Solutions (29.5K) + Garden Sage (24.7K) | faceless | **24** |
| 7 | Build a 4-Gallon Gravity Water Filter in 15 Minutes | 429,993 | 5mo | Why Am I Green (84.5K) | face DIY | 5.1 |
| 8 | We Filtered Liquids That Should NEVER Be Filtered (Ninja HydraSense) | 424,936 | 2w | Freakin' Reviews (875K) + Barry Lewis | face | 0.5 |
| 9 | $200 Ninja HydraSense vs $50 Waterdrop: Is It Really 4X Better? | 395,927 | 1mo | Freakin' Reviews (875K) | face | 0.5 |
| 10 | I Installed A WHOLE HOUSE Water Filtration System \| Should Have Done this Sooner... | 385,087 | 2mo | Jeff Harris (1.06M) | face | 0.4 |
| 11 | The 5 Best Countertop Water Filters for 2026 (Unbiased, Data-Driven Review) | 258,559 | 10mo | Water Filter Guru (86.6K) | expert/affiliate brand, face | 3.0 |
| 12 | Stop Buying This Now!  It is not Safe For You! | 212,783 | 4mo | LJ and Oree (77.3K) | face couple | 2.8 |
| 13 | BERKEY, what happened? This is what I'm using instead | 205,722 | 4mo | Water Filter Guru (86.6K) | expert/brand, face | 2.4 |
| 14 | The Water Filter Mistake Almost Nobody Talks About | 194,843 | **6d** | PreparedAirman (76.8K) | prepper (likely face) | 2.5 in 6 days |
| 15 | Doctor Reveals the Best Water Filters in 2026 | 178,712 | 7mo | Dr. G Reviews Products (56.8K) | face | 3.1 |
| 16 | GE Refrigerator Filter Ripoff Exposed - What They're Hiding | 146,269 | 7mo | DIY Homestead Projects (76K) | face DIY | 1.9 |
| 17 | The $50 Water Filter That Outlasts Any $5,000 System. Why Don't They Sell It? | 142,899 | 7mo | Lost Build Archives (77.5K) | faceless | 1.8 |
| 18 | We Investigated 8 Popular Water Filters—Only 2 Are Certified to Reduce PFAS | 106,546 | 1mo | Consumer Exposed (163K) | faceless exposé | 0.7 |
| 19 | Stop Throwing Out Water Filters — The Refill Trick That Lasts a Lifetime | 96,072 | 4mo | Sidney Explains (315K) | faceless persona | 0.3 |

### Old benchmarks (all-time)

| Title | Views | Age | Channel |
|---|---|---|---|
| Best Water Filter? Brita, ZeroWater, PUR, Berkey, Aquaphor, AquaTrue | 4,374,680 | 5y | Project Farm |
| Reverse osmosis water purification scam: Hidden camera investigation (CBC Marketplace) | 2,321,582 | 9y | CBC News |
| How To Re-inflate or Re-Pressurize A Storage Tank To A Reverse Osmosis Filtration System (RO) | 1,623,011 | 15y | WaterProBill |
| How to Install a Whole-House Water Filter \| Ask This Old House | 1,515,976 | 9y | This Old House |
| Best Water Pitcher Filters Tier List - 3rd Party Laboratory Tested | 781,393 | 4y | Modern Castle |

### Read

- **The demand is real and current.** Roughly 2-3M at the top, with many videos at 150-430K.
- **The topic splits into two markets:**
  1. **Honest-verdict / buyer content:** Project Farm, Freakin' Reviews, Jeff Harris, Water Filter Guru, Dr. G. This is almost all face creators or expert brands, mostly at 0.4-3x of subs.
  2. **"Don't buy a filter, the forgotten method" content:** Historia Prime, Apocalypse Solutions, Holic, Lost Build Archives, Sidney. This is faceless and over-indexes (5-24x).
- **The "salesman/scam" angle has almost no recent supply.** "Water filter salesman" returned only tiny videos (2-6K). The best recent piece is a face comedy skit ("Door To Door Salesmen Are The Worst...", 2.0M, Papa Meat), which isn't water-specific. CBC's hidden-camera RO scam is 9 years old. That leaves the gap open.

---

## (b) Water softeners and hard water / scale

### Last 12 months

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | The Best Way to Clean Your Toilet! | 1,211,600 | 11mo | Clean That Up (1.38M) | face cleaning | 0.9 |
| 2 | 90-Second Shower Hack: INSTANTLY Remove Water Spots | 542,562 | 10mo | How To with Doc (584K) | face | 0.9 |
| 3 | Preventive Measures: Water Softener Maintenance - S01E10 | 285,193 | 5mo | Maintenance Care (CMMS brand) | brand | n/a |
| 4 | 1 Cup of This Removes Every Toilet Bowl Ring Forever — And It's NOT Bleach | 178,599 | 2mo | The Vintage Pipefitter + Roger the Pipe Guy | faceless persona (operator's own) | 2.3 vs Roger |
| 5 | A Better Water Softener? No Salt, No Slimy Feeling & Less Hard Water Buildup | 84,538 | 3w | Matt Risinger (1.23M) | face | 0.07 |
| 6 | How to Install a NU Aqua 4-Stage Salt-Free Water Softener & Whole House Filtration System | 82,483 | 2mo | The Home Service Pro (393K) | face | 0.2 |
| 7 | Complete Guide to Well Water Filtration Systems | 76,703 | 7mo | Mid Atlantic Water (1.54K) | dealer | **50** |
| 8 | 8 Best Water Softener Systems For 2026 To Know Before Buying | 58,925 | 8mo | The Chris Review (27K) | faceless affiliate | 2.2 |
| 9 | Stop Buying Hard Water Cleaners — This $2 Powder Lasts 2 Years | 48,368 | 4mo | Sidney Explains (315K) | faceless | 0.15 |
| 10 | Whole House Water Filter vs Water Softener: Which One is Best for Your Home? | 43,371 | 6mo | Climate Experts Air Plumbing & Electric | company | n/a |
| 11 | Best Water Softener 2026 \| Angel Water, Inc | 38,556 | 8mo | Drew the Water Guru (7.31K) | dealer | 5.3 |
| 12 | 🧲 These $12 Magnets on Your Pipes Eliminate Hard Water — No Salt, No Filters, Ever! | 33,159 | 5mo | Sidney Explains (315K) | faceless | 0.1 |
| 13 | Salt-Free vs Salt-Based Water Softeners (32 Years of Real Experience) | 9,449 | 5mo | Mid Atlantic Water (1.54K) | dealer | 6.1 |
| 14 | Salt - Free Water Softeners: Scam or Legit? | 7,764 | 9mo | Garden Fundamentals (226K) | face | 0.03 |

### Old benchmarks

| Title | Views | Age | Channel |
|---|---|---|---|
| Cleaning Hard Water Deposits | 9,859,256 | 14y | Crouton Crackerjacks |
| Water Softener Cleaning & Restore it Like New - Don't skip this EASY maintenance | 3,859,738 | 7y | Silver Cymbal |
| WATER SOFTENER SYSTEM : HOW IT WORKS !! | 1,330,612 | 8y | Pan The Organizer |
| How to Remove a Salt Clog from Your Water Softener | 1,041,993 | 14y | Water eStore |
| This Water Softener Blew Me Away!  SO Much Better! | 616,446 | 4y | Matt Risinger |
| The Truth About Salt-Free Water Softeners | 571,900 | 7y | Fresh Water Systems |

The earlier research also found Thetruthaboutwatersoftening's ex-salesman video at 216K (8y).

### Read

- **Softener demand is old.** The big softener videos are 4-14 years old. In the last 12 months no softener-specific video in these searches passed about 85K.
- **The hard-water money is in cleaning hacks** (toilet rings, shower spots), which face cleaning channels own. Roger's own collab, "1 Cup of This Removes Every Toilet Bowl Ring Forever", hit 179K. That's the proof that hard-water topics work when framed as a cheap fix rather than an appliance.
- **The salesman-exposé angle is still empty**, but the feed isn't currently rewarding softeners as a topic.

---

## (c) Well water (iron, sulfur smell, bacteria, pressure tank, shock chlorination)

### Last 12 months, homeowner-relevant

Village/India well-drilling spectacle videos (2-14M) were excluded.

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | Repairing a 100-Year-Old Collapsed Water Well | 1,269,549 | 2mo | M. Bjoernstroem | face (EU restoration) | n/a |
| 2 | Drilling Behind a Well Dowser! (Video made for Facebook, or Mobile Device) | 1,191,945 | 2mo | H²O Mechanic (188K) | face well driller | 6.3 |
| 3 | What YouTubers Don't Tell You About Hand Pump Wells (Sand Point) | 809,651 | 11mo | Wilson Forest Lands | face | n/a |
| 4 | Building a 1,500-Gallon Spring Water System in Alaska | 547,970 | 11d | North To Alaska | face | n/a |
| 5 | Restoring an Abandoned Water Well Pump Jack for my New Property! | 531,046 | 1mo | Hunter Goodrich | face | n/a |
| 6 | Hydro-Fracking... We Blew up neighbors Well! | 353,276 | 11mo | H²O Mechanic (188K) | face | 1.9 |
| 7 | Heavy Sediment Issues with Well Water. Here's how I address the Pump, Tank, and Filter. | 130,330 | 8mo | H²O Mechanic (188K) | face | 0.7 |
| 8 | Well Pump Troubleshooting - Breaker Trips, but the Pump is not Bad! | 100,994 | 2mo | H²O Mechanic (188K) | face | 0.5 |
| 9 | How to Set the Pressure in your Well Tank the Right Way! | 61,791 | 9mo | The Home Service Pro (393K) | face | 0.2 |
| 10 | How to Run a 240V Well Pump on a Small 120V Generator | 41,533 | 8mo | There's A Trick For That | face | n/a |
| 11 | Iron Filters for Well Water: The Complete Guide (32 Years of Experience) | 18,912 | 6mo | Mid Atlantic Water (1.54K) | dealer | 12 |
| 12 | How to Remove Sulfur Smell from Well Water (What Actually Works) | 16,260 | 5mo | Mid Atlantic Water (1.54K) | dealer | 10.6 |
| 13 | Rotten Egg Smell in Your Hot Water? The Real Cause No Plumber Explains | 3,531 | 3mo | Mark Silverbridge Plumbing (12.7K) | faceless persona (operator's own) | 0.3 |
| 14 | One $5 Jug of Bleach Cleans Out Your Whole Well — The Job Well Companies Charge $200 For | 690 | 3w | The Off-Grid Well Finder (934) | faceless | 0.7 |
| 15 | This CHEAP Trick Makes Well Water Safe to Drink | 993 | 10mo | Clean Water Store (4.97K) | dealer | 0.2 |

### Old benchmarks

| Title | Views | Age | Channel |
|---|---|---|---|
| How To Adjust a Pressure Switch | 6,060,474 | 9y | R.C. Worst & Co. |
| How to Check and Adjust Pressure Tanks | 2,837,674 | 9y | R.C. Worst & Co. |
| Low Water Pressure - Well Pump Problems? Check This First | 2,124,434 | 8y | Silver Cymbal |
| Well Water Pressure, Pumps & Tanks - How It Works | 1,523,621 | 8y | Silver Cymbal |
| Add 20 Extra Years To Your Water Heater & Get Rid Of Rotten Egg Smell! | 1,136,696 | 2y | How To Home |
| How to Disinfect Your Well | 784,662 | 9y | Manitoba Government |
| Shock Chlorination of a Private Well | 580,564 | 15y | MSUExtWaterQuality |

### Read

- **Old evergreen search demand is large** (0.5-6M), but it's almost entirely old how-to videos.
- **Recent winners are face well drillers and restoration stories.** Iron, sulfur and shock-chlorination treatment content is at 1-20K in the last 12 months, and recent faceless tries (Off-Grid Well Finder, Clean Water Store) sit under 1K.
- **The operator's own Mark Silverbridge sulfur video did 3.5K.**
- **Bottom line:** this is a search niche, not a browse niche right now.

---

## (d) Tap water safety / PFAS / lead / chlorine-chloramine / testing / fluoride / microplastics

### Last 12 months

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | Woman arrested after Facebook post over water concerns | 3,930,650 | 5mo | FOX 4 Dallas-Fort Worth | news | n/a |
| 2 | Proof That Most Water Purifiers Don’t Work! | 2,064,753 | 7mo | Project Farm (3.94M) | face | 0.5 |
| 3 | We Tested Water From Walmart, Costco, Target, Aldi & 19 More US Stores \| Only 8 Were Worth Buying | 1,851,789 | 2mo | Everything Uncovered (~30.7K*) | faceless exposé | **~60** |
| 4 | Why does tap water taste different now? | 630,416 | 9d | Rabbit Hole | explainer (subs not retrieved) | n/a |
| 5 | Comparison: How Safe Is Tap Water Worldwide? | 537,695 | 3w | WatchData | faceless data-viz | n/a |
| 6 | “Contaminated: The Carpet Industry’s Toxic Legacy”  (full documentary) \| FRONTLINE (PBS) | 517,233 | 8mo | FRONTLINE PBS | broadcaster | n/a |
| 7 | Gravity water filters: which one REALLY makes water healthy? | 480,440 | 10mo | Les Nouvelles Anciennes + Pure Filters | brand collab | n/a |
| 8 | How Safe Is Tap Water In Every Country? | 402,952 | 2w | Luke Davidson (18.3M) | face | 0.02 |
| 9 | America's Water Crisis is Escalating RAPIDLY - The New Emergency Order | 204,517 | 1mo | Neal K. Shah (466K) | face | 0.4 |
| 10 | EPA UNLEASHES $3 billion war on America’s lead pipe disaster | 188,994 | 10mo | Fox Business | news | n/a |
| 11 | The $2 Metal Trick That Kills ALL Bacteria in Water — They Never Told You This | 143,417 | 7mo | Sidney Explains (315K) | faceless | 0.5 |
| 12 | I Started Filtering My Tap Water (but I discovered a 200 year old secret!) | 137,830 | 8mo | Ben Vallack (95.6K) | face | 1.4 |
| 13 | They KNEW This About Fluoride (And Kept Adding It Anyway) | 115,575 | 7mo | Dr. Eric Berg DC (15.1M) | face | 0.01 |
| 14 | We Investigated 8 Popular Water Filters—Only 2 Are Certified to Reduce PFAS | 106,546 | 1mo | Consumer Exposed (163K) | faceless | 0.7 |
| 15 | Filtered water still has microplastics. Here's the fix. | 98,329 | 5mo | Yvonne Burkart, PhD | face | n/a |
| 16 | Chlorine Isn't The Problem — What's Actually In Your Water Is Worse | 35,172 | 5mo | Humble Growth (50.5K) | face | 0.7 |

*Everything Uncovered: the video's channel ID didn't come back from search. The only channel by that name is 30.7K subs and runs the same "We Tested X From Walmart…" series ("…Chicken…" 1,140,659; "…Soap…" 377,768; "…Eggs…" 103,012), so the match is very likely.

### Old benchmarks

| Title | Views | Age | Channel |
|---|---|---|---|
| The Biggest Chemical Coverup In History | 37,222,944 | 1y | Veritasium |
| Why You Don’t Trust Tap Water | 2,803,694 | 1y | Johnny Harris |
| Flint's Deadly Water (full documentary) \| FRONTLINE | 2,193,707 | 5y | FRONTLINE PBS |
| The Only State Capital Where You Can’t Drink the Water | 1,288,375 | 3y | Practical Engineering |
| Why Do We STILL Use Lead Pipes?! | 967,107 | 6y | MinuteEarth |
| How “forever chemicals” polluted America’s water | 902,567 | 6y | Vox |

### Read

- **The ceiling is the highest of any sub-topic** (37M), but the recent top is news, big face explainers and data-viz.
- **The one faceless monster is a grocery-exposé format** ("We Tested Water From Walmart…" 1.85M), not a "what's in your pipes" video.
- **Lead and galvanized pipes have almost no recent demand.** Best was Fox Business at 189K. Roger's own "I've Inspected Thousands of Old Homes — These Are the 12 Pipes You Must Replace" did 3.2K.
- **PFAS works as a hook inside a test/verdict** (Project Farm, Consumer Exposed) more than as a standalone topic.

---

## (e) Emergency and off-grid water (storage, purification, grid-down, water heater reserve)

### Last 12 months

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | Harvest Water From Air With This Genius $12 Setup | 2,432,357 | 7mo | Sidney Explains (315K) | faceless persona | 7.7 |
| 2 | Connecting Two Metals Purifies ANY Water — The "Earth Filter" Secret They Buried | 1,632,756 | 7mo | Historia Prime (103K) | faceless | **15.9** |
| 3 | How Did Ancient Humans Survive Without Clean Water? | 798,859 | 2mo | Deep Epoch (10.1K) | faceless history | **79** |
| 4 | Home Water Is Changing: This Machine Creates Off-Grid Water FOREVER | 732,586 | 1mo | Wild Line (80.1K) | faceless | 9.1 |
| 5 | Stop Buying Water Filters - This WWII Ceramic Method Purifies Forever | 708,933 | 10mo | Apocalypse Solutions (29.5K) + Garden Sage | faceless | **24** |
| 6 | Build a Self Filling Water System for $12 — Engineers Have Known This for Centuries | 503,273 | 8mo | The Garden Of Wisdom (13.2K) + Deeply Rooted Knowledge (9.78K) | faceless | **38** |
| 7 | 2 Metals From the Hardware Store Purify ANY Water — $5 DIY System | 395,415 | 1mo | Caleb Greer — Off-Grid Water & Power (18.1K) | faceless persona | **22** |
| 8 | Endless Water for Your Backyard Garden — The Forgotten Engineering Trick | 361,089 | 7mo | Seeds of Time (29.3K) | faceless | 12 |
| 9 | 20 Off-Grid Water & Power Tricks From the 1940s That Your Electric Company Prays You Never Learn | 298,480 | 6mo | Golden American Memories (5.5K) | faceless | **54** |
| 10 | How to Store Water Long-Term for Emergencies \| Emergency Water Tanks | 294,129 | 2mo | The Bug Out Location (89K) | faceless | 3.3 |
| 11 | The Amish Have Never Bought Water. The $12 System They've Used for 200 Years | 280,793 | 7mo | Eli Yoder Secrets (249K) | faceless persona | 1.1 |
| 12 | 10 Survival Drinks That Keep You Alive When Water Is Limited | 253,375 | 2mo | Prepper Pulse (4.52K) | faceless | **56** |
| 13 | When Water Stops These 18 Items Become Priceless | 224,783 | 4mo | Smart Stockpile Pantry (12.5K) | faceless | **18** |
| 14 | We Tested America’s Emergency Water Sources. The Results Were Bad. Here's The Fix. | 221,459 | 1mo | Dirty Civilian (835K) | face | 0.3 |
| 15 | The Emergency Water Disinfection Trick That Costs Nothing | 217,626 | 2mo | The Provident Prepper (290K) | face couple | 0.75 |
| 16 | Make Your Own Water Filter and Never Buy Drinking Water Again | 176,231 | 2mo | Caleb Greer (18.1K) | faceless persona | 9.7 |
| 17 | 💧 WWII’s Forgotten Water Purification Method That Still Works Today | 164,618 | 11mo | Backyard WISDOM (6.99K) | faceless | **23.5** |
| 18 | STOCKPILE 10 Must-Have Survival Drinks To That NEVER EXPIRE | 157,741 | 3mo | The State Explorer (35.7K) | faceless | 4.4 |
| 19 | When Water Stops These 12 Items Become Priceless | 109,366 | 4mo | DISCOVER US STATE (42.2K) | faceless | 2.6 |
| 20 | Water Outage? This $199 Setup Keeps Your Family Supplied for WEEKS | 25,259 | 1mo | Ralph Harmon (1.19K) + 3 | faceless | 21 |

### Water-heater reserve and grid-down plumbing

- **No dedicated recent hit was found.** The search "water heater emergency water" surfaced only Dirty Civilian (221K, above) and plumbing repair videos under 72K.
- **The angle is unclaimed, but unproven as a standalone title.**

### Old benchmarks

| Title | Views | Age | Channel |
|---|---|---|---|
| FREE water forever.  LEGALLY!!!! | 12,320,018 | 3y | SuburbanBiology |
| Make your own water filter and never buy drinking water again. | 6,550,329 | 6y | Jon Jandai Life is Easy |
| Newly Discovered PRIMITIVE WATER FILTER! 100% Effective | 6,632,793 | 2y | Clay Hayes |
| 3 Mistakes Preppers Make When Storing Water | 2,195,296 | 3y | City Prepping |
| Emergency Water Supply Plan for any Budget | 1,041,721 | 2y | Dirty Civilian |
| The KEY to Emergency Water Preparation Before SHTF | 933,738 | 2y | Water Filter Guru |

Caleb Greer's 395K title is a near-copy of Jon Jandai's 6y-old 6.55M title. Old mega-hits are being remade by faceless channels right now.

### Read

- **This has the densest cluster of recent small-channel faceless outliers in water.** There are ten-plus videos at 10-79x on channels under 45K subs, all within the last 12 months.
- **The winning frame is "forgotten / WWII / Amish / 1940s / $12 / two metals"** plus "never buy water / filters again".
- **Caleb Greer has drifted from water to heat and power** in his last 2 weeks of uploads: "This $35 ALUMINUM MESH Blows 140°F Heat Into Your House" 258K in 4d; sand battery 113K. His water videos remain his best: 395K and 176K.

---

## (f) Bottled water and "best water to drink" for seniors and health

### Last 12 months

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | We Tested Water From Walmart, Costco, Target, Aldi & 19 More US Stores \| Only 8 Were Worth Buying | 1,851,789 | 2mo | Everything Uncovered (~30.7K) | faceless exposé | **~60** |
| 2 | NEVER Drink Plain Water Again After 60 — THIS Secret Trick Boosts Blood Flow \| Senior Health Tips | 1,006,216 | 2mo | Senior Lane (45K) | faceless/AI-avatar senior health | **22** |
| 3 | Urologist Reveals: How to Drink Water to Stop Getting up at Night After 50! | 925,751 | 1mo | Sehat with Malaika (5.73K) + Fit Lit Health (78.5K) | AI-avatar "doctor" | 12-160 |
| 4 | The REAL Reason You Wake Up to Pee at Night After 60! | 696,882 | 2mo | Dr. Ares Senior (91K) | AI-avatar "doctor" | 7.7 |
| 5 | NEVER Drink Plain Water Again After 60 — THIS Secret Japanese Trick Boosts Blood Flow 9,000x | 647,933 | 3mo | Seniors Circle (143K) | AI-avatar | 4.5 |
| 6 | Every Water Brand Explained | 637,783 | 7mo | FooDiscover (75.1K) | faceless (human VO) | 8.5 |
| 7 | How SENIORS Should Drink Water to Lower Blood Sugar and Avoid Diabetes \| Dr Megan Foster | 620,157 | 8mo | Dr. Megan Foster (55.1K) | AI-avatar "doctor" | 11 |
| 8 | Bottled Water Brands To AVOID at All Costs (And 2 That Won’t Poison You) | 580,046 | 7mo | Paul Saladino MD (1.18M) | face | 0.5 |
| 9 | Drink Water Right After Waking Up? 5 Powerful Benefits After 60 (Doctors Don’t Talk About #4) | 520,673 | 7mo | Elderly Active Life (9.87K) | faceless senior health | **53** |
| 10 | 13 Bottled Waters To Avoid At All Cost (And The 2 That Are ACTUALLY Safe) | 488,000 | 11mo | Consumed (103K) | faceless exposé | 4.7 |
| 11 | We Tested Water From Walmart, Costco, Target, Aldi and 19 Other Stores \| Only 8 Were Worth It | 476,670 | 1mo | Etiqueta Oculta (20.5K) | faceless (same script, other language channel) | **23** |
| 12 | 11 Water Bottle Brands to Never Buy And 8 That Are Actually Safe | 462,367 | 2mo | Consumer Exposed (163K) | faceless exposé | 2.8 |
| 13 | Doctor Explains: How Seniors Should Drink Water to Support Blood Sugar and Diabetes Health | 422,780 | 7mo | Health & Healing (73.7K) | AI-avatar | 5.7 |
| 14 | The Actual Difference Between $2 and $56 Water | 412,547 | 7mo | The Hustle (318K) | faceless explainer | 1.3 |
| 15 | 5 Bottled Waters to Never Buy (And 5 That Are Actually Spring water) | 395,159 | 7mo | Built to Eat (108K) | faceless exposé | 3.7 |
| 16 | UROLOGIST reveals HOW to drink WATER to avoid getting up at NIGHT OVER 50 | 381,475 | 2mo | i Senior (84.5K) | AI-avatar | 4.5 |
| 17 | STOP Drinking These 12 Bottled Water Brands (And 5 That Are Actually Pure) | 310,711 | 6mo | All Foods Uncovered (76.4K) | faceless | 4.1 |
| 18 | NEVER Drink These 5 Water Bottle Brands (Here's Why) | 284,298 | 11mo | Steak and Butter Gal (777K) | face | 0.4 |
| 19 | I Investigated 10 Bottled Water Brands (Only 4 Are Actually Clean) | 224,107 | 4mo | Dishclosure (211K) | faceless | 1.1 |
| 20 | 13 Bottled Waters You Should Never Drink — And 5 That Are Actually SAFE | 112,656 | 2mo | Food Fraud Watch (42.7K) | faceless | 2.6 |

Also seen:
- UK version: "DON'T Drink These 10 UK Water Brands (And 4 That Are ACTUALLY Pure)", 529,620, 5mo, Protect Our Plates (170K).
- Korean senior channel: "Never buy bottled water at the store if you see 'this letter'!…", 850,169, 2w, 시니어살림노트.

### Read

- **This is the hottest recent water cluster by far, and it's almost entirely faceless or AI-avatar.**
- **Two formats drive it:**
  1. **"Brands to never buy / we tested X stores":** faceless grocery-exposé channels. The format repeats across chicken, eggs and soap.
  2. **"How seniors should drink water" / "never drink plain water after 60":** AI-avatar doctors at 5-53x.
- **Caution on format 2.** It's medical-claim territory, and the earlier lanes flagged it as a trust risk. A plumber persona can credibly own the *bottled vs tap vs filtered* half, not the urology half.
- **Copycat titles die.** Exact clones of "We Tested Water From Walmart…" on other channels got 173, 339 and 1,307 views (Crock & Jar, America's Checkout, Food Secrets).

---

## (g) Water bills and saving water

### Last 12 months

| # | Title | Views | Age | Channel (subs) | Type | xN |
|---|---|---|---|---|---|---|
| 1 | $230 a Year. No Mortgage. No Electric Bill. No Water Bill. | 693,872 | 7mo | Tiny Home Tours (1.93M) | face | 0.4 |
| 2 | Are Data Centers Wasting Water and Raising Electric Bills? | 593,505 | 2w | Kite & Key Media | explainer | n/a |
| 3 | Data Center Water is a Distraction | 550,268 | 3mo | Kyle Hill | face | n/a |
| 4 | 5 Energy Bill Mistakes Utility Companies Hope You Keep Making | 397,499 | 1mo | Ray Dutton's Garage | faceless persona (HVAC; not water) | n/a |
| 5 | New Yorker loses million-dollar house after unpaid water bill caused foreclosure, lien sale | 304,613 | 11mo | Eyewitness News ABC7NY | news | n/a |
| 6 | 25 ILLEGAL Water Bill Tricks I've Used for 40 Years (The Water Company Hates Me) | 227,222 | 1mo | Frugal Frannie (26.3K) + Vintage Lifestyle USA (272K) | faceless persona | 8.6 vs Frannie |
| 7 | 3 Reasons Your Toilet KEEPS Running - And The PERMANENT Fix For Each One! | 225,431 | 7mo | Roger the Pipe Guy (76.4K) | faceless persona (operator's own) | 2.9 |
| 8 | 25 "Illegal" British Pensioner Water Bill Tricks the Water Companies Tried to Hide | 205,990 | 4mo | Britain As It Was (19.4K) | faceless | **10.6** |
| 9 | Residents ‘refuse to pay’ DeKalb HOA, $5.1 million water bill unpaid | 155,242 | 6mo | Atlanta News First | news | n/a |
| 10 | Woman says inherited home came with $228,000 water bill tied to neighborhood use | 147,003 | 3mo | KBAK Eyewitness News | news | n/a |
| 11 | FREE Water Forever — 11 Systems I Use to Never Pay a Water Bill | 43,651 | 1mo | Caleb Greer (18.1K) | faceless persona | 2.4 |
| 12 | 25 ILLEGAL Water Bill Tricks I've Used for 40 Years (The Water Company Hates Me) | 7,713 | 1mo | Silas Mercer (148K) | faceless persona (copy) | 0.05 |
| 13 | 25 'ILLEGAL' Water Bill Tricks I've Used for 45 Years (The Water Company Hates Me) | 4,713 | 3w | Roger the Pipe Guy (76.4K) | operator's own copy | 0.06 |
| 14 | The Trick I Use to Cut My Water Bill by $40 Every Month, Nobody Does This Anymore | 1,374 | 3mo | Betty's Old Secrets | faceless | n/a |

### Read

- **Demand is narrow.** Two faceless originals hit 206-227K. Everything else is news or energy-bill content, plus the data-center water debate, which is a face explainer topic.
- **The operator's own Roger copy of the Frannie title did 4.7K in 3 weeks**, and Silas Mercer's copy did 7.7K. That's direct evidence the exact title doesn't transfer.
- **Water waste through fixtures** (Roger's running-toilet 225K) outperforms "bill tricks" on Roger's own channel.

---

## Rankings

### By recent (last 12 months) demand

| Rank | Sub-topic | Evidence | Trend |
|---|---|---|---|
| 1 | **(f) Bottled water / "how to drink water" for seniors** | 20+ videos at 112K-1.85M in 12 months; many under 3 months old | Hot and rising |
| 2 | **(e) Emergency / off-grid water** | about 20 videos at 109K-2.43M, many 1-4 months old, densest small-channel outlier cluster | Hot |
| 3 | **(a) Filters / RO / whole-house** | 2-3M at top, plus a steady 150-430K tier; a 195K video in 6 days (PreparedAirman) | Steady-warm |
| 4 | **(d) Tap safety / PFAS / lead / fluoride** | Huge old ceiling (37M); recent top is news and big explainers at 400-630K; faceless entry only via exposé or test format | Steady, news-driven |
| 5 | **(g) Water bills** | Two faceless hits around 200K, then news; copies flop | Narrow |
| 6 | **(b) Softeners / hard water** | Softener-specific recent max is about 85K; hard-water *cleaning* hacks do 0.18-1.2M (face) | Cold for softeners |
| 7 | **(c) Well water** | Treatment content 1-20K recent; only face drillers and restoration break out | Search-only |

### By share of that recent demand going to faceless or persona channels

Shares are estimated from the top-15 tables above, by views.

| Rank | Sub-topic | Faceless/persona share | Who wins |
|---|---|---|---|
| 1 | **(f) Bottled / seniors** | about 85-90% | Faceless grocery-exposé channels and AI-avatar "doctor" channels; only Saladino and Steak and Butter Gal are face |
| 2 | **(e) Emergency / off-grid** | about 75-80% | Faceless "forgotten method" channels; face preppers (Dirty Civilian, Provident Prepper) take a minority |
| 3 | **(g) Water bills** | about 50% of the topical (non-news) demand | Faceless granny/pensioner personas; news takes the rest |
| 4 | **(a) Filters** | about 45-50% | Faceless "don't buy a filter" DIY and history channels vs face product testers (Project Farm, Freakin', Jeff Harris, Water Filter Guru) |
| 5 | **(d) Tap safety / PFAS** | about 25% | Mostly face explainers, broadcasters and news; faceless gets in only through the "we tested" exposé |
| 6 | **(b) Softeners / hard water** | about 15% | Face cleaners, face builders, dealers |
| 7 | **(c) Well water** | about 5% | Face well drillers, dealers |

### Combined read for Roger the Water Guy

- **Best fit for a faceless persona with current feed reward: (f) and (e), then (a).**
- **The best entry is the "honest-verdict + exposé" hybrid**, which no faceless channel owns. Examples:
  - a filter/softener salesman exposé
  - "the only filter I'd put in my own house"
  - "we tested the water from X"
- **It sits between three proven formats:** Project Farm's tester format (face), the grocery-exposé "never buy" format (faceless) and the "forgotten method" format (faceless).
- **Keep (b) and (c) as search-driven filler**, not as launch topics.

---

## 15 title patterns winning in water right now

Titles are quoted exactly. All are from the last 12 months.

1. "We Tested Water From Walmart, Costco, Target, Aldi & 19 More US Stores | Only 8 Were Worth Buying" (1,851,789, 2mo, Everything Uncovered, faceless) — store-test exposé
2. "Harvest Water From Air With This Genius $12 Setup" (2,432,357, 7mo, Sidney Explains, faceless) — cheap-object miracle
3. "Don't Buy a Whole House Water Filter! DIY Water Treatment Innovation 2026 from Natural Materials" (3,188,881, 3mo, Holic Creation, faceless) — "Don't buy X"
4. "Proof That Most Water Purifiers Don’t Work!" (2,064,753, 7mo, Project Farm, face) — "proof most X don't work"
5. "Connecting Two Metals Purifies ANY Water — The "Earth Filter" Secret They Buried" (1,632,756, 7mo, Historia Prime, faceless) — two cheap things + buried secret
6. "I Made My Own Wastewater Filtration System at Home! A 65-Year-Old Plumber’s Secret Using PVC Update!" (1,310,677, 5mo, Holic Clever, faceless) — **old-plumber authority in the title**
7. "NEVER Drink Plain Water Again After 60 — THIS Secret Trick Boosts Blood Flow | Senior Health Tips" (1,006,216, 2mo, Senior Lane, AI-avatar) — "NEVER … again after 60"
8. "Urologist Reveals: How to Drink Water to Stop Getting up at Night After 50!" (925,751, 1mo, Sehat with Malaika + Fit Lit Health, AI-avatar) — expert reveals + age
9. "How Did Ancient Humans Survive Without Clean Water?" (798,859, 2mo, Deep Epoch, faceless) — history question
10. "Stop Buying Water Filters - This WWII Ceramic Method Purifies Forever" (708,933, 10mo, Apocalypse Solutions + Garden Sage, faceless) — "Stop buying X" + era method + "forever"
11. "Build a Self Filling Water System for $12 — Engineers Have Known This for Centuries" (503,273, 8mo, The Garden Of Wisdom, faceless) — $ figure + "they've known for centuries"
12. "11 Water Bottle Brands to Never Buy And 8 That Are Actually Safe" (462,367, 2mo, Consumer Exposed, faceless) — "N to never buy and N that are actually safe"
13. "2 Metals From the Hardware Store Purify ANY Water — $5 DIY System" (395,415, 1mo, Caleb Greer, faceless persona) — hardware-store items + $
14. "25 ILLEGAL Water Bill Tricks I've Used for 40 Years (The Water Company Hates Me)" (227,222, 1mo, Frugal Frannie, faceless persona) — "ILLEGAL tricks I've used for N years" + company hates me
15. "BERKEY, what happened? This is what I'm using instead" (205,722, 4mo, Water Filter Guru, face expert) — fallen-brand + "what I use instead"

Runners-up:
- "The Water Filter Mistake Almost Nobody Talks About" (194,843, 6d, PreparedAirman)
- "When Water Stops These 18 Items Become Priceless" (224,783, 4mo, Smart Stockpile Pantry)
- "10 Survival Drinks That Keep You Alive When Water Is Limited" (253,375, 2mo, Prepper Pulse, 4.52K subs)
- "The $50 Water Filter That Outlasts Any $5,000 System. Why Don't They Sell It?" (142,899, 7mo, Lost Build Archives)

### Warning signals from the same searches

**Framing matters more than topic.**
- **TheCheapFix:** "12 Things Plumbers Don't want You to Know About Hydrogen Peroxide!" = 1,711,550 (2mo). "11 Things Water Treatment Companies Dont Want You To Know About Hydrogen Peroxide (#6 Saves $3000)" = 1,157 (1mo).
- **Roger's own copies:** water bill = 4,713; old pipes = 3,179.
- **Mark Silverbridge:** sulfur = 3,531.
- **Clones of the Walmart water-test title:** 173-1,307 views.
