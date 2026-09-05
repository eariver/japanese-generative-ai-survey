# Survey Production Core v2 Pre-Human Evidence Regeneration Repair Validation r1

Date: 2026-09-05

Status: `CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

## Fixed-head scope

- Starting reviewed `main` SHA: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
- W34 exact regression fixture SHA: `df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`
- W34 fixture remote writes: `0`
- `main` writes: `0`
- W34 canonical branch writes: `0`
- Sidecar runs: `0`

This is a shared-Core maintenance candidate. It is not a W34 production-branch
write, a merge, a Human review, or a seven-point final audit.

## Changed paths

The candidate changes the generic Core contract, authority resolution, runners,
tests, and current-facing operational documentation:

- `config/survey-production-v2.json`
- `schemas/operator-pending-gate-invalidation-v2.schema.json`
- `schemas/evidence-authority-supplement-v2.schema.json`
- `schemas/evidence-v2-run-package.schema.json`
- `schemas/evidence-v2-task.schema.json`
- `scripts/survey_human_gate_v2.py`
- `scripts/survey_evidence_v2.py`
- `scripts/survey_agent_control_v2.py`
- `scripts/run_evidence_v2_interactive.py`
- `scripts/run_selection_architecture_v2_interactive.py`
- `scripts/run_drafting_synthesis_v2_interactive.py`
- `scripts/run_semantic_publication_v2_interactive_base.py`
- `scripts/survey_weekly_semantic_publication_v2.py`
- `tests/test_survey_operator_invalidation_v2.py`
- `tests/test_survey_active_evidence_views_v2.py`
- `tests/test_survey_evidence_v2.py`
- `docs/survey-production-core-v2-authority.md`
- `docs/survey-production-core-v2-session-bootstrap.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`
- this validation record

No edition source, accepted historical run, Human review record, or sidecar
repository was changed.

## Design summary

The repair adds three generic Core capabilities while preserving the existing
seven-workflow lifecycle and the two Human Gates:

1. operator-side invalidation of a still-pending Human Gate before its first
   Human presentation;
2. post-Screening Evidence Authority Supplements that bind exact retrieved
   primary-source bytes to existing non-DROP Evidence tasks; and
3. checkpoint-bound active Evidence and Edition View resolution when immutable
   historical accepted runs coexist.

These are authority and regeneration mechanisms, not new lifecycle states,
new Human decisions, or hidden rescreening.

## Pending Human Gate invalidation

`scripts/survey_human_gate_v2.py` implements the operator-only
`invalidate-pending-gate` path. The record schema is
`schemas/operator-pending-gate-invalidation-v2.schema.json`; the repository
record is written under the configured
`execution/operator-invalidations/` directory. The record contains the issue,
gate, contiguous invalidation sequence, exact prior State and Gate-input
paths/SHA-256 values, invalidated commit, expected branch head, regeneration
boundary, reason, operator reference, invalidated checkpoint authority,
superseded canonical paths/SHA values, timestamp, and
`human_decision: false`.

The operation is fail-closed on the target gate and lifecycle, terminal reason,
pending/null Human provenance, agent validation, exact State and Gate-input
bytes at a reachable repository commit, current checkout HEAD, expected work
branch head, review-record count, checkpoint provenance, safe paths, and
deterministic cleanup. The W34 supported boundary is
`ARCHITECTURE_REVIEW -> CANDIDATES_NORMALIZED`. `PUBLICATION_PREVIEW` has no
operator rewind boundary: an active Architecture approval cannot be crossed by
this mechanism.

State is regenerated through the existing Core revision/state derivation logic;
operators do not hand-edit `production-state.json`. Downstream checkpoint
statuses become pending and provenance becomes null. Superseded mutable
canonical singleton artifacts and downstream Stage Checkpoints are recorded
and removed transactionally so the supported runners can regenerate them.

This path creates no Human Review Record, no `REQUEST_CHANGES`, no `APPROVED`,
no Human revision increment, no reviewer identity/time, and no Human feedback.
The Human Review Index remains unchanged. It cannot invalidate an existing
Human approval.

## Cleanup and immutable history

Cleanup is derived from the generic configuration rather than W34-specific
hard-coding. The invalidation record preserves the exact path/SHA set before
supersession. Git history keeps the unpresented Architecture surface
recoverable. Content-addressed accepted Screening, Evidence, Edition View, and
Human-review history remain immutable and are not deleted merely because new
runs exist.

## Evidence Authority Supplement

`schemas/evidence-authority-supplement-v2.schema.json` defines the supplement
manifest. Each entry binds an existing Discovery ID and exact Evidence task ID
to a locator, source class/type, title, publication/access time, repository-local
Raw path, byte count, SHA-256, and rationale. The manifest also binds the exact
issue-local Discovery and Screening acceptance authorities.

`survey_evidence_v2.py` validates repository-relative safe paths, rejects
symlinks and missing files, checks issue/task/Screening identity, source class,
timestamps, byte count, and exact Raw SHA-256. DROP, unknown, duplicate,
cross-issue, and ambiguous bindings fail closed. The package records the exact
manifest path/SHA and task-bound supplement source IDs.

Supplements do not create Discovery events, change Screening decisions, or
permit hidden rescreening. An Evidence Card may cite only the task's original
Discovery source records or explicitly bound supplement source IDs. Interactive
Evidence input must select those IDs explicitly when a task has multiple bound
sources; arbitrary URL invention is rejected. Existing packages without a
supplement retain their prior single-source compatibility behavior.

## Active Evidence and Edition View resolution

`survey_agent_control_v2.resolve_active_evidence_views()` resolves the active
pair only through:

`Production State -> passed Evidence Stage Checkpoint provenance -> exact Stage
Checkpoint -> exact named artifact -> exact path/SHA validation`.

It requires the Edition View to be bound to the exact active Evidence acceptance
SHA and rejects missing, pending, duplicate, cross-run, drifted, or mismatched
artifacts. Selection/Architecture, drafting, semantic publication, and weekly
publication production paths use this resolver. Accepted-directory count,
mtime, lexical order, and digest-order heuristics are not active-authority
selectors. Historical accepted runs therefore remain valid and coexist with a
new active run without ambiguity.

## W34 exact read-only regression

The candidate was applied only in a temporary detached checkout at the exact
W34 fixture SHA. The W34 production branch and remote were not checked out for
write and were not pushed.

### Invalidation

- Gate: `ARCHITECTURE_REVIEW`
- Boundary: `CANDIDATES_NORMALIZED`
- Operation: PASS
- Human records created: `0`
- Human Review Index rows added: `0`
- Human revision/provenance changes: `0` / `null`
- Final invalidation record: `sources/2026-W34/execution/operator-invalidations/architecture-invalidation-0001.json`
- Final lifecycle after the operation: `CANDIDATES_NORMALIZED`
- Discovery and Screening remained passed; Evidence and all downstream
  checkpoints became pending before regeneration.

Old mutable canonical surfaces were superseded through the operator record;
old accepted Screening/Evidence/View runs remained present.

### Supplement and regenerated runs

The W34 supplement is
`sources/2026-W34/execution/luna/w34-core-repair-r1/evidence-authority-supplement.json`.
It contains 61 substantive exact authority-body bindings with 60 unique Raw
body SHA-256 values across 50 tasks. The research ledger retained accounting
for all 80 non-DROP tasks: KEEP 45/45, INSPECT 16/16, MAYBE 19/19, and all 80
verification attempts. Research-only classifications remained VERIFIED 32,
PARTIALLY_VERIFIED 27, UNRESOLVED 14, and OUT_OF_WINDOW 7.

Historical and new accepted runs coexist: 2 Evidence acceptance directories
and 2 Edition View acceptance directories are present in the fixture. The new
active pair is checkpoint-bound to:

- Evidence acceptance:
  `evidence/v2/accepted/5e1aac043af77fa7e2d57ba1379eb14243cf28d18ce7484a8b2954e474c35118/evidence-accepted.json`
- Edition View acceptance:
  `evidence/v2/views/accepted/0b43c8898006ae99b1698de37ec1d8836f13cf97e5aa12b137d4d6cdbc34e7eb/edition-views-accepted.json`

New Evidence results were `VERIFIED 32 / PARTIAL 27 / NEEDS_MORE 14 /
REJECTED 7`, replacing the previous `PARTIAL 80`. New Edition Views were
`CONTEXT 41 / HOLD 31 / NON_MATERIAL 7 / MATERIAL 1`. The regenerated
Materiality ledger was `MATERIAL 1 / CONTEXT 41 / HOLD 31 / NON_MATERIAL 7 /
DUPLICATE 4 / EXCLUDED 26`; Completeness remained `LIMITED` with concrete
authority/chronology/access boundaries. Selection was `SELECTED 1 / HOLD 64 /
INSPECT 15` based on the new Evidence and View authorities. The regenerated
Architecture contains one package titled `Verified developer-tooling change`
with Transformers v5.15.1 as its selected primary candidate; its basis hashes
reference the new Evidence/Materiality/Matrix/Selection outputs and it is not a
reuse of the old Architecture bytes.

The final fixture lifecycle is `ARCHITECTURE_ESTABLISHED`, with
`next_action = ARCHITECTURE_REVIEW`, `terminal_reason = HUMAN_GATE_REACHED`,
Architecture Review pending, Publication Preview pending, and zero Human
decisions. This is the expected first real Human Architecture Review surface.

## Validation results

Targeted new invalidation, supplement, active-authority, Evidence, and related
Core tests passed. The full Python diagnostic suite passed:

`Ran 743 tests in 301.043s — OK (skipped=6)`

The suite also covered existing Human Gate round-trip and Architecture
`REQUEST_CHANGES` behavior, Publication Preview cross-gate protections, agent
control, Stage Checkpoint resolution, Evidence/Card/acceptance, Edition View,
interactive Evidence, Selection/Architecture, stage validation,
Screening-active-acceptance, completeness/materiality, bootstrap/operator, and
downstream publication paths. The only diagnostic warning was the pre-existing
`SyntaxWarning` in untouched
`scripts/normalize_special_legacy_partial_enums.py`.

The candidate preserves the seven workflows and two Human Gates. No Human
review record was created, no sidecar was run, and no seven-point audit was
performed.

## Remaining limitations and stop state

- Human Architecture Review is still pending and must be performed by a Human;
  no Human decision is inferred here.
- Publication Preview remains pending and cannot be crossed by operator
  invalidation.
- The completeness boundary remains `LIMITED` for candidate-local unresolved
  authority, chronology, access, or out-of-window reasons; it is not a result of
  skipped investigation.
- Historical accepted runs are retained as immutable history and are not
  treated as active when the State-bound checkpoint names a newer run.
- External Publication Boundary Validator and Survey Core v2 Authority Auditor
  sidecars remain intentionally unexecuted.

Final branch SHA, branch ahead/behind counts, and the exact reviewed repository
commit SHA are reported after this validation record and the implementation
are committed and pushed to the maintenance branch.
