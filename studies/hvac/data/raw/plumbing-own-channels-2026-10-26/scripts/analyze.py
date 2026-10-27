import json,sys,csv,statistics as st,re,collections,datetime
P=sys.argv[1]; sys.path.insert(0,P+"/scripts")
from tag import main2
o=json.load(open(f"{P}/built.json"))
SUB=[("hydrogen peroxide",r"[Hh]ydrogen [Pp]eroxide"),("vinegar",r"[Vv]inegar"),("baking soda",r"[Bb]aking [Ss]oda"),("borax",r"[Bb]orax"),("washing soda",r"[Ww]ashing [Ss]oda"),("bleach",r"[Bb]leach"),("dish soap",r"Dawn|Dish Soap"),("WD-40",r"WD-40"),("dishwasher/denture tablet",r"(Dishwasher|Denture) Tablet"),("withheld 'this' substance",r"(Cup|Glass|Spoonful|Drops) [Oo]f This|One of These|This \$1 Powder|The \$1 Powder|Pour This|\$3 Powder|This ONE Thing|These \d+ Things Down"),("salt",r"[Ss]alt "),("CLR/citric",r"CLR|Citric"),("aluminum foil/ice/lemons",r"Foil|Ice and|Lemons")]
FIX=[("toilet",r"[Tt]oilet"),("drain/clog",r"[Dd]rain|[Cc]log|Unclog|[Ss]ink"),("water heater",r"[Ww]ater [Hh]eater|Hot Water|Tankless"),("SharkBite/fittings",r"SharkBite|ProPress|Push|Fitting"),("S-trap",r"S-?\s?Trap"),("solder/copper",r"[Ss]older|Copper"),("PEX/pipe material",r"PEX|CPVC|Polybutylene|Galvanized|Pipe Material|Cast Iron"),("garbage disposal",r"Disposal"),("sewer/roots",r"[Ss]ewer|Roots"),("AC/furnace/heating",r"\bAC\b|Furnace|Heating|Heat Pump|Cool Our House"),("washing machine/dishwasher",r"Washing Machine|Dishwasher Tonight|Your Dishwasher|in Your Dishwasher"),("limescale/hard water",r"Limescale|Hard Water|Showerhead"),("water bill/pressure",r"Water Bill|Water Pressure|Shower Pressure|Water Use")]
def lab(t,L): return [n for n,p in L if re.search(p,t)]
allrows=[]
for k,c in o.items():
    rows=[]
    # month normal
    bym=collections.defaultdict(list)
    for v in c["vids"]: bym[v["date"][:7]].append(v["views"])
    for v in c["vids"]:
        m,s=main2(v["title"])
        v["F_main"]=m; v["F_mod"]=s
        v["month_median"]=st.median(bym[v["date"][:7]]); v["x_month"]=round(v["views"]/v["month_median"],2)
        v["substance"]="; ".join(lab(v["title"],SUB)); v["fixture"]="; ".join(lab(v["title"],FIX))
        v["channel"]=k; rows.append(v)
    rows.sort(key=lambda v:-v["multiple"])
    with open(f"{P}/videos_{k}.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["id","title","date","views","multiple","F_main","F_mod","age_days","views_per_day_if_under_60d","duration","collab_credit","x_same_month_median","substance","fixture","views_source"])
        for v in rows: w.writerow([v["id"],v["title"],v["date"],v["views"],v["multiple"],v["F_main"],v["F_mod"],v["age"],v["vpd"],v["dur"],v["collab"],v["x_month"],v["substance"],v["fixture"],"YouTube innertube /next, pulled "+v["pulled"]+" UTC"])
    allrows+=rows
json.dump(allrows,open(f"{P}/all_tagged.json","w"))
print("rows",len(allrows))
