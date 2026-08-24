# Survey Production Core v2 — Audited Redesign Authority Overlay

Status: `INTEGRATED REDESIGN + OPERATOR/HUMAN-GATE FOLLOW-UP REPAIR CANDIDATE / SEVEN-POINT REAUDIT PENDING`  
Established: 2026-08-23 JST  
Updated: 2026-08-24 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`

## 1. Purpose and precedence

This overlay governs the redesign after W33/SP001 production evidence and the later operator/Human-Gate maintenance. It does not erase historical Core v2 design documents; where they conflict with this overlay or later production evidence, this overlay wins.

Current precedence:

```text
1. repository reality + production/review evidence
2. this redesign authority overlay
3. docs/survey-production-core-v2-operator-execution-bridge.md
4. docs/survey-production-core-v2-github-actions-policy.md
5. docs/survey-production-core-v2-execution-record-policy.md
6. docs/survey-production-core-v2-final-audit-rule.md
7. current Profile/edition/series authority
8. older redesign/audit documents where not superseded
```

## 2. Fundamental operator model

**ChatGPT remains the primary research/editorial/publication operator. The Human remains the authority for the two normal Human Gate decisions.**

```text
Profile + edition/series authority + Production State
-> ChatGPT research/editorial work
-> narrow deterministic validation/provenance helpers
-> ARCHITECTURE_REVIEW
   -> APPROVED: record -> drafting
   -> REQUEST_CHANGES: record/invalidate -> ChatGPT repair -> Architecture rN+1
-> ChatGPT reader-facing authorship + semantic/editorial QA + exact-PDF visual QA
-> atomic Publication Candidate
-> PUBLICATION_PREVIEW
   -> APPROVED: record -> Freeze
   -> REQUEST_CHANGES publication-local: invalidate downstream -> repair -> Publication rN+1
   -> REQUEST_CHANGES upstream: reopen dependency boundary -> Architecture rN+1 -> redraft -> Publication rN+1
