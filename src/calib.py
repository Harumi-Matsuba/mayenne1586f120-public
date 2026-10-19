# 較正：当時の解読がある行で、書き起こし＋鍵から出した文字列と、当時の解読を文字の単位で突き合わせる。
# 使い方: python3 src/calib.py data/key.tsv calib/transcription_f104r_l18-24.txt calib/ref_f104r_l18-24.txt [--table-only]
# 参照の平文は、書き起こしの最初の行から最後の行までに当たる当時の解読（# で始まる行は読まない）。
# 文字は小文字にし、アクセントを外し、j→i、v→u に寄せ、文字以外を除いて比べる。
# 区切りの斜線（/ と |）は飛ばす。行間の書き込み ^(…) と消した記号 {…} は decode.load_lines が除く。
# 値の分からない記号は ? として残し（必ず不一致）、i|s のように値が2つある記号は最初の値を使う。
import sys, re, unicodedata
from decode import load_key, load_lines, norm

def letters(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z?]', '', s)

def decoded_stream(lines, key):
    out = []
    for _, toks in lines:
        for t in toks:
            if t in ('|', '/'):
                continue
            v = key.get(norm(t))
            out.append('?' if v is None or v == '?' else v.split('|')[0])
    return letters(''.join(out))

def align(a, b):
    # レーベンシュタイン距離と、置換・脱落・挿入の内訳
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): d[i][0] = i
    for j in range(m + 1): d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (a[i-1] != b[j-1]))
    i, j, sub, dele, ins, ops = n, m, 0, 0, 0, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i-1][j-1] + (a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]:
                sub += 1; ops.append((i-1, a[i-1], b[j-1]))
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i-1][j] + 1:
            dele += 1; ops.append((i-1, a[i-1], '-')); i -= 1
        else:
            ins += 1; ops.append((i, '-', b[j-1])); j -= 1
    return d[n][m], sub, dele, ins, ops[::-1]

def sign_lines(path):
    # Burford 氏の記号の参照：「18 g 9 lambda …」の形。a|b はどちらでも一致とする。区切りの / は飛ばす
    out = {}
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'(\d+)\s+(.*)', ln)
        if m:
            out[int(m.group(1))] = [t.split('|') for t in m.group(2).split() if t != '/']
    return out

def compare_signs(hyp_path, ref_path, offset):
    # 書き起こしの c(n+offset) 行を、参照の n 行と記号の単位で突き合わせる
    hyp = {int(lab[1:]): [norm(t) for t in toks if t not in ('|', '/')] for lab, toks in load_lines(hyp_path)}
    ref = sign_lines(ref_path)
    a, b = [], []
    for n in sorted(ref):
        if n + offset in hyp:
            a += ref[n]; b += hyp[n + offset]
    # 参照の要素は候補のリスト。一致は候補のどれかと同じとき
    la, lb = len(a), len(b)
    d = [[0] * (lb + 1) for _ in range(la + 1)]
    for i in range(la + 1): d[i][0] = i
    for j in range(lb + 1): d[0][j] = j
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (b[j-1] not in a[i-1]))
    i, j, ops = la, lb, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i-1][j-1] + (b[j-1] not in a[i-1]):
            if b[j-1] not in a[i-1]: ops.append(('|'.join(a[i-1]), b[j-1]))
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i-1][j] + 1:
            ops.append(('|'.join(a[i-1]), '-')); i -= 1
        else:
            ops.append(('-', b[j-1])); j -= 1
    return la, lb, d[la][lb], ops[::-1]

if __name__ == '__main__' and '--signs' in sys.argv:
    # 使い方: python3 src/calib.py --signs 書き起こし 参照の記号 行のずれ（参照の n 行 = 書き起こしの n+ずれ 行）
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    la, lb, dist, ops = compare_signs(args[0], args[1], int(args[2]))
    print(f'参照の記号 {la}、書き起こしの記号 {lb}、編集距離 {dist}')
    print(f'記号の一致率 1−距離/参照 = {1 - dist/la:.1%}')
    print('違い（参照>書き起こし）:', ' '.join(f'{r}>{h}' for r, h in ops))
elif __name__ == '__main__':
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    key, _ = load_key(args[0], '--table-only' in sys.argv)
    hyp = decoded_stream(load_lines(args[1]), key)
    ref = letters(''.join(l for l in open(args[2], encoding='utf-8') if not l.startswith('#')))
    dist, sub, dele, ins, ops = align(ref, hyp)
    print(f'参照の文字数 {len(ref)}、解読の文字数 {len(hyp)}')
    print(f'編集距離 {dist}（置換 {sub}、解読側の脱落 {dele}、解読側の余分 {ins}）')
    print(f'文字の一致率 1−距離/参照 = {1 - dist/len(ref):.1%}')
    print('違い（参照の位置、参照、解読）:', ' '.join(f'{p}:{r}>{h}' for p, r, h in ops))
