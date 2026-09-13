# W34 Selection r2 bounded correction execution request

Status: `EXECUTION_AUTHORITY / SOL_SELECTION_R1_REQUEST_CHANGES / ONE_CLUSTER_REASSIGNMENT / STOP_AT_SOL_SELECTION_REVIEW_R2`

Date: `2026-09-10 JST`

## Mission

Materialize the Sol Selection r2 bounded correction after Sol Selection Review r1 found exactly one semantic cluster misclassification in the Sol-owned r1 directive.

This is not a new Selection exercise.

The executor must make exactly one semantic assignment change:

`w34-event-c045` / `OpenAI API regional processing`

from:

`WEEKLY:retrieval-tool-orchestration`

to:

`WEEKLY:model-economics-distribution`

and then revalidate the Selection stage under current reviewed Core.

Architecture remains unauthorized.

## Mandatory authority read order

Read before writing:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-sol-luna-review-governance.md`
4. `docs/survey-production-core-v2-authority.md`
5. `docs/survey-production-core-v2-issue-prevention-checklist.md`
6. `sources/2026-W34/execution/reviews/sol-selection-review-20260910-r1.md`
7. `sources/2026-W34/execution/reviews/sol-selection-directive-20260910-r2.md`
8. prior r1 directive and r1 Muse handoff for historical comparison only.

## External guards

Exact Starting SHA / Expected Starting Tree / Reviewed main SHA are supplied by the outer execution prompt so this request does not self-reference its own commit.

Before any write, verify read-only:

- remote W34 branch HEAD == externally supplied Exact Starting SHA
- remote W34 branch tree == externally supplied Expected Starting Tree
- remote main HEAD == externally supplied Reviewed main SHA

On any mismatch: zero writes, report expected vs actual, stop.

## Authorized write scope

Canonical Selection/state paths that may be updated:

- `sources/2026-W34/candidate-selection-v2.json`
- `sources/2026-W34/orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json`
- `sources/2026-W34/production-state.json`

New execution records may be created only under:

`sources/2026-W34/execution/luna/w34-selection-c045-cluster-correction-r2/`

This directory must be absent at start. If it already exists, stop and do not invent an alternate directory.

Do not modify Candidate Matrix or any upstream research artifact.

## Frozen upstream

No writes to:

- Discovery
- Screening
- Evidence tasks/results
- Evidence Authority Supplement
- Edition Views
- Materiality
- Completeness
- `sources/2026-W34/candidate-matrix-v2.json`

No re-research and no new web/source retrieval.

## Exact Selection delta

Find the existing Selection assignment whose Matrix row contains discovery identity:

`w34-event-c045`

Verify Matrix title is:

`OpenAI API regional processing`

Verify before editing:

- current disposition = `SELECTED`
- current architecture_usage = `SUPPORTING`
- current publication_role = `WEEKLY_MAGAZINE:supporting-evidence`
- current architecture_role = `WEEKLY:retrieval-tool-orchestration`
- Matrix materiality = `MATERIAL`
- Matrix evidence_status is not `NEEDS_MORE` or `REJECTED`

Then change only Selection semantics for that assignment:

- `architecture_role = WEEKLY:model-economics-distribution`
- rationale updated to identify Sol Selection r2 supporting evidence for `WEEKLY:model-economics-distribution`

Preserve its Matrix-derived `profile_extensions` exactly.

Do not change candidate_id, disposition, architecture_usage, publication_role, or any other candidate assignment.

## Exact invariant comparison

Before writing and again after materialization, compare r1 vs proposed r2 Selection.

Required:

- candidate count unchanged: 409
- selected identity set unchanged: 41
- HOLD identity set unchanged: 368
- PRIMARY identity set unchanged: 10
- SUPPORTING identity set unchanged: 31
- only one assignment has changed semantic fields
- changed assignment is exactly the candidate mapped from `w34-event-c045`
- changed fields are limited to `rationale` and `architecture_role`
- all `profile_extensions` are byte/structurally identical to r1 and Matrix rows
- no other assignment changes

Corrected cluster totals:

- agent-control-plane: PRIMARY 2 / SUPPORTING 6
- collaborative-agent-workflows: PRIMARY 1 / SUPPORTING 9
- retrieval-tool-orchestration: PRIMARY 1 / SUPPORTING 1
- safety-security-governance: PRIMARY 2 / SUPPORTING 5
- model-economics-distribution: PRIMARY 2 / SUPPORTING 5
- creative-multimodal-production: PRIMARY 1 / SUPPORTING 4
- ecosystem-infrastructure-economics: PRIMARY 1 / SUPPORTING 1

Global totals remain PRIMARY 10 / SUPPORTING 31 / SELECTED 41 / HOLD 368.

## Validation

Run current-Core Selection validation and stage-contract validation using the corrected Selection.

The validator must revalidate the immutable upstream basis under the current reviewed implementation.

Do not rewrite historical Evidence checkpoint implementation identity.

Record validation outputs under the authorized r2 execution directory.

If the Selection validator or stage validator requires an upstream research artifact change, stop and report the exact failure rather than changing upstream.

## State transition semantics

This correction does not conceptually advance beyond Selection.

Final canonical state remains:

`SELECTION_COMPLETE`

with:

- Discovery passed
- Screening passed
- Evidence passed
- Materiality passed
- Completeness passed
- Selection passed
- Architecture pending
- Draft/Validation/Publication Preview/Freeze/Release pending
- Human Architecture Review pending
- next action may remain architecture, but Architecture must not be executed.

## Required execution records

Under:

`sources/2026-W34/execution/luna/w34-selection-c045-cluster-correction-r2/`

create bounded records sufficient to prove:

- start guards
- exact r1 -> r2 diff
- corrected cluster counts
- current-Core Selection validation PASS
- current-Core stage validation/checkpoint PASS
- final remote read-back
- executor identity

Executor identity for this run:

`Execution agent: Muse Spark 1.3`

`Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION`

## Commit discipline

Use the existing W34 branch only.

No new/fallback/repair/review branch.

No force push, reset, rebase, history rewrite or revert-based workaround.

Prefer two logical commits if practical:

1. corrected Selection + bounded reconciliation/validation records
2. canonical checkpoint/state + final handoff

Before every push, fresh-read remote HEAD and require it to equal the exact expected parent for that write.

Use normal non-force forward push only and read back the remote after each push.

## Mandatory stop

Stop after corrected Selection is established and validated.

Do not execute:

- Architecture
- Architecture Review Summary
- Architecture Review Attention
- Drafting
- Publication Preview
- sidecar QA
- PDF
- freeze
- release

Final handoff must include:

- `SOL_SELECTION_R1_REQUEST_CHANGES`
- `SOL_SELECTION_DIRECTIVE_R2_MATERIALIZED`
- `ONLY_C045_CLUSTER_CHANGED`
- `GLOBAL_SELECTION_COUNTS_UNCHANGED`
- `CURRENT_CORE_SELECTION_VALIDATION_PASS`
- `ARCHITECTURE_NOT_AUTHORIZED`
- `SOL_SELECTION_REVIEW_R2_REQUIRED`
- `SOL_SELECTION_REVIEW_R2_READY`

STOP.
