# Survey Production Core v2 — Operator Execution Bridge

Status: `FOLLOW-UP REVIEW REPAIR / DEFAULT-BRANCH TRUST ROOT + ISOLATED RUNTIME + DURABLE HUMAN REVIEW + CROSS-GATE REOPEN IMPLEMENTED / REAUDIT PENDING`

Established: 2026-08-23 JST  
Follow-up review repair: 2026-08-24 JST

Related authority:

- `docs/survey-production-core-v2-github-actions-policy.md`
- `docs/survey-production-core-v2-execution-record-policy.md`
- `docs/survey-production-core-v2-final-audit-rule.md`
- `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`
- `docs/checkpoints/survey-production-core-v2-rvf026-runtime-import-boundary-2026-08-24.md`
- operator transport queue: GitHub Issue `#448`

## 1. Purpose

The normal ChatGPT runtime can read and write exact GitHub repository files but cannot necessarily mount the exact work branch and invoke the canonical Core CLI. The operator bridge supplies that missing deterministic execution substrate. It is not an editorial agent and may not fabricate Profile/State/checkpoint/Human Gate authority by hand.

The bridge covers three deterministic classes:

1. generic Weekly / configured Retrospective / Thematic initialization;
2. one validated lifecycle-stage advancement over already-authored artifacts;
3. recording an already explicit Human `APPROVED` or `REQUEST_CHANGES` decision and applying its deterministic lifecycle consequence.

Human judgment remains external. ChatGPT owns research/editorial/visual work; the Human owns the two normal Human Gate decisions.

## 2. Trust bootstrap — default-branch authority only

A work branch must never be allowed to prove its own trusted Core state with a write-capable workflow loaded from that same untrusted branch.

The connector-safe execution topology therefore uses the existing operator workflow only from GitHub's default-branch `issue_comment` event authority. There is no work-branch signal workflow and no `workflow_run` trust hop.

```text
ChatGPT commits one immutable request-only commit
  -> request commit is pushed as the exact current Profile-bound work-branch head
  -> ChatGPT posts on persistent transport Issue #448:
       /survey-core-execute <exact-request-commit-sha>
  -> survey-production-v2-operator-bridge.yml
       loaded from default-branch issue_comment authority
  -> operator-preflight (contents: read)
       parse exact command; supplied SHA is untrusted data
       checkout that exact request SHA
       parse untrusted JSON only with isolated Python startup
       prove it is the exact current canonical work-branch head
       prove request-only commit / branch / reviewed-main identity
       prove Human reviewed-commit == request parent where applicable
       derive protected paths from reviewed-main config using isolated runtime
       prove protected Core/contract bytes equal reviewed main
  -> operator-execute (contents: write only after preflight PASS)
       recheck the work branch and reviewed-main authority
       materialize reviewed-main scripts/ into runner-temporary trusted runtime
       execute the canonical bridge package from that trusted runtime
       pass admitted checkout only as explicit repository data/write target
       enforce Profile-bound edition-local writes
       push with force-with-lease against the admitted request head
```

GitHub's `issue_comment` event requires the workflow file to exist on the default branch, so the untrusted work branch is data rather than workflow authority. A work branch can neither replace the preflight logic nor grant itself repository write permission before admission.

The workflow's Python import boundary is part of the trust root. While the checkout is untrusted, Python helpers must run with isolated/safe import startup and must not import repository-local modules. After admission, the write-capable job must execute Core Python from a runtime materialized from the named reviewed-main commit, not from the admitted checkout's Python import root. The admitted checkout remains the explicit repository/data/write target.

Issue `#448` is transport only. It is not a Human Gate, does not contain editorial authority, and does not create a generic comment-driven command surface. Only the exact command form `/survey-core-execute <lowercase-40-hex-request-commit>` is actionable, and the immutable repository request remains the operation authority.

## 3. Request surface

The allowlist remains exactly eight operations:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

There is no arbitrary command/module/script/workflow surface and no generic `EXECUTE_HUMAN_DECISION` operation.

