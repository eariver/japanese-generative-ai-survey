# W34 Selection materialization after Sol Evidence Review r1

Status: `EXECUTION_AUTHORITY / SOL_EVIDENCE_REVIEW_PASS / SOL_OWNED_SELECTION_DIRECTIVE / STOP_AT_SOL_SELECTION_REVIEW`

Date: `2026-09-09 JST`

## 1. Mission

Materialize the already-decided Sol Selection r1 into canonical Survey Production Core v2 artifacts on the existing W34 production branch.

This is **not** a new research task and is **not** an invitation for the executor to make editorial Selection decisions.

Normal path:

```text
EVIDENCE_REVIEWED
-> derive current-Core Candidate Matrix
-> exact Sol Selection r1 materialization
-> current-Core Selection validation
-> current-Core stage validation / checkpoint
-> SELECTION_COMPLETE
-> SOL_SELECTION_REVIEW_READY
-> STOP
```

Do not generate Architecture in this execution.

## 2. External exact-start guard

The exact W34 Starting SHA/tree for this request is intentionally supplied by the external Sol handoff prompt, because embedding the request's own eventual commit SHA inside this file would create a self-reference problem.

Before any write, verify read-only:

- remote `weekly/2026-W34-v2-work` HEAD == external Exact Starting SHA;
- remote W34 tree == external Expected Starting Tree;
- remote `main` HEAD == `6d748a962d57beff89da7c1b20cb5a9a86c8e261`.

Mismatch => zero writes and STOP with expected/actual values.

## 3. Mandatory read order

