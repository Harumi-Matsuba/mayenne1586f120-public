# 2行ずつ・左右半分のタイルを作る（行番号を左端に赤で書く）
# 使い方: python3 src/tiles.py 補正済み画像 接頭辞 y1,y2,...
import sys
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS=None
src,pre=sys.argv[1:3]; ys=[int(v) for v in sys.argv[3].split(',')]
c=Image.open(src).convert('RGB'); w=c.size[0]
f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',40)
for i in range(0,len(ys),2):
    grp=ys[i:i+2]; top=grp[0]-130; bot=grp[-1]+60
    for j,(u0,u1) in enumerate([(0,0.53),(0.47,1.0)]):
        t=c.crop((int(w*u0),top,int(w*u1),bot)).copy(); d=ImageDraw.Draw(t)
        for k,y in enumerate(grp): d.text((2,y-top-70),str(i+k+1),fill=(255,0,0),font=f)
        t.save(f'tiles/{pre}_{i+1:02d}{"LR"[j]}.jpg',quality=90)
