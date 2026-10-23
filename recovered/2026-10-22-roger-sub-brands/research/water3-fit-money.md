# Roger the Water Guy: audience fit, crossover proof and money (water lane 3, 2026-10-22)

## How the data was gathered (read first)

- **NexLev did not work this run.** Every NexLev call (channel videos, outliers, comments, promotions, analytics, niche search) returned `429 Too Many Requests` for about 40 minutes. Retries after waits of 1 to 5 minutes failed too.
- **The fallback was YouTube's own public data.** Channel video tabs, in-channel search, YouTube search and the innertube `/next` endpoint (views, publish date, description, top comments) were fetched directly on 2026-10-22. The scripts are in `scratchpad/w3tools/` and the raw JSON is in `scratchpad/w3data/`.
- **Rounding.** View counts on channel grids are rounded by YouTube (for example "3.8M"). Where a video was opened individually, the exact count is given (for example 3,859,748).
- **What "x" means here.** "x" = video views ÷ the channel's **lifetime average** (total views ÷ video count, from the `roger-similar-channels.txt` scrape). A second ratio against the median of the sampled videos is shown where the mean is skewed. These are my ratios, not NexLev outlier scores.
- **RPM.** No new NexLev RPM could be pulled. The only RPMs below are NexLev readings already recorded in this folder by earlier lanes, and each is labelled with its source.
- **Persona types:** face = real presenter; faceless = voice-over on b-roll or images (usually AI-narrated); dealer = a company selling the equipment.

---

## 1. CROSSOVER: water topics on Roger-audience channels

### Summary

