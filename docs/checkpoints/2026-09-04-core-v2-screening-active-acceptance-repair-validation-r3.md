# Core v2 active Screening acceptance repair — validation r3

Status: **CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW**

Date: 2026-09-04

## 1. Execution identity and boundary

- Repository: `eariver/japanese-generative-ai-survey`
- Maintenance branch: `fix/core-v2-screening-expansion-authority-20260904`
- Exact Starting SHA: `508c5aae952e00bd5736117df78d0c0161624bd7`
- Ending SHA (validated Core implementation before this record): `535e447b97a9bf10b90fa3de0962b0cd85436a08`
- Final record commit: the subsequent fast-forward commit containing this file; the final branch tip is reported in the completion handoff.
- Start guard: remote branch HEAD matched the Exact Starting SHA before any branch update.
- Main comparison at the validated implementation ending SHA: `main`=`c7a898889463b049dea4ee7337ee16ad5fbf3191`; `6 ahead / 0 behind / 6 commits`.
- No merge to `main`, W34, W33, or any other branch was performed.
- No force, reset, rewrite, or rebase was used.

Only the following five implementation/test paths were included in the validated implementation commit. The validation record is the only additional path in the following documentation commit.

```text
scripts/run_evidence_v2_interactive.py
scripts/run_selection_architecture_v2_interactive.py
scripts/survey_agent_control_v2.py
scripts/survey_screening_v2.py
tests/test_survey_active_screening_acceptance_v2.py
docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-repair-validation-r3.md
```

## 2. Repair implemented

`survey_agent_control_v2.resolve_checkpoint_artifact()` is now the generic fail-closed resolver for an artifact adopted by a passed Stage Checkpoint. It validates the current agent State, passed machine checkpoint, exactly one State checkpoint provenance authority, checkpoint path/hash, Stage Checkpoint schema and issue/lifecycle identity, checkpoint-set identity, unique artifact names, exactly one requested artifact row, regular non-symlink artifact path, and exact artifact SHA.

`survey_screening_v2.resolve_active_screening_acceptance()` uses that resolver for the passed `screening` Stage Checkpoint and then runs the current `validate_acceptance()` against the exact checkpoint-bound `screening-acceptance` path. It never enumerates accepted run directories and never chooses by directory count, mtime, digest order, or enumeration order. The reviewed agent-first historical State-SHA compatibility scope is used only while revalidating the immutable accepted package after lifecycle transition.

The interactive Evidence and Selection/Architecture runners now use the active resolver. The remaining `materialize_annual_chronology.py` directory scan is a separate legacy `screening/runs/*/acceptance.json` annual schema path, not the v2 `screening/v2/accepted/*/screening-accepted.json` active-authority path; it was not generalized because this repair does not change that legacy contract.

The strict Screening expansion authority repair is unchanged: complete accepted-root closure, accepted-root-only parent refs, parent Raw-union binding, rooted source identity, no obligation invention, unrelated Discovery substitution rejection, direct/non-expanded compatibility, and effective derived IDs for Evidence remain enforced.

## 3. Synthetic active-authority regressions

Dedicated test file: `tests/test_survey_active_screening_acceptance_v2.py`.

The synthetic fixture creates two content-addressed immutable Screening acceptance runs, retains the historical run, binds the corrected run to a passed Screening Stage Checkpoint, and resolves the corrected run through the active resolver. It also verifies directory creation order independence, explicit historical acceptance validation, missing/not-passed checkpoint failure, missing and duplicate artifact rows, artifact SHA drift, checkpoint authority SHA drift, pre-Screening rejection, and downstream-runner scan removal.

Result: **10/10 active-authority tests PASS**.

Required strict expansion regression suite remained green: **12/12 PASS** in `tests/test_screening_expansion_authority_v2.py`. This preserves all accepted-root accounting and provenance guarantees.

## 4. W34 read-only temporary regression

Fixture authority:

- Branch: `weekly/2026-W34-v2-work`
- Exact read-only SHA: `7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`

The W34 checkout was not modified. A separate temporary fixture combined exact W34 source bytes with the validated Core implementation. Its temporary corrected Screening set added only the five coverage passthrough children required by the instruction:

```text
w34-coverage-comfy-org-comfyui
w34-coverage-ggml-org-llama-cpp
w34-coverage-nvidia-tensorrt-llm
w34-coverage-sgl-project-sglang
w34-coverage-vllm-project-vllm
```

Each child used its exact accepted GitHub Releases root parent, the parent stable source identity, parent Raw paths only, no invented obligations, and an explicit coverage-only/non-new-Weekly-event rationale.

Measured temporary result:

