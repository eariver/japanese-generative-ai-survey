# Survey Production Core v2 — post-completion final audit rule

Status: `CANONICAL SEVEN-POINT FIXED-HEAD AUDIT RULE / RVF-026 RUNTIME-IMPORT HARDENING SYNCHRONIZED`  
Established: 2026-08-22 JST  
Updated: 2026-08-24 JST

## 1. Mandatory order

A final audit is valid only after every intended implementation/test/doc/worklog change is complete.

```text
finish all candidate changes
-> finish diagnostic regression/CI repair
-> synchronize repository authority
-> pre-freeze cross-check full PR scope
-> freeze one candidate head SHA
-> run all seven acceptance points from zero on that exact SHA
-> do not mutate candidate during audit
-> only 7/7 PASS may be presented for Human full-candidate review
```

Any candidate-tree mutation invalidates the entire audit. No PASS verdict may be carried forward after mutation.

The final result is recorded outside the candidate tree, normally in PR/Human-review metadata, so recording PASS does not change the audited SHA.

## 2. Seven acceptance points

1. **Weekly viability** — generic Weekly Profile, required X/Grok intake, exact Drive handoff/result disposition, reader-facing Weekly requirements, no edition-specific rescue Core.
2. **Special viability** — configured Retrospective through the pre-existing generic `survey_period_v2`, standalone Thematic/LONGFORM, and Foundations living-series compatibility without parallel cadence/series engines.
3. **Generality** — no W33/SP001/topic/cadence/source-depth/branch-family overfit; Profile/Publication/edition authority remain orthogonal.
4. **Historical/clarified recurrence prevention** — crisp invariants are deterministic; semantic/editorial/visual judgment remains ChatGPT-owned; Human decision remains at the two normal Gates.
5. **Control proportionality** — no unnecessary workflow/Human ceremony or machine impersonation of qualitative judgment; Actions policy is satisfied.
6. **Autonomous progression / stop discipline** — after target+requested Gate, ordinary research/editorial/QA/retry work proceeds without routine Human confirmation; production does not debug shared Core in place.
7. **Human Gate round-trip viability** — both normal Gates support exact committed review, `APPROVED`, `REQUEST_CHANGES`, dependency-aware invalidation, rN continuation, stale/byte-drift rejection, durable review provenance, and connector-safe execution without delegating Human judgment.

## 3. Point 7 mandatory evidence

Point 7 must explicitly prove all of the following.

### Architecture

- Architecture r1 `APPROVED` resumes drafting.
- Architecture r1 `REQUEST_CHANGES` can return to every allowed pre-Architecture dependency class and return as Architecture r2.
- stale r1 approval after r2 fails.
- changed reviewed bytes and invalid boundaries fail closed.

### Publication Preview — publication-local repair

- Publication r1 `APPROVED` resumes Freeze.
- Publication r1 `REQUEST_CHANGES` to drafting/validation boundaries invalidates only affected publication authority and preserves valid active Architecture approval.
- r2 approval binds only r2 Candidate/PDF bytes.

### Publication Preview — upstream/cross-gate repair

- Publication r1 `REQUEST_CHANGES` may select an allowed boundary before `ARCHITECTURE_ESTABLISHED` when feedback reveals an upstream defect.
- active canonical Architecture approval is verified, superseded, and removed from current authority.
- prior Architecture rN review record and immutable approval snapshot remain hash-verifiable historical evidence.
- Architecture Review becomes pending and the run must pass through Architecture rN+1 before publication may continue.
- a later Publication rN+1 can be approved and resume Freeze.
- cross-gate reopen is normal revision, not an Owner Exception Gate.

### Reviewed-commit durability

Direct-local Core must reject:

- nonexistent reviewed commit;
- dangling/unreachable reviewed commit not retained on canonical Profile work branch;
- commit missing a reviewed path;
- non-regular reviewed path;
- same-path/different-byte reviewed commit.

A valid reviewed commit must be reachable from canonical `work_branch` and contain exact reviewed State/Gate bytes. Publication includes exact Candidate-bound PDF.

### Connector-safe trust bootstrap and runtime isolation

The audit must not merely inspect the bridge helper. It must prove the complete root of trust, including process startup/import behavior:

- operator execution is initiated only through `survey-production-v2-operator-bridge.yml` loaded from default-branch `issue_comment` authority;
- the persistent transport surface is Issue `#448`, which is not a Human Gate or editorial authority;
- only exact `/survey-core-execute <lowercase-40-hex-request-commit>` comments from an authorized repository association are actionable;
- supplied request SHA/work branch are treated as untrusted data until preflight completes;
- every Python helper that inspects untrusted request/config data before admission uses isolated Python startup and cannot import repository-local work-branch code;
- the request SHA must be the exact current canonical work-branch head;
- request-only commit, reviewed-main ancestry, Human reviewed-commit/request-parent binding, and protected-Core equality all pass before a write-capable job exists;
- protected-path configuration is read from the named reviewed-main commit, not the untrusted work branch, using an isolated parser environment;
- only a dependent post-preflight job receives `contents: write`;
- the write-capable executor rechecks work-branch/reviewed-main authority and executes Core Python from a separately materialized reviewed-main runtime, not from the admitted worktree import root;
- the actual package-module subprocess startup form used by Actions is regression-tested in a clean trusted runtime while a poisoning top-level `json.py` exists in the admitted repository root, and the poison is not imported;
- JSON-only helper parsing after execution remains isolated from repository-local imports;
- the canonical work branch is rechecked after preflight and output push is lease-bound to the admitted request head;
- generated writes remain Profile-bound and immutable request authority is not mutated;
- generic/arbitrary Human-decision or executable surfaces remain absent;
- there is no work-branch signal workflow and no `workflow_run` trust hop.

