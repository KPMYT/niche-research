#!/usr/bin/env python3
"""Round 2 keyword sweep: build (2026-10-24). Rerunnable.

Reads the logged-out YouTube search sweep made by sweep_round2.py
(raw/sweep-2026-10-24/priority.jsonl and extended-*.jsonl), the keyword list (raw/keywords-round2.csv)
and the round 1 channel files (seeds/channel-finds-round1.md, leads-channels.md, known-channels-recheck.md).

Writes:
  raw/sweep-videos-2026-10-24.csv     unique long-form English videos (one row each)
  raw/sweep-keywords-2026-10-24.csv   one row per (keyword, sort) search: counts, median, top video, sort checks
  raw/sweep-channels-2026-10-24.csv   channel tally (every channel), NEW flag
  raw/sweep-build-2026-10-24.json     the counts used in the write-ups
  round2/keyword-sweep.md, round2/formats.md

Format tags are rule-based (FORMAT_RULES below, in the order of labels.md section 3: first match wins).
The hand-check of 100 random titles (seed 24) is read from raw/format-handcheck-2026-10-24.csv when it exists
(columns: id, title, rule_tag_v1, hand_tag, note); hand_tag is a reading by the helper.

Usage: python3 -I sweep_build.py            (run from anywhere; paths are relative to this file)
       python3 -I sweep_build.py sample N SEED   (print N random tagged titles for a hand-check)
"""
import csv, json, os, re, sys, glob, random, statistics, unicodedata, urllib.parse, datetime, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from autocomplete import is_hvac  # the round 1 keyword filter (STRONG / WEAK / CONTEXT / EXCLUDE), reused on titles

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.dirname(HERE)
STUDY = os.path.dirname(DATA)
RAW = os.path.join(DATA, "raw")
SWEEP = os.path.join(RAW, "sweep-2026-10-24")
SEEDS = os.path.join(STUDY, "seeds")
OUTMD = os.path.join(STUDY, "round2")
TODAY = datetime.date(2026, 10, 24)
LONG_MIN = 300
MIN_SEARCH_N = 5  # a search needs at least this many kept long-form results to be used for "above search median"

# ---------------------------------------------------------------- parsing

def parse_views(t):
    if not t: return None
    if t.strip().lower().startswith("no views"): return 0
    m = re.match(r"([\d,]+)\s+views?", t.strip())
    return int(m.group(1).replace(",", "")) if m else None

def parse_len(t):
    if not t: return None
    p = [int(x) for x in t.split(":")]
    s = 0
    for x in p: s = s * 60 + x
    return s

AGE_RE = re.compile(r"^(Streamed )?(\d+)\s*(min|h|d|w|mo|y) ago$")
UNIT_DAYS = {"min": 1 / 1440, "h": 1 / 24, "d": 1, "w": 7, "mo": 30.44, "y": 365.25}

def parse_age(t):
    """Returns (number, unit, streamed) or None."""
    if not t: return None
    m = AGE_RE.match(t.replace("\xa0", " ").strip())
    if not m: return None
    return int(m.group(2)), m.group(3), bool(m.group(1))

def approx_date(age, pulled):
    a = parse_age(age)
    if not a: return ""
    d = datetime.datetime.strptime(pulled[:10], "%Y-%m-%d").date()
    return (d - datetime.timedelta(days=a[0] * UNIT_DAYS[a[1]])).isoformat()

def within_12m(age):
    a = parse_age(age)  # YouTube shows 1-11mo, then 1y: so 12 months = any unit below "y"
    return bool(a) and a[1] != "y"

def within_5w(age):
    a = parse_age(age)  # min/h/d (up to 13d)/w (2w-4w); "1mo ago" (30+ days) is out
    return bool(a) and a[1] in ("min", "h", "d", "w")

# ---------------------------------------------------------------- English rule

FOREIGN = set("""para como cómo que qué del los las una por acondicionado calefaccion calefacción instalación
instalacion condicionado não nao você voce fazer limpeza comment pour avec chauffage climatisation und mit wie für heizung
klimaanlage kaise kare karen karein hai kya nahi aur kaun sasta kitna bijli garmi thanda lagaye lagwaye wala wali kare
cara yang untuk bukan oleh pihak disebut dengan tidak sudah bisa juga mga ang paano naman ito kung ng bakit ganito panas dingin pemasangan cuci
el también muy esto este esta cuando porque sin sobre mejor tu tus nuestro hacer cómo limpiar
ou est les une des sur dans très pas
und ist nicht auch eine einen
ar-condicionado
ka ki ke se ko hain sasti sasta bhare khud banao karna kaisa ghar paise lagana chahiye kitne karo wale sab bhai ooltah chashmah hota kyun""".split())
STRONG_FOREIGN_LETTERS = set("ṭḍṇṣṛḥışğőűřčěůžłąęśźżạảấầẩậắằẳặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđơư")
ENGLISH = set("""the to a an and of how your my is for in on with this you it do what why not best are can does will
i we our that these those from or at by be don't won't never before after when vs""".split())

def english_check(title):
    """Returns (is_english, reason). Rule-based: drops titles mostly in a non-Latin script, and Latin-script
    titles whose function words are clearly another language."""
    letters = [c for c in title if c.isalpha()]
    if letters:
        nonlatin = sum(1 for c in letters if not unicodedata.name(c, "").startswith("LATIN"))
        if nonlatin / len(letters) >= 0.3:
            return False, "non-Latin script"
    if re.search(r"\bin (hindi|urdu|tamil|telugu|bangla|bengali|marathi|kannada|malayalam|punjabi|nepali|tagalog|spanish|arabic|portuguese)\b|\ben español\b", title.lower()):
        return False, "title says the video is in another language"
    words = re.findall(r"[a-zà-ÿ'\-]+", title.lower().replace("los angeles", ""))
    f = sum(1 for w in words if w in FOREIGN)
    e = sum(1 for w in words if w in ENGLISH)
    if f >= 2 and f > e:
        return False, "foreign function words"
    if f >= 1 and e == 0:
        return False, "foreign function word, no English ones"
    if any(c in STRONG_FOREIGN_LETTERS for c in title.lower()) and e < 2:
        return False, "letters used only in other languages (Turkish, Polish, Czech, Vietnamese...)"
    return True, ""

# ---------------------------------------------------------------- format rules (labels.md section 3 order)

def R(p): return re.compile(p, re.I)

