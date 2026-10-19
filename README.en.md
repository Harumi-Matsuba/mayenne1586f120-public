# BnF fr. 15573 f. 120, a cipher letter in Mayenne–Forget's Cipher-2 (1586): a reading

[日本語 README](README.md)

A reading of an undated cipher letter of unknown sender, BnF Français 15573 f. 120, with Mayenne–Forget's Cipher-2 as reconstructed by Satoshi Tomokiyo and the key that Brett Burford built for another Cipher-2 letter in the same volume.

## Status (20 October 2026)
- **A reading of the whole letter** (meeting all the numerical conditions under "Basis" below). Thirteen kinds of signs (16 places) have no value, and some short stretches are not read ([docs/READING.en.md](docs/READING.en.md), [docs/OPEN.en.md](docs/OPEN.en.md)). The sender and the date are not known.
  - Basis (the conditions under our publishing rules for calling a reading "whole"): control 0 / 1000. Agreement of values between the first transcription and the independent second (Codex, two runs): the lower is 90.7% (condition: 85% or more). Share of signs with a value, including inferred: 98.5% (95% or more). Sign accuracy in the calibration, by the same way of reading as the published transcription (one Opus reader decoding with the key while reading): 90.5% (90% or more).
- **Relation to prior work**: Tomokiyo lists f. 120 as a Cipher-2 letter, « Endorsement illegible (to me). Undeciphered. » ([Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm), last modified 2023-09-23). The key is prior work (Tomokiyo's table, Brett Burford's key); the transcription and the reading were made in this repository. The check for prior work ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md), 20 October 2026) found nothing ("not found"). That check was made by the same session that read the letter; no check by a separate session has been made. Not finding something does not prove that nobody has read it.
- **No person has checked the transcription.** It was read from the images by AI. Agreement between AI readings is not a substitute for a human check.
- **Figures** (details in [docs/METHOD.en.md](docs/METHOD.en.md)):
  | Item | Result |
  |---|---|
  | Control with the letter values of the key shuffled (1,000 times, three conditions) | no shuffled key reached the real key |
  | **Independent second transcription**: agreement of values between readings by OpenAI's Codex (codex-cli 0.163.0-alpha.10.2, default model), made without seeing the first, and the first | second run (straightened line images): 92.9% recto, 92.1% verso. First run (right halves one line off): 92.9% recto, 90.7% verso. By name: 89.7% / 88.4% and 89.6% / 88.0%. The first was not corrected from this comparison |
  | Calibration: sign accuracy on seven lines of f. 104r (with a contemporary decipherment), read without seeing the answer (as Burford counts; in brackets, also counting same-value names) | same way of reading as the published transcription (one Opus reader, decoding with the key): 90.5% (95.6%). One pass by shape only: 86.9% (89.1%). Vote of three Opus readers: 90.5% (95.6%). Burford on the same lines: 91.1–93.5% single passes, 92.9% vote |
  | Calibration: letter agreement | 79.4% by the same way of reading as the published transcription (current key); 70.6% for the blind shape-only pass |
  | Record of checks: agreement of values between the first and the Claude Sonnet transcription / the vote of three Claude Opus readers | Sonnet 87.7% recto, 87.5% verso; vote 93.1% recto, 87.0% verso (the first was corrected after looking at differences with these on the image, so these are not independent comparisons) |
- **Use of AI**: the transcription, the inferred values, the decipherment, the scripts and the documents were made by Anthropic's Claude (Claude Code, Claude Opus 5.5); the independent second transcription by OpenAI's Codex; the transcriptions used for checking and calibration by Claude Sonnet and Claude Opus readers. A person chose the target, saved the images and decided to publish ("Use of AI" in [docs/METHOD.en.md](docs/METHOD.en.md)).

