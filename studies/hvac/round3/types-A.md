# Round 3 census: channel types, tier A (221 channels)

The round 3 "types A" helper typed these channels on 2026-10-26. The file covers every row with `tier = A` in `data/raw/census-channels-2026-10-26.csv` (221 channels). The helpers for tiers B and C did the rest. **Every type here is my reading of thumbnails plus the channel's own name and About text. None of it is measured, and no videos were watched.** No web searches were used (cap 0).

**Files**

| File | What it is |
|---|---|
| `data/raw/census-types-A-2026-10-26.csv` | One row per channel, rows A001 to A221 in census-CSV order. It has: channel_id, name, handle, subs (and their source), type, ai_character_in_thumbnails, persona_name, claimed_background (quoted, or "not found"), confidence, style_note, notes, type_basis (the long-form video IDs viewed), type_basis_padding (shorter videos used when a channel had fewer than 4 long-form), previous_type and its source, agrees_with_previous, about_source, the re-check columns and the sheet. |
| `thumbnails/census-sheets/A/sheet-01.jpg` … `sheet-28.jpg` | 28 contact sheets (JPEG). Each holds 8 channels, one row per channel, labelled `#n name (subs)`, with the 4 thumbnails and their video IDs. Row #n on the sheets = A00n in the CSV. A "P" after a video ID marks a padding video under 5:00. |
| `thumbnails/census-sheets/A/recheck-01.jpg`, `recheck-02.jpg` | The re-check sheets: the next 4 long-form videos for 16 sampled channels. |

## Method

