# Core v2 Screening expansion authority repair — validation record r2

Status: **NEEDS_SOL_REVIEW**

This is the durable validation record for the strict accepted-root closure
repair on the existing Core maintenance branch. It is edition-neutral and
does not modify W34 production artifacts.

## Scope and exact refs

- Repository: `eariver/japanese-generative-ai-survey`
- Branch: `fix/core-v2-screening-expansion-authority-20260904`
- Exact starting / pre-write HEAD: `8313e06ba2a32d51f716e3af33b849b241bb2421`
- Reviewed `main`: `c7a898889463b049dea4ee7337ee16ad5fbf3191`
- W34 read-only fixture: `weekly/2026-W34-v2-work`
- W34 exact SHA: `7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`

The pre-write branch guard matched exactly. No force, reset, rewrite, rebase,
merge, main write, or W34 write was used.

## Implemented contract repair

`validate_discovery_expansion()` now fails closed unless:

```text
accounted_root_ids == accepted_root_ids
```

Any accepted root not referenced by at least one derived child's `parent_refs`
raises `ValueError` with the complete `unaccounted_root_ids` list. The prior
normal-success return of non-empty `unaccounted_root_ids` was removed. Existing
per-child checks remain active for expansion origin, accepted parent IDs, Raw
path union, rooted source identity, obligation subset, duplicate IDs, and issue
identity.

## Executed commands and results

The dependency-backed commands used the existing read-only temporary runtime
`/tmp/core-v2-venv.fmkeWB/bin/python` with `jsonschema 4.23.0`.

1. Targeted strict authority regressions:

   ```text
   PYTHONPATH=. /tmp/core-v2-venv.fmkeWB/bin/python -m pytest -q \
     tests/test_screening_expansion_authority_v2.py
   ```

   Result: **PASS — 5 passed, 0 failed**.

   This covers direct-compatible resolution through existing tests, valid
   one-to-many expansion, valid multi-parent expansion, complete root closure,
   silent root omission, orphan/unknown parent, cross-issue parent, invented
   Raw, source identity substitution, unrelated `BASE`, obligation invention,
   and duplicate derived ID.

2. Affected downstream Core regression:

   ```text
   PYTHONPATH=. /tmp/core-v2-venv.fmkeWB/bin/python -m pytest -q \
     tests/test_screening_expansion_authority_v2.py \
     tests/test_survey_screening_v2.py \
     tests/test_survey_screening_archive_v2.py \
     tests/test_accept_screening_results.py \
     tests/test_validate_screening_result.py \
     tests/test_survey_evidence_v2.py \
     tests/test_evidence_acceptance_boundary.py \
     tests/test_prepare_evidence_run.py \
     tests/test_build_evidence_tasks.py \
     tests/test_accept_evidence_results.py \
     tests/test_validate_evidence_run.py \
     tests/test_run_evidence_v2_agent_first.py \
     tests/test_run_selection_architecture_v2_interactive.py \
     tests/test_survey_stage_validation_v2.py \
     tests/test_survey_agent_control_v2.py \
     tests/test_survey_agent_tool_v2.py \
     tests/test_survey_completeness_v2.py \
     tests/test_survey_architecture_v2.py
   ```

   Result: **PASS — 76 passed, 0 failed**. This revalidated effective-derived
   Discovery propagation through stage validation, Evidence, agent-first
   execution, interactive Evidence, interactive Selection/Architecture,
   Materiality/Completeness, and Architecture validators. Direct/non-expanded
   paths remained green.

3. Repository contract and schema syntax:

   ```text
   PYTHONPATH=. /tmp/core-v2-venv.fmkeWB/bin/python -m pytest -q \
     tests/test_repository_contract_syntax.py tests/test_schema_syntax.py
   ```

   Result: **PASS — 3 passed, 0 failed, 1 pre-existing SyntaxWarning**.

4. Full Python suite:

   ```text
   PYTHONPATH=. /tmp/core-v2-venv.fmkeWB/bin/python -m pytest -q
   ```

   Result: **729 passed, 6 failed, 6 skipped, 1 warning**. The six failures
   are outside this repair's changed Core paths: longform publication helper,
   Special half-year navigation-window repair, Special reader enum cleanup,
   historical W33 repository-owned boundary, and two pilot-bootstrap
   initialization expectations. None exercises the strict expansion contract;
   the affected downstream suite above is fully green.

## W34 read-only regression

The W34 remote ref still resolves to the exact fixture SHA above. Read-only
inspection found:

- accepted root Discovery: **40** records;
- effective event-level Discovery: **105** records / **105** unique IDs;
- event mapping: `W34-C001`–`W34-C105`, **105/105**;
- existing accepted Screening decisions: **KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 25**;
- existing Screening acceptance metadata: **105 records / 3 batches**.

Under the repaired strict Core, the exact event file fails before it can be
credited as an effective downstream basis:

```text
ValueError: accepted root Discovery silently omitted from derived parent closure:
unaccounted_root_ids=[
  'w34-github-releases-comfy-org-comfyui',
  'w34-github-releases-ggml-org-llama-cpp',
  'w34-github-releases-nvidia-tensorrt-llm',
  'w34-github-releases-sgl-project-sglang',
  'w34-github-releases-vllm-project-vllm'
]
```

The strict W34 result is therefore:

```text
accepted root count:       40
effective derived count:   105
accounted root count:      35
unaccounted root count:     5
strict expansion:          FAIL (fail-closed)
Screening acceptance:      not credited under repaired Core
Evidence package:          not prepared under repaired Core
expected non-DROP tasks:   80 (45 + 19 + 16; not reached)
```

The five records are existing `BASE` GitHub Releases roots with no event
child `parent_ref` in the exact immutable W34 event JSONL and no corresponding
crosswalk row. Adding synthetic parent references, changing the event JSONL,
or changing its accepted Screening package hash would violate the W34
read-only/immutable boundary. Treating those roots as implicitly accounted
would violate the repaired contract. This is the blocking semantic mismatch
requiring Sol review.

An additional pre-existing exact-fixture issue was observed when invoking the
full archived acceptance validator: the W34 State/checkpoint history has an
implementation/checkpoint semantic inconsistency before the expansion check.
It was not repaired or bypassed here, and no W34 artifact was changed.

## Changed paths and main boundary

Current-task paths relative to the pre-write maintenance HEAD:

```text
scripts/survey_screening_v2.py
tests/test_screening_expansion_authority_v2.py
docs/checkpoints/2026-09-04-core-v2-screening-expansion-authority-repair-validation-r2.md
```

Cumulative maintenance-branch paths relative to reviewed `main` are limited
to these shared-Core repair paths:

```text
scripts/run_evidence_v2_interactive.py
scripts/run_selection_architecture_v2_interactive.py
scripts/survey_evidence_v2.py
scripts/survey_handlers_v2.py
scripts/survey_screening_v2.py
scripts/survey_stage_validation_v2.py
tests/test_screening_expansion_authority_v2.py
docs/checkpoints/2026-09-04-core-v2-screening-expansion-authority-repair-validation-r2.md
```

`main` was not changed or merged. W34, W33, production state, accepted root
Discovery, and unrelated Core files were not changed.

## Remaining limitation and disposition

The Core invariant is now strict and all synthetic/downstream regressions
pass. The exact W34 fixture cannot satisfy the new invariant without an
edition artifact correction that is explicitly outside this maintenance task.
The candidate therefore stops at:

`NEEDS_SOL_REVIEW`

No production-state advancement, Screening decision mutation, Screening
acceptance creation, Evidence acceptance, Materiality, Completeness, Selection,
or Architecture advancement was performed by this repair.
