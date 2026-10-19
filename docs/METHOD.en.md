# Method and checks

[日本語](METHOD.md)

## Steps
1. **Images**: Gallica, BnF fr. 15573 (ark:/12148/btv1b90618780), view 246 (f. 120r) and view 247 (f. 120v). The folio number "120" at the top right of the leaf (with another, older number to its left) confirmed that this is the right leaf. The view number is 2 off from the « p.248 » in Tomokiyo's list. The images are not included here.
2. **Deskewing and cutting**: we searched for the angle at which the horizontal projection of the lines is sharpest (`src/angle.py`) and corrected f. 120r by −1.2° and f. 120v by −2.4° (`src/deskew.py`). Giving the baseline positions of the lines, we cut the pages into tiles of two lines, left and right halves, and enlarged them (`src/tiles.py`).
3. **Transcription**: line by line, in the sign names of Brett Burford's reference sheet v3 (made from the Cipher-2 letters of the same volume, fr. 15573) (`data/transcription_*.txt`). Signs not on his sheet were given names of our own (`inferred` and `unknown` in `data/key.tsv`). The word-divider slash of the original is kept as `/`, interlinear additions as `^(…)` and struck-out signs as `{…}`; the last two are not used for decoding or scoring.
4. **Key**: `data/key.tsv` was built from Burford's `data/key-cipher2.json` (commit cc0daf74). His origins beginning with T (Tomokiyo's table) are `table`; E and F (alignments with contemporary decipherments) are `burford`. Values added from this letter are `inferred`. The evidence is in column 4 (Japanese) and column 5 (English).
5. **Decoding**: `src/decode.py` applies the key to the transcription (`data/decoded_*.txt`). The reading ([READING.en.md](READING.en.md)) is that output with word divisions and punctuation added.

## Figures (`src/decode.py`, `src/control.py`, run on 20 October 2026, after the key was revised following the calibration and the second transcription)
### Share of signs with a value
| Page | Signs | Table signs only | Table + Burford's alignments | Also inferred |
|---|---|---|---|---|
| f. 120r | 887 | 790 (89.1%) | 858 (96.7%) | 871 (98.2%) |
| f. 120v | 216 | 185 (85.6%) | 211 (97.7%) | 213 (98.6%) |
| Total | 1,103 | 975 (88.4%) | 1,069 (96.9%) | 1,084 (98.3%) |

Signs with two values, such as f (`i|s`), are counted as having a value. Before the revision (the first commit, v0.1) the totals were 970 (87.9%) / 1,064 (96.5%) / 1,082 (98.1%).

### Control with shuffled keys (both pages, 1,000 times each)
The same transcription was decoded with keys in which the values of the letter signs were swapped among themselves, and the French-likeness was compared with that of the real key. French-likeness is the mean log-likelihood of letter trigrams (built from the top 50,000 French words of `wordfreq`, with j→i and v→u). Word signs and signs with two values are not scored.

| Transcription | Condition | Signs scored | Real key | Shuffled keys (min / median / max) | Shuffled ≥ real |
|---|---|---|---|---|---|
| First | Table signs only | 751 | −2.778 | −5.614 / −4.838 / −3.933 | 0 / 1000 |
| First | Table + Burford | 831 | −2.788 | −5.667 / −4.976 / −4.125 | 0 / 1000 |
| First | Also inferred | 842 | −2.801 | −5.678 / −4.994 / −4.246 | 0 / 1000 |
| Second (see "Second transcription") | Table signs only | 717 | −3.079 | −5.493 / −4.767 / −3.948 | 0 / 1000 |
| Second | Also inferred | 835 | −3.011 | −5.687 / −4.952 / −4.186 | 0 / 1000 |

This shows only that the key's values produce text far closer to French than chance assignments do; it does not show that each sign is read correctly. In the first transcription some look-alike signs were chosen by context, which favours the real key. The second was read by shape only and has no context bias, but more misreadings (its real-key score is lower).

### Values inferred in this letter
| Sign | Value | Times | Evidence |
|---|---|---|---|
| Lp (ℓ-shape) | i | 5 | n'y a (r c02), Guise (r c10), irai (r c24). Only in r c04 does p fit (ra[p]portent) |
| curlo (stroke whose foot curls right) | o | 5 | auons (r c25), corps (r c27), offres (r c26), souffr- (r c03). Named curl in our first transcription |
| nous (gg struck through) | nous | 3 | que nous somes (r c12–13), mais nous somes (r c26), qui nous le (r c29) |
| 2c (2 with a swirl) | m | 1 | initial of a name (r c22, [M]ontablaye?) |
| qx (q with x) | le | 1 | [le]urs estrangers (v c02). The second transcription read r |

