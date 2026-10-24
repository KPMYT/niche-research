#!/usr/bin/env python3
"""Round 2 master channel list, step 4: write round2/channels-master.md from the master CSV (2026-10-24).

Usage: python3 -I master_report.py COLLECT.json STATS.json ABOUT_REQUESTED.txt XWHY.json TAIL.md ABOUT1.json [ABOUT2.json ...]
XWHY.json: {channel_id: why-X reading} for the X examples; TAIL.md: the problems and files sections, appended as written.
"""
import csv, json, os, sys, collections, re

HERE = os.path.dirname(os.path.abspath(__file__))
HV = os.path.normpath(os.path.join(HERE, "..", ".."))
RAW = os.path.join(HV, "data", "raw")
collect = json.load(open(sys.argv[1], encoding="utf-8"))
st = json.load(open(sys.argv[2], encoding="utf-8"))
requested = [l.strip() for l in open(sys.argv[3]) if l.strip()]
xwhy = json.load(open(sys.argv[4], encoding="utf-8")) if os.path.exists(sys.argv[4]) else {}
tail = open(sys.argv[5], encoding="utf-8").read() if os.path.exists(sys.argv[5]) else ""
about_new = {}
for p in sys.argv[6:]:
    about_new.update(json.load(open(p, encoding="utf-8")))
rows = list(csv.DictReader(open(os.path.join(RAW, "channels-master-2026-10-24.csv"), encoding="utf-8")))
recs = collect["recs"]
by_id = {r["channel_id"]: r for r in rows}


def n(x):
    try:
        return f"{int(x):,}"
    except Exception:
        return x or ""


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def trunc(s, k):
    s = s or ""
    return s if len(s) <= k else s[:k - 1].rstrip() + "\u2026"


L = []
A = L.append
A("# HVAC round 2: the master channel list (2026-10-24)")
A("")
A("Helper: round 2 master-list helper. Built 2026-10-24. Nothing committed or pushed. **Not yet re-checked by a second helper (working rule 3).**")
A("")
A("**What this is:** every channel found so far in the HVAC study (round 1 and round 2), merged into one list, one row per YouTube channel ID, and tiered so round 3 (the census) knows which channels to pull full metrics for. Full table, every column, every tier: `studies/hvac/data/raw/channels-master-2026-10-24.csv`.")
A("")
A("**NexLev RPM is not used** (operator, 2026-10-24). No NexLev revenue or RPM figure is in this list. NexLev's outlier score and first-video date are carried in the CSV only where an earlier helper pulled them.")
A("")
A("**Readings vs measurements.** Subscribers, total views, joined dates, video counts and view counts are measured (each with its source and pull date in the CSV). **Tier, type, audience and main topics are readings** (an earlier helper's or mine, marked in the CSV columns `tier_basis`, `type_source`, `audience_source`). \"not found\" = no source gave it.")
A("")
bt = st["by_tier"]
A("## Result")
A("")
A(f"**{st['total']:,} channels** in the master list.")
A("")
A("| Tier | Rule (my reading, applied to every channel) | Channels |")
A("|---|---|---:|")
rules = {
    "A": "HVAC-first for homeowners: HVAC is the channel's main subject (AC, heat pumps, furnaces, boilers, thermostats, filters, ducts, the heating / cooling bill).",
    "B": "General home DIY / home repair / handyman, with a real HVAC, insulation or bill share (not the main subject).",
    "C": "Adjacent lanes: off-grid and supplemental heat (wood, pellet, diesel, waste oil, \"free heat\"), outage / blackout, energy and insulation, product and brand verdict lists, frugal living, old-ways heating and cooling history.",
    "D": "Trade-facing (technicians, students, HVAC business) or a brand / contractor / retailer / manufacturer channel.",
    "X": "Off-niche: car AC, PC cooling, Indian / Pakistani-market AC, electronics, gaming, sport, news, sleep sounds, fan collectors, camping, single viral hits. Kept in the CSV, dropped from the census.",
}
for t in "ABCDX":
    A(f"| {t} | {rules[t]} | {bt.get(t, 0):,} |")
