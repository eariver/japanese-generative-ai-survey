# W42 r28 — read-only stage-contract feasibility (NONCANONICAL isolated proof)

Reproduction: `python3 /tmp/r28-sandbox/r28_routing_tests.py` (sandbox kept outside the repo; imports frozen modules
read-only from the r28 worktree; sole sandbox write is its own stdout log). Real functions, synthetic inputs, no
canonical State loaded as an output target, no repo writes.

## 1. Results

| # | test (real code) | result |
|---|---|---|
| T1 | `survey_handlers_v2.register_handlers` → 20 names | reader-publication pair ABSENT; semantic pair present-but-unreferenced |
| T2 | orchestrator `registry.get` lines (`survey_orchestrator_v2.py:531-536`) with exact identities | fail-closed `ValueError: registered handler/semantic validator unavailable` (both) |
| T3 | `validate_stage` signature + bridge source scan | NO registry parameter; ZERO registry/orchestrator/handler-module references in bridge file |
| T4 | real `_validate_stage_semantics`, synthetic `DRAFT_COMPLETE` state, empty artifacts | `StageValidationError` naming all 7 reader artifacts — dispatch proven, registry-free |
| T5 | `stage_plan[DRAFT_COMPLETE]` read | exact identities + `VALIDATED_DRAFT` + 6 listed artifacts; `plan_action` copies them verbatim |
| T6 | `validate_semantic_publication` input contract vs DRAFT_COMPLETE contract | 3 handoff inputs ≠ 7 required — NOT interchangeable |

Object hashes (frozen, verified identical pinned-vs-main): config `cffe16fe…`, handlers `510a2aba…`,
orchestrator `5019b4f3…`. Command log: `/tmp/r28-sandbox/r28_routing_tests.log` (sandbox-local, not committed).

## 2. Feasibility verdict

**A Core-compliant dispatch path EXISTS and is proven at handler + validator + stage-contract levels:**
operator-bridge `ADVANCE_STAGE` → `stage_validation.validate_stage` → DRAFT_COMPLETE 7-artifact reader/quality/surface-gate
validation → `VALIDATED_DRAFT`. It uses the frozen State-pinned Core and config, changes nothing canonical, invents no alias.

## 3. Fatal missing dependency: NONE for routing. Secondary contract gap recorded (not a blocker)

Frozen stage code requires a 7th artifact, `reader-surface-gate`, which `config/...stage_plan.DRAFT_COMPLETE.artifacts`
does NOT list (6 listed). The gate validator (`survey_reader_surface_gate_v2.validate_reader_surface_gate:1437`) demands a
schema-valid PASSED record with 0 blocking findings binding exact source bytes + semantic review authority.
The future canonical unit must author this artifact per that validator; the bridge will enforce it at ADVANCE_STAGE time.
Flagged for Core-maintenance awareness (config/code artifact-list asymmetry); NOT an r28 routing blocker and NOT edited here.

## 4. What was NOT done (boundaries kept)

No canonical Reader/manuscript, no validated-source/PDF production, no quality/semantic/visual review authorship, no
`ADVANCE_STAGE` request, no stage transition, no candidate, no Gate action. Synthetic inputs only; live W42 State used
solely as a read-only guard reference (HEAD/tree/pin checks), never as a test output target.
