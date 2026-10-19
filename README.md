# BnF fr. 15573 f. 120 の暗号書簡（Mayenne–Forget の Cipher-2、1586年）の第一の読み

[English README](README.en.md)

フランス国立図書館 BnF Français 15573 f. 120 にある、差出人の分からない暗号書簡を、友清理士氏が復元した Mayenne–Forget の Cipher-2 の表と、Brett Burford 氏が同じ巻の別の書簡で作った鍵を使って読んだ記録です。

## 状態（2026-10-20）
- **部分的な読み**です。多くの行がフランス語の文として通りますが、値の分からない記号が13種19か所あり、読めない短い箇所も残っています（[docs/READING.md](docs/READING.md)、[docs/OPEN.md](docs/OPEN.md)）。差出人と日付は分かっていません。
- **先行との関係**：友清理士氏は f. 120 を Cipher-2 の書簡として挙げ、« Endorsement illegible (to me). Undeciphered. » としています（[Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm)、2023-09-23 更新）。2026-10-19〜20 に調べた範囲では、この書簡の読みは見つかっていません（調べた先は [SOURCES.md](SOURCES.md)）。鍵は先行研究のもの（友清氏の表、Brett Burford 氏の鍵）で、書き起こしと読みがこのリポジトリの新しい点です。
- **人は書き起こしを確かめていません。** 書き起こしは AI が画像から読んだものです。複数の AI の読みどうしの一致は、人の確認の代わりにはなりません。
- **数字**（詳しくは [docs/METHOD.md](docs/METHOD.md)）：
  | 項目 | 結果 |
  |---|---|
  | 鍵の文字記号の値をかき混ぜた対照実験（1,000回、3条件） | 本物の鍵以上は0回 |
  | 較正：当時の解読がある f. 104r の7行を、答えを見ずに読んだ記号の正確さ | Opus の読み手3人の多数決で90.5%（同じ値の別名も一致なら95.6%）。最初の較正（1人、1回）は86.9%（89.1%）。Burford 氏の同じ行での値は1回ずつ91.1〜93.5%、多数決92.9% |
  | 較正：文字の一致率（最初の較正、答えを見ない測定） | 70.6%（表の記号だけで62.9%） |
  | 2回目の書き起こし（Claude Sonnet、独立）と1回目の値の一致率 | 表88.0%・裏88.4% |
  | 3人の多数決（Claude Opus、独立）と1回目の値の一致率 | 表93.1%・裏88.0% |
- **AI の使用**：書き起こし・鍵の補い・解読・スクリプト・文書は Anthropic の Claude（Claude Code、Claude Opus 5.5）、2回目の書き起こしは Claude Sonnet、3人の多数決の読みは Claude Opus が行いました。人は、対象の選定、画像の保存、公開の判断をしました（[docs/METHOD.md](docs/METHOD.md) の「AI の使用」）。

## 資料
- BnF Français 15573（1586年の書簡集。友清氏の一覧では f. 7–8 が1586年8月の書簡）、Gallica ark:/12148/btv1b90618780 の246コマ（f. 120r、全面が暗号31行）と247コマ（f. 120v、暗号8行）。平文の部分はありません。

## 値が付いた記号の割合
| ページ | 記号の数 | 表の記号だけ | 表＋Burford 氏の照合 | この書簡での推定も合わせる |
|---|---|---|---|---|
| f. 120r | 885 | 89.2% | 96.7% | 98.2% |
| f. 120v | 216 | 85.6% | 97.7% | 98.6% |
| 計 | 1,101 | 88.5% | 96.9% | 98.3% |

## 更新履歴
- 2026-10-20（3人の多数決を受けた見直し、コミット 8f35df6）
  - 答えを見ていない Claude Opus の読み手3人に、f. 104r の18〜24行目と f. 120 を別々に読ませ、多数決をとった（`third/`、`src/vote.py`）。f. 104r での記号の正確さは、最初の較正の86.9%（同じ値の別名も一致で89.1%）から、多数決で90.5%（95.6%）。
  - 3人全員がそろって1回目と違う値を読んだ23か所を画像と文脈で見て、9か所を直した（« qu'il souffre ne soit a desseing »、« les efects »、« je vous puis dire »、« s[en] aler »、« qu'il saura ce que »、« de grands efects » など）。記号の数は1,103から1,101、値が付いた割合（推定も合わせる）は98.3%のまま。
  - 記号の正確さを Burford 氏の数え方にそろえて出せるようにした（`src/calib.py --lenient`）。