A(f"| | **Census (A to D)** | **{sum(bt.get(t, 0) for t in 'ABCD'):,}** |")
A("")
nn = collections.Counter(r["tier"] for r in rows if r["new_12m"] == "yes")
pp = collections.Counter(r["tier"] for r in rows if r["persona_flag"] == "yes")
A(f"Flags: **NEW_12M** (joined on or after 2025-10-24, or a restart in that window) = {sum(nn[t] for t in 'ABCD'):,} channels in tiers A-D ({', '.join(f'{t} {nn[t]}' for t in 'ABCD')}); {nn['X']} more in X. **PERSONA** (faceless persona or AI avatar, by an earlier type reading) = {sum(pp[t] for t in 'ABCD'):,} in tiers A-D ({', '.join(f'{t} {pp[t]}' for t in 'ABCD')}). Joined date not found for {sum(1 for r in rows if r['joined']=='not found' and r['tier']!='X')} A-D channels, so NEW_12M is a floor.")
A("")

# ---------------------------------------------------------------- method
A("## Method")
A("")
A("### 1. Sources")
A("")
A("| Source | File(s) | What was taken | Channels in the master list from it | Only in this source |")
A("|---|---|---|---:|---:|")
srcmeta = [
    ("known8", "seeds/known-channels-recheck.md (s.1-2)", "the 8 known channels, YT figures 2026-10-23, type readings, top video"),
    ("known8-leads", "seeds/known-channels-recheck.md (s.4 Leads)", "24 lead rows (26 channels; 3 by handle only, resolved below)"),
    ("round1", "seeds/channel-finds-round1.md, data/raw/channel-finds-round1.csv", "174 channels with fit, audience, type, About figures, example video"),
    ("round1-rejected", "seeds/channel-finds-round1.md (\"left out\")", "19 rejected candidates (names only; IDs matched by exact name in the round 1 raw JSON)"),
    ("leads-hvac", "seeds/leads-channels.md", "129 HVAC / partly HVAC up-next and similar-video leads"),
    ("leads-nonhvac", "seeds/leads-channels.md", "20 non-HVAC channels YouTube pairs with the seeds"),
    ("r2-nexlev", "round2/nexlev-channels.md, data/raw/round2-nexlev-channels.csv", "164 channels with fit, audience, type, NexLev flags, About figures"),
    ("oldheat-heat", "round2/old-house-heat.md, data/raw/round2-oldheat-2026-10-24.json (pool_heat)", "channels of the 380 kept old-house heat videos"),
    ("oldheat-ac", "same JSON (pool_ac)", "channels of the 315 kept AC videos in the helper's matched comparison set"),
    ("sweep", "round2/keyword-sweep.md, data/raw/sweep-channels-2026-10-24.csv, sweep-videos-2026-10-24.csv", "channels passing the rule below (and the sweep counts of every listed channel)"),
]
SHORT = {"known8": "K8", "known8-leads": "K8L", "round1": "R1", "round1-rejected": "R1X", "leads-hvac": "UN", "leads-nonhvac": "UNX",
         "r2-nexlev": "NX2", "oldheat-heat": "OHH", "oldheat-ac": "OHA", "sweep": "SW"}
for s, f, w in srcmeta:
    A(f"| {s} (`{SHORT[s]}`) | `{f}` | {w} | {st['src_n'].get(s, 0):,} | {st['only'].get(s, 0):,} |")
