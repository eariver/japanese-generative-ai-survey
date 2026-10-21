# W42 r23 Candidate SB bottom-float proof (ALL 22 pages opened @150dpi; REJECTED)

Build: LuaHBTeX 1.24.0, SOURCE_DATE_EPOCH=1792311600 (runs 2–4 identical SHA256 `a2714f551e5e1eab7f355cb60715e578f661551b35e306ed3777ccd073315d23`). TeX SHA `804636fe56e59581458ea105dc80c6bffbcfeefadedb40f61c3ba9b8d83b2e97`; `table*[htbp]`→`table*[bp]` for all 7 + `dblfloatfix` package (validated TeX Live); barriers + C2 ASPIRE needspace retained. 22pp. Per-page: 480/2495/2668/2050/2503/2221/2749/2414/856/2368/2546/1442/1849/2407/1983/2723/2010/1769/1795/2850/3108/2698. Tables: T1 p04 / T2 p06 / T3 p09 / T4 p13 / T5 p15 / T6 p17 / T7 p18.

- Table1 p04 FAIL: p04 top starts `しの手順が残ることが…[B05…]` (continuation of p03 `立直`), i.e. bottom float did NOT prevent split — Table1 (at p04 bottom or p03 bottom via dblfloatfix) still interposes between `立直/しの手順…` halves. Word split persists. Images `candidates/SB/pages/p-03.png` (ends `立直`) vs `p-04.png` (starts `しの手順…`).
- Table2 p06: p06 contains Table2 mid-page (bottom-float) with `母つき…` fragments nearby; paragraph-unsafe (see audit ledger; conservative FAIL).
- p09 856-char sparse page (Table3 p09 + little text), p12 1442 / p13 1849 / p15 1983 low-fill: bottom-float scheduling spreads tables but leaves multiple partial pages. No 702 tail (p18 1769 + p19 1795 fuller — tail eliminated), but at cost of persistent splits + new sparse pages (p09 856). Tradeoff FAIL.
- Old regressions PASS (90/19, display labels, B28/B57/B74/B90, cover, log 0). Holistic FAIL (≥1 word split + sparse p09). Rejected; archived full here as second distinct global strategy proof (float scheduling vs SA paragraph-completion). Technique `dblfloatfix` bottom floats validated as rendering (no crash, log 0) but rejected on print-quality grounds with actual images, not on package grounds.

(End — SB 22/22 opened, REJECTED.)
