# Survey Production Core v2 — Audited Redesign Authority Overlay

Status: `INTEGRATED REDESIGN + OPERATOR BRIDGE/HUMAN-GATE MAINTENANCE CANDIDATE / SEVEN-POINT REAUDIT PENDING`  
Established: 2026-08-23 JST  
Human-Gate synchronization: 2026-08-24 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`

## 1. Purpose

This document is the authority overlay for the redesign that followed the failed W33/SP001 real-production validation and for the narrow operator-runtime/Human-Gate maintenance exposed by later clean revalidation and pre-approval audit.

It does not erase earlier Core v2 design history. `docs/survey-production-core-v2-authority.md` and earlier audit/remediation documents remain historical evidence. Where earlier authority conflicts with post-production evidence or this audited redesign direction, this overlay wins.

## 2. Redesign authority precedence

For current redesign/maintenance work, use:

```text
1. repository reality + Issues #400/#433/#434 + W33/SP001 execution/revalidation evidence
2. this redesign authority overlay
3. docs/survey-production-core-v2-operator-execution-bridge.md
4. docs/survey-production-core-v2-redesign-preimplementation-audit.md
5. docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md
6. docs/survey-production-core-v2-github-actions-policy.md
7. docs/survey-production-core-v2-execution-record-policy.md
8. docs/survey-production-core-v2-final-audit-rule.md
9. profile/edition/series editorial authorities
10. earlier Core v2 authority/audit documents as historical evidence where not superseded
```

Do not implement a clause from earlier authority when this overlay explicitly supersedes it.

## 3. Fundamental operator model

**ChatGPT remains the primary research/editorial/publication operator. The Human remains the authority for the two normal Human Gate decisions.**

The target production model is:

```text
Profile + edition/series authority + Production State
-> ChatGPT research/editorial work
-> narrow deterministic provenance/validation helpers
-> Architecture Review Human Gate
   -> APPROVED: deterministic recording -> resume drafting
   -> REQUEST_CHANGES: deterministic review record/selective invalidation -> ChatGPT repair -> Architecture Review rN
-> ChatGPT reader-facing manuscript / publication authorship
-> ChatGPT semantic/editorial QA
-> reproducible build + deterministic QA
-> ChatGPT exact-PDF visual QA
-> atomic Publication Candidate finalization
-> Publication Preview Human Gate
   -> APPROVED: deterministic recording -> Freeze
   -> REQUEST_CHANGES: deterministic review record/selective invalidation -> ChatGPT repair/revalidation -> Publication Preview rN
