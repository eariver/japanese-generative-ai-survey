# Survey Production Core v2 — RVF-025 pre-freeze checkpoint

Status: `PRE-FREEZE SYNCHRONIZED / EXACT-HEAD CI REQUIRED`

Recorded: 2026-08-24 JST

This file supplements `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md` immediately before the next fixed-head freeze for PR #447. It records the final pre-freeze findings discovered after the RVF-025 follow-up repairs. The canonical worklog remains historical state-at-commit evidence; this checkpoint is the last intended candidate-tree mutation before exact-head CI and freeze.

## Candidate context

- Repository: `eariver/japanese-generative-ai-survey`
- Maintenance branch: `maintenance/core-v2-operator-execution-bridge`
- PR: `#447 Core v2: add deterministic operator execution bridge`
- Base: `main`
- Operator transport queue: GitHub Issue `#448`
- W33/SP001 production validation remains paused until reviewed unchanged Core integration.

No earlier fixed-head PASS is acceptance evidence for the next candidate. In particular, the former `9932c8b7a14f1c3bdcc775df88056681b2841514` 7/7 result remains invalidated by RVF-025.

## Diagnostic head and CI

Pre-freeze diagnostic head:

`04043b2d71b8ce00b53ef4dce1c59e0ad7956af0`

Exact-head diagnostic CI on that SHA:

- Survey Production Core v2 CI run `32732448477`: `PASS`
- Pipeline contract tests run `32732448326`: `PASS`

These runs prove the synchronized tree at `04043b2d...`, but they become historical diagnostic evidence after this checkpoint commit changes the candidate head. They must not be carried forward as final fixed-head evidence.

## Final pre-freeze findings repaired

### PF-001 — stale textual regressions after authority synchronization

Four tests failed after current authority wording changed while their string-level expectations remained stale. The implementation and Human Gate round-trip E2E were already passing. Repairs changed only the assertions so they verify current semantics rather than superseded wording:

- configured Retrospective identity checks the reusable Period builder contract rather than one historical sentence;
- final-audit mutation semantics accept the current `invalidates` wording rather than requiring the literal `invalidate` token in one location;
- bootstrap regression checks current autonomous-progression wording;
- request-path glob presence is distinguished from a prohibited work-branch `push` trigger.

### PF-002 — canonical Human-review work-branch ref was implicit

`scripts/survey_human_gate_v2.py` requires a reviewed commit to remain reachable from the Profile-bound canonical `origin/<work_branch>` ref when an origin exists. The operator workflow previously fetched the branch into a temporary alias and could therefore rely on incidental `actions/checkout` remote-ref materialization.

Repair:

- trusted preflight explicitly materializes `refs/remotes/origin/<request_work_branch>`;
- executor explicitly materializes `refs/remotes/origin/<REQUEST_HEAD_BRANCH>` before canonical Human Gate execution;
- exact current work-head equality is checked against that canonical ref;
- the temporary `origin/operator-work` alias is no longer used.

This makes the workflow explicitly satisfy the same durable-reachability contract enforced by canonical Human Gate Core.

### PF-003 — focused Core CI did not watch operator workflow-only changes

`pipeline-contract-tests.yml` already watched `.github/workflows/*.yml`, but `survey-production-v2-ci.yml` omitted `survey-production-v2-operator-bridge.yml` from its push/pull_request path filters.

Repair:

- add `.github/workflows/survey-production-v2-operator-bridge.yml` to both Core CI path filters;
- add a dedicated regression test requiring both regression workflows to watch the operator workflow.

A future operator workflow-only change must therefore receive both focused Core and pipeline-contract validation.

### PF-004 — stale trusted-workflow config authority

`config/survey-production-v2.json` still carried an intermediate design value:

`workflow_control.operator_execution_trusted_workflow = pipeline-contract-tests.yml`

That contradicted current authority, where `pipeline-contract-tests.yml` is CI-only and the operator workflow itself is trusted because `issue_comment` workflow code is loaded from the default branch.

Repair:

- `operator_execution_trusted_workflow = survey-production-v2-operator-bridge.yml`;
- dedicated regression fixes this identity and explicitly rejects `pipeline-contract-tests.yml` as the trusted operator executor.

## Current trust topology

The intended connector path is now exactly:

