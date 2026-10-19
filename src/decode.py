# key.tsv を transcription_*.txt に当てて平文を出す。
# 使い方: python3 src/decode.py data/key.tsv data/transcription_f120r.txt [--table-only|--no-inferred]
#   --table-only  : 出典が table（友清氏の表）の記号だけを使う
#   --no-inferred : table と burford（Burford 氏の照合）の記号だけを使う
import sys, re

def load_key(path, table_only=False):
    key, src = {}, {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('# ') or not ln.strip():
            continue
        p = ln.rstrip('\n').split('\t')
        key[p[0]], src[p[0]] = p[1], p[2]
    if table_only:
        key = {k: v for k, v in key.items() if src[k] == 'table'}
    elif '--no-inferred' in sys.argv:
        key = {k: v for k, v in key.items() if src[k] in ('table', 'burford')}
    key = {k: v for k, v in key.items() if v != '?'}
    return key, src

def load_lines(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'(c\d+):\s*(.*)', ln)
        if m:
            body = re.sub(r'\^\([^)]*\)|\{[^}]*\}', ' ', m.group(2))  # 行間の書き込みと消した記号は除く
            out.append((m.group(1), body.split()))
    return out

def norm(tok):
    return tok[:-1] if tok.endswith('?') and len(tok) > 1 else tok

def decode(lines, key):
    res = []
    for lab, toks in lines:
        s = []
        for t in toks:
            if t in ('|', '/'):
                s.append(' ')
                continue
            v = key.get(norm(t))
            if v is None:
                s.append('[?]')
            elif '|' in v:
                s.append('(' + v + ')')
            elif len(v) > 1 or t.startswith('=') or t.startswith('.'):
                s.append(' ' + v.upper() + ' ')
            else:
                s.append(v)
        res.append((lab, re.sub(r'\s+', ' ', ''.join(s)).strip()))
    return res

if __name__ == '__main__':
    key, src = load_key(sys.argv[1], '--table-only' in sys.argv)
    lines = load_lines(sys.argv[2])
    n_all = sum(1 for _, ts in lines for t in ts if t not in ('|', '/'))
    n_ok = sum(1 for _, ts in lines for t in ts if t not in ('|', '/') and norm(t) in key)
    for lab, s in decode(lines, key):
        print(lab, s)
    label = '表（Tomokiyo）の記号だけで' if '--table-only' in sys.argv else ('表と Burford の照合で' if '--no-inferred' in sys.argv else '表・Burford・推定を合わせて')
    print(f'# 記号 {n_all} 個のうち、{label}値が付いたもの {n_ok} 個（{n_ok/n_all:.1%}）')
