# 2026-W33 Sol→Luna handoff — Selection deterministic advancement r1

Status: `READY_FOR_LUNA / SELECTION_ADVANCEMENT_ONLY / STOP_AFTER_STATE_TRANSITION`

Issue: `2026-W33`
Canonical branch: `weekly/2026-W33-v2-work`
Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
Current lifecycle at handoff creation: `EVIDENCE_REVIEWED`
Current machine action: `stage:selection`
Target Human Gate: `ARCHITECTURE_REVIEW`
Sol Selection review: `sources/2026-W33/execution/reviews/w33-selection-sol-review-20260830-r1.md`

The caller must provide Luna the exact current branch SHA containing this handoff and the Sol Selection review. Luna must begin from that exact SHA. If remote branch HEAD differs before execution, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`. Do not silently rebase, merge, change basis, or force-push.

## 1. Objective

Perform only the deterministic Core transition for the already Sol-approved W33 Selection semantic package:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

The worker must:

1. verify the exact frozen Candidate Matrix and Candidate Selection bytes;
2. verify Production State is still the exact accepted pre-state;
3. create and validate one immutable operator request;
4. commit the request alone and record its canonical GitHub commit SHA;
5. execute the canonical operator/Core bridge with that request commit as event SHA;
6. create the canonical `EVIDENCE_REVIEWED` Stage Checkpoint with checkpoint set exactly `selection`;
7. advance Production State exactly once to `SELECTION_COMPLETE`;
8. verify `next_action=stage:architecture`;
9. record bridge/checkpoint/State/session provenance;
10. commit/push and stop for Sol.

Do not perform Architecture reasoning or create Architecture artifacts.

Successful endpoint:

`SELECTION_COMPLETE_READY_FOR_SOL_ARCHITECTURE_POLICY`

## 2. Exact starting authority

### Production State

Before any write verify:

- path: `sources/2026-W33/production-state.json`
- SHA-256: `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`
- lifecycle: `EVIDENCE_REVIEWED`
- next action: `stage:selection`
- Selection checkpoint: `pending`
- Architecture checkpoint: `pending`
- Architecture Review: `pending`
- terminal reason: null

### Candidate Matrix

Path:

`sources/2026-W33/candidate-matrix-v2.json`

Exact SHA-256:

`1b660291564bda5f30debd86bb6911eb53edf06e8f735710f84652d972c4d198`

Expected structure:

- 37 candidates
- MATERIAL 25 / CONTEXT 6 / HOLD 6
- VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

### Candidate Selection

Path:

`sources/2026-W33/candidate-selection-v2.json`

Exact SHA-256:

`9c6997d2ed3921a847db5e001ec9377189bb25d5475454593f23016308557005`

Expected structure:

- selection version: `w33-selection-luna-r1`
- assignments: 37
- SELECTED 28
  - PRIMARY 21
  - SUPPORTING 7
- HOLD 6
- REJECT 3
- INSPECT 0

These two artifacts are frozen byte-for-byte. This task must not modify either file.

### Sol semantic authority

Path:

`sources/2026-W33/execution/reviews/w33-selection-sol-review-20260830-r1.md`

Decision:

`ACCEPT / SELECTION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

The worker must not reconsider Selection decisions.

## 3. Mandatory read order

Before writing, read in this order:

