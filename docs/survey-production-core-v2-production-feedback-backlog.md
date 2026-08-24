# Survey Production Core v2 — Post-Merge Production Feedback Backlog

Status: `REDESIGN INTEGRATED / PFB-014 FOLLOW-UP REVIEW REPAIRS IMPLEMENTED / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Initial review closed: 2026-08-23 JST  
Last updated: 2026-08-24 JST

Current maintenance branch: `maintenance/core-v2-operator-execution-bridge`

## Current authority

The initial W33/SP001 feedback drove the integrated Core v2 redesign. Clean post-merge revalidation then exposed the connector-only deterministic execution gap. Later audits and follow-up review expanded PFB-014 from simple bridge bootstrap into the complete safe operator/Human-Gate integration boundary.

Current authority:

- cross-edition worklog: `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`
- operator bridge: `docs/survey-production-core-v2-operator-execution-bridge.md`
- Actions policy: `docs/survey-production-core-v2-github-actions-policy.md`
- final audit rule: `docs/survey-production-core-v2-final-audit-rule.md`
- connector transport queue: GitHub Issue `#448`

PFB-001 through PFB-013 remain applicable. PFB-014 is the open maintenance finding until fixed-head acceptance and post-integration real-production validation complete.

## PFB-001 — one self-contained Grok task file in Google Drive

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

Use one run-specific Markdown task file. Repository provenance hash-binds exact task/result bytes.

## PFB-002 — Human passes exact Drive task-file path; do not search for a Grok connector

Status: `IMPLEMENTED / REAL W33 OPERATION CONFIRMED`

```text
ChatGPT prepares one self-contained task file
-> Human passes exact Drive path/reference to Grok
-> Grok reads/writes instructed result
-> ChatGPT imports/dispositions result and resumes
```

Absence of a Grok connector is not an Exception Gate.

## PFB-003 — concluding synthesis in every Weekly and Special

Status: `IMPLEMENTED`

Every reader-facing Weekly/Special requires substantive `総括` or equivalent. ChatGPT judges quality; deterministic checks only protect crisp structure.

## PFB-004 — Weekly always has explicit community movement informed by Grok/X

Status: `IMPLEMENTED / CLEAN W33 EDITORIAL VALUE CONFIRMED`

Every Weekly requires reader-facing `コミュニティの動き`; Grok/X remains Discovery/community-signal rather than final technical Evidence authority.

## PFB-005 — Production sessions repair editions, not shared Core

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

> **A Production session repairs the edition. It does not repair shared Core v2.**

W33/SP001 remain paused while PFB-014 is repaired in Core maintenance.

## PFB-006 — reduce Actions from production author to narrow deterministic infrastructure

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT / PFB-014 TRUST ROOT UNDER FINAL VALIDATION`

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, Human-decision, or publication-authoring agent.**

The operator bridge is admissible only as a constrained deterministic execution substrate because the connector runtime lacks an exact checked-out CLI environment. It may record an already explicit Human decision but may not choose one.

The intended Actions surface remains exactly seven workflows.

## PFB-007 — retain failed W33/SP001 trials as non-validating evidence

Status: `RESOLVED / HISTORICAL FAILED EVIDENCE PRESERVED`

Pre-redesign failures and post-merge blocked attempts remain non-PASS evidence.

## PFB-008 — structural reader-facing Publication Boundary

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Internal editorial/provenance state is not legal fallback reader prose. Missing reader content fails closed to ChatGPT authoring.

## PFB-009 — Architecture fidelity means reader-facing content fulfillment

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

```text
requirement
-> accepted Evidence/Observation
-> actual reader-facing location
-> ChatGPT fulfillment judgment
```

## PFB-010 — separate deterministic QA from semantic/editorial and visual QA

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT`

Candidate readiness requires deterministic QA + ChatGPT semantic/editorial QA + exact-PDF visual QA. The bridge owns none of these judgments.

## PFB-011 — atomic publication revision/candidate authority

Status: `IMPLEMENTED / REQUIRED CORE INVARIANT / DEPENDENCY-AWARE HUMAN REVISION ADDED`

Reader Manuscript, exact source/PDF, deterministic QA, semantic/editorial review and visual review bind atomically. Source/PDF revision invalidates downstream authority. Publication Preview revision now supports both publication-local repair and an explicit upstream Human-selected boundary that reopens Architecture when required.

