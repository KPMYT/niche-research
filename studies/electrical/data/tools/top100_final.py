#!/usr/bin/env python3
"""Build data/top100/top100-final.csv from top250-checked.csv plus checker E's fixes (2026-10-26).
One scope rule for theory and experiments: IN = home electrical work, household device safety, or shock / fire
danger to people (incl. battery explosion demos, "which one kills you"); OUT = pure theory with no home or safety angle.
Adds the videos checker E found missing; flags unnarrated "hack" channels (narrated = n) so the top 100 can be shown with and without them."""
import csv, json, os, subprocess, sys
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
YT = os.path.join(base, "tools", "yt.py")
rows = list(csv.DictReader(open(os.path.join(base, "top100", "top250-checked.csv"))))
_seen = {r["video_id"] for r in rows}
for r in csv.DictReader(open(os.path.join(base, "top100", "search-candidates-checked.csv"))):  # the helper's 15-keyword search finds
    if r["video_id"] not in _seen: rows.append(r); _seen.add(r["video_id"])
flip_in = {"sTSQwtwr-Gg": "battery explosion demo: danger to people (one rule, checker E)",
           "cTJh_bzI0QQ": "battery explosion demo: danger to people (one rule, checker E)"}
flip_out = {"S7C5sSde9e4": "general theory: AC vs DC, no home or safety angle (checker E)"}
add = {"WOK_EH5YHjM": ("lighting-led", "how-to", "19:43", 1183), "mmR5iEEP9q8": ("lighting-led", "how-to", "5:19", 319),
       "A3Dblph1fig": ("breakers-panels", "test", "17:41", 1061)}
unnarrated = {"BEEE Works", "Handcraft", "Inventor J", "DIYTechTrends", "DIY Hacks", "Tuan CT", "Invention 75", "Jr Electric School"}
for r in rows:
    if r["video_id"] in flip_in: r["status"], r["why_out"], r["notes"] = "in", "", (r["notes"] + " | " + flip_in[r["video_id"]]).strip(" |")
    if r["video_id"] in flip_out: r["status"], r["why_out"] = "out", flip_out[r["video_id"]]
have = {r["video_id"] for r in rows}
for vid, (sub, fmt, length, secs) in add.items():
    if vid in have: continue
    d = json.loads(subprocess.run([sys.executable, "-I", YT, "video", vid], capture_output=True, text=True).stdout)
    rows.append({"video_id": vid, "title": d["title"], "channel": d["channel"], "channel_id": d["channel_id"], "views": str(d["views"]),
                 "views_source": "yt.py video 2026-10-26 (checker E miss)", "upload_date": d["date"], "length": length, "length_s": str(secs),
                 "language": "en", "subniche": sub, "format": fmt, "status": "in", "why_out": "", "notes": "added after checker E (missed by the sweeps)"})
ins = [r for r in rows if r["status"] == "in"]
ins.sort(key=lambda r: -int(float(r["views"])))
out = []
for i, r in enumerate(ins[:100], 1):
    out.append({"rank": i, "video_id": r["video_id"], "title": r["title"], "channel": r["channel"], "channel_id": r["channel_id"],
                "views": r["views"], "upload_date": r["upload_date"], "length": r["length"], "subniche": r["subniche"], "format": r["format"],
                "narrated": "n (unnarrated hack / hands-only channel, flagged)" if r["channel"] in unnarrated else "y",
                "thumbnail": f"https://i.ytimg.com/vi/{r['video_id']}/hqdefault.jpg", "notes": r.get("notes", "")})
fn = os.path.join(base, "top100", "top100-final.csv")
with open(fn, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(out)
narr = [r for r in ins if r["channel"] not in unnarrated][:100]
fn2 = os.path.join(base, "top100", "top100-narrated.csv")
with open(fn2, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n"); w.writeheader()
    for i, r in enumerate(narr, 1):
        w.writerow({"rank": i, "video_id": r["video_id"], "title": r["title"], "channel": r["channel"], "channel_id": r["channel_id"], "views": r["views"],
                    "upload_date": r["upload_date"], "length": r["length"], "subniche": r["subniche"], "format": r["format"], "narrated": "y",
                    "thumbnail": f"https://i.ytimg.com/vi/{r['video_id']}/hqdefault.jpg", "notes": r.get("notes", "")})
print("in-scope pool", len(ins), "cut-off #100", out[-1]["views"], "| narrated-only cut-off", narr[-1]["views"] if len(narr) == 100 else "fewer than 100")
