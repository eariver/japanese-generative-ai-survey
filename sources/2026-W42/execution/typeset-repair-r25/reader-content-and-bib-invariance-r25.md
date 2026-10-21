# W42 r25 reader-content-bib invariance (NONCANONICAL)

r18 blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` re-verified; 7ch/28/157/136P/25015ch/7T/7N; 90/19/177; proposals + maps unchanged.

## Wrapper-only (source bytes preserved)

- MULTICOL-V2 vs C2: `\twocolumn`→9× `multicols{2}` segments; `placeins`→`multicol`+`capt-of` (+`\columnsep 7mm` enforced same gutter); barriers/needspace removed (float-specific); 7× `table*[htbp]`+`\caption`→ inter-segment `{\centering\footnotesize \captionof{table}` + `tabularx` (visible words identical all 7); 7× `\end{table*}`→ segment resume; 7 measured atomicity needspaces (18/18/30/30/22/22/20 + safety; geometry proof in Phase A doc + V1→V2 orphan fix); bib wrapped in `multicols{2}` (was twocolumn bib; same two-column widths/gutter). No cell/row/cite/order/chapter/heading/note/prose changes. TeX `837f5535…` (vs C2 `7e95ae84…`).
- Numbering: `\captionof{table}` in source order → printed `表 1..7` in order (verified p04/p06/p09/p12/p14/p16/p17); no `\label` in source tables; citation hyperlinks work inter-segment (blue Bxx links verified sample + full).
- Typography: same fonts/margins/baseline/pagesize/column widths/gutter (multicol widths = textwidth-sep derived, visually match twocolumn; full-issue QA confirms); two-column body retained (8 segments, not one-column fallback); `multicols*` not needed (balancing acceptable; no blank leaves).

## Checks (V2 vs C2 same-method)

- 150 non-TABLE blocks inherited (zero-prose diff) + PDF-text spot: `立直しの手順`, `分母の開示だ…AutomationBench`, `エンドポイント` (both), `染料と水による検証`, `80課題で99%…卓上片づけ`, `WGO 42.70…HSS 46.36` all present intact in V2 print (split-free).
- 7 bodies source-identical AND print-complete (all rows visible incl Decider `2セント…[B37…]` 2 occurrences; caption+rows same pages; no orphan/clip/collision — contrast r24 strip missing row).
- Captions visible words 7/7 identical; table cites 169 `\cite{B` both; numbering order preserved.
- Bib 90 (71+19), 19 `同一資料`, 17 `[二次・参考]`/0 `[SECONDARY]`, B28/B57/B74/B90, cover 3 lines, zero machine IDs — all preserved (viewed p19–p21 = C2 bib reflowed to multicol two-column; entries complete).
- Regressions (Argon random, Maia 24/96/750GB/s, Earth negatives, MTP length, wet-lab 131/311 vs 8 clones, LFM entity, ASPIRE robot) preserved bytes + print.

## Hashes

- V2 TeX `837f5535…`; PDF 21pp `ce1d50cd…`; V1 multicol (no needspace) hash in session (T3/T4 orphans); strip V2-Table7-end `a4f09f01…` (tail 405, hash only). No Core/main/canonical/State/Gate/r11–r24 bytes touched.

(End.)
