# 出典

[English](SOURCES.en.md)

## 一次資料（リポジトリには含めていない）
- **BnF, Français 15573**
  - Gallica ark:/12148/btv1b90618780
  - 246コマ：f. 120r（全面が暗号31行）。https://gallica.bnf.fr/ark:/12148/btv1b90618780/f246.item
  - 247コマ：f. 120v（暗号8行）。https://gallica.bnf.fr/ark:/12148/btv1b90618780/f247.item
  - 213コマ：f. 104r（較正に使った。暗号の18〜24行目）。https://gallica.bnf.fr/ark:/12148/btv1b90618780/f213.item

画像は再配布していません。コマ番号で参照してください。Source gallica.bnf.fr / BnF.

## 鍵
- 友清理士（Satoshi Tomokiyo）, *French ciphers during the Reigns of Charles IX and Henry III*（Cryptiana）
  - https://cryptiana.web.fc2.com/code/henryiii.htm （Last-Modified 2023-09-23）
  - BnF fr. 15573 の一覧：« f.120 (p.248) Endorsement illegible (to me). Undeciphered. Uses Mayenne-Forget's Cipher-2. »
  - 表の画像：https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png （このリポジトリには含めていない）
- Brett Burford, *First reading of the whole cipher letter BnF fr. 15573 f. 385 (Mayenne-Forget Cipher-2, 1586)*
  - https://github.com/BravoBravoIX/mayenne-forget-1586-cipher-reading （コミット cc0daf749aecebae0e7eb163035abe9ba679a9d3、2026-10-19、文書とデータは CC BY 4.0）
  - `data/key-cipher2.json`：`data/key.tsv` の table・burford の行は、この鍵の値と出どころの印を写したもの（4列目に原文の印を残した）。
  - `method/sheet-v3.png`：記号の名前の見本。画像はこのリポジトリに含めていない。
  - `data/known-text/f104r-decipherment.txt`（コミット cc0daf74）：f. 104r の当時の解読を同氏の側で目読みしたもの。その一部を `calib/ref_f104r_l18-24.txt` に写した（較正の参照）。写した後、213コマの画像と照らし、« qui reste icy » を « qui restent icy » に直した（2026-10-20）。
  - `data/known-text/ref-104r-l18-24.txt`（コミット 22ab58c39dbd98a853044349d98294af93124e30、2026-10-19）：f. 104r の暗号の記号の書き起こし。`calib/ref_signs_f104r_burford.txt` にそのまま写した（較正の参照）。

## 2回目の書き起こし
- `second/transcription2_f120r.txt`・`f120v.txt`：Anthropic の Claude Sonnet が、1回目の書き起こしを見ずに、画像の切り出しと Burford 氏の見本表、記号の名前と形の説明だけから読んだもの（2026-10-20）。読み手を変えた独立の読みとして、1回目と突き合わせた（[docs/METHOD.md](docs/METHOD.md)）。

## 方法の手本
- Harumi-Matsuba, *matignon1586-public*（同じ Cipher-2 の書簡 BnF fr. 15572 ff. 218–219 の読み）
  - https://github.com/Harumi-Matsuba/matignon1586-public
  - スクリプト（`src/decode.py`・`src/control.py`・`src/calib.py`）を元にした。較正のやり方も同リポジトリの `docs/METHOD.md` に合わせた（同リポジトリの f. 103v での一致率は74.8%）。

## 先行の確かめ
見つからないことは、手を付けた人がいないことの証明にはなりません。

| 調べた先 | 日付・版 | 結果 |
|---|---|---|
| Cryptiana（henryiii.htm） | Last-Modified 2023-09-23 | f. 120 は « Undeciphered » |
| Cryptiana（unsolved.htm、ai.htm） | Last-Modified 2026-10-13、2026-10-19 | 確かめたのは更新日だけ。本文は読んでいない |
| D. Bourdeau, cyphersolver（https://github.com/dbourdeau/cyphersolver ） | origin/main 0258b8ab（2026-10-18）、issue・PR は #48 まで（2026-10-20 に確認） | catalogue.json と targets/ の NOTES に「15573」はない。「15573」を含む9ファイル（友清氏のページの写し、Gallica の検索結果など）にも、その前後に f. 120 の記述はない。issue・PR の題名にもない |
| Brett Burford（GitHub BravoBravoIX）のリポジトリ一覧と、fr. 15573 の2リポジトリ（f. 385、ff. 379–381） | 最新 2026-10-19T12:24Z（2026-10-20 に確認） | f. 120 のリポジトリはない。2リポジトリのファイル名に「120」を含むものはない |
| NoAutopilot/cipher-lab | 2026-10-20 に確認 | issue とコミットの検索で「15573」は0件 |
| pangoleen/cipher-readings | 2026-10-20 に確認 | fr. 15573 のフォルダはない |
| Cryptoole（https://cryptoole.satoru.net/api.cgi ） | 2026-10-20、全854件 | 「15573」「Mayenne」「Forget」「Marsil」を含む項目はない |
| GitHub のリポジトリ検索（15573、mayenne cipher、forget 1586）とコード検索（15573 "f. 120" など） | 2026-10-20 | 関係するのは Burford 氏のリポジトリと、Harumi-Matsuba/matignon1586-public だけ |
| ウェブ検索 | 2026-10-19、3回（この作業の前の会話で実施） | 該当なし |

調べていない先：DECODE の検索画面、Lasry 氏の論文一覧、Cryptiana のブログ。