| Channel (type) | Avg/video (lifetime) | Water-quality videos found | Views | x avg | Age |
|---|---|---|---|---|---|
| **Roger the Pipe Guy** (faceless, 76.4K) | 42,593 mean / 3,600 median (all 224 videos) | "$1 Fix ENDS EVERY Hard Water Stain. PERMANENTLY. Big Water Doesn't Want You to Know" | 677 | 0.02x mean / 0.19x median | Jun 9, 2026 |
| | | "25 'ILLEGAL' Water Bill Tricks I've Used for 45 Years (The Water Company Hates Me)" | 4,713 | 0.11x / 1.3x | Sep 27, 2026 |
| | | No softener, filter, well or drinking-water video on the channel itself | | | |
| **Roger collabs hosted on sister channels** | | "Half a Cup of This Dissolves Years of Limescale Overnight — And It's NOT Vinegar" (host: Vintage Pipefitter) | **240,739** | **87x** VP lifetime avg | Aug 20, 2026 |
| | | "1 Cup of This Removes 10 Years of Sediment From Your Water Heater" (host: Mark Silverbridge) | 58,902 | 4.7x Mark avg | Aug 10, 2026 |
| | | "Vinegar vs Citric Acid vs CLR vs Muriatic — A 45-Year Plumber Ranks All 4 for Limescale" (VP) | 4,732 | 1.7x | Sep 9, 2026 |
| | | "How to Remove ANY Limescale in Minutes — 5 GENIUS Methods…" (VP) | 1,473 | 0.5x | Sep 11, 2026 |
| | | **"Water Softener vs Filter: Which One Do You ACTUALLY Need?"** (VP) | **337** | 0.12x | Jul 25, 2026 |
| | | **Same title** (Mark) | **174** | 0.01x | Jul 26, 2026 |
| **Mark Silverbridge Plumbing** (faceless, 12.7K) | 12,536 (median 730) | "Rotten Egg Smell in Your Hot Water? The Real Cause No Plumber Explains" | 3,531 | 0.28x / 4.8x median | Jun 30, 2026 |
| **The Vintage Pipefitter** (faceless, 10.2K) | 2,766 (median 371) | "The 1800s Water Filter That Outlasts Any $5,000 System. Why Don't They Tell You?" | 2,836 | 1.0x / 7.6x median | Mar 8, 2026 |
| **Roger Wakefield Plumbing Education** (face, 732K) | 68,735 | "Do NOT Buy This Water Filtration System" (pushes the Halo 5, a dealer/sponsor angle) | 114,236 | 1.66x | May 9, 2023 |
| | | "Whole House WATER FILTER Installation Plumber Recommended" | 47,979 | 0.70x | ~5y |
| | | "You Won't Believe What These North Star Water Softeners Do!" | 30,004 | 0.44x | ~5y |
| | | "Reality of Whole House Water Filtration in 2025" | 28,452 | 0.41x | ~1y |
| | | "Hard Water is Destroying Your Plumbing" | 10,914 | 0.16x | ~1y |
| | | "The Best Alkaline Water System For Your Home" | 9,549 | 0.14x | ~1y |
| **Got2Learn** (face, 637K) | 802,725 | None. Its "water" videos are about pressure, valves and fridge lines, not water quality. | | | |
| **Silver Cymbal** (face, 1.09M) | 863,605 | "Water Softener Cleaning & Restore it Like New - Don't skip this EASY maintenance" | **3,859,748** | **4.5x** | Oct 4, 2019 |
| | | "Low Water Pressure - Well Pump Problems? Check This First" | 2,124,437 | 2.5x | ~8y |
| | | "Well Water Pressure, Pumps & Tanks - How It Works" | 1,523,626 | 1.8x | ~8y |
| | | "How to Clean Your Water Softener Salt Tank - Restore it Like New" | 820,909 | 0.95x | ~5y |
| | | "How I Beat the Refrigerator Water Filter Cartel at their Dirty Game - DIY Bypass" | 407,396 | 0.47x | Sep 7, 2025 |
| | | (off-grid) "How to INSTALL YOUR OWN WELL with a Sledge Hammer for FREE OFF GRID WATER" 6.97M (8.1x, ~5y); "DIY BACKYARD WELL with ELECTRIC PUMP" 3.37M (3.9x) | | | |
| **How To Home** (face, 854K) | ~696K (lane 1 figure) | "Viqua UV Light Water Filter / How To Get Rid of Bacteria In Well Water" | 2,035 | ~0.003x | ~6y |
| | | (adjacent) "Add 20 Extra Years To Your Water Heater & Get Rid Of Rotten Egg Smell!" | 1.1M | ~1.6x | ~2y |
| **TheCheapFix** (faceless, 65.9K) | 141,791 (median 7,500) | "11 Things Water Treatment Companies Dont Want You To Know About Hydrogen Peroxide (#6 Saves $3000)" | **1,100** | 0.01x | ~1 mo |
| | | "11 Things Ice Maker Companies Don't Want You to Know About Hydrogen Peroxide! #6 Ends the $50 Filter" | 78,000 | 0.55x / 10.4x median | ~1 mo |
| | | "Pour Hydrogen Peroxide Through Your Shower Head Tonight…" | 1,800 | (1 day old) | 1d |
| **Eli Yoder Secrets** (faceless Amish persona, 249K) | 96,991 (median 7,850) | "The Amish Have Never Bought Water. The $12 System They've Used for 200 Years" | 280,793 | 2.9x / 36x median | Mar 12, 2026 |
| | | "How the Amish Purify Any Water for $2 — The Method Hospitals Won't Use" | 161,000 | 1.7x | ~5 mo |
| | | "The $6 Pipe That Gives Free Water Forever — EPA Wants It Banned" | 27,000 | 0.28x | collab |
| | | "This $3 Pipe Trick Cuts Any Water Bill 80% — Why Water Companies Want It Banned" | 7,600 | 0.08x | ~4 mo |
| **Sidney Explains** (faceless, 315K) | 100,962 (median 11,000) | "Harvest Water From Air With This Genius $12 Setup" | 2,400,000 | 23.8x | ~7 mo |
| | | "The Forgotten Water Harvesting Method That Actually Works" | 238,000 | 2.4x | ~6 mo |
| | | "The $2 Metal Trick That Kills ALL Bacteria in Water — They Never Told You This" | 143,000 | 1.4x | ~7 mo |
| | | "Stop Throwing Out Water Filters — The Refill Trick That Lasts a Lifetime" | 96,000 | 0.95x | ~4 mo |
| | | "This $25 Clay Pot Purifies Any Water Without Electricity" | 53,000 | 0.5x | ~6 mo |
| | | "Stop Buying Hard Water Cleaners — This $2 Powder Lasts 2 Years" | 48,000 | 0.5x | ~4 mo |
| | | "🧲 These $12 Magnets on Your Pipes Eliminate Hard Water — No Salt, No Filters, Ever!" | 33,000 | 0.3x | ~5 mo |
| | | "Your Water Filter Is Lying to You — This Is What Actually Removes Fluoride" | 10,661 | 0.1x | ~6 mo |
| | | "Get Emergency Water From Your Water Heater: It's Easier Than You Think" | 6,265 | 0.06x | 2w |
| | | "The $6 Purple Crystals That Bring a Dead Well Filter Back to Life" | 4,200 | 0.04x | ~5 mo |
| **Bertha's House Hacks** (faceless persona, 126K) | 55 videos | None. Its peroxide, pantry and Costco formats carry the channel. | | | |
| **Japanese Home Hacks** (faceless persona, 37.2K) | 30 videos | None. | | | |

