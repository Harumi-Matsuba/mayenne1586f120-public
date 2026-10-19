# Check for prior work (BnF fr. 15573 f. 120, 20 October 2026)

[日本語](PRIOR_CHECK.md)

## Conclusion
- **Category: not found.** In the places checked below, nothing was found that reads the cipher of this letter (BnF fr. 15573 f. 120r–v), shows a correspondence between its ciphertext and a plaintext, or gives its plaintext (a contemporary decipherment or a printed edition).
- Not finding something does not prove that nobody has read it. The reading in this repository is not called the "first".
- **Limit of this check:** RULES.md 2.2 (5) asks for the search to be made, with the aim of disproving novelty, by a session other than the one that read the letter. This check was made, on the user's instruction, by the same Claude Code session that read the letter, so that condition is not met: the side that might have missed something searched for it itself.

## Places checked (20 October 2026, 01:00–02:30 JST)
| Where | Date, version | How | Result |
|---|---|---|---|
| Cryptiana (Satoshi Tomokiyo), henryiii.htm | Last-Modified 2023-09-23 | read the list for fr. 15573 | f. 120: « Endorsement illegible (to me). Undeciphered. Uses Mayenne-Forget's Cipher-2. » |
| Cryptiana unsolved.htm, ai.htm, verification.htm, GL.htm | 2026-10-13, 10-19, 10-15, 10-15 | searched the text for "15573", "Marsil", "Montablay", "Bilart" | only GL.htm (Lasry's solutions) has fr. 15573 f. 127 (Duval to Villeroi); no f. 120 |
| Cryptiana blog (cryptiana.blogspot.com) | latest 100 feed entries (2025-07-06 to 2026-10-15) | the same words and "Mayenne", "Forget" | nothing |
| D. Bourdeau, cyphersolver (ledger) | origin/main 0258b8ab (2026-10-18) | `git grep` for "15573", "marsil", "montablaye", "bilart" | no entry for f. 120. Hits are the same words in other documents (« le Sr de Vesin de la Marsilliere » in docs/navarre1586.html, the word list under targets/matignon1586, etc.) |
| Same, issues and PRs | up to #49 (2026-10-19) | titles and bodies for "15573", "f. 120", "Marsil", "Montablaye" | hits: #44, #46 (Burford, other leaves of fr. 15573) and #49 (ours, fr. 15572) |
| Brett Burford (GitHub BravoBravoIX) | latest in the repository list 2026-10-19T12:24Z | the list and the two fr. 15573 repositories | no repository for f. 120 |
| NoAutopilot/cipher-lab | 2026-10-20 | issue, commit and code search for "15573"; of the 10 files found by code search, the text of the 5 likely ones (LESSONS-TOMOKIYO.md, sources/pools-scout/2026-10-03/P1.md, the NOTES.md and second-opinions of ciphers/matignon-mayenne-1586, sources/cryptiana/CRYPTO-INDEX.tsv) | issue #72 is our own report on fr. 15572. In the 5 files, "15573" occurs in catalogue copies, Lasry's f. 127 and notes that fr. 15573 should be looked at; no reading of f. 120. The other 5 files are folders of other ciphers (baluze167, sp99, armstrong) and were not read |
| pangoleen/cipher-readings | 2026-10-20 | folder list and issue search | no fr. 15573 |
| Cryptoole (https://cryptoole.satoru.net/api.cgi) | 2026-10-20, all 854 items | "15573", "Mayenne", "Forget", "Marsil", "Montablay", "Bilart" | nothing |
| DECODE (decode-catalog.csv in aaymeloglu/unsolved-ciphers, a copy of the DECODE catalogue) | 10,106 records, updated 2026-10-09 | "15573", "Mayenne", "Forget" | nothing |
| BnF catalogue (Archives et manuscrits, Français 15573) | fetched 2026-10-20 | read the description of contents | no entry for f. 120 and no mention of a decipherment. Nearby leaves listed: ff. 114, 118 (L'Aubespine-Chasteauneuf), f. 119 (documents on the negotiations with the King of Navarre) |
| GitHub code search | 2026-10-20 | « Marsiliere », « Marsilliere », « Montablaye », « Mayenne Forget Cipher-2 » | « Marsilliere »: Armael/voyageur and cyphersolver (other documents); « Mayenne Forget Cipher-2 »: cipher-lab and cyphersolver (as above); « Marsiliere », « Montablaye »: 0 |
| GitHub repository search | 2026-10-20 | "mayenne cipher", "15573", "forget 1586", "henri III cipher" | relevant: only Burford's repositories and this one |
| Web search (English, French, Japanese) | 2026-10-20, 7 searches | shelfmark with f. 120, plaintext phrases (« Marsillière », « Montablaye », « Bilart », « six sepmaines … estonnés »), Japanese | nothing |

## Not reachable or not checked
- Gallica full-text search: 403 (Cloudflare) with curl; not used.
- The DECODE search interface itself (only the catalogue copy was checked).
- The text of printed collections (Berger de Xivrey, *Recueil des lettres missives de Henri IV*; *Archives historiques de la Gironde*; L'Estoile's journals, etc.). Only web searches for the phrases were made; the texts were not read.
- The text of Lasry's papers (only the list in Cryptiana's GL.htm).

## Notes (not prior work, but leads for the content)
- The ledger's docs/navarre1586.html mentions « le Sr de Vesin de la Marsilliere » as an envoy of the King of Navarre. This suggests that the « secretaire La Marsilière » of the letter may be on the King of Navarre's side (not checked).
- The BnF catalogue describes f. 192 of the same volume as an intercepted original letter addressed to a secretary of the chamber of the King of Navarre. This may be related to the letter's « [?] du secretaire La Marsilière … tombé entre les mains » (not checked).