FORMAT_RULES = [
    ("test", [R(r"\b(i|we) test(ed)?\b"), R(r"^(?!.*\b(best|top \d+)\b).*\btested\b"), R(r"\bhow (warm|cold|hot|long|far|cool) can (i|we)\b"), R(r"^(?!.*\bhow to\b).*\btesting (\d+|the|these|every|all|cheap|popular|viral|amazon|my|a|an|out)\b(?! (capacitor|thermostat|contactor|relay|fuse|motor|igniter|ignitor|flame sensor|transformer|breaker|limit switch|pressure switch|voltage|for)\b)"),
              R(r"\b(put|putting) .* to the test\b"), R(r"\bhow safe (is|are)\b"), R(r"\bsurviv(e|ing|ed)\b.*\b\d+\s*(hours?|hrs?|days?|nights?)\b"),
              R(r"\bexperiments?\b"), R(r"\b(does|do|will|can) (it|this|they|these) (really |actually )?work\b"), R(r"\b(real[- ]world|side[- ]by[- ]side|torture|stress) test\b"),
              R(r"\btest\s*:|\btest results?\b"), R(r"\bwhich (one )?(is|works|lasts|cools|heats) (best|better|longer|the most)\b")]),
    ("X vs Y", [R(r"\bvs\.?\b"), R(r"\bversus\b"), R(r"\b(better|worse|cheaper|safer) than\b"), R(r"\bcompar(ed|ison|ing)\b"),
                R(r"\b(?!this\b|that\b|it\b)\w+ instead of (a |an |the )?(?!this\b|that\b)\w+")]),
    ("the only X", [R(r"\bonly\b.*\b(buy|brands?|worth|i'?d|recommend|install|use|own)\b"), R(r"\bbest\b(?! (way|ways|time|times|practice|practices|setting|settings|temp|temperature|tips?|thing|of both)\b)"),
                    R(r"\bworst\b"), R(r"\b(brands?|models?) to (avoid|buy)\b"), R(r"\bnever buy\b"), R(r"\b(avoid|stay away from) (these|this|the) .*\b(brands?|models?|units?)\b"),
                    R(r"\bwhich (brand|model|one|unit|filter|thermostat|heater)\b.*\b(buy|best|choose|get)\b"), R(r"\btop \d+\b.*\b(brands?|units?|heaters?|air conditioners?|acs?|filters?|thermostats?|heat pumps?|furnaces?|mini splits?|dehumidifiers?|humidifiers?|purifiers?|fans?)\b"),
                    R(r"\bmost reliable\b"), R(r"\bonly (one|1)\b"), R(r"\bmust[- ]haves?\b"), R(r"\b(don'?t|do not) buy\b(?!.*\b(before|until)\b)")]),
    ("review", [R(r"^(?!.*\binstall).*\breview(ed|s)?\b"), R(r"^(?!.*\binstall).*\bfirst look\b"), R(r"\bis (it|this|the \w+) worth (it|buying|the money)\b"), R(r"\bworth it\??"),
                R(r"\bunbox(ing|ed)?\b"), R(r"\bhonest (opinion|thoughts|review)\b"), R(r"\b(long[- ]term|\d+ (month|year)s?) (later|update|review)\b"), R(r"\bhands[- ]on\b")]),
    ("myth-bust", [R(r"\bmyth"), R(r"\b(doesn'?t|don'?t|does not|do not|won'?t) (really |actually )?(work|save|help)\b"), R(r"\bstop (doing|using|closing|putting|running|turning|setting|believing|covering|blocking|spraying|cleaning|changing)\b"),
                   R(r"\b(they|you) (were|was|are) wrong\b"), R(r"\byou'?ve been (told|lied|doing it)\b"), R(r"\bwaste of money\b"), R(r"\bdebunk"), R(r"\bdon'?t fall for\b"),
                   R(r"\bis (a )?(lie|myth|hoax)\b"), R(r"\b(is|are) ?(not|n'?t) (really |actually )?(saving|working|helping)\b"), R(r"\b(not|isn'?t) (what|as) you think\b")]),
    ("Y doesn't want you to know", [R(r"\bsecrets?\b"), R(r"\b(don'?t|doesn'?t|won'?t|never) (want you to know|tell you|talk about|mention)\b"), R(r"\bhidden\b"), R(r"\bunknown\b"),
                   R(r"\b(nobody|no one|no-one) (tells|knows|talks|told)\b"), R(r"\btruth\b"), R(r"\blies\b"), R(r"\bscams?\b|\bscammed\b"), R(r"\b(hates?|hate it when)\b"),
                   R(r"\bforgot to tell\b"), R(r"\b(known by|only \d+%)\b"), R(r"\binsider\b"), R(r"\bexpos(ed|ing|e)\b"), R(r"\brip(ped|ping)?[- ]?off\b"),
                   R(r"\bwhat (they|techs?|contractors?|companies|dealers?|installers?|the \w+) (won'?t|don'?t|never)\b"), R(r"\b(doesn'?t|don'?t) (everyone|anyone|people|most people) know\b|\bforgotten\b"), R(r"\bdecept|\bdeceiv|\bmislead|\bmisled\b|\boverlooked\b"), R(r"\b(nobody|no one)\b"), R(r"\b(do not|don'?t) (even )?(know|notice|realize)\b"), R(r"\b(industry|they|companies|contractors|utilities) (is |are |stay |stays |kept |keep )?(silent|quiet)\b"), R(r"\bdidn'?t know\b"), R(r"\bsneaky\b"), R(r"\bthey don'?t\b")]),
    ("mistakes", [R(r"\bmistakes?\b"), R(r"\bdoing it wrong\b"), R(r"\bwrong (way|thing|size)\b"), R(r"\bnever (do|put|use|run|turn|set|close|leave|cover|let|spray|clean|block|ignore)\b"),
                  R(r"\b(don'?t|do not) (ever )?(do|make|put|use|run|turn|set|close|leave|cover|spray|block|ignore|let)\b"), R(r"\bstop wasting\b"), R(r"\byou'?re (doing|using|setting|running|changing|wasting)\b"),
                  R(r"\b(killing|ruining|destroying|damaging) (your|the)\b"), R(r"\b(bad|common) habits?\b"), R(r"\b(reasons|ways|how) to avoid\b|\bavoid (these|this|common|costly)\b"), R(r"\bhabits?\b.*\b(wear|kill|ruin|cost|destroy|damag|shorten|waste)"), R(r"\bwear(s|ing)? out\b|\bshorten(s|ing)? (the |its |your )?life\b|\byears early\b"), R(r"\bavoid (these|this)\b")]),
    ("before you do X", [R(r"\bbefore (you|replacing|buying|calling|installing|hiring|signing|paying|turning|starting|running|using|switching|getting|trying|throwing|selling|scrapping|tossing)\b"),
                         R(r"\bwatch (this )?(video )?(first|before)\b"), R(r"\b(don'?t|do not) (buy|replace|call|pay|hire|sign|get|install)\b")]),
    ("news-warning", [R(r"\bnews\b"), R(r"\b(are|is) now\b"), R(r"\bnow (failing|leaving|banned|illegal|required|mandatory)\b"), R(r"\bbann?(ed|ing)?\b"), R(r"\bnew (rules?|laws?|regulations?|refrigerants?|standards?|requirements?|mandates?)\b"),
                      R(r"\btax credits?\b|\brebates?\b"), R(r"\bwarning\b"), R(r"\balert\b"), R(r"\brecall(ed|s)?\b"), R(r"\bphas(e|ed|ing)[- ]?out\b"), R(r"\b(going away|is ending|being discontinued|discontinued|shortage)\b"),
                      R(r"\bprices? (are )?(going up|skyrocket|increas|doubl)"), R(r"\beveryone (will|is)\b"), R(r"\b(coming|starting|in) 20(2[5-9])\b.*\b(change|rule|refrigerant|law|ban)"), R(r"\b(r-?22|r-?410a?|r-?454b?|r-?32)\b.*\b(ban|end|phase|change|price|shortage|new)\b"),
                      R(r"\b(dangerous|deadly)\b"), R(r"\bkill(s|ing)? (you|people|your family|families)\b|\bsilent killer\b"), R(r"\bchanges? (for|in|coming)\b"), R(r"\bthe future of\b")]),
    ("cheap hack", [R(r"\bhacks?\b"), R(r"\btricks?\b"), R(r"\bcheap(ly)?\b(?!est)(?=.*\b(and|&|way|alternative|fix|trick|solution|option|diy|hack|heat|cool)\b)|\bfor cheap\b|\bcheaply\b|\bcheaper (way|than|alternative)\b"), R(r"\$\s?[\d,.]+\s?(trick|hack|fix|part|tool|item|solution|device|gadget|way|filter|upgrade|thing|product|secret|cover|kit)\b"), R(r"\b(use|try) (this|these|that) instead\b"), R(r"\binstead\b"),
                    R(r"\bfor (under|less than)\b"), R(r"\bdollars?\b"), R(r"\bfree (heat|heating|cooling|ac|a/c|air conditioning|energy|electricity|power|air)\b|\bfor free\b"),
                    R(r"\bsav(e|es|ing) (money|\$|big|hundreds|thousands|on)\b"), R(r"\b(lower|cut|reduce|slash|lowering|cutting|reducing) (your |the |my |our )?(electric|electricity|energy|heating|cooling|power|gas|utility|ac)? ?bills?\b"),
                    R(r"\bbudget\b"), R(r"\b\d+x (stronger|faster|warmer|cooler|better|hotter|more)\b|\b(aluminum|aluminium|tin|the|kitchen) foil\b"), R(r"\blow[- ]cost\b|\binexpensive\b|\baffordable\b"), R(r"\bgenius\b"), R(r"\bwithout (ac|a/c|air conditioning|electricity|power)\b"), R(r"\bno elec\w* needed\b|\bno (power|gas|fuel) needed\b|\bunlimited (free )?(heat|cooling|hot)\b")]),
    ("symptom-fix", [R(r"\bnot (cooling|heating|working|turning on|blowing|igniting|lighting|starting|running|coming on|getting (hot|warm|cold)|kicking on|shutting off|cold|warm|hot)\b"),
                     R(r"\b(won'?t|doesn'?t|does not|will not|wont) (turn|start|cool|heat|ignite|light|kick|shut|stop|blow|come|work|run|get|stay|hold)\b"),
                     R(r"\bno (heat|cool|cold|air|hot)\b"), R(r"\bblowing (hot|warm|cold|cool) air\b|\bblows (hot|warm|cold) air\b"), R(r"\bfreez(e|es|ing)\b|\bfrozen\b|\biced? ?up\b|\bice (build|buildup|on|forming|in)\b|\bicing\b"),
                     R(r"\bleak(s|ing|y)?\b"), R(r"\bshort[- ]?cycl"), R(r"\bkeeps? (turning|shutting|running|tripping|cycling|going|blowing|clicking)\b"), R(r"\btrip(s|ping|ped)\b"),
                     R(r"\bsmell(s|ing|y)?\b|\bodou?rs?\b|\bstinks?\b"), R(r"\bnois(e|es|y)\b|\bloud\b|\bsqueal|\bbang(s|ing)\b|\brattl|\bhumming\b|\bbuzz(ing)?\b|\bclicking\b|\bwhistl|\bknock(ing)?\b|\bhiss(ing)?\b|\bgrind(ing)?\b|\bvibrat|\bscreech"),
                     R(r"\bwater (on|in|under|around|dripping|leaking|coming)\b|\bdripping\b|\bcondensation\b|\bsweat(s|ing)?\b|\bstains?\b"), R(r"\berror codes?\b|\bflashing\b|\bblinking\b|\bcode \d+\b"),
                     R(r"\boverheat"), R(r"^(?!\s*what\b).*\b(problems?|issues?)\b"), R(r"\bbroken\b|\bstopped working\b|\bquit working\b|\bdead\b|\bfail(ing|ed|s|ure)?\b"), R(r"\bruns? (constantly|all the time|nonstop|non-stop|all day)\b"),
                     R(r"\btoo (hot|cold|humid|dry)\b|\buneven\b|\bhot (rooms?|spots?|upstairs|bedroom)\b|\bcold (rooms?|spots?|upstairs|bedroom)\b|\bweak (air|airflow)\b|\blow (airflow|air flow|pressure)\b"),
                     R(r"\b(not|isn'?t|aren'?t) [a-z]{3,}ing\b"), R(r"\bmou?ld\b|\bmildew\b|\bblack (gunk|stuff|slime)\b"), R(r"\bsigns? (of|your|that)\b|\bsymptoms?\b"), R(r"\bwhy (is|does|isn'?t|won'?t) (my|your)\b"), R(r"\bwhat causes\b"),
                     R(r"\bhigh (electric |energy |power )?bills?\b|\bbill (is )?(so )?high\b"), R(r"\bsoaring\b|\bskyrocketing\b")]),
    ("install/DIY project", [R(r"^(?=.*\b(ac|a/c|air condition\w*|mini[- ]?splits?|heat pumps?|furnaces?|boilers?|systems?|units?|hvac|thermostats?|ductwork|ducts?|central air|wood ?stoves?|stoves?|heaters?|insulation|fans?|radiators?|baseboards?|geothermal|condensers?|outlets?|generators?|dehumidifiers?|humidifiers?|purifiers?|vents?|windows?|attic|tubes?|solar|panels?|radiant|ptac|chiller|air handler|zoning)\b).*\binstall(s|ing|ed|ation|ations|er)?\b|^(?!.*\bhow to\b).*\binstall(s|ing|ed|ation|ations)?\b"), R(r"^(?!.*\b(clean|maint|repair|fix|replac|servic|tune|flush|unclog)).*\bdiy\b.*\b(mini[- ]?split|system|heat pump|furnace|boiler|duct(s|work)?|project|central air|air conditioning|ac unit|geothermal|radiant)\b"), R(r"\badding\b"), R(r"\brestor(e|es|ed|ing|ation)\b|\bmaking (a|an|of|my|your|the|smoke|wood|homemade)\b|\bcreative ideas?\b|\bthe idea of\b|\b(from|out of) (red )?(bricks?|cement|barrels?|cans?|clay|pots?|bottles?|scrap|pallets?)\b"),
                             R(r"\bbuild(ing)? (a|my|your|an|our|the)\b|\bi built\b|\bwe built\b|\bhomemade\b|\bmake (a|your own|my own)\b"), R(r"\bin (\d+|one|a|1) (hours?|hrs?|day|days|weekend)\b"),
                             R(r"\bstart to finish\b|\bfrom scratch\b|\btransformation\b|\bfull (job|install|project|build)\b"), R(r"\bconvert(ing|ed)?\b|\bconversion\b"), R(r"\badd(ing|ed)? (air conditioning|ac|a mini split|central air|a heat pump)\b"),
                             R(r"\breplac(e|ing|ed) (my|our|the|a|an) ?(whole|entire|old)? ?(furnace|boiler|ac|air conditioner|system|heat pump|condenser|hvac)\b(?! (compressor|capacitor|contactor|fan|motor|coil|filter|board|valve|pump|thermostat|switch|sensor|igniter|ignitor|relay|blower|belt|line|drain))")]),
    ("how-to", [R(r"\bhow (to|i|we)\b"), R(r"\bstep[- ]by[- ]step\b|\bguide\b|\btutorial\b|\bwalkthrough\b"), R(r"\bclean(ing|ed|er)?\b"), R(r"\breplac(e|ing)\b|\bchang(e|ing) (the|your|a|my)\b"),
                R(r"\bmaintenance\b|\bmaintain\b|\btune[- ]?up\b|\bservicing\b|\bservice (your|the|a|my)\b|\bcheck ?list\b|\binspect"), R(r"\breplacement\b(?! cost)|\b(re)?charg(e|ing) (the |your |an? )?(system|refrigerant|freon|ac|unit)|\bvacuum|\bbraz(e|ing)\b"), R(r"\bset ?up\b|\bsetting up\b|\bwir(e|es|ing)\b|\bprogram(ming)?\b|\breset\b"),
                R(r"\bfix(ed|ing|es)?\b|\brepair(s|ing|ed)?\b"), R(r"\b(the )?(right|proper|correct|best|easiest|fastest|quickest) way\b|\bproperly\b|\bcorrectly\b"), R(r"\bdo this\b|\btips?\b|\bways to\b|\bsteps\b|\bthings (to|you)\b"),
                R(r"\bmake (it|your|the)\b|\bkeep(ing)? (your|the|a|it|you)\b|\bprepar(e|ing)\b|\bwinteriz|\bsummeriz|\bflush|\bseal(ing)?\b|\binsulat(e|ing)\b|\bunclog|\bbleed(ing)?\b|\bdrain(ing)?\b"),
                R(r"\btroubleshoot|\b(annual|yearly|seasonal|fall|spring) service\b|\binstall(s|ing|ed|ation)?\b|\b(filter|bearing|capacitor|motor|belt|battery|oil|coil) (change|swap|replacement)\b"), R(r"\bdiy\b"), R(r"\bwhat to do\b|\bwhat (i|we) do\b|\bwhere to\b|\bhow and\b|\bcheck(ing)? (the|your|a)\b|\bwatch out for\b|\bchoos(e|ing)\b|\brules (of|for)\b"), R(r"\bsize\b|\bsizing\b|\bcalculat"), R(r"\b(stay|staying) (cool|warm)\b"), R(r"\b(heat|cool|warm) (your|a|the) (home|house|room|garage)\b")]),
    ("explainer", [R(r"\bhow\b(?! to\b).{0,50}\bworks?\b"), R(r"\bwhy\b"), R(r"\b(types|kinds) of\b|\bq ?(&|and) ?a\b|\bfaq\b|\bquestions\b"), R(r"\bexplain(ed|s|ing)?\b"), R(r"\bbasics\b|\b101\b|\bintro(duction)? to\b|\bbeginners?'?\b"),
                   R(r"\bwhat (is|are|'?s) (a|an|the)?\b"), R(r"\bwhat'?s the (difference|point|deal)\b|\bdifference between\b"), R(r"\bwhy (do|does|is|are|you|we|it|they|some|most|so|did|should|would|people|homes|houses|americans|old)\b"),
                   R(r"\bunderstand(ing)?\b"), R(r"\b(everything|what|things|equations|facts|rules) you (need|should|must) (to )?know\b"), R(r"\bthe science\b|\bmeaning\b"), R(r"\bhow (much|long|often|many|cold|hot|efficient|big)\b"), R(r"\b(should|do|can|could|will|would) (i|you|we)\b"),
                   R(r"^(is|are|can|do|does|should|will|would|could)\b.*\?"), R(r"^what\b.*\?\s*$"), R(r"\bcost(s)?\b|\bpros and cons\b")]),
    ("story", [R(r"\bsurviv(e|ing|ed|al)\b"), R(r"\bwhat happened\b|\bhappens when\b"), R(r"\b(i|we) (tried|bought|got|had|was|were|spent|paid|lived|went|called|found|did|made|lost|finally|switched|moved|ditched|ran|left)\b"),
               R(r"\bmy (experience|story|journey|disaster|nightmare|first|new|old|house|home|wife|husband|dad|mom|attic|basement|furnace|ac|boiler|heat pump|electric|homemade)\b"), R(r"\bdisaster\b|\bnightmare\b|\bgone wrong\b|\bvlog\b|\bday in the life\b|\ba day of\b|\bride[- ]?along\b"),
               R(r"\b(i|we)'?(ve|m)\b"), R(r"\b(after|for) (\d+|one|a|two|three) (years?|months?|winters?|summers?|weeks?)\b"), R(r"\bour (house|home|first|new|old)\b")]),
]
FORMATS = [f for f, _ in FORMAT_RULES] + ["plain topic/other"]

