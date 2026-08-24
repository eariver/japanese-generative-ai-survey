# Survey Production Core v2 — post-completion final audit rule

Status: `CANONICAL SEVEN-POINT FIXED-HEAD AUDIT RULE / FOLLOW-UP REVIEW HARDENING SYNCHRONIZED`  
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

### Connector-safe trust bootstrap

The audit must not merely inspect the bridge helper. It must prove the root of trust:

- work-branch `survey-production-v2-operator-bridge.yml` is read-only/unprivileged signal only;
- it has no repository-write permission, Core execution, or trusted admission logic;
- trusted operator admission/execution is owned by `pipeline-contract-tests.yml` through `workflow_run` default-branch authority;
- the read-only preflight checks exact `workflow_run.head_sha` as data;
- request-only commit, request/head-branch identity, reviewed-main ancestry, Human reviewed-commit/request-parent binding, and protected-Core equality all pass before a write-capable job exists;
- protected-path configuration is read from the named reviewed-main commit, not the untrusted work branch;
- only a dependent post-preflight job receives `contents: write`;
- generated writes remain Profile-bound and immutable request authority is not mutated;
- generic/arbitrary Human-decision or executable surfaces remain absent.

A write-capable verifier loaded from the work branch under review is a Point-7 failure even if its script text appears to perform the right checks.

## 4. CI evidence

The final audit requires exact-head evidence from:

- Survey Production Core v2 CI;
- Pipeline contract tests;
- schema/config parse/compile checks included by those suites;
- positive/negative Human Gate direct and bridge regressions;
- workflow trust-bootstrap static contract regressions;
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

- operator-bridge workflow = read-only work-branch signal;
- pipeline-contract workflow = normal CI plus trusted default-branch workflow_run operator preflight/execution;
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

The connector-safe matrix must also prove the trusted default-branch operator path in real branch execution after integration; static PR tests cannot by themselves prove the default-branch `workflow_run` transport is operational.

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

The candidate `9932c8b7a14f1c3bdcc775df88056681b2841514` and its former 7/7 result are historical/invalidated evidence. Follow-up review found:

- untrusted work-branch trust bootstrap;
- insufficient reviewed-commit durability;
- missing Publication Preview upstream correction/reopen path.

Those findings must be fully repaired and audited on a later exact SHA before PR #447 can return to Ready for Human review.