## PFB-012 — standardized edition-local execution records

Status: `IMPLEMENTED / PFB-014 EXTENDS EXECUTION + HUMAN-REVIEW PROVENANCE`

Canonical execution tree may add `requests/` and `bridge-runs/`. Human-readable review records point to exact machine Human-review authority under `{source_root}/gates/reviews/`; these are provenance, not a second State machine.

## PFB-013 — real cold-start profile trials required after Core repair

Status: `PARTIALLY EXERCISED / NOT PASSED`

Required post-integration acceptance remains:

- clean Weekly;
- clean Thematic/LONGFORM with SP001 regression;
- representative configured `RETROSPECTIVE_PERIOD`;
- Foundations-guided Thematic/Longform;
- structural monthly/half-year/annual compatibility through one generic Period Profile.

## PFB-014 — deterministic Core execution fallback for connector-only runtimes

Status: `IMPLEMENTATION CANDIDATE / TRUST ROOT + DURABLE REVIEW + CROSS-GATE REOPEN REPAIRED / SEVEN-POINT REAUDIT PENDING`

### Accumulated findings

The maintenance accumulated the following defects and follow-up findings:

- **HG-001:** connector-only operation could reach a Human Gate but could not canonically record explicit Human approval.
- **HG-002:** routine Human `REQUEST_CHANGES` lacked canonical selective invalidation/rN continuation.
- **RVF-023:** connector transport originally conflated the Human-reviewed parent commit with the later request/event commit.
- **HG-003:** direct-local Human Gate recording did not prove that the named reviewed commit existed and exact-bound reviewed bytes.
- **Follow-up F1 — trust bootstrap:** a write-capable verifier must not be supplied by the untrusted work branch it is admitting.
- **Follow-up F2 — durability:** a dangling synthetic reviewed commit is not durable historical authority even when its bytes currently exist locally.
- **Follow-up F3 — upstream Publication correction:** Publication Preview feedback can legitimately require Evidence/Selection/Architecture repair and needs one canonical non-Exception path.

The former candidate `9932c8b7a14f1c3bdcc775df88056681b2841514` and its 7/7 audit are invalidated by the three follow-up findings. No earlier PASS result is reusable.

### Retrospective diagnosis

Core already contains canonical generic Retrospective support:

- `scripts/survey_period_v2.py`
- `tests/test_survey_period_v2.py`

The bridge exposes that existing initializer only; it does not create a second Retrospective builder, scope schema, or monthly/half-year/annual engine.

### Current connector-safe execution contract

```text
ChatGPT authors edition work
-> commit/push exact canonical work branch
-> when deterministic connector execution is needed, add exactly one immutable request-only commit
-> that request commit is the exact current canonical work-branch head
-> ChatGPT comments on persistent transport Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> default-branch issue_comment workflow treats supplied SHA/branch as untrusted data
-> read-only preflight proves:
     exact command / authorized association
     exact current work-branch head
     request-only commit
     reviewed-main ancestry
     protected-Core equality using reviewed-main config
     Human reviewed-commit == request parent where applicable
-> dependent job receives contents: write only after PASS
-> branch head is rechecked
-> canonical bridge executes only allowlisted deterministic mechanics
-> edition-local write boundary is enforced
-> output push is lease-bound to admitted request head
-> ChatGPT resumes from canonical State
```

There is no work-branch workflow trust bootstrap and no `workflow_run` trust hop. An intermediate signal/`workflow_run` design was considered during repair and rejected because the work-branch signal workflow definition itself remained branch-supplied.

Issue #448 is transport only, not a third Human Gate or editorial control surface.

### Current direct-local / Human-review contract

Before either Human Gate is presented:

```text
commit exact Production State + Gate inputs
-> push/retain that commit on Profile work_branch
-> Human reviews that exact durable commit
```

Canonical `survey_human_gate_v2` then requires the reviewed commit to:

- be a real Git commit;
- be reachable from the canonical Profile work branch;
- exact-bind current reviewed State and Gate input bytes;
- for Publication Preview, exact-bind the Candidate-bound PDF.

Connector-safe Human Gate execution additionally requires that reviewed commit to equal the immutable request-only commit parent.