def clean_title(title, channel):
    t = title.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    t = re.sub(r"\s+", " ", t).strip()
    if channel:
        ch = re.escape(channel.strip())
        t = re.sub(r"\s*[|\-–—:]\s*(Ask )?" + ch + r"\s*$", "", t, flags=re.I)
    return t

AMBIENT = R(r"\basmr\b|white noise|brown noise|pink noise|\bsleep(ing)?\b|black screen|\brelax(ing|ation)?\b|\b\d+\s*hours? of\b|\bambien|\bgameplay\b|minecraft|roblox|fortnite|\bboiler room\b|\blyrics\b|\bofficial (video|audio)\b|\bfull episode\b")

def tag_format(title, channel=""):
    t = clean_title(title, channel)
    if AMBIENT.search(t): return "plain topic/other"
    for name, rules in FORMAT_RULES:
        for r in rules:
            if r.search(t): return name
    return "plain topic/other"

# ---------------------------------------------------------------- inputs

def load_lines():
    files = [os.path.join(SWEEP, "priority.jsonl")] + sorted(glob.glob(os.path.join(SWEEP, "extended-*.jsonl")))
    lines = []
    for f in files:
        mode = "priority" if os.path.basename(f).startswith("priority") else "extended"
        for l in open(f):
            try: j = json.loads(l)
            except Exception: continue
            j["mode"] = mode
            lines.append(j)
    # one line per (mode, keyword, sort): keep the first (resumable sweep should not duplicate)
    seen, out = set(), []
    for j in lines:
        k = (j["mode"], j["keyword"], j["sort"])
        if k in seen: continue
        seen.add(k); out.append(j)
    return out

