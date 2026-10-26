#!/usr/bin/env python3
"""Deliverables 6 and 7 (HVAC study, round 3): the top 100 long-form English HVAC videos of all time, and what has
worked recently (last 90 days, last 12 months; by views and by multiple; rising / falling). Written 2026-10-26.

Stages
  python3 -I top_build.py pool <scratch_dir>     build the candidate pool, write ids to pull (no network)
  python3 -I top_build.py build <exact.jsonl> [<baselines.json>]
                                                 read the exact pulls (top_pull.py output) and the extra channel
                                                 baselines, apply the hand review, write the outputs.

Video pool (stated in the outputs):
  (a) raw/census-videos-2026-10-26.csv: every long-form (>= 5:00) video the census pulled from the 1,122 channels
      of the round 2 master list's tiers A-D (Latest, Popular, Oldest; up to ~120 each). After the census re-tier
      some of these channels are X; their videos stay in the pool for the top lists (so big HVAC videos on
      off-niche channels count), and are left out of the rising / falling comparison (A-D only).
  (b) raw/sweep-videos-2026-10-24.csv: keyword-sweep videos from any channel (exact views from search pages).
  In scope = HVAC title by the census rule (census_build.hvac_title) or the census is_hvac mark, then a rule
  pre-filter (off-scope words, logged) and a HAND REVIEW of every title that would enter a list (logged).
Everything here that is a label (sub-niche, format, emotions, villain, scope) is a READING.
"""
import csv, json, os, re, statistics, sys
from collections import Counter, defaultdict
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(os.path.dirname(HERE), "raw")
STUDY = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from census_build import hvac_title, subniche as rule_subniche  # noqa: E402
from sweep_build import tag_format, english_check  # noqa: E402

TODAY = date(2026, 10, 26)
D90 = TODAY - timedelta(days=90)     # 2026-07-28
D365 = TODAY - timedelta(days=365)   # 2025-10-26
AGE_RX = re.compile(r"^(Streamed )?(\d+)\s*(min|h|d|w|mo|y)\s+ago$")


def age(t):
    m = AGE_RX.match((t or "").replace("\xa0", " ").strip())
    return (int(m.group(2)), m.group(3)) if m else None


def maybe_in(agetext, days):
    """Could the age text fall inside the window? Generous on purpose (exact dates decide later)."""
    a = age(agetext)
    if not a:
        return False
    n, u = a
    if u in ("min", "h", "d", "w"):
        return True
    if u == "mo":
        return n <= (3 if days == 90 else 12)
    if u == "y":
        return days == 365 and n == 1
    return False


# ---------------------------------------------------------------------------------------------------------------
# Rule pre-filter: clear off-scope titles (brief: kids' "hot vs cold" challenges, games, car AC, commercial /
# industrial HVAC and training, non-English; plus the census scope rules). Each drop is logged with its rule.
# ---------------------------------------------------------------------------------------------------------------
PRE = [
    ("kids / challenge video", r"\bchallenge\b|\bhot (vs\.?|and|or) cold\b|\bcold (vs\.?|and|or) hot\b|\bprank\b|\bkids?\b.*\b(play|fun)|"
                               r"\bnursery\b|\bcartoon\b|\banimated\b|\bepisode\b|\bmagic air conditioner\b|\bloud house\b|\bcasagrandes\b|"
                               r"\btoys?\b|\bdoll\b|\bbarbie\b|\bpeppa\b|\bmasha\b|\bcocomelon\b"),
    ("game", r"\bminecraft\b|\broblox\b|\bfortnite\b|\bgta\b|\bsims\b|\bgameplay\b|\bsimulator\b|\bpokemon\b"),
    ("vehicle / RV AC or heat", r"\bcars?\b|\btrucks?\b|\bvehicles?\b|\bheater core\b|\bautomotive\b|\bjeep\b|\bhonda\b|\btoyota\b|"
                                r"\bford\b|\bchevy\b|\bchevrolet\b|\bf-?150\b|\btesla\b|\brv\b|\bcamper\b|\bvan ?life\b|\bvan\b|\bbus\b|"
                                r"\bsuv\b|\bmotorhome\b|\bcaravan\b|\btractor\b|\bboat\b|\bmechanics?\b|\brecharge your ac system\b|"
                                r"\bac system\b.*\b(recharge|refill)|\bcar ac\b|\bnissan\b|\bbmw\b|\bmercedes\b|\bhyundai\b|\bkia\b|\bsubaru\b|\bdodge\b|\bram 1500\b|\bdiesel engine\b"),
    ("commercial / industrial / trade training", r"\bpower plant\b|\bthermal power\b|\bindustrial\b|\bcommercial\b|\bchillers?\b|\bfactory\b|"
                                                 r"\bmanufacturing\b|\bmaking of\b|\bcooling tower\b|\brooftop units?\b|\brtu\b|\bepa ?608\b|"
                                                 r"\bhvac (school|training|students?|apprentice|career|business)\b|\bapprentice\b|\bsuperheat\b|"
                                                 r"\bsubcool|\bvrf\b|\bvrv\b|\bdata cent(er|re)\b|\bship\b|\bsteam turbine\b|\beconomizer\b|"
                                                 r"\barc furnace\b|\bsmelt|\bforge\b|\bfoundry\b|\bmetal (casting|melting)\b|\bkiln\b"),
    ("bushcraft / camping shelter (not home heat)", r"\bbushcraft\b|\bcamping\b|\bshelter\b|\btent\b|\bcamp\b|\bhammock\b|\bsurvival shelter\b|\bdugout\b|\bigloo\b|\bsnow cave\b"),
    ("electronics / non-HVAC gadget", r"\bcapacitors? explained\b|\bfan capacitor\b|\bwinding machine\b|\bcoil winding\b|\bceiling fan\b|"
                                      r"\bunboxing\b|\bmini fan\b|\bneck fan\b|\bhand(held)? fan\b|\bpc\b|\bgpu\b|\bcpu\b|\blaptop\b|\bphone\b|\bthermoelectric generator\b|\barduino\b|\bpeltier\b(?!.*\b(air conditioner|ac|cool (your|a|the) room))"),
]
PRE_RX = [(n, re.compile(p, re.I)) for n, p in PRE]
# DIY / craft stove builds whose packaging is the build (cement, bricks, barrels, sinks, plastic chairs) with no
# heating word: read as craft / cooking stoves, not home heating. Main-session default to confirm with the operator.
CRAFT_STOVE = re.compile(r"\b(stoves?|furnaces?)\b", re.I)
CRAFT_WORDS = re.compile(r"\bcement\b|\bconcrete\b|\bbricks?\b|\bbarrels?\b|\bsinks?\b|\bplastic\b|\bclay\b|\bdrum\b|\bmold\b|"
                         r"\bmould\b|\biron box\b|\btrash can\b|\bbottles?\b|\broof sheets?\b|\bcreative ideas?\b|\bidea of\b|"
                         r"\bmulti[- ]?(purpose|functional|function)\b|\b2 in 1\b|\btwo in one\b|\b3 in 1\b|\bself-made\b|\bdiy\b|"
                         r"\bhow to (make|build)\b|\bbuild(ing)?\b|\bmaking\b|\btin can\b|\brocket stoves?\b|\bsmokeless\b|\bsmoke[- ]free\b|"
                         r"\bfirewood stoves?\b|\boutdoor\b|\bgarden\b|\bkitchen\b|\bcooking\b|#\s?\d+", re.I)
