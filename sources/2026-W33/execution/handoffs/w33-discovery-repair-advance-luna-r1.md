# 2026-W33 Sol→Luna handoff — repaired Discovery deterministic advancement r1

Status: `READY_FOR_LUNA / DISCOVERY_ADVANCEMENT_ONLY / STOP_AFTER_DISCOVERY_COLLECTED`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at specification time: `ISSUE_INITIALIZED`  
Current machine next action: `stage:discovery`

The caller supplies the exact branch SHA containing this handoff. Luna must verify that the remote branch HEAD equals that exact SHA before any write. If it does not, write nothing and stop with the actual remote HEAD.

## 1. Objective

Perform exactly one deterministic Core transition:

`ISSUE_INITIALIZED -> DISCOVERY_COLLECTED`

using a newly regenerated Discovery acceptance bound to the Sol-accepted repaired Discovery basis.

Stop immediately after the transition. Do not begin Screening in this task.

Expected success status:

`DISCOVERY_COLLECTED_READY_FOR_SOL_SCREENING_POLICY`

## 2. Frozen semantic authority

Sol review authority:

`sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`

Decision:

`ACCEPT / FIVE_CARRYOVER_SOURCE_AUTHORITY_REPAIRED / HANDOFF_ORIGIN_TYPO_CORRECTED / APPROVED_FOR_DISCOVERY_ADVANCEMENT`

Frozen repaired Discovery:

