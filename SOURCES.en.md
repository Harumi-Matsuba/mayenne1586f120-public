# Sources

[日本語](SOURCES.md)

## Primary sources (not included in this repository)
- **BnF, Français 15573**
  - Gallica ark:/12148/btv1b90618780
  - View 246: f. 120r (31 lines of cipher throughout). https://gallica.bnf.fr/ark:/12148/btv1b90618780/f246.item
  - View 247: f. 120v (8 lines of cipher). https://gallica.bnf.fr/ark:/12148/btv1b90618780/f247.item
  - View 213: f. 104r (used for the calibration; cipher lines 18–24). https://gallica.bnf.fr/ark:/12148/btv1b90618780/f213.item

The images are not redistributed; please refer to them by view number. Source gallica.bnf.fr / BnF.

## Key
- Satoshi Tomokiyo, *French ciphers during the Reigns of Charles IX and Henry III* (Cryptiana)
  - https://cryptiana.web.fc2.com/code/henryiii.htm (Last-Modified 2023-09-23)
  - List for BnF fr. 15573: « f.120 (p.248) Endorsement illegible (to me). Undeciphered. Uses Mayenne-Forget's Cipher-2. »
  - Table image: https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png (not included here)
- Brett Burford, *First reading of the whole cipher letter BnF fr. 15573 f. 385 (Mayenne-Forget Cipher-2, 1586)*
  - https://github.com/BravoBravoIX/mayenne-forget-1586-cipher-reading (commit cc0daf749aecebae0e7eb163035abe9ba679a9d3, 19 October 2026; documents and data CC BY 4.0)
  - `data/key-cipher2.json`: the `table` and `burford` rows of `data/key.tsv` copy the values and origin marks of this key (the original marks are kept in columns 4 and 5).
  - `method/sheet-v3.png`: the reference sheet of sign names. The image is not included here.
  - `data/known-text/f104r-decipherment.txt` (commit cc0daf74): his eye-reading of the contemporary decipherment of f. 104r. Part of it was copied into `calib/ref_f104r_l18-24.txt` (calibration reference). After copying, it was checked against the image of view 213, and « qui reste icy » was changed to « qui restent icy » (20 October 2026).
  - `data/known-text/ref-104r-l18-24.txt` (commit 22ab58c39dbd98a853044349d98294af93124e30, 19 October 2026): sign transcription of the cipher of f. 104r, copied unchanged into `calib/ref_signs_f104r_burford.txt` (calibration reference).

## Transcription used for checking (Sonnet)
- `second/transcription2_f120r.txt`, `f120v.txt`: read by Anthropic's Claude Sonnet from the image tiles, Burford's reference sheet and a list of sign names with shape descriptions only, without seeing the first transcription (20 October 2026). Compared with the first as an independent reading by a different reader ([docs/METHOD.en.md](docs/METHOD.en.md)).

## Independent second transcription (Codex)
- `codex/transcription_codex_f120*.txt`: read by OpenAI's Codex CLI (codex-cli 0.163.0-alpha.10.2, default model) from the line images, Burford's reference sheet and `codex/PROMPT.md` (sign names and shape descriptions only) (20 October 2026). Run after the first transcription had been corrected; the first was not corrected from this comparison.

## Transcriptions by three readers
- `third/*_pass1–3.txt`: f. 104r lines 18–24 and f. 120, read separately by three blind Claude Opus readers (subagents) from the line images, Burford's reference sheet and a list of sign names with shape descriptions only (20 October 2026). The vote is in `third/*_vote.txt` ("Three-reader vote" in [docs/METHOD.en.md](docs/METHOD.en.md)).

## Model for the method
- Harumi-Matsuba, *matignon1586-public* (a reading of another Cipher-2 letter, BnF fr. 15572 ff. 218–219)
  - https://github.com/Harumi-Matsuba/matignon1586-public
  - The scripts (`src/decode.py`, `src/control.py`, `src/calib.py`) are based on it, and the calibration follows its `docs/METHOD.md` (its agreement on f. 103v was 74.8%).

## Check for prior work
Not finding something does not prove that nobody has worked on it.

| Where | Date, version | Result |
|---|---|---|
| Cryptiana (henryiii.htm) | Last-Modified 2023-09-23 | f. 120 is « Undeciphered » |
| Cryptiana (unsolved.htm, ai.htm) | Last-Modified 2026-10-13, 2026-10-19 | only the dates were checked; the text was not read |
| D. Bourdeau, cyphersolver (https://github.com/dbourdeau/cyphersolver) | origin/main 0258b8ab (2026-10-18); issues and PRs up to #48 (checked 2026-10-20) | "15573" is in neither catalogue.json nor the NOTES under targets/. In the nine files containing "15573" (copies of Tomokiyo's page, Gallica search results, etc.) there is no mention of f. 120 near it. Not in the titles of issues and PRs |
| Brett Burford (GitHub BravoBravoIX): list of repositories and the two fr. 15573 repositories (f. 385, ff. 379–381) | latest 2026-10-19T12:24Z (checked 2026-10-20) | no repository for f. 120; no file name containing "120" in the two repositories |
| NoAutopilot/cipher-lab | checked 2026-10-20 | "15573": 0 hits in issue and commit search |
| pangoleen/cipher-readings | checked 2026-10-20 | no folder for fr. 15573 |
| Cryptoole (https://cryptoole.satoru.net/api.cgi) | 2026-10-20, all 854 items | no item containing "15573", "Mayenne", "Forget" or "Marsil" |
| GitHub repository search (15573, mayenne cipher, forget 1586) and code search (15573 "f. 120" etc.) | 2026-10-20 | relevant: only Burford's repositories and Harumi-Matsuba/matignon1586-public |
| Web search | 2026-10-19, 3 searches (in the conversation before this work) | nothing relevant |

Not checked: the DECODE search interface, Lasry's list of papers, the Cryptiana blog.
