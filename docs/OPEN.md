# 未解決の点

## 値が分からない記号（14種21か所、2ページの記号1,103個のうち）
`src/decode.py` で値が付かない記号。行番号は `data/transcription_f120_all.txt` の番号（c1NN＝f. 120r の NN 行、c2NN＝f. 120v の NN 行）。

| 記号 | 回数 | 場所 | 文脈・候補 |
|---|---|---|---|
| oo（∞ 形） | 6 | c108、c109、c111、c114、c208（2） | trente mil [∞] en or、cinq mil [∞] a venir icy、cinq mil [∞] ne [?] sauroient relever。escus と読むと3か所は通る。c109 の les [∞]voyer では en（envoyer）と読みたくなり、合わない。c208 は末尾の2つ |
| pdot（縦線に輪と点） | 2 | c112、c116 | je vous [?] dice、que vous s[?] … ies faire |
| hsb（ʃ に横線と点） | 2 | c114、c124 | ne [?] sauroient relever、ce que l'on en dira [?] |
| thb・7・Sbar | 各1 | c101 | 冒頭 « [thb] a [7] u [Sbar] je vous asseure »。呼びかけ（Monsieur の類）か |
| 30 | 1 | c105 | ne se ra[p]portent [30] aux advis |
| Esign（E 形） | 1 | c115 | que [E] est tout resolu（人名・称号の記号か） |
| Om（平たい Ω 形） | 1 | c117 | partir si [?] qu'il saura（tost か） |
| invTl（⊏ 形） | 1 | c123 | je croy que [?] ne s'y trouvera pas（on・nul の類か） |
| 15 | 1 | c128 | profit de n[?] [15] … tombé |
| .u.（点で挟んだ u） | 1 | c129 | un[e] [?] du secretaire La Marsilière（lettre の類か） |
| 4d（4 に点） | 1 | c130 | des affaires de [?]spe… |
| Dsign（大きな D に点） | 1 | c208 | 末尾 |

## 読めない箇所・読みが割れる箇所
- r c03–c04：« qu'il [?]souffr[e] une [?]soit a desseing »。語の切れ目が定まらない。
- r c05：« que l'on de[?]a donne[?s] »。
- r c09：« qu'un[?e] n de ment a les [∞]voyer »。
- r c15–c16：« que quelque [?…]ment et conjuration que vous s[?] [pdot] i es faire de s[en] a l'el[?] »。
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
- curl：Burford 氏の鍵では pour。この書簡では o と読むと通る。同じ記号かどうかを見本と比べ直していない。
- lambda：Burford 氏の鍵では x。この書簡では q（qu'une）。r c22 の « d[λ] iours » は dix と読みたくなる。

## 確かめていないこと
- 差出人と日付。内容（Guise 枢機卿の2日付の書簡、Biron、軍の代表、La Marsilière、あと6週間）から、巻の前後の書簡と照らせば絞れる可能性がある。
- 人名：Bilart、[M]ontablaye、La Marsilière がどの人物か。
- 友清氏が « Endorsement illegible » と書いた裏書きは、246・247コマには見当たらない（別の葉にある可能性）。
- 書き起こしの正確さ：f. 104r の7行での較正では、文字の一致率69.5%（[METHOD.md](METHOD.md) の「較正」）。f. 120 そのものの正確さは測っていない。
- 較正で見つかった違いを f. 120 に当てること（まだしていない）：f. 104r では、bslash（＼ に o）と名付けた記号が当時の解読で2か所とも pour（Burford 氏の curl）、λ は « deux » の位置で x と合い、# を 4t と読み違えた所が2つあった。f. 120 の bslash（r c09・c11、v c03）、λ（r c09）、4t の読みを見直す必要がある。
