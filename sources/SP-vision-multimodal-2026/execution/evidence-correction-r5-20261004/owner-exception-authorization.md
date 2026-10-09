# Owner Exception authorization — materialization (immutable provenance)

Provenance: worker transcription of the explicit Human authorization received via the
operator question channel on 2026-10-04 for the rewind-authorization question in run
`evidence-correction-r5-20261004`. This file transcribes the Human's decision verbatim
to the extent reproduced below; it does NOT create a Human GATE decision record
(no `gates/reviews/*-rN.json`, no approval, no REQUEST_CHANGES/ APPROVED).
It is an Owner Exception authorization for a bounded Core-controlled rewind, recorded
as edition-local immutable provenance. Worker generated no part of the decision.

## Human authorization (verbatim)

"Authorize the Owner Exception rewind.
This authorization is strictly bounded to the current TS-003 targeted Evidence correction run.
Use the Core's own revision/rewind machinery with immutable Owner Exception provenance. Do not hand-edit production state, checkpoints, gate records, or approval records.
Preserve the historical Architecture r4 APPROVED decision as historical provenance only; it must not be reused as approval for regenerated downstream authority.
Re-enter at CANDIDATES_NORMALIZED, consume only the already staged and canonical-validated targeted Evidence corrections plus any strictly necessary deterministic downstream regeneration, then replay Evidence → Materiality/Completeness → Selection → Architecture.
Preserve Discovery/Screening authority, the 112-record scope, the 16-package architecture skeleton, and Frozen Core. Do not modify shared Core implementation.
Do not regenerate Draft, TeX, PDF, Publication Candidate, or advance reader-publication-validation.
Stop at fresh ARCHITECTURE_ESTABLISHED with Human Architecture Review r5 PENDING.
If the Owner Exception rewind cannot satisfy these conditions through Core-controlled machinery, stop as blocked rather than falling back to manual state mutation or a go-forward publication cycle."

## Bounds acknowledged by worker

- Single run only (`evidence-correction-r5-20261004`); single boundary (CANDIDATES_NORMALIZED).
- Core-controlled machinery only: `survey_human_gate_v2._revised_state`,
  `_superseded_paths_for_regeneration`, `_superseded_gate_authority_paths`,
  `survey_production_v2.write_json/refresh_state_control`, `validate_agent_state`.
  No Human-gate decision function invoked (`request_changes` and both `record_*_approval`
  NOT called; no `reviewed_by/reviewed_at` fabricated).
- State/checkpoint/gate/approval bytes changed ONLY as the deterministic output of the
  above Core functions (plus exact-set file deletions computed by Core).
- Fallback contracted: any condition unsatisfiable → stop blocked (no manual mutation,
  no go-forward publication cycle).