### What the crossover data says

1. **The single strongest operator data point is a cleaning-substance video, not a water-quality video.** "Half a Cup of This Dissolves Years of Limescale Overnight" did 240.7K in two months, about 87x Vintage Pipefitter's average. The answer it reveals is 3% hydrogen peroxide (the top comment says so).
   - Water-heater sediment ("1 Cup of This…") did 58.9K.
   - The same family's straight water-quality explainer, "Water Softener vs Filter: Which One Do You ACTUALLY Need?", flopped **twice**: 337 and 174 views.
   - So Roger's audience bought the *cheap substance plus damage to the house* frame. It did **not** buy "water quality" as a topic.
2. **Roger's own water titles flopped.** Fake-conspiracy hooks ("Big Water Doesn't Want You to Know", "'ILLEGAL' Water Bill Tricks") got 677 and 4,713 views. Do not carry those hooks into the water channel.
3. **Generalist homeowner channels pay off for softener maintenance and well pressure.**
   - Silver Cymbal softener cleaning: 3.86M (4.5x average).
   - Silver Cymbal well pump: 2.1M (2.5x); well tanks: 1.5M (1.8x).
   - These are the best water results on any channel in the list. They are *equipment-care* topics (keep your softener or pump alive), not drinking-water or health topics.
4. **Filter and softener *product* videos from trades channels run below average.** Wakefield's are 0.14-0.70x, apart from one "Do NOT Buy" negative-verdict video at 1.66x. How To Home's UV well filter is about 0.003x.
5. **The faceless persona network wins with "free water" and "purify any water for $2" survival framing**: Sidney 2.4M and 143K, Eli Yoder 281K and 161K. The claims behind those wins are the risky ones (see section 4). Their honest hard-water and filter-maintenance titles run at 0.3-0.95x.
6. **"Companies Don't Want You to Know" does not transfer to water treatment.** TheCheapFix's water-treatment version got 1,100 views in a month, against 78K for its ice-maker filter version.

---

## 2. AUDIENCE: do 55-75 homeowners watch water content?

### Senior-framed water titles exist almost only as health content

| Title | Channel | Views | Age |
|---|---|---|---|
| "Seniors, You're Drinking Water WRONG! (Dehydration-Muscle Loss)" | Barbara O'Neill | 1,038,349 | — |
| "NEVER Drink Plain Water Again After 60 — THIS Secret Trick Boosts Blood Flow" | Senior Health Tips | 1,006,216 | — |
| "NEVER Drink Plain Water Again After 60 — THIS Secret Japanese Trick Boosts Blood Flow 9,000x" | Seniors Circle | 647,933 | 3 mo |
| "Urologist Reveals: How to Drink Water to Avoid Getting up at Night Over 60!" | Dr. Elias Senior Health | 420,462 | 1 mo |
| "Doctor Explains: How Seniors Should Drink Water to Support Blood Sugar and Diabetes Health" | Health & Healing | 422,780 | 7 mo |
| "Don't Drink Plain Water Again After 60 — THIS 1 Trick Boosts Blood Flow Fast" | Senior Health Tips | 357,980 | — |
| "Why Plain Water Stops Hydrating You After 70" | Your Body's Secrets | 101,574 | 2w |
| "NEVER Drink Plain Water Again After 60: THIS Japanese Trick Boosts Circulation 9,000x" | Vitalité Senior | 46,291 | 3 days |

**Home-water titles framed for seniors barely exist, and the ones that do are weak:**

