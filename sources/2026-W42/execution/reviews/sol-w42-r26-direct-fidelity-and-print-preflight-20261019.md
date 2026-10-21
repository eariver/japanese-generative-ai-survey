# J-GAS W42 r26 — Sol direct Reader-fidelity and print preflight

Date: 2026-10-19 JST
Status: `SOL_W42_R26_DIRECT_PREFLIGHT_PASS_TO_FOCUSED_INDEPENDENT_REAUDIT / NONCANONICAL / PROCESS_EXCEPTION_FLAGGED`
Repository: `eariver/japanese-generative-ai-survey`
FIXED audited r26 HEAD: `2981b30b783e858737fc69cf439afbbfe19d5105`
FIXED audited r26 root Tree: `617a52200d82575b91a3cd345037daad2e8fbbbd`
r25 baseline HEAD: `b992685a66ccfd9eef3073a448771d2f224bea9c`
r18 Reader master Git blob: `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`
r26 print TeX Git blob: `ffdd45742c16fc2f19fd21805479ca9d8373f30b`

## 1. Commit identity / unmodified authority

Read-only GitHub remote W42 HEAD/Tree verified; one normal fast-forward commit from Sol r26 dispatch `49f1fec10fa421dcb6f8116efc8bd6bc3c65a74e` with 36 touched paths, only `sources/2026-W42/execution/` (new r26 diagnostics/evidence/session and truthful index append). Reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` and Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` unchanged. `production-state.json` Git blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb` remains `DRAFT_COMPLETE`, Architecture r1 Human `approved`, Publication Preview `pending`. No official Publication/Architecture/Gate/Reader/Freeze/Release authorized.

## 2. Sol FRESH independent-of-Worker source-fidelity analysis

Sol read authoritative r18 `reader-preview-r18.PROPOSED.json` and r26 actual `diagnostic-r26/main.tex` directly from fixed r26 commit, rather than reusing Worker-reported counts or a previously shortened diagnostic TeX. Implemented a separate temporary JS comparison: parse seven Reader TABLE text fields as newline-separated rows, U+FF5C-delimited cells; extract seven TeX `tabularx` bodies, remove `\\midrule` lines and `\\cite{...}` suffixes only, split `\\\\` rows/`&` columns, trim surrounding whitespace and compare **each cell string for byte equality**, no unit/denominator/provenance normalization.

Results:
- Exactly 7 Reader TABLE blocks, 7 TeX tables; 27 data rows / 110 cells independently parsed, ALL 110 cells MATCH (per table T1 11, T2 8, T3 23, T4 26, T5 15, T6 15, T7 12).
- All 7 `【比較表：...】` Reader captions match 7 TeX `\\captionof{table}{...}` after removing only the Reader's visual bracket wrapper; table numbering 1..7 observed.
- All 150 non-TABLE Reader blocks (7 HEADING / 136 PARAGRAPH / 7 NOTE) are contained **exactly as raw strings** in TeX, 150/150. This tests TeX source fidelity, not full PDF glyph coverage.
- In the correct cells T2 LFM2.5 includes `商用上限1000万米ドル（法主体の年商）`; T3 Nemotron includes `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`; bad variants `商用上限1000万ドル` and `Super VL未開封` absent from TeX.
- Independently reconstructed r25 TeX from r26 by reversing ONLY (a) a header revision marker, (b) one new provenance comment, (c) exact T2 cell restoration, (d) exact T3 cell restoration; equality to fixed r25 TeX is byte-for-byte TRUE. This is a verified limited change, not a claim of r25=>r18 transitive fidelity.
- Independently counted 729 total expanded `\\cite` key uses, 90 unique, 0 undefined relative to 90 `\\bibitem` keys. Seven table captions preserved, no cell omission.
- Independently inspected r26 `main.log` text: `Output written on main.pdf (21 pages, 508624 bytes)`; no Overfull/Underfull/Missing character/LaTeX or Package warning lines. Same `preview.sty` Git blob as r25.

## 3. Sol full 21-page direct PNG visual preflight

Sol directly fetched/opened EVERY fixed-commit r26 page `diagnostic-r26/pages/p-01.png` through `p-21.png` at visual resolution. Critical source-to-physical checkpoints:
- p06 Table2: LFM2.5 complete restored license cell `1000万米ドル（法主体の年商）` visibly appears with `B11/B69/B12`, caption and both Maia/LFM rows same page. No clipped qualifier despite extra wrapping.
- p09 Table3: Nemotron `Super VLファイル未確認、OSI主張不可、EXO不採用` visibly appears with `B21/B72/B22/B20`; caption + all six rows same p09, no r24 caption orphan.
- T1 p04 Wonder/Argon, T4 p12 6 rows including Decider full final row and citations (no footer collision), T5 p14 4 rows, T6 p16 4 rows, T7 p17 3 rows complete. Each table is inside its hosting chapter and before the next chapter.
- All old r22 word/sentence interpositions (`立直し`, `分母の開示`, `エンドポイント`, `染料と水による検証`), r24 Table3 orphan / Table4 cut, r21/22 Table7 ASPIRE bisection are NOT observed.
- p03/p05/p11/p13 intentionally sparse below columns preceding atomic full-width tables; visually same category as r25, no newly lost prose. p18 is genuinely two-column and no old 508/702-character left-only huge empty tail. Effective occupied area remains `UNMEASURED`, not claimed perfect.
- p01 noncanonical diagnostic 3-line stamp present; p19–p21 bibliography 90 entries B01..B90 and visually intact B28, B57, B74, B90 terminal URL; no obviously truncated captions, machine IDs, paragraph endings, note boxes or clipped URLs in images. Actual hyperlink click destination/HTTP liveness not retested.

r26 manifest PDF SHA256 `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0` / 508624 bytes / 21 pages and TeX SHA256 `5bbdca1b5f2d9671e123aed2a4bc25f876fdef28027158e8cbb9fc960d158b73` are WORKER/MANIFEST values; Sol did not independently download PDF binary to recompute its SHA256 in this session. This limitation is reserved for the independent re-auditor.

## 4. Procedure nonconformity recorded, no silent waiver

Muse r26 session reports using **local `reset --hard origin/weekly/2026-W42-v2-work` to align a stale local workspace** after initial guard. This action violates the literal r26 execution prohibition of reset, even though Muse labels it "position-only". Remote GitHub history is verified fast-forward only and protected source untouched; therefore NO remote rewrite is observed. Sol cannot establish whether this local reset discarded uncommitted local work. Record as `PROCESS_EXCEPTION_LOCAL_RESET` with unresolved local-workspace impact; do NOT silently call the entire execution contract perfectly complied. Focused independent reviewer should assess this separately from PDF correctness. A future Worker contract must direct safe fetch/checkout or stop rather than forbidden reset.

## 5. Sol disposition

`SOL_W42_R26_DIRECT_PREFLIGHT_PASS_TO_FOCUSED_INDEPENDENT_REAUDIT / NONCANONICAL`.

This is a constrained source+print preflight PASS; it does **not** resolve the procedural exception, does not approve formal Publication Preview/Human Gate, and does not adjudicate Architecture page-plan. The separate independent reviewer must independently verify the two restored cells, all 7 tables/content, PDF hash/build, all-page integrity and the procedural exception. Independent terminal may be PASS, PASS_WITH_LIMITATIONS, REQUEST_CHANGES or INCOMPLETE, with clearly separated CONTENT/PRINT/PROCESS results.

Formal Architecture r1 remains body26.5 target28 max30; proposed Option B 17.0 body and 21/23 Sol recommendation are NON-GATE. No canonical file, state or Gate may change until independent verification and separate Human Architecture decision.

Next one-shot read-only instruction: `sources/2026-W42/execution/instructions/2026-10-19_w42-r26-independent-focused-reaudit-read-only.md`.
