#!/usr/bin/env python3
"""Round 4 build (2026-10-26, main session): turns the hand labels into deliverables 3, 4 and the format/villain
tables. Reads raw/round4/batch-N.csv (the titles with views, multiple, tier, type, last-12-months flag) and
raw/round4/labels-N.csv (the labellers' readings), N = 1..8.

Writes:
  raw/round4/labels-all-2026-10-26.csv   one row per video (calibration rows: the majority reading)
  raw/round4/calibration-2026-10-26.json the 40 calibration titles: every labeller's reading, agreement per field
  round4/labels-summary.md                agreement, counts, and the build notes
  emotions.md                             deliverable 4: emotions per sub-niche
  subniches.md                            deliverable 3 rebuilt from the hand labels (the rule-based version is
                                          kept as round3/subniches-rule-based-2026-10-26.md)
  formats.md                              formats and villains from the hand labels

Views are the Videos-tab figures (rounded) and dates approximate; the multiple is views / that channel's baseline
(census, labels.md section 6). Only scope_ok = y rows are counted. Labels are readings.
Usage: python3 -I round4_build.py"""
import csv, json, os, re, statistics
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(os.path.dirname(HERE), "raw")
STUDY = os.path.dirname(os.path.dirname(HERE))
R4 = os.path.join(RAW, "round4")

EMO = {"E1": "fear of the big bill", "E2": "resentment of the service call", "E3": "distrust of the store shelf",
       "E4": "dread of silent, hidden damage", "E5": "emergency dread and urgency", "E6": "frustration of failed attempts",
       "E7": "disgust", "E8": "satisfaction of the clear payoff", "E9": "embarrassment and household shame",
       "E10": "insider curiosity", "E11": "being let in", "E12": "vindication and the myth-bust",
       "E13": "pride in self-reliance", "E14": "relief and reassurance", "E15": "nostalgia and inherited wisdom",
       "E16": "protectiveness", "E17": "safety fear", "E18": "rule-curiosity and mild defiance", "E19": "comfort",
       "E20": "new-gadget wonder"}
MIN_N = 50  # round 6 check: ranking needs 50+ videos (was 15)
MIN_BASE = 100  # round 6 check: multiples only for channels whose baseline is 100+ views


