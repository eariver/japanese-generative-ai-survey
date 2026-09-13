# Shared-Core defect record — revalidation pointer vs Human-gate revision (no Core edit on edition branch)

Date: 2026-09-13 JST
Found during: W34 Publication Preview Human REQUEST_CHANGES r1 recording (boundary `DRAFT_COMPLETE`, publication-local)

## Observation

`survey_human_gate_v2._revised_state()` validates the rolled-back state via
`validate_agent_state()`, which consults an active `publication_revalidation_provenance`
pointer. The canonical revision itself deletes that pointer's basis (the old
`DRAFT_COMPLETE` validation checkpoint), so a revision recorded while the pointer
is still set fails closed inside `_revised_state` with a stale-basis error.

`_revised_state()` predates the pointer key (introduced by Core PR #489) and has
no branch that clears publication-revalidation authority when the validation
checkpoint is invalidated.

## Empirical proof (both paths fail, zero side effects) — see above.

## Edition-side handling (this branch only)

With pointer removed (manual single-key deletion as revision consequence):
`verify_agent_state_basis` at `request_changes` entry fails with the 5
pre-regeneration drift errors (publication-pdf, quality-regression-bundle,
reader-manuscript, semantic-review, visual-review).

With pointer intact:
`_revised_state` fails with `refusing inconsistent Human Gate revision State:
publication revalidation does not bind the active validation checkpoint`,
because the rollback nulls `checkpoint_provenance.validation` while the
pointer still references the deleted-basis checkpoint.

Neither path writes anything (both raise before record/deletion/state writes;
verified via clean tree afterward).

Final disposition on this branch: the exploratory pointer removal was reverted;
production-state.json is byte-identical to the reviewed HEAD and the pointer
remains set (state validates PASS). No shared-Core code was modified on this
edition branch. Awaiting either a reviewed Core repair of `_revised_state` or
explicit Sol authorization of an alternate boundary/procedure.

## Required shared-Core repair (separate maintenance)

`_revised_state()` (or the revision preflight) should clear
`publication_revalidation_provenance` exactly when the revision invalidates the
referenced validation checkpoint, instead of failing on the orphaned pointer.

Markers: `SHARED_CORE_DEFECT_RECORDED_FOR_SEPARATE_REPAIR`.