- "Why Seniors Should Never Drink Tap Water Without Doing This First" (Senior Health Tips): 38 views in 1 month.
- BackupWise Seniors "5 Best Whole House Water Filters 2026…": 183 views.
- "water filter seniors" and "old house water lead pipes" searches return mostly utility, TV-news and This Old House videos. The best of those are ATOH "How to Choose a Water Filter" at 1.05M and "How to Diagnose Problems with Well Water Systems" at 813K.

**Reading:**

- The 55-75 audience clearly watches *water* when it is framed as body or health. That lane is YMYL (health) and pseudo-medical ("9,000x"), and it is off-limits under this brief.
- For *house water*, the "after 60" label does not add pull. The audience fit has to come through Roger's channel and older-home or well-owner topics, not through age-labelled titles.
- I found **no direct age evidence** that softener or filter viewers are 55-75. Comment authors rarely state their age (only 4 age or retiree markers in about 430 top comments).

### Comments: who is watching and what they ask (about 430 top comments across 6 videos)

| Video | n | Well | Softener/salt | Filter/RO | Cost/bill | Health | Salesman/dealer | AI/visuals complaint |
|---|---|---|---|---|---|---|---|---|
| Limescale, operator collab (240.7K) | 29 | 0 | 0 | 0 | 4 | 1 | 0 | 3 |
| Silver Cymbal softener (3.86M) | 80 | 12 | 54 | 5 | 7 | 2 | 2 | 0 |
| Wakefield "Do NOT Buy" filter (114K) | 80 | 2 | 7 | 14 | 5 | 2 | 1 | 0 |
| Eli Yoder Amish water (281K) | 80 | 1 | 0 | 3 | 6 | 3 | 0 | 1 |
| Project Farm purifiers (2.06M) | 80 | 2 | 1 | 44 | 13 | 14 | 3 | 0 |
| Silver Cymbal fridge filter "cartel" (407K) | 80 | 4 | 1 | 42 | 8 | 2 | 1 | 0 |

**What the comments show:**

- **Softener viewers are owners of aging equipment.** Examples:
  - "My water softener is 17 years old and I never did any maintenance… made a big difference" (56 likes)
  - "I've had a water system for 10 years and never knew about iron out" (88)
  - "My plumber said the resin beads had gone bad… IT WORKS" (232)
  - "As a relatively new homeowner who's having to learn all about hard water, septic systems" (153)
  - About 1 in 7 mention a well.
  - Trade insiders correct the host ("I work on softener systems… do not recommend a regen in the middle of the day", 659 likes). A veteran persona will be fact-checked by real technicians.
- **Filter viewers ask about recurring cost and specific contaminants.**
  - "Filter pricing should be on the chart since it's an ongoing recurring cost" (7.6K likes).
  - Requests for lead, PFAS and microplastics tests (1K and 804 likes).
  - "Test bottled water brands" (1K).
- **Roger-family limescale video:** the commenters read as women ("My husband got upset because it degraded the rubber rings", 30 likes). Their complaints are about production:
  - "sick and tired of… images that have NOTHING to do with what's being said… copied from other sources" (78 likes, the **top** comment)
  - "22 minutes to show an alternative to vinegar. Video could have been 5 minutes" (28)
  - "AI content. They've lost me for good" (6)
  - **Flag:** the third comment is a seeded-looking plug for a book ("Rogue Remedies by Ruth Vance… FOUR women on my street have already read it", 43 likes). Watch for comment-spam networks on this audience.
- **Eli Yoder's water audience leans conspiratorial:** "they spray our skies with Chemtrails" (24), Oregon rainwater-arrest claims (16). That audience is reachable, but it is not the trust-the-veteran audience.
- **"Water bill" interest is real but small in comments** (4-13 cost mentions per 80 comments). Health worries come almost entirely from the filter-test audience (Project Farm), not from softener or well owners.

---

## 3. MONEY

### RPM (NexLev; no new readings were possible this run, so these are from earlier lanes in this folder)

| Channel | RPM | Source |
|---|---|---|
| Roger the Pipe Guy | 8.13 | lane8-notes batch |
| Caleb Greer — Off-Grid Water & Power | 5.72 (~$4.0K/mo) | lane6 / WATER-BRIEF |
| Eli Yoder Secrets | 9.62 (lane8) / blended 6.53, base 3.0 (lane1) | earlier lanes; the readings differ |
| Sidney Explains | 5.50 | lane8 |
| Seniors Circle (water-after-60 health) | 6.2 | lane6 |
| Smart Stockpile Pantry (water outage) | 7.08 | lane6 |

