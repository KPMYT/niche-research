import re, os
S = "/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/"
t1 = open(S + "tables.md").read(); t2 = open(S + "tables2.md").read()
def sec(txt, head, nxt=None):
    a = txt.index(head) + len(head)
    b = txt.index(nxt, a) if nxt else len(txt)
    return txt[a:b].strip()
pool = sec(t1, "## pool", "## funnel")
perkw = sec(t1, "## per keyword")
top20 = sec(t2, "## top20 heat\n", "## top20 heat US-listed")
top20us = sec(t2, "## top20 heat US-listed", "## recent top10\n")
rec10 = sec(t2, "## recent top10\n", "## channels")
rec10us = sec(t2, "## recent top10 US-listed", "## check")
check = sec(t2, "## check").rsplit("\n", 1)[0]
TYPES = {
 "Mikey Pipes - Pipe Doctor Plumbing & Heating & Air": "on camera",
 "steven lavimoniere / PLUMBING HEATING & AC VIDEO'S": "on camera (job footage; no face in the 2 thumbnails checked)",
 "This Old House": "on camera (TV show)",
 "The DIY Guy": "on camera", "Heating Help": "faceless (diagrams)", "dereton33 Plumbing and heating, DIY and blogging.": "faceless (job footage, text)",
 "Heatable": "on camera", "Boiler Room Detective": "faceless (text cards; illustrated mascot man)", "plumberparts": "on camera",
 "Allen Hart": "on camera", "grayfurnaceman": "faceless (job footage)", "Silver Cymbal": "faceless (hands and equipment)",
 "Skill Builder": "on camera", "Heat Geek": "on camera", "BobsPlumbingVideos": "on camera", "askmediy": "on camera",
 "How2D2": "faceless (diagrams)", "Proper DIY": "faceless (hands)", "Fix It With Zim": "faceless (text and equipment)",
 "K. S. Engineering and Exeter City Council": "faceless (hands)", "AC Service Tech LLC": "on camera",
 "Handyman Hints": "faceless (text slides)", "Arthur Weber": "faceless persona (AI old man)",
}
def addtype(tbl):
    out = []
    for l in tbl.split("\n"):
        if l.startswith("| Channel |"): out.append(l + " Type (my reading) |"); continue
        if l.startswith("|---"): out.append(l + "---|"); continue
        name = l.split("|")[1].strip()
        out.append(l + f" {TYPES.get(name, 'not checked')} |")
    return "\n".join(out)
bycount = addtype(sec(t2, "### by count", "### by views"))
byviews = addtype(sec(t2, "### by views", "### recent channels"))
recch = addtype(sec(t2, "### recent channels (last 12 mo uploads in pool) by count", "## all recent heat"))
faceless = open(S + "faceless.md").read().strip()
tpl = open(S + "report_tpl.md").read()
for k, v in dict(POOL=pool, PERKW=perkw, TOP20=top20, TOP20US=top20us, REC10=rec10, REC10US=rec10us, CHECK=check, BYCOUNT=bycount, BYVIEWS=byviews, RECCH=recch, FACELESS=faceless).items():
    tpl = tpl.replace("{{" + k + "}}", v)
assert "{{" not in tpl
os.makedirs("/home/user/niche-research/studies/hvac/round2", exist_ok=True)
open("/home/user/niche-research/studies/hvac/round2/old-house-heat.md", "w").write(tpl)
print(len(tpl))
