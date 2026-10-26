#!/usr/bin/env python3
"""Build channels.md / channels.csv (deliverable 1) and new-channels.md (deliverable 2) from the census, NexLev daily figures,
channel medians and the corrected presenter table. Monthly views = NexLev 30-day views (get_daily_analytics) when current and
possible; estimated monthly earnings = 30-day views x NexLev RPM / 1000 (an estimate; ad revenue only)."""
import csv, os, re, statistics
from collections import Counter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."); S = os.path.join(D, "..")
def rd(p): return list(csv.DictReader(open(os.path.join(D, p))))
def num(x):
    m = re.search(r"-?[\d,.]+\s*[KMB]?", str(x or ""))
    if not m: return None
    t = m.group(0).replace(",", "").strip(); mult = 1
    if t[-1:] in "KMB": mult = {"K": 1e3, "M": 1e6, "B": 1e9}[t[-1]]; t = t[:-1]
    try: return int(float(t) * mult)
    except: return None
def esc(t): return (t or "").replace("|", "/").replace("\n", " ").strip()
cen = [r for r in rd("census/census-all.csv")]
daily = {r["channel_id"]: r for r in rd("census/nexlev-daily.csv")}
med = {r["channel_id"]: r for r in rd("medians/channel-medians.csv") if r["median"]}
out = []
for r in cen:
    d = daily.get(r["channel_id"], {}); note = d.get("notes", "") or ""
    v30 = num(d.get("view30Day")); bad = (v30 is None or v30 < 0 or "stale" in note.lower() or "not found" in note.lower()
                                          or (num(d.get("currentViews")) is not None and v30 > (num(d.get("currentViews")) or 0)))
    rpm = None
    try: rpm = float(re.search(r"\d+(\.\d+)?", r["rpm"]).group(0)) if r["rpm"] and "null" not in r["rpm"].lower() else None
    except: rpm = None
    mv = "" if bad else v30
    earn = round(mv * rpm / 1000) if (mv != "" and rpm) else ""
    m = med.get(r["channel_id"], {})
    out.append({"name": r["name"], "handle": r["handle"], "channel_id": r["channel_id"], "link": f"https://www.youtube.com/channel/{r['channel_id']}",
                "scope": r["scope"], "type": r["type"], "persona": r["persona"], "claimed_background": r["claimed_background"], "subs": r["subs"],
                "total_views": r["total_views"], "joined": r["started_join"], "first_upload": r["first_upload"], "new_12mo": r["new_12mo"],
                "videos": r["videos_count"], "uploads_last_90d": r["uploads_last_90d"],
                "monthly_views_30d": mv, "monthly_views_note": ("unreliable or missing: " + note[:120]) if bad else "NexLev get_daily_analytics view30Day, 2026-10-26",
                "rpm": rpm or "", "est_monthly_earnings_usd": earn, "nexlev_outlier": r["nexlev_outlier"],
                "median_longform_views": m.get("median", ""), "median_basis": m.get("basis", ""),
                "top3": r["top3"], "main_subniches": r["main_subniches"], "sells": r["sells"], "inscope_share_popular30": r["inscope_share_popular30"],
                "source": r["source"], "pulled": r["pulled"], "notes": r["notes"]})
