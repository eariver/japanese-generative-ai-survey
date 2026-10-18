# W42 r25 global seven-table source-to-physical ledger (MULTICOL-V2 selected; BLOCKED nowhere — READY)

Build: MULTICOL-V2 21pp `ce1d50cd…` (TeX `837f5535…`; multicol v2.0b segments + 7 inter-segment tables + 7 measured atomicity needspaces T1 18/T2 18/T3 30/T4 30/T5 22/T6 22/T7 20; no twocolumn/floats/barriers; bib in multicols). Log 0 errors/warnings. Per-page: 480/2495/2087/2338/2319/2501/2636/2696/2020/2338/2303/2163/1868/2039/2726/2335/2121/1772/2879/3124/2708. Tables: T1 p04 / T2 p06 / T3 p09 / T4 p12 / T5 p14 / T6 p16 / T7 p17 (all caption+rows same page, atomic via needspace; no orphan/clip/collision).

| N | Chapter | Physical | Before (trailing glyphs, complete) | After (leading, fresh) | Atomic | Chapter order |
|---|---|---|---|---|---|---|
| T1 `WonderとArgon` | P1 | p04 inter-segment | p03 ends `…の証拠ではない。[B05…]` (complete cite) | p04 note + `Wonderの例示タスク…` fresh; `失敗の内訳…立直しの手順…[B05…]` complete p04 (NO `立直/し` split) | caption+2 rows p04 | P1 (p04) before P2 heading p04 — PASS |
| T2 `効率主張` | P2 | p06 inter-segment | p05 ends complete | p06 fresh; phrase `分母の開示だ…温度・ベンチ名…` intact (NO `開/示だ` split) | caption+2 rows p06 | P2 before P3 — PASS |
| T3 `重み・実装・ライセンス` | P3 | p09 inter-segment | p08 ends complete `[B14…B71]/[B29…]` | p09 fresh; `エンドポイント` intact both occurrences (NO `エンドポ/イント` split, NO caption orphan — contrast r24 F24-02, Track A a-2 orphan) | caption+6 rows p09 | P3 before P4 heading — PASS |
| T4 `生産性とゲート` | P4 | p12 inter-segment | p11 ends `…手本たるゆえんだ。[B37…]` complete | p12 note + closing + P5 heading `5 安全性…` below table (Table4 BEFORE P5) | caption+6 rows p12 incl Decider `2セント…精度は発行者[B37…]` present (NO footer collision — contrast r24 F24-01, 93pt clip; Decider 2 occurrences) | P4 before P5 — PASS (F-08 preserved) |
| T5 `安全の四つの局面` | P5 | p14 inter-segment | p13 ends complete | p14 fresh; before P6 heading — PASS |
| T6 `科学エージェントの証拠` | P6 | p16 inter-segment | p15 ends complete | p16 fresh; VERID `染料と水による検証…` intact (NO `によ/る` split) | caption+4 rows p16 | P6 before P7 heading — PASS |
| T7 `専門・身体の三件` | P7 | p17 inter-segment | p16 ends complete | p17 fresh `独立評価…`; ASPIRE `80課題で99%…卓上片づけ…[B57…]` complete (NO Table7 bisection) | caption+3 rows p17 | P7 (p17) before bib p19 — PASS |

Headings P1–P7 + bib heading in order (P2 p04, P5 p12, P6 p14?, P7 p16 verified images; no heading orphaned). Notes (7 tcolorbox incl P4 note p12) render inside segments. URLs/B28 (complete) /B57 (kept-together) /B74 (clean) /B90 terminus verified p19–p21. 90 = 71+19, 7× secondary, 177-ledger, zero machine IDs preserved (see invariance). Cover 3 lines intact. No table-only pages (each table shares page with text above/below via segments). No chapter crossings. Tail p18 1772 chars both columns (Glimpse + note + PLawBench/Harvey/frozen/future/common-points; left+right filled) — NO large near-empty (contrast C2 702, strip 508, V2-early 405). All 21 PNGs opened; both columns quoted (review index + sheets).

Compared: C2 21pp/4 splits/702 tail; SA 22pp/splits+713 void; SB 22pp/splits+856 void; SC 23pp/voids; r24 STRIP 21pp/Decider missing/508 tail+warnings; Track A sample FAIL orphan+clip; Track B sample PASS small; V1 multicol (no needspace) T3/T4 caption orphans (p08/p11 bottoms) → V2 needspace fixes atomicity with 0 warnings. V2 (Table7 early-intro source position) selected; second anchor V2-Table7-end tested in strip (worse tail 405) but multicol Table7-early already fills tail via segment balancing (p18 1772) — no second multicol anchor needed (strip V2 hash recorded for comparison only).

Geometry model enforced: each Table caption + entire row grid same page between safe bounds, no footer collision, no orphan, no bisection, manageable occupancy — proven on images + bounding (not pdftotext alone). Effective area `UNMEASURED` (no invented decimals).

(End — 7/7 PASS, READY.)
