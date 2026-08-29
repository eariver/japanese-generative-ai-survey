# 2026-W33 Sol→Luna handoff — Screening deterministic advancement r1

Status: `READY_FOR_LUNA / SCREENING_ADVANCEMENT_ONLY / STOP_AFTER_STATE_TRANSITION`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Sol/Luna policy authority: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`  
Screening materialization handoff: `sources/2026-W33/execution/handoffs/w33-screening-materialization-luna-r1.md`  
Sol Screening materialization review: `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`  
Current lifecycle at handoff creation: `DISCOVERY_COLLECTED`  
Current machine next action: `stage:screening`

The caller must give Luna the exact branch SHA containing this handoff and the Sol review above. Luna must begin from that exact SHA. If the branch has moved, stop and report drift instead of rebasing, merging, force-pushing, or selecting a new basis.

## 1. Objective

Execute only the deterministic Core transition for the already-Sol-reviewed Screening acceptance:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`

The task must:

1. bind the exact accepted Screening run reviewed by Sol;
2. create and validate the Core stage contract;
3. create the canonical Screening Stage Checkpoint;
4. advance Production State exactly one lifecycle transition;
5. record exact request/bridge/checkpoint/state provenance;
6. commit and push the deterministic advancement result;
7. stop for Sol verification before any Evidence / Materiality / Completeness research begins.

This task contains no new research and no new Screening, Materiality, Selection, or Architecture judgment.

## 2. Frozen advancement authority

### Accepted Screening artifact

Use exactly:

`sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json`

Expected accepted-run identity:

- result-set SHA-256: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- acceptance SHA-256: `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b`
- record count: 41
- batch count: 1
- KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4

### Sol review authority

Use exactly:

`sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`

Review decision:

`ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT`

The review also normalizes the local-vs-GitHub transport SHA discrepancy. Do not modify Screening bytes to address that historical transport note.

### Current State boundary

Before execution, Production State must still be:

- lifecycle: `DISCOVERY_COLLECTED`
- next action: `stage:screening`
- machine checkpoint `screening`: `pending`
- terminal reason: null

The current State Git blob before advancement is expected to remain the same as the S1 start/end blob until this task executes:

`7fb09e7b1b00f8c1fb8fde83d4516f2afd6f3b22`

If State differs semantically or the Screening checkpoint is already passed, stop with `STATE_DRIFT_NEEDS_SOL_REVIEW` rather than performing a second advancement.

## 3. Required authority reads

Read before writing, in this order:

1. `AGENTS.md` from reviewed `main`.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed `main`.
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed `main`.
4. `docs/survey-production-core-v2-operator-execution-bridge.md` from reviewed `main`.
5. `schemas/operator-execution-request-v2.schema.json` from reviewed `main`.
6. `scripts/survey_stage_validation_v2.py` from reviewed `main`.
7. `scripts/survey_agent_control_v2.py` from reviewed `main`.
8. `scripts/survey_core_execution_bridge_v2.py` from reviewed `main`.
9. `sources/2026-W33/production-profile.json` on the exact work-branch start.
10. `sources/2026-W33/production-state.json` on the exact work-branch start.
11. `sources/2026-W33/execution/index.md`.
12. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`.
13. `sources/2026-W33/execution/handoffs/w33-screening-materialization-luna-r1.md`.
14. `sources/2026-W33/execution/sessions/w33-luna-screening-materialization-20260830-r1.md`.
15. `sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md`.
16. this handoff.

If current reviewed-main Core no longer matches the exact authority above, stop with `CORE_DRIFT_NEEDS_SOL_REVIEW` before changing Production State.

## 4. Preflight invariants

Verify and record:

- branch is exactly `weekly/2026-W33-v2-work`;
- HEAD is exactly the caller-supplied SHA containing this handoff;
- reviewed main is still `6267de3f6876f491950139757bfdf1085fc07bdc`;
- current Screening acceptance exists at the frozen path;
- accepted run validates under the current stage-basis override used by Core;
- accepted result-set id is the frozen value above;
- Sol review exists and says `ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT`;
- Production State is `DISCOVERY_COLLECTED / stage:screening`;
- Screening checkpoint is pending;
- no Evidence/Materiality/Completeness current-stage artifacts are being supplied in this operation.

## 5. Preferred deterministic execution path

Use the existing operator bridge contract, following the already-successful W33 Discovery advancement pattern.

### Step A — request-only commit

Create one immutable operator request at:

`sources/2026-W33/execution/requests/w33-screening-advance-20260830-r1.json`

Use current schema `2.0-rc1` and this semantic payload shape:

```json
{
  "schema_version": "2.0-rc1",
  "request_id": "w33-screening-advance-20260830-r1",
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
        "path": "sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json"
      }
    ],
    "agent_reviews": [
      {
        "check_id": "SOL_SCREENING_SEMANTIC_REVIEW",
        "kind": "AGENT_RESEARCH",
        "executor": "ChatGPT GPT-5.6 Sol",
        "evidence": "ACCEPT / APPROVED_FOR_CORE_ADVANCEMENT. Sol independently reviewed the exact 41-record W33 Screening materialization, content-addressed result-set identity, duplicate and verification semantics, Core package/result/acceptance consistency, changed-path boundary, and unchanged Production State. Review authority: sources/2026-W33/execution/reviews/w33-screening-sol-review-20260830-r1.md."
      }
    ],
    "summary": "Adopt the Sol-reviewed 41-record 2026-W33 Screening acceptance and advance deterministically from DISCOVERY_COLLECTED to CANDIDATES_NORMALIZED."
  }
}
```

Validate this request against current schema before commit.

Commit the request **alone** first. Record that request commit SHA. Before updating the branch, confirm remote branch still equals the exact caller-supplied start SHA. Use a normal fast-forward update only.

### Step B — execute the bridge against the request commit

Run the canonical bridge from the request commit basis, equivalent to:

```bash
python scripts/survey_core_execution_bridge_v2.py \
  --repo-root . \
  --request sources/2026-W33/execution/requests/w33-screening-advance-20260830-r1.json \
  --event-sha <REQUEST_COMMIT_SHA> \
  --ref-name weekly/2026-W33-v2-work
