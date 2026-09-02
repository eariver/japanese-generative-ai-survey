# 2026-W33 Sol→Luna handoff — Selection revision deterministic advancement r1

Status: `READY_FOR_LUNA / SELECTION_REVISION_ADVANCEMENT_ONLY / STOP_AFTER_STATE_TRANSITION`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at handoff creation: `EVIDENCE_REVIEWED`  
Current machine action: `stage:selection`  
Target Human Gate: `ARCHITECTURE_REVIEW`  
Sol Selection revision review: `sources/2026-W33/execution/reviews/w33-selection-revision-sol-review-20260831-r1.md`

The caller must supply the exact current branch SHA containing this handoff, the Sol review above, and the recovery-index update pointing to this handoff. Luna must begin from that exact SHA. If remote branch HEAD differs before execution starts, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`. Do not rebase, merge, change basis, or force-push.

## 1. Objective

Perform only the deterministic Core transition:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

for the already Sol-reviewed revised W33 Candidate Matrix and Candidate Selection.

Do not perform Architecture reasoning or create Architecture artifacts.

Successful endpoint:

`SELECTION_COMPLETE_READY_FOR_SOL_ARCHITECTURE_REVISION_POLICY`

## 2. Frozen current authority

### Production State

Path:

`sources/2026-W33/production-state.json`

Expected SHA-256:

`b546d8856ed60579c35627dfbe010a7c44ca0bacb526fe7a99b7cf8326a2aee7`

Required semantics before execution:

- lifecycle: `EVIDENCE_REVIEWED`;
- next action: `stage:selection`;
- discovery/screening/evidence/materiality/completeness: `passed`;
- selection: `pending`;
- architecture: `pending`;
- Architecture Review: `pending`;
- terminal reason: `null`;
- Exception Gate: inactive.

### Candidate Matrix

Path:

`sources/2026-W33/candidate-matrix-v2.json`

Expected SHA-256:

`4ff1a622a05e4b559d4531e2361e5b10d34affbc8cc5a244105cf1d994c9bc08`

Expected summary:

- candidates: `37`;
- `MATERIAL 25 / CONTEXT 10 / HOLD 1 / NON_MATERIAL 1`;
- `VERIFIED 24 / PARTIAL 12 / NEEDS_MORE 1 / REJECTED 0`.

### Candidate Selection

Path:

`sources/2026-W33/candidate-selection-v2.json`

Expected SHA-256:

`7d7b56c27fa31c17d1ee00f8a508d6afb96802990d33fb0d6ef848d1e6f9df7e`

Expected summary:

- selection version: `w33-selection-revision-luna-r1`;
- assignments: `37`;
- `SELECTED 28`;
- `HOLD 1`;
- `REJECT 8`;
- `INSPECT 0`;
- selected usage remains `PRIMARY 21 / SUPPORTING 7`;
- MiniMax is the sole HOLD;
- the five repaired carry-over candidates are REJECT and not selected.

These two semantic artifacts are frozen byte-for-byte for this task.

### Sol semantic authority

Path:

`sources/2026-W33/execution/reviews/w33-selection-revision-sol-review-20260831-r1.md`

Decision:

`ACCEPT / SELECTION_REVISION_SEMANTICS_FROZEN / CARRY_OVER_DISPOSITIONS_CLOSED / APPROVED_FOR_CORE_ADVANCEMENT`

Do not reconsider Selection decisions.

## 3. Mandatory read order

Before writing, read in order:

1. `AGENTS.md` from reviewed main.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed main.
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed main.
4. `docs/survey-production-core-v2-operator-execution-bridge.md` from reviewed main.
5. `schemas/operator-execution-request-v2.schema.json` from reviewed main.
6. `scripts/survey_stage_validation_v2.py` from reviewed main.
7. `scripts/survey_agent_control_v2.py` from reviewed main.
8. `scripts/survey_core_execution_bridge_v2.py` from reviewed main.
9. `sources/2026-W33/production-profile.json`.
10. `sources/2026-W33/production-state.json`.
11. `sources/2026-W33/execution/index.md`.
12. `sources/2026-W33/gates/reviews/architecture-r2.json`.
13. `sources/2026-W33/execution/handoffs/w33-selection-revision-luna-r1.md`.
14. `sources/2026-W33/execution/sessions/w33-luna-selection-revision-20260830-r1.md`.
15. `sources/2026-W33/execution/reviews/w33-selection-revision-sol-review-20260831-r1.md`.
16. the exact Candidate Matrix and Candidate Selection.
17. this handoff.

If Core authority materially conflicts, stop with `CORE_DRIFT_NEEDS_SOL_REVIEW`.

## 4. Current-stage contract

At `EVIDENCE_REVIEWED`, current Core requires exactly:

- `candidate-matrix`;
- `candidate-selection`.

Current-stage validation must PASS using the exact frozen artifacts above and the already-checkpointed revised E/M/C authority.

Expected transition:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

Checkpoint set must be exactly:

`selection`

## 5. Operator request

Create exactly:

`sources/2026-W33/execution/requests/w33-selection-revision-advance-20260831-r1.json`

Use current schema `2.0-rc1`, actual offset-aware execution timestamp, current work branch, and reviewed-main SHA above.

Semantic operation:

```json
{
  "kind": "ADVANCE_STAGE",
  "expected_from_state": "EVIDENCE_REVIEWED",
  "state_path": "sources/2026-W33/production-state.json",
  "artifacts": [
    {
      "name": "candidate-matrix",
      "path": "sources/2026-W33/candidate-matrix-v2.json"
    },
    {
      "name": "candidate-selection",
      "path": "sources/2026-W33/candidate-selection-v2.json"
    }
  ],
  "agent_reviews": [
    {
      "check_id": "SOL_SELECTION_REVISION_SEMANTIC_REVIEW",
      "kind": "AGENT_RESEARCH",
      "executor": "ChatGPT GPT-5.6 Sol",
      "evidence": "ACCEPT / SELECTION_REVISION_SEMANTICS_FROZEN / CARRY_OVER_DISPOSITIONS_CLOSED / APPROVED_FOR_CORE_ADVANCEMENT. Review authority: sources/2026-W33/execution/reviews/w33-selection-revision-sol-review-20260831-r1.md."
    }
  ],
  "summary": "Adopt the Sol-reviewed revised W33 Candidate Matrix and Candidate Selection and advance exactly from EVIDENCE_REVIEWED to SELECTION_COMPLETE."
}
```

Validate against current schema.

## 6. Request-only commit rule

The first worker commit must contain only:

`sources/2026-W33/execution/requests/w33-selection-revision-advance-20260831-r1.json`

Before branch update, re-read remote HEAD and require exact caller-supplied starting SHA.

Use normal fast-forward only, `force=false`.

Record the canonical request commit SHA and use that exact SHA as the bridge event SHA.

## 7. Canonical bridge execution

Use the established canonical Survey Production Core v2 operator bridge / Issue #448 transport.

The bridge must validate the exact State, Matrix, Selection, and Sol review and generate the canonical deterministic transition artifacts.

Expected bridge-run directory:

`sources/2026-W33/execution/bridge-runs/w33-selection-revision-advance-20260831-r1/`

Expected generated files:

- `core-stage-contract.json`;
- `reviews.json`;
- `receipt.json`.

Expected checkpoint:

`sources/2026-W33/orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json`

Expected updated State:

`sources/2026-W33/production-state.json`

Preferred session record:

`sources/2026-W33/execution/sessions/w33-luna-selection-revision-advance-20260831-r1.md`

## 8. Checkpoint requirements

The canonical `EVIDENCE_REVIEWED` Stage Checkpoint must bind exactly:

- candidate-matrix SHA-256 `4ff1a622a05e4b559d4531e2361e5b10d34affbc8cc5a244105cf1d994c9bc08`;
- candidate-selection SHA-256 `7d7b56c27fa31c17d1ee00f8a508d6afb96802990d33fb0d6ef848d1e6f9df7e`.

Checkpoint set exactly:

- `selection`.

Reviews must include:

1. `CORE_STAGE_CONTRACT = PASS`;
2. `SOL_SELECTION_REVISION_SEMANTIC_REVIEW = PASS`.

## 9. Expected post-State

After exactly one transition:

- lifecycle: `SELECTION_COMPLETE`;
- next action: `stage:architecture`;
- discovery/screening/evidence/materiality/completeness/selection: `passed`;
- architecture: `pending`;
- Architecture Review: `pending`;
- draft and later checkpoints: `pending`;
- terminal reason: `null`;
- Exception Gate: inactive.

State history must gain exactly one edge:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

bound to the canonical request/event commit SHA.

## 10. Explicit prohibitions

Do not:

- modify Candidate Matrix or Candidate Selection;
- reopen Discovery, Screening, Evidence, Materiality, or Completeness;
- access external sources;
- create or modify Architecture artifacts;
- create the mandatory synthesis chapter yet;
- run Architecture stage validation;
- create or alter Human Gate records;
- draft article prose;
- advance beyond `SELECTION_COMPLETE`;
- modify shared Core/config/schema/workflow code;
- force-push, rebase, merge, or rewrite history.

## 11. Required validation

Verify and record at minimum:

1. exact starting remote HEAD PASS;
2. pre-State SHA and semantics PASS;
3. exact Matrix/Selection SHA PASS;
4. Matrix/Selection schema + current-stage validation PASS;
5. request schema PASS;
6. request-only commit boundary PASS;
7. Core stage contract PASS;
8. checkpoint schema/control PASS;
9. exact two artifact bindings PASS;
10. checkpoint set exactly `selection`;
11. both required reviews PASS;
12. bridge receipt `ADVANCE_STAGE / PASS / SELECTION_COMPLETE`;
13. post-State agent-first validation PASS;
14. Architecture remains pending;
15. Matrix/Selection remain byte-identical;
16. no Architecture/Draft/publication artifact created;
17. final history remains fast-forward/non-force.

## 12. Final report

Report:

- branch;
- exact supplied starting SHA;
- request-only commit SHA;
- bridge result commit SHA;
- final bookkeeping SHA;
- Issue #448 comment / workflow run if used;
- exact changed paths;
- pre/post State SHA-256;
- final lifecycle and next action;
- confirmation Matrix/Selection unchanged;
- confirmation no Architecture work started.

Stop exactly at:

`SELECTION_COMPLETE_READY_FOR_SOL_ARCHITECTURE_REVISION_POLICY`
