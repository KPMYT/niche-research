#!/usr/bin/env python3
"""Build the study's readable deliverables from the checked CSVs (re-run after any data fix).
Writes in studies/electrical/: top-100.md + top-100.csv, recent-winners.md, subniches.md, emotions.md, keyword-sweep.md, formats.md."""
import csv, os, re, statistics
from collections import defaultdict, Counter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
S = os.path.join(D, "..")
def rd(p): return list(csv.DictReader(open(os.path.join(D, p))))
def num(x):
    try: return int(float(str(x).replace(",", "")))
    except: return None
def fmt(n): return f"{n:,}" if isinstance(n, int) else (n or "")
def esc(t): return (t or "").replace("|", "/").strip()
def secs(l):
    p = [int(x) for x in re.findall(r"\d+", l or "")]
    return p[0]*3600+p[1]*60+p[2] if len(p) == 3 else (p[0]*60+p[1] if len(p) == 2 else None)

med = {r["channel_id"]: float(r["median"]) for r in rd("medians/channel-medians.csv") if r["median"]}
def mult(cid, v):
    m = med.get(cid)
    return round(v / m, 1) if (m and m >= 200 and v is not None) else ""
EMO = {"E1": "fear of the big bill", "E2": "resentment of the service call", "E3": "distrust of the store shelf", "E4": "dread of hidden damage",
       "E5": "emergency dread", "E6": "frustration of failed attempts", "E7": "disgust", "E8": "satisfaction of the clear payoff",
       "E9": "embarrassment / doing it wrong", "E10": "insider curiosity", "E11": "being let in", "E12": "vindication / myth-bust",
       "E13": "pride in self-reliance", "E14": "relief and reassurance", "E15": "nostalgia / old houses", "E16": "protectiveness",
       "E17": "safety fear", "E18": "rule-curiosity / defiance", "N1": "nuisance irritation (NEW)", "N2": "how-it-works curiosity (NEW)",
       "N3": "spectacle and thrill (NEW)", "N4": "comeuppance (NEW)"}
ROBUST = {"E3", "E9", "E12", "E1", "N1", "E13", "E17", "E8", "E18"}; RANGE = {"E15", "E4", "N2"}
labels = {}
for g in ["A", "B", "C", "extra"]:  # extra = 4 top-100 videos labelled by the main session after checker G
    for r in rd(f"labels/labelled-{g}.csv"): labels[r["video_id"]] = r

# ---------- top 100 ----------
top = rd("top100/top100-final.csv"); narr = rd("top100/top100-narrated.csv")
rows = []
for r in top:
    v = num(r["views"]); L = labels.get(r["video_id"], {})
    rows.append({**r, "multiple": mult(r["channel_id"], v), "emotions": L.get("emotions", ""), "villain": L.get("villain", ""),
                 "format_r4": L.get("format_r4", "") or r["format"]})
