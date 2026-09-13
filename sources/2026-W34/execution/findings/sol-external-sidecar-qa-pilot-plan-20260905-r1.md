# W34 external sidecar QA pilot plan — Sol authority r1

Status: `APPROVED_EDITION_LOCAL_SIDECAR_PILOT / EXECUTION_DEFERRED_UNTIL_POST_ARCHITECTURE_REVIEW`

Date: 2026-09-05 JST

## 1. Scope and authority boundary

W34 will pilot two independently benchmarked tools as **read-only sidecar QA instruments**. They are not Survey Production Core v2 authority, do not create lifecycle state, do not create a Human Gate, and do not replace Core-native validation, Sol review, or Human approval.

Primary authority remains reviewed `eariver/japanese-generative-ai-survey` Core v2.

Post-PR #483 reviewed main authority at pilot adoption time:

- repository: `eariver/japanese-generative-ai-survey`
- main SHA: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- merge: PR #483, Human-approved frozen candidate `cb834747cce0736a116b8bcd4c4404a179e090fb`, seven-point fixed-head audit 7/7 PASS

W34 current pre-sync branch authority when this plan is recorded:

- branch: `weekly/2026-W34-v2-work`
- pre-plan HEAD: `7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`

## 2. Pinned external tools

### Publication Boundary Validator

- tool name: `Publication Boundary Validator`
- repository: `eariver/publication-boundary-redteam`
- reviewed tool SHA: `7b9de2105c690daaafa6698c1791d51ca84a92c0`
- purpose: deterministic detection of reader-facing leakage from internal editorial/provenance/Screening/Evidence/Architecture/review-response material
- role: independent publication-boundary instrument only

### Survey Core v2 Authority Auditor

- tool name: `Survey Core v2 Authority Auditor`
- repository: `eariver/survey-core-v2-authority-auditor`
- reviewed tool SHA: `4f88e55c66646a350ed286683f98b0cbca61f633`
- purpose: independent second-opinion audit of Publication Candidate / exact PDF / reviews / Human approval / lifecycle / stale authority / exact-byte binding
- role: independent authority second opinion only

The model used to develop a tool is not production execution authority. Luna/Work is the intended deterministic execution operator; Sol triages semantic/authority conflicts; Human authority remains only at the two canonical Gates.

## 3. Post-#483 compatibility check

Compatibility review compared the tools' pinned upstream assumptions with reviewed main `a9f121f0...` after PR #483.

PR #483 changed Screening expansion authority, active Screening acceptance resolution, Evidence/downstream propagation, tests, and current authority documentation. It did **not** change the reader-facing TeX/Markdown contract, Publication Candidate schema, reader publication candidate structure, semantic/visual review schemas, Publication Preview approval contract, PDF authority structure, or canonical lifecycle value set.

Disposition:

- Publication Boundary Validator `7b9de210...`: `COMPATIBLE_AS_PINNED` for W34 sidecar pilot.
- Authority Auditor core invariants at `4f88e55c...`: `COMPATIBLE_ASSUMPTIONS`, but its current CLI is fixture-directory oriented. A thin read-only production adapter is required before actual W34 authority runs.

No full re-benchmark is required solely because of PR #483.

## 4. Immediate W34 production order

Do **not** run either sidecar tool against the current W34 artifacts.

First complete the normal Core flow:

```text
reviewed main@a9f121f0
-> sync reviewed Core into weekly/2026-W34-v2-work
-> revalidate only affected accepted boundary
-> repair W34 derived Screening authority to full accepted-root closure
-> formal Screening acceptance / stage advance
-> Evidence
-> Materiality / Completeness
-> Selection
-> Architecture
-> HUMAN ARCHITECTURE_REVIEW
```

The existing W34 105-event semantic decisions remain historical authority for those 105 events. The reviewed Core repair established that five accepted GitHub Releases roots require explicit coverage passthrough children. The corrected Screening basis is expected to be 110 derived records with 40/40 accepted-root accounting and five coverage-only `DROP` decisions, preserving 80 non-DROP Evidence tasks. This repair must be performed under reviewed post-#483 Core, not by weakening root closure.

## 5. Publication Boundary Validator runs

### Run A — reader-facing draft complete

Run after the principal reader-facing TeX/Markdown body is complete, before Publication Candidate formation.

Target the exact reader-facing source bytes in the W34 worktree. Do not construct a normalized or reserialized copy for scanning.

Interpretation:

- any `HARD_FAIL` finding / aggregate `FAIL` -> deterministic defect; Luna normally repairs and reruns; if the finding conflicts with Core/publication semantics, stop for Sol disposition.
- `REVIEW_REQUIRED` finding / aggregate `NEEDS_REVIEW` -> mandatory Sol semantic/editorial triage.
- aggregate `PASS` -> publication-boundary sidecar QA clear for that exact source revision.

