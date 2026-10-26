# Round 3 census: channel types, tier C (123 channels)

Typed 2026-10-26 by the round 3 "types C" helper. Covers every row with `tier = C` in `data/raw/census-channels-2026-10-26.csv` (123 channels). Tiers A and B are done by other helpers. **Every type here is my reading of thumbnails plus the channel's own text. None of it is measured.** No web searches were used (cap 0).

**Files**

| File | What it is |
|---|---|
| `data/raw/census-types-C-2026-10-26.csv` | One row per channel: channel_id, name, handle, subs, type, type_basis (the 4 video IDs viewed), persona_name, persona_pictured, claimed_background (quoted, or "not found"), confidence, style_note, sheet row, the earlier reading by the "sells" helper, date. |
| `thumbnails/census-sheets/C/sheet-01-rows-001-008.jpg` … `sheet-16-rows-121-123.jpg` | 16 contact sheets (JPEG). One row per channel: row number, name, subs, and its 4 newest long-form thumbnails. Row numbers match the order of the CSV. |

## Method

1. **Videos.** For each channel, from its census JSON (`data/raw/census-2026-10-26/<channelId>.json`, Videos tab pulled 2026-10-26): the 4 newest videos in the Latest sort with length 5:00 or more. All 123 channels had at least 4, so none were padded with shorter videos.
2. **Thumbnails.** `https://i.ytimg.com/vi/<id>/mqdefault.jpg` for all 492 videos (direct loads, 2026-10-26, 0 failures). Contact sheets built with Python PIL, 8 channels per sheet. Each sheet was read by eye.
3. **Text.** The channel name, the About text (`channels-master-about-2026-10-24.json`; only 50 of the 123 have an About record, and 48 of those have a description), and the 2 video descriptions per channel the "sells" helper pulled (`census-sells-desc-2026-10-26.jsonl`). I searched those for self-descriptions ("I'm…", "my name", "years", "retired", "AI"). Backgrounds are quoted exactly with their source. Where none was found it says "not found". I made none up.
4. **Rules used** (`labels.md` section 5, plus the brief for this task):
   - **on camera**: the same real-looking person appears across the thumbnails, or the About text names real presenters.
   - **faceless persona**: the same AI-generated character recurs across the thumbnails (usually named in the channel name, About or descriptions; 6 are unnamed and marked so).
   - **faceless**: hands, products, renders, stock or AI scenes with different people each time, or cartoons. A channel that *names* a narrator who is never pictured (Mason Reed, Silas Yoder, Eli Yoder, Dean) stays **faceless**, with the name recorded and `persona_pictured = no`.
   - **AI avatar**: only for a consistent lip-synced talking-head studio look. No tier C channel showed that in thumbnails. A thumbnail can't show lip-sync, so this type can't be confirmed from thumbnails alone.
   - **brand**: a logo with branded staff. None in tier C.
5. **Spot check.** I reloaded 12 doubtful thumbnails at a larger size (`hqdefault.jpg`): Darrin Stevenson, Caleb Greer, Backyard Low Tech, Ray, TrustRanker, Wade Corbin (2), Consumer Pick, Christopher Johnson, Gary Miller, Harry B, Lone Star Prepping. All 12 readings held. Working rule 3 still applies: a second helper should re-check a sample against the sheets before this goes to the operator.

## Counts by type (reading)

| Type | Channels | high | medium | low |
|---|---|---|---|---|
| faceless | 68 | 43 | 19 | 6 |
| faceless persona | 34 | 22 | 11 | 1 |
| on camera | 21 | 18 | 1 | 2 |
| AI avatar | 0 | | | |
| brand | 0 | | | |
| **Total** | **123** | 83 | 31 | 9 |

Of the 34 personas, 28 are named and 6 are unnamed recurring AI characters.

## Faceless personas (34)

Subscribers come from the census CSV (Videos tab header, 2026-10-26, rounded). Row numbers refer to the contact sheets.