- **Not measured:** Water Filter Guru, Water eStore, Silver Cymbal and Project Farm RPMs.
- **Working range** for a water channel built on Roger's audience: about $5.5-8. That is an inference from the rows above, not a measurement. Re-run `get_batch_channel_metrics_v2` on Water Filter Guru (UCs_wwjJQkH13dHcnDQV6aLw), Water eStore (UC0l2hLDQZtnYTaTV3iW6IpQ) and Caleb Greer (UCSDjTXpjDQxxaQA4jzVZiXw) once NexLev is back.

### Off-YouTube money (from video descriptions; `get_channel_promotions` was rate-limited)

| Channel | Type | Model seen in description |
|---|---|---|
| Water Filter Guru (86.6K subs, 940 videos, recent median ~25K) | face, lab-test reviewer | Affiliate links (geni.us), "not sponsored" disclosure, **paid consulting** ("custom treatment plan from a Certified Water Specialist"). Top outlier: "The SCAM Water Filter Brands Don't Want You to Know" 417K (2y). |
| Water eStore (103K subs) | dealer ("Gary the Water Guy") | Own store (waterestore.com / .ca), "talk to our team" lead form. Legacy hits are 1.0M / 949K softener troubleshooting (10-14y); recent uploads have a median ~1.9K. |
| Mid Atlantic Water (1.54K subs) | dealer, "32 Years of Real Experience" | Own store and blog. Best recent: "Complete Guide to Well Water Filtration Systems" 76K (7 mo). |
| Clean Water Store | dealer | Store. "Hydrogen Peroxide Well Water Treatment for Sulfur Odors" 208K (3y). |
| Silver Cymbal | face DIY | Amazon affiliate in description and pinned comment (Iron Out, his softener model). |
| Project Farm | face tester | 20+ amzn.to affiliate links on the filter video. |
| Roger Wakefield | face plumber | Amazon storefront, stan.store, courses (thinkific), and a Halo filter partnership on the "Do NOT Buy" video. |
| Caleb Greer | faceless off-grid | **Own e-book**: "Off-Grid Manual — 126 methods, 368 pages" (calebgreeroffgrid.com). |
| Eli Yoder Secrets | faceless Amish | **Own guide/book** ("How to Cut Every Household Bill to Zero", eliyodersecrets.com). |
| TheCheapFix | faceless | **Own handbook** (thecheapfix.netlify.app). |
| Sidney Explains | faceless | Hop-link style affiliate offers ("Ditch Your Electric Company for Less Than $98", "Self-sufficient on ¼ acre 70% off"). |
| Vintage Pipefitter (Roger collab) | faceless | Own book ("101 Ways to Unclog ANY Drain"). |
| Thetruthaboutwatersoftening (216K ex-salesman video, 8y) | face | Website only. |

**What this means:**

1. The book/e-book model this portfolio already uses (Roger, Vintage Pipefitter, Eli Yoder, Caleb Greer, TheCheapFix) is normal in this lane. A "Roger's Water Book" (test, treat, maintain, and which salesman questions to ask) fits.
2. **Affiliate income is natural and large here:** pitchers, under-sink and RO filters, test kits, softener cleaner, resin, sediment filters. Water Filter Guru shows a third tier: paid water-treatment consulting.
3. **Dealer channels own the search results but are decaying on recency.** Water eStore's recent uploads get ~1-4K views and Mid Atlantic's ~100-200.

---

## 4. RISKS

### a. Health and misinformation exposure

- **YouTube's Medical Misinformation policy** bans promoting harmful substances or unapproved treatments. Named examples include Miracle Mineral Solution (MMS, a chlorine-dioxide product that is often sold as "water purification drops"), drinking high-grade hydrogen peroxide, turpentine and others. The policy also covers external links in descriptions. Source: https://support.google.com/youtube/answer/13813322
- For a water channel this means:
  - never present peroxide, chlorine dioxide or bleach as something to *drink* or as a remedy;
  - keep shock-chlorination and peroxide-injection content strictly procedural (equipment and odor), citing extension or EPA guidance;
  - never link a "supplement" or "mineral drop".

