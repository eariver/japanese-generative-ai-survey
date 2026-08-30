# 2026-W33 Sol→Luna handoff — revised Screening deterministic advancement r1

Status: `READY_FOR_LUNA / SCREENING_REVISION_ADVANCEMENT_ONLY / STOP_AFTER_STATE_TRANSITION`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at specification time: `DISCOVERY_COLLECTED`  
Current machine next action: `stage:screening`

The caller supplies the exact branch SHA containing this handoff and its Sol review. Luna must verify that the remote branch HEAD equals that exact SHA before any write. If it differs, write nothing and stop with the actual remote HEAD.

## 1. Objective

Execute exactly one deterministic Core transition for the Sol-reviewed revised Screening acceptance:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`

This task contains no new research and no new Screening judgment.

Successful stop:

`CANDIDATES_NORMALIZED_READY_FOR_SOL_EVIDENCE_REVISION_POLICY`

Do not begin Evidence / Materiality / Completeness work in this task.

## 2. Frozen revised Screening authority

Use exactly:

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json`

Frozen identities:

- result-set identity: `0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a`
- acceptance SHA-256: `e6f0392004191b4668e4231c57839044e4b08ff1e32763403f2d92630b0b0a0f`
- package SHA-256: `047f595c0b8216a780c4b5c11d9e0cfa9a263e5ec35aa4287f15aae82bdfbd46`
- record count: `41`
- batch count: `1`
- decision counts: `KEEP 31 / INSPECT 3 / MAYBE 3 / DROP 4`

Package basis must remain:

- profile SHA-256: `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`
- State SHA-256: `6ef1fb8724989ed69251bef0a77421339933133feccb21781fa688f0b17f997d`
- repaired Discovery SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`

Historical accepted Screening result-set `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706` is historical only and must not be used as the current stage artifact.

## 3. Sol review authority

Use exactly:

`sources/2026-W33/execution/reviews/w33-screening-revision-sol-review-20260830-r1.md`

Decision:

`ACCEPT / SCREENING_REVISION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

The review freezes the 36 exact carry-forward decisions and the five repaired `KEEP / high` decisions. Do not modify any Screening bytes.

## 4. Current State boundary

Before execution require:

- lifecycle: `DISCOVERY_COLLECTED`
- next action: `stage:screening`
- discovery checkpoint: `passed`
- screening checkpoint: `pending`
- evidence/materiality/completeness/selection/architecture checkpoints: `pending`
- Architecture Review Human Gate: `pending`
- terminal reason: `null`
- exception gate: inactive

Current pre-advancement State SHA-256 must be:

`6ef1fb8724989ed69251bef0a77421339933133feccb21781fa688f0b17f997d`

If State differs semantically or Screening is already passed, stop rather than performing a second transition.

## 5. Required reads

Read before writing:

1. reviewed-main `AGENTS.md`;
2. reviewed-main `docs/survey-production-core-v2-session-bootstrap.md`;
3. reviewed-main `docs/survey-production-core-v2-execution-record-policy.md`;
4. reviewed-main `docs/survey-production-core-v2-operator-execution-bridge.md`;
5. reviewed-main `schemas/operator-execution-request-v2.schema.json`;
6. reviewed-main `scripts/survey_stage_validation_v2.py`;
7. reviewed-main `scripts/survey_agent_control_v2.py`;
8. reviewed-main `scripts/survey_core_execution_bridge_v2.py`;
9. `sources/2026-W33/production-profile.json`;
10. `sources/2026-W33/production-state.json`;
11. `sources/2026-W33/discovery/discovery-accepted-v2.json`;
12. current `sources/2026-W33/execution/index.md`;
13. `sources/2026-W33/execution/sessions/w33-luna-screening-revision-20260830-r1.md`;
14. `sources/2026-W33/execution/reviews/w33-screening-revision-sol-review-20260830-r1.md`;
15. the revised accepted Screening run above;
16. this handoff.

