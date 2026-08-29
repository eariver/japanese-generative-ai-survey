# 2026-W33 Sol→Luna handoff — Screening materialization r1

Status: `READY_FOR_LUNA / SCREENING_MATERIALIZATION_ONLY / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical work branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Handoff policy authority: `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`  
Current lifecycle at handoff creation: `DISCOVERY_COLLECTED`  
Current machine next action: `stage:screening`  
Requested Human stop: `ARCHITECTURE_REVIEW`

The caller must give Luna the exact branch commit SHA that contains this handoff. Luna must start from that exact SHA and must not silently rebase, merge, or switch to a later branch state. If the branch has moved before execution starts, Luna must stop and report the drift to Sol rather than choosing a new basis itself.

## 1. Objective

Materialize the **current Core v2 Screening accepted run** for 2026-W33 from the exact already-reviewed Sol semantic Screening seed.

This task is intentionally narrow. It performs no new research and makes no new Screening judgment.

The endpoint is:

- current-Core Screening package/result/acceptance artifacts committed on the canonical work branch;
- an exact Luna execution record committed with them;
- **no Production State advancement**;
- stop for Sol semantic review.

Do not begin Evidence, Materiality, Completeness, Selection, or Architecture work in this task.

## 2. Frozen semantic authority

Use exactly the following repository authority.

### Discovery basis

- path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- record count: **41**
- SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- acceptance path: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`

### Sol Screening semantic seed

- path: `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- semantic-authority Git blob: `ba649d6e805bac5316b88a78d259a3de97f839b2`
- authority field: `SOL_SEMANTIC_SCREENING_SPEC`
- decisions: **41 exactly**
- expected aggregate:
  - KEEP: **26**
  - INSPECT: **8**
  - MAYBE: **3**
  - DROP: **4**

Luna must not change any of the following semantic fields from the seed:

- `discovery_id`
- `decision`
- `reason`
- `scope_tags`
- `duplicate_group`
- `verification_targets`
- `confidence`

The seed wrapper itself is not the current interactive runner schema. Luna may transform only the outer wrapper needed by the runner; the 41 decision objects must remain semantically and structurally identical to the seed decision objects.

## 3. Recovery/check invariant from Sol r7

Sol independently reconstructed the complete Discovery and Screening decision sets and calculated the following expected content-addressed Screening result-set id:

`648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`

This is a **validation expectation, not acceptance authority**.

Luna must compare the generated current-Core `result_set_sha256` to this value.

- If it matches, record the match.
- If it differs, **do not rename, rewrite, or force the generated run**. Record the actual generated value and investigate only enough to identify the deterministic basis difference. Stop for Sol review with status `RESULT_SET_ID_MISMATCH_NEEDS_SOL_REVIEW`.

The previous Git-data blob experiments described in r7 are unreachable test objects and must not be reused as production artifacts.

## 4. Required authority reads before writing

Read in this order:

1. `AGENTS.md` from reviewed `main`.
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed `main`.
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed `main`.
4. `config/survey-production-v2.json` from reviewed `main`, especially `DISCOVERY_COLLECTED -> stage:screening`.
5. `schemas/screening-v2-run-package.schema.json` from reviewed `main`.
6. `schemas/screening-v2-batch-result.schema.json` from reviewed `main`.
7. `config/prompts/source-screening-v2.md` from reviewed `main`.
8. `scripts/survey_screening_v2.py` from reviewed `main`.
9. `scripts/run_screening_v2_interactive.py` from reviewed `main`.
10. `scripts/survey_agent_tool_v2.py` from reviewed `main` if needed to understand current-stage basis override.
11. `sources/2026-W33/production-profile.json` on the exact starting branch SHA.
12. `sources/2026-W33/production-state.json` on the exact starting branch SHA.
13. `sources/2026-W33/discovery/discovery-accepted-v2.json` and its referenced Discovery on the exact starting SHA.
14. `sources/2026-W33/screening/sol-screening-decisions-r1.json` on the exact starting SHA.
15. `sources/2026-W33/execution/sessions/w33-sol-screening-20260829-r6.md`.
16. `sources/2026-W33/execution/sessions/w33-sol-screening-materialization-recovery-20260830-r7.md`.
17. `sources/2026-W33/execution/handoffs/w33-screening-to-architecture-review-sol-luna-r3.md`.
18. this handoff.

If any of these authorities materially disagree with the state described here, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW` before writing production artifacts.

