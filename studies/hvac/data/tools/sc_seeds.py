#!/usr/bin/env python3
"""Build Silver Cymbal seed table (md + csv) from the full list + NexLev details.
Usage: python3 -I sc_seeds.py <rawdir> <out.md> <out.csv>
Seed selection, topic groups, borderline/adjacent lists are the helper's reading (2026-10-23), hard-coded below."""
import sys, json, os, csv, statistics, datetime
raw, out_md, out_csv = sys.argv[1], sys.argv[2], sys.argv[3]
allv = json.load(open(os.path.join(raw, "silver-cymbal-all-2026-10-23.json")))
V = {v["id"]: v for v in allv["videos"]}
NX = json.load(open(os.path.join(raw, "silver-cymbal", "nexlev-video-details-seeds-2026-10-23.json")))["videos"]

SEEDS = {  # id: topic group (reading)
 "_b6p0fkWhCY": "AC (central) - not cooling / condenser + filter", "qAxJb0J1HH0": "AC (central) - condensate drain",
 "Wejop_Rjpv0": "mini-split - DIY install", "o8KQu_MlpoY": "AC (window) - not cooling / cleaning",
 "DSNUyxZtrmo": "mini-split - condenser cleaning", "nsRHhU6q5RY": "AC (central) - condenser cleaning",
 "zvFKD95z7IM": "mini-split - DIY install", "5GbXgEYw5TE": "boiler (oil heat) - how it works",
 "leEsPGaaru8": "AC (portable, battery) - product review", "BP1iDvKpNZA": "heat pump - cold-climate failure",
 "NsPBamTmOPM": "AC (portable) - product review", "uObGbs4sGQY": "AC (portable heat pump) - product review",
 "yCZqfnlBYW8": "boiler - circulator pump repair (no heat)", "ED3bfesbE_Y": "filter - furnace filter",
 "GdTOl1WcHV0": "heating fuel - oil vs gas", "flpbqJu2sT8": "boiler - circulator pump replace",
 "kEWzIfnIhUw": "mini-split - DIY install (heat + AC)", "Xd-Og809TUo": "boiler/furnace - no-heat troubleshooting",
 "yZavrHJsBAw": "AC (portable heat pump) - product review", "S8XO4wFhrPU": "AC (portable) + portable fridge - product first look",
 "OGVXmIZtEG8": "AC (portable) - product review", "cC-J0ZCUH28": "mini-split - hidden features",
}
BORDER = [  # id, reason (reading), lean
 ("sHL4lBAhklA", "Spray foam alternative (duct seal) for sealing gaps around wires/pipes (description). Title is about the cost of spray foam, not heating, cooling or the bill.", "operator call"),
 ("EjLJm0g4whg", "Garage-door weatherstripping. Description says 'hot, humid, drafty' but also bugs and mice; garage, not living space; title not about heat/bill.", "operator call"),
 ("9d9TL02idO4", "Pellet stove install + US tax credit 'to help pay for heating your home' (description). Home heating and cost, but a stove is not in the brief's HVAC list.", "lean include"),
 ("CRTh8fIhV5E", "Wood stove restoration (cosmetic). Heating appliance, not HVAC system.", "lean exclude"),
 ("3x5t4Zvkqms", "Diesel heater for a shop (description: vans, sheds, tents, RVs). Not the house.", "lean exclude"),
 ("ZJQjKOnbLKU", "Space-heater safety. Space heaters sit in the electrical/fire study's scope.", "electrical study"),
 ("CXjNHwFg0aQ", "Crawlspace encapsulation; description: humidity, mold, dehumidifier. Humidity is in scope, but this is a building-envelope project.", "operator call"),
 ("r31vJXrZD3Y", "Bathroom exhaust fan refresh. Ventilation, often filed as electrical.", "lean exclude"),
 ("zMSWKLvDFTc", "Kitchen range hood vented outside. Ventilation install.", "lean exclude"),
 ("KV4tWIPLFc8", "Removing fiberglass insulation. Insulation, but title not about heating, cooling or the bill (rule 5).", "exclude (rule)"),
 ("k8hK9duZIGo", "Heat tape to stop pipes freezing. Plumbing freeze protection.", "plumbing"),
 ("OYM8aSESAY8", "Snowstorm with no power (description: 'what I did to make it through'). Outage, but heat not named in title or description.", "operator call"),
 ("pPMm0reEBPM", "Generator inlet/interlock hookup; description mentions running 'heating systems'. Generator how-to (backfeed safety = electrical study).", "lean exclude"),
 ("BACQ3167pkA", "Generator transfer switch install. Generator how-to.", "exclude (rule)"),
 ("yNBXE3BszEM", "Whole-house battery backup (EcoFlow); description mentions heat. Product/power-station video.", "exclude (rule)"),
 ("_G7ZPjmR5ck", "36-hour outage on an EcoFlow battery. Power-station product video.", "exclude (rule)"),
 ("IgeexSKIEOQ", "Storm prep with an Anker battery. Power-station product video.", "exclude (rule)"),
 ("Roz9OXl5uEU", "Rooftop solar contractor disaster. Energy, but not the bill or HVAC.", "lean exclude"),
 ("TVkQ_aU2cWQ", "Car interior smell (cabin filter, ozone). Car, not house.", "exclude"),
]
ADJ = ["YNBdtC9jjLA", "e1TpseQATTw", "R5lfB2G8fnQ"]
SHORT_HVAC = [  # under 300 s, HVAC-ish, dropped by the length rule (reading)
 ("M-pa_vUNGl4", "AC (window) install/review"), ("NI-KNyp9tdQ", "AC (portable)"), ("NqFgelKaQvc", "AC (portable)"),
 ("dgpGsszbF4E", "AC (portable)"), ("JDq4i_lT8YI", "AC (cheapest on Amazon)"), ("biNdfKcxaqE", "dehumidifier"),
 ("k8PlPcKGENw", "filter - furnace filter"), ("xuswKBmauI4", "boiler - zone valve (no heat)"), ("5cvAHDqpgUY", "AC (Sony pocket AC)"),
 ("SIyntnwE7O8", "outage heat"), ("ydRveyXkf4M", "generator hookup to 'run heat' (borderline)"), ("Lw9awU9xehE", "water heater flush (adjacent)"),
]