### Values revised after the calibration and the second transcription
| Sign | Before | After | Reason |
|---|---|---|---|
| curl (large backslash with a small o; named bslash in our first transcription) | a (inferred) | pour | In the calibration on f. 104r the contemporary decipherment has pour in both places. It is the same sign as Burford's curl = pour (T+E-eye). In f. 120: pour venir icy (r c11), pour les [∞]voyer (r c09), pour [u] temps (v c03) |
| lambda (λ) | q | q or x | q in Tomokiyo's table; x in Burford's key (E) and in the calibration (where the decipherment has deux). In f. 120, q fits qu'une (r c09) and x fits d[i]x iours (r c22) |
| pdot (small loop half-way up a stroke) | unknown | puis | Re-examined because the second transcription read it as phi (en). Burford's sheet example of phi has two loops, a different form; we take it as the same form as Tomokiyo's puis (a stroke with a loop). je vous puis di[r]e que nous somes (r c12). The c (S) of dice may be a misread r (ls) |

Signs also named from Tomokiyo's table: dsi+ (ꝺ with a cross) = c, xd (u-shape with a dot) = x, w2 (ϖ with two humps) = il, 6b (б-shape) = f, R = h, yy = encore.

## Calibration (measured on a letter with a contemporary decipherment, 20 October 2026)
- Target: BnF fr. 15573 f. 104r (Mayenne to the King, September 1586, the same Cipher-2; Gallica ark:/12148/btv1b90618780, view 213). The contemporary decipherment is in the left margin and at the foot.
- Steps taken not to see the answer: done in a separate piece of work (another Claude Code session) from the one that read f. 120, without opening the margin or a reduced image of the page. The amount of dark pixels per column and the line period (about 119 px for the marginal decipherment, about 150 px for the cipher) gave the border between margin and text (x ≈ 1,400 px). The left side of each line was blanked before deskewing (−1.6°), and only the text area was cut out and looked at.
  - At the left end of line 23 a faint grey trace (probably the edge of the marginal decipherment, about two letters) appeared. It was not read as a word. The left ends of lines 23–24 were then read on a binarised image that keeps only dark pixels (the grey writing does not show).
  - The only images opened were the top of the text area (folio number "104" and cipher lines 1–3) and the cuts of lines 18–24.
  - One note in `data/key.tsv` carries Burford's alignment mark « f. 104r l. 19 'menant' », which was seen before transcribing.
- Transcription: cipher lines 18–24 (181 signs), in the same sign names, read once by shape only (`calib/transcription_f104r_l18-24.txt`). Signs were not chosen by context. Three line-initial signs were cut off at the blanked border and could not be read.
- References (fetched after the transcription was finished):
  1. Characters: the part of the contemporary decipherment corresponding to these seven lines, « [empor]ter pour plusieurs … qu'il en fallu[st] » (`calib/ref_f104r_l18-24.txt`), copied from `data/known-text/f104r-decipherment.txt` in Burford's repository (commit cc0daf74, CC BY 4.0; according to his note, read by eye by Claude from the Gallica images). The calibration work did not check it on the image (that would have meant looking at the margin); it was checked later, as follows.
  2. Signs: his `data/known-text/ref-104r-l18-24.txt` (commit 22ab58c3, CC BY 4.0; checked against the contemporary decipherment). He counts lines from 0, so his lines 18–23 are lines 19–24 of this transcription (`calib/ref_signs_f104r_burford.txt`).