with open(os.path.join(S, "top-100.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rows)
o = ["# The top 100 of all time (deliverable 7)", "",
     "Long-form (5:00+), English, in scope (homeowner electrical and fire safety), ranked by exact views (`yt.py video`, 2026-10-26). Built from the round 2 sweeps (212 keywords) plus 23 broad searches, then every row re-checked (checker E). Source: `data/top100/top100-final.csv`; this table with labels: `top-100.csv`.", "",
     "- **Multiple** = views ÷ the channel's median long-form video (last 12 months, or last 30); blank where the channel's median is under 200 views or unknown. Search finds a channel's winners, so multiples run high.",
     "- **Emotions, villain, format** are readings (round 4; checker F: first emotion 78% consistent; see `labels.md` for which emotions are robust).",
     "- **Narrated = n**: an unnarrated \"hack\" or hands-only channel. A narrated persona channel can't copy that format; `data/top100/top100-narrated.csv` is the top 100 without them.", "",
     "| # | Title | Channel | Views | Uploaded | Length | Sub-niche | Format | Emotions | Villain | Multiple | Narrated |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    o.append(f"| {r['rank']} | [{esc(r['title'])}](https://www.youtube.com/watch?v={r['video_id']}) | {esc(r['channel'])} | {fmt(num(r['views']))} | {r['upload_date']} | {r['length']} | {r['subniche']} | {r['format_r4']} | {r['emotions']} | {r['villain']} | {r['multiple']} | {r['narrated'][:1]} |")
sc = Counter(r["subniche"] for r in rows); fc = Counter(r["format_r4"] for r in rows)
ec = Counter(e for r in rows for e in r["emotions"].split()); vc = Counter(r["villain"] for r in rows if r["villain"])
o += ["", "## Counts within the top 100", "", "| Sub-niche | Videos |", "|---|---|"] + [f"| {k} | {n} |" for k, n in sc.most_common()]
o += ["", "| Format | Videos |", "|---|---|"] + [f"| {k} | {n} |" for k, n in fc.most_common()]
o += ["", "| Emotion (any position; reading) | Videos |", "|---|---|"] + [f"| {k} {EMO.get(k,'')} | {n} |" for k, n in ec.most_common()]
o += ["", "| Villain (reading) | Videos |", "|---|---|"] + [f"| {k} | {n} |" for k, n in vc.most_common()]
nn = sum(1 for r in rows if r["narrated"].startswith("n"))
o += ["", f"{nn} of the 100 are unnarrated hack / hands-only videos. Without them the #100 cut-off is {fmt(num(narr[-1]['views']))} (with them {fmt(num(rows[-1]['views']))})."]
open(os.path.join(S, "top-100.md"), "w").write("\n".join(o) + "\n")

# ---------- recent winners ----------
def table(L, title):
    t = [f"## {title}", "", "| # | Title | Channel | Views | Uploaded | Length | Sub-niche | Format | Emotions | Multiple |", "|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(L, 1):
        v = num(r["views"]); Lb = labels.get(r["video_id"], {})
        t.append(f"| {i} | [{esc(r['title'])}](https://www.youtube.com/watch?v={r['video_id']}) | {esc(r['channel'])} | {fmt(v)} | {r['upload_date']} | {r.get('length','')} | {r['subniche']} | {Lb.get('format_r4') or r['format']} | {Lb.get('emotions','')} | {mult(r['channel_id'], v)} |")
    return t
r90 = rd("top100/recent-90d.csv"); r12 = rd("top100/recent-12mo.csv")
m = rd("merged/videos-with-multiples.csv")
# rising / falling: share of each sub-niche and format among videos under 12 months old vs older, with median multiple
def recent(age):
    a = (age or "").lower()
    if re.match(r"\d{4}-\d{2}-\d{2}", a): return a >= "2025-10-26"
    try:  # "Dec 28, 2025" (fixed after checker G: these were counted as older)
        import datetime
        return datetime.datetime.strptime((age or "").strip(), "%b %d, %Y").date() >= datetime.date(2025, 10, 26)
    except ValueError: pass
    if re.search(r"\d+\s*(y|year)", a): return False
    return bool(re.search(r"\d+\s*(mo|month|w|week|d|day|h|hour)", a))
def rf(key):
    d = defaultdict(lambda: {"new": [], "old": []})
    for r in m:
        k = (r[key] or "").split(";")[0].replace("other:", "")
        d[k]["new" if recent(r["age_or_date"]) else "old"].append(r)
    N = sum(len(x["new"]) for x in d.values()); O = sum(len(x["old"]) for x in d.values())
    res = []
    for k, x in d.items():
        if len(x["new"]) + len(x["old"]) < 25: continue
        mn = [float(r["multiple"]) for r in x["new"] if r["multiple"]]; mo = [float(r["multiple"]) for r in x["old"] if r["multiple"]]
        vn = [num(r["views"]) for r in x["new"] if num(r["views"]) is not None]; vo = [num(r["views"]) for r in x["old"] if num(r["views"]) is not None]
        res.append((k, len(x["new"]), 100*len(x["new"])/N, 100*len(x["old"])/O, int(statistics.median(vn)) if vn else "", int(statistics.median(vo)) if vo else "",
                    round(statistics.median(mn), 1) if mn else "", round(statistics.median(mo), 1) if mo else ""))
    res.sort(key=lambda t: -(t[2] - t[3]))
    t = [f"| {key} | Videos under 12 months | Share of recent videos | Share of older videos | Median views, recent | Median views, older | Median multiple, recent | Median multiple, older |", "|---|---|---|---|---|---|---|---|"]
    for k, n, sn, so, vn, vo, mn, mo in res: t.append(f"| {k} | {n} | {sn:.1f}% | {so:.1f}% | {fmt(vn)} | {fmt(vo)} | {mn} | {mo} |")
    return t
o = ["# What has worked recently (deliverable 6)", "",
     "Exact views and upload dates (`yt.py video`, 2026-10-26); in scope and English, re-checked by checker E (20 rows of each list). Sources: `data/top100/recent-90d.csv`, `recent-12mo.csv`. Emotions are readings (round 4). Multiple as in `top-100.md`.", "",
     "**The 90-day list thins fast:** below #2 the views are low (#50 has 68,777)."] + [""]
o += table(r90, "Top 50 of the last 90 days (uploaded 2026-07-28 or later)") + [""] + table(r12, "Top 50 of the last 12 months (uploaded 2025-10-26 or later)")
o += ["", "## Rising and falling against all-time", "",
      "From the 4,758 merged sweep videos, split by age (under 12 months against older; relative ages from search pages). A sub-niche or format is \"rising\" when its share of recent videos is above its share of older ones. Read with care: recent videos have had less time to gather views, so recent medians are naturally lower; compare shares and multiples more than raw views. Many recent videos come from tiny new channels, which pulls recent medians down further.", ""]
o += ["### Sub-niches", ""] + rf("subniche") + ["", "### Formats", ""] + rf("format")
open(os.path.join(S, "recent-winners.md"), "w").write("\n".join(o) + "\n")

# ---------- sub-niche map ----------
sm = rd("merged/subniche-map.csv")
o = ["# The sub-niche map (deliverable 3)", "",
     "From the 4,758 unique in-scope long-form videos found by the round 2 sweeps (212 keywords, four sorts each), after two checkers' corrections (`data/merged/corrections.csv`). Views are search-page exact counts (2026-10-24). Source: `data/merged/subniche-map.csv`; per-video data `data/merged/videos-with-multiples.csv`.", "",
     "- **Typical views** = the median video in the sub-niche. **Multiple** = views ÷ the channel's median long-form video (2,674 videos have one; channels whose median is under 200 views are left out). **Share at 2x+** = videos at least twice their channel's median.",
     "- **Caveat:** search returns each channel's winners, so multiples and 2x shares run high everywhere. Compare sub-niches with each other; don't read them as absolute.",
     "- Sub-niche labels are readings of titles.", "",
     "| Sub-niche | Videos | Channels | Typical views | Videos 1M+ | Median multiple | Share at 2x+ | Biggest videos |", "|---|---|---|---|---|---|---|---|"]
for r in sm: o.append(f"| {r['subniche']} | {r['videos']} | {r['channels']} | {fmt(num(r['median_views']))} | {r['videos_1M_plus']} | {r['median_multiple']} | {r['share_2x_plus']} | {esc(r['biggest'])} |")
open(os.path.join(S, "subniches.md"), "w").write("\n".join(o) + "\n")

# ---------- emotions ----------
by = defaultdict(list)
for r in labels.values(): by[r["subniche"]].append(r)
o = ["# Emotions in each sub-niche (deliverable 4)", "",
     "1,007 videos labelled with up to three emotions (round 4): the top 100, both recent lists, and per sub-niche its top 30 by views plus 10 random others (so the typical video shows, not just winners). Labels are **readings** of titles (and thumbnails for the top 100 and recent winners), not counts. Sources: `data/labels/labelled-A/B/C.csv`.", "",
     "**How far to trust them (checker F, a blind re-label of 90 rows):** first emotion 78% the same, any emotion shared 98%, villain 92%. Robust enough to count: E3, E9, E12, E1, N1, E13, E17, E8, E18. Report as a range: E15, E4, N2. **Only \"present\", never a count or rank:** E10, E11, E6, E16, E5 (marked * below). E13 (self-reliance) and N2 (how-it-works) largely mirror the format (how-to, explainer). New emotions N1-N4 are defined in `labels.md`.", "",
     "In each table: videos carrying the emotion in any position / as the first emotion; median views of those videos (the sample mixes top-30 and random rows, so medians describe the sample); one example.", ""]
allc = Counter()
for sub in sorted(by, key=lambda s: -len(by[s])):
    L = by[sub]; c_any = Counter(); c_first = Counter(); views = defaultdict(list); ex = {}
    for r in L:
        es = r["emotions"].split()
        for i, e in enumerate(es):
            c_any[e] += 1; allc[e] += 1
            if i == 0: c_first[e] += 1
            v = num(r["views"])
            if v is not None: views[e].append(v)
            if e not in ex or (num(r["views"]) or 0) > (num(ex[e]["views"]) or 0): ex[e] = r
    vil = Counter(r["villain"] for r in L)
    o += [f"## {sub} ({len(L)} labelled videos)", "", "| Emotion | Any / first | Median views | Biggest example |", "|---|---|---|---|"]
    for e, n in c_any.most_common():
        if n < 3: continue
        star = "*" if e not in ROBUST | RANGE else ("~" if e in RANGE else "")
        o.append(f"| {e}{star} {EMO.get(e,'')} | {n} / {c_first[e]} | {fmt(int(statistics.median(views[e]))) if views[e] else ''} | {esc(ex[e]['title'])} ({esc(ex[e]['channel'])}, {fmt(num(ex[e]['views']))}) |")
    o += ["", "Villains: " + ", ".join(f"{k} {n}" for k, n in vil.most_common()), ""]
o += ["## All 1,007", "", "| Emotion | Videos (any position) |", "|---|---|"] + [f"| {e} {EMO.get(e,'')} | {n} |" for e, n in allc.most_common()]
o += ["", "* = not robust (report only as present). ~ = report as a range."]
open(os.path.join(S, "emotions.md"), "w").write("\n".join(o) + "\n")

# ---------- keyword sweep + formats ----------
o = ["# The keyword sweep (deliverable 8)", "",
     "Round 2 (2026-10-24): six topic groups; every keyword searched by relevance (2 pages), most viewed (3), most viewed this year (2) and this month (1); the strongest five per group also over-20-minutes. **Sort checks:** YouTube's \"upload date\" sort no longer sorts by date, so \"newest\" used the date windows (this week / month / year), which filter correctly; YouTube search has **no \"oldest\" sort**, so \"oldest\" came from channels' Oldest tabs. Round 3 added 38 investigator keywords and 23 broad top-100 searches. Raw pages are in each group's `raw/`.", ""]
total = 0
for g in ["wiring", "panels", "cords", "devices", "fire", "explainers"]:
    K = rd(f"sweep/{g}/keywords.csv"); total += len(K)
    o += [f"## {g} ({len(K)} keywords)", "", "| Keyword | Source | Sorts run | Relevant long-form | Relevant under 5:00 |", "|---|---|---|---|---|"]
    for k in K:
        kk = k.get("keyword") or list(k.values())[0]
        o.append(f"| {esc(kk)} | {esc(k.get('source',''))} | {esc(k.get('sorts_run',''))} | {k.get('relevant_long','')} | {k.get('relevant_short','')} |")
    o.append("")
inv = rd("investigator/keywords.csv")
o += [f"## Investigator angle (round 3; {len(inv)} keyword/sort rows)", "", "See `data/investigator/keywords.csv`.", "", f"**Total: {total} round 2 keywords.** Formats that keep coming up, with counts and performance: `formats.md`."]
open(os.path.join(S, "keyword-sweep.md"), "w").write("\n".join(o) + "\n")
fm = rd("merged/format-map.csv")
o = ["# Formats (deliverable 8, second part)", "",
     "Every in-scope long-form video from the sweep, by title format (round 2 labels, readings; definitions in `labels.md`). Typical views = median; multiple and 2x share as in `subniches.md` (inflated by search; compare formats with each other). The top 100's formats (round 4 labels) are in `top-100.md`.", "",
     "| Format | Videos | Typical views | Videos 1M+ | Median multiple | Share at 2x+ | Biggest videos |", "|---|---|---|---|---|---|---|"]
for r in fm:
    if int(r["videos"]) < 10: continue
    o.append(f"| {r['format']} | {r['videos']} | {fmt(num(r['median_views']))} | {r['videos_1M_plus']} | {r['median_multiple']} | {r['share_2x_plus']} | {esc(r['biggest'])} |")
o += ["", "Labels from different helpers that mean the same thing (inspection-walk / inspection-walkthrough; never-list / insider-never; explainer / explainer fallback) appear as separate rows here; read them together."]
open(os.path.join(S, "formats.md"), "w").write("\n".join(o) + "\n")
print("built: top-100.md/.csv, recent-winners.md, subniches.md, emotions.md, keyword-sweep.md, formats.md")
