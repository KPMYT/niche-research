#!/usr/bin/env python3
"""Round 2 master channel list, step 3: merge, fill, tier and write (2026-10-24).

Inputs:
  COLLECT.json   from master_collect.py (every source record per channel ID)
  TIERS.txt      this helper's tier readings for the channels with no earlier fit tag
                 (lines "index tier [audience]", index into REVIEW_IDS.json)
  REVIEW_IDS.json
  ABOUT*.json    About panels pulled by master_about.py (any number)
Writes:
  data/raw/channels-master-2026-10-24.csv
  OUT_STATS.json (counts for the .md)

Usage: python3 -I master_build.py COLLECT.json TIERS.txt REVIEW_IDS.json OUT_STATS.json ABOUT1.json [ABOUT2.json ...]
"""
import csv, json, os, re, sys, collections, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))
collect = json.load(open(sys.argv[1], encoding="utf-8"))
tier_lines = [l.split() for l in open(sys.argv[2], encoding="utf-8") if l.strip()]
review_ids = json.load(open(sys.argv[3], encoding="utf-8"))
OUT_STATS = sys.argv[4]
recs, about_seen, oh_types = collect["recs"], collect["about_seen"], collect["oh_types"]
for p in sys.argv[5:]:
    for cid, a in json.load(open(p, encoding="utf-8")).items():
        if "error" not in a:
            about_seen.setdefault(cid, []).append((a, "YouTube About (master-list helper)", (a.get("pulled") or "2026-10-24")[:10] + "T" + (a.get("pulled") or "")[11:16]))

SRC_LABEL = {
    "known8": "known 8 (seeds/known-channels-recheck.md, 2026-10-23)",
    "known8-leads": "known-channels leads (seeds/known-channels-recheck.md s.4, 2026-10-23)",
    "round1": "round 1 finds (seeds/channel-finds-round1.md, 2026-10-23)",
    "round1-rejected": "round 1 rejected candidates (seeds/channel-finds-round1.md, 2026-10-23)",
    "leads-hvac": "up-next leads, HVAC (seeds/leads-channels.md, 2026-10-23)",
    "leads-nonhvac": "up-next leads, non-HVAC (seeds/leads-channels.md, 2026-10-23)",
    "r2-nexlev": "round 2 NexLev (round2/nexlev-channels.md, 2026-10-24)",
    "oldheat-heat": "old-house heat pool (round2/old-house-heat.md, 2026-10-24)",
    "oldheat-ac": "old-house heat helper's AC matched pool (round2/old-house-heat.md, 2026-10-24)",
    "sweep": "keyword sweep (round2/keyword-sweep.md, 2026-10-24)",
}
SHORT = {"known8": "K8", "known8-leads": "K8L", "round1": "R1", "round1-rejected": "R1X", "leads-hvac": "UN", "leads-nonhvac": "UNX",
         "r2-nexlev": "NX2", "oldheat-heat": "OHH", "oldheat-ac": "OHA", "sweep": "SW"}

# ------------------------------------------------------------------ tier readings
review_tier = {}
for parts in tier_lines:
    i = int(parts[0]); t = parts[1]; aud = parts[2] if len(parts) > 2 else ""
    review_tier[review_ids[i]] = (t, aud)

