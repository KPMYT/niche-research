# Round 3 census: channel types, tier B (224 channels)

The round 3 "types B" helper typed these channels on 2026-10-26. The file covers every row with `tier = B` in `data/raw/census-channels-2026-10-26.csv` (224 channels). Other helpers did tiers A and C. **Every type here is my reading of 3 thumbnails plus the channel's own text. None of it is measured, and no videos were watched.** No web searches were used (cap 0).

**Files**

| File | What it is |
|---|---|
| `data/raw/census-types-B-2026-10-26.csv` | One row per channel, with these columns: row (B001 to B224, same order as the census CSV), channel_id, name, handle, subs, country, joined, type, type_basis (the 3 video IDs viewed), persona_name, claimed_background (quoted, or "not found"), background_source, confidence, style_note, sheet, method. |
| `thumbnails/census-sheets/B/sheet-01-rows-001-010.jpg` … `sheet-23-rows-221-224.jpg` | 23 contact sheets (JPEG), 10 channels per sheet. Each row shows the row number, the name, the subscriber count and that channel's 3 newest long-form thumbnails. |

## Method

1. **Videos.** For each channel I took the 3 newest videos of 5:00 or longer from the Latest sort in its census JSON (`data/raw/census-2026-10-26/<channelId>.json`, Videos tab pulled 2026-10-26). All 224 channels had at least 3, so I never had to fill in with shorter videos.
2. **Thumbnails.** I loaded `https://i.ytimg.com/vi/<id>/mqdefault.jpg` directly for all 672 videos on 2026-10-26, with 0 failures. I built the contact sheets with Python PIL and read each one by eye.
3. **Text.** I read the channel name and handle, the About text (`channels-master-about-2026-10-24.json`) and all video titles in the census JSON. I searched the titles of the persona channels for self-descriptions ("I've", "years", "retired", "tech", "inspector", "Amish", "Norwegian", and similar words). Backgrounds are quoted exactly, with their source. Where none was found the file says "not found". I made none up.
4. **Rules used** (`labels.md` section 5, plus the task brief):
   - **on camera:** the same real-looking person appears across the thumbnails, even if only in 1 of 3 (confidence drops when it's only 1).
   - **faceless persona:** the same AI-generated character recurs across the thumbnails. It is usually named in the channel name, handle, About text or a shirt patch. 9 are unnamed and marked "not found (unnamed …)".
   - **faceless:** hands, products, renders, diagrams, stock or AI scenes with different people each time. A named narrator or mascot logo who is never pictured as a recurring character stays **faceless** (Ross Does Stuff B043, Building Grounds with Greg B164, Air Purifier First B063). This matches the tier C helper's rule.
   - **AI avatar:** used only for a consistent lip-synced talking-head studio look. No tier B channel showed that. Thumbnails can't show lip-sync, so this type can't be confirmed from thumbnails alone.
   - **brand:** a company or media logo with staff or rotating presenters.
5. **Spot check.** I reloaded the 30 thumbnails of 10 doubtful channels at a larger size (`hqdefault.jpg`): B003, B019, B033, B045, B094, B118, B163, B179, B186 and B199. All 10 readings held. Working rule 3 still applies: a second helper should re-check a sample against the sheets before this goes to the operator.

## Counts by type (reading)

| Type | Channels | high | medium | low |
|---|---|---|---|---|
| faceless | 105 | 76 | 25 | 4 |
| on camera | 85 | 53 | 26 | 6 |
| faceless persona | 31 | 16 | 13 | 2 |
| brand | 3 | 1 | 2 | 0 |
| AI avatar | 0 | | | |
| **Total** | **224** | 146 | 66 | 12 |

Of the 31 personas, 22 are named and 9 are unnamed recurring AI characters. 18 of the 31 channels joined in 2026 (joined date from the census CSV).

## Faceless personas (31)

Subscriber counts come from the census CSV (Videos tab header, 2026-10-26, rounded). Joined dates come from the census CSV (YouTube About). Backgrounds are quoted. "Not found" means no claim was found in the About text, the channel name or the titles.

| Row | Channel | Subs | Joined | Persona name | Claimed background (quoted) | Conf. |
|---|---|---|---|---|---|---|
| B143 | Elias Yoder (@EliasYoderAmish) | 369,000 | 2020-08-14 | Elias Yoder | Amish: handle "@EliasYoderAmish"; titles "12 AMISH Things We Do Before the First HARD FREEZE", "Nothing Keeps a TROUGH From Freezing Here's What We Do Instead" | high |
| B033 | Ramón Delgado (@FixTheMexicanWay) | 33,600 | 2026-08-15 | Ramón Delgado | Mexican: handle "@FixTheMexicanWay"; titles "(The Mexican Way)", "This Is How We Heat Our House Without the Furnace (The Mexican Way)" | medium |
| B145 | DTD History Radio | 28,700 | 2025-06-26 | not found (unnamed older man) | not found. The About text describes another format: "your personal history radio, delivering visceral military history stories" | medium |
| B001 | Elias Homestead | 26,600 | 2026-04-09 | Elias | "Hi, I'm Elias. I was raised around people who believed in simple living, hard work, and practical wisdom passed down through generations." / "I share traditional Amish-inspired living, homesteading knowledge, senior life advice"; title "I Have Never Had a Roach in My House in 40 Years" | high |
| B046 | Let Sal Explain | 17,900 | 2024-10-06 | Sal (cartoon, not photoreal) | not found | medium |
| B052 | Sylvie Mercer | 9,950 | 2019-01-21 | Sylvie Mercer | "I'm Sylvie Mercer, a lifelong frontierswoman" / "Drawing from my own everyday experience living entirely off the grid" (About links silasmercer.shop) | high |
| B009 | Walter's Tool Talk | 8,370 | 2026-05-18 | Walter | no trade claim; About: "the place where I dig into old fishing gear, vintage tools, collectible knives, classic gear, and forgotten brands" | high |
| B102 | Dick Colter Winterproof | 2,240 | 2020-01-12 | Dick Colter | Alaska theme: titles "How Alaskans Store Them", "10 Dollar Tree Items Alaskan Households Buy Before Winter"; also "I Don't Fix Refrigerators. These Are the Only 2 I'd Buy. The Home Inspector Way" | high |
| B158 | Hidden Systems | 2,020 | 2025-05-15 | not found (unnamed reaction character) | not found | low |
| B072 | Donna Fixes | 1,920 | 2026-09-18 | Donna | titles "12 Things I Checked in Every Home Before Winter (41 Years, 400 Units)", "The $2 Trick I Used on 400 Units", "This Cheap Window Trick Kept 400 Apartments Warm" | high |
| B050 | Home Guard (@homeguardusa) | 1,590 | 2026-03-12 | not found (shirt patch "Home Guard") | titles "I Inspected 10,000 Homes. These Are the Only 2 Washing Machines I Ever Saw Last 25 Years", "I've Inspected 10,000 Homes" | medium |
| B200 | Walter Handyman (@theoldhandymanyt) | 880 | 2025-12-04 | Walter (painted-illustration style) | handle "@theoldhandymanyt"; no About text | medium |
| B191 | Walt Brandt | 719 | 2026-04-30 | Walt Brandt | titles "A Repair Tech's Checklist", "Here's What a Repair Tech Does Instead", "the 4 a Repair Tech Would Actually Buy" | high |
| B142 | Nick Salermo | 668 | 2026-07-01 | Nick Salermo | not found | medium |
| B160 | Apocalypse Survival | 357 | 2026-03-02 | not found (unnamed reaction character) | title only: "My Family's Used It for 30 Years" | low |
| B020 | Lars Halvorsen (@LarsHalvorsenNorwegian) | 307 | 2026-08-25 | Lars Halvorsen | Norwegian: handle; titles "(The Norwegian Way)", "When the Power Dies at Thirty Below, We Do Not Heat the Whole House" | high |
| B082 | They Said Buy New (@janaraab) | 134 | 2008-03-28 | Dale (shirt name patch) | not found | medium |
| B105 | Wade Caudill | 58 | 2019-05-10 | Wade Caudill | Appalachian theme: titles "25 Forgotten Appalachian Power Tricks", "The $5 Appalachian Water System" | high |
| B186 | The Appliance Guide | 47 | 2026-08-25 | not found (unnamed young man) | not found | medium |
| B182 | Practical Homeowner | 27 | 2023-10-27 | not found (unnamed older man) | not found | medium |
| B222 | Pat's DIY Insider | 27 | 2026-02-24 | Pat | "I am Pat, an industrial mechanic, handy man since birth, and real estate investor with more than 20 yrs of experience." | high |
| B163 | Shaun Meeker | 23 | 2017-08-01 | Shaun Meeker | no stated trade; title "Inside The Worst Roof Job I've Ever Seen" | medium |
| B013 | Arthur Weber | 16 | 2026-04-28 | Arthur Weber | no stated background; German theme: titles "(The German Way)", "7 Old German Habits" | high |
| B208 | Homeowner Money | 15 | 2026-09-23 | not found (unnamed man) | not found | medium |
| B114 | Caleb Vance (@CalebVanceWisdom) | 12 | 2026-09-19 | Caleb Vance | not found | high |
| B004 | Dan Carters Workshop | 7 | 2026-09-07 | Dan Carter | no trade claim; About: "Hi, my name is Dan Carter, and welcome to my channel where I show you how to fix problems around your home without getting ripped off." | high |
| B064 | Simple Savings at Home | 5 | 2026-10-12 | not found (unnamed older woman) | title "What I'd Buy First If I Could Only Buy One Winter Item After 60"; thumbnail text "GRANDMA'S 20 WARM HOUSE TRICKS" | high |
| B094 | Walt's Workshop | 1 | 2026-01-09 | Walt | not found | medium |
| B119 | Ask Rose | 1 | 2026-10-03 | Rose | "For 32 years, I was the maintenance supervisor for 140 apartments" | high |
| B019 | The House Papers | not found | 2019-12-29 | not found (unnamed recurring character) | not found (channel country: Brazil) | medium |
| B195 | Old House Walt | not found | 2008-09-24 | Walt | titles "Home Inspector: 7 Smells in Your House Never to Ignore", "7 Contractor Tricks I Watched Work on Seniors for 38 Years" | high |

**Patterns I noticed (my reading, not measured):**

- **Tradition-key personas.** Some personas are built around a culture or tradition: Amish (Elias Yoder, Elias Homestead), Mexican (Ramón Delgado), Norwegian (Lars Halvorsen), German (Arthur Weber), Appalachian (Wade Caudill) and Alaskan (Dick Colter). The largest is Elias Yoder at 369K subs. Ramón Delgado reached 33.6K subs with a join date of 2026-08-15.
- **Trade-veteran claims.** Several personas claim a trade career, the background planned for Roger: maintenance or apartments (Rose "32 years … 140 apartments", Donna "41 Years, 400 Units"), home inspector (Home Guard "10,000 Homes", Old House Walt) and repair tech (Walt Brandt, Pat). Most of these channels are small and new (2026).
- **Shared look.** Most personas share one thumbnail look: a grey-haired AI man or woman pointing at the problem, a red arrow, and 2 to 4 words in yellow or white caps. Some also use a shirt name patch (Dan Carter, Dale, Home Guard).

## Doubtful cases

| Row | Channel | Reading | Why it's doubtful |
|---|---|---|---|
| B003 | HVAC Life | on camera, low | Hands and a screen in 2 of 3; a blurred real face behind a flashlight in the 3rd. |
| B045 | Keith Smith | on camera, low | Same smiling man in all 3, but as cut-outs. Could be a real photo or an AI image. Joined 2025-12-23, 82 subs, first-person About ("I'm Keith Smith…"). Could be a persona. |
| B199 | I Like To Build Stuff | on camera, low | Same older man in cap and glasses in all 3, very polished. Could be AI-made. |
| B118 / B179 | Jay Of All Trades / HomePro Hero | on camera, medium | Look like real people but heavily retouched. The larger images held the reading. |
| B067, B162, B220 | Ben Huttash, KenTraining, Alex The Handyman | on camera, low | The real person is only partly or barely visible in 1 of 3 thumbnails. |
| B028 | Silver Cymbal | on camera, medium | A man is crouched beside the product in 1 of 3, face not clear. `labels.md` cites his face in `sHL4lBAhklA`. |
| B033 | Ramón Delgado | faceless persona, medium | Looks AI-made (smooth skin, staged scenes), but that's not proven. |
| B046 / B200 | Let Sal Explain / Walter Handyman | faceless persona, medium | The character is a cartoon or painted illustration, not photoreal. |
| B158 / B160 | Hidden Systems / Apocalypse Survival | faceless persona, low | An unnamed shocked "reaction" AI face recurs. It may be a thumbnail template rather than a persona. |
| B145 | DTD History Radio | faceless persona, medium | The About text says military-history radio, but the recent videos are homestead/heating items with a recurring AI old man. The channel looks repurposed. |
| B112 | Rational Buyer | faceless, low | A cartoon man in 2 of 3, unnamed. Could be counted as a cartoon persona. |
| B080 | You Can Do It | faceless, low | A tiny photo of real people sits in the corner of every thumbnail, most likely a logo. |
| B103 | LRN2DIY (1.28M subs) | faceless, low | No face in these 3 thumbnails. A presenter may appear in the videos, which I didn't check. |
| B209 | Fix It With Zim | faceless, low | A real woman's face is partly visible in 1 of 3. |
| B021 | Home Repair Price | faceless, medium | A price-card template with a different AI tradesperson each time and a website footer. Could be counted as brand. |
| B088 | Fixmyroof | faceless, medium | A "FIX MY ROOF" logo strip. Could be counted as brand. |
| B029, B180, B207 | Structure Tech, Homebuilding & Renovating, Rise | brand | A company or magazine logo with staff or rotating presenters. Each could also be read as on camera. |
| B198 | Build Show Network | on camera, medium | A network with several presenters. Could be counted as brand. |
| B175 | The Fixer 2 | faceless, high | Sister channel of The Fixer (B129, on camera). Typed separately from its own thumbnails. |

**Off-topic channels in tier B:** these channels have little or no home or HVAC content in their recent videos. I noted it in the style notes for whoever reviews the tiers: B027 Halden Row (food history), B076 TalkAnalysisGuy (Breaking Bad analysis) and B155 Peace TV Urdeo (religious debate).
