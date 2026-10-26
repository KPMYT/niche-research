"""Round 2 (2026-10-24): channel type, my reading from one example thumbnail per channel (contact sheets of hqdefault.jpg,
viewed 2026-10-24) plus the channel description. Not a measurement. Codes:
OC = on camera (a real presenter's face shown); FR = faceless, real footage (hands, equipment; presenter unseen);
FG = faceless, graphics/animation/text only; FA = faceless, AI images (no recurring presenter);
AV = AI avatar (an AI-made presenter face, no stated name); FP = faceless persona (a named character shown as an AI-made face).
BR = company/brand channel (logo, product or staff shots)."""
T = {
"BIG TICKET TRUTH":"AV","Jack Miller":"AV","Patina":"FA","Quality Rot":"FA","TheAirConditionerGuy":"FR","Wonders":"FA",
"ACiQ":"BR","American Veteran Air & Heat":"BR","Any Hour Services - Electric, Plumbing, Heating & Air":"BR","AprilAire":"BR","Atlantis Energy Heat Pumps":"BR",
"Bosch Home Comfort USA":"BR","Bryant Home Comfort":"BR","Clean Air Heating & Cooling":"BR","D Air Conditioning":"BR","Derek Cole":"OC","Fire & Ice Home Services":"BR",
"HVACDirect":"BR","HomeServe":"BR","ICS Comfort Boss":"BR","Ideal Conditions":"BR","Jackson Systems":"BR","Leaky’s Plumbing, Heating & A/C":"BR","Lennox Learning Solutions":"BR",
"Maryland Hvac Repair":"FG","PRIME AC AND HEAT":"BR","Stephen Shares HVAC Tips at Goettl":"FR","Surf Bros HVAC":"BR","The Insulation Team":"BR","Williams Plumbing & Heating":"BR",
"Worcester Bosch":"BR","eMotors Direct":"BR","Budget Phil":"FR","Flannel Guy DIY":"FR","Kevin Jones":"OC","The Lovely Place":"FR","AEPowerHouseTV":"FR",
"Eric George | Home Performance Pro":"OC","Firewood For Life":"OC","Green Exposed":"FA","Harlan Sawyer":"FP","Tim & Kat's Green Walk":"OC","AC Professor":"FG",
"Blueprint Archive":"AV","Brian Barraza":"OC","Caleb Vance":"FP","Conditioned Air Secrets":"AV","DIY HVACMillionaire Advice Class \"Capacitor Freon\"":"FR",
"Dale Kirkwood":"FP","Dale Prosser":"AV","David Jones":"FR","Earl The HVAC Guy":"FR","Earl Whitaker":"FP","EdgeTek HVAC":"OC","Frank From Maintenance":"FP",
"FurnacePrices.ca":"OC","HVAC Academy":"FG","HVAC Bee":"OC","HVAC Explained":"OC","HVAC Home Guide":"AV","HVAC Made Clear":"FG","HVAC Talkshow and Review For Homeowners & DIY":"FR",
"HVAC in SC":"FR","Home Comfort Guy":"FG","HomeFix Guide":"FA","Homeowner Money":"AV","INDOOR AIR QUALITY":"FR","Joe Tollari":"OC","Leroy Bell's Repair":"FP","Lex Vance":"FR",
"Mechanics For Non Mechanics":"OC","ResCom Contractors":"FG","The HVAC Veteran":"OC","The Heat and Air Guy":"OC","The House Papers":"AV","The Outspoken Engineer":"OC",
"The Smart Way to Buy HVAC with Doug Cross":"AV","The Technician’s Blacklist":"FA","Vern Holt | Home Repair":"FP","Walt Brenner's Boiler":"FP","fixmyownac":"FR","hvacrepairguy":"FR",
"Creative DIY365":"FA","Creative inventions LMTN":"FR","DIY mr.T":"FR","Darrin Stevenson":"FP","Del Rasmussen":"FP","Eli Forgotten Ways":"FP","Forgotten American Homes":"FA",
"Forgotten Appalachian Skills":"FA","Gus Halvorsen":"FA","Hidden Build":"FA","Hidden Heat Lab":"FR","Hidden Passive Tech":"FA","Hidden Systems":"FA","Jake Holloway":"FP",
"Lars Halvorsen":"FP","Lost Blueprints":"FA","Lost Methods Archive":"FA","Mr iPoo":"FR","Off-Grid Blueprint":"FA","OffGrid Secrets":"FA","Ray Holton Secrets":"not checked (thumbnail did not load)",
"The Archive of Builds":"FA","The Build Guide":"FA","The Hillbilly Way":"FP","The Sensei's Home":"FG","Tip for you DIY":"FR","Wade Caudill":"FA","Walter Handyman":"FA",
"desertsun02":"FR","ecophage":"FG","Blackout Basics":"FA","Blackout Logic":"AV","David Bennett":"FP","Eli's Plain Heat":"FP","Emmett Boone Prepping":"FP",
"Forgotten American Survival":"FA","Gary Miller":"FP","Hank Dockery":"FP","Harlan Pike Prepping":"FP","Ivan’s Survival Journal":"FP","Jhon Survival Mode":"FP",
"Kate Sullivan Ready Living":"FP","Linda Fairbrook":"FP","Mason Reed Preparedness":"FP","Stay Ready. Urban Survival.":"OC","Tactical Psychology":"FG","Wade Corbin":"FP",
"Zach Of All Trades":"FG","AB HVAC":"FR","Adrian Garcia":"FR","Building Systems Academy":"FG","ChilesHeatCool":"FR","Drewdriskle":"OC","Everything HVACR":"FR","Ewok":"FR",
"Forever Tech English":"FR","HVAC Greatness by Pete Ramsey":"OC","HVAC Guide for Pros":"FR","HVAC OTJ":"FR","HVAC Service Technician Talk":"FR","HVAC Tech Knowledgy":"FR",
"HVAC Technician Sales Secrets":"OC","HVAC Training 101":"FG","HVACJess - The HVAC Diaries":"OC","HVACR VIDEOS":"FR","HVACTIME":"FR","HVACmillionaire":"OC","Hall’s HVAC":"OC",
"Jeff’s HVAC Adventures":"FR","Love2HVAC with Ty Branaman":"OC","MEP Academy":"FG","Mikey Pipes HVAC Training":"OC","Mikey Pipes Uncensored":"FG","Nighthawk HVAC":"FR",
"OnemanHVAC":"OC","ProCalcs University":"FG","Rosa The Female HVAC Tech":"OC","ServiceTechSonny":"FR","Stephen Rardon":"FR","The Air Conditioning Guy":"FR","The HVAC Hacker":"FR","WW HVAC":"OC",
}
LABEL = {"OC":"on camera","FR":"faceless (real footage, presenter unseen)","FG":"faceless (graphics/animation)","FA":"faceless (AI images)",
 "AV":"AI avatar (AI-made presenter, no stated name)","FP":"faceless persona (named character, AI-made face)","BR":"company/brand channel"}