A write-capable verifier loaded from the work branch under review is a Point-7 failure even if its script text appears to perform the right checks. Likewise, a default-branch workflow that executes/imports untrusted checkout Python before admission, or a write-capable executor that uses the admitted worktree as its Core Python import root, is a Point-7 failure.

## 4. CI evidence

The final audit requires exact-head evidence from:

- Survey Production Core v2 CI;
- Pipeline contract tests;
- schema/config parse/compile checks included by those suites;
- positive/negative Human Gate direct and bridge regressions;
- workflow trust-bootstrap static contract regressions;
- RVF-026 import-poisoning regression and exact package-module subprocess startup smoke matching the Actions command form;
- cross-profile fixtures.

CI may run on the PR merge candidate only when it consists of the exact frozen head plus the unchanged audited base.

## 5. Actions surface

The intended workflow set remains exactly seven:

1. `pipeline-contract-tests.yml`
2. `survey-production-v2-ci.yml`
3. `build-weekly-survey.yml`
4. `build-special-pdf.yml`
5. `survey-production-v2-export-publication-preview.yml`
6. `survey-production-v2-release.yml`
7. `survey-production-v2-operator-bridge.yml`

Responsibilities matter as much as filenames:

- `pipeline-contract-tests.yml` = independent read-only CI only;
- `survey-production-v2-operator-bridge.yml` = trusted default-branch Issue `#448` admission/preflight plus dependent deterministic executor using isolated pre-admission parsing and reviewed-main runtime execution;
- Release remains the only lifecycle `WORKFLOW_DISPATCH` edge.

An eighth workflow is prima facie regression unless separately reviewed under the Actions admission rule.

## 6. Reader/publication boundary

The audit must confirm:

- internal Selection/Evidence/Architecture/Draft artifacts are not legal fallback publication prose;
- ChatGPT authors canonical reader-facing source;
- deterministic QA, semantic/editorial QA, and exact-PDF visual QA remain distinct;
- Candidate atomically binds exact source/PDF/review authority;
- changed source/PDF invalidates Candidate/Preview/Freeze identity.

## 7. Production/Core boundary

A formal post-integration production validation run that discovers a shared-Core defect is failed evidence. Repair Core separately and rerun the affected scenario cleanly. Do not salvage the same edition in place and call it cold-start PASS.

## 8. Post-integration validation matrix

After fixed-head 7/7 PASS, Human approval, and unchanged integration into `main`, run:

- one future Weekly cold start;
- standalone Thematic/LONGFORM with SP001 regression;
- representative configured Retrospective Period through existing `survey_period_v2`;
- one Foundations-guided scenario through at least Architecture Review;
- structural monthly/half-year/annual and unplanned-Thematic compatibility confirmation.

The connector-safe matrix must also exercise the trusted default-branch Issue `#448` operator path in real branch execution after integration; static PR tests cannot by themselves prove the default-branch transport is operational.

## 9. Invalidation rule

If any point reveals a defect requiring repository mutation:

```text
record/classify finding
-> audit INVALID
-> leave Human full-candidate review boundary
-> repair Core
-> rerun CI/synchronization
-> freeze new SHA
-> rerun Points 1–7 from Point 1
```

There is no partial-audit resume after candidate mutation.

## 10. Current historical warning

The candidates `9932c8b7a14f1c3bdcc775df88056681b2841514` and `109579e0f9b2988b62074165b28f144ac3b1ad55` and their former 7/7 results are historical/invalidated evidence.

Follow-up review findings across those candidates established four trust/lifecycle requirements:

- operator trust bootstrap must originate from default-branch authority, not a work-branch workflow;
- reviewed Human commits must be durable/reachable and exact-bind reviewed bytes;
- Publication Preview must support dependency-aware upstream correction/reopening of Architecture;
- default-branch workflow authority is still insufficient if Python startup/import behavior can execute repository-local work-branch code before admission or if the write-capable executor imports Core from the admitted worktree. RVF-026 therefore requires isolated pre-admission parsing, reviewed-main runtime execution, and exact CLI startup regression.

An intermediate read-only branch signal + `workflow_run` design was also rejected during repair because it still depended on work-branch workflow definition for signaling. It must not be treated as current authority.

Those findings must be fully repaired and audited on a later exact SHA before PR #447 can return to Ready for Human review.
