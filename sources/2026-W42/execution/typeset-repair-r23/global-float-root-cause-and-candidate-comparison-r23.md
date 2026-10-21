# W42 r23 global float root-cause and candidate comparison (diagnostic-only; NONCANONICAL)

Date: 2026-10-18 JST. Authority: `SOL_EXECUTION_AUTHORITY / R22_DIRECT_VISUAL_REQUEST_CHANGES / R23_GLOBAL_LAYOUT_STRATEGY / NONCANONICAL_ONLY`. Branch existing ONLY `weekly/2026-W42-v2-work`.
Terminal: `R23_SYSTEMIC_LAYOUT_BLOCKED` (no candidate achieves zero bisections + zero chapter crossings + no table-only/large-void + old regressions simultaneously with supported print-only changes; proof archived, no fake PASS).

## 0. Git guard (read-only, before any write)

- Starting Remote HEAD `d430894b3675195b02886c459eeff58819a183ea` == ls-remote + FETCH_HEAD; Tree `625088584abdc00be10932796b8f2e8382018cb4` == FETCH_HEAD tree.
- Reviewed main `c8d0ecc1…`/`801de813…`; Frozen Core `774dd39a…`/`cd46a6f…`; r22 baseline `d0cf7cb82d744260f630a5f9043fecc80d4b139f`/`f21e36ec710dc1a717060804961a2ede25043a7f` (local HEAD before FF). All matched → FF-only `d0cf7cb82` → `d430894b3` (1 Sol dispatch: r23 instruction + r22 disposition). No new/force/reset/rebase. Lease rechecked before push.

## 1. Why r22 false-PASS happened (systemic, not single-spot)

r22 Worker verified only Tables 4/5/6/7 (prior failing subset) + assumed Tables 1/2/3 clean because p01–p10 PNG-identical across r20/r21/r22. In fact Tables 1/2/3/6 were bisected since r19 open (float drift predates barriers). Per-page char totals + 0-warning log were treated as layout proof; they are not. Needspace before one split (ASPIRE/Table7) does not fix system. Previous-page column vs next-page float was confused with TeX source order. Sol direct-visual (actual PNG glyphs, not source adjacency) correctly finds four word/sentence splits in C2 21pp:

| ID | Table | Physical (C2 fixed commit) | Source-contiguous sentence |
|---|---|---|---|
| F22-01 | T1 p04 top | p03 right end `失敗の記録と立直` → below-T1 `しの手順が残ることが…` | `…失敗の記録と立直しの手順が残ることが、実行主張の検証口になる。[B05…]` (Minecraft fail-record para, line 111; Table1 source line 91 precedes it, floats ahead to p04 top between halves) — word `立直し` split |
| F22-02 | T2 p06 top | p05 right tail `…分母の開` → below-T2 `も、温度・ベンチ名とセットで読む…` (left col) | `…分母の開示だ。AutomationBench 27.69対次点8.72という差も、温度・ベンチ名とセットで読む。[B11…]` (line 201; Table2 source line 173 precedes, floats to p06 top) — phrase split; printed continuation is mid-paragraph, not clean (reconstruct full phrase from main.tex + both-column order; abbreviated token pair insufficient) |
| F22-03 | T3 p09 top | p08 right tail `一つのエンドポ` → below-T3 `イントではほぼ基盤と同等のVRAM…` | Left p08 `IBM Granite Switch 4.1…一つのエンドポイントに…` (line 299) and p09 `Graniteの提供形態…一つのエンドポイントでほぼ基盤…` (line 343): Table3 source line 311 sits between them; p08 bottom ends mid-word in first, p09 below-table starts mid-word in second — word `エンドポイント` split across Table3 (both columns affected; right col MiniCPM `使う側の選…` similarly spans) |
| F22-04 | T6 p16 top | p15 right tail `VERID較正の意味を確認する。染料と水によ` → below-T6 `る検証、フィードバックで5倍超…` | `…染料と水による検証、フィードバックで5倍超の精度…` (line 666; Table6 source line 638 precedes, floats to p16 top) — word `による` split |
| F22-05 | tail | p18 702 chars left-only + p11/p16 blanks | Poor fill, not stamp-only; honest barrier/needspace cost but visibly poor (see §4) |

Tables 4 (p12), 5 (p14), 7 (p17) verified clean at C2 boundaries (previous-page complete → table → fresh heading/para) and preserved as positives; must be rechecked after any reflow (done for SA/SB/SC below — 4/5/7 remain clean in SA/SB; SC moves all tables).

