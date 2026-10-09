# TS-003 Muse execution — minimal Evidence semantic-fidelity repair after Sol r2

Status:

`EXECUTION_AUTHORITY / EVIDENCE_R2_REQUEST_CHANGES / MINIMAL_EVIDENCE_REPAIR_ONLY / STOP_FOR_SOL_R3`

Date: `2026-09-30 JST`

Issue:

`SP-vision-multimodal-2026`

Branch:

`special/vision-multimodal-2026-work`

## 0. Guard authority and precedence

Do not use a work-branch SHA/tree hardcoded inside this file.

The exact work-branch HEAD/tree supplied in the Sol launch message are the sole work-branch start guard for this execution.

Before any write, read-only verify the launch-message values for:

- remote work branch HEAD/tree;
- remote main HEAD/tree;
- remote `production/survey-core-v2` HEAD/tree.

Also verify canonical edition state:

- issue = `SP-vision-multimodal-2026`;
- lifecycle = `CANDIDATES_NORMALIZED`;
- discovery checkpoint = `passed`;
- screening checkpoint = `passed`;
- evidence checkpoint = `pending`;
- materiality/completeness/selection/architecture = `pending`;
- Human Architecture Review = `pending`;
- Human Publication Preview = `pending`.

If any guard differs, perform zero writes, report expected vs actual, and stop.

No new/fallback/repair/review/iteration branch. No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

## 1. Mandatory authorities

Read in this order:

1. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r2.md`
2. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r1.md`
3. `sources/SP-vision-multimodal-2026/execution/evidence-semantic-repair-r1-20260930/repair-report-r1-to-r2.md`
4. r2 accepted Evidence manifest under `sources/SP-vision-multimodal-2026/evidence/v2/accepted/3f6be211.../evidence-accepted.json`
5. r2 accepted Edition Views under `sources/SP-vision-multimodal-2026/evidence/v2/views/accepted/73c06689.../`
6. current `production-state.json`
7. current Screening acceptance + same canonical Evidence task package
8. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-020

Sol r2 review is authoritative over worker repair reports and semantic check summaries.

## 2. Mission

Perform only the minimal r2→r3 semantic-fidelity repair required by Sol r2.

Do not rerun research broadly. Do not rerun Discovery or Screening. Do not change task selection.

Repair two defect classes only:

### A. Supplemental HF/API claim binding

Audit VM-D074, VM-D075 and VM-D077.

Their r2 Cards contain HF release/API-derived facts while their canonical source arrays bind only GitHub repository roots.

For each affected fact:

- if the current canonical Evidence/task authority can legitimately admit the exact supplemental HF/API authority as a source without changing Discovery/Screening, add the exact source and bind claims to its source_id through the canonical machinery;
- otherwise remove that supplemental fact from the canonical Card and retain it only in an execution/audit note as non-canonical supplemental observation.

Never cite the repository source_id for a fact that was actually established only from HF/API.

Do not weaken or remove genuinely repository-supported deployment facts.

Preserve honest uncertainty. D077 remains PARTIAL unless its original unresolved condition is genuinely resolved by canonical authority.

### B. VM-D101 stale term-origin semantics

Repair VM-D101 Card and View so the canonical r3 surfaces contain no positive term-origin or terminology-inheritance claim.

Remove/replace all stale semantics including:

- `term-origin content consumed`;
- `Terminological origin ... recorded`;
- `d14-term-origin`;
- positive `terminology inherited` wording.

Retain only the source-safe edition synthesis:

- 2018 Ha & Schmidhuber as a major historical neural-world-model / dream-training formulation anchor for this edition;
- Dreamer = latent-dynamics/model-based-decision branch;
- JEPA/V-JEPA = predictive-representation branch;
- Genie = interactive-generative branch;
- no direct ancestry assertion among branches without explicit authority;
- no claim about broad origin/inheritance of the term `world model`.

Use a schema-valid non-origin transition annotation if one exists; otherwise omit that transition annotation rather than inventing an invalid value.

## 3. Append-only artifact contract

Preserve r1 and r2 accepted Evidence and Views exactly.

Build a **new append-only r3** Evidence result set and corresponding r3 Views from the same canonical task package.

Do not overwrite any accepted directory.

Produce at minimum:

- r3 Evidence input;
- new r3 Evidence acceptance;
- new r3 Edition Views acceptance;
- r2→r3 repair report;
- r3 semantic/source-binding audit;
- r3 coverage/validation summary.

The repair report must state exactly which records changed and why.

## 4. Required r3 semantic checks

Fail closed unless all pass:

1. 111/111 canonical tasks are still represented.
2. r1 and r2 accepted directories are byte-unchanged.
3. No canonical r3 claim or verification finding mentions an external HF/API/repo/vendor authority unless that actual authority is represented by a valid bound source_id for that Card.
4. Specifically audit every occurrence of `HF`, `Hugging Face`, `release API`, `release tag`, `license:`, and external SHA/date license binding in r3 claims/verification text.
5. D101 canonical Card/View contain none of: `Terminological origin`, `term-origin content`, `d14-term-origin`, or an affirmative terminology-inheritance claim.
6. D101 lineage is branch-separated and does not assert unsupported ancestry.
7. `PRIMARY_FACT` synthesis does not reappear.
8. G01–G06 are not silently closed.
9. VERIFIED/PARTIAL statuses remain evidence-driven; no count optimization.
10. canonical Production State remains unchanged at `CANDIDATES_NORMALIZED`.
11. Materiality Ledger, Profile Completeness, Selection, Architecture and Human Gate artifacts are not created.
12. main and Production Core remain unchanged.

## 5. Stop condition

Normal completion state:

`TS-003 EVIDENCE_SEMANTIC_REPAIR_R2_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R3`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`

Stop there. Do not proceed into the next pipeline stage.
