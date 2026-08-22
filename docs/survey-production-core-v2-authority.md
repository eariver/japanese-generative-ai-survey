# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY / WU-012 CHATGPT-FIRST REALIGNMENT`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`

## 1. Purpose

This index identifies the live semantic authority for Survey Production Core v2 while preserving earlier design/audit documents as historical reasoning.

Current `main` remains the production source of truth until the coherent v2 candidate is explicitly Human-reviewed and merged. This file is authoritative for work on the improvement branch only until that merge.

The 2026-08-22 ChatGPT-first pre-approval re-audit corrected a material premise mismatch in the first WU-012 audit. Where older documents require stronger machine/external-workflow authority than this index or `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`, the ChatGPT-first re-audit controls.

## 2. Fundamental operating model

**ChatGPT is the primary research/editorial operator.**

A normal production session is expected to:

```text
user supplies target + requested stopping Human Gate
-> ChatGPT reads current main/repository policy/state
-> ChatGPT performs research/editorial reasoning
-> deterministic helpers perform repetitive/crisp/provenance-sensitive work
-> ChatGPT records enough repository state for another session to resume
-> stop only at the requested Human Gate or a genuine Exception Gate
```

Scripts, schemas and GitHub workflows exist to support this work. They are not the editorial intelligence and should not replace qualitative reasoning with ceremonial machine state.

This is consistent with the existing repository-agent model in `AGENTS.md` and `docs/special-session-bootstrap.md`.

## 3. Authority precedence

For Survey Production Core v2 improvement work, use:

```text
1. repository reality
2. this authority index
3. docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md
4. docs/checkpoints/survey-production-core-v2-worklog.md for status/next action only
5. whole-system audit + explicit remediation status
6. WU-011 second-audit closure / earlier audit amendments
7. base improvement plan and Phase 0/1/2/3 design documents
8. historical/current-main implementation docs used as evidence
```

`docs/survey-production-core-v2-improvement-plan.md` remains the base plan, but its first pre-approval §§16–18 machine-first remediation is **superseded where conflicting** by the ChatGPT-first re-audit.

## 4. Document status map

| Document | Current status | Role |
|---|---|---|
| `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md` | `AUTHORITATIVE PRE-APPROVAL RE-AUDIT` | corrected operator/tool boundary and WU-012 scope |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL WORK STATUS` | current WU status, evidence and next action |
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE BASE PLAN / §§16–18 SUPERSEDED IN PART` | overall goals/phases; not current WU-012 authority where machine-first language conflicts |
| `docs/survey-production-core-v2-component-inventory.md` + audit amendment | `ACTIVE HISTORICAL DESIGN EVIDENCE` | Core/Profile/Publication/Series ownership map |
| `docs/survey-production-core-v2-contract-normalization*.md` | `ACTIVE BASE CONTRACT / SUPERSEDED IN PART` | two Human Gates, temporal/Profile model; edition-wide implementation pin to be corrected by WU-012C |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | source for the agent/tool Issue Prevention Checklist |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE HISTORICAL CORPUS EVIDENCE` | all fifteen completed Specials and repair interactions |
| `docs/survey-production-core-v2-minimum-vertical-slice*.md` | `ACTIVE HISTORICAL PHASE-3 EVIDENCE` | first-slice reasoning; orchestration details may be simplified by WU-012 |
| `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md` | `AUTHORITATIVE HISTORICAL INTEGRATED AUDIT` | originating cross-cutting findings |
| `docs/survey-production-core-v2-wu011-second-audit-closure.md` | `AUTHORITATIVE HISTORICAL WU-011 EXIT` | exact publication/release/bootstrap evidence; not final approval authority |
| `docs/survey-production-core-v2-session-bootstrap.md` | `PRE-PILOT OPERATIONS / REQUIRES WU-012 REVISION` | current W33/SP001 procedure; external Pilot use remains disabled |
| `docs/generative-ai-foundations-special-series.md` | `ACTIVE LIVING SERIES RESEARCH AUTHORITY` | sufficient initial Series-layer guidance; no machine Series engine required pre-merge |
| `docs/checkpoints/survey-production-core-v2-audit-findings/` | `ACTIVE MACHINE-READABLE AUDIT EVIDENCE` | Findings/Repair Sets; current status normalized below |

## 5. What ChatGPT owns vs what tools own

### 5.1 ChatGPT reasoning/editorial authority

ChatGPT owns open-ended decisions including:

- Source Intake/search strategy and expansion;
- source-quality and gap-fill decisions;
- research completeness/materiality judgment;
- semantic Screening/Evidence interpretation;
- Candidate Selection and Architecture;
- drafting and synthesis;
- historical attribution and significance;
- Weekly `why this week`, Watchlist and Late Breaking semantics;
- editorial quality review;
- visual/layout judgment of the rendered issue;
- classification/generalization of new findings.

Structured records should make these decisions resumable and reviewable. They do not need to be converted into deterministic algorithms.

### 5.2 Deterministic tool authority

Tools own or assist work where deterministic execution is materially safer or cheaper:

- issue/date/window calculation;
- bootstrap path/branch/profile construction;
- schema and structural validation;
- Raw hashes/immutability/provenance;
- exact IDs/paths/URLs/source refs;
- missing/duplicate/disposition accounting;
- targeted period-label checks;
- bibliography/render/build/preflight;
- deterministic historical regression checks;
- exact Publication Preview/PDF/Freeze/Release identity;
- GitHub Release side effects/reconciliation.

### 5.3 Human authority

Normal Human Gates remain exactly:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`.

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not additional routine Human Gates. Exception Gate is only for a genuine unresolved editorial/publication/compatibility decision.

