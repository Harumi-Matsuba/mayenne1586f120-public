# BnF fr. 15573 f. 120 の暗号書簡（Mayenne–Forget の Cipher-2、1586年）の第一の読み

[English README](README.en.md)

フランス国立図書館 BnF Français 15573 f. 120 にある、差出人の分からない暗号書簡を、友清理士氏が復元した Mayenne–Forget の Cipher-2 の表と、Brett Burford 氏が同じ巻の別の書簡で作った鍵を使って読んだ記録です。

- 資料：BnF Français 15573（1586年の書簡集。友清氏の一覧では f. 7–8 が1586年8月の書簡）、Gallica ark:/12148/btv1b90618780 の246コマ（f. 120r、全面が暗号31行）と247コマ（f. 120v、暗号8行）。平文の部分はありません。
- 先行：友清理士氏は f. 120 を Cipher-2 の書簡として挙げ、« Endorsement illegible (to me). Undeciphered. » としている（[Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm)、2023-09-23 更新）。2026-10-19〜20 に調べた範囲では、この書簡の読みは見つかっていない（調べた先は [SOURCES.md](SOURCES.md)）。

## 現状（v0.1、部分的）
| ページ | 記号の数 | 表の記号だけで値が付いた割合 | 表＋Burford 氏の照合 | この書簡での推定も合わせる |
|---|---|---|---|---|
| f. 120r | 887 | 88.6% | 96.3% | 98.0% |
| f. 120v | 216 | 85.2% | 97.2% | 98.6% |
| 計 | 1,103 | 87.9% | 96.5% | 98.1% |

- 鍵の文字記号の値をかき混ぜた対照実験（1,000回）では、3つの条件とも、本物の鍵以上にフランス語らしくなったことは1回もありませんでした（[docs/METHOD.md](docs/METHOD.md)）。
- 多くの行がフランス語の文として通ります（[docs/READING.md](docs/READING.md)）。値の分からない記号は14種21か所あり、読めない短い箇所も残っています（[docs/OPEN.md](docs/OPEN.md)）。
- **較正はしていません。** 書き起こしは1回の目視で、当時の解読がある書簡で正確さを測っていません。理由は [docs/METHOD.md](docs/METHOD.md) の「限界」にあります。細部には誤りを含む前提で使ってください。

## 内容（要約。読めた範囲から。主語や語の切れ目が不確かな箇所は、そう書いた）
- 「この君主（ce prince）」は、これまでになく不機嫌で腹を立てており、思いとどまらせる手立てがない。
- 金の話：会計官（tresorier）Bilart は、前月21日付の最後の便で、10日以上前に « trente mil [?] en or » があったと書いた。Guise 枢機卿は2日付の書簡で、« cinq mil [?] » がこちらへ向けて出たと書いた（partoient の読みは不確か）が、まだ知らせ（nouvelle と推定）はない。« 5千どころか10万5千 [?] でも立て直せない » ほどの状態にある（cent の読みは不確か）。
- Biron 元帥を引き留める望みは、もうない。Biron の側からは、退く途中で通りがけに会うのはたやすいだろう、という趣旨の便りがあった（主語と « chez » の後は不確か）。
- 今夜、軍の代表（deputés de l'armée）がここに来ている。こちらは何もできないほど弱った集まりである。秘書 La Marsilière の [?]（手紙の類か）が手に入り、事情（finances など）が詳しく分かる。
- この軍の解体は損である。あと6週間保てば大きな成果が出せたはずで、敵がこれほど驚いたことはなかった。

［?］は値の分からない記号（mil の後の ∞ 形など）。詳しくは [docs/READING.md](docs/READING.md)。差出人と日付は、まだ分かりません。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- Cipher-2 の表：友清理士氏の復元（[henryiii_MayenneForget2.png](https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png)）。表の画像はこのリポジトリに含めていません。
- 記号の名前と、表にない記号の値：Brett Burford 氏の見本表と鍵（[BravoBravoIX/mayenne-forget-1586-cipher-reading](https://github.com/BravoBravoIX/mayenne-forget-1586-cipher-reading) の `method/sheet-v3.png` と `data/key-cipher2.json`、コミット cc0daf74、CC BY 4.0）。同氏が同じ巻の当時の解読と照らして出した値（E・F）を使っています。
- この書簡が Cipher-2 で、未解読であること：友清理士氏。

**この読みで加えたこと**
1. 2ページの記号を、Burford 氏の記号名で行ごとに書き起こした（`data/transcription_*.txt`）。見本にない記号には名前を足した。
2. この書簡の文脈から、いくつかの記号の値を補った（ℓ 形＝i、＼ 形＝a、gg に横線＝nous など。`data/key.tsv` の inferred）。また、Burford 氏の鍵と違う値で読んだ記号が2つある（curl を pour でなく o、λ を x でなく q）。
3. 書簡の内容（上の要約）。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f120r.txt                # 推定も使う
python3 src/decode.py data/key.tsv data/transcription_f120r.txt --no-inferred  # 表と Burford 氏の照合だけ
python3 src/decode.py data/key.tsv data/transcription_f120r.txt --table-only   # 表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f120_all.txt 1000       # 対照実験（wordfreq が必要）
python3 -m unittest discover -s tests
```

## AI の使用
書き起こし・鍵の補い・解読・スクリプト・文書は、Anthropic の Claude（Claude Code、Claude Opus 5.5）が行いました。対象の選定、画像の保存、公開の判断は人が行いました。人による書き起こしの照合はしていません。詳しくは [docs/METHOD.md](docs/METHOD.md)。

## ファイル
| 場所 | 中身 |
|---|---|
| data/transcription_f120r.txt・f120v.txt | 記号名での書き起こし（行ごと） |
| data/transcription_f120_all.txt | 2ページをまとめたもの（表は c101〜、裏は c201〜） |
| data/key.tsv | 記号名→値。出典を table（友清氏の表）・burford（Burford 氏の照合）・inferred（この書簡での推定）・unknown で区別 |
| data/decoded_*.txt | `src/decode.py` の出力 |
| docs/READING.md | 読み（句読点を補ったもの） |
| docs/METHOD.md | 方法、数字、AI の使用、限界 |
| docs/OPEN.md | 値の分からない記号、読めない箇所、確かめていないこと |
| src/angle.py・deskew.py・tiles.py | 画像の傾きの推定・補正、行の切り出し |
| SOURCES.md | 出典と、先行の確かめ |

ライセンス：コードは MIT、自作の文書とデータは CC BY 4.0（[LICENSE](LICENSE)）。
