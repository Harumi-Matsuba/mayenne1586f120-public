import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

from decode import load_key, load_lines, decode  # noqa: E402

PAGES = ['f120r', 'f120v', 'f120_all']
KEY = os.path.join(ROOT, 'data', 'key.tsv')


def run_decode(page, *opts):
    return subprocess.run(
        [sys.executable, os.path.join(ROOT, 'src', 'decode.py'), KEY,
         os.path.join(ROOT, 'data', f'transcription_{page}.txt'), *opts],
        capture_output=True, text=True, check=True).stdout


class TestDecode(unittest.TestCase):
    def setUp(self):
        self.key, self.src = load_key(KEY)

    def test_key_sources(self):
        # 出典は table・burford・inferred・unknown のどれか
        self.assertTrue(set(self.src.values()) <= {'table', 'burford', 'inferred', 'unknown'})

    def test_table_only_drops_others(self):
        key_t, _ = load_key(KEY, table_only=True)
        self.assertEqual(key_t['9'], 'd')
        self.assertNotIn('g', key_t)       # burford
        self.assertNotIn('bslash', key_t)  # inferred
        self.assertNotIn('oo', key_t)      # unknown

    def test_decoded_files_are_current(self):
        # data/decoded_*.txt が、いまの鍵と書き起こしから作り直したものと一致する
        for p in PAGES:
            with open(os.path.join(ROOT, 'data', f'decoded_{p}.txt'), encoding='utf-8') as f:
                self.assertEqual(run_decode(p), f.read(), p)

    def test_all_is_both_pages(self):
        # まとめたファイルの記号の並びは、表と裏の書き起こしをつないだものと同じ
        r = [t for _, ts in load_lines(os.path.join(ROOT, 'data', 'transcription_f120r.txt')) for t in ts]
        v = [t for _, ts in load_lines(os.path.join(ROOT, 'data', 'transcription_f120v.txt')) for t in ts]
        a = [t for _, ts in load_lines(os.path.join(ROOT, 'data', 'transcription_f120_all.txt')) for t in ts]
        self.assertEqual(r + v, a)

    def test_coverage_numbers(self):
        # README・docs/METHOD.md に書いた割合
        self.assertIn('974 個（88.5%）', run_decode('f120_all', '--table-only'))
        self.assertIn('1067 個（96.9%）', run_decode('f120_all', '--no-inferred'))
        self.assertIn('1082 個（98.3%）', run_decode('f120_all'))

    def test_revised_values(self):
        # 較正と2回目の書き起こしを受けて直した値
        self.assertEqual(self.key['curl'], 'pour')
        self.assertEqual(self.key['curlo'], 'o')
        self.assertEqual(self.key['pdot'], 'puis')
        self.assertEqual(self.key['lambda'], 'q|x')
        self.assertNotIn('bslash', self.key)

    def test_known_words(self):
        # 文脈で確かめた語が出ること（鍵の取り違えの検出用）
        lines = load_lines(os.path.join(ROOT, 'data', 'transcription_f120_all.txt'))
        text = ' '.join(s for _, s in decode(lines, self.key)).lower()
        for w in ['ceprince', 'guise', 'biron', 'marsil', 'secretaire', 'tombe', 'epmaines', 'ranger', 'rupture']:
            self.assertIn(w, text)


class TestSecond(unittest.TestCase):
    def test_agreement_numbers(self):
        # docs/METHOD.md の「2回目の書き起こし」に書いた一致率
        for page, names, values in [('f120r', '81.7%', '88.0%'), ('f120v', '79.2%', '87.5%')]:
            out = subprocess.run(
                [sys.executable, os.path.join(ROOT, 'src', 'compare2.py'),
                 os.path.join(ROOT, 'data', f'transcription_{page}.txt'),
                 os.path.join(ROOT, 'second', f'transcription2_{page}.txt'), '--key', KEY],
                capture_output=True, text=True, check=True).stdout
            self.assertIn(f'一致率 {names}', out)
            self.assertIn(f'値の単位：記号', out)
            self.assertIn(f'一致率 {values}', out)

    def test_decoded2_is_current(self):
        out = subprocess.run(
            [sys.executable, os.path.join(ROOT, 'src', 'decode.py'), KEY,
             os.path.join(ROOT, 'second', 'transcription2_f120_all.txt')],
            capture_output=True, text=True, check=True).stdout
        with open(os.path.join(ROOT, 'second', 'decoded2_f120_all.txt'), encoding='utf-8') as f:
            self.assertEqual(out, f.read())