Retrospective initialization reuses the pre-existing `survey_period_v2.resolve_configured_period()` + `period_profile()` path. It does not introduce a second cadence engine.

## 4. Trusted request preflight

Before a write-capable job exists, the default-branch workflow must:

1. accept only Issue `#448` comments from an authorized repository association and reject bot comments;
2. require the exact trigger syntax `/survey-core-execute <lowercase-40-hex-request-commit>`;
3. checkout the supplied SHA only as untrusted request data;
4. require exactly one newly added operator request and no other file change in that commit;
5. parse all untrusted request fields with isolated Python startup that excludes repository-local import paths;
6. validate the request `work_branch` and fetch that exact branch;
7. require the supplied request SHA to equal the current canonical work-branch head exactly;
8. validate `reviewed_main_sha` as an existing current-main ancestor;
9. require request parent to descend from that reviewed baseline;
10. for initialization, require execution-record reviewed-main equality;
11. for Human Gate operations, require `reviewed_repository_commit_sha` == exact request parent;
12. derive the protected-path set from `reviewed_main_sha:config/survey-production-v2.json`, seeded at minimum with `.github/workflows`, `config`, `schemas`, and `scripts`, using an isolated non-repository import environment;
13. require protected bytes at request parent to equal reviewed main exactly.

Only after those checks may the dependent executor receive `contents: write`.

Immediately before execution it re-fetches the canonical work branch and current main, requires the head to remain the admitted request SHA, and requires the named reviewed-main commit to remain on current main history. It then materializes `scripts/` from that reviewed-main commit into runner-temporary storage and executes `scripts.survey_core_execution_bridge_v2` from that trusted runtime. The work checkout is supplied explicitly through `--repo-root` and request-path arguments; it is not a Python import root. Output push uses `force-with-lease` against the admitted SHA, so a concurrent branch movement fails rather than overwriting later work.

JSON-only helpers in the write-capable job also use isolated Python startup, so unrelated unprotected checkout files cannot gain execution through import shadowing after admission.

## 5. Human review surface durability

Exact bytes alone are not sufficient provenance if the named review commit is a dangling Git object that can disappear after garbage collection or a fresh clone.

Before presenting either Human Gate, ChatGPT must:

1. commit the exact current Production State and configured Gate inputs;
2. push/retain that commit on the Profile-bound canonical work branch;
3. present that retained commit as the Human review surface.

Canonical `survey_human_gate_v2` requires `reviewed_repository_commit_sha` to:

- name a real Git commit;
- be reachable from the canonical Profile `work_branch` (`origin/<work_branch>` when an origin exists, otherwise the local branch ref);
- contain the exact current reviewed Production State and every configured Gate input as regular-file bytes;
- for Publication Preview, also contain the exact Candidate-bound PDF bytes.

Connector-safe execution adds one more invariant: the retained Human-reviewed commit must be exactly the immutable request-only commit parent. The later request/event commit remains separate execution provenance.

## 6. Immutable Human-review history

Current canonical approval files remain the active State-machine authority:

```text
{source_root}/gates/architecture-approval.json
{source_root}/gates/publication-preview-approval.json
```

Every successful approval also creates an immutable per-revision snapshot:

```text
{source_root}/gates/reviews/approvals/architecture-rN.json
{source_root}/gates/reviews/approvals/publication-rN.json
```

The corresponding machine review record points to that immutable snapshot. Therefore an old active approval may later be superseded while the historical rN decision remains reconstructable and hash-verifiable.

Machine review history remains:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

Review revisions are contiguous per Gate. Historical APPROVED decisions are allowed to be followed by a later Architecture revision only when a recorded Publication Preview `REQUEST_CHANGES` explicitly reopens Architecture by selecting an upstream regeneration boundary.

## 7. Architecture Review revision

Architecture `REQUEST_CHANGES` may select an allowed boundary from initialization through `SELECTION_COMPLETE`. Core:

- records the exact Human review revision;
- resets only downstream checkpoint/gate authority;
- removes superseded canonical Stage Checkpoints;
- returns State to the selected boundary;
- leaves the Human decision itself and repair content to Human/ChatGPT.

