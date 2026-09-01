# 2026-W33 Sol→Luna handoff — Evidence / Materiality / Completeness deterministic advancement r1

Status: `READY_FOR_LUNA / EVIDENCE_MATERIALITY_COMPLETENESS_ADVANCEMENT_ONLY / STOP_AFTER_STATE_TRANSITION`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Sol/Luna policy authority: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`  
Sol acceptance authority: `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`  
Current lifecycle at handoff creation: `CANDIDATES_NORMALIZED`  
Current machine next action: `stage:evidence-materiality-completeness`

The caller must supply the exact branch SHA containing this handoff, the Sol r2 acceptance review, and the recovery-index update that points here. Luna must start from that exact SHA. If the branch moved before execution starts, stop with `STATE_DRIFT_NEEDS_SOL_REVIEW`; do not silently rebase, merge, select a newer basis, or force-push.

## 1. Objective

Perform only the deterministic Core transition for the already-Sol-reviewed W33 Evidence / Materiality / Completeness authority:

`CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED`

This task must:

1. bind the exact frozen Evidence acceptance;
2. bind the exact Sol-accepted repaired Edition View acceptance;
3. bind the exact deterministic Materiality Ledger;
4. bind the exact accepted Profile Completeness, including its explicit `INCOMPLETE` status;
5. create/validate the current Core stage contract;
6. create the canonical `CANDIDATES_NORMALIZED` Stage Checkpoint carrying all three stage checkpoints: `evidence`, `materiality`, `completeness`;
7. advance Production State exactly one lifecycle transition;
8. record exact request/bridge/checkpoint/State provenance;
9. commit/push the deterministic result;
10. stop for Sol verification before Selection begins.

There is no new research or semantic reconsideration in this task.

## 2. Frozen semantic authority

### Sol acceptance

Use exactly:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`

Decision:

`ACCEPT / REPAIR_VERIFIED / EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

### Evidence acceptance

Path:

`sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/evidence-accepted.json`

Expected identity:

- Evidence result-set: `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524`
- Evidence acceptance SHA-256: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- result count: 37
- statuses: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

### Repaired Edition View acceptance

Path:

`sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/edition-views-accepted.json`

Expected identity:

- View set: `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f`
- acceptance SHA-256: `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`
- View count: 37
- materiality: MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0

### Materiality Ledger

Path:

`sources/2026-W33/materiality-ledger-v2.json`

Expected SHA-256:

`cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`

Expected row count: 41.

### Profile Completeness

Path:

`sources/2026-W33/profile-completeness-v2.json`

Expected SHA-256:

`9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`

Expected semantics:

- overall: `INCOMPLETE`
- `weekly:current-relevance`: `LIMITATION`
- `weekly:technical-significance`: `LIMITATION`
- `weekly:carry-over`: `NEEDS_RESEARCH`

Do not attempt to convert this to `READY`. Sol explicitly accepted this as a bounded limitation.

## 3. Current State boundary

Before execution, Production State must still be:

- lifecycle: `CANDIDATES_NORMALIZED`
- next action: `stage:evidence-materiality-completeness`
- `evidence`: pending
- `materiality`: pending
- `completeness`: pending
- `selection`: pending
- Architecture Review: pending
- terminal reason: null

Expected pre-advance Production State SHA-256:

`bc7d2cad5a2a53634b3eeaab12336dfd4a3c56e1db8677534c8dc5b03f60ba6f`

If lifecycle/checkpoint semantics differ, stop. Do not perform a second or compensating advancement.

## 4. Required authority reads

Before writing, read in order:

1. `AGENTS.md` from reviewed `main`.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed `main`.
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed `main`.
4. `docs/survey-production-core-v2-operator-execution-bridge.md` from reviewed `main`.
5. `schemas/operator-execution-request-v2.schema.json` from reviewed `main`.
6. `scripts/survey_stage_validation_v2.py` from reviewed `main`.
7. `scripts/survey_agent_control_v2.py` from reviewed `main`.
8. `scripts/survey_core_execution_bridge_v2.py` from reviewed `main`.
9. `sources/2026-W33/production-profile.json`.
10. `sources/2026-W33/production-state.json`.
11. `sources/2026-W33/execution/index.md`.
12. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`.
13. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-review-20260830-r1.md`.
14. `sources/2026-W33/execution/handoffs/w33-evidence-view-semantic-repair-luna-r1.md`.
15. `sources/2026-W33/execution/sessions/w33-luna-evidence-view-semantic-repair-20260830-r1.md`.
16. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md`.
17. the four frozen advancement artifacts listed above.
18. this handoff.

