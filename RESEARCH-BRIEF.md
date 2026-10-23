# Research brief: the HVAC and electrical niche studies

Set by the operator on 2026-10-23. Two research chats run side by side, one per niche. Both follow this brief exactly, so the two studies can be compared. When something here doesn't fit what you find, tell the operator and ask; don't quietly change the method.

**What it's for:** two new channels.
- **Roger the HVAC Guy:** a new channel, run alongside Roger the Pipe Guy (who carries on). The persona and niche rules stay very close to Roger's, hitting the same triggers.
- **Frederick Barnes, a new brand:** electrical DIY, staying safe doing electrical work, avoiding electrical mistakes, and fire prevention. He moves from his old fire-prevention channel, Just Stop Fire. The audience overlaps with plumbing and HVAC, but the emotions are different, and "we're going to really focus on emotions". His background (firefighter, electrician, lineman, none) is open; his book changes.

**The order of work:**
1. Research.
2. Back and forth with the operator.
3. Conclusions.
4. Then, on the operator's call, the ideation skill, the base ideation plan and the thumbnail plan, in this repository.
5. The scripting happens later, in `KPMYT/script-system`.

---

## 1. Scope of each study

### HVAC study (`studies/hvac/`)

- **Start from:** Silver Cymbal's HVAC videos (about 35 on the channel as of 2026-10-22), plus his insulation and energy-bill videos.
- **Spread out to:**
  - AC (central, window, mini-split)
  - heat pumps and furnaces
  - boilers, radiators and steam ("old-house heat")
  - thermostats, filters, ducts and vents
  - capacitors and other parts homeowners touch
  - seasonal maintenance
  - energy bills, insulation, drafts and weatherstripping
  - humidity and dehumidifiers, indoor air
  - heat during power outages
  - brand verdicts ("the only X brands worth buying")
  - anything else the search turns up
