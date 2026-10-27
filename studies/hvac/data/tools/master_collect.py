#!/usr/bin/env python3
"""Round 2 master channel list, step 1: collect every channel from every round 1 / round 2 source.

Written 2026-10-24 by the round 2 master-list helper. Reads only files already in studies/hvac/.
Writes one JSON (path given as argv[1]) holding, per channel ID, every source record found,
plus the unresolved handles/names and the sweep inclusion counts. No figure is invented: every
field keeps the source it came from and that source's pull date.

Usage: python3 -I master_collect.py OUT.json
"""
import csv, json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
HV = os.path.normpath(os.path.join(HERE, "..", ".."))
RAW = os.path.join(HV, "data", "raw")
OUT = sys.argv[1]

ID_RX = re.compile(r"UC[\w-]{22}")
recs = collections.defaultdict(list)   # channel_id -> [source record]
unresolved = []                        # records with no channel ID yet


def add(cid, rec):
    if cid and ID_RX.fullmatch(cid):
        recs[cid].append(rec)
    else:
        unresolved.append(rec)


def cells(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    s = s.replace("\\|", "│")  # escaped pipes inside titles
    parts = [p.strip().replace("│", "|") for p in s.strip("|").split("|")]
    return parts


def md_section(path, start_rx, end_rx):
    lines = open(path, encoding="utf-8").read().splitlines()
    out, on = [], False
    for ln in lines:
        if not on and re.search(start_rx, ln):
            on = True
            continue
        if on and end_rx and re.search(end_rx, ln):
            break
        if on:
            out.append(ln)
    return out


# ---------------------------------------------------------------- 1. the 8 known channels (hand-copied from
# seeds/known-channels-recheck.md section 1 and 2; YT figures pulled 2026-10-23)
KNOWN = [
    ("Ray Dutton's Garage", "@RayDuttonsGarage", "UCvcKEgZcY9ZgEULZouaNAOA", "faceless persona", "Ray Dutton, 'a retired HVAC pro', 25 years", "31.5K", "6,227,051", "Jul 1, 2026", "51", "first upload Jul 29, 2026",
     ("Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)", "dOZ-8__G4uU", 1202740), "AC, furnace, thermostat, filters, energy-bill mistakes"),
    ("HVAC Exposed", "@HVACExposed", "UCZ1IwSV46bb09fMvqHn6_2A", "faceless (expose brand; recent thumbnails show an unnamed, likely AI older man)", "none named; e-book domain askfrankhvac.com", "9.59K", "2,016,579", "Feb 27, 2026", "79", "first upload Feb 28, 2026",
     ("The Only 5 HVAC Brands Worth Buying (The Lifetime List)", "QKPPm6M0__o", 577619), "brand verdicts, filters, HVAC industry expose"),
    ("Vent Exposed", "@VentExposed", "UCTDbUAjE9Ab_wwvuV7cgtvQ", "faceless", "'your consumer advocate for home climate'; no person", "1.93K", "696,224", "Mar 31, 2026", "12", "dormant since May 30, 2026; started as pest control",
     ("The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)", "86S3ITbfzQY", 669737), "AC brand verdicts (4-channel collab hit)"),
    ("John The HVAC Guy", "@JohnTheHVACGuy", "UCOyYTw-deou3ax6gvCmX2dg", "faceless persona", "'Hey, I'm John. I've spent years around HVAC systems'", "7.13K", "986,134", "Sep 30, 2020", "69", "account 2020; first HVAC video Aug 13, 2026 (restart)",
     ("Do THIS Once a Month and Your AC Will Last 25 Years", "CJhglI70jw8", 232657), "AC and furnace longevity, brand lists (copies Ray / HVAC Exposed titles)"),
    ("Exposi", "@Exposerosi34", "UCQCRIhHQ__ncUxtOHiIXI4A", "faceless", "no persona; About copies HVAC Exposed", "2.52K", "744,853", "Jun 8, 2026", "43", "first upload Jun 23, 2026",
     ("Doing This Will Make Your AC Run Like NEW Again!", "ExzlvE5GfX8", 329473), "AC 'secret tricks'"),
    ("Hank Cole", "@HankColeUS", "UC5NJ3yYhsZFkfWLJJJVoxMA", "faceless persona", "'Forty years in heating and cooling'", "1.37K", "246,171", "Jul 20, 2026", "31", "pivoted to car videos in Oct 2026",
     ("The $5 Fix That Makes Your AC Blow 9° Colder — 40 Years In, Nobody Tells You This", "HPYZfXWGzjQ", 156562), "AC cheap fixes; now cars"),
    ("Gus Whitaker", "@GusWhitakerr", "UCLdI4EbF3WcHS_oyhjSvwDw", "faceless persona", "'kept the same old Ohio house warm through forty winters'", "822", "201,227", "Aug 27, 2026", "19", "first upload Oct 3, 2026; not monetized",
     ("Turning Your Heat Up Past 70 Is NOT Warming Your House. Do This Instead", "dBPrCiISyX0", 96251), "home heating, heat bill, outage heat"),
    ("The DIY HVAC Guy", "@diyhvacguy", "UC2w60mhlxFmAhoi2oSDcEng", "on camera", "Dave, HVAC contractor in Utah", "527K", "102,187,575", "Mar 22, 2017", "362", "",
     ("Keep Your Family Warm During A Power Outage By Installing This $5 Part", "y07w1hiKIrI", 4266302), "DIY HVAC repair and install, outage heat"),
]
for (n, h, cid, typ, per, subs, tv, joined, vids, note, best, topics) in KNOWN:
    add(cid, dict(src="known8", date="2026-10-23", name=n, handle=h, type=typ + " (reading, seeds/known-channels-recheck.md)",
                  persona=per, audience="homeowner (reading)", fit="HVAC (known channel)", subs=subs, subs_src="YouTube About 2026-10-23",
                  total_views=tv, joined=joined, video_count=vids, note=note, topics=topics,
                  best_title=best[0], best_id=best[1], best_views=best[2], best_src="YouTube video page 2026-10-23 (vid.py)"))

# known-channels leads table (section 4)
for ln in md_section(os.path.join(HV, "seeds", "known-channels-recheck.md"), r"^## 4\. Leads", r"^\*\*Reading"):
    c = cells(ln)
    if not c or len(c) < 6 or c[0] in ("Channel",) or set(c[0]) <= set("-"):
        continue
    name, hid, subs, joined, what, srcs = c[:6]
    ids = ID_RX.findall(hid)
    handles = re.findall(r"@[\w.-]+", hid)
    if "/" in name and not ids:  # Prime Rundown / Hull Honest / Grill Verdict
        for nm, hh, ss in zip([x.strip() for x in name.split("/")], handles, [x.strip() for x in subs.replace("(YT)", "").split("/")]):
            add(None, dict(src="known8-leads", date="2026-10-23", name=nm, handle=hh, subs=ss, subs_src="YouTube (Collaborators panel) 2026-10-23",
                           note=what, found=srcs))
        continue
    m = re.search(r"\(([^)]*)\)", subs)
    add(ids[0] if ids else None, dict(src="known8-leads", date="2026-10-23", name=name, handle=handles[0] if handles else "",
                                      subs=re.sub(r"\s*\(.*\)", "", subs) if "not shown" not in subs else "",
                                      subs_src=("YouTube 2026-10-23" if m and m.group(1) == "YT" else ("NexLev 2026-10-23" if m else "")),
                                      joined=joined if re.match(r"\d{4}-\d\d-\d\d", joined) else "", note=what, found=srcs))

# ---------------------------------------------------------------- 2. round 1 channel finds (174)
for r in csv.DictReader(open(os.path.join(RAW, "channel-finds-round1.csv"), encoding="utf-8")):
    add(r["channel_id"], dict(src="round1", date=r["date_pulled"] or "2026-10-23", name=r["name"], handle=r["handle"], type=r["type"],
                              persona=r["persona_background"], audience=r["audience"], fit=r["fit"], subs=r["subs"],
                              subs_src=r["subs_source"] + " 2026-10-23", total_views=r["total_views"], joined=r["joined"],
                              video_count=r["video_count"], country=r["country"], topics=r["main_topics"],
                              nexlev_outlier=r["nexlev_outlier_score"], nexlev_monthly_views=r["nexlev_monthly_views"],
                              best_title=r["example_video_title"], best_id=r["example_video_id"], best_views=r["example_views"],
                              best_src=r["example_source"] + " (round 1 example video, 2026-10-23)", found=r["found_by"]))

# round 1 rejected candidates (19, names only in the .md). IDs matched by exact name in the round 1 raw JSON
# (2026-10-24, this helper); each is checked against its About panel title in step 2.
REJECTED = {
    "Brand Meter": ("UCSlwgqAXct9Oa-8XnzzlkXA", "clothing brands"),
    "Consumer Truth": ("UCidqAQ2CxzBp4OYzapEu_og", "grocery tests"),
    "Sergeant Dale Whitfield": ("UCGQz5_mS75Awg5HUMhiiJ2w", "stump, car and drain hacks"),
    "Patina": ("UC4xatswWsvs81cQSnDrJqsA", "Japanese culture; one senior winter-tricks video (377K)"),
    "Project Renewed Homes": ("UCzOi__BRsEE3CAR2bKXqsIg", "renovation stories"),
    "Clever Hacks": ("UCF7WlkgQIFOktAJVY5ZgRtw", "mostly Shorts"),
    "Sidney Explains": ("UCdyG3WX1yILqhYHe3EK4bQw", "food and frugal living; one air-purifier video"),
    "The roots survived": ("UCEKUEXO7sBNrasXwS2hoy8Q", "concrete hacks"),
    "Stop Wasting Stuff": ("UCFNWzOwiK6wmSQpBPG_ZP9Q", "hydrogen peroxide hacks; no HVAC hit found"),
    "The Household Formula": ("UCGD4IPN_ywGUOeLF74qUM7w", "one HVAC video, 60 views"),
    "Amos Miller": ("UCzDvYjtRgZ4mGuPGMioBY5A", "batteries and power"),
    "Cantrell Hoffman": ("UCcZ4RylQGWTCkdM0PT2k9fg", "prepper water and food"),
    "Amish Frugal Life": ("UCfKWxYMpFy2paDbsv0YSPbg", "Amish lifestyle; one humidity and mold video (363K)"),
    "Finn Stone": ("UCpDSkMeuhhAqJ0IfO-70UKA", "mixed (mafia history, lathes, alternators)"),
    "AC PRO": ("UCJCk5Iz8UO4jrLb07hvrNgQ", "car AC brand"),
    "Thomson AC": ("UCaxva4G655ldv6AHf1B9vvw", "videos mostly under 5 minutes"),
    "The Thermo Expert": ("UCvtgUPTFH0vnjUnWKxpWgeA", "videos mostly under 5 minutes"),
    "STAYCOOLHVAC": ("UCtBzNpJfPU8AWUEnEfAQFPw", "videos mostly under 5 minutes"),
    "Gary Whitaker Backup Power": ("UCNdp0HrrequO9puyQvvh0Lw", "generator and power-station reviews, out of scope per the operator"),
}
for n, (cid, why) in REJECTED.items():
    add(cid, dict(src="round1-rejected", date="2026-10-23", name=n, note="left out in round 1: " + why))

# ---------------------------------------------------------------- 3. up-next / similar leads (129 + 20)
lp = os.path.join(HV, "seeds", "leads-channels.md")
for ln in md_section(lp, r"^## Channels in the up-next and similar results", r"^## Non-HVAC channels"):
    c = cells(ln)
    if not c or len(c) < 9 or not c[0].isdigit():
        continue
    ids = ID_RX.findall(c[2]); hh = re.findall(r"@[\w.-]+", c[2])
    ex = c[7]; m = re.match(r'"(.*)" \(`([\w-]{11})`, ([^,]+) views', ex)
    sm = re.match(r"([\d.,]+[KM]?)\s*\((.*)\)", c[8])
    add(ids[0] if ids else None, dict(src="leads-hvac", date="2026-10-23", name=c[1], handle=hh[0] if hh else "",
                                      fit="up-next lead: " + c[6], subs=sm.group(1) if sm else "", subs_src=("leads-channels.md: " + sm.group(2) + " 2026-10-23") if sm else "",
                                      best_title=m.group(1) if m else "", best_id=m.group(2) if m else "", best_views=m.group(3) if m else "",
                                      best_src="YouTube up-next (rounded short text) 2026-10-23" if m else "",
                                      found=f"up-next hop1 {c[3]}; hop2 {c[4]}; NexLev similar videos {c[5]}"))
for ln in md_section(lp, r"^## Non-HVAC channels", r"^## Most-recommended"):
    c = cells(ln)
    if not c or len(c) < 6 or not ID_RX.search(c[1]):
        continue
    ids = ID_RX.findall(c[1]); hh = re.findall(r"@[\w.-]+", c[1])
    ex = c[5]; m = re.match(r'"(.*)" \(`([\w-]{11})`, ([^,]+) views', ex)
    add(ids[0], dict(src="leads-nonhvac", date="2026-10-23", name=c[0], handle=hh[0] if hh else "", fit="up-next lead, non-HVAC: " + (c[4] or "not described"),
                     note="example up-next video: " + ex, found=f"up-next hop1 {c[2]}; hop2 {c[3]}"))
# About panels pulled by the leads helper
up = json.load(open(os.path.join(RAW, "upnext-2026-10-23.json"), encoding="utf-8"))
about_seen = {}  # cid -> list of (about dict, source, date)
for cid, a in up.get("channel_about_this_pull", {}).items():
    about_seen.setdefault(cid, []).append((a, "YouTube About (leads helper)", (a.get("pulled") or "2026-10-23")[:10]))

# ---------------------------------------------------------------- 4. round 2 NexLev channels (164)
for r in csv.DictReader(open(os.path.join(RAW, "round2-nexlev-channels.csv"), encoding="utf-8")):
    add(r["channel_id"], dict(src="r2-nexlev", date=r["date_pulled"] or "2026-10-24", name=r["name"], handle=r["handle"], type=r["type"],
                              nexlev_flags=f"faceless={r['nexlev_faceless_flag']}; ai={r['nexlev_ai_flag']}; style={r['nexlev_editing_style']}",
                              persona=r["persona_background"], audience=r["audience"], fit=r["fit"], subs=r["subs"], subs_src=r["subs_source"],
                              total_views=r["total_views"], joined=r["joined"], video_count=r["video_count"], country=r["country"],
                              nexlev_first_video=r["nexlev_first_video"], nexlev_outlier=r["nexlev_outlier_score"], nexlev_monthly_views=r["nexlev_monthly_views"],
                              best_title=r["example_title"], best_id=r["example_id"], best_views=r["example_views"], best_src=r["example_source"],
                              top_title=r["top_video_title"], top_id=r["top_video_id"], top_views=r["top_video_views"], found=r["found_by"]))

# About panels already pulled by round 1 and round 2 helpers
for d, label, date in [("channel-finds-pages-2026-10-23", "YouTube About (round 1 helper)", "2026-10-23"),
                       ("round2-nexlev-pages-2026-10-24", "YouTube About (round 2 NexLev helper)", "2026-10-24")]:
    p = os.path.join(RAW, d, "about.json")
    if os.path.exists(p):
        for cid, a in json.load(open(p, encoding="utf-8")).items():
            about_seen.setdefault(cid, []).append((a, label, date))

# ---------------------------------------------------------------- 5. old-house heat pool (round 2)
oh = json.load(open(os.path.join(RAW, "round2-oldheat-2026-10-24.json"), encoding="utf-8"))
for cid, a in oh["channel_about"].items():
    about_seen.setdefault(cid, []).append((a, "YouTube About (old-house heat helper)", (a.get("pulled") or "2026-10-24")[:10]))
for pool, label in [("pool_heat", "oldheat-heat"), ("pool_ac", "oldheat-ac")]:
    by = collections.defaultdict(list)
    for v in oh[pool]:
        by[(v.get("channelId"), v.get("channel"))].append(v)
    for (cid, ch), vs in by.items():
        best = max(vs, key=lambda v: v.get("views_n") or 0)
        add(cid, dict(src=label, date="2026-10-24", name=ch, handle=(vs[0].get("handle") or "").lstrip("/"),
                      country=vs[0].get("channel_country") or "", pool_videos=len(vs), pool_views=sum(v.get("views_n") or 0 for v in vs),
                      best_title=best.get("orig_title") or best["title"], best_id=best["id"], best_views=best.get("views_n"),
                      best_src=f"YouTube search ({'old-house heat' if pool == 'pool_heat' else 'AC matched'} pool) 2026-10-24"))
# faceless table in old-house-heat.md (type readings by name)
oh_types = {}
for ln in md_section(os.path.join(HV, "round2", "old-house-heat.md"), r"^### Faceless and faceless-persona channels found", r"^Notes:"):
    c = cells(ln)
    if c and len(c) >= 8 and c[0] not in ("Channel",) and not set(c[0]) <= set("-"):
        oh_types[c[0]] = c[7]

# ---------------------------------------------------------------- 6. keyword sweep
V = list(csv.DictReader(open(os.path.join(RAW, "sweep-videos-2026-10-24.csv"), encoding="utf-8")))
C = list(csv.DictReader(open(os.path.join(RAW, "sweep-channels-2026-10-24.csv"), encoding="utf-8")))
oemb = {}
for ln in open(os.path.join(RAW, "sweep-oembed-2026-10-24.jsonl"), encoding="utf-8"):
    try:
        o = json.loads(ln); oemb[o["id"]] = o.get("author") or ""
    except Exception:
        pass
name2id = {}
for r in C:
    if r["channelId"]:
        name2id.setdefault(r["channel"].strip().lower(), r["channelId"])
for cid, rs in recs.items():
    for x in rs:
        if x.get("name"):
            name2id.setdefault(x["name"].strip().lower(), cid)
# names and handles resolved to IDs by master_resolve.py (YouTube channel search / NexLev resolver), if run
RES_P = os.path.join(RAW, "channels-master-resolve-2026-10-24.json")
RES = json.load(open(RES_P, encoding="utf-8")) if os.path.exists(RES_P) else {}
for key, r in RES.items():
    if r.get("channelId"):
        name2id.setdefault(key.strip().lower(), r["channelId"])
handle_of = {r["channelId"]: r["handle"].lstrip("/") for r in C if r["channelId"]}
collab = collections.Counter()
for v in V:
    v["_cid"] = v["channelId"]; v["_collab"] = ""
    if not v["channelId"]:
        up_name = oemb.get(v["id"], "")
        first = re.split(r" and (?:\d+ more|)", v["channel"])[0].strip()
        cid = name2id.get(up_name.lower()) or name2id.get(first.lower())
        v["_cid"] = cid or ""
        v["_collab"] = f"collab video '{v['channel']}' (uploader per oEmbed: {up_name or 'not found'})"
        collab["attributed" if cid else "not attributed"] += 1
        if not cid:
            v["_uploader"] = up_name or first
sw = collections.defaultdict(lambda: dict(videos=0, hvac=0, hvac_views=0, best=None, collab_hvac=0, big=0, titles=[]))
for v in V:
    cid = v["_cid"]
    if not cid:
        continue
    s = sw[cid]; s["videos"] += 1
    s["titles"].append((int(v["views"] or 0), v["title"], v["hvac_word_in_title"] == "yes", v["approx_upload_date"]))
    if v["hvac_word_in_title"] == "yes":
        n = int(v["views"] or 0)
        s["hvac"] += 1; s["hvac_views"] += n
        if v["_collab"]:
            s["collab_hvac"] += 1
        if n >= 500000:
            s["big"] += 1
        if s["best"] is None or n > s["best"][2]:
            s["best"] = (v["title"], v["id"], n, v["approx_upload_date"])
csv_hvac = {r["channelId"]: int(r["hvac_word_videos"] or 0) for r in C if r["channelId"]}
rule = collections.Counter()
sweep_incl = {}
names_sw = {r["channelId"]: (r["channel"], r["handle"].lstrip("/"), r["new"]) for r in C if r["channelId"]}
for v in V:  # names for attributed collab uploaders that have no own row
    if v["_cid"] and v["_cid"] not in names_sw:
        names_sw[v["_cid"]] = (oemb.get(v["id"]) or v["channel"], "", "")
for cid, s in sw.items():
    r3 = s["hvac"] >= 3; rb = s["big"] >= 1
    r3_csv = csv_hvac.get(cid, 0) >= 3
    if r3 or rb:
        sweep_incl[cid] = ("3+ HVAC-title videos" if r3 else "") + (" ; " if r3 and rb else "") + ("a 500K+ HVAC-title video" if rb else "")
        rule["rule A (3+)"] += r3; rule["rule B only (500K+, fewer than 3)"] += (rb and not r3); rule["both"] += (r3 and rb)
        rule["rule A only because of collab videos"] += (r3 and not r3_csv)
    nm, hh, new = names_sw.get(cid, ("", "", ""))
    rec = dict(src="sweep", date="2026-10-24", name=nm, handle=hh, sweep_videos=s["videos"], sweep_hvac=s["hvac"],
               sweep_hvac_views=s["hvac_views"], sweep_collab_hvac=s["collab_hvac"], sweep_big=s["big"], sweep_new=new,
               sweep_titles=sorted(s["titles"], reverse=True)[:10])
    if s["best"]:
        rec.update(best_title=s["best"][0], best_id=s["best"][1], best_views=s["best"][2],
                   best_src=f"YouTube search page (keyword sweep) 2026-10-24; approx upload {s['best'][3]}")
    rec["sweep_included"] = cid in sweep_incl
    if cid in recs or cid in sweep_incl:  # carry sweep counts for every listed channel; add a channel only by the rule
        recs[cid].append(rec)

# unattributed collab uploaders that would meet the rule (to resolve by name)
ua = collections.defaultdict(lambda: [0, 0])
for v in V:
    if v.get("_uploader") and v["hvac_word_in_title"] == "yes":
        ua[v["_uploader"]][0] += 1; ua[v["_uploader"]][1] = max(ua[v["_uploader"]][1], int(v["views"] or 0))
to_resolve = sorted(k for k, x in ua.items() if x[0] >= 3 or x[1] >= 500000)
# unresolved records from other sources: resolve their handle (or, for collab rows, the lead name) by RES
still = []
for r in unresolved:
    key = r.get("handle") or re.split(r" and (?:\d+ more|)", r["name"])[0].strip()
    cid = (RES.get(key) or {}).get("channelId") or name2id.get(key.lower())
    if cid:
        r["resolved_by"] = (RES.get(key) or {}).get("how", "name match to a listed channel")
        recs[cid].append(r)
    else:
        still.append(r); to_resolve.append(key)
unresolved = still
json.dump(dict(recs=recs, to_resolve=sorted(set(to_resolve)), unresolved=unresolved, about_seen=about_seen, oh_types=oh_types,
               sweep_rule=dict(rule), sweep_collab=dict(collab), sweep_incl=sweep_incl,
               sweep_totals=dict(channels_csv=len(C), videos=len(V), hvac_title_videos=sum(1 for v in V if v["hvac_word_in_title"] == "yes"))),
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
src_count = collections.Counter(x["src"] for rs in recs.values() for x in rs)
print("channels:", len(recs), "unresolved:", len(unresolved), "to resolve:", sorted(set(to_resolve)))
print(src_count)
print("sweep rule:", dict(rule), "collab:", dict(collab))