# ADJ-tagged channels (round 1 / round 2 "ADJ") and a few others: my reading
ADJ_TIER = {
    "UCqCz10_64ISJCoc1xV1a8-w": "C",  # Walt Brandt: appliance / furnace "worth buying" verdicts
    "UCAPrhJwVweWZA8GEPoClSdw": "X",  # Pleasant Green: one HVAC hit
    "UCyDPTQMaRk_Z6k76M0BP-8w": "X",  # Becoming a Farm Girl: one heating-bill hit, mostly food
    "UCkHDMmVa2MkgKdK7B05s9dQ": "C",  # Bertha's House Hacks: frugal winter hacks
    "UC7xrSTuKm8YPd2l6WPgMt-g": "C",  # TheCheapFix: 'things X don't want you to know' hacks incl. HVAC
    "UCAsjbTlJ9B4GVQJ8yirIEdg": "C",  # Home Guard: brands still built to last
    "UC4xatswWsvs81cQSnDrJqsA": "C",  # Patina: rejected in round 1, kept by round 2 (Japanese home / winter ways); latest pull kept
    "UCmGizvYWqUH3DGYEgRbHr8g": "C",  # Wonders: grandma winter / outage tricks
    "UCQJHoc6ncQ3-6JFROw13Zfg": "C",  # Quality Rot: brand verdicts
    "UCRIRd-k1miHBiqPa3V_SOeA": "X",  # TheAirConditionerGuy: vintage AC and fan collector (same reading as other collectors)
    "UC1NZkNj4itSR6mth3Q9ApKA": "C",  # Jack Miller: appliance and heat-pump tips, then rancher stories
    "UCX35pnn1Z4rOKD__K_gMn-A": "C",  # BIG TICKET TRUTH: big-ticket brand verdicts
}
# corrections from the round 2 checker (relayed by the main session, 2026-10-24)
TYPE_FIX = {
    "UCRdNcv3g_4rpbNEyFopZwDg": "on camera (round 2 checker, 2026-10-24; was 'faceless, real footage')",   # HVACTIME
    "UCKDkGhLRlzs1bV1tmeokcNQ": "on camera (round 2 checker, 2026-10-24; was 'faceless, real footage')",   # Adrian Garcia
    "UCcrs-w2r-S3VR7pe8t9DIew": "on camera (round 2 checker, 2026-10-24; was 'faceless, real footage')",   # Stephen Shares HVAC Tips at Goettl
    "UC5knbXUbhA0MAGcQNM1SkKA": "faceless, AI images (round 2 checker, 2026-10-24; was read as a named character)",  # Halden Row
}
DROP_BEST = {"UCKDkGhLRlzs1bV1tmeokcNQ": "r2-nexlev"}  # Adrian Garcia: round 2 example is a tool-bag video, not HVAC (checker)
EXTRA_NOTE = {"UCO4alIAsCWzFaJ414P9Mwcw": "round 2 checker: its 'How To Remove Air From Your Heating System' (z80WspC4Nmg, 2,050,577 views) belongs in the old-house heat set; the old-heat helper's rule missed it"}
FIT_TIER = {"HVAC": "A", "DIY": "B", "ENERGY": "C", "OUTAGE": "C", "OFFGRID": "C", "TRADE": "D", "BRAND": "D"}
TIER_RULE = {
    "A": "A: HVAC is the channel's main subject, made for homeowners (AC, heat pumps, furnaces, boilers, thermostats, filters, ducts, the bill).",
    "B": "B: general home DIY / home repair / handyman channel; HVAC, insulation or the bill is a real share, not the main subject.",
    "C": "C: adjacent lane: off-grid and supplemental heat (wood, pellet, diesel, waste oil, 'free heat'), outage / blackout, energy and insulation, product and brand verdict lists, frugal living, old-ways history of heating and cooling.",
    "D": "D: trade-facing (technicians, students, HVAC business owners) or a brand / contractor / retailer / manufacturer channel.",
    "X": "X: off-niche (car AC, PC cooling, Indian / Pakistani market AC, electronics, gaming, sport, news, sleep sounds, collectors, camping, one-off hits); kept in the file, dropped from the census.",
}


