# W42 r28 — operator module / bridge search (NONCANONICAL, read-only)

Question: does any pre-existing, authorized module or operator bridge lawfully supply
`stage:reader-publication-validation` / `validate:reader-publication`?

## 1. Search scope (bounded, explicit)

- `scripts/*.py` for `register_handlers` definitions: exactly ONE (`survey_handlers_v2.py:452`). No other registrar module exists.
- Repo-wide grep for both identities outside edition-local governance/proposal text: hits ONLY in
  `config/survey-production-v2.json:332-333` (the requirement itself), r11 historical feasibility notes, and r27 session/index notes. No implementation.
- `.github/workflows/`: 8 workflows. Only `survey-production-v2-operator-bridge.yml` executes Core stage operations.
  It never invokes `survey_orchestrator_v2`, never passes `--handler-module`, never references the handler registry.
  Invocation is fixed: `python -m scripts.survey_core_execution_bridge_v2 --repo-root … --request … --event-sha … --ref-name …`
  with a reviewed-main-only trusted runtime (`git archive $REVIEWED_MAIN_SHA scripts`).
- Bridge operation surface (bounded, from workflow + bridge source): `INITIALIZE_WEEKLY | INITIALIZE_RETROSPECTIVE |
  INITIALIZE_THEMATIC | ADVANCE_STAGE | RECORD_ARCHITECTURE_APPROVAL | REQUEST_ARCHITECTURE_REVISION |
  RECORD_PUBLICATION_PREVIEW_APPROVAL | REQUEST_PUBLICATION_PREVIEW_REVISION`. `ADVANCE_STAGE` is an explicitly allowed
  operator transport op (AGENTS.md bridge surface confirms).

## 2. The lawful dispatch path (found, pre-existing, authorized)

`survey_core_execution_bridge_v2._advance_stage` (`:365-411`) → `stage_validation.validate_stage(...)`.
Static facts (verified by source read + `grep -c` = 0 for `registry|register_handlers|survey_orchestrator|handler-module`
anywhere in the bridge file):
- The bridge imports `agent, execution_record, human_gate, period, core, schema_gate, stage_validation` — never the orchestrator or handlers registry.
- `validate_stage(repo_root, cfg, state_path, supplied, output_path, recorded_at)` takes NO registry parameter (real signature, isolated test T3).
- DRAFT_COMPLETE semantics are hardcoded in `_validate_stage_semantics` (`survey_stage_validation_v2.py:429-474`):
  requires 7 artifact authorities (reader-manuscript, validated-source, publication-pdf, quality-regression-bundle,
  semantic-review, visual-review, **reader-surface-gate**) and validates each with the concrete reader/quality/surface-gate
  validators. Dispatch proven at runtime with the real function on synthetic empty input (isolated test T4):
  `StageValidationError: stage validation missing artifact authorities: reader-manuscript, validated-source,
  publication-pdf, quality-regression-bundle, semantic-review, visual-review, reader-surface-gate`
  — i.e. execution reaches the exact DRAFT_COMPLETE stage contract with zero registry involvement.

**Conclusion: the authorized operator bridge already implements the exact DRAFT_COMPLETE→VALIDATED_DRAFT dispatch
without needing the two registry names.** No new module, alias, or Core change is required for routing.

## 3. Negative findings (explicit)

- No pre-existing `--handler-module` registrar supplying the two identities exists in-repo. The orchestrator-CLI path
  remains fail-closed for DRAFT_COMPLETE (proven, not worked around).
- The `stage:semantic-publication-validation` / `validate:semantic-publication` pair is NOT a lawful substitute:
  its validator requires only 3 handoff inputs (validated-source/publication-pdf/quality-regression-bundle,
  `survey_handlers_v2.py:364-376`) vs the 7 required by the DRAFT_COMPLETE contract (incl. manuscript, both reviews,
  surface gate); no `stage_plan` lifecycle references it; the r11 independent audit already forbade shimming the Weekly
  renderer onto the `reader-publication` configuration. Assumed NOT interchangeable — now proven non-interchangeable.
- `validate:reader-publication` as a *name* is unimplemented anywhere; nothing in this unit invents it. The bridge path
  makes the name unnecessary rather than supplying it.

## 4. Limits of this search

- External (non-repo) handler modules cannot be proven nonexistent; the claim is bounded to authorized in-repo +
  documented bridge transports. A `--handler-module` pointing outside reviewed-main code would violate the bridge's
  trusted-runtime rule (`git archive $REVIEWED_MAIN_SHA scripts`) and is therefore not an authorized route.
- No live stage was executed; artifact bytes for a real ADVANCE_STAGE do not exist yet (future canonical unit).