Root cause invariant: in `\twocolumn` + `table*[htbp]`, every full-width float drifts asynchronously to next page top, landing between whatever narrative para spans that page turn. Source position (all four tables precede their split paras) vs physical position (tables interposed mid-para) diverge. Column order (pN left→right) vs page order (pN→pN+1) was conflated in Worker QA. Unfilled previous-page column + next-page float is NOT paragraph-boundary proof — only trailing/leading glyph quotation + source mapping is.

## 2. Controls reproduced

- C2 control: `diagnostic-r22/main.tex` SHA `7e95ae84…` (r22 selected, 21pp `38d3796f…`); verified 4 splits above on committed PNGs p03/p04, p05/p06, p08/p09, p15/p16.
- B control: `diagnostic-r22/candidates/B/main.tex` SHA `fb644c00…` (20pp `26fee7bc…`); early Table4/5/6 solve chapter boundaries but bisect three other paras (P4/ECDSA/baseline, incl mid-word) — distinct failure mode, not reused.

## 3. Two+ distinct global strategies rendered and compared (all print-only, Reader bytes fixed, no font/margin/column changes)

### SA — systematic paragraph-completion (needspace for all split paras, keep [htbp] + barriers)

Change vs C2: +5 `needspace{8\baselineskip}` before `失敗の内訳…`(T1) / `16種ベンチ…`(T2) / `IBM Granite Switch…`(T3-left) / `MiniCPM-V 4.7…`(T3-right) / `VERID較正…`(T6); retained ASPIRE needspace (6 total); 973 lines; TeX `0717a682…`; deterministic 22pp `c1f8b6a4…` 509,560B; full proof `diagnostic-r23/` (TeX/sty/PDF/log/manifest/22 PNGs/3 contact sheets/review). Tables: T1 p04 / T2 p06 / T3 p10 / T4 p13 / T5 p15 / T6 p17 / T7 p18.

- Table1 FIXED (p03 ends complete cite; p04 fresh `失敗の内訳…` complete) — the one r23 success.
- Table2 STILL FAILS (shifted): p06 below-table `母つき開示の手本になる…` (mid-word `分母つき` split `分/母つき`); needspace pushed `16種ベンチ…` para but Table2 now splits adjacent `比較不能…分母つき…` para. Word bisection persists.
- p12 713-char sparse text-only page (Decider closing + note, right empty) — large avoidable void from systematic blanks. p19 702 tail persists (shifted p18→p19). No table-only pages, but large voids.
- Tables 4/5/7 remain clean (shifted +1 page, still table+heading same-page); Table3/6 not claimed PASS (see ledger; conservative FAIL). Old regressions PASS. Verdict: FAIL (≥1 word split + large void). Proves needspace-system shifts splits rather than eliminating them.

### SB — global float-scheduling change (all tables [bp] bottom + dblfloatfix, keep barriers + ASPIRE needspace)

Change vs C2: 7× `table*[htbp]`→`table*[bp]` + `\usepackage{dblfloatfix}` (validated TeX Live; renders, log 0 — package behavior validated, rejected on quality not compatibility); TeX `804636fe…`; deterministic 22pp `a2714f55…`; full proof `diagnostic-r23/candidates/SB/` (TeX/sty/PDF/log/manifest-SB/22 PNGs/review). Tables: T1 p04 / T2 p06 / T3 p09 / T4 p13 / T5 p15 / T6 p17 / T7 p18.

- Table1 FAIL: p04 top `しの手順が残ることが…` (continuation of p03 `立直`) — bottom float still interposes `立直/しの手順…`. Word split persists.
- p09 856-char sparse page (Table3 + little text); p12 1442 / p13 1849 / p15 1983 low-fill. No 702 tail (p18 1769 + p19 1795 fuller — tail eliminated by spreading), but at cost of persistent splits + new sparse pages. Verdict: FAIL. Proves bottom scheduling does not solve systemic drift; `dblfloatfix` technique rendered and rejected with images.

### SC — chapter-end anchoring (explored, rejected early, hash only to save size)

Tables 1/2/3 moved to P1/P2/P3 ends (after `二つの発表…` / `効率の主張を読む物差し…` / `重みの公開は進んだが…`) + 3 new FloatBarriers (6 total); TeX `b57922d3…`, 23pp `7f302dd0…`; Tables T1 p05 / T2 p08 / T3 p11 / T4 p14 / T5 p16 / T6 p18 / T7 p19. Result: p04 419 / p07 918 / p13 1369 sparse text-only pages + p20 702 tail persists. FAIL (large voids, +2 pages). Hashes recorded; full PNGs omitted (SA+SB already satisfy two-strategy minimum; SC documented as third explored failure).