def tier_of(cid, rs):
    srcs = {r["src"] for r in rs}
    if cid == "UC67dKTEwpAhKv2oYDATwR8g":
        return "B", "Silver Cymbal (study seed): on-camera general home DIY; HVAC and insulation are a large share"
    if "known8" in srcs:
        return "A", "known HVAC channel (fit HVAC)"
    if cid in ADJ_TIER:
        return ADJ_TIER[cid], "my reading of an ADJ / rejected-then-kept channel"
    fits = [(r["src"], (r.get("fit") or "").replace(" (reading)", "").strip(), (r.get("audience") or "").replace(" (reading)", ""))
            for r in rs if r["src"] in ("r2-nexlev", "round1")]
    fits.sort(key=lambda x: 0 if x[0] == "r2-nexlev" else 1)
    for s, f, aud in fits:
        if f in FIT_TIER:
            t = FIT_TIER[f]
            if t == "A" and aud == "trade":
                t = "D"
            return t, f"from the {SHORT[s]} fit tag '{f}'"
    if "round1-rejected" in srcs:
        return "X", "rejected in round 1 (kept as rejected)"
    if "leads-nonhvac" in srcs:
        return "X", "up-next lead marked non-HVAC"
    if cid in review_tier:
        return review_tier[cid][0], "my reading of the returned titles and channel name (2026-10-24)"
    return "X", "no reading (no titles available)"


# ------------------------------------------------------------------ helpers
def num(s):
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return int(s)
    s = str(s).strip().replace(",", "")
    m = re.match(r"^([\d.]+)\s*([KMB]?)", s)
    if not m or m.group(1) in ("", "."):
        return None
    v = float(m.group(1)) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)]
    return int(round(v))


MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def iso_date(s):
    if not s:
        return ""
    s = str(s).replace("Joined", "").strip()
    m = re.match(r"(\d{4})-(\d\d)-(\d\d)", s)
    if m:
        return s[:10]
    m = re.match(r"([A-Z][a-z]{2})\w* (\d{1,2}), (\d{4})", s)
    if m and m.group(1) in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"
    return ""


def about_fields(a):
    t = a.get("TITLE") or ""
    name, _, url = t.rpartition(" | ") if " | http" in t else (t, "", "")
    h = re.search(r"/(@[^/\s]+)", url)
    return dict(name=name.strip(), handle=h.group(1) if h else "", subs=num((a.get("subscriberCountText") or "").replace(" subscribers", "").replace(" subscriber", "")),
                subs_text=a.get("subscriberCountText") or "", views=num((a.get("viewCountText") or "").replace(" views", "")),
                videos=num((a.get("videoCountText") or "").replace(" videos", "").replace(" video", "")),
                joined=iso_date(a.get("joinedDateText")), country=(a.get("country") if a.get("country") not in (None, "None", "") else ""), desc=a.get("DESC") or "")


def type_cat(t):
    tl = (t or "").lower()
    if not tl or tl.startswith("not checked"):
        return "not checked"
    if "persona" in tl:
        return "faceless persona"
    if "ai avatar" in tl or "ai_avatar" in tl:
        return "AI avatar"
    if "company/brand" in tl or tl.startswith("brand"):
        return "brand"
    if "on camera" in tl:
        return "on camera"
    if "faceless" in tl:
        return "faceless"
    if "flag only" in tl or "nexlev" in tl:
        return "not checked"
    return "not checked"


BRAND_RX = re.compile(r"\b(LLC|Inc\.?|Ltd\.?|Corporation|Company|Supply|Supplies|Distributors?|Industries|Store|Heating (?:&|and) (?:Air|Cooling)|Air Conditioning (?:&|and)|Plumbing,? Heating|Mechanical(?: Inc| Services)?|Services|Boilers?|Stoves|Radiators Direct|Insulation (?:Distributors|Online)|Home Improvement|Official)\b", re.I)

# sweep topics per channel (main-topic fallback)
sweep_topics = {}
for r in csv.DictReader(open(os.path.join(RAW, "sweep-channels-2026-10-24.csv"), encoding="utf-8")):
    if r["channelId"]:
        sweep_topics[r["channelId"]] = r["topics"]

