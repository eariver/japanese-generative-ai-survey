# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `FOLLOW-UP REVIEW F1–F3 REPAIRED / DEFAULT-BRANCH TRUST ROOT / PRE-FREEZE DIAGNOSTIC CI`

Established: 2026-08-23 JST  
Last updated: 2026-08-24 JST

Integrated Core baseline that exposed the operator gap: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`  
Maintenance-start `main`: `2bcaa7d1df1826ab8848c25de8bf2373d85a8e75`  
Maintenance branch: `maintenance/core-v2-operator-execution-bridge`  
Maintenance PR: `#447 Core v2: add deterministic operator execution bridge`  
Connector operator transport queue: GitHub Issue `#448`

W33/SP001 remain paused non-PASS production-validation evidence until reviewed unchanged maintenance integration.

## Resume checkpoint

The post-merge W33/SP001 trials proved real ChatGPT research/editorial work and the real W33 Human-mediated Grok/Drive handoff, but exposed that the connector runtime cannot necessarily invoke canonical local Core on the exact work branch. Shared-Core maintenance added a narrow deterministic operator bridge and later expanded it to cover canonical Human Gate approval/revision mechanics.

The bridge request allowlist remains exactly:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

Human remains sole decision authority. ChatGPT owns research/editorial/visual repair. Actions/Core only validate and record explicit input and deterministic lifecycle consequences.

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

One self-contained Drive task file + exact Human path mediation + exact Raw import works. No Grok connector is required.

### RVF-002 — X/community and technical Evidence separation works
Status: `CONFIRMED EDITORIALLY / CANONICAL MANIFEST VALIDATION PENDING POST-INTEGRATION`

Grok/X supplies salience/community signal; technical claims still require authoritative Evidence verification.

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

`{source_root}/execution/` remains operational continuity; Human-readable review Markdown points to exact machine review JSON.

### RVF-008 — old failed artifacts remain non-authoritative
Status: `CONFIRMED`

W33 historical `pipeline-state.json` and failed SP001 accepted artifacts remain archival only.

### RVF-009 — first maintenance audit found stale workflow-count authority
Status: `FOUND / REPAIRED / AUDIT INVALIDATED`

Candidate `89b0a02c8699c957dc8ca09d0228e9d8b4ce7287` still described six workflows after bridge made seven.

### RVF-010 — second maintenance audit found missing Retrospective bridge exposure
Status: `FOUND / REPAIRED / AUDIT INVALIDATED / DIAGNOSIS CORRECTED`

Existing generic `survey_period_v2.resolve_configured_period()` + `period_profile()` was discovered and reused; temporary duplicate Retrospective adapter/schema/tests were removed.

### RVF-011 — bridge glue init -> Discovery E2E exists
Status: `IMPLEMENTED / REGRESSION RETAINED`

Thematic initialization + X `NOT_REQUIRED` + Discovery acceptance + bridge-backed `ADVANCE_STAGE` is covered.

### RVF-012 — Retrospective authority synchronized
Status: `HISTORICAL REPAIR RETAINED`

Current authority consistently reuses existing `survey_period_v2` and prohibits a second cadence engine.

### RVF-013 — Retrospective request fixture binds existing Period builder
Status: `IMPLEMENTED / REGRESSION RETAINED`

Representative configured request identity matches generic Period Profile; Period tests cover monthly/half-year/annual/custom bounded periods.

### RVF-014 — earlier frozen candidate cross-check
Status: `HISTORICAL PASS FOR a65e714b... / INVALIDATED BY RVF-015`

`a65e714b711e76006318a14b252aa0a4e9727b4f` passed then-current CI/six-point audit but lacked complete Human Gate continuation semantics.

### RVF-015 — pre-approval full-system audit found Human Gate control gaps
Status: `BLOCKERS IDENTIFIED / REPAIR IMPLEMENTED / REAUDIT PENDING`

- **HG-001:** connector-only Human approval recorder missing.
- **HG-002:** ordinary Human `REQUEST_CHANGES` rN/selective invalidation path missing.

PR #447 returned to Draft and final acceptance expanded to seven points.

### RVF-016 — Human Gate round-trip completion contract
Status: `PLAN LOCKED / ACCUMULATED REPAIRS IMPLEMENTED / FREEZE NOT YET DECLARED`