- The character reference was checked on the image (after the calibration transcription, in the work that read f. 120): compared with the left margin and foot of view 213, only his « qui reste icy » was changed to « qui restent icy » (on the image there are about four letters after res; the second may also be an o). The other words agree with the image.
- Results (`src/calib.py`):
  | Key | Character agreement (reference 248 characters) | Table signs only |
  |---|---|---|
  | Key at the time of the calibration (backslash sign = a) | 70.6% (edit distance 73) | 62.9% (edit distance 92) |
  | Key revised after the calibration (backslash sign = curl = pour; see "Kinds of difference") | 73.4% (edit distance 66) | 65.7% (edit distance 85) |

  The revised values were decided after seeing the answer (by following Burford's key), so the first row (70.6%) is the blind measurement; `src/calib.py --key-at-calibration` reproduces it. Before the reference was corrected on the image, the figure was 69.5% (62.6% with table signs only). Signs with two values (`a|n` etc.) count with their first value; signs with no value count as mismatches.
  - Sign agreement (lines 19–24, `src/calib.py --signs`): 78.1% (edit distance 30 against 137 reference signs; 77.4%, distance 31, before the renaming). Eleven of the differences are places where the reference lacks a line-initial sign (as counted in the calibration work; due to the line-band fitting mentioned in his note).
- Kinds of difference (classified by eye; one place may count more than once):
  - One sign read as two: 2o (qui) read as "a 0" and "a a" (twice); the number sign .24. (peu) read as "2 q+".
  - Look-alike signs confused: # (r) read as 4t (e) twice (« desgarnie », « resoluant »). The start of line 18 (« pour plu[sieurs] » in the decipherment) read as Gamma, 2u (vous de). The start of line 22 (« tout des[garnie] ») read as Qh, .12. (armée des). The humps of ϖ counted as two (w2) instead of three.
  - Different key values: the sign named bslash (backslash with o; now renamed curl) in this transcription is Burford's curl, and the contemporary decipherment has pour in both places (« emporter pour », « parle pour »). The key of this letter had inferred bslash = a, curl = o. λ stands where the decipherment has « deux », in line with Burford's x (dx = deux); the key of this letter had q.
  - Spelling differences between cipher and decipherment (not misreadings; Burford's sign reference has the same signs): faicts/faictz, principales, dificultes, restent, Guyenne, estans, campes, etc.
  - Place names (Xaintonge, Poitou): signs with no value in the key, or not read. Three line-initial signs cut off.
- Following the calibration, bslash in the key of f. 120 was renamed curl (pour), the former curl renamed curlo, and λ given q or x (see "Values revised"). The confusions of # and 4t, and of 2o and "a 0", were not re-examined in the transcription of f. 120.
- Meaning: a transcription read once by shape, combined with the key, may contain about 30% character errors. In f. 120 signs were chosen by context, so fewer errors are expected, but this was not checked. This is of the same order as the calibration of matignon1586-public on f. 103v (74.8%).

## Second transcription (an independent reading, 20 October 2026)
- Another AI (Anthropic's Claude Sonnet) was given the same image tiles (two lines, left and right halves), Burford's reference sheet, and a list of sign names with descriptions of shape only (no values, plaintext or evidence words), and transcribed by shape only, without seeing the first transcription, the key, the decoded text or the notes (`second/transcription2_f120r.txt`, `f120v.txt`). Turning signs into plaintext was forbidden. Its list of names was the one before renaming, so for comparison bslash→curl and curl→curlo were applied (`second/transcription2_f120_all.txt`).
- The second reader's own report: only two places were enlarged; the rest was read on the tiles at their own size. About a fifth of the signs (226) were marked as uncertain.
- Comparison with the first (`src/compare2.py`):
  | Page | Agreement of sign names | Agreement of values (different names with the same value count as agreeing) |
  |---|---|---|
  | f. 120r | 81.4% (887 signs, edit distance 165) | 87.7% (edit distance 109) |
  | f. 120v | 78.7% (216 signs, edit distance 46) | 87.0% (edit distance 28) |
- Most differences that change a value fall in three look-alike pairs: ls (r) and S (c), 24 places; r (e) and xbar (s), 18; 8s (m) and 8 (t), 8. In every case the first reading gives a French word (asseure, ordre, lettre, derniere, passé, trente, mil, mar[eschal], etc.). That means these were chosen by context, not decided by shape.
- The only revision prompted by the second reading is pdot (puis), one kind of sign in two places (see "Values revised"). The second reader also read the ⊏-shape as ⊣ (plus) (r c23), the first sign as tt (les) (r c01), and qx as r (v c02); all are left as candidates in [OPEN.en.md](OPEN.en.md).
- Decoded with the same key, the second transcription also gave 0 / 1000 in the control (table above).

## Use of AI
- The image transcription, the inferred values, the decipherment, the scripts and the documents were made by Anthropic's Claude (Claude Code, model Claude Opus 5.5). A person (the repository's maintainer) chose the target, saved the images and decided to publish.
- The first transcription (`data/`) is one reading of each line by Claude Opus 5.5. The second (`second/`) is an independent reading by Claude Sonnet. No majority vote was taken; differences were decided by the first reader from the image and the context. No person checked the transcription.
- While transcribing, lines already written were read with the key. Some look-alike signs were chosen by context (e.g. the second sign of r c04 read as r rather than x, giving desseing; written `r?` in the transcription).

## Limits
- The calibration covers only seven lines of f. 104r (181 signs), from one transcription. Results are under "Calibration" (blind measurement: 70.6% character agreement, 62.9% with table signs only). In the work that read f. 120, part of the contemporary decipherment came into view when a reduced image of f. 103v was opened while preparing, so the calibration was done in a separate piece of work (another Claude Code session) that had not seen the margin.
- Look-alike signs (r and x, 8 and 8s, S and ls and hs, f and f2, th and 4t, # and 4t and tt, 2o and "a 0") are easily confused. In the calibration, # / 4t and 2o were actually confused. The choices made by context favour the real key in the control.
- Most inferred values are checked in only one to five places in this letter.
- Signs with no value and unread stretches are in [OPEN.en.md](OPEN.en.md).
