# Survey Production Core v2 — Operator Execution Bridge

Status: `MAINTENANCE CANDIDATE / HUMAN-GATE ROUNDTRIP + REVIEW-COMMIT PROVENANCE IMPLEMENTED / FIXED-HEAD REAUDIT PENDING`

Established: 2026-08-23 JST  
Human-Gate synchronization: 2026-08-24 JST

Related evidence:

- `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`
- W33 clean revalidation branch `weekly/2026-W33-v2-work`
- SP001 clean revalidation branch `special/SP001-v2-work`

Related policy:

- `docs/survey-production-core-v2-github-actions-policy.md`
- `docs/survey-production-core-v2-execution-record-policy.md`
- `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Problem statement

The post-merge W33/SP001 clean revalidation established that the redesigned responsibility split is directionally correct but one operational assumption was incomplete.

The normal ChatGPT production runtime can read/write exact repository files through the GitHub connector, inspect commits/trees/blobs/Actions, perform open-ended research/editorial work, and perform the Human-mediated Google Drive Grok/X handoff. It cannot necessarily mount the exact GitHub work branch and invoke the repository's canonical local Core CLI over that exact tree.

This is an operator execution capability gap. Hand-authoring `production-state.json`, Stage Checkpoints, Architecture approvals, Publication Preview approvals, review-revision authority or other machine records is not an acceptable workaround.

The later pre-approval full-system audit exposed the same gap after a normal Human Gate: connector-only operation could reach a gate but could not canonically record an already explicit Human approval or ordinary `REQUEST_CHANGES` decision. The bridge therefore covers those deterministic recording/invalidation mechanics as well as initialization/stage advancement.

A subsequent fixed-head seven-point audit found a related provenance asymmetry after the bridge's request-parent binding was repaired: the preferred direct-local Human Gate path accepted a syntactically valid reviewed commit SHA without proving that the commit existed or contained the exact reviewed State/Gate-input bytes. The canonical `survey_human_gate_v2` helper now performs that Git commit-tree proof in both execution modes; Actions adds the connector-specific request-parent proof on top.

## 2. Governing boundary

The bridge does **not** change the primary-operator model.

ChatGPT remains responsible for Source Intake/research strategy, Evidence interpretation, materiality/completeness, Selection, Architecture, drafting/synthesis, semantic/editorial review, exact-PDF visual review, applying requested revisions and deciding when a genuine Owner-level Exception Gate is necessary.

The Human remains the sole authority for the actual Human Gate decision. The bridge/Core may not infer approval, invent requested changes or choose a regeneration boundary.

The bridge may execute only deterministic Core mechanics already defined by repository authority:

1. canonical Weekly Profile + Production State initialization through existing Core logic;
2. canonical configured Retrospective Period Profile + Production State initialization through existing `scripts/survey_period_v2.py`;
3. canonical Thematic Profile + Production State initialization through existing Core logic;
4. deterministic stage-contract validation over already-authored artifacts;
5. compact Stage Checkpoint materialization and one-edge lifecycle advancement;
6. deterministic recording of an explicitly supplied Architecture approval;
7. deterministic recording of an explicitly supplied Architecture `REQUEST_CHANGES` decision plus allowed selective invalidation;
8. deterministic recording of an explicitly supplied Publication Preview approval;
9. deterministic recording of an explicitly supplied Publication Preview `REQUEST_CHANGES` decision plus allowed selective invalidation.

Items 6–9 do not create Human judgment. They require explicit Human provenance and call canonical `scripts/survey_human_gate_v2.py` mechanics.

For Retrospective Period work, **no new profile builder was added by this maintenance**. Core already contained `survey_period_v2.resolve_configured_period()` and `survey_period_v2.period_profile()`, covering generic monthly, half-year and annual configured periods. The bridge merely exposes that existing deterministic path to connector-only runtimes.

Foundations remains a living series authority layered over Thematic/LONGFORM rather than a bridge initialization operation. Once canonical Profile/State exists, stage and Human Gate mechanics are Profile/path driven.

Release remains owned by the dedicated release workflow.

## 3. Transport model

```text
ChatGPT reviews one exact main Core baseline
-> ChatGPT authors/researches edition artifacts
-> ChatGPT commits those artifacts normally
-> when a Human Gate is reached, Human reviews the exact current branch-parent commit
-> Human supplies APPROVED or REQUEST_CHANGES + feedback/boundary
-> ChatGPT commits ONE immutable operator request as a request-only commit
   whose reviewed_repository_commit_sha names that reviewed parent commit
