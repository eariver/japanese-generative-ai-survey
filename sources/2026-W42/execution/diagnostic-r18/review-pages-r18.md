# W42 r18 diagnostic visual QA — per-page review index (21 pages @150dpi)

Build: LuaHBTeX 1.24.0 (TeX Live 2026), `SOURCE_DATE_EPOCH=1792308600 lualatex -interaction=nonstopmode -halt-on-error` ×4 (final two byte-identical SHA256 `d42510f975cbfb60db52ef29e55eb6209214512e439d592c578990c934701683`, 511,523 bytes). Log: 0 warnings (excl. pkg info), 0 overfull, 0 underfull, 0 errors, 0 missing glyphs. Fonts: HaranoAji Mincho/Gothic + Latin Modern. TeX 96,865 bytes; 136/136 paragraphs verified; 90/90 bib keys cited. Contact sheets split 3× (~2.2MB each).

Text-identity vs r17 (extracted): SAME p1,2,4–13,16,18; DIFF p3 (t1-23), p14 (t6-08), p15 (reflow −24), p17 (t7-19), p19–21 (bib repagination from B57 needspace). SAME pages carry r17 visual QA + spot verification; all DIFF pages opened below.

- p01 cover (SAME text): stamp + cutoff/repo/build. Sparse by design. PASS (text-identical to viewed r17; spot-opened structure unchanged).
- p02 P1 head (SAME). PASS (text-identical).
- p03 P1 ledger **FIXED**: t1-23 now `…提供原価ではない。初回起動の単一試行という限界とセットで読む。固定シードや…` — no `t1-16`. Cost/single-run/random-world kept. PASS (viewed).
- p04–p13 body (SAME text; P4 Maia 1-pod/750GB/s, P6 LFM entity-revenue/§5(c) from r17 intact). PASS (text-identical to viewed r17).
- p14 P6 **FIXED**: t6-08 now `…計画の上乗せは効かない。CBGBも…` — parenthetical `t6-06` note gone; GeoKTools/Table-5 negatives kept. PASS (viewed).
- p15 P6→P7 reflow (knock-on −24 chars, no edit on page): paragraphs complete, no split sentences, no orphans. PASS (viewed).
- p16 P7 GLM anchor (SAME). PASS (text-identical).
- p17 Table-7 in-body kept + t7-19 **FIXED**: `…前提で読む。HSS46.36が…` — `t7-07` note gone. Table at top with body below/after; t7-04 complete before table, ASPIRE complete after — no sentence split by float. No orphan. PASS (viewed).
- p18 bib head B01–B28 (SAME text). PASS (text-identical).
- p19 bib B29–B56 (repaginated): B28 URL tail `lein` 4-char carry at page top (consequence of B57 needspace pushing bib flow; readable entry continuation, not isolated). No other splits. PASS with noted carry (viewed).
- p20 bib B57–B81: B57 entry kept together on page via needspace (URL wraps ASPI/RE intra-entry, readable) — r17 page-top lone-`RE` orphan GONE. B58–B81 alias cross-refs readable. PASS (viewed).
- p21 bib B82–B90 + footer stamp (repaginated, +62 chars from shift): aliases readable, B89/B90 caveats kept, stamp present. PASS (viewed).

No clipped glyphs, no isolated table page, no cross-chapter floats (7 tables in-chapter). Old r17 B57 page-top orphan class: absent. Residual minor: B28 4-char URL carry (p18→p19), readable, documented.