```

Do not substitute a handcrafted Production State edit or handcrafted checkpoint.

The bridge must deterministically:

- validate the current stage using only `screening-acceptance` as the current artifact;
- bind prior Discovery checkpoint authority automatically;
- write a `CORE_STAGE_CONTRACT` PASS;
- record the Sol Screening semantic review row;
- build the canonical checkpoint for the `DISCOVERY_COLLECTED` producer stage;
- advance Production State exactly once;
- write a bridge receipt.

## 6. Expected generated paths

Under the normal bridge contract, expect at least:

- `sources/2026-W33/execution/requests/w33-screening-advance-20260830-r1.json`
- `sources/2026-W33/execution/bridge-runs/w33-screening-advance-20260830-r1/core-stage-contract.json`
- `sources/2026-W33/execution/bridge-runs/w33-screening-advance-20260830-r1/reviews.json`
- `sources/2026-W33/execution/bridge-runs/w33-screening-advance-20260830-r1/receipt.json`
- `sources/2026-W33/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`
- `sources/2026-W33/production-state.json`
- one Luna advancement session record under `sources/2026-W33/execution/sessions/`

Use a stable session name such as:

`sources/2026-W33/execution/sessions/w33-luna-screening-advance-20260830-r1.md`

If current Core legitimately chooses an equivalent canonical location, record the exact difference. Do not invent alternate paths to bypass Core.

## 7. Expected resulting State

After successful bridge execution, verify:

- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- machine checkpoint `discovery`: `passed`
- machine checkpoint `screening`: `passed`
- checkpoint provenance for `screening` points to the canonical `DISCOVERY_COLLECTED` Stage Checkpoint
- evidence/materiality/completeness checkpoints remain pending
- Human Architecture Review remains pending
- terminal reason remains null

The state history must contain one new transition:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`

bound to the implementation commit used by the deterministic bridge.

## 8. Required post-execution validation

Validate and record:

1. operator request schema passes;
2. Core stage-contract validation passes;
3. Stage Checkpoint validates under current schema and current agent-state validation;
4. checkpoint artifact `screening-acceptance` points to the exact Sol-reviewed acceptance and SHA;
5. checkpoint includes `CORE_STAGE_CONTRACT` deterministic PASS and `SOL_SCREENING_SEMANTIC_REVIEW` PASS;
6. bridge receipt says operation `ADVANCE_STAGE`, status `PASS`, and lifecycle `CANDIDATES_NORMALIZED`;
7. Production State validates as resumable;
8. `next_action` is exactly `stage:evidence-materiality-completeness`;
9. no Evidence/Materiality/Completeness/Selection/Architecture artifact was created;
10. branch update is fast-forward and no unrelated paths changed.

## 9. Git/commit boundary

Preferred commit sequence:

1. **request commit** — request JSON only;
2. **execution/result commit** — bridge-generated stage contract/reviews/receipt/checkpoint/Production State plus Luna advancement session record.

If transport reconstruction changes commit SHAs, preserve exact trees/content and report both local and GitHub canonical SHAs distinctly. Repository recovery must use GitHub canonical SHAs.

Do not force-push.

## 10. Luna advancement session record

Record at minimum:

- exact caller-supplied start SHA;
- request-only commit local/GitHub SHA as applicable;
- execution/result commit local/GitHub SHA as applicable;
- reviewed main SHA;
- request path and request SHA-256;
- accepted Screening path and SHA-256;
- Core stage-contract path/SHA and result;
- reviews path/SHA and included check IDs;
- Stage Checkpoint path/SHA;
- bridge receipt path/SHA;
- Production State before/after SHA-256;
- lifecycle/next_action before and after;
- exact changed paths for each commit;
- validation commands/results;
- any local-vs-remote transport identity mapping;
- final stop status.

Use final stop status:

`CANDIDATES_NORMALIZED_READY_FOR_SOL_EVIDENCE_POLICY`

or, on failure:

- `STATE_DRIFT_NEEDS_SOL_REVIEW`
- `CORE_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`
- `TRANSPORT_FAILURE_NEEDS_SOL_REVIEW`

## 11. Explicit prohibitions

Do not:

- reconsider or edit Screening decisions;
- edit the accepted Screening run;
- perform new source research;
- resolve INSPECT/MAYBE items;
- create Evidence cards or Evidence proposals;
- assign Materiality;
- perform Completeness analysis;
- make Selection or Architecture proposals;
- advance beyond `CANDIDATES_NORMALIZED`;
- invoke any Human Gate;
- modify shared Core implementation;
- silently resolve transport drift with force push or history rewrite.

## 12. Endpoint and next owner

Successful endpoint:

`CANDIDATES_NORMALIZED -> STOP FOR SOL`

After success, the next owner is Sol. Sol will verify the deterministic transition and then author the Evidence / Materiality / Completeness policy/rubric and the bounded Luna E-stage task matrix under the r3 operating model.
