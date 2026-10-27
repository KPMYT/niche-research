p='/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/build.py'
s=open(p).read()
s=s.replace('|chaudi\\w*|','|chaudi\\w*|selbst|gemacht|abgleich|kostet|bringt|ketel|reparatie|loopt|volledig|warmtepomp|wärmepumpe|entlüften|spart|kosten|sparen|niet|voor|ook|deze|zo|je|jij|wat|werkt|hoe|haar|zijn|nog|naar|ich|nicht|auch|sich|jetzt|immer|richtig||')
s=s.replace('|thermostat housing|last caretaker", re.I)','|thermostat housing|last caretaker|hot water heat pump|solar|burner stove|box turtle|keara riley", re.I)')
open(p,'w').write(s)