**How pseudoscience titles perform in this niche:**

| Claim type | Example | Views |
|---|---|---|
| "Purify ANY water" with copper/zinc metals (a disinfection claim) | Caleb Greer "2 Metals From the Hardware Store Purify ANY Water" | 395K (1 mo) |
| | Hidden Homestead (earlier lane) | 971K |
| | Sidney "$2 Metal Trick That Kills ALL Bacteria in Water" | 143K |
| | Eli Yoder "How the Amish Purify Any Water for $2 — The Method Hospitals Won't Use" | 161K |
| Magnets / descalers | Sidney "$12 Magnets on Your Pipes Eliminate Hard Water" | 33K |
| | Ask Jon Eakes "About Magnetic Water Softeners" (skeptical) | 194K (9y) |
| | Farm Dad "Do Electronic Descalers Work? 3-Month Test" | 154K |
| Structured water | Dr. Bobby Price | 484K (3y) |
| | Bumblebee Apothecary | 71K |
| Alkaline water | Dr. Berg "Why You Should NOT Drink Alkaline Water" | 1.6M (8y) |
| | Wakefield's own alkaline-system video | 9.5K |
| Hydrogen water | "Sensation or Scam?" | 165K |
| | "Is Hydrogen Water a Scam?" | 55K |
| "Dead water" | Kangen and ORP videos | 51-1,005 views |
| Water-after-60 health hooks ("boosts blood flow 9,000x") | see section 2 | 0.4-1.0M |
| Fake "banned" | Eli Yoder "EPA Wants It Banned" | 27K |
| | Eli Yoder "Water Companies Want It Banned" | 7.6K |
| Fake "illegal" | Roger "'ILLEGAL' Water Bill Tricks" | 4.7K |
| Conspiracy | Roger "Big Water Doesn't Want You to Know" | 677 |

**Reading:**

- Pseudo-health and "purify anything" claims pull big views, but they carry policy risk and could hurt the brand.
- The **debunk** angle performs too: Dr. Berg 1.6M, "SCAM Water Filter Brands" 417K, the hydrogen-water "scam?" videos 55-165K.
- A veteran-plumber "salesman's gadget" verdict on magnets, descalers, structured water and alkaline machines is the safe way to ride this demand. Rank the equipment; make no body claims.
- Fluoride and PFAS: keep to "what removes it, per NSF/EPA certification". Sidney's fluoride title got 10K, so the topic is not a big draw on these channels anyway.

### b. Dealer bias and trust

- The water-treatment trade has a documented hard-sell reputation:
  - CBC Marketplace hidden-camera RO scam: 2.32M (9y)
  - Tampa Bay "free water test scam": 47.6K (10y)
  - Ex-salesman tips: 216K (8y)
  - "Don't Get SCAMMED By Water Softener Companies…" (WatchJRGo): 157K (2y)
  - Trade-side titles openly sell to homeowners: "Selling $6,000 Water Systems with Facebook Ads", "How I Sell $3,000 Water Filtration Systems…", "$1.7MM in Water Treatment Sales"
- Roger's salesman-distrust angle has real evidence behind it. The weak spot is the *channel itself*: if it carries affiliate links for a filter it "verdicts", commenters will notice (Wakefield's Halo video drew comments about the business, not the water).
- Recommendation: add a fixed "no sponsor, no dealer" line, and link certification standards (NSF/ANSI 42/53/58) next to any affiliate links.

### c. Seasonality