def fnum(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return "n/a"
    if x >= 1e6: return f"{x / 1e6:.2f}M"
    if x >= 1e4: return f"{x / 1e3:.0f}K"
    if x >= 1e3: return f"{x / 1e3:.1f}K"
    return f"{x:.0f}"


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def md(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def load():
    meta, labs, calib = {}, {}, defaultdict(list)
    for n in range(1, 9):
        bf, lf = os.path.join(R4, f"batch-{n}.csv"), os.path.join(R4, f"labels-{n}.csv")
        if not os.path.exists(lf):
            continue
        b = list(csv.DictReader(open(bf, encoding="utf-8")))
        l = list(csv.DictReader(open(lf, encoding="utf-8")))
        if [r["video_id"] for r in b] != [r["video_id"] for r in l]:
            print(f"batch {n}: labels incomplete or out of order ({len(l)} of {len(b)}); skipped")
            continue
        for br, lr in zip(b, l):
            meta[br["video_id"]] = br
            lr = {k: (v or "").strip() for k, v in lr.items()}
            lr["batch"] = n
            if br["calib"] == "1":
                calib[br["video_id"]].append(lr)
            else:
                labs[br["video_id"]] = lr
    return meta, labs, calib


def majority(rows, field):
    c = Counter(r[field] for r in rows)
    v, k = c.most_common(1)[0]
    return v, k, len(rows)


def emoset(r):
    return {r[k] for k in ("e1", "e2", "e3") if r.get(k)}


def calibration(calib):
    out, agree = {}, defaultdict(list)
    for vid, rows in calib.items():
        rec = {"labellers": len(rows), "readings": rows}
        for f in ("scope_ok", "subniche", "format", "villain"):
            v, k, n = majority(rows, f)
            rec["majority_" + f] = v
            agree[f].append(k / n)
        e1 = Counter(r["e1"] for r in rows)
        rec["majority_e1"] = e1.most_common(1)[0][0]
        agree["e1"].append(e1.most_common(1)[0][1] / len(rows))
        allem = Counter(e for r in rows for e in emoset(r))
        rec["emotions_by_votes"] = allem.most_common()
        # share of labellers whose emotion set includes the most-voted emotion
        if allem:
            top = allem.most_common(1)[0][0]
            agree["top_emotion_present"].append(sum(1 for r in rows if top in emoset(r)) / len(rows))
        out[vid] = rec
    summary = {f: round(statistics.mean(v), 3) for f, v in agree.items() if v}
    return out, summary


def baseline(r):
    v, m = num(r["views"]), num(r["multiple"])
    return v / m if v and m else None


def stats(rows):
    """Median multiple and share at 2x+ use only videos whose channel baseline is MIN_BASE+ views (a 2-view baseline
    turns one video into 47,000x). top3 = share of the rows from the 3 channels with the most rows."""
    m = [num(r["multiple"]) for r in rows if num(r["multiple"]) is not None and (baseline(r) or 0) >= MIN_BASE]
    v = [num(r["views"]) for r in rows if num(r["views"]) is not None]
    cc = Counter(r["channel_id"] for r in rows)
    return {"n": len(rows), "channels": len(cc),
            "med_views": statistics.median(v) if v else None,
            "med_mult": statistics.median(m) if m else None, "n_mult": len(m),
            "share2x": (sum(1 for x in m if x >= 2) / len(m)) if m else None,
            "top3": (sum(c for _, c in cc.most_common(3)) / len(rows)) if rows else None}


def cells(s):
    mm = "n/a" if s["med_mult"] is None else f"{s['med_mult']:.2f}x"
    sh = "n/a" if s["share2x"] is None else f"{100 * s['share2x']:.0f}%"
    t3 = "n/a" if s.get("top3") is None else f"{100 * s['top3']:.0f}%"
    return f"{s['n']:,} | {s['channels']:,} | {t3} | {fnum(s['med_views'])} | {mm} | {sh}"


def examples(rows, k=3, min_views=1000, min_base=500):
    """Best examples by multiple: 1K+ views, and a channel baseline of 500+ views so tiny channels' 1,000x+
    outliers don't crowd the examples out."""
    rr = [r for r in rows if num(r["views"]) and num(r["views"]) >= min_views and (baseline(r) or 0) >= min_base]
    rr.sort(key=lambda r: -(num(r["multiple"]) or 0))
    out = []
    for r in rr[:k]:
        out.append(f"\"{md(r['title'])[:90]}\" ({md(r['channel'])}, {fnum(r['views'])}, {num(r['multiple']) or 0:.1f}x, `{r['video_id']}`)")
    return "<br>".join(out) or "-"


def biggest(rows, k=5):
    rr = sorted(rows, key=lambda r: -(num(r["views"]) or 0))[:k]
    return "<br>".join(f"\"{md(r['title'])[:90]}\" ({md(r['channel'])}, {fnum(r['views'])}, {num(r['multiple']) or 0:.1f}x, `{r['video_id']}`)" for r in rr) or "-"


def table(groups, title_col, recent_only=False):
    L = [f"| {title_col} | Videos | Channels | Top 3 channels' share | Median views | Median multiple | Share at 2x+ |", "|---|---:|---:|---:|---:|---:|---:|"]
    small = []
    items = []
    for k, rows in groups.items():
        rr = [r for r in rows if (r["last12m"] in ("yes", "1", "True", "true")) or not recent_only]
        if not rr: continue
        s = stats(rr)
        if k == "adjacent":
            small.append((k + " (not counted: labels.md)", s)); continue
        (items if s["n"] >= MIN_N else small).append((k, s))
    items.sort(key=lambda x: -(x[1]["med_mult"] or 0))
    for k, s in items:
        L.append(f"| {k} | {cells(s)} |")
    if small:
        L.append("")
        L.append(f"Not ranked (fewer than {MIN_N} videos, or not counted): " + "; ".join(
            f"{k} ({s['n']}, {'n/a' if s['med_mult'] is None else format(s['med_mult'], '.2f') + 'x'})" for k, s in sorted(small, key=lambda x: -x[1]['n'])))
    return L


HEATWORD = re.compile(r"\b(heat\w*|warm\w*|winter|room|house|home|cold|freez\w*|furnace|fireplace|radiator|bills?)\b", re.I)
STOVEBUILD = re.compile(r"\b(stoves?|burners?|heaters?)\b", re.I)
CRAFT = re.compile(r"\b(cement|concrete|bricks?|clay|mud|gas cylinders?|barrel|cans?|pot)\b", re.I)
TOPLIST = re.compile(r"\b(top \d+|\d+ best|best \d+|\d+ (most )?(reliable|worst)|brands? worth|worth buying)\b", re.I)


def harmonize(rows):
    """Round 6 check found two labeller habits that differ by batch; one rule for all batches (logged in the summary):
    1. a DIY stove/burner build with a craft word and no heat word in the title is set to scope '?' (most batches
       read these as cooking or craft stoves; two batches counted them in);
    2. a 'Top N / N best' list labelled only-x goes to the brand-verdict sub-niche (batch 2 filed these under the
       equipment). The original reading is kept in note."""
    n1 = n2 = 0
    for r in rows:
        t = r.get("title") or ""
        if r["scope_ok"] in ("y", "?", "n") and STOVEBUILD.search(t) and CRAFT.search(t) and not HEATWORD.search(t) \
                and r["subniche"] in ("offgrid-heat", "") and r["scope_ok"] != "?":
            r["note"] = (r.get("note") or "") + f" [harmonized: scope {r['scope_ok']} -> ?]"
            r["scope_ok"] = "?"; n1 += 1
        if r["scope_ok"] == "y" and r["format"] == "only-x" and TOPLIST.search(t) and r["subniche"] not in ("brand-verdict",):
            r["note"] = (r.get("note") or "") + f" [harmonized: sub-niche {r['subniche']} -> brand-verdict]"
            r["subniche"] = "brand-verdict"; n2 += 1
    HARMONIZED.update({"stove_builds_to_unsure": n1, "top_lists_to_brand_verdict": n2})


HARMONIZED = {}


def main():
    meta, labs, calib = load()
    cal, cal_sum = calibration(calib)
    rows = []
    for vid, m in meta.items():
        if vid in labs:
            l = labs[vid]
        elif vid in cal:
            c = cal[vid]
            l = {"scope_ok": c["majority_scope_ok"], "subniche": c["majority_subniche"], "format": c["majority_format"],
                 "villain": c["majority_villain"], "note": "calibration majority"}
            em = [e for e, _ in c["emotions_by_votes"] if _ >= max(2, c["labellers"] / 2)][:3]
            l.update({"e1": em[0] if len(em) > 0 else "", "e2": em[1] if len(em) > 1 else "", "e3": em[2] if len(em) > 2 else ""})
        else:
            continue
        r = dict(m)
        r.update({k: l.get(k, "") for k in ("scope_ok", "subniche", "format", "e1", "e2", "e3", "villain", "note")})
        r["labeller_batch"] = l.get("batch", "calibration")
        rows.append(r)
    cols = list(rows[0].keys())
    with open(os.path.join(R4, "labels-all-2026-10-26.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    json.dump({"agreement": cal_sum, "titles": cal}, open(os.path.join(R4, "calibration-2026-10-26.json"), "w"), indent=1)

    harmonize(rows)
    ins = [r for r in rows if r["scope_ok"] == "y"]
    rec = [r for r in ins if r["last12m"] in ("yes", "1", "True", "true")]
    scope = Counter(r["scope_ok"] for r in rows)
    batches_done = sorted({r["labeller_batch"] for r in rows if r["labeller_batch"] != "calibration"})

    by_sn = defaultdict(list)
    for r in ins: by_sn[r["subniche"]].append(r)
    by_fmt = defaultdict(list)
    for r in ins: by_fmt[r["format"]].append(r)
    by_vil = defaultdict(list)
    for r in ins: by_vil[r["villain"]].append(r)
    by_emo = defaultdict(list)
    for r in ins:
        for e in emoset(r): by_emo[e].append(r)

    head = (f"Built {__import__('datetime').date.today().isoformat()} by `data/tools/round4_build.py` from the round 4 hand labels "
            f"(batches done: {', '.join(map(str, batches_done))} of 8). {len(rows):,} titles labelled; scope y {scope['y']:,}, "
            f"n {scope['n']:,}, ? {scope['?']:,}. Only the {len(ins):,} in-scope (y) videos are counted; {len(rec):,} of them are "
            f"from the last 12 months. Views are Videos-tab figures (rounded), dates approximate; the multiple is views / the "
            f"channel's baseline (`channels.md`). **Every label is a reading from the title only.** Agreement between the 8 "
            f"labellers on 40 shared titles: scope {cal_sum.get('scope_ok', 0):.0%}, sub-niche {cal_sum.get('subniche', 0):.0%}, "
            f"format {cal_sum.get('format', 0):.0%}, villain {cal_sum.get('villain', 0):.0%}, first emotion {cal_sum.get('e1', 0):.0%}, "
            f"the most-voted emotion present {cal_sum.get('top_emotion_present', 0):.0%} (average share of labellers agreeing with the majority).\n")

    # ---- emotions.md (deliverable 4)
    L = ["# Emotions in each HVAC sub-niche (deliverable 4)\n", head,
         "## Emotions across the niche\n",
         "**Read the last-12-months columns first.** The multiple compares a video's lifetime views with its channel's "
         "recent typical video, so old videos (years of views) score high whatever their emotion; within the last 12 months "
         "that age effect is much smaller.\n",
         "| Emotion | Last 12 months: videos | Channels | Top 3 channels' share | Median views | Median multiple | Share at 2x+ | All time: videos / median multiple | Best examples (by multiple; 1K+ views, channel baseline 500+) |",
         "|---|---:|---:|---:|---:|---:|---:|---|---|"]
    rec_ids = {r["video_id"] for r in rec}
    for e in sorted(by_emo, key=lambda e: -(stats([r for r in by_emo[e] if r["video_id"] in rec_ids] or [{"multiple": None, "views": None, "channel_id": ""}])["med_mult"] or 0)):
        s = stats(by_emo[e]); rr = [r for r in by_emo[e] if r["video_id"] in rec_ids]
        s12 = stats(rr) if rr else {"n": 0, "channels": 0, "med_views": None, "med_mult": None, "share2x": None, "top3": None}
        ma = "n/a" if s["med_mult"] is None else f"{s['med_mult']:.2f}x"
        L.append(f"| {e} {EMO.get(e, '')} | {cells(s12)} | {s['n']:,} / {ma} | {examples(rr or by_emo[e])} |")
    L.append("")
    ne = [r for r in ins if not emoset(r)]; ne12 = [r for r in ne if r["video_id"] in rec_ids]
    L.append(f"Videos with no emotion: {len(ne):,} all time (median multiple {stats(ne)['med_mult'] or 0:.2f}x); "
             f"{len(ne12):,} in the last 12 months (median multiple {(stats(ne12)['med_mult'] or 0) if ne12 else 0:.2f}x).\n")
    L.append("## Every emotion that matters, sub-niche by sub-niche\n")
    L.append(f"For each sub-niche with {MIN_N}+ videos: every emotion carried by at least 5% of its videos (and 5+ videos). "
             "'Lift' = the median multiple of the sub-niche's videos carrying the emotion divided by the sub-niche's own "
             "median multiple (1.00 = no difference); the 12-month lift needs 5+ videos. Examples from the last 12 months "
             "where there are any.\n")
    for sn in sorted(by_sn, key=lambda k: -len(by_sn[k])):
        rows_sn = by_sn[sn]
        if len(rows_sn) < MIN_N: continue
        s_sn = stats(rows_sn)
        L.append(f"### {sn} ({s_sn['n']:,} videos, median multiple {s_sn['med_mult'] or 0:.2f}x)\n")
        sn12 = [r for r in rows_sn if r["video_id"] in rec_ids]; s_sn12 = stats(sn12) if sn12 else None
        L.append(f"Last 12 months: {len(sn12):,} videos, median multiple {(s_sn12['med_mult'] or 0) if s_sn12 else 0:.2f}x.\n")
        L.append("| Emotion | Videos (all time) | Share | Lift all time | Videos (12 months) | Lift 12 months | Examples |")
        L.append("|---|---:|---:|---:|---:|---:|---|")
        ec = Counter(e for r in rows_sn for e in emoset(r))
        for e, c in ec.most_common():
            if c < 5 or c / len(rows_sn) < 0.05: continue
            rr = [r for r in rows_sn if e in emoset(r)]; rr12 = [r for r in rr if r["video_id"] in rec_ids]
            s = stats(rr); s12 = stats(rr12) if rr12 else None
            lift = (s["med_mult"] / s_sn["med_mult"]) if s["med_mult"] and s_sn["med_mult"] else None
            lift12 = (s12["med_mult"] / s_sn12["med_mult"]) if s12 and s12["n"] >= 5 and s12["med_mult"] and s_sn12 and s_sn12["med_mult"] else None
            L.append(f"| {e} {EMO.get(e, '')} | {c:,} | {100 * c / len(rows_sn):.0f}% | "
                     f"{'n/a' if lift is None else f'{lift:.2f}'} | {len(rr12):,} | {'n/a' if lift12 is None else f'{lift12:.2f}'} | {examples(rr12 or rr, 2)} |")
        L.append("")
    open(os.path.join(STUDY, "emotions.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    # ---- subniches.md (deliverable 3, rebuilt)
    L = ["# HVAC sub-niche map (deliverable 3, from the round 4 hand labels)\n", head,
         "The rule-based round 3 version is kept as `round3/subniches-rule-based-2026-10-26.md`.\n",
         "## All time\n"] + table(by_sn, "Sub-niche") + ["", "## Last 12 months\n"] + table(by_sn, "Sub-niche", True)
    L += ["", "## By channel tier (all time, median multiple, n)\n", "| Sub-niche | Tier A | Tier B | Tier C |", "|---|---|---|---|"]
    for sn in sorted(by_sn, key=lambda k: -len(by_sn[k])):
        if len(by_sn[sn]) < MIN_N: continue
        cs = []
        for t in "ABC":
            rr = [r for r in by_sn[sn] if r["tier"] == t]
            s = stats(rr) if rr else None
            cs.append("-" if not s else f"{s['med_mult'] or 0:.2f}x ({s['n']})")
        L.append(f"| {sn} | " + " | ".join(cs) + " |")
    L += ["", "## By channel type (all time, median multiple, n)\n", "| Sub-niche | Faceless persona | Faceless | On camera |", "|---|---|---|---|"]
    for sn in sorted(by_sn, key=lambda k: -len(by_sn[k])):
        if len(by_sn[sn]) < MIN_N: continue
        cs = []
        for t in ("faceless persona", "faceless", "on camera"):
            rr = [r for r in by_sn[sn] if (r.get("type") or "") == t]
            s = stats(rr) if rr else None
            cs.append("-" if not s else f"{s['med_mult'] or 0:.2f}x ({s['n']})")
        L.append(f"| {sn} | " + " | ".join(cs) + " |")
    L += ["", "## Biggest videos per sub-niche\n", "| Sub-niche | Top channels (videos) | 5 biggest (views, multiple) |", "|---|---|---|"]
    for sn in sorted(by_sn, key=lambda k: -len(by_sn[k])):
        tc = Counter(r["channel"] for r in by_sn[sn]).most_common(3)
        L.append(f"| {sn} | " + "; ".join(f"{md(c)} ({n})" for c, n in tc) + f" | {biggest(by_sn[sn])} |")
    open(os.path.join(STUDY, "subniches.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    # ---- formats.md (formats and villains)
    L = ["# Formats and villains (from the round 4 hand labels)\n", head,
         "The rule-based keyword-sweep version is `round2/formats.md`.\n", "## Formats, all time\n"] + table(by_fmt, "Format")
    L += ["", "## Formats, last 12 months\n"] + table(by_fmt, "Format", True)
    L += ["", "## Formats by channel type (all time, median multiple, n)\n", "| Format | Faceless persona | Faceless | On camera |", "|---|---|---|---|"]
    for k in sorted(by_fmt, key=lambda k: -len(by_fmt[k])):
        cs = []
        for t in ("faceless persona", "faceless", "on camera"):
            rr = [r for r in by_fmt[k] if (r.get("type") or "") == t]
            s = stats(rr) if rr else None
            cs.append("-" if not s else f"{s['med_mult'] or 0:.2f}x ({s['n']})")
        L.append(f"| {k} | " + " | ".join(cs) + " |")
    L += ["", "## Best examples per format (by multiple, 1K+ views)\n", "| Format | Examples |", "|---|---|"]
    for k in sorted(by_fmt, key=lambda k: -len(by_fmt[k])):
        L.append(f"| {k} | {examples(by_fmt[k])} |")
    L += ["", "## Villains, all time\n"] + table(by_vil, "Villain")
    L += ["", "## Villains, last 12 months\n"] + table(by_vil, "Villain", True)
    L += ["", "## Villain examples (by multiple, 1K+ views)\n", "| Villain | Examples |", "|---|---|"]
    for k in sorted(by_vil, key=lambda k: -len(by_vil[k])):
        L.append(f"| {k} | {examples(by_vil[k])} |")
    open(os.path.join(STUDY, "formats.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    # ---- summary
    L = ["# Round 4 labels: summary\n", head,
         f"**Round 6 changes (2026-10-26, after `round6/check-labels.md`):** ranking needs {MIN_N}+ videos; 'adjacent' is listed but not ranked; "
         f"median multiples and 2x shares use only channels whose baseline is {MIN_BASE}+ views; a top-3-channels share column shows concentration; "
         f"two labeller habits harmonized by rule: {HARMONIZED.get('stove_builds_to_unsure', 0)} craft stove builds with no heat word set to '?', "
         f"{HARMONIZED.get('top_lists_to_brand_verdict', 0)} 'Top N / N best' lists moved to brand-verdict. The blind re-label of 200 titles "
         "agreed 88% on scope, 90% sub-niche, 88% format, 95% villain, 68% first emotion (77% where both gave one).\n",
         "## Calibration (40 titles, every labeller)\n",
         "| Field | Average share agreeing with the majority |", "|---|---:|"]
    for f, v in cal_sum.items():
        L.append(f"| {f} | {v:.0%} |")
    L += ["", "## Counts (in scope)\n", "| Field | Top values |", "|---|---|"]
    for f in ("subniche", "format", "villain"):
        L.append(f"| {f} | " + "; ".join(f"{k} {v:,}" for k, v in Counter(r[f] for r in ins).most_common(12)) + " |")
    L.append("| emotions | " + "; ".join(f"{k} {v:,}" for k, v in Counter(e for r in ins for e in emoset(r)).most_common(20)) + " |")
    os.makedirs(os.path.join(STUDY, "round4"), exist_ok=True)
    open(os.path.join(STUDY, "round4", "labels-summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(json.dumps({"rows": len(rows), "in_scope": len(ins), "recent": len(rec), "batches": batches_done, "agreement": cal_sum}))


if __name__ == "__main__":
    main()
