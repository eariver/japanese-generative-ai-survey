# 2026-W34 Luna instruction — Discovery X-binding repair verification and deterministic advancement

Status: `READY_FOR_LUNA / BOUNDED REPAIR + DISCOVERY ADVANCE ONLY`

Issue: `2026-W34`  
Canonical work branch: `weekly/2026-W34-v2-work`  
Reviewed `main`: `c7a898889463b049dea4ee7337ee16ad5fbf3191`  
Expected lifecycle at task start: `ISSUE_INITIALIZED`  
Expected next action at task start: `stage:discovery`

The caller supplies the exact branch SHA containing this instruction. Start only from that exact SHA.

## 1. Objective

Repair/verify the one mechanical X-manifest↔Discovery-graph binding defect found by Sol after Luna materialization r1, prove the committed Discovery candidate with the **actual current Core implementation**, and, only if that proof passes, execute the deterministic Core advancement from `ISSUE_INITIALIZED` to `DISCOVERY_COLLECTED`.

Stop immediately after verified Discovery advancement. Do **not** begin Screening.

This is not a new Discovery pass and not a new semantic review.

## 2. Frozen Sol authorities

Read before writing:

1. `sources/2026-W34/execution/decisions/sol-discovery-completeness-20260903-r1.md`
2. `sources/2026-W34/execution/findings/sol-discovery-materialization-review-20260903-r1.md`
3. `docs/checkpoints/2026-W34-luna-discovery-materialization-instruction-20260903.md`
4. `sources/2026-W34/execution/luna/w34-discovery-materialization-r1/materialization-validation-v0.1.json`
5. `sources/2026-W34/discovery/discovery-v2.jsonl`
6. `sources/2026-W34/discovery/event-discovery-crosswalk-v0.1.json`
7. `sources/2026-W34/external/x/x-source-intake-v2.json`
8. `sources/2026-W34/external/x/weekly-x-2026-W34-r2/raw/grok-x-result.corrected.md`
9. `sources/2026-W34/external/x/weekly-x-2026-W34-r2/raw/x-url-ledger.corrected.tsv`
10. `sources/2026-W34/production-state.json`
11. `sources/2026-W34/raw-index.json`
12. reviewed-main `AGENTS.md`
13. reviewed-main `docs/survey-production-core-v2-session-bootstrap.md`
14. reviewed-main `docs/survey-production-core-v2-operator-execution-bridge.md`
15. reviewed-main `docs/survey-production-core-v2-execution-record-policy.md`
16. reviewed-main `scripts/survey_x_intake_v2.py`
17. reviewed-main `scripts/survey_discovery_v2.py`
18. reviewed-main `scripts/survey_core_execution_bridge_v2.py`
19. reviewed-main `schemas/x-source-intake-v2.schema.json`
20. reviewed-main `schemas/discovery-acceptance-v2.schema.json`
21. reviewed-main `schemas/operator-execution-request-v2.schema.json`

Do not substitute remembered Core behavior for these exact reviewed-main bytes.

## 3. Sol-reviewed starting facts

The previous materialization is accepted in all of these respects:

- 40 Discovery records / 40 unique Discovery IDs;
- W34-C001–W34-C105 event traceability: 105/105, 0 silently dropped;
- DailyX: 76/76 topics across seven imported Drive-returned Raw files;
- corrected Grok r2: 47/47 URLs;
- corrected Grok window counts: 10 `ORDINARY_WINDOW` / 20 `BACKGROUND_ONLY` / 17 `LATE_BREAKING`;
- existing GitHub Releases Raw reused immutably;
- carry-over remains one `RECHECKED_UNRESOLVED` obligation with no current promotion;
- Production State remained byte-identical through materialization r1.

Sol has already accepted the semantic Discovery completeness baseline. Do not re-open materiality or broad Discovery.

## 4. Exact defect and exact Sol correction

At Luna materialization end, the COMPLETE X manifest incorrectly named event-level working IDs (`W34-C...`) as `result.discovery_ids`.