| Measure | Result |
| --- | ---: |
| accepted root Discovery | 40 |
| original derived Screening Discovery | 105 |
| corrected derived Screening Discovery | 110 |
| accounted accepted roots | 40 |
| unaccounted accepted roots | 0 |
| historical acceptance retained | yes; `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662` |
| corrected acceptance | retained as a second immutable run; `796f15e1df3a90677e8a693817124100a6ff8d2a73f556f51a44283126263b22` |
| active resolver result | corrected acceptance only |
| Evidence tasks from active corrected run | 80 |

The original 105 event decisions were preserved. The five coverage-only children were assigned `DROP`, producing exactly:

```text
KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 30 / TOTAL 110
```

The temporary corrected acceptance and active checkpoint simulation passed. The 80 Evidence tasks use the effective derived Discovery IDs; no X/community observation was promoted to technical Evidence.

## 5. Test commands and results

All commands below used `/tmp/core-active-venv-MRD8cT/bin/python` with `jsonschema` installed and `PYTHONDONTWRITEBYTECODE=1`. The targeted commands were rerun in a fresh detached checkout of the remote implementation ending SHA `535e447b...`.

### Affected Core and active-authority suite

```text
python -m unittest -q \
  tests.test_survey_active_screening_acceptance_v2 \
  tests.test_screening_expansion_authority_v2 \
  tests.test_survey_screening_v2 \
  tests.test_survey_screening_archive_v2 \
  tests.test_accept_screening_results \
  tests.test_survey_agent_control_v2 \
  tests.test_survey_agent_tool_v2 \
  tests.test_survey_stage_validation_v2 \
  tests.test_survey_evidence_v2 \
  tests.test_run_evidence_v2_agent_first \
  tests.test_run_selection_architecture_v2_interactive
```

Result: **56 run / 56 PASS / 0 FAIL / 0 ERROR**.

### Affected downstream suite

```text
python -m unittest -q \
  tests.test_survey_completeness_v2 \
  tests.test_survey_completeness_closure_audit_v2 \
  tests.test_survey_architecture_v2 \
  tests.test_survey_architecture_cross_package_synthesis_v2 \
  tests.test_survey_architecture_review_expansion_v2 \
  tests.test_candidate_selection_gate \
  tests.test_evidence_acceptance_boundary \
  tests.test_prepare_evidence_run \
  tests.test_build_evidence_tasks
```

Result: **32 run / 32 PASS / 0 FAIL / 0 ERROR**.

### Repository/schema syntax suite

```text
python -m unittest -q tests.test_repository_contract_syntax tests.test_schema_syntax
```

Result: **3 run / 3 PASS / 0 FAIL / 0 ERROR**.

### Full Python suite diagnostic

```text
python -m unittest discover -s tests -p 'test*.py' -v
```

Result: **737 run / 728 PASS / 3 FAIL / 0 ERROR / 6 skipped**.

The three failures are pre-existing, unrelated diagnostic failures and were not repaired in this Core task:

1. `test_wu011_repair_set_remains_historical_and_current_premerge_boundary_is_repository_owned` (`tests.test_survey_findings_v2`) — the fixture repository already contains `sources/2026-W33/production-state.json`.
2. `test_sp001_profile_is_materialized_from_current_backlog_authority_not_registry_copy` (`tests.test_survey_pilot_bootstrap_v2`) — the test environment reports `RESUME` where the isolated test expects `INITIALIZE`.
3. `test_w33_initializes_but_sp001_first_requires_internal_scope_materialization` (`tests.test_survey_pilot_bootstrap_v2`) — the same pre-existing bootstrap environment state reports `RESUME` instead of `INITIALIZE`.

No changed path is implicated by these failures. The affected Core, downstream, and syntax suites are fully green.

## 6. Authority and lifecycle safety checks

- Historical accepted Screening runs remain present and unchanged.
- Active selection is checkpoint-bound and independent of accepted-directory order.
- Missing, non-passed, malformed, duplicate, drifted, and hash-mismatched checkpoint/artifact authorities fail closed.
- Direct explicit Screening acceptance validation remains supported.
- Effective derived Discovery IDs continue to propagate into Evidence task generation and downstream contracts.
- W34 `production-state.json`, accepted root Discovery, Discovery acceptance, W34 checkpoint, and W34 source artifacts were not written.
- W33 and `main` were not written.
- Production State lifecycle semantics were not changed by this Core repair; no edition State was advanced.
- Screening decisions/results/acceptance for production were not created or changed by this maintenance task.

## 7. Remaining limitations and handoff

- The legacy annual chronology helper still has its separate v1 `screening/runs/*/acceptance.json` single-run contract; migrating that unrelated legacy schema requires a separate scoped decision.
- The full-suite diagnostic retains the three unrelated failures listed above.
- This is a maintenance candidate only. It has not been merged to `main`, and Sol review remains required before adoption.

The strict provenance guarantees and full affected regressions pass. The candidate is therefore bounded at:

`CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`
