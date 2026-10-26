#!/usr/bin/env python3
"""Build the round 1 channel-finds table (2026-10-23).
Joins: YouTube About panels + Videos tab (raw/channel-finds-pages-2026-10-23/), the YouTube search sweep
(raw/channel-finds-ytsearch-2026-10-23*.json), and the NexLev pulls (raw/channel-finds-nexlev-2026-10-23.json).
The ANN table below is the helper's reading (fit, audience, persona, topics, type where it comes from a thumbnail
look); everything numeric comes from a tool result.
Usage: python3 -I channel_finds_build.py  -> writes raw/channel-finds-round1.csv and prints markdown rows."""
import json, re, csv, os, sys

RAW = "/home/user/niche-research/studies/hvac/data/raw"
PAGES = RAW + "/channel-finds-pages-2026-10-23"
NEX = json.load(open(RAW + "/channel-finds-nexlev-2026-10-23.json"))
about = json.load(open(PAGES + "/about.json"))
sw = [r for r in json.load(open(RAW + "/channel-finds-ytsearch-2026-10-23.json"))["rows"]]
sw += [r for r in json.load(open(RAW + "/channel-finds-ytsearch-2026-10-23-run1.json"))["rows"] if r["sort"] == "views"]

KW = re.compile(r"(hvac|furnace|heat pump|\bac\b|a/c|air condition|thermostat|boiler|radiator|ductless|ductwork|air ducts?|duct clean|mini.?split|insulat|drafts?\b|draughts?|heating|heat bill|electric bill|power bill|energy bill|cooling|cools?\b|cooler|dehumid|humidi|refrigerant|freon|capacitor|filters?\b|power outage|power goes out|blackout|no power|warm|attic|weatherstrip|propane|wood stove|firewood|heater|no heat|cold room|hot room|hottest room|hot house|free heat|heat (your|a|any|the) (home|house|room)|55.?f|air purif|heats?\b)", re.I)

NEG = re.compile(r"(\bcar\b|car's|recessed|doorbell|water heater|hardwood|generator|tankless|#(?!\d)\w|jeep|dodge|shop vac)", re.I)

def secs(t):
    if not t: return 0
    try:
        s = 0
        for x in t.split(":"): s = s * 60 + int(x)
        return s
    except Exception: return 0

def num(v):
    if v is None: return None
    if isinstance(v, (int, float)): return int(v)
    m = re.match(r"([\d.,]+)\s*([KMB]?)", str(v).strip())
    if not m: return None
    n = float(m.group(1).replace(",", ""))
    return int(n * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])

