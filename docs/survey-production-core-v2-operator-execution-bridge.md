# Survey Production Core v2 — Operator Execution Bridge

Status: `FOLLOW-UP REVIEW REPAIR / TRUST BOOTSTRAP + DURABLE HUMAN REVIEW + CROSS-GATE REOPEN IMPLEMENTED / REAUDIT PENDING`

Established: 2026-08-23 JST  
Follow-up review repair: 2026-08-24 JST

Related authority:

- `docs/survey-production-core-v2-github-actions-policy.md`
- `docs/survey-production-core-v2-execution-record-policy.md`
- `docs/survey-production-core-v2-final-audit-rule.md`
- `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`

## 1. Purpose

The normal ChatGPT runtime can read and write exact GitHub repository files but cannot necessarily mount the exact work branch and invoke the canonical Core CLI. The operator bridge supplies that missing deterministic execution substrate. It is not an editorial agent and may not fabricate Profile/State/checkpoint/Human Gate authority by hand.

The bridge covers three deterministic classes:

1. generic Weekly / configured Retrospective / Thematic initialization;
2. one validated lifecycle-stage advancement over already-authored artifacts;
3. recording an already explicit Human `APPROVED` or `REQUEST_CHANGES` decision and applying its deterministic lifecycle consequence.

Human judgment remains external. ChatGPT owns research/editorial/visual work; the Human owns the two normal Human Gate decisions.

## 2. Trust bootstrap — default-branch authority first

A work branch must never be allowed to prove its own trusted Core state with a write-capable workflow loaded from that same untrusted branch.

The connector-safe execution topology is therefore intentionally split while keeping the repository at seven workflows:

```text
work-branch request-only commit
  -> survey-production-v2-operator-bridge.yml
       read-only / unprivileged signal only
       no checkout-based trust decision
       no Core execution
       no repository write
  -> workflow_run
       pipeline-contract-tests.yml loaded from default-branch authority
  -> operator-preflight (contents: read)
       checkout exact workflow_run.head_sha as untrusted data
       request-only commit proof
       branch/request identity proof
       reviewed_main ancestor proof
       Human reviewed-commit/request-parent proof where applicable
       protected-Core equality proof using protected-path configuration read
       from the named reviewed_main commit, not the untrusted branch config
  -> operator-execute (contents: write only after preflight PASS)
       checkout exact admitted request SHA
       fetch canonical work branch
       run canonical bridge helper
       enforce Profile-bound edition-local writes
       push deterministic output commit
```

A malicious or drifted work branch may suppress or alter its read-only signal and thereby cause denial of service, but it cannot obtain repository write authority or weaken the trusted preflight. The trust decision and write-capable execution job come from default-branch workflow authority.

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

## 4. Reviewed-main preflight

Trusted preflight must, before a write-capable job exists:

1. use the exact `workflow_run.head_sha` as the request commit;
2. require exactly one newly added operator request and no other file change in that commit;
3. require request `work_branch` == `workflow_run.head_branch`;
4. validate `reviewed_main_sha` as an existing current-main ancestor;
5. require request parent to descend from that reviewed baseline;
6. for initialization, require execution-record reviewed-main equality;
7. for Human Gate operations, require `reviewed_repository_commit_sha` == exact request parent;
8. derive the protected-path set from `reviewed_main_sha:config/survey-production-v2.json`, seeded at minimum with `.github/workflows`, `config`, `schemas`, and `scripts`;
9. require protected bytes at request parent to equal reviewed main exactly.

Only after those checks may the dependent executor receive `contents: write`.

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

The bridge/Human-Gate system must reject:

- work-branch write-capable self-verification;
- request commits that change anything besides one new request;
- reviewed-main or protected-Core drift;
- Human Gate request whose reviewed commit is not its exact request parent;
- nonexistent or dangling/unreachable review commits;
- review commits missing reviewed paths or containing different bytes;
- stale lifecycle or Human-review revisions;
- invalid Gate-specific regeneration boundaries;
- cross-gate reopen without an active canonical Architecture approval whose bytes match State provenance;
- arbitrary command or generic Human-decision surfaces;
- writes outside Profile-bound `source_root`;
- mutation of immutable request authority;
- recursive bot-trigger execution.

## 10. Direct local and connector-safe parity

Direct-local CLI remains preferred when available. Both modes call the same canonical Core/Human Gate implementation and must produce the same State/review semantics.

Differences are transport-only:

- direct local: canonical work-branch reachability + exact commit-tree byte proof;
- connector-safe: the same proof plus trusted default-branch request-parent/preflight execution and bridge receipts.

## 11. Acceptance consequence

The former fixed candidate `9932c8b7a14f1c3bdcc775df88056681b2841514` and its 7/7 audit were invalidated by follow-up review findings on trust bootstrap, reviewed-commit durability, and Publication upstream revision handling.

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
