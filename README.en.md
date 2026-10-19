# BnF fr. 15573 f. 120, a cipher letter in Mayenne–Forget's Cipher-2 (1586): a first reading

[日本語 README](README.md)

A reading of an undated cipher letter of unknown sender, BnF Français 15573 f. 120, with Mayenne–Forget's Cipher-2 as reconstructed by Satoshi Tomokiyo and the key that Brett Burford built for another Cipher-2 letter in the same volume.

- Source: BnF Français 15573 (letters of 1586; in Tomokiyo's list, ff. 7–8 are a letter of August 1586), Gallica ark:/12148/btv1b90618780, view 246 (f. 120r, 31 lines of cipher) and view 247 (f. 120v, 8 lines of cipher). There is no plaintext on these two pages.
- Prior work: Tomokiyo lists f. 120 as a Cipher-2 letter, « Endorsement illegible (to me). Undeciphered. » ([Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm), last modified 2023-09-23). In what we checked on 19–20 October 2026, no reading of this letter was found (see [SOURCES.en.md](SOURCES.en.md)).

## Status (v0.2, partial)
| Page | Signs | Valued by Tomokiyo's table only | Table + Burford's alignments | Also inferred in this letter |
|---|---|---|---|---|
| f. 120r | 887 | 89.1% | 96.7% | 98.2% |
| f. 120v | 216 | 85.6% | 97.7% | 98.6% |
| Total | 1,103 | 88.4% | 96.9% | 98.3% |

- In a control with the letter values of the key shuffled (1,000 times), no shuffled key scored as French-like as the real key, in all three conditions ([docs/METHOD.en.md](docs/METHOD.en.md)).
- Many lines read as French sentences ([docs/READING.en.md](docs/READING.en.md)). 13 kinds of signs (19 places) have no value, and some short stretches are not read ([docs/OPEN.en.md](docs/OPEN.en.md)).
- **Calibration:** seven lines of f. 104r, a Cipher-2 letter with a contemporary decipherment, were transcribed by the same method without looking at the decipherment. Character agreement with the decipherment was 70.6% (62.9% with table signs only); the character reference was checked on the image. Sign accuracy, counted as Burford counts, is 86.9–89.1% (his single passes: 91.1–93.5%). With the key revised after the calibration (the backslash-with-o sign is *pour*), it is 73.4%, but that figure comes after seeing the answer.
- **Second transcription:** another AI (Claude Sonnet) re-read both pages by shape only, without seeing the first transcription. Agreement of values with the first is 87.7% (recto) and 87.0% (verso); most differences fall in three look-alike pairs (ls/S, r/xbar, 8s/8). Decoded with the same key, the second transcription also gave 0 / 1000 in the control.
- Please use the transcription on the assumption that details may be wrong. See "Calibration" and "Second transcription" in [docs/METHOD.en.md](docs/METHOD.en.md).

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
3. A calibration (seven lines of f. 104r) and an independent second transcription by another AI (`calib/`, `second/`).
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
python3 src/compare2.py data/transcription_f120r.txt second/transcription2_f120r.txt --key data/key.tsv  # first vs second transcription
python3 -m unittest discover -s tests
```

## Use of AI
The transcription, the inferred values, the decipherment, the scripts and the documents were made by Anthropic's Claude (Claude Code, Claude Opus 5.5); the second transcription by Claude Sonnet. A person chose the target, saved the images and decided to publish. The transcription was not checked by a person. Details in [docs/METHOD.en.md](docs/METHOD.en.md).

## Files
| Path | Content |
|---|---|
| data/transcription_f120r.txt, f120v.txt | transcription in sign names (line by line) |
| data/transcription_f120_all.txt | both pages together (recto c101–, verso c201–) |
| data/key.tsv | sign name → value; source marked table (Tomokiyo), burford (Burford's alignments), inferred (this letter) or unknown; notes in Japanese and English |
| data/decoded_*.txt | output of `src/decode.py` |
| docs/READING.en.md, METHOD.en.md, OPEN.en.md | reading, method and figures, open points (Japanese versions without .en) |
| calib/ | calibration on f. 104r lines 18–24 (transcription and references, CC BY 4.0 for the references) |
| second/ | second transcription (Claude Sonnet, by shape only) and its decoding |
| src/ | decoding, control, calibration, comparison, image preparation |
| SOURCES.en.md | sources and the check for prior work |

Licence: code MIT; our documents and data CC BY 4.0 ([LICENSE](LICENSE)).
