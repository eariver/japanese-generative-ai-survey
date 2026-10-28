# W43 architecture coverage and volume diagnosis r2 (grounded, no new audit)

Source: `sources/2026-W43/architecture-v2.json` (8 packages, 31 must-cover). Reader: r3.5 fixed `6f07cb49…` (62 paras, 20 tables/80 rows, 3 figs, 29 claims). PDF: r2 `main.pdf` 22 pages (cover1/TOC1/body18/bib2). Prior independent baseline **20 SUBSTANTIVE_COMPLETE / 11 PARTIAL preserved**; this is worker location/depth observation only, NOT a new 31/31 authoritative audit.

## P1 (5) — PDF p3-5

1. §1.1 Kimi API先行 vs Nov4 FUTURE — reader P1 paras + table p1-t1 — PDF p3 — SUBSTANTIVE (17:15:24Z, 4h44m36s, $2/$10, FUTURE separation explicit).
2. §1.2 MoE対比（2.8T Xのみ等） — paras + p1-t2 — p3-4 — SUBSTANTIVE (count conventions separated, no equivalence table).
3. §1.3 文脈長三層 — figure p1-f1 + prose — p5 — SUBSTANTIVE (1M/512k/256k/262144/64K distinguished).
4. §1.4 学習・量子化・bench帰属 — prose + p1-t3 — p4 — PARTIAL (vendor harness conditions listed; no independent rerun — as approved).
5. §1.5 可用性・約款・価格 — p1-t4 — p4-5 — SUBSTANTIVE (API/FUTURE/live separated, OpenMDW vs Apache distinguished).

## P2 (6) — PDF p6-8

6. §2.1 DeepInfer核 — p2-t1 — p6 — SUBSTANTIVE (6 components + DP/CP/EP roles).
7. §2.2 排他的構成例 — prose + bash/python verbatim — p6-8 — SUBSTANTIVE (MUST-NOT simultaneous, NVIDIA限定, NOT_EXECUTED preserved).
8. §2.3 実装条件 — prose — p6 — SUBSTANTIVE (SM100/950, 1017, 4xSM100 bench, exclusions explicit).
9. §2.4 MemT記憶 — prose + p2-t2 — p7 — SUBSTANTIVE (66x storage-only, parametric scope, 1.86x SOURCE_UNVERIFIED separated).
10. §2.5 権利分離 — table p2-f2 — p7 — SUBSTANTIVE (CC/PolyForm/MIT/excluded + README-only caveat).
11. §2.6 限界 — reading note — p7-8 — PARTIAL (DEPTH_LIMITED: no independent run, 65pp unread — as approved).

## P3 (4) — PDF p9-10

12. §3.1 権限×条件 — p3-t1 — p9 — SUBSTANTIVE (waitlist/prior/limits + behaviors).
13. §3.2 目録vs live・1Password — figure p3-f1 + prose — p10 — SUBSTANTIVE (coming-soon not live, prohibitions explicit).
14. §3.3 安全積層・承認注入 — prose — p9-10 — PARTIAL (vendor-described layers, classifier no independent test — as approved).
15. §3.4 auto-mode — p3-t2 — p10 — SUBSTANTIVE (8/7 OUT, 10/22 IN, next-week FUTURE not complete).

## P4 (3) — PDF p11-12

16. §4.1 post-train・keyframes — prose — p11 — PARTIAL (UNRESOLVED_FAQ_ATTRIBUTION preserved, live not confirmed — as approved).
17. §4.2 速度再計算 — p4-t1 — p11 — SUBSTANTIVE (25.37x/22.31x/95.52% verified arithmetic, 26.5x incongruent, 22x lower-bound, no falsely-mathematical claim).
18. §4.3 Elo・価格 — prose — p11-12 — PARTIAL (+47/+50 not unified, AA unfetched — as approved).

## P5 (4) — PDF p12-14

19. §5.1 Voxtral家族 — p5-t1 — p12 — PARTIAL (TTS counts unresolved, 11-lang sample ≠ coverage — as approved).
20. §5.2 TTS内部評価 — prose + p5-f1 part — p12-13 — PARTIAL (gemini-3.8-flash vendor-selected, units qualified — as approved).
21. §5.3 Ming — p5-t2 — p13 — PARTIAL (MIT confirmed, AA cited originals unfetched — as approved).
22. §5.4 Eleven — prose — p13-14 — PARTIAL (compat listed, guide unopened, AA via blog — as approved).

## P6 (3) — PDF p14-15

23. §6.1 Patch五段階 — figure p6-f1 + prose — p15 — SUBSTANTIVE (stages verbatim, Daybreak/checker outside, CVE unidentified≠absent).
24. §6.2 Securing — prose — p14-15 — PARTIAL (vendor-described isolation, RSS secondary — as approved).
25. §6.3 囲い・W42区別・来歴保存 — prose — p14 — SUBSTANTIVE (Oct23 vs W42 separated).

## P7 (3) — PDF p15-17

26. §7.1 Bio — p7-t1 — p15-16 — PARTIAL (team-internal, wet-lab unconfirmed — as approved).
27. §7.2 Low-resource — p7-t1/p7-f1/p7-t2 — p16-17 — SUBSTANTIVE (20-lang table, COBOL 10.9→72.1 + 40%+ prevalence separate from accuracy, hidden kept, cost≠quality).
28. §7.3 盲検・標本・請求限界 — prose — p17 — PARTIAL (bias/unverified retained — as approved).

## P8 (3) — PDF p17-20

29. §8.1 Decisions — p8-t1 + JSON illustrative — p17-18 — SUBSTANTIVE (400 per-request, v1/beta, cache, NOT_RUN preserved).
30. §8.2 TanStack — p8-f2 — p19 — SUBSTANTIVE (GH 15:18:14Z vs npm 15:21:49Z separated, scoped URL, Metrics OUT, Grok excluded).
31. §8.3 DeepSeek — p8-t2/p8-f3 — p19-20 — PARTIAL (MIT vendor-declared SHA unseen, bench vendor harness — as approved).

Count: SUBSTANTIVE 20 / PARTIAL 11 / NOT_VISIBLE 0 — consistent with prior 20/11 baseline; no new 31/31 claim. 19 placements (12+7) all printed; 5-para recap p20 after P8 (not P9).

## Volume: why 22 vs 38

- Actual: cover1 + TOC1 + body/closing18 + bib2 = 22. Body holds 62 paras (~3.4 paras/page) + 20 tables (avg 4 rows) + 3 figs + 4 code blocks, single-column 10pt jlreq 18mm margins, honest density, 0 overfull.
- Architecture page_plan: P1 5.0+P2 6.0+P3 4.5+P4 3.0+P5 4.5+P6 4.0+P7 4.5+P8 3.5=35.0 + front/back 2.0 = 37.0, target 38/max 44, with note “見積であり保証ではない” and “r1(29.0)からの増分は必須節の細分化による”. r3.5 approved prose is concise (71841B); subdivision did not materialize as 35 body pages.
- Bibliography: 36 entries in 2 pages (dense but readable, URLs break). No third-page padding (contract forbids).
- W42 final 21 pages precedent shows ~22 is normal weekly density for this style.
- No NOT_VISIBLE requirement; all 31 located with pages above. Depth matches approved PARTIALs (unresolved qualifiers retained, not erased for length).

Conclusion: gap is estimate-vs-actual density, not missing must-cover. No padding applied. No material unexplained gap warranting `VOLUME_OR_LAYOUT_REVIEW_REQUIRED` on coverage grounds; Sol adjudicates whether 22-page honest proof suffices for Human PDF Gate or a separate substantive expansion is authorized elsewhere.