Goal: both normal Human Gates must support committed exact review → Human `APPROVED` or `REQUEST_CHANGES` → deterministic consequence → autonomous repair/revalidation → next contiguous revision, without Actions/Core making the Human/editorial decision.

PR may return to Ready only after exact-head CI, complete authority synchronization, fixed-head seven-point audit 7/7, and exact PR metadata binding.

### RVF-017 — canonical Human Gate review authority implemented
Status: `IMPLEMENTED / FINAL FIXED-HEAD EVIDENCE PENDING`

Added machine review records/index under `{source_root}/gates/reviews/`, exact reviewed State/artifact hashes, explicit Human provenance, and deterministic State/checkpoint invalidation.

### RVF-018 — operator bridge expanded from four to eight request kinds
Status: `IMPLEMENTED / DIRECT + BRIDGE REGRESSION COVERAGE PRESENT`

Four explicit Human Gate recorder/revision kinds were added. Generic `EXECUTE_HUMAN_DECISION`, arbitrary rejection, command/module/script/workflow surfaces remain absent.

### RVF-019 — Publication Preview E2E exposed `{survey_root}` checkpoint expansion defect
Status: `FOUND / SHARED CORE FIXED / HISTORICAL DIAGNOSTIC CI PASS`

Generic Profile path-token expansion was repaired. Diagnostic Core CI `32650031572` and Pipeline `32650031520` passed that earlier tree.

### RVF-020 — direct Human Gate approve/revise E2E
Status: `IMPLEMENTED / EXTENDED BY RVF-025`

Architecture r1 revision→r2 approval, Publication-local r1 revision→r2 approval, stale/changed/invalid inputs, exact Candidate/PDF binding, and reviewed-commit negative cases are covered.

### RVF-021 — bridge-backed Human Gate E2E
Status: `IMPLEMENTED / EXTENDED BY RVF-025`

Bridge Architecture and Publication cycles use the same canonical Human Gate implementation and preserve request/event vs Human-reviewed commit identities.

### RVF-022 — seven-point/Human Gate authority synchronization
Status: `SUPERSEDED BY RVF-024/RVF-025`

Later audits strengthened reviewed-commit and trust/cross-gate requirements.

### RVF-023 — Human-reviewed commit differs from request/event commit
Status: `FOUND / REPAIRED / RETAINED`

Human Gate request now carries `reviewed_repository_commit_sha`; connector transport requires it to equal exact request parent, while receipt records the later request/event commit separately.

### RVF-024 — first seven-point audit found direct-local reviewed-commit gap
Status: `FOUND / 0a9 FREEZE INVALIDATED / REPAIRED / SUPERSEDED BY FOLLOW-UP REVIEW`

Candidate `0a9e2d2c5bd9124ba626cdc7558e645d8021946c` had Core CI `32652165318` PASS and Pipeline `32652165338` PASS, but fresh seven-point audit failed Point 7 because direct-local Human Gate accepted a syntactically valid SHA without proving commit existence/tree-byte identity.

Repair made commit-tree byte proof canonical. The next candidate later reached `9932c8b7a14f1c3bdcc775df88056681b2841514` and passed a fresh 7/7 audit, but that later acceptance was itself invalidated by RVF-025 follow-up review.

### RVF-025 — follow-up PR review found three post-7/7 hardening gaps
Status: `FOUND / 9932 FREEZE INVALIDATED / REPAIRS IMPLEMENTED / NEW FREEZE PENDING`

Follow-up review comment on PR #447 examined fixed candidate:

`9932c8b7a14f1c3bdcc775df88056681b2841514`

Its former 7/7 PASS is **INVALIDATED**. Three findings were accepted:

#### F1 — operator trust bootstrap

Problem: the workflow that verified work-branch Core equality was itself loaded from the work-branch event commit. A branch could theoretically alter/remove the verifier it was asking to trust.

Initial attempted repair used a read-only work-branch signal plus a default-branch `workflow_run` consumer. During independent pre-freeze analysis this was rejected as incomplete because the signal workflow definition itself was still supplied by the untrusted branch.

Final repair direction:

```text
request-only commit is pushed as exact current work-branch head
-> ChatGPT posts on persistent operator queue Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> survey-production-v2-operator-bridge.yml runs from default-branch issue_comment authority
-> read-only preflight treats supplied SHA/branch as untrusted data
-> require exact current work-branch head
-> require request-only commit
-> require reviewed-main ancestry
-> derive protected paths from reviewed-main config
-> require protected-Core byte equality
-> require Human reviewed parent binding where applicable
-> only then dependent executor receives contents: write
-> recheck branch head
-> execute canonical bridge
-> push edition-local outputs with force-with-lease against admitted head
```

`pipeline-contract-tests.yml` remains CI-only. No eighth workflow was introduced.

Persistent transport Issue: `#448 Survey Production Core v2 operator bridge queue`.

#### F2 — Human reviewed-commit durability

Problem: a dangling `commit-tree` object can exact-bind bytes but may disappear after GC or fresh clone.

Repair:

- review commit must exist;
- exact reviewed State/Gate-input/PDF bytes must match;
- commit must be reachable from Profile-bound canonical work branch;
- production procedure requires commit + push/retain before Human Gate presentation;
- direct test rejects dangling/unreachable commit;
- approvals create immutable `gates/reviews/approvals/*-rN.json` snapshots so superseded active approvals do not erase historical decision evidence.

#### F3 — Publication Preview upstream correction path

Problem: Publication Preview feedback can reveal a defect in Evidence/Selection/Architecture. Draft-only rollback was insufficient, while turning this into an Owner Exception would be incorrect.

Repair:

- Publication revision schema/config permits Human-selected upstream boundaries;
- if boundary is before `ARCHITECTURE_ESTABLISHED`, active canonical Architecture approval is validated then superseded/removed;
- prior Architecture rN review and immutable approval snapshot remain historical authority;
- Architecture Review becomes pending;
- lifecycle/checkpoints return to Human-selected boundary;
- run must reach Architecture rN+1 before redrafting/publication;
- Publication returns as rN+1;
- direct and bridge E2E cover Publication r1 → Selection → Architecture r2 → Publication r2.

This does not add a third Human Gate and Core does not choose the boundary.

## Current maintenance design after RVF-025

### Trust / connector transport

Operator trust starts only from default-branch `issue_comment` workflow authority. Work-branch workflow code is never used to decide trust or obtain write authority.

Issue #448 comments are transport only. Exact request JSON remains operation authority. Supplied request SHA must equal exact current work-branch head; branch movement before execution/push fails closed.

### Human review provenance

A Human review surface is valid only when it is a durable canonical work-branch commit whose exact State/Gate bytes are reconstructable. Connector Human Gate requests additionally use that commit as exact request-only parent.

### Cross-gate revision

Publication-local corrections preserve approved Architecture. Upstream Publication corrections explicitly supersede current Architecture and reopen `ARCHITECTURE_REVIEW` at its next contiguous revision.

### Actions surface

Exactly seven workflow filenames remain. `pipeline-contract-tests.yml` is CI-only; `survey-production-v2-operator-bridge.yml` is the trusted default-branch Issue #448 operator workflow.

## Historical diagnostic evidence

Earlier CI/audit evidence remains diagnostic only after later tree changes. Notable historical runs include:

- `5ffc942...`: Core `32650031572` PASS; Pipeline `32650031520` PASS after Profile path expansion fix.
- `0a9e2d2...`: Core `32652165318` PASS; Pipeline `32652165338` PASS; seven-point audit failed Point 7.
- `9932c8b7...`: exact-head CI and fresh 7/7 audit passed, then RVF-025 follow-up review invalidated that freeze.

No historical PASS may be reused for the next candidate.

## Current PR scope rule

PR #447 must contain only shared Core/authority/schema/workflow/test files. No edition-local `sources/` or `surveys/` production output may be included. Issue #448 is external operational metadata, not candidate-tree output.

## Freeze boundary

**No current candidate is frozen.**

Before a new freeze:

```text
finish RVF-025 implementation/test/authority synchronization
-> obtain green diagnostic CI
-> search current authority for stale workflow_run/work-branch-signal/old cross-gate/reachability text
-> inspect exact PR scope/head
-> require Core CI + Pipeline contract PASS on the final synchronized head
-> freeze that exact SHA
```

After freeze, do not change code/schema/config/workflow/test/doc/worklog content during audit. Any defect requiring mutation invalidates the freeze.

## Next actions

```text
finish diagnostic CI repair for RVF-025
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