## 6. Core/Profile principles retained

1. `shared file format != shared semantic Core`.
2. Weekly semantics remain Weekly/Profile-owned.
3. bounded-period semantics remain Period/Profile-owned.
4. Thematic research scope/lineage semantics remain Thematic/Profile-owned.
5. Publication-format/layout rules remain Publication Profile-owned.
6. The Foundations living series memo is outer research guidance; do not force it into per-volume Core state.
7. Frozen historical releases remain immutable.
8. W33 is a first real Weekly validation, not a design template.
9. SP001 is a first real Thematic validation, not a design template.
10. W33/SP001-specific editorial scope must not leak into generic Core code.

## 7. Provenance principles retained and corrected

Retain:

- immutable accepted Raw bytes;
- exact artifact/source hashes where useful;
- exact reviewed Architecture and Publication Preview identities;
- subject/entity binding;
- material-discovery disposition traceability;
- exact publication/release byte chain;
- explicit Human approval records;
- exact Release reconciliation/idempotency.

Correct during WU-012:

- **do not lock the whole edition to one initialization implementation commit**;
- record implementation/tool basis per checkpoint/action;
- permit a later stage to use newer reviewed `main` tooling;
- revalidate/migrate only affected accepted artifact boundaries when contracts change;
- use Exception Gate only when safe compatibility cannot be determined.

Provenance answers “what produced/validated this artifact?” It does not require that all later work use the same tool commit.

## 8. Orchestration correction

The current WU-010R/WU-011 local path over-serializes every stage as:

```text
Action Spec
-> Handoff Request
-> Handoff
-> Action Result
-> Validation Attestation
-> State transition
```

WU-012 must simplify normal local/model-assisted work toward:

```text
ChatGPT reads Profile + State + applicable guidance
-> produces canonical stage artifacts
-> runs only applicable deterministic checks
-> records compact checkpoint provenance/status
-> continues
```

Richer request/receipt machinery remains justified for meaningful external/asynchronous/irreversible boundaries, especially build artifacts and Release.

The objective is resumability and safety, not maximizing control records.

## 9. Historical Issue recurrence model

Every material historical defect family must be owned by one primary prevention/inspection mode:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

A crisp deterministic defect should not rely on agent memory when a small reliable validator exists. Conversely, a semantic or visual judgment should not be forced into a brittle validator merely to claim automation.

`docs/survey-production-core-v2-historical-invariants.md` is the source corpus for the WU-012 Issue Prevention Checklist.

## 10. Corrected finding status

### WU-010R / WU-011 historical repairs

AUD-013 through AUD-026 remain historical `FIXED_GENERIC` findings governed by their existing Repair Sets. WU-012 may simplify or supersede some implementation mechanisms without invalidating the defect lessons they captured.

In particular, WU-012 is allowed to replace State-pinned implementation/Handoff mechanics so long as the underlying provenance/resume/human-approval safety requirement remains satisfied by a simpler design.

### WU-012 findings

| Finding | Status | Current meaning |
|---|---|---|
| AUD-027 | `OPEN` | Completeness requires an explicit substantive ChatGPT research-review contract, not external proof of every search |
| AUD-028 | `OPEN` | Weekly Issue #9 must become a mandatory agent editorial review/checklist |
| AUD-029 | `OPEN` | quality must distinguish deterministic vs agent semantic/visual review and Profile applicability |
| AUD-030 | `OPEN` | lightweight generic Retrospective Period bootstrap/profile helper is missing |
| AUD-031 | `DEFERRED` | machine Series engine is premature; living Foundations memo is sufficient initial authority |
| AUD-032 | `OPEN` | SP001 Pilot scope is duplicated/narrowed instead of referencing TS-001 canonical planning authority |
| AUD-033 | `DEFERRED` | exhaustive synthetic future-edition fixture matrix is unnecessary; use small structural tests + real Pilots |
| AUD-034 | `OPEN` | one concise agent/tool/Human Issue Prevention Checklist is missing |
| AUD-035 | `OPEN` | ChatGPT operator model is insufficiently explicit and local stages are over-serialized |
| AUD-036 | `OPEN` | edition-wide implementation commit pin blocks controlled toolchain evolution |

No WU-012 Repair Set exists yet.

## 11. Corrected WU-012 scope

The authoritative detailed scope is `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`:

- **WU-012A:** establish ChatGPT-first operating contract;
- **WU-012B:** simplify local orchestration/control records;
- **WU-012C:** per-checkpoint implementation provenance + controlled toolchain upgrade/revalidation;
- **WU-012D:** stage/profile-aware Issue Prevention Checklist;
- **WU-012E:** lightweight Period bootstrap and Thematic planning-authority references; only small structural genericity tests;
- **WU-012F:** quality tiers `DETERMINISTIC / AGENT_SEMANTIC / AGENT_VISUAL`.

Do not implement the superseded full machine Series engine or exhaustive synthetic edition matrix before merge.

## 12. Current stop rule

PR #310 remains draft and unmerged. W33, W34, SP001, SP002 and SP003 remain unstarted.

Before requesting Human full-candidate approval again:

1. implement corrected WU-012A–F;
2. preserve immutable Raw and exact publication/release authority;
3. keep exactly two normal Human Gates;
4. run deterministic regression only for deterministic retained behavior;
5. re-audit the whole candidate against Weekly viability, Special viability, generality, Issue recurrence prevention and over-validation risk;
6. synchronize `AGENTS.md`, bootstrap guidance, plan/worklog/PR review package;
7. stop at Human full-candidate review.

Only after explicit approval and merge to `main` may external W33/SP001 production validation begin.
