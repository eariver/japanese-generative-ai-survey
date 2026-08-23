# Survey Production Core v2 — Audited Redesign Authority Overlay

Status: `INTEGRATED REDESIGN + OPERATOR BRIDGE MAINTENANCE CANDIDATE / FIXED-HEAD REAUDIT PENDING`  
Established: 2026-08-23 JST  
Bridge-maintenance synchronization: 2026-08-23 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`

## 1. Purpose

This document is the authority overlay for the redesign that followed the failed W33/SP001 real-production validation and for the narrow operator-runtime maintenance exposed by the later clean post-merge revalidation.

It does not erase the earlier Core v2 design history. `docs/survey-production-core-v2-authority.md` and earlier audit/remediation documents remain historical evidence of how the merged Core was designed and why it behaved as it did.

For the current redesigned Core and this maintenance candidate, where earlier authority conflicts with post-production evidence or this audited redesign direction, this overlay wins.

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

**ChatGPT remains the primary research/editorial/publication operator.**

The target production model is:

```text
Profile + edition/series authority + Production State
-> ChatGPT research/editorial work
-> narrow deterministic provenance/validation helpers
-> Architecture Review Human Gate
-> ChatGPT reader-facing manuscript / publication authorship
-> ChatGPT semantic/editorial QA
-> reproducible build + deterministic QA
-> ChatGPT exact-PDF visual QA
-> atomic Publication Candidate finalization
-> Publication Preview Human Gate
-> exact-byte Freeze / Release integrity
```

Deterministic helpers may execute either through a direct exact local checkout/CLI or, when that substrate is unavailable to the ChatGPT operator runtime, through the reviewed operator execution bridge. The bridge is an execution transport for the same canonical Core mechanics, not a parallel state machine or an editorial agent.

## 4. Core / Profile / edition layering

### Shared Core

Owns cross-profile invariants only:

- lifecycle and Human Gates;
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

Scale/topic/series-specific guidance remains available without creating new generic workflow families.

Examples:

- monthly / half-year / annual retrospective guidance;
- standalone Thematic planning authority;
- Generative AI Foundations living series memo.

## 5. Publication Boundary invariant

Internal research/editorial/provenance material is not a legal fallback source for reader-facing prose.

Internal-only examples include:

- Screening/Selection/Evidence/materiality state;
- Architecture rationale and Human Review response rationale;
- internal IDs and obligations;
- Core contract vocabulary;
- package/coverage/promotion language used to manage production;
- raw internal paths.

Before publication assembly, ChatGPT must have explicitly authored a reader-facing manuscript/publication surface.

The exact representation is implementation-dependent. It does **not** need to be one universal JSON payload. The invariant is semantic separation and exact provenance.

If required reader-facing content is missing, fail closed to ChatGPT authoring. Never fall back to internal fields.

Cadence-specific or post-render helpers must not synthesize reader-facing bibliography notes, Evidence/materiality labels, provenance legends, production-language annotations, or other prose from internal production artifacts. Deterministic tooling may validate or build exact authored publication bytes, but reader-facing wording and source-note presentation remain publication-authoring responsibility.

## 6. Content-fidelity invariant

Architecture fidelity means that approved `must-cover` obligations and materially selected story/lineage questions are actually explained to the reader.

It does not mean:

- mentioning the Architecture;
- reproducing review rationale;
- rendering one paragraph per Evidence record;
- meeting a page/word quota.

Supporting Evidence may appear through narrative, chronology, Technical Notes, comparison, attribution or bibliography as appropriate.

`architecture_coverage` in the Reader Manuscript manifest is an **author-declared accountability and traceability map**. Deterministic validation must prove that every approved `must_cover_requirement` has exactly the required non-empty mapping and that the manifest remains bound to exact artifacts. It does **not** machine-prove that the cited reader prose substantively satisfies the requirement. That substantive judgment belongs to ChatGPT semantic/editorial QA through the required `ARCHITECTURE_CONTENT_FIDELITY` review; a claimed `FULFILLED` mapping must be rejected or revised when the prose is materially inadequate.

## 7. Quality ownership

### Deterministic

Scripts/CI may prove crisp properties such as:

- schemas;
- paths/hashes;
- source/PDF/candidate identity;
- identifiers;
- citation/reference integrity;
- completeness of the author-declared Architecture coverage map, without treating it as substantive content proof;
- reproducible build/preflight;
- known exact-token leakage;
- Freeze/Release identity.

### ChatGPT semantic/editorial

ChatGPT must review:

- Publication Boundary;
- content fidelity to approved Architecture, including whether every claimed `architecture_coverage` location materially satisfies its requirement;
- technical depth;
- profile-specific synthesis/chronology/historical semantics;
- claim-boundary wording;
- `総括` quality;
- applicable Grok/X editorial disposition;
- repetition/generic fallback/production-language leakage.

### ChatGPT visual

ChatGPT reviews the exact PDF for layout identity, whitespace, hierarchy, tables/boxes/URLs, clipping/glyphs and visually obvious content-thin output.

Machine PASS alone is never equivalent to publication-quality PASS.

## 8. GitHub Actions invariant

Adopt `docs/survey-production-core-v2-github-actions-policy.md` as a hard design constraint.

GitHub Actions is a deterministic executor/verifier, not an editorial or publication-authoring agent.

Retain Actions only where:

- Actions execution has concrete independent/reproducibility/security value; or
- the task is genuinely mechanical and no research/editorial judgment is transferred into CI.

The operator bridge is admitted only because it supplies the exact checked-out execution substrate that the normal connector-only ChatGPT runtime lacks. It may execute only an enum allowlist of canonical deterministic Core operations from an immutable edition-local request. It must not accept arbitrary commands or take ownership of research, Selection, Architecture, drafting, semantic/visual review, Human approval, layout repair or Release.

Direct local CLI execution remains preferred when available.

Do not replace the old workflow set with cadence/topic-specific authoring workflows.

## 9. Production vs Core-maintenance invariant

> **Production sessions repair editions; Core-maintenance sessions repair shared Core.**

Production sessions may autonomously repair:

- research gaps;
- edition-local Evidence/Selection/Architecture/draft errors;
- reader-facing prose/layout;
- transient execution failures where shared behavior does not change.

Production sessions must not author changes to reusable Core scripts/schemas/workflows/config/shared renderer/shared style merely to keep the edition moving.

A shared-Core defect is recorded under the edition execution record and returned to Core maintenance.

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

Do not search for or configure a Grok connector merely because X Source Intake is required.

The handoff is transport, not a Human approval Gate.

## 11. Human Gates

The two normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Do not add a third routine Human Gate to compensate for inadequate autonomous editorial QA.

A genuine Exception Gate remains only for an unresolved Owner decision that cannot be safely derived from authority.

A shared-Core implementation defect is a maintenance dependency, not a reason for repeated routine Human confirmation.

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

Preserve existing period coverage-audit, chronology/lifecycle, period-normalization and period-synthesis authority, including annual temporal-skew/trajectory rules where applicable.

### Thematic

Preserve research closure, lineage/parallel-branch reasoning where relevant, historical attribution and hindsight boundaries.

### Longform Special

Preserve longform depth and mixed-layout identity without forcing one topic taxonomy or one-to-one Evidence rendering.

### Foundations

Remain a living series authority layered over `THEMATIC + LONGFORM_SPECIAL`; do not build a rigid generic series engine unless later real production demonstrates repeated need.

## 13. Execution records

Every new production run uses the Profile-declared canonical edition source root:

```text
{source_root}/execution/
  index.md
  sessions/
  reviews/
  defects/