If reviewed-main Core or exact repository authority conflicts with this handoff, stop with `CORE_DRIFT_NEEDS_SOL_REVIEW` rather than altering semantic artifacts.

## 5. Preflight invariants

Verify and record:

- branch is exactly `weekly/2026-W33-v2-work`;
- HEAD equals the caller-supplied exact starting SHA;
- reviewed main is still `6267de3f6876f491950139757bfdf1085fc07bdc`;
- Sol r2 review contains the exact ACCEPT decision above;
- all four frozen artifacts exist and match the expected SHA-256 values/identities;
- Production State is exactly `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`;
- Evidence/Materiality/Completeness checkpoints are all pending;
- no Selection artifact is supplied as a current-stage artifact;
- a current-stage validation using exactly the four frozen artifacts passes for target `EVIDENCE_REVIEWED`.

## 6. Operator request

Create one immutable request at:

`sources/2026-W33/execution/requests/w33-evidence-materiality-completeness-advance-20260830-r1.json`

Use current schema `2.0-rc1` and this semantic shape:

```json
{
  "schema_version": "2.0-rc1",
  "request_id": "w33-evidence-materiality-completeness-advance-20260830-r1",
  "issue_id": "2026-W33",
  "source_root": "sources/2026-W33",
  "work_branch": "weekly/2026-W33-v2-work",
  "reviewed_main_sha": "6267de3f6876f491950139757bfdf1085fc07bdc",
  "recorded_at": "<actual offset-aware execution time>",
  "operation": {
    "kind": "ADVANCE_STAGE",
    "expected_from_state": "CANDIDATES_NORMALIZED",
    "state_path": "sources/2026-W33/production-state.json",
    "artifacts": [
      {
        "name": "evidence-acceptance",
        "path": "sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/evidence-accepted.json"
      },
      {
        "name": "edition-views-acceptance",
        "path": "sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/edition-views-accepted.json"
      },
      {
        "name": "materiality-ledger",
        "path": "sources/2026-W33/materiality-ledger-v2.json"
      },
      {
        "name": "profile-completeness",
        "path": "sources/2026-W33/profile-completeness-v2.json"
      }
    ],
    "agent_reviews": [
      {
        "check_id": "SOL_EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTIC_REVIEW",
        "kind": "AGENT_RESEARCH",
        "executor": "ChatGPT GPT-5.6 Sol",
        "evidence": "ACCEPT / REPAIR_VERIFIED / EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT. Sol reviewed the frozen 37-result Evidence authority, all 37 repaired candidate-specific Weekly Edition Evidence Views, the deterministic 41-row Materiality Ledger, and the valid Profile Completeness including explicit INCOMPLETE limitations. No source expansion or upstream rewind is required. Review authority: sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-sol-rereview-20260830-r2.md."
      }
    ],
    "summary": "Adopt the Sol-reviewed W33 Evidence, repaired Edition Views, deterministic Materiality Ledger, and explicit Profile Completeness limitations, then advance exactly from CANDIDATES_NORMALIZED to EVIDENCE_REVIEWED."
  }
}
```

Validate the request against the current schema.

Commit the request alone first. Record the canonical request commit SHA. Before branch update, verify remote branch still equals the exact supplied starting SHA. Use normal fast-forward only.

## 7. Execute canonical bridge

From the request-commit basis, use the canonical operator bridge equivalent to:

```bash
python scripts/survey_core_execution_bridge_v2.py \
  --repo-root . \
  --request sources/2026-W33/execution/requests/w33-evidence-materiality-completeness-advance-20260830-r1.json \
  --event-sha <CANONICAL_REQUEST_COMMIT_SHA> \
  --ref-name weekly/2026-W33-v2-work
```

Do not hand-edit Production State or handcrafted checkpoint bytes.

The bridge must validate exactly the four current-stage artifacts, include the Sol semantic review, build the canonical checkpoint, and advance State once.

## 8. Expected generated paths

Expect the normal bridge outputs:

- request above;
- `sources/2026-W33/execution/bridge-runs/w33-evidence-materiality-completeness-advance-20260830-r1/core-stage-contract.json`;
- `sources/2026-W33/execution/bridge-runs/w33-evidence-materiality-completeness-advance-20260830-r1/reviews.json`;
- `sources/2026-W33/execution/bridge-runs/w33-evidence-materiality-completeness-advance-20260830-r1/receipt.json`;
- canonical checkpoint `sources/2026-W33/orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json`;
- updated `sources/2026-W33/production-state.json`;
- one Luna advancement session record.

Preferred session path:

`sources/2026-W33/execution/sessions/w33-luna-evidence-materiality-completeness-advance-20260830-r1.md`