Current Core `scripts/survey_discovery_v2.py::_validate_x_integration()` requires those values to be actual Discovery IDs in `discovery-v2.jsonl` and to bind the imported Grok Raw.

Sol corrected the manifest before this task. At task start, verify that:

```json
"discovery_disposition": "DISCOVERY_RECORDED",
"discovery_ids": [
  "w34-grok-r2-corrected-47-url-ledger"
]
```

and verify that the Discovery record `w34-grok-r2-corrected-47-url-ledger` directly includes:

`sources/2026-W34/external/x/weekly-x-2026-W34-r2/raw/grok-x-result.corrected.md`

in `source.raw_paths`.

Do not change the X Raw bytes, Grok classification, event crosswalk, or Sol semantic scope.

If the branch does not contain exactly this Sol correction, stop `NEEDS_SOL_REVIEW` without lifecycle write.

## 5. Mandatory real-Core validation

The previous custom/schema-equivalent temporary PASS is not sufficient authority.

Use the actual reviewed-main Core implementation against the exact work-branch repository data.

You must execute the functional equivalent of:

```python
from scripts import survey_x_intake_v2
from scripts import survey_discovery_v2

survey_x_intake_v2.validate_manifest(..., require_complete=True)
survey_discovery_v2.build_acceptance(..., output_path=<temporary non-repository path>)
survey_discovery_v2.validate_acceptance(...)
```

The temporary output must be outside the repository and must be newly created for this validation.

Do not replace `build_acceptance()` with a hand-built/schema-equivalent validator.

Record at minimum:

- actual function path/version/commit used;
- X manifest validation result;
- temporary acceptance `record_count`;
- temporary acceptance `graph_sha256`;
- Discovery JSONL SHA256;
- X manifest SHA256;
- X integration result;
- Raw-ref normalization/hash result;
- graph validation result;
- exact exception if any.

Expected Discovery count is 40, not 105. Event traceability must independently remain 105/105.

## 6. Fail-closed condition

If the actual current-Core build or validation fails for any reason other than the already-corrected X binding:

- do not guess a fix;
- do not mutate Discovery scope;
- do not modify `production-state.json`;
- do not create the operator advancement request;
- record the exact exception and affected path/record;
- stop `NEEDS_SOL_REVIEW`.

Likewise stop if:

- 40/40 Discovery IDs changes unexpectedly;
- event crosswalk is not 105/105;
- DailyX is not 76/76;
- Grok is not 47/47 or not 10/20/17;
- any pre-existing indexed Raw changed;
- current Production State is not `ISSUE_INITIALIZED / stage:discovery` before advancement;
- reviewed-main/protected Core bytes drift.

## 7. Deterministic advancement authority

If and only if Section 5 passes completely, Sol authorizes deterministic Discovery advancement.

This authorization derives from:

- semantic acceptance: `sources/2026-W34/execution/decisions/sol-discovery-completeness-20260903-r1.md`
- independent defect review + exact correction: `sources/2026-W34/execution/findings/sol-discovery-materialization-review-20260903-r1.md`
- the actual current-Core PASS produced by this task.

Do not perform another semantic or materiality decision.

## 8. Preferred execution path for lifecycle advancement

Use current Core authority. If a direct local Core CLI execution can prove exact canonical branch/worktree identity and uses reviewed-main Core bytes, it is allowed.

For connector-safe execution, prefer the documented operator bridge:

1. commit repair-validation/session records first;
2. verify remote canonical branch HEAD equals that validation commit;
3. create exactly one new operator request file in an otherwise request-only commit;
4. use operation `ADVANCE_STAGE`;
5. expected from state: `ISSUE_INITIALIZED`;
6. artifact: `sources/2026-W34/discovery/discovery-accepted-v2.json`;
7. trigger persistent transport Issue `#448` with exactly:

   `/survey-core-execute <exact-request-commit-sha>`

8. synchronously inspect the operator workflow result and resulting canonical branch HEAD;
9. verify the generated acceptance/state/checkpoint bytes using current reviewed-main Core.