A("")
A("Silver Cymbal (`UC67dKTEwpAhKv2oYDATwR8g`) is in round 1's table and the sweep, so it is in the list; it is tiered B (on-camera general home DIY with a large HVAC share; reading).")
A("")
A("The old-house heat helper's AC pool is a set of AC channels it pulled only to compare with heat. I included its channels too (\"every channel found so far\"); 15 of them are found by no other source.")
A("")
A("### 2. The sweep rule")
A("")
sr = collect["sweep_rule"]; tot = collect["sweep_totals"]
incl = collect["sweep_incl"]
only_sweep = [cid for cid in incl if {r["src"] for r in recs[cid]} == {"sweep"}]
r3_ids = [cid for cid, why in incl.items() if why.startswith("3+")]
rb_ids = [cid for cid, why in incl.items() if not why.startswith("3+")]
A(f"The sweep returned {tot['videos']:,} distinct long-form English videos from {tot['channels_csv']:,} channel rows; {tot['hvac_title_videos']:,} of the videos have a title that passes the HVAC filter (`is_hvac` in `data/tools/autocomplete.py`, as already applied in `sweep-videos-2026-10-24.csv`, column `hvac_word_in_title`).")
A("")
A("A sweep channel is included when **(a)** it has **3 or more distinct returned long-form videos whose title passes the HVAC filter**, or **(b)** it has **at least one returned HVAC-title video with 500,000+ views**.")
A("")
A("| Rule | Channels meeting it | Of these, not found by any other source (added by the sweep alone) |")
A("|---|---:|---:|")
a_only = [c for c in r3_ids if c in only_sweep]
b_only = [c for c in rb_ids if c in only_sweep]
both = [c for c, w in incl.items() if "500K" in w and w.startswith("3+")]
A(f"| (a) 3+ HVAC-title videos | {len(r3_ids):,} | {len(a_only):,} |")
A(f"| (b) a 500K+ HVAC-title video, and fewer than 3 HVAC-title videos | {len(rb_ids):,} | {len(b_only):,} |")
A(f"| (both a and b) | {len(both):,} | (counted in a) |")
A(f"| **Total included from the sweep** | **{len(incl):,}** | **{len(only_sweep):,}** |")
A("")
A(f"Collaboration videos: the sweep CSV leaves the channel ID empty when a video is a collaboration (\"John The HVAC Guy and 9 more\"); {collect['sweep_collab'].get('attributed', 0) + collect['sweep_collab'].get('not attributed', 0)} sweep videos are like that. I credited each to its uploader (the oEmbed `author`, pulled by the sweep helper) when that name matched a channel already in the sources or resolved by search (below): {collect['sweep_collab'].get('attributed', 0)} credited, {collect['sweep_collab'].get('not attributed', 0)} not. That lifted {sr.get('rule A only because of collab videos', 0)} channels over the 3-video line that the sweep CSV's own count (`hvac_word_videos`, which skips collabs) leaves below it. The CSV keeps both: `sweep_hvac_title_videos` (with collabs) and the note.")
A("")
A("Reading: rule (b) is wide. Many of its channels are one viral video on a channel about something else (\"Hot vs Cold Room Challenge\", NBA \"Heat\", \"Furnace\" in a game). They are kept and tiered X, as the rule asks.")
A("")
A("### 3. IDs, duplicates and overlap")
A("")
res_p = os.path.join(RAW, "channels-master-resolve-2026-10-24.json")
res = json.load(open(res_p, encoding="utf-8")) if os.path.exists(res_p) else {}
ok = {k: v for k, v in res.items() if v.get("channelId")}
A(f"- Every source row was keyed by channel ID. Rows with no ID: 3 handle-only leads (`@PrimeRundown`, `@HullHonest`, `@GrillVerdict`), resolved from each handle's YouTube page (`channelMetadataRenderer`); collaboration rows in the old-house heat file (\"Vent Exposed and 3 more\", \"Sylvie Mercer and 3 more\" ...), credited to the lead channel by name.")
A(f"- Names searched on YouTube's channel search, accepted only on one exact-name match: {len(res)} looked up, **{len(ok)} resolved**, {len(res) - len(ok)} not (\"Handy Leo\": several channels have that exact name; left unresolved, so the one old-house heat video `QBTgvGGHl1U` (281 views) is not in the list). Script `data/tools/master_resolve.py`; results `data/raw/channels-master-resolve-2026-10-24.json` (pulled 2026-10-24). No NexLev `channel_resolver` call was needed.")
A("- The 19 round-1 rejected names were matched to IDs by exact name inside round 1's raw JSON (`channel-finds-nexlev-2026-10-23.json`, `channel-finds-ytsearch-*.json`); each About title was then checked (problems section).")
A(f"- Duplicates merged: {sum(len(v) for v in recs.values()):,} source records collapsed into {len(recs):,} channel IDs. Every source that found a channel is kept in the `sources` column (codes in the table above) and, where the source said how, in `found_by_detail`.")
A("")
h = st["n_sources_hist"]
A("| Sources finding the channel | Channels |")
A("|---|---:|")
for k in sorted(h, key=int):
    A(f"| {k} | {h[k]:,} |")
