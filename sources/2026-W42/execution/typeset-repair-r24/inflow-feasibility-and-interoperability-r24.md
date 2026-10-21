# W42 r24 inflow feasibility and interoperability (isolated Phase A + full-issue result)

Date: 2026-10-18 JST. Status: `R24_LAYOUT_QUALITY_BLOCKED` (sample viable; full 7-table strip fails quality: missing Table4 row + sparse tail + overfull/only-floats warnings). No Gate.

## 1. Installed versions (actual environment, not assumed)

- `lualatex`: LuaHBTeX 1.24.0, TeX Live 2026 (`/home/eariver/.local/bin/lualatex`; TinyTeX, tlmgr 80600).
- `cuted.sty`: NOT preinstalled (kpsewhich exit 1). Installed for isolated test via `tlmgr install sttools capt-of` (local `~/.TinyTeX` only; shared `preview.sty` untouched — cuted/capt-of added to `main.tex` only, never blindly into shared style). Installed: `cuted 2025/12/15 v2.10` (`.../sttools/cuted.sty`), `capt-of 2009/12/29 v0.2`. Purpose per source: insert onecolumn full-width material in twocolumn, resume two-column; options spread/shrink, `stripsep 15pt`; known caveats (docs): floats/footnotes/right-column/output-routine/multiple-strips interactions. W42 has zero `\footnote` (7 `footnote` hits are all `\footnotesize`), so footnote caveat inapplicable; float caveat applicable (see full-build warnings).
- Kernel/log versions in `diagnostic-r24/phaseA-sample/sample-strip.log` and `diagnostic-r24/main.log` (complete logs archived).

## 2. Phase A sample (mandatory first; 2 consecutive verbatim tables + verbatim paras)

Isolated `/tmp` sample (NOT canonical): jlreq + preview toolchain + `cuted` strip + `\captionof{table}`, `\twocolumn`, verbatim P1 Table1 (`WonderとArgon`) + surrounding verbatim paras (`Wonderの例示タスク…`, `失敗の内訳…立直しの手順…`, `実演と検証…`, `二つの発表…`) + P2 heading + verbatim (`比較不能…分母つき…`, `16種ベンチ…分母の開示だ…`) + Table2 (`効率主張`) + `温度の個別開示…`. No bibliography (citations undefined in sample only; full W42 has thebibliography and resolves — sample warnings are sample artifact).

Result: compiles exit 0, 3pp, 2× Overfull `\vbox (25.37pt)` (output active) — same class as Sol synthetic (overfull noted, not ignored). Tables in-flow mid-page/between complete paras (Table1 p02 middle, Table2 p02 bottom): above each table ends complete cite/para, below each starts fresh para — the previously split sentences (`立直し`, `分母の開示だ`) intact on same pages, NO bisection. Captions `表 1`/`表 2` numbered via `\captionof`, visible words match source (`比較表：WonderとArgonの読み分け`, `比較表：効率主張の読み分け`); cells/rows/cites intact; no missing/duplicated chars; no page-order mix; no footnote displacement (none exist); two-column body retained (not one-column fallback); no font/margin/baseline/column-gap change. Archived: `diagnostic-r24/phaseA-sample/` (TeX/sty/PDF/log/3 PNGs/manifest).

Viability: PASS for small tables as mechanism (in-flow placement works, captions work, interoperability with jlreq/luatexja/tabularx/tcolorbox/hyperref holds for sample). Overfull warnings flagged for full-build monitoring (they predicted Table4 clipping below).

## 3. Alternative considered

Independent safe alternative (bounded column-switch/output-routine method) not needed — `strip` satisfied mechanism viability in Phase A. No silent one-column fallback used. Rejected `float[H]`/more-needspace/float-placement variants per r23 (already proven to shift splits); not re-tested here.

## 4. Full-issue outcome (summary; details in boundary audit)

Phase B full 7-table strip (all `table*[htbp]`→`strip` + `\captionof`, `cuted`+`capt-of` in main.tex only, removed `placeins`/3 barriers/ASPIRE-needspace as float-specific; cells/captions/cites/rows/chapters unchanged): deterministic 21pp `8dea62f2…`, tables T1 p03 / T2 p05 / T3 p08 / T4 p11 / T5 p13 / T6 p15 / T7 p16 in-flow (not page-top floats) — splits fixed by construction (tables between complete paras). BUT: Table4 Decider row missing in print (`Decider v1.2` 1 occurrence vs C2 2; overfull `\vbox 93pt` p11 clips row) = missing table cells HARD FAIL; p18 tail 508 chars (worse than C2 702) = large near-empty FAIL; warnings `twocolumn too tall` + `Text page contains only floats` (with zero floats — output-routine interaction) + 4 overfull/underfull hits. Second anchor V2 (Table7 P7-end): 21pp `a4f09f01…`, p18 405 chars (worse) — hash only. Hence `R24_LAYOUT_QUALITY_BLOCKED` (sample works, full fails), NOT `FEASIBILITY_BLOCKED`, NOT READY. Never grounds for Core change.

(End.)
