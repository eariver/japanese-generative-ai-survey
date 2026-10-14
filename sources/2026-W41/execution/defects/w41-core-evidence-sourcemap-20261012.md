# W41 edition-local defect — Core Evidence SOURCE_CLASS_MAP gap (2026-10-12)

Status: `EDITION_LOCAL / CORE_MAP_GAP / NO_PATCH / RERUN_REQUIRED_BEFORE_ACCEPTANCE`
Scope: shared Core is read-only in production (AGENTS.md). No patch applied.

## Gap

`scripts/survey_evidence_v2.py::SOURCE_CLASS_MAP` has no entry for Discovery
`source_type = "SECONDARY_OBSERVATION"`, although it is the honest r1/r2-era
classification used by 9 W41 canonical Discovery rows (5 DailyX vendor-X rows +
Tencent HOLD + 2 W40 carry HOLDs + ELYZA pre-window context):

- w41-dailyx-agr-20261006, w41-dailyx-nemotron-hf-20261006,
  w41-dailyx-nace-drex-20261010, w41-dailyx-nace-ndi-20261010,
  w41-dailyx-elevenlabs-20261010, w41-hold-tencent-20261011,
  w41-hold-pixelcanary-20261011, w41-hold-tbcvideo-20261011,
  w41-weak-elyza-rsi-20261002

`task_authority_sources()` raises `ValueError: unsupported source_type for
Evidence authority: 'SECONDARY_OBSERVATION'`, which blocks the canonical
interactive-Evidence runner (`run_evidence_v2_interactive.run`) for these 9
tasks. Same failure class as W40 defect
`execution/defects/w40-core-evidence-sourcemap-20261010.md`
(PRIMARY_RESEARCH_ABSTRACT + EVALUATOR_PUBLISHER).

## Edition-local handling (r3, review-substance unaffected)

- Cards for the 9 tasks built with the REAL Core `_build_card` +
  `validate_evidence_card`, under a narrow documented fallback mapping ONLY
  `"SECONDARY_OBSERVATION" -> "SECONDARY"` (mirrors established siblings
  `carryover_recheck`, `sol_working_set_observation`, `prior-week-authority`).
- Every other Core check rerun unmodified. No shared-Core file touched.
- All 9 cards keep NEEDS_MORE/PARTIAL + HOLD/CONTEXT with UNRESOLVED targets;
  the fallback does not upgrade any materiality.
- A formal production-validation run that needs these cards MUST be rerun
  cleanly after reviewed Core repair. Evidence acceptance remains blocked
  pending Sol review in any case.