| Row | Channel | Persona | Subs | Claimed background (quoted) | Conf. | Look |
|---|---|---|---|---|---|---|
| 75 | Silas Mercer | Silas Mercer | 149,000 | About: "I'm Silas Mercer, a lifelong frontiersman ... Drawing from my own everyday experience living entirely off the grid" | high | AI old mountain man (wide hat, long grey beard) in cabins |
| 54 | Earl Knows How | Earl | 43,900 | not found (sells "Earl's Home Repair Manual", video lWHN6GgFcA4) | high | AI old man (cap, white moustache), "WHICH ONE WINS?" comparisons |
| 65 | Ray Sutter | Ray Sutter | 32,000 | not found (sells a "315-page illustrated guide · $47", video icGMjokbmUA) | high | AI older man (grey hair, cardigan) beside stockpiles |
| 2 | Frugal Frannie | Frannie | 27,500 | "a grandmother who knew the value of a dollar" (video oLuOs5Gx4WI); title "I Haven't Bought Paper Towels in 40 Years" | high | AI grandmother (white hair, red cardigan) |
| 32 | Jhon Construction | Jhon | 23,300 | not found (site jhon-construction.com) | high | AI old man (white beard, glasses, blue shirt): the same character as row 15 |
| 84 | WiseMoney | (unnamed) | 22,000 | not found | medium | AI young East-Asian man (glasses) with carts and panic crowds |
| 58 | Caleb Greer — Off-Grid Water & Power | Caleb Greer | 20,500 | About: "I'm Caleb Greer and I build off-grid water and energy systems on my property" | medium | photoreal man in a red "GREER OFF-GRID" cap; AI is my reading |
| 60 | Backyard Low Tech | (unnamed) | 12,300 | not found (sells "The Backyard LowTech Systems Manual") | medium | AI older man (navy polo) with stoves, salt bucket |
| 8 | Christopher Johnson | Christopher Johnson | 7,100 | "I draw on my experience as a locksmith across the north of England" (video Phtfiy7eVBw) | medium | AI British man (gilet, plaid), Poundland, UK heating |
| 98 | Richard Nakamura Secrets | Richard Nakamura | 4,000 | About: "I spent thirty years fixing the machines people were about to throw away"; "I fixed appliances in other people's homes for thirty years" (video 71D4-5UmgU8) | high | AI Japanese-American man (olive polo) at appliances |
| 16 | Eli Forgotten Ways | Eli | 3,940 | not found | high | AI Amish-style old man (straw hat, white beard) |
| 68 | The Hillbilly Way | Billy Ray McCoy | 2,610 | "Billy Ray McCoy, sixth-generation Appalachian homesteader ... from Sassafras Holler" (video csonQscHgNE) | high | AI old man (felt hat, overalls) |
| 112 | David Bennett | David Bennett | 1,880 | not found (no About, no description data) | high | AI older British man in Tesco/B&M |
| 11 | Harlan Pike Prepping | Harlan Pike | 1,260 | not found ("We use AI tools to support the production of this video", video OCfVJ8OigBc) | high | AI grey-haired man in snow |
| 46 | Ivan's Survival Journal | Ivan | 1,250 | "After years of preparing for winter emergencies and experiencing multi-day power outages, I tested..." (video MNgN_P7e-tw) | high | AI old man (grey hair, moustache, sweater) |
| 97 | Kate Sullivan Ready Living | Kate Sullivan | 1,170 | "I've spent 20 years in home safety, working with retired officers and emergency responders" (video 8Nh34wXH25I) | high | AI woman (red buffalo-check coat) |
| 43 | Linda Fairbrook | Linda Fairbrook | 895 | "the 7 things I'm doing at my own house before the first freeze" (video WyrCiiTJPso) | high | AI woman (braid, glasses, mustard cardigan) |
| 40 | Gus Halvorsen | Gus Halvorsen | 727 | "Up here in the Alaskan bush, nobody owns an air conditioner" (video Vrd7qN3rkYc) | high | AI old man (beanie, plaid) |
| 87 | Vault Breaker | (unnamed) | 569 | not found (titles "A Japanese Housekeeper's $3 Secret ...") | medium | AI East-Asian man (glasses, apron) |
| 100 | Dan Cooper / Ready Home | Dan Cooper | 452 | "I built houses in Ohio for thirty-five years. I'm Dan Cooper." (video ZPmG1ZT0WVg) | high | AI older man (grey beard, plaid) |
| 15 | Jhon Survival Mode | Jhon | 436 | not found ("The stories in this channel are told to illustrate the methods", video Y0uOxQtpFNc) | high | same character as row 32 |
| 66 | BIG TICKET TRUTH | (unnamed) | 420 | not found | low | photoreal young man in a "BIG TICKET TRUTH" cap |
| 79 | The Old House Fix | (unnamed) | 342 | "My grandfather built a water pump seventy-nine years ago" (video 5cWM-dGe-Dg) | high | AI older man (suspenders, shocked face) |
| 39 | Old Amish Wisdom | Elias | 331 | "Elias shares the old barn-wall lesson his grandfather taught him" (video Wgc7ScpQItQ) | medium | AI Amish old man (black hat) in 3 of 4 |
| 18 | Ray | Ray | 309 | "I spent thirty-five years on the lines for a utility company" (video MlrIAWIDI3Q) | high | AI grey-haired man, navy work shirt with "RAY" name patch; HVAC titles |
| 13 | Gary Miller | Gary Miller | 214 | "built from twenty-two years in the Army and two decades of preparing" (video runSR6-BTno) | medium | AI bald man with dog tags |
| 3 | Darrin Stevenson | Darrin Stevenson | 203 | not found | medium | same middle-aged man pointing at AI homes (could be a real face composited) |
| 7 | Hank Dockery | Hank Dockery | 281 | not found ("Educational content from one household getting ready") | high | AI old man (white beard, plaid) |
| 62 | Ray Donnelly DIY | Ray Donnelly | 246 | About: "Hi, I'm Ray. I've always been the guy who'd rather fix it himself than pay somebody else to do it." | high | AI older man (glasses, blue shirt) |
| 71 | Rosalind Gray Cooking | Rosalind Gray | 161 | not found | medium | AI older woman (blonde bob, red cardigan, apron) |
| 61 | Del Rasmussen | Del Rasmussen | 128 | not found | high | AI old man (white beard, tan vest) |
| 42 | Japanese Offgrid Survival | (unnamed) | 100 | not found (the About is about shipwrecks: "This channel investigates the wrecks, disasters, and naval failures") | medium | AI older Japanese man, Japanese flag |
| 111 | Paddy's Old School Fixes | Paddy O'Rourke | 35 | About: "I'm Paddy O'Rourke — 40 years a plumber in Boston, now retired to my basement workshop" | high | AI old man (flat cap, Aran sweater), "STOP ..." titles |
| 41 | Wade Corbin | Wade Corbin | 14 | "My name is Wade Corbin." ... "I am not an exterminator." (video GyxAzZTn8RU) | medium | weathered AI man in 2 of 4 |

