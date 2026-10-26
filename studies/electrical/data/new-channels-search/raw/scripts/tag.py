import re,json
SUB=[('generators-backfeed',r'generator|backfeed|back-feed|interlock|transfer switch|alternator'),
('backup-power-stations',r'power station|ecoflow|jackery|bluetti|home battery|battery backup|solar generator|backup power'),
('old-panels',r'federal pacific|zinsco|\bfpe\b|federal pioneer|recalled.*panel|panel.*recall|dangerous electrical panel'),
('breakers-panels',r'breaker|electrical panel|panel brand|subpanel|400 amp|200a'),
('old-wiring',r'knob.and.tube|alumin(um|ium) wir|old wiring|old house|victorian|1920s|1950s|100.year.old|old.home features|old home'),
('gfci-afci',r'gfci|afci|ground fault'),
('outlets-switches',r'outlet|socket|receptacle|switch(es)?\b'),
('cords-strips-surge',r'extension cord|power strip|surge'),
('space-heaters',r'space heater|heater'),
('smoke-co-alarms',r'smoke (alarm|detector)|carbon monoxide|\bco detector|fire alarm'),
('dryer-vents',r'dryer'),
('batteries-lithium',r'e-?bike|lithium|power bank|charg(ing|er)|battery (fire|safety)|batteries.*(fire|explo)'),
('electric-bill',r'electric(ity)? bill|power bill|energy bill|electricity (cost|price)|utility bill|unplug.*bill|electricity.*wast|wasting electricity'),
('storms-outages',r'power outage|blackout|power goes out|power (went|is) out|power died|grid (goes |is )?(down|fail|dies|dead)|no power|without power|without electricity|no electricity|ice storm|winter storm|hurricane|nor.?easter|lights go out|lights went out|when the grid|no heat'),
('home-inspection',r'inspector|inspection'),
('holiday-lights',r'christmas light|holiday light|halloween'),
('wildfire',r'wildfire'),
('wiring-mistakes',r'wiring|wire|romex|crimp|wago|electrical mistake|electrician|electrical (problem|warning|hazard|thing)|electrics'),
('fire-habits',r'plugged in|unplug|house fire|fire hazard|start(s)? (a )?(house )?fire|catch(es)? fire|caught fire|burn(s|ing)? (down|your house|houses|american homes)|fire risk|fire danger|firefighter|fire marshal|fire inspector|fire safety|fire prevention|fire starter|banned for starting'),
('electrical-explainer',r'\bvolt|\bamps?\b|60 hz|electricity|grounded|short circuit|lineman|linemen'),
]
EXC=re.compile(r"police|bodycam|murder|k!ll|killer|crime|karen|\bhoa\b|offensive lineman|lineman (drop|get)|rams |paw patrol|kids|toy|gta|minecraft|\bcreate\b|pokopia|free fire|asmr|cozy|anime|reddit|movie|chicago fire|lottery|vtuber|react|9/11|ground zero|realme|scooter|tesla|\bev\b|electric car|motorcycle|\brv\b|subaru|mopar|guitar|well pump|hot tub|microwave|goodman|fridge light|camper|trucker|plane|flight|airline|sasquatch|bigfoot|world cup|mortgage|stockpile|canned|meals|food|mouse|pantry|survival tools|daughter-in-law|son-in-law|dil |grandma's|story|stories|realtor|real estate|seller|buyer|buying a house|buy a house|mold|termite|basement|foundation|roof|plumbing|toilet|water heater|furnace|thermostat|hvac|\bac\b|air condition|insulation|wood stove|firewood|fireplace|chimney|retire(s|ment)? (party|ceremony)|retirement for|six figures|6 figures|cash jobs|trade school|start over|quit my|economics|career|vacancy|data center|net metering|solar panel|solar math|solar system|salt battery|graphene|scrap|recycl|copper vs|fan motor|load shedding|tube behind|volume control|railway|factory|hospital|marina|hotel|nursing home|helmet|hollywood|coffee crew|council|commissioner|evacuation|flashover|backdraft|rescue|response compilation|dollhouse|battery pack|48v|72v|diy lithium|ups surge|best surge|top 5|monitor|amazon's #1|smart socket|news|exposed my|mistress|switch 2|berry avenue|royalty family|tic tac|nintendo|e-bike riders|skatepark|mountain bik",re.I)
def nonascii(t): 
    letters=[c for c in t if c.isalpha()]
    return letters and sum(1 for c in letters if ord(c)>591)/len(letters)>0.15
def subniche(t):
    tl=t or ''
    for code,p in SUB:
        if re.search(p,tl,re.I): return code
    return None
FMT=[('mistakes',r'mistake|wrong|never|don.?t|stop|avoid|beware|habits? that|dangerous|deadly|fatal|ruin|traps'),
('x-vs-y',r'\bvs\.?\b|versus| or '),('only-x',r'only \d|worth buying|brands to avoid|best '),('before-you',r'before you|before the'),
('dont-want-you',r"don.?t want you|hope you never|won.?t tell|never tell|hiding|hidden|secret|scam|lie"),('cheap-hack',r'\$\d|cheap|dollar tree|free\b|pennies|trick|hack'),
('myth-bust',r'myth|is not|isn.?t|not what you think|truth'),('how-to',r'how to|step.by.step|fix it|install'),('story','almost burned|what went wrong|caught fire|found|happened'),('test',r'what happens|tested|i tried|really (replace|run|power|heat|warm)')]
def fmt(t):
    for code,p in FMT:
        if re.search(p,t or '',re.I): return code
    return 'explainer'
def relevant(t,channel=''):
    if not t or nonascii(t): return False
    if EXC.search(t): return False
    return subniche(t) is not None
