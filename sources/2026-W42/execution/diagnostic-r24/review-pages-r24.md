# W42 r24 visual QA — STRIP full 21pp (ALL pages opened @150dpi; QUALITY-BLOCKED)

Build: LuaHBTeX 1.24.0, epoch 1792311600 (runs 2–4 identical `8dea62f2…`, 509,?B — see manifest for exact bytes, 21pp). TeX `7ba80abf…`; preview.sty identical to r22; cuted v2.10 + capt-of in main.tex only. Log 0 errors; warnings: 2× twocolumn-too-tall + 2× contains-only-floats + 4 overfull (37pt p03, 93pt p11). Per-page chars: 480/2495/2548/2425/2408/2527/2712/1991/2075/2325/2606/2320/2148/2444/2429/2188/2557/508/2850/3108/2698. Tables in-flow: T1 p03 / T2 p05 / T3 p08 / T4 p11 / T5 p13 / T6 p15 / T7 p16 (none at page tops by float drift).

- p01 cover PASS (3 lines intact).
- p02–p10: P1/P2/P3 text + T1 p03 / T2 p05 / T3 p08 in-flow between complete paras; previously split words (`立直し`, `分母の開示だ`, `エンドポイント`) intact on their pages (verified trailing/leading glyphs in audit). No table-top bisections. PASS continuity.
- p11 Table4 in-flow BUT Decider row clipped (overfull 93pt; image cut at page bottom; PDF text missing row) — HARD FAIL completeness. Chapter P4 before P5 heading p12 — PASS position.
- p12–p17: P5/P6/P7 text + T5 p13 / T6 p15 / T7 p16 in-flow; VERID `による` intact, ASPIRE intact. PASS continuity.
- p18 tail 508 chars left-only (worse than C2 702) — large near-empty FAIL.
- p19–p21 bib PASS (90/19, secondary labels, B28/B57/B74/B90, no stamp).
- No table-only pages; no chapter crossings; no machine IDs; cover intact. BUT missing Table4 cells + sparse tail + output warnings → NOT eligible. BLOCKED (quality).

V2 (Table7 P7-end, 21pp `a4f09f01…`, p18 405) worse fill — hash only, rejected.
Phase A sample (3pp, 2 strips) viable for small tables — proof in `phaseA-sample/`.

(End — 21/21 opened, BLOCKED.)
