#!/usr/bin/env python3
"""Ray Dutton's Garage copycat check (deliverable 2, HVAC round 3, 2026-10-26).

Finds titles in every census channel's long-form list (data/raw/census-videos-2026-10-26.csv, all tiers) that
(a) match one of Ray's title templates (regex, list below), or (b) are 0.70+ similar (difflib ratio, lower-cased)
to one of Ray's 12 most-viewed long-form titles, and channel names that echo his ("<Name>'s Garage", a "Ray"
persona). It writes the match list and the video IDs to pull exactly (innertube /next), so who came first is
decided on exact upload dates, not the tab's age text.

Usage: python3 -I new_channels_copycats.py <matches_out.json> <ids_out.txt>
"""
import csv, json, re, sys, os, difflib, collections

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))
RAY = "UCvcKEgZcY9ZgEULZouaNAOA"
csv.field_size_limit(10**9)

# Ray's title templates: (key, regex on the lower-cased title, Ray's example video IDs)
TEMPLATES = [
    ("T1 'Before you X this fall, do this (or pay for it ...)'", r"or pay (for it|the price)", ["dOZ-8__G4uU", "fHAlfm21vYw", "9MbOdR2x0N8", "AglSKzOY2E8"]),
    ("T2 'N X mistakes [company] hope you keep making'", r"(hope|want|wish|happy)( you)? (you )?(keep|are happy you keep) making|hope you keep making", ["qbWN3OViWxQ", "wZk06FJWMlM", "FKpbCUt26W0"]),
    ("T3 'The $30 filter is destroying your HVAC system (here's why)'", r"\$\d+ .*filter.* (is |that'?s )?(destroying|ruining)", ["_ZgVjFpBnQA", "MoB-obRdbro"]),
    ("T4 'The 5 thermostat habits that wear out your AC years early'", r"habits? (that )?(are )?(wear|wearing|ruin|kill|quietly wearing)\w* (out )?your", ["K2jCz3D5z_0"]),
    ("T5 'What to set your thermostat to this winter (68 is not for everyone)'", r"what to set your thermostat to", ["H0MBgMMzmyg"]),
    ("T6 'Why 70 degrees feels cold in your house every winter (it's not the furnace)'", r"\d+ degrees (still )?feels? cold|it'?s not the furnace", ["GKizclJLSq0"]),
    ("T7 'You're cleaning your AC wrong (and it's costing you)'", r"you'?re (cleaning|running|using) your .* wrong", ["UdyqMC1GVxQ"]),
    ("T8 'Top 5 things your AC companies don't want you to know how to do'", r"companies (don'?t|do not) want you (to know|knowing|to learn)", ["sMMZZiiD4NI"]),
]
NAME_RX = re.compile(r"'s garage|\bgarage\b|\bray\b|dutton", re.I)


def main():
    out_json, out_ids = sys.argv[1], sys.argv[2]
    ch = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(RAW, "census-channels-2026-10-26.csv")))}
    V = list(csv.DictReader(open(os.path.join(RAW, "census-videos-2026-10-26.csv"))))
    ray = [v for v in V if v["channel_id"] == RAY]
    raytop = sorted(ray, key=lambda v: -int(v["views_tab"] or 0))[:12]
    matches = collections.defaultdict(list)
    for v in V:
        if v["channel_id"] == RAY:
            continue
        t = v["title"].lower()
        why = []
        for key, rx, _ in TEMPLATES:
            if re.search(rx, t):
                why.append(key.split(" ")[0])
        for rv in raytop:
            sm = difflib.SequenceMatcher(None, t, rv["title"].lower())
            if sm.real_quick_ratio() >= 0.70 and sm.quick_ratio() >= 0.70:
                s = sm.ratio()
                if s >= 0.70:
                    why.append(f"SIM {s:.2f} to {rv['video_id']}")
        if why:
            matches[v["channel_id"]].append({"video_id": v["video_id"], "title": v["title"], "views_tab": v["views_tab"],
                                             "age_text": v["age_text"], "approx_date": v["approx_date"], "why": why})
    name_hits = [cid for cid, r in ch.items() if cid != RAY and NAME_RX.search(r["name"])]
    res = {"pulled_from": "census-videos-2026-10-26.csv / census-channels-2026-10-26.csv (Videos tabs pulled 2026-10-26)",
           "templates": [{"key": k, "regex": rx, "ray_examples": ex} for k, rx, ex in TEMPLATES],
           "ray_top12": [{"video_id": v["video_id"], "title": v["title"], "views_tab": v["views_tab"]} for v in raytop],
           "title_matches": {cid: {"name": ch[cid]["name"].strip(), "handle": ch[cid]["handle"], "tier": ch[cid]["tier"],
                                   "videos": L} for cid, L in matches.items()},
           "name_matches": {cid: {"name": ch[cid]["name"].strip(), "handle": ch[cid]["handle"], "tier": ch[cid]["tier"]}
                            for cid in name_hits}}
    json.dump(res, open(out_json, "w"), indent=1, ensure_ascii=False)
    ids = [v["video_id"] for v in ray] + [m["video_id"] for L in matches.values() for m in L]
    open(out_ids, "w").write("\n".join(dict.fromkeys(ids)) + "\n")
    print(len(matches), "channels with title matches;", sum(len(L) for L in matches.values()), "videos;", len(name_hits), "name matches")


main()
