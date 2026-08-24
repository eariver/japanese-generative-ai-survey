# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `RVF-025 FOLLOW-UP REVIEW REPAIRS SYNCHRONIZED / PRE-FREEZE DIAGNOSTIC CI`

Established: 2026-08-23 JST  
Last updated: 2026-08-24 JST

Integrated Core baseline that exposed the operator gap: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`  
Maintenance-start `main`: `2bcaa7d1df1826ab8848c25de8bf2373d85a8e75`  
Maintenance branch: `maintenance/core-v2-operator-execution-bridge`  
Maintenance PR: `#447 Core v2: add deterministic operator execution bridge`  
Connector operator transport queue: GitHub Issue `#448`

W33/SP001 remain paused non-PASS production-validation evidence until reviewed unchanged maintenance integration.

## Resume checkpoint

The post-merge W33/SP001 trials proved real ChatGPT research/editorial work and the W33 Human-mediated Grok/Drive handoff, but exposed that the connector runtime cannot necessarily invoke canonical local Core on the exact work branch. Shared-Core maintenance added a narrow deterministic operator bridge and later expanded it to canonical Human Gate approval/revision mechanics.

The bridge request allowlist remains exactly eight:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

Human remains sole decision authority. ChatGPT owns research/editorial/visual repair. Actions/Core only validate and record explicit input and deterministic lifecycle consequences. Configured Retrospective initialization reuses existing `scripts/survey_period_v2.py`; no second Retrospective builder survives.

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

### RVF-002 — X/community and technical Evidence separation works
Status: `CONFIRMED EDITORIALLY / CANONICAL VALIDATION PENDING POST-INTEGRATION`

### RVF-003 — fresh X can materially change Weekly Architecture
Status: `CONFIRMED BY W33`

### RVF-004 — Thematic X may legitimately be `NOT_REQUIRED`
Status: `CONFIRMED EDITORIALLY BY SP001 / CANONICAL RECORD PENDING POST-INTEGRATION`

### RVF-005 — operator execution path was a blocking dependency
Status: `CONFIRMED / BRIDGE IMPLEMENTED / FINAL REAUDIT PENDING`

### RVF-006 — do not fabricate machine acceptance
Status: `CONFIRMED OPERATIONAL RULE`

### RVF-007 — edition-local execution records remain required
Status: `CONFIRMED / POLICY SYNCHRONIZED`

### RVF-008 — old failed artifacts remain non-authoritative
Status: `CONFIRMED`

### RVF-009 — stale workflow-count authority
Status: `FOUND / REPAIRED / AUDIT INVALIDATED`

Candidate `89b0a02c8699c957dc8ca09d0228e9d8b4ce7287` described six workflows after bridge made seven.

### RVF-010 — missing Retrospective bridge exposure
Status: `FOUND / REPAIRED / AUDIT INVALIDATED / DIAGNOSIS CORRECTED`

Existing generic `survey_period_v2.resolve_configured_period()` + `period_profile()` was reused; temporary duplicate Retrospective adapter/schema/tests were removed.

### RVF-011 — bridge glue init -> Discovery E2E
Status: `IMPLEMENTED / REGRESSION RETAINED`

### RVF-012 — Retrospective authority synchronization
Status: `HISTORICAL REPAIR RETAINED`

### RVF-013 — Retrospective request fixture binds existing Period builder
Status: `IMPLEMENTED / REGRESSION RETAINED`

### RVF-014 — earlier frozen candidate cross-check
Status: `HISTORICAL PASS FOR a65e714b... / INVALIDATED BY RVF-015`

### RVF-015 — pre-approval audit found Human Gate control gaps
Status: `HG-001/HG-002 FOUND / REPAIR IMPLEMENTED / REAUDIT PENDING`

- HG-001: connector-only Human approval recorder missing.
- HG-002: ordinary Human `REQUEST_CHANGES` rN/selective invalidation path missing.