with open(os.path.join(S, "channels.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(out)
inscope = [r for r in out if r["scope"] in ("core", "partial")]
def key(r): return -(num(r["subs"]) or 0)
def row(r):
    return (f"| [{esc(r['name'])}]({r['link']}) | {r['scope']} | {esc(r['type'])} | {esc(r['claimed_background'])} | {esc(str(r['subs']).split('(')[0])} | "
            f"{esc(str(r['first_upload']).split('(')[0])} | {esc(str(r['uploads_last_90d']).split('(')[0])} | {r['monthly_views_30d'] if r['monthly_views_30d']=='' else f'{r[chr(109)+chr(111)+chr(110)+chr(116)+chr(104)+chr(108)+chr(121)+chr(95)+chr(118)+chr(105)+chr(101)+chr(119)+chr(115)+chr(95)+chr(51)+chr(48)+chr(100)]:,}'} | "
            f"{r['rpm']} | {('$'+format(r['est_monthly_earnings_usd'],',')) if r['est_monthly_earnings_usd']!='' else ''} | {esc(str(r['median_longform_views']))} | {esc(r['top3'])[:260]} | {esc(r['main_subniches'])} | {esc(r['sells'])} |")
H = ["| Channel | Scope | Type | Claimed background | Subs | First upload | Uploads, 90 days | Monthly views (30 d) | RPM | Est. $/month | Median long-form views | Top 3 videos | Main sub-niches | Sells |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
o = ["# The channel census (deliverable 1)", "",
     f"{len(out)} channels from the round 2 master list (957 found, re-scoped under the narrow scope), each pulled in round 3 (2026-10-26): {sum(1 for r in out if r['scope']=='core')} core, {sum(1 for r in out if r['scope']=='partial')} partial, {sum(1 for r in out if r['scope']=='out')} re-judged out. Full data, sources and notes per channel: `channels.csv`.", "",
     "**Sources and limits:** subs, total views, join date: YouTube About pages. Monthly views: NexLev's 30-day views (`get_daily_analytics`), blank where NexLev had nothing current or gave an impossible value (e.g. more views in 30 days than in the channel's life; 43 such rows flagged). **Estimated earnings = 30-day views × NexLev RPM**, ad revenue only, an estimate. NexLev's outlier score exists only for channels in its niche-finder database. Median long-form views: our own pull (`data/medians/`). **Type** (on camera / faceless / AI persona) is judged from thumbnails, because NexLev marks AI-image personas \"not faceless\". Scope and type are readings (checker E: about 13% disagreement on scope).", "",
     "## Core channels (most of their long-form videos are in scope), by subscribers", ""] + H + [row(r) for r in sorted([r for r in out if r["scope"] == "core"], key=key)]
o += ["", "## Partial channels (general DIY or science channels with in-scope hits), by subscribers", ""] + H + [row(r) for r in sorted([r for r in out if r["scope"] == "partial"], key=key)]
tc = Counter(r["type"].split("(")[0].strip() for r in inscope); bc = Counter(r["claimed_background"].split("(")[0].strip() for r in inscope)
o += ["", "## Counts (core and partial)", "", "| Type (reading) | Channels |", "|---|---|"] + [f"| {k} | {n} |" for k, n in tc.most_common()]
o += ["", "| Claimed background | Channels |", "|---|---|"] + [f"| {k} | {n} |" for k, n in bc.most_common()]
pres = rd("checks/presenters-summary-corrected.csv")
o += ["", "## Who presents, and how they perform (for the open decision on Frederick's background)", "",
      "From the round 2 presenter search (138 channels found by trade keywords, 122 counted), corrected by checker D (52 channels re-checked by description and thumbnails). \"Median of channel medians\" = the typical channel's typical long-form video. The round 3 investigator look (`data/investigator/report.md`) adds: no real fire investigator channel over 10K subscribers; persona \"investigator\" titles perform like the firefighter lists (about 100-300 views).", "",
      "| Background | Channels | Over 10K subs | Median of channel medians | Best in-scope video | Note |", "|---|---|---|---|---|---|"]
o += [f"| {p['background']} | {p['channels']} | {p['over_10k_subs']} | {p['median_of_channel_medians']} | {esc(p['best_in_scope_video'])} | {esc(p['note'])} |" for p in pres]
open(os.path.join(S, "channels.md"), "w").write("\n".join(o) + "\n")
# ---------- new channels ----------
def topv(r):
    vs = [num(x) for x in re.findall(r"\]\s*([\d,]+)", r["top3"] or "")]
    return max([v for v in vs if v] or [0])
new = [r for r in inscope if str(r["new_12mo"]).lower().startswith("y")]
for r in new:
    r["_top"] = topv(r); s = num(r["subs"]) or 0
    r["_why"] = []
    if r["_top"] >= 100_000: r["_why"].append("a video over 100K")
    if r["monthly_views_30d"] not in ("", None) and r["monthly_views_30d"] >= 100_000: r["_why"].append("100K+ views in 30 days")
    mm = num(r["median_longform_views"])
    if mm and s and mm >= 2 * s and mm >= 1000: r["_why"].append("median video at least 2x its subscribers (and 1K+)")
taking = sorted([r for r in new if r["_why"]], key=lambda r: -r["_top"])
o = ["# New channels taking off (deliverable 2)", "",
     f"Channels in the census (core and partial) whose first visible upload is in the last 12 months (or a relaunch in that window): {len(new)}. \"Taking off\" = at least one of: a long-form video over 100K views; 100K+ views in the last 30 days (NexLev); a median long-form video at least twice its subscriber count and at least 1,000 views. {len(taking)} qualify. Many \"new\" channels are older accounts relaunched or repurposed (first visible upload is a junk clip or years after joining); `channels.csv` notes each. Views from list pages (rounded) unless noted; data 2026-10-26.", "",
     "| Channel | Scope | Type | Claimed background | Subs | First upload | Monthly views (30 d) | Why | Videos that took it off |", "|---|---|---|---|---|---|---|---|---|"]
for r in taking:
    o.append(f"| [{esc(r['name'])}]({r['link']}) | {r['scope']} | {esc(r['type'])} | {esc(r['claimed_background'])} | {esc(str(r['subs']).split('(')[0])} | {esc(str(r['first_upload']).split('(')[0])} | {r['monthly_views_30d'] if r['monthly_views_30d']=='' else format(r['monthly_views_30d'],',')} | {'; '.join(r['_why'])} | {esc(r['top3'])[:300]} |")
rest = [r for r in new if not r["_why"]]
o += ["", f"## New but not taking off ({len(rest)})", "", ", ".join(f"{esc(r['name'])} ({esc(str(r['subs']).split('(')[0])}, {esc(r['type'])})" for r in sorted(rest, key=key)), "",
      "Round 1's new-channel hunts (`data/new-channels-nexlev/`, `data/new-channels-search/`) also list adjacent new channels (blackouts, heat without power, seniors' safety) that the operator ruled out of scope on 2026-10-24."]
open(os.path.join(S, "new-channels.md"), "w").write("\n".join(o) + "\n")
print("channels", len(out), "in scope", len(inscope), "new", len(new), "taking off", len(taking), "with monthly views", sum(1 for r in out if r["monthly_views_30d"] != ""), "with earnings", sum(1 for r in out if r["est_monthly_earnings_usd"] != ""))