-> exact-byte Freeze / Release integrity
```

Deterministic helpers may execute through a direct exact local checkout/CLI or, when unavailable to the ChatGPT runtime, through the reviewed operator execution bridge. The bridge is execution transport for the same canonical Core mechanics, not a parallel state machine, editorial agent, or Human decision-maker.

## 4. Core / Profile / edition layering

### Shared Core

Owns cross-profile invariants only:

- lifecycle and the two normal Human Gates;
- explicit Human Gate decision recording and revision/selective-invalidation mechanics;
- provenance and Evidence boundaries;
- internal-vs-reader-facing Publication Boundary;
- deterministic / semantic / visual QA separation;
- exact candidate identity and atomic revision invalidation;
- execution-record requirements;
- Production-vs-Core-maintenance boundary;
- Grok/X transport/evidence-role invariants;
- safe deterministic execution semantics, including the optional operator bridge.

### Research Profiles

- `WEEKLY`
- `RETROSPECTIVE_PERIOD`
- `THEMATIC`

Research Profile guidance owns temporal/research semantics and must not be flattened into Publication Profile logic.

### Publication Profiles

- `WEEKLY_MAGAZINE`
- `LONGFORM_SPECIAL`

Publication Profile guidance owns publication-format semantics but does not replace Research Profile requirements.

### Edition / series authority

Scale/topic/series-specific guidance remains available without creating new generic workflow families, including monthly/half-year/annual retrospective guidance, standalone Thematic planning authority and the Generative AI Foundations living series memo.

## 5. Publication Boundary invariant

Internal research/editorial/provenance material is not a legal fallback source for reader-facing prose.

Internal-only examples include Screening/Selection/Evidence/materiality state, Architecture rationale, Human Review response rationale, internal IDs/obligations, Core contract vocabulary, package/coverage/promotion language and raw internal paths.

Before publication assembly, ChatGPT must explicitly author a reader-facing manuscript/publication surface. If required reader-facing content is missing, fail closed to ChatGPT authoring. Never fall back to internal fields.

Cadence-specific or post-render helpers must not synthesize reader-facing bibliography notes, Evidence/materiality labels, provenance legends, production-language annotations or other prose from internal artifacts. Deterministic tooling may validate or build exact authored publication bytes, but reader-facing wording remains publication-authoring responsibility.

## 6. Content-fidelity invariant

Architecture fidelity means approved `must-cover` obligations and materially selected story/lineage questions are actually explained to the reader. It does not mean mentioning the Architecture, reproducing review rationale, rendering one paragraph per Evidence record, or meeting a page/word quota.

`architecture_coverage` in the Reader Manuscript manifest is an author-declared accountability map. Deterministic validation proves structural completeness and exact binding; substantive fulfillment remains ChatGPT semantic/editorial judgment through `ARCHITECTURE_CONTENT_FIDELITY`.

## 7. Quality ownership

### Deterministic

Scripts/CI may prove schemas, paths/hashes, source/PDF/candidate identity, identifiers, citation/reference integrity, structural completeness of author-declared Architecture coverage, reproducible build/preflight, known exact-token leakage, Human Gate revision/state consistency, and Freeze/Release identity.

### ChatGPT semantic/editorial

ChatGPT reviews Publication Boundary, content fidelity, technical depth, profile-specific synthesis/chronology/historical semantics, claim-boundary wording, `総括`, applicable Grok/X disposition, repetition/generic fallback/production-language leakage, and applies requested Human revisions.

### ChatGPT visual

ChatGPT reviews the exact PDF for layout identity, whitespace, hierarchy, tables/boxes/URLs, clipping/glyphs and visually obvious content-thin output.

Machine PASS alone is never publication-quality PASS.

## 8. GitHub Actions invariant

Adopt `docs/survey-production-core-v2-github-actions-policy.md` as a hard design constraint.

GitHub Actions is a deterministic executor/verifier, not an editorial, publication-authoring or Human-decision agent.

The operator bridge is admitted only because it supplies the exact checked-out execution substrate that the connector-only ChatGPT runtime lacks. It may execute only the schema-enumerated canonical deterministic operations from an immutable edition-local request. It must not accept arbitrary commands or take ownership of research, Selection, Architecture, drafting, semantic/visual review, layout repair, Release, or the Human decision itself.

The bridge **may record an already explicit Human `APPROVED` or `REQUEST_CHANGES` decision and apply its deterministic lifecycle consequence**. Such requests require explicit Human provenance, exact pending gate/current State and the next contiguous review revision; revision requests additionally require Human-supplied requested changes and a gate-specific enum-constrained regeneration boundary. Core validates these inputs but does not choose or reinterpret them.

Retrospective initialization is admissible only by exposing the pre-existing generic `scripts/survey_period_v2.py` configured-period Profile path. The bridge must not introduce a second Retrospective scope schema, Profile builder, or monthly/half-year/annual execution engines.

Direct local CLI execution remains preferred when available. Do not replace the old workflow set with cadence/topic-specific authoring workflows.

## 9. Production vs Core-maintenance invariant

> **Production sessions repair editions; Core-maintenance sessions repair shared Core.**

Production sessions may autonomously repair research gaps, edition-local Evidence/Selection/Architecture/draft errors, reader-facing prose/layout and transient execution failures where shared behavior does not change.

Production sessions must not author changes to reusable Core scripts/schemas/workflows/config/shared renderer/shared style merely to keep the edition moving. A shared-Core defect is recorded under the edition execution record and returned to Core maintenance.

For a formal Core acceptance run, discovering a shared-Core defect invalidates that run as acceptance evidence. Repair separately and rerun cleanly.

## 10. Grok/X handoff invariant

Normal manual mediation is:

```text
ChatGPT creates one self-contained Grok task file in Google Drive
-> ChatGPT gives Human the exact Drive task-file path/reference
-> Human gives that path/reference to Grok
-> Grok reads the file and writes the instructed result
-> ChatGPT imports/dispositions the result and resumes automatically
```

Do not search for or configure a Grok connector merely because X Source Intake is required. The handoff is transport, not a Human approval Gate.

## 11. Human Gates and revision semantics

The two normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Do not add a third routine Human Gate to compensate for inadequate autonomous editorial QA.

At either normal gate, the Human may explicitly choose:

- `APPROVED`; or
- routine `REQUEST_CHANGES` with requested changes and a regeneration boundary allowed by the current Core contract.

`REQUEST_CHANGES` is not an Owner-level Exception Gate. Deterministic Core records an immutable rN review authority, resets only downstream machine/gate provenance required by the Human-supplied boundary, removes superseded canonical Stage Checkpoints that would prevent clean regeneration, and returns control to ChatGPT. ChatGPT performs the actual research/editorial/visual repair and revalidates to the same gate as rN+1.

Machine review authority is retained under:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

Prior review revisions remain reconstructable through exact SHA-256 values and reviewed repository commit provenance while only current Production State/checkpoint/gate authority is active.

A genuine Exception Gate remains only for an unresolved Owner decision that cannot safely be expressed as a normal revision. A shared-Core implementation defect is a maintenance dependency, not a reason for routine Human confirmation.

## 12. Universal/profile-specific reader requirements

### Every Weekly/Special

- final substantive `総括` or explicitly equivalent reader-facing synthesis;
- no internal production-state leakage;
- Human Review rationale is applied to the artifact, not serialized as reader-facing rebuttal;
- page targets remain planning envelopes, not padding quotas.

### Weekly

- mandatory reader-facing `コミュニティの動き` every issue;
- Grok/X result receives explicit editorial disposition;
- quiet week remains an explicit finding rather than silent omission.

### Retrospective Period

Preserve configured-period authority plus coverage-audit, chronology/lifecycle, period-normalization and period-synthesis authority, including annual temporal-skew/trajectory rules where applicable. Canonical initialization uses the existing `survey_period_v2` generic Profile builder; richer cadence-specific research/synthesis remains guide/edition semantics.

### Thematic

Preserve research closure, lineage/parallel-branch reasoning where relevant, historical attribution and hindsight boundaries.

### Longform Special

Preserve longform depth and mixed-layout identity without forcing one topic taxonomy or one-to-one Evidence rendering.

### Foundations

Remain a living series authority layered over `THEMATIC + LONGFORM_SPECIAL`; do not build a rigid generic series engine unless later real production demonstrates repeated need.

## 13. Execution records

Every new production run uses the Profile-declared source root:

```text
{source_root}/execution/
  index.md
  sessions/
  reviews/
  defects/