## Source
- BnF Français 15573 (letters of 1586; in Tomokiyo's list, ff. 7–8 are a letter of August 1586), Gallica ark:/12148/btv1b90618780, view 246 (f. 120r, 31 lines of cipher) and view 247 (f. 120v, 8 lines of cipher). There is no plaintext on these two pages.

## Share of signs with a value
| Page | Signs | Tomokiyo's table only | Table + Burford's alignments | Also inferred in this letter |
|---|---|---|---|---|
| f. 120r | 885 | 89.2% | 96.7% | 98.5% |
| f. 120v | 216 | 85.6% | 97.7% | 98.6% |
| Total | 1,101 | 88.5% | 96.9% | 98.5% |

## History
- 20 October 2026 (revision to meet the conditions for a "whole" reading)
  - The right halves of the line images given to Codex were one line off in lines 6–9 and others (the right side of the lines slopes down). Straightened line images were made by following the baseline of each line, all lines were checked by eye, and Codex was run again. Agreement of values with the first: 92.9% recto, 92.1% verso (the run on the shifted images: 92.9%, 90.7%).
  - The calibration was taken again by the same way of reading as the published transcription (one Opus reader decoding with the key), on the seven lines of f. 104r, without the answer. Sign accuracy: 90.5%.
  - The sign after mil has three loops (ooo) and is a different sign from the two-loop sign (oo) in r l. 9, as seen on the image. ooo is read as escus by inference. Signs with no value: 13 kinds, 19 places → 13 kinds, 16 places; share with a value (also inferred): 98.3% → 98.5%.
- 20 October 2026 (check for prior work)
  - docs/PRIOR_CHECK.en.md (and Japanese) added. Category: not found. Made by the same session that read the letter.
- 20 October 2026 (revision for the amended publishing rules)
  - Following "correct only where the image confirms it", the nine places corrected after the vote were re-checked on the image: seven were confirmed, and two (v c05, v c07) could not be confirmed and were returned to the first reading. Share with a value unchanged (88.5% table only, 98.3% also inferred).
  - After that, OpenAI's Codex read both pages independently without seeing the first (`codex/`). Agreement of values with the first: 93.2% recto, 90.7% verso. The first was not corrected from this comparison.
  - Version numbers and CITATION.cff removed.
- 20 October 2026 (revision after the three-reader vote, commit 8f35df6)
  - Three blind Claude Opus readers read f. 104r lines 18–24 and f. 120 separately, and a vote was taken (`third/`, `src/vote.py`). Sign accuracy on f. 104r went from 86.9% (89.1% with same-value names) in the first calibration to 90.5% (95.6%) for the vote.
  - The 23 places where all three readers agreed on a value different from the first transcription were looked at on the image and in context, and 9 were corrected (« qu'il souffre ne soit a desseing », « les efects », « je vous puis dire », « s[en] aler », « qu'il saura ce que », etc.; two of them were later returned because the image could not confirm them). Sign count 1,103 → 1,101; share with a value (also inferred) unchanged at 98.3%.
  - Sign accuracy can be counted as Burford does (`src/calib.py --lenient`).
- 20 October 2026 (revision after the calibration and the second transcription, commit 441b3e9)
  - Calibration (another session, seven lines of f. 104r) added; the character reference checked on the image (« qui reste icy » → « qui restent icy »). Blind letter agreement: 70.6%.
  - Key revised after the calibration: the backslash-with-o sign is Burford's curl (pour), so it was renamed and the former curl renamed curlo (o); λ given q or x; the stroke-with-a-loop sign (pdot) identified with Tomokiyo's *puis*. Share with a value: table only 87.9% → 88.4%; also inferred 98.1% → 98.3%.
  - Independent second transcription (Claude Sonnet, `second/`) and its comparison (`src/compare2.py`).
  - English versions (docs/*.en.md, SOURCES.en.md, English column in key.tsv, English output of the scripts).
- 20 October 2026 (first reading, commit 6982c5d)
  - Transcription of both pages, key, decoding, reading, shuffled-key control. Share with a value: table only 87.9%, also inferred 98.1%.

## Content (summary of what is read; uncertain subjects and word divisions are marked)
- "This prince" (ce prince) is more vexed and angry than ever, and there is no way to dissuade him.
- Money: the treasurer Bilart wrote in his last despatch, of the 21st of last month, that more than ten days before there had been « trente mil [?] en or ». The Cardinal of Guise wrote on the 2nd that « cinq mil [?] pour venir icy » had set out (the reading *partoient* is uncertain), yet there is no news (*nouvelle*, inferred) of it. Things are such that « not five thousand but a hundred and five thousand [?] » could not set them right (*cent* uncertain).
- There is no longer any hope of keeping the Marshal of Biron. A message, apparently from Biron, says that on his way home it would be easy to see him in passing (subject and the word after *chez* uncertain).
- Tonight the deputies of the army are here; "we" are a body so weak that it can do nothing. A [?] (perhaps a letter) of the secretary La Marsilière has fallen into "our" hands and tells in detail of affairs (finances among them).
- The breaking-up of this army is a loss: had it held six more weeks it could have done great things here; the enemy were never so astonished.

[?] is a sign with no value (e.g. the ∞-shaped sign after *mil*). Details in [docs/READING.en.md](docs/READING.en.md). The sender and the date are not known yet.

## Prior work used, and what this reading adds
**Used**
- The Cipher-2 table: Satoshi Tomokiyo's reconstruction ([henryiii_MayenneForget2.png](https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png)). The table image is not included here.
- Sign names and values outside the table: Brett Burford's reference sheet and key ([BravoBravoIX/mayenne-forget-1586-cipher-reading](https://github.com/BravoBravoIX/mayenne-forget-1586-cipher-reading), `method/sheet-v3.png` and `data/key-cipher2.json`, commit cc0daf74, CC BY 4.0), including the values he aligned with contemporary decipherments in the same volume (E, F).
- That this letter is in Cipher-2 and undeciphered: Satoshi Tomokiyo.

**Added here**
1. A line-by-line transcription of both pages in Burford's sign names (`data/transcription_*.txt`), with names added for signs not on his sheet.
2. A few values inferred from this letter (ℓ-shape = i, a stroke whose foot curls right (curlo) = o, gg struck through = nous, and others; `inferred` in `data/key.tsv`). The stroke with a loop was identified with Tomokiyo's *puis*. λ is taken to be used both as Tomokiyo's q and as Burford's x.
3. A calibration (seven lines of f. 104r), an independent second transcription by OpenAI's Codex, and the transcriptions used for checking: Claude Sonnet and a vote of three Claude Opus readers (`calib/`, `codex/`, `second/`, `third/`).
4. The content of the letter (summary above).

## Usage
```
python3 src/decode.py data/key.tsv data/transcription_f120r.txt                # with inferred values
python3 src/decode.py data/key.tsv data/transcription_f120r.txt --no-inferred  # table + Burford only
python3 src/decode.py data/key.tsv data/transcription_f120r.txt --table-only   # table only
python3 src/control.py data/key.tsv data/transcription_f120_all.txt 1000       # control (needs wordfreq)
python3 src/calib.py data/key.tsv calib/transcription_f104r_l18-24.txt calib/ref_f104r_l18-24.txt --key-at-calibration  # calibration (characters, key at the time)
python3 src/calib.py --signs calib/transcription_f104r_l18-24.txt calib/ref_signs_f104r_burford.txt 1  # calibration (signs, strict)
python3 src/calib.py --lenient data/key.tsv calib/transcription_f104r_l18-24.txt calib/ref_signs_f104r_burford.txt 1  # calibration (signs, counted as Burford does)
python3 src/compare2.py data/transcription_f120r.txt second/transcription2_f120r.txt --key data/key.tsv  # first vs the Sonnet transcription
python3 src/calib.py --lenient --no-alias data/key.tsv calib/transcription_f104r_l18-24_context.txt calib/ref_signs_f104r_burford.txt 1  # calibration, same way of reading as the published transcription
python3 src/vote.py third/f104r_vote.txt third/f104r_pass1.txt third/f104r_pass2.txt third/f104r_pass3.txt  # three-reader vote
python3 src/calib.py --lenient --no-alias data/key.tsv third/f104r_vote.txt calib/ref_signs_f104r_burford.txt 1  # accuracy of the vote
python3 -m unittest discover -s tests
```

## Use of AI
See "Status" above and "Use of AI" in [docs/METHOD.en.md](docs/METHOD.en.md). No person has checked the transcription.

## Files
| Path | Content |
|---|---|
| data/transcription_f120r.txt, f120v.txt | transcription in sign names (line by line) |
| data/transcription_f120_all.txt | both pages together (recto c101–, verso c201–) |
| data/key.tsv | sign name → value; source marked table (Tomokiyo), burford (Burford's alignments), inferred (this letter) or unknown; notes in Japanese and English |
| data/decoded_*.txt | output of `src/decode.py` |
| docs/READING.en.md, METHOD.en.md, OPEN.en.md | reading, method and figures, open points (Japanese versions without .en) |
| calib/ | calibration on f. 104r lines 18–24 (transcription and references, CC BY 4.0 for the references) |
| codex/ | independent second transcription (OpenAI's Codex, by shape only), the prompt given, and its decoding; run1_misaligned/ is the first run, on images whose right halves were shifted |
| calib/transcription_f104r_l18-24_context.txt | calibration transcription by the same way of reading as the published one (decoding with the key) |
| second/ | transcription used for checking (Claude Sonnet, by shape only) and its decoding |
| third/ | transcriptions by three Claude Opus readers (f. 104r lines 18–24 and f. 120) and their vote |
| src/ | decoding, control, calibration, comparison, vote, image preparation |
| docs/PRIOR_CHECK.en.md | check for prior work (places, dates, places not reached) |
| SOURCES.en.md | sources and the check for prior work |

Licence: code MIT; our documents and data CC BY 4.0 ([LICENSE](LICENSE)).