The next Architecture review is rN+1. Stale earlier revision requests fail closed.

## 8. Publication Preview revision — local versus cross-gate

Publication Preview feedback may reveal defects at different dependency depths. The Human chooses one allowed regeneration boundary; Core never chooses it.

### Publication-local revision

For boundaries at or after `ARCHITECTURE_ESTABLISHED`:

- approved Architecture remains active;
- Publication Preview returns to the selected drafting/validation boundary;
- affected validation/candidate authority is invalidated;
- ChatGPT repairs/rebuilds/reviews and returns to Publication Preview rN+1.

### Cross-gate upstream revision

For boundaries before `ARCHITECTURE_ESTABLISHED` — e.g. Selection, Evidence, Screening, or Discovery — the Publication feedback invalidates the dependency basis of the approved Architecture.

Core therefore:

1. records Publication `REQUEST_CHANGES` rN against exact reviewed Candidate/PDF bytes;
2. preserves the prior Architecture APPROVED review record and immutable approval snapshot;
3. removes/supersedes the active canonical Architecture approval only after verifying it matches current State provenance;
4. clears active Architecture approval provenance and marks Architecture Review pending again;
5. invalidates downstream checkpoints from the selected boundary;
6. returns State to that boundary;
7. requires normal progression back through a new Architecture Review rN+1 before drafting/publication may continue.

This is a normal Human revision path, not an Owner Exception Gate.

## 9. Fail-closed invariants

The bridge/Human-Gate system must reject or structurally prevent:

- any work-branch workflow as trust bootstrap for operator execution;
- unauthorized or malformed Issue `#448` trigger comments;
- request SHA that is not the exact current canonical work-branch head;
- request commits that change anything besides one new request;
- repository-local Python import/code execution while the request checkout is still untrusted;
- reviewed-main or protected-Core drift;
- Human Gate request whose reviewed commit is not its exact request parent;
- nonexistent or dangling/unreachable review commits;
- review commits missing reviewed paths or containing different bytes;
- branch movement between admission and execution/push;
- write-capable Core execution that uses the admitted worktree as its Python import root rather than a reviewed-main runtime;
- stale lifecycle or Human-review revisions;
- invalid Gate-specific regeneration boundaries;
- cross-gate reopen without an active canonical Architecture approval whose bytes match State provenance;
- arbitrary command or generic Human-decision surfaces;
- writes outside Profile-bound `source_root`;
- mutation of immutable request authority.

## 10. Direct local and connector-safe parity

Direct-local CLI remains preferred when available. Both modes call the same canonical Core/Human Gate implementation and must produce the same State/review semantics.

Differences are transport-only:

- direct local: canonical work-branch reachability + exact commit-tree byte proof;
- connector-safe: the same proof plus default-branch Issue `#448` request admission, isolated pre-admission parsing, request-parent/protected-Core checks, reviewed-main runtime materialization, branch-head/race checks, and bridge receipts.

The connector workflow must regression-test the actual package-module subprocess startup form used in Actions, not only in-process calls to `execute_request()`.

## 11. Acceptance consequence

The former fixed candidates `9932c8b7a14f1c3bdcc775df88056681b2841514` and `109579e0f9b2988b62074165b28f144ac3b1ad55`, including their historical 7/7 audit records, are invalidated by later follow-up review findings. The latter was specifically invalidated by RVF-026, which extended the trust boundary to Python startup/import behavior.

An intermediate read-only work-branch signal + default-branch `workflow_run` design was also discarded during repair because the work-branch signal workflow definition itself remained work-branch supplied. It is historical diagnostic design only.

No earlier PASS may be carried forward. The next candidate requires:

```text
finish implementation/test/doc/worklog synchronization
-> exact-head CI
-> pre-freeze cross-check
-> freeze one SHA
-> fresh seven-point audit from Point 1
-> Human full-candidate review
-> unchanged integration
-> clean real-production validation matrix
```