## 5. Preflight invariants

Before materialization, verify and record:

- branch is exactly `weekly/2026-W33-v2-work`;
- repository HEAD is exactly the caller-supplied starting SHA containing this handoff;
- reviewed main is still `6267de3f6876f491950139757bfdf1085fc07bdc`, unless Sol explicitly supplies a newer reviewed-main authority;
- `production-state.json.lifecycle_state == DISCOVERY_COLLECTED`;
- `production-state.json.next_action == stage:screening`;
- Screening checkpoint is still pending;
- Discovery acceptance validates;
- Discovery record count is 41;
- Discovery SHA-256 is the frozen value above;
- semantic seed Git blob is `ba649d6e805bac5316b88a78d259a3de97f839b2` or its file bytes otherwise exactly match current repository authority;
- semantic seed has 41 unique Discovery IDs;
- semantic seed covers exactly the accepted Discovery IDs;
- decision aggregate is 26 KEEP / 8 INSPECT / 3 MAYBE / 4 DROP;
- `sources/2026-W33/screening/v2/accepted/` contains no conflicting incomplete run directory.

A pre-existing complete accepted run is not automatically an error. If the current runner validates it and it corresponds exactly to this frozen semantic seed, record that fact and avoid destructive overwrite. Stop for Sol review after committing only any required execution record if no production bytes need to change.

## 6. Interactive runner input construction

The current runner requires exactly these top-level fields:

- `schema_version`
- `issue_id`
- `runner`
- `decisions`

Construct an execution-local input object as follows:

- `schema_version`: `2.0-rc1`
- `issue_id`: `2026-W33`
- `decisions`: exact 41 decision objects copied from `sol-screening-decisions-r1.json`, with no semantic edits
- `runner.provider`: `OpenAI`
- `runner.model`: identify the actual Luna model/session used by Work; do not impersonate Sol
- `runner.invocation`: a concise value identifying this exact bounded handoff, such as `w33-screening-materialization-luna-r1`
- `runner.generated_at`: actual offset-aware UTC execution time

The execution-local wrapper may be created in a temporary/work directory. The runner will archive the exact wrapper into the accepted run as `interactive-decisions.json`.

Do not edit `sources/2026-W33/screening/sol-screening-decisions-r1.json` to make it directly runnable.

## 7. Prescribed execution path

Use the repository's current interactive Screening runner, rather than reimplementing acceptance logic.

Equivalent command shape:

```bash
python scripts/run_screening_v2_interactive.py \
  --repo-root . \
  --state sources/2026-W33/production-state.json \
  --decisions <execution-local-interactive-decisions.json>
```

The current implementation is expected to:

1. validate Production State and accepted Discovery;
2. regenerate the current Screening package from canonical Discovery;
3. partition the current 41 records under Core limits — expected to be one batch unless current Core authority says otherwise;
4. materialize one result decision for every generated batch input record using the exact frozen decision object;
5. call current `survey_screening_v2.accept_results`;
6. create the content-addressed accepted run under:
   `sources/2026-W33/screening/v2/accepted/<result_set_sha256>/`;
7. archive at least:
   - `package.json`
   - `input/batches/batch-001.jsonl` for the expected one-batch case
   - `results/batch-001.json` for the expected one-batch case
   - `screening-accepted.json`
   - `interactive-decisions.json`
   - `interactive-audit.json`;
8. leave Production State unchanged.

If current Core legitimately generates more than one batch, accept the current implementation result rather than forcing one batch, but record the reason and exact batch count for Sol review.

## 8. Required post-materialization validation

After the runner succeeds, independently verify and record:

### Identity and coverage

- accepted issue id is `2026-W33`;
- research profile is `WEEKLY`;
- record count is 41;
- every accepted Discovery ID appears exactly once;
- no extra ID exists;
- accepted decision objects equal the exact Sol seed decision objects after sorting by `discovery_id`;
- aggregate remains 26 / 8 / 3 / 4.

### Package/batch provenance

- package basis points to the current production profile/state/Discovery;
- Discovery SHA-256 equals the frozen value;
- package prompt and result-contract hashes match current reviewed-main Core bytes;
- each archived input batch hash matches package metadata;
- each result basis matches the package/batch/profile/state/prompt/result-contract hashes;
- `screening-accepted.json` validates with current `survey_screening_v2.validate_acceptance` or the current repository-prescribed equivalent.

