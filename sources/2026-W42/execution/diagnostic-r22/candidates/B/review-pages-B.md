# W42 r22 Candidate B visual proof — per-page index (ALL 20 pages opened @150dpi; REJECTED, archived for independent audit)

Build: LuaHBTeX 1.24.0, SOURCE_DATE_EPOCH=1792311600 (runs 2–4 byte-identical SHA256 `26fee7bc8720dd6c36fd613a80ee61cae4c3ef6f23e7ef389476ac94ed1310ae`, 508,225B, 20pp). TeX 95,106B/971 lines, SHA `fb644c008b54c7c81024f43804597906f39d660147a51ce0f11f0a9c686a9651`; preview.sty identical to r21; NO placeins/FloatBarrier (early relocation, no barrier). Display fix preserved (7× `[二次・参考]`, 71 full + 19 aliases). Per-page chars: 480/2495/2668/2353/2552/2431/2731/2674/1787/2526/2351/2434/2049/2693/2486/2361/2115/2850/3108/2698 (p11 2351/p12 2434/p13 2049 match r21 Alt-B report exactly; 971 lines match r21 Alt-B report).

Chapter boundaries (F-08 SOLVED, as r21 reported):
- p11 Table4 `生産性とゲートの条件` top, P5 heading p12 → Table4 BEFORE P5. SOLVED.
- p13 Table5 `安全の四つの局面` top, P6 heading same p13 below table → Table5 BEFORE P6. SOLVED.
- p15 Table6 `科学エージェントの証拠` top, P7 heading p16 → Table6 BEFORE P7. SOLVED.
- p17 Table7 `専門・身体の三件` top, bib p18 → in P7, before bibliography. Table7 clean: p16 ends complete ASPIRE `…[B57,B56,B89]` (all three ASPIRE paras complete on p16), p17 below-table starts fresh Glimpse `ElorianのGlimpseは…`, no ASPIRE bisection. S21-01 absent in B.
- 20pp = cover1 + body16 (p2–p17) + bib3 (p18–p20); no sparse tail (p17 2115 chars full; p18 bib head). S21-02 absent in B.

Holistic sentence-continuity FAIL (reason for rejection despite 20pp/full pages):
- Table4 p11 top bisects P4 `納品と検出のゲートは…` para: p10 bottom-right ends mid-sentence `…無制限の` / p11 below-table starts `自動化ではないことの宣言であり…` (completing `無制限の自動化ではない…` with Table4 interposed). Mid-sentence split by full-width table — HARD FAIL per r22 §2(2).
- Table5 p13 top bisects P5 ECDSA para: p12 bottom ends mid-word `…隠れビッ` / p13 below-table starts `ト総当たりと格子…` (completing `隠れビット総当たり…`). Mid-word split — HARD FAIL.
- Table6 p15 top bisects P6 baseline-procedure para: p14 bottom ends `…採点` / p15 below-table starts `コードまで公開…` (completing `採点コードまで…`). Mid-phrase split — HARD FAIL.
Images: `candidates/B/pages/p-10.png` (ends `無制限の`) vs `p-11.png` (Table4 then `自動化ではない…`); `p-12.png` (ends `隠れビッ`) vs `p-13.png` (Table5 then `ト総当たり…`); `p-14.png` (ends `採点`) vs `p-15.png` (Table6 then `コードまで…`). All three viewed and confirmed.

Tradeoff documented in r21 (tables before some summarized prose, `preview-then-details`) is valid article design, but physical sentence bisection is not. B proves 20pp fix exists for chapter boundaries + tail, but does NOT pass holistic paragraph-flow. Therefore REJECTED for final selection; C2 (barrier + needspace, 21pp, zero bisections) selected instead. B archived here full (TeX/sty/PDF/log/manifest/20 PNGs) so independent auditor can verify both the 20pp tail fix and the three bisections.

Old regressions in B: cover intact, 90/19 preserved, `[二次・参考]` 7× preserved, B28 complete, B57 kept-together, B74 clean, B90 terminus, no stamp-only page, log 0 errors. Only holistic continuity fails.

(End — B 20/20 pages opened, rejected with proof.)
