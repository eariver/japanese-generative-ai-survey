# Survey Production Core v2 — RVF-026 operator runtime import-boundary repair

Status: `FOLLOW-UP REVIEW FINDING ACCEPTED / FREEZE INVALIDATED / EXACT-HEAD CI REQUIRED`

Recorded: 2026-08-24 JST

Previous frozen candidate:

`109579e0f9b2988b62074165b28f144ac3b1ad55`

Previous exact-head evidence:

- Survey Production Core v2 CI `32735493697`: PASS
- Pipeline contract tests `32735493721`: PASS
- fresh fixed-head audit: 7/7 PASS

Those results are now **historical only**. A follow-up Human review identified a new shared-Core trust-boundary defect after that audit.

## RVF-026 — untrusted checkout could influence Python startup before admission

The default-branch `issue_comment` topology remains the correct operator-bridge trust root, but the trusted preflight checked out the untrusted request commit and then parsed request/config data with ordinary Python startup:

```text
python -c ...
python - ...
```

Before protected-Core equality had been proven, normal Python import search could include repository-local paths. A work-branch parent could therefore add a top-level module such as `json.py` outside the protected roots, then add an otherwise request-only child commit. The trusted workflow definition would still come from default branch, but the preflight Python process could execute/import work-branch bytes before trust admission.

The same review also noted that the write-capable executor used:

```text
python scripts/survey_core_execution_bridge_v2.py ...
```

while the bridge imports sibling Core modules through the `scripts` package. That exact Actions process-startup form was not covered by the existing in-process bridge E2E and could have different `sys.path` behavior.

## Repair

The operator workflow is hardened in two layers.

### 1. Pre-admission helpers are isolated

Every Python helper used while the checkout is still untrusted now starts in isolated mode (`-I`), including:

- request field extraction;
- Human Gate parent-binding extraction;
- reviewed-main protected-path derivation.

This blocks repository-local import shadowing such as a top-level `json.py`, `sitecustomize.py`, or `PYTHONPATH`-supplied checkout module from participating in the trust decision.

### 2. Write-capable Core execution uses a reviewed-main-only runtime

After preflight admission, the executor:

1. rechecks the canonical work branch and reviewed-main ancestry;
2. materializes only `scripts/` from the admitted `reviewed_main_sha` into a separate runner-temporary trusted runtime;
3. installs dependencies with isolated Python startup;
4. runs the bridge as the package module `scripts.survey_core_execution_bridge_v2` from that trusted runtime;
5. passes the admitted checkout explicitly as `--repo-root` and the request as an explicit absolute data path;
6. uses isolated Python for later JSON-only result parsing before commit/push.

Therefore arbitrary unprotected files in the work checkout are never a Python import root inside the write-capable job.

## Regression coverage

`tests/test_survey_operator_workflow_ci_contract_v2.py` now additionally requires:

- isolated preflight Python command forms;
- no legacy non-isolated request/config parse form;
- the reviewed-main `scripts/` runtime materialization;
- package-module CLI execution with explicit `--repo-root`;
- isolated dependency/result helper invocations;
- a poisoning regression proving a checkout-local `json.py` cannot affect isolated preflight parsing;
- an exact subprocess smoke matching the workflow module-startup shape from a separate trusted runtime while a malicious top-level `json.py` exists in the admitted repository root.

The CLI smoke uses a schema-valid request at a deliberately noncanonical request path. Success means the actual module process starts, imports the Core package, loads the operator request schema, and reaches canonical-path validation without importing the poisoning module.

## Acceptance sequence reset

Because this repair mutates the candidate tree:

```text
109579e0... freeze invalidated
+ 109579e0... 7/7 audit invalidated
-> repair commit
-> exact-head Survey Production Core v2 CI PASS
+ exact-head Pipeline contract tests PASS
-> final stale-text / PR-scope / workflow-count cross-check
-> freeze new exact SHA outside candidate tree
-> rerun Points 1-7 from Point 1
```

Any further tree mutation after the next freeze invalidates that freeze and the complete audit again.

PR #447 remains Draft until a new unchanged fixed-head 7/7 PASS is recorded. Human explicit approval is still required before merge.

W33 and SP001 real-production validation remain paused until reviewed unchanged Core integration.