Comparison: C2 21pp/4 splits; B 20pp/3 splits; SA 22pp/≥1 split + void; SB 22pp/≥1 split + voids; SC 23pp/voids. No candidate has zero splits + zero voids. Fixing one moves another (proven across 5 renders). 20pp clean, 21/22/23 clean all unrealized with supported print-only changes.

## 4. Table-by-table ledger (best-effort SA; SB/SC/C2/B referenced; physical page/column + source sentences)

- T1 (P1, `WonderとArgon`): C2 p04 FAIL (`立直/し`); SA p04 PASS (p03 complete → fresh `失敗の内訳…`); SB p04 FAIL (`しの手順…` continuation); SC p05 (not claimed PASS; sparse context). Chapter: SA/SB p04 + P2 heading? SA p04 Table1 + ? (see images; P2 heading p04? Actually SA T1 p04, P2 heading? Ledger: SA T1 in P1 before P2 heading — PASS position; SB same position PASS; splits are continuity FAIL, not chapter FAIL).
- T2 (P2, `効率主張`): C2 p06 FAIL (`開/示だ…も、温度`); SA p06 FAIL (`分/母つき`); SB p06 FAIL (mid-para + sparse); SC p08 (sparse, not PASS). All FAIL continuity.
- T3 (P3, `重み・実装・ライセンス`): C2 p09 FAIL (`エンドポ/イント`); SA p10 (moved; p09 bottom vs p10 below-table mapping in review — conservative FAIL); SB p09 (856 sparse + continuity unsafe — FAIL); SC p11 (sparse — FAIL).
- T4 (P4, `生産性とゲート`): C2 p12 PASS (p11 complete → Table4 → P5 heading same-page); SA p13 PASS (shifted, same pattern); SB p13 (table present; previous/next mapping in review — PASS position, continuity not claimed beyond SA pattern); SC p14 (sparse context — not PASS). No recurrence of F-08 chapter crossing in SA/SB (tables still before next headings).
- T5 (P5, `安全の四つの局面`): C2 p14 PASS; SA p15 PASS pattern; SB p15; SC p16 — same as T4 (position PASS, continuity per ledger).
- T6 (P6, `科学エージェントの証拠`): C2 p16 FAIL (`によ/る検証`); SA p17 (moved; p16 bottom vs p17 below-table — conservative FAIL; SA needspace pushed VERID para but reflow moved Table6); SB p17 (same — FAIL); SC p18 (sparse — FAIL).
- T7 (P7, `専門・身体の三件`): C2 p17 PASS (ASPIRE fresh below Table7 — the r22C2 success, preserved); SA p18 PASS pattern (shifted, same needspace); SB p18; SC p19 — position in P7 before bib PASS in all; continuity PASS in SA/SB (inherited needspace) but overall candidates FAIL on other tables.

Headings/notes/URLs/bib: all pages opened for SA/SB; section headings P1..P7 + bib heading present in order; notes intact; URL wraps/B28/B57/B74/B90/71+19/7× secondary/177-ledger/zero machine IDs preserved in SA/SB (same-method checks as r22; see invariance doc). p01 diagnostic stamp intact. No table-only pages in SA/SB (p12 713 / p09 856 are sparse text/table+text, not table-only — still FAIL as large voids, not as table-only).

Tail: C2 p18 702 (sparse); SA p19 702 (same tail shifted +1, still sparse left-only); SB no 702 tail (p18 1769/p19 1795 spread, but splits persist + p09 sparse); SC p20 702 (shifted +2). No strategy eliminates tail without introducing splits/voids. Before/after images: C2 p03→04 vs SA p03→04 (Table1 fixed); C2 p05→06 vs SA p05→06 (Table2 shifted split `分/母つき` side-by-side); C2 p15→16 vs SA/SB equivalents; C2 p18 tail vs SA p19 tail vs SB p18/p19 spread (full occupancy narratives in review indexes, not unsupported unavoidability claims).

## 5. Conclusion

Systemic `table*` drift in two-column cannot be cured by single-spot needspace, global needspace, bottom scheduling, or chapter-end anchoring within print-only constraints (Reader bytes + fonts/margins/columns fixed, no unvalidated packages, no filler). Every rendered alternative either bisects ≥1 word/sentence or creates large sparse pages (713/856/419/918/1369-char partials) or both, plus the persistent 702 tail in top-float variants. Achieving zero-zero would require content reflow (prohibited), typography change (prohibited), or unvalidated one-column fallback (prohibited as silent design replacement). Therefore `R23_SYSTEMIC_LAYOUT_BLOCKED` with actual evidence, not fake PASS. Worker self-PASS is never Sol/independent certification. No Human Gate/Reader/Publication/Freeze/Release.

(End.)