def mmss(s): return f"{s // 60}:{s % 60:02d}"
lf = [v for v in allv["videos"] if v["duration_s"] >= 300]
win = [v for v in lf if "2025-10-23" <= v["published"] <= "2026-10-23"]
base = statistics.median([v["views"] for v in win])
rows = []
for vid, topic in SEEDS.items():
    v = V[vid]; n = NX[vid]
    rows.append({"id": vid, "title": v["title"], "views": v["views"], "views_nexlev": n["viewCount"],
                 "published": v["published"], "published_nexlev": n["publishDate"], "length_s": n["lengthSeconds"],
                 "length": mmss(n["lengthSeconds"]), "length_tab": v["duration_text"],
                 "multiple": round(v["views"] / base, 2), "topic": topic,
                 "thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", "thumb_maxres": n["maxres"] or "not found",
                 "url": f"https://www.youtube.com/watch?v={vid}"})
rows.sort(key=lambda r: -r["views"])
with open(out_csv, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["rank", "video_id", "title", "views", "views_nexlev_crosscheck", "upload_date", "length_seconds", "length", "length_tab_text",
                "multiple", "topic_group_reading", "thumbnail_url", "thumbnail_maxres", "url", "sub_niche", "format", "emotions", "villain",
                "source_views", "source_date", "source_length"])
    for i, r in enumerate(rows, 1):
        w.writerow([i, r["id"], r["title"], r["views"], r["views_nexlev"], r["published"], r["length_s"], r["length"], r["length_tab"],
                    r["multiple"], r["topic"], r["thumb"], r["thumb_maxres"], r["url"], "", "", "", "",
                    "YouTube innertube /next exact count, pulled 2026-10-23", "YouTube innertube /next dateText; matches NexLev publishDate",
                    "NexLev youtube_video_details lengthSeconds"])
sv = [r["views"] for r in rows]; sm = [r["multiple"] for r in rows]
lfm = [v["views"] / base for v in lf]
md = []
A = md.append
A("# Silver Cymbal: HVAC seed videos\n")
A("**Channel:** Silver Cymbal, [@SilverCymbal](https://www.youtube.com/@SilverCymbal), channel ID `UC67dKTEwpAhKv2oYDATwR8g`. On-camera home DIY. Header on 2026-10-23: "
  f"{allv['subs_header']}, {allv['videos_header']} (measured, channel page).\n")