HEAT_WORDS = re.compile(r"\bheat\w*|\bwarm\w*|\bwinter\b|\bcold\b|\broom\b|\bhouse\b|\bhome heat|\bgreenhouse\b|\bgarage\b|"
                        r"\bindoor\b|\bfree energy\b|\bno gas\b|\bno electric|\bwaste oil\b|\bused oil\b", re.I)


def pre_filter(title):
    t = title or ""
    for n, rx in PRE_RX:
        if rx.search(t):
            return n
    if CRAFT_STOVE.search(t) and CRAFT_WORDS.search(t) and not HEAT_WORDS.search(t):
        return "craft / cooking stove build, no heating word in the title (reading; operator to confirm)"
    ok, why = english_check(t)
    if not ok:
        return "not English (title rule: " + why + ")"
    return None


def load_pool():
    chans = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(RAW, "census-channels-2026-10-26.csv")))}
    pool = {}
    for r in csv.DictReader(open(os.path.join(RAW, "census-videos-2026-10-26.csv"))):
        hv = r["is_hvac"] == "yes" or hvac_title(r["title"])
        if not hv:
            continue
        pool[r["video_id"]] = {"id": r["video_id"], "title": r["title"], "channel": r["channel"], "channel_id": r["channel_id"],
                               "views_approx": int(r["views_tab"] or 0), "views_basis": "census tab (rounded)",
                               "dur": int(r["dur_seconds"]) if r["dur_seconds"] else None, "dur_source": "census Videos tab overlay 2026-10-26",
                               "age_text": r["age_text"], "approx_date": r["approx_date"], "src": ["census"],
                               "census_is_hvac": r["is_hvac"]}
    for r in csv.DictReader(open(os.path.join(RAW, "sweep-videos-2026-10-24.csv"))):
        if not r["length_s"] or int(r["length_s"]) < 300:
            continue
        if r["id"] in pool:
            p = pool[r["id"]]
            p["src"].append("sweep")
            p["views_approx"] = int(r["views"])  # exact on 2026-10-24, better than the rounded tab figure
            p["views_basis"] = "sweep search page 2026-10-24 (exact then)"
            continue
        if not hvac_title(r["title"]):
            continue
        pool[r["id"]] = {"id": r["id"], "title": r["title"], "channel": r["channel"], "channel_id": r["channelId"],
                         "handle": (r["handle"] or "").lstrip("/"), "views_approx": int(r["views"] or 0),
                         "views_basis": "sweep search page 2026-10-24 (exact then)", "dur": int(r["length_s"]),
                         "dur_source": "search page length 2026-10-24", "age_text": r["age_text"],
                         "approx_date": r["approx_upload_date"], "src": ["sweep"], "live_replay": r["live_replay"]}
    for p in pool.values():
        c = chans.get(p["channel_id"])
        p["in_census"] = bool(c)
        if c:
            p["tier"] = c["tier"]
            p["baseline"] = int(c["baseline"]) if c["baseline"] else None
            p["baseline_rule"] = c["baseline_rule"]
            p["baseline_n"] = int(c["baseline_n"]) if c["baseline_n"] else None
            p["handle"] = c["handle"]
            p["ctype"] = c["type"]
        p["mult_approx"] = (p["views_approx"] / p["baseline"]) if p.get("baseline") else None
        p["pre_drop"] = pre_filter(p["title"])
    return pool, chans


def stage_pool(scratch):
    pool, chans = load_pool()
    vs = list(pool.values())
    keep = [p for p in vs if not p["pre_drop"]]
    ids = set()
    # all-time: top 600 kept-by-rule candidates by approx views (rounded views can reorder near the cut)
    at = sorted(keep, key=lambda p: -p["views_approx"])[:600]
    ids |= {p["id"] for p in at}
    for days, nv, nm in ((365, 300, 300), (90, 150, 150)):
        rec = [p for p in keep if maybe_in(p["age_text"], days)]
        ids |= {p["id"] for p in sorted(rec, key=lambda p: -p["views_approx"])[:nv]}
        withm = [p for p in rec if p.get("mult_approx") and (p.get("baseline_n") or 0) >= 10]
        ids |= {p["id"] for p in sorted(withm, key=lambda p: -p["mult_approx"])[:nm]}
        # sweep-only channels: their baseline is unknown until pulled; take their 12-month videos at 50K+ views
        if days == 365:
            ids |= {p["id"] for p in rec if not p["in_census"] and p["views_approx"] >= 50000}
    os.makedirs(scratch, exist_ok=True)
    open(os.path.join(scratch, "ids.txt"), "w").write("\n".join(sorted(ids)) + "\n")
    json.dump(pool, open(os.path.join(scratch, "pool.json"), "w"))
    print("pool", len(vs), "pre-dropped", len(vs) - len(keep), Counter(p["pre_drop"] for p in vs if p["pre_drop"]).most_common())
    print("ids to pull", len(ids))



# ---------------------------------------------------------------------------------------------------------------
# Hand review (main-session helper, 2026-10-26). Every title that would enter a list was read. KEEP lists the IDs read
# and kept (including rule pre-drops reversed by hand); DROP holds the IDs read and dropped, with the reason.
# ---------------------------------------------------------------------------------------------------------------
from top_review import KEEP, DROP, LABELS, LANG_NOTES  # noqa: E402

LANG_DESC = re.compile(r"\b(in|en) (hindi|urdu|tamil|telugu|bangla|bengali|marathi|kannada|malayalam|punjabi|nepali|"
                       r"tagalog|spanish|arabic|portuguese|español|kurdish|vietnamese|indonesian|russian)\b|"
                       r"\bhindi\b|\burdu\b|\bespañol\b|\bportuguês\b|\bvideo ini\b|\bcara membuat\b|\bकैसे\b", re.I)


