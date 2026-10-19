# W42 r29 physical print page and table ledger (all pages inspected via PNG + PDF text)

Status: deterministic print evidence (not a semantic/visual PASS)
Date: 2026-10-20 JST
PDF: `surveys/weekly/2026-W42/main.pdf` (SHA256 `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9`, 21 pages, 505102 bytes)
Log: 0 errors, 0 Overfull/Underfull, 0 missing glyphs, 0 LaTeX warnings

## 1. Page map (pymupdf chars; r26 baseline in parentheses)

- p01 cover: 380 (r26 467, -87 diagnostic stamp removed), neutral `週刊Technical Survey`, headline/deck preserved, no anchors
- p02 P1 start: 2283 (same)
- p03 P1 cont: 1888 (same, residual whitespace, UNMEASURED)
- p04 T1 atomic: 2137 (same)
- p05 P2: 2155 (same)
- p06 T2 atomic (restored cell intact): 2345 (same)
- p07 P3 start: 2400 (same)
- p08 P3 cont: 2529 (same)
- p09 T3 atomic caption+6 rows: 1939 (same, restored cell visually intact)
- p10 P4 start: 2204 (same)
- p11 P4 body: 2145 (same, residual whitespace, UNMEASURED)
- p12 T4 atomic incl Decider: 1981 (same, no footer collision)
- p13 P5 body: 1765 (same, residual whitespace, UNMEASURED)
- p14 T5 atomic: 1936 (same)
- p15 P6 body: 2546 (same)
- p16 T6 atomic: 2106 (same)
- p17 T7 atomic incl ASPIRE: 2002 (same)
- p18 P7 tail both columns: 1618 (same, not near-empty)
- p19 bib B01–B27: 2751 (same)
- p20 bib B28–B54: 3018 (same, B28 visible)
- p21 bib B55–B90: 2573 (same, B57/B74/B90 to end, no truncation)

All body/bib pages char-identical to r26; only cover changed. No reflow.

## 2. Tables (7/7 atomic, caption + all rows same physical page)

- T1 p04: caption + 2 rows (Wonder/Argon) + note box same page; no sentence bisection
- T2 p06: caption + 2 rows + restored `法主体の年商` + cites B11/B69/B12; no orphan
- T3 p09: caption + 6 rows incl Nemotron restored `Super VL / ファイル未確認` + 4 cites; caption/row cohesion PASS
- T4 p12: caption + 6 rows incl Decider v1.2; footer collision none (fixed vs r24)
- T5 p14: caption + 4 rows; right column P6 intro follows normally
- T6 p16: caption + 4 rows; no cut
- T7 p17: caption + 3 rows incl ASPIRE; real-robot limits in body continuation

No table-only isolated page, no caption-only page, no footer/page-number collision observed in PNGs, no visible missing glyphs or footnote/URL clipping.

## 3. Visual QA (PNGs, not a formal visual PASS)

- All 21 `pages/p-01.png`..`p-21.png` (150 DPI, 1241×1754) inspected; contact sheets ×3
- Cover p01: neutral descriptor, no diagnostic stamp, no fake APPROVED/RELEASED claim
- Chapter order P1→P7 correct; no story interrupted by full-width table (tables inter-segment within own chapter)
- Bibliography B90 readable to end; URLs intact
- Residual whitespace p03/p11/p13 + lighter p05/p18 accepted per Route A; area UNMEASURED (no density % invented)
- r22 top-float bisection, r24 caption orphan/Decider clip, r25 ASPIRE issue: not recurring in corresponding PNGs

Independent semantic/visual audit still required; this ledger is build evidence only.
