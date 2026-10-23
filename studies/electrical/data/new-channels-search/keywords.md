# Keywords: new-channel hunt, YouTube search side (helper 7)

Pulled 2026-10-23 with `yt.py search` (logged-out YouTube search, US/English), 1 page (about 20 results) per keyword and sort. Sorts: `views_year` = most viewed, uploaded this year (YouTube's "This year" filter, which in practice returned uploads from the last ~12 months); `month` = uploaded this month (YouTube's default relevance order inside that window); `relevance` = plain search, run for the 17 keywords marked core. One retry: "house fire prevention tips" month came back empty on the first pull and was re-pulled.

"Relevant long-form" = 5:00 or longer, English title, and the title matches the electrical / fire / outage / backup power / home inspection keyword filter in the helper script (scratchpad `tag.py`; news, crime, HOA stories, kids, games, EV cars, RV, food stockpiling, HVAC-only and plumbing-only titles excluded). This is a title filter, my reading; a few off-topic titles slip through (e.g. storm news) and some adjacent videos are dropped (e.g. titles with "stockpile"). Counts are per search page, so the same video can count under several keywords.

| # | Keyword | Source | Sorts run | Results returned (yr/mo/rel) | Relevant long-form (yr/mo/rel) |
|---|---|---|---|---|---|
| 1 | electrical mistakes homeowners | task list | views_year, month, relevance | 20/20/20 | 10/16/10 |
| 2 | never plug into power strip | task list | views_year, month, relevance | 20/20/20 | 17/16/9 |
| 3 | things electricians never do | task list | views_year, month, relevance | 12/20/20 | 12/18/17 |
| 4 | retired electrician | task list (persona) | views_year, month, relevance | 20/20/20 | 5/13/14 |
| 5 | retired firefighter warning | task list (persona) | views_year, month, relevance | 11/20/20 | 7/13/6 |
| 6 | fire marshal | task list (persona) | views_year, month, relevance | 20/20/20 | 0/4/4 |
| 7 | house fire causes | task list | views_year, month, relevance | 20/20/20 | 0/11/3 |
| 8 | space heater fire | task list | views_year, month, relevance | 20/20/20 | 10/15/3 |
| 9 | extension cord mistakes | task list | views_year, month, relevance | 20/20/20 | 9/13/12 |
| 10 | smoke detector mistakes | task list | views_year, month, relevance | 20/20/20 | 12/12/5 |
| 11 | dryer vent fire | task list | views_year, month, relevance | 20/20/20 | 3/12/2 |
| 12 | e-bike battery fire | task list | views_year, month, relevance | 20/20/20 | 6/10/5 |
| 13 | federal pacific panel | task list | views_year, month, relevance | 20/20/20 | 13/12/6 |
| 14 | aluminum wiring | task list | views_year, month, relevance | 20/20/20 | 10/9/6 |
| 15 | knob and tube | task list | views_year, month, relevance | 20/20/20 | 10/11/9 |
| 16 | GFCI outlet mistakes | task list | views_year, month, relevance | 20/20/20 | 11/15/15 |
| 17 | generator backfeed | task list | views_year, month, relevance | 20/20/20 | 15/16/15 |
| 18 | electric bill too high | task list | views_year, month | 20/20 | 10/11 |
| 19 | things plugged in at night | task list | views_year, month | 20/20 | 18/13 |
| 20 | over 60 home safety | task list | views_year, month | 20/20 | 2/0 |
| 21 | retired lineman | brief scope: retired-trade personas | views_year, month | 20/20 | 3/8 |
| 22 | retired fire marshal | brief scope: retired-trade personas | views_year, month | 20/20 | 1/7 |
| 23 | retired home inspector | brief scope: retired-trade personas | views_year, month | 20/20 | 5/8 |
| 24 | home inspector reveals | brief scope: home inspection | views_year, month | 20/20 | 5/6 |
| 25 | old house electrical problems | brief scope: old houses | views_year, month | 20/20 | 12/12 |
| 26 | whole house generator mistakes | brief scope: generators/backup power | views_year, month | 16/20 | 13/16 |
| 27 | power outage preparation | brief scope: outages and storms | views_year, month | 20/20 | 11/15 |
| 28 | lithium battery fire home | brief scope: lithium battery fires | views_year, month | 20/20 | 2/9 |
| 29 | unplug these appliances | autocomplete-style variant of "things plugged in at night" | views_year, month | 15/20 | 10/11 |
| 30 | electrical outlet warning signs | autocomplete-style variant | views_year, month | 20/20 | 11/13 |
| 31 | firefighter reveals house fire | autocomplete-style variant of "retired firefighter warning" | views_year, month | 20/20 | 3/8 |
| 32 | never do this with extension cord | autocomplete-style variant of "extension cord mistakes" | views_year, month | 20/20 | 13/14 |
| 33 | seniors home fire safety | autocomplete-style variant of "over 60 home safety" | views_year, month | 20/20 | 5/15 |
| 34 | breaker keeps tripping | brief scope: electrical DIY | views_year, month | 20/20 | 7/13 |
| 35 | zinsco panel | brief scope: old panels | views_year, month | 20/20 | 13/10 |
| 36 | power bank fire | brief scope: lithium battery fires | views_year, month | 20/20 | 2/3 |
| 37 | portable generator mistakes | brief scope: generators | views_year, month | 20/20 | 19/18 |
| 38 | surge protector mistakes | title seen in results / variant of "never plug into power strip" | views_year, month | 20/20 | 4/7 |
| 39 | electrician warns homeowners | autocomplete-style variant | views_year, month | 20/20 | 12/9 |
| 40 | hidden fire hazards in your home | autocomplete-style variant of "house fire causes" | views_year, month | 20/20 | 13/19 |
| 41 | lineman explains power outage | brief scope: lineman persona / outages | views_year, month | 20/20 | 9/13 |
| 42 | storm power outage what to do | brief scope: outages and storms | views_year, month | 20/20 | 11/15 |
| 43 | why is my electric bill so high | autocomplete-style variant of "electric bill too high" | views_year, month | 20/20 | 11/10 |
| 44 | things that use the most electricity | autocomplete-style variant (electric bill) | views_year, month | 20/20 | 3/11 |
| 45 | burning smell outlet | brief scope: electrical safety | views_year, month | 15/20 | 3/9 |
| 46 | warm outlet dangerous | autocomplete-style variant | views_year, month | 20/20 | 12/14 |
| 47 | old wiring dangers | brief scope: old houses | views_year, month | 20/20 | 14/12 |
| 48 | house fire prevention tips | brief scope: fire prevention | views_year, month | 20/20 | 8/9 |
| 49 | carbon monoxide detector mistakes | autocomplete-style variant of "smoke detector mistakes" | views_year, month | 20/20 | 9/12 |
| 50 | christmas lights fire hazard | brief scope: holiday lights (seasonal, Oct) | views_year, month | 20/20 | 3/5 |

