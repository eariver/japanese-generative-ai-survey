# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY / WU-012 IMPLEMENTED / HUMAN FULL-CANDIDATE REVIEW`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
WU-012 closure: `docs/survey-production-core-v2-wu012-preapproval-closure.md`

## 1. Purpose

This index identifies the live semantic authority for Survey Production Core v2 while preserving earlier design/audit documents as historical reasoning.

Current `main` remains the production source of truth until PR #310 is explicitly Human-reviewed and merged. This file is authoritative for work on the improvement branch only until that merge.

The 2026-08-22 ChatGPT-first re-audit corrected a material premise mismatch in the first WU-012 audit. Where older documents require stronger machine/external-workflow authority than this index or the ChatGPT-first re-audit, the newer ChatGPT-first authority controls.

## 2. Fundamental operating model

**ChatGPT is the primary research/editorial operator.**

Normal production is:

```text
user supplies target + requested stopping Human Gate
-> ChatGPT reads current repository policy/Profile/State
-> ChatGPT performs research/editorial reasoning
-> deterministic helpers perform repetitive/crisp/provenance-sensitive work
-> canonical stage artifacts are produced
-> one compact Stage Checkpoint binds exact stage artifacts + review/tool/contract provenance
-> ChatGPT continues autonomously
-> stop only at the requested Human Gate or a genuine Exception Gate
```

Scripts, schemas and GitHub workflows support this work. They are not the editorial intelligence and must not replace qualitative reasoning with ceremonial machine state.

## 3. Authority precedence

For Survey Production Core v2 improvement work, use:

```text
1. repository reality
2. this authority index
3. docs/survey-production-core-v2-wu012-preapproval-closure.md
4. docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md
5. docs/checkpoints/survey-production-core-v2-worklog.md for current status/next action
6. docs/survey-production-core-v2-improvement-plan.md
7. whole-system audit + explicit remediation status
8. WU-011 second-audit closure / earlier audit amendments
9. historical/current-main implementation docs used as evidence
```

Older machine-first WU-012 language is superseded where it conflicts with this index, the closure document, or the ChatGPT-first re-audit.

## 4. Current document map