# ------------------------------------------------------------------ build rows
rows = []
for cid, rs in recs.items():
    srcs = sorted({r["src"] for r in rs}, key=lambda s: list(SRC_LABEL).index(s))
    by = collections.defaultdict(list)
    for r in rs:
        by[r["src"]].append(r)
    notes, conflicts = [], []
    # --- About candidates (most recent first)
    abouts = sorted(about_seen.get(cid, []), key=lambda x: x[2], reverse=True)
    abouts = [(about_fields(a), lab, dt) for a, lab, dt in abouts if (a.get("subscriberCountText") or a.get("joinedDateText") or a.get("TITLE"))]
    # --- name / handle
    name = next((a["name"] for a, _, _ in abouts if a["name"]), "")
    if not name:
        for s in ("known8", "r2-nexlev", "round1", "leads-hvac", "leads-nonhvac", "known8-leads", "sweep", "oldheat-heat", "oldheat-ac", "round1-rejected"):
            n = next((r.get("name") for r in by.get(s, []) if r.get("name") and " and " not in r.get("name", "")[-12:]), "")
            if n:
                name = n; break
        if not name:
            name = next((r.get("name") for r in rs if r.get("name")), "")
    handle = next((a["handle"] for a, _, _ in abouts if a["handle"]), "")
    if not handle:
        handle = next((("@" + r["handle"].lstrip("@/")) for s in ("known8", "r2-nexlev", "round1", "leads-hvac", "leads-nonhvac", "known8-leads", "sweep", "oldheat-heat", "oldheat-ac")
                       for r in by.get(s, []) if r.get("handle") and not r["handle"].startswith("channel/")), "")
    if handle.startswith("@channel"):
        handle = ""
    # --- subs / views / joined / videos / country: candidates (value, source, date)
    cand = collections.defaultdict(list)
    for a, lab, dt in abouts:
        d = dt[:10]
        if a["subs"] is not None: cand["subs"].append((a["subs"], f"{lab} {d}", dt))
        if a["views"] is not None: cand["views"].append((a["views"], f"{lab} {d}", dt))
        if a["videos"] is not None: cand["videos"].append((a["videos"], f"{lab} {d}", dt))
        if a["joined"]: cand["joined"].append((a["joined"], f"{lab} {d}", dt))
        if a["country"]: cand["country"].append((a["country"], f"{lab} {d}", dt))
    for s in ("known8", "r2-nexlev", "round1", "leads-hvac", "known8-leads"):
        for r in by.get(s, []):
            d = r.get("date", "")
            if num(r.get("subs")) is not None: cand["subs"].append((num(r["subs"]), r.get("subs_src") or SHORT[s], d))
            if num(r.get("total_views")) is not None: cand["views"].append((num(r["total_views"]), f"{SHORT[s]} ({d})", d))
            if num(r.get("video_count")) is not None: cand["videos"].append((num(r["video_count"]), f"{SHORT[s]} ({d})", d))
            if iso_date(r.get("joined")): cand["joined"].append((iso_date(r["joined"]), f"{SHORT[s]} ({d})", d))
            if r.get("country") and r["country"] not in ("None", "not stated"): cand["country"].append((r["country"], f"{SHORT[s]} ({d})", d))
    for s in ("oldheat-heat", "oldheat-ac"):
        for r in by.get(s, []):
            if r.get("country") and r["country"] not in ("not stated", "None"):
                cand["country"].append((r["country"], "old-house heat helper About (2026-10-24)", "2026-10-24"))
    pick = {}
    for k, lst in cand.items():
        lst.sort(key=lambda x: x[2], reverse=True)
        pick[k] = lst[0]
        if k in ("subs", "views", "videos"):
            v0 = lst[0][0]
            for v, src, _ in lst[1:]:
                if v0 and v and abs(v - v0) / max(v, v0) > 0.05:
                    conflicts.append(f"{k}: {v0:,} ({lst[0][1]}) vs {v:,} ({src})")
                    break
        if k == "joined":
            for v, src, _ in lst[1:]:
                if v != lst[0][0]:
                    conflicts.append(f"joined: {lst[0][0]} ({lst[0][1]}) vs {v} ({src})")
                    break
    # --- type
    typ_detail, typ_src = "", ""
    for s in ("known8", "r2-nexlev", "round1"):
        t = next((r.get("type") for r in by.get(s, []) if r.get("type")), "")
        if t and type_cat(t) != "not checked":
            typ_detail, typ_src = t, SHORT[s]; break
    if typ_src == "NX2":
        typ_detail += " [provisional: read from one thumbnail, per the round 2 checker]"
        typ_src = "NX2 (provisional)"
    if cid in TYPE_FIX:
        typ_detail, typ_src = TYPE_FIX[cid], "round 2 checker"
    if not typ_detail:
        nm_plain = re.split(r" and (?:\d+ more|)", name)[0].strip()
        for s in ("oldheat-heat",):
            for r in by.get(s, []):
                nn = re.split(r" and (?:\d+ more|)", r.get("name", ""))[0].strip()
                for k, v in oh_types.items():
                    if re.split(r" and (?:\d+ more|)", k)[0].strip() in (nn, nm_plain):
                        typ_detail, typ_src = v + " (reading, round2/old-house-heat.md)", "OHH"
    tier, tier_basis = tier_of(cid, rs)
    if not typ_detail:
        if tier == "D" and (BRAND_RX.search(name) or (review_tier.get(cid, ("", ""))[1] == "brand")):
            typ_detail, typ_src = "brand (company / maker / retailer channel; my reading from the name)", "name"
        else:
            nf = next((r.get("type") for s in ("round1", "r2-nexlev") for r in by.get(s, []) if r.get("type")), "")
            typ_detail, typ_src = (nf + "; not checked by thumbnail") if nf else "not checked", (SHORT["round1"] if nf else "")
    tcat = type_cat(typ_detail)
    if typ_src == "name":
        tcat = "brand"
    # --- persona / audience / topics
    persona = next((r.get("persona") for s in ("known8", "r2-nexlev", "round1") for r in by.get(s, []) if r.get("persona")), "")
    if not persona:
        desc = next((a["desc"] for a, _, _ in abouts if a["desc"]), "")
        persona = ("About text (not a reading): " + desc[:160]) if desc else "not checked"
    aud = next(((r.get("audience") or "").replace(" (reading)", "") for s in ("known8", "r2-nexlev", "round1") for r in by.get(s, []) if r.get("audience")), "")
    aud_src = "earlier helper's reading" if aud else ""
    if not aud:
        ra = review_tier.get(cid, ("", ""))[1]
        aud = {"brand": "mixed", "": ""}.get(ra, ra)
        if not aud:
            aud = {"A": "homeowner", "B": "homeowner", "C": "homeowner", "D": "trade", "X": "n/a (off-niche)"}[tier]
        aud_src = "my reading (2026-10-24)"
    topics = next((r.get("topics") for s in ("known8", "r2-nexlev", "round1") for r in by.get(s, []) if r.get("topics")), "")
    if not topics:
        if cid in sweep_topics:
            topics = "sweep keyword topics: " + sweep_topics[cid].replace(" ; ", ", ")
        elif by.get("oldheat-heat"):
            topics = "old-house heat (one returned video)"
        elif by.get("oldheat-ac"):
            topics = "AC (one returned video)"
        elif by.get("leads-hvac"):
            topics = by["leads-hvac"][0]["fit"].replace("up-next lead: ", "")
    # --- best known HVAC video: highest-view candidate from the HVAC-scoped sources
    bests = []
    for s in ("known8", "r2-nexlev", "round1", "leads-hvac", "oldheat-heat", "oldheat-ac", "sweep"):
        for r in by.get(s, []):
            if DROP_BEST.get(cid) == s:
                continue
            if r.get("best_id") and num(r.get("best_views")) is not None:
                bests.append((num(r["best_views"]), r.get("best_title", ""), r["best_id"], str(r.get("best_views")), r.get("best_src", SHORT[s]), r.get("date", "")))
    bests.sort(key=lambda x: (x[0], x[5]), reverse=True)
    best = bests[0] if bests else None
    # the same video seen in several pulls with different counts: keep the most recent pull's figure
    if best:
        same = sorted([b for b in bests if b[2] == best[2]], key=lambda x: x[5], reverse=True)
        best = same[0]
    # --- sweep figures
    sw = next(iter(by.get("sweep", [])), None)
    # --- NexLev extras (kept, not relied on)
    nl_out = next((r.get("nexlev_outlier") for s in ("r2-nexlev", "round1") for r in by.get(s, []) if r.get("nexlev_outlier") not in (None, "", "not found")), "")
    nl_flags = next((r.get("nexlev_flags") for r in by.get("r2-nexlev", []) if r.get("nexlev_flags")), "")
    nl_first = next((r.get("nexlev_first_video") for r in by.get("r2-nexlev", []) if r.get("nexlev_first_video") not in (None, "", "not found")), "")
    # --- NEW_12M
    joined = pick.get("joined", ("", "", ""))[0]
    new12, new_basis = "", ""
    if joined and joined >= "2025-10-24":
        new12, new_basis = "yes", f"joined {joined}"
    elif cid == "UCOyYTw-deou3ax6gvCmX2dg":
        new12, new_basis = "yes", "restart: account 2020, first HVAC video 2026-08-13 (seeds/known-channels-recheck.md)"
    elif nl_first and iso_date(nl_first) >= "2025-10-24" and joined and joined < "2025-10-24":
        new12, new_basis = "yes", f"restart: joined {joined}, NexLev first video {iso_date(nl_first)} (month only)"
    elif not joined:
        new12, new_basis = "not found", "no joined date"
    else:
        new12 = "no"
    persona_flag = "yes" if tcat in ("faceless persona", "AI avatar") else ""
    # --- notes
    for r in rs:
        if r.get("note") and r["src"] in ("known8", "round1-rejected", "known8-leads"):
            notes.append(r["note"])
        if r.get("resolved_by"):
            notes.append(f"ID resolved by {r['resolved_by']} ({r.get('name')})")
    if sw and sw.get("sweep_collab_hvac"):
        notes.append(f"{sw['sweep_collab_hvac']} of its sweep HVAC-title videos are collaboration uploads credited to it by oEmbed uploader name")
    if any(a[1].startswith("YouTube About (master-list helper)") for a in abouts) and name and not any(
            (r.get("name") or "").split(" and ")[0].strip().lower() == name.strip().lower() for r in rs if r.get("name")):
        notes.append("About title differs from the source name(s): " + "; ".join(sorted({r.get('name') for r in rs if r.get('name')}))[:120])
    if cid in EXTRA_NOTE:
        notes.append(EXTRA_NOTE[cid])
    found_by = " ; ".join(sorted({r.get("found") for r in rs if r.get("found")}))[:400]
    rows.append(dict(
        tier=tier, tier_basis=tier_basis, new_12m=new12, new_12m_basis=new_basis, persona_flag=persona_flag,
        name=name, handle=handle, channel_id=cid, link=f"https://www.youtube.com/channel/{cid}",
        type=tcat, type_detail=typ_detail, type_source=typ_src or "", nexlev_flags=nl_flags,
        persona_background=persona, audience=aud, audience_source=aud_src,
        subs=pick.get("subs", ("not found",))[0], subs_source=pick.get("subs", ("", ""))[1] if "subs" in pick else "",
        total_views=pick.get("views", ("not found",))[0], total_views_source=pick.get("views", ("", ""))[1] if "views" in pick else "",
        joined=joined or "not found", joined_source=pick.get("joined", ("", ""))[1] if "joined" in pick else "",
        video_count=pick.get("videos", ("not found",))[0], video_count_source=pick.get("videos", ("", ""))[1] if "videos" in pick else "",
        country=pick.get("country", ("not found",))[0],
        main_topics=topics or "not found",
        best_hvac_title=best[1] if best else "not found", best_hvac_id=best[2] if best else "", best_hvac_views=best[3] if best else "",
        best_hvac_source=best[4] if best else "",
        sweep_included_by=collect["sweep_incl"].get(cid, ""),
        sweep_videos=sw["sweep_videos"] if sw else "", sweep_hvac_title_videos=sw["sweep_hvac"] if sw else "",
        sweep_hvac_title_views=sw["sweep_hvac_views"] if sw else "", sweep_hvac_500k_videos=sw["sweep_big"] if sw else "",
        oldheat_videos=sum(r["pool_videos"] for r in by.get("oldheat-heat", [])) or "", oldheat_views=sum(r["pool_views"] for r in by.get("oldheat-heat", [])) or "",
        nexlev_outlier=nl_out, nexlev_first_video=nl_first,
        sources=" ; ".join(SHORT[s] for s in srcs), n_sources=len(srcs), found_by_detail=found_by,
        conflicts=" | ".join(conflicts), notes=" | ".join(notes)[:600],
    ))

