# W43 r2 reader-to-print fidelity and citations (body unchanged, bib repaired)

Source r3.5 `6f07cb49…`, ledger `6fd9d6fe…`, manifest `85d94d74…` (checker PASS exit 0).
r1 projection `e1a49da9…` == r2 projection (body identical); r2 TeX `1430f2e1…` differs only in bibliography block (36 complete entries) + sty version comment.
PDF r2 `922fa1d5…` 483473B 22 pages (r1 `fd88cb7c…` 480229B 22 pages; +3244B from complete bib sentences, no new pages).

## Body parity (r1 = r2)

- P1–P8, 19 selected (12+7), 20 tables/80 rows (78 DATA+2 NOTE), 3 figures, 2 code + 2 JSON illustrative, 29 claims, 5-para recap after P8 — all byte-identical to r1 projection (diff `diff -u` clean except TeX bib).
- Operator tokens naturalized, internal paths neutralized, limits retained (see r1 diff + r2 diff).
- 29 claims: p2-f2 licenses (4), p5-f1 Voxtral (9), p7-f1 low-resource (8 incl. COBOL 40%+ prevalence separate), p8 clocks/scale (4), p8 DeepSeek (4) — own-block DATA with physical-value proof, units/comparators/URLs/tiers unchanged.

## Bibliography repair (r1 -> r2, the only TeX change)

- 36/36 entries rewritten from 60-char truncation to complete sentences preserving negatives (see source-key audit).
- Fixed: MEMT storage-vs-speed, Voxtral comparator/unit, DeepInfer import path, Patch 5 stages, TanStack GH-vs-npm separation (GH proves GH only), decisions post-cutoff guards.
- No invented URL/date, no tier upgrade, no URL dump. 典拠キー -> bibitem mapping unchanged and now unambiguous.

Tiers preserved: 5 RAW_PRIMARY / 24 QUALIFIED_UNAVAILABLE / 0 OTHER.