A PASS is not Publication Preview approval.

### Run B — final source before Candidate binding

After deterministic QA and semantic/editorial repair, rerun against the exact final reader source that will be bound into Publication Candidate. A previous Run A PASS is not reusable after source mutation.

## 6. Authority Auditor runs

### Run A — exact Publication Candidate complete, before Human Publication Preview

Run only after exact final reader source, PDF, Publication Candidate, Quality bundle, Semantic Review, Visual Review, Production State, and relevant Gate records exist.

Audit must resolve and read the exact repository bytes bound by the Candidate. Do not copy/re-serialize the W34 artifacts into an auditor fixture and then treat the copy as authority.

Key second-opinion areas include Candidate digest, source/PDF exact bytes, PDF byte/page authority, semantic/visual review binding, stale review reuse, lifecycle consistency, pending-vs-approval, repository-local authority paths, and exact candidate/direct authority tuples.

### Run B — Human Publication Preview APPROVED, immediately before Freeze

After canonical Human approval is recorded and before Freeze, rerun against the current exact Candidate/PDF/approval/State bytes. Confirm exact Human approval binding, no post-approval Candidate/PDF drift, no stale approval, and lifecycle/next-action compatibility with Freeze.

## 7. Authority Auditor production adapter requirement

Before Run A, prepare a thin adapter in `eariver/survey-core-v2-authority-auditor` if practical.

Required behavior:

```text
exact japanese-generative-ai-survey checkout
+ issue_id
-> resolve canonical Production State
-> resolve exact current Publication Candidate
-> follow Candidate-bound source/PDF/quality/semantic/visual refs
-> resolve current Gate/review authority needed by implemented invariants
-> read exact bytes from upstream checkout
-> construct the auditor's in-memory Bundle without rewriting upstream files
-> emit deterministic JSON + Markdown report
```

Hard requirements:

- upstream survey repository is read-only input;
- no mutation, normalization, reserialization, or fixture-copy authority substitution;
- paths must be repository-local, regular, and fail closed if ambiguous/missing;
- adapter must preserve the auditor's existing invariant catalog and its FULLY_IMPLEMENTED/PARTIAL distinctions;
- PARTIAL invariants do not become blocking production authority;
- adapter should live in the auditor repository and produce a new reviewed tool SHA before W34 Authority Run A.

## 8. W34 report-only policy

No new GitHub Actions workflow, no eighth workflow, no new lifecycle state, no new Production State authority, and no new Human Gate are permitted for this pilot.

Operational disposition:

- Boundary Validator HARD_FAIL/FAIL: repair or explicit Sol disposition before Publication Preview.
- Boundary Validator REVIEW_REQUIRED/NEEDS_REVIEW: Sol semantic review required.
- Authority Auditor FAIL: Sol authority triage; if confirmed against Core authority, do not proceed until repaired.
- Authority Auditor PARTIAL/known limitation: report and triage; do not auto-block merely because the invariant is PARTIAL.
- Core-native validation and Human authority outrank sidecar output when scopes differ.

## 9. Mandatory run provenance

Every sidecar run must record at least:

- tool name;
- tool repository;
- exact tool SHA;
- target repository;
- target W34 commit SHA;
- issue_id;
- inspected artifact paths;
- execution time;
- exit status;
- PASS / FAIL / NEEDS_REVIEW (and finding severities where applicable);
- report path;
- Sol disposition if applicable.

Tool reports are independent QA evidence only and must not be inserted as a new canonical Production State authority.

Recommended W34 storage root:

`sources/2026-W34/execution/sidecar-qa/`

with one immutable subdirectory per tool/run/revision.

## 10. Post-W34 evaluation

After W34 Release, evaluate:

- false positives;
- false negatives discovered by Sol/Human;
- execution burden;
- repair burden;
- duplicate coverage with Core-native checks;
- useful findings unique to each sidecar tool.

Only after W34 evidence may W35+ consider adding report-only jobs/steps to existing CI workflows. Preserve the seven-workflow contract; do not create a new workflow merely for these tools.

## 11. Canonical W34 pilot flow

```text
PR #483 merged / reviewed main
-> W34 Core sync + affected-boundary revalidation
-> Screening
-> Evidence
-> Selection
-> Architecture
-> HUMAN ARCHITECTURE REVIEW
-> Drafting
-> Publication Boundary Validator Run A
-> editorial / semantic / deterministic QA
-> Publication Boundary Validator Run B
-> exact PDF + Candidate + Reviews
-> Authority Auditor Run A
-> HUMAN PUBLICATION PREVIEW
-> APPROVED
-> Authority Auditor Run B
-> Freeze
-> Release
-> post-W34 sidecar effectiveness review
```

This plan does not redesign W34 production. It adds independent read-only observation around the existing Core v2 publication boundary and authority boundary.