A("")
A("Overlap between sources (channels found by both; the biggest pairs):")
A("")
A("| Pair | Channels |")
A("|---|---:|")
for k, v in sorted(st["pairs"].items(), key=lambda x: -x[1])[:16]:
    a, b = k.split("+")
    A(f"| {SHORT[a]} + {SHORT[b]} | {v:,} |")
A("")
A(f"Of the {st['src_n'].get('round1', 0)} round-1 channels, {st['pairs'].get('round1+sweep', 0)} were returned again by the sweep; of the {st['src_n'].get('r2-nexlev', 0)} NexLev round-2 channels, {st['pairs'].get('r2-nexlev+sweep', 0)}.")
A("")
A("### 4. Merging and gap-filling")
A("")
ok_new = {k: v for k, v in about_new.items() if "error" not in v and v.get("subscriberCountText")}
A(f"- **Most recent pull wins.** For subscribers, total views, joined date, video count and country, every candidate value was collected (About panels pulled by the round 1, up-next, round 2 NexLev and old-house heat helpers; the source tables; my own About pulls) and the latest pull kept, with its source in the `*_source` columns. Where another source differs by more than 5% (or a different joined date), the CSV `conflicts` column gives both ({st['conflicts']} channels).")
A(f"- **About pages for the gaps.** {len(requested):,} channels had no subscriber / joined / video-count figure in any source. Their YouTube About panels were pulled logged out (`data/tools/master_about.py`, the `yt_water1.py about` method, about 1 s between channels, 4 workers, 2026-10-24); raw panels in `data/raw/channels-master-about-2026-10-24.json`. **{len(ok_new):,} returned figures**; {len(requested) - len(ok_new)} did not (no About panel, a terminated or missing channel, or a parse error). Still not found after this: subscribers for {st['gaps']['subs']:,} channels ({st['gaps_ABCD']['subs']} in tiers A-D), joined date for {st['gaps']['joined']:,} ({st['gaps_ABCD']['joined']} in A-D).")
A("- **Type** comes from the earlier helpers' readings (known 8, round 1, round 2 NexLev, the old-house heat faceless table). For channels no one had looked at, it is \"not checked\" (round 3 looks at thumbnails), except channels tiered D whose name is plainly a company (\"... Heating & Air\", \"... LLC\", \"... Supply\"): those are \"brand\" (my reading from the name). Type categories: on camera / faceless / AI avatar / faceless persona / brand / not checked; the earlier wording is kept in `type_detail`.")
A("- **Best known HVAC video:** the highest-view HVAC-scope video any source recorded for the channel (the known-channel top video, round 1 / round 2 example video, the up-next example, the old-house heat or AC pool video, or the sweep's biggest HVAC-title video). The same video seen in several pulls keeps the latest pull's count. Up-next figures are YouTube's rounded short text (\"763K\") and are kept as given.")
A("- **Sweep columns** (every listed channel the sweep returned): videos returned, HVAC-title videos returned (with collabs), their total views, and how many of them have 500K+ views.")
A("- **Audience:** earlier helpers' reading where they gave one; otherwise mine from the titles (A-C homeowner unless stated; D trade, or mixed for brand channels).")
A("- **NEW_12M:** joined date on or after 2025-10-24 (About panel), or a restart: John The HVAC Guy (2020 account, first HVAC video 2026-08-13, per the known-channels re-check) and round 2 channels whose NexLev first-video date is in the window while the account is older (NexLev dates read as month only).")
A("- **PERSONA:** type is faceless persona or AI avatar. Only channels an earlier helper typed can carry it, so it is a floor: most sweep-only channels are \"not checked\".")
A("")
A("### 5. How tiers were read")
A("")
tb = collections.Counter()
for r in rows:
    b = r["tier_basis"]
    b = re.sub(r"'.*'", "'...'", b)
    tb[b] += 1