A("**Pulled:** 2026-10-23 by the Round 1 seed helper. Not yet re-checked by a second helper (working rule 3).\n")
A("## How this list was made\n")
A("| Item | Value | Source |\n|---|---|---|")
A(f"| Videos on the Videos tab | {len(allv['videos'])} | YouTube channel Videos tab, logged-out curl + innertube continuations, all 18 pages (`data/tools/yt_allsorts.py`) |")
A("| Shorts | 1 (`EpGDf1jp0vA`, on the Shorts tab, not on the Videos tab) | YouTube Shorts tab; header count 539 = 538 + 1 Short |")
A("| Live streams | none found (no Live tab on the channel) | YouTube channel tabs: Home, Videos, Shorts, Playlists, Posts |")
A(f"| Long-form (>= 300 s) | {len(lf)} | tab duration text; seed lengths re-checked with NexLev `lengthSeconds` |")
A(f"| Dropped as under 5 minutes | {len(allv['videos']) - len(lf)} (plus the 1 Short) | same |")
A(f"| Baseline rule used | last-12-months rule: long-form uploaded 2025-10-23 to 2026-10-23, n = {len(win)} (>= 10, so the last-30 fallback was not needed) | exact dates from innertube /next |")
A(f"| Baseline median views | **{int(base):,}** | median of those {len(win)} exact view counts (mean of the 9th and 10th: 78,736 and 80,878) |")
A(f"| His all-time long-form median, for context | {int(statistics.median([v['views'] for v in lf])):,} (= {statistics.median(lfm):.2f}x the baseline) | same data |")
A("| Multiple | views / 79,807 | calculated |")
A("")
A("**Sorts checked (measured, 2026-10-23):**\n")
A("- **Popular** works: 538 videos, view counts never go up from one video to the next (0 breaks in order); starts with `TofHP1moT78` \"NEVER SOLDER PIPE AGAIN\" at 21M.")
A("- **Oldest** works: 538 videos, the age text never gets newer down the list (0 breaks); starts with `KZL7tt3culs` \"World's ONLY Factory Built GLASS ENGINE\" (2015-08-29), ends with the newest upload.")
A("- **Latest** works only through its chip: the default page plus its own continuation stopped at 30 videos (the old `yt.py` method). Loading the \"Latest\" chip and paging gave all 538, exactly the Oldest list reversed.")
A("- All three sorts return the same 538 IDs.\n")
A("**Where each figure comes from:**\n")
A("- **Views:** exact counts from the YouTube video page data (innertube `/next`), pulled 2026-10-23 at about 03:30 UTC. NexLev `youtube_video_details` was called for every seed; its counts are a few views higher on most (pulled minutes later; largest gap +107 on `DSNUyxZtrmo`, and -53 on `yCZqfnlBYW8`). Both are in the CSV.")
A("- **Upload date:** YouTube `/next` date text. It matches NexLev `publishDate` on all 24 videos checked (the 22 seeds, `sHL4lBAhklA` and `JyZgGSmtCRY`).")
A("- **Length:** NexLev `lengthSeconds`. The Videos-tab text is the same or 1 second longer (of 24 checked: 13 identical, 11 one second longer), so the tab rounds up. The 5-minute filter used the tab text; the two edge videos (tab 5:00 and 5:01) were checked in NexLev: 300 s each, so both stay long-form.")
A("- **Thumbnail:** `https://i.ytimg.com/vi/<id>/hqdefault.jpg`; the maxres URL NexLev returned is in the CSV (`yCZqfnlBYW8` has none: not found).")
A("- **Topic group, borderline calls, lean:** my reading from titles and, where unsure, the video description. Not measured.\n")
A("**Problems found:**\n")
A("- The watch page (`/watch?v=`) and the `/player` endpoint are blocked from the cloud (Google 'sorry' redirect, LOGIN_REQUIRED), so exact length came from NexLev, not YouTube.")
A("- NexLev `youtube_channel_videos` dates are guessed from the rounded '1 month ago' text, not real: it gives `sHL4lBAhklA` 2026-09-23, the real date is 2026-08-30. Its views are rounded (1.5M). Don't use its listing dates.")
A("- NexLev's channel listing said `videosCount: 31` for this channel, which is wrong (the tab has 538).\n")
A("## Seed videos (22), sorted by views\n")
A("Long-form only. Sub-niche, format, emotions and villain are left blank for the labelling round.\n")
A("| # | Video ID | Title | Views | Upload date | Length | Multiple | Topic group (reading) | Thumbnail | Sub-niche | Format | Emotions | Villain |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for i, r in enumerate(rows, 1):
    A(f"| {i} | `{r['id']}` | \"{r['title']}\" | {r['views']:,} | {r['published']} | {r['length']} | {r['multiple']:.2f}x | {r['topic']} | {r['thumb']} |  |  |  |  |")
A("")
A("## Summary\n")
n2 = sum(1 for m in sm if m >= 2)
A(f"- **Count:** {len(rows)} long-form seeds (out of {len(lf)} long-form videos, {len(rows)/len(lf)*100:.1f}%).")
A(f"- **Median views:** seeds {int(statistics.median(sv)):,} vs his long-form median {int(statistics.median([v['views'] for v in lf])):,} (all time) and {int(base):,} (last 12 months).")
A(f"- **Median multiple:** seeds {statistics.median(sm):.2f}x vs {statistics.median(lfm):.2f}x for all his long-form videos (both against the 79,807 baseline).")
A(f"- **Share at 2x or more:** seeds {n2} of {len(rows)} ({n2/len(rows)*100:.0f}%) vs {sum(1 for m in lfm if m >= 2)} of {len(lf)} ({sum(1 for m in lfm if m >= 2)/len(lf)*100:.0f}%) for all his long-form.")
yrs = {}
for r in rows: yrs[r["published"][:4]] = yrs.get(r["published"][:4], 0) + 1
A(f"- **Upload years of the seeds:** " + ", ".join(f"{y}: {c}" for y, c in sorted(yrs.items())) + ". Only 1 seed (`OGVXmIZtEG8`) is inside the 12-month baseline window.")
A("- **Reading (not measured):** the multiples are high partly because most seeds are years old and the baseline is his last 12 months, when his output turned to power-station reviews (7 of the 18 baseline videos have generator, power-station or battery-backup titles). Treat the multiples as 'this beat his current typical video', not as a fair same-age comparison. The seeds' strongest group by views is AC cleaning/fixing (central, window, drain, condenser); product reviews of portable ACs sit at the bottom.")
A("\n**Top 5 seeds:**\n")
for r in rows[:5]: A(f"1. \"{r['title']}\" (`{r['id']}`): {r['views']:,} views, {r['multiple']:.1f}x, {r['published']}")
A("\n**Bottom 5 seeds:**\n")
for r in rows[-5:]: A(f"1. \"{r['title']}\" (`{r['id']}`): {r['views']:,} views, {r['multiple']:.2f}x, {r['published']}")
A("\n## Borderline and excluded (long-form)\n")
A("Not counted as seeds. 'Lean' is my reading, for the operator to decide.\n")
A("| Video ID | Title | Views | Upload date | Length (tab) | Multiple | Why borderline | Lean |\n|---|---|---|---|---|---|---|---|")
for vid, why, lean in sorted(BORDER, key=lambda b: -V[b[0]]["views"]):
    v = V[vid]; A(f"| `{vid}` | \"{v['title']}\" | {v['views']:,} | {v['published']} | {v['duration_text']} | {v['views']/base:.2f}x | {why} | {lean} |")
kw = ("generator", "power station", "battery backup", "solar generator", "ecoflow", "jackery", "bluetti", "anker solix", "power backup", "backup power", "battery generator", "inverter generator", "whole house backup")
gen = [v for v in lf if any(k in v["title"].lower() for k in kw) and v["id"] not in {b[0] for b in BORDER}]
A(f"\nAlso excluded without listing one by one: **{len(gen)} long-form generator / power-station / battery-backup videos** (title keyword count, my reading of the rule 'generator and power-station product reviews are OUT'). IDs are in the raw file.\n")
A("## Adjacent: water heaters (plumbing, not seeds)\n")
A("| Video ID | Title | Views | Upload date | Length (tab) | Multiple |\n|---|---|---|---|---|---|")
for vid in ADJ:
    v = V[vid]; A(f"| `{vid}` | \"{v['title']}\" | {v['views']:,} | {v['published']} | {v['duration_text']} | {v['views']/base:.2f}x |")
A("\n## HVAC-type videos dropped by the 5-minute rule (for reference)\n")
A("Under 300 seconds on the tab, so not seeds. Listed because they are a real part of his HVAC output (10 of the 12 are HVAC proper), and the window-AC install (2,861,907 views) would rank 4th among the seeds. Topic is my reading.\n")
A("| Video ID | Title | Views | Upload date | Length (tab) | Topic (reading) |\n|---|---|---|---|---|---|")
for vid, t in sorted(SHORT_HVAC, key=lambda x: -V[x[0]]["views"]):
    v = V[vid]; A(f"| `{vid}` | \"{v['title']}\" | {v['views']:,} | {v['published']} | {v['duration_text']} | {t} |")
A("\n## Files\n")
A("- Full list: `data/raw/silver-cymbal-all-2026-10-23.json` (538 videos: id, title, exact views, date, duration, Popular and Latest rank, source of each field)")
A("- Seed CSV: `data/raw/silver-cymbal-seeds-2026-10-23.csv`")
A("- Raw pulls: `data/raw/silver-cymbal/` (tab pull for all three sorts, `/next` results, NexLev seed details)")
A("- Tools: `data/tools/yt_allsorts.py`, `vid_next_batch.py`, `sc_build.py`, `sc_seeds.py` (`vid_exact.py` is the watch-page attempt that was blocked)")
open(out_md, "w").write("\n".join(md) + "\n")
json.dump([v["id"] for v in gen], open(os.path.join(raw, "silver-cymbal", "excluded-generator-ids.json"), "w"))
print("seeds", len(rows), "median", statistics.median(sv), "medmult", statistics.median(sm), "2x+", n2, "gen", len(gen), "lf 2x+", sum(1 for m in lfm if m >= 2))