| Document | Current status | Role |
|---|---|---|
| `docs/survey-production-core-v2-wu012-preapproval-closure.md` | `AUTHORITATIVE WU-012 PRE-MERGE CLOSURE` | acceptance-priority verdict, final audit, merge boundary |
| `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md` | `AUTHORITATIVE OPERATOR-MODEL RE-AUDIT` | corrected operator/tool boundary and WU-012 scope |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL WORK STATUS` | current WU status, validation evidence and exact next action |
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE CONSOLIDATED PLAN / WU-012 IMPLEMENTED` | overall architecture, rationale and rollout |
| `docs/survey-production-core-v2-issue-prevention-checklist.md` | `CANONICAL PRODUCTION PREVENTION CHECKLIST` | historical Issue recurrence ownership |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | historical prevention source corpus |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE HISTORICAL CORPUS EVIDENCE` | completed Special corpus and repair interactions |
| `docs/survey-production-core-v2-session-bootstrap.md` | `CANONICAL AGENT-FIRST SESSION BOOTSTRAP` | short-request start/resume behavior |
| `docs/generative-ai-foundations-special-series.md` | `ACTIVE LIVING SERIES RESEARCH AUTHORITY` | outer Series guidance; no machine Series engine required pre-merge |
| `docs/checkpoints/survey-production-core-v2-audit-findings/` | `ACTIVE MACHINE-READABLE AUDIT EVIDENCE` | Findings/Repair Sets |

## 5. Responsibility boundaries

### 5.1 ChatGPT owns

- Source Intake/search strategy and expansion;
- source-quality and gap-fill decisions;
- research completeness/materiality judgment;
- semantic Screening/Evidence interpretation;
- Candidate Selection and Architecture;
- drafting and synthesis;
- historical attribution and significance;
- Weekly `why this week`, Watchlist, Late Breaking and carry-over semantics;
- editorial quality review;
- visual/layout judgment of the rendered issue;
- classification/generalization of new findings.

Structured records make these decisions resumable and reviewable; they do not turn them into deterministic truth claims.

### 5.2 Deterministic tools own or assist

- issue/date/window calculation;
- bootstrap path/branch/profile construction;
- schema and structural validation;
- Raw hashes/immutability/provenance;
- exact IDs/paths/URLs/source refs;
- missing/duplicate/disposition accounting;
- subject/entity/property binding;
- targeted period-label checks;
- bibliography/render/build/preflight;
- deterministic historical regression checks;
- lifecycle-specific exact artifact binding in compact checkpoints;
- exact Publication Preview/PDF/Freeze/Release identity;
- GitHub Release side effects/reconciliation.

### 5.3 Humans own exactly two normal gates

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not additional routine Human Gates.

Exception Gate is used only when a genuine unresolved editorial/publication/compatibility decision cannot be derived safely from repository authority. Retryable deterministic failures and normal reviewed tool upgrades are not Exception Gates.

## 6. Core/Profile principles

1. `shared file format != shared semantic Core`.
2. Weekly semantics remain Weekly/Profile-owned.
3. bounded-period semantics remain Period/Profile-owned.
4. Thematic research scope/lineage semantics remain Thematic/Profile-owned.
5. Publication-format/layout rules remain Publication Profile-owned.
6. Foundations uses the living series memo as outer research authority; do not force it into per-volume Core state before demonstrated need.
7. Frozen historical releases remain immutable.
8. W33 is a first real Weekly validation, not a design template.
9. SP001 is a first real Thematic validation, not a design template.
10. W33/SP001-specific editorial scope must not leak into generic Core code.

## 7. Provenance model

Retain:

- immutable accepted Raw bytes;
- exact accepted research artifact authority where used;
- subject/entity binding and material-discovery disposition traceability;
- exact reviewed Architecture identity;
- exact Publication Preview/Freeze/Release byte chain;
- explicit Human approval records;
- exact Release reconciliation/idempotency.

Corrected by WU-012:

- initialization implementation identity remains historical provenance, not an edition-wide execution lock;
- every material checkpoint records actual implementation/tool and current contract basis;
- newer reviewed generic tooling may be adopted later in the edition;
- changed contracts require targeted revalidation/migration of affected boundaries;
- compatibility ambiguity fails closed and may require an Exception Gate;
- compact local checkpoints must bind the canonical logical artifacts establishing each lifecycle transition.

## 8. Canonical orchestration model

Normal local/model-assisted production is:

```text
Profile + Production State + applicable guidance
-> ChatGPT research/editorial work
-> canonical stage artifacts
-> applicable deterministic and/or ChatGPT review
-> compact Stage Checkpoint with exact artifact SHA + implementation/contract basis
-> State transition
```

Canonical `config/survey-production-v2.json` sets every `stage_plan[*].handoff_required=false`. The legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery remains historical/compatibility material, not canonical local production authority. Compatibility fixtures may explicitly opt into Handoff behavior only when exercising that legacy path.

Richer request/receipt/reconciliation machinery remains justified at external asynchronous or irreversible boundaries, especially public Release.

## 9. Historical Issue recurrence model

Every material recurring defect family has a primary owner:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

Deterministic recurrent issues should not depend on reviewer memory when a small reliable validator exists. Semantic/visual judgment should not be converted into brittle global automation merely to claim coverage.

`docs/survey-production-core-v2-issue-prevention-checklist.md` is the production-facing authority; the historical invariant/deep-audit corpus provides its evidence base.

## 10. WU-012 finding disposition

Generic repairs:

- AUD-027 `FIXED_GENERIC`
- AUD-028 `FIXED_GENERIC`
- AUD-029 `FIXED_GENERIC`
- AUD-030 `FIXED_GENERIC`
- AUD-032 `FIXED_GENERIC`
- AUD-034 `FIXED_GENERIC`
- AUD-035 `FIXED_GENERIC`
- AUD-036 `FIXED_GENERIC`
- AUD-037 `FIXED_GENERIC`
- AUD-038 `FIXED_GENERIC`

Intentional deferrals:

- AUD-031 `DEFERRED` — machine Series engine is premature; living Foundations authority is sufficient to start real work.
- AUD-033 `DEFERRED` — exhaustive synthetic future-edition fixture matrix is unnecessary; small structural tests + real Pilots are the chosen evidence strategy.

Repair Set `REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, until real W33/SP001 verification editions exist.

## 11. Pre-merge validation evidence

Semantic implementation head `1d6e37f48cd24ce96ef7970df0e70697e546f2e3` passed all five required validation families:

| Validation family | Result | Run |
|---|---|---|
| Survey Production Core v2 CI | PASS | `32568620742` |
| Screening contract CI | PASS | `32568620692` |
| Evidence contract CI | PASS | `32568620743` |
| Pipeline contract tests | PASS | `32568620721` |
| Weekly pipeline spine + committed Raw integrity | PASS | `32568620741` |

The final config/docs/test synchronization head must also remain CI-green before the review package is considered synchronized.

## 12. Current stop rule

PR #310 remains draft and unmerged. W33, W34, SP001, SP002 and SP003 remain unstarted.

**Current action: Human full-candidate review of PR #310 after final synchronized-head CI is green.**

Do not perform more architectural expansion before Human review unless synchronization reveals a concrete defect.

Do not start any Pilot before explicit Human approval and merge.

If approved:

```text
merge PR #310 to main
-> merged main becomes production source of truth
-> start real W33 and SP001 validation
-> record production findings
-> repair only the narrowest correct layer
-> continue W34 and SP002/SP003 as second-round generalization evidence
```

If Human review finds a defect, record a Finding and reopen repair work before merge.
