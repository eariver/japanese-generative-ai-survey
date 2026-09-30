# TS-003 Muse execution — Evidence semantic micro-repair after Sol r3

Status:

`EXECUTION_AUTHORITY / EVIDENCE_R3_REQUEST_CHANGES / MICRO_REPAIR_ONLY / STOP_FOR_SOL_R4`

Date: `2026-09-30 JST`

Issue:

`SP-vision-multimodal-2026`

Branch:

`special/vision-multimodal-2026-work`

## 0. Guard authority

Do not use a work-branch SHA/tree hardcoded inside this file.

The exact work-branch HEAD/tree supplied in the Sol launch message are the sole work-branch start guard.

Before any write, read-only verify:

- remote work branch HEAD/tree against the launch message;
- remote main HEAD/tree;
- remote `production/survey-core-v2` HEAD/tree;
- issue = `SP-vision-multimodal-2026`;
- lifecycle = `CANDIDATES_NORMALIZED`;
- discovery checkpoint = `passed`;
- screening checkpoint = `passed`;
- evidence checkpoint = `pending`;
- materiality/completeness/selection/architecture = `pending`;
- Human Architecture Review and Publication Preview = `pending`.

If any guard differs, perform zero writes and report expected vs actual.

No new/fallback/repair/review/iteration branch. No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

## 1. Mandatory authority

Read and obey:

1. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r3.md`
2. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r2.md`
3. `sources/SP-vision-multimodal-2026/execution/evidence-semantic-repair-r2-20260930/repair-report-r2-to-r3.md`
4. r3 accepted Evidence under `sources/SP-vision-multimodal-2026/evidence/v2/accepted/c6763f1c.../`
5. r3 Views under `sources/SP-vision-multimodal-2026/evidence/v2/views/accepted/fc8556a3.../`
6. current `production-state.json`
7. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-020.

Sol r3 review is authoritative over worker summaries.

## 2. Mission

Perform only the micro-repair required by Sol r3.

The substantive HF/API-derived facts were already removed correctly in r3. Do not reintroduce them and do not attempt new supplemental-source admission.

Repair only canonical wording in VM-D074, VM-D075 and VM-D077 so no canonical claim/limitation/context/verification text names an unbound external HF/API authority.

### VM-D074

Preserve:

- repository-supported deployment claims;
- repo-root LICENSE-supported Apache 2.0 code-license claim;
- unresolved model-weight license.

Remove canonical wording that mentions Hugging Face/HF/release surfaces/audit-note provenance.

A safe semantic form is equivalent to:

`Model-weight license remains unresolved in canonical Evidence.`

### VM-D075

Preserve:

- repository-supported deployment/thinker-only claims;
- unresolved model-weight/code license.

Remove canonical wording that names Hugging Face/HF/release API/audit-note provenance.

### VM-D077

Preserve:

- repository-supported pipeline/open-stack scope;
- repo-root LICENSE-supported Apache 2.0 code-license claim;
- unresolved model-weight license;
- unresolved released-data/per-dataset licensing and third-party mixture constraints;
- PARTIAL status.

Remove canonical wording that names Hugging Face/HF/release API/audit-note provenance.

Do not alter unrelated records merely for style.

VM-D101 is semantically accepted at r3. Preserve its historical-formulation-anchor and branch-separated lineage. Do not regress to any term-origin framing.

## 3. Append-only r4

Preserve r1, r2 and r3 accepted Evidence/Views as immutable history.

Generate a new append-only r4 Evidence acceptance and r4 Views acceptance from the same canonical task package.

Produce at minimum:

- r4 Evidence input;
- r4 accepted Evidence set;
- r4 accepted Edition Views set;
- r3→r4 micro-repair report;
- r4 validation/coverage summary.

The report must identify exactly which records changed.

## 4. Fail-closed checks

Before completion verify:

- 111/111 tasks remain represented;
- r1/r2/r3 accepted directories remain unchanged;
- VM-D074/D075/D077 canonical Card text contains none of: `HF`, `Hugging Face`, `release API`, `release tag` as reference to an unbound external source;
- unresolved license/data semantics remain explicit;
- VM-D101 remains free of term-origin/inheritance assertions and uses the accepted formulation-anchor semantics;
- `PRIMARY_FACT` synthesis remains absent;
- G01–G06 remain preserved unless already-bound authority genuinely resolves one without new research;
- VERIFIED/PARTIAL statuses remain evidence-driven;
- lifecycle remains `CANDIDATES_NORMALIZED`;
- no Materiality/Completeness/Selection/Architecture/Human Gate artifacts are created;
- main and frozen Production Core remain unchanged.

## 5. Prohibited

Do not:

- rerun Discovery;
- rerun/alter Screening;
- change the task set;
- perform new research;
- build Materiality Ledger or Profile Completeness;
- run Selection or Architecture;
- make Human decisions;
- modify main or Production Core.

Normal commit + non-force push only.

## 6. Stop

Normal completion state:

`TS-003 EVIDENCE_SEMANTIC_MICRO_REPAIR_R3_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R4`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`

Stop there.