1. `AGENTS.md` from reviewed main.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed main.
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed main.
4. `docs/survey-production-core-v2-operator-execution-bridge.md` from reviewed main.
5. `schemas/operator-execution-request-v2.schema.json` from reviewed main.
6. `scripts/survey_stage_validation_v2.py` from reviewed main.
7. `scripts/survey_agent_control_v2.py` from reviewed main.
8. `scripts/survey_core_execution_bridge_v2.py` from reviewed main.
9. `scripts/survey_agent_tool_v2.py` from reviewed main.
10. `scripts/survey_architecture_v2.py` and `scripts/survey_architecture_v2_base.py` from reviewed main.
11. `sources/2026-W33/production-profile.json`.
12. `sources/2026-W33/production-state.json`.
13. `sources/2026-W33/execution/index.md`.
14. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`.
15. `sources/2026-W33/execution/handoffs/w33-selection-luna-r1.md`.
16. `sources/2026-W33/execution/handoffs/w33-selection-luna-r2.md`.
17. `sources/2026-W33/execution/sessions/w33-luna-selection-20260830-r1.md`.
18. `sources/2026-W33/execution/reviews/w33-selection-sol-review-20260830-r1.md`.
19. the exact Candidate Matrix and Candidate Selection.
20. this handoff.

If reviewed Core no longer provides equivalent Selection stage validation/bridge semantics, stop with `CORE_DRIFT_NEEDS_SOL_REVIEW`.

## 4. Core stage contract

At lifecycle `EVIDENCE_REVIEWED`, current Core requires exactly:

- `candidate-matrix`
- `candidate-selection`

The current-stage validator must validate the frozen Matrix against upstream accepted Evidence/View/Materiality/Completeness and validate the frozen Selection against the Matrix and exact basis hashes.

Expected deterministic stage transition:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

No other current-stage artifact is allowed.

## 5. Operator request

Create exactly:

`sources/2026-W33/execution/requests/w33-selection-advance-20260830-r1.json`

Use an offset-aware actual execution timestamp for `recorded_at`.

Required semantic payload:

```json
{
  "schema_version": "2.0-rc1",
  "request_id": "w33-selection-advance-20260830-r1",
  "issue_id": "2026-W33",
  "source_root": "sources/2026-W33",
  "work_branch": "weekly/2026-W33-v2-work",
  "reviewed_main_sha": "6267de3f6876f491950139757bfdf1085fc07bdc",
  "recorded_at": "<actual offset-aware execution time>",
  "operation": {
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
        "check_id": "SOL_SELECTION_SEMANTIC_REVIEW",
        "kind": "AGENT_RESEARCH",
        "executor": "ChatGPT GPT-5.6 Sol",
        "evidence": "ACCEPT / SELECTION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT. Sol reviewed the exact deterministic 37-row Candidate Matrix and complete 37-assignment Candidate Selection, including six fixed HOLDs, three justified rejects, single-home consolidation, PARTIAL-evidence boundaries, and the distinction between the 28 selected-candidate pool and later Architecture package count. Review authority: sources/2026-W33/execution/reviews/w33-selection-sol-review-20260830-r1.md."
      }
    ],
    "summary": "Adopt the Sol-reviewed W33 Candidate Matrix and Candidate Selection and advance exactly from EVIDENCE_REVIEWED to SELECTION_COMPLETE."
  }
}
```

Validate the request against current Core/schema before commit.

## 6. Request-only commit rule

The first worker commit must contain only:

`sources/2026-W33/execution/requests/w33-selection-advance-20260830-r1.json`

Record the canonical GitHub request commit SHA after non-force branch update.

Before executing the bridge, re-check the branch history is a direct descendant of the exact caller-supplied starting SHA and that the only worker change so far is the request file.

If native Git push is unavailable but the authenticated GitHub connection can create an equivalent commit/tree and move the ref non-force, use the established transport-reconstruction procedure. Clearly distinguish worker-local and canonical GitHub SHAs in the session record. Recovery always uses canonical GitHub SHAs.

No force push, rebase, merge, or history rewrite.

## 7. Canonical bridge execution

Execute equivalent to:

```bash
python scripts/survey_core_execution_bridge_v2.py \
  --repo-root . \
  --request sources/2026-W33/execution/requests/w33-selection-advance-20260830-r1.json \
  --event-sha <CANONICAL_REQUEST_COMMIT_SHA> \
  --ref-name weekly/2026-W33-v2-work
