# HVAC round 2: the keyword sweep

Built 2026-10-24 by a round 2 helper with `studies/hvac/data/tools/sweep_build.py` (rerunnable) from the logged-out YouTube search sweep run by the main session (`sweep_round2.py`). Deliverable 8 of `RESEARCH-BRIEF.md`. Formats are in `formats.md`.

**Status:** not yet re-checked by a second helper (working rule 3). Every count below is computed by the script from the raw search pages. Topic and framing labels on keywords are the keyword list's rule-based labels; format tags on titles are rule-based (see `formats.md`). Where a line says "reading", it is the helper's judgement, not a count.

Files: `data/raw/sweep-2026-10-24/*.jsonl` (raw search results), `data/raw/sweep-videos-2026-10-24.csv` (unique videos), `data/raw/sweep-keywords-2026-10-24.csv` (one row per search), `data/raw/sweep-channels-2026-10-24.csv` (every channel), `data/raw/sweep-build-2026-10-24.json` (the counts), `data/raw/format-handcheck-2026-10-24.csv` (the hand-check).

## Method

- **Source:** YouTube search result pages, loaded logged out (`hl=en`, `gl=US`), pulled 2026-10-24T06:54:55Z to 2026-10-24T08:18:59Z (UTC). Views are YouTube's own counts on the search page ("1,234 views"); lengths are the page's length text; ages are YouTube's relative text ("3y ago").
- **Sorts.** PRIORITY keywords: 4 searches each, 2 result pages each: `relevance`; `views` (sorted by view count); `year` (view count, uploaded this year); `month` (view count, uploaded this month). The brief asks for relevance, newest, oldest and most viewed: YouTube's "upload date" sort no longer works (tested 2026-10-23) and search has no "oldest" sort, so the operator approved this substitute on 2026-10-24 (old videos come from channels' Oldest tabs instead). EXTENDED keywords: relevance only, 1 page.
- **Coverage:** 600 PRIORITY searches (150 keywords x 4 sorts); 5675 EXTENDED searches of 5675 EXTENDED keywords (complete). 127,553 result rows in all.
- **Age windows (my rule, from the age text):** YouTube shows ages as min, h, d (up to 13d), w (2w to 4w), mo (1mo to 11mo), then y. `year` results count only if the age is below "1y" (under 12 months). `month` results count only if the age is in min, h, d or w (under about 5 weeks); "1mo ago" is out. A video outside the window is still kept in the video list (it is a real result for the keyword), but that search row is not counted in the per-search figures.
- **Upload date** in the CSV is approximate: pull date minus the age (1y = 365.25 days, 1mo = 30.44 days). YouTube rounds ages down, so the real upload is up to one unit earlier.
- **Long-form:** length 5:00 (300 s) or more. Live streams with no length are dropped; replays of past streams ("Streamed ... ago") with a length are kept and marked in the CSV.
- **English (rule-based):** a title is dropped if (a) 30% or more of its letters are in a non-Latin script; (b) it has 2+ common words from Spanish, Portuguese, French, German, Hindi or Urdu written in Latin letters, Indonesian or Tagalog, and more of those than English function words; (c) it has 1+ such word and no English function word; or (d) it has a letter used only in other languages (Turkish, Polish, Czech, Vietnamese, transliteration marks) and fewer than 2 English function words; or (e) it says it is "in Hindi" (or Urdu, Tamil, Spanish and so on). The word lists are `FOREIGN`, `ENGLISH` and `STRONG_FOREIGN_LETTERS` in the script.
- **Original titles (oEmbed):** logged-out search auto-translates foreign titles into English (found by the old-house heat helper, 2026-10-24). So each video's original title was fetched from YouTube oEmbed (`tools/sweep_oembed.py`, pulled 2026-10-24, raw in `data/raw/sweep-oembed-2026-10-24.jsonl`) and the English rule was run on it too. Original title checked for 25,153 of the 26,122 long-form videos that passed the search-title rule; oEmbed 401: 464, oEmbed 403: 1 (those keep the search-page check only; oEmbed 401 = embedding turned off, 404 = gone). **504 videos dropped** because the original title is not English. Titles shown in these files are the original titles.
- **Per video:** views = the highest count seen across its searches (pulls were minutes to hours apart). Keywords, sorts and topics are every one that returned it. Best rank = its best position in any search (position counts every row on the page, including Shorts and lives).
- **"Above search median" (a within-search relative measure):** for each search, the median views of the long-form English results it kept (`year` and `month` searches: only those inside the age window). Each time a video shows up in a search, it either beats that search's median or not. A group's figure is the share of its appearances that beat the median (searches with fewer than 5 kept results are not used). Across all videos this is a little under 50% by construction (the median video itself never beats it), so a format or topic well over the all-videos figure beats the other videos returned for the same keywords. A video returned by many searches counts once per search. It is not the channel multiple; that comes in round 3. The video CSV gives each video's own count (`searches_above` of `searches_counted`; `above_search_median` = yes when more than half).

### Rows dropped (counted per search row, so a video can be counted more than once)

| Reason | Search rows |
|---|---:|
| under 5:00 | 53,665 |
| no length (live / upcoming) | 2,483 |
| not English (rule, on the search-page title) | 918 |
| not English: original title (oEmbed); the search page showed an English translation | 607 |
| month search: outside my age window (video kept, search row not counted) | 149 |
| year search: outside my age window (video kept, search row not counted) | 53 |
| long-form but no view count | 5 |
| no length (other) | 2 |

Distinct titles dropped by the English rule: 648. First 15 (for checking):

- `ajUSq7KoJgE` "[ASMR] Air Conditioner Sound \| Sonido del AIRE ACONDICIONADO \| Som do AR CONDICIONADO \| 에어컨 소리" (foreign function words)
- `LOY5duLbu-Y` "May lamig ang aircon pero kulang? Huwag kang magpadagdag ng Freon agad! \| GAWIN MO ITO PARA LUMAMIG" (foreign function words)
- `RNlSzOXgUp0` "একদিনেই ১০ লাখ Loss 😱 কোথায় ভুল করলাম? \| My Trading Mistake \| AC Trader" (non-Latin script)
- `0teSMtUcEmg` "Don't Waste AC Water \| Best Usage & How to Make Money from Ac Waste Water \| in Urdu @TechKnowledge64" (title says the video is in another language)
- `eyLBaiJ_cCc` "AC Gas Leak Scam Explained \| AC सर्विस में गैस लीक बताकर कैसे हो रहा धोखा और कैसे बचें" (non-Latin script)
- `hchGCss1ujk` "पैसा बचाने के 5 ऐसे तरीके जो आपको किसी ने नहीं बताये होंगे \| Beat Inflation & Invest Smartly" (non-Latin script)
- `sOKgpnLA-Ac` "اسرار التو فير وفري فلوسك " (non-Latin script)
- `4gQWkmI0TGo` "Sardiyo Mein AC Band Karne Ka Sahi Tarika \| Paise Bachayein! 💰 AC Service At Home 🏡" (foreign function words)
- `g_yT09hsjMQ` "Air Conditioner कैसे काम करता है? 😳 AC ठंडी हवा कैसे बनाता है" (non-Latin script)
- `TLT1xlBxBQU` "KONDISI AC WINDOW REIWA SETELAH PEMAKAIAN 2 TAHUN ? APAKAH MASIH DINGIN ? BAGAIMANA CARA NYUCI NYA" (foreign function words)
- `5VqqTax_FdM` "Solution to all window AC problems in one video \|\| window ac ice problem 100% solution in Hindi" (title says the video is in another language)
- `7A38LRpGDXk` "LG AC Remote Full Guide 2026 \| All Functions Information in Hindi! #airconditioner #lgac #remote #lg" (title says the video is in another language)
- `M5lM2-zSC90` "घर में AC लगाना चाहिए या Cooler? \| कुछ भी लगाने से पहले इस वीडियो को एकबार देख लें.! #airconditioner" (non-Latin script)
- `sCV6sBriwSY` "Unboxing Portable Air Conditioner A/C - चलता फिरता AC 🥶 कूलर का ज़माना गया" (non-Latin script)
- `pDSNp_lk5tE` "Japani AC Lagwao Aur Garmi Ko Door Bhagao \| Bijli Ka Bill Fan Se Bhi Kam   Best AC 2026 \| Cheap AC" (foreign function words)

Videos dropped on the original title (oEmbed): 504. First 15 (search-page title -> original title):

- `bvSub27JivE` "Mike and his uncle fix a broken air conditioner - A Toy Story for Kids" -> "مايك وعمه يصلحان مكيف هواء معطل - قصة لعبة للأطفال" (non-Latin script)
- `BD-GkaspxwY` "Kids' Funny Adventure with the Magic AC" -> "Petualangan Lucu Anak-Anak dengan AC Ajaib" (foreign function word, no English ones)
- `idSKb7zzOeM` "Air conditioner noise / White noise / Relaxing sounds" -> "Air conditioner noise / Klimaanlage Geräusch / Bruit climatisation / Ruido aire acondicionado" (foreign function words)
- `qfquXy1FOBI` "Funny Kids Adventures with a Magical Air Conditioner" -> "مغامرات أطفال مضحكة مع مكيف الهواء السحري" (non-Latin script)
- `UTcXCOp5BVk` "Fun Kids' Adventures with the Magic Air Conditioner" -> "Divertidas aventuras infantiles con el aire acondicionado mágico" (foreign function words)
- `n9HNbLJcogo` "Funny Adventures with the Magic Air Conditioner" -> "Lustige Abenteuer mit der magischen Klimaanlage" (foreign function words)
- `x-SllU9ufc4` "Sugar and Slime Everywhere! 🍬 A Funny Air Conditioner Story ❄️" -> "Her Yer Şeker ve Slime! 🍬 Komik Bir Klima Hikâyesi ❄️" (letters used only in other languages (Turkish, Polish, Czech, Vietnamese...))
- `3cHdNgrWyhg` "The BEST Air Conditioner of 2026 is NOT the Most EXPENSIVE! - (TOP 5 UNSPONSORED)" -> "O MELHOR Ar-Condicionado de 2026 NÃO é o Mais CARO! - (TOP 5 SEM PATROCÍNIO)" (foreign function words)
- `T1xbfbbfd5k` "Funny Kids' Adventures with a Magic Air Conditioner - A Funny Video for Kids" -> "مغامرات أطفال مضحكة مع مكيف الهواء السحري - فيديو مضحك للأطفال" (non-Latin script)
- `g4v45gQC_d8` "China: "We're not making any more air conditioner parts lol" - The result of enraging Daikin... C..." -> "中国「エアコン部品もうやらんｗ」ダイキンをブチギレさせた結果…中国国策が完全停止し国家崩壊へｗ【海外の反応・ゆっくり解説】" (non-Latin script)
- `RD6Xus60ZUc` "Children learn about teamwork thanks to a magical air conditioner" -> "Les enfants apprennent le travail d'équipe grâce à un climatiseur magique" (foreign function word, no English ones)
- `jZswcICmyIs` "Portable Air Conditioner You Can Use on the Go" -> "길거리에서 쓸 수 있는 휴대용 에어컨" (non-Latin script)
- `tVJ11XmmUk8` "Feels like 104°F! I installed an air conditioner in my mother-in-law's house for the first time!" -> "체감온도 40도! 장모님 집에 처음으로 에어컨 설치 해드렸습니다!" (non-Latin script)
- `XqavjhJv6X0` "Kids' Fun Adventure with the Magic Air Conditioner - Video for Kids" -> "मैजिक एयर कंडीशनर के साथ बच्चों के मज़ेदार एडवेंचर - बच्चों के लिए वीडियो" (non-Latin script)
- `aOKDbLYDDqM` "12V ELECTRIC COMPRESSOR REVIEW, SUITABLE FOR ALL CARS" -> "REVIEW KOMPRESOR ELEKTRIK 12V, BISA UNTUK SEMUA MOBIL" (foreign function words)

### Did each sort behave? (PRIORITY searches)

| Sort | Searches | Check | Result |
|---|---:|---|---|
| relevance | 150 | none possible (no order to test) | 1,870 long-form English rows kept |
| views | 150 | views descending? | 19 of 150 searches strictly in descending view order; 329 of 2,810 adjacent pairs (12%) go up instead of down, 66 of them by more than double |
| year | 150 | views descending? Results recent? | 4 of 150 searches strictly in descending view order; 696 of 2,720 adjacent pairs (26%) go up instead of down, 162 of them by more than double; 2,794 of 2,870 dated rows (97%) inside my 12-month window |
| month | 150 | views descending? Results recent? | 19 of 150 searches strictly in descending view order; 716 of 2,258 adjacent pairs (32%) go up instead of down, 139 of them by more than double; 2,211 of 2,405 dated rows (92%) inside my 5-week window |