# sort: tier, then subs desc
def subsk(r):
    return r["subs"] if isinstance(r["subs"], int) else -1
rows.sort(key=lambda r: ("ABCDX".index(r["tier"]), -subsk(r)))
cols = list(rows[0].keys())
out = os.path.join(RAW, "channels-master-2026-10-24.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)

# ------------------------------------------------------------------ stats
st = {}
st["total"] = len(rows)
st["by_tier"] = collections.Counter(r["tier"] for r in rows)
st["tier_type"] = collections.Counter(f"{r['tier']}|{r['type']}" for r in rows)
st["tier_aud"] = collections.Counter(f"{r['tier']}|{r['audience'].split(' ')[0]}" for r in rows)
st["tier_type_aud"] = collections.Counter(f"{r['tier']}|{r['type']}|{r['audience'].split(' ')[0]}" for r in rows)
src_n = collections.Counter(); combo = collections.Counter(); pair = collections.Counter(); only = collections.Counter()
for cid, rs in recs.items():
    ss = sorted({r["src"] for r in rs})
    for s in ss: src_n[s] += 1
    combo[len(ss)] += 1
    if len(ss) == 1: only[ss[0]] += 1
    for i in range(len(ss)):
        for j in range(i + 1, len(ss)):
            pair[f"{ss[i]}+{ss[j]}"] += 1
st["src_n"] = src_n; st["n_sources_hist"] = combo; st["pairs"] = pair; st["only"] = only
st["new12"] = collections.Counter(f"{r['tier']}|{r['new_12m']}" for r in rows)
st["persona"] = collections.Counter(f"{r['tier']}|{r['persona_flag']}" for r in rows)
st["gaps"] = dict(subs=sum(1 for r in rows if r["subs"] == "not found"), joined=sum(1 for r in rows if r["joined"] == "not found"),
                  videos=sum(1 for r in rows if r["video_count"] == "not found"))
st["gaps_ABCD"] = dict(subs=sum(1 for r in rows if r["subs"] == "not found" and r["tier"] != "X"), joined=sum(1 for r in rows if r["joined"] == "not found" and r["tier"] != "X"))
st["about_new"] = sum(1 for r in rows if "master-list helper" in r["subs_source"] or "master-list helper" in r["joined_source"])
st["conflicts"] = sum(1 for r in rows if r["conflicts"])
st["tier_basis"] = collections.Counter(r["tier_basis"].split("'")[0] for r in rows)
json.dump(st, open(OUT_STATS, "w"), indent=1, default=dict)
print(out, len(rows)); print(dict(st["by_tier"])); print(st["gaps"], st["about_new"], st["conflicts"])
