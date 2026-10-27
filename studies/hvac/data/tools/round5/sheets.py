import json
from PIL import Image, ImageDraw, ImageFont
L=json.load(open('list.json'))
img='/home/user/niche-research/studies/hvac/thumbnails/img/'
W,H=640,360
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
except: font=ImageFont.load_default()
sizes={}
for s in range(0,len(L),6):
    sheet=Image.new('RGB',(2*W+10,3*(H+30)),'white')
    d=ImageDraw.Draw(sheet)
    for i,it in enumerate(L[s:s+6]):
        im=Image.open(img+it['video_id']+'.jpg').convert('RGB')
        sizes[it['video_id']]=im.size
        # crop hqdefault letterbox (480x360 with black bars) to 16:9
        if im.size==(480,360): im=im.crop((0,45,480,315))
        im=im.resize((W,H))
        x=(i%2)*(W+10); y=(i//2)*(H+30)
        d.text((x+4,y+3),f"#{s+i+1}  {it['video_id']}",fill='black',font=font)
        sheet.paste(im,(x,y+30))
    sheet.save(f'sheets/s{s//6+1:02d}.jpg',quality=90)
json.dump(sizes,open('sizes.json','w'))
from collections import Counter; print(Counter(map(tuple,sizes.values())))
