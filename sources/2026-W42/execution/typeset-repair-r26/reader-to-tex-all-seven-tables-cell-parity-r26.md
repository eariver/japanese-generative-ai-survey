# W42 r26 — Reader→TeX all-seven-tables cell parity, fresh (NONCANONICAL)

Method: direct comparison of **r18 Reader JSON bytes** (blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`) against **r26 print TeX bytes** (blob `ffdd45742c16fc2f19fd21805479ca9d8373f30b`). No r22/r25 transitivity is used anywhere. Checker: edition-local script (rules below); result `PARITY PASS`.

## 1. Parser rules (explicit; no hidden normalization)

Reader TABLE blocks (`block_type == "TABLE"`, 7 total, package order P1..P7):
- R1: block text split on `\n` (U+000A). First line MUST match `【比較表：X】`; caption `X` (brackets stripped) compared to TeX `\captionof{table}{X}` byte-for-byte.
- R2: remaining lines = data rows, in order. Each row split on `｜` U+FF5C FULLWIDTH VERTICAL LINE. Verified fact: ASCII `|` (U+007C) occurs **zero** times in all 7 TABLE texts, so U+FF5C is the unambiguous cell delimiter. No escape mechanism exists in Reader TABLE texts.
- R3: cells stripped of surrounding whitespace only. NOTHING else is removed or normalized: currency units (`米ドル`, `ドル`), parenthetical qualifiers (`（法主体の年商）`, `（ファイルなし）`), numbers, provenance/uncertainty terms (`未確認`, `未検証`, `発行者`), license names, URLs (none inside cells), and semantic punctuation (`：`, `・`, `、`, `。`) are all compared byte-for-byte.

Print TeX tables (7 `tabularx` environments, source order T1..T7 ↔ P1..P7):
- T1: body = text between `\toprule` and `\bottomrule`.
- T2: `\midrule` separator LINES deleted first (they share chunks with following rows after splitting — a naive chunk filter drops the next row; this was caught and fixed during r26 execution, documented here so re-audits do not repeat it).
- T3: split rows on the two-character TeX row terminator `\\` (U+005C U+005C). Verified fact: no cell contains a literal `\\`, `\_`, `\&`, `\%`, `\#`, or other backslash escapes anywhere in the 7 bodies, so no escape handling is required; this was checked, not assumed.
- T4: split cells on `&`. Strip each cell of `\cite{...}` groups (regex `\\cite\{[^}]*\}`) and surrounding whitespace only. Citations are verified separately (§4); their removal here isolates *word* fidelity.
- T5: visible-caption numbering (`表 1`..`表 7`) is a LaTeX counter product of source-ordered `\captionof`; order match is asserted by positional pairing T1..T7 ↔ P1..P7 plus exact caption-string match.

Comparison: row count per table, cell count per row, then byte equality per cell. Any parse failure (unknown row terminator, unbalanced splits, caption mismatch) is a STOP, not a skip.

## 2. Results — per-row / per-cell

| table | Reader block | rows (Reader ↔ TeX) | cells/row (Reader ↔ TeX) | total cells | mismatches |
|---|---|---|---|---|---|
| T1 | P1 `t1-13` | 2 ↔ 2 | [5,6] ↔ [5,6] | 11 | 0 |
| T2 | P2 `t2-11` | 2 ↔ 2 | [4,4] ↔ [4,4] | 8 | 0 |
| T3 | P3 `t3-18` | 6 ↔ 6 | [4,4,5,4,3,3] ↔ same | 23 | 0 |
| T4 | P4 `t4-15` | 6 ↔ 6 | [5,5,4,4,4,4] ↔ same | 26 | 0 |
| T5 | P5 `t5-11` | 4 ↔ 4 | [4,3,4,4] ↔ same | 15 | 0 |
| T6 | P6 `t6-14` | 4 ↔ 4 | [4,4,4,3] ↔ same | 15 | 0 |
| T7 | P7 `t7-09` | 3 ↔ 3 | [4,4,4] ↔ same | 12 | 0 |
| **total** | 7 blocks | **27 ↔ 27** | — | **110** | **0** |

Captions 7/7 byte-identical (`比較表：WonderとArgonの読み分け`, `効率主張の読み分け`, `重み・実装・ライセンス`, `生産性とゲートの条件`, `安全の四つの局面`, `科学エージェントの証拠`, `専門・身体の三件`).

The two audit-flagged cells now match byte-for-byte:
- T2 LFM2.5 tail: `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）` ✓ (was `…商用上限1000万ドル` in r22/r25)
- T3 Nemotron tail: `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用` ✓ (was `…Super VL未開封、…` in r22/r25)

## 3. Non-TABLE blocks (150/150)

All 150 non-TABLE Reader blocks (HEADING 7, PARAGRAPH 136, NOTE 7) are byte-contained in r26 TeX: **150/150 literal inclusion**. (TeX appends `\cite{...}` after paragraphs and wraps notes in `tcolorbox`; containment of the raw Reader prose is unaffected.) Total Reader surface re-verified: 157 blocks, 7 chapters P1–P7, 28 MATERIAL selection topics (materiality-r7 `28/14/7/1`), 19 aliases / 177 ledger lines (see §4–5).

Known editorial boundaries preserved (unchanged from r18, verified present in TeX): Argon random one-run Minecraft world; Maia 24-tray/96-accelerator/750GB/s; Earth dependent negatives; native MTP accepted-token *length* (not rate); wet-lab 131/311 screening vs independent 8-clone step; LFM legal-entity cap; ASPIRE real-robot results with publisher limits.

## 4. Citations (regenerated, not copied)

- TeX `\cite{...}` occurrences expanded: **729 total uses, 90 unique keys, 0 unknown** (checked against bibmap 90 keys `B01`–`B90`). Audit-reported `729/90/0` reproduced exactly by fresh count.
- `reader-preview` citation repair ledger: **177 rows** (`PARAGRAPH 135 / TABLE 8 / TABLE_ROW 27 / NOTE 7`) — matches audit; TABLE_ROW 27 = one ledger row per printed table row (2+2+6+6+4+4+3 = 27 ✓, cross-checks §2 row totals).
- In-print `[二次・参考]` labels: 17; `[SECONDARY]` leaks: 0.

## 5. Bibliography (regenerated, not copied)

- TeX `\bibitem`: 90 entries, key set 1:1 with bibmap 90 keys.
- `alias_of` entries: 19; duplicate-matrix: 19 pairs, alias sets equal, all `identical`-mapped to same canonical (B62→B01 … B88→B59 etc.).
- Non-alias URLs: 71/71 byte-present in TeX `\url{...}` vs bibmap URL strings (HTTP liveness NOT tested — same boundary as independent audit).
- Display corrections: 7 `[二次・参考]` category labels on alias entries; B28 (BFL model API), B57 (NVlabs/ASPIRE), B74 (OpenBMB/MiniCPM-V), B90 terminal `https://huggingface.co/LiquidAI/LFM2.5-24B-A2B` all verified in print (p19–p21 images).
- Machine-ID scan: `candidate:2026-W42`, `TODO`, `FIXME`, `REVIEW-LEAK` — 0 hits in r26 TeX.

## 6. Verdict

Fresh r18→r26 comparison: **27 rows / 110 cells / 0 substantive mismatches; 150/150 non-TABLE identical; cites 729/90/0-unknown; bib 90/19/71.** Both audit-flagged cells restored. Zero TeX warnings alone do not certify this — the cell table above does.
