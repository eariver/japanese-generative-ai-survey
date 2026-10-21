# W42 r24 nonfloating table boundary audit (ALL pages opened; BLOCKED)

Build: STRIP full 21pp `8dea62f2…` (TeX `7ba80abf…`; cuted v2.10 + capt-of; no placeins/barriers/ASPIRE-needspace; 7 strips in-flow at source para boundaries). Log 0 errors; 2× `twocolumn too tall` + 2× `contains only floats` + 4 overfull (37pt p03, 93pt p11). Per-page chars: 480/2495/2548/2425/2408/2527/2712/1991/2075/2325/2606/2320/2148/2444/2429/2188/2557/508/2850/3108/2698. Tables (in-flow, NOT page-top floats): T1 p03 / T2 p05 / T3 p08 / T4 p11 / T5 p13 / T6 p15 / T7 p16. V2 (Table7 P7-end): 21pp `a4f09f01…`, T7 p18, p18 405 chars (worse; hash only).

Ledger (verbatim trailing/leading; source→print mapping; left+right columns):

- T1 (P1, `WonderとArgon`, p03 bottom in-flow): above ends complete `…の証拠ではない。[B05…]`; below (p04 top) fresh note box + `Wonderの例示タスク…`. Split para `失敗の記録と立直しの手順…` complete on p04 (both halves together). NO `立直/し` split. Chapter: P1 (p03) before P2 heading p04 — PASS position + PASS continuity. Before/after: C2 p03 `立直`→p04 `しの手順…` (FAIL) vs STRIP p03 Table1 in-flow + p04 fresh (PASS).
- T2 (P2, `効率主張`, p05 bottom in-flow): above complete; below (p06) fresh. Source phrase `分母の開示だ…温度・ベンチ名…` intact (no `開/示だ` split). PASS continuity. Chapter P2 before P3 — PASS.
- T3 (P3, `重み・実装・ライセンス`, p08 in-flow): above/below complete paras; no `エンドポ/イント` split (both `エンドポイント` occurrences intact on their pages). PASS continuity. Chapter P3 before P4 — PASS.
- T4 (P4, `生産性とゲート`, p11 bottom in-flow): above ends complete `…手本たるゆえんだ。[B37…]`; table rows Codex/Scion/HydraFusion/AutoFix visible BUT Decider row (`Decider v1.2…版継承…`) MISSING in PDF text (1 vs C2 2 occurrences) — clipped by overfull 93pt. Missing table cells HARD FAIL (continuity PASS, completeness FAIL). Chapter P4 before P5 heading p12 — PASS position.
- T5 (P5, `安全の四つの局面`, p13 in-flow): rows intact (counts match C2); above/below complete; no split. PASS.
- T6 (P6, `科学エージェントの証拠`, p15 bottom in-flow): rows intact; VERID para `染料と水による検証…` complete (no `によ/る` split; C2 split fixed). PASS continuity. Chapter P6 before P7 heading — PASS.
- T7 (P7, `専門・身体の三件`, p16 in-flow): above/below complete; ASPIRE `80課題で99%…卓上片づけ…` intact (no Table7 bisection; C2-needspace fix preserved by construction). PASS. V2 moves T7 to p18 (P7-end): p18 405 chars (Table7 + minimal tail) — worse fill, same continuity PASS; documented as second anchor, rejected for fill.

Headings P1–P7 + bib heading present in order (P5 p12, P7 p16 in STRIP; no heading orphaned by tables). Notes/citations/URLs checked all 21 pages; B28 complete, B57 kept-together, B74 clean, B90 terminal, 71+19/90, 7× secondary, 177-ledger, zero machine IDs preserved same-method (see invariance; Decider-row exception is print-clipping, not source deletion — source bytes intact). Cover 3 lines intact. No table-only pages (tables share pages with text above/below by strip construction). No table beyond hosting chapter (all strips at source chapter positions; P-headings after tables verified).

Tail: STRIP p18 508 chars left-only (P7 closing `Vals…凍結…Glimpse…三件の共通点…` partial? Actually p18 508 vs C2 702 — even sparser). Large near-empty FAIL (worse than r22 702 gate example). V2 p18 405 worse. Honest closing content, no filler, but visibly poor fill; not claimed unavoidable (B 20pp has no tail, but splits) — within print-only, tail vs splits tradeoff persists (proven r22–r24 across 7 renders).

No page judged on log/char-totals; every PNG opened; both columns quoted (see review index + contact sheets). Compared vs C2 (21pp/4 splits/702 tail) and SA/SB (22pp/splits+voids): strip fixes all 4 splits by construction BUT introduces missing-row + worse tail + output warnings. Hence BLOCKED (quality), not READY.

(End — 21/21 STRIP pages opened.)