If current Core chooses an equivalent canonical generated path, record the exact path. Do not invent a noncanonical substitute.

## 9. Expected checkpoint semantics

The single canonical `CANDIDATES_NORMALIZED` Stage Checkpoint must have:

- from state: `CANDIDATES_NORMALIZED`
- to state: `EVIDENCE_REVIEWED`
- checkpoint set exactly: `evidence`, `materiality`, `completeness`
- exact four artifacts from this handoff
- deterministic `CORE_STAGE_CONTRACT` PASS
- `SOL_EVIDENCE_MATERIALITY_COMPLETENESS_SEMANTIC_REVIEW` PASS
- current contract/implementation provenance as Core derives it.

After advancement, Production State checkpoint provenance for `evidence`, `materiality`, and `completeness` should all resolve to this canonical Stage Checkpoint, according to current Core behavior.

## 10. Expected post-state

After successful execution verify:

- lifecycle: `EVIDENCE_REVIEWED`
- next action: `stage:selection`
- discovery: passed
- screening: passed
- evidence: passed
- materiality: passed
- completeness: passed
- selection: pending
- architecture: pending
- Architecture Review: pending
- terminal reason: null

State history must gain exactly one transition:

`CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED`

bound to the implementation/event provenance produced by the bridge.

## 11. Required post-execution validation

Record all of the following:

1. request schema PASS;
2. exact pre-state match PASS;
3. four frozen artifact hashes/identities PASS;
4. current-stage validation PASS;
5. Core stage-contract PASS;
6. Stage Checkpoint schema/control validation PASS;
7. checkpoint artifact bindings are exact;
8. checkpoint contains all three stage checkpoint names;
9. Sol semantic review appears as PASS;
10. bridge receipt says `ADVANCE_STAGE / PASS / EVIDENCE_REVIEWED`;
11. Production State is safely resumable under the current agent-first path;
12. next action is exactly `stage:selection`;
13. no Selection/Architecture/Draft artifact was created;
14. branch history is fast-forward with no force and no unrelated path changes.

If the standalone legacy state-basis probe still reports the already-known historical checkpoint-layout mismatch while the prescribed current stage/agent-first validator passes, record it as the pre-existing nonblocking maintenance boundary. Do not repair State/Core in this task.

## 12. Git boundary

Preferred sequence:

1. request-only commit;
2. deterministic bridge/result commit containing generated stage contract, reviews, receipt, checkpoint, Production State, and Luna advancement session.

If a bookkeeping session requires a third commit under the actual transport implementation, that is acceptable if exact path boundaries and SHA mapping are recorded.

If authenticated GitHub transport reconstructs commits and local SHA differs from canonical remote SHA, preserve tree/content identity, report both, and use GitHub canonical SHAs for recovery.

Never force-push.

## 13. Luna advancement session record

Record at minimum:

- caller-supplied exact starting SHA;
- clone/checkout verification;
- reviewed main SHA;
- local and canonical request commit identities if different;
- local and canonical execution/result commit identities if different;
- request path/SHA-256;
- exact four stage artifact paths/SHA-256 values;
- Core stage-contract path/SHA/result;
- reviews path/SHA/check IDs;
- Stage Checkpoint path/SHA/checkpoint set;
- bridge receipt path/SHA/result;
- Production State before/after SHA-256;
- lifecycle and next_action before/after;
- exact changed paths per commit;
- validation results;
- any transport SHA mapping;
- final stop status.

Successful stop status:

`EVIDENCE_REVIEWED_READY_FOR_SOL_SELECTION_POLICY`

Failure statuses:

- `STATE_DRIFT_NEEDS_SOL_REVIEW`
- `CORE_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`
- `TRANSPORT_FAILURE_NEEDS_SOL_REVIEW`

## 14. Explicit prohibitions

Do not:

- acquire or inspect new external Evidence sources;
- change Discovery or Screening;
- change accepted Evidence/Card bytes;
- change repaired View bytes;
- change Materiality Ledger or Profile Completeness;
- reinterpret the accepted `INCOMPLETE` status;
- create Candidate Matrix or Candidate Selection;
- begin Selection reasoning;
- create Architecture/Draft/publication artifacts;
- invoke any Human Gate;
- modify shared Core/config/schema/workflow files;
- advance beyond `EVIDENCE_REVIEWED`;
- force-push or rewrite branch history.

## 15. Endpoint

Successful endpoint:

`EVIDENCE_REVIEWED -> STOP FOR SOL`

The next owner is Sol. Sol will verify the deterministic transition and then define the Selection rubric and bounded Luna Selection proposal task.