```

When the operator execution bridge is used, it may additionally create:

```text
  requests/
  bridge-runs/
```

Those optional directories contain immutable execution requests and exact deterministic execution receipts. They are transport/provenance, not a second Production State. Direct-local CLI runs need not create them.

Follow `docs/survey-production-core-v2-execution-record-policy.md` for content and granularity.

## 14. Candidate/revision invariant

Any source/PDF change invalidates the superseded Publication Candidate authority.

Candidate finalization must atomically bind:

- exact reader-facing source identity;
- exact PDF identity;
- deterministic QA;
- ChatGPT semantic/editorial QA;
- ChatGPT visual QA;
- Publication Candidate identity.

No legal Human Gate state may point to old candidate bytes while displaying new preview bytes.

## 15. Acceptance/generalization invariant

The redesign cannot be validated only by W33/SP001-shaped tests.

Final acceptance must include representative evidence for:

- Weekly;
- standalone Thematic/LONGFORM (SP001 regression);
- Retrospective Period;
- Foundations-guided series work;
- structural monthly/half-year/annual and unplanned-Thematic compatibility.

The operator bridge must remain Profile/path driven. It must not hardcode W33/SP001 topic structure, fixed edition source-root depth, or `weekly/**` / `special/**` branch naming. It may expose only initialization operations already owned by canonical Core builders; it must not invent Retrospective/series semantics merely to broaden its API. Once a canonical Profile/State exists, `ADVANCE_STAGE` is Profile-neutral and must bind the exact Profile-declared `source_root` and `work_branch`.

Use a small representative matrix plus structural audits rather than an exhaustive synthetic future-edition matrix.

## 16. Implementation and acceptance status

The original redesign is integrated. The connector-only clean revalidation exposed the operator-runtime execution gap, and the current maintenance candidate adds the narrow fallback described above.

Current intended boundaries include:

- ChatGPT-owned ordinary lifecycle stages with Release as the only lifecycle workflow-dispatched stage;
- direct local deterministic execution when available, with an optional deterministic operator bridge when an exact local checkout is unavailable;
- explicit Reader Manuscript and reader-facing Publication Boundary;
- deterministic Quality Bundle separated from semantic/editorial and exact-PDF visual review;
- atomic Publication Candidate identity and revision invalidation;
- standardized edition execution records;
- one-file Grok/X Drive handoff;
- **seven-workflow Actions surface**: two CI/contract workflows, two reproducible build workflows, exact-byte Preview transport, Release, and one narrowly constrained deterministic operator bridge.

`tests/test_survey_pilot_bootstrap_v2.py` requires exact equality with that seven-workflow set. A new eighth workflow is prima facie architectural regression unless deliberately reviewed against the Actions admission rule.

This maintenance implementation is **not** final Core acceptance. Before Human full-candidate review, the repository must:

```text
finish regression/CI repair
-> synchronize all intended candidate wording and contracts
-> freeze one candidate head SHA
-> run the complete six-point final audit from zero on that exact unchanged SHA
-> invalidate the audit if any tree change is required
-> present only the unchanged passing SHA for Human full-candidate review
```

Cold-start production re-validation remains required after the bridge maintenance is reviewed/integrated; the prior W33/SP001 attempts remain non-PASS evidence and are not converted into PASS by this maintenance.
