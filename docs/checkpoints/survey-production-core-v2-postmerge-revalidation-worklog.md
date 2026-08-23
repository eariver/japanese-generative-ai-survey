# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `OPERATOR BRIDGE + HUMAN-GATE ROUNDTRIP IMPLEMENTED / FREEZE PREPARATION`

Established: 2026-08-23 JST  
Last updated: 2026-08-24 JST

Integrated Core baseline that exposed the operator gap: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`  
Maintenance-start `main`: `2bcaa7d1df1826ab8848c25de8bf2373d85a8e75`  
Maintenance branch: `maintenance/core-v2-operator-execution-bridge`  
Maintenance PR: `#447 Core v2: add deterministic operator execution bridge`

W33/SP001 remain paused non-PASS production-validation evidence until reviewed unchanged maintenance integration.

## Resume checkpoint

The post-merge clean W33/SP001 trials exercised real ChatGPT research/editorial work and the real W33 Human-mediated Grok/Drive handoff, but could not begin canonical Core lifecycle execution because the connector runtime had no exact checkout/CLI execution substrate.

Shared-Core maintenance first added a narrow deterministic operator bridge. A later independent pre-approval audit proved that reaching a Human Gate was insufficient: connector-only production also needed canonical deterministic recording of explicit Human approval and ordinary requested-revision cycles.

The current maintenance candidate therefore covers:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

The Human remains the sole decision authority. Actions/Core only validate and record explicit input and deterministic lifecycle consequences.

Configured Retrospective initialization reuses existing `scripts/survey_period_v2.py`; no second Retrospective builder survives.

## Edition-local resume authority

### W33

Branch: `weekly/2026-W33-v2-work`  
Resume file: `sources/2026-W33/postmerge-validation-status.md`

Prepared work includes canonical Weekly window resolution, real one-file Grok/Drive execution, exact Raw import, X/community disposition, primary-source follow-up and editorial Architecture preparation.

Exact Raw:

`sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md`

SHA-256:
`93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`

Do not rerun Grok unless canonical validation later proves these exact bytes unusable.

### SP001

Branch: `special/SP001-v2-work`  
Resume file: `sources/SP001/postmerge-validation-status.md`

Prepared authority/research:

- `sources/SP001/research-scope-v2.json`
- `sources/SP001/intake/postmerge-primary-source-intake.md`
- `sources/SP001/architecture-preparation.md`

X/Grok applicability is prepared as `NOT_REQUIRED`. Do not copy failed pre-redesign accepted artifacts into the clean rerun.

## Revalidation findings

### RVF-001 — Human-mediated Grok/Drive transport works

Status: `CONFIRMED BY REAL W33 OPERATION`

```text
ChatGPT prepares exact grok-task.md
-> Human passes exact Drive path/reference to Grok
-> Grok writes result in instructed run folder
-> ChatGPT retrieves/imports exact Raw
-> ChatGPT resumes
```

No Grok connector is required.

### RVF-002 — X/community and technical Evidence separation works

Status: `CONFIRMED EDITORIALLY / CANONICAL MANIFEST VALIDATION PENDING POST-INTEGRATION`

Grok/X supplies salience/community signal. Technical claims still require authoritative verification before Evidence acceptance.

### RVF-003 — fresh X can materially change Weekly Architecture

Status: `CONFIRMED BY W33`

W33's Aug. 12–14 release wave materially changed package selection and synthesis after primary-source verification.

### RVF-004 — Thematic X may legitimately be `NOT_REQUIRED`

Status: `CONFIRMED EDITORIALLY BY SP001 / CANONICAL RECORD PENDING POST-INTEGRATION`

### RVF-005 — operator execution path was a blocking dependency

Status: `CONFIRMED / BRIDGE IMPLEMENTED / FINAL REAUDIT PENDING`

Connector runtime can research/edit GitHub but cannot necessarily invoke exact-branch Core CLI. Manual imitation of machine authority is prohibited.

### RVF-006 — do not fabricate machine acceptance

Status: `CONFIRMED OPERATIONAL RULE`

If canonical deterministic execution is unavailable, preserve preparation/provenance and stop before machine acceptance.

### RVF-007 — edition-local execution records remain required

