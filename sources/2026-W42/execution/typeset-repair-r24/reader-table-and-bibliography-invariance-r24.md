# W42 r24 reader-table-bibliography invariance (NONCANONICAL)

r18 blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` re-verified; 7ch/28/157/136P/25015ch/7T/7N; 90 keys/19 aliases/177 rows; 7 v18.0 proposals + maps unchanged.

## Wrapper-only diffs (prose/cells preserved in source)

- STRIP vs C2: `placeins`→`cuted`+`capt-of` (main.tex only; preview.sty identical); 3 FloatBarriers + ASPIRE-needspace removed (float-specific, no floats remain); 7× `\begin{table*}[htbp]\centering\footnotesize` + `\caption{…}` → `\begin{strip}%…` + `\centering\footnotesize` + `\captionof{table}{…}` (visible caption words identical: `比較表：WonderとArgonの読み分け` / `効率主張の読み分け` / `重み・実装・ライセンス` / `生産性とゲートの条件` / `安全の四つの局面` / `科学エージェントの証拠` / `専門・身体の三件`); 7× `\end{table*}`→`\end{strip}`. No cell/row/cite/order/chapter changes. TeX `7ba80abf…` (vs C2 `7e95ae84…`).
- Table numbering: `\captionof{table}` increments table counter in source order → printed `表 1..7` in order (verified p03/p05/p08/p11/p13/p15/p16). No `\label` in source tables → no anchor semantics to preserve; hyperref citation links (`\cite{Bxx}` blue links) work inside strip (verified B01/B05/B09/etc. links on strip pages; sample `[?]` were sample-only missing-bib artifact, full resolves).
- Typography: no font/margin/baseline/pagesize/column-gap/ratio/prose changes; `stripsep 15pt` default (cuted) is package geometry, not content styling;两-column body retained (not one-column fallback).

## Preservation checks (same-method STRIP vs C2)

- 150 non-TABLE blocks: source diff zero-prose → inherited; PDF-text spot checks (normalized): `立直しの手順`, `分母の開示だ…AutomationBench`, `エンドポイント`, `染料と水による検証`, `80課題で99%…卓上片づけ`, `WGO 42.70…HSS 46.36` all present in STRIP PDF (split-free, same pages as paras).
- 7 table bodies: source bytes identical; PRINT exception: Table4 Decider row (`Decider v1.2…2セント…精度は発行者`) missing in STRIP PDF text/print (1 vs 2 occurrences; p11 image cut at page bottom; overfull 93pt) — source intact, print clipped = quality FAIL (recorded here as invariance exception, not source violation).
- Captions/labels/cites: 7/7 visible captions identical words; table `\cite{Bxx}` keys unchanged (169 `\cite{B` in both); numbering `表1..7` order preserved; PDF-text `[B` counts same-method (B-count identical except Decider-row delta).
- Bibliography 90 (71+19), 177 rows, 7× `[二次・参考]`, 0 `[SECONDARY]`, B28/B57/B74/B90, cover 3 lines, zero machine IDs (`alias-of`/`normalization`/`CLAIM_BOUNDARY` 0; `t7-02` comment only) — all preserved in STRIP (viewed p19–p21 identical to C2 bib).
- Prior regressions (Argon random world, Maia 24/96/750GB/s, Earth negatives, MTP length, wet-lab 131/311 vs 8 clones, LFM legal entity, ASPIRE robot caveats) preserved in source bytes and print (except Table4-row clipping noted).

## Hashes

- STRIP TeX `7ba80abf091c6ba7…`; PDF 21pp `8dea62f2b1d33168…`; sample TeX/PDF in phaseA manifest. V2 TeX `a4f09f01…`-family (hash in session; PDF 21pp p18 405).
- No Core/main/canonical/State/Gate/r11–r23 bytes touched.

(End.)
