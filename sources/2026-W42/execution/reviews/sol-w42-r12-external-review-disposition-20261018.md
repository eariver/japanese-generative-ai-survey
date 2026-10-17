# W42 r12 independent-review intake and Sol editorial disposition

Date: 2026-10-18 JST
Authority: **separate independent review report received from Human Owner**; this file is a **Sol operator/editorial disposition**, NOT a second self-conducted independent audit or Human approval.
Source document: `20261018025700_SolReview.md` (user-provided separate-session independent read-only review, full 9-section report; independently archived by reviewer on Google Drive according to its declaration). This ledger summarizes rather than fabricates a GitHub-persisted copy of the full independent report.

## Fixed reviewed identity

- Existing W42 branch: `weekly/2026-W42-v2-work`
- r12 starting HEAD/Tree: `64cb2967ea77e3db5ef8eebe8a22fff48164fb3a` / `e27a8b01b4d29ad32b6fb28147a74276d4548f1d`
- Independent reviewer-reported and operator read-only cross-checked final r12 HEAD: `456f662e412c7c467e9a07a6b8308795f213e1d0`, Tree `2dc024d74b32d3226a250edb9a3dd6195ef09852`
- main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Frozen Core HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`; unchanged by r12.
- Exact r12 diff: one normal child commit, 21 changes only in `sources/2026-W42/execution/`, including 16-page NONCANONICAL proof PDF. Canonical Draft, State, Gate, Architecture and checkout Core untouched.
- Formal lifecycle remains `DRAFT_COMPLETE`, Human Architecture Gate `approved`, Publication Preview `pending`; **neither validated publication nor Human Preview approval exists**.

## External auditor verdict — ADOPTED

**`REQUEST_CHANGES / PDF_VISUAL_UNVERIFIED / NO_PUBLICATION_AUTHORIZATION`.**

The separate reviewer confirmed prior F01 (LFM operative license clauses vs complete LICENSE, Beam Apache 2.0 obligations) and F02 (seven unrelated internal OCP/Claude/Minecraft source mappings) had been repaired in the targeted r12 proposed files; the 106-row r12 citation ledger has 0 non-http source values, 59 distinct external URLs. That does not certify every source-to-claim correspondence. The reviewer could not obtain actual PDF binary through its connected GitHub text API; it **did not inspect PDF page images**. Muse reports 16 pages and visual QA, but **this is NOT independently verified**. The PDF exists by Git blob `5b2614ac368fe18e6d8241f50865333e3a824b15` (419471 bytes) under `execution/preview-r12/main.pdf`.

Do not repeat Human Architecture Review: r1 APPROVED persists with existing seven packages, 28 selected, target 28 pages, max 30. No new editorial gate is granted; do not alter accepted upstream.

### Mandatory Major findings for r13

- **M01 technical mistranslation**: P3 Nemotron MTP `4.287→4.718` is an **average speculative decoding acceptance length**, not `受理率`; qualify unit, draft-length and decoding condition from original NVIDIA report (reviewer's recommendation: greedy, draft length 7; independently reconfirm exact condition before quoting).
- **M02 wet-lab experiment denominator**: P6 `131/311=42.1%` is the screening/sample outcome; **eight clones** belong to a later titer/confirmation stage, NOT the denominator behind 42.1%. Distinguish assay stages, purpose and limitations explicitly.
- **M03 scale/word-count methodology**: 92 paragraphs independently counted **18,165 paragraph-only characters**; Muse's `21,281 body chars` mixes in table/notes/headings or other categories, not a comparable metric. Relative r11 17,004 → r12 18,165 **+1,161 characters**, not a meaningful 28-page restoration. ~16-page proof versus target 28pp means substantial evidence-backed method/explanation development is still required; **no layout padding** or hidden Architecture reduction.
- **M04 reader traceability**: TeX has **no inline `\\cite{}`** and chapter-level 59 raw URLs, making individual benchmark numbers/license terms untraceable. P7 "一次リンク" includes MarkTechPost SECONDARY; label primary/evaluator/secondary accurately and bind assertions/table cells to precise source keys. Use appropriate formal bibliography tools only through unchanged Core/tooling.
- **M05 independent PDF QA blocked**: no versioned compile log or all-page PNG/contact-sheet/density report was committed, so separate reviewer could not inspect binary rendering; generate reproducible visual inspection material and **test accessibility with the independent auditor's likely retrieval path**, or remain BLOCKED. Do not upgrade Muse's self-QA to independent PASS.
- **M06 provenance timestamps**: r12 proposals `runner.generated_at=2026-10-18T03:00:00Z`, synthesis `04:00:00Z`, but parent-creation commit `2026-10-17T17:47:18Z` predates those recorded generation timestamps by ~9–10h. Investigate actual executor clock/source (likely placeholder or TZ error), write an explicit edition-local provenance correction notice; **do not rewrite immutable r12 or accepted files**. Neither fabricate timestamps nor allege intentional falsification without proof.

### Minor findings for r13

- m01 P2 `分母の practice`: replace with idiomatic Japanese describing evaluation denominator/method.
- m02 P6 `100万`: source-check meaning and units; use `100万トークン` only after verified.
- m03 P5 METR `6名の常駐`: limit to independent evaluators granted employee-equivalent access, unless onsite residency is actually documented.
- m04 Remove repetition about Argon pricing, Maia N2P, Scion WAL/API, Rosalind and legal/robotics pricing; redirect remaining space toward causal methods and clear denominator.
- m05 Avoid absolute or process-style conclusions (`成果ゼロ`, `記事の作法`) when exact accurate formulation is `評価結果未公表`, `未確認`, etc.

## Sol decision: r13 stage boundaries

1. Accept r12 external `REQUEST_CHANGES` and hold publication authority. **M01/M02 and timestamp + citation fixes precede further rendering.**
2. Build a meaningful **source-grounded r13 article-depth expansion** of the seven existing packages (not seven padded essays), with candidate coverage and proof of actual new mechanisms, denominator, failure cases and comparisons; split source access conditions, real original source passages, vendor and independent statements. Scope/Architecture unchanged, else stop for renewed Sol/Human decision.
3. Produce new edition-local r13 proposed complete Drafts and source ledger, without modifying accepted Draft or State. Compile only expressly NONCANONICAL TeX/PDF after textual/source correction and genuine unchanged Core Draft validators pass.
4. Store full compile logs, versioned all-page images and per-page density/content QA, and an easily opened visual review index. Separate auditor must be able to inspect actual pages; binary GitHub text-API failure is a **delivery issue to solve**, not proof visuals passed.
5. Stop at **`SOL_W42_R13_EXTERNAL_INDEPENDENT_REVIEW_READY`** (or earlier concrete BLOCKED), and hand to a **different read-only ChatGPT session** for a new independent audit Prompt. The present Sol editorial manager does not self-certify r13 content or visuals.
6. Do not advance Core `DRAFT_COMPLETE→VALIDATED_DRAFT`, Publication Preview, Freeze, Release, create branch, or modify frozen Core, main, accepted Evidence/Architecture/Draft/Gate/State/checkpoints.

Document status: `R12_EXTERNAL_REVIEW_ADOPTED / R13_MANDATORY_CORRECTIONS_AND_DEPTH_BUILD_AUTHORIZED / NO_PUBLICATION`. This file is a Sol orchestration decision, not a raw independent reviewer reproduction.
