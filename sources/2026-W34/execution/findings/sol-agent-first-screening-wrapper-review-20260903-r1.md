# 2026-W34 Sol review — agent-first Screening wrapper retry

Status: `RETRY_WITH_CANONICAL_AGENT_TOOL`

Issue: `2026-W34`  
Reviewed branch: `weekly/2026-W34-v2-work`  
Reviewed Luna end: `f974a81ffe4f8d38c35a341cd660860331ff4753`

Decision / finding ID: `SOL-W34-AGENT-FIRST-SCREENING-WRAPPER-20260903-R1`

## 1. Luna materialization result

The bounded Luna event-level expansion succeeded at the semantic/provenance layer:

- `sources/2026-W34/screening/input/event-discovery-v2.jsonl`: 105 records / 105 unique IDs;
- `W34-C001` through `W34-C105`: 105/105 accounted, missing 0, duplicate 0;
- every event-level record has existing accepted parent Discovery provenance;
- 36 unique Raw paths exist;
- DailyX remains 7/7 files and 76/76 topics;
- corrected Grok r2 remains 47/47 URLs with 10 ORDINARY_WINDOW / 20 BACKGROUND_ONLY / 17 LATE_BREAKING;
- carry-over remains represented without promotion;
- actual `survey_screening_v2.validate_discovery_set()` passed;
- Production State and immutable accepted Discovery were not modified.

These outputs remain the candidate Screening input. Do not rebuild or semantically alter them solely because the next package-preparation attempt failed.

## 2. Why the direct `prepare_package()` invocation failed

The Luna task invoked `scripts/survey_screening_v2.py` directly and supplied the initialization implementation SHA. Direct WU-006/WU-007 helper execution still reaches the legacy `core.verify_state_basis()` semantics, which reject the current agent-first State because they expect:

- legacy checkpoint attestation paths under `orchestration/v2/attestations`; and
- edition-wide history implementation identity equal to the initialization implementation SHA.

The current W34 State was legitimately advanced by the agent-first operator path. It therefore carries:

- Stage Checkpoint provenance under `orchestration/v2/checkpoints`; and
- per-stage implementation provenance in `history`, including the Discovery advancement commit.

Do not mutate W34 State, checkpoint bytes, or history to satisfy the legacy direct helper verifier.

## 3. Existing reviewed-main compatibility authority

Reviewed main already contains `scripts/survey_agent_tool_v2.py` specifically for this situation.

Its documented contract states that some WU-006/WU-007 helpers still call legacy `core.verify_state_basis`, and that the wrapper replaces that verifier only for the lifetime of one helper process with the agent-first State validator while retaining fail-closed Profile/contract/checkpoint/hash checks.

The wrapper allowlist includes:

- `scripts/survey_screening_v2.py`;
- `scripts/survey_evidence_v2.py`.

`verify_current_stage_basis()` requires the implementation SHA supplied to the helper to equal the actual current work-branch HEAD and validates the State with `survey_agent_control_v2.validate_agent_state()`.

This behavior is covered by `tests/test_survey_agent_tool_v2.py`, including historical accepted Screening/Evidence State-SHA handling and rejection of non-State drift.

Therefore the observed direct-helper failure is not yet evidence of a new shared-Core defect. The canonical agent-first wrapper must be exercised before classifying a Core defect.

## 4. Correction to the previous Luna instruction

The previous Sol instruction said to run the actual current-Core `prepare_package()` but did not explicitly require the canonical agent-first wrapper. That omission allowed a direct helper invocation that is valid as a diagnostic but not the intended agent-first production execution path.

The retry must use `scripts/survey_agent_tool_v2.py` and the actual current work-branch HEAD as the helper `--implementation-sha`.

## 5. Required retry semantics

Reuse unchanged:

- `sources/2026-W34/screening/input/event-discovery-v2.jsonl`;
- `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`;
- current `sources/2026-W34/production-state.json`;
- immutable accepted 40-record Discovery graph/checkpoint.

Run Screening preparation through the canonical wrapper, conceptually:

```text
python3 scripts/survey_agent_tool_v2.py \
  --repo-root . \
  --state sources/2026-W34/production-state.json \
  --helper scripts/survey_screening_v2.py \
  -- \
  prepare \
  --state sources/2026-W34/production-state.json \
  --discovery sources/2026-W34/screening/input/event-discovery-v2.jsonl \
  --output-dir <new bounded package directory> \
  --max-records 50 \
  --max-json-chars 120000 \
  --implementation-sha <actual current HEAD>
```

Equivalent invocation is acceptable if it goes through `survey_agent_tool_v2` and preserves the same contract.

The retry must prove:

- agent-first State validation PASS;
- Screening package preparation PASS;
- input record count 105;
- 105 unique event-level Discovery IDs exactly represented in batches;
- package basis points to `sources/2026-W34/screening/input/event-discovery-v2.jsonl`;
- no Screening decisions or acceptance created;
- Production State and accepted Discovery remain byte-identical.

## 6. Stop rule

If the canonical wrapper succeeds, stop with a Screening-ready package for independent Sol semantic Screening.

If the canonical wrapper itself fails, record the exact exception and stop `NEEDS_SOL_REVIEW`. Only then should the failure be evaluated as a potential shared-Core defect.

Do not modify shared Core in W34.