# 右ページの暗号部分を傾き補正し、行ごとに切り出す
# 使い方: python3 src/deskew.py 元画像 出力フォルダ 接頭辞 x0 y0 x1 y1 角度(度)
import sys, numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src,out,pre=sys.argv[1:4]; x0,y0,x1,y1,ang=map(float,sys.argv[4:9])
a=Image.open(src).convert('L'); W,H=a.size
c=a.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))).rotate(ang,resample=Image.BICUBIC,fillcolor=255)
arr=np.asarray(c,dtype=float)
ink=(arr<120).sum(1).astype(float)
sm=np.convolve(ink,np.ones(31)/31,mode='same')
pk=[i for i in range(46,len(sm)-46) if sm[i]==sm[i-45:i+46].max() and sm[i]>sm.max()*0.25]
pk2=[]
for p in pk:
    if not pk2 or p-pk2[-1]>40: pk2.append(p)
pk=pk2
print('lines',len(pk),pk)
c.save(f'{out}/{pre}_deskew.jpg',quality=85)
w=c.size[0]
for k,p in enumerate(pk,1):
    for j,(u0,u1) in enumerate([(0,0.37),(0.31,0.69),(0.63,1.0)]):
        cc=c.crop((int(w*u0),max(0,p-95),int(w*u1),min(c.size[1],p+85)))
        cc=cc.resize((1400,int(1400*cc.size[1]/cc.size[0])))
        cc.save(f'{out}/{pre}_L{k:02d}{"abc"[j]}.jpg',quality=88)
