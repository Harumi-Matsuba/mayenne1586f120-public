# 行の水平投影の鋭さが最大になる角度を探す
# 使い方: python3 src/angle.py 画像 x0 y0 x1 y1（切り出す範囲を画像の幅・高さに対する割合で）
import sys, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src=sys.argv[1]; x0,y0,x1,y1=map(float,sys.argv[2:6])
a=Image.open(src).convert('L'); W,H=a.size
c=a.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1)))
c=c.resize((c.size[0]//4,c.size[1]//4))
best=[]
for ang in np.arange(-4,4.01,0.1):
    r=np.asarray(c.rotate(ang,resample=Image.BICUBIC,fillcolor=255),dtype=float)
    p=(r<120).sum(1).astype(float); best.append((p.var(),round(ang,1)))
best.sort(reverse=True); print(best[:5])
