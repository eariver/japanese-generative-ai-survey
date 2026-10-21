# W42 Muse r9 — Materialize Sol-reviewed Selection, build seven-package Architecture, stop for independent Sol audit

Status: **`EXECUTION_AUTHORITY / SOL_SELECTION_SCOPE_DECIDED / FROZEN_CORE_NO_CHANGES / STOP_AT_SOL_ARCHITECTURE_AUDIT`**
Date: 2026-10-17 JST
Repo: `eariver/japanese-generative-ai-survey`
Existing branch: `weekly/2026-W42-v2-work`.

## 1. Preflight — exact reviewed authority

Sol dispatch supplies current W42 exact remote Starting HEAD and Tree. Verify BOTH read-only; also:
- Reviewed `main` HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`.
- Frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
If any mismatch: **ZERO WRITES** and report expected/actual. Do not create any new branch, fallback, review/repair branch. Do not rebase, reset, force-push, rewrite history, or change shared `scripts/`, `schemas/`, `config/`, `.github/`, Frozen Core or main.

Read before work:
1. `sources/2026-W42/execution/reviews/sol-w42-r8-evidence-materiality-selection-semantic-review-20261017.md` **in full** — authoritative 28 selected material candidates, 22 non-selected, precise seven-package thesis and 27–30-page approach.
2. `sources/2026-W42/execution/SOL_MATERIALITY_SELECTION_REVIEW_HANDOFF-r8.md`; `sources/2026-W42/production-state.json`, `orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json`; canonical 50-row Discovery/Screening/Evidence/Edition Views/Materiality/Completeness; r8 `selection-proposal-r8.PROPOSED.md` **only as non-binding background**.
3. Sol governance `docs/survey-production-core-v2-sol-luna-review-governance.md` §§4–8; frozen Candidate Matrix/Selection/Architecture and Architecture Review Attention schemas/validators, stage validator; W41 reviewed Architecture precedent for mechanics, NOT content.
4. `docs/core-v2-deferred-maintenance-summary.md` (DM-016/DM-020/DM-022/DM-023) and Issues #568/#569. Human Owner has forbidden shared Core changes.

## 2. Authentic Core State and accepted artifacts (DO NOT rewrite)

Current authoritative lifecycle must be `EVIDENCE_REVIEWED`; passed Discovery/Screening/Evidence/Materiality/Completeness, pending Selection and Architecture. Actual accepted sets:
- Evidence 50 cards: 43 PARTIAL + 7 NEEDS_MORE + **zero VERIFIED**; SHA-bounded root `f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7`.
- Edition Views 50: `4296ffd0bd9864ea764a95fa7c0eea8d7384ca4d7a0336db0fa99359148e384a`.
- Materiality Ledger 50 = 28 MATERIAL, 14 CONTEXT, 7 HOLD, 1 non-material X receipt; Completeness LIMITED.
- Keep exact production State and stage receipts until **lawful** next Core-validated transition. No r7/r8 proposed JSON can override accepted SHA-bound artifacts. Do not re-run Evidence acceptance or rewrite generated results in place.
- W42 Grok/X ledger is a truthful non-editorial provenance binder, **NEVER an article**, but has an accepted Evidence task/View and must have a valid non-selected candidate assignment.

## 3. Selection assignments — Sol already owns decisions

Use the **exact 28 unique MATERIAL candidate IDs** and per-package PRIMARY/SUPPORTING roles in Sol r8 §3. Count must be 28 SELECTED = 16 PRIMARY + 12 SUPPORTING. The non-selected §4 **14 CONTEXT** map to 5 INSPECT (Fish, Claude perf, LeChonk, NVIDIA OCP, OpenAI EU agents) plus 9 REJECT; **7 HOLD** remain HOLD; 1 Grok receipt REJECT. Therefore candidate matrix/selection assignments must cover **exactly 50 unique IDs**, dispositions `SELECTED 28 / INSPECT 5 / HOLD 7 / REJECT 10`. One-to-one candidate placement, no discretionary moving a MATERIAL item to another package, no unreviewed additions.

Semantically specific rationale for EVERY one of 50, not mechanical `KEEP, 3 claims`. For SELECTED specify technical novelty, date boundary, strongest actual first-party authority, vendor-vs-independent caveat, and package role. For INSPECT/HOLD/REJECT state concrete non-selection reason; do not conflate an out-of-window paper's old results with a W42 launch.

Build the Candidate Matrix using frozen `survey_architecture_v2(_base).derive_candidate_matrix` or genuine contract-equivalent reviewed path; build formal Candidate Selection (status `ESTABLISHED`, correct role namespaces and exact SHA bases); execute original Core `validate_candidate_matrix`, `validate_selection` and `stage_validation` with real receipt and normal agent-first bridge. Complete `EVIDENCE_REVIEWED → SELECTION_COMPLETE` ONLY if authentic PASS. Do not label the r8 executor sketch Sol-approved.

## 4. Seven-package Architecture from Sol's explicit design

Use Sol r8 §3 as the editorial design authority. Proposed package titles/roles (Japanese final titles may improve):

- P1 frontier agent systems (Wonder and Argon): 4.0 pages.
- P2 accelerator hardware and inference efficiency (Maia 300 + LFM2.5): 2.5 pages. **Maia must not disappear again.**
- P3 open weights, usage conditions and model tradeoffs (Spark, Beam, Nemotron + Granite, MiniCPM, FLUX): 5 pages.
- P4 engineering/coding agent operations (Codex, Scion, HydraFusion + AutoFix, AI Scan, Decider): 4 pages. **Scion must have explicit placement.**
- P5 model safety and external assessment (Anthropic unintended, distillation + ECDSA, METR): 3 pages.
- P6 science and experimental agency (wet-lab, Earth AI, Deep Review + two Rosalind entries): 4.5 pages.
- P7 specialized/embodied systems (GLM-Legal, ASPIRE + Glimpse): 3.5 pages. **Glimpse must have explicit placement.**

Total body ~26.5 pages, with opening/methodology/sources 1–2 pages. Target **~27–30 pages**, not an artificial hard cap; respect exact Core page/profile contracts. Only truthful source-supported narrative counts as depth; do not expand via padding, filler tables, empty-pages, or an unsupported theme. If validation necessitates a different shape, STOP and report; do not silently replace Sol-approved editorial choices.

Each package requires: central question/technical thesis, exact PRIMARY vs SUPPORTING IDs, source authority map, timeline distinction, target technical depth (mechanism, architecture, benchmark methodology, denominator/baseline, negative result), model/license restrictions, vendor claims vs independent measurements, cross-package interactions without redundant full coverage, omissions and clear reader takeaway. At least one nontrivial methodological/architecture comparison where source-supported. Treat open-source software, openly distributed weights and OSI-approved license **as separate claims**.

## 5. Content provenance fix without rewriting accepted Core

The 91 `supplement-r8` items are **derived, bounded short notes**, not original captured webpage/PDF/LICENSE byte archives. Never describe them as 91 original full-text archival captures. R6 prior work claimed full PDF reads, but its original full bytes aren't retained in r8 for independent review. Include this distinction in Architecture limitation dossier and Human review summary; no invented re-execution or full-text guarantee.

The accepted r8 Evidence cards often attach **all task-bound sources** to each individual claim and have generic unresolved verification targets. Their formal schema acceptance **does not prove each source supports each claim**. Create an **edition-local, non-authoritative claim-to-best-specific-source crosswalk** for all selected/high-risk quantitative or license assertions: candidate_id, actual claim excerpt, direct exact URL (not `primary:` locator shorthand), source category, article usage/caveat, internal derivation file, unresolved denominator/method notes. Use genuine primary primary-body/context link, independent evaluation if genuinely independent, else label vendor; do not silently promote X as first-party experimental benchmark. Never mutate already accepted Evidence/Card/View/Materiality SHA-bound records (DM-022).

For a critical factual claim lacking suitable source evidence, mark `NON_PROMOTABLE` in the crosswalk and **omit/downgrade the claim in Architecture**. If omitting a claim would change a selected candidate's materiality/role, stop and refer to Sol; no hidden substitute event. If first-party body remains accessible, verify/consume exact passage, but keep a real source-read note with precise date; no fake raw original bytes. Crosswalk belongs to edition editorial interpretation only and cannot be used to rewrite formal Core Evidence silently. Explicitly review original license files and full paper method pages when available for lead article critical claims.

## 6. Core-validated Architecture and Sol stop

After real Selection stage success, Muse may materialize Architecture proposal faithfully implementing the reviewed Sol design and build the Core `issue-architecture`, `architecture-review-summary`, `architecture-review-attention` with correct exact hashes. Run original frozen validators and issue-/profile-specific QA. If all real gates PASS, a machine transition `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED` is allowed **without recording Human approval**; otherwise stop at exact failure, preserving current stage.

Required terminal **`SOL_ARCHITECTURE_AUDIT_READY`**. The executor must NOT request or synthesize Human `ARCHITECTURE_REVIEW APPROVED`, must NOT advance drafting, TeX, PDF, Publication Preview, Freeze or Release. Sol will independently inspect research consumption, candidate omissions, package assignments, page allocation, alternative framing and technical claims and then present the full Human Architecture Review dossier.

Audit deliverables: actual latest HEAD/Tree, unchanged Core/main and accepted upstream identities, full 50 candidate assignment crosswalk, selected packages with page counts, technical authority crosswalk, W42 completeness limitations/uncertain claims, machine stage receipt IDs and exact validation PASS/fail logs, seven-package source+quality mapping. Explicitly report any discrepancies from Sol's 28 selected and 7 packages; these deviations are NOT preauthorized.

No new branches. Normal commits, non-force push on the existing work branch only.
