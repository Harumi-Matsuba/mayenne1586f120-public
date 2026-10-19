# EN: Compare the first and second transcriptions line by line, by sign name and (with --key) by value. Usage: python3 src/compare2.py data/transcription_f120r.txt second/transcription2_f120r.txt [--detail] [--key data/key.tsv]
# 1回目と2回目の書き起こしを、行ごとに記号の単位で突き合わせる
# 使い方: python3 src/compare2.py data/transcription_f120r.txt second/transcription2_f120r.txt [--detail] [--key data/key.tsv]
# （2回目のページ別のファイルは改名前の名前なので、bslash→curl、curl→curlo と読み替える。second/transcription2_f120_all.txt は改名済みなので使わない）
import sys, re
sys.path.insert(0, sys.argv[0].rsplit('/',1)[0] if '/' in sys.argv[0] else '.')
REN = {'bslash': 'curl', 'curl': 'curlo'}   # 2回目は改名前の名前の一覧を使った
def toks(path, second=False):
    out = {}
    for l in open(path, encoding='utf-8'):
        m = re.match(r'(c\d+):\s*(.*)', l)
        if not m: continue
        body = re.sub(r'\^\([^)]*\)|\{[^}]*\}|<[^>]*>', ' ', m.group(2))
        ts = []
        for t in body.split():
            if t in ('/', '|'): continue
            t = t[:-1] if t.endswith('?') and len(t) > 1 else t
            if second: t = REN.get(t, t)
            ts.append(t)
        out[m.group(1)] = ts
    return out
def align(a, b):
    n, m = len(a), len(b)
    d = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): d[i][0] = i
    for j in range(m+1): d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+(a[i-1] != b[j-1]))
    i, j, ops = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i-1][j-1]+(a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]: ops.append((i-1, a[i-1], b[j-1]))
            i, j = i-1, j-1
        elif i > 0 and d[i][j] == d[i-1][j]+1:
            ops.append((i-1, a[i-1], '-')); i -= 1
        else:
            ops.append((i, '-', b[j-1])); j -= 1
    return d[n][m], ops[::-1]
A, B = toks(sys.argv[1]), toks(sys.argv[2], True)
tot = dist = 0
from collections import Counter
pairs = Counter()
for lab in A:
    dd, ops = align(A[lab], B.get(lab, []))
    tot += len(A[lab]); dist += dd
    for _, x, y in ops: pairs[(x, y)] += 1
    if '--detail' in sys.argv:
        print(lab, f'{len(A[lab])}記号 距離{dd}:', ' '.join(f'{p}:{x}>{y}' for p, x, y in ops))
print(f'1回目の記号 {tot}、編集距離 {dist}、一致率 {1-dist/tot:.1%}')
print(f'EN: names: first {tot} signs, edit distance {dist}, agreement {1-dist/tot:.1%}')
print('多い食い違い（1回目>2回目）:', ', '.join(f'{x}>{y} {n}' for (x, y), n in pairs.most_common(25)))

# 値の単位でも比べる（鍵で値に直してから突き合わせる。値が同じ別名は一致とみなす）
if '--key' in sys.argv:
    from decode import load_key
    key, _ = load_key(sys.argv[sys.argv.index('--key')+1])
    def val(t): return key.get(t, '[' + t + ']')
    tot = dist = 0; vp = Counter(); ex = {}
    for lab in A:
        a = [val(t) for t in A[lab]]; b = [val(t) for t in B.get(lab, [])]
        dd, ops = align(a, b); tot += len(a); dist += dd
        for p, x, y in ops:
            vp[(x, y)] += 1; ex.setdefault((x, y), []).append(f'{lab}:{p}')
    print(f'値の単位：記号 {tot}、編集距離 {dist}、一致率 {1-dist/tot:.1%}')
    print(f'EN: values: {tot} signs, edit distance {dist}, agreement {1-dist/tot:.1%}')
    print('値が変わる食い違い（1回目>2回目）:', ', '.join(f'{x}>{y} {n} ({" ".join(ex[(x,y)][:4])})' for (x, y), n in vp.most_common(20)))
