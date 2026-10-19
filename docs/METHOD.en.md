# Method and checks

[日本語](METHOD.md)

## Steps
1. **Images**: Gallica, BnF fr. 15573 (ark:/12148/btv1b90618780), view 246 (f. 120r) and view 247 (f. 120v). The folio number "120" at the top right of the leaf (with another, older number to its left) confirmed that this is the right leaf. The view number is 2 off from the « p.248 » in Tomokiyo's list. The images are not included here.
2. **Deskewing and cutting**: we searched for the angle at which the horizontal projection of the lines is sharpest (`src/angle.py`) and corrected f. 120r by −1.2° and f. 120v by −2.4° (`src/deskew.py`). Giving the baseline positions of the lines, we cut the pages into tiles of two lines, left and right halves, and enlarged them (`src/tiles.py`).
3. **Transcription**: line by line, in the sign names of Brett Burford's reference sheet v3 (made from the Cipher-2 letters of the same volume, fr. 15573) (`data/transcription_*.txt`). Signs not on his sheet were given names of our own (`inferred` and `unknown` in `data/key.tsv`). The word-divider slash of the original is kept as `/`, interlinear additions as `^(…)` and struck-out signs as `{…}`; the last two are not used for decoding or scoring.
4. **Key**: `data/key.tsv` was built from Burford's `data/key-cipher2.json` (commit cc0daf74). His origins beginning with T (Tomokiyo's table) are `table`; E and F (alignments with contemporary decipherments) are `burford`. Values added from this letter are `inferred`. The evidence is in column 4 (Japanese) and column 5 (English).
5. **Decoding**: `src/decode.py` applies the key to the transcription (`data/decoded_*.txt`). The reading ([READING.en.md](READING.en.md)) is that output with word divisions and punctuation added.

## Figures (`src/decode.py`, `src/control.py`, run on 20 October 2026, after the revisions following the calibration, the second transcription and the three-reader vote)
### Share of signs with a value
| Page | Signs | Table signs only | Table + Burford's alignments | Also inferred |
|---|---|---|---|---|
| f. 120r | 885 | 789 (89.2%) | 856 (96.7%) | 872 (98.5%) |
| f. 120v | 216 | 185 (85.6%) | 211 (97.7%) | 213 (98.6%) |
| Total | 1,101 | 974 (88.5%) | 1,067 (96.9%) | 1,085 (98.5%) |

Signs with two values, such as f (`i|s`), are counted as having a value. In the first reading (commit 6982c5d) the totals were 970 (87.9%) / 1,064 (96.5%) / 1,082 (98.1%), after the revision following the calibration and the second transcription (441b3e9) 975 (88.4%) / 1,069 (96.9%) / 1,084 (98.3%) (two signs were removed in the revision after the three-reader vote, so the count went from 1,103 to 1,101). Before the three-loop sign was taken as ooo = escus (inferred), the total including inferred values was 1,082 (98.3%).

### Control with shuffled keys (both pages, 1,000 times each)
The same transcription was decoded with keys in which the values of the letter signs were swapped among themselves, and the French-likeness was compared with that of the real key. French-likeness is the mean log-likelihood of letter trigrams (built from the top 50,000 French words of `wordfreq`, with j→i and v→u). Word signs and signs with two values are not scored.

| Transcription | Condition | Signs scored | Real key | Shuffled keys (min / median / max) | Shuffled ≥ real |
|---|---|---|---|---|---|
| First (revised) | Table signs only | 751 | −2.752 | −5.611 / −4.834 / −3.910 | 0 / 1000 |
| First (revised) | Table + Burford | 830 | −2.761 | −5.663 / −4.974 / −4.109 | 0 / 1000 |
| First (revised) | Also inferred | 841 | −2.775 | −5.698 / −4.992 / −4.235 | 0 / 1000 |
| Independent second (Codex, second run; see "Independent second transcription") | Table signs only | 734 | −2.702 | −5.664 / −4.800 / −3.856 | 0 / 1000 |
| Independent second (Codex, second run) | Table + Burford | 816 | −2.752 | −5.652 / −4.956 / −4.179 | 0 / 1000 |
| Independent second (Codex, second run) | Also inferred | 819 | −2.752 | −5.623 / −4.941 / −3.944 | 0 / 1000 |
| Independent second (Codex, first run, shifted images) | Table signs only | 736 | −2.680 | −5.675 / −4.798 / −3.877 | 0 / 1000 |
| Independent second (Codex, first run) | Also inferred | 826 | −2.785 | −5.649 / −4.945 / −3.983 | 0 / 1000 |
| Three-reader vote (see below) | Table signs only | 742 | −2.762 | −5.622 / −4.827 / −3.890 | 0 / 1000 |
| Three-reader vote | Also inferred | 832 | −2.786 | −5.697 / −4.975 / −3.979 | 0 / 1000 |
| Second (see "Second transcription") | Table signs only | 717 | −3.079 | −5.493 / −4.767 / −3.948 | 0 / 1000 |
| Second | Also inferred | 835 | −3.011 | −5.687 / −4.952 / −4.186 | 0 / 1000 |