```

When the operator bridge is used it may additionally create `requests/` and `bridge-runs/`. Human-readable `execution/reviews/architecture-rN.md` and `publication-rN.md` summarize/pointer the machine Human-review JSON authorities; they are not a second state machine.

Follow `docs/survey-production-core-v2-execution-record-policy.md` for granularity.

## 14. Candidate/revision invariant

Any source/PDF change invalidates superseded Publication Candidate authority.

Candidate finalization atomically binds exact reader-facing source identity, exact PDF identity, deterministic QA, ChatGPT semantic/editorial QA, ChatGPT visual QA and Publication Candidate identity.

No legal Human Gate state may point to old candidate bytes while displaying new preview bytes. Publication Preview `REQUEST_CHANGES` must invalidate affected Validation/Candidate authority before rN+1 can be approved.

## 15. Acceptance/generalization invariant

The redesign cannot be validated only by W33/SP001-shaped tests.

Final acceptance must include representative evidence for Weekly, standalone Thematic/LONGFORM (SP001 regression), Retrospective Period, Foundations-guided series work, structural monthly/half-year/annual compatibility, unplanned Thematic work, and profile-neutral Human Gate round trips.

The operator bridge must remain Profile/path driven and must not hardcode W33/SP001 topic structure, source-root depth or `weekly/**` / `special/**` branch naming. Allowed cold-start operations correspond to Weekly, configured Retrospective Period and Thematic Profile construction. Foundations remains a Thematic/Longform series authority, not a fourth initialization engine. Once canonical Profile/State exists, `ADVANCE_STAGE` and Human Gate recording/revision mechanics bind exact Profile-declared `source_root` and `work_branch`.

## 16. Implementation and acceptance status

The original redesign is integrated. Clean connector-only revalidation exposed the deterministic execution gap; pre-approval full-system audit then exposed missing Human Gate continuation/revision semantics. The current maintenance candidate addresses both with:

- direct local deterministic execution when available and one optional reviewed operator bridge otherwise;
- canonical Weekly/configured-Retrospective/Thematic cold start;
- compact deterministic stage execution over ChatGPT-authored artifacts;
- explicit Reader Manuscript and Publication Boundary;
- deterministic Quality Bundle separated from semantic/editorial and exact-PDF visual review;
- atomic Publication Candidate identity;
- canonical Human Gate rN review records, approval recording and `REQUEST_CHANGES` selective invalidation for both normal gates;
- standardized edition execution records;
- one-file Grok/X Drive handoff;
- exactly seven workflows: two CI/contract workflows, two reproducible builds, exact-byte Preview transport, Release, and one deterministic operator bridge.

The bridge request allowlist is exactly eight kinds: three initializers, `ADVANCE_STAGE`, and four explicit Human Gate recording/revision operations. A generic Human-decision command surface is prohibited.

`tests/test_survey_human_gate_v2.py` exercises direct Architecture/Publication approve/revise round trips and negative boundaries. `tests/test_survey_core_execution_bridge_human_gate_v2.py` exercises the same connector-safe bridge path. `tests/test_survey_period_v2.py` protects generic configured monthly/half-year/annual Retrospective construction. `tests/test_survey_pilot_bootstrap_v2.py` protects the seven-workflow surface.

This maintenance implementation is **not** final Core acceptance. Before Human full-candidate review, the repository must:

```text
finish regression/CI repair
-> synchronize all current candidate authority/contracts/worklog
-> resolve any remaining pre-freeze consistency finding
-> freeze one exact candidate head SHA
-> run exact-head Core CI + Pipeline contract tests
-> run the complete seven-point final audit from point 1 on that unchanged SHA
-> invalidate all seven verdicts if any tree change becomes necessary
-> present only the unchanged 7/7 passing SHA for Human full-candidate review
```

Cold-start production re-validation remains required after the maintenance is reviewed/integrated. Prior W33/SP001 attempts and all earlier six-point candidate audits remain non-PASS/historical evidence.
