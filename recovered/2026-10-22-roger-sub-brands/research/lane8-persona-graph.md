# Lane 8: Persona channels in Roger's NexLev similar-channel graph

Research date: 2026-10-22. Sources: NexLev `youtube_channel_outliers` (max 60 videos, ≥1.5x), `youtube_channel_videos` (sorted by popular), `get_batch_channel_metrics_v2` (RPM) and `youtube_search` (to find channel IDs). Every number here comes from a tool result. Video ages are YouTube's rounded "N months ago", so dates marked "~" are approximate. Subs per month = current subs ÷ months since the channel's join date. A channel that joined long ago and was repurposed (Stop Wasting Stuff, Japanese Home Hacks) is noted as such. Raw notes: `lane8-notes.txt` in this folder.

Benchmark: **Roger the Pipe Guy**: 76.4K subs, about 2,260 subs/mo over 33.8 months, **RPM $8.13**, average 42,770 views per video.

---

## 1. Channel-by-channel table

| Channel | Narrator archetype | Topic lane | Subs | Joined | Subs/mo | RPM | Avg views (last 60) |
|---|---|---|---|---|---|---|---|
| **Bertha's House Hacks** (@HackTheMexicanWay) | Mexican mother/grandmother ("Mexican mothers swear by") | Cheap substance uses, Walmart/Dollar Tree buys, repairs | 126K | 2026-08-18 | **~59,000** | 7.67 | 206,703 |
| **Japanese Home Hacks** | Japanese grandmother/mother ("my grandma", "my mother swore by") | Cleaning, hydrogen peroxide, mold, sells *The Japanese Method* ebook | 37.2K | 2026-07-23 (first real upload 2026-09-24) | 12,400 (from join date); **~40,000** (from first real upload) | **10.09** | 82,318 |
| **Bertha's Clean Home** (from the list, not pulled) | Mexican mother/grandmother | Cleaning | 215K | 2026-03-24 | ~30,900 | n/a | n/a |
| **Eli Yoder Secrets** | Old Order Amish man | Energy bills to zero, heating and cooling with no machine, borax and peroxide, pests, engine and fuel "they buried" | 249K | 2026-02-05 | **~29,300** | **9.62** | 96,991 |
| **Sidney Explains** | "Sidney", an old-school explainer (fix it, cook it, grow it) | Planned obsolescence, cheap DIY swaps, pests, gardening, off-grid | 315K | 2025-10-20 | **~26,100** | 5.50 | 100,962 |
| **Dave Jennings** | Budget RV-living retiree | RV costs, hacks, cheap RVs, free places to park and retire | 10.5K | 2026-08-31 | **~6,150** | 7.23 | 27,395 |
| **Britain As It Was** | British pensioner thrift ("old British ways") | Winter heating, bills, money owed to pensioners, 1970s thrift | 19.4K | 2026-02-16 | ~2,380 | **10.91** | 24,980 |
| **Sergeant Dale Whitfield** | 30-year Army quartermaster | "Military method" yard, car, home and peroxide fixes | 11.4K | 2026-05-19 | ~2,220 | **9.14** | 24,854 |
| **The Buried Vault** | No persona (faceless) | Suppressed tech: sand-to-stone, "$0 device cuts bill" | 16.4K | 2026-03-09 | ~2,200 | 7.94 (not monetized) | 19,745 |
| **The Hillbilly Way** | Kentucky "Papaw/Mamaw" grandson (Billy Ray McCoy) | Old Appalachian ways: heating, no-power dehumidifying, borax, blizzard prep | 2.22K | 2026-09-13 | ~1,730 | 8.75 (not monetized) | 3,860 |
| **Forgotten Fixes** | No persona ("billion-dollar industries tried to bury") | Lost chemistry fixes | 6.86K | 2026-03-22 | ~980 | 5.93 | 2,371 |
| **Walter Bennet Home Remedies** | "Walter" (persona in name only) | Cleaning remedies | 2.37K | 2026-08-05 | ~925 | 5.97 | 21,461 |
| **Walter Tries It** | 25-year fixer who tests viral hacks | Myth test with a 1–5 wrench verdict | 2.58K | 2026-07-12 | ~770 | **3.45** (UK-led) | 19,840 |
| **Eli Yoder The Plumber** (spin-off of Eli Yoder, found while checking) | Amish plumber | Peroxide and drains | 4.4K | 2026-03-09 | ~590 | n/a | 4,614 |
| **Collapse Crate** | No persona | Grid-down Home Depot gear | 2.13K | 2026-05-03 | ~380 | 3.71 | 7,158 |
| **Frank Holloway**, now **"Untold Record"** | *Was* a retired Midwest home inspector | **Abandoned:** renamed to pre-1991 US military history | 76 | 2026-08-26 | ~40 | n/a | 1,110 |
| Stop Wasting Stuff | No persona, uses "we" | Repairs and repurposing ("make a $300 repair look like a scam") | 68K | 2007 (repurposed old channel) | n/a | 7.06 | 41,151 |
| Frozen Pennies | Real woman, certified financial coach (Sara Conklin) | Frugal living for midlife women | 160K | 2018 | ~1,550 lifetime | 4.10 | 48,194 |
| Under the Median | Real frugal couple (Hope and Larry) | Frugal living, stock-ups | 227K | 2018 | ~2,300 lifetime | 3.69 | 44,198 |
| Natural Health Remedies (list only) | "Tim" | Health remedies | 1.09M | 2013 | ~6,650 lifetime | n/a | n/a |
| Project Farm (list only) | Real on-camera product tester | Product and tool tests | 3.94M | 2017 | ~33,700 lifetime | n/a | n/a |