Do not use force/reset/rewrite/rebase.

## 9. Operator request content

Use a stable request path such as:

`sources/2026-W34/execution/requests/w34-discovery-advance-20260903-r1.json`

The request must validate against current `schemas/operator-execution-request-v2.schema.json` and contain the current exact reviewed-main SHA.

Required semantic content:

```text
request_id: w34-discovery-advance-20260903-r1
issue_id: 2026-W34
source_root: sources/2026-W34
work_branch: weekly/2026-W34-v2-work
reviewed_main_sha: c7a898889463b049dea4ee7337ee16ad5fbf3191
operation.kind: ADVANCE_STAGE
operation.expected_from_state: ISSUE_INITIALIZED
operation.state_path: sources/2026-W34/production-state.json
artifact name: discovery-acceptance
artifact path: sources/2026-W34/discovery/discovery-accepted-v2.json
```

Include one agent review recording that Sol has accepted W34 semantic Discovery completeness, with evidence pointing to the two Sol authority files above and this task's real-Core validation record.

The request-only commit must contain no other change.

## 10. Expected successful post-state

After successful canonical Core advancement, verify:

- lifecycle state: `DISCOVERY_COLLECTED`;
- next action: `stage:screening`;
- machine checkpoint `discovery`: complete/accepted per current Core representation;
- `sources/2026-W34/discovery/discovery-accepted-v2.json` exists;
- canonical acceptance validates with `survey_discovery_v2.validate_acceptance()`;
- acceptance `record_count`: 40;
- acceptance graph SHA matches the pre-advance real-Core temporary candidate;
- X manifest binding uses `w34-grok-r2-corrected-47-url-ledger`;
- event crosswalk remains 105/105;
- DailyX remains 76/76;
- Grok remains 47/47 and 10/20/17;
- carry-over remains represented;
- no Screening artifacts were created.

## 11. Write boundary before the operator request

Allowed repair-validation writes before request-only commit:

- `sources/2026-W34/execution/luna/w34-discovery-binding-repair-r1/**`
- `sources/2026-W34/execution/sessions/w34-luna-discovery-binding-repair-20260903-r1.md`
- `sources/2026-W34/execution/index.md`

Do not edit:

- `sources/2026-W34/discovery/discovery-v2.jsonl`
- `sources/2026-W34/discovery/event-discovery-crosswalk-v0.1.json`
- DailyX Raw
- Grok Raw
- GitHub Releases Raw
- source-local capture Raw
- `sources/2026-W34/raw-index.json`
- `sources/2026-W34/external/x/x-source-intake-v2.json` (already corrected by Sol)
- shared Core
- W33

The later request-only commit may add only the operator request file.

Core operator execution may then write only the edition-local files allowed by current Core for the Discovery advancement.

## 12. Forbidden downstream work

Even after successful `DISCOVERY_COLLECTED` advancement, do not execute:

- Screening
- Evidence review
- Materiality
- Completeness overwrite
- Selection
- Architecture
- Human Gate decision
- drafting
- publication validation
- Freeze
- Release

Stop for Sol at `DISCOVERY_COLLECTED / stage:screening`.

## 13. Completion report

Return exact measured values:

- Exact Starting SHA;
- pre-request validation commit SHA;
- operator request commit SHA if created;
- operator execution/resulting branch SHA if successful;
- Ending SHA;
- start→end ahead / behind / commit count;
- all changed paths grouped by repair-validation / request / Core advancement;
- real `build_acceptance()` PASS/FAIL;
- real `validate_acceptance()` PASS/FAIL;
- temporary and canonical record counts / graph SHA values;
- X manifest SHA and exact `discovery_ids`;
- 40/40 Discovery IDs;
- 105/105 event traceability;
- DailyX 76/76;
- Grok 47/47 + 10/20/17;
- Raw integrity status;
- Production State before and after;
- Discovery checkpoint provenance;
- carry-over status;
- unresolved authority/chronology/capture gaps retained for Screening/Evidence;
- explicit confirmation that Screening and later stages were not executed.