A("| Basis | Channels |")
A("|---|---:|")
for k, v in tb.most_common():
    A(f"| {esc(k)} | {v:,} |")
A("")
A("Earlier fit tags were mapped as: HVAC -> A (D if the earlier audience was \"trade\"), DIY -> B, ENERGY / OUTAGE / OFFGRID -> C, TRADE / BRAND -> D; ADJ channels were read one by one (12). Round-1 rejects stay X (Patina is the exception: round 2 re-found and kept it, so the latest reading, C, wins). For the 1,565 channels no earlier helper had tagged, I read each one's returned titles (up to 5 HVAC-title and other titles, with views) and its name; these readings are in the build script inputs and the CSV says which basis each row has.")
A("")

# ---------------------------------------------------------------- counts
A("## Counts by tier x type x audience")
A("")
types = ["on camera", "faceless", "faceless persona", "AI avatar", "brand", "not checked"]
A("**Tier x type** (type is an earlier helper's reading or \"not checked\")")
A("")
A("| Tier | " + " | ".join(types) + " | Total |")
A("|---|" + "---:|" * (len(types) + 1))
for t in "ABCDX":
    c = collections.Counter(r["type"] for r in rows if r["tier"] == t)
    A(f"| {t} | " + " | ".join(str(c.get(x, 0)) for x in types) + f" | {sum(c.values())} |")
A("")
auds = ["homeowner", "mixed", "trade", "n/a"]
A("**Tier x audience** (reading)")
A("")
A("| Tier | " + " | ".join(auds) + " |")
A("|---|" + "---:|" * len(auds))
for t in "ABCDX":
    c = collections.Counter(r["audience"].split(" ")[0] for r in rows if r["tier"] == t)
    A(f"| {t} | " + " | ".join(str(c.get(x, 0)) for x in auds) + " |")
A("")
A("**Tier x type x audience** (A to D; zero cells left out)")
A("")
A("| Tier | Type | homeowner | mixed | trade |")
A("|---|---|---:|---:|---:|")
for t in "ABCD":
    for ty in types:
        c = collections.Counter(r["audience"].split(" ")[0] for r in rows if r["tier"] == t and r["type"] == ty)
        if sum(c.values()):
            A(f"| {t} | {ty} | {c.get('homeowner', 0)} | {c.get('mixed', 0)} | {c.get('trade', 0)} |")
A("")


# ---------------------------------------------------------------- tier tables
def flags(r):
    f = []
    if r["new_12m"] == "yes":
        f.append("NEW_12M")
    if r["persona_flag"] == "yes":
        f.append("PERSONA")
    return " ".join(f)


def best_cell(r):
    if not r["best_hvac_id"]:
        return "not found"
    return f"\"{esc(trunc(r['best_hvac_title'], 70))}\" `{r['best_hvac_id']}` {n(r['best_hvac_views'])}"


def sweep_cell(r):
    if r["sweep_hvac_title_videos"] in ("", None):
        return ""
    return f"{r['sweep_hvac_title_videos']} / {n(r['sweep_hvac_title_views'])}"


blurb = {
    "A": "HVAC-first for homeowners. These are the census core.",
    "B": "General home DIY / repair channels with a real HVAC, insulation or bill share.",
    "C": "Adjacent lanes: off-grid heat, outage, energy / insulation, product and brand verdicts, frugal living.",
    "D": "Trade-facing or brand / contractor / retailer / manufacturer channels.",
}
for t in "ABCD":
    rr = [r for r in rows if r["tier"] == t]
    A(f"## Tier {t} ({len(rr)} channels)")
    A("")
    A(blurb[t] + " Sorted by subscribers (latest pull; \"not found\" last). Subs and joined: YouTube About unless the CSV says otherwise. Best HVAC video: title, ID, views (source in the CSV). Sweep: HVAC-title videos returned / their total views.")
    A("")
    A("| # | Channel | Handle | Channel ID | Type (reading) | Audience (reading) | Subs | Joined | Videos | Country | Best known HVAC video | Sweep HVAC vids / views | Sources | Flags |")
    A("|---:|---|---|---|---|---|---:|---|---:|---|---|---|---|---|")
    for i, r in enumerate(rr, 1):
        A(f"| {i} | {esc(trunc(r['name'], 40))} | {esc(r['handle'])} | `{r['channel_id']}` | {r['type']} | {r['audience']} | {n(r['subs'])} | {r['joined']} | {n(r['video_count'])} | {esc(r['country'])} | {best_cell(r)} | {sweep_cell(r)} | {r['sources']} | {flags(r)} |")
    A("")

