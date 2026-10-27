#!/usr/bin/env python3
"""Round 2 (2026-10-24) second-pass decisions, made after the channel-page pull (r2_pages_summary.py).
My readings. Sets fit for the '?' picks and drops picks that turned out off-topic, short-form or unloadable.
Usage: python3 -I r2_decide.py <scratch> -> writes <scratch>/kept.json and <scratch>/dropped.json"""
import json, sys
sd = sys.argv[1]
picks = json.load(open(sd + '/picks.json')); pages = json.load(open(sd + '/pages_summary.json'))
SET = {  # name: fit|audience|note
 "TheAirConditionerGuy": "ADJ|mixed|vintage air conditioner and fan collector",
 "Tactical Psychology": "OUTAGE|homeowner|", "David Jones": "HVAC|mixed|", "Joe Tollari": "HVAC|mixed|sheet-metal and duct work",
 "The House Papers": "HVAC|homeowner|warranty and brand-verdict explainers", "Dale Prosser": "HVAC|homeowner|",
 "AEPowerHouseTV": "ENERGY|homeowner|utility-sponsored TV programme (Alliant Energy)", "The Lovely Place": "DIY|homeowner|Tennessee DIY, wood stove installs",
 "Quality Rot": "ADJ|homeowner|'everything is getting worse' brand verdicts (appliances, homes, AC)", "AC Professor": "HVAC|homeowner|",
 "Forever Tech English": "TRADE|mixed|AC and appliance circuit-board repair", "Lex Vance": "HVAC|mixed|The Dirty Maintenance Show (apartment maintenance)",
 "Flannel Guy DIY": "DIY|homeowner|Eric, DIY tutorials", "Stay Ready. Urban Survival.": "OUTAGE|homeowner|urban survival, Los Angeles",
 "Homeowner Money": "HVAC|homeowner|repair-or-replace and quote math", "ecophage": "OFFGRID|homeowner|ChrisB, pellet and rocket stove builds",
 "Zach Of All Trades": "OUTAGE|homeowner|preparedness", "Wonders": "ADJ|homeowner|'forgotten household wisdom', grandma hacks",
 "Budget Phil": "DIY|homeowner|making, fixing, cleaning", "BIG TICKET TRUTH": "ADJ|homeowner|big-ticket brand verdicts (mowers, generators, HVAC)",
 "The Technician’s Blacklist": "HVAC|homeowner|appliance and AC 'secret' tricks", "Wade Corbin": "OUTAGE|homeowner|says his house is last on the power line (desc)",
 "INDOOR AIR QUALITY": "HVAC|mixed|furnace parts troubleshooting, many short videos", "The Outspoken Engineer": "HVAC|mixed|Jacob Swei, UK, air-to-air heat pump reviews",
 "Off-Grid Blueprint": "OFFGRID|homeowner|Wade, property manager (desc)", "Blueprint Archive": "HVAC|homeowner|",
 "Jack Miller": "ADJ|homeowner|appliance and heat-pump tips, then rancher stories", "Patina": "ADJ|homeowner|Japanese home ways",
 "Forgotten Appalachian Skills": "OFFGRID|homeowner|Appalachian old ways", "Forgotten American Survival": "OUTAGE|homeowner|'poor man' blackout and off-grid tricks",
 "Gus Halvorsen": "OFFGRID|homeowner|Gus Halvorsen persona", "Caleb Vance": "HVAC|homeowner|Old-School Living with Caleb Vance",
 "Forgotten American Homes": "OFFGRID|homeowner|before air conditioning and central heating (desc)", "Hidden Passive Tech": "OFFGRID|homeowner|",
 "Eli's Plain Heat": "OUTAGE|homeowner|Eli persona, heat without power", "Wade Caudill": "OFFGRID|homeowner|Appalachian heat-and-home tricks",
 "Lost Methods Archive": "OFFGRID|homeowner|forgotten household methods", "Hidden Systems": "OFFGRID|homeowner|rocket mass heaters, wood heat systems",
 "Ray Holton Secrets": "OFFGRID|homeowner|", "Lars Halvorsen": "OFFGRID|homeowner|Lars Halvorsen persona, Norwegian wood heat",
 "Harlan Sawyer": "ENERGY|homeowner|Harlan Sawyer persona, firewood and wood stoves", "Darrin Stevenson": "OFFGRID|homeowner|says 26 years with a police department (desc)",
 "The Sensei's Home": "OFFGRID|homeowner|Japanese household ways", "Rosa The Female HVAC Tech": "TRADE|mixed|Rosa, says EPA-certified HVAC tech (desc)",
 "The HVAC Veteran": "HVAC|homeowner|JC, says 25 years in the industry, Ontario (desc)", "Kevin Jones": "DIY|mixed|facilities and home maintenance",
 "Conditioned Air Secrets": "HVAC|homeowner|", "The Air Conditioning Guy": "TRADE|mixed|residential installer, San Diego area",
}
DROP = {  # name: reason
 "The Japanese Method": "decluttering channel; no heating or cooling videos in 30 loaded", "The HVAC Maven": "all videos under 2 minutes",
 "Smart AC Solutions": "all loaded videos under 5 minutes", "Talyn875": "Videos tab did not load; not checked", "HowtoDoit": "no HVAC videos in 30 loaded",
 "Sobrevivência Oculta": "mixed Portuguese and English titles", "Harold's Forgotten Trade": "old-home nostalgia; 2 of 37 heating/cooling",
 "Mr. Hardware": "general DIY; 1 heating-related video", "Arthur Whitfield": "pest and cleaning hacks", "Marlowe Beck": "general hacks",
 "Frugal Picks": "TV and appliance brand verdicts; no HVAC", "Lyle Danforth": "general engineering explainers", "Forbidden Vault": "mostly fuel-additive 'hacks'",
 "MetalCraftLab": "metal crafts, Ukraine", "Home Rapid Repair": "mostly short general repairs", "Modern Decay": "generator reviews (out of scope, operator 2026-10-23)",
 "FixVault": "general hacks", "Consumer Truth": "grocery", "Brand Meter": "clothing", "Industrial Decay": "appliance brand verdicts; 1 of 44 HVAC",
 "The Rot Report with Dave": "mower brand verdicts", "Don't Call The Pro": "appliances, pest", "Infinity Inventor": "gadget and remote-control hacks",
 "Prepper Pulse": "food and water prep; 1 heat video", "Future Proof Survival": "general prepping; 2 of 59 heat", "BuriedFix": "power gear (inverters, batteries)",
 "Hank Off Grid": "off-grid relocation; 3 of 52", "United States Home Services": "all videos under 1 minute", "Home Tips Daily": "hydrogen peroxide hacks",
 "Simply Filters": "all videos under 2 minutes", "Ralph Harmon": "backup-power products for food", "Fair & Square": "groceries and prep",
 "Pitch Evidence": "mostly football news", "Granny Edna": "homestead cooking", "Fixit Mr.K": "plastic recycling crafts",
 "Home Owner's Guide to HVAC": "3 videos; Videos tab did not load", "True HVAC Tips Official": "Videos tab did not load", "The Homeowner's HVAC Blueprint": "Videos tab did not load",
 "Gene DeJoannis": "1 video", "Hamel's Air Conditioning & Heating": "short promos", "AC Install Hub": "all videos under 3 minutes",
 "City Home Comfort": "1 short video loaded", "Verlorenes Bauwissen": "German channel: thumbnails in German, NexLev language de; English titles are YouTube auto-translations (my reading)", "Naturpfad": "German channel: thumbnails in German, NexLev language de; English titles are YouTube auto-translations (my reading)", "Tru Comfort HVAC Reno": "short promos",
 "DeHart Plumbing Heating & Cooling": "Videos tab did not load", "One Hour Heating & Air Conditioning": "no long-form HVAC videos loaded",
 "Anthony Plumbing, Heating, Cooling & Electric": "no long-form HVAC videos loaded", "AmeriTech Air Conditioning and Heating": "no long-form videos loaded",
 "Della": "no long-form videos loaded", "Dick Ray Plumbing Heating and Cooling": "no long-form videos loaded",
 "TRANE EMEA": "1 long-form video, commercial", "Trane Commercial HVAC North America": "commercial; 2 long-form HVAC of 58",
 "United Refrigeration Inc.": "distributor; 1 long-form HVAC", "Wm.T.Spaeder": "1 long-form HVAC", "Affordable Comfort": "1 long-form HVAC",
}
kept, dropped = {}, {}
for cid, p in picks.items():
    n = p['name'].strip()
    if n in DROP: dropped[cid] = dict(p, reason=DROP[n]); continue
    if n in SET:
        f, a, note = SET[n].split('|', 2); p = dict(p, fit=f, audience=a, note=note or p['note'])
    if p['fit'] == '?': dropped[cid] = dict(p, reason='not decided'); continue
    kept[cid] = p
json.dump(kept, open(sd + '/kept.json', 'w'), indent=1); json.dump(dropped, open(sd + '/dropped.json', 'w'), indent=1)
print(len(kept), 'kept;', len(dropped), 'dropped')
for cid, p in dropped.items():
    if p['reason'] == 'not decided': print('UNDECIDED', p['name'])