# ---------- helper's reading per channel ----------
# fit: HVAC = HVAC for homeowners is the main subject; ENERGY = bills/insulation/building science/heating fuels;
# OUTAGE = keeping warm in outages / prepper heat; OFFGRID = "forgotten / banned" heating-cooling hacks;
# DIY = general home DIY with HVAC as a side topic; TRADE = aimed at technicians; BRAND = company / maker / retailer;
# ADJ = adjacent (appliances, home systems, one-off HVAC hits)
# type: None = take NexLev's flag; otherwise the reading given (source stated in the string)
P = "faceless persona (AI-image presenter; my reading of thumbnails)"
FO = "faceless (AI-image objects/diagrams, no presenter; my reading of thumbnails)"
OC = "on camera (my reading)"
ANN = {
# cid: (fit, audience, type or None, persona / claimed background, main topics)
"UCvcKEgZcY9ZgEULZouaNAOA": ("HVAC","homeowner",P,"Ray Dutton, 'retired HVAC pro', 25 years; sells 'HVAC Survival Guide' e-book","seasonal AC/heat shutdown-startup, thermostat habits, filters, 'companies don't want you to know'"),
"UCZ1IwSV46bb09fMvqHn6_2A": ("HVAC","homeowner",FO,"none named; 'real research, no contractor kickbacks'","brand verdicts, filters, refrigerant bans, industry exposes"),
"UCOyYTw-deou3ax6gvCmX2dg": ("HVAC","homeowner",FO,"'John', 'years around HVAC systems'","maintenance 'do THIS once a month', brands, hydrogen peroxide hacks"),
"UCQCRIhHQ__ncUxtOHiIXI4A": ("HVAC","homeowner",FO,"none named; sells 'Fall Changeover Field Manual'","'secret AC tricks only 1% of techs know', maintenance"),
"UCgFpqO9vKw4HvjhnN6moalQ": ("HVAC","homeowner",P,"'Mike'; sells 'The Real HVAC Guide' (payhip)","brand lists, 'things AC companies don't want you knowing'"),
"UCczJ6EU5aLBogQOzFZ_W0HQ": ("HVAC","homeowner",None,"none; 'independent, data-driven investigation'","brands, refrigerant, filters, contractor exposes"),
"UCTDbUAjE9Ab_wwvuV7cgtvQ": ("HVAC","homeowner",FO,"none named","brand verdicts (AC, water heater, mini-split), filters"),
"UC5NJ3yYhsZFkfWLJJJVoxMA": ("HVAC","homeowner",P,"Hank Cole, 'forty years in heating and cooling'","cheap AC fixes, hottest room, 1950s cooling"),
"UCt47_v_207fZOLrHhwXpIdA": ("HVAC","homeowner",None,"none (same description text as Vent Exposed)","window vs mini-split vs central cost, insulation, filters"),
"UCLdI4EbF3WcHS_oyhjSvwDw": ("HVAC","homeowner",P,"none in description; older-man AI character in thumbnails","thermostat myths (heat up/down), outage heat"),
"UC2w60mhlxFmAhoi2oSDcEng": ("HVAC","mixed","on camera (NexLev: not faceless)","Dave, HVAC tech; sells equipment via affiliate code","outage heat, DIY installs, capacitors, contractor secrets, power stations"),
"UCp_5AZlvvW9jn6L4EZuCbNQ": ("HVAC","homeowner","on camera (NexLev check: not faceless)","New HVAC Guide; buying guidance, financing, contractor mastermind","winter mistakes, contractor secrets, ductwork, thermostats, refrigerant news"),
"UCekKmUEJxBRx5tI1tUyHOqA": ("HVAC","homeowner",OC,"DIY repair host (not stated)","AC/furnace won't turn on, freon level, water heaters"),
"UCOZR-1IqsAer9wzlvFgb4mA": ("TRADE","mixed",OC,"HVAC tech/contractor","refrigerant charging, mini-split installs, pilot lights, step-by-step"),
"UCdLlUhD9LUGm0-NTYDASPFA": ("TRADE","trade",OC,"Bryan Orr; 'for techs, by techs'","refrigeration cycle, evacuation, electrical basics"),
"UCchpiPYTBEg4DpK6mKfYi2A": ("HVAC","mixed",OC,"'HVAC serviceman and instructor, 35 years'","furnace won't start, pilot, pressure switch"),
"UC2AsqyR6xLMkte3mQHf-umw": ("TRADE","mixed",OC,"family HVAC company, middle TN","ductless failures, fabrication, installs"),
"UCiz21FXLOV65NTgiUfJsxTg": ("TRADE","trade",OC,"'HVAC GUY', instructs technicians","service calls, heat pumps, humidity"),
"UCjKCB2ujHpe0mYEKhKVe3Aw": ("BRAND","mixed",OC,"Sacramento HVAC company","compressor diagnosis, refrigerant, coils"),
"UCFxf3hjNRSQ706L3jgDYnBw": ("HVAC","mixed",OC,"Ted Cook, veteran tech; 'leave HVAC to the pros'","hack-job installs, scams, coil cleaning"),
"UCtjmjQ_lBAg-XdoT1MJgdTQ": ("TRADE","trade",OC,"Indian AC technician","split AC service, wiring"),
"UC-MsPg9zbyneDX2qurAqoNQ": ("TRADE","trade",OC,"Gary McCreadie, field tech (Canada)","3-phase, superheat, commercial"),
"UCWtuOnlW7BeXLgr6M1_Z49g": ("HVAC","homeowner","on camera (NexLev check: not faceless)","Atlas AC Repair, Texas HVAC company","AC brands, stages, filters, sizing"),
"UCXuC2KTVSVH7sS7bNkirRZQ": ("HVAC","homeowner",OC,"residential HVAC company; 'tips that can save you money'","AC not cooling, freeze-ups, dampers, filters"),
"UCpSSopClZmwUZ-TrGgJ4z-w": ("TRADE","trade",OC,"NYC/Long Island tech, 15+ years","thermostat wiring, commercial troubleshooting"),
"UCOtjEgHlsAxG0YNzaSVIOgw": ("BRAND","homeowner",OC,"OKC HVAC & plumbing company","best/worst AC and mini-split brand rankings, staging"),
"UCAiLfdXEsKVOAarqANjSweQ": ("BRAND","homeowner",OC,"plumbing/HVAC company","heat pump pros/cons, tankless"),
"UC0FlY2puWKptIB7yZ_riKBg": ("HVAC","homeowner","not faceless per NexLev check (presentation not viewed)","none named","brands worth buying, filters, window vs mini-split vs central"),
"UCmjXrFek17Xf3QU1GUiHMQQ": ("HVAC","homeowner",P,"Frank Coyle, 'retired HVAC pro', 28 years at the big companies (old 2007 account repurposed)","thermostat mistakes, 'what techs don't want you to know'"),
"UCimosvXXx33o2BIrEpMQQ-g": ("HVAC","homeowner",None,"Spanish-language homeowner AC help, also English titles","'before turning on your heater', thermostat habits, tech secrets"),
"UCk_Epq89IzNRDJDLvlnS9rg": ("TRADE","mixed",OC,"field tech, 'real service calls'","angry-customer service-call stories"),
"UCqCz10_64ISJCoc1xV1a8-w": ("ADJ","homeowner",P,"Walt Brandt, 40 years fixing appliances","water heaters, dishwashers, fridges worth buying"),
"UCMDHm9pBWFY8r1NUkyWxPBw": ("HVAC","homeowner",None,"Raymond Whitaker, 'retired handyman'; sells a guide","AC units he'd buy, coil cleaning, mini-split brands"),
"UC7XxBUQRmL32Kzr5ozkNfLg": ("ENERGY","homeowner",None,"none","attic cooling, ventilation, attic fans to avoid"),
"UCbLxS9ZtFptl1rHVYn9oouA": ("HVAC","homeowner",None,"none; 'your contractor won't tell you'","HVAC failure, filters, sewer relining"),
"UC7LoJyDWLZg9mb9V5FV4UNQ": ("HVAC","homeowner",P,"Gord, '30 years fixing things in people's homes'","AC upgrades, hydrogen peroxide/outlet 'don't want you to know'"),
"UCqCKKYsi9U37xNIBgOZdflg": ("HVAC","homeowner",None,"'a retired HVAC pro' (unnamed)","furnace before first cold night, thermostat settings, storms"),
"UChM1RxTctTXapgVSLqIh1uA": ("HVAC","homeowner",None,"none in description","no-heat checks, night setback, winter trips"),
"UCaT_bPLxSEi3krSWoAvigMQ": ("HVAC","homeowner",P,"Nick Salermo, grandfather's notebooks","AC mistakes HVAC companies hope you keep making, off-grid water"),
"UCWWquw3-kxz-OhjepFUqj_g": ("HVAC","homeowner",P,"none in description; aimed at 'seniors over 55'","furnace filter, warning signs for seniors, water heaters"),
"UCyYzJxK_6DMvIgqSpR2zN6Q": ("HVAC","homeowner",P,"Earl Lindgren, 45 years with furnaces","heat loss, furnace before cold night, thermostat"),
"UCrMC4iG9qnvyAvOG3okKb0g": ("ENERGY","homeowner",P,"Walt Harmon, 38 years a home inspector; 'over 65'","winter checks, drafts, radon, sump pump"),
"UC_ihL-pHoRfwYNHW_OZSniQ": ("ENERGY","homeowner",P,"Dale, retired, 'furnaces, wiring and drafty old houses'; 'over 60'","window film, blackout numbers, thermostat"),
"UC-fWFS7gBfkP-wSUORdeLAg": ("HVAC","mixed","faceless per NexLev check; text thumbnails (my reading)","Dave Hartzell, Oklahoma, 47 years HVAC (company channel)","story-style repair lessons, geothermal, airtight homes"),
"UCgYEaHGOU2bAIj9QgBsDkJQ": ("HVAC","homeowner",P,"Shaun Meeker, early 60s, 30 years a general contractor","AC fall shutdown, techs don't want you to know"),
"UCCnMC8LKp3qS2rkJ5O0xtXQ": ("OUTAGE","homeowner",None,"none; blackout preparedness, seniors living alone","blackout meals, keep warm when furnace dies"),
"UCfTHtV7bx4xgDjpZHxbieHQ": ("HVAC","homeowner",None,"none","zoning, SEER 'scams', buying mistakes"),
"UCq9F4BKWrOtnUYuzePEhkJQ": ("OUTAGE","homeowner",None,"none","winter survival, blackout tips, scams"),
"UC7xrSTuKm8YPd2l6WPgMt-g": ("ADJ","homeowner","faceless (NexLev check 99%)","none (old 2007 account)","'things X don't want you to know about hydrogen peroxide' incl. HVAC"),
"UCPba1zh0V9QQAVju7D--SzA": ("ENERGY","homeowner",P,"'Earl' (no description); older-man AI character","window heat trick, free cooling fan, Canadian well, hydrogen peroxide"),
"UCkHDMmVa2MkgKdK7B05s9dQ": ("ADJ","homeowner",P,"'Bertha', Mexican-mother home hacks","hydrogen peroxide/foil hacks, Dollar Tree before winter"),
"UCEInLGzWBsSsI5UVb4NowUQ": ("ENERGY","homeowner",P,"Donna, 67, kept 400 Chicago apartments warm for 41 years","living alone in winter after 60, free home repairs, electric bill"),
"UCN-fPt8rIaXt2h37qZZLR-w": ("HVAC","homeowner",None,"Gus Hollis, 41 winters fixing pipes and furnaces in Vermont","heating bill tricks, blackout, drafty windows"),
"UCJYXqMeVdMG6m_b1a9cyCFA": ("ENERGY","homeowner",None,"none","attic fan/vent tricks, condenser tricks"),
"UCUBvvBHGf6WOlc1MVfoZdZQ": ("ENERGY","homeowner",None,"Hollis, Maine; heats with wood","firewood seasoning, wood-heat mistakes"),
"UCmWhnLZQDqHbZ7HO6t9NhmQ": ("OFFGRID","homeowner",FO,"Amish-community framing ('Eli Yoder')","'$300 tunnel keeps home 55F', hydrogen peroxide, engines"),
"UCMAmymzGNS1CE07KOwUWCNA": ("OFFGRID","homeowner",FO,"Amish-community framing ('Eli Yoder')","underground cooling pipe, salt-bucket heat, alternator power"),
"UCZC0peuG11nBp0GculOqulw": ("OFFGRID","homeowner",FO,"'Eddie'","banned cooling tunnel/pipe, free AC"),
"UCanuLFQFuNBSYHqNvqHIpdA": ("OFFGRID","homeowner",FO,"none","$0-to-heat homes 'banned', mold, rust"),
"UCCPCEUtao-g9_iWYyfF-B1w": ("OFFGRID","homeowner",P,"older-man AI character; sells 'senior prep' book","salt bucket room heat 'why don't seniors', sand-to-stone"),
"UCIHN6eDQGhfblRdhqNHgaKA": ("ENERGY","homeowner","faceless persona (illustrated woman, AI art; my reading)","woman 'at 52' bringing back grandmothers' habits","1970s winter heating habits, grocery habits"),
"UCVkVhwXnattecHEyw7xSIJA": ("ENERGY","homeowner",P,"none named; 'frugal, self-reliant home methods'","AC bill fixes 1950s houses knew, attic, Canadian well"),
"UC_nd6NX_6D52OL4qFWVFbnQ": ("OFFGRID","homeowner",FO,"description is for 'John The RV Guy' (pivoted channel)","NASA insulation trick, attic mesh, inverters"),
"UCzHCjjAcD9XNGUCEhKKKVkQ": ("OFFGRID","homeowner",FO,"none; 'hidden physics' of passive cooling","attic foil, window screens, $5 AC"),
"UCE3DzKfdkEEf3kwQYPqcJFA": ("ENERGY","homeowner","faceless (AI-image scenes; my reading)","none","old-house designs that stayed cool, basements, crawlspaces, ventilation"),
"UCHN7pq3IboX6lTsWTTDPICg": ("OFFGRID","homeowner",None,"none","attic foil, 2-wall heat system, window panels"),
"UCgiAu709SKq9GOQICPzffgQ": ("ENERGY","homeowner",None,"Walter Northwood, northern farm-family ways","attic/basement tricks to cut heating bills, shed heater"),
"UCzJUR7biTTdJoizeIAWtTNA": ("HVAC","mixed",OC,"HVAC tech (not stated in description)","AC fan not spinning, thermocouples, boilers"),
"UCSedPjb56LMeiq_VV8164OA": ("OFFGRID","homeowner",None,"none","attic box fan, thermoelectric, solar"),
"UC3sYHaAZtJI-vrD64K7Qe9w": ("ENERGY","homeowner",OC,"UK home tinkerer","diesel heater heating home, waste-heat radiators"),
"UC8A5jlib95OPDiV1yCS6t1Q": ("ENERGY","homeowner",None,"none; 'methods industries don't want you to know'","hot-room vent/fan tricks, radiant barrier"),
"UC1AtJIwlt9tI-Z-QKQJJ_Vw": ("OFFGRID","homeowner",None,"'small group of writers'","natural cooling, $0-heat homes"),
"UCam5-STAaS2ddkKEYF9w8RA": ("TRADE","trade",OC,"HVAC technician (comedy)","trade culture, service calls, tool reviews"),
"UCuezPXEDYWG_oXWDtZjguwA": ("ENERGY","homeowner",OC,"Alex Kessler, indoor air quality","air purifiers, DIY purifier, HRV"),
"UCo_LXXyDPV1cRAa5hIxTb6g": ("OFFGRID","homeowner",None,"description is a Regency-romance channel (pivoted)","attic $0 fix, window screens, curtain sheet insulation"),
"UC18XWxoUKP_YC_i7g9SiyjA": ("OUTAGE","homeowner",None,"none","heating sources without electricity, Dollar Tree heating items, seniors"),
"UCOs-UENpz7ovjph0Ok6-Pnw": ("OUTAGE","homeowner",None,"'Dick Colter' Alaskan households","Dollar Tree winter items, heating sources, window brands"),
"UChoVwGVLPHvm55zLbDOeJXA": ("OUTAGE","homeowner","faceless persona (description: 'fictional character: an AI-generated grandmother')","June Halvorsen, AI grandmother, Minnesota Iron Range","keep bed/room warm with no heat, ice storms, bubble wrap"),
"UCxVLjOSnuB9vtDCMsEl_9lg": ("ENERGY","homeowner",None,"Hal, 40 years laying brick","brick thermal mass 'why don't seniors', fireplace heat loss"),
"UCoreRxzSj2qK18IXgtwColg": ("ENERGY","homeowner",None,"Gene Halvorsen, North Pole Alaska, hauled heating oil","heating mistakes, windows before winter, one warm room"),
"UCK1RNqDyZ0Mzqg1p8Ruj9_w": ("OFFGRID","homeowner",None,"none","outside window shades, attic foil, earth battery"),
"UCBhlbZiTKjF11v7-VAErDXw": ("DIY","homeowner",OC,"Handyman Hertz","window AC cleaning, water heater 2-minute tutorials"),
"UCm76z_NC8DU6zxxmnjZW22g": ("ENERGY","mixed",OC,"ASIRI Designs, building science","vapor barriers, house wrap, insulated walls"),
"UC0BnbW-S7r-fCwL9b2DeyKw": ("ENERGY","homeowner","faceless persona (grandmother voice; NexLev: faceless)","'Frannie', grandmother who 'never needed Google'","cool house for $5, water bill tricks, frugal living"),
"UCAe1DFdhgDxmhzuaCxjzz6A": ("OFFGRID","homeowner",None,"Earl Sizemore, Clinch Mountain TN, blacksmith's son","salt-bucket room heat, cheap power"),
"UCmpz9jj83ditlYP4XA74r8w": ("OUTAGE","homeowner",P,"'Wes Tucker' (no description)","DIY stove heat, off-grid heaters, grid-down power"),
"UCMXFneU1qRWt9X_lNc36Zdw": ("OUTAGE","homeowner",None,"Elias Mercer, off-grid survival","old-timer outage heat, wood stove overnight"),
"UCRKwB8DarX5_lykpnh8BolQ": ("ENERGY","homeowner",None,"none","electric bill/panel loophole, buy-it-for-life brands"),
"UC7AQ2xtsH_55cyb9gkhbDTg": ("OFFGRID","homeowner",None,"recycled-materials DIY hacks","'free heat all winter', homemade AC"),
"UCmHk4rHe9oDPkBEBESMVcvg": ("OUTAGE","homeowner",None,"Dan Cooper, winter power-outage readiness","one warm room in a blackout, cooking, pantry"),
"UCZalgfOzTQ7XjAFtIuUD8jw": ("OUTAGE","homeowner",None,"'Grandma' (no description)","grandma's heating hacks"),
"UCx0OIvHyA-rLE1_jHfrJTbQ": ("OFFGRID","homeowner",None,"none; 'homes built to heat, cool and power themselves'","earth battery, bury a cool loop, free power"),
"UC-JjgZLelrq83F4vIfmD3Jw": ("OUTAGE","homeowner","faceless (AI-image scenes; my reading)","early-American homestead skills","items worth gold when the furnace dies, warm without electricity"),
"UCiGOVbSR3aWWFAO0_ux_fwA": ("OUTAGE","homeowner",None,"none","Dollar Tree heating items, Red Cross stockpile, EMP"),
"UCVIirwqWdBCyynoWRsld2Ug": ("OUTAGE","homeowner",None,"Ray Sutter, 22 years Army; sells e-book","heating sources without electricity, power-out first steps"),
"UCAnmPt5TiGJLN-C2dCq1baA": ("OUTAGE","homeowner","faceless (hand-drawn sketches, per description)","none","no power in winter, polar vortex blackout"),
"UCc_vM5wQ_AmOTw_q1BHrlnA": ("OFFGRID","homeowner",None,"household hacks","free heating without gas or electricity, lock hacks"),
"UCAsjbTlJ9B4GVQJ8yirIEdg": ("ADJ","homeowner",None,"Walt Harden, 35 years licensed contractor and home inspector","only brands still built to last (water heater, fridge, panel)"),
"UCpCfTy6di2SLqFnlRyJQNsQ": ("TRADE","mixed",OC,"Canadian HVAC technician, DIY solar","AC on solar, furnace leaks, heat pumps"),
"UCjB9zT33NNsQU2lzgUVQ7Dg": ("ENERGY","homeowner",None,"none","wood stove efficiency, firewood rules"),
"UCw1V3VC3xAzL66X4VwqaKlg": ("DIY","homeowner",OC,"Scott, hands-on DIYer","furnace won't turn on, general home repair"),
"UCPKAKrjoMz7POptCloy7AIQ": ("DIY","homeowner",OC,"DIY host","DIY mini-split install, general DIY"),
"UCFCTrfb1JUJjs3Im8OZDtBw": ("ENERGY","mixed",OC,"Matt Risinger, Austin builder","building science, insulation, tankless"),
"UC67dKTEwpAhKv2oYDATwR8g": ("DIY","homeowner",OC,"Silver Cymbal (study seed)","central air not cooling, plumbing, generators"),
"UCpb-xu6Oun_d41RjztUgFWA": ("DIY","homeowner",OC,"Adam, 'not a professional... fellow DIYer'","AC coil cleaning, wiring mistakes"),
"UCjhwaa5Ufj-l_5JGFwfp98Q": ("DIY","homeowner",OC,"DIY host","garage door heat loss, home repairs"),
"UCUtWNBWbFL9We-cdXkiAuJA": ("DIY","homeowner",OC,"This Old House (TV brand)","mini-split install, furnace maintenance, all home topics"),
"UCjtUS7-SZTi6pXjUbzGHQCg": ("ENERGY","homeowner",OC,"Matt Ferrell, sustainable tech","geothermal, heat pumps, solar"),
"UCy0tKL1T7wFoYcxCe0xjN6Q": ("DIY","homeowner",OC,"explainer host (Alec Watson; my knowledge, not on page)","portable AC, heat pumps, dehumidifiers explained"),
"UCI2VDyfqdsttBE0X3c-ArXg": ("ENERGY","mixed",OC,"Corbett and Grace Lunsford, home science","weatherstripping, window film, thermal cameras"),
"UCM9ofY098XFqp-cCzVKhEyA": ("TRADE","mixed",OC,"HVAC/R journeyman, Phoenix; 'HVAC hacks'","bad installs; mostly car videos at top"),
"UC-5zd31qI3tWQt8u4ZIJr-A": ("TRADE","trade",OC,"HVAC tech","reversing valves, boilers, tool loadouts"),
"UCE5lQKOyYXz6J6UgZQn2ptw": ("TRADE","trade",None,"AMK online training (India)","HVAC training, heat load, chilled water"),
"UCPgg9cUPr9g5dB_hb4k5cOQ": ("DIY","mixed",OC,"'Master HVAC technician', handyman influencer","plumbing/handyman shorts and long-form"),
"UCq0fxytZwEYul4AmfEiXL_w": ("OFFGRID","homeowner",OC,"gardener (bonsai)","'unlimited heat for your home, no electric' (2 huge hits); gardening"),
"UCZ32JAyPXVY2f3g2VxekBjA": ("DIY","homeowner",OC,"home repair host","window AC install/review, pellet stove, carpentry"),
"UCnorhjQR4zJkT7AVNhu395Q": ("DIY","homeowner",OC,"renovation host ('30 years' per a title)","rim joist insulation/heat bill hit; renovation"),
"UCP9-ESl_NU-f9iz9Tl_J3oQ": ("OUTAGE","homeowner",OC,"homestead/prepping couple","emergency heat, outages, recalls"),
"UC99qA3pCW0u0-J2r49-naNA": ("OUTAGE","homeowner",OC,"survival/preparedness host","fan-to-AC hack, cut heating bill in half, power out"),
"UCk0fGHsCEzGig-rSzkfCjMw": ("TRADE","mixed","faceless (animated explainers; my reading)","Paul Evans, engineering","heat pumps, HVAC and electrical explained"),
"UCbJ8oD5Gmh6CKv0GPpXpK8w": ("DIY","homeowner",OC,"UK multi-trade DIYer","radiator valves and balancing, general DIY"),
"UC2rzsm1Qi6N1X-wuOg_p0Ng": ("DIY","homeowner",OC,"product tester","furnace filter test; tools, auto"),
"UC9GdB6vG6m6cDAwrTAWXgyg": ("DIY","mixed",OC,"UK builder","heat pumps 'not the future', spray foam problems"),
"UC9TcuDlGy9FTaYxhkOet0Ig": ("OFFGRID","homeowner",None,"'Amish wisdom' for modern families","how Amish heat homes without gas/electricity, food"),
"UCwF8vOEatNvJUiXXJtDx-zA": ("DIY","mixed",OC,"UK plumber","radiators not working, plumbing"),
"UC1GLDECMH83KqDn6hypodYw": ("DIY","homeowner",OC,"Brandon, third-generation janitor","AC unit and coil cleaning; all cleaning"),
"UCCZbLEJAq6HCJu4_iOfVs3g": ("BRAND","homeowner",OC,"Dr. Energy Saver dealer network","attic insulation done wrong, jumper ducts, spray foam"),
"UCGDy78008pRm0Y-HYq9jOwg": ("DIY","homeowner",OC,"'regular guy' DIY","AC drain line tool; outlets, doorbells"),
"UCDLxnaDQzo8YolFqsBAHVLQ": ("DIY","homeowner",OC,"carpenter","weatherstrip old doors; carpentry"),
"UCteXKxQW6oOCvZjAnHlSw_g": ("BRAND","mixed",OC,"AMRE Supply, parts supplier (Canada)","furnace starts then stops; multimeter, plumbing"),
"UCHYSw4XKO_q1GaChw5pxa-w": ("DIY","homeowner",OC,"woodworking/DIY host","15 cheap ways to fix cold rooms; flooring"),
"UCt08e2_TicHGW1GqP-zqKDQ": ("ENERGY","mixed",OC,"Heat Geek, UK heating engineers network","leave heating on?, energy bills, smart stats, heat pumps"),
"UCLnGgnj-hneDI3CFzBmdGLg": ("ENERGY","homeowner",OC,"Alex Beale, solar and power stations","electric-bill device test, solar setups"),
"UCuMyjTVlkM4xZ5z_eSyoB1w": ("HVAC","mixed","on camera (NexLev check: not faceless)","Tad, HVAC since 2003","solar AC, mini-split DIY vs tech, furnace checks"),
"UC2sAny8hk9VtLrE4ylZbGjQ": ("OFFGRID","homeowner","faceless (hand-drawn, per description)","none","$300 tunnel cooling, $7 powder vs AC, freezing physics"),
"UCaj8oe2fiZNjXzX1QEZ1F2A": ("OFFGRID","homeowner",None,"Elias Yoder, raised Amish-style","$4 fix for hot house, cool a room for $7, mosquitoes"),
"UCdmyYTlRW9kIn67GBZfFHvw": ("DIY","homeowner",OC,"smart-home reviewer","Nest thermostat manual; cameras, doorbells"),
"UC9QeaKy-AXk9yRQ9WqTvvmQ": ("OUTAGE","homeowner","faceless (sketch animation, per description)","none","not freezing to death, winter blackout survival"),
"UCx1m6AboILQKMNXbsLjjI4Q": ("DIY","homeowner",OC,"UK DIYer","bleed radiators; general DIY"),
"UCcPAcUV5haCy4Y46t-VsRWA": ("ENERGY","homeowner",OC,"DIY host ('a trick for that')","eliminate AC power bill hack, plug-in solar, batteries"),
"UCAGvsxwZ3pd5BC0fsLiBmRg": ("OUTAGE","homeowner",OC,"preparedness and backup-power reviewer","day 2 of a power outage, generators, batteries"),
"UCgexv0zlYzl_Q0otBfb6TXg": ("OUTAGE","homeowner",OC,"preparedness host","Mr Buddy heater tips, stockpiles"),
"UCyDPTQMaRk_Z6k76M0BP-8w": ("ADJ","homeowner",OC,"Cassandra, food and home systems","one heating-bill hit; mostly food"),
"UCwOBG77Tm8cE24FPxHb_abw": ("DIY","homeowner",OC,"Reed, smart home","Nest vs Ecobee; home automation"),
"UCL3_8mlFDtcVCZ-JatBEJKw": ("OUTAGE","homeowner",None,"frugal-living ('Grandma/Grandpa hacks') channel, Philippines","grandma's winter survival tricks for seniors living alone"),
"UC8eT35xEnHJH6uUStaQkzsg": ("BRAND","homeowner",None,"Got Ductless, ductless retailer","Mitsubishi multi-zone reviews, brand choice"),
"UC25wvCM4xBbfZHged4XyAgw": ("OUTAGE","homeowner",None,"David Bennett, UK household preparedness","Poundland heating items, heating without electricity (UK)"),
"UCj-e0GX6QhDChCPUBeX-FbA": ("DIY","homeowner",OC,"20-year retired vet","mini-split cleaning, used-oil burner, mowers"),
"UCo1j38r5C6_tJfA-7u64d0w": ("OFFGRID","homeowner",None,"none","$5 attic heat setup, attic hatch fan"),
"UCmPc7lvTIm-J9GmvQku5wAw": ("DIY","homeowner",OC,"veteran/police officer DIYer","ducted mini-split install; framing"),
"UCMX8nbmbyPU4v-Yi6beBFyg": ("DIY","homeowner",OC,"DIY host","garage insulation R-13 vs R-15"),
"UC6vA_TPy34Xb_oin4WV-_vA": ("TRADE","trade",OC,"Armando, HVAC instructor, Los Angeles","refrigeration cycle, control boards, ECM motors"),
"UCARn8zLnCi13ikrr-OjIVkQ": ("OUTAGE","homeowner",None,"none","Dollar Tree heating items, FEMA items"),
"UCCBDciZlJRGkwjHn45AuyxQ": ("ENERGY","homeowner",OC,"Shan, UK solar/heat pumps/EVs","gas boiler to heat pump story, heat loss"),
"UCl16ptu7IK-jhdsBBdm1xQw": ("DIY","homeowner",None,"'pro tech bro / professional homeowner'","Honeywell thermostat programming how-tos"),
"UClCRWNfP-7P5q35NA4olTUg": ("DIY","homeowner",OC,"UK DIYer","uPVC door/window draughts; fence posts"),
"UChuBBg6_uHGUk9x7vtZwzmQ": ("OFFGRID","homeowner",None,"none","AC-to-geothermal tricks 'HVAC pros hide'"),
"UCIdzZrKCdyNf1Oh1cGjSYnA": ("BRAND","homeowner",OC,"crawl space/foundation contractor","attic ventilation, crawl space moisture, air sealing"),
"UCkN5jNYky03jok8jy5mKhzw": ("OUTAGE","homeowner",None,"American-nostalgia channel","Dollar Tree heating items for blackouts, prepper lists"),
"UCpgty9Km_rAnzOZhwJUVMqg": ("ENERGY","homeowner",OC,"UK home renewables enthusiast","heat pump at -3C, solar, EV power"),
"UCG_Pwm8tfMnJg1Rp2Fsd-qA": ("TRADE","mixed",OC,"Mikey Pipes, master plumber and HVAC tech","steam boilers, no-heat calls, ductless cleaning"),
"UCQLQI7hMy_v7cXknTdGrqQw": ("HVAC","mixed",OC,"licensed HVAC contractor, Greenville SC, 15 years","service-call stories (elderly neighbour's AC), diagnostics"),
"UCItXgo_xQhTFQfEMphmzPwA": ("BRAND","homeowner",OC,"Heatable, UK boiler/solar installer","boiler pressure, thermostat guides, heat pumps"),
"UCf0mHkUi_xiAdb97QnecFAA": ("BRAND","homeowner",OC,"Rich Morgan, Magic Touch Mechanical, Phoenix","mini-split review, best AC for Phoenix, staging"),
"UCqPFxcbyCnlWz6tmackoJMQ": ("ENERGY","homeowner",OC,"Mick Wall, Energy Stats UK","boiler flow temperature savings, tariffs, heat pumps"),
"UCfyMMHJv-V10UpTkXxCvikg": ("HVAC","homeowner",None,"Jordan, 20 years in HVAC","heat pump vs furnace, wrong HVAC brands, SEER"),
"UC4mZGMmJ1kOaOG1oRACZDbQ": ("TRADE","mixed",OC,"Steven Lavimoniere, 40+ years plumbing/heating/AC","daily job videos, HVAC scam exposed"),
"UCik3JUx29XhSgEWKv7MUv8w": ("ENERGY","homeowner",OC,"UK homeowner community, renewable heating","thermal cameras, heat pumps, buffer tanks"),
"UCMvzPcAmmdFJr6Yk-2v0k-w": ("BRAND","homeowner",None,"alpinehomeair, HVAC retailer (Blueridge)","ductless mini-split install and product videos"),
"UCnaa_80Xxuoq0jNA68uddaw": ("BRAND","homeowner",OC,"Missouri Wind and Solar store","cut electric bill in half series, wind/solar"),
"UCAPrhJwVweWZA8GEPoClSdw": ("ADJ","homeowner",OC,"scam-baiter","one HVAC hit: air duct cleaning scam exposed"),
"UCgx_ERh6IE-Td3FLJstu1iQ": ("DIY","homeowner",OC,"carpenter (Canada)","5 furnace filter mistakes; caulking, doors"),
"UCWWJfC_I8KyZdJPnajPWtjg": ("DIY","homeowner",None,"home-fix channel","stop buying cardboard AC filters; stumps"),
"UCakhWWxvy7-kI3NfetLetPw": ("ENERGY","homeowner",None,"'Earl', Appalachian","firewood mix, splitting, salt-bucket heat, stumps"),
}