def load_keywords():
    return {r["keyword"]: r for r in csv.DictReader(open(os.path.join(RAW, "keywords-round2.csv")))}

def norm_handle(h):
    if not h: return ""
    h = urllib.parse.unquote(h).strip()
    h = re.sub(r"^https?://(www\.)?youtube\.com", "", h)
    h = h.lstrip("/")
    if h.startswith("channel/"): return ""
    return h.lstrip("@").lower()

def load_known():
    ids, handles = set(), set()
    for fn in ("channel-finds-round1.md", "leads-channels.md", "known-channels-recheck.md"):
        txt = open(os.path.join(SEEDS, fn)).read()
        ids |= set(re.findall(r"UC[A-Za-z0-9_-]{22}", txt))
        handles |= {h.lower() for h in re.findall(r"@([A-Za-z0-9._\-]+)", txt)}
    return ids, handles

def short_source(src):
    parts = [p.strip() for p in src.split(";")]
    kinds = []
    for p in parts:
        if p.startswith("autocomplete"): k = "autocomplete"
        elif p.startswith("brief topic"): k = "brief topic list"
        elif p.startswith("helper-added"): k = "helper-added seed"
        elif p.startswith("known title"): k = "known title"
        elif p.startswith("Silver Cymbal"): k = "Silver Cymbal title"
        else: k = p[:30]
        if k not in kinds: kinds.append(k)
    return ", ".join(kinds)

# ---------------------------------------------------------------- build

def med(xs):
    return statistics.median(xs) if xs else None

def fmt_int(x):
    if x is None: return "not found"
    return f"{int(round(x)):,}"

def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "n/a"

def md_esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")

def load_oembed():
    """id -> original title (oEmbed, http 200 only), and id -> http code for failures."""
    p = os.path.join(RAW, "sweep-oembed-2026-10-24.jsonl")
    ok, err = {}, {}
    if os.path.exists(p):
        for l in open(p):
            try: j = json.loads(l)
            except Exception: continue
            if j.get("orig_title") is not None: ok[j["id"]] = j["orig_title"]; err.pop(j["id"], None)
            elif j["id"] not in ok: err[j["id"]] = j.get("http", "")
    return ok, err

OEMBED, OEMBED_ERR = {}, {}

def build():
    global OEMBED, OEMBED_ERR
    OEMBED, OEMBED_ERR = load_oembed()
    lines = load_lines()
    kws = load_keywords()
    known_ids, known_handles = load_known()
    drop = collections.Counter()
    nonenglish_examples = []
    oembed_drops = []
    videos = {}         # id -> dict
    searches = []       # per (mode, keyword, sort)
    for j in lines:
        sort = j["sort"]
        raw = j["rows"]
        kept = []
        raw_views = []
        in_window = 0; with_age = 0
        for rank, r in enumerate(raw, 1):
            v = parse_views(r.get("views")); L = parse_len(r.get("length"))
            if v is not None: raw_views.append(v)
            if r.get("age"):
                with_age += 1
                if (sort == "year" and within_12m(r["age"])) or (sort == "month" and within_5w(r["age"])): in_window += 1
            # filters, counted per search row
            if L is None:
                drop["no length (live / upcoming)" if r.get("views") is None else "no length (other)"] += 1; continue
            if L < LONG_MIN:
                drop["under 5:00"] += 1; continue
            if v is None:
                drop["long-form but no view count"] += 1; continue
            eng, why = english_check(r.get("title") or "")
            if eng and r["id"] in OEMBED:
                eng, why = english_check(OEMBED[r["id"]])
                if not eng:
                    drop["not English: original title (oEmbed); the search page showed an English translation"] += 1
                    if r["id"] not in {x[0] for x in oembed_drops}: oembed_drops.append((r["id"], r["title"], OEMBED[r["id"]], why))
                    continue
            if not eng:
                drop["not English (rule, on the search-page title)"] += 1
                if r["id"] not in {x[0] for x in nonenglish_examples}: nonenglish_examples.append((r["id"], r["title"], why))
                continue
            win_ok = True
            if sort == "year": win_ok = within_12m(r.get("age"))
            if sort == "month": win_ok = within_5w(r.get("age"))
            vid = videos.setdefault(r["id"], {"id": r["id"], "title": OEMBED.get(r["id"], r["title"]), "search_title": r["title"], "channel": r.get("channel") or "", "channelId": r.get("channelId") or "",
                                              "handle": r.get("handle") or "", "views": v, "age": r.get("age") or "", "pulled": j["pulled"],
                                              "length": L, "apps": []})
            if v > vid["views"]: vid["views"] = v
            vid["apps"].append({"mode": j["mode"], "keyword": j["keyword"], "topic": j["topic"], "framing": j["framing"], "sort": sort, "rank": rank,
                                "views": v, "in_window": win_ok})
            if not win_ok:
                drop[f"{sort} search: outside my age window (video kept, search row not counted)"] += 1; continue
            kept.append((rank, r, v))
        rises = sum(1 for a, b in zip(raw_views, raw_views[1:]) if b > a)
        big_rises = sum(1 for a, b in zip(raw_views, raw_views[1:]) if b > 2 * a)
        searches.append({"mode": j["mode"], "keyword": j["keyword"], "topic": j["topic"], "framing": j["framing"], "sort": sort, "pulled": j["pulled"],
                         "raw_n": len(raw), "kept": kept, "views_pairs": max(len(raw_views) - 1, 0), "rises": rises, "big_rises": big_rises,
                         "with_age": with_age, "in_window": in_window})
    # search medians and above-median per appearance
    smed = {}
    for s in searches:
        vs = [v for _, _, v in s["kept"]]
        s["median"] = med(vs)
        smed[(s["mode"], s["keyword"], s["sort"])] = (s["median"], len(vs))
    for vid in videos.values():
        above = tot = 0
        for a in vid["apps"]:
            if not a["in_window"]: continue
            m, n = smed[(a["mode"], a["keyword"], a["sort"])]
            if n < MIN_SEARCH_N: continue
            tot += 1
            if a["views"] > m: above += 1
        vid["above_n"], vid["above_of"] = above, tot
        vid["above"] = (above / tot > 0.5) if tot else None
        vid["topics"] = sorted({a["topic"] for a in vid["apps"]})
        vid["keywords"] = sorted({a["keyword"] for a in vid["apps"]})
        vid["sorts"] = sorted({a["sort"] + ("" if a["in_window"] else "(outside window)") for a in vid["apps"]})
        vid["best_rank"] = min(a["rank"] for a in vid["apps"])
        rel = [a["rank"] for a in vid["apps"] if a["sort"] == "relevance"]
        vid["best_rel_rank"] = min(rel) if rel else ""
        vid["format"] = tag_format(vid["title"], vid["channel"])
        vid["hvac_title"] = is_hvac(clean_title(vid["title"], vid["channel"]).lower())
        vid["recent"] = within_12m(vid["age"])
        vid["date"] = approx_date(vid["age"], vid["pulled"])
        vid["live_replay"] = (parse_age(vid["age"]) or (0, "", False))[2]
        h = norm_handle(vid["handle"])
        vid["is_new"] = not (vid["channelId"] in known_ids or (h and h in known_handles))
    for vid in videos.values():
        vid["orig_checked"] = "yes" if vid["id"] in OEMBED else ("oEmbed " + OEMBED_ERR[vid["id"]] if vid["id"] in OEMBED_ERR else "not fetched")
    return lines, kws, searches, videos, drop, nonenglish_examples, oembed_drops

# ---------------------------------------------------------------- outputs

TOPIC_NAMES = {}

def load_topic_names():
    txt = open(os.path.join(SEEDS, "keywords-round2.md")).read()
    for name, code in re.findall(r"^\| ([^|]+?) \| `([a-z\-]+)` \|", txt, flags=re.M):
        TOPIC_NAMES.setdefault(code, name.strip())