-> GitHub Actions checks out that exact request commit
-> workflow proves reviewed_repository_commit_sha == request-only commit parent
-> workflow proves the branch's shared Core/contract tree still matches reviewed main
-> canonical Human Gate helper proves that reviewed commit exists and its tree contains
   the exact reviewed Production State + Gate-input bytes
-> bridge executes one whitelisted deterministic Core operation
-> bridge verifies its outputs
-> workflow enforces Profile-bound edition-local write scope
-> github-actions[bot] commits only generated edition-local authorities
-> no output commit retriggers the bridge
-> ChatGPT resumes from canonical State and applies any requested editorial repair
```

Every request explicitly binds:

- `issue_id`;
- Profile-declared `source_root`;
- `work_branch`;
- one exact lowercase 40-hex `reviewed_main_sha`;
- one operation from the schema enum.

Initialization requests also carry `operation.execution_record.reviewed_main_sha`; the workflow requires it to equal the top-level baseline.

Human Gate requests additionally carry explicit:

- canonical `state_path`;
- `expected_revision`;
- exact lowercase 40-hex `reviewed_repository_commit_sha` identifying the commit whose edition bytes the Human actually reviewed;
- `reviewed_by`;
- `reviewed_at`;
- `review_reference`;
- for revision requests, `requested_changes` and an enum-constrained `regeneration_boundary`.

For connector-safe bridge execution, `reviewed_repository_commit_sha` must equal the parent of the immutable request-only commit. The request commit itself is execution transport and is **not** the reviewed edition commit. Independently of that transport rule, canonical Human Gate Core requires the named commit to exist and to contain regular-file bytes whose SHA-256 values equal the current reviewed State and all Gate inputs. Publication Preview includes the exact Candidate-bound PDF in that proof.

Canonical request location:

```text
{source_root}/execution/requests/<request-id>.json
```

Canonical bridge-run receipt location:

```text
{source_root}/execution/bridge-runs/<request-id>/
```

Canonical machine Human-review history:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

`source_root` must remain repository-local under `sources/`. It is not inferred by the workflow from `issue_id`. The request filename stem and `request_id` must match exactly.

## 4. Why this still satisfies the Actions responsibility policy

The bridge satisfies the Actions admission rule because:

- **concrete advantage:** it supplies the exact checked-out execution environment unavailable to the connector-only ChatGPT runtime;
- **mechanical scope:** it invokes only enumerated deterministic Core operations whose semantics exist independently of the workflow.

The bridge must not:

- search the web or choose sources;
- author Retrospective/Thematic editorial scope or Architecture;
- write Evidence/Selection/Architecture prose or decisions;
- generate reader-facing prose;
- make semantic or visual PASS judgments;
- decide Human approval or rejection;
- invent requested changes or select a regeneration boundary;
- perform layout repair;
- mutate shared Core/config/schema/workflow paths during edition production;
- accept shell snippets, Python expressions, module names, executable paths, workflow names or other arbitrary command surfaces.

Recording an already explicit Human decision is mechanical execution, not delegation of the decision itself.

## 5. Request operations

The allowlist is exactly eight request kinds:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

### Initialization operations

Weekly, configured Retrospective Period and Thematic initialization use only their existing canonical Profile builders, require generated Profile `issue_id` / `source_root` / `work_branch` identity to equal the request, and create canonical Profile/State/execution records.

Configured Retrospective initialization accepts only the configured `special_slug` and delegates to:

```text
survey_period_v2.resolve_configured_period(...)
-> survey_period_v2.period_profile(...)
-> exact request/Profile identity check
-> canonical Core initialize(...)
```

No cadence-specific bridge engine or second Retrospective scope schema is introduced.

### `ADVANCE_STAGE`

Allowed deterministic effect:

- require exact current `expected_from_state`;
- require current Production Profile identity to equal request identity;
- validate exact already-authored stage artifacts with canonical stage-validation semantics;
- generate `CORE_STAGE_CONTRACT` deterministic result authority;
- wrap ChatGPT-authored research/editorial/visual review rows without changing their meaning;
- create the compact Stage Checkpoint;
- advance Production State exactly one lifecycle edge.

The request cannot supply its own deterministic `CORE_STAGE_CONTRACT` PASS.

### Human Gate approval operations

`RECORD_ARCHITECTURE_APPROVAL` and `RECORD_PUBLICATION_PREVIEW_APPROVAL` require a pending matching gate and exact reviewed-byte authority. They call `survey_human_gate_v2`, which first proves reviewed-commit existence and exact tree-byte identity, then delegates to the existing canonical exact-byte approval mechanics and writes the contiguous machine review revision record/index.

An approval request does not contain a generic `decision` field. The operation kind itself is a narrow recorder invoked only after the Human has explicitly approved.

### Human Gate revision operations

`REQUEST_ARCHITECTURE_REVISION` and `REQUEST_PUBLICATION_PREVIEW_REVISION` require:

- pending matching Human Gate;
- exact current reviewed State/gate inputs;
- next contiguous `expected_revision`;
- explicit Human provenance, including exact reviewed repository commit;
- non-empty requested-changes summary;
- a gate-specific enum-constrained regeneration boundary.

Core then:

1. proves the named reviewed commit exists and contains the exact reviewed State/Gate-input bytes;
2. records exact reviewed State/artifact hashes plus the explicit reviewed repository commit;
3. writes the immutable `REQUEST_CHANGES` review revision;
4. returns State to the supplied allowed boundary;
5. resets only machine checkpoints/gate provenance downstream of that boundary;
6. removes superseded canonical Stage Checkpoint files that would block regeneration;
7. preserves unaffected upstream authority, including approved Architecture when Publication Preview alone is revised.

ChatGPT then performs the requested editorial/research repair and re-runs normal validation to the same Human Gate. The next review must use the next contiguous revision number.

## 6. Human review provenance and historical/current authority

Machine review JSON is the durable exact provenance layer. Human-readable `execution/reviews/architecture-rN.md` and `publication-rN.md` remain operational summaries and pointers, not a second State machine.

Each machine review revision records:

- gate + contiguous revision;
- `APPROVED` or `REQUEST_CHANGES`;
- exact reviewed Production State path/SHA;
- exact reviewed gate artifacts and SHA-256 values;
- exact reviewed repository commit SHA supplied by the Human Gate request/direct-local invocation;
- Human identity/time/reference;
- requested changes + regeneration boundary when applicable;
- approval authority when applicable.

Canonical Human Gate Core verifies that the named reviewed repository commit is a real commit and that each recorded reviewed path is a regular file in that commit tree with bytes matching the exact current review SHA. For connector-safe bridge execution, the workflow additionally verifies that this reviewed repository commit is exactly the request-only commit parent. The bridge-run receipt separately records the request/event commit and the Human-reviewed repository commit, preventing those two identities from being conflated.

After `REQUEST_CHANGES`, superseded artifact bytes may be replaced at their canonical paths during regeneration. Historical exact identity remains reconstructable from the review record's hashes and reviewed repository commit. Current Production State/checkpoint/gate provenance alone determines current authority.

A stale request for r1 after r1 has already been recorded fails because the next revision is r2. Once a gate revision is `APPROVED`, no later review revision for that gate is accepted.

## 7. Reviewed-main Core preflight

Before installing dependencies or invoking the bridge, the workflow must:

1. validate request-level `reviewed_main_sha` shape;
2. fetch current `main` and require the reviewed SHA to be an ancestor of current main;
3. resolve the exact request-only commit parent and require it to descend from the reviewed SHA;
4. for any Human Gate operation, require `reviewed_repository_commit_sha` to equal that exact request parent;
5. for any initialization operation, require execution-record reviewed-main SHA equality;
6. protect at minimum `.github/workflows`, `config`, `schemas`, and `scripts`, plus configured `implementation_control_roots` and every pipeline/quality contract file;
7. require those protected bytes at the request parent to equal the reviewed-main baseline;
8. only then install dependencies and execute Core.

Legitimate edition-local Raw/research/Evidence/manuscript/Human-review artifacts may differ from main.

## 8. Fail-closed controls

The workflow/bridge/Core combination must enforce:

1. trigger limited to `sources/**/execution/requests/*.json` and not `main`;
2. one newly added request and request-only triggering commit;
3. exact reviewed-main provenance and shared-Core byte equivalence;
4. Human Gate request explicitly binds a reviewed repository SHA equal to the request-only parent, not the request/event commit;
5. canonical Human Gate Core rejects a nonexistent reviewed commit, a commit missing any reviewed path, a non-regular reviewed tree entry, or same-path bytes that do not match current reviewed authority;
6. exact request branch/ref match;
7. source root under `sources/` and canonical request path;
8. generated/current Profile identity match;
9. configured Retrospective slug resolution through existing `survey_period_v2` only;
10. unconfigured Retrospective slug and pre-period-end initialization rejection;
11. exact lowercase event commit SHA;
12. eight-kind enum operation surface only;
13. traversal-safe repository paths;
14. initialization refusal when canonical Profile/State already exists;
15. stale `expected_from_state` refusal;
16. no agent impersonation of deterministic reviews;
17. Human Gate operation requires pending matching gate/current State;
18. stale/non-contiguous Human review revision refusal;
19. gate-specific regeneration-boundary refusal;
20. changed reviewed/checkpoint bytes fail before approval/revision recording;
21. generic Human-decision/rejection command surfaces are absent;
22. immutable/non-overwritable bridge-run ids;
23. generated writes only below validated Profile `source_root`;
24. no mutation of immutable request authority;
25. bot output commits cannot recursively chain the bridge.

The trigger intentionally does not hardcode cadence branch prefixes. Branch authority comes from request/Profile equality.

## 9. Validation consequence

The W33/SP001 clean revalidation attempts that exposed the operator gap remain non-PASS evidence. Adding the bridge and Human Gate round-trip mechanics changes shared Core implementation/contracts.

The first seven-point fixed-head audit of `0a9e2d2c5bd9124ba626cdc7558e645d8021946c` is also historical/invalidated evidence: Points 1–6 passed, but Point 7 found the direct-local reviewed-commit provenance gap described above. No verdict from that audit may be carried into the next candidate.

Acceptance sequence is:

```text
finish bridge + Human Gate + reviewed-commit provenance maintenance
-> exact-head CI/regression
-> complete fixed-head seven-point audit from zero
-> Human full-candidate review
-> unchanged integration
-> clean Weekly + Thematic/SP001 + representative Retrospective + Foundations validation
```

No pre-maintenance W33/SP001 lifecycle result and no earlier six/seven-point maintenance audit may be relabeled as successful canonical validation.

## 10. Direct-local CLI remains preferred

The bridge is a fallback execution substrate. If ChatGPT/operator runtime has an exact local checkout, use canonical local helpers directly, including `scripts/survey_human_gate_v2.py` for deterministic Human-decision recording/revision consequence.

Direct local and bridge modes must produce the same canonical artifact semantics and the same reviewed-commit reconstructability guarantee. In direct-local mode, `survey_human_gate_v2` itself proves the named reviewed commit exists and contains the exact reviewed State/Gate-input bytes before recording a Human decision. In bridge mode, the same canonical proof runs and Actions additionally proves the reviewed commit is the immutable request-only parent. The bridge adds transport and execution receipts, not a parallel state machine.
