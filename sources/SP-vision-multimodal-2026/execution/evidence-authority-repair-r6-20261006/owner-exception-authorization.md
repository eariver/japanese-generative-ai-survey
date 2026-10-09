# Owner Exception authorization — materialization (immutable provenance)

Provenance: worker transcription of the explicit Human Owner authorization
supplied IN THIS RUN's task message (§0, "HUMAN OWNER AUTHORIZATION — BOUNDED
OWNER EXCEPTION") for run `evidence-authority-repair-r6-20261006`. This file
transcribes the Human's bounds; it does NOT create a Human GATE decision record
(no `gates/reviews/*-rN.json`, no approval, no REQUEST_CHANGES/APPROVED).
It is an Owner Exception authorization for a bounded Core-controlled rewind,
recorded as edition-local immutable provenance. Worker generated no part of
the decision.

## Human authorization (bounds, transcribed)

- Bounded Owner-Exception rewind from DRAFT_COMPLETE to the minimum Core-v2
  re-entry boundary required to correct confirmed canonical Evidence defects.
- Authorized defect scope: VM-D023 LayoutLM, VM-D039 CLIP, VM-D116 π₀, and only
  directly dependent regenerated artifacts.
- Reason: factual/provenance defects inside canonical Evidence itself; patching
  only the Draft would leave the authority chain internally incorrect.
- Does NOT permit: new Discovery, new candidate intake, new external research
  lane, V-JEPA Policy intake, shared Core modification, manual
  lifecycle/checkpoint editing, destructive history rewrite, fabrication or
  carry-forward of a Human gate decision, TeX/PDF/publication work.

## Bounds acknowledged by worker

- Single run only (`evidence-authority-repair-r6-20261006`); single boundary
  (CANDIDATES_NORMALIZED, preferred minimum re-entry).
- Fail-closed probes of formal Core mechanisms first (recorded in
  `reentry-probes-r6.md`); on confirmed absence, consume this run-specific
  Owner Exception.
- Core-controlled machinery only: `survey_human_gate_v2._revised_state`,
  `_superseded_paths_for_regeneration`, `_superseded_gate_authority_paths`,
  `survey_production_v2.write_json`, `survey_agent_control_v2` advance/checkpoint
  machinery, `validate_agent_state`. No Human-gate decision function invoked
  (`request_changes`, `record_architecture_approval`,
  `record_publication_preview_approval` NOT called; no `reviewed_by/reviewed_at`
  fabricated).
- State/checkpoint/gate/approval bytes changed ONLY as deterministic output of
  the above Core functions (plus exact-set file deletions computed by Core).
- r5 APPROVED review/approval records preserved as immutable HISTORY only;
  never reused as approval for regenerated authority. After replay the fresh
  Architecture is PROPOSED with Human Architecture Review r6 PENDING; no r6
  decision created.
- Fallback contracted: any condition unsatisfiable → stop blocked (no manual
  mutation, no go-forward publication cycle, no Draft regeneration).
