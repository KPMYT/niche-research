#!/usr/bin/env python3
"""Round 5 thumbnail page (2026-10-26, main session). Reads thumbnails/labels-top-winners.csv and
thumbnails/labels-channel-top5.csv and the images in thumbnails/img/, makes 320x180 copies as data URIs, and writes
thumbnails/thumbnail-styles.html (one self-contained page: thumbnails grouped by style, views and multiple under each,
counts of which styles go with the biggest videos, and each persona channel's house style).
Usage: python3 -I thumb_page.py"""
import base64, csv, io, json, os, statistics
from collections import Counter, defaultdict
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.dirname(os.path.dirname(HERE))
TH = os.path.join(STUDY, "thumbnails")


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def clean(t):
    """Labels quoted some titles with a markdown-escaped bar ("\\|"); show the plain character."""
    return (t or "").replace("\\|", "|").replace("\\", "")


def small(vid):
    p = os.path.join(TH, "img", vid + ".jpg")
    if not os.path.exists(p):
        return None
    im = Image.open(p).convert("RGB")
    w, h = im.size
    tw = int(h * 16 / 9)
    if tw < w:  # crop letterbox to 16:9
        x = (w - tw) // 2; im = im.crop((x, 0, x + tw, h))
    else:
        th = int(w * 9 / 16); y = (h - th) // 2; im = im.crop((0, y, w, y + th))
    im = im.resize((320, 180), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=62, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def main():
    vids = {}
    for r in csv.DictReader(open(os.path.join(TH, "labels-top-winners.csv"), encoding="utf-8")):
        sets = []
        for s in r["list"].split(";"):
            sets.append({"top100": "top100", "recent-12m": "r12", "recent-90d": "r90"}.get(s.strip(), s.strip()))
        vids[r["video_id"]] = {"id": r["video_id"], "t": clean(r["title"]), "c": r["channel"], "v": num(r["views"]),
                               "m": num(r["multiple"]), "g": r["style_group"], "w": clean(r["text_words"]), "d": r["upload_date"],
                               "rank": r["rank"], "sets": sets, "look": r["overall_look"], "person": r["person"]}
    personas = defaultdict(list)
    chan_meta = {}
    for r in csv.DictReader(open(os.path.join(TH, "labels-channel-top5.csv"), encoding="utf-8")):
        if r["style_group"] == "not labelled yet":
            continue
        v = vids.get(r["video_id"])
        if not v:
            v = {"id": r["video_id"], "t": clean(r["title"]), "c": r["channel"], "v": num(r["views"]), "m": num(r["multiple"]),
                 "g": r["style_group"], "w": clean(r["text_words"]), "d": "", "rank": "", "sets": [], "look": r["overall_look"],
                 "person": r["person"]}
            vids[r["video_id"]] = v
        if "ch5" not in v["sets"]:
            v["sets"].append("ch5")
        v["chrank"] = r["rank_in_channel"]
        chan_meta[r["channel"]] = {"tier": r["tier"], "type": r["type"]}
        personas[r["channel"]].append(r["video_id"])
    for v in vids.values():
        v["img"] = small(v["id"])
    groups = Counter(v["g"] for v in vids.values())
    # which styles go with the biggest videos (top 100 by rank)
    top = sorted([v for v in vids.values() if "top100" in v["sets"]], key=lambda v: -(v["v"] or 0))
    def share(vs):
        c = Counter(v["g"] for v in vs); return {k: c[k] for k in c}
    stats = {}
    for g in groups:
        vs = [v for v in vids.values() if v["g"] == g]
        views = [v["v"] for v in vs if v["v"]]
        stats[g] = {"n": len(vs), "medv": statistics.median(views) if views else None,
                    "top10": sum(1 for v in top[:10] if v["g"] == g), "top25": sum(1 for v in top[:25] if v["g"] == g),
                    "top100": sum(1 for v in top if v["g"] == g),
                    "r12": sum(1 for v in vs if "r12" in v["sets"]), "r90": sum(1 for v in vs if "r90" in v["sets"]),
                    "ch5": sum(1 for v in vs if "ch5" in v["sets"])}
    chans = []
    for ch, ids in personas.items():
        m = chan_meta.get(ch, {})
        chans.append({"c": ch, "tier": m.get("tier", ""), "type": m.get("type", ""), "ids": ids})
    chans.sort(key=lambda x: (x["type"] != "faceless persona", -max((vids[i]["v"] or 0) for i in x["ids"])))
    data = {"vids": list(vids.values()), "stats": stats, "chans": chans}
    tpl = open(os.path.join(HERE, "thumb_page_template.html"), encoding="utf-8").read()
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, separators=(",", ":")))
    out = os.path.join(TH, "thumbnail-styles.html")
    open(out, "w", encoding="utf-8").write(html)
    print(out, len(vids), "videos", len(chans), "channels", round(len(html) / 1e6, 2), "MB")


if __name__ == "__main__":
    main()
