# J-GAS W42 — r25 independent print-quality audit, one-shot READ-ONLY

Date: 2026-10-19 JST
Status: `INDEPENDENT_REVIEW_REQUEST / PRINT_AND_SOURCE_EQUIVALENCE / FIXED_R25_COMMIT / READ_ONLY_NO_GATES`
Repository: `eariver/japanese-generative-ai-survey`
**Audited fixed commit:** `b992685a66ccfd9eef3073a448771d2f224bea9c`
**Audited fixed root Tree:** `d552721744c4e8b6e71adf0bdb90753f36036066`
Current Sol editorial review file is outside this fixed commit in later branch history; it is not an independent-source substitute.

## 0. Independence and permissions

You are a fresh, independent read-only Sol/ChatGPT reviewer, not the worker Muse and not the editorial Sol who performed first-pass review. Do NOT accept Muse's `READY` or Sol's `PASS_TO_INDEPENDENT_AUDIT` as evidence of print correctness. Examine GitHub at exact fixed r25 commit, and compare earlier failures yourself. NO GitHub/repository writes, no commands to Stage/Reader/Publication/Architecture/Human Gate/Freeze/Release, no branch creation, no code/paper edits.

Before reviewing record actual GitHub commit/root tree, whether reviewed `main` and frozen Core unchanged if accessible, and the authoritative production state at this exact commit. If evidence cannot be inspected, mark scope UNVERIFIED, not PASS.

## 1. Materials in review priority order

1. `sources/2026-W42/execution/diagnostic-r25/main.pdf`, `build-manifest-r25.json`, `main.tex`, `preview.sty`, complete `main.log`, **ALL 21 individual `pages/p-01.png` through `p-21.png`**. Inspect images individually; contact sheets are supplementary only.
2. `execution/typeset-repair-r25/global-seven-table-source-to-physical-ledger-r25.md`, `reader-content-and-bib-invariance-r25.md`, `phaseA-two-system-geometry-and-interoperability-r25.md`, `human-option-b-pageplan-r25.PROPOSED.md`, worker session and review-page index.
3. The authoritative unmodified r18 Reader `execution/editorial-revision-r18/reader-preview-r18.PROPOSED.json` Git blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`, all chapter v18.0 proposals, 90 B key display map / 19 aliases / 177 citation ledger.
4. Compare control r24 `diagnostic-r24/main.pdf` and p08/p09/p11/p18 (caption orphan, clipped Decider, sparse last page), r22 `diagnostic-r22/main.pdf` plus p03/04 p05/06 p08/09 p15/16 and p18 (four sentence bisections, sparse tail), r23 SA/SB and r22 B as needed.

## 2. Required tests (no worker self-certification)

**A. Every wide table** T1..T7: make an actual physical ledger of PDF page, enclosing chapter, full-width caption coordinates and exact row list/number, note exact text immediately BEFORE/AFTER table by correct left-to-right/page reading order. Verify table after legitimate introduction and STRICTLY before next chapter heading. Caption and all rows must be on SAME page, no row/cite missing/duplicate, no cropped cell or footer collision. Specifically: Table3 p09 six rows, Table4 p12 Decider row + all five peers, Table5 p14, Table6 p16, Table7 p17; source-contiguous exact fragments `立直し`, `分母の開示`, `エンドポイント`, `染料と水による検証`, and ASPIRE `80課題で99%` must not be interrupted by any table.

**B. Physical reader flow and geometry:** inspect ALL 21 pages, both columns, not just PDF text extraction. Identify all significant voids: p03, p05, p11, p13 and p18, and any new ones; assess if avoidable or a legitimate price for indivisible full-width comparisons. Count cover/body/reference actual pages from PDF, identify table-only leaves, orphan headings, caption-only and partially printed tables, low-fill/blank columns, vertical collisions. Effective occupied area should be `UNMEASURED` unless truly measured; never confuse 17 body physical pages with Human's 17.0 planned body allocation. Check that segmentation has not reordered text or damaged citations within paragraphs or notes.

**C. Source-to-print invariance:** independently compare the 150 non-table Reader blocks, all 7 captions/rows/cites/notes/headings and 28 selections against exact r18 source with the new r25 TeX and, as feasible, PDF extraction plus images. Do not treat unchanged source Git blob or 0 TeX warnings as proof of zero printed omission. Verify table numbering 1–7, href destinations where available, 90 B items = 71 full + 19 aliases, 177 ledger rows, seven new secondary-label display fixes, B28/B57/B74/B90 URL and B90 end, internal-ID/editor-note leakage zero; cover three diagnostic warnings. Confirm source regressions: Argon random generated Minecraft world and single run; Maia 24 trays/96 accelerators/750GB/s; Earth model-dependent negative; NVIDIA native MTP mean acceptance LENGTH not rate; wet-lab 131/311 versus independent eight clones; LFM license legal entity; ASPIRE model-dependent real-robot publisher results and caveats.

**D. Toolchain and build:** check manifest true SHA256/PDF page count/bytes and LaTeX logs; distinguish reported hashes from independently recomputed hashes. Explicitly flag any compiler warnings, overfull, underfull, missing glyphs, malformed hyperlink, or glyph clipping. If binary cannot be retrieved, report UNVERIFIED rather than pretending to recompute.

**E. Governance:** Core v2 immutability, Architecture r1 approved, publication pending, canonical Reader/State unchanged; NONCANONICAL diagnostic PDF cannot be approved as Publication Preview. Human Option B is an editorial preference, not Gate. Sol tentative 21/max23 does not override formal approved Architecture 26.5/28/30.

## 3. Report exact outcome and evidence

Return a structured independent report in the chat with:
- audited immutable HEAD/Tree + methods and limitations;
- table-by-table findings (T1..T7), any line/word/table clipping or disordered elements;
- per-page print review across 21 pages; residual whitespace and objective reason acceptable/unacceptable;
- Reader/citation/reference equivalence results;
- differences from prior r22–r24 faults and any NEW regressions;
- exact blocker severity and page anchors if found;
- terminal `INDEPENDENT_W42_R25_PRINT_AUDIT_PASS`, `PASS_WITH_LIMITATIONS`, or `REQUEST_CHANGES` (do not invent approval of any Gate).

No write to repository. If any high-severity print fault, source-text omission, caption orphan or sentence bisection is observed, `REQUEST_CHANGES`. If layout is readable but optional aesthetic whitespace remains, `PASS_WITH_LIMITATIONS` may be defensible. If complete evidence is inaccessible, explicitly `INCOMPLETE / UNVERIFIED`, not fabricated PASS. The user will deliver your report back to editorial Sol for adjudication.
