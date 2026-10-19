# EN: Majority vote of three (or more) independent sign transcriptions, line by line. Each line is aligned to a pivot (the reading whose line is closest to the others) by edit distance; at each pivot position the name chosen by most readers wins (a gap counts as a vote for "no sign"); a tie keeps the pivot's name. Insertions found by a majority of the other readers at the same place are added. Usage: python3 src/vote.py out.txt pass1.txt pass2.txt pass3.txt
# 3つ（以上）の独立の書き起こしを、行ごとに多数決する。
# 使い方: python3 src/vote.py 出力 読み手1 読み手2 読み手3
# 各行で、他の読みとの距離の合計がいちばん小さい読みを軸にし、他の読みを編集距離で軸に合わせる。
# 軸の各位置で、いちばん多くの読み手が選んだ名前を採る（合わせた先が無い＝「記号なし」も1票）。同数なら軸の名前を残す。
# 軸に無く、他の読み手の過半数が同じ位置に同じ記号を足しているときは、それを加える。
# 名前の末尾の ? は外して数える。行間の書き込み ^(…) と消した記号 {…}、<…>、区切りの / は除く。
import sys, re
from collections import Counter

def load(path):
    out = {}
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'(c\d+):\s*(.*)', ln)
        if not m:
            continue
        body = re.sub(r'\^\([^)]*\)|\{[^}]*\}|<[^>]*>', ' ', m.group(2))
        toks = [t[:-1] if t.endswith('?') and len(t) > 1 else t for t in body.split() if t not in ('/', '|')]
        out[m.group(1)] = toks
    return out

def align(a, b):
    # a（軸）の各位置に b の記号を対応させる。返り値：軸の位置 i ごとの b の記号（無ければ None）と、
    # 軸の位置 i の前に b が足した記号のリスト
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): d[i][0] = i
    for j in range(m + 1): d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (a[i-1] != b[j-1]))
    sub = [None] * n
    ins = [[] for _ in range(n + 1)]
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i-1][j-1] + (a[i-1] != b[j-1]):
            sub[i-1] = b[j-1]; i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i-1][j] + 1:
            i -= 1
        else:
            ins[i].insert(0, b[j-1]); j -= 1
    return sub, ins, d[n][m]

def vote_line(readings):
    # 軸：他の読みとの距離の合計が最小のもの
    best = min(range(len(readings)), key=lambda k: sum(align(readings[k], readings[o])[2] for o in range(len(readings)) if o != k))
    piv = readings[best]
    others = [align(piv, readings[o]) for o in range(len(readings)) if o != best]
    need = len(readings) // 2 + 1
    out = []
    for i in range(len(piv) + 1):
        # 軸の位置 i の前への挿入：他の読み手のうち、同じ記号を足したのが過半数（軸を含めた全体で need）なら加える
        cnt = Counter()
        for sub, ins, _ in others:
            for t in set(ins[i]):
                cnt[t] += 1
        for t, c in cnt.items():
            if c >= need:
                out.append(t)
        if i == len(piv):
            break
        votes = Counter([piv[i]] + [sub[i] for sub, _, _ in others])
        top = max(votes.values())
        winners = [t for t, c in votes.items() if c == top]
        choice = piv[i] if piv[i] in winners else winners[0]
        if choice is not None:
            out.append(choice)
    return out, best

if __name__ == '__main__':
    out_path, paths = sys.argv[1], sys.argv[2:]
    passes = [load(p) for p in paths]
    labels = sorted(set().union(*passes), key=lambda s: int(s[1:]))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f'# {len(paths)} つの読み（{", ".join(paths)}）の多数決（src/vote.py）\n')
        for lab in labels:
            rs = [p.get(lab, []) for p in passes]
            v, best = vote_line(rs)
            f.write(f'{lab}: ' + ' '.join(v) + '\n')
    print(f'{len(labels)} 行を {out_path} に書いた')