EXCLUDED = {  # candidates looked at and left out of the table, with the reason (reading)
"UCSlwgqAXct9Oa-8XnzzlkXA": "Brand Meter: clothing brands, no HVAC",
"UCidqAQ2CxzBp4OYzapEu_og": "Consumer Truth: grocery tests, no HVAC",
"UCGQz5_mS75Awg5HUMhiiJ2w": "Sergeant Dale Whitfield: stumps/cars/drains persona, no HVAC long-form found",
"UC4xatswWsvs81cQSnDrJqsA": "Patina: Japanese-culture channel; one senior winter-tricks video (377K)",
"UCzOi__BRsEE3CAR2bKXqsIg": "Project Renewed Homes: renovation stories",
"UCF7WlkgQIFOktAJVY5ZgRtw": "Clever Hacks: mostly Shorts",
"UCdyG3WX1yILqhYHe3EK4bQw": "Sidney Explains: food/frugal; one air purifier video",
"UCEKUEXO7sBNrasXwS2hoy8Q": "The roots survived: concrete/sand hacks",
"UCFNWzOwiK6wmSQpBPG_ZP9Q": "Stop Wasting Stuff: hydrogen peroxide hacks, no HVAC hit found",
"UCGD4IPN_ywGUOeLF74qUM7w": "The Household Formula: general hacks; one HVAC video with 60 views",
"UCzDvYjtRgZ4mGuPGMioBY5A": "Amos Miller: batteries/power, not heating",
"UCcZ4RylQGWTCkdM0PT2k9fg": "Cantrell Hoffman: prepper water/food",
"UCfKWxYMpFy2paDbsv0YSPbg": "Amish Frugal Life: Amish lifestyle (one humidity/mold video 363K)",
"UCpDSkMeuhhAqJ0IfO-70UKA": "Finn Stone: mixed (mafia history, lathes, alternators)",
"UCJCk5Iz8UO4jrLb07hvrNgQ": "AC PRO: car AC brand",
"UCaxva4G655ldv6AHf1B9vvw": "Thomson AC: videos mostly under 5 minutes",
"UCvtgUPTFH0vnjUnWKxpWgeA": "The Thermo Expert: videos under 5 minutes (rebate news)",
"UCtBzNpJfPU8AWUEnEfAQFPw": "STAYCOOLHVAC: install clips, mostly under 5 minutes",
"UCNdp0HrrequO9puyQvvh0Lw": "Gary Whitaker Backup Power: generator/power-station reviews (out of scope per operator)",
}