- 2026-10-20（較正と2回目の書き起こしを受けた見直し、コミット 441b3e9）
  - 較正（別のセッション、f. 104r の7行）を足し、参照の文字を画像で照らした（« qui reste icy » を « qui restent icy » に）。答えを見ない文字の一致率は70.6%。
  - 較正を受けて鍵を直した：＼ 形の記号は Burford 氏の curl（pour）だったので名前を付け直し、もとの curl は curlo（o）とした。λ は q と x の両方とした。縦線に輪の形（pdot）を友清氏の表の puis と同定した。値が付いた割合は、表の記号だけで87.9%から88.4%、推定も合わせて98.1%から98.3%。
  - 独立の2回目の書き起こし（Claude Sonnet、`second/`）と、その突き合わせ（`src/compare2.py`）を足した。
  - 英語版（docs/*.en.md、SOURCES.en.md、key.tsv の英語の列、スクリプトの英語の出力）を足した。
- 2026-10-20（最初の読み、コミット 6982c5d）
  - 2ページの書き起こし、鍵、解読、読み、鍵をかき混ぜた対照実験。値が付いた割合は、表の記号だけで87.9%、推定も合わせて98.1%。

## 内容（要約。読めた範囲から。主語や語の切れ目が不確かな箇所は、そう書いた）
- 「この君主（ce prince）」は、これまでになく不機嫌で腹を立てており、思いとどまらせる手立てがない。
- 金の話：会計官（tresorier）Bilart は、前月21日付の最後の便で、10日以上前に « trente mil [?] en or » があったと書いた。Guise 枢機卿は2日付の書簡で、« cinq mil [?] pour venir icy » が出たと書いた（partoient の読みは不確か）が、まだ知らせ（nouvelle と推定）はない。« 5千どころか10万5千 [?] でも立て直せない » ほどの状態にある（cent の読みは不確か）。
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
2. この書簡の文脈から、いくつかの記号の値を補った（ℓ 形＝i、縦線の下が右に巻く形（curlo）＝o、gg に横線＝nous など。`data/key.tsv` の inferred）。縦線に輪の形を友清氏の表の puis と同定した。λ は、友清氏の表の q と Burford 氏の鍵の x の両方に使われているとみた。
3. 較正（f. 104r の7行）、別の AI による独立の2回目の書き起こし、答えを見ていない読み手3人の多数決（`calib/`、`second/`、`third/`）。
4. 書簡の内容（上の要約）。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f120r.txt                # 推定も使う
python3 src/decode.py data/key.tsv data/transcription_f120r.txt --no-inferred  # 表と Burford 氏の照合だけ
python3 src/decode.py data/key.tsv data/transcription_f120r.txt --table-only   # 表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f120_all.txt 1000       # 対照実験（wordfreq が必要）
python3 src/calib.py data/key.tsv calib/transcription_f104r_l18-24.txt calib/ref_f104r_l18-24.txt --key-at-calibration  # 較正（文字、較正のときの鍵）
python3 src/calib.py --signs calib/transcription_f104r_l18-24.txt calib/ref_signs_f104r_burford.txt 1  # 較正（記号、厳密）
python3 src/calib.py --lenient data/key.tsv calib/transcription_f104r_l18-24.txt calib/ref_signs_f104r_burford.txt 1  # 較正（記号、Burford 氏にそろえた数え方）
python3 src/compare2.py data/transcription_f120r.txt second/transcription2_f120r.txt --key data/key.tsv  # 1回目と2回目の突き合わせ
python3 src/vote.py third/f104r_vote.txt third/f104r_pass1.txt third/f104r_pass2.txt third/f104r_pass3.txt  # 3人の多数決
python3 src/calib.py --lenient --no-alias data/key.tsv third/f104r_vote.txt calib/ref_signs_f104r_burford.txt 1  # 多数決の正確さ
python3 -m unittest discover -s tests
```

## AI の使用
冒頭の「状態」と [docs/METHOD.md](docs/METHOD.md) の「AI の使用」を見てください。人による書き起こしの照合はしていません。

## ファイル
| 場所 | 中身 |
|---|---|
| data/transcription_f120r.txt・f120v.txt | 記号名での書き起こし（行ごと） |
| data/transcription_f120_all.txt | 2ページをまとめたもの（表は c101〜、裏は c201〜） |
| data/key.tsv | 記号名→値。出典を table（友清氏の表）・burford（Burford 氏の照合）・inferred（この書簡での推定）・unknown で区別。注は日本語と英語 |
| data/decoded_*.txt | `src/decode.py` の出力 |
| docs/READING.md（英語版 READING.en.md） | 読み（句読点を補ったもの） |
| docs/METHOD.md（英語版 METHOD.en.md） | 方法、数字、較正、2回目の書き起こし、AI の使用、限界 |
| docs/OPEN.md（英語版 OPEN.en.md） | 値の分からない記号、読めない箇所、確かめていないこと |
| src/angle.py・deskew.py・tiles.py | 画像の傾きの推定・補正、行の切り出し |
| calib/transcription_f104r_l18-24.txt | 較正用の f. 104r 18〜24行目の書き起こし |
| calib/ref_f104r_l18-24.txt・ref_signs_f104r_burford.txt | 較正の参照（当時の解読の文字、Burford 氏の記号の書き起こし。CC BY 4.0） |
| src/calib.py | 較正の一致率の計算 |
| second/ | 2回目の書き起こし（Claude Sonnet、形だけで読んだもの）と、その解読 |
| src/compare2.py | 1回目と2回目の書き起こしの突き合わせ |
| third/ | Claude Opus の読み手3人の書き起こし（f. 104r の18〜24行目と f. 120）と多数決 |
| src/vote.py | 書き起こしの多数決 |
| SOURCES.md（英語版 SOURCES.en.md） | 出典と、先行の確かめ |

ライセンス：コードは MIT、自作の文書とデータは CC BY 4.0（[LICENSE](LICENSE)）。