If reviewed-main Core or the frozen artifacts drift, stop with `CORE_OR_AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 6. Preflight invariants

Verify and record:

- remote branch HEAD equals caller-supplied Starting SHA exactly;
- reviewed `main` remains `6267de3f6876f491950139757bfdf1085fc07bdc`;
- revised Screening acceptance exists and SHA-256 is exact;
- canonical Screening validation passes under the current stage-basis override used by Core;
- result-set directory name equals its `result_set_sha256`;
- package basis binds current repaired Discovery and current State;
- Sol review exists with the exact decision above;
- no Evidence/Materiality/Completeness artifact is supplied to this operation.

## 7. Operator request

Create one request-only commit containing exactly:

`sources/2026-W33/execution/requests/w33-screening-revision-advance-20260830-r1.json`

Use request id:

`w33-screening-revision-advance-20260830-r1`

Semantic payload:

```json
{
  "schema_version": "2.0-rc1",
  "request_id": "w33-screening-revision-advance-20260830-r1",
  "issue_id": "2026-W33",
  "source_root": "sources/2026-W33",
  "work_branch": "weekly/2026-W33-v2-work",
  "reviewed_main_sha": "6267de3f6876f491950139757bfdf1085fc07bdc",
  "recorded_at": "<actual offset-aware execution time>",
  "operation": {
    "kind": "ADVANCE_STAGE",
    "expected_from_state": "DISCOVERY_COLLECTED",
    "state_path": "sources/2026-W33/production-state.json",
    "artifacts": [
      {
        "name": "screening-acceptance",
        "path": "sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json"
      }
    ],
    "agent_reviews": [
      {
        "check_id": "SOL_SCREENING_REVISION_SEMANTIC_REVIEW",
        "kind": "AGENT_RESEARCH",
        "executor": "ChatGPT GPT-5.6 Sol",
        "evidence": "ACCEPT / SCREENING_REVISION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT. Review authority: sources/2026-W33/execution/reviews/w33-screening-revision-sol-review-20260830-r1.md."
      }
    ],
    "summary": "Adopt the Sol-reviewed revised 41-record W33 Screening acceptance based on repaired Discovery and advance deterministically from DISCOVERY_COLLECTED to CANDIDATES_NORMALIZED."
  }
}
```

Validate against current schema before commit.

The request commit must contain the request JSON only. Before pushing it, recheck that the remote branch still equals the supplied Starting SHA. Push by normal fast-forward only (`force=false`).

## 8. Canonical bridge execution

Dispatch the request commit through the existing canonical Survey Production Core v2 operator bridge. Follow the same Issue #448 transport pattern used by prior successful W33 stage transitions.

The bridge must, without handcrafted State/checkpoint edits:

- validate current stage contract;
- bind the existing Discovery checkpoint automatically;
- validate the revised Screening acceptance;
- record `CORE_STAGE_CONTRACT = PASS`;
- record `SOL_SCREENING_REVISION_SEMANTIC_REVIEW = PASS`;
- create the canonical `DISCOVERY_COLLECTED` producer-stage checkpoint;
- advance Production State exactly once;
- emit the bridge receipt.

## 9. Expected generated paths

Expect the canonical equivalents of:

- `sources/2026-W33/execution/requests/w33-screening-revision-advance-20260830-r1.json`
- `sources/2026-W33/execution/bridge-runs/w33-screening-revision-advance-20260830-r1/core-stage-contract.json`
- `sources/2026-W33/execution/bridge-runs/w33-screening-revision-advance-20260830-r1/reviews.json`
- `sources/2026-W33/execution/bridge-runs/w33-screening-revision-advance-20260830-r1/receipt.json`
- `sources/2026-W33/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`
- `sources/2026-W33/production-state.json`
- `sources/2026-W33/execution/sessions/w33-luna-screening-revision-advance-20260830-r1.md`

If Core chooses an equivalent canonical location, record it rather than inventing alternate paths.

## 10. Expected resulting State

After a successful transition verify:

- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- discovery checkpoint: `passed`
- screening checkpoint: `passed`
- evidence/materiality/completeness/selection/architecture checkpoints: `pending`
- Architecture Review Human Gate: `pending`
- terminal reason: `null`
- exception gate: inactive

History must add exactly one transition:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`

bound to the request/event commit SHA used by the bridge.

## 11. Required post-validation

Verify and record:

1. request schema PASS;
2. bridge preflight PASS;
3. Core executor PASS;
4. stage contract PASS;
5. Sol review check PASS;
6. checkpoint artifact path/SHA points to the exact revised Screening acceptance;
7. bridge receipt status PASS and lifecycle `CANDIDATES_NORMALIZED`;
8. Production State is valid and resumable;
9. no new Evidence/View/Materiality/Completeness/Selection/Architecture artifact exists from this task;
10. branch updates are normal fast-forwards only.

## 12. Session record

Create only after successful bridge execution:

`sources/2026-W33/execution/sessions/w33-luna-screening-revision-advance-20260830-r1.md`

Record:

- supplied and verified Starting SHA;
- reviewed-main SHA;
- request commit SHA and parent;
- request path/SHA-256;
- revised Screening acceptance path/SHA-256/result-set identity;
- bridge workflow/run if exposed;
- bridge output commit and parent;
- stage-contract/reviews/receipt/checkpoint paths and SHA-256;
- State before/after SHA-256;
- exact lifecycle and next_action before/after;
- exact changed paths;
- validation results;
- final remote SHA;
- no Evidence work performed.

## 13. Prohibitions

Do not:

- edit Discovery or Screening bytes;
- use the historical Screening result-set as current authority;
- perform source research;
- create or edit Evidence cards/tasks/results;
- assign Materiality or Completeness;
- change Selection or Architecture;
- add the weekly synthesis chapter yet;
- advance beyond `CANDIDATES_NORMALIZED`;
- invoke a Human Gate;
- modify shared Core;
- force-push, rebase, or rewrite history.

## 14. Stop conditions

Stop without write on Starting SHA mismatch.

Stop after request commit without bypass if bridge preflight or executor fails. Report the exact failure as:

`SCREENING_REVISION_ADVANCEMENT_BLOCKED_NEEDS_SOL_REVIEW`

Successful endpoint is exactly:

`CANDIDATES_NORMALIZED_READY_FOR_SOL_EVIDENCE_REVISION_POLICY`