# ---------- sources ----------
nf = NEX["niche_finder"]["channels"]
sim = NEX["similar_channels"]["channels"]
outrows = NEX["outlier_and_viral_videos"]
lfn = {c["url"].split("/")[-1]: c for c in NEX["latest_faceless_niches_hvac_subset"]}
fcheck = NEX["check_faceless"]
yts = NEX["youtube_search_rows"]
web = NEX["web_search_names"]

swq = {}
for r in sw:
    if r.get("channelId"): swq.setdefault(r["channelId"], set()).add(f'yt "{r["query"]}" [{r["sort"]}]')

def example(cid):
    cands = []
    for r in sw:
        if r.get("channelId") == cid and secs(r.get("length")) >= 300 and KW.search(r["title"] or ""):
            cands.append((num(r["views"]), r["title"], r["id"], "YouTube search " + r.get("age", "")))
    f = PAGES + "/" + cid + ".json"
    if os.path.exists(f):
        j = json.load(open(f))
        for p in (j.get("popular") or []) + (j.get("latest") or []):
            if secs(p.get("dur")) >= 300 and KW.search(p.get("title") or ""):
                cands.append((p.get("views"), p["title"], p["id"], "Videos tab"))
    if cid in nf:
        for v in nf[cid]["rec"].get("lastUploadedVideos") or []:
            if secs(v.get("length_text")) >= 300 and KW.search(v.get("video_title") or ""):
                cands.append((v.get("video_view_count"), v["video_title"], v["video_id"], "NexLev niche finder"))
    for v in outrows:
        if v.get("ytChannelId") == cid and (v.get("videoLengthSeconds") or 0) >= 300:
            t = v.get("videoTitle") or v.get("title")
            if KW.search(t or ""): cands.append((v.get("videoViews"), t, v["videoId"], "NexLev outliers/viral"))
    for v in yts:
        if v.get("channelId") == cid and secs(v.get("duration")) >= 300:
            cands.append((num(v.get("viewCount")), v["title"], v["videoId"], "NexLev youtube_search"))
    cands = [c for c in cands if c[0] is not None and not NEG.search(c[1] or "")]
    return max(cands) if cands else None

