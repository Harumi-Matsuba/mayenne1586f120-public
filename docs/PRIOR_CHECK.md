# 先行の確かめ（BnF fr. 15573 f. 120、2026-10-20）

[English](PRIOR_CHECK.en.md)

## 結論
- **区分：見つからない。** 下の先を調べた範囲では、この書簡（BnF fr. 15573 f. 120r–v）の暗号を読んだもの、暗号文と平文の対応を示したもの、この書簡の平文（当時の解読や刊本）は見つからなかった。
- 見つからないことは、誰も読んでいないことの証明にはならない。このリポジトリの読みを「初めて」とは言わない。
- **この確かめの限界：** RULES.md §2.2 の5 は、解いたのとは別のセッションが、否定するつもりで探すことを求めている。この確かめは、ユーザーの指示で、書簡を読んだのと同じ Claude Code のセッションが行った。そのため、この条件は満たしていない。解いた側の見落としを、同じ側が探したことになる。

## 調べた先（2026-10-20 01:00〜02:30 JST）
| 先 | 日付・版 | 調べ方 | 結果 |
|---|---|---|---|
| Cryptiana（友清理士氏）henryiii.htm | Last-Modified 2023-09-23 | fr. 15573 の一覧を読んだ | f. 120 は « Endorsement illegible (to me). Undeciphered. Uses Mayenne-Forget's Cipher-2. » |
| Cryptiana unsolved.htm・ai.htm・verification.htm・GL.htm | 2026-10-13・10-19・10-15・10-15 | 本文で「15573」「Marsil」「Montablay」「Bilart」を探した | GL.htm（Lasry 氏の解読の一覧）に fr. 15573 f. 127（Duval から Villeroi へ）があるだけ。f. 120 はない |
| Cryptiana のブログ（cryptiana.blogspot.com） | フィードの最近100件（2025-07-06〜2026-10-15） | 同じ語と「Mayenne」「Forget」 | 該当なし |
| D. Bourdeau, cyphersolver（台帳） | origin/main 0258b8ab（2026-10-18） | `git grep` で「15573」「marsil」「montablaye」「bilart」 | f. 120 の項目はない。当たったのは別の文書の同じ語（docs/navarre1586.html の « le Sr de Vesin de la Marsilliere »、targets/matignon1586 の語の一覧など） |
| 同 issue・PR | #49 まで（2026-10-19） | 題名と本文で「15573」「f. 120」「Marsil」「Montablaye」 | 当たったのは #44・#46（Burford 氏、fr. 15573 の別の葉）と #49（私たち、fr. 15572） |
| Brett Burford 氏（GitHub BravoBravoIX） | リポジトリ一覧の最新 2026-10-19T12:24Z | 一覧と、fr. 15573 の2リポジトリ | f. 120 のリポジトリはない |
| NoAutopilot/cipher-lab | 2026-10-20 | issue・コミット・コード検索で「15573」。コード検索で当たった10ファイルのうち、関係しそうな5ファイル（LESSONS-TOMOKIYO.md、sources/pools-scout/2026-10-03/P1.md、ciphers/matignon-mayenne-1586 の NOTES.md と second-opinions、sources/cryptiana/CRYPTO-INDEX.tsv）の本文 | issue #72 は私たちの名義の fr. 15572 の報告。5ファイルの「15573」は、目録の写し、Lasry 氏の f. 127、「fr. 15573 の葉を見るべき」というメモで、f. 120 の読みはない。残る5ファイルは別の暗号のフォルダ（baluze167・sp99・armstrong）で、本文は読んでいない |
| pangoleen/cipher-readings | 2026-10-20 | フォルダの一覧と issue 検索 | fr. 15573 はない |
| Cryptoole（https://cryptoole.satoru.net/api.cgi ） | 2026-10-20、全854件 | 「15573」「Mayenne」「Forget」「Marsil」「Montablay」「Bilart」 | 該当なし |
| DECODE（aaymeloglu/unsolved-ciphers の decode-catalog.csv、DECODE の目録の写し） | 10,106件、2026-10-09 更新 | 「15573」「Mayenne」「Forget」 | 該当なし |
| BnF の目録（Archives et manuscrits、Français 15573） | 2026-10-20 に取得 | 内容の説明を読んだ | f. 120 の項目はなく、解読（déchiffrement）の記載もない。近くの葉では f. 114・118（L'Aubespine-Chasteauneuf）、f. 119（ナバール王との交渉の文書）が挙がっている |
| GitHub のコード検索 | 2026-10-20 | « Marsiliere »、« Marsilliere »、« Montablaye »、« Mayenne Forget Cipher-2 » | « Marsilliere » は Armael/voyageur と cyphersolver（別の文書）、« Mayenne Forget Cipher-2 » は cipher-lab と cyphersolver（上のとおり）。« Marsiliere »・« Montablaye » は0件 |
| GitHub のリポジトリ検索 | 2026-10-20 | 「mayenne cipher」「15573」「forget 1586」「henri III cipher」 | 関係するのは Burford 氏のリポジトリと、このリポジトリだけ |
| ウェブ検索（英・仏・日） | 2026-10-20、7回 | 所蔵記号と f. 120、平文の語句（« Marsillière »、« Montablaye »、« Bilart »、« six sepmaines … estonnés »）、日本語 | 該当なし |

## 調べられなかった先・調べていない先
- Gallica の全文検索：curl では 403（Cloudflare）で、使っていない。
- DECODE の検索画面そのもの（写しの目録だけを見た）。
- 刊本の史料集（Berger de Xivrey『Recueil des lettres missives de Henri IV』、Archives historiques de la Gironde、L'Estoile の日記など）の本文。ウェブ検索で語句が当たらなかっただけで、本文は読んでいない。
- Lasry 氏の論文の本文（Cryptiana の GL.htm の一覧だけを見た）。

## 参考（先行ではないが、内容の手がかりになるもの）
- 台帳の docs/navarre1586.html に « le Sr de Vesin de la Marsilliere » が、ナバール王の使いとして出てくる。書簡の « secretaire La Marsilière » が、ナバール王の側の人物である可能性を示す（確かめていない）。
- BnF の目録は、同じ巻の f. 192 を「ナバール王の宮廷の常任秘書あての、横取りされた手紙の原本」としている。書簡の « [?] du secretaire La Marsilière … tombé entre les mains » と関係するかもしれない（確かめていない）。
