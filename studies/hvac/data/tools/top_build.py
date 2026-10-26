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
from top_review import KEEP, DROP, LABELS  # noqa: E402

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
    for l in open(exact_path):
        if l.strip():
            j = json.loads(l)
            ex[j["id"]] = j
    extra = json.load(open(baselines_path)) if baselines_path and os.path.exists(baselines_path) else {}
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
        r["handle"] = e.get("owner_handle") or p.get("handle") or ""
        cid = e.get("owner_channel_id") or p["channel_id"]
        r["channel_id"] = cid
        c = chans.get(cid)
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
        rows.append(r)
    return rows


if __name__ == "__main__":
    if sys.argv[1] == "pool":
        stage_pool(sys.argv[2])
    elif sys.argv[1] == "build":
        build(*sys.argv[2:])