Status: `CONFIRMED / POLICY SYNCHRONIZED`

Once canonical Profile/State exists, `{source_root}/execution/` is the operational continuity record. Human-readable review Markdown points to exact machine review JSON under `{source_root}/gates/`.

### RVF-008 — old failed artifacts remain non-authoritative

Status: `CONFIRMED`

W33 historical `pipeline-state.json` remains `NON_AUTHORITATIVE_READ_ONLY`; SP001 failed accepted artifacts remain archived only.

### RVF-009 — first maintenance audit found stale workflow-count authority

Status: `FOUND / REPAIRED / AUDIT INVALIDATED`

Candidate `89b0a02c8699c957dc8ca09d0228e9d8b4ce7287` still described six workflows while the operator bridge made seven. Any PASS from that audit is non-reusable.

### RVF-010 — second maintenance audit found missing Retrospective bridge exposure

Status: `FOUND / REPAIRED / AUDIT INVALIDATED / DIAGNOSIS CORRECTED`

Candidate `0caa2c4f9ed87a32e50cf7813990b916489581bc` could not cold-start required Retrospective validation. Deeper review found existing generic `survey_period_v2.resolve_configured_period()` + `period_profile()` support, so the repair was bridge exposure only. Temporary duplicate Retrospective adapter/schema/tests were removed.

### RVF-011 — bridge glue init -> Discovery E2E exists

Status: `IMPLEMENTED / REGRESSION RETAINED`

`tests/test_survey_core_execution_bridge_v2.py` exercises immutable Thematic initialization, canonical Profile/State/execution record, X `NOT_REQUIRED`, Discovery acceptance and one bridge-backed `ADVANCE_STAGE` to `DISCOVERY_COLLECTED`.

### RVF-012 — Retrospective authority text was synchronized before the earlier freeze

Status: `HISTORICAL REPAIR RETAINED`

Current authority consistently reuses existing `survey_period_v2` and prohibits a second Retrospective cadence engine.

### RVF-013 — Retrospective request fixture binds existing Period builder

Status: `IMPLEMENTED / REGRESSION RETAINED`

Representative configured `2024-H1` request identity must equal Profile `issue_id`, `source_root` and `work_branch`. Existing Period tests cover representative monthly/half-year/annual periods.

### RVF-014 — earlier frozen candidate cross-check

Status: `HISTORICAL PASS FOR a65e714b... / INVALIDATED BY RVF-015`

Earlier candidate:
`a65e714b711e76006318a14b252aa0a4e9727b4f`

It passed then-current Core CI, Pipeline contract tests and six audit points. That evidence is historical only because the subsequent full-system audit exposed missing Human Gate continuation semantics.

### RVF-015 — pre-approval full-system audit found Human Gate control gaps

Status: `BLOCKERS IDENTIFIED / REPAIR IMPLEMENTED / REAUDIT PENDING`

Two blocking gaps invalidated the earlier candidate:

- **HG-001:** connector-only operation could reach a Human Gate but not canonically record an explicit Human approval;
- **HG-002:** ordinary Human `REQUEST_CHANGES` had no coherent revision/selective-invalidation path, so changed reviewed bytes caused pinned checkpoint drift or an inappropriate Exception Gate.

The audit consequence was to return PR #447 to Draft, change the final audit from six-only coverage to seven points, and require both direct and connector-safe approve/revise E2E before review readiness.

### RVF-016 — Human Gate round-trip repair work plan and completion contract

Status: `PLAN LOCKED / IMPLEMENTATION SUBSTANTIALLY COMPLETE / FREEZE NOT YET DECLARED`

#### Work goal

> **Make both normal Human Gates round-trip capable in canonical Core v2 — reach gate → record explicit Human APPROVED or REQUEST_CHANGES → resume or selectively invalidate/regenerate → reach the same gate again when needed — and expose only those deterministic mechanics through the connector-safe operator bridge.**

The goal does not permit GitHub Actions/Core to decide Human approval, infer requested changes, choose a regeneration boundary, author editorial content or replace ChatGPT/Human judgment.

#### Locked required work