def g(d, *ks):
    for k in ks:
        if d is None: return None
        d = d.get(k)
    return d

rows = []
for cid, (fit, aud, typ, persona, topics) in ANN.items():
    a = about.get(cid, {})
    s = sim.get(cid, {}).get("a", {})
    n = nf.get(cid, {}).get("rec")
    title = a.get("TITLE", "")
    name = title.split(" | ")[0] if title else (s.get("channelName") or (n or {}).get("title") or "")
    url = title.split(" | ")[1] if " | " in title else ""
    handle = ("@" + url.split("/@")[1]) if "/@" in url else ((("@" + n["username"]) if n and n.get("username") else "not found"))
    subs = num((a.get("subscriberCountText") or "").replace(" subscribers", "")) if a.get("subscriberCountText") else (s.get("subscriberCount") or g(n, "stats", "subscribers"))
    subs_src = "YouTube About" if a.get("subscriberCountText") else ("NexLev similar" if s.get("subscriberCount") else ("NexLev niche finder" if n else ""))
    tv = num((a.get("viewCountText") or "").replace(" views", "")) if a.get("viewCountText") else (s.get("viewCount") or g(n, "stats", "totalViews"))
    joined = (a.get("joinedDateText") or "").replace("Joined ", "") or (s.get("joinedDate") or "")[:10] or (n or {}).get("channelCreationDate") or "not found"
    nv = num((a.get("videoCountText") or "").replace(" videos", "")) if a.get("videoCountText") else (s.get("videoCount") or g(n, "stats", "totalVideos"))
    country = a.get("country") or s.get("country") or (n or {}).get("location") or ""
    # type
    if typ: t = typ
    elif cid in fcheck: t = ("faceless" if fcheck[cid]["isFaceless"] else "not faceless") + f' (NexLev check {fcheck[cid]["confidence"]})'
    elif n is not None and n.get("isFaceless") is not None: t = ("faceless" if n["isFaceless"] else "not faceless") + " (NexLev niche finder flag" + (", AI channel" if n.get("isAiChannel") else "") + ")"
    else: t = "not checked"
    found = []
    if n: found += ["NexLev NF: " + q for q in nf[cid]["found_by"]]
    if cid in sim: found += ["NexLev similar to " + x for x in sorted(set(sim[cid]["seeds"]))]
    found += sorted(swq.get(cid, []))[:6] + ([f"(+{len(swq[cid]) - 6} more YouTube searches)"] if len(swq.get(cid, [])) > 6 else [])
    found += sorted(set(v["query"] for v in outrows if v.get("ytChannelId") == cid))
    found += sorted(set("NexLev youtube_search: " + v["query"] for v in yts if v.get("channelId") == cid))
    if cid in lfn: found.append("NexLev latest_discovered_faceless_niches")
    if cid in web: found.append("web search: " + web[cid])
    ex = example(cid)
    st = g(n, "stats") or {}
    rows.append({
        "name": name, "handle": handle, "channel_id": cid, "link": f"https://www.youtube.com/channel/{cid}",
        "type": t, "persona_background": persona, "audience": aud, "fit": fit,
        "subs": subs, "subs_source": subs_src, "total_views": tv, "joined": joined, "video_count": nv, "country": country,
        "nexlev_monthly_views": st.get("monthlyViews"), "nexlev_monthly_revenue_usd": st.get("monthlyRevenue"),
        "nexlev_rpm_base": g(st, "rpm", "base"), "nexlev_outlier_score": (n or {}).get("outlierScore"),
        "main_topics": topics,
        "example_video_title": ex[1] if ex else "not found", "example_video_id": ex[2] if ex else "",
        "example_views": ex[0] if ex else "", "example_source": ex[3] if ex else "",
        "found_by": " ; ".join(found) if found else "candidate list (see method)", "date_pulled": "2026-10-23",
    })

rows.sort(key=lambda r: -(r["subs"] or 0))
with open(RAW + "/channel-finds-round1.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump({"rows": rows, "excluded": EXCLUDED}, open("/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/cf1/rows.json", "w"))
print(len(rows), "rows")