1. **Videos.** For each channel I took the 4 newest videos of 5:00 or longer, in Latest-sort order, from its census JSON (`data/raw/census-2026-10-26/<channelId>.json`, Videos tab pulled 2026-10-26). 209 channels had 4. For 7 channels I added shorter videos from Latest, then from Popular: A011, A019, A038, A069, A123, A204 and A216. A069 (hvacrepairguy) had no long-form video in its Latest list, so all 4 of its thumbnails are shorter videos. Even with padding, 8 channels have fewer than 4 thumbnails, because they have only 1 to 3 videos: A038, A061, A066, A099, A123, A216, A217 and A221.
2. **Thumbnails.** I loaded `https://i.ytimg.com/vi/<id>/mqdefault.jpg` for 868 videos on 2026-10-26, with 0 failures. I built the contact sheets with Python PIL and read each one by eye.
3. **Text.** I read the channel name, the handle, the 4 titles and the About text. About texts come from the four About files already in `data/raw/`: `channel-finds-pages-2026-10-23/about.json`, `round2-nexlev-pages-2026-10-24/about.json`, `round2-oldheat-2026-10-24.json` (channel_about) and `channels-master-about-2026-10-24.json`. 195 of the 221 channels had About text (the CSV's `about_source` column says which file). Backgrounds are quoted exactly. Where no claim was found, the CSV says "not found". I made none up.
4. **Rules used** (`labels.md` section 5, plus the task brief):
   - **on camera:** the same real-looking person appears across the thumbnails, even if only in 1 of 4 (confidence drops when it's only 1). A company channel whose About names its host also counts (for example A115 Atlas AC, "hosted by Kenneth Carpenter").
   - **brand:** a company channel whose thumbnails show a logo, branded uniforms or branded staff, with no named host. Staff may appear on camera. A company channel with no logo or staff in the thumbnails was typed by what is shown, usually **faceless** (A036, A113, A136, A169, A173).
   - **faceless persona:** the same AI-generated character recurs across the thumbnails. It is usually named in the channel name, About or a shirt patch. 12 are unnamed. They are typed "faceless persona" with the name "not found (unnamed …)" to match the tier B and C helpers. labels.md asks for a named persona, so these 12 are listed separately below.
   - **faceless:** hands, products, renders, diagrams, or stock or AI scenes with different people each time. A named narrator who is never pictured stays **faceless** (A047 Green Exposed "I'm Reid", A112 HVAC Training 101 "my name is Bob", A125 Construction Odyssey with Eddie). This matches the tier B and C rule. Real tradespeople who film only their hands (POV) are also faceless by the "no face in 3 recent" rule, though they are real people, not AI channels.
   - **AI avatar:** this needs a consistent, lip-synced, talking-head studio look. No tier A channel met that bar from thumbnails. Four channels earlier tagged AI avatar are now faceless persona; A027 Doug Cross still needs a video check.
5. **Re-check (working rule 3, done by me, not a second helper).** For 16 randomly sampled channels (seed 20261026) I viewed the **next** 4 long-form thumbnails (`recheck-01.jpg`, `recheck-02.jpg`). Two of the 16 had no further long-form videos. Of the other 14, 12 readings held and 2 changed. Both changes were real tradesmen I had read as faceless from hands-only thumbnails who show their face in older videos: A023 ChilesHeatCool and A094 JustintimeHVAC, both now on camera. So the faceless "real tech POV" group (about 15 channels) may hold more on-camera channels. **A second helper should still re-check a sample against the sheets before this goes to the operator.**

## Counts by type (reading)

| Type | Channels | high | medium | low |
|---|---|---|---|---|
| faceless | 62 | 43 | 17 | 2 |
| on camera | 57 | 40 | 13 | 4 |
| faceless persona | 55 | 35 | 16 | 4 |
| brand | 47 | 25 | 21 | 1 |
| AI avatar | 0 | | | |
| **Total** | **221** | 143 | 67 | 11 |

Of the 55 personas, 43 are named and 12 are unnamed recurring AI characters. 31 of the 55 claim a background in their own words. 28 of the 55 joined in 2026 and 5 in 2025 (joined date from the census CSV).

**Against the earlier type tags.** 160 of the 221 rows already had a type tag: 117 match my reading and 43 differ. 61 had no tag. The main differences:
- faceless → faceless persona: 11
- on camera → brand: 8 (company channels with branded staff)
- brand → faceless: 7 (company names, but no logo or staff in the thumbnails)
- faceless → on camera: 6
- AI avatar → faceless persona: 4
- on camera → faceless: 3
- brand → on camera: 2
- faceless → brand: 1
- faceless persona → faceless: 1

The CSV's `agrees_with_previous` column marks each row.

## Faceless personas (55)

Subscriber counts come from the census CSV (Videos tab header, 2026-10-26, rounded). Joined dates also come from the census CSV. Backgrounds are quoted from the About text or titles. "Not found" means I found no claim in the About text, the channel name or the 4 titles.

| Row | Channel | Subs | Joined | Persona name | Claimed background (quoted) | Conf. |
|---|---|---|---|---|---|---|
| A174 | Eli Yoder Secrets (@EliYoderSecrets) | 249,000 | 2026-02-05 | Eli Yoder | About: "For generations, Amish communities across Pennsylvania and Ohio have lived without energy bills ... We just knew things" | high |
| A206 | Ray Dutton's Garage (@RayDuttonsGarage) | 31,900 | 2026-07-01 | Ray Dutton | About: "Hi, I'm Ray Dutton, a retired HVAC pro ... For twenty-five years I worked in attics, basements and crawlspaces for the same companies I now expose, so I know what a twelve dollar part looks like on a four hundred dollar invoice." | high |
| A181 | Candlelight Archives (@CandlelightArchivesYT) | 16,400 | 2016-02-20 | not found (unnamed recurring man) | not found | medium |
| A122 | HVAC Exposed (@HVACExposed) | 9,590 | 2026-02-27 | not found (unnamed recurring man) | not found | medium |
| A091 | John The HVAC Guy (@JohnTheHVACGuy) | 7,230 | 2020-09-30 | John | About: "Hey, I'm John. I've spent years around HVAC systems" | high |
| A069 | hvacrepairguy (@hvacrepairguy) | 6,360 | 2008-04-30 | HVAC Repair Guy (no personal name) | About: "Led by a specialist with 17 years of industry experience ... As a former nuclear power electrician turned HVAC contractor" | medium |
| A007 | Harlan Sawyer (@HarlanSawyer1) | 5,950 | 2019-07-30 | Harlan Sawyer | titles: "(From an Old Logger)", "An Old LUMBERJACK Tests..." | high |
| A176 | Wes Tucker Prepping (@WesTuckerPrepping) | 4,190 | 2026-07-19 | Wes Tucker | not found | high |
| A108 | Old Ways Restored (@OldWaysRestored) | 2,950 | 2026-05-28 | not found (unnamed older man) | About: "Every video starts in the primary sources ... I read those, work out what the method ac[tually does]" | medium |
| A163 | Repara Fácil USA (@not found) | 2,460 | 2025-02-02 | not found (unnamed recurring man) | not found | low |
| A148 | HVAC Mike (@HVAC-Mike) | 2,430 | 2026-05-23 | Mike | not found (About sells "The Real HVAC Guide"; no background claimed) | high |
| A042 | Earl Sizemore (@EarlTheHillbilly) | 2,420 | 2021-03-13 | Earl Sizemore | About: "I'm Earl Sizemore, up on Clinch Mountain in Hancock County, Tennessee. My daddy was the blacksmith for our end of the county"; title: "I'm 74 and Live Alone in the Mountains" | high |
| A175 | Frank Coyle's Wrench (@FrankCoyleWrench_Yt) | 2,170 | 2007-10-14 | Frank Coyle | About: "Hi, I'm Frank Coyle, a retired HVAC pro who spent twenty-eight years working for the big companies in the trade" | high |
| A157 | June's Kitchen Table (@JunesKitchenTable) | 1,840 | 2025-07-08 | June Halvorsen | About: "June Halvorsen is a fictional character: an AI-generated grandmother living at the end of a gravel road on Minnesota's Iron Range. In her story, her late husband Walt restored power for the electric co-op for 38 years, and she drove a rural mail route for 31 winters." | high |
| A004 | Deals with Lucy (@TheHvac-Insider) | 1,490 | 2020-01-20 | not found (unnamed recurring man) | not found | medium |
| A024 | Hank Cole (@HankColeUS) | 1,370 | 2026-07-20 | Hank Cole | About: "Forty years in heating and cooling. Now I tell you what the companies won't." | high |
| A126 | Hidden life Hacks (@HiddenlifeHacks-h4q) | 1,190 | 2026-04-16 | not found (unnamed recurring man) | not found | medium |
| A077 | Gus Whitaker (@GusWhitakerr) | 1,000 | 2026-08-27 | Gus Whitaker | not found | high |
| A081 | Elias Mercer (@EliasMercerYT) | 613 | 2025-04-04 | Elias Mercer | About: "everything I know about survival, I learned the hard way, alone, off the grid" | high |
| A054 | TheUnknownMarks (@TheUnknownMarks) | 529 | 2026-06-08 | not found (unnamed recurring man; channel name "TheUnknownMarks") | About: "I measure the heating hacks nobody measured" | low |
| A079 | Ask Big Jim. (@ask.big.jim01) | 444 | 2022-12-03 | Big Jim / Raymond Whitaker | About: "my name is Raymond Whitaker and I'm a retired handyman who's spent decades keeping American homes running smooth" | high |
| A134 | Earl Appalachia (@EarlAppalachia) | 440 | 2018-07-20 | Earl | not found | medium |
| A213 | Shelved Science (@ShelvedScience) | 295 | 2026-10-02 | Hal | About: "I'm Hal. 40 years laying brick, now sharing the old-school fixes the trades used for generations" | high |
| A120 | Jake Holloway (@jakeholloways) | 287 | 2023-01-28 | Jake Holloway | not found (About: "Welcome To My Channel!") | high |
| A150 | Walter Northwood (@WalterNorthwood) | 287 | 2026-08-01 | Walter Northwood | not found (About: "Welcome, I'm Walter Northwood. For generations, families across the northern U.S. and Canada kept their homes warm") | high |
| A014 | Earl The HVAC Guy (@EarlTheHVACGuy) | 225 | 2022-10-30 | Earl | About: "Thirty-two years ago, I bought a fixer-upper ... I spent that winter studying used HVAC textbooks from a community college library" | medium |
| A217 | Earl The Furnace Man (@EarlTheFurnaceMan) | 185 | 2023-08-02 | Earl Lindgren | About: "I'm Earl Lindgren. I spent 45 years helping people with their furnaces ... I've been down in more than ten thousand basements" | high |
| A029 | Gord The Tradesman (@GordTheTradesman) | 164 | 2017-08-01 | Gord | About: "I spent 30 years fixing things in people's homes" | high |
| A182 | Gene Halvorsen (@GeneHalvorsenAK) | 158 | 2026-08-27 | Gene Halvorsen | About: "My name's Gene Halvorsen. I live in North Pole, Alaska ... I hauled heating oil on the same route for thirty-seven winters and looked after houses for people who left when the cold came." | high |
| A056 | Earl Whitaker (@Earl-Whitaker) | 111 | 2026-08-12 | Earl Whitaker | not found (About gives no tenure or background) | high |
| A159 | Built to DIY (@Built-to-DIY) | 103 | 2006-07-11 | not found (unnamed recurring man) | titles: "Contractor Reveals ...", "Old Contractor's Method" | medium |
| A027 | The Smart Way to Buy HVAC with Doug Cross (@TheSmartWaytoBuyHVAC) | 75 | 2025-11-03 | Doug Cross | not found | low |
| A078 | Walt Brennan (@WaltBrennan1) | 71 | 2026-08-27 | Walt Brennan | About: "Thirty years in appliance service. Now on your side of the invoice. I'm Walt Brennan. I spent my career fixing refrigerators, washers and dryers — and eight of those years in the office, training the technicians" | high |
| A006 | Frank From Maintenance (@FrankFromMaintenance) | 69 | 2026-08-18 | Frank | About: "Frank shows you what an experienced maintenance man checks first" | high |
| A016 | Eli's Plain Heat (@EliPlainHeat) | 68 | 2016-03-15 | Eli | not found | high |
| A211 | Mick's Air Con (@MicksAirCon) | 44 | 2023-03-14 | Mick | not found | high |
| A186 | Walt Brenner's Boiler (@WaltBrennersBoiler1) | 40 | 2022-12-15 | Walt Brenner | About: "I'm Walt Brenner. I spent thirty years fixing furnaces and air conditioners in basements, attics and boiler rooms — for the same companies I'm now going to tell you the truth about." | high |
| A100 | Conditioned Air Secrets (@ConditionedAirSecrets) | 31 | 2026-08-10 | not found (unnamed recurring man) | About: "Built on twenty-three years around home heating and cooling." | medium |
| A103 | Old Maine Firewood (@OldMaineFirewood) | 29 | 2026-08-25 | Hollis | About: "My name's Hollis. I've lived and heated my home in Maine for forty years" | high |
| A096 | Dennis Kubiak (@HermanCameron) | 28 | 2026-09-18 | Dennis Kubiak | not found | high |
| A071 | RURAL WORTH (@RuralWorthUSA) | 21 | 2015-04-08 | not found (unnamed recurring man) | not found | medium |
| A009 | George Smith's Garage (@GeorgeSmithGarage) | 14 | 2016-03-12 | George Smith | not found | medium |
| A128 | Ray's Workshop (@RaysWorkshopYT) | 14 | 2026-07-31 | Ray | not found (About: "home repair gets explained the old way — slowly, plainly, and with real numbers") | high |
| A156 | Hal's Boiler Room (@HVAC-s6m) | 13 | 2026-10-12 | Hal | not found (titles: "Old Furnace Men Put Them UNDER You") | medium |
| A104 | Hank Álvarez (@hankalvarez1964) | 9 | 2026-06-29 | Hank Álvarez | not found (About: "Hi, I'm Hank. I help homeowners understand what is really going on inside their home") | high |
| A153 | Dale Prosser (@daleprosser101) | 9 | 2024-01-18 | Dale Prosser | not found | medium |
| A119 | Practical Home Energy (@PracticalHomeEnergy) | 7 | 2020-09-27 | Miguel Cárdenas | About: "Hi, I'm Miguel Cárdenas. I spent decades working inside American homes" | high |
| A082 | Gus Hollis (@GusHollis) | 5 | 2026-09-29 | Gus Hollis | About: "I fixed pipes and furnaces for forty-one winters up in Vermont's Northeast Kingdom, and I'm retired now." | high |
| A178 | Dale Kirkwood (@dalekirkwood) | 5 | 2026-06-23 | Dale Kirkwood | About: "Hi, I'm Dale Kirkwood, a retired heating engineer ... For twenty-five years I worked in basements and crawl spaces for the same companies I now expose" | high |
| A064 | Home Ready with Calvin (@JeanHiggins-p3u) | 3 | 2026-09-15 | Calvin | title: "I've Never Had Condensation on My Windows in 40 Years — The Old Trick My Dad Swore By" | high |
| A073 | Blueprint Archive (@blueprintsarchive) | 3 | 2026-08-18 | not found (unnamed recurring man) | not found | low |
| A066 | Leroy Bell's Repair (@leroybellgarage) | 1 | 2025-11-15 | Leroy Bell | About: "Hey, I'm Leroy Bell, a veteran HVAC technician ... For nearly three decades, I spent time in attics, basements, and crawlspaces for the exact companies I now help expose." | medium |
| A164 | Vern Holt / Home Repair (@VernHoltHomeRepair) | 1 | 2014-07-03 | Vern Holt | not found (About: "Hi, I'm Vern Holt, and I show you what's really going on inside your house") | high |
| A132 | Dale's Winter Fixes (@DalesWinterFixes) | not found | 2026-09-30 | Dale | About: "I'm Dale. I spent a working life around furnaces, wiring and drafty old houses, and I'm retired now in a place where winter means it." | high |
| A190 | Home Fix Garage (@HomeFixGarage) | not found | 2026-09-21 | not found (unnamed recurring man) | About: "Hi, I'm a retired HVAC pro ... For twenty-five years I worked in attics and crawlspaces for the same companies I now expose" | medium |

### Patterns among the personas (my reading, not proof of shared ownership)

- **A shared "retired HVAC pro" template.** Ray Dutton's About says: "For twenty-five years I worked in attics, basements and crawlspaces for the same companies I now expose, so I know what a twelve dollar part looks like on a four hundred dollar invoice." Near-copies of that line appear in:
  - A190 Home Fix Garage: "For twenty-five years I worked in attics and crawlspaces for the same companies I now expose — so I know what a twelve dollar part looks like on a four hundred doll[ar invoice]"
  - A178 Dale Kirkwood: "For twenty-five years I worked in basements and crawl spaces for the same companies I now expose"
  - A066 Leroy Bell: "for the exact companies I now help expose"
  - A186 Walt Brenner: "for the same companies I'm now going to tell you the truth about"

  The look is shared too: a grey-haired AI man in a navy work shirt with a name patch, pointing. The patch reads "RAY" on Ray Dutton (A206), and also "RAY" on A056 Earl Whitaker (`lz-RIZga2l0`) and A153 Dale Prosser (`Qv-aFsAhZc8`). Near-identical titles recur. Leroy Bell has "Before You Shut Your AC Down This Fall, Do These 3 Things (or Pay for It Next Spring)", Dale Prosser has "... This Fall, Do This (Or Pay for It Next Spring)" and Walt Brennan has "... for Winter, Do This (Or Pay for It Next Spring)". "BIG FALL MISTAKE!" thumbnail text appears on A066, A153 and A186.
- **Shared surname:** A157 June Halvorsen, who the About says is openly AI, and A182 Gene Halvorsen, both cold-north "hauled heating oil / mail route" stories.
- **Shared About text among faceless exposé channels:** A101 Vent Exposed and A200 Coil Exposed have the same About. A093 Exposi, A122 HVAC Exposed and A139 HVAC Uncovered all open with "Your HVAC system is the most expensive thing in your home you know nothing about". A046 The Technician's Blacklist uses the same line about appliances.
- **Culture keys** like the operator's own: A119 Practical Home Energy (Miguel Cárdenas) uses "(The Mexican Way)". The Amish personas are A016 Eli's Plain Heat and A174 Eli Yoder Secrets, which has 249,000 subs and is by far the largest persona in tier A.

## Unnamed recurring AI characters (counted as faceless persona above)

| Row | Channel | Subs | Note |
|---|---|---|---|
| A181 | Candlelight Archives | 16,400 | same AI bearded man in cap in 3 of 4; the About text is about historical-romance stories |
| A122 | HVAC Exposed | 9,590 | same grey-haired man, AI by my reading |
| A108 | Old Ways Restored | 2,950 | same AI man in all 4 re-check thumbnails |
| A163 | Repara Fácil USA | 2,460 | Spanish-language; AI or real is unclear (low) |
| A004 | Deals with Lucy (@TheHvac-Insider) | 1,490 | same polished bearded man |
| A126 | Hidden life Hacks | 1,190 | same AI young Asian man with glasses |
| A054 | TheUnknownMarks | 529 | AI or real is unclear (low) |
| A100 | Conditioned Air Secrets | 31 | earlier tag AI avatar; About: "Built on twenty-three years around home heating and cooling." |
| A159 | Built to DIY | 103 | titles: "Old Contractor's Method" |
| A071 | RURAL WORTH | 21 | real-estate About text, HVAC titles |
| A073 | Blueprint Archive | 3 | earlier tag AI avatar |
| A190 | Home Fix Garage | not found | About: "Hi, I'm a retired HVAC pro …", a persona in all but name |

## Doubtful cases

| Row | Channel | Typed | Why doubtful |
|---|---|---|---|
| A027 | The Smart Way to Buy HVAC with Doug Cross | faceless persona (low) | Talking-head selfie look; earlier tag AI avatar. Needs a video check for lip-sync. |
| A098 | FurnacePrices.ca | on camera (low) | Smooth studio presenter in 2 of 4; may be an AI avatar. |
| A065 | Home Performance (103,000) | on camera (low) | No face in 4 thumbnails. The About names the hosts (Corbett and Grace Lunsford). By the thumbnail rule alone it would read faceless. |
| A061, A137 | Michaels HVAC Service, AC Professor | on camera (low) | Face in only 1 thumbnail. |
| A144 | Maryland Hvac Repair | faceless (low) | The About names a real person ("Ernie Braveboy"), but the men in the thumbnails look AI-made. |
| A054, A163 | TheUnknownMarks, Repara Fácil USA | faceless persona (low) | Recurring man; AI or real is unclear. |
| A069 | hvacrepairguy | faceless persona (medium) | Only videos under 5:00 in its Latest list. |
| A099, A221 | HomeFix Guide, DaVine Air | faceless (low), brand (low) | 1 video each. |
| A003, A008, A068, A106, A152, A195, A209 | company channels with one recurring real host | brand or on camera | The split is a judgment. I used "named host in About = on camera". A008 Quality HVACR (132,000) and A068 Crawl Space Ninja (72,500) were tagged on camera before. |
| A005, A020, A025, A052, A059, A084, A187, A198 | real tradesmen filming hands only | faceless (medium) | The re-check flipped 2 such channels to on camera, so some of these may show a face in older videos. |

Topic drift seen in the titles: A024 Hank Cole's 4 newest videos are about cars. A075 Passive House Secrets posts prison-escape and retirement videos. A109 The Thought Provocateur (formerly The HVAC Dope Show) posts politics. A158 Talyn875's newest video is a goodbye.
