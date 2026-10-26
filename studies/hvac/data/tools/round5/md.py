import re
A=open('analysis.txt').read()
def sec(title):
    m=re.search(r'### '+re.escape(title)+r'[^\n]*\n(.*?)(?=\n### |\Z)',A,re.S); return m.group(1).strip()
def tbl(title):
    return '\n'.join(l for l in sec(title).split('\n') if l.startswith('|'))
top10hdr='| Rank | Video | Channel | Views | Multiple | Style group | Thumbnail words |\n|---:|---|---|---:|---:|---|---|\n'
md=f"""# HVAC round 5: thumbnails of the top 100 and the recent winners

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

{tbl('TABLE1')}

Readings from the table:

- **The all-time top 100 is mostly real photos** (81 of 100 look like real photos): a home-made build or product with short text (36) or no text (17), a real person at work with no text (10), or a real YouTuber face with text (17).
- **The recent winners are mostly AI images** (92 of 120): an AI build or object (35, with or without words), an AI persona with bold words and usually a red arrow (23), an AI persona beside a stove with no words (10), AI cut-away houses with a buried-pipe claim (8) and AI store fronts with a list (6).
- Look follows upload year (measured on these 214): uploads to 2023: 66 of 74 real photos, 3 AI; 2024: 10 of 10 real; 2025: 8 real, 19 AI of 32; 2026: 12 real, 77 AI of 98. So "real photo versus AI" in this table is largely "old versus new", not a test of which style wins.
- Within the recent lists, the highest median multiples are the cartoon / sketch group (1,038x, n=8), the AI cut-away claim houses (430x, n=8), AI store fronts (421x, n=6, but low views: median 243,492) and the AI persona beside a stove with no text (320x, n=10). Real faces with text have the lowest recent multiple (6.3x, n=12), because they are mostly big channels (Linus Tech Tips, Guy Martin, Project Farm). These are small groups; read them as leads, not proof.

## Which styles go with the biggest videos

### All-time top 100, by rank

{tbl('TIERS top 100 all-time, by views')}

The all-time top 10:

{top10hdr}{tbl('TOP10 top100')}

### Last 12 months, top 50 by views

{tbl('TIERS last 12 months, top 50 by views')}

The 12-month top 10:

{top10hdr}{tbl('TOP10 12m-views')}

### Last 90 days, top 30 by views

{tbl('TIERS last 90 days, top 30 by views')}

The 90-day top 10:

{top10hdr}{tbl('TOP10 90d-views')}

### By multiple (recent lists)

Last 12 months, top 50 by multiple:

{tbl('TIERS last 12 months, top 50 by multiple')}

Last 90 days, top 30 by multiple:

{tbl('TIERS last 90 days, top 30 by multiple')}

### Features by tier

{tbl('FEATURES')}

Readings:

- **The very biggest videos use less text, not more.** All-time top 10: 5 of 10 have no headline text (two home-made coolers/burners, a real installer, an AI old man at a stove, a slush-hack-type photo); 12-month top 10: 5 of 10 have none. The three biggest 12-month videos by views include two thumbnails with no words at all: an AI old man warming his hands at a home-made stove (`RotAhlS7LQ4`, 11.9M; `H2SrcFJ8g6s`, 7.5M).
- **The no-text winners are "show the thing working":** a flame, a glowing coil, mist, a cut-away. Of the 18 real no-text photos, 17 are in the all-time top 100 (median 4.9M views).
- **Lower down the recent lists, the AI persona + bold words + red arrow style takes over:** 23 of 120 recent thumbnails, 9 of the 90-day top 30 by views and 12 of the 90-day top 30 by multiple, but none in the 12-month top 10 by views. Its median views are lower (545,458 recent) but its median multiple is high (193x): it does well for new, small channels.
- **Red arrows and circles** rise from 13% of the top 100 to 29% of the recent set; **before/after or split** from 3% to 14%.
- **Faces:** a third of the top 100 show a face (27 real, 4 AI); about half of the recent set do, and those are mostly AI (39 AI, 12 real, 6 cartoon).

## Text length and colour

{tbl('WORDS')}

Text colour (a thumbnail with several colours counts under each):

{tbl('COLOURS')}

Readings:

- **Short text is the norm:** median 3 words in the top 100, 5 in the recent set (when there is text). Most top 100 headlines are 1-6 words ("ROOM HEATER", "These suck (no, really)", "Stop Buying These", "$5 FIX").
- **Recent thumbnails carry more words** (29 of 92 with text have 7+ words, against 7 of 66 in the top 100): stacked claims such as "ATTIC IS A TRAP" / "75°F YEAR ROUND" / "160°F DEADLY HEAT" / "BURIED SINCE 1824" / "$4 TO BUILD" / "NASA HID THIS" (19 words, `H8-QNBd7MIo`). In the recent lists, more words go with fewer views (11+ words: median 306,194) but a higher multiple (354x): long text is a small-channel style.
- **White is the base colour** (about 80% of thumbnails with text in both sets). **Yellow and red double in the recent set** (yellow 23% to 50%, red 24% to 45%). White plus yellow together: 7 of 66 top 100 thumbnails with text, 33 of 92 recent. Text on a coloured box or banner (red brush stroke, black bar, yellow box): 11 of 66 top 100, 40 of 92 recent.
- The recent house style (my reading): big white condensed capitals, one key word in yellow, a red brush-stroke or red bar under a second line, and a red curved arrow to the object.

## The style groups, with 3 example IDs each

The three biggest videos in each group (views pulled 2026-10-26; list: top100 / 12m / 90d).

{sec('EXAMPLES')}

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
"""
open('/home/user/niche-research/studies/hvac/round5/thumbs-top-winners.md','w').write(md)
