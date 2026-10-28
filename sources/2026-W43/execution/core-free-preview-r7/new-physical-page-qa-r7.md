# W43 r7 physical page + table QA (bounded worker scope)

Build: lualatex ×2 exit 0/0, 0 errors, 0 overfull/underfull. PDF 487514 B,
22 A4 pages, Subject/Keywords `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`.
150dpi PNGs `pages/p-01..p-22.png` + 3 contact sheets. Per-page SHA256 (full)
in `pdf-links-fonts-raw-r7.json` notes? No — recorded here (truncated 16):

p-01 0e3e3cb0… cover single-col, neutral descriptor, proof mark separate. FULL-RES PASS.
p-02 93a470dd… TOC single-col, 8 entries sans P-prefix, pp.3–17. FULL-RES PASS.
p-03 1a9a0ff9… interior heading sans print tag; §1 two-col; full-width 表1. FULL-RES PASS.
p-04 7ef97ff8… §1 two-col + tables (sheet-scale + text layer). SHEET PASS.
p-05 3ac4b826… §1 fig box full-width + note in-col (sheet-scale + text). SHEET PASS.
p-06 435c0200… §2 two-col, full-width 表5. FULL-RES PASS.
p-07 c8abb11d… §2 code blocks full-width (sheet-scale + text). SHEET PASS.
p-08 6afd1d2b… §2 tables + hrule (sheet-scale + text). SHEET PASS.
p-09 b0f33faf… §3 two-col, full-width 表8. FULL-RES PASS.
p-10 686e001a… §3 fig box + tables (sheet-scale + text). SHEET PASS.
p-11 236a85d3… §4 two-col + tables (sheet-scale + text). SHEET PASS.
p-12 fd39c325… §4→§5, full-width 表10, hrule divider. FULL-RES PASS.
p-13 c7dcd362… §5 tables (sheet-scale + text). SHEET PASS.
p-14 4561572b… §5→§6 (sheet-scale + text). SHEET PASS.
p-15 8bbf6255… §6 fig box full-width (sheet-scale + text). SHEET PASS.
p-16 cadb10cb… §7 two-col, full-width 表14. FULL-RES PASS.
p-17 b2187f03… §7→§8 (sheet-scale + text). SHEET PASS.
p-18 546f9456… §8 full-width 表17 + full-width JSON code, neutral example header. FULL-RES PASS.
p-19 4060661a… §8 tables 18–20 full-width (sheet-scale + text). SHEET PASS.
p-20 c7a2a7af… §8 close + note + hrule + 今週の総括 head, two-col. FULL-RES PASS.
p-21 95d5a44d… recap end flows into 出典一覧 heading mid-page (no forced break), bib starts two-col. FULL-RES PASS.
p-22 4a4f239d… bib tail 36 keys two-col + centered proof footer, final-page tail blank below (normal). FULL-RES PASS.

Coverage honest: 22/22 sheet-scale + 11/22 full-res (p01,02,03,06,09,12,16,18,20,21,22)
+ full text-layer cross-check (meta scan §C, 36 keys, 5 recap paras, clocks,
POST route). No blank BODY pages (only TOC short page + final tail, both
normal). No tofu/overlap/clipping observed at inspected scales; 0 TeX
overfull/underfull corroborates but does not replace looking (all scales above).
Old p20 production note ABSENT (deleted in r6, still absent; text-layer grep 0).
Recap exactly 5 paragraphs (validator S-recap 5/5). 36 bib items legible p21–22.
Headers/footers correct (Weekly title + 2026-W43 + page number) all pages.

Flow order: source→caption proximity kept (each full-width block immediately
follows its referring prose segment; sequential emission in transform script).
No floating migration (no `table`/`figure` floats remain).

Independent auditor must newly inspect EVERY r7 page at full res; this record
does not substitute for `INDEPENDENT_W43_R7_*` visual verdict.