Every approval writes an immutable historical snapshot under `gates/reviews/approvals/*-rN.json`, separate from the active canonical approval path.

### Publication Preview dependency-aware correction

If the Human chooses a publication-local boundary (`ARCHITECTURE_ESTABLISHED` or later), active Architecture approval is preserved and only downstream publication authority is regenerated.

If the Human chooses a boundary before `ARCHITECTURE_ESTABLISHED` because Publication review found an upstream defect, Core:

1. records Publication `REQUEST_CHANGES` rN against exact Candidate/PDF review bytes;
2. validates active Architecture approval provenance;
3. preserves the prior Architecture review record and immutable rN approval snapshot;
4. removes the active canonical Architecture approval;
5. marks Architecture Review pending again;
6. invalidates dependent checkpoints from the Human-selected boundary;
7. requires a new Architecture rN+1 before drafting/publication continues;
8. eventually returns to Publication Preview rN+1.

Core never chooses the repair boundary. Cross-gate reopen is normal Human revision, not an Owner Exception Gate and not a third Human Gate.

### Operator request surface

Exactly eight operations remain allowed:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

Release remains outside the bridge.

### Regression evidence required before freeze

The candidate must cover:

- generic Thematic init → Discovery bridge E2E;
- configured Retrospective reuse of existing Period builder;
- no arbitrary execution/deterministic-review impersonation;
- static default-branch `issue_comment` trust-root contract;
- exact work-branch-current-head requirement and branch-movement/lease protection;
- Architecture r1 `REQUEST_CHANGES` → r2 → approval, direct and bridge-backed;
- Publication-local r1 revision → r2 approval;
- Publication r1 upstream revision → Architecture r2 → Publication r2 approval, direct and bridge-backed;
- nonexistent/dangling/missing-path/mismatched reviewed commit rejection;
- immutable approval snapshot preservation;
- stale review revision/changed reviewed bytes/invalid boundary failure;
- connector Human reviewed-parent mismatch failure;
- exactly seven workflow filenames.

These regressions do not replace post-integration real branch validation of Issue #448 transport.

### Acceptance criteria

PFB-014 cannot close until all conditions below hold:

1. no arbitrary executable surface from request data;
2. exact request path/id/branch/source-root and eight-kind schema;
3. every operation binds reviewed main; initialization record agrees;
4. connector operator trust root is default-branch `issue_comment` authority, not work-branch workflow code;
5. only authorized exact Issue #448 trigger syntax is actionable;
6. request commit is exactly one new request, changes nothing else, and equals current canonical work-branch head;
7. protected Core/contract bytes match reviewed main before write-capable execution;
8. branch movement between admission and output push fails closed;
9. generated writes stay under Profile-bound source root and request bytes remain immutable;
10. `ADVANCE_STAGE` requires exact lifecycle State and Core owns deterministic stage result;
11. Human Gate decisions remain Human-supplied only;
12. Human review commit is real, reachable from canonical work branch, and exact-binds current reviewed bytes;
13. connector Human Gate request additionally binds reviewed commit == request-only parent;
14. direct-local remains preferred and has equivalent Human-review provenance strength;
15. prior approval revisions remain reconstructable through immutable approval snapshots/review records;
16. Publication upstream correction can reopen Architecture and return through Architecture rN+1 / Publication rN+1;
17. Retrospective reuses existing `survey_period_v2` only;
18. positive/negative direct and bridge regressions pass;
19. exact-head Core CI + Pipeline contract tests PASS on final synchronized candidate;
20. complete seven-point fixed-head audit passes from Point 1 without tree mutation;
21. after unchanged reviewed integration, clean Weekly/SP001/Retrospective/Foundations production matrix passes without in-run shared-Core repair.

## Current next step

Do not resume W33/SP001 acceptance before PFB-014 is reviewed and integrated.

```text
finish follow-up test/authority/worklog synchronization
-> obtain green diagnostic CI
-> pre-freeze cross-check current PR
-> require exact-head Core CI + Pipeline contract PASS
-> freeze one exact candidate SHA
-> fresh seven-point audit from Point 1
-> only 7/7 PASS: Human full-candidate review
-> unchanged integration
-> clean Weekly / Thematic-SP001 / Retrospective / Foundations validation matrix
```

Any candidate-tree change after freeze invalidates all seven verdicts.