### Top titles per channel (views, age, outlier score)

**Bertha's House Hacks**
- Put Hydrogen Peroxide on Your Feet and Watch What Happens (6 Uses Mexican Mothers Swear By): **6.4M**, ~1 mo, **31.0x**
- 11 Pantry Staples Mexican Households Buy in Bulk, All Under $5 at Walmart: 687K, ~1 mo, 3.3x
- 10 Dollar Tree Items Mexican Households Buy Before Winter (And 5 They Never Touch): 431K, 3 wks, 2.1x
- Put Aluminum Foil in Your Toilet and Watch What Happens (6 Uses Mexican Mothers Swear By): 320K, ~1 mo, 1.5x

**Japanese Home Hacks** (all 30 videos are under 2 months old)
- 16 Ways The Japanese Use Hydrogen Peroxide (99% of People Don't Know): **1.3M**, 3 wks, 15.8x
- 22 Surprising Japanese Cleaning Hacks You'll Wish You Knew Sooner!: 536K, 3 wks, 6.5x
- 15 Deep Cleaning Hacks for a Spotless Home in Minutes (The Japanese Way): 111K, 4 wks
- Cleaning Products That Are Actually Worth Your Money - That The Japanese Swear By: 73K, 2 wks
- Put Hydrogen Peroxide on Your Feet and SEE What Happens (6 Japanese Tricks From My Grandma): 67K, 2 wks
- Vinegar vs Hydrogen Peroxide vs Washing Soda vs Baking Soda: Which One Works The Best?: 32K, 10 days (**copies the format of Roger's "ranks all 4" video, 176K**)
- I've Never Had Mold in My House in 40 Years, The Old Japanese Trick My Mother Swore By: 19K (**Roger's "In 45 years…" template**)

**Eli Yoder Secrets** (no ≥1.5x outliers, because nearly every video does well)
- This $300 Tunnel Keeps Any Home 55°F Forever: The Amish System the Cooling Industry Made Illegal: **1.2M**, ~6 mo
- 20 Hydrogen Peroxide Hacks That Kill Roaches, Ants & Mice: The $1 Bottle Exterminators Hide: **1.2M**, ~4 mo
- Why the Amish Have Never Needed a Gas Station: The Plant That Fuels Any Engine They Buried in 1937: 1.1M, ~6 mo
- The $2 Liquid That Makes Any Engine Last 500,000 Miles: Mechanics Want This BANNED: 1.1M, ~6 mo
- Your Roof Is Cooking You Alive: The Amish Fixed This 200 Years Ago for $7: 1.0M, ~6 mo
- Your Attic Is Cooking You Alive: The Amish Fixed This 200 Years Ago for $4: 981K, ~5 mo
- Amish's 25 BANNED Hydrogen Peroxide Hacks from the 60s That Scientists Now Say Were GENIUS: 952K, ~6 mo
- The Amish $50 System That Heats Any Home Forever: They Have Never Paid an Energy Bill: 813K, ~6 mo

**Sidney Explains** (the source many of these channels copy titles from)
- Stop Buying Laundry Detergent: This $0 Recipe Lasts a Year!: **3.7M**, ~5 mo
- Harvest Water From Air With This Genius $12 Setup: 2.4M, ~7 mo
- Food-Grade Powder That Destroys Fleas, Bed Bugs, Roaches | The Truth They Hide: 2.2M, ~6 mo
- Your Razor Is Designed to Dull After 3 Uses: How to Make It Last 2 years!: 2.1M, ~4 mo
- Every TV Has a Secret Mode the Manufacturer Doesn't Want You to Find!: 1.9M, ~5 mo
- The WASP Trick Pest Control Companies Don't ADVERTISE: 1.2M, ~4 mo
- The $4 "Dry" Trick That Dehumidifies Any Room Forever, No Power Needed!: 914K, ~6 mo
- The REAL Reason Fruit Flies Keep Coming Back: It's Hiding in Your DRAIN!: 610K, ~4 mo

**Dave Jennings (RV)**
- Wish I Knew These Hydrogen Peroxide RV Tricks Before! I Would've Saved Thousands: **254K**, 3 wks, **9.3x**
- 5 Dirt-Cheap Luxury RVs "Rotting" on Lots (Buy Once, Never Shop Again): 216K, ~1 mo, 7.9x
- 10 Hidden U.S. Towns Where RV Owners Retire in Their RVs For Free in 2026 (And 5 to Avoid): 141K, ~1 mo, 5.1x
- 5 Dirt-Cheap Luxury Motorhomes "Rotting" on Lots: 72K, 2 wks, 2.6x
- Where RV Owners Actually Find $500 RVs To Live In: 67K, 2.4x
- 25 GENIUS RV Hacks NO ONE Knows About: 58K, 2.1x
- 15 RV Hacks You Won't Believe Actually Work!: 54K, 2.0x

**Britain As It Was**
- 25 Secret British Freezer Tricks That Make One Shop Last Twice as Long: 238K, ~4 mo, 9.5x
- 25 "Illegal" British Pensioner Water Bill Tricks the Water Companies Tried to Hide: 205K, ~4 mo, 8.2x
- 25 "Outdated" British Habits Pensioners Were Mocked For: Now Everyone Wishes They Had Them: 167K, ~2 mo, 6.7x
- 20 Winter Clothing Tricks British Pensioners Kept Using While Everyone Else Turned Up the Heating: 158K, 11 days, 6.3x
- 23 "Lost" British Money-Saving Tricks From the 1970s That Still Outsmart Modern Banks: 146K, 5.8x
- 20 Free Things Every British Pensioner Is Owed (You Just Have to Ask): 131K, 5.2x
- 20 Old British Ways to Sleep Warm in a Freezing Bedroom Without Leaving the Heating On All Night: 80K, 9 days, 3.2x

**Sergeant Dale Whitfield**
- The 3 Fastest and Cheapest Ways To Remove a Tree Stump (Military Method): **1.0M**, ~1 mo, **40.2x**
- 11 Hydrogen Peroxide Car Hacks Mechanics Hope You Never Learn: 207K, ~2 mo, 8.3x
- 10 Things Army Supply Never Throw Away Americans Toss Them Every Week: 19K
- 1 Cup of This Destroys Every Drain Clog - But Never Touches Your Pipes: 18K (**Roger's title, copied word for word**)
- 12 WD-40 Uses You'll Wish You Knew Sooner: 18K; Doing This Will Make Your Car's AC Blow Twice as Cold (Military Trick): 13K
- After that, mostly 1–3K views. The channel is carried by two hits.

**The Hillbilly Way** (5 weeks old)
- The Hillbilly $50 System That Heats Any Home Forever: They Never Paid a Heating Bill: 41K, 3 wks, **10.6x** (the Eli Yoder title, word for word)
- Hillbilly Grandma's 27 Forgotten Blizzard Survival Hacks You'll Wish You Knew Sooner!: 36K, **3 days**, 9.3x
- Hillbilly's 25 BANNED Borax Hacks From the 60s That Scientists Now Say Were GENIUS: 8.1K, 2.1x (Eli Yoder template)
- The $4 "Dry" Hillbilly Trick That Dehumidifies Any Room Forever... No Power Needed!: 5.9K, 1.5x (Sidney template)

**Walter Tries It**
- 1 Cup of This Destroys Every Drain Clog - But Never Touches Your Pipes: **767K**, ~2 mo, **38.7x** (**Roger's title, word for word. It beat Roger's own 456K.**)
- Every TV Has a Secret Mode the Manufacturer Doesn't Want You to Find!: 43K, 2.2x (Sidney's 1.9M title)
- 1 Cup of This Removes Every Toilet Ring Forever - It's NOT Bleach: 27K
- This DIY Washer Costs Less Than Laundry Detergent: 8.9K
- In 45 Years of Plumbing, I've Never Had a Clogged Drain: Here's Exactly What I Do: **953** (Roger's title again)
- Most of the other ~38 videos got 130–800 views. One copied hit accounts for about 90% of the channel's 853K views.

**The Buried Vault**
- Electricity Turns Sand Into Solid Stone. No Cement Required. Could Concrete Become Obsolete?: 254K, ~7 mo, 12.9x
- Urine Turns Sand Into Stone: No Cement, No Heat, No Cost: 160K, 8.1x
- Turn Sand to Stone With Vinegar. Stronger Than Steel - Hidden Since 1627: 122K, 6.2x
- One $0 Device Cuts Your Electric Bill in Half Forever: The "Load Secret" They Buried!: 66K, 3.3x

**Walter Bennet Home Remedies**: I Clean My Couch and Carpets With a Pot Lid: I Wish I Knew This Years Ago: 461K, ~1 mo, 21.5x. That one video is about 93% of the channel's views.

**Forgotten Fixes**: nothing at ≥1.5x. The channel is flat at about 2.4K views per video.

**Collapse Crate**: 15 Home Depot Items That Become PRICELESS When The Grid Goes Down!: 205K, 28.6x. Then 54K and 13K. Average 7.2K.

**Frank Holloway (now "Untold Record")**: the only home videos left are "Why Your Shower Drain Clogs Again and Again…" at 4.6K and "The 3 Times a Water Heater Actually Needs Replacing" at 3.5K. The retired-home-inspector persona was dropped after about 10 videos.

**Eli Yoder The Plumber** (the Amish brand's plumbing spin-off)
- 9 Things Plumbers Don't Want You to Learn About Hydrogen Peroxide and Your Drains: 217K, ~4 mo, **47.0x**
- 7 Things Plumbers Don't Want You to Know About Hydrogen Peroxide and Your Pipes: 110K, 23.8x
- 5 Cheap Bottles Already Under Your Sink That Destroy Any Clog: 17K. The channel averages 4.6K.

**Stop Wasting Stuff**: 9 Cheap Sliding Glass Door Tricks That Make a $300 Repair Look Like a Scam: 236K, 5.7x. 9 Hydrogen Peroxide Window Tricks That Make Professional Glass Cleaners Look Overpriced: 121K, 2.9x.

**Frozen Pennies**: 20 Things That Are No Longer Worth Your Money: 499K, 10.4x. Low Income Frugal Habits That Help You Survive on $1,240 a Month (Social Security ONLY): 223K, 4.6x. 9 Grocery Shopping Tricks Stores Hope You Never Learn: 165K.

**Under the Median**: I'm Stocking Up on These Foods NOW: 104K, 2.4x. We Tested the New Jackery HomePower 1000 Plus V2: 93K (sponsored power station).

---

## 2. What the graph shows

### Which narrator types are growing fastest

1. **An elder from a named culture, usually a woman, passing down household methods.** Bertha's House Hacks (Mexican mother) gains about 59K subs a month. Japanese Home Hacks (Japanese grandmother) gains about 40K a month counted from its first real upload. Bertha's Clean Home gains about 31K a month and Eli Yoder (Amish) about 29K. RPMs run from $7.67 to $10.09. This is the clear winner. What carries it is a culture people trust ("Mexican mothers swear by", "the Japanese way", "the Amish never…") combined with cheap household substances.
2. **A generalist explaining old-school know-how (Sidney).** About 26K a month, 315K subs, but RPM is only $5.50 and the videos are short (7–9 minutes). Many other channels copy its titles.
3. **A retiree with a specific lifestyle (Dave Jennings, RV).** About 6.1K a month in its first 7 weeks, RPM $7.23. Roger's hydrogen-peroxide angle applied to RVs is its biggest video.
4. **A veteran of an institution, or a pensioner from another country (Army quartermaster, British pensioner).** About 2.2–2.4K a month with the highest RPMs in the graph ($9.14 and $10.91). Their growth is slower and comes in spikes: Sgt Dale is mostly two hits.
5. **Weak or failing:** the myth-tester (Walter Tries It, about 770 a month, RPM $3.45, its one hit copied from Roger); the retired home inspector (Frank Holloway, abandoned and renamed); channels with no persona selling "buried knowledge" (Forgotten Fixes about 980 a month, Collapse Crate about 380 a month, RPM $3.71); and **named spin-offs of a brand that already worked** (Eli Yoder The Plumber about 590 a month; Martha Yoder Secrets has 104 subs since August 2026, from the list).

### Which topics are growing fastest

1. **Hydrogen peroxide, plus "watch what happens".** It is the strongest topic across the whole graph. Bertha's feet video got 6.4M. Japanese Home Hacks got 1.3M. Eli Yoder got 1.2M (pests) and 952K ("banned hacks"). Dave Jennings got 254K (RV). Sgt Dale got 207K (car). Eli Yoder The Plumber got 217K and 110K. Roger's own peroxide videos got 495K and 402K. **Roger already owns this topic, and every sub-brand can apply it to its own area.**
2. **Cutting bills to zero by heating, cooling or drying the house with no machine.** Examples: Eli Yoder's tunnel (1.2M), roof (1.0M), attic (981K) and $50 heater (813K); Sidney's dry trick (914K) and room cooler (339K); Hillbilly Way's $50 heater (41K at 10.6x); Britain As It Was on winter heating (158K and 80K, both under 2 weeks old). The lane is seasonal and it is heating up right now (October).
3. **"The industry buried or banned this".** Examples: Eli Yoder's engine and fuel videos (1.1M each), Sidney's planned-obsolescence videos (razor 2.1M, TV 1.9M, printer 303K, internet 894K) and The Buried Vault's sand-to-stone videos.
4. **Store-run lists** ("11 items X buy in bulk under $5 at Walmart", "Dollar Tree before winter"): Bertha 687K and 431K, Eli Yoder 462K, Collapse Crate 205K.
5. **Pests treated as a household problem:** Eli Yoder 1.2M, Sidney 2.2M and 1.2M. Pest control is already in Roger's audience tab.

### Roger's titles are already being copied across this graph
- "1 Cup of This Destroys Every Drain Clog - But Never Touches Your Pipes" (Roger: 456K) was copied word for word by Walter Tries It (**767K**) and Sgt Dale (18K).
- "In 45 Years of Plumbing, I've Never Had a Clogged Drain" was copied by Walter Tries It (953). Japanese Home Hacks adapted it as "I've Never Had Mold in My House in 40 Years…" (19K).
- "Vinegar vs Baking Soda vs Washing Soda vs Borax: A 45-Year Plumber Ranks All 4" (176K) was copied as a format by Japanese Home Hacks (32K).
- **What this means:** the narrator persona decides how far a copied title travels. The same title did 767K on one channel and 18K on another. Roger's audience graph is mostly a template-sharing network, so his sub-brands should be distinct personas, not relabelled copies of Roger.

### Who runs these channels, and collab bylines
- **I saw no YouTube collab bylines in any data these tools return** (outlier lists, popular lists, channel about pages). The channels are linked in other ways:
  - **The same contact email, nostalgicoperations@gmail.com**, appears on Walter Bennet Home Remedies, Britain As It Was and Stop Wasting Stuff, so one operator runs all three.
  - **Identical title templates:**
    - Eli Yoder and Hillbilly Way share "$50 System That Heats Any Home Forever" and "25 BANNED Borax Hacks from the 60s That Scientists Now Say Were GENIUS".
    - Walter Tries It and Sgt Dale share "11 Things HVAC Technicians Don't Want You to Know About Hydrogen Peroxide (#8 Saves $900)" and "11 Things Auto Detailers…".
    - Sidney's titles are copied by Walter Tries It, Sgt Dale, Hillbilly Way and Eli Yoder.
  - **The Bertha network:** Bertha's House Hacks uses the handle @HackTheMexicanWay, sells an ebook at oldmexicanway.com and links the Instagram "berthacooksandcleans". Smart Home Hacks (60 subs) uses Bertha's channel description word for word.
  - **Brand spin-offs that did not catch on:** Eli Yoder Secrets led to Eli Yoder The Plumber (4.4K) and Martha Yoder Secrets (104 subs). Japanese Home Hacks has a look-alike in Home Hacks with Uncle Kenji (4.1K subs, 6,887 views).
- **Lesson for Roger:** putting the parent brand in the name does not move the audience over (Eli Yoder The Plumber gets about 590 subs a month against the parent's 29K). The handoff has to be built deliberately: a collab byline, a pinned end screen, and an on-screen character the viewer already knows from Roger's videos.

### How the example sub-brands score

| Proposed sub-brand | Evidence | Verdict |
|---|---|---|
| "Roger Tries It" (myth-tester) | Walter Tries It: about 770 subs a month, RPM $3.45, its one hit is Roger's own title. Project Farm (3.94M) shows testing works, but only with real on-camera tests. | **Weak.** Keep it as a recurring series on Roger's main channel, not a separate channel. |
| "Roger's Army Buddy" (quartermaster) | Sgt Dale: about 2.2K a month, **RPM $9.14**, a 1M stump video (40x) and a 207K peroxide car video. Everything else is under 20K. | **Moderate.** High RPM but hit-driven. Viable if it sticks to yard and car "military method" problems. |
| "Roger's Holler" (Appalachian old ways) | Hillbilly Way: two videos at 9–10x in its first 5 weeks, still unmonetized. Its lane is the same as Eli Yoder's (about 29K a month, RPM $9.62). | **Strong lane, archetype not yet proven.** A good bet. |
| "Roger on the Road" (RV plumbing) | Dave Jennings: about 6.1K a month, RPM $7.23, peroxide RV video 254K (9.3x). | **Strong.** Real plumbing transfer and the fastest growth of the "lifestyle retiree" type. |

---

## 3. Candidate Roger sub-brands, ranked

### 1. "The Plumber's Wife" / "Roger's Wife June" (working names: *June's House: Roger's Better Half*, or *The Old Plumber's Wife*)
- **Concept:** Roger's wife of 40+ years. She runs the household with cheap substances and the "what a plumber's family never buys" lever: cleaning, laundry, mold, odors, pantry and Dollar Tree runs.
- **Why this audience watches:** it is the fastest-growing type in the graph (an elder woman passing down household methods). The main session also found that Roger's top commenters are largely women aged 70+.
- **Evidence:**
  - Bertha's House Hacks: 126K subs in 2.1 months, about 59K a month, RPM $7.67, peroxide-feet video 6.4M (31x).
  - Japanese Home Hacks: 37.2K in about 4 weeks of real uploads, RPM $10.09, peroxide video 1.3M.
  - Bertha's Clean Home: 215K, about 31K a month.
  - Walter Bennet: pot-lid couch-cleaning video 461K (21.5x).
  - Stop Wasting Stuff: peroxide window video 121K.
- **RPM:** $7.67–10.09 in this cluster.
- **Handoff:** a Roger video titled "My Wife Banned These 7 Cleaners From Our House After 40 Years: She Was Right", with June shown as a co-host card and a collab byline.
- **Risks:**
  - The culture hook ("Mexican mothers", "the Japanese way") is part of what drives this cluster. "A plumber's wife" has insider authority but no culture hook. One option is a time hook such as "the Depression-era way" or "1950s housewife".
  - The operator already runs a Backyard Bertha (chickens), so stay away from the name Bertha.
  - Commenters already notice the text-to-speech voice. A female voice needs to be the best one available.

### 2. "Roger's Holler" (or "Roger's Kentucky Kin": Roger's cousin or uncle up the holler)
- **Concept:** old rural ways for an old house. Heat, cool and dry the house with no machine; borax and lye; winter and blizzard prep; keeping rats out for $2.
- **Why:** the "bills to zero / the old ways" lane is the second-largest engine in the graph and it is seasonal right now (heating season).
- **Evidence:**
  - Eli Yoder Secrets: 249K in 8.5 months, RPM $9.62, a 1.2M tunnel video, roof and attic videos at 1.0M and 981K, and a $50 heater video at 813K.
  - Hillbilly Way: $50 heater 41K (10.6x) and "Blizzard Survival Hacks" 36K in 3 days (9.3x), with RPM $8.75 once monetized.
  - Sidney: dry trick 914K, room cooler 339K.
  - Britain As It Was: winter-warmth videos at 158K and 80K, both under 2 weeks old.
- **Handoff:** "My Kentucky Uncle Never Called a Plumber in 60 Years: Here's What He Did Instead".
- **Risks:** Hillbilly Way and Eli Yoder are probably the same template network, so expect title fights. "Industry made it illegal" claims are risky (the operator's claims policy applies). Keep to "old method" framing.

### 3. "Roger on the Road" (RV and camper plumbing)
- **Concept:** RV and camper water systems: black and grey tanks, winterizing, water heaters, leaks and smells, plus the money side of RV retirement.
- **Why:** it carries Roger's plumbing authority over directly. The audience skews to retirees, and Roger's peroxide lever has already been proven in RVs.
- **Evidence:**
  - Dave Jennings: 10.5K in 7 weeks (about 6.1K a month), RPM $7.23, 7 outliers including peroxide RV tricks 254K (9.3x), cheap luxury RVs 216K (7.9x) and towns where you can retire in an RV for free 141K (5.1x).
- **Handoff:** "Pour This Into Your RV Black Tank Before Winter: A 45-Year Plumber's Warning" on Roger's channel, with a collab byline.
- **Risks:** a smaller total audience than home cleaning. Winterizing is a seasonal spike (now). Dave Jennings is still small, so there is room.

### 4. "Roger's Army Buddy: Sarge" (a quartermaster friend)
- **Concept:** a 30-year supply sergeant fixing yard, car and garage problems the "military method" way.
- **Evidence:**
  - Sgt Dale Whitfield: about 2.2K subs a month, **RPM $9.14**, tree-stump video 1.0M (40.2x), peroxide car hacks 207K (8.3x).
  - Eli Yoder's mechanic-bait videos: "$2 Liquid… Engine Last 500,000 Miles" at 1.1M.
  - The brief's audience tab also shows a mechanic WD-40 video at 272K.
- **Handoff:** "My Army Buddy Showed Me How the Military Kills a Tree Stump for $3".
- **Risks:** Sgt Dale's median views are about 1–3K, so this is a hits business. The lane drifted into car, AC and lawn, which lowers focus. Military impersonation is sensitive: present it clearly as a fictional character, never claim real service records.

### 5. "Roger's Brother Ray: 40 Years Fixing TVs and Appliances" (planned obsolescence)
- **Concept:** "it's designed to break". Razors, TVs, printers, internet, washers and appliances, and how to make them last.
- **Evidence:**
  - Sidney: razor 2.1M, TV secret mode 1.9M, internet slowed on purpose 894K, printer 303K; 315K subs at about 26K a month.
  - Walter Tries It's one non-plumbing hit was the TV-secret-mode copy (43K).
  - The audience tab already shows appliances.
- **RPM:** Sidney's is $5.50, lower than the household cluster.
- **Handoff:** "My Brother Fixed Appliances for 40 Years: He Says This $8 Part Kills Your Water Heater".
- **Risks:** Sidney is short-form-ish (7–9 minutes) and the most-copied channel, so this would be crowded. It is better as a persona with a trade (appliance repairman) than as a generalist.

### 6. "Roger's British Cousin" (pensioner thrift, the British way)
- **Concept:** a 75-year-old British pensioner's frugal home: winter heating, bills, freezers, laundry drying. It works as a tradition-tagged flip, the way "The Japanese Way" does.
- **Evidence:**
  - Britain As It Was: 19.4K, about 2.4K a month, **RPM $10.91 (the highest in the graph)**, NexLev's top country is the **US**, 11 outliers including freezer tricks 238K and pensioner water-bill tricks 205K.
  - The audience tab shows a Nan Margaret video at 305K.
- **Handoff:** "My British Cousin Pays £0 to Heat Her Bathroom: The Old Pipe Trick Americans Never Learned".
- **Risks:** moderate growth. The same operator runs three channels in this lane. UK specifics such as water-company rules don't translate to US viewers.

### 7. "Roger Tries It / Roger's Verdict" (not a separate channel)
- **Evidence against a channel:**
  - Walter Tries It gains about 770 subs a month at RPM $3.45, with about 90% of its views from one copied Roger title.
  - Its real "test" videos got 130–800 views.
  - Project Farm's 3.94M subs depend on real physical testing, which the faceless AI-footage pipeline can't do convincingly (commenters already flag b-roll that doesn't match the narration).
- **Evidence for keeping it on the main channel:** Roger's "Ranks All 4" verdict format got 176K and is being copied (Japanese Home Hacks, 32K).
- **Recommendation:** run "Roger's Verdict" as a recurring segment on the main channel.

### Not supported by this lane's evidence
- **Grid-down / prepper gear:** Collapse Crate gains about 380 a month at RPM $3.71, mostly from one hit.
- **Retired home inspector:** the Frank Holloway persona was abandoned within 2 months (76 subs). Home Inspector Dan exists at 17.1K subs and 33M views (from the list) but wasn't pulled here.
- **"Buried knowledge" with no persona:** Forgotten Fixes is flat at about 2.4K views per video. The Buried Vault gains about 2.2K a month and is not monetized.
- **Frugal personal finance with a real face:** Frozen Pennies and Under the Median have RPMs of $3.69–4.10 and need a real presenter.
- **Brand-name spin-offs:** Eli Yoder The Plumber and Martha Yoder show that "Roger's ___" in the name does not move viewers over by itself.

---

## 4. Strongest reference channels from this lane

| Channel | Subs | What it does / why it matters |
|---|---|---|
| Bertha's House Hacks | 126K (2.1 mo) | Mexican-mother household hacks. Peroxide-feet video 6.4M. Fastest grower in the graph (about 59K a month). |
| Eli Yoder Secrets | 249K (8.5 mo) | Amish bills-to-zero and old ways. Many videos at about 1M. RPM $9.62. Daily uploads. Ebook. |
| Sidney Explains | 315K (12 mo) | Old-school fix/cook/grow explainer, and the source of most copied titles. 3.7M laundry-detergent video. |
| Japanese Home Hacks | 37.2K (about 4 wks real) | Japanese-grandma cleaning. Peroxide video 1.3M. RPM $10.09. Sells a book. Copies Roger's formats. |
| Dave Jennings | 10.5K (7 wks) | Budget RV retiree. Peroxide RV video 254K. RPM $7.23. |
| Sergeant Dale Whitfield | 11.4K (5 mo) | Army quartermaster "military method". Stump video 1.0M. RPM $9.14. |
| Britain As It Was | 19.4K (8 mo) | British pensioner thrift. RPM $10.91. US is the top country. |
| The Hillbilly Way | 2.2K (5 wks) | Kentucky Papaw old ways. Early 9–10x outliers, still unmonetized. |
| Walter Tries It | 2.6K (3.4 mo) | Myth-tester. A cautionary case: one copied Roger title got 767K. |
| Eli Yoder The Plumber | 4.4K (7.5 mo) | Amish-brand plumbing spin-off. Peroxide drain videos at 217K and 110K, but slow overall. A cautionary case for brand spin-offs. |