This shows only that the key's values produce text far closer to French than chance assignments do; it does not show that each sign is read correctly. In the first transcription some look-alike signs were chosen by context, which favours the real key. The second transcription (Sonnet) and the three-reader vote (Opus) were read by shape only and have no context bias. The vote's real-key score is about the same as that of the context-chosen first transcription.

### Values inferred in this letter
| Sign | Value | Times | Evidence |
|---|---|---|---|
| Lp (ℓ-shape) | i | 5 | n'y a (r c02), Guise (r c10), irai (r c24). Only in r c04 does p fit (ra[p]portent) |
| curlo (stroke whose foot curls right) | o | 5 | auons (r c25), corps (r c27), offres (r c26), souffr- (r c03). Named curl in our first transcription |
| nous (gg struck through) | nous | 3 | que nous somes (r c12–13), mais nous somes (r c26), qui nous le (r c29) |
| 2c (2 with a swirl) | m | 1 | initial of a name (r c22, [M]ontablaye?) |
| qx (q with x) | le | 1 | [le]urs estrangers (v c02). The second transcription read r |
| ooo (three loops in a row) | escus | 3 | trente mil [escus] en or (r c08), cinq mil [escus] pour venir icy (r c11), cent cinq mil [escus] ne … sauroient relever (r c14). At first given the same name as the two-loop sign (oo) in r c09; the image shows a different shape. Two independent readers also noted "three loops" |

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
  - Sign agreement (lines 19–24, 137 reference signs):
    | Counting | Agreement |
    |---|---|
    | Strict (edit distance; line-initial signs missing from the reference count as errors; `src/calib.py --signs`) | 78.1% (edit distance 30; 77.4%, distance 31, before the renaming) |
    | As Burford counts: a match if equal to any of the reference's alternatives (a｜b); the 12 transcribed line-initial signs missing from the reference are not counted (`--lenient --no-alias`) | 86.9% (18 errors) |
    | As above, also counting different names with the same value (dots and :, ooC and phi) as matches (`--lenient`) | 89.1% (15 errors) |

    Burford's reader accuracy on the same lines of f. 104r was 91.1–93.5% for single passes and 92.9% for a vote of three passes (either name accepted for look-alikes; his README, "Measured numbers"). The details of the counting are not the same, so this is not a strict comparison.
    The remaining 15 errors: 2o read as "a 0" and "a" (two places), .24. read as "2 q+", # read as 4t (two places), w read as w2, z9 read as 9, rC read as Lp and :, unreadable (?) or extra signs, etc. Searching the transcription of f. 120 for these types: all five places of 4t are where the context requires e (prince, fasché, Guise, le mar[eschal], etc.), both places of w2 are il, and there is no "a 0" or "2 q+".