### RVF-016 — Human Gate round-trip completion contract
Status: `PLAN LOCKED / ACCUMULATED REPAIRS IMPLEMENTED / FREEZE NOT YET DECLARED`

Both normal Human Gates must support committed exact review → explicit Human `APPROVED` or `REQUEST_CHANGES` → deterministic consequence → autonomous repair/revalidation → next contiguous revision without Actions/Core making Human/editorial decisions.

### RVF-017 — canonical Human Gate review authority
Status: `IMPLEMENTED / FINAL FIXED-HEAD EVIDENCE PENDING`

Machine review rN records/index, exact reviewed State/artifact hashes, explicit Human provenance and deterministic invalidation are implemented.

### RVF-018 — bridge expanded from four to eight request kinds
Status: `IMPLEMENTED / DIRECT + BRIDGE REGRESSION COVERAGE PRESENT`

No generic Human-decision/rejection/arbitrary executable surface was added.

### RVF-019 — Publication E2E exposed `{survey_root}` checkpoint expansion defect
Status: `FOUND / SHARED CORE FIXED / HISTORICAL DIAGNOSTIC PASS`

Generic Profile path-token expansion was repaired.

### RVF-020 — direct Human Gate approve/revise E2E
Status: `IMPLEMENTED / EXTENDED BY RVF-025`

### RVF-021 — bridge-backed Human Gate E2E
Status: `IMPLEMENTED / EXTENDED BY RVF-025`

### RVF-022 — seven-point/Human Gate authority sync
Status: `SUPERSEDED BY RVF-024/RVF-025`

### RVF-023 — Human-reviewed commit differs from request/event commit
Status: `FOUND / REPAIRED / RETAINED`

Connector Human Gate requests carry explicit `reviewed_repository_commit_sha`; workflow requires it to equal exact request parent while receipt records request/event commit separately.

### RVF-024 — direct-local reviewed-commit provenance gap
Status: `FOUND / 0a9 FREEZE INVALIDATED / REPAIRED`

Candidate `0a9e2d2c5bd9124ba626cdc7558e645d8021946c` had Core CI `32652165318` PASS and Pipeline `32652165338` PASS, but fresh seven-point audit failed Point 7 because direct-local Human Gate did not prove commit existence/tree-byte identity. Canonical commit-tree proof was added.

A later candidate `9932c8b7a14f1c3bdcc775df88056681b2841514` then passed fresh 7/7, but follow-up PR review invalidated that freeze under RVF-025.

### RVF-025 — follow-up PR review found three post-7/7 gaps
Status: `FOUND / 9932 FREEZE INVALIDATED / REPAIRS SYNCHRONIZED / NEW FREEZE PENDING`

Follow-up review comment on PR #447 examined fixed candidate `9932c8b7a14f1c3bdcc775df88056681b2841514`. Its former 7/7 PASS is **INVALIDATED**.

#### F1 — operator trust bootstrap

Problem: the verifier/executor was loaded from the same work-branch event commit it was trying to admit.

An intermediate read-only work-branch signal + default-branch `workflow_run` design was implemented temporarily, then rejected during independent pre-freeze analysis because the signal workflow definition itself still came from the untrusted branch.

Final design:

```text
request-only commit pushed as exact current work-branch head
-> ChatGPT comments on persistent operator queue Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> survey-production-v2-operator-bridge.yml runs from default-branch issue_comment authority
-> read-only preflight treats supplied SHA/branch as untrusted data
-> prove exact current work head / request-only commit / reviewed-main ancestry
-> derive protected paths from reviewed-main config and prove byte equality
-> prove Human reviewed-parent binding where applicable
-> only then dependent executor receives contents: write
-> recheck branch head
-> execute canonical bridge
-> push edition-local output with force-with-lease against admitted head
```

`pipeline-contract-tests.yml` is CI-only. No eighth workflow exists. Issue #448 is transport only, not a Human Gate.

