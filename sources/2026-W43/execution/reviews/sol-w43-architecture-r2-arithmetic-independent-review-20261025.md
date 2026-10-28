# Sol W43 Architecture r2 independent audit — substantial editorial repair, P1 arithmetic error

Status: `SELECTION_PASS_WITH_LIMITATIONS / ARCHITECTURE_R2_REQUEST_CHANGES / NO_ADVANCE_STAGE`
Date: 2026-10-25 JST
Repository `eariver/japanese-generative-ai-survey`
Reviewed remote work branch `weekly/2026-W43-v2-work` HEAD `3f3c40b77d7ca7acde9ecb0612452210a4f45d26`, root Tree `0307dee0296c7685bd1bb73c5a90d50eb0c7a2fc`, exact parent `fe6809f53969ad388d7288a54a4fd7aa509d515d`.
Reviewed main HEAD/Tree `041a08dfef3112643cbf85b4a86a7b6f9128aed6`/`a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core branch HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
Work commit one ordinary FF, 19 W43-only files; 12 new, 7 modified proposal/index artifacts; no shared Core, Evidence r4, State, Gate or Stage mutation. Actual Production State still `EVIDENCE_REVIEWED`, next `stage:selection`; Selection/Architecture checkpoints pending; Architecture and Publication Preview Human Gates PENDING.

## Independently verified structural and integrity items

- Candidate Matrix 32 and Selection exact 19 SELECTED/1 HOLD/12 REJECT. Canonical Matrix/Selection unchanged byte-for-byte from r1 as shown by identical Git blobs. All 19 selected candidates occur once in the eight proposed Architecture packages; none unplaced, HOLD/REJECT never placed, Metrics POST_CUTOFF NON_MATERIAL and Grok NEVER_STORY REJECT. One technical HOLD moss-trainer remains appropriately quarantined. Accepted Discovery/Screening/Evidence unchanged.
- Historical r1 versions of Matrix/Selection/Architecture/Review Summary/Review Attention plus input/audit preserved under `execution/history/selection-architecture-r1/`; exact Git blob equality of archived matrix/selection with r1 canonical confirmed.
- Independently recomputed SHA-256 from the exact five canonical r2 JSON text files; **5/5 MATCH** against `orchestration/v2/interactive/selection-architecture-audit.json`:
  - Matrix `16a6bbfe569b3215d05fbae7175b3ca04efc6c1846d28c48662245b68f854c3b`
  - Selection `50decd8697e1737d7adf6fe9f1ac0f4c7cc891353a7be09461b86e8b90beccea`
  - Architecture `53f049d059626245bc316b9c77e1c5b4a68ed24eee5f6439b5b4ffedde9981c9`
  - Review Summary `6bc2784079c1889da7699db6ae00d0257ccaa09e8a4b7b1e8363eca97e89d612`
  - Attention `7c3e4deb4a2cd077acac148c777aa2300f1f4dad45bbc4d0624a6b693528f12b`
- Attention is **68/68 unique items**, limit 100, truncated FALSE, overflow 0 (r1 was 50/68), frozen Core `build_attention(limit=100)` legitimately supports this; Muse reports native runner + `validate_attention` PASS, frozen Stage scratch precheck EVIDENCE_REVIEWED→SELECTION_COMPLETE PASS. Sol did **not** independently execute Python CLI in this review; source SHA/invariants were independently read from GitHub.
- Sol SA-001 Kimi headline corrected: model API in-window, weights promised Nov4 future, Flint/Nemotron available now; distinction between OSI open-source and published weight files explicit.
- SA-002 canonical page figures internally coherent: P1 5.0, P2 6.0, P3 4.5, P4 3.0, P5 4.5, P6 4.0, P7 4.5, P8 3.5 = **35.0**, front matter/reference allowance 2 = **37.0 estimate** versus target 38/max 44. The 38 target and 44 ceiling are estimates, not frozen Profile limits.
- SA-003 eight packages now have 31 explicit numbered technical subsections (§1.1–§8.3 etc.), source constraints/tables and limitations. P2 6pp, P5 and P7 4.5pp, P8 3.5pp, substantially improved source-bound depth vs ~29pp r1. Actual body/benchmarks still not independently reproduced; no guarantee of actual final page count.
- SA-004 original mistranslation `Corde`, `符号化`, `辺境訓練` removed and replaced with mostly natural technical phrases. SA-005 full attention resolved. SA-006 per-package MUST-NOT and evidence classes present; Kimi X/blog, Flint article/HF, MemT PDF/README, Patch rendered-only, Securing RSS, TanStack product/blog, FLUX vendor numerical contradictions and AA gaps explicitly bounded. Five earlier LIMITED domains remain.
- Architecture Review Summary is `READY_FOR_ARCHITECTURE_REVIEW` with zero mechanical errors, but this is **NOT** editorial nor real Human Architecture approval. `architecture-v2.json.human_review` fields remain null.

## New W43-SA-007 — P1 numeric equation transposition in publication-facing article brief

In **current r2 canonical** `sources/2026-W43/architecture-v2.json` `packages[P4].must_cover_requirements[1]` (and repeated in edition-local interactive input) states:
`§4.2 速度の再計算(10.95/277.80=25.37x、12.45/277.80=22.31x、頁~22x は正、blog 26.5x/96.2% は同入力で不整合・真 95.52%)`.

These equations are **mathematically false** even though the intended speedup factors are correct:
- `10.95 / 277.80 = 0.0394168`, NOT 25.37.
- `12.45 / 277.80 = 0.0448164`, NOT 22.31.
- Correct baseline / candidate speedups: **`277.80 / 10.95 = 25.3699 ≈ 25.37x`** and **`277.80 / 12.45 = 22.3133 ≈ 22.31x`**.
- For 12.45s case, time reduction is **`(277.80 - 12.45) / 277.80 ×100 = 95.5184% ≈95.52%`**. Publisher's claimed 26.5x/96.2% is inconsistent with 12.45s/277.80s, which must remain a clearly attributed vendor inconsistency, not corrected away or called independently benchmarked.
- Critical risk: this package's sole premise is **numeric methodology and denominator discipline**; a reversed equation undermines its technical reliability, may be copied literally into Japanese article, table or PDF, and conflicts with the accurate ratio in earlier independent Source/Materiality reviews. Old r1 had same reversed equations; the r2 repair preserved them. Record as a newly discovered editorial failure, not as a new source fact.
- 10.95s original PR-origin figure is not archived in the current fal product/blog raw; retain the explicit `PR origin NOT RAW VERIFIED` uncertainty. Do NOT synthesize evidence for 10.95s or promote vendor AA/Elo into independent reproduction.

**Mandatory r3 action:** correct both equations in interactive input and canonical Architecture; any other r2/reader-facing page allocation or reviews that repeat them must be corrected consistently; regenerate derived Core Review Summary and audit SHA, maintaining full 68/68 Attention basis. Check math via two independent arithmetic evaluations including numerator/denominator labelling. Add bounded negative test `reversed-speedup-equation must not appear in canonical architecture/summary/review packet`.

## Current disposition and next stage guard

**SELECTION PASS_WITH_LIMITATIONS; ARCHITECTURE REQUEST_CHANGES solely on SA-007**; previous six r1 SA findings sufficiently addressed with the noted LIMITATIONS. No `ADVANCE_STAGE`, Selection Bridge, Architecture Bridge, Human approval, Draft/PDF or Publication. Formal State remains EVIDENCE_REVIEWED. Do not broadly re-research or reselect 19.

Proposed narrow, repeatable worker action: snapshot original r2 unadvanced proposal set; isolate and regenerate r3 Architecture-only numeric correction via unchanged frozen Core without overwriting accepted r4 Evidence, ensure exact Matrix and Selection **byte-identical** to r2, all 19 placements and eight package count stable, Summary fresh READY, untruncated native Attention 68/68, all five hashes and runner metadata consistent. New current Stage scratch precheck only; stop for Sol re-audit, then separately trusted Selection and Architecture advancement. If regeneration blocked, stop with true diagnostics rather than stale hashes or local validator bypass.