```

The bridge must validate the exact current State, Matrix, Selection, and Sol review and then generate the current Core advancement artifacts.

## 8. Expected generated paths

Expected bridge-run directory:

`sources/2026-W33/execution/bridge-runs/w33-selection-advance-20260830-r1/`

Expected files:

- `core-stage-contract.json`
- `reviews.json`
- `receipt.json`

Expected Stage Checkpoint:

`sources/2026-W33/orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json`

Expected changed State:

`sources/2026-W33/production-state.json`

Expected session record:

`sources/2026-W33/execution/sessions/w33-luna-selection-advance-20260830-r1.md`

No Architecture file is permitted.

## 9. Stage Checkpoint requirements

The canonical `EVIDENCE_REVIEWED` Stage Checkpoint must bind exactly:

- `candidate-matrix` -> `sources/2026-W33/candidate-matrix-v2.json`
- `candidate-selection` -> `sources/2026-W33/candidate-selection-v2.json`

Checkpoint set must be exactly:

- `selection`

Reviews must include at least:

1. `CORE_STAGE_CONTRACT = PASS`
2. `SOL_SELECTION_SEMANTIC_REVIEW = PASS`

No Architecture review or Human approval belongs in this checkpoint.

## 10. Expected post-State

After one and only one transition, Production State must be:

- lifecycle: `SELECTION_COMPLETE`
- next action: `stage:architecture`
- Discovery: passed
- Screening: passed
- Evidence: passed
- Materiality: passed
- Completeness: passed
- Selection: passed
- Architecture: pending
- Architecture Review: pending
- Draft and later checkpoints: pending
- terminal reason: null
- Exception Gate: inactive

Checkpoint provenance for Selection must point to the new canonical `EVIDENCE_REVIEWED` Stage Checkpoint.

State history must gain exactly one row:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

The history event SHA must be the canonical request commit SHA used by the bridge.

## 11. Required deterministic checks

At minimum verify:

1. remote starting HEAD exactly matches caller-supplied SHA before worker write;
2. pre-State SHA-256 equals `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`;
3. Matrix SHA-256 equals `1b660291564bda5f30debd86bb6911eb53edf06e8f735710f84652d972c4d198`;
4. Selection SHA-256 equals `9c6997d2ed3921a847db5e001ec9377189bb25d5475454593f23016308557005`;
5. Matrix/Selection schema and current-Core stage validation PASS;
6. request schema PASS;
7. request-only commit boundary PASS;
8. Core stage contract PASS for `EVIDENCE_REVIEWED -> SELECTION_COMPLETE`;
9. checkpoint schema/control PASS;
10. checkpoint artifacts and checkpoint set exact;
11. both required reviews PASS;
12. bridge receipt `ADVANCE_STAGE / PASS / SELECTION_COMPLETE`;
13. post-State agent-first validation PASS;
14. Selection checkpoint passed and Architecture still pending;
15. no Architecture/Draft/publication artifact created;
16. `git diff --check` PASS;
17. final changed paths remain inside this handoff's allowlist.

## 12. Allowed writes

Allowed worker-created/modified paths are only:

- `sources/2026-W33/execution/requests/w33-selection-advance-20260830-r1.json`
- `sources/2026-W33/execution/bridge-runs/w33-selection-advance-20260830-r1/core-stage-contract.json`
- `sources/2026-W33/execution/bridge-runs/w33-selection-advance-20260830-r1/reviews.json`
- `sources/2026-W33/execution/bridge-runs/w33-selection-advance-20260830-r1/receipt.json`
- `sources/2026-W33/orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json`
- `sources/2026-W33/production-state.json`
- `sources/2026-W33/execution/sessions/w33-luna-selection-advance-20260830-r1.md`

Do not modify Candidate Matrix or Candidate Selection.

## 13. Explicit prohibitions

Do not:

- change Selection assignments, rationales, roles, or Matrix rows;
- reopen Evidence, Materiality, Completeness, Screening, or Discovery;
- research new sources;
- create Issue Architecture;
- draft an editorial thesis, package plan, page plan, Architecture Review Summary, or review-attention artifact;
- run Architecture stage validation;
- advance beyond `SELECTION_COMPLETE`;
- resolve Architecture Review Human Gate;
- modify shared Core/config/schema/workflow code;
- force-push or rewrite history.

If any frozen semantic artifact fails deterministic validation, stop for Sol rather than repairing it.

## 14. Failure statuses

Use one of:

- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `STATE_DRIFT_NEEDS_SOL_REVIEW`
- `CORE_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`
- `TRANSPORT_FAILURE_NEEDS_SOL_REVIEW`

Do not improvise Architecture work around a failed Selection advancement.

## 15. Final report

Report at least:

- branch;
- exact supplied starting SHA;
- canonical GitHub request commit SHA;
- canonical GitHub result commit SHA;
- canonical GitHub final bookkeeping SHA;
- local SHAs separately if transport reconstruction occurred;
- exact changed paths;
- request/core/checkpoint/receipt validation results;
- pre/post State SHA-256;
- final lifecycle and next action;
- confirmation that Matrix/Selection were unchanged;
- confirmation that no Architecture work started.

Stop with:

`SELECTION_COMPLETE_READY_FOR_SOL_ARCHITECTURE_POLICY`