- Kinds of difference (classified by eye; one place may count more than once):
  - One sign read as two: 2o (qui) read as "a 0" and "a a" (twice); the number sign .24. (peu) read as "2 q+".
  - Look-alike signs confused: # (r) read as 4t (e) twice (« desgarnie », « resoluant »). The start of line 18 (« pour plu[sieurs] » in the decipherment) read as Gamma, 2u (vous de). The start of line 22 (« tout des[garnie] ») read as Qh, .12. (armée des). The humps of ϖ counted as two (w2) instead of three.
  - Different key values: the sign named bslash (backslash with o; now renamed curl) in this transcription is Burford's curl, and the contemporary decipherment has pour in both places (« emporter pour », « parle pour »). The key of this letter had inferred bslash = a, curl = o. λ stands where the decipherment has « deux », in line with Burford's x (dx = deux); the key of this letter had q.
  - Spelling differences between cipher and decipherment (not misreadings; Burford's sign reference has the same signs): faicts/faictz, principales, dificultes, restent, Guyenne, estans, campes, etc.
  - Place names (Xaintonge, Poitou): signs with no value in the key, or not read. Three line-initial signs cut off.
- Following the calibration, bslash in the key of f. 120 was renamed curl (pour), the former curl renamed curlo, and λ given q or x (see "Values revised"). The confusions of # and 4t, and of 2o and "a 0", were not re-examined in the transcription of f. 120.
- **Calibration by the same way of reading as the published transcription (20 October 2026)**: the calibration and the vote above read by shape only. The published transcription (`data/`) was written by one Opus reader decoding with the key while reading, choosing between look-alike signs by both the sentence and the shape. A blind Claude Opus reader (subagent) was therefore asked to read the same seven lines in that way (`calib/transcription_f104r_l18-24_context.txt`). It was given the line cuts with the margin side blanked, the reference sheet, the sign names with shape descriptions, and a key of names and values only (no notes, evidence words or mention of f. 104r). It was told not to open the references, the full page or other transcriptions, and reported that it did not.
  | Counting | Result |
  |---|---|
  | Signs (as Burford counts, reference alternatives only) | **90.5%** (13 errors, 8 of them naming differences: 24 vs .24., : vs dots, ooC vs phi) |
  | Signs (also same-value names) | 95.6% |
  | Signs (strict) | 81.8% |
  | Letters (current key) | 79.4% (70.2% with table signs only) |

  Caveats: a single measurement. The key value curl = pour was learnt from these seven lines in the earlier calibration, so this reader may have had a slight advantage when choosing by context. Through a bug of ours, the row for the sign # (value r) was missing from the key list given to the reader (the reader wrote # by shape, so sign accuracy is not affected).
- Meaning: a transcription read once by shape, combined with the key, may contain about 30% character errors. In f. 120 signs were chosen by context, so fewer errors are expected, but this was not checked. This is of the same order as the calibration of matignon1586-public on f. 103v (74.8%).

## Record of checks 1: Claude Sonnet transcription (20 October 2026)
A key value of the first (pdot = puis) was revised after looking at differences with this transcription, so this comparison is not called independent. The independent second transcription is "Independent second transcription (Codex)" below.
- Another AI (Anthropic's Claude Sonnet) was given the same image tiles (two lines, left and right halves), Burford's reference sheet, and a list of sign names with descriptions of shape only (no values, plaintext or evidence words), and transcribed by shape only, without seeing the first transcription, the key, the decoded text or the notes (`second/transcription2_f120r.txt`, `f120v.txt`). Turning signs into plaintext was forbidden. Its list of names was the one before renaming, so for comparison bslash→curl and curl→curlo were applied (`second/transcription2_f120_all.txt`).
- The second reader's own report: only two places were enlarged; the rest was read on the tiles at their own size. About a fifth of the signs (226) were marked as uncertain.
- Comparison with the first (`src/compare2.py`; against the first transcription before the three-reader vote. Against the revised one (after the ooo renaming): recto 81.4% / 87.7%, verso 79.2% / 87.5%):
  | Page | Agreement of sign names | Agreement of values (different names with the same value count as agreeing) |
  |---|---|---|
  | f. 120r | 81.4% (887 signs, edit distance 165) | 87.7% (edit distance 109) |
  | f. 120v | 78.7% (216 signs, edit distance 46) | 87.0% (edit distance 28) |
- Most differences that change a value fall in three look-alike pairs: ls (r) and S (c), 24 places; r (e) and xbar (s), 18; 8s (m) and 8 (t), 8. In every case the first reading gives a French word (asseure, ordre, lettre, derniere, passé, trente, mil, mar[eschal], etc.). That means these were chosen by context, not decided by shape.
- The only revision prompted by the second reading is pdot (puis), one kind of sign in two places (see "Values revised"). The second reader also read the ⊏-shape as ⊣ (plus) (r c23), the first sign as tt (les) (r c01), and qx as r (v c02); all are left as candidates in [OPEN.en.md](OPEN.en.md).
- Decoded with the same key, the second transcription also gave 0 / 1000 in the control (table above).

## Record of checks 2: vote of three Claude Opus readers (20 October 2026)
The first transcription was corrected after looking at differences with the vote on the image, so its comparison with the first is not called independent (the accuracy on f. 104r is a blind measurement).
- Three blind Claude Opus readers (subagents) read the same material separately: f. 104r lines 18–24 (the calibration lines; only the line cuts with the margin side blanked were given) and all 39 lines of f. 120. They were given the line images, Burford's reference sheet, and a list of sign names with shape descriptions only (no values, plaintext or evidence words). They were told not to open the first transcription, the key, the decoded text, the notes, the references or the full page of f. 104r, and all three reported that they did not. Turning signs into plaintext was forbidden. Readings: `third/*_pass1–3.txt`; vote: `src/vote.py` (on each line the reading closest to the others is the pivot, and the majority name is taken at each position) → `third/*_vote.txt`.
- Share of positions where all three gave the same name (relative to reader 1's signs): f. 104r 94.8% (164/173), f. 120r 89.3% (781/875), f. 120v 84.3% (182/216).
- **Accuracy on f. 104r lines 18–24** (137 reference signs; `src/calib.py`):
  | Reading | Signs (as Burford counts, reference alternatives only) | Signs (also same-value names) | Signs (strict) | Letters (key at the time of the calibration) |
  |---|---|---|---|---|
  | First calibration (another session, one pass) | 86.9% | 89.1% | 78.1% | 70.6% |
  | Reader 1 | 89.1% | 94.2% | 80.3% | 73.4% |
  | Reader 2 | 87.6% | 94.2% | 78.8% | 73.8% |
  | Reader 3 | 89.8% | 94.9% | 81.0% | 73.0% |
  | **Vote of the three** | **90.5%** | **95.6%** | 81.8% | 74.2% |

  Burford's figures on the same lines: 91.1–93.5% for single passes, 92.9% for a vote of three (either name accepted for look-alikes). Of the 13 errors left in the vote (reference alternatives only), 8 are differences of naming (the reference's 24 vs .24., : vs dots, ooC vs phi) and 5 are misreadings that change the value (z9→9, rC→Lp, w→w2, rC missing, x?|uC|y→9). Letter agreement is lower than sign accuracy because of code signs with no value (place names etc.) and spelling differences between cipher and decipherment (see "Calibration").
- **Comparison on f. 120**: agreement of values between the revised first transcription and the vote is 93.1% recto (885 signs, edit distance 61) and 87.0% verso (216 signs, edit distance 28), higher than for the Sonnet transcription (87–88%).
- **Places corrected after the vote**: there were 23 places where all three readers agreed on a value different from the first transcription. Each was looked at on the image, and the following 7, confirmed on the image, were changed to the readers' reading (at first 9 were changed, including v c05 and v c07; on re-checking under the rule "correct only where the image confirms it", those two were returned to the first reading):
  | Where | First | Corrected | Reason |
  |---|---|---|---|
  | r c03 | x (u) | r (e) | on the image an x with a dot, the sheet's r. qu'il souffre ne soit a desseing |
  | r c04 | hs (r) | r (e) | on the image the sign after the box is the dotted r, not ʃ. les efects |
  | r c12 | S (c) | ls (r) | on the image a thin ʃ. je vous puis dire |
  | r c16 | H (l) | # (r) | on the image the bar runs beyond the uprights, as in #. de s[en] aler et partir |
  | r c17 | 4 (a) | removed | the 4 was counted twice in the overlap of the two tiles (one on the image). qu'il saura ce que |
  | r c19 | z9 (de) | removed | on the image there is only one sign (Ee) between 6 and 4 |
  | v c03 | ls (r) | S (c) | on the image a round S, unlike the ʃ before it |

  Sixteen were checked and not changed: x in v c07 (an x with a bar at its foot, no dot of r visible), ls in v c05 (a small 5-shape, neither S nor ls can be decided), curlo read as curl in two places (taken as caused by our shape descriptions; souffre and rapportent need o), w2 in r c20 (two humps on the image; il seroit), hb in r c15 (ʃ with a bar; tout resolu), dbar in r c09 (a separate sign from the 4 on the image), Tl in v c01 (plus de fondement), 6b in v c06 (faire), L and xbar in v c07–c08 (the signs are on the image), r in v c01 (pauureté), f in v c07 (efects), + in r c01 (a run of signs with no value), oo in v c08 (at the end).

- Why the vote was not made the main transcription: in many places the vote breaks words that read in the first transcription (« plus de dix iours » becomes « de di[?] iour[?] », « cardinal » becomes « mn…nal », the curlo of « auons » and « corps », etc.). So the first transcription remains the main one, and only the places where all three agreed against it were checked on the image and corrected.

## Independent second transcription (OpenAI's Codex, 20 October 2026)
- Run after the first transcription had been corrected from the checks above, with OpenAI's Codex CLI (codex-cli 0.163.0-alpha.10.2 bundled with the ChatGPT app, default model; no model name appears in the configuration or the run record). `codex exec --ephemeral -s read-only` was run from an empty folder, given only the line images (each line in left and right halves, 78 images), Burford's reference sheet and an English prompt (`codex/PROMPT.md`: sign names and shape descriptions only; no values, first reading, key or plaintext).
- **First run** (`codex/run1_misaligned/`): in lines 6–9 and others, the right halves of the images were one line off (the right side of the lines slopes down, but the right halves were cut at the left half's baseline). The run record contains only the reply, with no command execution or file reading.
- **Second run** (`codex/transcription_codex_*`): each line was straightened by following its baseline every 200 pixels and shifting columns up or down, then cut into left and right halves again. All 39 strips were checked by eye; the end of verso line 7 that showed at the right of verso line 8 was blanked. Besides the reply, the run record has one command execution (`ls ../img3`, listing the image folder). The folder holds only images; no other file was read.
- Agreement with the (revised) first transcription:
  | Run | Page | Sign names | Values (same-value names count as agreeing) |
  |---|---|---|---|
  | second | f. 120r | 89.7% (885 signs, edit distance 91) | 92.9% (edit distance 63) |
  | second | f. 120v | 88.4% (216 signs, edit distance 25) | 92.1% (edit distance 17) |
  | first (shifted images) | f. 120r | 89.6% (edit distance 92) | 92.9% (edit distance 63) |
  | first (shifted images) | f. 120v | 88.0% (edit distance 26) | 90.7% (edit distance 20) |

  The lowest value over both runs (values 90.7%, names 88.0%) is used for the judgement. (Compared before the three-loop sign was named ooo, the first run gave 93.2% recto and 90.7% verso.)
- The first transcription was not corrected from this comparison (that would make it no longer independent). Checking the differences is left in [OPEN.en.md](OPEN.en.md).
- Decoded with the same key, the Codex transcription also gave 0 / 1000 in the control (table above). Its sign count is higher than the first's because descriptions in <…> are split into words.

## Use of AI
- The image transcription, the inferred values, the decipherment, the scripts and the documents were made by Anthropic's Claude (Claude Code, model Claude Opus 5.5). A person (the repository's maintainer) chose the target, saved the images and decided to publish.
- The first transcription (`data/`) is one reading of each line by Claude Opus 5.5. Differences from the transcriptions used for checking (`second/` by Claude Sonnet, `third/` by three Claude Opus readers) were looked at on the image, and the seven places the image confirmed were corrected. After that, OpenAI's Codex made the independent second reading (`codex/`). No person checked the transcription. Agreement between AI readings is not a substitute for a human check.
- While transcribing, lines already written were read with the key. Some look-alike signs were chosen by context (e.g. the second sign of r c04 read as r rather than x, giving desseing; written `r?` in the transcription).

## Limits
- The calibration covers only seven lines of f. 104r. The measurement by the same way of reading as the published transcription was made once (sign accuracy 90.5%, letter agreement 79.4%). The first, shape-only calibration gave 70.6% letter agreement in the blind measurement (62.9% with table signs only). In the work that read f. 120, part of the contemporary decipherment came into view when a reduced image of f. 103v was opened while preparing, so the calibration was done in a separate piece of work (another Claude Code session) that had not seen the margin.
- Look-alike signs (r and x, 8 and 8s, S and ls and hs, f and f2, th and 4t, # and 4t and tt, 2o and "a 0") are easily confused. In the calibration, # / 4t and 2o were actually confused. The choices made by context favour the real key in the control.
- Most inferred values are checked in only one to five places in this letter.
- Signs with no value and unread stretches are in [OPEN.en.md](OPEN.en.md).
