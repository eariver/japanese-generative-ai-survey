# W42 r25 visual QA — MULTICOL-V2 (ALL 21 pages opened @150dpi; READY)

Build: LuaHBTeX 1.24.0, epoch 1792311600 (runs 2–4 identical `ce1d50cd74860101…`). TeX `837f5535…`; preview.sty identical to r22; multicol v2.0b + capt-of in main.tex only; 7 measured atomicity needspaces (T1 18 / T2 18 / T3 30 / T4 30 / T5 22 / T6 22 / T7 20 baselines + safety). Log 0 errors, 0 overfull, 0 underfull, 0 missing glyphs, 0 warnings (excl pkg-info). Per-page chars: 480/2495/2087/2338/2319/2501/2636/2696/2020/2338/2303/2163/1868/2039/2726/2335/2121/1772/2879/3124/2708. Tables inter-segment (NOT floats): T1 p04 / T2 p06 / T3 p09 / T4 p12 / T5 p14 / T6 p16 / T7 p17 — each caption + ALL rows same page (atomic via measured needspace; no orphan, no clip, no footer collision).

- p03→p04 Table1: p03 ends complete; p04 Table1 (Wonder 2 rows + Argon 2 rows? Actually T1: Wonder + Argon rows) atomic; below-table note + `Wonderの例示タスク…` fresh; `失敗の記録と立直しの手順…` complete on p04. NO `立直/し` split. P1 before P2 heading p04 — PASS.
- p05→p06 Table2: p05 ends complete; p06 Table2 (Maia + LFM rows) atomic; below fresh. NO `開/示だ` split. P2 before P3 — PASS.
- p08→p09 Table3: p08 ends complete; p09 Table3 caption + ALL 6 rows (Spark/Beam/Nemotron/Granite/MiniCPM/FLUX) same p09; below fresh. NO `エンドポ/イント` split, NO caption orphan (contrast r24 F24-02, Track A a-2 orphan). PASS.
- p11→p12 Table4: p11 ends complete `…手本たるゆえんだ。[B37…]`; p12 Table4 caption + ALL 6 rows (Codex/Scion/HydraFusion/AutoFix/AI Scan/Decider v1.2 rows) same p12; Decider row present in print (2 occurrences, vs r24 strip 1 = clipped). NO footer collision (contrast r24 F24-01, 93pt overfull). Below-table note + P4 closing + P5 heading `5 安全性…` same p12 below table — Table4 BEFORE P5. PASS.
- p13→p14 Table5: atomic; before P6 heading — PASS.
- p15→p16 Table6: atomic; VERID `染料と水による検証…` complete (NO `によ/る` split); before P7 heading — PASS.
- p16→p17 Table7: atomic (GLM/ASPIRE/Glimpse rows same p17); above ends complete, below fresh `独立評価…`; ASPIRE `80課題で99%…卓上片づけ…` complete (NO Table7 bisection). In P7 before bib — PASS.
- p18 tail 1772 chars both columns (Glimpse + note + PLawBench/Harvey/frozen/future/common-points; left+right filled, no left-only orphan). NO large near-empty (contrast C2 702, strip 508, V2-early 405). PASS fill.
- p19–p21 bib PASS (90 = 71+19, 7× secondary, B28 complete, B57 kept-together, B74 clean, B90 `…/LFM2.5-24B-A2B` terminus, no stamp). Cover 3 lines intact. No table-only pages; no chapter crossings; no machine IDs; B-count same-method identical to C2 (except Decider-row delta fixed: V2 has row, strip missing). 7 notes intact; tcolorbox notes render inside multicols segments (proven in Track B sample + full).

Compared vs C2 (21pp/4 splits/702 tail), SA/SB (22pp/splits+voids), r24 STRIP (21pp/Decider missing/508 tail + warnings), Track A sample (FAIL orphan+clip), Track B sample (PASS small tables): V2 is first zero-splits + zero-missing + full-tail + zero-warnings full-issue build. Selected.

(End — 21/21 opened, READY.)
