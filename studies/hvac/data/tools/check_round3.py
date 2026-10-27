#!/usr/bin/env python3
"""Round 3 checker (2026-10-26): independent recomputation helpers for check-round3.md.
Written by the round 3 checker. Does NOT import census_build.py (independent re-implementation).
Usage: python3 -I check_round3.py census <dir_with_yt_allsorts_json>   -> JSON summary per channel to stdout
       python3 -I check_round3.py titles <file.json>                    -> latest 30 long-form titles (for hand reading)
"""
import json, re, statistics, sys, glob, os

AGE = re.compile(r"^(\d+)\s*(second|minute|hour|day|week|month|year|min|h|d|w|mo|y)s?\s+ago$")


def age(meta):
    for p in reversed(meta or []):
        m = AGE.match(p.replace("\xa0", " ").strip())
        if m:
            u = {"second": "min", "minute": "min", "hour": "h", "day": "d", "week": "w", "month": "mo", "year": "y"}.get(m.group(2), m.group(2))
            return int(m.group(1)), u, p.strip()
    return None


def dur(s):
    if not s or not re.match(r"^\d+(:\d+){1,2}$", s):
        return None
    t = 0
    for x in s.split(":"):
        t = t * 60 + int(x)
    return t


def in12(a):
    n, u, _ = a
    return u in ("min", "h", "d", "w") or (u == "mo" and n <= 11)


def in90(a):
    n, u, _ = a
    return u in ("min", "h", "d", "w") or (u == "mo" and n <= 2)


def load(f):
    d = json.load(open(f))
    s = d["sorts"]
    lat = s.get("Latest") if s.get("Latest") is not None and len(s["Latest"]) >= len(s.get("Latest_initialpage") or []) else (s.get("Latest_initialpage") or [])
    return d, lat, s


def summarize(f):
    d, lat, s = load(f)
    longs = []
    for it in lat:
        a = age(it.get("meta")); du = dur(it.get("dur"))
        if du is not None and du >= 300 and a:
            longs.append({"id": it["id"], "title": it["title"], "views": it.get("views_tab"), "age": a[2], "a": a, "dur": it.get("dur")})
    l12 = [v for v in longs if in12(v["a"]) and v["views"] is not None]
    if len(l12) >= 10:
        rule, bs = "12M", l12
    else:
        rule, bs = "last30", [v for v in longs if v["views"] is not None][:30]
    base = statistics.median([v["views"] for v in bs]) if bs else None
    u90 = sum(1 for v in longs if in90(v["a"]))
    # top long-form by views across all sorts
    allv = {}
    for k, lst in s.items():
        for it in (lst or []):
            du = dur(it.get("dur"))
            if du is not None and du >= 300 and it.get("views_tab") is not None:
                allv[it["id"]] = it
    top = sorted(allv.values(), key=lambda x: -x["views_tab"])[:1]
    return {"id": d.get("id"), "channel": d.get("channel"), "subs": d.get("subs"), "videos": d.get("videos"),
            "pulled": d.get("pulled"), "latest_n": len(lat), "longform_in_latest": len(longs),
            "latest30_long": [(v["id"], v["title"], v["dur"], v["age"], v["views"]) for v in longs[:30]],
            "newest10": [v["title"] for v in longs[:10]],
            "baseline_rule": rule, "baseline_n": len(bs), "baseline": base, "uploads_90d_long": u90,
            "top": (top[0]["id"], top[0]["title"], top[0]["views_tab"]) if top else None,
            "popular_top10": [(it["id"], it["title"], it.get("dur")) for it in (s.get("Popular") or [])[:10]]}


if __name__ == "__main__":
    if sys.argv[1] == "census":
        out = [summarize(f) for f in sorted(glob.glob(os.path.join(sys.argv[2], "UC*.json")))]
        json.dump(out, sys.stdout, indent=1)
    elif sys.argv[1] == "titles":
        r = summarize(sys.argv[2])
        print("##", r["channel"], r["id"], r["subs"], r["videos"], "long in latest:", r["longform_in_latest"])
        for i, t in enumerate(r["latest30_long"]):
            print(i + 1, t[2], t[3], "|", t[1])
        print("-- popular top10:")
        for t in r["popular_top10"]:
            print("   ", t[2], "|", t[1])
