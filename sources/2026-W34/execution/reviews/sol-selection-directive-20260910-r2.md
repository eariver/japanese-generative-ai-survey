# W34 Sol Selection Directive r2 — bounded cluster correction

Status: `SOL_SELECTION_DIRECTIVE_R2 / BOUNDED_CORRECTION / MATERIALIZATION_AUTHORIZED / ARCHITECTURE_NOT_AUTHORIZED`

Date: `2026-09-10 JST`

## Basis

This directive supersedes the cluster assignment portion of:

`sources/2026-W34/execution/reviews/sol-selection-directive-20260909-r1.md`

only as explicitly stated below.

Review authority:

`sources/2026-W34/execution/reviews/sol-selection-review-20260910-r1.md`

The r1 executor correctly materialized the r1 directive. Sol Selection Review r1 found one Sol-owned semantic classification defect.

## Exact authorized delta

Move exactly one selected Discovery identity:

`w34-event-c045` — `OpenAI API regional processing`

from architecture role:

`WEEKLY:retrieval-tool-orchestration`

to architecture role:

`WEEKLY:model-economics-distribution`

Keep:

- `disposition = SELECTED`
- `architecture_usage = SUPPORTING`
- `publication_role = WEEKLY_MAGAZINE:supporting-evidence`
- the exact Matrix `candidate_id`
- `profile_extensions` byte/semantic content derived from the Matrix row

The rationale must identify it as Sol Selection r2 supporting evidence for `WEEKLY:model-economics-distribution` and must not claim retrieval/tool-orchestration significance.

## Everything else remains frozen

No other Selection decision may change.

The r1 exact selected identity set remains 41.

PRIMARY identities remain exactly the same 10.

All other 30 SUPPORTING identities retain their r1 cluster roles.

All 368 non-selected candidates remain HOLD.

No candidate may be promoted, demoted, added, removed, or changed between PRIMARY/SUPPORTING.

## Expected corrected counts

Global:

- candidate_count = 409
- SELECTED = 41
- HOLD = 368
- REJECT = 0
- INSPECT = 0
- PRIMARY = 10
- SUPPORTING = 31

Cluster distribution after correction:

### `WEEKLY:agent-control-plane`
- PRIMARY = 2
- SUPPORTING = 6

### `WEEKLY:collaborative-agent-workflows`
- PRIMARY = 1
- SUPPORTING = 9

### `WEEKLY:retrieval-tool-orchestration`
- PRIMARY = 1
- SUPPORTING = 1

### `WEEKLY:safety-security-governance`
- PRIMARY = 2
- SUPPORTING = 5

### `WEEKLY:model-economics-distribution`
- PRIMARY = 2
- SUPPORTING = 5

### `WEEKLY:creative-multimodal-production`
- PRIMARY = 1
- SUPPORTING = 4

### `WEEKLY:ecosystem-infrastructure-economics`
- PRIMARY = 1
- SUPPORTING = 1

Totals remain 10 PRIMARY + 31 SUPPORTING.

## Upstream freeze

Do not regenerate or modify:

- Discovery
- Screening
- Evidence tasks/results
- Evidence Authority Supplement
- Edition Views
- Materiality
- Completeness
- Candidate Matrix

The current deterministic Candidate Matrix remains the source of candidate identity and profile_extensions.

## Materialization boundary

The correction is Selection-only.

The executor may replace `sources/2026-W34/candidate-selection-v2.json` with the r2 Selection artifact and regenerate only the Selection-stage validation/checkpoint/state/handoff needed to establish a corrected `SELECTION_COMPLETE` surface.

Historical r1 Selection artifacts and execution records must remain preserved as historical provenance where the canonical regeneration rules permit. Do not rewrite historical review records.

Architecture remains unauthorized.

Required stop:

`SOL_SELECTION_REVIEW_R2_READY`

with explicit markers:

- `SOL_SELECTION_R1_REQUEST_CHANGES`
- `SOL_SELECTION_DIRECTIVE_R2_MATERIALIZED`
- `ONLY_C045_CLUSTER_CHANGED`
- `GLOBAL_SELECTION_COUNTS_UNCHANGED`
- `CURRENT_CORE_SELECTION_VALIDATION_PASS`
- `ARCHITECTURE_NOT_AUTHORIZED`
- `SOL_SELECTION_REVIEW_R2_REQUIRED`