# ---------------------------------------------------------------- NEW_12M
nr = [r for r in rows if r["new_12m"] == "yes" and r["tier"] != "X"]
A(f"## NEW_12M: started since 2025-10-24 (tiers A to D, {len(nr)} channels)")
A("")
A("Joined on or after 2025-10-24 (About panel) or a restart in that window. Sorted by tier, then subscribers. \"Taking off\" is not judged here (round 3 pulls the metrics); best known video is shown for a first look.")
A("")
A("| # | Tier | Channel | Channel ID | Type (reading) | Subs | Joined / restart | Best known HVAC video | Flags |")
A("|---:|---|---|---|---|---:|---|---|---|")
for i, r in enumerate(nr, 1):
    A(f"| {i} | {r['tier']} | {esc(trunc(r['name'], 40))} | `{r['channel_id']}` | {r['type']} | {n(r['subs'])} | {esc(r['new_12m_basis'])} | {best_cell(r)} | {flags(r)} |")
A("")
xn = [r for r in rows if r["new_12m"] == "yes" and r["tier"] == "X"]
A(f"{len(xn)} more NEW_12M channels are tier X (in the CSV).")
A("")

# ---------------------------------------------------------------- PERSONA
pr = [r for r in rows if r["persona_flag"] == "yes"]
A(f"## PERSONA: faceless personas and AI avatars ({len(pr)} channels)")
A("")
A("Type from an earlier helper's thumbnail / About reading (`type_source`). Roger the HVAC Guy is planned as this type. Sorted by tier, then subscribers.")
A("")
A("| # | Tier | Channel | Channel ID | Type | Persona / background (as recorded) | Subs | Joined | Best known HVAC video | NEW_12M |")
A("|---:|---|---|---|---|---|---:|---|---|---|")
for i, r in enumerate(pr, 1):
    A(f"| {i} | {r['tier']} | {esc(trunc(r['name'], 36))} | `{r['channel_id']}` | {r['type']} | {esc(trunc(r['persona_background'], 90))} | {n(r['subs'])} | {r['joined']} | {best_cell(r)} | {r['new_12m']} |")
A("")

# ---------------------------------------------------------------- X
xr = [r for r in rows if r["tier"] == "X"]
A(f"## Tier X: off-niche ({len(xr)} channels; dropped from the census, kept in the CSV)")
A("")
A("20 examples (the biggest by subscribers, one per kind where possible), with why they are X (my reading):")
A("")
A("| # | Channel | Channel ID | Subs | Returned HVAC-title video that brought it in | Why X |")
A("|---:|---|---|---:|---|---|")
why = {}
ex = sorted([r for r in xr if isinstance(r["subs"], str) and r["subs"].isdigit()], key=lambda r: -int(r["subs"]))
picked = []
seen_first = set()
for r in ex:
    w = r["name"].split()[0].lower() if r["name"] else ""
    if w in seen_first:
        continue
    seen_first.add(w)
    picked.append(r)
    if len(picked) == 20:
        break
for i, r in enumerate(picked, 1):
    A(f"| {i} | {esc(trunc(r['name'], 36))} | `{r['channel_id']}` | {n(r['subs'])} | {best_cell(r)} | {esc(xwhy.get(r['channel_id'], trunc(r['main_topics'], 60)))} |")
A("")
open(os.path.join(HV, "round2", "channels-master.md"), "w", encoding="utf-8").write("\n".join(L) + "\n" + tail)
print(len(L))