Rows per search (all rows on the page, before filters; 2 pages were requested for PRIORITY): `relevance` median 20, 74 of 150 searches with more than 20 rows; `views` median 20, 73 of 150 searches with more than 20 rows; `year` median 20, 73 of 150 searches with more than 20 rows; `month` median 20, 64 of 150 searches with more than 20 rows. So the second page often added nothing (YouTube's continuation, as fetched logged out, returned few or no extra rows); most searches are effectively one page of about 20.

- `views`: most out-of-order searches: "air filter" (6 rises in 19 pairs); "heat pump vs furnace" (5 rises in 19 pairs); "spray foam alternative" (5 rises in 19 pairs); "before you turn on your heat" (5 rises in 19 pairs); "do this before winter furnace" (5 rises in 19 pairs).
- `year`: most out-of-order searches: "dehumidifier" (9 rises in 19 pairs); "stay warm without power" (9 rises in 19 pairs); "space heater" (9 rises in 19 pairs); "electric bill" (8 rises in 19 pairs); "ac filter destroying" (8 rises in 19 pairs).
- `month`: most out-of-order searches: "geothermal" (10 rises in 19 pairs); "heating oil vs gas" (10 rises in 39 pairs); "save money on heating" (9 rises in 19 pairs); "air purifier" (9 rises in 19 pairs); "insulation mistakes" (9 rises in 19 pairs).
- `year`: least recent searches: "bleeding radiators old house" (2 of 4 in window); "banging radiator" (4 of 7 in window); "heat pumps leaving people cold" (2 of 3 in window); "ceiling fan direction" (16 of 20 in window); "baseboard heater" (16 of 20 in window).
- `month`: least recent searches: "adding air conditioning to old house" (2 of 4 in window); "steam radiator not getting hot" (1 of 2 in window); "central air conditioner condenser cleaning" (1 of 2 in window); "mini split vs central air" (3 of 6 in window); "banging radiator" (1 of 2 in window).

Reading: the `views` sort is mostly but not strictly descending: most rises are small, and Shorts sit between long videos in the order. The `year` and `month` sorts are looser still (a quarter to a third of adjacent pairs rise), so they are best read as "popular recent videos", not a ranked list. The `year` and `month` filters let some older videos through, which the age window above removes. The per-search figures below do not depend on the order.

## The keyword list

The keywords are `seeds/keywords-round2.md` (built 2026-10-23 from the brief's topic list, helper-added seeds, phrases from known winning titles, Silver Cymbal title phrases and YouTube autocomplete; full sources per keyword in `data/raw/keywords-round2.csv`). 5,825 keywords: 150 PRIORITY (picked by hand by the round 1 helper to cover every topic and framing) and 5,675 EXTENDED (autocomplete phrases that passed the home-HVAC word filter). That list has not yet been re-checked by a second helper. Sources of the 150 PRIORITY keywords, by kind (a keyword can have several):

| Source kind | PRIORITY keywords |
|---|---:|
| autocomplete | 118 |
| brief topic list | 69 |
| known title | 21 |
| helper-added seed | 10 |
| Silver Cymbal title | 8 |

## Per keyword (PRIORITY)

Long-form English results kept / median views of those, per sort. `year` and `month` counts are after my age window. Check: `views` and `year`/`month` rises = adjacent pairs where the next result has more views (0 = strictly descending); `in win` = rows inside the age window of all dated rows.

| # | Keyword | Topic | Framing | Source kind | relevance n / median | views n / median | year n / median | month n / median | views rises | year in win | month in win |
|---:|---|---|---|---|---|---|---|---|---:|---:|---:|
| 1 | adding air conditioning to old house | `ac-central` | plain topic | autocomplete | 12 / 528,464 | 18 / 2,437,100 | 19 / 44,608 | 1 / 366,267 | 2/19 | 20/20 | 2/4 |
| 2 | air conditioner | `ac-central` | plain topic | brief topic list, autocomplete | 17 / 2,414,166 | 11 / 9,356,062 | 7 / 3,707,997 | 7 / 110,263 | 3/19 | 20/20 | 19/20 |
| 3 | ac not cooling | `ac-central` | problem symptom | brief topic list, autocomplete | 12 / 310,402 | 17 / 2,937,395 | 16 / 340,058 | 12 / 7,848 | 2/19 | 20/20 | 19/20 |
| 4 | central air conditioning not cooling | `ac-central` | problem symptom | Silver Cymbal title | 15 / 676,986 | 14 / 2,664,794 | 17 / 425,941 | 9 / 202 | 3/19 | 19/20 | 16/20 |
| 5 | unclog ac drain line | `ac-central` | problem symptom | Silver Cymbal title, autocomplete | 8 / 561,654 | 13 / 1,676,076 | 15 / 33,458 | 15 / 650 | 1/19 | 20/20 | 16/20 |
| 6 | why is my ac blowing hot air | `ac-central` | problem symptom | autocomplete | 11 / 170,813 | 18 / 2,476,596 | 14 / 95,904 | 2 / 2,006 | 1/19 | 20/20 | 7/7 |
| 7 | ac mistakes | `ac-central` | mistakes | known title | 18 / 34,017 | 18 / 1,734,312 | 18 / 127,431 | 11 / 1,785 | 3/19 | 20/20 | 16/20 |
| 8 | secret ac trick | `ac-central` | they don't want you to know | known title | 19 / 175,541 | 18 / 1,359,734 | 20 / 487,680 | 8 / 11,785 | 4/19 | 20/20 | 10/14 |
| 9 | save money on ac | `ac-central` | cheap hack | autocomplete | 11 / 173,514 | 17 / 2,280,659 | 14 / 436,299 | 6 / 7,292 | 1/19 | 20/20 | 16/20 |
| 10 | ac freezing up | `ac-freezing` | problem symptom | brief topic list, autocomplete | 13 / 216,709 | 18 / 1,186,702 | 13 / 18,359 | 6 / 7,098 | 2/19 | 20/20 | 10/13 |
| 11 | frozen evaporator coil | `ac-freezing` | problem symptom | brief topic list, autocomplete | 18 / 91,166 | 17 / 775,314 | 16 / 1,614 | 4 / 796 | 2/19 | 20/20 | 5/5 |
| 12 | why is my ac freezing up | `ac-freezing` | problem symptom | autocomplete | 13 / 216,724 | 18 / 736,469 | 12 / 5,590 | 2 / 30 | 1/19 | 20/20 | 3/3 |
| 13 | window air conditioner | `ac-window` | plain topic | brief topic list, autocomplete | 12 / 153,272 | 17 / 4,019,112 | 17 / 501,807 | 15 / 32,029 | 0/19 | 20/20 | 19/20 |
| 14 | window ac not cooling | `ac-window` | problem symptom | autocomplete | 13 / 145,453 | 17 / 2,559,447 | 13 / 366,678 | 8 / 256 | 0/19 | 17/20 | 17/20 |
| 15 | window ac vs portable ac | `ac-window` | X vs Y | autocomplete | 11 / 98,357 | 13 / 2,793,625 | 16 / 469,472 | 11 / 114 | 0/19 | 20/20 | 18/20 |
| 16 | best portable air conditioner | `ac-window` | the only X | Silver Cymbal title, autocomplete | 19 / 32,847 | 16 / 2,022,724 | 20 / 592,636 | 15 / 15,204 | 3/19 | 20/20 | 16/20 |
| 17 | attic fan | `attic-fan` | plain topic | brief topic list, autocomplete | 7 / 207,120 | 15 / 894,509 | 19 / 229,494 | 19 / 320 | 1/19 | 20/20 | 19/20 |
| 18 | cool your attic | `attic-fan` | plain topic | known title | 11 / 152,132 | 14 / 1,205,764 | 19 / 425,941 | 16 / 238 | 2/19 | 19/20 | 17/20 |
| 19 | whole house fan | `attic-fan` | plain topic | brief topic list, autocomplete | 9 / 16,361 | 14 / 4,290,570 | 16 / 251,952 | 13 / 4,005 | 2/19 | 20/20 | 20/20 |
| 20 | boiler | `boiler-steam` | plain topic | brief topic list | 19 / 5,578,797 | 18 / 23,247,732 | 16 / 1,748,112 | 14 / 69,534 | 1/19 | 20/20 | 20/20 |
| 21 | old house boiler | `boiler-steam` | plain topic | autocomplete | 8 / 329,018 | 18 / 4,828,391 | 18 / 98,794 | 15 / 544 | 2/19 | 20/20 | 19/19 |
| 22 | steam heat | `boiler-steam` | plain topic | brief topic list, autocomplete | 5 / 40,618 | 12 / 2,164,898 | 14 / 187,734 | 15 / 2,276 | 0/19 | 20/20 | 19/20 |
| 23 | steam radiator | `boiler-steam` | plain topic | brief topic list, autocomplete | 12 / 13,643 | 12 / 1,027,528 | 17 / 13,495 | 11 / 79 | 2/19 | 20/20 | 19/20 |
| 24 | boiler no heat | `boiler-steam` | problem symptom | Silver Cymbal title, autocomplete | 15 / 29,046 | 17 / 1,246,905 | 18 / 26,506 | 15 / 676 | 0/19 | 20/20 | 20/20 |
| 25 | steam radiator not getting hot | `boiler-steam` | problem symptom | autocomplete | 13 / 153,319 | 13 / 930,467 | 7 / 251 | 1 / 875 | 2/19 | 8/8 | 1/2 |
| 26 | boiler vs furnace | `boiler-steam` | X vs Y | autocomplete | 6 / 66,462 | 14 / 157,862 | 9 / 585 | 0 / n/a | 2/19 | 20/20 | 1/1 |
| 27 | bleeding radiators old house | `boiler-steam` | how-to | autocomplete | 6 / 88,334 | 10 / 836,634 | 2 / 502 | 3 / 130 | 4/19 | 2/4 | 3/3 |
| 28 | best ac brands | `brands` | the only X | brief topic list, autocomplete | 15 / 161,125 | 18 / 1,110,588 | 16 / 714,178 | 15 / 35,585 | 2/19 | 19/20 | 20/20 |
| 29 | best furnace brands | `brands` | the only X | brief topic list, autocomplete | 18 / 27,229 | 18 / 313,534 | 19 / 48,494 | 10 / 2,390 | 1/19 | 20/20 | 10/10 |
| 30 | best heat pump brands | `brands` | the only X | brief topic list, autocomplete | 17 / 31,864 | 19 / 670,769 | 17 / 232,642 | 6 / 265 | 3/19 | 18/20 | 18/20 |
| 31 | best hvac brands | `brands` | the only X | brief topic list, autocomplete | 19 / 103,208 | 20 / 1,243,542 | 19 / 103,106 | 11 / 1,911 | 2/19 | 20/20 | 18/20 |
| 32 | hvac brands to avoid | `brands` | the only X | brief topic list, autocomplete | 19 / 47,329 | 19 / 199,222 | 20 / 47,770 | 2 / 36 | 1/19 | 20/20 | 2/2 |
| 33 | only hvac brands worth buying | `brands` | the only X | known title | 19 / 113,653 | 10 / 110,093 | 19 / 43,507 | 5 / 794 | 1/10 | 19/19 | 5/5 |
| 34 | ceiling fan direction | `ceiling-fan` | plain topic | brief topic list, autocomplete | 1 / 19,666 | 12 / 1,840,613 | 13 / 17,869 | 1 / 19,666 | 1/19 | 16/20 | 8/12 |
| 35 | ceiling fan winter | `ceiling-fan` | plain topic | brief topic list, autocomplete | 2 / 15,874 | 9 / 535,416 | 9 / 60,046 | 17 / 213 | 1/19 | 17/20 | 19/20 |
| 36 | central air conditioner condenser cleaning | `coil-cleaning` | how-to | Silver Cymbal title | 11 / 1,454,188 | 18 / 2,318,818 | 15 / 6,017 | 1 / 55 | 2/19 | 20/20 | 1/2 |
| 37 | cleaning ac unit with pressure washer | `coil-cleaning` | how-to | autocomplete | 13 / 139,723 | 16 / 2,748,886 | 13 / 118,197 | 5 / 278 | 0/19 | 17/20 | 16/20 |
| 38 | how to clean ac unit | `coil-cleaning` | how-to | autocomplete | 14 / 1,381,816 | 18 / 5,062,946 | 14 / 556,620 | 13 / 2,195 | 0/19 | 20/20 | 20/20 |
| 39 | draft stopper | `drafts` | plain topic | brief topic list, autocomplete | 2 / 6,034 | 8 / 389,211 | 10 / 1,234 | 5 / 559 | 2/19 | 20/20 | 19/20 |
| 40 | drafty house | `drafts` | plain topic | brief topic list, autocomplete | 13 / 23,945 | 15 / 79,134 | 17 / 19,094 | 20 / 207 | 1/19 | 20/20 | 20/20 |
| 41 | weatherstripping | `drafts` | plain topic | brief topic list | 7 / 188,487 | 11 / 693,644 | 11 / 17,671 | 8 / 812 | 1/19 | 17/20 | 17/20 |
| 42 | closing vents | `ducts-vents` | plain topic | brief topic list | 2 / 3,254 | 7 / 336,066 | 16 / 356 | 7 / 137 | 1/19 | 20/20 | 13/13 |
| 43 | is ac duct cleaning worth it | `ducts-vents` | myth | autocomplete | 15 / 127,328 | 14 / 254,172 | 11 / 2,264 | 1 / 5 | 2/19 | 18/20 | 2/3 |
| 44 | duct cleaning | `ducts-vents` | how-to | brief topic list, autocomplete | 16 / 149,676 | 13 / 1,693,397 | 11 / 46,932 | 9 / 7,482 | 3/19 | 20/20 | 19/20 |
| 45 | baseboard heater | `electric-heat` | plain topic | helper-added seed, autocomplete | 11 / 44,776 | 9 / 307,367 | 11 / 5,308 | 9 / 39 | 3/19 | 16/20 | 17/20 |
| 46 | electric bill | `energy-bill` | plain topic | brief topic list, autocomplete | 13 / 253,815 | 7 / 3,026,380 | 14 / 1,142,596 | 7 / 281,836 | 3/19 | 20/20 | 19/20 |
| 47 | heating bill | `energy-bill` | plain topic | brief topic list, autocomplete | 17 / 17,299 | 12 / 2,257,524 | 15 / 397,174 | 16 / 84,014 | 4/19 | 20/20 | 20/20 |
| 48 | why is my electric bill so high | `energy-bill` | problem symptom | autocomplete | 12 / 62 | 14 / 938,216 | 14 / 397,390 | 16 / 60 | 4/19 | 17/20 | 20/20 |
| 49 | why is your heat bill so high | `energy-bill` | problem symptom | known title | 9 / 916 | 16 / 314,541 | 17 / 1,349 | 19 / 180 | 1/19 | 20/20 | 20/20 |
| 50 | energy bill mistakes | `energy-bill` | mistakes | known title | 19 / 605 | 12 / 198,290 | 12 / 26,486 | 14 / 170 | 3/19 | 20/20 | 20/20 |
| 51 | power company doesn't want you to | `energy-bill` | they don't want you to know | known title | 15 / 363 | 14 / 494 | 20 / 403,020 | 2 / 68,004 | 2/19 | 20/20 | 3/3 |
| 52 | how to save money on electric bill in winter | `energy-bill` | cheap hack | autocomplete | 4 / 29,835 | 14 / 446,228 | 15 / 61,721 | 17 / 13,949 | 1/19 | 20/20 | 20/20 |
| 53 | lower your electric bill | `energy-bill` | cheap hack | known title, autocomplete | 14 / 123,754 | 14 / 2,651,406 | 18 / 443,950 | 7 / 29,438 | 2/19 | 20/20 | 19/20 |
| 54 | swamp cooler | `evap-cooler` | plain topic | helper-added seed, autocomplete | 11 / 145,665 | 15 / 1,240,002 | 14 / 289,236 | 16 / 124,778 | 0/19 | 20/20 | 19/20 |
| 55 | air filter | `filters` | plain topic | brief topic list, autocomplete | 18 / 633,440 | 13 / 1,443,540 | 13 / 426,147 | 14 / 54,541 | 6/19 | 17/20 | 17/20 |
| 56 | ac filter destroying | `filters` | mistakes | known title | 16 / 3,798 | 18 / 27,052 | 19 / 5,378 | 2 / 3,555 | 4/19 | 20/20 | 2/2 |
| 57 | furnace filter mistakes | `filters` | mistakes | autocomplete | 16 / 12,034 | 18 / 239,202 | 16 / 3,356 | 16 / 132 | 2/19 | 20/20 | 18/20 |
| 58 | furnace filters cheap vs expensive | `filters` | X vs Y | autocomplete | 11 / 687,535 | 13 / 306,910 | 3 / 350,951 | 0 / n/a | 0/18 | 3/3 | 0/0 |
| 59 | do air filters really work | `filters` | myth | autocomplete | 12 / 522,102 | 18 / 1,983,973 | 18 / 171,198 | 7 / 6,095 | 2/19 | 20/20 | 15/15 |
| 60 | how often should you change your air filter | `filters` | myth | autocomplete | 9 / 278,313 | 16 / 2,802,462 | 16 / 356,176 | 8 / 226 | 4/19 | 18/20 | 17/20 |
| 61 | furnace | `furnace` | plain topic | brief topic list, autocomplete | 18 / 238,696 | 14 / 5,063,578 | 16 / 1,129,130 | 13 / 353,708 | 3/19 | 20/20 | 16/20 |
| 62 | why is my furnace blowing cold air | `furnace` | problem symptom | autocomplete | 10 / 103,968 | 17 / 1,277,558 | 12 / 397 | 5 / 35 | 1/19 | 20/20 | 7/7 |
| 63 | save money on heating | `furnace` | cheap hack | autocomplete | 5 / 337,351 | 14 / 1,355,089 | 12 / 276,963 | 17 / 68,263 | 2/19 | 20/20 | 20/20 |
| 64 | geothermal | `geothermal` | plain topic | helper-added seed, autocomplete | 11 / 557,758 | 17 / 1,190,524 | 13 / 283,417 | 18 / 39,688 | 3/19 | 20/20 | 20/20 |
| 65 | heat pump | `heat-pump` | plain topic | brief topic list, autocomplete | 18 / 189,316 | 14 / 2,464,040 | 10 / 526,990 | 13 / 122,924 | 4/19 | 20/20 | 18/20 |
| 66 | heat pumps leaving people cold | `heat-pump` | plain topic | Silver Cymbal title | 11 / 211,297 | 5 / 37 | 2 / 23 | 2 / 23 | 0/5 | 2/3 | 2/3 |
| 67 | why is my heat pump blowing cold air | `heat-pump` | problem symptom | autocomplete | 7 / 18,891 | 17 / 2,034,672 | 9 / 10,068 | 3 / 38 | 1/19 | 20/20 | 5/5 |
| 68 | heat pump vs furnace | `heat-pump` | X vs Y | brief topic list, autocomplete | 13 / 108,861 | 16 / 2,786,146 | 14 / 624,304 | 16 / 12,096 | 5/19 | 20/20 | 19/20 |
| 69 | the truth about heat pumps | `heat-pump` | they don't want you to know | autocomplete | 16 / 287,158 | 17 / 450,066 | 18 / 57,385 | 4 / 13,074 | 1/19 | 20/20 | 6/6 |
| 70 | do heat pumps save money | `heat-pump` | myth | autocomplete | 11 / 134,166 | 14 / 566,266 | 17 / 88,235 | 16 / 952 | 2/19 | 20/20 | 19/20 |
| 71 | home warranty hvac | `home-warranty` | plain topic | helper-added seed, autocomplete | 10 / 2,653 | 10 / 335,206 | 14 / 10,222 | 17 / 88 | 4/19 | 20/20 | 20/20 |
| 72 | dehumidifier | `humidity` | plain topic | brief topic list, autocomplete | 11 / 356,231 | 11 / 946,439 | 12 / 266,601 | 10 / 5,722 | 4/19 | 20/20 | 20/20 |
| 73 | humidity in house | `humidity` | plain topic | brief topic list, autocomplete | 12 / 116,506 | 15 / 1,606,999 | 18 / 331,704 | 14 / 3,872 | 0/19 | 20/20 | 19/20 |
| 74 | dehumidifier mistakes | `humidity` | mistakes | autocomplete | 5 / 29,811 | 10 / 49,733 | 8 / 4,657 | 0 / n/a | 3/19 | 20/20 | 6/6 |
| 75 | hvac mistakes | `hvac-general` | mistakes | autocomplete | 20 / 28,294 | 19 / 1,526,472 | 18 / 198,395 | 17 / 1,879 | 3/19 | 20/20 | 20/20 |
| 76 | hvac secrets | `hvac-general` | they don't want you to know | helper-added seed, autocomplete | 15 / 26,664 | 18 / 795,160 | 20 / 250,872 | 14 / 404 | 4/19 | 20/20 | 17/20 |
| 77 | hvac tips | `hvac-general` | how-to | helper-added seed, autocomplete | 20 / 199,299 | 17 / 2,770,141 | 19 / 589,312 | 14 / 4,070 | 2/19 | 20/20 | 20/20 |
| 78 | air purifier | `indoor-air` | plain topic | brief topic list, autocomplete | 18 / 68,562 | 6 / 4,436,190 | 11 / 469,396 | 11 / 66,575 | 4/19 | 18/20 | 17/20 |
| 79 | carbon monoxide furnace | `indoor-air` | plain topic | brief topic list, autocomplete | 9 / 23,758 | 12 / 493,278 | 18 / 8,672 | 16 / 5,270 | 4/19 | 20/20 | 17/20 |
| 80 | indoor air quality | `indoor-air` | plain topic | brief topic list, autocomplete | 13 / 16,473 | 12 / 2,501,330 | 10 / 123,291 | 8 / 4,010 | 3/19 | 18/20 | 20/20 |
| 81 | attic insulation | `insulation` | plain topic | brief topic list, autocomplete | 10 / 141,747 | 16 / 1,605,832 | 15 / 354,879 | 15 / 12,596 | 2/19 | 17/20 | 19/20 |
| 82 | rim joist insulation | `insulation` | plain topic | brief topic list, autocomplete | 12 / 387,890 | 17 / 755,085 | 16 / 3,006 | 13 / 506 | 4/19 | 20/20 | 16/16 |
| 83 | spray foam | `insulation` | plain topic | brief topic list, autocomplete | 15 / 671,095 | 17 / 3,540,821 | 13 / 671,095 | 13 / 8,534 | 3/19 | 20/20 | 20/20 |
| 84 | spray foam alternative | `insulation` | plain topic | Silver Cymbal title | 14 / 51,196 | 16 / 1,836,689 | 20 / 16,562 | 2 / 6,368 | 5/19 | 20/20 | 2/2 |
| 85 | window insulation | `insulation` | plain topic | brief topic list, autocomplete | 9 / 62,354 | 13 / 1,029,110 | 17 / 216,146 | 15 / 20,463 | 3/19 | 19/20 | 17/20 |
| 86 | insulation mistakes | `insulation` | mistakes | autocomplete | 15 / 148,999 | 18 / 2,801,226 | 16 / 115,553 | 12 / 1,142 | 3/19 | 19/20 | 16/20 |
| 87 | home designs that stayed cool | `keep-cool` | plain topic | known title | 18 / 4,160 | 15 / 406,995 | 18 / 2,984 | 16 / 250 | 2/19 | 20/20 | 17/18 |
| 88 | cool house without ac | `keep-cool` | cheap hack | helper-added seed, autocomplete | 12 / 347,926 | 12 / 3,645,536 | 18 / 740,930 | 12 / 3,845 | 0/19 | 20/20 | 16/20 |
| 89 | keep house cool | `keep-cool` | how-to | helper-added seed, autocomplete | 10 / 391,921 | 10 / 2,706,586 | 20 / 366,744 | 14 / 3,002 | 1/19 | 20/20 | 16/20 |
| 90 | heat house cheap | `keep-warm` | cheap hack | helper-added seed, autocomplete | 14 / 509,515 | 17 / 1,647,013 | 20 / 912,742 | 18 / 59,060 | 2/19 | 20/20 | 19/20 |
| 91 | keep house warm | `keep-warm` | how-to | helper-added seed, autocomplete | 11 / 206 | 13 / 172,170 | 16 / 76,582 | 18 / 113,238 | 1/19 | 18/20 | 20/20 |
| 92 | before you shut your ac down | `maintenance` | before you | known title | 11 / 18,863 | 11 / 118,183 | 20 / 1,516 | 15 / 422 | 4/18 | 20/20 | 16/19 |
| 93 | before you turn on your ac | `maintenance` | before you | known title | 16 / 907,452 | 19 / 2,559,447 | 15 / 222,410 | 16 / 1,230 | 2/19 | 17/20 | 20/20 |
| 94 | before you turn on your heat | `maintenance` | before you | known title | 14 / 114,828 | 19 / 922,523 | 16 / 89,503 | 16 / 17,306 | 5/19 | 20/20 | 20/20 |
| 95 | do this before winter furnace | `maintenance` | before you | known title | 13 / 1,472 | 16 / 1,077,766 | 18 / 164,337 | 19 / 9,061 | 5/19 | 20/20 | 20/20 |
| 96 | do this once a month ac | `maintenance` | how-to | known title | 14 / 330,100 | 10 / 45,696 | 12 / 13,876 | 0 / n/a | 2/15 | 16/16 | 0/0 |
| 97 | hvac maintenance | `maintenance` | how-to | brief topic list, autocomplete | 19 / 97,960 | 15 / 2,885,405 | 17 / 589,312 | 16 / 13,154 | 4/19 | 20/20 | 20/20 |
| 98 | mini split | `mini-split` | plain topic | brief topic list, autocomplete | 18 / 205,814 | 17 / 3,087,232 | 15 / 395,227 | 13 / 35,585 | 3/19 | 18/20 | 15/20 |
| 99 | mini split mistakes | `mini-split` | mistakes | autocomplete | 11 / 133,288 | 10 / 1,682,559 | 6 / 15,290 | 4 / 317 | 2/19 | 20/20 | 16/16 |
| 100 | mini split vs central air | `mini-split` | X vs Y | brief topic list, autocomplete | 13 / 15,172 | 19 / 2,007,929 | 19 / 37,244 | 3 / 188 | 2/19 | 20/20 | 3/6 |
| 101 | ac making noise | `noises` | problem symptom | brief topic list, autocomplete | 15 / 608,848 | 13 / 3,020,583 | 19 / 365,797 | 17 / 5,290 | 0/19 | 20/20 | 19/22 |
| 102 | banging radiator | `noises` | problem symptom | brief topic list, autocomplete | 1 / 64,797 | 8 / 329,678 | 3 / 13,495 | 0 / n/a | 1/19 | 4/7 | 1/2 |
| 103 | furnace noise | `noises` | problem symptom | brief topic list, autocomplete | 17 / 838,582 | 17 / 3,618,895 | 18 / 77,863 | 13 / 163 | 4/19 | 20/20 | 20/20 |
| 104 | oil furnace | `oil-furnace` | plain topic | brief topic list, autocomplete | 17 / 132,843 | 17 / 1,864,469 | 15 / 165,849 | 12 / 6,724 | 2/19 | 20/20 | 18/20 |
| 105 | oil furnace won't ignite | `oil-furnace` | problem symptom | autocomplete | 8 / 377,514 | 11 / 866,298 | 3 / 3,699 | 0 / n/a | 1/19 | 3/3 | 0/0 |
| 106 | heating oil vs gas | `oil-furnace` | X vs Y | Silver Cymbal title | 8 / 48,819 | 17 / 3,223,542 | 19 / 734,130 | 27 / 7,077 | 2/19 | 20/20 | 34/40 |
| 107 | oil furnace vs gas furnace | `oil-furnace` | X vs Y | autocomplete | 11 / 50,764 | 19 / 1,260,201 | 13 / 34,542 | 7 / 133 | 3/19 | 17/20 | 7/10 |
| 108 | oil furnace maintenance | `oil-furnace` | how-to | autocomplete | 15 / 23,459 | 18 / 1,054,003 | 16 / 19,008 | 14 / 910 | 3/19 | 17/20 | 17/20 |
| 109 | power outage heat | `outage-heat` | plain topic | brief topic list, autocomplete | 10 / 183,754 | 15 / 2,918,128 | 17 / 520,565 | 17 / 117,623 | 3/19 | 20/20 | 19/20 |
| 110 | furnace not working after power outage | `outage-heat` | problem symptom | autocomplete | 10 / 460,112 | 16 / 1,624,176 | 15 / 14,203 | 15 / 556 | 2/19 | 19/20 | 16/16 |
| 111 | heat without power | `outage-heat` | cheap hack | brief topic list, autocomplete | 15 / 214,964 | 17 / 2,937,427 | 20 / 1,185,484 | 17 / 117,623 | 3/19 | 20/20 | 19/20 |
| 112 | stay warm without power | `outage-heat` | cheap hack | brief topic list, autocomplete | 19 / 80,158 | 18 / 2,470,302 | 20 / 507,749 | 18 / 45,854 | 2/19 | 20/20 | 19/20 |
| 113 | keep your family warm during a power outage | `outage-heat` | how-to | known title, autocomplete | 17 / 67,761 | 18 / 817,648 | 15 / 286,874 | 18 / 10,906 | 2/19 | 17/20 | 19/20 |
| 114 | ac capacitor | `parts` | plain topic | brief topic list, autocomplete | 10 / 280,009 | 17 / 1,369,012 | 16 / 248,144 | 14 / 14,157 | 1/19 | 20/20 | 20/20 |
| 115 | contactor | `parts` | plain topic | brief topic list, autocomplete | 10 / 130,220 | 11 / 1,175,813 | 11 / 21,501 | 10 / 7,166 | 4/19 | 20/20 | 20/20 |
| 116 | furnace flame sensor | `parts` | plain topic | brief topic list, autocomplete | 8 / 97,202 | 14 / 1,377,959 | 13 / 10,653 | 13 / 203 | 2/19 | 20/20 | 20/20 |
| 117 | furnace igniter | `parts` | plain topic | brief topic list | 10 / 78,606 | 14 / 1,161,105 | 12 / 2,473 | 4 / 234 | 2/19 | 20/20 | 12/13 |
| 118 | ac recharge | `refrigerant` | plain topic | brief topic list | 13 / 1,028,667 | 13 / 2,596,983 | 15 / 220,122 | 12 / 567 | 0/19 | 20/20 | 19/20 |
| 119 | freon | `refrigerant` | plain topic | brief topic list, autocomplete | 11 / 130,580 | 12 / 2,318,268 | 12 / 21,596 | 6 / 1,703 | 1/19 | 20/20 | 16/20 |
| 120 | ac losing freon | `refrigerant` | problem symptom | autocomplete | 13 / 266,813 | 14 / 1,388,734 | 13 / 4,979 | 3 / 199 | 1/19 | 20/20 | 8/8 |
| 121 | hvac replacement cost | `replacement-cost` | cost | brief topic list, autocomplete | 10 / 14,811 | 19 / 1,355,028 | 15 / 575,464 | 14 / 1,816 | 2/19 | 17/20 | 17/20 |
| 122 | mini split cost installed | `replacement-cost` | cost | autocomplete | 8 / 168,385 | 20 / 1,974,778 | 20 / 110,418 | 8 / 398 | 3/19 | 20/20 | 15/16 |
| 123 | new ac cost | `replacement-cost` | cost | brief topic list | 12 / 243,268 | 14 / 1,396,458 | 15 / 670,769 | 11 / 50,801 | 4/19 | 20/20 | 18/20 |
| 124 | new furnace cost | `replacement-cost` | cost | brief topic list, autocomplete | 9 / 59 | 19 / 544,755 | 15 / 64,648 | 17 / 627 | 2/19 | 20/20 | 18/20 |
| 125 | beating the hvac industry | `scams-upsells` | they don't want you to know | known title | 16 / 2,811 | 9 / 646 | 6 / 684 | 1 / 88 | 0/9 | 7/7 | 1/1 |
| 126 | duct cleaning scams | `scams-upsells` | they don't want you to know | autocomplete | 11 / 247,312 | 13 / 646,933 | 10 / 662 | 1 / 261 | 1/19 | 17/20 | 2/2 |
| 127 | hvac companies don't want you to know | `scams-upsells` | they don't want you to know | known title | 18 / 16,341 | 20 / 703,946 | 20 / 83,746 | 12 / 246 | 2/19 | 20/20 | 13/15 |
| 128 | hvac companies hate | `scams-upsells` | they don't want you to know | known title | 16 / 46,966 | 18 / 87,952 | 19 / 333 | 1 / 54,982 | 1/19 | 19/19 | 1/1 |
| 129 | hvac scam | `scams-upsells` | they don't want you to know | brief topic list, autocomplete | 12 / 194,722 | 15 / 2,292,088 | 19 / 395,370 | 18 / 292 | 0/19 | 20/20 | 20/20 |
| 130 | hvac scam caught on camera | `scams-upsells` | they don't want you to know | autocomplete | 10 / 329,946 | 12 / 329,946 | 1 / 84 | 1 / 84 | 0/19 | 1/1 | 1/1 |
| 131 | hvac upsell | `scams-upsells` | they don't want you to know | brief topic list | 13 / 26 | 12 / 1,437 | 12 / 30 | 1 / 4,574 | 3/19 | 20/20 | 1/1 |
| 132 | ac short cycling | `short-cycling` | problem symptom | brief topic list, autocomplete | 10 / 48,795 | 13 / 436,023 | 15 / 3,636 | 4 / 360 | 2/19 | 20/20 | 7/11 |
| 133 | furnace short cycling | `short-cycling` | problem symptom | brief topic list, autocomplete | 9 / 48,054 | 13 / 439,699 | 10 / 2,806 | 14 / 70 | 0/19 | 20/20 | 20/20 |
| 134 | short cycling | `short-cycling` | problem symptom | brief topic list, autocomplete | 13 / 96,761 | 15 / 1,656,060 | 17 / 120,234 | 12 / 2,231 | 5/19 | 20/20 | 17/20 |
| 135 | burning smell furnace | `smells` | problem symptom | brief topic list | 9 / 28,883 | 14 / 303,240 | 11 / 735 | 8 / 177 | 0/19 | 20/20 | 13/15 |
| 136 | furnace smell | `smells` | problem symptom | brief topic list, autocomplete | 5 / 28,883 | 16 / 2,218,758 | 12 / 17,912 | 9 / 269 | 4/19 | 20/20 | 15/20 |
| 137 | space heater | `space-heater` | plain topic | brief topic list, autocomplete | 20 / 1,636,782 | 17 / 5,244,071 | 15 / 405,114 | 17 / 106,887 | 3/19 | 17/20 | 18/20 |
| 138 | space heater vs central heat | `space-heater` | X vs Y | brief topic list, autocomplete | 9 / 19,092 | 14 / 1,111,226 | 13 / 44,169 | 16 / 234 | 1/19 | 20/20 | 19/20 |
| 139 | space heater save money | `space-heater` | cheap hack | autocomplete | 11 / 1,063 | 17 / 1,006,781 | 17 / 51,584 | 16 / 1,044 | 1/19 | 20/20 | 18/20 |
| 140 | turning your heat down | `thermostat` | plain topic | known title | 12 / 1,140 | 14 / 729,746 | 16 / 841 | 18 / 192 | 2/19 | 20/20 | 20/20 |
| 141 | thermostat habits | `thermostat` | mistakes | known title | 19 / 257 | 12 / 16,050 | 14 / 2,212 | 17 / 238 | 5/19 | 20/20 | 19/20 |
| 142 | nest thermostat vs ecobee | `thermostat` | X vs Y | autocomplete | 17 / 11,624 | 17 / 351,029 | 19 / 11,355 | 6 / 360 | 2/19 | 20/20 | 9/9 |
| 143 | smart thermostat save money | `thermostat` | cheap hack | autocomplete | 12 / 65,112 | 13 / 346,205 | 9 / 17,562 | 11 / 28 | 5/19 | 20/20 | 20/20 |
| 144 | thermostat save money | `thermostat` | cheap hack | autocomplete | 7 / 98,899 | 15 / 412,706 | 13 / 16,683 | 11 / 795 | 5/19 | 20/20 | 17/20 |
| 145 | what temperature should you set your thermostat | `thermostat` | myth | autocomplete | 5 / 129,066 | 14 / 1,431,712 | 19 / 83,219 | 12 / 747 | 3/19 | 20/20 | 20/20 |
| 146 | thermal curtains | `windows` | plain topic | brief topic list, autocomplete | 9 / 2,098 | 11 / 243,350 | 15 / 11,609 | 10 / 200 | 2/19 | 20/20 | 19/20 |
| 147 | window film | `windows` | plain topic | brief topic list, autocomplete | 14 / 320,819 | 18 / 2,904,373 | 18 / 228,234 | 17 / 207,838 | 5/19 | 20/20 | 18/20 |
| 148 | pellet stove | `wood-stove` | plain topic | brief topic list, autocomplete | 18 / 53,316 | 15 / 2,045,141 | 14 / 133,472 | 9 / 91,981 | 4/19 | 20/20 | 17/20 |
| 149 | wood stove | `wood-stove` | plain topic | brief topic list, autocomplete | 15 / 139,162 | 18 / 21,790,972 | 19 / 2,140,814 | 18 / 415,634 | 1/18 | 20/20 | 19/20 |
| 150 | wood stove mistakes | `wood-stove` | mistakes | autocomplete | 18 / 57,048 | 17 / 1,368,087 | 18 / 151,760 | 18 / 15,700 | 3/19 | 20/20 | 20/20 |

### Top video per keyword and sort (PRIORITY)

The most-viewed kept long-form English result of each search.

| Keyword | Sort | Top video (title, channel, views, ID) |
|---|---|---|
| adding air conditioning to old house | relevance | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| adding air conditioning to old house | views | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| adding air conditioning to old house | year | "How to Run Electrical Power to a Shed \| Ask This Old House" (This Old House, 535,862, `AWG-gQh1WFQ`) |
| adding air conditioning to old house | month | "Our Wood Stove Can't Heat This House..." (EXPEDITION ROVE, 366,267, `N4aWxk8_yCs`) |
| air conditioner | relevance | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,616,745, `OE9bF80KQGk`) |
| air conditioner | views | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,616,745, `OE9bF80KQGk`) |
| air conditioner | year | "Funny Kids Adventures with Magic Air Conditioner" (Vlad and Niki, 23,456,370, `BbhASJOsWms`) |
| air conditioner | month | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,680, `1H20xp8Brnc`) |
| ac not cooling | relevance | "Window Air Conditioner Not Cooling And The Most Common Fix" (Word of Advice TV, 2,308,345, `an1yClPV4i4`) |
| ac not cooling | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| ac not cooling | year | "Portable Mini Viral AC Review Hindi \| Scam or Useful?" (Tanu Superstar, 1,382,648, `M3MC5bb13UU`) |
| ac not cooling | month | "AC Ain't Working, And It Is 98° Inside!" (HVAC GUY, 24,966, `_wWZbr3O2gk`) |
| central air conditioning not cooling | relevance | "#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" (Silver Cymbal, 4,307,745, `_b6p0fkWhCY`) |
| central air conditioning not cooling | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| central air conditioning not cooling | year | "Genius AC Upgrade That Makes Air Colder And Bills Lower!" (How To Home, 1,769,523, `gQjotD-B0OU`) |
| central air conditioning not cooling | month | "Builders Grade Rheem Central AC Freezing Up in October! MUST FIX NOW!" (Mikey Pipes - Pipe Doctor Plumbing & Heating & Air, 4,763, `hg-_6ZyXuLs`) |
| unclog ac drain line | relevance | "How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling? or in the Pan" (Silver Cymbal, 3,772,429, `qAxJb0J1HH0`) |
| unclog ac drain line | views | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| unclog ac drain line | year | "11 Things HVAC Technicians Don't Want You to Know About Hydrogen Peroxide! (#8 Saves $900)" (TheCheapFix and John Brown, 1,093,030, `yIh1HAlbhc0`) |
| unclog ac drain line | month | "Insane MASSIVE Flooded Unclogging \| Watch The Water Release Instantly!" (Unclogging culvert KH, 3,269, `oX0EyT1Kchs`) |
| why is my ac blowing hot air | relevance | "How To Fix Car AC That Blows Hot - Possible Causes" (proclaimliberty2000, 2,143,805, `Bw0RmMHWRTU`) |
| why is my ac blowing hot air | views | "How to Recharge Your Car's AC System (Fast and Easy)" (ChrisFix, 10,771,363, `SHg2xRMnM38`) |
| why is my ac blowing hot air | year | "This SECRET Will Make Your Car's AC Blow Twice as Cold" (All Car Talk, 1,017,667, `Uz9YxPmkvjc`) |
| why is my ac blowing hot air | month | "Why is the A/C blowing hot air?" (My HVAC Life, 3,933, `FkbAbPPCN0o`) |
| ac mistakes | relevance | "IV ACCESS: 3 TOP MISTAKES" (NYSORA - Education, 1,713,117, `CGaMWDI6Vxk`) |
| ac mistakes | views | "7 FATAL Wiring Mistakes Most DIYers Don't Know They Are Making \| Most Are Guilty of 3" (How To Home, 12,128,990, `-jeP1d8PC1I`) |
| ac mistakes | year | "The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,495, `K2jCz3D5z_0`) |
| ac mistakes | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,202,980, `mP0IjyvQtxw`) |
| secret ac trick | relevance | "Assassin's Creed Odyssey: 14 Tips & Tricks The Game Doesn't Tell You" (WhatCulture Gaming, 865,248, `R9G18ICtSSM`) |
| secret ac trick | views | "30+ HIDDEN Features, Functions & Tricks on EVERY BMW! MUST SEE If You Own a BMW" (BeamerView, 4,533,736, `rjXge8rRPGE`) |
| secret ac trick | year | "Vivo y11 Tips And Tricks \| Top 20++ Hidden Features 🔥 vivo y11" (Techno Helper Hindi, 1,848,448, `lWOeACavBNo`) |
| secret ac trick | month | "Moto Edge 60 Fusion Android 17 Update Hidden All Features Explained \| Hello UI Big Update 🔥🔥🔥" (Magical Tech Guru, 168,163, `JY2MOE9lYyc`) |
| save money on ac | relevance | "Can This Device Actually Lower Your Electric Bill By 30%??" (The DIY HVAC Guy, 2,680,305, `SWc0StyZiJs`) |
| save money on ac | views | "This Mean Girl Shames Friend For Shopping At Thrift Store \| Dhar Mann" (Dhar Mann Studios, 23,662,146, `VwGC3OEUxmw`) |
| save money on ac | year | "Genius AC Upgrade That Makes Air Colder And Bills Lower!" (How To Home, 1,769,523, `gQjotD-B0OU`) |
| save money on ac | month | "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" (Ray Dutton's Garage, 200,886, `H0MBgMMzmyg`) |
| ac freezing up | relevance | "8 Reasons Why Your AC is Freezing Up" (Word of Advice TV, 2,034,672, `stZs8Co80vk`) |
| ac freezing up | views | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| ac freezing up | year | "Turn Any Fan Into an Air Conditioner with 2 Ice Bottles ($0 DIY AC)" (Why Am I Green, 3,707,997, `H514-w6ttNo`) |
| ac freezing up | month | "How to Run AC in Freezing Temps: Carrier MotorMaster Installation" (HVACR Survival, 15,439, `e_HabhQ6HXI`) |
| frozen evaporator coil | relevance | "8 Reasons Why Your AC is Freezing Up" (Word of Advice TV, 2,034,672, `stZs8Co80vk`) |
| frozen evaporator coil | views | "How To Properly Clean An AC Evaporator Coil & Save HUNDREDS!" (The DIY HVAC Guy, 2,280,659, `kJNwqa7YXF0`) |
| frozen evaporator coil | year | "Permanently Fix A Samsung Refrigerator That Is Icing Up!" (DuctTape Mechanic, 85,257, `7NtIFdfC9fk`) |
| frozen evaporator coil | month | "Frozen Dairy CoolerEvap: EPR Valve Bleeding Through During Defrost" (Hillbilly Refrigeration , 1,874, `XEmMJrR6bMo`) |
| why is my ac freezing up | relevance | "8 Reasons Why Your AC is Freezing Up" (Word of Advice TV, 2,034,673, `stZs8Co80vk`) |
| why is my ac freezing up | views | "Clean Window AC the LAZY (but still effective) way!" (Handyman Hertz, 3,178,486, `nVLRm_S0zto`) |
| why is my ac freezing up | year | "1 Year with OutEquip 12V AC: Still Freezing in a 24-Hour 100°F Desert Test" (The Cummins Camper, 148,074, `xpw1ThzuJ04`) |
| why is my ac freezing up | month | "Why is my AC freezing up, EVEN when its hot outside?" (BEHIND THE GAUGES, 53, `B1U-VIoR_qA`) |
| window air conditioner | relevance | "The COLDEST And QUIETEST AC Unit Ever Made!  Still Use Your Window!" (How To Home, 2,007,929, `_Qa5teuVPRg`) |
| window air conditioner | views | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,616,745, `OE9bF80KQGk`) |
| window air conditioner | year | "Coldest and Quietest Air Conditioner Ever Tested!" (Project Farm, 1,100,009, `BSTkKiJPeaQ`) |
| window air conditioner | month | "Voltas new Latest Window AC installation in Supaul \|\| Ehsan Shaikh " (Ehsan Shaikh , 318,633, `6J1PgvNY0k0`) |
| window ac not cooling | relevance | "Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" (Silver Cymbal, 2,363,767, `o8KQu_MlpoY`) |
| window ac not cooling | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| window ac not cooling | year | "Portable Mini Viral AC Review Hindi \| Scam or Useful?" (Tanu Superstar, 1,382,648, `M3MC5bb13UU`) |
| window ac not cooling | month | "Kenmore (WCI) 25371055005 5,600 BTU Window Air Conditioner \| Initial Checkout" (Jordan U, 831, `AwOWHJTF9tg`) |
| window ac vs portable ac | relevance | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| window ac vs portable ac | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| window ac vs portable ac | year | "Portable Mini Viral AC Review Hindi \| Scam or Useful?" (Tanu Superstar, 1,382,659, `M3MC5bb13UU`) |
| window ac vs portable ac | month | "Mitsubishi Heavy Duty 2.25 Ton Hyper Inverter AC DXK27YAMDA \| Best AC for Big Halls \| Full Review" (DECENT ZONE, 2,603, `HN_1snNi4UE`) |
| best portable air conditioner | relevance | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| best portable air conditioner | views | "$649 Dyson Fan vs. $15 Walmart Fan: The Hard Truth" (Mark Spurrell, 12,715,289, `dS0oFmzU06g`) |
| best portable air conditioner | year | "Breeza Max Exposed: Inside The Viral Portable A/C Scam #BreezaMaxScam #PortableAC #PolarBreeze" (JDub Adventures, 2,619,488, `JZ4vlMZlCj8`) |
| best portable air conditioner | month | "Cheapest Electronics & Home Appliances Diwali bonaza Sale, Ac Led Tv Home Decor Fridge Crockery Gift" (Journey of Jaiswal, 144,357, `CK0vwjoPTDg`) |
| attic fan | relevance | "Attic Fan Installation - Make your House Cooler for Cheap!" (Every other Karl, 469,754, `l2GZNi1kF5g`) |
| attic fan | views | "There's Something LIVING in our Attic" (The Royalty Family, 25,008,610, `NLPkz9TJNP8`) |
| attic fan | year | "Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,674, `SVuQqEXaWdw`) |
| attic fan | month | "Whirlybird Roof Vents Explained: How They Work and Why They’re Disappearing" (Small Things, 27,354, `5Zh3E-ruOHg`) |
| cool your attic | relevance | "Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,674, `SVuQqEXaWdw`) |
| cool your attic | views | "Valuable Things You Might Have In Your Attic" (BE AMAZED, 5,361,289, `jhFl5aHx0Qw`) |
| cool your attic | year | "Why Did We Stop Using This Natural Cooling System?" (Wild Line, 2,129,674, `SVuQqEXaWdw`) |
| cool your attic | month | "This $22 Copper Coil Drops Any Attic 30°F. HVAC Companies Are Furious." (Paddy's Old School Fixes, 1,014, `ACuLhY1RcYs`) |
| whole house fan | relevance | "THIS Is Why Your AC Bill Is So High! Whole House Fan Solution" (Home RenoVision DIY, 815,789, `8pArX4ww0ZI`) |
| whole house fan | views | "I Turned My House Into a Trampoline Park!" (Unspeakable, 79,772,408, `lSSWH4NOdgE`) |
| whole house fan | year | "This $4 "DRY BUILD" Dehumidifies Your Whole Home WITHOUT USING ELECTRICITY" (Zen Garden Oasis, 1,667,217, `KphunxyIbKM`) |
| whole house fan | month | "🔴No Need For Stool & Hands, Clean your Fan Easily In Minutes 😱\| Bathroom tiles cleaning tips" (Tips and Tricks with Hina, 329,049, `V5xmCgvx5rE`) |
| boiler | relevance | "Limp Bizkit - Boiler (Official Music Video)" (limpbizkit, 93,572,265, `qex0OjXolzc`) |
| boiler | views | "Limp Bizkit - Boiler (Official Music Video)" (limpbizkit, 93,572,265, `qex0OjXolzc`) |
| boiler | year | "1st January \|\| পয়লা জানুয়ারি \|\| Bengali Best Funny Video 2025 \|\| Baccha Party School " (Baccha Party School , 30,314,679, `3QYVojJAz6w`) |
| boiler | month | "LIVE : తిరుపతిలో భారీ పేలుడు \| Tirupati Sricity Boiler Blast : Injured in Massive Explosion \|UTVNews" (Its UTV News, 723,726, `IJ9fJhOUuNE`) |
| old house boiler | relevance | "How to Install a Combination Boiler/Water Heater \| Ask This Old House" (This Old House, 865,991, `BuxvKbIIYLU`) |
| old house boiler | views | "Solomun \| Boiler Room: Tulum" (Boiler Room, 77,228,420, `bk6Xst6euQk`) |
| old house boiler | year | "FREE Heating With Used Motor Oil? I Built This Waste Oil Heater" (Snowstead, 1,137,983, `nvgRcY40xX4`) |
| old house boiler | month | "Gulli Bulli Old House Sale Full Story \|\| GULLI BULLI CARTOON \|\| MAKE JOKE HORROR" (Make Joke Bazigar, 312,887, `RiC70Z8hin4`) |
| steam heat | relevance | "Steam Heating System Basics" (MEP Academy, 117,642, `0OgbvugIRWA`) |
| steam heat | views | "How a Steam Locomotive Works (Union Pacific "Big Boy")" (Animagraffs, 10,341,179, `Hszu80NJ438`) |
| steam heat | year | "How the Super Soaker Inventor Just Killed the Steam Engine" (Undecided with Matt Ferrell, 597,166, `MuQRxatte5g`) |
| steam heat | month | "This Machine Turns Waste Heat Into Electricity \| China’s Supercritical CO₂ Breakthrough" (Science Explorer, 60,983, `c16DYRAj6Wc`) |
| steam radiator | relevance | "Thermostatic Radiator Valves (TRV'S) How They Work" (PlumbingGuy , 133,589, `_d5-OzlOah0`) |
| steam radiator | views | "Overheating After Replacing Radiator, Pump, Thermostat? Burp Coolant to Remove Air Pockets!" (1A Auto: Repair Tips & Secrets Only Mechanics Know, 2,182,417, `VvkAvt8_fMc`) |
| steam radiator | year | "Cast-iron Radiator Gaming PC" (Billet Labs, 373,215, `xxtZ9DnQJVk`) |
| steam radiator | month | "50-Year-Old Leaking Steam Radiator Valves REPLACED Before Heat Turns ON!" (Mikey Pipes - Pipe Doctor Plumbing & Heating & Air, 13,791, `zAHTpkI2qr4`) |
| boiler no heat | relevance | "How to Fix One Radiator Not Working - Plumbing Tips" (plumberparts, 2,479,340, `wqku_Rc_YuI`) |
| boiler no heat | views | "UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,263, `7LV5wY-iM34`) |
| boiler no heat | year | "DIY Waste Oil Burner No Fan! Homemade Free Heat!" (Country Living Experience: A Homesteading Journey, 381,079, `pFGSAkditqk`) |
| boiler no heat | month | "This $35 ALUMINUM MESH Blows 140°F Heat Into Your House (No Gas NEEDED)" (Caleb Greer — Off-Grid Water & Power, 353,463, `fOW5Cv5cBoM`) |
| steam radiator not getting hot | relevance | "How to Fix One Radiator Not Working - Plumbing Tips" (plumberparts, 2,479,340, `wqku_Rc_YuI`) |
| steam radiator not getting hot | views | "How to Fix One Radiator Not Working - Plumbing Tips" (plumberparts, 2,479,340, `wqku_Rc_YuI`) |
| steam radiator not getting hot | year | "Here’s Why Your Radiator Hose Hot on Top Cold on Bottom" (OBD Insights, 24,955, `atUJMoSXSn0`) |
| steam radiator not getting hot | month | "How To Bleed An Old Radiator - Don't try it until you watch this" (The Old House Fix, 875, `r9Zf1X5cOoQ`) |
| boiler vs furnace | relevance | "Heat Pump vs Gas Furnace - Which is the Best Choice For You?" (HVACDirect, 248,405, `wbY3n5ofevU`) |
| boiler vs furnace | views | "The Future Of Firewood Furnaces Is Here!" (Neil Koch: Dig-Drive-DIY, 1,000,226, `GncndyCnNPA`) |
| boiler vs furnace | year | "Emergency Oil to Gas Conversion \| US Boiler Burnham Alta Tankless Combi Install on Long Island" (Mikey Pipes - Pipe Doctor Plumbing & Heating & Air, 14,003, `BtCZZUZlDjA`) |
| boiler vs furnace | month | not found |
| bleeding radiators old house | relevance | "How To Bleed A Radiator - Don’t try it until you watch this" (Allen Hart, 2,404,182, `tbLz8icLr2U`) |
| bleeding radiators old house | views | "How To Bleed A Radiator - Don’t try it until you watch this" (Allen Hart, 2,404,182, `tbLz8icLr2U`) |
| bleeding radiators old house | year | "How To Bleed An Old Radiator - Don't try it until you watch this" (The Old House Fix, 875, `r9Zf1X5cOoQ`) |
| bleeding radiators old house | month | "How To Bleed An Old Radiator - Don't try it until you watch this" (The Old House Fix, 875, `r9Zf1X5cOoQ`) |
| best ac brands | relevance | "Top 10 Best Air Conditioner Brands in the World" (Top 10 List, 1,635,826, `kgtkUkHRoBw`) |
| best ac brands | views | "A/C Buying Guide \| Inverter AC vs Non Inverter AC, Window AC vs Split AC, What is Ton & Star Rating?" (SidTalk, 10,772,005, `QNM9ASapu58`) |
| best ac brands | year | "Panasonic AC 1.5 Ton 5 Star \| Best 1.5 Ton 5 Star AC \| Best AC 2026" (Vineet Malhotra, 3,243,403, `a93CLRfZSj4`) |
| best ac brands | month | "Big Billion Days Deals \| Best AC 2026 \| Great Indian Festival Sale" (Vineet Malhotra, 109,944, `yjCMRvjUMmg`) |
| best furnace brands | relevance | "Don't Buy a High Efficiency Furnace!" (Word of Advice TV, 383,347, `7d783qs3laA`) |
| best furnace brands | views | "Best Furnace Filter Brand? 3M Filtrete vs HoneyWell BestAir, Nordic Pure, Flanders EZ Flow" (Project Farm, 2,573,534, `RkjRKIRva58`) |
| best furnace brands | year | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,769, `86S3ITbfzQY`) |
| best furnace brands | month | "Ranking the Best and Worst HVAC Brands (2026 Update)" (Yarbrough & Sons Heating, Cooling & Plumbing, 13,687, `Kdk-nTX4FZg`) |
| best heat pump brands | relevance | "The Genius of the World's Most Efficient Heat Pump" (Ziroth, 807,776, `BZzrZ0UxoEY`) |
| best heat pump brands | views | "How My Geothermal Heat Pump Really Performed (2 Years)" (Undecided with Matt Ferrell, 1,350,432, `DTb7TKJzr5g`) |
| best heat pump brands | year | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,769, `86S3ITbfzQY`) |
| best heat pump brands | month | "THE 10 BEST DRYERS DEFINITELY WORTH BUYING" (Alperen Kılınç, 13,255, `5dTPxIbtgsg`) |
| best hvac brands | relevance | "STOP Buying This HVAC Brand" (The DIY HVAC Guy, 1,295,595, `x2BK-zr4raE`) |
| best hvac brands | views | "Top 5 Things AC Companies Don't Want You To Know How To Do!" (How To Home, 2,979,991, `AQQH9QwC46A`) |
| best hvac brands | year | "Best AC Under 30000 \| Best AC 2026 \| AC Buying Guide 2026" (Vineet Malhotra, 904,809, `Ax_ivx5AOGw`) |
| best hvac brands | month | "Different Types of AC Systems Explained! உங்கள் வீட்டிற்கு எந்த AC Best?" (Ansari Architects, 50,037, `8VvwtgdYakI`) |
| hvac brands to avoid | relevance | "STOP Buying the WRONG Air Conditioner Brands" (Atlas AC, 1,873,918, `r_uP9itJ0HQ`) |
| hvac brands to avoid | views | "STOP Buying the WRONG Air Conditioner Brands" (Atlas AC, 1,873,918, `r_uP9itJ0HQ`) |
| hvac brands to avoid | year | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,769, `86S3ITbfzQY`) |
| hvac brands to avoid | month | "9 HVAC Secrets Most Homeowners Don't Know" (The Smart Fix, 42, `CBGFbel8XnU`) |
| only hvac brands worth buying | relevance | "DIY Mini Split Install: 3 Regrets After 1 Year of Use" (LRN2DIY, 2,387,613, `5dCCntGj1wM`) |
| only hvac brands worth buying | views | "STOP Buying This HVAC Brand" (The DIY HVAC Guy, 1,295,595, `x2BK-zr4raE`) |
| only hvac brands worth buying | year | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,769, `86S3ITbfzQY`) |
| only hvac brands worth buying | month | "The Only 6 Brands Worth Buying In 2026" (Jordan Dearden, 3,019, `rF2UxwEcVS4`) |
| ceiling fan direction | relevance | "Your Ceiling Fan Has Two Directions… But Why?" (History of Simple Things, 19,666, `vUd0r3fi7rE`) |
| ceiling fan direction | views | "Best fan placement to move air through the house" (Matthias random stuff, 11,467,376, `1L2ef1CP-yw`) |
| ceiling fan direction | year | "Your Fan is NOT Cooling Your Room (Do This Instead)" (Archi notes, 136,081, `IL31s5MrIUQ`) |
| ceiling fan direction | month | "Your Ceiling Fan Has Two Directions… But Why?" (History of Simple Things, 19,666, `vUd0r3fi7rE`) |
| ceiling fan winter | relevance | "Hunter 59033 Westover Ceiling Fan With Heater" (In_The_Woods, 25,212, `uQBZG-woMDM`) |
| ceiling fan winter | views | "► Box Fan (High Speed) and Rain Sounds for Sleeping with Distant Thunder, 10 hours Fan White Noise" (SleepDroid Studios Sleep Sounds, 10,143,736, `as7kf-LTVaE`) |
| ceiling fan winter | year | "Homemade products ceiling fan for summer air conditioner with winter mode" (Toy invention, 304,239, `JT6vRjCIO7E`) |
| ceiling fan winter | month | "Your Ceiling Fan Has Two Directions… But Why?" (History of Simple Things, 19,666, `vUd0r3fi7rE`) |
| central air conditioner condenser cleaning | relevance | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| central air conditioner condenser cleaning | views | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| central air conditioner condenser cleaning | year | "How to Unclog or Clean your AC Condensate Drain Line" (Home DIY with Martin, 359,225, `37LrIgMDDTk`) |
| central air conditioner condenser cleaning | month | "Before You Shut Down Your AC This Fall, DO THIS (Or Pay for It Next Spring)" (Home Metric, 55, `tbOLfUJ2XYA`) |
| cleaning ac unit with pressure washer | relevance | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| cleaning ac unit with pressure washer | views | "Learn SPLIT AC Servicing at Home full process \|\| Learn SPLIT AC Cleaning at home full process \|\|" (emm vlogs, 6,134,962, `XrMS3v4jZyM`) |
| cleaning ac unit with pressure washer | year | "Air Cooler Pad Cleaning / Honeycomb Pad cleaning / How to Clean Air Cooler Honeycomb Pad Urdu/Hindi" (Tech Knowledge, 341,278, `Ig6vee-64nI`) |
| cleaning ac unit with pressure washer | month | "Your AC Coils Could Be FILTHY... Here’s How to Clean Them Properly" (Carl The Janitor, 479, `BI-QB9KdUB0`) |
| how to clean ac unit | relevance | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| how to clean ac unit | views | "How to Properly Recharge Your AC System" (ChrisFix, 12,893,673, `Pdq8JAlct6s`) |
| how to clean ac unit | year | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,902, `dOZ-8__G4uU`) |
| how to clean ac unit | month | "Before You Shut Down Your AC This Fall, Do THIS!" (Fix This House, 14,779, `6J5IUqH2Cx8`) |
| draft stopper | relevance | "TOP 5 Best Door Draft Stopper [ Buyer's Guide ]" (Techs You Can't Live Without, 12,061, `Z3hMVHVKJu8`) |
| draft stopper | views | "How To Make Double Door Draft Stopper / Weatherstripping Under Door Step by Step  -  ENERGY SAVINGS" (Estadistica Datos del Mundo, 3,665,737, `y5jlkhKRkII`) |
| draft stopper | year | "592🎀Floral door draft stopper" (Cosa fa la Beche? , 10,625, `ePbI9P32uxY`) |
| draft stopper | month | "592🎀Floral door draft stopper" (Cosa fa la Beche? , 10,625, `ePbI9P32uxY`) |
| drafty house | relevance | "WW3 Draft Mix - Rock x House MOONLGHT Mix Vol. 1" (MOONLGHT, 3,289,490, `GvfwUfbs82w`) |
| drafty house | views | "15 Cheap Ways to Fix Cold Rooms" (Fix This Build That, 939,136, `zKQi5vavSpw`) |
| drafty house | year | "How to Seal a Drafty Exterior Door (Garage → House Entry) \| Easy DIY Weatherproofing" (The Fixer, 115,984, `VPgZIWgKOd8`) |
| drafty house | month | "SIDEMEN FIGHT TO BUILD THE BEST $20 DRAFT" (SidemenReacts, 2,160,949, `B9BrzofcYd8`) |
| weatherstripping | relevance | "How To Replace Weatherstripping On Your Vehicle (Andy’s Garage: Episode - 395)" (Phillips Vision, 581,361, `EE2X0_JjlvQ`) |
| weatherstripping | views | "How To Make Double Door Draft Stopper / Weatherstripping Under Door Step by Step  -  ENERGY SAVINGS" (Estadistica Datos del Mundo, 3,665,742, `y5jlkhKRkII`) |
| weatherstripping | year | "Garage Companies HATE This Weather Seal Hack!" (Is It Worth It, 512,248, `qv7igI8QOws`) |
| weatherstripping | month | "How to Reduce Wind Noise in a Toyota RAV4 \| Weather Stripping" (2doordude, 25,257, `uXEyNPykYPA`) |
| closing vents | relevance | "Turning Off The Vents In Empty Rooms Is NOT Saving You Money. Do This Instead" (Gus Whitaker, 6,312, `rIIHadwEegE`) |
| closing vents | views | "Don't CLOSE Your Vents!" (LRN2DIY, 910,745, `yL_cVCGwZCk`) |
| closing vents | year | "This $0 Fix Cools Your Attic by 55°F. Why Don't Roofers Tell You?" (Candlelight Archives, 593,892, `7iKXXv4bHvU`) |
| closing vents | month | "Turning Off The Vents In Empty Rooms Is NOT Saving You Money. Do This Instead" (Gus Whitaker, 6,312, `rIIHadwEegE`) |
| is ac duct cleaning worth it | relevance | "Air Duct Cleaning Scam Exposed!" (Pleasant Green, 3,414,993, `J_FMXc7F_bM`) |
| is ac duct cleaning worth it | views | "Air Duct Cleaning Scam Exposed!" (Pleasant Green, 3,414,993, `J_FMXc7F_bM`) |
| is ac duct cleaning worth it | year | "Car AC Vent, Duct & Cooling Coil Cleaner Review \| Before & After \| Cooling Test \| kangaroo, 3m Foam" (Lazy Detailer’s Choice, 139,187, `RLO3x3lNeBQ`) |
| is ac duct cleaning worth it | month | "What Makes a Local Air Duct Cleaning Company Worth Choosing? \| Land O’ Lakes" (Bright Air Duct Cleaning - Florida, 5, `jHLCB0sAuOk`) |
| duct cleaning | relevance | "Air Duct Cleaning Scam Exposed!" (Pleasant Green, 3,414,993, `J_FMXc7F_bM`) |
| duct cleaning | views | "How To Clean Your Dryer Vent Duct - Step By Step - It's Super Simple!" (AmplifyDIY, 3,803,747, `GLZSqhUoF_g`) |
| duct cleaning | year | "How to Clean Your Dryer Vent (The Mexican Way)" (Ramón Delgado and 4 more, 373,064, `CxDyHLLkQi4`) |
| duct cleaning | month | "ASMR✨Tear Eye Duct Cleaning, Intense Lash Scratching, Buccal Massage, Soft Whispers" (Oly Asmr Tv, 36,101, `lisbmE2e3G4`) |
| baseboard heater | relevance | "Installing Electric Baseboard Heater. DIY" (agiftedcurse, 536,424, `CVUQXQWovdc`) |
| baseboard heater | views | "How To Remove Air From Your Heating System" (TheDIYGuyDOTnet, 2,050,577, `z80WspC4Nmg`) |
| baseboard heater | year | "How to Get Spray-Quality Baseboards With a Brush" (The Funny Carpenter, 355,105, `D01GZX1QuoQ`) |
| baseboard heater | month | "How to Install New "Dummy" Baseboard Heat Covers \| Slant-Fin \| The Fixer Clips" (The Fixer 2, 1,645, `l-NcArLVtK8`) |
| electric bill | relevance | "Who Broke Your Power Bill?" (Climate Town, 899,236, `3fDGcZ8qpPM`) |
| electric bill | views | "'JUST THE TWO OF US' (GROVER WASHINGTON JNR - BILL WITHERS) cover by HSCC" (The Hindley Street Country Club, 40,504,078, `dS7kzPGkb3o`) |
| electric bill | year | "Small plug-in solar panels gain traction as an affordable way to cut electricity bills" (PBS NewsHour and KQED, 3,057,508, `yVO9GcNlkLQ`) |
| electric bill | month | "বিদ্যুৎ বিলের আতঙ্ক \| Electricity Bill \| Bangla Funny Video \| Family Entertainment bd \| Bangla Natok" (Family Entertainment Bd, 2,587,290, `zJNosjp9eiw`) |
| heating bill | relevance | "The Heating Bill \| Funny Episodes \| Mr Bean World" (Mr Bean World, 5,670,426, `5luF65i0kLc`) |
| heating bill | views | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,619, `J95l9Ue4224`) |
| heating bill | year | "Genius AC Upgrade That Makes Air Colder And Bills Lower!" (How To Home, 1,769,523, `gQjotD-B0OU`) |
| heating bill | month | "Why I Went Back To 1970s Winter Heating Habits At 52 (And Saved Hundreds)" (Living Like It's 1950, 485,101, `wonMXWuCSIk`) |
| why is my electric bill so high | relevance | "Troubleshooting a High Electric Bill \| Ask This Old House" (This Old House, 352,976, `jjX5B8Txc7E`) |
| why is my electric bill so high | views | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,619, `J95l9Ue4224`) |
| why is my electric bill so high | year | "This One Change Can Reduce Your Electricity Bill by 95%" (Keerthi, 1,159,215, `m8CQNYvjB_Q`) |
| why is my electric bill so high | month | "Smart Meter लगते ही Electricity Bill 4X? - असली Reason क्या है?" (SolarSquare, 229,701, `VBLgbnDBhKA`) |
| why is your heat bill so high | relevance | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,619, `J95l9Ue4224`) |
| why is your heat bill so high | views | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,619, `J95l9Ue4224`) |
| why is your heat bill so high | year | "This $8 Trick Cuts Your Electricity Bill in Half, And Nobody’s Aware Of It!" (WiseMoney, 331,860, `Y0teFh7cVrA`) |
| why is your heat bill so high | month | "THIS Is Why Your Heating Bill Is So High — And the $30 Fix 1950s Houses Knew" (John The HVAC Guy and 9 more, 916, `DXWGLnh2Kpw`) |
| energy bill mistakes | relevance | "5 Energy Bill Mistakes Utility Companies Hope You Keep Making" (Ray Dutton's Garage, 400,942, `wZk06FJWMlM`) |
| energy bill mistakes | views | "10 Common Mistakes DIYers Make In Circuit Breaker Boxes" (LRN2DIY, 3,763,646, `NF4zxBAuRoI`) |
| energy bill mistakes | year | "1 Bed Apartment Pays Crazy Energy Bills!  Let’s Investigate" (Cablesmith Electrical, 997,721, `0CF-EEqdohY`) |
| energy bill mistakes | month | "Is Your Net Metering Bill WRONG? 🚨 MFES CEO Reveals How to Check (Step-by-Step Guide)" (MFES Solar Energy, 4,416, `IDKNcw43GQU`) |
| power company doesn't want you to | relevance | "I Bought a Banned Chinese Car From a Rental Company for $2,000" (Rich Rebuilds, 2,741,910, `Jdm8qnlnzqc`) |
| power company doesn't want you to | views | "What the oil industry doesn’t want you to know - Stephanie Honchell Smith" (TED-Ed, 887,783, `_vDZmVXtA7k`) |
| power company doesn't want you to | year | "AI Whistleblower: We Are Being Gaslit By AI Companies, They’re Hiding The Truth! - Karen Hao" (The Diary Of A CEO, 5,567,669, `Cn8HBj8QAbk`) |
| power company doesn't want you to | month | "Your Power Company Doesn't Want You To See This! Fix These Now!" (How To Home, 135,942, `YlPhqsMeegs`) |
| how to save money on electric bill in winter | relevance | "11 Easy Ways To Reduce Your Energy Bills \| SAVE UP TO 51%!" (Heat Geek, 337,351, `YCCdw3ZFbsg`) |
| how to save money on electric bill in winter | views | "How Amish Heat Their Living Room Without Gas/Electricity" (Frugal Solutions, 2,533,993, `SrC3wms8pQ8`) |
| how to save money on electric bill in winter | year | "11 Ways I Cut My Electric Heat Bill In Half (Not sponsored)" (Over the Hill & Loving It, 203,027, `546lBfX7ugs`) |
| how to save money on electric bill in winter | month | "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" (Ray Dutton's Garage, 201,002, `H0MBgMMzmyg`) |
| lower your electric bill | relevance | "$1,000 Solar Setup vs My Electric Bill" (Footprint Hero with Alex Beale, 1,272,583, `6ERzqzcySUQ`) |
| lower your electric bill | views | "how to lower your electric bill ... Oncor said I was meter tampering Really !" (ranchitout, 9,461,124, `OgKQihUEFA0`) |
| lower your electric bill | year | "Small plug-in solar panels gain traction as an affordable way to cut electricity bills" (PBS NewsHour and KQED, 3,057,508, `yVO9GcNlkLQ`) |
| lower your electric bill | month | "Your Power Company Doesn't Want You To See This! Fix These Now!" (How To Home, 135,942, `YlPhqsMeegs`) |
| swamp cooler | relevance | "Personal "air conditioners" aren't what they seem" (Technology Connections, 3,221,718, `2horH-IeurA`) |
| swamp cooler | views | "Homemade air conditioner DIY - Awesome Air Cooler! - EASY Instructions - can be solar powered!" (desertsun02, 15,266,378, `ITtlxjvLQis`) |
| swamp cooler | year | "Genius AC Upgrade That Makes Air Colder And Bills Lower!" (How To Home, 1,769,523, `gQjotD-B0OU`) |
| swamp cooler | month | "Best Water Purifier 2026 \| Best RO Water Purifier \| Best Water Purifier for Home" (Vineet Malhotra, 438,931, `8MV9zHA6iTM`) |
| air filter | relevance | "Do Performance Air Filters Actually Work?" (Engineering Explained, 6,465,119, `GS69owXpGdY`) |
| air filter | views | "Are Aftermarket Intakes Even Worth It?" (Donut, 9,328,597, `q9ZcPtvTKpY`) |
| air filter | year | "This Air Filter Will Destroy Your Engine!" (Project Farm, 1,839,958, `1PA8AHGJMPQ`) |
| air filter | month | "Best Water Purifier 2026 \| Best RO Water Purifier \| Best Water Purifier for Home" (Vineet Malhotra, 438,931, `8MV9zHA6iTM`) |
| ac filter destroying | relevance | "This Air Filter Will Destroy Your Engine!" (Project Farm, 1,839,958, `1PA8AHGJMPQ`) |
| ac filter destroying | views | "This Air Filter Will Destroy Your Engine!" (Project Farm, 1,839,958, `1PA8AHGJMPQ`) |
| ac filter destroying | year | "This Air Filter Will Destroy Your Engine!" (Project Farm, 1,839,958, `1PA8AHGJMPQ`) |
| ac filter destroying | month | "The $30 Filter Is Destroying Your Furnace (Here's Why)" (Ray Dutton's Garage, 6,493, `MoB-obRdbro`) |
| furnace filter mistakes | relevance | "5 Furnace Filter Mistakes That Will Cost You Money!" (The Funny Carpenter, 2,871,470, `_g8gQ1gg1FM`) |
| furnace filter mistakes | views | "10 Common Mistakes DIYers Make In Circuit Breaker Boxes" (LRN2DIY, 3,763,646, `NF4zxBAuRoI`) |
| furnace filter mistakes | year | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,017, `mP0IjyvQtxw`) |
| furnace filter mistakes | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,017, `mP0IjyvQtxw`) |
| furnace filters cheap vs expensive | relevance | "Best Furnace Filter Brand? 3M Filtrete vs HoneyWell BestAir, Nordic Pure, Flanders EZ Flow" (Project Farm, 2,573,534, `RkjRKIRva58`) |
| furnace filters cheap vs expensive | views | "5 Furnace Filter Mistakes That Will Cost You Money!" (The Funny Carpenter, 2,871,470, `_g8gQ1gg1FM`) |
| furnace filters cheap vs expensive | year | "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" (Ray Dutton's Garage, 767,255, `_ZgVjFpBnQA`) |
| furnace filters cheap vs expensive | month | not found |
| do air filters really work | relevance | "Do Performance Air Filters Actually Work?" (Engineering Explained, 6,465,119, `GS69owXpGdY`) |
| do air filters really work | views | "$649 Dyson Fan vs. $15 Walmart Fan: The Hard Truth" (Mark Spurrell, 12,715,299, `dS0oFmzU06g`) |
| do air filters really work | year | "I Improved MPGs by 22.4%! Don’t Get Scammed and Do What Works!" (Project Farm, 2,620,097, `Tl2FroJMUt8`) |
| do air filters really work | month | "Best Air Purifier 2026 \| Best Air Purifier for Home \| Best Air Purifier under 10000" (Vineet Malhotra, 139,611, `fJpk977NJi4`) |
| how often should you change your air filter | relevance | "Do Performance Air Filters Actually Work?" (Engineering Explained, 6,465,119, `GS69owXpGdY`) |
| how often should you change your air filter | views | "How to Change EVERY FLUID in your Car or Truck (Oil, Transmission, Coolant, Brake, and More)" (ChrisFix, 14,646,599, `t7JCh7PHoDc`) |
| how often should you change your air filter | year | "6 Rules for 300k Miles: A Parts Guy's Maintenance Guide" (Chris from Beachside Auto Parts, 2,382,144, `8Ote9sLF0Jw`) |
| how often should you change your air filter | month | "How Often Should You Change Your AC Filter? \| Ask Andy! HVAC Tips" (Advantage HVAC, Plumbing, and Electrical, 11,057, `7-B7T4Ul_eM`) |
| furnace | relevance | "🔥 Cozy Fireplace 4K (12 HOURS). Fireplace with Crackling Fire Sounds. Fireplace Burning 4K" (FOBOS PLANET, 4,310,550, `CIj-ZDSjZ2E`) |
| furnace | views | "Primitive Technology: Natural Draft Furnace" (Primitive Technology, 24,938,704, `u7wAJTGl2gc`) |
| furnace | year | "Primitive Technology: Grate furnace, wood fired smelting experiment" (Primitive Technology, 2,750,290, `eIBEK-_NMJc`) |
| furnace | month | "Ethiopia: At the Heart of the Furnace - Deadliest Roads" (Deadliest Roads, 2,465,163, `v60PNv_k3BM`) |
| why is my furnace blowing cold air | relevance | "Furnace Not Blowing Hot Air - Easy Fix" (Word of Advice TV, 1,803,626, `pJzP1jzYPqg`) |
| why is my furnace blowing cold air | views | "How to Fix a Car with No Heat (Easy)" (ChrisFix, 9,796,007, `-XjXTVJhFLM`) |
| why is my furnace blowing cold air | year | "This SECRET Will Make Your RV Furnace Blow Twice As Hot" (Bruce RV Guy, 15,525, `yslxL1_31So`) |
| why is my furnace blowing cold air | month | "Heat Pump Blowing Cold Air? What to Check Before You Call (Homeowner + Tech Guide)" (Taddy Digest, 11,630, `sDoIIUgMXH8`) |
| save money on heating | relevance | "How to Save Money on Heating Bills \| Ask This Old House" (This Old House, 527,531, `2-29z0yFDL4`) |
| save money on heating | views | "Dehumidifiers are confusing. Here's why." (Technology Connections, 3,297,613, `j_QfX0SYCE8`) |
| save money on heating | year | "The $4 Amish Fix for a Deadly Hot House (Save $3000 This Summer)" (Elias Yoder, 1,937,922, `H8-QNBd7MIo`) |
| save money on heating | month | "Why I Went Back To 1970s Winter Heating Habits At 52 (And Saved Hundreds)" (Living Like It's 1950, 485,101, `wonMXWuCSIk`) |
| geothermal | relevance | "My DIY Geothermal System Was So CHEAP!!!" (The Challenged One, 3,277,577, `MUWjjjFgXdg`) |
| geothermal | views | "Would you swim in power plant wastewater?" (Tom Scott, 6,918,558, `OgMXjAQ5q14`) |
| geothermal | year | "Why Drilling To The Earth's Mantle Is Almost Impossible \| Pushing Limits" (Business Insider and 2 more, 875,923, `ij61TLsjKD8`) |
| geothermal | month | "Is this how to get lithium without ruining the planet?" (DW Planet A, 283,417, `PmMFRhlKjuI`) |
| heat pump | relevance | "Heat Pumps: the Future of Home Heating" (Technology Connections, 4,844,715, `7J52mDjZzto`) |
| heat pump | views | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| heat pump | year | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,686, `1H20xp8Brnc`) |
| heat pump | month | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,707, `1H20xp8Brnc`) |
| heat pumps leaving people cold | relevance | "Why Heat Pumps are now leaving people COLD" (Silver Cymbal, 632,290, `BP1iDvKpNZA`) |
| heat pumps leaving people cold | views | "Why Heat Pumps are now leaving people COLD" (Silver Cymbal, 632,290, `BP1iDvKpNZA`) |
| heat pumps leaving people cold | year | "Do Heat Pumps Work in a Real Winter?" (Pro Grade Home Science, 37, `AmTI_4Mjd08`) |
| heat pumps leaving people cold | month | "Do Heat Pumps Work in a Real Winter?" (Pro Grade Home Science, 37, `AmTI_4Mjd08`) |
| why is my heat pump blowing cold air | relevance | "10 Reasons Why Your AC Is NOT Blowing Cold Air In Your Home! DIY How To FIX!" (Fix This House, 765,600, `drb2fdVKZlk`) |
| why is my heat pump blowing cold air | views | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| why is my heat pump blowing cold air | year | "How to fix Kia Car A/C Air Conditioner Not Blowing Cold Air" (TampaTec, 40,437, `VV6Aszi_AFk`) |
| why is my heat pump blowing cold air | month | "Heat Pump Blowing Cold Air? What to Check Before You Call (Homeowner + Tech Guide)" (Taddy Digest, 11,630, `sDoIIUgMXH8`) |
| heat pump vs furnace | relevance | "Heat Pumps: the Future of Home Heating" (Technology Connections, 4,844,715, `7J52mDjZzto`) |
| heat pump vs furnace | views | "Space Heater Nonsense" (Technology Connections, 5,386,816, `V-jmSjy2ArM`) |
| heat pump vs furnace | year | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,686, `1H20xp8Brnc`) |
| heat pump vs furnace | month | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,686, `1H20xp8Brnc`) |
| the truth about heat pumps | relevance | "This is Why Heat Pumps May NOT Be The Future" (Skill Builder, 2,540,466, `GhAKMAcmJFg`) |
| the truth about heat pumps | views | "This is Why Heat Pumps May NOT Be The Future" (Skill Builder, 2,540,466, `GhAKMAcmJFg`) |
| the truth about heat pumps | year | "Heat Pumps Explained — And Tested \| Guy Martin" (Guy Martin , 819,141, `jbWQV2DTb3Q`) |
| the truth about heat pumps | month | "Heat Pumps Explained — And Tested \| Guy Martin" (Guy Martin , 819,141, `jbWQV2DTb3Q`) |
| do heat pumps save money | relevance | "Are Heat Pumps a Scam?" (Undecided with Matt Ferrell, 395,370, `K2c6Rucbi84`) |
| do heat pumps save money | views | "Dehumidifiers are confusing. Here's why." (Technology Connections, 3,297,613, `j_QfX0SYCE8`) |
| do heat pumps save money | year | "Why Your Water Heater Should Be a Battery" (Undecided with Matt Ferrell, 733,425, `N-gSE_eHKHg`) |
| do heat pumps save money | month | "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" (Ray Dutton's Garage, 201,002, `H0MBgMMzmyg`) |
| home warranty hvac | relevance | "Why Smart Homeowners Never Buy Home Warranties!" (HVAC GUY, 19,622, `-RFg426z5Y4`) |
| home warranty hvac | views | "STOP Buying This HVAC Brand" (The DIY HVAC Guy, 1,295,595, `x2BK-zr4raE`) |
| home warranty hvac | year | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,769, `86S3ITbfzQY`) |
| home warranty hvac | month | "Ranking the Best and Worst HVAC Brands (2026 Update)" (Yarbrough & Sons Heating, Cooling & Plumbing, 13,690, `Kdk-nTX4FZg`) |
| dehumidifier | relevance | "Dehumidifiers are confusing. Here's why." (Technology Connections, 3,297,613, `j_QfX0SYCE8`) |
| dehumidifier | views | "Dehumidifiers are confusing. Here's why." (Technology Connections, 3,297,613, `j_QfX0SYCE8`) |
| dehumidifier | year | "This $4 "DRY BUILD" Dehumidifies Your Whole Home WITHOUT USING ELECTRICITY" (Zen Garden Oasis, 1,667,248, `KphunxyIbKM`) |
| dehumidifier | month | "20 Old British Habits That Kept Winter Damp Out Before Dehumidifiers Became Normal" (Britain As It Was, 23,258, `aFcGI_GJhpw`) |
| humidity in house | relevance | "Why You Need to Keep Moisture Low this Winter" (Charlie DIYte (CharlieDIYte), 853,439, `NbtijHKy2Vo`) |
| humidity in house | views | "EASY - How to STOP CONDENSATION - Get Rid of Black Mold and Clean Mould" (Fixmyroof, 6,835,028, `Oj99RNY55Es`) |
| humidity in house | year | "Franklin's House Destroyed by Giant Tsunami in GTA 5 \| SHINCHAN and CHOP" (HAMID-T GAMING, 5,407,800, `wzpfZn4NpWM`) |
| humidity in house | month | "Franklin Mafia Boss Went Inside the Duggan Mafia’s House in GTA 5!" (HAMID-T GAMING, 976,607, `0WCqx2LKdjA`) |
| dehumidifier mistakes | relevance | "Alorair HD35P Dehumidifier Installation, Setup and Review" (Applisense, 946,439, `TCVKRQkl_0Q`) |
| dehumidifier mistakes | views | "This Grouting Mistake will Ruin Your Tile Job" (Home RenoVision DIY, 2,576,989, `cOnvsU0Q-eg`) |
| dehumidifier mistakes | year | "Where to Place an Air Purifier (Avoid These Mistakes!)" (Air Purifier First, 36,013, `-z7RVtk-FLI`) |
| dehumidifier mistakes | month | not found |
| hvac mistakes | relevance | "3 Things HVAC Contractors Don't Want You To Know About." (The DIY HVAC Guy, 2,770,141, `SkLMRM9NnBY`) |
| hvac mistakes | views | "10 Common Mistakes DIYers Make In Circuit Breaker Boxes" (LRN2DIY, 3,763,654, `NF4zxBAuRoI`) |
| hvac mistakes | year | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,929, `dOZ-8__G4uU`) |
| hvac mistakes | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,050, `mP0IjyvQtxw`) |
| hvac secrets | relevance | "3 Secrets HVAC Contractors Don't Want You to Know!" (HVAC Guide for Homeowners, 893,066, `SCquQ1LD49c`) |
| hvac secrets | views | "3 PROVEN Methods To Getting Colder Air From HVAC Vents." (The DIY HVAC Guy, 1,908,635, `hl3u2Zd7U4E`) |
| hvac secrets | year | "This $300 Tunnel Keeps Any Home 55°F Forever — The Amish System the Cooling Industry Made Illegal" (Eli Yoder Secrets, 1,275,208, `--bKaRdZGO4`) |
| hvac secrets | month | "This SECRET Fall AC Trick Is Only Known by 1% of HVAC Technicians (DO IT BEFORE WINTER)" (Exposi, 43,204, `HfELRedGjpQ`) |
| hvac tips | relevance | "Top 5 Things AC Companies Don't Want You To Know How To Do!" (How To Home, 2,979,991, `AQQH9QwC46A`) |
| hvac tips | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| hvac tips | year | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,686, `1H20xp8Brnc`) |
| hvac tips | month | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,686, `1H20xp8Brnc`) |
| air purifier | relevance | "We Tested Every Air Purifier! One Clear Winner!" (Project Farm, 1,141,349, `sQGfO4hNb60`) |
| air purifier | views | "$649 Dyson Fan vs. $15 Walmart Fan: The Hard Truth" (Mark Spurrell, 12,715,303, `dS0oFmzU06g`) |
| air purifier | year | "Delhi Air Is Getting Worse, You Need To See This \| Dhruv Rathee" (Dhruv Rathee, 6,831,238, `UE9xMBZCRJg`) |
| air purifier | month | "Best Water Purifier 2026 \| Best RO Water Purifier \| Best Water Purifier for Home" (Vineet Malhotra, 438,931, `8MV9zHA6iTM`) |
| carbon monoxide furnace | relevance | "Are BUDDY HEATERS SAFE Inside an RV ?? \| Carbon Monoxide FULL TEST( REVIEW)" (Taylor Dzaman, 2,800,973, `5vqyfOq0D-8`) |
| carbon monoxide furnace | views | "Are BUDDY HEATERS SAFE Inside an RV ?? \| Carbon Monoxide FULL TEST( REVIEW)" (Taylor Dzaman, 2,800,973, `5vqyfOq0D-8`) |
| carbon monoxide furnace | year | "How to Sleep in a Freezing Car Without a Heater" (The Last Chapter, 379,719, `6Sg63ks_4Zc`) |
| carbon monoxide furnace | month | "15 Wallmart Items Every Woman Living Alone Needs When the Furnace Dies" (Kate Sullivan Ready Living and Kate Sullivan Safer Living, 14,485, `p3DWnEKIUOI`) |
| indoor air quality | relevance | "Indoor air systems crucial to curbing spread of viruses, aerosol researchers say \| 60 Minutes" (60 Minutes, 127,016, `WxEssOeEsVk`) |
| indoor air quality | views | "Why India's Air is So Deadly (And Getting Worse!) \| Dhruv Rathee" (Dhruv Rathee, 9,820,522, `Fzs5fEbT4ic`) |
| indoor air quality | year | "We Tested Every Air Purifier! One Clear Winner!" (Project Farm, 1,141,349, `sQGfO4hNb60`) |
| indoor air quality | month | "How is Ubiquiti selling this for $99?" (Level 2 Jeff, 189,450, `bqBD8M_uYnE`) |
| attic insulation | relevance | "Insulating Attic Ceilings & Cathedral Ceilings (Phillips Vision: Episode - 63)" (Phillips Vision, 833,228, `gyAMujxceIM`) |
| attic insulation | views | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,638, `J95l9Ue4224`) |
| attic insulation | year | "Most Homeowners Insulate Shed Roofs WRONG (Do This Instead)" (Everyday Home Repairs and Everyday Shed, 1,902,406, `2uixLIvv4H0`) |
| attic insulation | month | "Building a New Roof on The Old House - House Build #26" (Wolf Pup Fab, 260,861, `SCFD0eMzC5k`) |
| rim joist insulation | relevance | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,638, `J95l9Ue4224`) |
| rim joist insulation | views | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,638, `J95l9Ue4224`) |
| rim joist insulation | year | "This System Will Change How You Renovate a Basement Forever" (Home RenoVision DIY, 588,908, `8W2PoGpSCYM`) |
| rim joist insulation | month | "Contractor Reveals 3 Insulations That Are WAY Better Than Spray Foam" (Built to DIY, 4,202, `rXQ2IA3lNWo`) |
| spray foam | relevance | "DIY Spray Foam Kit! Does It WORK???" (The Kelley's Country Life, 1,977,684, `1XFe2KuXdYU`) |
| spray foam | views | "Why Didn’t I Know This! Spray WD-40 on Foam and Fix Any Broken Plastic in Your Home!" (Inventor Hacks, 8,776,083, `pXWAABQj0-g`) |
| spray foam | year | "Most Homeowners Insulate Shed Roofs WRONG (Do This Instead)" (Everyday Home Repairs and Everyday Shed, 1,902,406, `2uixLIvv4H0`) |
| spray foam | month | "This Pre-Drywall Inspection Was BAD BAD " (gold.star.inspections, 226,800, `ZyYx7qmGpy0`) |
| spray foam alternative | relevance | "We Built Our House In 4 DAYS With FOAM!" (Bisbone Ranch, 3,540,777, `wBbHlahTm7M`) |
| spray foam alternative | views | "It's Been a Good Run, Drywall." (LRN2DIY, 6,423,093, `uHGHeTzznhM`) |
| spray foam alternative | year | "Drywall Is Dead. Do This Instead." (HAXMAN, 3,227,779, `ji5UfRIVAvI`) |
| spray foam alternative | month | "Tired of scrubbing your tires? Get them done fast with 4-X Tire Spray. Shiny, clean tires in unde..." ( Wax Master, 8,534, `23gfAnUnawE`) |
| window insulation | relevance | "Why Don't More People Insulate Windows Like This?" (Fix This Build That, 811,914, `1jJILdeZ1jg`) |
| window insulation | views | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (Home RenoVision DIY, 5,826,638, `J95l9Ue4224`) |
| window insulation | year | "Most Homeowners Insulate Shed Roofs WRONG (Do This Instead)" (Everyday Home Repairs and Everyday Shed, 1,902,406, `2uixLIvv4H0`) |
| window insulation | month | "I Tested Window Film, Bubble Wrap & Thermal Curtains — Not Even Close" (Ivan’s Survival Journal and 3 more, 243,332, `e1f_psQ1zBs`) |
| insulation mistakes | relevance | "The Spray Foam Insulation Problem Nobody's Talking About" (Skill Builder, 3,022,192, `jYNufQVIFfA`) |
| insulation mistakes | views | "10 Beginner Mistakes Installing Vinyl Plank Flooring" (Fix This Build That, 15,713,486, `kvo-n2AYZnA`) |
| insulation mistakes | year | "Most Homeowners Insulate Shed Roofs WRONG (Do This Instead)" (Everyday Home Repairs and Everyday Shed, 1,902,406, `2uixLIvv4H0`) |
| insulation mistakes | month | "Use These 7 Tricks To Sleep Like A Baby In Your Van In FREEZING Canadian winters.." (Matz Veenstra, 2,411, `Yv6R3xVqoQA`) |
| home designs that stayed cool | relevance | "When Interior Designs Are Next Level" (BE AMAZED, 4,608,246, `UhUuBnDZMpk`) |
| home designs that stayed cool | views | "How to cool our homes (even without ACs)" (DW Planet A, 3,648,225, `sKbEOMCsqaI`) |
| home designs that stayed cool | year | "20 Forgotten Home Designs That Stayed Cool Before Air Conditioning" (Forgotten Home Engineering and Forgotten American Survival, 406,979, `mD6BZwBSq6c`) |
| home designs that stayed cool | month | "20 Small House Features That Should Be Standard in Every House" (Home Central and 2 more, 172,891, `yCM145y0QYA`) |
| cool house without ac | relevance | "Best fan placement to move air through the house" (Matthias random stuff, 11,467,376, `1L2ef1CP-yw`) |
| cool house without ac | views | "Best fan placement to move air through the house" (Matthias random stuff, 11,467,376, `1L2ef1CP-yw`) |
| cool house without ac | year | "Turn Any Fan Into an Air Conditioner with 2 Ice Bottles ($0 DIY AC)" (Why Am I Green, 3,707,998, `H514-w6ttNo`) |
| cool house without ac | month | "How Ancient Egyptians Survived 50°C Heat Without Air Conditioning" (GRENY, 1,539,873, `lC4HeSA5bwU`) |
| keep house cool | relevance | "How to cool our homes (even without ACs)" (DW Planet A, 3,648,225, `sKbEOMCsqaI`) |
| keep house cool | views | "Best fan placement to move air through the house" (Matthias random stuff, 11,467,352, `1L2ef1CP-yw`) |
| keep house cool | year | "How Ancient Egyptians Survived 50°C Heat Without Air Conditioning" (GRENY, 1,539,873, `lC4HeSA5bwU`) |
| keep house cool | month | "I Secretly Hid a Viral Toy Store In My House!" (Zhong, 4,323,830, `3hXzig1a9XQ`) |
| heat house cheap | relevance | "My DIY Geothermal System Was So CHEAP!!!" (The Challenged One, 3,277,577, `MUWjjjFgXdg`) |
| heat house cheap | views | "How to cool our homes (even without ACs)" (DW Planet A, 3,648,225, `sKbEOMCsqaI`) |
| heat house cheap | year | "FREE Heat All Winter😱!! Millions of people don't know this secret! No Gas, No Electricity" (Creation Daily, 11,837,842, `RotAhlS7LQ4`) |
| heat house cheap | month | "15 Cheap Walmart Items That Become WORTH GOLD When Your Furnace Dies" (Lost Survival Knowledge and Everyday Survival Knowledge, 1,309,038, `rX4eyZaHAjw`) |
| keep house warm | relevance | "How Do We Keep Warm at -71°C (-95°F)? House Tour \| Yakutia" (Kiun B, 6,660,399, `xZotuV1qkvA`) |
| keep house warm | views | "How Do We Keep Warm at -71°C (-95°F)? House Tour \| Yakutia" (Kiun B, 6,660,399, `xZotuV1qkvA`) |
| keep house warm | year | "Why Scandinavian Cabins Stayed Warm At -30°F While Modern Homes Freeze" (Medieval Way, 1,402,893, `eVqwiMtoDhk`) |
| keep house warm | month | "How Did Japanese People Survive Winter in Houses Made of Paper?" (inkly, 579,766, `OQCl9rN0xyM`) |
| before you shut your ac down | relevance | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,929, `dOZ-8__G4uU`) |
| before you shut your ac down | views | "AC not working!!! The CAR WIZARD shows how to easily isolate the problem" (Car Wizard, 2,559,447, `bVYUzp8QQ0M`) |
| before you shut your ac down | year | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,929, `dOZ-8__G4uU`) |
| before you shut your ac down | month | "Before You Shut Down Your AC This Fall, Do THIS!" (Fix This House, 14,767, `6J5IUqH2Cx8`) |
| before you turn on your ac | relevance | "I can't believe Mechanics don't know How to Recharge AC system correctly!" (NATES INTERACTIVE AUTO, 6,280,120, `Ehls11Ddm8A`) |
| before you turn on your ac | views | "How to Recharge Your Car's AC System (Fast and Easy)" (ChrisFix, 10,771,363, `SHg2xRMnM38`) |
| before you turn on your ac | year | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,929, `dOZ-8__G4uU`) |
| before you turn on your ac | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,050, `mP0IjyvQtxw`) |
| before you turn on your heat | relevance | "How to Fix a Car with No Heat (Easy)" (ChrisFix, 9,796,007, `-XjXTVJhFLM`) |
| before you turn on your heat | views | "How to Fix a Car with No Heat (Easy)" (ChrisFix, 9,796,007, `-XjXTVJhFLM`) |
| before you turn on your heat | year | "The SADDEST Game on Roblox... (NEED MORE HEAT, All Endings)" (Bundun, 3,092,695, `wJg0B5ZMTqk`) |
| before you turn on your heat | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,050, `mP0IjyvQtxw`) |
| do this before winter furnace | relevance | "Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night)" (Ray Dutton's Garage, 934,734, `fHAlfm21vYw`) |
| do this before winter furnace | views | "Top 5 Furnace Problems and How to Fix Them" (Word of Advice TV, 2,163,220, `T4IWtKy--Vk`) |
| do this before winter furnace | year | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (Ray Dutton's Garage, 1,212,929, `dOZ-8__G4uU`) |
| do this before winter furnace | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,050, `mP0IjyvQtxw`) |
| do this once a month ac | relevance | "The COLDEST And QUIETEST AC Unit Ever Made!  Still Use Your Window!" (How To Home, 2,007,929, `_Qa5teuVPRg`) |
| do this once a month ac | views | "1 Ton AC Electricity Bill \|\| 1 Month Unit Consumption & Electricity Bill \|\| 1Ton AC Bill Calculation" (Universal Lineman, 314,037, `Vqq8Bu_7U-M`) |
| do this once a month ac | year | "Do THIS Once a Month and Your AC Will Last 25 Years" (John The HVAC Guy, 232,707, `CJhglI70jw8`) |
| do this once a month ac | month | not found |
| hvac maintenance | relevance | "How To Check & Replace An Air Conditioner Capacitor" (The DIY HVAC Guy, 2,393,744, `FQisFmMtAis`) |
| hvac maintenance | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| hvac maintenance | year | "How Data Centers Actually Work" (MEP Academy, 1,543,660, `cTwvUqLNQrM`) |
| hvac maintenance | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,050, `mP0IjyvQtxw`) |
| mini split | relevance | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| mini split | views | "Building a Tiny Office Pod Under My Stairs" (Man Made, 18,449,234, `b0npGI9WCzs`) |
| mini split | year | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,693, `1H20xp8Brnc`) |
| mini split | month | "I Have Strong Feelings About Air Conditioning in the Tech House" (Linus Tech Tips, 1,975,693, `1H20xp8Brnc`) |
| mini split mistakes | relevance | "DIY Mini Split Install: 3 Regrets After 1 Year of Use" (LRN2DIY, 2,387,613, `5dCCntGj1wM`) |
| mini split mistakes | views | "7 FATAL Wiring Mistakes Most DIYers Don't Know They Are Making \| Most Are Guilty of 3" (How To Home, 12,129,083, `-jeP1d8PC1I`) |
| mini split mistakes | year | "Top 5 Mini Split Installation Mistakes - Don't Do This!" (Taddy Digest, 133,281, `D_2T5H7CFmA`) |
| mini split mistakes | month | "Mini Split Ac PCB Looked Unrepairable… But The Result Surprised Me!" (Forever Tech English, 3,706, `DIJ7JQtQ24A`) |
| mini split vs central air | relevance | "Ranking the Best and Worst Mini Split Brands" (Yarbrough & Sons Heating, Cooling & Plumbing, 259,940, `yIOmar-8Rl0`) |
| mini split vs central air | views | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| mini split vs central air | year | "Why Didn't Anyone Think Of This Sooner?" (The DIY HVAC Guy, 971,434, `vDhwBsP0Ybs`) |
| mini split vs central air | month | "The $1,500 Mini Split That Beats a $4,500 Central AC (For One Hot Room)" (Ask Big Jim., 220, `7U4bpzweVqQ`) |
| ac making noise | relevance | "AIR CONDITIONER \| Relaxing White Noise For Great Sleep (10 Hours)" (Relaxing White Noise, 5,235,555, `MsfbGmctqLM`) |
| ac making noise | views | "(No Ads) 10 Hours of Soft White Noise \| Black Screen for Sleep" (Let's Find Out, 25,778,285, `Og40mpl8VNc`) |
| ac making noise | year | "Panasonic AC 1.5 Ton 5 Star \| Best 1.5 Ton 5 Star AC \| Best AC 2026" (Vineet Malhotra, 3,243,403, `a93CLRfZSj4`) |
| ac making noise | month | "[NO ADS] FALL ASLEEP FAST \| AC & Rain Sounds for Sleep \| 12 Hours Black Screen 🌧️😴" (Your Nature Sound, 98,698, `PmZ4QR49kmU`) |
| banging radiator | relevance | "Noisy radiator. How To Fix Banging Ticking Knocking Hammering radiator noise?" (Heating Solutions, 64,797, `5hurO6e1xlc`) |
| banging radiator | views | "How To Bleed A Radiator - Don’t try it until you watch this" (Allen Hart, 2,404,197, `tbLz8icLr2U`) |
| banging radiator | year | "Steam Boiler BANGING Like a Jackhammer! Flooded Burnham Independence FIXED 🔧💥" (Mikey Pipes - Pipe Doctor Plumbing & Heating & Air, 19,039, `PmH0TyW91u4`) |
| banging radiator | month | not found |
| furnace noise | relevance | "0°C outside and you are near the fan heater... \| heater sound, white noise, relaxing, sleeping," (-Extreme Relaxing ASMR Sounds-, 8,876,364, `yhKe7roI82M`) |
| furnace noise | views | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,616,840, `OE9bF80KQGk`) |
| furnace noise | year | "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" (Ray Dutton's Garage, 767,290, `_ZgVjFpBnQA`) |
| furnace noise | month | "CEO Fired a Single Dad Furnace Tech to Cut Costs—3 Days Later, He Heard What No One Else Could" (Secret Life, 46,471, `_6Q6IF8BC2I`) |
| oil furnace | relevance | "Millions Don’t Know That Waste Oil Is a Gold Mine! DIY 3-in-1 Heating Stove" (Creative inventions LMTN, 7,559,821, `ZVlv3r1KQyo`) |
| oil furnace | views | "Millions of people do not know this knowledge! 3 in 1 waste oil heater! Warm for winter 2024" (Creative inventions LMTN, 14,876,612, `UawMGmg87ho`) |
| oil furnace | year | "Millions Don’t Know That Waste Oil Is a Gold Mine! DIY 3-in-1 Heating Stove" (Creative inventions LMTN, 7,559,821, `ZVlv3r1KQyo`) |
| oil furnace | month | "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" (Ray Dutton's Garage, 201,098, `H0MBgMMzmyg`) |
| oil furnace won't ignite | relevance | "Troubleshoot the oil furnace part 1. Burner won't start." (grayfurnaceman, 1,043,525, `cog7MaShR7M`) |
| oil furnace won't ignite | views | "TOP 10 Reasons Why the Gas Pilot Light Goes Out & Won't Stay Lit!" (AC Service Tech LLC, 2,062,038, `PiCmfW1rTRY`) |
| oil furnace won't ignite | year | "BECKETT OIL BURNER NOT FIRING UP" (steven lavimoniere / PLUMBING HEATING & AC VIDEO'S, 16,167, `KzSlMKMSiTE`) |
| oil furnace won't ignite | month | not found |
| heating oil vs gas | relevance | "Jet Fuel VS Diesel VS Gasoline how they burn and what color are they." (Just Think, 6,170,959, `7nL10C7FSbE`) |
| heating oil vs gas | views | "Petroleum - Modern history of oil on a Map" (Geo History, 10,754,521, `xMQUGSrnbP8`) |
| heating oil vs gas | year | "Steve Ballmer Explains The Cost of Oil" (USAFacts, 10,751,181, `KEiKy6mf2Ew`) |
| heating oil vs gas | month | "Rising diesel prices putting more pressure on businesses" (KXAN, 495,801, `dcEshNIrHpg`) |
| oil furnace vs gas furnace | relevance | "Don't Buy a High Efficiency Furnace!" (Word of Advice TV, 383,347, `7d783qs3laA`) |
| oil furnace vs gas furnace | views | "5 Furnace Filter Mistakes That Will Cost You Money!" (The Funny Carpenter, 2,871,508, `_g8gQ1gg1FM`) |
| oil furnace vs gas furnace | year | "Are Heat Pumps a Scam?" (Undecided with Matt Ferrell, 395,370, `K2c6Rucbi84`) |
| oil furnace vs gas furnace | month | "STOP Paying $3,000 for HEAT — This $50 HOMEMADE FURNACE Heats Your Home All Winter" (Amos Miller, 1,271, `QkhFk8icbms`) |
| oil furnace maintenance | relevance | "Oil Heat 🔥 Boilers - How it works - Understand the Basics" (Silver Cymbal, 821,099, `5GbXgEYw5TE`) |
| oil furnace maintenance | views | "5 Furnace Filter Mistakes That Will Cost You Money!" (The Funny Carpenter, 2,871,508, `_g8gQ1gg1FM`) |
| oil furnace maintenance | year | "Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night)" (Ray Dutton's Garage, 934,746, `fHAlfm21vYw`) |
| oil furnace maintenance | month | "RIELLO OIL BURNER  FURNACE SERVICE" (steven lavimoniere / PLUMBING HEATING & AC VIDEO'S, 9,167, `-9-DQH8yx2I`) |
| power outage heat | relevance | "Crisco candle room heating \| Power Outage Room Heating \| 9 hour test" (Riverside Homestead , 1,285,119, `0vwONToPGXg`) |
| power outage heat | views | "UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,298, `7LV5wY-iM34`) |
| power outage heat | year | "UNLIMITED Heat For Your Home Or Greenhouse \| No Electric Needed" (Zen Garden Oasis, 4,009,364, `kO3rWyULVYY`) |
| power outage heat | month | "FLORIDA HIT BY HURRICANE ISAIAS — Severe Flooding, Widespread Power Outages & Dangerous Conditions" (US Housing Report, 1,554,357, `FmruBdrbiQs`) |
| furnace not working after power outage | relevance | "Keep Your Family Warm During A Power Outage By Installing This $5 Part" (The DIY HVAC Guy, 4,275,329, `y07w1hiKIrI`) |
| furnace not working after power outage | views | "How to fix your AC: fan not spinning" (Kent's Garage Gym, 4,863,494, `SRNjf4-F9Tg`) |
| furnace not working after power outage | year | "15 Dollar Tree Items That Become WORTH GOLD When Your Furnace Stops Working" (Lost Survival Knowledge and Everyday Survival Knowledge, 510,576, `lm1kEiEnlPQ`) |
| furnace not working after power outage | month | "15 Dollar Tree Items That Become WORTH GOLD When Your Furnace Stops Working" (Lost Survival Knowledge and Everyday Survival Knowledge, 510,576, `lm1kEiEnlPQ`) |
| heat without power | relevance | "UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,298, `7LV5wY-iM34`) |
| heat without power | views | "The Most Misunderstood Concept in Physics" (Veritasium, 31,362,549, `DxL2HoqLbyA`) |
| heat without power | year | "FREE Heat All Winter😱!! Millions of people don't know this secret! No Gas, No Electricity" (Creation Daily, 11,837,982, `RotAhlS7LQ4`) |
| heat without power | month | "9 Ways I Keep My Bed Warm With No Heat (The Cold Comes From Underneath)" (June's Kitchen Table, 518,715, `1Oz08l8RTWg`) |
| stay warm without power | relevance | "FREE Heat All Winter😱!! Millions of people don't know this secret! No Gas, No Electricity" (Creation Daily, 11,837,982, `RotAhlS7LQ4`) |
| stay warm without power | views | "Winter Survival Shelter, Stay Warm Overnight With No Fire" (Scavenger Survival, 19,456,552, `lwv-vKYJV1o`) |
| stay warm without power | year | "UNLIMITED Heat For Your Home Or Greenhouse \| No Electric Needed" (Zen Garden Oasis, 4,009,364, `kO3rWyULVYY`) |
| stay warm without power | month | "9 Ways I Keep My Bed Warm With No Heat (The Cold Comes From Underneath)" (June's Kitchen Table, 518,715, `1Oz08l8RTWg`) |
| keep your family warm during a power outage | relevance | "Keep Your Family Warm During A Power Outage By Installing This $5 Part" (The DIY HVAC Guy, 4,275,329, `y07w1hiKIrI`) |
| keep your family warm during a power outage | views | "Keep Your Family Warm During A Power Outage By Installing This $5 Part" (The DIY HVAC Guy, 4,275,329, `y07w1hiKIrI`) |
| keep your family warm during a power outage | year | "90s Village Storm Night 🌧️ Power Cut & Rooftop Sleep \| Cozy Rain Story" (Cozy Ghibli vlogs, 6,097,310, `-RLc5voRm4w`) |
| keep your family warm during a power outage | month | "Government Says Prepare for Winter: Get These 10 Things Now" (Be Prepared UK, 357,057, `mtDx0ajdvq4`) |
| ac capacitor | relevance | "How To Check & Replace An Air Conditioner Capacitor" (The DIY HVAC Guy, 2,393,744, `FQisFmMtAis`) |
| ac capacitor | views | "Capacitors Explained - The basics how capacitors work working principle" (The Engineering Mindset, 11,078,034, `X4EUwTwZ110`) |
| ac capacitor | year | "Multimeter चलाना सीखें (A to Z) \| How to use Digital Multimeter \| Multimeter Checking Hindi" (Technical Jugaad Hindi, 1,912,817, `LWMZma2E6LE`) |
| ac capacitor | month | "Resistor vs Capacitor vs Inductor — Why They Behave So Differently ?" (Prof MAD, 253,370, `5KQBgmvRHnA`) |
| contactor | relevance | "Contactors: how we power the big stuff" (Technology Connections, 1,664,333, `VsNHrAzx5_w`) |
| contactor | views | "Star Delta Starter Control Wiring Using Tense ERV-YU Timer \| @ElectricalTechnician" (Electrical Technician, 2,676,770, `_-efxckFkFw`) |
| contactor | year | "Contactor Issues " (Cursed Controls, 280,033, `Kd_YNg2RNxA`) |
| contactor | month | "Silver Recovery from Circuit Breaker Contacts \| Complete Extraction Process" (Iman Gold Recovery, 50,056, `vsRLVbMORBI`) |
| furnace flame sensor | relevance | "How To Clean Your Furnace Flame Sensor" (HouseImprovements, 1,064,481, `R7AKPgBB_R4`) |
| furnace flame sensor | views | "The Most Common Reason Why A Gas Furnace Won't Turn On" (Everyday Home Repairs, 2,773,003, `sRvH-io-ZtA`) |
| furnace flame sensor | year | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,076, `mP0IjyvQtxw`) |
| furnace flame sensor | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,076, `mP0IjyvQtxw`) |
| furnace igniter | relevance | "Furnace Not Igniting - How to Check and Replace Ignitor" (Word of Advice TV, 1,365,238, `1bRsFAMgZRQ`) |
| furnace igniter | views | "How To Light A Gas Water Heater Pilot Light" (HouseImprovements, 3,777,125, `t5gJRU-20a0`) |
| furnace igniter | year | "How to Test and Replace an RV Furnace Circuit Board \| Step by Step" (Mobile RV Tech Services (Radar Road Warriors), 15,143, `4MbiAdrygwc`) |
| furnace igniter | month | "3 Camper Maintenance Items: Sun-Lite 16BH" (Videozar, 553, `kBAZMj_K_UU`) |
| ac recharge | relevance | "How to Properly Recharge Your AC System" (ChrisFix, 12,893,682, `Pdq8JAlct6s`) |
| ac recharge | views | "How to Properly Recharge Your AC System" (ChrisFix, 12,893,682, `Pdq8JAlct6s`) |
| ac recharge | year | "This SECRET Will Make Your Car's AC Blow Twice as Cold" (All Car Talk, 1,017,667, `Uz9YxPmkvjc`) |
| ac recharge | month | "Electric Appliances, AC, TV । Gold-Silver Price । Mobile Recharge । Asian Games । THE KHALAS TV" (The Khalas TV, 15,446, `d7MB9wfdDbg`) |
| freon | relevance | "Kenyan RNBs Love Songs ft Dj Freon Sauti Sol Elani Nyashinski Bensoul Nviiri Gilad Hart the Band" (Dj Freon, 2,944,337, `WNlXR6llLew`) |
| freon | views | "DAD Reacts to 11 Year old Son's CRINGE TIKTOKS!! 😂" (The Royalty Family, 63,418,912, `4SuPs7XrBW8`) |
| freon | year | "WATCH: Trump rolls back Biden-era refrigerant rules" (LiveNOW from FOX, 210,485, `vuwHM5x7Dk0`) |
| freon | month | "#AUTOPSI \| Bongkar Garansi Mobil 5 Tahun⁉️Sengaja Dibikin Gak Awet⁉️ - Dokter Mobil Indonesia" (Dokter Mobil Indonesia, 63,577, `-8zyGOkc8iw`) |
| ac losing freon | relevance | "How to Find AC Leaks in Your Car (UV Dye)" (ChrisFix, 5,912,281, `pCv7rCdcXsc`) |
| ac losing freon | views | "How to Recharge Your Car's AC System (Fast and Easy)" (ChrisFix, 10,771,363, `SHg2xRMnM38`) |
| ac losing freon | year | "$4,000 vs Reality (DEALERSHIP LIED) What's Actually Wrong With This 2019 Jeep Grand Cherokee?" (Rainman Ray's Repairs, 377,226, `mpZXXDkKAmk`) |
| ac losing freon | month | "Finding AC Evaporator Leaks and Welding" (Karir Kedua, 781, `nQtnjw00VZ8`) |
| hvac replacement cost | relevance | "STOP Replacing Your AC Unit TOO Soon!!!" (Atlas AC, 330,711, `EKBueP7_n7c`) |
| hvac replacement cost | views | "Is Geothermal Heating and Cooling Worth the Cost?  Heat Pumps Explained" (Undecided with Matt Ferrell, 3,682,327, `PI45yUhUWgk`) |
| hvac replacement cost | year | "Genius AC Upgrade That Makes Air Colder And Bills Lower!" (How To Home, 1,769,523, `gQjotD-B0OU`) |
| hvac replacement cost | month | "The ONLY Fall AC Maintenance Schedule You'll Ever Need (Save Thousands)" (Exposi, 11,092, `mQUhC-ZuuEs`) |
| mini split cost installed | relevance | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| mini split cost installed | views | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| mini split cost installed | year | "How to Install a $360 Mini Split Heat Pump — Complete DIY Guide" (There's A Trick For That, 555,879, `uv75G4ed2dw`) |
| mini split cost installed | month | "$80 Wood Stove vs $900 Mini-Split: Which One Really Heats a Room Cheaper?" (Backyard Low Tech, 1,413, `vGvdKaUPEeQ`) |
| new ac cost | relevance | "Best AC Buying Guide 2026 \| Monthy Electricity Bill \| Inverter vs Non-Inverter \| 3 Star vs 5 Star \|" (MR KNOWN, 757,609, `4_A_tGg6HrE`) |
| new ac cost | views | "Learn SPLIT AC Servicing at Home full process \|\| Learn SPLIT AC Cleaning at home full process \|\|" (emm vlogs, 6,134,983, `XrMS3v4jZyM`) |
| new ac cost | year | "Tesla New Solar Panel लांच : पूरी Solar Industry एक झटके में खत्म! 😱 Game Over? ⚡" (Deepak chaudhary Nexus solar energy, 5,836,908, `1WDLM5K0bVM`) |
| new ac cost | month | "ICG New Vacancy 2027 \| Cost Guard Eligibility, Age Limit, Online Form \| ICG GD DB Notification" (Rojgar with Ankit Defence, 353,518, `_AREZXhqxVM`) |
| new furnace cost | relevance | "What is the BEST Furnace Brand to Get?" (Word of Advice TV, 91,302, `OLhZVaWH9Tw`) |
| new furnace cost | views | "Is Geothermal Heating and Cooling Worth the Cost?  Heat Pumps Explained" (Undecided with Matt Ferrell, 3,682,327, `PI45yUhUWgk`) |
| new furnace cost | year | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,769, `86S3ITbfzQY`) |
| new furnace cost | month | "Carney announces $2B to help homeowners lower heating costs and reduce emissions \| FULL" (Global News, 16,767, `Ap8Q9xkiH1Y`) |
| beating the hvac industry | relevance | "How Smart Homeowners Are Beating the HVAC Industry (The 15-Year Loophole)" (HVAC Exposed, 382,368, `wz-06sf2Dy0`) |
| beating the hvac industry | views | "How Smart Homeowners Are Beating the HVAC Industry (The 15-Year Loophole)" (HVAC Exposed, 382,368, `wz-06sf2Dy0`) |
| beating the hvac industry | year | "How Smart Homeowners Are Beating the HVAC Industry (The 15-Year Loophole)" (HVAC Exposed, 382,368, `wz-06sf2Dy0`) |
| beating the hvac industry | month | "How Smart Homeowners Are Beating the HVAC Industry (The 20-Year Loophole)" (George Smith's Garage, 88, `dxu0VHyB_-s`) |
| duct cleaning scams | relevance | "Air Duct Cleaning Scam Exposed!" (Pleasant Green, 3,414,997, `J_FMXc7F_bM`) |
| duct cleaning scams | views | "I Gave HACKED SCAMMERS a PANIC ATTACK On CCTV!" (Scam Sandwich, 13,674,344, `fhej9kABoyQ`) |
| duct cleaning scams | year | "AIR DUCT CLEANING GREATER MONTREAL - How to avoid scams - Includes pricing" (Air Plus Montreal, 31,122, `-cmaRDcL7Z0`) |
| duct cleaning scams | month | "17 AC SCAMS Everyone Is Falling For (Don't Be One)" (Exposi, 261, `EDloptyqd4g`) |
| hvac companies don't want you to know | relevance | "Top 5 Things AC Companies Don't Want You To Know How To Do!" (How To Home, 2,980,017, `AQQH9QwC46A`) |
| hvac companies don't want you to know | views | "Top 5 Things AC Companies Don't Want You To Know How To Do!" (How To Home, 2,980,017, `AQQH9QwC46A`) |
| hvac companies don't want you to know | year | "9 Things Exterminators Don't Want You to Know About Hydrogen Peroxide" (Stop Wasting Stuff, 2,597,239, `XGTMtSyDPYQ`) |
| hvac companies don't want you to know | month | "Top 5 Things HVAC Companies Don't Want You To Know How To Do!" (John The HVAC Guy and 6 more, 1,727, `rd2dwGnTLQg`) |
| hvac companies hate | relevance | "HVAC Contractors Hate Me For Sharing This Secret" (The DIY HVAC Guy, 1,617,270, `FMr4xOkUbO8`) |
| hvac companies hate | views | "HVAC Contractors Hate Me For Sharing This Secret" (The DIY HVAC Guy, 1,617,270, `FMr4xOkUbO8`) |
| hvac companies hate | year | "The Utility Company HATES This Air Conditioner" (The DIY HVAC Guy, 317,652, `aFOSLm4RXwQ`) |
| hvac companies hate | month | "HVAC Contractors HATE ME For Sharing This." (The DIY HVAC Guy, 54,982, `AWHQ9OPv9tk`) |
| hvac scam | relevance | "Hidden cameras catch HVAC scam in action (Marketplace)" (CBC News, 2,292,088, `4NPPRoqd7No`) |
| hvac scam | views | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`) |
| hvac scam | year | "Breeza Max Exposed: Inside The Viral Portable A/C Scam #BreezaMaxScam #PortableAC #PolarBreeze" (JDub Adventures, 2,619,488, `JZ4vlMZlCj8`) |
| hvac scam | month | "HVAC Scam Exposed: What They Don't Want You To Know" (steven lavimoniere / PLUMBING HEATING & AC VIDEO'S, 30,274, `skAR4jVHNyA`) |
| hvac scam caught on camera | relevance | "Hidden cameras catch HVAC scam in action (Marketplace)" (CBC News, 2,292,088, `4NPPRoqd7No`) |
| hvac scam caught on camera | views | "Oil change scams: Hidden camera investigation on what really happens to your car (CBC Marketplace)" (CBC News, 48,175,189, `-avpx8UTakI`) |
| hvac scam caught on camera | year | "NEVER Sign The $8,000 Estimate — Say This Sentence Instead (HVAC Scam)" (Shaun Meeker, 84, `_D6QDaQmgIs`) |
| hvac scam caught on camera | month | "NEVER Sign The $8,000 Estimate — Say This Sentence Instead (HVAC Scam)" (Shaun Meeker, 84, `_D6QDaQmgIs`) |
| hvac upsell | relevance | "Selling, Upselling, IAQ , Hardstart Kits and More" (HVAC School, 30,221, `HgifX1OxpXY`) |
| hvac upsell | views | "Oil change scams: Hidden camera investigation on what really happens to your car (CBC Marketplace)" (CBC News, 48,175,189, `-avpx8UTakI`) |
| hvac upsell | year | "The Economics of Owning a HVAC Company" (Cost Anatomy, 4,574, `p-WnvOqHz_A`) |
| hvac upsell | month | "The Economics of Owning a HVAC Company" (Cost Anatomy, 4,574, `p-WnvOqHz_A`) |
| ac short cycling | relevance | "Air Conditioner Condenser Short Cycling - 10 Possible Causes" (Word of Advice TV, 562,343, `GEVNSrOrohA`) |
| ac short cycling | views | "Ford A/C Quick Tips #7: How To Quickly Diagnose A/C Concerns" (FordTechMakuloco, 1,899,846, `VhU2KeumoVk`) |
| ac short cycling | year | "Signs of bad AC compressor vs Pressure Switch (how to Fix, test, and reset)" (Auto V Fix , 575,464, `m9iqmUVQs74`) |
| ac short cycling | month | "Short Cycling Lennox AC – Low Charge, Coil Leak & Warranty Claim" (WW HVAC, 4,434, `DGZn_wr0ysk`) |
| furnace short cycling | relevance | "Furnace Starts Then Stops - Troubleshooting \| Repair and Replace" (AMRE Supply, 1,089,225, `b0sAGt-1niU`) |
| furnace short cycling | views | "Furnace Starts Then Stops - Troubleshooting \| Repair and Replace" (AMRE Supply, 1,089,225, `b0sAGt-1niU`) |
| furnace short cycling | year | "ecobee Essential: Common Problems Solved (Don’t Make This Install Mistake!)" (Rob - Tools and Tech, 8,849, `lkIbboSSjVk`) |
| furnace short cycling | month | "Short Cycling Lennox AC – Low Charge, Coil Leak & Warranty Claim" (WW HVAC, 4,434, `DGZn_wr0ysk`) |
| short cycling | relevance | "15 Min HIIT Cardio Indoor Cycling Workout \| Belly Fat Loss Exercise" (GCN Training, 3,138,185, `ewrf_rCHUdA`) |
| short cycling | views | "If it were not filmed, nobody would believe │ Short Documentary" (RIFIANBOY, 11,761,233, `d-kPcOVub4M`) |
| short cycling | year | "CYCLING THE WORLD \| Award-Winning Adventure Documentary" (McKenzie Barney, 822,222, `riosld1YI9w`) |
| short cycling | month | "MTBWS HIGHLIGHTS 🇺🇸 Men's Elite XCC \| 2026 Lake Placid Olympic Sites" (WHOOP UCI Mountain Bike World Series and 2 more, 120,234, `acjoDwMrzqA`) |
| burning smell furnace | relevance | "This Furnace Malfunction KILLS PEOPLE! Homeowners Should watch (ROLLOUT GAS BURN FURNACE)" (The Honest Carpenter, 807,163, `YIReblFci9c`) |
| burning smell furnace | views | "Yearly Furnace Cleaning And Maintenance Pro Tips" (Everyday Home Repairs, 2,156,846, `--A2I2s7aNw`) |
| burning smell furnace | year | "OLD GAS FURNACE WITH FAN ISSUES" (steven lavimoniere / PLUMBING HEATING & AC VIDEO'S, 10,612, `ypnDiKmJau0`) |
| burning smell furnace | month | "Heater Smells Like It's Burning? Here's Why (And When to Worry!) " (Fix it with Jay , 735, `uU8GjghESPA`) |
| furnace smell | relevance | "Yearly Furnace Cleaning And Maintenance Pro Tips" (Everyday Home Repairs, 2,156,846, `--A2I2s7aNw`) |
| furnace smell | views | "I Built The Worlds Largest Minecraft Furnace" (Carvs, 12,044,095, `qsarR6CnN1w`) |
| furnace smell | year | "Minecraft, But You Smelt Any Item..." (Wisp, 1,223,611, `Eq5kIVlmtS4`) |
| furnace smell | month | "Do THIS To Your Furnace Before October 1st" (Mr. Barlow and Mrs. Doris, 847, `_PiH7KbaqqE`) |
| space heater | relevance | "WHITE NOISE  FAN HEATER Sleep, Meditation, RELAXING" (CALM and RELAX, 8,999,133, `hWQPenWeW_s`) |
| space heater | views | "WHITE NOISE \| House Sounds \| Fan Heater" (Soundbuds™, 9,416,492, `_wGwcPuXykI`) |
| space heater | year | "My water heater is cooler than yours" (Technology Connections, 1,890,309, `F_7B2shTPPU`) |
| space heater | month | "The Room Heater That Killed 155 People" (Fathom, 420,077, `ocuuaeKt94A`) |
| space heater vs central heat | relevance | "Space Heater Nonsense" (Technology Connections, 5,386,824, `V-jmSjy2ArM`) |
| space heater vs central heat | views | "Space Heater Nonsense" (Technology Connections, 5,386,824, `V-jmSjy2ArM`) |
| space heater vs central heat | year | "No Central Heating? Here's What Japanese Homes Do Instead" (Japan with Nao, 1,915,681, `FsmLvHuA96M`) |
| space heater vs central heat | month | "These Cheap Tricks Keep You Warm All Winter Without Central Heat" (Earl Knows How, 2,180, `AgQ9NXtjSKo`) |
| space heater save money | relevance | "Space Heater Nonsense" (Technology Connections, 5,386,824, `V-jmSjy2ArM`) |
| space heater save money | views | "Space Heater Nonsense" (Technology Connections, 5,386,824, `V-jmSjy2ArM`) |
| space heater save money | year | "I’ve Never Seen A Space Heater This Good!" (Project Farm, 1,166,039, `ND2mrzPnBic`) |
| space heater save money | month | "10 Grandma Tricks That Instantly Make Living Alone Easier After 60" (Wonders and 6 more, 117,754, `Dm7vY60TToA`) |
| turning your heat down | relevance | "Thermostat Not Turning On Heat - How To Fix It" (Word of Advice TV, 934,071, `054cRskeh5k`) |
| turning your heat down | views | "Turning Our Pool Into the World's Biggest Hot Tub!!!" (Beyond Family, 8,470,904, `kcBexIQ70ok`) |
| turning your heat down | year | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,076, `mP0IjyvQtxw`) |
| turning your heat down | month | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (The DIY HVAC Guy, 1,203,076, `mP0IjyvQtxw`) |
| thermostat habits | relevance | "The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,505, `K2jCz3D5z_0`) |
| thermostat habits | views | "How to (actually) shift your identity (to Succeed) \| Psycho-Cybernetics by Maxwell Maltz" (Dan Zakaria, 1,159,467, `sTwZKzNE0qE`) |
| thermostat habits | year | "How to (actually) shift your identity (to Succeed) \| Psycho-Cybernetics by Maxwell Maltz" (Dan Zakaria, 1,159,467, `sTwZKzNE0qE`) |
| thermostat habits | month | "The 5 Thermostat Habits That Wear Out Your Furnace Years Early" (John The HVAC Guy and 9 more, 2,138, `uJiPTsBGPY4`) |
| nest thermostat vs ecobee | relevance | "Nest vs Ecobee! The BEST Smart Thermostat is…" (Smart Home Solver, 495,916, `Xa-jrrBnNSw`) |
| nest thermostat vs ecobee | views | "Fix Nest Thermostat C-Wire Issues Without Adding a C-Wire" (Tech With Brett, 748,856, `tgAiEBqUXIk`) |
| nest thermostat vs ecobee | year | "Apple’s Adaptive Temperature Made Me Replace My Ecobee (Aqara W200 Smart Thermostat)" (Shane Whatley, 308,053, `RliA3Isv40U`) |
| nest thermostat vs ecobee | month | "Best Smart Thermostats 2026 \| 5 Top Picks Compared" (The Home Gear, 486, `eB5MWt5cNl4`) |
| smart thermostat save money | relevance | "Nest vs Ecobee! The BEST Smart Thermostat is…" (Smart Home Solver, 495,916, `Xa-jrrBnNSw`) |
| smart thermostat save money | views | "How to Balance Your Radiators \| Save Money and Increase Heat" (The DIY Guy, 2,059,737, `7NsZ2d2Oups`) |
| smart thermostat save money | year | "The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,505, `K2jCz3D5z_0`) |
| smart thermostat save money | month | "9 TIPS TO SAVE £££ ON YOUR ENERGY BILLS THIS WINTER!" (DanEVSolar, 1,836, `WqlJ6zY-c14`) |
| thermostat save money | relevance | "Smart Thermostats: what I WISH I knew earlier…" (Smart Home Solver, 346,205, `S6rI1Sbasrw`) |
| thermostat save money | views | "How to Balance Your Radiators \| Save Money and Increase Heat" (The DIY Guy, 2,059,737, `7NsZ2d2Oups`) |
| thermostat save money | year | "The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,507, `K2jCz3D5z_0`) |
| thermostat save money | month | "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" (Ray Dutton's Garage, 201,121, `H0MBgMMzmyg`) |
| what temperature should you set your thermostat | relevance | "What Is The Best Temperature To Set Your Air Conditioning?" (Efficient AC, Electric & Plumbing, 292,884, `M6QeNWNDR8M`) |
| what temperature should you set your thermostat | views | "How to install the Google Nest Learning Thermostat" (Google Nest, 8,009,347, `dHKD-9uI24I`) |
| what temperature should you set your thermostat | year | "The 5 Thermostat Habits That Wear Out Your AC Years Early" (Ray Dutton's Garage, 1,127,507, `K2jCz3D5z_0`) |
| what temperature should you set your thermostat | month | "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" (Ray Dutton's Garage, 201,121, `H0MBgMMzmyg`) |
| thermal curtains | relevance | "I Tested Window Film, Bubble Wrap & Thermal Curtains — Not Even Close" (Ivan’s Survival Journal and 3 more, 243,350, `e1f_psQ1zBs`) |
| thermal curtains | views | "10 Curtain Mistakes That Make Your Home Look Cheap (How to Fix Them!)" (Cozy DIY Home, 1,288,235, `T9nKVV4-wTQ`) |
| thermal curtains | year | "Why Don't More People Insulate Windows Like This?" (Fix This Build That, 811,942, `1jJILdeZ1jg`) |
| thermal curtains | month | "I Tested Window Film, Bubble Wrap & Thermal Curtains — Not Even Close" (Ivan’s Survival Journal and 3 more, 243,350, `e1f_psQ1zBs`) |
| window film | relevance | "How To: Properly Apply Window Tint" (O'Reilly Auto Parts, 1,391,630, `B5KscTSk_5E`) |
| window film | views | "Mindo Taseeldarni (Punjabi Movie) Karamjit Anmol \| Kavita Kaushik \| Harby Sangha \| Malkeet Rauni" (R R Records, 70,896,838, `aYF5x3fRpqk`) |
| window film | year | "BINDU - बिंदू I ANJANA SINGH, JAY YADAV I BHOJPURI SUPERHIT FULL MOVIE" (BTS Bhojpuri Movies, 2,713,135, `n2Kp2bBxqwA`) |
| window film | month | "Mazda CX50 Ceramic Window Tint" (Tint Studio, 543,213, `JY-xRWdxj9c`) |
| pellet stove | relevance | "Everyone will be buying pellet stoves after learning this news" (Silver Cymbal, 1,403,139, `9d9TL02idO4`) |
| pellet stove | views | "How To Make Homemade Manual Feed Pellet Machine Without Welding \| Simple Diy Feed Pellet Machine" (Diamleon Diy Builds, 4,749,265, `narp5klugCo`) |
| pellet stove | year | "I Burned Wood Pellets in My Fireplace.. You Won't BELIEVE What Happened!" (Ryan’s Fireplace Diaries, 934,102, `i64diJdemfM`) |
| pellet stove | month | "20 Heating Sources That Don't Need Electricity in uk (Stockpile NOW)" (Christopher Johnson, 206,775, `yCgv4IA6W0s`) |
| wood stove | relevance | "How to build a smokeless wood stove with an oven on another level" (Creative Project, 18,879,806, `giF2ohDJ7NQ`) |
| wood stove | views | "Outdoor wood stove from red brick and cement" (Creative Cement, 38,516,965, `EElfn2tYqmA`) |
| wood stove | year | "Camping in Heavy Snow with My Dog . 3-Room Inflatable Tent . Wood Stove ASMR" (RYUCAMP, 8,744,105, `SGRKm8FXcDw`) |
| wood stove | month | "Winter Is Coming — I’m Starting to Build a STOVE for My Log Cabin" (Bjorn Brenton, 1,193,994, `pcwYevp32xs`) |
| wood stove mistakes | relevance | "These WOODSTOVE MISTAKES Are Costing You Time & Money!" (Jill Winger - Old Fashioned on Purpose, 1,510,442, `sUeQpQCY2Zo`) |
| wood stove mistakes | views | "7 FATAL Wiring Mistakes Most DIYers Don't Know They Are Making \| Most Are Guilty of 3" (How To Home, 12,129,104, `-jeP1d8PC1I`) |
| wood stove mistakes | year | "What They Don't Tell You About Tiny Wood Stoves" (Wilson Forest Lands, 702,671, `L7X-xAX-Jss`) |
| wood stove mistakes | month | "Is Your Woodpile Disappearing Too Fast? 7 Mistakes to Avoid" (Mémoire de Survie, 152,518, `kZp4jJ3NY1E`) |

## Channel tally

**25,618 unique long-form English videos** from **13,708 channels**. **13,466 channels are NEW**: neither their channel ID nor their handle appears anywhere in `seeds/channel-finds-round1.md`, `seeds/leads-channels.md` or `seeds/known-channels-recheck.md` (a channel those files mention, even as a lead or a rejected candidate, counts as known). Of the top 100 below, 48 are NEW. Full list: `data/raw/sweep-channels-2026-10-24.csv`.

Videos = distinct long-form English videos the sweep returned from the channel (all keywords, all sorts); total views = the sum of those videos' views. This measures how often the channel turns up in these searches, not its size. Many are off-niche channels that a broad keyword pulled in (reading).

Most NEW channels are off-niche (one stray video). A rough cut on the HVAC-word title rule (see `formats.md`): **811 NEW channels have 3 or more returned videos with a home-HVAC word in the title, 281 have 5 or more.** These are the ones worth a round 3 look (reading).

| # | Channel | Handle | Videos | HVAC-word videos | Total views | Median views | Last 12 mo | Topics | Biggest returned video (title, views, ID) | NEW |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | AC Service Tech LLC | @acservicetechchannel | 239 | 214 | 77,120,402 | 184,360 | 10 | 29 | "Electric Expansion Valve (EEV) Operation and Testing! HVAC Metering Device Training!" (2,562,093, `LzvVjvUpOVM`) |  |
| 2 | HVAC School | @HVACS | 166 | 99 | 24,429,647 | 58,962 | 22 | 22 | "Refrigeration Cycle 101" (987,403, `VJX0LyxRV0E`) |  |
| 3 | The DIY HVAC Guy | @diyhvacguy | 162 | 136 | 83,326,393 | 208,678 | 34 | 31 | "Keep Your Family Warm During A Power Outage By Installing This $5 Part" (4,275,377, `y07w1hiKIrI`) |  |
| 4 | This Old House | @thisoldhouse | 154 | 92 | 106,543,457 | 345,634 | 26 | 31 | "How to Install a Ductless Mini-Split Air Conditioner \| This Old House" (5,271,262, `ozaw9QhxkQU`) |  |
| 5 | Taddy Digest | @taddydigest | 149 | 138 | 11,336,346 | 37,341 | 20 | 28 | "Gas Furnace Turning Off? Here's What Might Be Happening" (538,837, `zHNYVt9oQ1Y`) |  |
| 6 | steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | @stevenlavimoniere | 145 | 134 | 6,613,699 | 21,092 | 38 | 21 | "HVAC HACK SCAM IN MY AREA TAKING ADVANTAGE OF OLDER COUPLE EXPOSED" (336,618, `hxnfRiq23Zg`) |  |
| 7 | Word of Advice TV | @WordofAdviceTV | 137 | 120 | 89,938,681 | 432,575 | 2 | 31 | "AC Not Turning on or Working? Try THESE Fixes (Works on Most Units)" (3,642,848, `wzAA4dlp_70`) |  |
| 8 | HVAC Guide for Homeowners | @NewHVACGuide | 126 | 121 | 9,981,694 | 27,345 | 6 | 25 | "5 BIGGEST Winter HVAC Mistakes Homeowners Don't Know!" (981,366, `Unx9Ze10N98`) |  |
| 9 | HVAC GUY | @HVACGUY | 126 | 92 | 4,622,698 | 18,828 | 60 | 23 | "Source Of Really High Humidity Found, And It's Not What You Might Expect!" (454,372, `bYy4nY79yDI`) |  |
| 10 | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | @PipeDoctor | 102 | 92 | 3,808,487 | 21,623 | 43 | 20 | "How to Properly Perform Annual Service and Maintenance on a Central AC System" (458,748, `sJiRT_tNOQk`) |  |
| 11 | TRQ | @TRQ | 78 | 11 | 5,244,806 | 45,694 | 12 | 11 | "How to Replace Blower Motor 2012-2020 Ford Focus" (288,284, `dvPf2n3A-OU`) | NEW |
| 12 | Matt Risinger | @buildshow | 77 | 52 | 34,812,508 | 331,205 | 9 | 17 | "10 DUMB (and Common) Building Practices" (2,383,883, `LuUxUt6MwIU`) |  |
| 13 | Quality HVACR | @QualityHVACR | 66 | 59 | 8,243,486 | 87,538 | 6 | 18 | "#1 Reason Why DUCTLESS Units Fail \| How I Fix It..." (1,004,154, `QjTXu1pMlGA`) |  |
| 14 | Skill Builder | @SkillBuilder | 58 | 51 | 22,943,167 | 214,068 | 9 | 21 | "The Spray Foam Insulation Problem Nobody's Talking About" (3,022,192, `jYNufQVIFfA`) |  |
| 15 | The Engineering Mindset | @EngineeringMindset | 52 | 37 | 73,512,790 | 709,286 | 0 | 20 | "Capacitors Explained - The basics how capacitors work working principle" (11,078,060, `X4EUwTwZ110`) |  |
| 16 | Jumper man Tech | @JumpermanTech | 52 | 47 | 4,976,378 | 37,034 | 14 | 20 | "How To Braze Copper Pipe Like A Pro (HVAC Refrigerant Lines)" (1,415,706, `dfXQV3m63ag`) |  |
| 17 | Jersey Mike HVAC | @JerseyMikeHVAC | 52 | 41 | 3,998,864 | 52,034 | 3 | 12 | "HVAC Low voltage control wiring (Basics For Beginners)" (352,131, `qTqlr8y7USo`) |  |
| 18 | Boiler Room | @boilerroom | 51 | 0 | 436,945,123 | 2,633,462 | 16 | 3 | "Solomun \| Boiler Room: Tulum" (77,228,502, `bk6Xst6euQk`) | NEW |
| 19 | Nighthawk HVAC | @NighthawkHVAC | 51 | 42 | 794,192 | 5,429 | 18 | 15 | "Flame Rollout!!! Finding the Cause! EP44" (139,113, `fWC2smK9hvg`) | NEW |
| 20 | The Thought Provocateur | @thethoughtprovocateur | 50 | 44 | 3,403,962 | 39,452 | 2 | 18 | "Ductless Mini Split In 2026 \| What you should know" (382,084, `lSqN4VuteVc`) |  |
| 21 | Tool Junkie | @Tooljunkie4you | 50 | 43 | 548,209 | 5,644 | 22 | 19 | "3 Blade Vs 5 Blade Ceiling Fan: Key Differences" (64,840, `JMFpfyFoyIQ`) | NEW |
| 22 | Crawl Space Ninja | @CrawlSpaceNinja | 49 | 45 | 3,702,834 | 35,212 | 10 | 10 | "Attic Insulation Done Wrong? Here's What Goes Wrong" (436,095, `ao8KnAgTbfo`) |  |
| 23 | Love2HVAC with Ty Branaman | @love2hvac | 49 | 44 | 2,727,698 | 36,990 | 0 | 13 | "Saturation, Superheat,  Subcooling" (228,621, `nwPA56cXqMA`) | NEW |
| 24 | Fox Family Heating and Air Conditioning | @foxfamilyhvac | 48 | 46 | 6,504,385 | 79,282 | 0 | 19 | "How to Diagnose a Bad Compressor on your Air Conditioner" (506,139, `raG_N_hz6ng`) |  |
| 25 | grayfurnaceman | @grayfurnaceman | 45 | 37 | 11,587,475 | 111,618 | 0 | 19 | "Diagnosing pressure switch problems on gas furnaces" (1,157,867, `QLpxsquyx1k`) |  |
| 26 | MEP Academy | @MEPAcademy | 45 | 36 | 4,004,375 | 15,798 | 7 | 21 | "How Data Centers Actually Work" (1,543,660, `cTwvUqLNQrM`) | NEW |
| 27 | 1A Auto: Repair Tips & Secrets Only Mechanics Know | @1AAuto | 43 | 6 | 16,586,163 | 179,453 | 1 | 16 | "Heat Stopped Working In My Car! Blower Motor or Resistor?" (2,937,428, `lupH6PY8-DM`) | NEW |
| 28 | Air Conditioner Lab | @AirConditionerLab | 43 | 42 | 2,003,077 | 26,759 | 7 | 16 | "7 Fans That Cool Like Air Conditioners - Relief From The Heat!" (284,684, `T4S8CHfYBUs`) |  |
| 29 | Heat Geek | @HeatGeek | 41 | 37 | 3,877,411 | 44,386 | 11 | 14 | "Is It Better To Leave The Heating On Constantly? Boilers & Heat Pumps \| Consumer Advice" (922,523, `kGs_biFA87Q`) |  |
| 30 | Soundproof Guide | @soundproofguide | 39 | 9 | 12,549,213 | 111,143 | 10 | 7 | "CHEAPEST Budget way For SOUNDPROOFING a Room" (4,767,265, `h_oIgdWjqmE`) | NEW |
| 31 | One Hour Smart Home | @OneHourSmartHome | 39 | 32 | 8,340,835 | 140,777 | 0 | 5 | "How To Use Nest Thermostat [The Missing Manual]" (779,393, `rdfUbAZi7k0`) |  |
| 32 | ASIRI Designs | @ASIRIDesigns | 39 | 30 | 5,914,700 | 100,579 | 10 | 5 | "The Ugly Truth About Basement Vapor Barriers" (821,063, `QnFoiUXr4h4`) |  |
| 33 | How To Home | @HowToHomeDIY | 38 | 26 | 57,801,399 | 825,355 | 9 | 25 | "7 FATAL Wiring Mistakes Most DIYers Don't Know They Are Making \| Most Are Guilty of 3" (12,129,104, `-jeP1d8PC1I`) |  |
| 34 | Homey Vibe | @homeyvibe1 | 38 | 38 | 242,542 | 2,263 | 30 | 15 | "Propane Vs Kerosene Heater: What’s Safer & Cheaper?" (53,262, `RkUdySAh_mo`) | NEW |
| 35 | Silver Cymbal | @SilverCymbal | 37 | 29 | 43,786,213 | 528,273 | 4 | 28 | "92% of Homeowners Use Teflon Pipe Tape Wrong - Here's Why it Leaks" (8,083,301, `EkuLHpYz02Y`) |  |
| 36 | Home RenoVision DIY | @HomeRenoVisionDIY | 37 | 15 | 35,441,700 | 658,225 | 4 | 18 | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (5,826,898, `J95l9Ue4224`) |  |
| 37 | GAMETIME HIGHLIGHTS | @TheGametimeHighlights | 37 | 1 | 12,151,611 | 113,485 | 33 | 2 | "LeBron James vs Stephen Curry NASTY Duel 2014.02.12 Heat at GSW - Game Winner For James!" (3,205,708, `m_Ikt0lJA5s`) | NEW |
| 38 | Benjamin Sahlstrom | @BenjaminSahlstrom | 36 | 29 | 15,818,460 | 179,084 | 0 | 20 | "How To Make an R410A Flare for a Mini Split AC Unit Installation" (2,384,118, `itoro65YpZM`) |  |
| 39 | HVAC OFFICIAL CHANNEL | @HVACOFFICIALCHANNEL | 36 | 29 | 272,214 | 685 | 33 | 12 | "HVAC Full Course \| Complete Guide for Beginners \| Learn AC & Chiller Systems Easily" (201,389, `WH7GiDVmNRc`) | NEW |
| 40 | plumberparts | @plumberparts | 35 | 27 | 14,976,326 | 238,710 | 1 | 13 | "How to Fix One Radiator Not Working - Plumbing Tips" (2,479,360, `wqku_Rc_YuI`) |  |
| 41 | HVAC Know It All | @HVACKnowItAll | 35 | 31 | 520,762 | 646 | 18 | 10 | "How To Read Wiring Diagrams For HVAC" (90,895, `41vjaZoqwWI`) |  |
| 42 | Everyday Home Repairs | @EverydayHomeRepairs | 34 | 26 | 31,034,420 | 530,794 | 0 | 27 | "How To Fix A Sunken Sidewalk With Spray Foam" (5,193,652, `AL1Xrd8IScY`) |  |
| 43 | Forever Tech English | @forevertechenglish | 34 | 26 | 7,036,421 | 46,522 | 5 | 15 | "Cleaning Extremely Dirty AC With Pressure Washer!" (2,509,292, `DzhAHKicOFI`) | NEW |
| 44 | HVACR VIDEOS | @HVACRVIDEOS | 33 | 8 | 2,631,045 | 46,453 | 18 | 10 | "THEY SAID PLEASE HURRY THE AC'S ARE NOT WORKING" (467,198, `JFgdlDQnYdA`) | NEW |
| 45 | HVACR Survival | @HVACRSurvival | 33 | 20 | 1,469,783 | 20,218 | 11 | 12 | "HEAT PUMP FROZEN UP LIKE A ICE MACHINE I MISSED  UP & TOASTED THE FUSE" (301,711, `Y3z-yiQj64Y`) |  |
| 46 | Ray Dutton's Garage | @RayDuttonsGarage | 32 | 31 | 6,000,301 | 19,198 | 32 | 23 | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" (1,212,971, `dOZ-8__G4uU`) |  |
| 47 | OnemanHVAC | @Onemanhvac | 32 | 30 | 241,398 | 4,433 | 21 | 10 | "My HVAC Tuesday 5 no heat calls #hvaccontractor #hvac #bluecollar " (46,657, `pzK6HbsHoG8`) | NEW |
| 48 | Linus Tech Tips | @LinusTechTips | 31 | 8 | 89,620,486 | 2,746,172 | 5 | 14 | "Why you shouldn't water cool your PC" (9,620,561, `23vjWtUpItk`) |  |
| 49 | Ewok | @ewokdoeshvac | 31 | 30 | 2,565,570 | 29,379 | 20 | 11 | "Day in the Life of an 19 Year Old HVAC Technician" (833,701, `2pyime545l4`) | NEW |
| 50 | Yarbrough & Sons Heating, Cooling & Plumbing | @yarbrough_and_sons | 30 | 26 | 827,825 | 4,256 | 22 | 19 | "Ranking the Best and Worst Air Conditioner Brands" (308,481, `1fu7qtmaJN4`) |  |
| 51 | Mark Ballard LTD, Professional Heating Engineer | @MarkBallardLTDHeatingEngineer | 29 | 24 | 3,911,982 | 63,583 | 0 | 7 | "Replace a Leaking Radiator Valve with Out Draining the System. Professional Step by Step Guide" (1,102,292, `mjsPZirB9Cg`) | NEW |
| 52 | The Air Of Authority | @TheAirOfAuthority | 29 | 26 | 3,034,760 | 65,884 | 0 | 18 | "What to do when air conditioner freezes up: Air conditioner tips for summer" (701,872, `2nph6MNJK-Q`) |  |
| 53 | Undecided with Matt Ferrell | @UndecidedTechnology | 28 | 20 | 35,607,951 | 1,118,850 | 5 | 19 | "Is Geothermal Heating and Cooling Worth the Cost?  Heat Pumps Explained" (3,682,327, `PI45yUhUWgk`) |  |
| 54 | Vineet Malhotra | @VMone | 28 | 7 | 15,641,779 | 304,736 | 25 | 11 | "Panasonic AC 1.5 Ton 5 Star \| Best 1.5 Ton 5 Star AC \| Best AC 2026" (3,243,403, `a93CLRfZSj4`) | NEW |
| 55 | Atlas AC | @atlasacrepair | 28 | 23 | 6,042,879 | 122,170 | 5 | 21 | "STOP Buying the WRONG Air Conditioner Brands" (1,873,918, `r_uP9itJ0HQ`) |  |
| 56 | Pioneer HVAC Controls | @PioneerHVACControls | 28 | 27 | 1,899,269 | 32,684 | 14 | 11 | "The Refrigeration Cycle (SIMPLIFIED) - HVAC Training" (300,183, `ZYLPQJxNOhE`) |  |
| 57 | Adrian Garcia | @ReliableHVACR | 28 | 15 | 512,507 | 8,920 | 9 | 5 | "Comparing & Testing Several Valve Core Removal Tools" (68,210, `V4erA0mi-BU`) | NEW |
| 58 | Fix This House | @FixThisHouse | 27 | 16 | 16,674,848 | 351,792 | 8 | 26 | "How To Replace And Install A Bathroom Exhaust Fan To A Quiet Motion Sensor Exhaust Fan! DIY Tutorial" (3,262,106, `NzjmnIv89Ls`) |  |
| 59 | MythBusters | @Mythbusterstvshow | 27 | 3 | 7,816,397 | 179,869 | 15 | 7 | "Can A Sailboat Really Push Itself Forward With Its Own Fan? \| MythBusters" (1,282,022, `vVlsKdQ-o3I`) | NEW |
| 60 | HouseFresh | @HouseFresh | 27 | 19 | 1,725,964 | 36,584 | 9 | 5 | "Don’t Buy a Dehumidifier Before Watching This → The Best Dehumidifiers We Tested" (356,284, `DfbRZXJSQ2I`) | NEW |
| 61 | WW HVAC | @WWHVAC | 27 | 23 | 656,893 | 8,415 | 13 | 15 | "Why Your AC Can't Hit 70° When It's 110° Outside" (166,162, `m_e6DRJY9UQ`) | NEW |
| 62 | NBA | @NBA | 26 | 10 | 58,349,079 | 283,230 | 9 | 1 | "Warriors vs Cavaliers: Game 7 NBA Finals - 06.19.16 Full Highlights" (27,389,508, `Mxv5h-RZWVs`) | NEW |
| 63 | Project Farm | @ProjectFarm | 26 | 8 | 48,131,214 | 1,630,386 | 10 | 22 | "Best Water Filter? Brita, ZeroWater, PUR, Berkey, Aquaphor, AquaTrue" (4,374,897, `ja0ioX6GSz0`) |  |
| 64 | The Fixer | @TheFixerHomeRepair | 26 | 22 | 19,866,127 | 200,816 | 4 | 15 | "Midea 8,000 BTU U Smart Inverter Window AC Installation and Review" (7,070,864, `hux4BEKiu6k`) |  |
| 65 | Embers Fireplaces & Outdoor Living | @embersliving | 26 | 24 | 5,125,837 | 159,230 | 3 | 6 | "Wood vs Pellet Stove: What’s Best for Heating in 2026?" (609,143, `i13br5bdF0A`) | NEW |
| 66 | The HVAC Hacker | @thehvachacker | 26 | 25 | 1,722,165 | 46,720 | 0 | 13 | "Replacing Evaporator HVAC Repair" (366,061, `Sic_93G7UrI`) | NEW |
| 67 | Technology Connections | @TechnologyConnections | 25 | 19 | 78,632,022 | 2,616,485 | 3 | 26 | "Portable Air Conditioners - Why you shouldn't like them" (10,388,788, `_-mBeYC2KGc`) |  |
| 68 | Allen Hart | @AllenHart999 | 25 | 17 | 6,255,827 | 99,262 | 0 | 7 | "How To Bleed A Radiator - Don’t try it until you watch this" (2,404,207, `tbLz8icLr2U`) | NEW |
| 69 | Home Performance | @HomePerformance | 25 | 22 | 2,637,082 | 30,257 | 3 | 13 | "Ductless Mini-Split: How to Take Apart & Clean DIY (Mitsubishi M-Series High Wall Unit)" (494,948, `2e6by0tV8h4`) |  |
| 70 | Apartment Maintenance Pro | @ApartmentMaintenancePro | 25 | 21 | 1,140,341 | 17,492 | 8 | 17 | "Nest Learning Thermostat Install (3rd Generation)" (294,646, `howVw9iAyPY`) | NEW |
| 71 | HVACR Training Membership | @HVACRMembership | 25 | 23 | 284,056 | 8,344 | 5 | 8 | "E4 Error Code in Air Conditioners: What It Means, Common Causes & Easy Fix!" (40,196, `nAbv55gdN5I`) | NEW |
| 72 | Relaxing White Noise | @RelaxingWhiteNoise | 24 | 3 | 645,471,506 | 2,823,284 | 0 | 11 | "White Noise Black Screen \| Sleep, Study, Focus \| 10 Hours" (384,357,623, `nMfPqeZjc2c`) | NEW |
| 73 | Talyn875 | @TALYN875 | 24 | 22 | 1,161,096 | 19,276 | 0 | 11 | "HVAC Training \| Dual Run Capacitor Wiring" (591,303, `yuINo7CWFaE`) | NEW |
| 74 | Hvac Budget | @hvacbudget8600 | 24 | 2 | 664,334 | 12,138 | 21 | 1 | "This Multitool Destroys Leatherman!" (307,881, `i4oIfHkbNKE`) | NEW |
| 75 | dereton33 Plumbing and heating, DIY and blogging. | @dereton33 | 23 | 17 | 3,518,809 | 44,039 | 1 | 7 | "How to cure damp in the bedroom." (781,840, `St3z3DW6N6w`) | NEW |
| 76 | HVACTIME | @HVACTIME | 23 | 16 | 1,322,699 | 32,454 | 0 | 7 | "YK Overview Centrifugal Chiller York HVAC Training" (259,056, `flAMZUK3f18`) | NEW |
| 77 | Jeff’s HVAC Adventures | @JeffsHVACAdventures | 23 | 21 | 494,727 | 11,443 | 3 | 16 | "Quick Oil Boiler Service! Nozzle and Filter Change!" (114,625, `BQsSICx5H6g`) | NEW |
| 78 | HVACmillionaire | @hvacmillionaire | 23 | 23 | 287,236 | 700 | 11 | 8 | "HVAC beginner: Wiring a basic heat pump system" (196,026, `C-VyY1fkc7k`) | NEW |
| 79 | Electro Demolish | @ElectroDemolish | 22 | 17 | 35,711,190 | 787,514 | 1 | 1 | "🇮🇳 Happy Independence Day Special \| 3 Ceiling Fans Combined \| Ultimate Wobble & Final Drop Test 🔥😱 ⭐" (9,170,051, `voOYrD1p4rE`) | NEW |
| 80 | Anti DIY HVAC | @TedCookHVAC | 22 | 21 | 1,814,019 | 47,511 | 7 | 11 | "HVAC Scam Rip Off told customer furnace heat exchanger cracked" (333,510, `ouyl5Yp0zQg`) |  |
| 81 | LRN2DIY | @LRN2DIY | 21 | 13 | 32,499,177 | 910,745 | 3 | 23 | "It's Been a Good Run, Drywall." (6,423,113, `uHGHeTzznhM`) |  |
| 82 | emm vlogs | @emmvlogs | 21 | 10 | 19,629,194 | 39,779 | 11 | 9 | "Using ceiling Fan while using Air Conditioner Explained \| Benefits to Using AC with ceiling Fan" (7,544,999, `4qs6Sk8JbJE`) | NEW |
| 83 | The Organic Chemistry Tutor | @TheOrganicChemistryTutor | 21 | 4 | 12,812,932 | 374,203 | 0 | 6 | "Specific Heat Capacity Problems & Calculations - Chemistry Tutorial - Calorimetry" (1,595,353, `ePm_N6RgLfk`) | NEW |
| 84 | Roger Wakefield Plumbing Education | @RogerWakefield | 21 | 4 | 5,944,712 | 93,709 | 1 | 7 | "A NEW & FUN Way to Flush a Water Heater" (1,365,613, `2ikQ6Zuh7LA`) | NEW |
| 85 | FCP Euro | @fcpeuro | 21 | 7 | 1,714,606 | 36,420 | 8 | 3 | "BMW N54 Water Pump and Thermostat - DIY, Symptoms, Tips, and Self Bleeding Procedure" (353,050, `g8qozaA0PJU`) | NEW |
| 86 | Fire & Ice Home Services | @fireiceheatingandaircondit4363 | 21 | 20 | 1,600,311 | 25,353 | 0 | 15 | "Our Duct Cleaning Process from Start to Finish" (344,713, `L8yojsdz8EA`) | NEW |
| 87 | Zach of All Trades | @zachofallskilledtrades | 21 | 11 | 803,986 | 13,806 | 10 | 3 | "5 Best and Worst Trade Jobs" (253,684, `kL_KZtQEK3U`) | NEW |
| 88 | Exposi | @Exposerosi34 | 21 | 18 | 362,671 | 2,464 | 21 | 12 | "This SECRET AC Trick is Only Known by 1% of HVAC Technicians (USE THEM NOW)" (197,213, `F0ENEEqAyaE`) |  |
| 89 | Home Caprice | @homecapricehc | 20 | 18 | 1,799,676 | 25,038 | 3 | 13 | "Dry Mode in Air Conditioners Explained [Quick Overview]" (793,178, `ANcISCxrvTQ`) |  |
| 90 | HVAC Training 101 | @HVACTraining101 | 20 | 19 | 947,907 | 31,432 | 0 | 11 | "How To Clean Window AC Unit Without Removing 🌬️  \| HVAC Training 101" (132,981, `GI6TBdRus_8`) | NEW |
| 91 | Koolin’ with Krauss  | @KoolinwithKrauss | 20 | 17 | 537,725 | 12,079 | 8 | 12 | "Failed Honeywell Damper motor \| no AIR in bedroom \| HVAC" (122,476, `8T2co-Qughw`) |  |
| 92 | HVAC Greatness by Pete Ramsey | @HVACPete | 20 | 19 | 129,287 | 2,160 | 2 | 5 | "Make $1 Million as a ONE-MAN HVAC Business Owner/Operator" (26,665, `YHP8Xw_zZjU`) | NEW |
| 93 | My HVAC Life | @MYHVACLIFE | 20 | 15 | 83,404 | 3,132 | 9 | 13 | "RHEEM Heat pump on high pressure switch lock out." (18,243, `Qr0tpmRTgwI`) | NEW |
| 94 | HVAC Overtime | @HVACOvertime | 20 | 18 | 34,621 | 1,084 | 9 | 1 | "HVAC Overtime, where are they now?" (14,561, `7Cwyw3uDrMQ`) | NEW |
| 95 | Randall's Relaxation | @RandallsRestRelaxation | 19 | 4 | 23,981,115 | 539,562 | 1 | 9 | "FAN NOISE of 12 FANS for 12 HOURS = BOX FANS WHITE NOISE FOR SLEEPING" (5,400,633, `eixPkJo-cx4`) | NEW |
| 96 | Tint Studio | @DetroitTintStudio | 19 | 4 | 12,753,405 | 342,377 | 11 | 1 | "Walmart Tint so DUMB it’s GENIUS!" (5,018,366, `7CGKeoQ8m0o`) | NEW |
| 97 | HVAC Exposed | @HVACExposed | 19 | 18 | 1,813,270 | 5,980 | 19 | 12 | "The Only 5 HVAC Brands Worth Buying (The Lifetime List)" (577,877, `QKPPm6M0__o`) |  |
| 98 | HVAC Technician Sales Secrets | @hvactechsecrets | 19 | 19 | 23,446 | 740 | 5 | 4 | "The Dark Side Of HVAC Sales And Tech Work - The Truth About HVAC Sales [1 of 2]" (5,422, `ZvZlIBDBbvw`) | NEW |
| 99 | ChrisFix | @chrisfix | 18 | 5 | 140,361,847 | 7,257,613 | 0 | 18 | "How to SUPER FLUSH your Cars Cooling System" (19,323,840, `s--5ft5YiHg`) |  |
| 100 | RepairClinic.com | @repairclinic | 18 | 14 | 4,612,759 | 114,320 | 0 | 12 | "How Does a Central Air Conditioner Work? — HVAC Repair Tips" (1,442,108, `uElUCGNb6SY`) |  |

### Top 50 NEW channels by videos returned

| # | Channel | Handle | channelId | Videos | HVAC-word videos | Total views | Last 12 mo | Biggest returned video (title, views, ID) |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | TRQ | @TRQ | `UCWCdsftsTqYMO7cA_5Sc-yA` | 78 | 11 | 5,244,806 | 12 | "How to Replace Blower Motor 2012-2020 Ford Focus" (288,284, `dvPf2n3A-OU`) |
| 2 | Boiler Room | @boilerroom | `UCGBpxWJr9FNOcFYA5GkKrMg` | 51 | 0 | 436,945,123 | 16 | "Solomun \| Boiler Room: Tulum" (77,228,502, `bk6Xst6euQk`) |
| 3 | Nighthawk HVAC | @NighthawkHVAC | `UC7fmaDG-Q4ZLKSCmIkgMVWA` | 51 | 42 | 794,192 | 18 | "Flame Rollout!!! Finding the Cause! EP44" (139,113, `fWC2smK9hvg`) |
| 4 | Tool Junkie | @Tooljunkie4you | `UCB78N_DpnGKKSuwBknTN9CA` | 50 | 43 | 548,209 | 22 | "3 Blade Vs 5 Blade Ceiling Fan: Key Differences" (64,840, `JMFpfyFoyIQ`) |
| 5 | Love2HVAC with Ty Branaman | @love2hvac | `UCIoD-SEdUWMA74tWXRMyCZQ` | 49 | 44 | 2,727,698 | 0 | "Saturation, Superheat,  Subcooling" (228,621, `nwPA56cXqMA`) |
| 6 | MEP Academy | @MEPAcademy | `UCmFkUrOFd_FaASmI9HysA3g` | 45 | 36 | 4,004,375 | 7 | "How Data Centers Actually Work" (1,543,660, `cTwvUqLNQrM`) |
| 7 | 1A Auto: Repair Tips & Secrets Only Mechanics Know | @1AAuto | `UCVvE8kQTuZEykvMFZBVzftg` | 43 | 6 | 16,586,163 | 1 | "Heat Stopped Working In My Car! Blower Motor or Resistor?" (2,937,428, `lupH6PY8-DM`) |
| 8 | Soundproof Guide | @soundproofguide | `UCML7DcvQrG9sUw5kGqAGtaA` | 39 | 9 | 12,549,213 | 10 | "CHEAPEST Budget way For SOUNDPROOFING a Room" (4,767,265, `h_oIgdWjqmE`) |
| 9 | Homey Vibe | @homeyvibe1 | `UCwJ0MSnM3_3OGuekYGI6bzw` | 38 | 38 | 242,542 | 30 | "Propane Vs Kerosene Heater: What’s Safer & Cheaper?" (53,262, `RkUdySAh_mo`) |
| 10 | GAMETIME HIGHLIGHTS | @TheGametimeHighlights | `UC0LrZO9wORIqn_aRJtKdgfA` | 37 | 1 | 12,151,611 | 33 | "LeBron James vs Stephen Curry NASTY Duel 2014.02.12 Heat at GSW - Game Winner For James!" (3,205,708, `m_Ikt0lJA5s`) |
| 11 | HVAC OFFICIAL CHANNEL | @HVACOFFICIALCHANNEL | `UCDUAuJEO5e7GcBAPnodUvrw` | 36 | 29 | 272,214 | 33 | "HVAC Full Course \| Complete Guide for Beginners \| Learn AC & Chiller Systems Easily" (201,389, `WH7GiDVmNRc`) |
| 12 | Forever Tech English | @forevertechenglish | `UCSIClXw_5lT1buMo2BM6q7g` | 34 | 26 | 7,036,421 | 5 | "Cleaning Extremely Dirty AC With Pressure Washer!" (2,509,292, `DzhAHKicOFI`) |
| 13 | HVACR VIDEOS | @HVACRVIDEOS | `UC5Pnrxqqg4BLTsfsUzWw5Pw` | 33 | 8 | 2,631,045 | 18 | "THEY SAID PLEASE HURRY THE AC'S ARE NOT WORKING" (467,198, `JFgdlDQnYdA`) |
| 14 | OnemanHVAC | @Onemanhvac | `UCCfVNgkRrgMzNPrb8nOKigA` | 32 | 30 | 241,398 | 21 | "My HVAC Tuesday 5 no heat calls #hvaccontractor #hvac #bluecollar " (46,657, `pzK6HbsHoG8`) |
| 15 | Ewok | @ewokdoeshvac | `UCME4xG68IQbZP0YgkPT_3FQ` | 31 | 30 | 2,565,570 | 20 | "Day in the Life of an 19 Year Old HVAC Technician" (833,701, `2pyime545l4`) |
| 16 | Mark Ballard LTD, Professional Heating Engineer | @MarkBallardLTDHeatingEngineer | `UCeSzwJbwcKgQ9iJAhcd7S4w` | 29 | 24 | 3,911,982 | 0 | "Replace a Leaking Radiator Valve with Out Draining the System. Professional Step by Step Guide" (1,102,292, `mjsPZirB9Cg`) |
| 17 | Vineet Malhotra | @VMone | `UCxi-3zNcvJzAFEClr9nrpNw` | 28 | 7 | 15,641,779 | 25 | "Panasonic AC 1.5 Ton 5 Star \| Best 1.5 Ton 5 Star AC \| Best AC 2026" (3,243,403, `a93CLRfZSj4`) |
| 18 | Adrian Garcia | @ReliableHVACR | `UCKDkGhLRlzs1bV1tmeokcNQ` | 28 | 15 | 512,507 | 9 | "Comparing & Testing Several Valve Core Removal Tools" (68,210, `V4erA0mi-BU`) |
| 19 | MythBusters | @Mythbusterstvshow | `UChUAaNhjdc1aN5f_29BPrhw` | 27 | 3 | 7,816,397 | 15 | "Can A Sailboat Really Push Itself Forward With Its Own Fan? \| MythBusters" (1,282,022, `vVlsKdQ-o3I`) |
| 20 | HouseFresh | @HouseFresh | `UCW5aDZyLh2s8hOE18uqqrWg` | 27 | 19 | 1,725,964 | 9 | "Don’t Buy a Dehumidifier Before Watching This → The Best Dehumidifiers We Tested" (356,284, `DfbRZXJSQ2I`) |
| 21 | WW HVAC | @WWHVAC | `UCX9qUeV57Z7gqX1uwp8XOqg` | 27 | 23 | 656,893 | 13 | "Why Your AC Can't Hit 70° When It's 110° Outside" (166,162, `m_e6DRJY9UQ`) |
| 22 | NBA | @NBA | `UCWJ2lWNubArHWmf3FIHbfcQ` | 26 | 10 | 58,349,079 | 9 | "Warriors vs Cavaliers: Game 7 NBA Finals - 06.19.16 Full Highlights" (27,389,508, `Mxv5h-RZWVs`) |
| 23 | Embers Fireplaces & Outdoor Living | @embersliving | `UC8dn-miD_eGaLHMhTdCSQBA` | 26 | 24 | 5,125,837 | 3 | "Wood vs Pellet Stove: What’s Best for Heating in 2026?" (609,143, `i13br5bdF0A`) |
| 24 | The HVAC Hacker | @thehvachacker | `UCNOsm1Xq_tdrBXWyYGSSg6g` | 26 | 25 | 1,722,165 | 0 | "Replacing Evaporator HVAC Repair" (366,061, `Sic_93G7UrI`) |
| 25 | Allen Hart | @AllenHart999 | `UCCEkrdkurnRF-gNh0h_61HA` | 25 | 17 | 6,255,827 | 0 | "How To Bleed A Radiator - Don’t try it until you watch this" (2,404,207, `tbLz8icLr2U`) |
| 26 | Apartment Maintenance Pro | @ApartmentMaintenancePro | `UC6Ko62-E2iMcdJ48tBvLjUQ` | 25 | 21 | 1,140,341 | 8 | "Nest Learning Thermostat Install (3rd Generation)" (294,646, `howVw9iAyPY`) |
| 27 | HVACR Training Membership | @HVACRMembership | `UC6CeEomD0vavKtCwOyjcHIw` | 25 | 23 | 284,056 | 5 | "E4 Error Code in Air Conditioners: What It Means, Common Causes & Easy Fix!" (40,196, `nAbv55gdN5I`) |
| 28 | Relaxing White Noise | @RelaxingWhiteNoise | `UCbunYN0o9Yaid7zHaor_UHA` | 24 | 3 | 645,471,506 | 0 | "White Noise Black Screen \| Sleep, Study, Focus \| 10 Hours" (384,357,623, `nMfPqeZjc2c`) |
| 29 | Talyn875 | @TALYN875 | `UChqTAS8GVF1TM3pFyxvnPxg` | 24 | 22 | 1,161,096 | 0 | "HVAC Training \| Dual Run Capacitor Wiring" (591,303, `yuINo7CWFaE`) |
| 30 | Hvac Budget | @hvacbudget8600 | `UCbeg0eKEEf6L8lVWgz6Ddgw` | 24 | 2 | 664,334 | 21 | "This Multitool Destroys Leatherman!" (307,881, `i4oIfHkbNKE`) |
| 31 | dereton33 Plumbing and heating, DIY and blogging. | @dereton33 | `UCuDuSCyS4B1-KpEqllfYr0w` | 23 | 17 | 3,518,809 | 1 | "How to cure damp in the bedroom." (781,840, `St3z3DW6N6w`) |
| 32 | HVACTIME | @HVACTIME | `UCRdNcv3g_4rpbNEyFopZwDg` | 23 | 16 | 1,322,699 | 0 | "YK Overview Centrifugal Chiller York HVAC Training" (259,056, `flAMZUK3f18`) |
| 33 | Jeff’s HVAC Adventures | @JeffsHVACAdventures | `UCsVYxwEvQIlB6b0MDDi7dpw` | 23 | 21 | 494,727 | 3 | "Quick Oil Boiler Service! Nozzle and Filter Change!" (114,625, `BQsSICx5H6g`) |
| 34 | HVACmillionaire | @hvacmillionaire | `UCvqYNMZq4c2sTztlX7ZqeNg` | 23 | 23 | 287,236 | 11 | "HVAC beginner: Wiring a basic heat pump system" (196,026, `C-VyY1fkc7k`) |
| 35 | Electro Demolish | @ElectroDemolish | `UCgfeKYGaAMAgaITBNGQ18sA` | 22 | 17 | 35,711,190 | 1 | "🇮🇳 Happy Independence Day Special \| 3 Ceiling Fans Combined \| Ultimate Wobble & Final Drop Test 🔥😱 ⭐" (9,170,051, `voOYrD1p4rE`) |
| 36 | emm vlogs | @emmvlogs | `UCAlBwBSu9hrj1zULNahm4zg` | 21 | 10 | 19,629,194 | 11 | "Using ceiling Fan while using Air Conditioner Explained \| Benefits to Using AC with ceiling Fan" (7,544,999, `4qs6Sk8JbJE`) |
| 37 | The Organic Chemistry Tutor | @TheOrganicChemistryTutor | `UCEWpbFLzoYGPfuWUMFPSaoA` | 21 | 4 | 12,812,932 | 0 | "Specific Heat Capacity Problems & Calculations - Chemistry Tutorial - Calorimetry" (1,595,353, `ePm_N6RgLfk`) |
| 38 | Roger Wakefield Plumbing Education | @RogerWakefield | `UCGIMKh92vaL0_Yc0u4GYhHA` | 21 | 4 | 5,944,712 | 1 | "A NEW & FUN Way to Flush a Water Heater" (1,365,613, `2ikQ6Zuh7LA`) |
| 39 | FCP Euro | @fcpeuro | `UCS49P-SYzk08DDs9wMi6TZg` | 21 | 7 | 1,714,606 | 8 | "BMW N54 Water Pump and Thermostat - DIY, Symptoms, Tips, and Self Bleeding Procedure" (353,050, `g8qozaA0PJU`) |
| 40 | Fire & Ice Home Services | @fireiceheatingandaircondit4363 | `UCVdf0x94g-t4zIY5oGjma3g` | 21 | 20 | 1,600,311 | 0 | "Our Duct Cleaning Process from Start to Finish" (344,713, `L8yojsdz8EA`) |
| 41 | Zach of All Trades | @zachofallskilledtrades | `UCIgwmAZ3giU5QVV882LdacA` | 21 | 11 | 803,986 | 10 | "5 Best and Worst Trade Jobs" (253,684, `kL_KZtQEK3U`) |
| 42 | HVAC Training 101 | @HVACTraining101 | `UCWhFqsrrNfGWQnXSAVEAaZg` | 20 | 19 | 947,907 | 0 | "How To Clean Window AC Unit Without Removing 🌬️  \| HVAC Training 101" (132,981, `GI6TBdRus_8`) |
| 43 | HVAC Greatness by Pete Ramsey | @HVACPete | `UCcv3wg9ehzTs3UNPtBM88Fg` | 20 | 19 | 129,287 | 2 | "Make $1 Million as a ONE-MAN HVAC Business Owner/Operator" (26,665, `YHP8Xw_zZjU`) |
| 44 | My HVAC Life | @MYHVACLIFE | `UCBJ7O-VYUUHrKEQhuX9N7mg` | 20 | 15 | 83,404 | 9 | "RHEEM Heat pump on high pressure switch lock out." (18,243, `Qr0tpmRTgwI`) |
| 45 | HVAC Overtime | @HVACOvertime | `UCJGQJF0p5AxwZdeqx4Y8kFw` | 20 | 18 | 34,621 | 9 | "HVAC Overtime, where are they now?" (14,561, `7Cwyw3uDrMQ`) |
| 46 | Randall's Relaxation | @RandallsRestRelaxation | `UCYCmal9NJFAJqPzJXkPkcpQ` | 19 | 4 | 23,981,115 | 1 | "FAN NOISE of 12 FANS for 12 HOURS = BOX FANS WHITE NOISE FOR SLEEPING" (5,400,633, `eixPkJo-cx4`) |
| 47 | Tint Studio | @DetroitTintStudio | `UCGSxKdQi4PtxAQsNzh1Er1g` | 19 | 4 | 12,753,405 | 11 | "Walmart Tint so DUMB it’s GENIUS!" (5,018,366, `7CGKeoQ8m0o`) |
| 48 | HVAC Technician Sales Secrets | @hvactechsecrets | `UCRmPv4sdRiPqyWXqPDVWNKg` | 19 | 19 | 23,446 | 5 | "The Dark Side Of HVAC Sales And Tech Work - The Truth About HVAC Sales [1 of 2]" (5,422, `ZvZlIBDBbvw`) |
| 49 | Auto V Fix  | @AutoVFix | `UCYpjbQ_UObNjC_0WssGdoeg` | 18 | 4 | 2,340,889 | 13 | "Signs of bad AC compressor vs Pressure Switch (how to Fix, test, and reset)" (575,597, `m9iqmUVQs74`) |
| 50 | Rosenberg Wrestling | @RosenbergWrestling | `UCWOStv4POpK2XbG28R3iWtQ` | 18 | 1 | 164,376 | 16 | "Dominik Mysterio on Leaving Rhea Ripley, Teaming w/Liv Morgan, and the Truth About His "Real Dad"" (103,120, `Ny8v2bpeo1c`) |

### Top 30 NEW channels by HVAC-word videos returned

Same channels, ranked by returned videos with a home-HVAC word in the title (rule-based cut), then total views.

| # | Channel | Handle | channelId | HVAC-word videos | Videos | Total views | Last 12 mo | Biggest returned video (title, views, ID) |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | Love2HVAC with Ty Branaman | @love2hvac | `UCIoD-SEdUWMA74tWXRMyCZQ` | 44 | 49 | 2,727,698 | 0 | "Saturation, Superheat,  Subcooling" (228,621, `nwPA56cXqMA`) |
| 2 | Tool Junkie | @Tooljunkie4you | `UCB78N_DpnGKKSuwBknTN9CA` | 43 | 50 | 548,209 | 22 | "3 Blade Vs 5 Blade Ceiling Fan: Key Differences" (64,840, `JMFpfyFoyIQ`) |
| 3 | Nighthawk HVAC | @NighthawkHVAC | `UC7fmaDG-Q4ZLKSCmIkgMVWA` | 42 | 51 | 794,192 | 18 | "Flame Rollout!!! Finding the Cause! EP44" (139,113, `fWC2smK9hvg`) |
| 4 | Homey Vibe | @homeyvibe1 | `UCwJ0MSnM3_3OGuekYGI6bzw` | 38 | 38 | 242,542 | 30 | "Propane Vs Kerosene Heater: What’s Safer & Cheaper?" (53,262, `RkUdySAh_mo`) |
| 5 | MEP Academy | @MEPAcademy | `UCmFkUrOFd_FaASmI9HysA3g` | 36 | 45 | 4,004,375 | 7 | "How Data Centers Actually Work" (1,543,660, `cTwvUqLNQrM`) |
| 6 | Ewok | @ewokdoeshvac | `UCME4xG68IQbZP0YgkPT_3FQ` | 30 | 31 | 2,565,570 | 20 | "Day in the Life of an 19 Year Old HVAC Technician" (833,701, `2pyime545l4`) |
| 7 | OnemanHVAC | @Onemanhvac | `UCCfVNgkRrgMzNPrb8nOKigA` | 30 | 32 | 241,398 | 21 | "My HVAC Tuesday 5 no heat calls #hvaccontractor #hvac #bluecollar " (46,657, `pzK6HbsHoG8`) |
| 8 | HVAC OFFICIAL CHANNEL | @HVACOFFICIALCHANNEL | `UCDUAuJEO5e7GcBAPnodUvrw` | 29 | 36 | 272,214 | 33 | "HVAC Full Course \| Complete Guide for Beginners \| Learn AC & Chiller Systems Easily" (201,389, `WH7GiDVmNRc`) |
| 9 | Forever Tech English | @forevertechenglish | `UCSIClXw_5lT1buMo2BM6q7g` | 26 | 34 | 7,036,421 | 5 | "Cleaning Extremely Dirty AC With Pressure Washer!" (2,509,292, `DzhAHKicOFI`) |
| 10 | The HVAC Hacker | @thehvachacker | `UCNOsm1Xq_tdrBXWyYGSSg6g` | 25 | 26 | 1,722,165 | 0 | "Replacing Evaporator HVAC Repair" (366,061, `Sic_93G7UrI`) |
| 11 | Embers Fireplaces & Outdoor Living | @embersliving | `UC8dn-miD_eGaLHMhTdCSQBA` | 24 | 26 | 5,125,837 | 3 | "Wood vs Pellet Stove: What’s Best for Heating in 2026?" (609,143, `i13br5bdF0A`) |
| 12 | Mark Ballard LTD, Professional Heating Engineer | @MarkBallardLTDHeatingEngineer | `UCeSzwJbwcKgQ9iJAhcd7S4w` | 24 | 29 | 3,911,982 | 0 | "Replace a Leaking Radiator Valve with Out Draining the System. Professional Step by Step Guide" (1,102,292, `mjsPZirB9Cg`) |
| 13 | WW HVAC | @WWHVAC | `UCX9qUeV57Z7gqX1uwp8XOqg` | 23 | 27 | 656,893 | 13 | "Why Your AC Can't Hit 70° When It's 110° Outside" (166,162, `m_e6DRJY9UQ`) |
| 14 | HVACmillionaire | @hvacmillionaire | `UCvqYNMZq4c2sTztlX7ZqeNg` | 23 | 23 | 287,236 | 11 | "HVAC beginner: Wiring a basic heat pump system" (196,026, `C-VyY1fkc7k`) |
| 15 | HVACR Training Membership | @HVACRMembership | `UC6CeEomD0vavKtCwOyjcHIw` | 23 | 25 | 284,056 | 5 | "E4 Error Code in Air Conditioners: What It Means, Common Causes & Easy Fix!" (40,196, `nAbv55gdN5I`) |
| 16 | Talyn875 | @TALYN875 | `UChqTAS8GVF1TM3pFyxvnPxg` | 22 | 24 | 1,161,096 | 0 | "HVAC Training \| Dual Run Capacitor Wiring" (591,303, `yuINo7CWFaE`) |
| 17 | Apartment Maintenance Pro | @ApartmentMaintenancePro | `UC6Ko62-E2iMcdJ48tBvLjUQ` | 21 | 25 | 1,140,341 | 8 | "Nest Learning Thermostat Install (3rd Generation)" (294,646, `howVw9iAyPY`) |
| 18 | Jeff’s HVAC Adventures | @JeffsHVACAdventures | `UCsVYxwEvQIlB6b0MDDi7dpw` | 21 | 23 | 494,727 | 3 | "Quick Oil Boiler Service! Nozzle and Filter Change!" (114,625, `BQsSICx5H6g`) |
| 19 | Fire & Ice Home Services | @fireiceheatingandaircondit4363 | `UCVdf0x94g-t4zIY5oGjma3g` | 20 | 21 | 1,600,311 | 0 | "Our Duct Cleaning Process from Start to Finish" (344,713, `L8yojsdz8EA`) |
| 20 | HouseFresh | @HouseFresh | `UCW5aDZyLh2s8hOE18uqqrWg` | 19 | 27 | 1,725,964 | 9 | "Don’t Buy a Dehumidifier Before Watching This → The Best Dehumidifiers We Tested" (356,284, `DfbRZXJSQ2I`) |
| 21 | HVAC Training 101 | @HVACTraining101 | `UCWhFqsrrNfGWQnXSAVEAaZg` | 19 | 20 | 947,907 | 0 | "How To Clean Window AC Unit Without Removing 🌬️  \| HVAC Training 101" (132,981, `GI6TBdRus_8`) |
| 22 | HVAC Greatness by Pete Ramsey | @HVACPete | `UCcv3wg9ehzTs3UNPtBM88Fg` | 19 | 20 | 129,287 | 2 | "Make $1 Million as a ONE-MAN HVAC Business Owner/Operator" (26,665, `YHP8Xw_zZjU`) |
| 23 | HVAC Technician Sales Secrets | @hvactechsecrets | `UCRmPv4sdRiPqyWXqPDVWNKg` | 19 | 19 | 23,446 | 5 | "The Dark Side Of HVAC Sales And Tech Work - The Truth About HVAC Sales [1 of 2]" (5,422, `ZvZlIBDBbvw`) |
| 24 | HVAC Overtime | @HVACOvertime | `UCJGQJF0p5AxwZdeqx4Y8kFw` | 18 | 20 | 34,621 | 9 | "HVAC Overtime, where are they now?" (14,561, `7Cwyw3uDrMQ`) |
| 25 | Electro Demolish | @ElectroDemolish | `UCgfeKYGaAMAgaITBNGQ18sA` | 17 | 22 | 35,711,190 | 1 | "🇮🇳 Happy Independence Day Special \| 3 Ceiling Fans Combined \| Ultimate Wobble & Final Drop Test 🔥😱 ⭐" (9,170,051, `voOYrD1p4rE`) |
| 26 | Allen Hart | @AllenHart999 | `UCCEkrdkurnRF-gNh0h_61HA` | 17 | 25 | 6,255,827 | 0 | "How To Bleed A Radiator - Don’t try it until you watch this" (2,404,207, `tbLz8icLr2U`) |
| 27 | dereton33 Plumbing and heating, DIY and blogging. | @dereton33 | `UCuDuSCyS4B1-KpEqllfYr0w` | 17 | 23 | 3,518,809 | 1 | "How to cure damp in the bedroom." (781,840, `St3z3DW6N6w`) |
| 28 | Drewdriskle | @Drewdriskle | `UCMRQNX0-nhuyvl7SlGIzrNQ` | 17 | 17 | 42,450 | 7 | "How To Bleed Air From A Boiler \| Boilers" (13,591, `JyHB9bLUp_M`) |
| 29 | Urban Plumbers | @UrbanPlumbers | `UCWDa_bhiU5Vz-Xw487IQdZw` | 16 | 17 | 1,799,377 | 3 | "The Truth about Heat Pumps: Debunking the Myth." (372,271, `ZEJ0VUINV0s`) |
| 30 | HVACTIME | @HVACTIME | `UCRdNcv3g_4rpbNEyFopZwDg` | 16 | 23 | 1,322,699 | 0 | "YK Overview Centrifugal Chiller York HVAC Training" (259,056, `flAMZUK3f18`) |

## Topics (sub-niches, from the keyword's topic)

A video takes the topic of every keyword that returned it, so a video found by an `ac-central` and a `filters` keyword counts in both; topic rows add up to more than the unique total. `Only this topic` = videos returned by keywords of this topic alone. The topic is the keyword list's rule-based label, not a reading of the video. The "above search median" measure is not given here: a topic's videos are compared only with each other in the same searches, so it cannot rank topics against each other (compare median views instead; the channel multiple comes in round 3). Median views are of long-form English videos returned by any sort, so topics with more PRIORITY keywords (whose `views` sort pulls the biggest videos) read higher.

| Topic | Code | Keywords searched | Videos | Only this topic | Channels | Median views | HVAC-word videos: n / median | Last 12 mo: videos / median | 3 biggest (title, channel, views, ID) |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| Furnaces (gas) | `furnace` | 355 | 2,336 | 1,539 | 1,448 | 53,647 | 1,402 / 48,547 | 773 / 10,806 | "Fireplace Ambience – Cozy Fire for Relaxation & Background Viewing" (Fireplace Atmosphere, 166,006,610, `L_LUpnjgPso`)<br>"Aluminum and Mercury" (NileRed, 55,524,788, `IrdYueB9pY4`)<br>"12 HOURS of Relaxing Fireplace Sounds - Burning Fireplace & Crackling Fire Sounds (NO MUSIC)" (Cat Trumpet, 42,143,963, `UgHKb_7884o`) |
| HVAC general | `hvac-general` | 317 | 2,303 | 1,346 | 854 | 26,665 | 1,680 / 23,620 | 676 / 5,450 | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`)<br>"Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`)<br>"How to Fix a Car with No Heat (Easy)" (ChrisFix, 9,796,051, `-XjXTVJhFLM`) |
| Insulation | `insulation` | 426 | 1,811 | 1,605 | 1,234 | 47,766 | 1,168 / 38,857 | 488 / 11,974 | "Turning cotton balls into cotton candy" (NileRed, 19,287,629, `vHuFizITMdA`)<br>"10 Beginner Mistakes Installing Vinyl Plank Flooring" (Fix This Build That, 15,713,486, `kvo-n2AYZnA`)<br>"Kodak Black - No Love For A Thug [Official Audio]" (Kodak Black, 14,306,645, `VWfhqWh9G2A`) |
| Thermostats | `thermostat` | 356 | 1,534 | 1,303 | 1,096 | 36,328 | 1,002 / 35,820 | 339 / 2,721 | "*3 HOURS* Mark Adams BEST SHORTS OF 2023 \| Funny Marrkadams" (Yeap!, 12,431,298, `YSKstSLx3tk`)<br>"Car engine cooling system" (Sanya Tsvay, 8,859,691, `vRZu3-64yo0`)<br>"Turning Our Pool Into the World's Biggest Hot Tub!!!" (Beyond Family, 8,470,904, `kcBexIQ70ok`) |
| Boilers, radiators, steam (old-house heat) | `boiler-steam` | 262 | 1,488 | 1,145 | 847 | 50,266 | 879 / 31,501 | 330 / 7,070 | "FULL MATCH: Roman Reigns vs. Randy Orton vs. Kane vs. John Cena –Title Match: WWE Battleground 2014" (WWE, 94,521,566, `wk5EeNzH17o`)<br>"Limp Bizkit - Boiler (Official Music Video)" (limpbizkit, 93,572,265, `qex0OjXolzc`)<br>"Solomun \| Boiler Room: Tulum" (Boiler Room, 77,228,502, `bk6Xst6euQk`) |
| Filters | `filters` | 296 | 1,424 | 1,200 | 1,122 | 26,438 | 679 / 24,954 | 310 / 3,961 | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,617,421, `OE9bF80KQGk`)<br>"How to Change EVERY FLUID in your Car or Truck (Oil, Transmission, Coolant, Brake, and More)" (ChrisFix, 14,646,599, `t7JCh7PHoDc`)<br>"How to Change Your Oil (COMPLETE Guide)" (ChrisFix, 12,855,661, `O1hF25Cowv8`) |
| Space heaters | `space-heater` | 246 | 1,422 | 1,007 | 1,077 | 57,702 | 997 / 44,323 | 401 / 5,291 | "J Alvarez - Haters (Remix) [Official Music Video] ft. Bad Bunny, Almighty" (J Alvarez, 97,811,102, `9VgukIR8Qk8`)<br>"Don No. 1 - डॉन नंबर वन (4K ULTRA HD) Action Hindi Dubbed Full Movie \| Nagarjuna, Anushka Shetty" (Goldmines Dishoom, 34,763,989, `-2Z_-mLNgDs`)<br>"UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,348, `7LV5wY-iM34`) |
| AC: central air | `ac-central` | 227 | 1,411 | 680 | 858 | 148,885 | 891 / 110,547 | 456 / 40,258 | "AC/DC - Thunderstruck (Live At River Plate, December 2009)" (AC/DC, 378,894,765, `n_GFN3a0yj0`)<br>"REALLY AWESOME FAN SOUND FOR SLEEP \| White Noise For Superb Slumber, Studying & Relaxation" (Relaxing White Noise, 125,772,335, `C5Gm8UvxKlU`)<br>"AC/DC - Let There Be Rock (Live At River Plate, December 2009)" (AC/DC, 117,720,981, `O24AipZ-buQ`) |
| Heat pumps | `heat-pump` | 286 | 1,323 | 711 | 665 | 41,923 | 1,100 / 39,004 | 327 / 7,208 | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,617,421, `OE9bF80KQGk`)<br>"How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`)<br>"Would you swim in power plant wastewater?" (Tom Scott, 6,918,558, `OgMXjAQ5q14`) |
| Parts homeowners touch (capacitors, contactors, igniters...) | `parts` | 232 | 1,310 | 983 | 800 | 68,804 | 919 / 69,632 | 190 / 9,674 | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`)<br>"Capacitors Explained - The basics how capacitors work working principle" (The Engineering Mindset, 11,078,060, `X4EUwTwZ110`)<br>"Experiments with fan capacitor" (Let's See Inside, 10,449,175, `wRiNTWB3hrE`) |
| Energy bills | `energy-bill` | 268 | 1,287 | 1,123 | 1,016 | 25,649 | 670 / 14,189 | 595 / 6,620 | "Masha And The Bear 🌞🏖 Summer Holidays🏖🌞 Best episodes cartoon collection 🎬" (Masha and The Bear, 435,536,745, `jCvSEuHms5M`)<br>"Why Are 96,000,000 Black Balls on This Reservoir?" (Veritasium, 112,818,293, `uxPdPpi5W4o`)<br>"'JUST THE TWO OF US' (GROVER WASHINGTON JNR - BILL WITHERS) cover by HSCC" (The Hindley Street Country Club, 40,504,078, `dS7kzPGkb3o`) |
| Wood and pellet stoves, fireplaces | `wood-stove` | 163 | 1,079 | 975 | 755 | 65,842 | 747 / 53,262 | 301 / 20,523 | "Fireplace Ambience – Cozy Fire for Relaxation & Background Viewing" (Fireplace Atmosphere, 166,006,610, `L_LUpnjgPso`)<br>"12 HOURS of Relaxing Fireplace Sounds - Burning Fireplace & Crackling Fire Sounds (NO MUSIC)" (Cat Trumpet, 42,143,963, `UgHKb_7884o`)<br>"Outdoor wood stove from red brick and cement" (Creative Cement, 38,516,965, `EElfn2tYqmA`) |
| Ceiling fans and fans | `ceiling-fan` | 210 | 919 | 774 | 634 | 82,023 | 681 / 81,868 | 228 / 17,114 | "REALLY AWESOME FAN SOUND FOR SLEEP \| White Noise For Superb Slumber, Studying & Relaxation" (Relaxing White Noise, 125,772,335, `C5Gm8UvxKlU`)<br>"FAN WHITE NOISE \| Fall asleep, stay asleep (11 Hours)" (Relaxing White Noise, 51,199,807, `qorkD6nPYQM`)<br>"SML Movie: Jeffy's Bedtime" (SML, 37,597,774, `IWqTVk26T14`) |
| HVAC scams, upsells, contractors | `scams-upsells` | 86 | 800 | 373 | 445 | 21,132 | 646 / 20,338 | 370 / 6,134 | "Oil change scams: Hidden camera investigation on what really happens to your car (CBC Marketplace)" (CBC News, 48,175,189, `-avpx8UTakI`)<br>"I Gave HACKED SCAMMERS a PANIC ATTACK On CCTV!" (Scam Sandwich, 13,674,344, `fhej9kABoyQ`)<br>"The NEW Tesla Roadster: My Honest Reaction" (Marques Brownlee and Auto Focus, 12,083,826, `scwlR0QHGOk`) |
| Windows, film, curtains | `windows` | 114 | 769 | 716 | 581 | 116,809 | 331 / 71,348 | 241 / 35,297 | "Rain Sound On Window with Thunder SoundsㅣHeavy Rain for Sleep, Study and Relaxation, Meditation" (Relaxing Ambience ASMR, 141,067,168, `mPZkdNFkNps`)<br>"Mindo Taseeldarni (Punjabi Movie) Karamjit Anmol \| Kavita Kaushik \| Harby Sangha \| Malkeet Rauni" (R R Records, 70,896,838, `aYF5x3fRpqk`)<br>"BINDU I बिंदू  I ANJANA SINGH I NEW BHOJPURI MOVIE 2025" (B4U Bhojpuri, 58,061,857, `JbYFINBSGj8`) |
| AC: window and portable | `ac-window` | 158 | 676 | 401 | 479 | 53,174 | 513 / 40,511 | 234 / 14,136 | "Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,617,421, `OE9bF80KQGk`)<br>"$649 Dyson Fan vs. $15 Walmart Fan: The Hard Truth" (Mark Spurrell, 12,715,303, `dS0oFmzU06g`)<br>"A/C Buying Guide \| Inverter AC vs Non Inverter AC, Window AC vs Split AC, What is Ton & Star Rating?" (SidTalk, 10,772,005, `QNM9ASapu58`) |
| Humidity, dehumidifiers, humidifiers | `humidity` | 165 | 652 | 555 | 481 | 17,248 | 520 / 12,921 | 210 / 2,030 | "Best fan placement to move air through the house" (Matthias random stuff, 11,467,376, `1L2ef1CP-yw`)<br>"Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`)<br>"EASY - How to STOP CONDENSATION - Get Rid of Black Mold and Clean Mould" (Fixmyroof, 6,835,028, `Oj99RNY55Es`) |
| Replacement cost, repair or replace | `replacement-cost` | 68 | 636 | 258 | 404 | 55,045 | 472 / 53,266 | 264 / 16,080 | "FISHER - Losing It - Live at Coachella 2019 Friday April 12, 2019" (Coachella, 78,770,021, `oUbpmjOgmmU`)<br>"Carl Cox @ Château de Chambord in France for Cercle" (Cercle, 17,882,305, `ZdAwiV4T22I`)<br>"How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`) |
| Mini-splits | `mini-split` | 161 | 635 | 331 | 374 | 55,808 | 563 / 54,462 | 142 / 13,037 | "Building a Tiny Office Pod Under My Stairs" (Man Made, 18,449,234, `b0npGI9WCzs`)<br>"How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (alpinehomeair, 13,032,752, `DzVJiSQNbew`)<br>"7 FATAL Wiring Mistakes Most DIYers Don't Know They Are Making \| Most Are Guilty of 3" (How To Home, 12,129,104, `-jeP1d8PC1I`) |
| Oil furnaces and oil heat | `oil-furnace` | 109 | 607 | 403 | 381 | 45,928 | 441 / 38,733 | 173 / 11,451 | "Millions of people do not know this knowledge! 3 in 1 waste oil heater! Warm for winter 2024" (Creative inventions LMTN, 14,876,623, `UawMGmg87ho`)<br>"Petroleum - Modern history of oil on a Map" (Geo History, 10,754,521, `xMQUGSrnbP8`)<br>"Steve Ballmer Explains The Cost of Oil" (USAFacts, 10,751,181, `KEiKy6mf2Ew`) |
| Heat (and cooling) in a power outage | `outage-heat` | 78 | 599 | 396 | 429 | 64,613 | 428 / 45,480 | 303 / 18,783 | "The Most Misunderstood Concept in Physics" (Veritasium, 31,362,549, `DxL2HoqLbyA`)<br>"Winter Survival Shelter, Stay Warm Overnight With No Fire" (Scavenger Survival, 19,456,552, `lwv-vKYJV1o`)<br>"UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (Zen Garden Oasis, 12,939,348, `7LV5wY-iM34`) |
| Ducts and vents | `ducts-vents` | 162 | 586 | 349 | 420 | 43,994 | 440 / 45,138 | 119 / 2,264 | "Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`)<br>"How to Vent a Bath Fan Through the Roof \| This Old House" (This Old House, 4,555,765, `PqrZWd_CQIE`)<br>"How To Clean Your Dryer Vent Duct - Step By Step - It's Super Simple!" (AmplifyDIY, 3,803,747, `GLZSqhUoF_g`) |
| Seasonal maintenance | `maintenance` | 81 | 585 | 222 | 364 | 37,017 | 446 / 31,808 | 253 / 7,860 | "Pitbull Mashup" (dk, 42,209,548, `lNUxJ6SL7T0`)<br>"Air Conditioner - 10 hours of relaxing ambient sounds asmr" (UnReal Asmr, 23,617,421, `OE9bF80KQGk`)<br>"How to Properly Recharge Your AC System" (ChrisFix, 12,893,707, `Pdq8JAlct6s`) |
| Brand verdicts | `brands` | 70 | 582 | 259 | 342 | 57,520 | 483 / 55,117 | 184 / 11,330 | "A/C Buying Guide \| Inverter AC vs Non Inverter AC, Window AC vs Split AC, What is Ton & Star Rating?" (SidTalk, 10,772,005, `QNM9ASapu58`)<br>"Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`)<br>"How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| Noises | `noises` | 115 | 556 | 315 | 322 | 78,570 | 290 / 39,324 | 112 / 19,292 | "White Noise Black Screen \| Sleep, Study, Focus \| 10 Hours" (Relaxing White Noise, 384,357,623, `nMfPqeZjc2c`)<br>"REALLY AWESOME FAN SOUND FOR SLEEP \| White Noise For Superb Slumber, Studying & Relaxation" (Relaxing White Noise, 125,772,335, `C5Gm8UvxKlU`)<br>"FAN WHITE NOISE \| Fall asleep, stay asleep (11 Hours)" (Relaxing White Noise, 51,199,807, `qorkD6nPYQM`) |
| Indoor air (purifiers, mold, CO) | `indoor-air` | 84 | 518 | 351 | 404 | 19,358 | 362 / 13,473 | 170 / 4,704 | "White Noise Black Screen \| Sleep, Study, Focus \| 10 Hours" (Relaxing White Noise, 384,357,623, `nMfPqeZjc2c`)<br>"REALLY AWESOME FAN SOUND FOR SLEEP \| White Noise For Superb Slumber, Studying & Relaxation" (Relaxing White Noise, 125,772,335, `C5Gm8UvxKlU`)<br>"FAN WHITE NOISE \| Fall asleep, stay asleep (11 Hours)" (Relaxing White Noise, 51,199,807, `qorkD6nPYQM`) |
| Drafts and weatherstripping | `drafts` | 80 | 512 | 479 | 396 | 39,196 | 248 / 23,392 | 202 / 8,452 | "The Secret Caulking Tip That Will Transform Your Ability!" (The Funny Carpenter, 16,789,508, `cQNIv2QqP00`)<br>"SPEED GOES PRO, EPISODE 1: TOM BRADY  (Football)" (IShowSpeed, 8,965,041, `5ZKLMLm2YLs`)<br>"FASTEST DRAFT TEAM!!" (Miniminter, 4,866,725, `0I-ARCNlxjg`) |
| Refrigerant / Freon | `refrigerant` | 64 | 473 | 327 | 299 | 70,554 | 321 / 60,718 | 105 / 4,327 | "DAD Reacts to 11 Year old Son's CRINGE TIKTOKS!! 😂" (The Royalty Family, 63,418,912, `4SuPs7XrBW8`)<br>"12 Year old Son & Mom SWAP LIVES! *Instant Regret*" (The Royalty Family, 38,632,833, `ksJqjusYFt0`)<br>"How to Properly Recharge Your AC System" (ChrisFix, 12,893,707, `Pdq8JAlct6s`) |
| Keeping the house warm cheaply | `keep-warm` | 49 | 425 | 217 | 344 | 105,539 | 281 / 63,011 | 220 / 28,706 | "Dugout Shelter Under 10ft (3m) of Snow - Solo Camping in Survival Shelter During Snow Storm" (Outdoor Boys, 97,243,887, `wcDFgir_jgY`)<br>"Camping Under the Snow in Hot Tent - Heated Snow Shelter & Sledding Hill of Death" (Outdoor Boys, 26,940,980, `A6v5Vj6h_fQ`)<br>"Camping Under the Snow in Survival Shelter" (Outdoor Boys, 18,134,489, `PTnrqkMpfj8`) |
| Condenser and coil cleaning | `coil-cleaning` | 73 | 397 | 214 | 285 | 84,936 | 304 / 77,576 | 83 / 11,365 | "How to Properly Recharge Your AC System" (ChrisFix, 12,893,707, `Pdq8JAlct6s`)<br>"How to Flush a Heater Core (Fast)" (ChrisFix, 11,173,633, `M9SIafVsqyc`)<br>"How to Recharge Your Car's AC System (Fast and Easy)" (ChrisFix, 10,771,363, `SHg2xRMnM38`) |
| Keeping the house cool (no-AC tricks) | `keep-cool` | 51 | 349 | 276 | 280 | 224,914 | 194 / 31,082 | 166 / 11,756 | "HOT VS COLD Challenge Ryan vs Daddy 1hr Kids Show" (Ryan's World, 116,259,579, `SCyFBeIgaDc`)<br>"INCREDIBLE ROOM MAKEOVER IDEAS \|\| Low-Budget Decor Crafts" (5-Minute Crafts, 76,850,950, `OGvhmFZwY0s`)<br>"Jason plays the Hot and Cold Challenge" (Jason Vlogs, 65,645,927, `o1cW9Cv3rWM`) |
| Attic fans, whole-house fans, hot attics | `attic-fan` | 91 | 333 | 200 | 255 | 55,262 | 283 / 44,125 | 137 / 2,625 | "REALLY AWESOME FAN SOUND FOR SLEEP \| White Noise For Superb Slumber, Studying & Relaxation" (Relaxing White Noise, 125,772,335, `C5Gm8UvxKlU`)<br>"I Turned My House Into a Trampoline Park!" (Unspeakable, 79,772,408, `lSSWH4NOdgE`)<br>"There's Something LIVING in our Attic" (The Royalty Family, 25,008,610, `NLPkz9TJNP8`) |
| Geothermal | `geothermal` | 43 | 294 | 229 | 222 | 46,382 | 198 / 48,582 | 83 / 30,745 | "BEAUTIFUL PLANET \| The most beautiful places on Earth" (Lifeder, 17,165,124, `ExJf59ankJo`)<br>"Could Solar Storms Destroy Civilization? Solar Flares & Coronal Mass Ejections" (Kurzgesagt – In a Nutshell, 15,421,439, `oHHSSJDJ4oo`)<br>"How does a Thermal power plant work?" (Sabin Civil Engineering, 7,361,642, `IdPTuwKEfmA`) |
| Electric and baseboard heat | `electric-heat` | 70 | 287 | 151 | 215 | 66,574 | 224 / 59,981 | 46 / 2,886 | "How To Make An Electrical Arc Furnace" (TKOR, 14,668,783, `VTzKIs19eZE`)<br>"How to Fix a Car with No Heat (Easy)" (ChrisFix, 9,796,051, `-XjXTVJhFLM`)<br>"Space Heater Nonsense" (Technology Connections, 5,386,879, `V-jmSjy2ArM`) |
| AC freezing up | `ac-freezing` | 87 | 211 | 119 | 154 | 52,688 | 151 / 54,268 | 60 / 4,174 | "Ice Cube - It Was A Good Day" (Ice Cube / Cubevision, 396,896,882, `h4UqMyldS7Q`)<br>"Best fan placement to move air through the house" (Matthias random stuff, 11,467,376, `1L2ef1CP-yw`)<br>"How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (How To Home, 5,631,712, `k7PSzi7NSyc`) |
| Short cycling | `short-cycling` | 39 | 206 | 151 | 151 | 60,472 | 106 / 16,936 | 70 / 2,254 | "If it were not filmed, nobody would believe │ Short Documentary" (RIFIANBOY, 11,761,233, `d-kPcOVub4M`)<br>"Portable Air Conditioners - Why you shouldn't like them" (Technology Connections, 10,388,788, `_-mBeYC2KGc`)<br>"How To Adjust a Pressure Switch" (R.C. Worst & Co., Inc., 6,063,989, `1VNSv7xVzzU`) |
| Swamp / evaporative coolers | `evap-cooler` | 42 | 202 | 162 | 150 | 46,800 | 140 / 35,883 | 61 / 59,788 | "Homemade air conditioner DIY - Awesome Air Cooler! - EASY Instructions - can be solar powered!" (desertsun02, 15,266,378, `ITtlxjvLQis`)<br>"Make your own AIR CONDITIONER at home Fast and Easy!" (The Liberty Engine Project, 5,647,026, `WHLuimGVzBA`)<br>"Recycled Styrofoam Air Conditioner! TKOR Creates An Efficient DIY Air Conditioner!" (TKOR, 3,746,826, `TpqUr6bEYOs`) |
| Smells | `smells` | 32 | 130 | 88 | 91 | 22,158 | 73 / 32,316 | 38 / 822 | "I Built The Worlds Largest Minecraft Furnace" (Carvs, 12,044,095, `qsarR6CnN1w`)<br>"I Built a SMELTING FACTORY in Minecraft Hardcore" (aCookieGod, 5,370,381, `q9nBod8HbNw`)<br>"100 Days But SMELTING MULTIPLIES ITEMS In Minecraft 😰" (Anshu Bisht, 3,905,512, `3WeFFNTKoTI`) |
| Home warranties | `home-warranty` | 9 | 102 | 85 | 78 | 3,338 | 85 / 3,308 | 44 / 887 | "STOP Buying This HVAC Brand" (The DIY HVAC Guy, 1,295,597, `x2BK-zr4raE`)<br>"The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)" (Vent Exposed and 3 more, 670,918, `86S3ITbfzQY`)<br>"This $0 Fix Cools Your Attic by 55°F. Why Don't Roofers Tell You?" (Candlelight Archives, 593,943, `7iKXXv4bHvU`) |

