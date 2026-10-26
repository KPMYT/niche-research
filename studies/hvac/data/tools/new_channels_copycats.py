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




# ---------------------------------------------------------------------------------------------------------------
# report mode: python3 -I new_channels_copycats.py report <matches.json> <exact.jsonl> <out.md>
# Copies = titles uploaded on or after Ray's first exact use of a template Ray started (T1, T2, T4, T5, T6), or
# 0.80+ similar to one of Ray's top titles and uploaded after it. T3, T7 and T8 predate Ray (he borrowed them).
# ---------------------------------------------------------------------------------------------------------------
# Thumbnail readings (mine, one mqdefault thumbnail per channel: its most-viewed copy video, 2026-10-26).
LOOK = {
    "@WendyBurris-z8x": "same name ('Ray'); AI man in navy work shirt with a 'RAY' name patch; thermostat close-up",
    "@daleprosser101": "navy work shirt with a 'RAY' name patch; Ray's 'BIG FALL MISTAKE!' covered-AC thumbnail redone",
    "@leroybellgarage": "navy shirt with a 'LEROY' name patch; 'BIG FALL MISTAKE!' covered-AC thumbnail; handle says 'garage'",
    "@FrankCoyleWrench_Yt": "navy shirt with a 'Frank' name patch; thermostat + 'STOP DOING THIS!'",
    "@DanCartersWorkshop": "shirt patch 'DAN CARTER'S WORKSHOP'; thermostat + 'AVOID THIS'",
    "@WaltBrennan1": "navy shirt with a name patch; 'DON'T COVER YOUR AC!' covered-AC thumbnail",
    "@PracticalHomeowner": "'BIG FALL MISTAKE!' covered-AC thumbnail (no patch seen)",
    "@HomeFixGarage": "'COSTLY AC MISTAKE!' covered-AC thumbnail; 'Garage' in the name",
    "@WaltBrandt": "'COSTLY FALL MISTAKE' covered-AC thumbnail",
    "@GeorgeSmithGarage": "'<Name>'s Garage' name; navy shirt, thermostat + 'AVOID THIS'",
    "@HankColeUS": "navy shirt, thermostat + 'AVOID THIS!'",
    "@FixTheMexicanWay": "navy shirt, power meter + 'LOWER YOUR POWER BILL' (Ray's meter thumbnail)",
    "@GordTheTradesman": "navy shirt, power meter + 'LOWER YOUR POWER BILL'",
    "@hankalvarez1964": "navy shirt, power meter + 'LOWER YOUR WINTER POWER BILL'",
    "@PracticalHomeEnergy": "power meter + 'YOU'RE PAYING ALL NIGHT'",
    "@diyhvacguy": "real presenter; furnace + red circle + 'THEY HOPE YOU MISS THIS' (Ray's furnace thumbnail text)",
    "@EarlKnowsHow00": "furnace + red arrow + 'THEY HOPE YOU MISS THIS'",
    "@BackyardLowTech": "furnace + red circle + 'THEY HOPE YOU MISS THIS'",
    "@RayDonnellyDIY": "'Ray' first name; furnace + 'THEY HOPE YOU MISS THIS'",
    "@EliPlainHeat": "furnace + 'THEY HOPE YOU SKIP THIS' (Amish elder)",
    "@VernHoltHomeRepair": "thermostat + 'NOT 68!' (Ray's 'NOT 68!' thumbnail)",
    "@JeanHiggins-p3u": "thermostat + 'STOP DOING THIS!'",
    "@WaltBrennersBoiler1": "thermostat + 'STOP DOING THIS!'",
    "@nicksalermo": "thermostat + 'STOP DOING THIS!'",
    "@MicksAirCon": "'STOP DOING THIS' (indoor unit)",
    "@RaysWorkshopYT": "'Ray' first name; 'DON'T TURN IT ON YET!' (knit cap, plaid; not Ray's look)",
    "@Earl-Whitaker": "navy shirt; its 'NO HEAT? DO THIS!' thumbnail (lz-RIZga2l0) shows the same grey-haired man with a 'RAY' patch as Ray's own (round 2 saw it too, 2026-10-24)",
    "@JohnTheHVACGuy": "filter box + '$4,000 REPAIR BILL' (not Ray's look)",
}
EXTRA_LOOK = [  # channels whose thumbnails show the 'RAY' patch but whose titles did not match (round 2 reading + mine)
    ("HVAC Home Guide", "@Peacetvurdeo", "zA2bRll38TI", "navy shirt with a 'RAY' patch ('THERMOSTAT MISTAKES'); the channel's most-viewed video is an unrelated religious video (repurposed account, reading)"),
    ("Frank From Maintenance", "@FrankFromMaintenance", "Gxek0eXihgw", "navy shirt with a 'Frank' patch ('$20 ATTIC FIX')"),
]
ORIG = ["T1", "T2", "T4", "T5", "T6"]


