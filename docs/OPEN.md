# 未解決の点

[English](OPEN.en.md)

## 値が分からない記号（13種16か所、2ページの記号1,101個のうち）
`src/decode.py` で値が付かない記号。行番号は `data/transcription_f120_all.txt` の番号（c1NN＝f. 120r の NN 行、c2NN＝f. 120v の NN 行）。「2回目」は Claude Sonnet による書き起こし（`second/`）の読み。

| 記号 | 回数 | 場所 | 文脈・候補 |
|---|---|---|---|
| oo（∞ 形、輪2つ） | 3 | c109、c208（2） | c109 は pour les [∞]voyer（en と読みたくなる）。c208 は末尾の2つ。mil の後の輪3つの記号（ooo）とは別の形で、ooo は推定で escus とした |
| hsb（ʃ に横線と点） | 2 | c114、c124 | ne [?] sauroient relever、ce que l'on en dira [?] |
| thb・7・Sbar | 各1 | c101 | 冒頭 « [thb] a [7] u [Sbar] je vous asseure »。呼びかけ（Monsieur の類）か。2回目は thb を tt（les）と読んだ |
| 30 | 1 | c105 | ne se ra[p]portent [30] aux advis |
| Esign（E 形） | 1 | c115 | que [E] est tout resolu（人名・称号の記号か） |
| Om（平たい Ω 形） | 1 | c117 | partir si [?] qu'il saura（tost か） |
| invTl（⊏ 形） | 1 | c123 | je croy que [?] ne s'y trouvera pas（on・nul の類か）。2回目は ⊣（plus）と読んだ |
| 15 | 1 | c128 | profit de n[?] [15] … tombé |
| .u.（点で挟んだ u） | 1 | c129 | un[e] [?] du secretaire La Marsilière（lettre の類か） |
| 4d（4 に点） | 1 | c130 | des affaires de [?]spe… |
| Dsign（大きな D に点） | 1 | c208 | 末尾 |

## 読めない箇所・読みが割れる箇所
- r c03–c04：« qu'il souffre ne soit a desseing »（3人の多数決を見て直した読み）。« des seing » の切れ目は推定。
- r c05：« que l'on de[?]a donne[?s] »。
- r c09：« qu'un[?e] n de ment pour les [∞]voyer »。
- r c15–c16：« que quelque [?…]ment et conjuration que vous s[?] puis i es faire de s[en] aler »。
- r c22：« est le s[?ieu]r [?M]ontablaye »。記号は w q+ g f delta th r 2c : 6 a 4 pi q+ 4 dbar r。« le sieur » なら最後の r（e）が # か ls（r）のはず。
- r c24：« si je irai[s], [?s'ay en dray] »。
- r c25–c26：« qui sui[?vent] [?…] » の L r 6 a 4 pdots 9 delta # の部分。
- r c28：« de n [15] est m est tombé »（w 2 w a // 8s pi delta）。« estant tombé » の類か。
- r c29–c31：« qui nous le [?m]ort particulierement des affaires de [4d]spe … ade ment »。
- v c03–c05：« l'on ne sauroit [?rotir] rendre l[?λ]a … tort … faict [L] user ; [f] redu u »。
- 行間の書き込み（r c07・c10 の « 8δ »、r c11・c13 の « ar »、r c12 の « Hr »、r c19 の « +q+ »）は解読に使っていない。r c19 は mar＋al で mareschal の略記と読める。r c12 の « Hr »（le）は no＋le で nouvelle の略記か。

## 似た形で取り違えやすい記号
- r（e）と x（u）：r c01 の ennuyé、r c20 の se retirant、r c04 の desseing は、x に見える記号を r と読んだ。逆の取り違えも残っているはず。
- 8（t）と 8s（m）：mil・mareschal・sepmaines・ennemis は 8s と読んだ。形の差は小さい。
- S（c）、ls（r）、hs（r）：r c01 の asseure、r c22 の je croy は ls と読んだ。
- f（i|s）、f2（n）、長い f：r c15–c16 の conjuration は f2 と読んだ。
- curl（＼ の下に o）と curlo（縦線の下が右に巻く形）：最初の書き起こしでは、＼ 形を bslash、巻く形を curl と名付けていた。較正で、＼ 形が Burford 氏の curl（pour）だと分かり、付け直した。巻く形（o）は Burford 氏の見本にない記号とみているが、見本と比べ直してはいない。
- lambda（λ）：友清氏の表では q、Burford 氏の鍵と較正では x。この書簡では q（qu'une、r c09）と x（d[i]x iours、r c22）の両方に読める。
- 照合に使った Sonnet の書き起こしとの食い違いが多い組：ls と S（24か所）、r と xbar（18か所）、8s と 8（8か所）。1回目はどれも文脈で選んだ。
- 独立の2回目（Codex）との食い違い（判定に使う回で、値の編集距離が表56・裏21）は、まだ画像で見ていない。

## 確かめていないこと
- 差出人と日付。内容（Guise 枢機卿の2日付の書簡、Biron、軍の代表、La Marsilière、あと6週間）から、巻の前後の書簡と照らせば絞れる可能性がある。
- 人名：Bilart、[M]ontablaye、La Marsilière がどの人物か。La Marsilière は、台帳の別の文書でナバール王の使い（« le Sr de Vesin de la Marsilliere »）として出てくる。同じ巻の f. 192 は、目録でナバール王の宮廷の秘書あての横取りされた手紙とされている（[PRIOR_CHECK.md](PRIOR_CHECK.md) の「参考」）。どちらも確かめていない。
- 友清氏が « Endorsement illegible » と書いた裏書きは、246・247コマには見当たらない（別の葉にある可能性）。
- 書き起こしの正確さ：f. 104r の7行で、公開した書き起こしと同じ読み方（Opus 1人が鍵で解読しながら）の記号の正確さは90.5%（同じ値の別名も一致なら95.6%）。形だけで読んだ1人1回は86.9%（89.1%）、文字の一致率70.6%。f. 120 そのものの正確さは測っていない。f. 120 での独立の2回目（Codex、画像を正しく渡した回）との値の一致率は表93.7%・裏90.3%（[METHOD.md](METHOD.md)）。
- 較正で見つかった # と 4t、2o と「a 0」の取り違えは、f. 120 の書き起こしでは見直していない。