- **Channels already known** (re-check them; don't assume): Ray Dutton's Garage, HVAC Exposed, Vent Exposed, John The HVAC Guy, Exposi, Hank Cole, Gus Whitaker, The DIY HVAC Guy. Ray Dutton's Garage is a faceless "retired HVAC pro", Roger's model exactly. How a new Roger channel stands apart from it is a key question.

### Electrical and fire prevention study (`studies/electrical/`)

- **Start from:** Silver Cymbal's electrical videos (about 44 as of 2026-10-22).
- **Spread out to:**
  - wiring mistakes, outlets and switches, GFCI and AFCI
  - breakers and panels (including Federal Pacific and Zinsco)
  - old wiring (aluminium, knob-and-tube)
  - extension cords, power strips and surge protectors
  - lighting and LED, ceiling fans
  - generators and backfeed safety
  - lithium batteries (e-bikes, chargers, power banks)
  - space heaters
  - testers and multimeters
  - the electric bill
- **Fire prevention, on its own and where it overlaps electrical:**
  - smoke and CO alarms
  - dryer vents
  - kitchen and grease fires
  - extinguishers and escape plans
  - holiday lights
  - the habits that start house fires
- **Channels already known** (re-check them): Walt Brennan ("Retired Utility Man"), The Apprentice's Guide, Rational Buyer, FixItWithFil, Remote Electrician, The New Home Illusion.
- **Also study who presents** (for the open background question): electricians, linemen, firefighters, fire inspectors, home inspectors, or no stated trade. For each: how many channels, and how they perform.
- **Frederick's own history** is in `script-system/studies/home-diy/frederick-baseline-2026-10/`: his 23 old scripts, their views and an analysis.

### Both studies

- **Long-form only:** 5 minutes or more (300 seconds), in English. No Shorts.
- Re-check `findings/2026-10-22-hvac-and-electrical.md` as part of the study; don't build on it unchecked.

---

## 2. What each study delivers

Everything goes in the niche's folder (layout in section 5). Use tables, and give video IDs and channel handles so every row can be checked.

1. **The channel census: as many channels as you can find, in as much detail as possible.** One row per channel:
   - name, handle and link
   - **type:** on camera / faceless / AI avatar / faceless persona (a named character with AI images and an AI voice)
   - persona and claimed background
   - subscribers, total views and the date it started
   - videos, upload pace, monthly views and estimated monthly earnings (and RPM where available)
   - NexLev outlier score
   - top 3 videos (title, views)
   - main sub-niches
   - what it sells (book, course, affiliate)
   - source and date pulled
2. **New channels taking off:** started in the last 12 months (or a pivot that restarted in that window) and well above their niche, with the videos that took them off.
3. **The sub-niche map:** every topic, with:
   - how many videos and channels cover it
   - the typical views
   - the typical multiple (views divided by that channel's typical video)
   - the share of videos at 2x or more
   - the biggest videos
4. **The emotions in each sub-niche.** Label each video with up to three emotions from the list in section 3. Report every emotion that matters in each sub-niche, not just the top one, with example titles. Where the label is your reading, not a count, say so.
5. **Thumbnail styles, shown visually.** Download the thumbnails (top 100, recent winners, each main channel's top 5) and label each one's style:
   - face or no face
   - the person or object shown
   - text (how many words, colour, the words themselves)
   - arrows and circles
   - before and after
   - red or green marks
   - the background
   - the overall look (realistic, AI, cartoon)

   Build one page that shows them grouped by style, with views under each (publish it as a private Artifact and save the HTML in the folder). Count which styles go with the biggest videos.
6. **What has worked recently:**
   - the top videos of the last 90 days and the last 12 months, by views and by multiple
   - the topics and formats rising or falling compared with all-time
7. **The top 100 videos of all time** in the niche: long-form, English, ranked by views. For each: title, channel, views, upload date, length, sub-niche, format, emotions, villain (if any), and a thumbnail link. These are the big evergreen topics to spin off from.
8. **The keyword sweep:**
   - many different keywords (list them all, with where each came from)
   - each searched for relevance, newest, oldest and most viewed
   - the formats that keep coming up (mistakes, "X vs Y", "the only X I'd buy", "before you do X", "Y doesn't want you to know", cheap hacks, myth-busts, how-to, story, test), with their counts and performance
9. **The conclusions** (once the operator has been through the findings):
   - what the channel should make
   - which emotions and villains to use
   - which titles and thumbnails to use
   - where the gaps are
   - how to stand apart from the leaders
   - what the scripting pack should take from this

---

## 3. Labels (use the same ones in both studies)

**Emotions.** Start from the 18 triggers in the plumbing study (`script-system/studies/plumbing/comparison/05-emotions.md`). Add a new one only when none fits; name it, mark it new, and define it in `labels.md`.

E1 fear of the big bill · E2 resentment of the service call · E3 distrust of the store shelf · E4 dread of silent, hidden damage · E5 emergency dread and urgency · E6 frustration of failed attempts · E7 disgust · E8 satisfaction of the clear payoff · E9 embarrassment and household shame · E10 insider curiosity · E11 being let in · E12 vindication and the myth-bust · E13 pride in self-reliance · E14 relief and reassurance · E15 nostalgia and inherited wisdom · E16 protectiveness (family, pets, parents) · E17 safety fear · E18 rule-curiosity and mild defiance

**Villain:** the HVAC or electrical company / the service call / the upsell / the bill-sender (utility) / the maker and the store shelf / the last owner or the flipper / your own habit / none. The technician as the friendly insider is not a villain; mark it "insider".

**Format:** the list in deliverable 8, plus any new ones you find (define them in `labels.md`).

**The multiple:** views divided by the median views of that channel's long-form videos from the last 12 months (if it has fewer than 10, use its last 30 long-form videos). Say which you used.

---

## 4. Sources and method

- **NexLev:** niche finder (semantic searches with many phrasings), channel analytics, outliers, similar channels, batch metrics, `check_faceless_channel`, `youtube_search`, suggested videos, channel videos, video details and transcripts where needed.
- **YouTube pages, loaded directly:**
  - search results, sorted by relevance, upload date and view count
  - each main channel's Videos tab, sorted Popular and Oldest
  - suggested videos ("up next")

  Check that each sort filter really works before relying on it. A logged-out load works from the cloud chat (tested 2026-10-23: about 44 videos a search page).
- **The YouTube homepage:** only logged out from here. A trained, logged-in homepage would need the operator's own browser (Claude in Chrome or Cowork); that's an optional extra the operator may run separately.
- **Web search:** about 200 searches a round, shared by all helpers.
- **Rounds** (each one's helpers run in parallel, and their work is committed as it lands):
  1. Seeds: Silver Cymbal's videos in the niche, pulled and labelled.
  2. Spread: keyword sweep, niche finder, similar channels, suggested videos. Build the channel list.
  3. Census: metrics for every channel; the video pull for the top 100, the recent winners and the sub-niche map.
  4. Labelling: sub-niche, format, emotion, villain.
  5. Thumbnails: downloads, labels, the page.
  6. Checking: a second set of helpers re-checks a sample of every table against the source (views, lengths, dates, English, types). Fix and log what they find.
  7. Report to the operator, then the back and forth.
- **Every helper's brief** names its sources and its output file, and asks for quoted titles, IDs and view counts. Every report is checked before it reaches the operator.

---

## 5. Folder layout (per niche)

```
studies/<niche>/
  README.md            what's here, the status, the dates pulled
  log.md               every round: what ran, how many helpers, what changed
  labels.md            label definitions (emotions, formats, villains, types), including any new ones
  channels.md          deliverable 1 (and channels.csv)
  new-channels.md      deliverable 2
  subniches.md         deliverable 3
  emotions.md          deliverable 4
  thumbnails/          deliverable 5: images, labels.csv, thumbnail-styles.html
  recent-winners.md    deliverable 6
  top-100.md           deliverable 7 (and top-100.csv)
  keyword-sweep.md     deliverable 8 (and formats.md)
  data/                raw pulls (JSON, CSV) and the small scripts used
  CONCLUSIONS.md       deliverable 9, after the back and forth
```