class TestCodex(unittest.TestCase):
    def test_codex_agreement(self):
        # docs/METHOD.md の「独立の2回目」に書いた値の一致率（同じ値の別名は一致とみなす）
        sys.path.insert(0, os.path.join(ROOT, 'src'))
        from decode import load_key
        import importlib.util
        spec = importlib.util.spec_from_file_location('vote', os.path.join(ROOT, 'src', 'vote.py'))
        vote = importlib.util.module_from_spec(spec); spec.loader.exec_module(vote)
        key, _ = load_key(KEY)
        V = lambda t: key.get(t, '[' + t + ']')
        for page, want in [('f120r', 0.932), ('f120v', 0.907)]:
            A = vote.load(os.path.join(ROOT, 'data', f'transcription_{page}.txt'))
            B = vote.load(os.path.join(ROOT, 'codex', f'transcription_codex_{page}.txt'))
            tot = dist = 0
            for lab in A:
                a = [V(t) for t in A[lab]]; b = [V(t) for t in B.get(lab, [])]
                tot += len(a); dist += vote.align(a, b)[2]
            self.assertAlmostEqual(1 - dist / tot, want, places=3)


class TestVote(unittest.TestCase):
    def test_vote_files_are_current(self):
        # third/*_vote.txt が、3人の読みから src/vote.py で作り直したものと一致する
        import tempfile
        for page in ['f104r', 'f120r', 'f120v']:
            with tempfile.TemporaryDirectory() as d:
                out = os.path.join(d, 'v.txt')
                subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'vote.py'), out] +
                               [f'third/{page}_pass{k}.txt' for k in (1, 2, 3)],
                               capture_output=True, text=True, check=True, cwd=ROOT)
                with open(out, encoding='utf-8') as f1, open(os.path.join(ROOT, 'third', f'{page}_vote.txt'), encoding='utf-8') as f2:
                    self.assertEqual(f1.read(), f2.read(), page)

    def test_vote_accuracy_on_f104r(self):
        # docs/METHOD.md の「3人の読み手の多数決」に書いた正確さ
        run = lambda *a: subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'calib.py'), *a],
                                        capture_output=True, text=True, check=True, cwd=ROOT).stdout
        args = [KEY, 'third/f104r_vote.txt', 'calib/ref_signs_f104r_burford.txt', '1']
        self.assertIn('= 90.5%', run('--lenient', '--no-alias', *args))
        self.assertIn('= 95.6%', run('--lenient', *args))

    def test_vote_example(self):
        sys.path.insert(0, os.path.join(ROOT, 'src'))
        from vote import vote_line
        self.assertEqual(vote_line([['a', 'b', 'c', 'd'], ['a', 'b', 'q', 'd'], ['a', 'b', 'c', 'd', 'e']])[0], ['a', 'b', 'c', 'd'])
        self.assertEqual(vote_line([['x', 'y', 'z'], ['x', 'k', 'y', 'z'], ['x', 'k', 'y']])[0], ['x', 'k', 'y', 'z'])


class TestCalib(unittest.TestCase):
    def run_calib(self, *args):
        return subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'calib.py'), *args],
                              capture_output=True, text=True, check=True, cwd=ROOT).stdout

    def test_calib_numbers(self):
        # docs/METHOD.md の「較正」に書いた数字
        args = [KEY, 'calib/transcription_f104r_l18-24.txt', 'calib/ref_f104r_l18-24.txt']
        self.assertIn('= 70.6%', self.run_calib(*args, '--key-at-calibration'))  # 答えを見ない測定
        self.assertIn('= 62.9%', self.run_calib(*args, '--key-at-calibration', '--table-only'))
        self.assertIn('= 73.4%', self.run_calib(*args))  # 較正を受けて直した鍵
        self.assertIn('= 65.7%', self.run_calib(*args, '--table-only'))
        out = self.run_calib('--signs', 'calib/transcription_f104r_l18-24.txt', 'calib/ref_signs_f104r_burford.txt', '1')
        self.assertIn('参照の記号 137、書き起こしの記号 154、編集距離 30', out)
        args2 = [KEY, 'calib/transcription_f104r_l18-24.txt', 'calib/ref_signs_f104r_burford.txt', '1']
        self.assertIn('= 89.1%', self.run_calib('--lenient', *args2))
        self.assertIn('= 86.9%', self.run_calib('--lenient', '--no-alias', *args2))

    def test_slash_and_interlinear_skipped(self):
        # 区切りの / と行間の書き込み ^(2.) は、解読の文字にも ? にもならない
        sys.path.insert(0, os.path.join(ROOT, 'src'))
        from calib import decoded_stream
        key, _ = load_key(KEY)
        lines = load_lines(os.path.join(ROOT, 'calib', 'transcription_f104r_l18-24.txt'))
        s = decoded_stream(lines, key)
        self.assertTrue(s.startswith('terpour'))
        self.assertEqual(len(s), 220)  # curl＝pour の4文字を含む
        self.assertEqual(s.count('?'), 4)  # 読めない記号（書き起こしの単独の ?）の数

if __name__ == '__main__':
    unittest.main()
