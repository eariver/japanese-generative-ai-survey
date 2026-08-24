# Survey Production Core v2 — agent session bootstrap

Status: `FOLLOW-UP REVIEW HARDENED MAINTENANCE CANDIDATE / REAUDIT PENDING`  
Applies to: Weekly, Retrospective Period, standalone Thematic, and guided Special series work  
Primary operator: **ChatGPT**

## 1. Minimal user contract

A user may start or resume production with only a target and desired stopping Human Gate, for example:

```text
2026-W35をArchitecture Reviewまで編纂してください
Generative AI Foundationsの次巻をArchitecture Reviewまで進めてください
2025-H2をPublication Previewまで進めてください
```

That is sufficient. ChatGPT reconstructs mechanics from current reviewed repository authority and continues without routine confirmation.

Normal pauses are limited to:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`;
3. genuine Owner-level Exception Gate;
4. permitted Human-mediated Grok Drive task-file path handoff;
5. recorded blocking shared-Core defect.

Routine search refinement, Source Intake, Screening, Evidence, Selection, drafting, QA, layout repair, transient tool/CI retry, and normal `REQUEST_CHANGES` are not extra Human Gates.

## 2. Session-start authority

Read current reviewed `main`, then at minimum:

1. `AGENTS.md`;
2. Core authority/redesign authority;
3. this bootstrap;
4. issue-prevention checklist;
5. X/Grok intake policy;
6. execution-record policy;
7. applicable Profile/period/thematic/series guide;
8. current Profile/State/review index/execution index if resuming.

Repository state outranks chat history.

## 3. Production/Core boundary

Production repairs the edition, not shared Core. Shared roots are read-only during edition production:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

A shared-Core defect is recorded under the edition execution tree and repaired separately. A formal production-validation run that hits a shared-Core defect is failed evidence and must be rerun cleanly after reviewed Core repair.

## 4. Target resolution

### Weekly

Use configured Weekly cutoff logic and generic `WEEKLY + WEEKLY_MAGAZINE`. Weekly X/Grok is required.

### Retrospective Period

Configured monthly/half-year/annual Specials use the single pre-existing `scripts/survey_period_v2.py` path. Custom bounded periods remain generic. Do not create cadence-specific engines.

### Thematic

Resolve topic scope from canonical planning authority. Materializing a machine-readable scope is internal work, not a Human Gate.

### Generative AI Foundations

Use the living series memo as outer authority and materialize each volume as Thematic/LONGFORM work. Do not create a parallel machine series engine.

## 5. Deterministic execution mode

Use exact local CLI when available.

When connector-only ChatGPT cannot execute local Core, use the operator bridge through the persistent default-branch transport queue:

```text
ChatGPT adds one immutable request-only commit
-> push it as the exact current Profile-bound work-branch head
-> comment on GitHub Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> default-branch issue_comment workflow performs read-only trusted preflight
-> write-capable deterministic executor exists only after preflight PASS
```

The work branch supplies request data only; it does not supply the trust-deciding workflow. `pipeline-contract-tests.yml` remains CI-only. Issue #448 is transport, not a Human Gate.

Before posting the trigger, the request-only commit must be the current canonical work-branch head. If the branch moves during admission/execution, the workflow fails closed rather than overwriting newer work.

The bridge request surface remains exactly:

- `INITIALIZE_WEEKLY`
- `INITIALIZE_RETROSPECTIVE`
- `INITIALIZE_THEMATIC`
- `ADVANCE_STAGE`
- `RECORD_ARCHITECTURE_APPROVAL`
- `REQUEST_ARCHITECTURE_REVISION`
- `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- `REQUEST_PUBLICATION_PREVIEW_REVISION`

Human Gate operations only record already explicit Human input.

## 6. Human review surface preparation

Before presenting either normal Human Gate:

1. finish all current Gate inputs;
2. commit exact current Production State + configured Gate inputs;
3. **push/retain that commit on the Profile-bound canonical work branch**;
4. record that exact commit as `reviewed_repository_commit_sha`;
5. present exactly those committed bytes to the Human.

Canonical Human Gate Core rejects a decision unless the named commit:

- exists;
- is reachable from canonical work branch;
- contains exact current reviewed State/Gate-input bytes;
- for Publication Preview, contains exact Candidate-bound PDF.