-> exact-byte Freeze / Release integrity
```

Deterministic execution may use direct exact local CLI or the connector-safe operator bridge. The bridge is transport/execution for the same canonical mechanics, never a parallel editorial state machine.

## 3. Core / Profile / edition layering

### Shared Core

Shared Core owns only cross-profile invariants:

- lifecycle and exactly two normal Human Gates;
- Human decision recording, contiguous review revisions, dependency-aware invalidation and cross-gate reopening;
- durable exact reviewed-commit provenance;
- Evidence/provenance boundaries;
- internal-vs-reader-facing Publication Boundary;
- deterministic vs semantic/editorial vs visual QA separation;
- exact Candidate/Preview/Freeze identity;
- execution records;
- Production-vs-Core-maintenance separation;
- Grok/X transport/evidence-role invariants;
- optional safe deterministic operator execution.

### Research Profiles

- `WEEKLY`
- `RETROSPECTIVE_PERIOD`
- `THEMATIC`

### Publication Profiles

- `WEEKLY_MAGAZINE`
- `LONGFORM_SPECIAL`

### Edition / series authority

Monthly/half-year/annual guidance, standalone Thematic planning, and Generative AI Foundations remain editorial authorities layered over generic Core/Profile mechanics. They do not justify cadence/topic-specific engines.

## 4. Retrospective invariant

Configured Retrospective cold start uses the **existing** generic:

```text
survey_period_v2.resolve_configured_period(...)
-> survey_period_v2.period_profile(...)
```

Monthly, half-year, annual and custom bounded periods remain one generic `RETROSPECTIVE_PERIOD + LONGFORM_SPECIAL` Profile path. Do not introduce a second Retrospective adapter/schema/engine in the operator bridge.

## 5. Publication Boundary and fidelity

Internal Screening/Selection/Evidence/materiality/Architecture/Human-review state is not legal fallback reader prose. ChatGPT explicitly authors canonical reader-facing source. Missing reader content fails closed to authoring.

Architecture fidelity means approved `must_cover` obligations and materially selected story/lineage questions are actually explained to the reader. Deterministic validation may prove structural mapping; substantive fulfillment remains ChatGPT judgment.

Candidate readiness requires three distinct layers:

1. deterministic Quality Bundle for crisp invariants;
2. ChatGPT semantic/editorial review;
3. ChatGPT exact-PDF visual review.

Machine PASS alone is never publication-quality PASS.

## 6. GitHub Actions / trust-root invariant

GitHub Actions is a deterministic executor/verifier, not a reasoning, editorial, publication-authoring or Human-decision agent.

The operator bridge is admitted only because the connector runtime lacks a guaranteed exact local checkout/CLI. Its request surface remains eight explicit operations: three initializers, `ADVANCE_STAGE`, and four Human Gate approval/revision recorders. Arbitrary command/module/script/workflow and generic Human-decision surfaces are prohibited.

**The untrusted work branch must never supply the workflow that decides whether that branch is trusted.** Connector-safe execution therefore starts only from the default-branch `issue_comment` authority of `.github/workflows/survey-production-v2-operator-bridge.yml`:

```text
request-only commit pushed as exact current Profile work-branch head
-> ChatGPT comments on operator queue Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> default-branch workflow parses supplied SHA as untrusted data
-> read-only preflight proves exact work-head/request-only/reviewed-main/protected-Core invariants
-> only dependent post-PASS executor receives contents: write
-> branch head rechecked
-> exact Core operation executed
-> Profile-bound outputs pushed with force-with-lease
```

There is no work-branch signal workflow and no `workflow_run` trust hop. `pipeline-contract-tests.yml` remains CI-only.

Protected-path configuration comes from the named reviewed-main commit, not untrusted branch config. Issue #448 is transport only, not a Human Gate or editorial authority.

## 7. Human review provenance invariant

Before either normal Human Gate is presented, ChatGPT must commit **and push/retain** the exact current Production State and all Gate inputs on the Profile-bound canonical work branch. The Human reviews that exact durable commit.

Canonical `survey_human_gate_v2` requires `reviewed_repository_commit_sha` to:

- name a real Git commit;
- be reachable from canonical `work_branch`;
- contain exact current reviewed State and every configured Gate-input byte;
- for Publication Preview, contain the exact Candidate-bound PDF.

Connector-safe Human Gate requests additionally require that reviewed commit to be the exact request-only parent. The later request/event commit remains separate execution provenance.

A dangling commit object is insufficient historical authority even if its bytes temporarily exist in the local object database.

## 8. Human review history and cross-gate revision

Machine review authority remains:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

Each successful approval also stores an immutable snapshot:

```text
{source_root}/gates/reviews/approvals/architecture-rN.json
{source_root}/gates/reviews/approvals/publication-rN.json
```

The canonical approval files remain current active authority and may later be superseded; historical rN snapshots remain immutable evidence.

At `PUBLICATION_PREVIEW`, the Human chooses the regeneration boundary. If the boundary is at/after `ARCHITECTURE_ESTABLISHED`, valid Architecture approval is preserved. If the boundary is earlier because review found an upstream defect, Core:

1. records Publication `REQUEST_CHANGES` against exact Candidate/PDF review bytes;
2. verifies active Architecture approval provenance;
3. preserves old Architecture review + immutable approval snapshot;
4. removes/supersedes active canonical Architecture approval;
5. marks `ARCHITECTURE_REVIEW` pending again;
6. returns lifecycle/checkpoints to the Human-selected boundary;
7. requires Architecture rN+1 before publication continues.

This is a normal revision path, not a third Human Gate and not an Owner Exception Gate. Core never chooses the repair boundary.

## 9. Production vs Core maintenance

> **Production sessions repair editions; Core-maintenance sessions repair shared Core.**

Production may autonomously repair research gaps, edition-local Evidence/Selection/Architecture/draft errors, reader-facing prose/layout, and transient execution failures where the shared contract does not change.

A shared-Core defect is recorded and repaired separately. A formal production-validation run discovering such a defect is failed evidence and must be rerun cleanly after reviewed Core repair.

## 10. Grok/X invariant

```text
ChatGPT writes one self-contained Drive task file
-> Human passes exact task-file path/reference to Grok
-> Grok writes result
-> ChatGPT imports/dispositions exact bytes
-> ChatGPT resumes automatically
```

This is transport, not a third Human Gate. Do not search for/configure a Grok connector merely because X intake is required.

Weekly requires X/Grok and reader-facing `コミュニティの動き`; Retrospective/Thematic applicability remains explicit ChatGPT judgment under Profile/series policy.

## 11. Candidate/revision invariant

Any reader source/PDF change invalidates superseded Candidate authority. Candidate finalization atomically binds exact reader source, exact PDF, deterministic QA, semantic/editorial QA and visual QA. No Human Gate may point to old Candidate bytes while presenting new preview bytes.

## 12. Generality invariant

The redesign cannot be accepted only by W33/SP001-shaped tests. It must support:

- future Weekly;
- configured Retrospective monthly/half-year/annual/custom periods;
- standalone Thematic/LONGFORM including SP001 regression;
- Generative AI Foundations as a living outer authority;
- unplanned future Thematic topics;
- profile-neutral Human Gate round trips.

The operator bridge must remain Profile/path driven and must not hardcode topic names, source-root depth, branch-family prefixes, or Foundations volume structure.

## 13. Actions surface

The intended Actions surface remains exactly seven workflows:

1. `pipeline-contract-tests.yml` — CI only
2. `survey-production-v2-ci.yml` — focused Core CI
3. `build-weekly-survey.yml` — read-only build
4. `build-special-pdf.yml` — read-only build
5. `survey-production-v2-export-publication-preview.yml` — exact Preview transport
6. `survey-production-v2-release.yml` — exact-byte Release
7. `survey-production-v2-operator-bridge.yml` — trusted default-branch Issue #448 deterministic operator execution

Release remains the only lifecycle `WORKFLOW_DISPATCH` edge.

## 14. Acceptance status

Historical maintenance candidates and PASS results are non-reusable after mutation. In particular:

- `0a9e2d2c5bd9124ba626cdc7558e645d8021946c`: CI PASS, seven-point audit failed Point 7 on direct-local reviewed-commit provenance.
- `9932c8b7a14f1c3bdcc775df88056681b2841514`: fresh 7/7 PASS, then follow-up PR review invalidated the freeze with trust-bootstrap, review-durability and Publication-upstream-correction findings.
- an intermediate read-only work-branch signal + default-branch `workflow_run` design was considered and rejected because the signal workflow definition itself remained branch-supplied.

Before PR #447 may return to Human full-candidate review:

```text
finish implementation/test/doc/worklog synchronization
-> exact-head Core CI + Pipeline contract PASS
-> pre-freeze full-scope/stale-text cross-check
-> freeze one exact SHA
-> run all seven final-audit points from Point 1 on unchanged SHA
-> only unchanged 7/7 PASS may be recorded outside tree and presented
```

Post-integration real-production validation remains required for Weekly, SP001/Thematic, configured Retrospective, Foundations and structural cadence/generalization coverage.