- **Not measured.** No trend tool was available, and Google Trends was not reachable through NexLev.
- Expected pattern, as an inference only:
  - hard water, softeners and filters are evergreen;
  - well disinfection and testing peak after spring thaw and floods;
  - emergency water peaks with hurricane season and winter storms (Sidney's 2-week-old water-heater emergency-water video has only 6.3K so far).

### d. Production risk specific to this operator

- The top comment on the operator's best water-adjacent video (240.7K) complains about unrelated, copied images. Another calls the video "AI content" and says it lost them.
- Length complaints too ("could have been 5 minutes").
- A water channel will be judged harder on visuals, because viewers expect to *see* the scale, the resin and the test strip.

---

## 5. Twenty launch titles for "Roger the Water Guy"

Rules followed:

- no health or treatment claims;
- no "banned" or "illegal";
- no invented personal tests (no "I tested 12 filters" or "I lab-tested");
- dollar figures appear only where an evidence title or description already uses that figure.

**What the scripts must do to back the titles:** verdict titles ("the only…") must be built from certifications and service experience, not a fake test. The lead-line title must stay at "how to identify it", with no health outcome.

### A. Cheap substance mystery

| # | Title | Modelled on (views) |
|---|---|---|
| 1 | 1 Cup of This Brings a Dying Water Softener Back to Life — Most Owners Never Do It | Silver Cymbal "Water Softener Cleaning & Restore it Like New - Don't skip this EASY maintenance" 3.86M; Mark/Roger "1 Cup of This Removes 10 Years of Sediment From Your Water Heater" 58.9K |
| 2 | Pour This Into Your Softener's Brine Tank Tonight and Watch What Comes Up | Roger "Pour Hydrogen Peroxide Into Your Toilet Tank Tonight and Watch What Happens" 495K; Silver Cymbal "How to Clean Your Water Softener Salt Tank" 821K |
| 3 | Half a Cup of This Unclogs a Crusted Shower Head Overnight — And It's NOT Vinegar | VP/Roger "Half a Cup of This Dissolves Years of Limescale Overnight — And It's NOT Vinegar" 240.7K |
| 4 | The $2 Powder Old Plumbers Used on Hard-Water Scale — And It Isn't CLR | Sidney "Stop Buying Hard Water Cleaners — This $2 Powder Lasts 2 Years" 48K; Roger "1 Cup of This Removes Every Toilet Bowl Ring Forever — And It's NOT Bleach" 150K |

### B. What plumbers do in their own homes

| # | Title | Modelled on (views) |
|---|---|---|
| 5 | Why Plumbers' Faucets Never Crust Up — The $2 Habit They Don't Advertise | Roger "Why Plumbers' Own Drains Never Clog — The $2 Monthly Habit They Don't Advertise" 980K |
| 6 | Tap, Bottled or Filtered? What a 45-Year Plumber Actually Drinks at Home | Johnny Harris "Why You Don't Trust Tap Water" 2.8M; Water eStore "What's The BEST BOTTLED WATER?…" 690K; Roger "In 45 Years of Plumbing…" 456K |
| 7 | In 45 Years of Plumbing, I've Never Paid for a Softener Service Call — Here's Exactly What I Do | Roger "In 45 Years of Plumbing, I've Never Had a Clogged Drain — Here's Exactly What I Do" 456K |
| 8 | What a Plumber Puts Behind His Own Refrigerator Instead of the $50 Filter | Silver Cymbal "How I Beat the Refrigerator Water Filter Cartel…" 407K; TheCheapFix "…#6 Ends the $50 Filter" 78K (10.4x median) |

### C. Veteran verdict ("the only X I'd buy")

| # | Title | Modelled on (views) |
|---|---|---|
| 9 | I've Worked on Water Softeners for 45 Years — These Are the Only 3 Kinds I'd Buy | Harper & Knowles "I've Repaired Hundreds of Washers — These Are the Only 4 I'd Actually Buy" 2.0M (lane 6) |
| 10 | The Only Water Filter I'd Put Under My Own Sink (No Sales Pitch) | Harper & Knowles "The 3 Water Heaters I'd Buy in 2026 (No Sales Pitch)" 661K (lane 6); Project Farm "Proof That Most Water Purifiers Don't Work!" 2.06M |
| 11 | The Only 2 Well Pressure Tanks I'd Put in My Own Basement | Harper & Knowles verdict format; Silver Cymbal "Well Water Pressure, Pumps & Tanks - How It Works" 1.52M |

### D. Ranking ("A 45-Year Plumber Ranks All N")

| # | Title | Modelled on (views) |
|---|---|---|
| 12 | Pitcher vs Faucet vs Under-Sink vs Reverse Osmosis — A 45-Year Plumber Ranks All 4 | Roger "Vinegar vs Baking Soda vs Washing Soda vs Borax — A 45-Year Plumber Ranks All 4" 176K; Project Farm "Best Water Filter? Brita, ZeroWater, PUR…" 4.37M |
| 13 | Salt vs Salt-Free vs Magnets vs Electronic Descalers — A 45-Year Plumber Ranks All 4 Hard-Water Fixes | Roger ranking 176K; Fresh Water Systems "The Truth About Salt-Free Water Softeners" 572K; Farm Dad descaler test 154K; Ask Jon Eakes magnets 194K |
| 14 | Vinegar vs Citric Acid vs CLR vs Lime-Away — A 45-Year Plumber Ranks All 4 on Hard Water | Roger ranking 176K. **Caution:** the limescale version of this exact format got only 4,732 on VP. Test it on Roger's main channel first. |

### E. Fear of damage

| # | Title | Modelled on (views) |
|---|---|---|
| 15 | Hard Water Is Quietly Wrecking These 7 Things in Your House (#4 Is the Expensive One) | Roger "5 Reasons Your PEX Plumbing Will FAIL Within 5 Years…" 102K; TheCheapFix numbered "(#6 …)" parenthetical; Wakefield "Hard Water is Destroying Your Plumbing" 10.9K |
| 16 | 5 Things You Should NEVER Do to Your Water Softener | Roger "5 Things You Should NEVER Pour Down Your Drain" 1.2M |
| 17 | Your Old House May Still Have a Lead Water Line — The 2-Minute Check at Your Meter | NYS Dept. of Health "How to Find Out if You Have a Lead Water Service Line" 56.6K; MinuteEarth "Why Do We STILL Use Lead Pipes?!" 967K; Roger "Grandpa's House Had Cast Iron Drains…" 8K (2.2x median). Identification only, no health claims. |
| 18 | Well Water Pressure Dropping? Check This First Before You Pay for a New Pump | Silver Cymbal "Low Water Pressure - Well Pump Problems? Check This First" 2.12M; Mark "How To Fix LOW Water Pressure In ANY Faucet" 36K |

### F. Salesman distrust

| # | Title | Modelled on (views) |
|---|---|---|
| 19 | The "Free Water Test" Is How They Sell You a $6,000 System — An Old Plumber Explains the Pitch | Thetruthaboutwatersoftening "Tips for buying a water softener from an ex salesman" 216K; CBC "Reverse osmosis water purification scam: Hidden camera" 2.32M; Tampa Bay "Beware of free water test scam" 47.6K; the $6,000 figure is from the trade title "Selling $6,000 Water Systems with Facebook Ads" |
| 20 | Rotten Egg Smell in Your Hot Water? Salesmen Quote $3,000 — The Real Fix Is Usually a $40 Part | TheCheapFix description ("a rod inside your water heater that costs about forty dollars… the other is a three thousand dollar system"); How To Home "Add 20 Extra Years To Your Water Heater & Get Rid Of Rotten Egg Smell!" 1.1M; Mark "Rotten Egg Smell in Your Hot Water? The Real Cause No Plumber Explains" 3.5K (4.8x median) |

### Formats to avoid at launch (they already failed in this audience)

- **A softener-vs-filter explainer with no hook:** 337 and 174 views.
- **"Big Water" / "illegal" / "banned" conspiracy hooks:** 677, 4,713, 7.6K and 27K.
- **"Companies Don't Want You to Know About Hydrogen Peroxide" for water treatment:** 1,100.

---

## Bottom line for the panel

1. **The crossover is proven only partly.** Roger's audience follows *house-damage and cheap-substance* water topics: limescale 240.7K and water-heater sediment 58.9K on sister channels. It has not followed *water-quality* explainers: softener vs filter got 337 and 174. Generalist homeowners reward softener maintenance and well-pressure videos (Silver Cymbal 3.86M, 2.12M, 1.52M).
2. **The 55-75 audience watches water mostly as health content.** That lane is pseudo-medical and out of bounds. The house-water side has no proven senior label, so audience fit has to come from Roger's own subscribers.
3. **Money:**
   - RPM is in the $5.5-8 range, using earlier-lane NexLev readings only.
   - Affiliate income (filters, test kits, softener cleaner) and own books are normal in this lane.
   - Dealers dominate search but are fading.
4. **Biggest risks:**
   - drift into "purify any water" or health claims;
   - perceived dealer or affiliate bias;
   - the production complaints already on the operator's best water video (AI visuals, length).