**What stands out (my reading):**
- **No tier C persona claims to be an HVAC technician.** The trade backgrounds claimed are utility lineman, 35 years (Ray), plumber, 40 years (Paddy O'Rourke), appliance repairman, 30 years (Richard Nakamura), house builder, 35 years (Dan Cooper), locksmith (Christopher Johnson), Army, 22 years (Gary Miller) and home safety, 20 years (Kate Sullivan). Ray is the closest to "Roger the HVAC Guy": a name patch on a work shirt and titles like "5 AC Mistakes HVAC Companies Hope You Keep Making" and "The $30 AC Filter Is Destroying Your HVAC System". He has 309 subs.
- **Most personas are very new and small.** 22 of the 34 are under 2,000 subs. Only Silas Mercer (149K) is above 50K.
- **Same-operator signs** (shared wording or art; my reading, not proof):
  - Jhon Survival Mode and Jhon Construction (rows 15 and 32) use the same AI character.
  - Hank Dockery and Linda Fairbrook (rows 7 and 43) share the disclaimer "Educational content from one household getting ready."
  - The Review Guy and NextGadget (rows 25 and 113) use an identical "WHO WINS IN 2026?" template.
  - Creative Craft Ideas and Creative Cement Ideas (rows 80 and 116) use the same cement-stove-on-orange-tile style.
- **Repeated topic (measured from titles):** the aluminium-mesh solar air heater appears in 4 channels' newest titles:
  - Jhon Construction: "I Tested This $35 ALUMINUM MESH — It Blows 140°F Heat Into Your House"
  - Old Amish Wisdom: "This $35 ALUMINUM MESH Blows 140°F Heat Into Your House No Gas NEEDED"
  - Christopher Johnson: "This £30 ALUMINIUM MESH Blows 60°C Heat Into British Homes"
  - Caleb Greer: video fOW5Cv5cBoM, "blows 140°F air directly into the house"
- **Persona thumbnail formula (common to most):** one photoreal AI older man or woman pointing at the object, 2 to 4 words of huge white and yellow condensed text, a red or yellow arrow and a price tag. Store backdrops (Walmart, Dollar Tree, Home Depot, Tesco) are used for the "items to buy" lists.

## On camera (21)

Footprint Hero with Alex Beale, Country Living Experience, DIY Solar Power with Will Prowse (1.15M), The Provident Prepper (low), GerrysDiy, Everything Electric TECH, Greenhill Forge, Stefano Creatini, Mr. EV, Lone Star Prepping (low), Jonathan Tracey, Nicolas Raimo, Stay Ready. Urban Survival., Porter Creek, Major Dad's Garage, Tim & Kat's Green Walk, andyfireblade, matty tripps, Phil G, Colleens Reviews, Applisense (medium).

## Faceless (68)

The CSV has all 68. Main kinds:
- product-roundup and affiliate channels: 14 (rows 12, 17, 25, 29, 30, 36, 37, 56, 57, 76, 81, 88, 108, 113), e.g. TrustRanker, Tool Junkie, AirWater Base, TempTrends
- AI-render "forgotten/banned tech" channels: e.g. Wild Line, Hidden Build, The Archive of Builds, Grain & Gravity, The Passive House Files, Elderly Thoughts
- AI "grandma/grandpa" scene channels with no fixed character: Lost Survival Knowledge, Wonders, No Longer Here, Saving Savers, Forgotten American Survival
- hands-only real or AI build channels: Creative Project (1.46M), Creative Craft Ideas, Homemade, Creative inventions LMTN, Penpen vn 1
- cartoons: Sketchy Survival, Sketchsurvive

## Doubtful cases

| Row | Channel | My reading | Why doubtful |
|---|---|---|---|
| 66 | BIG TICKET TRUTH | faceless persona (low) | Same photoreal young man in a branded cap on every thumbnail. The sells helper read it as **AI avatar**. A thumbnail can't show whether he talks on screen, so a video check is needed. |
| 90 | Blackout Logic | faceless (low) | The sells helper read it as **AI avatar**. In the 4 thumbnails I viewed, the man is a different AI face each time (cartoonish young man, old man in hat, MrBeast-like face), although the titles say "I Tested". |
| 22 | Mason Reed Preparedness | faceless (medium) | Named narrator ("Mason Reed breaks down...") but never pictured: Trump news collages instead. The sells helper read it as a persona. |
| 47, 50, 121 | Silas Yoder, Builds With Eli Yoder, Dean Explains | faceless | Named narrators, not pictured. They become personas if the operator counts a named voice without an image. |
| 30, 108, 17 | TrustRanker, Consumer Pick, Harry B | faceless (low) | Review roundups with a man (reused cut-out or AI or stock) beside products. Not shown presenting. |
| 3, 58, 60 | Darrin Stevenson, Caleb Greer, Backyard Low Tech | faceless persona (medium) | The faces look AI to me (same pose and lighting, too clean), but they could be real people with heavy editing. |
| 69 | Lone Star Prepping | on camera (low) | A real-looking older man in only 1 of 4 thumbnails. The other 3 are product shots. |
| 114 | The Provident Prepper | on camera (low) | No face in the 4 thumbnails (branded logo frames). The About names the presenters ("We're Kylene and Jonathan Jones") and one description says "we sit down with Ola". |
| 31, 55, 67, 94, 105 | SeidelRanch, David McLuckie, Everyday Solar, Simple Tek, desertsun02 | faceless (medium/high) | Real owners filming hands and builds. Faceless by the "no face in 3 recent" rule, but they are real people, not AI channels. |
| 1, 33, 38, 95, 27 | Lost Survival Knowledge, When Power Fails, Forgotten Home Engineering, No Longer Here, Forgotten Discoveries 2026 | faceless (low/medium) | AI seniors appear often, but not clearly the same character across the 4 thumbnails. |

**Disagreements with the earlier "sells" helper's type column** (`census-sells-2026-10-26.csv`): 9 channels.
- I read persona where it read faceless: Christopher Johnson, Gus Halvorsen, Backyard Low Tech, Rosalind Gray Cooking, WiseMoney, Dan Cooper.
- I read faceless where it read persona: Mason Reed Preparedness.
- I read persona or faceless where it read AI avatar: BIG TICKET TRUTH, Blackout Logic.

The other 47 channels it had typed agree, and it had not typed 67.

## Limits

- Types are readings from 4 thumbnails each, not from watching videos. A presenter who appears only inside videos, or only in older videos, is missed.
- "AI-generated" is a visual judgement. Some "faceless persona" faces could be real people with heavy editing.
- Backgrounds come only from the About text (50 of 123 have one) and 2 video descriptions per channel. "not found" means not in those texts.
- Subscriber counts are as recorded in the census CSV (rounded YouTube header figures, 2026-10-26).