Connector-safe execution additionally binds the same reviewed commit to the immutable request-only commit parent. Do not substitute the later request/event commit.

## 7. Research → Architecture loop

Normal autonomous progression:

```text
Profile/State
-> Source Intake + research expansion
-> Screening
-> Evidence verification
-> materiality/completeness closure
-> Selection
-> Architecture
-> exact stage validation/checkpoint
-> ARCHITECTURE_REVIEW
```

## 8. Architecture Review

At pending Architecture Review, present committed Architecture + review summary + review-attention authority.

### APPROVED

Record Human approval against the durable reviewed commit. Core writes:

- current canonical Architecture approval;
- immutable `gates/reviews/approvals/architecture-rN.json` snapshot;
- `gates/reviews/architecture-rN.json` review record;
- review-index update.

Then continue to drafting.

### REQUEST_CHANGES

Require explicit requested changes and allowed pre-Architecture regeneration boundary. Core records rN, invalidates only affected downstream authority, and returns to the selected boundary. ChatGPT repairs and returns to Architecture Review rN+1.

## 9. Reader-facing authorship and QA

After active Architecture approval, ChatGPT authors canonical reader-facing source. Internal Evidence/Selection/Architecture/Draft artifacts are not legal fallback publication prose.

For one exact source/PDF revision complete:

1. deterministic QA;
2. ChatGPT semantic/editorial QA;
3. ChatGPT visual QA of exact rendered PDF.

Only then assemble Publication Candidate.

## 10. Publication Preview

Commit and push/retain exact current State, Candidate, and Candidate-bound PDF before presenting the Gate.

### APPROVED

Record approval against the durable reviewed commit, including immutable `publication-rN` approval snapshot, then continue to Freeze.

### REQUEST_CHANGES — publication-local

If Human selects `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, or `VALIDATED_DRAFT`, preserve valid active Architecture approval, invalidate affected publication authority, repair/rebuild/review, and return to Publication Preview rN+1.

### REQUEST_CHANGES — upstream / cross-gate

If Publication review reveals an Evidence/Selection/Architecture defect, the Human may select an allowed boundary before `ARCHITECTURE_ESTABLISHED`.

Core then:

1. records Publication `REQUEST_CHANGES` rN against exact reviewed Candidate/PDF;
2. preserves old Architecture rN review + immutable approval snapshot;
3. verifies current active canonical Architecture approval matches State provenance;
4. supersedes/removes that active canonical Architecture approval;
5. clears active Architecture provenance and marks Architecture Review pending;
6. invalidates downstream checkpoints from selected boundary;
7. resumes research/Selection/Architecture work;
8. stops at Architecture Review rN+1 before new drafting/publication can continue.

This is normal dependency-aware revision, not an Exception Gate.

## 11. Freeze / Release

After Publication approval:

```text
approved exact Candidate/PDF
-> Freeze Record / Release Manifest
-> FROZEN
-> reviewed merge to main
-> dedicated exact-byte Release workflow
-> merge/release verification
-> RELEASED
```

Do not add a second post-approval semantic/visual Human Gate.

## 12. X/Grok handoff

Weekly requires X/Grok. Retrospective/Thematic choose REQUIRED/NOT_REQUIRED with rationale. Foundations uses its dedicated Drive category when material.

Prepare one self-contained Drive task file and give the Human only the exact task-file path/reference. Returned bytes are imported exactly and dispositioned before continuing. Do not search for a Grok connector merely because intake is required.

## 13. Execution continuity

Maintain `{source_root}/execution/index.md`, concise session records, review summaries, defect records, request/receipt pointers when bridge transport is used, and current Human-review rN authority.

Keep distinct:

- reviewed main baseline;
- Human-reviewed edition commit;
- request-only commit;
- Issue #448 trigger comment;
- trusted default-branch operator workflow run;
- bot output commit.

## 14. Core candidate audit rule

Core maintenance follows:

```text
finish all candidate changes
-> exact-head diagnostic CI
-> synchronize authority
-> pre-freeze cross-check
-> freeze one SHA
-> fresh seven-point audit from Point 1
-> no tree changes during audit
-> only 7/7 PASS -> Human full-candidate review
```

Point 7 explicitly includes default-branch Issue #448 trust bootstrap, durable work-branch review commits, immutable approval history, and Publication→Architecture cross-gate reopen.

Any mutation after freeze invalidates the whole audit.