Read before execution:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-sol-luna-review-governance.md`
4. `docs/survey-production-core-v2-authority.md`
5. `sources/2026-W34/execution/reviews/sol-discovery-completeness-review-20260908-r2.md`
6. `sources/2026-W34/execution/reviews/sol-evidence-authority-consumption-review-20260909-r1.md`
7. `sources/2026-W34/execution/reviews/sol-selection-directive-20260909-r1.md`
8. current `config/survey-production-v2.json`
9. current `scripts/survey_stage_validation_v2.py`
10. current `scripts/survey_architecture_v2.py` / `scripts/survey_architecture_v2_base.py`

The Selection directive in item 7 is the semantic authority for every Selection assignment in this execution.

## 4. Executor role

The executor may be Muse Spark 1.3 acting in the Luna/Work execution role.

If Muse Spark 1.3 is used, record:

`Execution agent: Muse Spark 1.3`

`Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION`

The executor owns deterministic materialization, provenance and validation only.

Sol owns the Selection meaning already written in `sol-selection-directive-20260909-r1.md`.

## 5. No upstream rerun

Do not rerun or change:

- Source Intake
- Discovery
- Screening
- Evidence research/retrieval
- Evidence results
- Evidence Authority Supplement
- Edition Views
- Materiality
- Completeness

Use the existing immutable accepted upstream artifacts.

The completed Evidence work contains 409 non-DROP tasks. Do not perform those 409 retrievals again.

The historical Evidence stage checkpoint retains the old execution implementation SHA. Do not rewrite that historical checkpoint merely to replace its implementation identity.

Current Core Selection-stage validation is expected to revalidate the immutable upstream Evidence/View/Materiality/Completeness basis under the current repository implementation before accepting Selection.

If current-Core revalidation fails, stop and report the exact failure. Do not silently regenerate upstream Evidence or edit historical acceptance bytes to make validation pass.

## 6. Canonical Candidate Matrix

Materialize the canonical candidate matrix at:

`sources/2026-W34/candidate-matrix-v2.json`

Use the repository-owned current Core matrix derivation (`survey_architecture_v2.py matrix` or the exact current repository-owned equivalent).

The matrix must be a deterministic derivation from the existing accepted:

- Production Profile
- effective Discovery basis
- Screening acceptance
- Evidence acceptance
- Edition Views acceptance
- Materiality ledger
- Profile Completeness

Expected Matrix candidate count:

`409`

Do not hand-edit the derived Matrix.

If the canonical Matrix path already exists unexpectedly at execution start, do not overwrite it. Report and stop unless the current Core explicitly defines a safe regeneration/revision path applicable to this exact state.

## 7. Exact Sol Selection r1 materialization

Materialize:

`sources/2026-W34/candidate-selection-v2.json`

using exactly:

`sources/2026-W34/execution/reviews/sol-selection-directive-20260909-r1.md`

as the semantic authority.

Before writing Selection, verify the Matrix against the directive:

- exactly 41 Matrix rows have `materiality == MATERIAL`;
- every one of the 41 Discovery identities listed by Sol appears in exactly one Matrix row;
- no additional MATERIAL Matrix row is absent from the directive;
- all 10 Sol PRIMARY identities resolve exactly once;
- all 31 Sol SUPPORTING identities resolve exactly once;
- none of the selected rows has `NEEDS_MORE` or another disallowed Evidence status.

Any discrepancy => STOP. Do not reinterpret Sol's list.

Required Selection summary:

- candidate_count = 409
- SELECTED = 41
- HOLD = 368
- selected_count = 41
- REJECT = 0
- INSPECT = 0

Set a clear non-empty `selection_version`, e.g.:

`w34-sol-selection-r1`

For each assignment, preserve the exact Matrix row `profile_extensions` as required by the Sol directive.

Do not add Human approval fields.

## 8. Selection validation

Run current repository-owned Candidate Selection validation.

Then run the current Core stage validator for the `EVIDENCE_REVIEWED -> SELECTION_COMPLETE` transition using the current repository implementation identity.

This validation is expected to revalidate upstream accepted Evidence and current Core source taxonomy. The exact result must be captured in the new execution area.

Do not claim Sol review from deterministic validation.

## 9. Canonical state transition

Only after:

- Matrix derivation PASS;
- exact directive reconciliation PASS;
- Selection schema/semantic validation PASS;
- current-Core stage validation PASS;

may the canonical Production State advance from:

`EVIDENCE_REVIEWED`

to:

`SELECTION_COMPLETE`.

Use the repository-owned stage/checkpoint mechanism. Do not hand-edit Production State or checkpoint JSON if a canonical Core mechanism exists.

Expected final machine state:

- Discovery = passed
- Screening = passed
- Evidence = passed
- Materiality = passed
- Completeness = passed
- Selection = passed
- Architecture = pending
- lifecycle = `SELECTION_COMPLETE`

## 10. Execution area

Use only:

`sources/2026-W34/execution/luna/w34-selection-after-sol-evidence-r1/`

This path keeps the established execution namespace even if Muse Spark 1.3 is the actual executor.

It must be absent at fresh execution start.

If it already exists, do not invent retry/r2/repair/muse variants. Stop and report the collision.

Recommended contents include:

- `session-worklog.md`
- directive reconciliation report
- current-Core validation result
- final Sol handoff

Do not duplicate the full 409 Evidence corpus into this area.

## 11. Memory discipline

This phase should be much lighter than Evidence, but the executor environment may still have only 8 GB RAM.

- do not load raw Evidence bodies unnecessarily;
- let Core validation resolve content-addressed artifacts as designed;
- avoid copying giant Evidence JSON/body corpora into memory if not required;
- persist validation reports promptly.

## 12. Git discipline

Existing branch only.

Forbidden:

- new branch
- fallback branch
- repair branch
- review branch
- force push
- reset
- rebase
- history rewrite

Before every write phase, read remote W34 HEAD and confirm it remains the expected parent.

Use normal commits and non-force push only.

After each push, fresh remote read-back is mandatory.

A reasonable logical split is:

1. Matrix + exact Selection materialization/validation
2. canonical state/checkpoint + final Sol handoff

Do not create meaningless commits solely to increase checkpoint count.

## 13. Mandatory STOP

Do **not** execute:

- Architecture generation
- Architecture Review Summary
- Architecture Review Attention
- Human Architecture decision
- Drafting
- Publication Preview
- sidecar QA
- PDF build
- freeze
- release

Final marker:

`SOL_SELECTION_REVIEW_READY`

Also record:

`SOL_EVIDENCE_REVIEW_R1_PASS`

`SELECTION_DIRECTIVE_R1_MATERIALIZED`

`CURRENT_CORE_UPSTREAM_REVALIDATION_PASS`

`ARCHITECTURE_NOT_AUTHORIZED`

`SOL_SELECTION_REVIEW_REQUIRED`

## 14. Final handoff

Report at minimum:

- executor identity/mode
- external Starting SHA/tree
- final SHA/tree
- reviewed main SHA
- Matrix path/SHA256 and candidate count
- current-Core upstream revalidation result
- exact MATERIAL reconciliation result
- PRIMARY count = 10
- SUPPORTING count = 31
- Selection disposition counts
- Selection path/SHA256
- Selection validation result
- stage validation result/path/SHA256
- final Production State path/SHA256
- proof lifecycle is `SELECTION_COMPLETE`
- proof Architecture remains pending/not generated
- proof no upstream Evidence retrieval/regeneration occurred
- remote read-back result

Stop after handoff.