1. define Human Gate decision/revision protocol;
2. implement exact-byte approval and dependency-aware `REQUEST_CHANGES` mechanics;
3. expose only four narrow Human Gate operations through existing bridge;
4. synchronize Core/Actions/bridge/execution-record/final-audit authority;
5. add positive/negative direct and bridge E2E;
6. freeze only after all repairs/authority synchronization finish;
7. exact-head CI + Pipeline contracts + seven-point fixed-head audit from zero;
8. any tree mutation after freeze invalidates all seven verdicts.

#### Completion decision criteria

PR #447 may return to Ready only when all are true simultaneously:

- HG-001 closed;
- HG-002 closed;
- Actions/Core infer no Human decision;
- prior review revisions reconstructable while only current bytes are authoritative;
- required positive/negative direct and bridge E2E pass;
- authority/schema exactly match implementation;
- exact-head Core CI PASS;
- exact-head Pipeline contract tests PASS;
- Points 1–7 PASS on one unchanged candidate SHA;
- PR metadata binds that exact SHA and does not present earlier invalidated PASS as current evidence.

If any condition is false, PR remains Draft.

### RVF-017 — canonical Human Gate review authority implemented

Status: `IMPLEMENTED / DIAGNOSTIC REGRESSION PASS / FINAL FIXED-HEAD EVIDENCE PENDING`

Added:

- `schemas/human-gate-review-record-v2.schema.json`
- `schemas/human-gate-review-index-v2.schema.json`
- `scripts/survey_human_gate_v2.py`

Canonical machine review history:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

Each rN binds exact reviewed State/artifact SHA-256, reviewed repository commit, Human identity/time/reference, decision and—when applicable—requested changes + regeneration boundary.

Approval delegates to canonical exact-byte approval functions. `REQUEST_CHANGES` validates a gate-specific boundary, trims State/history/checkpoint provenance to that boundary, preserves unaffected upstream authority, removes superseded canonical Stage Checkpoints and returns control to ChatGPT for actual repair.

### RVF-018 — operator bridge expanded from four to eight request kinds

Status: `IMPLEMENTED / DIRECT + BRIDGE REGRESSION COVERAGE PRESENT`

Added exactly:

- `RECORD_ARCHITECTURE_APPROVAL`
- `REQUEST_ARCHITECTURE_REVISION`
- `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- `REQUEST_PUBLICATION_PREVIEW_REVISION`

Every Human Gate request requires canonical State path, next `expected_revision`, Human provenance; revision additionally requires non-empty requested changes and enum-constrained gate-specific regeneration boundary.

Generic `EXECUTE_HUMAN_DECISION`, generic rejection, arbitrary command/module/script/workflow surfaces remain absent.

### RVF-019 — full Publication Preview E2E exposed latent `{survey_root}` Stage Checkpoint defect

Status: `FOUND BY NEW E2E / SHARED CORE FIXED / DIAGNOSTIC CI PASS`

The new Publication Preview round-trip E2E reached a previously under-exercised agent-first path and failed because `survey_agent_control_v2._expand_stage_path()` expanded only `{source_root}` while canonical DRAFT_COMPLETE artifacts include `{survey_root}/main.tex` and `{survey_root}/main.pdf`.

Observed error:

```text
unsupported stage path template: {survey_root}/main.tex
```

Repair commit:
`5ffc942537eae1b9b3f40c8b344773725b72ca2f`

The helper now expands Profile path tokens generically. Diagnostic evidence on that tree:

- Survey Production Core v2 CI run `32650031572` — PASS;
- Pipeline contract tests run `32650031520` — PASS.

These are diagnostic only because the candidate changed afterward.

### RVF-020 — direct Human Gate approve/revise E2E implemented

Status: `IMPLEMENTED / DIAGNOSTIC PASS`

`tests/test_survey_human_gate_v2.py` covers:

- Architecture r1 `REQUEST_CHANGES` -> selective invalidation -> r2 -> approval;
- stale r1 approval after r2 refusal;
- changed reviewed Architecture bytes refusal;
- invalid Architecture boundary refusal;
- Publication Preview r1 `REQUEST_CHANGES` -> Validation/Candidate regeneration -> r2 -> approval;
- Publication revision cannot cross Architecture boundary;
- final r2 approval binds current Candidate/PDF;
- Publication Preview approval sets its special machine checkpoint and resumes Freeze.

### RVF-021 — bridge-backed Human Gate round-trip E2E implemented

Status: `IMPLEMENTED / FINAL EXACT-HEAD CI PENDING`

`tests/test_survey_core_execution_bridge_human_gate_v2.py` executes:

- bridge Architecture r1 revision -> r2 approval;
- bridge Publication r1 revision -> revalidation/new candidate -> r2 approval;
- explicit Human provenance schema requirements;
- invalid cross-gate boundary refusal;
- no generic Human-decision/rejection operation;
- existing one-request-only workflow transport.

First bridge E2E head `cdf5b858d0b162c16efa2b118eed4b27293d2cf1` produced one test-only error: the fixture incorrectly expected a nonexistent `machine_checkpoints["publication_candidate"]` key. Canonical `VALIDATED_DRAFT -> RELEASE_CANDIDATE` uses a Stage Checkpoint file but has `checkpoints: []`.

The test was corrected to verify deletion of superseded `VALIDATED_DRAFT.json` and pending `validation` checkpoint instead. No Core implementation change was required for this correction.

### RVF-022 — current authority synchronized to seven-point/Human Gate model

Status: `COMPLETE BEFORE FREEZE`

Synchronized current operational authority includes:

- `docs/survey-production-core-v2-final-audit-rule.md` — six -> seven points, Point 7 `Human Gate round-trip viability`;
- `docs/survey-production-core-v2-operator-execution-bridge.md` — exactly eight request kinds, Human decision-vs-recording boundary and reviewed-parent provenance;
- `docs/survey-production-core-v2-github-actions-policy.md` — bridge may record already explicit Human decision but never choose it;
- `docs/survey-production-core-v2-workflow-responsibility-inventory.md` — seven workflows unchanged, Human Gate mechanics remain inside existing bridge;
- `docs/survey-production-core-v2-redesign-authority.md` — round-trip semantics and seven-point re-audit;
- `docs/survey-production-core-v2-execution-record-policy.md` — Markdown rN summaries bind exact machine review JSON;
- `docs/survey-production-core-v2-production-feedback-backlog.md` — PFB-014 includes HG-001/HG-002, reviewed-parent provenance and seven-point acceptance;
- `AGENTS.md` and `docs/survey-production-core-v2-session-bootstrap.md` — operational sessions use seven-point final audit and routine `REQUEST_CHANGES` continuation.

### RVF-023 — Human-reviewed commit provenance was distinct from request/event commit

Status: `FOUND DURING FREEZE PREPARATION / REPAIRED / FINAL EXACT-HEAD CI PENDING`

Freeze-preparation inspection found that `survey_core_execution_bridge_v2.py` passed the immutable request/event commit SHA into `survey_human_gate_v2` as `reviewed_repository_commit_sha`. The exact reviewed State/artifact hashes were correct, but the named repository provenance was one commit too late: the Human had reviewed the edition bytes before ChatGPT added the request-only commit.

Repair:

- Human Gate operator requests now require exact lowercase 40-hex `reviewed_repository_commit_sha`;
- the bridge forwards that explicit reviewed SHA instead of `event_sha`;
- the workflow resolves the request-only commit parent and refuses execution unless the request's reviewed SHA equals that parent exactly;
- bridge receipt records both `event_commit_sha` and `reviewed_repository_commit_sha` separately;
- bridge E2E intentionally uses different values for those two identities and asserts the review record/receipt preserve the distinction;
- PFB-014 and bridge authority now make parent binding an explicit acceptance condition.

This repair closes the currently known provenance defect. It does not itself constitute final acceptance; exact-head CI and the independent seven-point audit remain required.

## Current maintenance design

### Reviewed-main preflight

Every request binds exact lowercase 40-hex `reviewed_main_sha`. Before dependency installation/Core execution, the workflow requires reviewed SHA on current `main` history, request-parent descent, initialization execution-record baseline equality and byte equality for fixed shared implementation roots plus configured contract files.

For Human Gate operations, the immutable request additionally binds exact `reviewed_repository_commit_sha`, and Actions requires it to equal the request-only commit parent. The request/event commit remains separate execution provenance.

### Request/receipt

```text
{source_root}/execution/requests/<request-id>.json
{source_root}/execution/bridge-runs/<request-id>/
```

Trigger is request-only; generated writes are Profile-source-root-bound; immutable request bytes cannot be mutated; bot output cannot recursively retrigger.

### Why this is not Actions-heavy production

The bridge supplies only missing exact checked-out deterministic execution. Human decides the two normal Gate outcomes; ChatGPT owns research/editorial/visual judgment and actual requested repair. Actions/Core validate and record deterministic authority only.

Actions surface remains exactly seven workflows. Human Gate round-trip support extends the existing seventh bridge; no eighth workflow is introduced.

### Interruption / transaction review

Connector-only bridge execution is fail-closed at repository publication boundary: workflow commits/pushes edition-local output only after the bridge process succeeds. Partial runner filesystem writes are not published after a failed process.

Direct-local CLI, like other multi-file local Core operations, can leave an uncommitted working tree if the local process is forcibly interrupted between file writes. This is not treated as a new distributed state transaction requirement for this maintenance: such partial local work must not be committed and is restored/retried from Git authority. The current acceptance scope proves successful deterministic semantics plus fail-closed stale/byte/boundary validation; it does not introduce a generic multi-file transaction engine.

## Current PR scope check

PR #447 currently changes only shared Core/authority/test files. It contains **no `sources/` or `surveys/` edition output**. Current changed-file families are:

- one operator bridge workflow;
- shared config + AGENTS;
- Core authority/policy/worklog docs;
- Human Gate/operator request schemas;
- shared Core/bridge/Human Gate scripts;
- Core regression tests.

This preserves the Production-vs-Core-maintenance boundary.

## Diagnostic CI evidence

Diagnostic runs are not final acceptance evidence after later candidate changes.

Retained useful evidence:

- `5ffc942537eae1b9b3f40c8b344773725b72ca2f`: Core CI run `32650031572` PASS; Pipeline contract `32650031520` PASS after generic Profile path expansion repair;
- `cdf5b858d0b162c16efa2b118eed4b27293d2cf1`: Core CI `32650222383` / Pipeline `32650222392` failed only on the subsequently corrected test expectation for nonexistent `publication_candidate` machine checkpoint; direct Human Gate suite and Architecture bridge E2E were already passing;
- earlier frozen `a65e714b711e76006318a14b252aa0a4e9727b4f`: historical six-point/CI PASS, invalidated by RVF-015 and never reusable as current acceptance.

## PFB-013 status

`PARTIALLY EXERCISED / NOT PASSED`

Real cold-start Weekly, SP001/LONGFORM, representative Retrospective and Foundations-guided validation remain required after reviewed unchanged integration.

## PFB-014 status

`IMPLEMENTATION CANDIDATE / HUMAN-GATE ROUNDTRIP + REVIEWED-PARENT PROVENANCE IMPLEMENTED / SEVEN-POINT REAUDIT PENDING`

Do not close PFB-014 and do not merge PR #447 until the completion criteria in RVF-016 are satisfied.

## Freeze boundary

The repository-owned implementation/authority synchronization is now complete for all currently known findings through RVF-023. The next unchanged branch head that passes both required CI workflows is the candidate to freeze for independent audit.

After freeze, do **not** modify code, schemas, config, workflows, tests, docs, findings, worklogs or other candidate-tree content while auditing. Any newly discovered defect requiring a change invalidates that freeze and returns work to Core maintenance.

## Next actions

```text
obtain green CI on the current synchronized tree
-> inspect exact PR scope/head one final time without mutation
-> declare that exact SHA frozen
-> rerun/confirm exact-head Core CI + Pipeline contract tests on that unchanged SHA
-> switch from implementer role to independent auditor role
-> audit Points 1–7 from Point 1 on unchanged SHA
-> if any point needs repository change: invalidate freeze and return to implementation
-> only after unchanged 7/7 PASS: record result outside candidate tree and mark PR #447 Ready for Human full-candidate review
```

W33/SP001 production validation remains paused. Do not restart those editions until the shared Core maintenance candidate is reviewed and integrated unchanged.

Repository reality and canonical Production State, once created, outrank this human-readable summary.