### Content-addressed identity

- accepted directory name equals `screening-accepted.json.result_set_sha256`;
- recomputed acceptance digest validates;
- compare actual result-set id to Sol r7 expected id `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`.

### State boundary

- `sources/2026-W33/production-state.json` byte/hash is unchanged from the starting SHA;
- no Screening checkpoint has been recorded in Production State;
- lifecycle remains `DISCOVERY_COLLECTED`;
- next action remains `stage:screening`;
- no Evidence/Materiality/Completeness/Selection/Architecture artifact has been created or modified.

## 9. Allowed repository writes

This task may write only:

1. the new or already-valid canonical accepted Screening run under:
   `sources/2026-W33/screening/v2/accepted/<generated-result-set-sha256>/...`
2. one Luna execution record under:
   `sources/2026-W33/execution/sessions/`
   with a stable name such as `w33-luna-screening-materialization-20260830-r1.md`.

If repository execution policy requires an additional edition-local temporary/request record to invoke a prescribed deterministic tool, keep it strictly bounded and document it. Do not leave unrelated temporary files committed.

Do not modify:

- `sources/2026-W33/production-state.json`
- `sources/2026-W33/discovery/**`
- `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- Core implementation roots (`config`, `schemas`, `scripts`, `.github/workflows`)
- Evidence/Materiality/Completeness/Selection/Architecture paths
- historical r6/r7/r3 records

Do not update `execution/index.md` in this Luna task unless the current execution-record policy explicitly requires the worker to do so. Sol will update the recovery index after reviewing the candidate if needed.

## 10. Luna execution record requirements

The Luna session record must contain at minimum:

- exact caller-supplied starting SHA;
- exact ending SHA after candidate commit;
- reviewed-main SHA used;
- Production State before and after, including SHA-256;
- semantic seed path, commit/blob identity, decision count and aggregate;
- generated accepted run path;
- generated result-set SHA-256;
- comparison with Sol expected result-set id;
- package SHA-256;
- batch count and each input/result SHA-256;
- `screening-accepted.json` SHA-256;
- `interactive-decisions.json` SHA-256;
- `interactive-audit.json` SHA-256;
- exact changed paths in the candidate commit;
- validators/commands run and their pass/fail results;
- confirmation that Production State was not modified;
- unresolved discrepancies, if any;
- final stop reason.

Use one of these stop statuses:

- `READY_FOR_SOL_REVIEW`
- `RESULT_SET_ID_MISMATCH_NEEDS_SOL_REVIEW`
- `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`
- `DETERMINISTIC_FAILURE_NEEDS_SOL_REVIEW`

Do not label the task `COMPLETE` in a way that implies Screening lifecycle completion; this handoff ends before Sol review and before Core advancement.

## 11. Git boundary

Commit the accepted Screening run and Luna session record to the canonical work branch.

Before updating the branch ref, verify that the branch still points to the exact starting SHA. If it has moved, do not force-push and do not merge. Stop and report the observed SHA.

The candidate commit must be a fast-forward descendant of the exact starting SHA.

After commit, re-read the branch and compare starting SHA to ending SHA. Confirm that only allowed paths changed.

## 12. Explicit prohibitions

Luna must not:

- perform new web/source research;
- reconsider Screening decisions;
- modify a reason, scope tag, duplicate group, verification target, confidence, or decision;
- resolve INSPECT/MAYBE items yet;
- create Evidence cards;
- decide Materiality or Selection;
- propose Architecture in this S1 task;
- run `ADVANCE_STAGE`;
- create a Screening checkpoint by hand;
- modify Production State;
- infer Human approval;
- repair shared Core implementation without returning to Sol.

## 13. Endpoint and next owner

Successful endpoint:

`SCREENING MATERIALIZATION CANDIDATE COMMITTED -> STOP FOR SOL REVIEW`

The next owner is **Sol**, not Luna.

Sol will review the exact committed accepted run for:

- 41-ID semantic fidelity;
- exact decision object equality;
- duplicate-group and verification-target fidelity;
- package/result/acceptance consistency;
- content-addressed identity;
- changed-path boundary;
- absence of lifecycle advancement.

Only after a Sol review pass will a separate handoff authorize deterministic Screening checkpoint/`ADVANCE_STAGE` execution to reach `CANDIDATES_NORMALIZED`.