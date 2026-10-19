# W42 r29 Reader fidelity and bibliography parity (fresh, r18 → canonical TeX)

Status: deterministic source-fidelity evidence (not a semantic PASS)
Date: 2026-10-20 JST
Primary: `surveys/weekly/2026-W42/main.tex` (SHA256 `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3`)

## 1. Tables (7/7, 27 rows / 110 cells, 0 substantive mismatches)

Method: r18 JSON `TABLE` blocks split by `｜`; TeX `tabularx` bodies split by `\\` / `&` with `\cite{...}` stripped (same as independent r26 audit, fixed column-spec handling). Titles via `\captionof{table}`.

| Table | r18 rows/cells | TeX rows/cells | Content diff | Caption | Print page |
|---|---|---|---|---|---|
| T1 Wonder/Argon | 2 / 11 | 2 / 11 | 0 | PASS | p04 |
| T2 Maia/LFM2.5 | 2 / 8 | 2 / 8 | 0 | PASS | p06 |
| T3 open weights etc. | 6 / 23 | 6 / 23 | 0 | PASS | p09 |
| T4 productivity/gates | 6 / 26 | 6 / 26 | 0 | PASS | p12 |
| T5 safety 4 aspects | 4 / 15 | 4 / 15 | 0 | PASS | p14 |
| T6 science agents | 4 / 15 | 4 / 15 | 0 | PASS | p16 |
| T7 specialist/embodied | 3 / 12 | 3 / 12 | 0 | PASS | p17 |
| Total | 27 / 110 | 27 / 110 | 0 | 7/7 | 7 tables |

Restored cells (r25 blockers, closed in r26, preserved in r29):

- T2 LFM2.5 `商用上限1000万米ドル（法主体の年商）` present (TeX count 1, PDF p06 text contains `法主体の年商`)
- T3 Nemotron `Super VLファイル未確認` present in TeX; PDF p09 shows `Super VL` + `ファイル未確認` across lines (extraction splits lines, PNG visually intact)
- Old errors absent in TeX: `商用上限1000万ドル` (short form) 0; `Super VL未開封` 0

## 2. Non-table blocks (150/150)

All 150 nonTABLE Reader blocks (7 HEADING + 136 PARAGRAPH + 7 NOTE) from r18 are literal substrings of canonical TeX. Missing: 0.

## 3. Citations / bibliography / URLs

- `\cite` calls: 169; expanded keys: 729; distinct: 90; unknown: 0
- `\bibitem`: 90; bibmap keys B01–B90: 90; missing/extra: 0
- alias: 19/19 match duplicate matrix; ledger: 177 rows = PARAGRAPH 135 + TABLE 8 + TABLE_ROW 27 + NOTE 7
- non-alias URL entries: 71 `\url{...}` present
- secondary badges `[二次・参考]`: 17; untranslated `[SECONDARY]`: 0
- internal IDs: `candidate:2026-W42`, `TODO`, `FIXME`, `REVIEW-LEAK`: all 0
- diagnostic-only strings: `NONCANONICAL`, `NOT A PUBLICATION`, `NOT FOR HUMAN`, `診断用・非正準・未承認`: all 0

Caveats preserved (per contract): Argon random world + one run; Maia 24/96/750GB/s; Earth model-dependent negatives; MTP mean accepted-token length not rate; wet lab 131/311 vs 8 clones; LFM legal-entity sales denominator; ASPIRE real-robot result + publisher limits; B28/B57/B74/B90 + 17 secondary badges; 71 full URLs.

## 4. Separation

Source fidelity (this report) is distinct from printed PDF text/visual checks (see physical ledger + PNGs). No inherited blanket PASS from r26; fresh comparison on exact canonical bytes.