def nonlatin_share(s):
    import unicodedata
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for c in letters if not unicodedata.name(c, "").startswith("LATIN")) / len(letters)


def fmt_len(s):
    if s is None:
        return "not found"
    h, m, sec = s // 3600, (s % 3600) // 60, s % 60
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"


def load_types():
    import glob
    types = {}
    for fn in sorted(glob.glob(os.path.join(RAW, "census-types-*-2026-10-26.csv"))):
        for r in csv.DictReader(open(fn)):
            cid = r.get("channel_id") or r.get("channelId") or r.get("id")
            t = r.get("type") or r.get("type_reading") or r.get("channel_type")
            if cid and t:
                types[cid] = (t, os.path.basename(fn))
    return types


def md(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def build(exact_path, baselines_path=None):
    pool, chans = load_pool()
    ex = {}
    extra = {}
    if exact_path.endswith(".json"):   # rebuild from the saved raw file (data/raw/topvideos-exact-2026-10-26.json)
        saved = json.load(open(exact_path))
        ex = {v["id"]: v["exact"] for v in saved["videos"]}
        extra = saved.get("extra_baselines", {})
    else:
        for l in open(exact_path):
            if l.strip():
                j = json.loads(l)
                ex[j["id"]] = j
    if baselines_path and os.path.exists(baselines_path):
        extra = json.load(open(baselines_path))
    types = load_types()
    rows = []
    for vid, p in pool.items():
        e = ex.get(vid)
        if not e:
            continue
        r = dict(p)
        r["exact"] = e
        r["views"] = e.get("views")
        r["date"] = e.get("date")
        r["title_final"] = e.get("title_original") or e.get("title_next") or p["title"]
        cid = e.get("owner_channel_id") or p["channel_id"]
        r["channel_id"] = cid
        c = chans.get(cid)
        h_oe = (e.get("oembed_author_url") or "").rsplit("/", 1)[-1]
        h_nx = e.get("owner_handle") or ""
        r["handle"] = (h_oe if h_oe.startswith("@") else "") or (h_nx if h_nx.startswith("@") else "") or \
            ((c or {}).get("handle") or "") or (p.get("handle") if (p.get("handle") or "").startswith("@") else "") or ("channel/" + cid)
        if c and c.get("name"):
            r["channel"] = c["name"].strip()
        if c:
            r["baseline"], r["baseline_rule"], r["baseline_n"] = (int(c["baseline"]) if c["baseline"] else None), c["baseline_rule"], (int(c["baseline_n"]) if c["baseline_n"] else 0)
            r["baseline_src"] = "census-channels-2026-10-26.csv"
            r["tier"] = c["tier"]
            r["ctype"] = c["type"]
        elif cid in extra and extra[cid].get("baseline"):
            b = extra[cid]
            r["baseline"], r["baseline_rule"], r["baseline_n"] = b["baseline"], b["rule"], b["n"]
            r["baseline_src"] = "pulled for this build (yt_allsorts.py, " + b["pulled"][:10] + ")"
            r["tier"] = "not in census"
            r["ctype"] = ""
        else:
            r["baseline"], r["baseline_rule"], r["baseline_n"], r["baseline_src"] = None, "", 0, "not found"
            r["tier"] = r.get("tier") or "not in census"
            r["ctype"] = r.get("ctype") or ""
        if cid in types:
            r["ctype"] = types[cid][0] + " (" + types[cid][1] + ")"
        elif r["ctype"]:
            r["ctype"] = r["ctype"] + " (census CSV)"
        else:
            r["ctype"] = "not found"
        r["mult"] = (r["views"] / r["baseline"]) if (r["views"] is not None and r["baseline"]) else None
        # English: original title rule + description words + description script
        ok, why = english_check(r["title_final"])
        lang = None
        if not ok:
            lang = "not English (original title: " + why + ")"
        elif LANG_DESC.search(e.get("description_head") or ""):
            lang = "not English (description names another language)"
        elif nonlatin_share(e.get("description_head") or "") >= 0.3:
            lang = "not English (description mostly in a non-Latin script)"
        r["lang_drop"] = lang
        # decision
        if vid in DROP:
            r["decision"], r["reason"] = "drop", "hand: " + DROP[vid]
        elif lang and vid not in KEEP:
            r["decision"], r["reason"] = "drop", lang
        elif vid in KEEP:
            r["decision"], r["reason"] = "keep", ("hand: kept (rule pre-drop reversed: " + p["pre_drop"] + ")") if p["pre_drop"] else "hand: kept"
        elif p["pre_drop"]:
            r["decision"], r["reason"] = "drop", "rule: " + p["pre_drop"]
        else:
            r["decision"], r["reason"] = "unreviewed", ""
        if r["dur"] is not None and r["dur"] < 300:
            r["decision"], r["reason"] = "drop", "under 5:00"
        if r["views"] is None:
            r["decision"], r["reason"] = "drop", "no exact views (" + e.get("error", "") + ")"
        r["lang_note"] = LANG_NOTES.get(vid, "")
        rows.append(r)
    return rows


# ---------------------------------------------------------------------------------------------------------------
# Lists and outputs
# ---------------------------------------------------------------------------------------------------------------
MIN_N, MIN_BASE = 10, 100   # multiple lists: channel baseline n >= 10 (brief) and baseline >= 100 views (added guard)


def make_lists(rows):
    live = [r for r in rows if r["decision"] != "drop"]
    def chk(lst, name):
        bad = [r["id"] for r in lst if r["decision"] != "keep"]
        if bad:
            raise SystemExit(f"{name}: unreviewed IDs would enter the list: {bad}")
        return lst
    L = {}
    L["top100"] = chk(sorted(live, key=lambda r: -r["views"])[:100], "top100")
    for tag, d0, nv in (("90", D90, 30), ("365", D365, 50)):
        win = [r for r in live if r["date"] and r["date"] >= d0.isoformat()]
        L["v" + tag] = chk(sorted(win, key=lambda r: -r["views"])[:nv], "v" + tag)
        mm = [r for r in win if r["mult"] is not None and (r["baseline_n"] or 0) >= MIN_N and (r["baseline"] or 0) >= MIN_BASE]
        L["m" + tag] = chk(sorted(mm, key=lambda r: -r["mult"])[:nv], "m" + tag)
        L["m" + tag + "_guarded_out"] = sorted([r for r in win if r["mult"] is not None and r["decision"] == "keep" and
                                                (r["baseline_n"] or 0) >= MIN_N and (r["baseline"] or 0) < MIN_BASE],
                                               key=lambda r: -r["mult"])
        L["m" + tag + "_no_baseline"] = [r for r in win if r["decision"] == "keep" and r["mult"] is None]
    return L


def label_of(r):
    if r["id"] in LABELS:
        sn, fm, em, vi = LABELS[r["id"]]
        return sn, fm, em, vi, "hand"
    return rule_subniche(r["title_final"]), tag_format(r["title_final"], r["channel"]), "", "not labelled", "rule"


def fnum(x):
    return "not found" if x is None else f"{x:,}"


def fmult(r):
    if r["mult"] is None:
        return "not found"
    return f"{r['mult']:.1f}x"


def base_str(r):
    if not r["baseline"]:
        return "not found"
    return f"{r['baseline']:,} ({(r['baseline_rule'] or '').split(' ')[0]}, n={r['baseline_n']})"


def stage_baselines(chan_dir, out_path):
    """Baseline for channels not in the census, the census way (labels.md section 6; census_build.build_channel):
    median tab views of the channel's long-form (>= 300 s) uploads in the last 12 months (age text up to '11mo ago'),
    from the Latest list only; if fewer than 10, the median of its last 30 long-form uploads."""
    from census_build import age_of, parse_dur, within
    out = {}
    for fn in sorted(os.listdir(chan_dir)):
        if not fn.endswith(".json"):
            continue
        try:
            d = json.load(open(os.path.join(chan_dir, fn)))
        except Exception:
            continue
        cid = d.get("id") or d.get("key")
        sorts = d.get("sorts") or {}
        lat_chip, lat_init = sorts.get("Latest"), sorts.get("Latest_initialpage") or []
        latest = lat_chip if (lat_chip is not None and len(lat_chip) >= len(lat_init)) else lat_init
        lat_long = []
        for it in latest:
            dur = parse_dur(it.get("dur"))
            a = age_of(it.get("meta"))
            if dur is not None and dur >= 300 and a and it.get("views_tab") is not None:
                lat_long.append((it, a))
        l12 = [it["views_tab"] for it, a in lat_long if within(a[1], a[2], 365)]
        if len(l12) >= 10:
            base, rule, n = statistics.median(l12), "12M", len(l12)
        else:
            vs = [it["views_tab"] for it, a in lat_long][:30]
            base, rule, n = (statistics.median(vs) if vs else None), "last30", len(vs)
        out[cid] = {"channel": d.get("channel"), "subs": d.get("subs"), "baseline": int(round(base)) if base else None,
                    "rule": rule, "n": n, "pulled": d.get("pulled"), "latest_items": len(latest),
                    "source": "YouTube Videos tab (yt_allsorts.py, Latest list, tab-rounded views)"}
    json.dump(out, open(out_path, "w"), indent=1)
    print("baselines", len(out), "with baseline", sum(1 for v in out.values() if v["baseline"]))


# ---------------------------------------------------------------------------------------------------------------
# Rising / falling (census videos, HVAC-flagged, tiers A-D; rule tags; tab-rounded views; approximate dates)
# ---------------------------------------------------------------------------------------------------------------
PATTERNS = [
    ("old ways / forgotten / Amish / grandparents", r"\bamish\b|\bforgotten\b|\bold[- ](timers?|ways?|trick|school|fashioned)\b|\bgrand(ma|pa|mother|father|parents)\b|\b19[2-7]0s\b|\bdepression\b|\bpioneers?\b|\bancient\b|\bvikings?\b|\bjapanese\b|\b(\d+)-year-old trick\b"),
    ("banned / illegal / they buried it", r"\bbann?ed\b|\billegal\b|\bburied\b|\bbury\b|\bhid(e|den|ing)?\b|\bsilent\b|\bdon'?t want you\b|\bhate\b"),
    ("dollar figure in the title ($N)", r"[$£]\s?\d"),
    ("free heat / no electricity / no gas", r"\bfree (heat|heating|energy|cooling|ac)\b|\bno (electricity|electric|power|gas)\b|\bwithout (electricity|power|gas)\b"),
    ("before you ... (seasonal)", r"\bbefore you\b"),
    ("the only N brands / brand lists", r"\bonly \d+\b.*\bbrands?\b|\bbrands? (worth|to avoid)\b|\bbest and worst\b"),
    ("not cooling / not heating / won't turn on", r"\bnot (cooling|heating|working|turning on|blowing)\b|\bwon'?t (turn|start|cool|heat)\b"),
    ("how to install / DIY mini-split", r"\binstall"),
]


def rising_falling():
    chans = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(RAW, "census-channels-2026-10-26.csv")))}
    vids = []
    for r in csv.DictReader(open(os.path.join(RAW, "census-videos-2026-10-26.csv"))):
        c = chans.get(r["channel_id"])
        if not c or c["tier"] not in ("A", "B", "C", "D") or r["is_hvac"] != "yes":
            continue
        a = age(r["age_text"])
        if not a:
            continue
        r["recent"] = a[1] != "y"   # age text below '1y ago' = uploaded in the last 12 months (approx.)
        r["fmt"] = tag_format(r["title"], r["channel"])
        r["mult_f"] = float(r["multiple"]) if r["multiple"] else None
        r["views_i"] = int(r["views_tab"] or 0)
        r["ex_ok"] = r["mult_f"] is not None and int(c["baseline_n"] or 0) >= MIN_N and int(c["baseline"] or 0) >= MIN_BASE
        vids.append(r)
    out = {"n_all": len(vids), "n_recent": sum(v["recent"] for v in vids), "n_older": sum(not v["recent"] for v in vids),
           "channels": len({v["channel_id"] for v in vids})}
    def table(key):
        groups = defaultdict(list)
        for v in vids:
            groups[key(v)].append(v)
        rows = []
        for g, vs in groups.items():
            rec = [v for v in vs if v["recent"]]
            old = [v for v in vs if not v["recent"]]
            def med(xs):
                xs = [x for x in xs if x is not None]
                return statistics.median(xs) if xs else None
            share_all = len(vs) / out["n_all"]
            share_rec = len(rec) / out["n_recent"] if out["n_recent"] else 0
            share_old = len(old) / out["n_older"] if out["n_older"] else 0
            ex = sorted([v for v in rec if v["ex_ok"]], key=lambda v: -(v["mult_f"]))[:2]
            rows.append({"group": g, "n_all": len(vs), "n_rec": len(rec), "n_old": len(old), "share_all": share_all,
                         "share_rec": share_rec, "share_old": share_old,
                         "ratio": (share_rec / share_old) if share_old else None,
                         "med_mult_all": med([v["mult_f"] for v in vs]), "med_mult_rec": med([v["mult_f"] for v in rec]),
                         "med_mult_old": med([v["mult_f"] for v in old]),
                         "share2x_rec": (sum(1 for v in rec if (v["mult_f"] or 0) >= 2) / len(rec)) if rec else None,
                         "examples": [(v["title"], v["channel"], v["views_i"], v["mult_f"], v["video_id"]) for v in ex]})
        return sorted(rows, key=lambda r: -r["n_all"])
    out["subniche"] = table(lambda v: v["subniche"] or "not mapped")
    out["format"] = table(lambda v: v["fmt"])
    prow = []
    for name, p in PATTERNS:
        rx = re.compile(p, re.I)
        hit = [v for v in vids if rx.search(v["title"])]
        rec = [v for v in hit if v["recent"]]
        old = [v for v in hit if not v["recent"]]
        def med(xs):
            xs = [x for x in xs if x is not None]
            return statistics.median(xs) if xs else None
        ex = sorted([v for v in rec if v["ex_ok"]], key=lambda v: -v["mult_f"])[:2]
        prow.append({"group": name, "n_all": len(hit), "n_rec": len(rec), "n_old": len(old),
                     "share_rec": len(rec) / out["n_recent"], "share_old": len(old) / out["n_older"],
                     "share_all": len(hit) / out["n_all"],
                     "ratio": ((len(rec) / out["n_recent"]) / (len(old) / out["n_older"])) if old else None,
                     "med_mult_rec": med([v["mult_f"] for v in rec]), "med_mult_old": med([v["mult_f"] for v in old]),
                     "med_mult_all": med([v["mult_f"] for v in hit]),
                     "examples": [(v["title"], v["channel"], v["views_i"], v["mult_f"], v["video_id"]) for v in ex]})
    out["patterns"] = prow
    return out