```text
ChatGPT commits one immutable request-only commit on the Profile work branch
-> request commit is exact current work-branch head
-> ChatGPT comments on Issue #448:
     /survey-core-execute <lowercase-40-hex-request-commit>
-> default-branch issue_comment authority loads survey-production-v2-operator-bridge.yml
-> read-only preflight treats supplied SHA/branch as untrusted data
-> prove request-only commit / exact current canonical work head / reviewed-main ancestry
-> derive protected paths from reviewed-main config and prove byte equality
-> for Human Gate operations, bind reviewed_repository_commit_sha to exact request parent
-> materialize canonical origin/<work_branch> review reachability
-> only dependent post-preflight job receives contents: write
-> recheck current branch head
-> execute narrow canonical bridge operation
-> enforce edition-local write boundary and immutable request boundary
-> lease-bound push against admitted request head
```

There is no work-branch signal workflow and no `workflow_run` trust hop. `pipeline-contract-tests.yml` remains independent read-only CI. The intended Actions surface remains exactly seven workflows.

## Human Gate invariants rechecked pre-freeze

The synchronized implementation was manually cross-checked before this checkpoint:

- operator request allowlist remains exactly eight operations: three initialization operations, `ADVANCE_STAGE`, and four gate-specific approval/revision operations;
- no arbitrary command/module/script/workflow surface exists;
- no generic `EXECUTE_HUMAN_DECISION` or routine `REJECTED` bridge operation exists;
- `expected_revision` is checked against contiguous per-Gate review history, so an r1 request cannot apply to r2;
- reviewed commit must exist, be reachable from canonical Profile work branch, and contain exact current State/Gate-input bytes;
- Publication Preview review additionally exact-binds the Candidate-bound PDF;
- `APPROVED` produces an immutable per-revision approval snapshot;
- `REQUEST_CHANGES` requires a Human-selected allowed regeneration boundary and non-empty requested changes;
- Publication-local revision preserves active Architecture;
- Publication upstream revision verifies and supersedes active canonical Architecture approval, preserves historical review/snapshot authority, clears current Architecture provenance, and reopens Architecture Review at the next contiguous revision;
- only downstream checkpoint/gate authority at or after the selected regeneration boundary is invalidated;
- bridge receipts distinguish request/event commit from Human-reviewed commit.

## Generality / responsibility cross-check

Pre-freeze inspection also reconfirmed:

- Weekly initialization remains generic rolling-window Profile construction;
- configured monthly, half-year, and annual retrospective editions reuse one `RETROSPECTIVE_PERIOD + LONGFORM_SPECIAL` builder;
- custom bounded Retrospective periods use the same generic builder;
- unknown configured period slugs and not-yet-ended periods fail closed;
- Thematic remains first-class and Profile-bound rather than SP001-specific;
- no W33/SP001 topic logic was added to the operator bridge;
- Actions count remains exactly seven;
- Release remains the only lifecycle `WORKFLOW_DISPATCH` edge;
- Pipeline contract workflow remains read-only CI, not operator admission or production mutation authority.

## PR scope

Immediately before this checkpoint, PR #447 contained only shared Core/authority/config/schema/workflow/test files and no edition-local `sources/` or `surveys/` output. This checkpoint itself is shared Core maintenance provenance under `docs/checkpoints/`.

## Freeze protocol from this commit forward

The commit produced by this file is the next **pre-freeze candidate head**, not yet a frozen or accepted candidate.

Required sequence:

```text
obtain Core CI PASS on exact new head
+ obtain Pipeline contract PASS on exact new head
-> confirm PR head/scope unchanged
-> declare that exact SHA frozen outside the candidate tree
-> do not mutate candidate-tree content
-> audit Points 1–7 from Point 1 with no inherited verdicts
-> Point 7 must explicitly cover:
     default-branch Issue #448 trust bootstrap
     canonical origin/<work_branch> reviewed-commit durability
     stale rN request rejection
     Architecture approve/revise round trip
     Publication approve/revise round trip
     Publication -> upstream Architecture reopen -> rN+1 round trip
-> any defect requiring repository mutation invalidates the freeze
-> only unchanged 7/7 PASS may mark PR #447 Ready for Human full-candidate review
```

The final audit verdict must be recorded outside the frozen candidate tree. W33/SP001 remain paused until reviewed shared Core integration.
