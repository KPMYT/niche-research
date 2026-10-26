#!/usr/bin/env python3
"""Round 2 (2026-10-24) first-pass picks from the merged NexLev candidates: my readings (not measurements).
Index = position in <scratch>/candidates.json as built by r2_candidates.py. fit codes as in round 1
(HVAC, ENERGY, DIY, OUTAGE, OFFGRID, TRADE, BRAND, ADJ); '?' = decide after the channel-page pull.
audience: homeowner / trade / mixed. note: persona or background as the channel describes itself.
Usage: python3 -I r2_picks.py <scratch>  -> writes <scratch>/picks.json and <scratch>/pick_ids.txt"""
import json, sys
P = {
0:"OFFGRID|homeowner|", 1:"OFFGRID|homeowner|Cal Renner, says about forty years working (desc)", 3:"?|homeowner|Japanese-ways home channel",
8:"OUTAGE|homeowner|Harlan Pike, outage prep for over-60s (desc)", 9:"OFFGRID|homeowner|", 10:"OFFGRID|mixed|DIY heater builds",
11:"OFFGRID|homeowner|Billy Ray McCoy, sixth-generation hillbilly (desc)", 12:"OUTAGE|homeowner|", 13:"OFFGRID|homeowner|solar/off-gridder",
15:"BRAND|homeowner|contractor, Bellingham WA", 17:"HVAC|homeowner|Canadian furnace price guides", 18:"TRADE|trade|Bob, retired HVAC (desc)",
20:"BRAND|homeowner|contractor", 21:"TRADE|trade|", 22:"TRADE|trade|", 23:"BRAND|homeowner|contractor, California", 24:"TRADE|mixed|sister of HVAC Guide for Homeowners",
25:"TRADE|trade|chiller technicians", 26:"TRADE|trade|contractor business coaching", 27:"TRADE|trade|tech sales coaching", 29:"TRADE|trade|business, 30 years in HVAC (desc)",
31:"BRAND|homeowner|contractor, Utah", 34:"TRADE|trade|Walter Washington, HVAC tech", 35:"TRADE|trade|", 36:"TRADE|mixed|Chris, tech", 37:"TRADE|mixed|tech, North NJ",
38:"HVAC|mixed|", 47:"BRAND|mixed|retailer", 48:"BRAND|trade|maker, commercial", 53:"BRAND|homeowner|franchise contractor", 54:"BRAND|homeowner|contractor, Montana",
58:"BRAND|homeowner|contractor", 61:"BRAND|homeowner|contractor tips (Goettl)", 64:"BRAND|homeowner|contractor tips", 65:"?|mixed|", 66:"BRAND|homeowner|insulation contractor, Australia",
67:"HVAC|homeowner|costs, quotes, repair-or-replace (desc)", 68:"HVAC|homeowner|HVAC stories and odd facts (desc)", 71:"TRADE|trade|Ty Branaman", 75:"HVAC|homeowner|Doug Cross, buying HVAC",
78:"?|homeowner|", 82:"OUTAGE|homeowner|", 83:"OFFGRID|mixed|DIY heater builds", 84:"OFFGRID|mixed|DIY heater builds", 85:"OUTAGE|homeowner|UK preparedness, seniors",
87:"?|mixed|", 89:"HVAC|mixed|", 92:"TRADE|trade|tech GA/SC", 93:"TRADE|trade|Rolando, HVAC business owner", 94:"TRADE|trade|", 95:"BRAND|homeowner|contractor tips",
96:"HVAC|mixed|", 98:"HVAC|homeowner|DIY central AC repair", 99:"HVAC|mixed|Adam Stasevich", 100:"HVAC|homeowner|Walt Brenner, says thirty years fixing furnaces (desc)",
104:"HVAC|homeowner|Steve Nagy, contractor-reviewer", 107:"OUTAGE|homeowner|", 115:"OFFGRID|homeowner|NexLev language de; titles English", 116:"OFFGRID|homeowner|Eli persona, sells books",
117:"OFFGRID|mixed|DIY gadget builds", 118:"OFFGRID|homeowner|", 119:"OFFGRID|homeowner|NexLev language de; titles English", 120:"OUTAGE|homeowner|Ivan persona", 121:"OUTAGE|homeowner|Gary Miller persona, immigrant (desc)",
122:"OUTAGE|homeowner|Hank Dockery persona", 130:"BRAND|homeowner|contractor", 131:"HVAC|mixed|", 135:"BRAND|homeowner|contractor, DFW", 137:"TRADE|trade|HVACJess", 138:"HVAC|homeowner|",
142:"TRADE|trade|Hunter, 25, HVAC business owner", 148:"OFFGRID|homeowner|forgotten domestic engineering", 151:"OUTAGE|homeowner|Emmett Boone, prepping since 2011 (desc)", 152:"?|homeowner|",
160:"BRAND|homeowner|contractor learning center", 165:"?|mixed|", 173:"BRAND|trade|maker training (Lennox)", 174:"TRADE|trade|Adrian, HVACR contractor, South Texas",
176:"HVAC|homeowner|Earl, bought a fixer-upper 32 years ago (desc)", 178:"HVAC|mixed|Brian the HVAC Guy", 179:"TRADE|trade|", 181:"TRADE|trade|21-year service tech (desc)", 182:"?|mixed|", 184:"?|mixed|",
188:"BRAND|trade|distributor", 192:"BRAND|homeowner|boiler maker, UK", 193:"BRAND|homeowner|maker", 195:"ENERGY|homeowner|Reid, investigates the green energy industry (desc)", 198:"TRADE|trade|",
203:"BRAND|homeowner|contractor", 204:"BRAND|trade|maker, commercial", 207:"HVAC|mixed|", 214:"BRAND|homeowner|maker", 215:"BRAND|homeowner|contractor", 216:"BRAND|homeowner|maker (indoor air)",
221:"BRAND|homeowner|veteran-owned contractor", 222:"TRADE|trade|load calculations", 226:"BRAND|trade|controls distributor", 228:"HVAC|homeowner|", 229:"HVAC|homeowner|",
230:"?|homeowner|", 231:"HVAC|homeowner|Frank, maintenance man persona", 234:"HVAC|homeowner|Leroy Bell, says veteran HVAC technician (desc)", 235:"TRADE|trade|",
236:"HVAC|homeowner|Vern Holt persona", 237:"?|homeowner|", 239:"?|mixed|", 240:"OFFGRID|homeowner|Del Rasmussen, Minnesota farmhouse (desc)", 241:"?|homeowner|", 243:"?|homeowner|",
246:"TRADE|trade|HVAC and building engineering explainers", 248:"OFFGRID|mixed|DIY gadget builds", 259:"OUTAGE|homeowner|Linda Fairbrook persona", 260:"?|homeowner|Tennessee DIY",
262:"OFFGRID|homeowner|Jake Holloway persona, wood stove", 267:"?|homeowner|brand-quality expose", 271:"OUTAGE|homeowner|Kate Sullivan, women living alone", 276:"TRADE|mixed|E, 20-year-old tech",
277:"?|mixed|", 279:"HVAC|homeowner|Earl Whitaker persona", 281:"BRAND|trade|motor supplier", 282:"ENERGY|homeowner|home performance, building science", 284:"?|mixed|",
285:"TRADE|trade|Drew, HVAC company owner", 287:"BRAND|homeowner|mini-split maker", 288:"BRAND|trade|contractor", 290:"HVAC|homeowner|DIY AC repair", 291:"TRADE|trade|",
293:"?|mixed|maintenance show", 302:"?|homeowner|", 304:"BRAND|homeowner|contractor, San Diego", 305:"BRAND|mixed|equipment brand", 307:"?|homeowner|1950s working man persona",
310:"BRAND|homeowner|contractor, Kansas City", 312:"BRAND|homeowner|One Hour GM", 315:"HVAC|homeowner|Dale Kirkwood, says retired heating engineer, UK (desc)", 317:"?|homeowner|",
318:"?|homeowner|Yorkshire Dales persona", 326:"BRAND|homeowner|mini-split installer", 328:"OFFGRID|homeowner|waste-to-heat builds", 329:"?|homeowner|", 330:"?|homeowner|",
335:"OFFGRID|homeowner|", 336:"ENERGY|homeowner|UK couple, heat pump", 342:"?|homeowner|", 343:"OUTAGE|homeowner|Mason Reed persona", 344:"HVAC|homeowner|plain-language house explainers",
348:"?|homeowner|", 353:"?|trade|sheet-metal duct fabrication", 356:"TRADE|trade|", 357:"TRADE|trade|MEP training", 358:"BRAND|homeowner|contractor, Canada", 359:"?|homeowner|",
360:"BRAND|homeowner|home warranty", 362:"TRADE|trade|Mikey Pipes", 367:"?|homeowner|", 370:"ENERGY|homeowner|firewood and wood heat", 372:"HVAC|homeowner|",
383:"?|homeowner|", 384:"?|homeowner|", 386:"?|homeowner|", 387:"?|homeowner|", 392:"?|homeowner|", 393:"?|homeowner|",
1390:"?|homeowner|", 648:"?|homeowner|", 649:"?|homeowner|", 1985:"?|homeowner|", 510:"?|homeowner|", 602:"?|homeowner|", 1170:"?|homeowner|", 1347:"?|homeowner|",
645:"?|homeowner|", 495:"?|homeowner|", 641:"?|mixed|", 1884:"?|homeowner|Wade, property manager persona", 638:"?|homeowner|", 642:"?|homeowner|", 1774:"?|homeowner|",
1453:"?|homeowner|", 1547:"?|homeowner|", 1439:"?|homeowner|", 1414:"?|homeowner|", 1421:"?|homeowner|", 656:"?|homeowner|", 1464:"?|homeowner|Hank Ross, seventy, off grid (desc)",
660:"?|homeowner|Gus Halvorsen persona", 504:"?|homeowner|Caleb Vance, old-school living", 502:"?|homeowner|", 1499:"?|homeowner|", 463:"?|homeowner|", 1319:"?|homeowner|", 490:"?|homeowner|",
1336:"?|homeowner|", 1340:"?|homeowner|", 1124:"?|homeowner|Ralph Harmon persona", 892:"?|homeowner|", 1968:"?|homeowner|", 521:"?|homeowner|", 1525:"?|homeowner|", 1538:"?|homeowner|",
410:"?|homeowner|Lars Halvorsen persona", 411:"?|homeowner|Harlan Sawyer persona", 427:"?|homeowner|Edna Mullins persona", 417:"?|homeowner|", 1523:"?|mixed|", 743:"?|homeowner|",
}
# channels found only by NexLev youtube_search (type=channel), 2026-10-24
YT = {"UCRzYyjFeCxMcrLf3kTnXXGw":("Home Owner's Guide to HVAC","?|homeowner|"), "UCDx7t_XxrIcwRU9DOmJqToA":("Rosa The Female HVAC Tech","?|mixed|Rosa, says EPA-certified HVAC tech (desc)"),
 "UCnArHdlfu6zzw4-zcMO-Y3A":("True HVAC Tips Official","?|mixed|"), "UC26Yh-JM4e4uANRStSRD2Qg":("The Homeowner's HVAC Blueprint","?|homeowner|Chris (desc)"),
 "UCFdB_qR3qdbNHBOzYrSBGdQ":("The HVAC Veteran","?|homeowner|JC, says 25 years in the industry, Ontario (desc)"), "UCte3kAK7XQjgOQGLUUk76Tw":("Gene DeJoannis","?|homeowner|retired HVAC engineer, New England (desc)"),
 "UCDHYnOLW4H9kZqdH8cofn7Q":("Kevin Jones","?|mixed|facilities and home maintenance"), "UCjeQYgDBpYQmIdVidExgxGQ":("Hamel's Air Conditioning & Heating","?|homeowner|contractor, 'exposing HVAC scams' (desc)"),
 "UCSvkdsbJ5f2R3sUY2_mL3-Q":("Conditioned Air Secrets","?|homeowner|"), "UCCsYuH_X4PX_mBBLwhKlCxw":("AC Install Hub","?|mixed|"), "UCAdFjmRMULgz3aGszCKenFA":("The Air Conditioning Guy","?|mixed|residential HVAC installer"),
 "UCBp4rUJw33bk_InU0pOrACQ":("City Home Comfort","?|homeowner|contractor, Toronto"), "UC7koRnCCM5txOF-eNIcK22A":("Tru Comfort HVAC Reno","?|homeowner|contractor, Reno")}
sd = sys.argv[1]
c = json.load(open(sd + '/candidates.json'))
known = set(json.load(open(sd + '/known.json'))['ids'])
picks = {}
for i, v in P.items():
    e = c[i]; f, a, n = v.split('|', 2)
    picks[e['cid']] = {"idx": i, "name": e['name'], "fit": f, "audience": a, "note": n, "src": "nexlev"}
for cid, (name, v) in YT.items():
    if cid in known: print('known already:', name); continue
    f, a, n = v.split('|', 2)
    picks.setdefault(cid, {"idx": None, "name": name, "fit": f, "audience": a, "note": n, "src": "nexlev youtube_search (type=channel)"})
json.dump(picks, open(sd + '/picks.json', 'w'), indent=1)
open(sd + '/pick_ids.txt', 'w').write('\n'.join(picks) + '\n')
print(len(picks), 'picks;', sum(1 for p in picks.values() if p['fit'] == '?'), 'to decide')