DROP_CATS = [
    ("craft / cooking stove or cooking-gas replacement", r"craft|cooking|gas cylinders|gas burner|replac(es|ing) gas|'replacing gas'|'to replace gas'"),
    ("vehicle (car, truck, van)", r"\bcar\b|vehicle|minivan|truck|engine air"),
    ("not English", r"not english|hindi|urdu"),
    ("insulation / drafts not about heat, cooling or the bill (operator rule)", r"operator rule|caulk|weatherstrip|spray foam"),
    ("bushcraft, camping, cabin trips, primitive skills", r"bushcraft|camping|cabin|primitive|survival night|shelter"),
    ("firewood handling", r"firewood|wood ash|tarps"),
    ("electronics, power, batteries, solar", r"electronic|capacitor|\bpc\b|induction|battery|solar|electricity|alternator|power factor|free energy|'free energy'|free electricity|power vs energy|generator|wind"),
    ("industrial, trade, lab, metal furnaces", r"industrial|trade|training|lab furnace|metal|smelt|power plant|commercial|career|pump curve"),
    ("bill / energy news or policy", r"news|policy|tariff|meter|data cent|qr code"),
    ("sounds, music, sermons, fiction, games", r"sound|music|sermon|fiction|drama|gaming|ambient|football"),
]


