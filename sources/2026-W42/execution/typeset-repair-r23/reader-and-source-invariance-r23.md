# W42 r23 reader-and-source invariance (diagnostic-only; NONCANONICAL)

Date: 2026-10-18 JST. SA (best-effort) + SB (comparison) both print-only transforms of exact r22 C2 TeX (itself print-only of exact r18 Reader). No Reader/prose/quote/order/scope bytes changed. No font/margin/line-spacing/column changes, no filler, no content deletion.

## 1. Master identities

- r18 `reader-preview-r18.PROPOSED.json` blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` (re-verified `git hash-object`), 7ch/28sel/157 blocks/136P/25015ch/7T/7N; 90 B keys, 19 aliases, 177 ledger rows. 7 v18.0 proposals + bib-map/ledger/dup-matrix unchanged.
- r22 C2 TeX `7e95ae84…` (95,226B/968 lines); PDF 21pp `38d3796f…`; B TeX `fb644c00…` (20pp `26fee7bc…`). r22 150/150 + 7 tables inherited by diff transitivity (r22 docs).

## 2. r23 TeX diffs (prose-preserving)

- SA vs C2: +5 `needspace{8\baselineskip}` before `失敗の内訳…`(T1) / `16種ベンチ…`(T2) / `IBM Granite Switch…`(T3-left) / `MiniCPM-V 4.7…`(T3-right) / `VERID較正…`(T6); retained ASPIRE needspace (6 total). No paragraph/quote/cite text added/removed/reordered. All 7 `table*` blocks byte-identical (positions unchanged in SA; only needspace lines added). TeX `0717a682…` (95,662B/973 lines).
- SB vs C2: 7× `table*[htbp]`→`table*[bp]` + `\usepackage{dblfloatfix}` (validated TeX Live; log 0, renders); barriers + ASPIRE needspace retained. No prose edits. TeX `804636fe…`.
- SC (hash only) vs C2: Tables 1/2/3 cut (589/480/961B byte-identical) from early to P1/P2/P3 ends + 3 FloatBarriers (6 total). No cell edits. TeX `b57922d3…`, 23pp `7f302dd0…` (documented, full PNGs omitted; SA+SB satisfy two-strategy minimum).

## 3. Equality checks (same-method, SA/SB vs C2)

- Tables 7/7 `begin{table*}`; captions/cites/rows byte-identical (diff shows only needspace/float-spec/barrier lines, no cell edits).
- Non-TABLE 150/150 inherited via zero-prose-diff (above) + PDF-text spot checks (normalized): Minecraft `立直しの手順…検証口`, LFM `分母の開示だ…AutomationBench`, Granite `エンドポイント`, VERID `染料と水による検証`, ASPIRE `80課題で99%…卓上片づけ`, Glimpse `WGO 42.70…HSS 46.36` all present in SA/SB PDFs (split across pages in print, but bytes present — print split ≠ source deletion).
- Zero machine IDs: TeX 0 `alias-of`/`normalization`/`CLAIM_BOUNDARY` in SA/SB; block-ID regex 1 hit each (`t7-02` provenance comment, as C2); PDF-text block-ID 0; `NONCANONICAL` 1 (cover only).
- Fonts/spacing: `preview.sty` byte-identical to r22 (verified); no margin/column/font/line-spacing changes; `dblfloatfix` only enables bottom dbl floats (no typography change; log 0 warnings).
- Bibliography 90/19/177: 90 `\bibitem[B`, 19 `（同一資料）`, 17 `[二次・参考]` (7× B63/64/66/67/68/70/71 + existing), 0 `[SECONDARY]` in SA/SB TeX (preserved); PDF-text `[B` counts identical same-method to C2; B28 complete, B57 kept-together, B74 clean, B90 terminal preserved (viewed SA/SB bib p20–p22/p20–p22).
- Prior regressions preserved in bytes (Argon random world, Maia 24/96/750GB/s, Earth dependent negatives, MTP accepted-token length, wet-lab 131/311 vs 8 clones, LFM legal entity, ASPIRE robot caveats) — print splits do not alter source bytes.

## 4. New hashes (read-back)

- SA TeX `0717a682…` (95,662B/973); PDF 22pp `c1f8b6a4699b2c3c21f80118e06499e43901d7a86372a6e1b999ce152b87ce3c` (509,560B); log 0 errors. Per-page chars [480/2495/2533/2343/2523/1551/2522/2429/2450/1990/2689/713/2227/2187/2231/2625/2171/2346/702/2850/3108/2698].
- SB TeX `804636fe…`; PDF 22pp `a2714f551e5e1eab7f355cb60715e578f661551b35e306ed3777ccd073315d23`; per-page [480/…/2050/…/856/…/1442/…/1769/1795/…].
- SC TeX `b57922d3…`; PDF 23pp `7f302dd0…` (hash only).
- No shared-Core/main/canonical/State/Gate/r11–r22 bytes touched (`git status` clean except new r23 paths + index append; `editorial-revision-r18/` diff empty).

(End.)