- path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`
- record count: `41`
- exact 41-ID set: preserved from the pre-revision Discovery

Frozen X Source Intake:

- path: `sources/2026-W33/external/x/x-source-intake-v2.json`
- SHA-256: `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`
- must remain byte-identical
- current complete validation must PASS

Frozen pre-State:

- path: `sources/2026-W33/production-state.json`
- SHA-256: `0f5b14d6f8afc85605fc621b88e9c4005f70e13e7dbc727f68dae2cc5ca4d56c`
- lifecycle: `ISSUE_INITIALIZED`
- next action: `stage:discovery`
- all machine checkpoints: pending
- Architecture Review Human Gate: pending
- terminal reason: null

## 3. Important stale-artifact condition

The repository currently contains:

`sources/2026-W33/discovery/discovery-accepted-v2.json`

but that file is stale. It binds the pre-repair Discovery SHA-256:

`632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`

It is **not** valid advancement authority after the five-carry-over repair.

You must regenerate and replace the canonical acceptance so that it binds:

- repaired Discovery SHA-256 `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`;
- unchanged X manifest SHA-256 `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`.

Current `scripts.survey_discovery_v2.build_acceptance(...)` refuses to overwrite an existing output. Therefore use a safe local procedure such as:

1. build and validate the new acceptance at a temporary path outside the repository; then
2. replace the canonical repository file with those validated bytes;
3. validate the canonical replacement with `validate_acceptance(...)`;
4. commit only the canonical acceptance replacement in the acceptance-materialization commit.

Do not delete the canonical acceptance in a separate commit. Do not preserve the stale acceptance merely because the path already exists.

## 4. Required authority reads

Read before writing:

1. reviewed-main `AGENTS.md`;
2. reviewed-main `docs/survey-production-core-v2-session-bootstrap.md`;
3. reviewed-main `docs/survey-production-core-v2-execution-record-policy.md`;
4. reviewed-main `scripts/survey_discovery_v2.py`;
5. reviewed-main operator request schema and operator bridge policy/implementation used by current Core;
6. current `sources/2026-W33/production-state.json`;
7. repaired `sources/2026-W33/discovery/discovery-v2.jsonl`;
8. `sources/2026-W33/external/x/x-source-intake-v2.json`;
9. stale `sources/2026-W33/discovery/discovery-accepted-v2.json` only to confirm that it is stale;
10. `sources/2026-W33/execution/reviews/w33-discovery-carryover-repair-sol-review-20260830-r1.md`;
11. prior successful W33 Discovery request/bridge records only as syntax/transport precedent, especially request `w33-discovery-advance-20260829-r1`.

## 5. Acceptance materialization commit

Before the operator request, create one normal fast-forward commit that changes only:

`sources/2026-W33/discovery/discovery-accepted-v2.json`

The regenerated acceptance must:

- validate under current reviewed-main Core;
- record exactly 41 Discovery records;
- bind the repaired Discovery SHA-256 exactly;
- bind the unchanged X Source Intake SHA-256 exactly;
- contain a graph that rebuilds exactly from current Discovery + Raw bytes;
- bind the ten new carry-over Raw captures through the five repaired records;
- preserve the actual repaired provenance origin `GAP_FILL` for those five records;
- contain no stale reference to the old Discovery SHA `632ba233...`.

After committing the acceptance replacement, re-read the remote branch HEAD and require that it equals the acceptance-materialization commit before proceeding.

## 6. Request-only commit

Create exactly:

`sources/2026-W33/execution/requests/w33-discovery-repair-advance-20260830-r1.json`

Request identity:

- `request_id`: `w33-discovery-repair-advance-20260830-r1`
- `issue_id`: `2026-W33`
- `source_root`: `sources/2026-W33`
- `work_branch`: `weekly/2026-W33-v2-work`
- `reviewed_main_sha`: `6267de3f6876f491950139757bfdf1085fc07bdc`

Operation:

- `kind`: `ADVANCE_STAGE`
- `expected_from_state`: `ISSUE_INITIALIZED`
- `state_path`: `sources/2026-W33/production-state.json`
- artifacts exactly:
  - name `discovery-acceptance`
  - path `sources/2026-W33/discovery/discovery-accepted-v2.json`

Agent review exactly one Sol semantic review is sufficient:

- `check_id`: `SOL_DISCOVERY_REPAIR_SEMANTIC_REVIEW`
- `kind`: `AGENT_RESEARCH`
- `executor`: `ChatGPT GPT-5.6 Sol`
- evidence must bind the Sol review path and its ACCEPT decision above.

Suggested summary:

`Adopt the Sol-reviewed repaired 41-record W33 Discovery graph and unchanged COMPLETE X Source Intake, then advance deterministically from ISSUE_INITIALIZED to DISCOVERY_COLLECTED.`

The request commit must be **request-only** relative to its parent. No acceptance byte may change in the request commit.

Before dispatch, prove:

- parent = exact acceptance-materialization commit;
- request commit is exactly one commit ahead;
- changed path from parent to request commit is exactly the request JSON;
- remote branch HEAD equals the request commit;
- reviewed `main` remains `6267de3f6876f491950139757bfdf1085fc07bdc`.

## 7. Canonical operator bridge

Dispatch the request through the existing canonical Survey Production Core v2 operator bridge using the same trusted transport used by the prior W33 advancement requests.

Do not execute the state mutation by directly editing `production-state.json`.

Do not bypass bridge preflight if it fails.

After dispatch, wait only in the sense of synchronously observing the workflow within this task; do not return success until the bridge result has been read back from GitHub.

Expected bridge run directory:

`sources/2026-W33/execution/bridge-runs/w33-discovery-repair-advance-20260830-r1/`

Expected generated bridge files include the current bridge contract set, normally:

- `core-stage-contract.json`
- `reviews.json`
- `receipt.json`

Expected checkpoint:

`sources/2026-W33/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`

Expected review results include at least:

- `CORE_STAGE_CONTRACT = PASS`
- `SOL_DISCOVERY_REPAIR_SEMANTIC_REVIEW = PASS`

Expected receipt:

- operation: `ADVANCE_STAGE`
- status: `PASS`
- lifecycle state: `DISCOVERY_COLLECTED`

## 8. Expected post-State

After successful Core execution, require:

- lifecycle: `DISCOVERY_COLLECTED`
- next action: `stage:screening`
- terminal reason: null
- Exception Gate inactive
- Discovery machine checkpoint: passed
- Screening: pending
- Evidence: pending
- Materiality: pending
- Completeness: pending
- Selection: pending
- Architecture: pending
- Human Architecture Review: pending
- Publication Preview Human Gate: pending

History must contain exactly the initialized history plus one new transition:

`ISSUE_INITIALIZED -> DISCOVERY_COLLECTED`

The transition repository/event SHA must equal the canonical request commit SHA, according to current Core semantics.

No later transition is allowed in this task.

## 9. Checkpoint requirements

The new `ISSUE_INITIALIZED.json` checkpoint must bind the newly regenerated Discovery acceptance, not the historical pre-repair acceptance.

At minimum verify:

- artifact set is the current Discovery-stage set expected by Core;
- `discovery-acceptance` path is canonical;
- its hash is the new acceptance hash;
- request event SHA is the canonical request commit;
- stage/review checks are PASS;
- no stale checkpoint from the previous pre-r2 run is being reused.

## 10. Protected paths and semantics

During this deterministic advancement, do not modify:

- repaired `sources/2026-W33/discovery/discovery-v2.jsonl`;
- any Raw capture;
- `sources/2026-W33/external/x/x-source-intake-v2.json` or X Raw;
- Screening results/packages;
- Evidence / Edition Views / Materiality / Completeness;
- Matrix / Selection / Architecture;
- Human Gate review records/index;
- shared Core/config/schema;
- publication/Draft artifacts.

The five carry-over findings are already semantically frozen by Sol. Do not reinterpret them here.

## 11. Allowed writes

Across the complete Luna task, allowed edition-local changes are limited to:

1. `sources/2026-W33/discovery/discovery-accepted-v2.json`
2. `sources/2026-W33/execution/requests/w33-discovery-repair-advance-20260830-r1.json`
3. files generated by the canonical bridge under `sources/2026-W33/execution/bridge-runs/w33-discovery-repair-advance-20260830-r1/`
4. `sources/2026-W33/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`
5. `sources/2026-W33/production-state.json`
6. `sources/2026-W33/execution/sessions/w33-luna-discovery-repair-advance-20260830-r1.md`

No other path may change.

## 12. Luna session record

Create:

`sources/2026-W33/execution/sessions/w33-luna-discovery-repair-advance-20260830-r1.md`

It must record:

- supplied Starting SHA and verified remote Starting SHA;
- acceptance-materialization commit SHA;
- new Discovery acceptance SHA-256;
- confirmation it binds repaired Discovery SHA `6e6590b5...` and unchanged X SHA `4e90919e...`;
- request commit SHA;
- bridge result commit SHA;
- final bookkeeping commit SHA reported externally/read back rather than self-embedded if necessary;
- reviewed-main SHA;
- pre-State SHA-256 and post-State SHA-256;
- bridge contract/reviews/receipt PASS results;
- checkpoint path/SHA-256;
- exact lifecycle transition;
- changed-path allowlist result;
- confirmation that Screening was not started;
- confirmation that Discovery JSONL/Raw/X were byte-identical throughout this advancement.

Preferred commit shape:

1. acceptance-materialization commit;
2. request-only commit;
3. bridge-generated result commit;
4. final bookkeeping commit containing only the Luna session record.

All branch pushes/updates must be normal fast-forward / `force=false`.

## 13. Stop conditions

Stop without writes if the starting remote HEAD does not equal the supplied Exact Starting SHA.

After work starts, stop and report rather than broadening scope if:

- repaired Discovery SHA differs from `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd` before acceptance materialization;
- X manifest SHA differs from `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`;
- pre-State differs from the frozen `ISSUE_INITIALIZED` basis;
- the regenerated acceptance fails current-Core validation;
- request-only preflight cannot be satisfied;
- canonical bridge rejects the request;
- Core generates a transition other than `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED`;
- a non-allowlisted path would need modification.

Use a precise failure status such as:

- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `STATE_DRIFT_NEEDS_SOL_REVIEW`
- `DISCOVERY_ACCEPTANCE_FAILURE_NEEDS_SOL_REVIEW`
- `CORE_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`
- `TRANSPORT_FAILURE_NEEDS_SOL_REVIEW`

## 14. Success condition

Success is exactly:

`DISCOVERY_COLLECTED_READY_FOR_SOL_SCREENING_POLICY`

At success, State is `DISCOVERY_COLLECTED / stage:screening`, and Screening has not begun.