def drop_cat(reason):
    t = (reason or "").lower()
    for name, p in DROP_CATS:
        if re.search(p, t):
            return name
    return "other off-topic (not HVAC)"


def pct(x):
    return "-" if x is None else f"{x * 100:.1f}%"


def f2(x):
    return "-" if x is None else f"{x:.2f}"


def write_outputs(rows, pool_stats, exact_path, baselines_path):
    L = make_lists(rows)
    if baselines_path and os.path.exists(baselines_path):
        extra = json.load(open(baselines_path))
    elif exact_path.endswith(".json"):
        extra = json.load(open(exact_path)).get("extra_baselines", {})
    else:
        extra = {}
    pulled = sorted({r["exact"]["pulled"][:10] for r in rows})
    # ---------------- CSV (top 100)
    cols = ["rank", "title", "channel", "handle", "channel_id", "views", "views_pulled_utc", "upload_date", "length_s",
            "length", "length_source", "subniche_reading", "format_reading", "emotions_reading", "villain_reading",
            "thumbnail", "video_id", "url", "channel_type", "multiple", "baseline", "baseline_rule", "baseline_n",
            "baseline_source", "census_tier", "pool_source", "language_note"]
    with open(os.path.join(STUDY, "top-100.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for i, r in enumerate(L["top100"], 1):
            sn, fm, em, vi, _ = label_of(r)
            w.writerow([i, r["title_final"], r["channel"], r["handle"], r["channel_id"], r["views"], r["exact"]["pulled"],
                        r["date"], r["dur"], fmt_len(r["dur"]), r["dur_source"], sn, fm, em, vi,
                        f"https://i.ytimg.com/vi/{r['id']}/hqdefault.jpg", r["id"], f"https://www.youtube.com/watch?v={r['id']}",
                        r["ctype"], "" if r["mult"] is None else round(r["mult"], 2), r["baseline"] or "",
                        r["baseline_rule"], r["baseline_n"], r["baseline_src"], r["tier"], "+".join(r["src"]), r["lang_note"]])
    # ---------------- drop logs
    cut100 = L["top100"][-1]["views"]
    drops_top = sorted([r for r in rows if r["decision"] == "drop" and r["views"] is not None and r["views"] >= cut100],
                       key=lambda r: -r["views"])
    reasons = Counter(drop_cat(x["reason"]) for x in drops_top)
    # pre-dropped (not pulled) with approx views above the cut
    pre_above = sorted([p for p in pool_stats["pool"].values() if p["pre_drop"] and p["views_approx"] >= cut100],
                       key=lambda p: -p["views_approx"])
    craft = [p for p in pre_above if p["pre_drop"].startswith("craft")]
    # ---------------- top-100.md
    T = []
    T.append("# HVAC study: the top 100 long-form HVAC videos of all time (deliverable 7)\n")
    T.append(f"Built 2026-10-26 by `data/tools/top_build.py` (round 3 helper). Exact views and upload dates pulled from YouTube's innertube `/next` endpoint (logged out) on {', '.join(pulled)} (UTC); every row carries its pull time in `top-100.csv` and `data/raw/topvideos-exact-2026-10-26.json`. Lengths are the Videos-tab overlay (census, 2026-10-26) or the search-page length (sweep, 2026-10-24), both to the second. **Not checked yet by a second helper** (round 6).\n")
    T.append("**What is measured and what is a reading.** Views, upload dates, lengths, baselines and multiples are measured (multiples use the census baseline, which is a median of tab-rounded views). Sub-niche, format, emotions, villain and the in-scope / English decisions are **readings** by the labels.md rules (title first; description only to confirm language). Channel type comes from the round 3 type helper's `data/raw/census-types-*-2026-10-26.csv` where the channel is there, else the census CSV's carried type, else `not found` (the source is named in each cell).\n")
    T.append("## How the list was built\n")
    ps = pool_stats
    T.append(f"1. **Pool.** (a) `data/raw/census-videos-2026-10-26.csv`: every long-form (5:00+) video the census pulled from the 1,122 channels of the round 2 master list's tiers A-D (Latest, Popular, Oldest sorts; up to about 120 each). Census channels re-tiered X keep their videos in the pool, so big HVAC videos on off-niche channels count. (b) `data/raw/sweep-videos-2026-10-24.csv`: keyword-sweep videos from any channel. Kept: titles that are HVAC by the census rule (`census_build.hvac_title`) or carry the census `is_hvac` mark. Pool: {ps['n_pool']:,} videos ({ps['n_census']:,} from the census, {ps['n_sweep_only']:,} sweep-only).")
    T.append(f"2. **Rule pre-filter** (logged): {ps['n_pre']:,} titles dropped as kids' challenges, games, vehicles, commercial / industrial / trade training, bushcraft and camping, electronics, non-English titles, and DIY craft stove builds with no heating word. Counts: " + "; ".join(f"{k} {v:,}" for k, v in ps['pre_counts']) + ".")
    T.append(f"3. **Exact pulls**: {ps['n_exact']:,} candidates (the top 600 by approximate views, plus the recent-list candidates) pulled from `/next` (views, date, owner) and oEmbed (original title; logged-out pages auto-translate).")
    T.append(f"4. **Hand review**: every title that would enter a list was read: {ps['n_keep']} kept and {ps['n_drop_hand']} dropped by hand across all lists (reasons in `data/tools/top_review.py`). English: the original title by the round 2 rule, plus the description head (another language named, or mostly non-Latin script). Where an English-titled video's audio could not be confirmed, NexLev transcripts were checked for 6 videos (1 Hindi, dropped; 1 English; 1 music only; 3 not available); rows with unconfirmed audio carry a language note in the CSV.")
    T.append("5. **Scope readings used** (main ones, to confirm with the operator): DIY cement / brick / barrel stove builds whose title doesn't mention heating are read as craft or cooking stoves and left out (see the side table below: they would otherwise take most of the top 30); waste-oil 'stoves' that replace cooking gas are out, waste-oil *heaters* are in; bushcraft and camping shelters are out; car AC is out; firewood splitting and stacking are out; insulation, spray foam and weatherstripping are in only when the title is about heating, cooling or the bill (operator rule); utility-bill news stories are out, homeowner bill-cutting videos are in; DIY and passive cooling (homemade coolers, earth tubes) are in, mapped as `not mapped: DIY / passive cooling (proposed sub-niche, not in labels.md)` because labels.md has no cooling equivalent of off-grid heat.")
    T.append("6. **Multiple** = exact views / the channel's baseline (labels.md section 6: median tab views of its long-form uploads in the last 12 months, or of its last 30 if fewer than 10). Census channels: baseline from `census-channels-2026-10-26.csv`. Channels not in the census: pulled for this build with `yt_allsorts.py` (Latest, Popular, Oldest; 4 pages) on 2026-10-26 and computed the same way (" + f"{len(extra)} channels" + "). An old video's multiple is inflated by age; compare multiples with the upload year in view.\n")
    T.append(f"The 100th video has {cut100:,} views.\n")
    T.append("## The top 100\n")
    T.append("Labels are readings. E-codes as labels.md (E1 big bill, E2 service-call resentment, E3 store-shelf distrust, E4 hidden damage, E5 emergency, E6 failed attempts, E8 payoff, E10 insider curiosity, E11 being let in, E12 myth-bust, E13 self-reliance, E14 relief, E15 nostalgia, E16 protectiveness, E17 safety fear, E18 rule-curiosity, E19 comfort, E20 new-gadget wonder).\n")
    T.append("| # | Title | Channel | Views | Uploaded | Length | Sub-niche (reading) | Format (reading) | Emotions (reading) | Villain (reading) | Multiple | Type | Thumbnail |")
    T.append("|---:|---|---|---:|---|---:|---|---|---|---|---:|---|---|")
    for i, r in enumerate(L["top100"], 1):
        sn, fm, em, vi, _ = label_of(r)
        ch = f"{md(r['channel'])} ({r['handle'] or 'not found'})"
        T.append(f"| {i} | \"{md(r['title_final'])}\" (`{r['id']}`) | {ch} | {r['views']:,} | {r['date']} | {fmt_len(r['dur'])} | {sn} | {fm} | {em} | {vi} | {fmult(r)} | {md(r['ctype'])} | [img](https://i.ytimg.com/vi/{r['id']}/hqdefault.jpg) |")
    # summaries
    T.append("\n## What the top 100 is made of (counts of the readings above)\n")
    for name, idx in (("Sub-niche", 0), ("Format", 1), ("Villain", 3)):
        c = Counter(label_of(r)[idx] for r in L["top100"])
        T.append(f"- **{name}:** " + "; ".join(f"{k} {v}" for k, v in c.most_common()))
    ce = Counter(e.strip() for r in L["top100"] for e in label_of(r)[2].split(",") if e.strip())
    T.append("- **Emotions (any of the up to 3):** " + "; ".join(f"{k} {v}" for k, v in ce.most_common()))
    yrs = Counter((r["date"] or "????")[:4] for r in L["top100"])
    T.append("- **Upload year:** " + "; ".join(f"{k} {v}" for k, v in sorted(yrs.items())))
    chc = Counter(r["channel"] for r in L["top100"])
    T.append("- **Channels with 3+ videos in the list:** " + "; ".join(f"{k} {v}" for k, v in chc.most_common() if v >= 3))
    srcs = Counter("+".join(r["src"]) for r in L["top100"])
    T.append("- **Pool source:** " + "; ".join(f"{k} {v}" for k, v in srcs.most_common()) + ". Census tier of the channel: " + "; ".join(f"{k} {v}" for k, v in Counter(r['tier'] for r in L['top100']).most_common()) + ".")
    T.append("\n## Dropped candidates above the cut\n")
    T.append(f"{len(drops_top)} pulled candidates with at least {cut100:,} exact views were dropped (hand or rule), plus {len(pre_above)} rule pre-drops (not pulled) whose approximate views were above the cut (" + "; ".join(f"{k} {v}" for k, v in Counter(re.sub(r" \(.*", "", p["pre_drop"]) for p in pre_above).most_common()) + f"). Reasons for the {len(drops_top)}: " + "; ".join(f"{k} {v}" for k, v in reasons.most_common()) + ".\n")
    T.append("| Views (exact) | Title | Channel | Reason |")
    T.append("|---:|---|---|---|")
    for r in drops_top:
        T.append(f"| {r['views']:,} | \"{md(r['title_final'])}\" (`{r['id']}`) | {md(r['channel'])} | {md(r['reason'])} |")
    T.append("\n### Side table: the biggest craft / cooking stove builds left out (approximate views, not pulled)\n")
    T.append("These are DIY cement, brick, barrel and plastic-mould stove builds, mostly from Vietnamese channels with English titles and no narration. Their titles don't mention heating a home, so they are read as craft or cooking stoves and left out. If the operator counts them as off-grid heat, the top 30 would be mostly these. Views are the census tab's rounded figure or the sweep's 2026-10-24 figure.\n")
    T.append("| Approx. views | Title | Channel |")
    T.append("|---:|---|---|")
    for p in craft[:25]:
        T.append(f"| {p['views_approx']:,} | \"{md(p['title'])}\" (`{p['id']}`) | {md(p['channel'])} |")
    T.append("\n## Problems and limits\n")
    nf = sum(1 for r in L["top100"] if r["ctype"] == "not found")
    T.append(f"- Channel type is `not found` for {nf} of the 100 (channels outside the census, or not yet typed by the round 3 type helper).")
    T.append("- The pool only holds what the census (up to about 120 videos per sort per channel) and the keyword sweep returned; a big HVAC video on a channel neither touched could be missing.")
    T.append("- English is judged on the original title and the description head; audio was checked by transcript for only a few videos. South Asian and Vietnamese channels with English titles and no narration are kept.")
    T.append("- Scope calls (craft stoves, firewood, bushcraft, bill news, DIY coolers) are readings; the side table and drop log let the operator reverse them.")
    open(os.path.join(STUDY, "top-100.md"), "w").write("\n".join(T) + "\n")
    # ---------------- recent-winners.md
    R = []
    R.append("# HVAC study: what has worked recently (deliverable 6)\n")
    R.append(f"Built 2026-10-26 by `data/tools/top_build.py`. Same pool, rule pre-filter, exact pulls and hand review as `top-100.md`. Windows by the **exact** upload date from `/next`: last 90 days = uploaded {D90.isoformat()} to 2026-10-26; last 12 months = {D365.isoformat()} to 2026-10-26. Views exact, pulled {', '.join(pulled)} (UTC). **Not checked yet by a second helper.**\n")
    R.append(f"**Multiple lists rule:** exact views / the channel's baseline (labels.md section 6), only channels whose baseline set has **n >= {MIN_N}** videos (brief) **and a baseline of at least {MIN_BASE} views** (added guard: below that, one video's views swing the multiple into the thousands). Census channels use the census baseline; {len(extra)} channels outside the census were pulled for this build and computed the same way. Channels outside both (no baseline) can't enter the multiple lists. Sub-niche, format, emotions and villain are readings.\n")
    def table(lst, title, by):
        R.append(f"## {title}\n")
        R.append("| # | Title | Channel | Views | Uploaded | Length | Multiple | Baseline (rule, n) | Sub-niche (reading) | Format (reading) | Emotions (reading) | Villain (reading) | Thumbnail |")
        R.append("|---:|---|---|---:|---|---:|---:|---|---|---|---|---|---|")
        for i, r in enumerate(lst, 1):
            sn, fm, em, vi, _ = label_of(r)
            R.append(f"| {i} | \"{md(r['title_final'])}\" (`{r['id']}`) | {md(r['channel'])} ({r['handle'] or 'not found'}) | {r['views']:,} | {r['date']} | {fmt_len(r['dur'])} | {fmult(r)} | {base_str(r)} | {sn} | {fm} | {em} | {vi} | [img](https://i.ytimg.com/vi/{r['id']}/hqdefault.jpg) |")
        c1 = Counter(label_of(r)[0] for r in lst); c2 = Counter(label_of(r)[1] for r in lst)
        R.append("\nSub-niches: " + "; ".join(f"{k} {v}" for k, v in c1.most_common()) + ".  \nFormats: " + "; ".join(f"{k} {v}" for k, v in c2.most_common()) + ".\n")
    table(L["v90"], "Last 90 days: top 30 by views", "views")
    table(L["m90"], f"Last 90 days: top 30 by multiple (n >= {MIN_N}, baseline >= {MIN_BASE})", "mult")
    table(L["v365"], "Last 12 months: top 50 by views", "views")
    table(L["m365"], f"Last 12 months: top 50 by multiple (n >= {MIN_N}, baseline >= {MIN_BASE})", "mult")
    g = [r for r in L["m365_guarded_out"]][:10]
    R.append(f"**Left out of the 12-month multiple list by the {MIN_BASE}-view baseline guard** ({len(L['m365_guarded_out'])} kept videos; the biggest): " + "; ".join(f"\"{md(r['title_final'])}\" ({md(r['channel'])}, {r['views']:,} views, baseline {r['baseline']}, {fmult(r)})" for r in g) + ".\n")
    nb = sorted(L["m365_no_baseline"], key=lambda r: -r["views"])[:10]
    if nb:
        R.append(f"**No baseline found** ({len(L['m365_no_baseline'])} kept 12-month videos, mostly sweep channels under 50K-view videos that were not pulled): biggest " + "; ".join(f"\"{md(r['title_final'])}\" ({md(r['channel'])}, {r['views']:,})" for r in nb) + ".\n")
    # rising / falling
    rf = rising_falling()
    R.append("## Rising and falling: last 12 months against all-time\n")
    R.append(f"From the census videos only: HVAC-flagged long-form videos of tier A-D channels ({rf['n_all']:,} videos from {rf['channels']} channels; {rf['n_recent']:,} uploaded in the last 12 months by age text, {rf['n_older']:,} older). Sub-niche and format are **rule tags** (census `SUBNICHE_RULES`, sweep `tag_format`; about 3 in 4 right on hand-checks), views are tab-rounded and dates approximate, so this is rough. 'Ratio' = share in the last 12 months / share in older videos. Multiples are against each channel's baseline. Examples are the two highest multiples among recent videos of channels with baseline n >= {MIN_N} and baseline >= {MIN_BASE} views; they are rule-tagged, not hand-reviewed, so a few are off-scope.\n")
    R.append("**Caution (reading):** older videos reach the census mostly through each channel's Popular and Oldest sorts (up to 120 each), so the older set leans to hits and its median multiple is inflated by that and by age. Many channels are new (2025-2026 faceless personas), so their style lifts the recent shares. Shares are the safer comparison; multiples only compare within a column.\n")
    def rftable(rows_, title, minn=30):
        R.append(f"### {title}\n")
        R.append("| Group (rule tag) | All-time n | Share all-time | Last 12 months n | Share 12 m | Share older | Ratio | Median multiple older | Median multiple 12 m | Best 12-month examples (by multiple) |")
        R.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
        for x in rows_:
            ex = "; ".join(f"\"{md(t[0])}\" ({md(t[1])}, {t[2]:,}, {t[3]:.1f}x)" for t in x["examples"])
            R.append(f"| {x['group']} | {x['n_all']:,} | {pct(x['share_all'])} | {x['n_rec']:,} | {pct(x['share_rec'])} | {pct(x['share_old'])} | {f2(x['ratio'])} | {f2(x['med_mult_old'])} | {f2(x['med_mult_rec'])} | {ex} |")
        R.append("")
    rftable(rf["subniche"], "Sub-niches")
    rftable(rf["format"], "Formats")
    rftable(rf["patterns"], "Title patterns (rule word lists, overlapping)")
    def named(rows_, minn=40):
        up = [x for x in rows_ if x["ratio"] and x["ratio"] >= 1.25 and x["n_rec"] >= minn]
        dn = [x for x in rows_ if x["ratio"] and x["ratio"] <= 0.8 and x["n_old"] >= minn]
        return sorted(up, key=lambda x: -x["ratio"]), sorted(dn, key=lambda x: x["ratio"])
    R.append("### Named (rule: ratio 1.25+ with 40+ recent videos = rising; 0.8 or less with 40+ older videos = falling)\n")
    for lab, key in (("Sub-niches", "subniche"), ("Formats", "format"), ("Title patterns", "patterns")):
        up, dn = named(rf[key])
        R.append(f"- **{lab} rising:** " + ("; ".join(f"{x['group']} ({pct(x['share_old'])} -> {pct(x['share_rec'])}, {x['n_rec']:,} recent videos)" for x in up) or "none by the rule"))
        R.append(f"- **{lab} falling:** " + ("; ".join(f"{x['group']} ({pct(x['share_old'])} -> {pct(x['share_rec'])}, {x['n_old']:,} older videos)" for x in dn) or "none by the rule"))
    R.append("")
    R.append("## Dropped candidates (recent lists)\n")
    cut = {k: (L[k][-1]["views"] if k[0] == "v" else L[k][-1]["mult"]) for k in ("v90", "m90", "v365", "m365")}
    win365 = [r for r in rows if r["date"] and r["date"] >= D365.isoformat() and r["decision"] == "drop"]
    above = [r for r in win365 if r["views"] >= cut["v365"] or (r["mult"] and r["mult"] >= cut["m365"] and (r["baseline_n"] or 0) >= MIN_N and (r["baseline"] or 0) >= MIN_BASE)]
    R.append(f"{len(above)} pulled 12-month candidates that would have entered a 12-month list (views >= {cut['v365']:,} or multiple >= {cut['m365']:.1f}x) were dropped. Reasons: " + "; ".join(f"{k} {v}" for k, v in Counter(drop_cat(r['reason']) for r in above).most_common()) + ".\n")
    R.append("| Views | Multiple | Uploaded | Title | Channel | Reason |")
    R.append("|---:|---:|---|---|---|---|")
    for r in sorted(above, key=lambda r: -r["views"]):
        R.append(f"| {r['views']:,} | {fmult(r)} | {r['date']} | \"{md(r['title_final'])}\" (`{r['id']}`) | {md(r['channel'])} | {md(r['reason'])} |")
    open(os.path.join(STUDY, "recent-winners.md"), "w").write("\n".join(R) + "\n")
    # ---------------- raw JSON
    listed = {k: [r["id"] for r in v] for k, v in L.items() if k in ("top100", "v90", "m90", "v365", "m365")}
    raw = {"built": "2026-10-26", "tool": "data/tools/top_build.py (+ top_pull.py, top_review.py)",
           "source": "innertube /next (logged out, hl=en gl=US) + YouTube oEmbed; lengths from census tab / sweep search page",
           "pool_stats": {k: v for k, v in pool_stats.items() if k != "pool"},
           "multiple_rule": {"min_n": MIN_N, "min_baseline": MIN_BASE},
           "windows": {"90d_from": D90.isoformat(), "365d_from": D365.isoformat(), "to": TODAY.isoformat()},
           "lists": listed,
           "extra_baselines": extra,
           "videos": [{"id": r["id"], "exact": r["exact"], "decision": r["decision"], "reason": r["reason"],
                       "channel_id": r["channel_id"], "dur_s": r["dur"], "dur_source": r["dur_source"],
                       "baseline": r["baseline"], "baseline_rule": r["baseline_rule"], "baseline_n": r["baseline_n"],
                       "baseline_source": r["baseline_src"], "multiple": r["mult"], "pool_source": r["src"],
                       "labels": dict(zip(("subniche", "format", "emotions", "villain", "by"), label_of(r))) if r["decision"] == "keep" else None,
                       "language_note": r["lang_note"]} for r in rows],
           "rising_falling": rf}
    json.dump(raw, open(os.path.join(RAW, "topvideos-exact-2026-10-26.json"), "w"), ensure_ascii=False, indent=0)
    print("top100 cut", cut100, "drops above", len(drops_top), "lists", {k: len(v) for k, v in listed.items()})
    return L


def pool_stats_of(pool, rows):
    return {"pool": pool, "n_pool": len(pool), "n_census": sum(1 for p in pool.values() if "census" in p["src"]),
            "n_sweep_only": sum(1 for p in pool.values() if p["src"] == ["sweep"]),
            "n_pre": sum(1 for p in pool.values() if p["pre_drop"]),
            "pre_counts": Counter(re.sub(r" \(.*", "", p["pre_drop"]) for p in pool.values() if p["pre_drop"]).most_common(),
            "n_exact": len(rows), "n_keep": sum(1 for r in rows if r["decision"] == "keep"),
            "n_drop_hand": sum(1 for r in rows if r["reason"].startswith("hand: ") and r["decision"] == "drop"),
            "n_unreviewed": sum(1 for r in rows if r["decision"] == "unreviewed")}


if __name__ == "__main__":
    if sys.argv[1] == "pool":
        stage_pool(sys.argv[2])
    elif sys.argv[1] == "baselines":
        stage_baselines(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "build":
        rows = build(*sys.argv[2:4])
        pool, _ = load_pool()
        write_outputs(rows, pool_stats_of(pool, rows), sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