#### F2 — reviewed-commit durability

Problem: a dangling `commit-tree` object can exact-bind bytes but disappear after GC/fresh clone.

Repair:

- reviewed commit must exist;
- exact reviewed State/Gate-input/PDF bytes must match;
- reviewed commit must be reachable from Profile-bound canonical work branch;
- Human Gate procedure requires commit + push/retain before presentation;
- dangling/unreachable commits fail closed;
- APPROVED decisions get immutable `gates/reviews/approvals/*-rN.json` snapshots.

#### F3 — Publication Preview upstream correction

Problem: Publication feedback may reveal Evidence/Selection/Architecture defects; Draft-only rollback was insufficient and Owner Exception would be inappropriate.

Repair:

- Publication revision boundaries can reach upstream lifecycle states;
- Human chooses the boundary; Core never does;
- crossing before `ARCHITECTURE_ESTABLISHED` verifies then supersedes/removes active canonical Architecture approval;
- prior Architecture rN review and immutable approval snapshot remain historical authority;
- Architecture Review becomes pending;
- lifecycle/checkpoints return to Human-selected boundary;
- Architecture rN+1 is mandatory before new drafting/publication;
- direct and bridge E2E cover Publication r1 → Selection → Architecture r2 → Publication r2.

This adds no third Human Gate.

## Current maintenance design after RVF-025

### Connector trust

Only default-branch `issue_comment` workflow authority can admit operator execution. The request SHA must equal the exact current canonical work-branch head. Work-branch movement before execution/push fails closed.

### Human review provenance

Review surfaces are durable canonical work-branch commits, not dangling objects. Connector Human Gate requests additionally use the reviewed commit as exact request-only parent.

### Cross-gate revision

Publication-local corrections preserve active Architecture. Upstream corrections supersede active Architecture and reopen `ARCHITECTURE_REVIEW` at its next contiguous revision.

### Actions surface

Exactly seven workflows. `pipeline-contract-tests.yml` is CI-only; `survey-production-v2-operator-bridge.yml` is trusted default-branch Issue #448 operator execution.

## Historical diagnostic evidence

Earlier runs/audits are diagnostic only after later tree changes. Notable examples:

- `5ffc942...`: Core `32650031572` PASS; Pipeline `32650031520` PASS after path expansion repair.
- `0a9e2d2...`: Core `32652165318` PASS; Pipeline `32652165338` PASS; seven-point audit failed Point 7.
- `9932c8b7...`: exact-head CI + fresh 7/7 PASS, later invalidated by RVF-025.

No historical PASS may be reused for the next candidate.

## Current PR scope rule

PR #447 must contain only shared Core/authority/schema/workflow/test files. No edition-local `sources/` or `surveys/` output may be included. Issue #448 is external operational metadata.

## Freeze boundary

**No current candidate is frozen.**

Before a new freeze:

```text
finish RVF-025 diagnostic CI repair
-> current-authority stale-text cross-check
-> exact PR scope/head inspection
-> require Core CI + Pipeline contract PASS on final synchronized head
-> freeze exact SHA
```

After freeze, do not change candidate-tree content during audit. Any defect requiring mutation invalidates the freeze.

## Next actions

```text
obtain green diagnostic CI
-> final stale-text + PR-scope cross-check
-> exact-head Core CI + Pipeline contract PASS
-> declare exact SHA frozen
-> switch to independent auditor role
-> audit Points 1–7 from Point 1; reuse no earlier verdict
-> Point 7 explicitly audits default-branch Issue #448 trust root, durable review reachability, and Publication→Architecture cross-gate round trip
-> if any point needs change: invalidate freeze and return to implementation
-> only unchanged 7/7 PASS: record audit outside candidate tree and mark PR #447 Ready for Human full-candidate review
```

W33/SP001 production validation remains paused until reviewed shared Core integration. Repository reality and canonical Production State outrank this human-readable summary.
