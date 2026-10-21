# J-GAS W42 — Muse r26 Reader-fidelity repair and physical-print regression

Date: 2026-10-19 JST
Status: `SOL_EXECUTION_AUTHORITY / INDEPENDENT_R25_REQUEST_CHANGES / R26_EXACT_TWO_CELL_REPAIR / NONCANONICAL_ONLY`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W42-v2-work`

## 0. Exact remote guard / immutable scope

Sol dispatch supplies Exact Starting Remote HEAD and Expected Root Tree matching the commit containing this instruction. Before ANY writes verify remote branch HEAD AND root Tree, plus:
- reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / Tree `801de813319f08777ab1581a5e8875fc1ac5df19`
- Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- audited r25 baseline HEAD `b992685a66ccfd9eef3073a448771d2f224bea9c` / Tree `d552721744c4e8b6e71adf0bdb90753f36036066`.

Missing proof or mismatch => `ZERO_WRITES_STOP` with expected/actual. Recheck remote lease before any push. Existing branch, normal fast-forward commit + non-force push only; never create alternate/fallback/repair/review branch, reset/rebase/force or rewrite history.

All shared Core/main and canonical W42 Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/Architecture/Draft/Synthesis/State/checkpoints/Human Gates must remain byte-exact, including r1 Human Architecture APPROVED and pending Publication Preview. r18 Reader JSON blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, all r18 proposals/maps/ledgers, ALL historical execution r11–r25 (including the original independent report), and any formally issued PDF remain immutable. Only NEW r26 artifacts in `sources/2026-W42/execution/typeset-repair-r26/`, `execution/diagnostic-r26/`, `execution/sessions/muse-w42-r26-20261019.md`, and truthful append-only `execution/index.md` permitted. No official Reader, Architecture r2, Human Gate, Publication, Freeze or Release.

## 1. Mandatory read order and exact source repairs

1. Read `execution/reviews/independent-w42-r25-print-audit-REQUEST_CHANGES-20261019.md` (verbatim user-provided independent audit), then `execution/reviews/sol-w42-r25-independent-audit-disposition-20261019.md`.
2. Read exact r18 `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` (authoritative master) and all v18 chapter proposals, bibliography map, alias matrix, citation repair ledger.
3. Read r25 `execution/diagnostic-r25/main.tex`, `main.pdf`, manifest/log/ALL 21 page PNGs, invariant checker/7-table ledger; r22 diagnostic TeX to see earlier provenance.

Two required changes **within the newly generated NONCANONICAL r26 print TeX only**:
- P2/Table2/LFM2.5, r18 block `t2-11`: restore exactly `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）`. Current r25 last part is merely `商用上限1000万ドル`; forbidden.
- P3/Table3/Nemotron3.5, r18 block `t3-18`: restore exactly `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`. Current r25 variant `Super VL未開封`; forbidden.

Preserve original in-cell citations `B11,B69,B12` and `B21,B72,B22,B20`; no rewriting/shortening of any other cell, caption, Reader paragraphs, seven notes, headings, technical terms, claim scope, quote or source authority. These strings were already incorrect in r22, so do not claim this to be a multicol bug.

## 2. NEW fresh Reader→TeX full cell parity, not inherited

Implement a reliable edition-local comparison of **every cell of every row in all 7 TABLE blocks** against r18 Reader, aligning by chapter/table/row identity/cell index. Reader TABLE is pipe/newline delimited; print TeX is `tabularx` with `&` and LaTeX markup: explicitly document parser rules for `\cite{}`, legitimate TeX escapes/line wraps, visible caption numbering etc. Only remove presentation commands and harmless whitespace to compare actual words. DO NOT normalize away currency units, parentheses, numbers, "法主体の年商", "ファイル未確認", provenance/uncertainty terms, licenses, URLs or semantic punctuation. Record row/cell totals and all mismatches; stop on unknown parse or nonzero substantive difference. Compare exact r18 cells to extracted **r26 TeX** cells; prior r22/r25 source/print transitivity is NOT a substitute.

Recheck 150/150 nonTABLE Reader blocks (HEADING7, PARAGRAPH136, NOTE7), 157 total blocks, 28 topics, citation map (90 unique B keys, 19 aliases, 177 ledger lines), 7 visible captions, all seven notes and known editorial evidence boundaries. Audit reports `\cite{}` 729 uses, 90 unique, zero unknown; regenerate actual counts rather than copy. All table cells/rows and restored strings must also appear in actual PDF and individual page images. Zero TeX warnings alone does NOT certify source fidelity.

## 3. Keep r25 MULTICOL-V2 geometry; rebuild ALL pages and prove no regression

Use r25 print TeX/style as **physical-layout baseline**; retain two-column `multicol` segments, `captionof` full-width atomic tables, gutter/margins/font/baselines, physical reading order and bib flow. Only two cell text restorations permitted; if restored text changes table height or pagination, minimal **print-only wrapper/needspace** changes allowed, documented with precise diff and justification (baseline needspace table1..7 = 18/18/30/30/22/22/20). Never shrink/change typography/column geometry, remove words, split captions/rows, pad content, or chase arbitrary 21 pages.

Build deterministically with LuaLaTeX, preserve complete TeX/sty/PDF/compilation log and hash manifest. Open and audit **each page PNG** from resulting full PDF, not just contact sheets. For EACH table T1–T7 identify physical page, caption+ALL rows/cites on SAME page, chapter inclusion, exact printed ending of preceding sentence and opening of following, no paragraph/sentence/word bisection, no footer collision/clipping, no table-only leaf. Check r22 broken `立直し`, `分母の開示`, `エンドポイント`, `染料と水による検証`; r24 Table3 caption orphan and Table4 Decider row clip; r25 Table7 ASPIRE boundary; newly expanded T2 and T3 cells fully printed and still atomic. Keep acceptable body fill, no new giant p18 508/702-char left-only tail; record blank regions honestly (area UNMEASURED unless measured).

Whole-magazine regressions: cover diagnostic 3 lines, 7 headings/notes, B01–B90 bibliography 71 full/19 aliases, 7 secondary label display corrections, B28/B57/B74/B90 intact and terminal B90; citations and 177 ledger; zero machine IDs; stable links/URLs/caveats (Argon random one-run Minecraft, Maia24/96/750GB/s, Earth dependent negatives, native MTP accepted-token length rather than rate, wet-lab131/311 and independent 8 clones, LFM legal entity, ASPIRE real robot results and publisher limitations). Investigate all errors, overfull/underfull, missing characters and warnings rather than suppress. 21 pages is Sol tentative not mandatory, and official Architecture page plan remains unchanged.

## 4. Required versioned evidence / final STOP

Write only NEW:
- `typeset-repair-r26/independent-audit-two-cell-origin-and-patch-r26.md`: exact r18/r22/r25/r26 source comparisons and why historical false PASS;
- `typeset-repair-r26/reader-to-tex-all-seven-tables-cell-parity-r26.md`: fresh parser, per-row/per-cell counts and zero substantive mismatches;
- `typeset-repair-r26/physical-page-and-table-regression-r26.md`: full physical 7-table ledger, all pages, whiteness/citations/chapters/old faults;
- `typeset-repair-r26/option-b-pageplan-r26.PROPOSED.md`: actual physical cover/body/bibliography, no Gate amendment;
- `diagnostic-r26/`: actual TeX, unchanged style copy, PDF, full log, SHA256 manifest, ALL individual page PNGs and contact sheets, precise review index;
- `execution/sessions/muse-w42-r26-20261019.md` and append-only execution index.

Pass only if BOTH exact restored Reader cells are visibly intact in PDF, all 7 table-cell comparisons 0 mismatches, all 150 nonTABLE blocks identical, all 7 captions/rows/cites physically complete, no print geometry/reading-order or bibliography regressions, immutable scope untouched. Terminal on verified success: `SOL_W42_R26_FOCUSED_INDEPENDENT_REAUDIT_READY / NONCANONICAL`. Any failure: `R26_READER_FIDELITY_OR_LAYOUT_BLOCKED` with full evidence; never falsely call PASS. Normal commit/non-force push and remote HEAD/Tree read-back.

Worker READY is not Sol or external audit approval. After r26 Sol will request a **new focused independent read-only re-audit** before separate Human Option B Architecture page-plan decision or canonical Reader/Publication.