def report(mpath, epath, out):
    m = json.load(open(mpath))
    ex = {}
    for l in open(epath):
        if l.strip():
            d = json.loads(l)
            if "error" not in d:
                ex[d["id"]] = d
    ch = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(RAW, "census-channels-2026-10-26.csv")))}
    types = {}
    for t in "ABC":
        p = os.path.join(RAW, f"census-types-{t}-2026-10-26.csv")
        if os.path.exists(p):
            for r in csv.DictReader(open(p)):
                types[r["channel_id"]] = r
    rayv = sorted([e for e in ex.values() if e.get("owner") == "Ray Dutton's Garage"], key=lambda e: e["date"])
    raydate = {e["id"]: e["date"] for e in rayv}
    first, ray_ex = {}, {}
    for t in m["templates"]:
        k = t["key"].split(" ")[0]
        rf = [e for e in rayv if re.search(t["regex"], e["title"].lower())]
        first[k] = rf[0]["date"] if rf else None
        ray_ex[k] = rf
    L = []
    for cid, c in m["title_matches"].items():
        for v in c["videos"]:
            e = ex.get(v["video_id"])
            if not e:
                continue
            ks = [w for w in v["why"] if w in ORIG and first[w] and e["date"] >= first[w]]
            sims = [w for w in v["why"] if w.startswith("SIM") and float(w.split()[1]) >= 0.80 and e["date"] >= raydate.get(w.split()[-1], "9")]
            if ks or sims:
                base = num(ch[cid]["baseline"])
                L.append({"cid": cid, "id": e["id"], "title": e["title"] + ("" if e["title"].strip() == v["title"].strip() else f" [tab title 2026-10-26: \"{v['title']}\"]"), "views": e["views"], "date": e["date"], "why": ks + sims,
                          "mult": round(e["views"] / base, 2) if base else None})
    lines = []
    # template table
    lines.append("| Template | Who used it first (exact date, views) | Ray's uses (exact views) | Later copies in the census: titles / channels | Copy views: median, best |")
    lines.append("|---|---|---|---|---|")
    for t in m["templates"]:
        k = t["key"].split(" ")[0]
        allm = []
        for cid, c in m["title_matches"].items():
            for v in c["videos"]:
                if k in v["why"] and v["video_id"] in ex:
                    allm.append((ex[v["video_id"]], cid))
        pre = sorted([x for x in allm if first[k] and x[0]["date"] < first[k]], key=lambda x: x[0]["date"])
        post = [x for x in allm if not first[k] or x[0]["date"] >= first[k]]
        if pre and k not in ORIG:
            e0, c0 = pre[0]
            who = f"{ch[c0]['name'].strip()}, \"{e0['title']}\" `{e0['id']}` ({e0['date']}, {e0['views']:,})"
        else:
            e0 = ray_ex[k][0]
            who = f"**Ray** `{e0['id']}` ({e0['date']}, {e0['views']:,})" + (f"; nearest earlier: {ch[pre[0][1]]['name'].strip()} \"{pre[0][0]['title']}\" ({pre[0][0]['date']}, {pre[0][0]['views']:,})" if pre else "")
        rays = "; ".join(f"`{e['id']}` {e['views']:,}" for e in sorted(ray_ex[k], key=lambda e: -e["views"])[:3])
        pv = sorted([x[0]["views"] for x in post])
        best = max(post, key=lambda x: x[0]["views"]) if post else None
        bt = f"{best[0]['views']:,} ({ch[best[1]]['name'].strip()}, `{best[0]['id']}`)" if best else "-"
        med = f"{pv[len(pv)//2]:,}" if pv else "-"
        lines.append(f"| {t['key']} | {who} | {rays} | {len(post)} / {len(set(x[1] for x in post))} | {med}; best {bt} |")
    # channel table
    by = collections.defaultdict(list)
    for x in L:
        by[x["cid"]].append(x)
    lines.append("")
    lines.append("| # | Channel | Tier | Type (types helper) | Started | Subs | Copies (titles) | First copy | Best copy: title, ID, exact views (multiple of the channel's baseline) | Name / look copy (my reading of one thumbnail) |")
    lines.append("|---:|---|:---:|---|---|---:|---:|---|---|---|")
    rows = sorted(by.items(), key=lambda kv: -max(x["views"] for x in kv[1]))
    for i, (cid, xs) in enumerate(rows, 1):
        r = ch[cid]
        b = max(xs, key=lambda x: x["views"])
        ty = types.get(cid, {}).get("type") or r["type"] or "not found"
        start = r["joined"] + (" (new)" if r["new_12m"] == "yes" else "")
        lines.append(f"| {i} | {r['name'].strip()} [{r['handle']}]({r['link']}) | {r['tier']} | {ty} | {start} | {r['subs']} | {len(xs)} | "
                     f"{min(x['date'] for x in xs)} | \"{b['title']}\" `{b['id']}` {b['views']:,} ({b['mult'] if b['mult'] is not None else 'n/a'}x) | {LOOK.get(r['handle'], '-')} |")
    hv = [x for x in L]
    over100 = [x for x in L if x["views"] >= 100000]
    over2x = [x for x in L if x["mult"] and x["mult"] >= 2]
    newc = [cid for cid in by if ch[cid]["new_12m"] == "yes"]
    lines.append("")
    lines.append(f"Counts: {len(L)} copy titles on {len(by)} channels ({len(newc)} of them new in the last 12 months); "
                 f"{len(over100)} copies at 100,000+ views; {len(over2x)} at 2x or more of their own channel's baseline; "
                 f"median copy views {sorted(x['views'] for x in L)[len(L)//2]:,}.")
    lines.append("")
    lines.append("Channels that wear Ray's look but whose titles did not match:")
    for n, h, vid, note in EXTRA_LOOK:
        e = ex.get(vid)
        lines.append(f"- {n} ({h}): {note}; `{vid}`" + (f" {e['views']:,} views ({e['date']})" if e else ""))
    open(out, "w").write("\n".join(lines) + "\n")
    json.dump(L, open(out + ".json", "w"), indent=1, ensure_ascii=False)
    print(lines[-6] if len(lines) > 6 else "", len(L))


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "report":
    report(sys.argv[2], sys.argv[3], sys.argv[4])
    sys.exit(0)


if __name__ == "__main__":
    main()
