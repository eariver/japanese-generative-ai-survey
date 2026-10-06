# Owner Exception authorization — materialization (immutable provenance)

Provenance: worker transcription of the explicit Human Owner authorization
supplied IN THIS RUN's task message (§0, "HUMAN OWNER DECISION AND AUTHORIZATION"
+ §2 "BOUNDED RE-ENTRY AUTHORIZATION") for run
`r6-final-authority-correction-20261006`. This file transcribes the Human's
bounds; it does NOT create a Human GATE decision record (no
`gates/reviews/*-rN.json`, no approval, no REQUEST_CHANGES/APPROVED). It is an
Owner Exception authorization for a bounded Core-controlled rewind, recorded as
edition-local immutable provenance. Worker generated no part of the decision.

## Human authorization (bounds, transcribed)

- Bounded Owner-Exception rewind from ARCHITECTURE_ESTABLISHED (r6 PENDING) to
  the minimum Core-v2 re-entry boundary required to correct confirmed canonical
  authority defects (CANDIDATES_NORMALIZED, preferred minimum re-entry).
- Authorized defect scope:
  A. VM-D038 / VQA-v2 attribution: bind Goyal et al. arXiv:1612.00837 as
     additional primary source to the EXISTING VM-D038 candidate (source
     enrichment, NOT new Discovery/candidate/materiality node; NO VQA-CP);
     remove `training contamination` wording; replace with language-prior /
     answer-prior / dataset-bias + complementary-image-pair semantics
     (same question + similar/complementary images + different answers).
  B. measurement-provenance taxonomy: three-way AUTHOR_DEVELOPER_SELF_REPORTED /
     PROVIDER_VENDOR_REPORTED / INDEPENDENT_THIRD_PARTY; targeted corrections to
     VM-D065, VM-D066, VM-D070, VM-D071 (+ VM-D038); preserve VM-D072/VM-D073/
     VM-D112 as provider/vendor; preserve VM-D074-D077 project roles; G05 →
     first-party reproduction gap; P09 + P15 provenance-contract refinement
     (map key rename only if safe, else keep legacy key with corrected labels).
  C. Only directly dependent regenerated artifacts (Evidence acceptance →
     Edition Views → Materiality → Completeness → Candidate Matrix → Selection
     → Architecture + review summary/attention + edition-local r6 delta-review
     supplement if needed).
- Reason: factual/provenance defects inside canonical Evidence itself; patching
  only Architecture/Draft would leave the authority chain internally incorrect.
- Conditional Human Architecture r6 APPROVAL is authorized IN ADVANCE (§12) and
  may be materialized IF AND ONLY IF every §12 condition is machine/audit
  verified on the ACTUAL regenerated Architecture; otherwise STOP with r6 PENDING.
- After r6 APPROVED: generate a COMPLETELY FRESH Draft from corrected authority
  (absolute freshness; r5-rev2 history/regression only); then STOP before
  reader-publication-validation/TeX/PDF/Preview/Freeze/Release for independent
  Human/Sol AI Architecture + Draft review.
- Does NOT permit: new Discovery, removed candidate, Selection role/disposition
  change, new PARTIAL, VERIFIED change, new Architecture limitation, package
  redesign/restructure, shared Core modification, manual lifecycle/checkpoint
  edits, destructive history rewrite, fabrication or carry-forward of a Human
  gate decision beyond the §12-conditional r6 APPROVED, TeX/PDF/publication work.

## Bounds acknowledged by worker

- Single run only (`r6-final-authority-correction-20261006`); single boundary
  (CANDIDATES_NORMALIZED).
- Fail-closed probes of formal Core mechanisms first (recorded in
  `reentry-probes-r6-final.md`); on confirmed absence, consume this run-specific
  Owner Exception. No prior exception reused.
- Core-controlled machinery only: `survey_human_gate_v2._revised_state`,
  `_superseded_paths_for_regeneration`, `_superseded_gate_authority_paths`,
  `survey_production_v2.write_json`, `survey_agent_control_v2.validate_agent_state`.
  No Human-gate decision function invoked for the rewind (`request_changes`,
  `record_architecture_approval`, `record_publication_preview_approval`,
  `invalidate_pending_gate` NOT called; no `reviewed_by/reviewed_at`
  fabricated).
- State/checkpoint/gate/approval bytes changed ONLY as deterministic output of
  the above Core functions (plus exact-set file deletions computed by Core).
- r5 (+ r1-r4) review/approval records preserved as immutable HISTORY only;
  never reused as approval for regenerated authority. After replay the fresh
  Architecture is PROPOSED with Human Architecture Review r6 PENDING; r6
  APPROVED is materialized ONLY after the §12 audit passes on actual bytes.
- Fallback contracted: any condition unsatisfiable → stop blocked with r6
  PENDING (no manual mutation, no go-forward publication cycle, no Draft unless
  r6 APPROVED).