Total: 50 keywords, 117 search pages, 2309 video results (with repeats).

## Channel-type searches (relevance, `channel` results)

Run to find persona channels by name: "retired electrician", "retired firefighter", "retired lineman", "fire marshal", "retired home inspector", "retired utility", "old electrician", "home fire safety" (raw/chsearch__*.json). They surfaced 11 persona channels the video searches missed (Earl The Electrician, Gary the Electrician, Harlan the Lineman, Walt Hensley, Lyle Brannock, Lineman Earl, Hal Brennan, Vernon Sloane, Earl Whitaker, Frank Home Check, Tom Brennan). Most other hits were tiny personal channels, fire departments and state fire marshal offices (not counted).

## Relevant under-5:00 hits (short reference, NOT counted)

Videos under 5:00 whose titles pass the same filter, top 25 by views (list-page values).

| video_id | channel | title | views | length | age |
|---|---|---|---|---|---|
| 9kjpS1vfGio | Silver Cymbal | Worst Electrical Mistake You Can Make - Backfeeding Generators | 2371253 | 4:15 | 4y ago |
| gtNrCezphEk | DIY-time Tech | How to reset smoke detector & make it stop beeping & chirping randomly for no reason. | 2200066 | 1:28 | 6y ago |
| unCD1kT0Zq8 | ClickAway Computer, Phone, Network Repair | lithium ion battery fire | 2184142 | 0:12 | 6y ago |
| yrlvfjUmpxs | Andrew DIY | New Battery & Smoke Detector Keeps Chirping How To Fix | 1725013 | 2:34 | 12y ago |
| GmRN3kL5Ah4 | DIY SITY | The #1 Cause of House Fires | 1562624 | 4:37 | 4mo ago |
| 6hkeFTzsyFM | The Funny Carpenter | The Hidden Problem That is Ruining Your Dryer! (Easy Fix) | 1414751 | 4:09 | 5mo ago |
| bu9fKfVD1bU | WSMV 4 Nashville | Solar light causes house fire | 1333870 | 3:26 | 7mo ago |
| ydRveyXkf4M | Silver Cymbal | How to Connect a Small Generator to Your House - Safe & Legal - Run Heat, Fridge & More! | 1021410 | 4:18 | 7y ago |
| Pe-L2pbQjoY | Silver Cymbal | EASY WAY to CLEAN a Dryer Vent FAST! | 842811 | 2:53 | 4y ago |
| 7LmmRJQnU3c | Felicitysolar | LUX-X-48100LG01 Lithium Battery Fire Protection Test - Built-in Aerosol Fire Extinguishing Module | 816039 | 2:43 | 11mo ago |
| dM0twdketVc | Electrical Safety First | Battery Breakdown: Inside the UK's e-bike fire crisis / ELECTRICAL SAFETY FIRST | 730808 | 0:30 | 6mo ago |
| IAAxeXhmQuE | My DIY E-Scooter | LiPo battery caught fire during charging | 627883 | 0:23 | 8y ago |
| JTbvEhm8RAw | KCRA 3 | Roseville family escapes house fire, says e-bike was charging in garage | 622687 | 2:26 | 2w ago |
| CpCoOoTRIQ0 | Silver Cymbal | How to Replace a GFCI Outlet - Not Working? | 591953 | 4:16 | 5y ago |
| j93MtW2JyN4 | Fox News | JUST IN: More than 548k power outages nationwide as winter storm hits | 528887 | 4:24 | 8mo ago |
| br1DHQJjyOo | Swarnim Tiwari | Best 20000 mAh Power banks in 2026 / Fast Charging, Long Backup, Under ₹1500 | 386570 | 4:39 | 5mo ago |
| DUo09gC6TY4 | Jonny DIY | How To Correctly Repair a Cut or Damaged Extension Cord -Jonny DIY | 369429 | 3:43 | 8y ago |
| Egq2qzk9qRo | The Wall Street Journal | E-Bike Batteries Keep Exploding. What’s the Solution? | 290227 | 4:40 | 3y ago |
| 1gEAxJQ-CAE | Kraun Electric | Help! My GFCI Outlet Won't Reset | 271832 | 1:16 | 3y ago |
| p6FBdi6rK1g | Classy Pak Tv | A power bank battery caught the fire // A lift viral video from UK/ USA sparks debates / safety must | 221960 | 3:04 | 4mo ago |
| _QDxBUgR17g | DIY SITY | The #2 Cause of House Fires | 219935 | 3:40 | 3mo ago |
| ZFpL675LKj4 | On Time Service Pros | How to Stop a Beeping Smoke Alarm / Quick Fix Tutorial | 213921 | 0:44 | 1y ago |
| kuDfDWUrEus | Schneider Electric | What Causes Electrical Fires? / Electrical Fire Safety from Schneider Electric | 207799 | 2:30 | 8y ago |
| quRgOakARio | Concord Carpenter | Tool Lab | Cleaning Smoke Alarms - Identifying a BAD Detector -  Preventing False Alarms | 205481 | 4:34 | 6y ago |
| ty93QZ8Sk9g | digitalcamproducer | Smoke Detector False Alarm Fix - How to Prevent Smoke Alarm Randomly Going Off | 204303 | 2:12 | 3y ago |

406 distinct relevant under-5:00 videos in all.