def write_csvs(searches, videos, channels):
    with open(os.path.join(RAW, "sweep-videos-2026-10-24.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "channel", "channelId", "handle", "views", "age_text", "approx_upload_date", "length_s", "live_replay",
                    "format_rule", "keywords", "n_keywords", "sorts", "best_rank", "best_relevance_rank", "topics", "above_search_median", "searches_above", "searches_counted", "new_channel", "hvac_word_in_title", "original_title_checked", "search_page_title"])
        for v in sorted(videos.values(), key=lambda x: -x["views"]):
            w.writerow([v["id"], v["title"], v["channel"], v["channelId"], v["handle"], v["views"], v["age"], v["date"], v["length"], "yes" if v["live_replay"] else "",
                        v["format"], " ; ".join(v["keywords"]), len(v["keywords"]), " ; ".join(v["sorts"]), v["best_rank"], v["best_rel_rank"], " ; ".join(v["topics"]),
                        "" if v["above"] is None else ("yes" if v["above"] else "no"), v["above_n"], v["above_of"], "NEW" if v["is_new"] else "", "yes" if v["hvac_title"] else "", v["orig_checked"], v["search_title"] if v["search_title"] != v["title"] else ""])
    with open(os.path.join(RAW, "sweep-keywords-2026-10-24.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["mode", "keyword", "topic", "framing", "sort", "pulled", "raw_results", "longform_english_kept", "median_views", "top_id", "top_title", "top_views",
                    "views_adjacent_pairs", "views_rises", "raw_with_age", "raw_in_age_window"])
        for s in searches:
            top = max(s["kept"], key=lambda x: x[2]) if s["kept"] else None
            w.writerow([s["mode"], s["keyword"], s["topic"], s["framing"], s["sort"], s["pulled"], s["raw_n"], len(s["kept"]),
                        "" if s["median"] is None else s["median"], top[1]["id"] if top else "", top[1]["title"] if top else "", top[2] if top else "",
                        s["views_pairs"], s["rises"], s["with_age"], s["in_window"] if s["sort"] in ("year", "month") else ""])
    with open(os.path.join(RAW, "sweep-channels-2026-10-24.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "channel", "handle", "channelId", "videos", "total_views", "median_views", "videos_last_12m", "top_id", "top_title", "top_views", "n_topics", "topics", "new", "hvac_word_videos"])
        for i, c in enumerate(channels, 1):
            w.writerow([i, c["channel"], c["handle"], c["channelId"], c["n"], c["total"], c["median"], c["recent"], c["top"]["id"], c["top"]["title"], c["top"]["views"],
                        len(c["topics"]), " ; ".join(sorted(c["topics"])), "NEW" if c["is_new"] else "", c["hvac"]])

def channel_tally(videos):
    ch = {}
    for v in videos.values():
        key = v["channelId"] or v["channel"]
        c = ch.setdefault(key, {"channel": v["channel"], "handle": v["handle"], "channelId": v["channelId"], "vids": [], "topics": set(), "is_new": v["is_new"]})
        c["vids"].append(v); c["topics"] |= set(v["topics"])
    out = []
    for c in ch.values():
        vs = [v["views"] for v in c["vids"]]
        c["n"] = len(vs); c["total"] = sum(vs); c["median"] = med(vs)
        c["recent"] = sum(1 for v in c["vids"] if v["recent"])
        c["hvac"] = sum(1 for v in c["vids"] if v["hvac_title"])
        c["top"] = max(c["vids"], key=lambda v: v["views"])
        out.append(c)
    out.sort(key=lambda c: (-c["n"], -c["total"]))
    return out

def group_stats(vs):
    views = [v["views"] for v in vs]
    # per appearance: each time a video showed up in a usable search, did it beat that search's median?
    above = sum(v["above_n"] for v in vs)
    flagged = [None] * sum(v["above_of"] for v in vs)
    return {"n": len(vs), "channels": len({v["channelId"] or v["channel"] for v in vs}), "median": med(views),
            "above": above, "flagged": len(flagged), "top": sorted(vs, key=lambda v: -v["views"])[:3]}

def ex_str(v):
    return f'"{md_esc(v["title"])}" ({md_esc(v["channel"])}, {v["views"]:,}, `{v["id"]}`)'

def format_table(vs, title):
    out = [f"### {title}", "", "| Format (rule-based) | Videos | Channels | Median views | Above their search median | 3 biggest (title, channel, views, ID) |", "|---|---:|---:|---:|---:|---|"]
    by = collections.defaultdict(list)
    for v in vs: by[v["format"]].append(v)
    for f in FORMATS:
        g = group_stats(by.get(f, []))
        if not g["n"]:
            out.append(f"| {f} | 0 | 0 | not found | n/a | none |"); continue
        out.append(f"| {f} | {g['n']:,} | {g['channels']:,} | {fmt_int(g['median'])} | {pct(g['above'], g['flagged'])} ({g['above']:,} of {g['flagged']:,} appearances) | " + "<br>".join(ex_str(v) for v in g["top"]) + " |")
    g = group_stats(vs)
    out.append(f"| **all** | **{g['n']:,}** | **{g['channels']:,}** | **{fmt_int(g['median'])}** | **{pct(g['above'], g['flagged'])}** ({g['above']:,} of {g['flagged']:,}) | |")
    return out

def topic_rows(vs_all):
    by = collections.defaultdict(list)
    for v in vs_all:
        for t in v["topics"]: by[t].append(v)
    rows = []
    for t in sorted(by, key=lambda t: -len(by[t])):
        g = group_stats(by[t]); only = sum(1 for v in by[t] if len(v["topics"]) == 1)
        rec = [v for v in by[t] if v["recent"]]; gr = group_stats(rec)
        rows.append((t, g, only, gr))
    return rows

def handcheck_summary(videos, fn):
    p = os.path.join(RAW, fn)
    if not os.path.exists(p): return None
    rows = list(csv.DictReader(open(p)))
    v1 = sum(1 for r in rows if r["rule_tag_v1"] == r["hand_tag"])
    cur = 0; errs_v1 = collections.Counter(); errs_cur = []
    for r in rows:
        now = videos[r["id"]]["format"] if r["id"] in videos else tag_format(r["title"])
        r["rule_now"] = now
        if now == r["hand_tag"]: cur += 1
        else: errs_cur.append(r)
        if r["rule_tag_v1"] != r["hand_tag"]: errs_v1[(r["rule_tag_v1"], r["hand_tag"])] += 1
    return {"rows": rows, "n": len(rows), "v1": v1, "cur": cur, "errs_v1": errs_v1, "errs_cur": errs_cur,
            "gone": sum(1 for r in rows if r["id"] not in videos)}

def main():
    load_topic_names()
    lines, kws, searches, videos, drop, nonen, odrops = build()
    channels = channel_tally(videos)
    write_csvs(searches, videos, channels)
    vs_all = list(videos.values())
    vs_recent = [v for v in vs_all if v["recent"]]
    pr = [s for s in searches if s["mode"] == "priority"]
    ex = [s for s in searches if s["mode"] == "extended"]
    raw_rows = sum(s["raw_n"] for s in searches)
    n_new = sum(1 for c in channels if c["is_new"])
    pulled = sorted(s["pulled"] for s in searches)
    ext_kw_total = sum(1 for k in kws.values() if k["priority"].strip().upper() != "PRIORITY")
    stats = {"lines": len(lines), "priority_lines": len(pr), "extended_lines": len(ex), "extended_keywords_total": ext_kw_total, "raw_rows": raw_rows,
             "drops": dict(drop), "unique_videos": len(videos), "recent_videos": len(vs_recent), "channels": len(channels), "new_channels": n_new,
             "nonenglish_unique_titles": len(nonen), "oembed_dropped_videos": len(odrops),
             "orig_title_checked": sum(1 for v in videos.values() if v["orig_checked"] == "yes"),
             "orig_title_failed": collections.Counter(v["orig_checked"] for v in videos.values() if v["orig_checked"] != "yes"), "pulled_first": pulled[0], "pulled_last": pulled[-1]}
    json.dump(stats, open(os.path.join(RAW, "sweep-build-2026-10-24.json"), "w"), indent=1)

    # ---- sort checks (priority)
    def sort_check(sort):
        ss = [s for s in pr if s["sort"] == sort]
        pairs = sum(s["views_pairs"] for s in ss); rises = sum(s["rises"] for s in ss)
        clean = sum(1 for s in ss if s["rises"] == 0)
        big = sum(s["big_rises"] for s in ss)
        wa = sum(s["with_age"] for s in ss); iw = sum(s["in_window"] for s in ss)
        return ss, pairs, rises, clean, wa, iw, big

    # ---- keyword-sweep.md
    K = []
    A = K.append
    A("# HVAC round 2: the keyword sweep")
    A("")
    A(f"Built 2026-10-24 by a round 2 helper with `studies/hvac/data/tools/sweep_build.py` (rerunnable) from the logged-out YouTube search sweep run by the main session (`sweep_round2.py`). Deliverable 8 of `RESEARCH-BRIEF.md`. Formats are in `formats.md`.")
    A("")
    A("**Status:** not yet re-checked by a second helper (working rule 3). Every count below is computed by the script from the raw search pages. Topic and framing labels on keywords are the keyword list's rule-based labels; format tags on titles are rule-based (see `formats.md`). Where a line says \"reading\", it is the helper's judgement, not a count.")
    A("")
    A("Files: `data/raw/sweep-2026-10-24/*.jsonl` (raw search results), `data/raw/sweep-videos-2026-10-24.csv` (unique videos), `data/raw/sweep-keywords-2026-10-24.csv` (one row per search), `data/raw/sweep-channels-2026-10-24.csv` (every channel), `data/raw/sweep-build-2026-10-24.json` (the counts), `data/raw/format-handcheck-2026-10-24.csv` (the hand-check).")
    A("")
    A("## Method")
    A("")
    A(f"- **Source:** YouTube search result pages, loaded logged out (`hl=en`, `gl=US`), pulled {pulled[0]} to {pulled[-1]} (UTC). Views are YouTube's own counts on the search page (\"1,234 views\"); lengths are the page's length text; ages are YouTube's relative text (\"3y ago\").")
    A("- **Sorts.** PRIORITY keywords: 4 searches each, 2 result pages each: `relevance`; `views` (sorted by view count); `year` (view count, uploaded this year); `month` (view count, uploaded this month). The brief asks for relevance, newest, oldest and most viewed: YouTube's \"upload date\" sort no longer works (tested 2026-10-23) and search has no \"oldest\" sort, so the operator approved this substitute on 2026-10-24 (old videos come from channels' Oldest tabs instead). EXTENDED keywords: relevance only, 1 page.")
    done_ext = {s["keyword"] for s in ex}
    missing = [k for k, r in kws.items() if r["priority"].strip().upper() != "PRIORITY" and k not in done_ext]
    A(f"- **Coverage:** {len(pr)} PRIORITY searches (150 keywords x 4 sorts); {len(ex)} EXTENDED searches of {ext_kw_total} EXTENDED keywords" + (" (complete)." if len(ex) >= ext_kw_total else f" (the extended sweep was still running when this was built; {len(ex)} of {ext_kw_total} done).") + f" {raw_rows:,} result rows in all." + (f" EXTENDED keywords with no search line (the sweep logged them as failed, or they are still to run): {len(missing)}: " + ", ".join(f'\"{k}\"' for k in missing[:80]) + ("..." if len(missing) > 80 else "") + "." if missing else ""))
    A("- **Age windows (my rule, from the age text):** YouTube shows ages as min, h, d (up to 13d), w (2w to 4w), mo (1mo to 11mo), then y. `year` results count only if the age is below \"1y\" (under 12 months). `month` results count only if the age is in min, h, d or w (under about 5 weeks); \"1mo ago\" is out. A video outside the window is still kept in the video list (it is a real result for the keyword), but that search row is not counted in the per-search figures.")
    A("- **Upload date** in the CSV is approximate: pull date minus the age (1y = 365.25 days, 1mo = 30.44 days). YouTube rounds ages down, so the real upload is up to one unit earlier.")
    A("- **Long-form:** length 5:00 (300 s) or more. Live streams with no length are dropped; replays of past streams (\"Streamed ... ago\") with a length are kept and marked in the CSV.")
    A("- **English (rule-based):** a title is dropped if (a) 30% or more of its letters are in a non-Latin script; (b) it has 2+ common words from Spanish, Portuguese, French, German, Hindi or Urdu written in Latin letters, Indonesian or Tagalog, and more of those than English function words; (c) it has 1+ such word and no English function word; or (d) it has a letter used only in other languages (Turkish, Polish, Czech, Vietnamese, transliteration marks) and fewer than 2 English function words; or (e) it says it is \"in Hindi\" (or Urdu, Tamil, Spanish and so on). The word lists are `FOREIGN`, `ENGLISH` and `STRONG_FOREIGN_LETTERS` in the script.")
    nchk = stats["orig_title_checked"]
    A(f"- **Original titles (oEmbed):** logged-out search auto-translates foreign titles into English (found by the old-house heat helper, 2026-10-24). So each video's original title was fetched from YouTube oEmbed (`tools/sweep_oembed.py`, pulled 2026-10-24, raw in `data/raw/sweep-oembed-2026-10-24.jsonl`) and the English rule was run on it too. Original title checked for {nchk:,} of the {len(videos) + len(odrops):,} long-form videos that passed the search-title rule; " + ", ".join(f"{k}: {v:,}" for k, v in stats["orig_title_failed"].items()) + f" (those keep the search-page check only; oEmbed 401 = embedding turned off, 404 = gone). **{len(odrops):,} videos dropped** because the original title is not English. Titles shown in these files are the original titles.")
    A("- **Per video:** views = the highest count seen across its searches (pulls were minutes to hours apart). Keywords, sorts and topics are every one that returned it. Best rank = its best position in any search (position counts every row on the page, including Shorts and lives).")
    A(f"- **\"Above search median\" (a within-search relative measure):** for each search, the median views of the long-form English results it kept (`year` and `month` searches: only those inside the age window). Each time a video shows up in a search, it either beats that search's median or not. A group's figure is the share of its appearances that beat the median (searches with fewer than {MIN_SEARCH_N} kept results are not used). Across all videos this is a little under 50% by construction (the median video itself never beats it), so a format or topic well over the all-videos figure beats the other videos returned for the same keywords. A video returned by many searches counts once per search. It is not the channel multiple; that comes in round 3. The video CSV gives each video's own count (`searches_above` of `searches_counted`; `above_search_median` = yes when more than half).")
    A("")
    A("### Rows dropped (counted per search row, so a video can be counted more than once)")
    A("")
    A("| Reason | Search rows |")
    A("|---|---:|")
    for k, v in sorted(drop.items(), key=lambda x: -x[1]): A(f"| {k} | {v:,} |")
    A("")
    A(f"Distinct titles dropped by the English rule: {len(nonen):,}. First 15 (for checking):")
    A("")
    for vid, t, why in nonen[:15]: A(f"- `{vid}` \"{md_esc(t)}\" ({why})")
    A("")
    A(f"Videos dropped on the original title (oEmbed): {len(odrops):,}. First 15 (search-page title -> original title):")
    A("")
    for vid, st, ot, why in odrops[:15]: A(f"- `{vid}` \"{md_esc(st)}\" -> \"{md_esc(ot)}\" ({why})")
    A("")
    A("### Did each sort behave? (PRIORITY searches)")
    A("")
    A("| Sort | Searches | Check | Result |")
    A("|---|---:|---|---|")
    ss, pairs, rises, clean, wa, iw, big = sort_check("relevance")
    A(f"| relevance | {len(ss)} | none possible (no order to test) | {sum(len(s['kept']) for s in ss):,} long-form English rows kept |")
    for sort in ("views", "year", "month"):
        ss, pairs, rises, clean, wa, iw, big = sort_check(sort)
        res = f"{clean} of {len(ss)} searches strictly in descending view order; {rises:,} of {pairs:,} adjacent pairs ({pct(rises, pairs)}) go up instead of down, {big:,} of them by more than double"
        if sort in ("year", "month"):
            res += f"; {iw:,} of {wa:,} dated rows ({pct(iw, wa)}) inside my {'12-month' if sort == 'year' else '5-week'} window"
        A(f"| {sort} | {len(ss)} | views descending?" + (" Results recent?" if sort != "views" else "") + f" | {res} |")
    A("")
    rn = collections.defaultdict(list)
    for s in pr: rn[s["sort"]].append(s["raw_n"])
    A("Rows per search (all rows on the page, before filters; 2 pages were requested for PRIORITY): " + "; ".join(f"`{k}` median {med(v):g}, {sum(1 for x in v if x > 20)} of {len(v)} searches with more than 20 rows" for k, v in rn.items()) + ". So the second page often added nothing (YouTube's continuation, as fetched logged out, returned few or no extra rows); most searches are effectively one page of about 20.")
    A("")
    # worst offenders
    for sort in ("views", "year", "month"):
        ss = [s for s in pr if s["sort"] == sort]
        worst = sorted(ss, key=lambda s: -s["rises"])[:5]
        A(f"- `{sort}`: most out-of-order searches: " + "; ".join(f"\"{s['keyword']}\" ({s['rises']} rises in {s['views_pairs']} pairs)" for s in worst) + ".")
    for sort in ("year", "month"):
        ss = [s for s in pr if s["sort"] == sort and s["with_age"]]
        worst = sorted(ss, key=lambda s: s["in_window"] / s["with_age"])[:5]
        A(f"- `{sort}`: least recent searches: " + "; ".join(f"\"{s['keyword']}\" ({s['in_window']} of {s['with_age']} in window)" for s in worst) + ".")
    A("")
    A("Reading: the `views` sort is mostly but not strictly descending: most rises are small, and Shorts sit between long videos in the order. The `year` and `month` sorts are looser still (a quarter to a third of adjacent pairs rise), so they are best read as \"popular recent videos\", not a ranked list. The `year` and `month` filters let some older videos through, which the age window above removes. The per-search figures below do not depend on the order.")
    A("")
    A("## The keyword list")
    A("")
    A(f"The keywords are `seeds/keywords-round2.md` (built 2026-10-23 from the brief's topic list, helper-added seeds, phrases from known winning titles, Silver Cymbal title phrases and YouTube autocomplete; full sources per keyword in `data/raw/keywords-round2.csv`). 5,825 keywords: 150 PRIORITY (picked by hand by the round 1 helper to cover every topic and framing) and 5,675 EXTENDED (autocomplete phrases that passed the home-HVAC word filter). That list has not yet been re-checked by a second helper. Sources of the 150 PRIORITY keywords, by kind (a keyword can have several):")
    A("")
    srcc = collections.Counter()
    for k in kws.values():
        if k["priority"].strip().upper() == "PRIORITY":
            for s in short_source(k["source"]).split(", "): srcc[s] += 1
    A("| Source kind | PRIORITY keywords |")
    A("|---|---:|")
    for s, n in srcc.most_common(): A(f"| {s} | {n} |")
    A("")
    # per keyword compact table
    A("## Per keyword (PRIORITY)")
    A("")
    A("Long-form English results kept / median views of those, per sort. `year` and `month` counts are after my age window. Check: `views` and `year`/`month` rises = adjacent pairs where the next result has more views (0 = strictly descending); `in win` = rows inside the age window of all dated rows.")
    A("")
    A("| # | Keyword | Topic | Framing | Source kind | relevance n / median | views n / median | year n / median | month n / median | views rises | year in win | month in win |")
    A("|---:|---|---|---|---|---|---|---|---|---:|---:|---:|")
    by_kw = collections.defaultdict(dict)
    for s in pr: by_kw[s["keyword"]][s["sort"]] = s
    order = [k for k in kws if kws[k]["priority"].strip().upper() == "PRIORITY"]
    for i, k in enumerate(order, 1):
        d = by_kw.get(k, {})
        def cell(sort):
            s = d.get(sort)
            if not s: return "not found"
            return f"{len(s['kept'])} / {fmt_int(s['median']) if s['median'] is not None else 'n/a'}"
        def win(sort):
            s = d.get(sort)
            return f"{s['in_window']}/{s['with_age']}" if s else "not found"
        A(f"| {i} | {md_esc(k)} | `{kws[k]['topic']}` | {kws[k]['framing']} | {short_source(kws[k]['source'])} | {cell('relevance')} | {cell('views')} | {cell('year')} | {cell('month')} | "
          f"{d['views']['rises'] if 'views' in d else 'n/a'}/{d['views']['views_pairs'] if 'views' in d else ''} | {win('year')} | {win('month')} |")
    A("")
    A("### Top video per keyword and sort (PRIORITY)")
    A("")
    A("The most-viewed kept long-form English result of each search.")
    A("")
    A("| Keyword | Sort | Top video (title, channel, views, ID) |")
    A("|---|---|---|")
    for k in order:
        for sort in ("relevance", "views", "year", "month"):
            s = by_kw.get(k, {}).get(sort)
            if not s or not s["kept"]:
                A(f"| {md_esc(k)} | {sort} | not found |"); continue
            r, v = max(s["kept"], key=lambda x: x[2])[1:]
            A(f"| {md_esc(k)} | {sort} | \"{md_esc(r['title'])}\" ({md_esc(r.get('channel'))}, {v:,}, `{r['id']}`) |")
    A("")
    # channels
    A("## Channel tally")
    A("")
    A(f"**{len(videos):,} unique long-form English videos** from **{len(channels):,} channels**. **{n_new:,} channels are NEW**: neither their channel ID nor their handle appears anywhere in `seeds/channel-finds-round1.md`, `seeds/leads-channels.md` or `seeds/known-channels-recheck.md` (a channel those files mention, even as a lead or a rejected candidate, counts as known). Of the top 100 below, {sum(1 for c in channels[:100] if c['is_new'])} are NEW. Full list: `data/raw/sweep-channels-2026-10-24.csv`.")
    A("")
    A("Videos = distinct long-form English videos the sweep returned from the channel (all keywords, all sorts); total views = the sum of those videos' views. This measures how often the channel turns up in these searches, not its size. Many are off-niche channels that a broad keyword pulled in (reading).")
    A("")
    nh3 = sum(1 for c in channels if c["is_new"] and c["hvac"] >= 3); nh5 = sum(1 for c in channels if c["is_new"] and c["hvac"] >= 5)
    A(f"Most NEW channels are off-niche (one stray video). A rough cut on the HVAC-word title rule (see `formats.md`): **{nh3:,} NEW channels have 3 or more returned videos with a home-HVAC word in the title, {nh5:,} have 5 or more.** These are the ones worth a round 3 look (reading).")
    A("")
    A("| # | Channel | Handle | Videos | HVAC-word videos | Total views | Median views | Last 12 mo | Topics | Biggest returned video (title, views, ID) | NEW |")
    A("|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|")
    for i, c in enumerate(channels[:100], 1):
        h = urllib.parse.unquote(c["handle"] or "").lstrip("/")
        A(f"| {i} | {md_esc(c['channel'])} | {md_esc(h)} | {c['n']} | {c['hvac']} | {c['total']:,} | {fmt_int(c['median'])} | {c['recent']} | {len(c['topics'])} | \"{md_esc(c['top']['title'])}\" ({c['top']['views']:,}, `{c['top']['id']}`) | {'NEW' if c['is_new'] else ''} |")
    A("")
    A("### Top 50 NEW channels by videos returned")
    A("")
    A("| # | Channel | Handle | channelId | Videos | HVAC-word videos | Total views | Last 12 mo | Biggest returned video (title, views, ID) |")
    A("|---:|---|---|---|---:|---:|---:|---:|---|")
    for i, c in enumerate([c for c in channels if c["is_new"]][:50], 1):
        h = urllib.parse.unquote(c["handle"] or "").lstrip("/")
        A(f"| {i} | {md_esc(c['channel'])} | {md_esc(h)} | `{c['channelId']}` | {c['n']} | {c['hvac']} | {c['total']:,} | {c['recent']} | \"{md_esc(c['top']['title'])}\" ({c['top']['views']:,}, `{c['top']['id']}`) |")
    A("")
    A("### Top 30 NEW channels by HVAC-word videos returned")
    A("")
    A("Same channels, ranked by returned videos with a home-HVAC word in the title (rule-based cut), then total views.")
    A("")
    A("| # | Channel | Handle | channelId | HVAC-word videos | Videos | Total views | Last 12 mo | Biggest returned video (title, views, ID) |")
    A("|---:|---|---|---|---:|---:|---:|---:|---|")
    for i, c in enumerate(sorted([c for c in channels if c["is_new"]], key=lambda c: (-c["hvac"], -c["total"]))[:30], 1):
        h = urllib.parse.unquote(c["handle"] or "").lstrip("/")
        A(f"| {i} | {md_esc(c['channel'])} | {md_esc(h)} | `{c['channelId']}` | {c['hvac']} | {c['n']} | {c['total']:,} | {c['recent']} | \"{md_esc(c['top']['title'])}\" ({c['top']['views']:,}, `{c['top']['id']}`) |")
    A("")
    # topics
    A("## Topics (sub-niches, from the keyword's topic)")
    A("")
    A("A video takes the topic of every keyword that returned it, so a video found by an `ac-central` and a `filters` keyword counts in both; topic rows add up to more than the unique total. `Only this topic` = videos returned by keywords of this topic alone. The topic is the keyword list's rule-based label, not a reading of the video. The \"above search median\" measure is not given here: a topic's videos are compared only with each other in the same searches, so it cannot rank topics against each other (compare median views instead; the channel multiple comes in round 3). Median views are of long-form English videos returned by any sort, so topics with more PRIORITY keywords (whose `views` sort pulls the biggest videos) read higher.")
    A("")
    A("| Topic | Code | Keywords searched | Videos | Only this topic | Channels | Median views | HVAC-word videos: n / median | Last 12 mo: videos / median | 3 biggest (title, channel, views, ID) |")
    A("|---|---|---:|---:|---:|---:|---:|---|---|---|")
    kw_by_topic = collections.Counter(s["topic"] for s in searches if s["sort"] == "relevance")
    for t, g, only, gr in topic_rows(vs_all):
        hv = group_stats([v for v in vs_all if t in v["topics"] and v["hvac_title"]])
        A(f"| {TOPIC_NAMES.get(t, t)} | `{t}` | {kw_by_topic.get(t, 0):,} | {g['n']:,} | {only:,} | {g['channels']:,} | {fmt_int(g['median'])} | {hv['n']:,} / {fmt_int(hv['median']) if hv['n'] else 'n/a'} | {gr['n']:,} / {fmt_int(gr['median']) if gr['n'] else 'n/a'} | " + "<br>".join(ex_str(v) for v in g["top"]) + " |")
    A("")
    open(os.path.join(OUTMD, "keyword-sweep.md"), "w").write("\n".join(K) + "\n")

    # ---- formats.md
    F = []
    B = F.append
    B("# HVAC round 2: formats in the keyword sweep")
    B("")
    B("Built 2026-10-24 by a round 2 helper with `studies/hvac/data/tools/sweep_build.py` from the keyword sweep (`keyword-sweep.md` has the method, sources and filters). Deliverable 8 of `RESEARCH-BRIEF.md`.")
    B("")
    B("**Status:** not yet re-checked by a second helper. **Every format tag here is rule-based** (regular expressions on the title), not a reading of the video. The hand-check below is the helper's reading.")
    B("")
    B("## How titles were tagged")
    B("")
    B("- One main format per video, from the title only (no thumbnails), following the ordered rules in `labels.md` section 3: test, X vs Y, the only X, review, myth-bust, Y doesn't want you to know, mistakes, before you do X, news-warning, cheap hack, symptom-fix, install/DIY project, how-to, explainer, story. The **first** rule that matches wins; a title that matches none is \"plain topic/other\". (The helper brief listed the formats in a different order; the labels.md order was used, as the brief asked.)")
    B("- The rules are `FORMAT_RULES` in the script. A trailing \"| channel name\" is stripped before matching. A list shape (\"Top 10\", \"5 things\") is not a format, as labels.md says.")
    B("- Thumbnail text is not read here, so a title that is only a topic label (\"Furnace Filters\") stays \"plain topic/other\" even where labels.md would read the thumbnail.")
    B(f"- **Above their search median** (a within-search relative measure): each time a video showed up in a search (with at least {MIN_SEARCH_N} kept long-form English results), did its views beat that search's median? The figure is the share of the format's appearances that did (counts in brackets). The all-videos row is the baseline (a little under 50% by construction); a format above it beats the other videos returned for the same keywords. Full definition in `keyword-sweep.md`.")
    B(f"- **Last 12 months** = age text below \"1y ago\" (approximate). {len(vs_recent):,} of {len(vs_all):,} videos.")
    B("")
    B("## Format table")
    B("")
    F.extend(format_table(vs_all, f"All time ({len(vs_all):,} videos)"))
    B("")
    F.extend(format_table(vs_recent, f"Last 12 months ({len(vs_recent):,} videos)"))
    B("")
    vh = [v for v in vs_all if v["hvac_title"]]; vhr = [v for v in vh if v["recent"]]
    B("### The same, only videos with a home-HVAC word in the title")
    B("")
    B(f"Broad EXTENDED keywords pull in many off-topic videos (games, sports, car AC, Indian-market TV). As a rough cut, this keeps only titles that pass the round 1 keyword filter (`is_hvac` in `tools/autocomplete.py`: a strong HVAC word, or a weak one plus a home word, and no excluded word such as car, game, hours, Hindi). Rule-based and strict: it also drops some on-topic titles (for example any title with \"hours\"). {len(vh):,} of {len(vs_all):,} videos pass; {len(vhr):,} in the last 12 months. The above-median share still compares each video with all the long-form English videos in its searches.")
    B("")
    F.extend(format_table(vh, f"HVAC-word titles, all time ({len(vh):,} videos)"))
    B("")
    F.extend(format_table(vhr, f"HVAC-word titles, last 12 months ({len(vhr):,} videos)"))
    B("")
    # format x framing
    B("### Which formats the keyword framings return (all time)")
    B("")
    B("Share of each keyword framing's returned videos in each format (a video counts once per framing that returned it). Framing is the keyword list's rule-based label.")
    B("")
    fr = collections.defaultdict(collections.Counter)
    for v in vs_all:
        for x in {a["framing"] for a in v["apps"]}: fr[x][v["format"]] += 1
    B("| Framing | Videos | " + " | ".join(FORMATS) + " |")
    B("|---|---:|" + "---:|" * len(FORMATS))
    for x in sorted(fr, key=lambda x: -sum(fr[x].values())):
        tot = sum(fr[x].values())
        B(f"| {x} | {tot:,} | " + " | ".join(pct(fr[x][f], tot) for f in FORMATS) + " |")
    B("")
    hc = handcheck_summary(videos, "format-handcheck-2026-10-24.csv")
    hf = handcheck_summary(videos, "format-handcheck-fresh-2026-10-24.csv")
    B("## Hand-check of the rules")
    B("")
    if not hc:
        B("not found: `data/raw/format-handcheck-2026-10-24.csv` has not been written yet.")
    else:
        B(HANDCHECK_TEXT.format(n=hc["n"], v1=hc["v1"], cur=hc["cur"], fn=hf["n"] if hf else 0, fv1=hf["v1"] if hf else 0, fcur=hf["cur"] if hf else 0,
                                gone=hc["gone"] + (hf["gone"] if hf else 0)))
        B("")
        B("First-pass disagreements in the seed-24 sample (rule tag -> my reading, count):")
        B("")
        for (a, b), n in hc["errs_v1"].most_common(): B(f"- {a} -> {b}: {n}")
        B("")
        for name, h in (("seed-24 sample", hc), ("fresh sample", hf)):
            if not h: continue
            B(f"Titles in the {name} where the current rules still disagree with my reading:")
            B("")
            B("| ID | Title | Rule tag now | My reading | Note |")
            B("|---|---|---|---|---|")
            for r in h["errs_cur"]: B(f"| `{r['id']}` | \"{md_esc(r['title'])}\" | {r['rule_now']} | {r['hand_tag']} | {md_esc(r['note'])} |")
            B("")
        B("Every row (title, first-pass rule tag, my reading, note) is in `data/raw/format-handcheck-2026-10-24.csv` and `data/raw/format-handcheck-fresh-2026-10-24.csv`.")
    B("")
    open(os.path.join(OUTMD, "formats.md"), "w").write("\n".join(F) + "\n")
    print(json.dumps(stats, indent=1))

HANDCHECK_TEXT = """**Method.** 100 videos drawn at random (Python `random.Random(24).sample` over the sorted video IDs, on 2026-10-24, from the sweep's video list before all original titles were checked; {gone} of the 150 sampled videos were later dropped as not English and are scored on their stored title). Each title was read by the helper against `labels.md` section 3, in its rule order, title only. "My reading" is a **reading**. The rules were then fixed and a **fresh** sample of 50 (seed 25, excluding the first 100) was read to see whether the fixes held on titles they were not tuned on.

| Check | Titles | Rule tag = my reading |
|---|---:|---:|
| Seed 24, first-pass rules | {n} | **{v1}** |
| Seed 24, rules after the fixes (in-sample, so flattering) | {n} | {cur} |
| Fresh sample (seed 25), rules after the first fixes (out-of-sample) | {fn} | **{fv1}** |
| Fresh sample, after four more small fixes (in-sample) | {fn} | {fcur} |

**Reading of the accuracy:** about three titles in four get the format a careful reader would give (72 of 100 first pass; 37 of 50 on the fresh sample). Treat format counts as approximate, good for spotting big differences between formats, not small ones.

**Common errors (reading):**
1. **Words that were too broad** (fixed): "troubleshooting" with no symptom read as symptom-fix; "problems" in a question ("What problems are most common...") read as symptom-fix; "avoid" ("Avoid plumber") read as mistakes; "should know" read as Y-doesn't-want-you-to-know; "prices" read as explainer; any "install" read as install/DIY project even for a small part ("How to Install a Flange Isolation Kit"); "replace an AC compressor" read as installing a whole system; "Tested & Reviews" on a best-of list read as test; "Mythbusters" missed by `myths?`.
2. **Missing cue words** (some fixed): "deception", "overlooked", "forgotten", "the foil" trick, "how warm can I get", "before trying", "filter change", "annual service". Adding "forgotten" to Y-doesn't-want-you-to-know is my reading of labels.md rule 6 ("unknown" knowledge).
3. **What a title-only rule can't see** (not fixable here): a title that only names a product ("Klein Carbon Monoxide Tester and Detector...") is a review in labels.md, but the rule needs the word "review"; stories without a first-person cue ("They Said He Wasn't built for HVAC. Now He Runs 20 Techs."); "How to heat your home" in a "101" explainer (labels.md puts how-to before explainer).
4. **Off-topic videos** (games, sports, music) get a format from stray words ("Heat vs Timberwolves" = X vs Y; "cheap and quick farm" = cheap hack). Their formats are counted but say nothing about HVAC; see the HVAC-word cut above.
5. The fresh sample also found one Indonesian title the English rule had missed; its words were added to the rule."""


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        n, seed = int(sys.argv[2]), int(sys.argv[3])
        _, _, _, videos, _, _, _ = build()
        ids = sorted(videos)
        for i in random.Random(seed).sample(ids, n):
            v = videos[i]
            print(f"{i}\t{v['format']}\t{v['title']}")
    else:
        main()
