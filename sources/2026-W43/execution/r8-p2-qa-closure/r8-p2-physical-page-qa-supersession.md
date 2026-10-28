# r8 P2-03 — physical page QA supersession (additive, no original edit)

Date: 2026-10-27 JST. Sidecar-only. Original `pdf-page-qa-r8.md`, PNGs, and fixed PDF are NOT modified.

Method: immutable r8 PDF bytes (`abd5b99b…`, 487351B) parsed per page with PyMuPDF text/layout + committed PNGs `p-01..p-22.png` re-viewed (image SHA in anchors JSON). Machine text and images agree; where PDF text line-splits occur (e.g. `表 11` vs `表11`), caption position is corroborated visually.

## Corrected locations (old wording → corrected page + evidence)

1. OLD `pdf-page-qa-r8.md` p12 line: “Table 11 header” on p12.
   - CORRECTION: Table 11 caption starts **p13** (with Table 12). p12 has NO table caption — only §5 prose + a body-text mention of 表18/表22 (not a caption).
   - Evidence: PDF text caps — p12: no `表11/表12` caption (only body `表18 言語・Docs…`); p13: `表11`, `表12`; image `p-12.png 39046020…` (no table) vs `p-13.png 8fa0fc96…` (Table 11+12 visible). Confidence: high.

2. OLD p14 line: “Table 13/16 full-width” on p14.
   - CORRECTION: **Table 13 on p14 ✓; Table 16 on p17** (with Table 15), NOT p14.
   - Evidence: PDF text — p14: `表13` only; p17: `表15`, `表16`; image `p-14.png 8ea35d0b…` (Table 13 only) vs `p-17.png b2187f03…` (Tables 15+16). Confidence: high.

3. OLD p19 line: “`今週の総括` head at bottom” on p19; 5 recap paras “start here”.
   - CORRECTION: p19 = TanStack/DeepSeek prose + **Table 18**, NO recap heading. `今週の総括` first appears at **p20 bottom**; recap body continues p20→p21.
   - Evidence: PDF text `今週の総括` hits ONLY p20 (0 hits p19/p21); image `p-19.png 4060661a…` (Table 18 + §8 prose, no heading) vs `p-20.png c7a2a7af…` (`今週の総括` heading at bottom + Tables 19/20). Confidence: high.

4. OLD p20 line: “`出典一覧と確認水準` + `参考文献` heads at bottom” on p20; p21 “bibliography start”.
   - CORRECTION: both heads first appear **mid-page p21** (not p20 bottom); bib entries start p21 and continue p22 (incl. corrected `[recap]` C on p22).
   - Evidence: PDF text heads ONLY p21 (0 hits p20/p22); image `p-20.png` (ends with recap prose, no bib heads) vs `p-21.png 95d5a44d…` (recap cont → `出典一覧と確認水準` → `参考文献` → `[KIMI-X]…` bib start). p21 bib-start claim in old QA remains correct; only the p20-heads location is superseded. Confidence: high.

## Full matrix

See `r8-p2-physical-page-anchors.json` (p01–p22: image SHA, tables, recap/bib/section anchors, PDF SHA). Summary: cover p01, TOC p02, P1 p03–p05, P2 p06–p08, P3 p09–p10, P4 p11–p12, P5 p12–p13, P6 p14–p15, P7 p16–p17, P8 p17–p20, recap p20(bottom)–p21, bib p21–p22. A p04 / B p11 / C p22 unchanged.
