# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY / WU-012 REPAIRS IMPLEMENTED / PRE-AUDIT CANDIDATE`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Purpose

This index identifies the live semantic authority for Survey Production Core v2 while preserving earlier design/audit documents as historical reasoning.

Current `main` remains the production source of truth until PR #310 is explicitly Human-reviewed and merged. This file is authoritative for work on the improvement branch only until that merge.

The 2026-08-22 ChatGPT-first re-audit corrected a material premise mismatch in the first WU-012 audit. A later post-completion audit of former review head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` found AUD-039 through AUD-044. The first subsequent fixed-head final-audit attempt at `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` found AUD-045: this Authority still described those repairs as in progress even though the Worklog and Repair Set already described them as implemented. That audit was therefore invalidated before completion.

The candidate tree intentionally stops at an **audit-stable pre-audit state**. It records that generic repairs are implemented and that exact-head CI/five-point final-audit evidence must be recorded outside the candidate tree in PR/Human-review metadata. This avoids changing the audited SHA merely to commit a PASS result.

## 2. Fundamental operating model

**ChatGPT is the primary research/editorial operator.**

Normal production is:

```text
user supplies target + requested stopping Human Gate
-> ChatGPT reads current repository policy/Profile/State
-> ChatGPT performs research/editorial reasoning
-> deterministic helpers perform repetitive/crisp/provenance-sensitive work
-> canonical stage artifacts are produced
-> deterministic stage-contract validation verifies exact semantic artifact authority
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
3. docs/survey-production-core-v2-final-audit-rule.md
4. docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md
5. docs/checkpoints/survey-production-core-v2-worklog.md for pre-audit implementation status
6. docs/survey-production-core-v2-improvement-plan.md
7. whole-system audit + explicit remediation status
8. WU-011 second-audit closure / earlier audit amendments
9. historical/current-main implementation docs used as evidence
```

`docs/survey-production-core-v2-wu012-preapproval-closure.md` remains historical evidence of an earlier candidate state. Its final-PASS conclusion is invalidated by later candidate changes/findings and is not current approval authority.

The **post-freeze final result** is not a candidate-tree document. Under `docs/survey-production-core-v2-final-audit-rule.md`, PR/Human-review metadata names the exact audited head SHA and CI runs. That external record may move the candidate from pre-audit to Human full-candidate review without mutating the audited tree.

## 4. Current document map

| Document | Current status | Role |
|---|---|---|
| `docs/survey-production-core-v2-final-audit-rule.md` | `CANONICAL PRE-MERGE REVIEW RULE` | all-changes-first/fixed-head five-point audit and invalidation semantics |
| `docs/survey-production-core-v2-wu012-preapproval-closure.md` | `HISTORICAL / PREVIOUS AUDIT INVALIDATED` | evidence for a former candidate; not current merge authority |
| `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md` | `AUTHORITATIVE OPERATOR-MODEL RE-AUDIT` | corrected operator/tool boundary and WU-012 scope |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL PRE-AUDIT WORK STATUS` | implemented repairs and required external final-validation handoff |
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE CONSOLIDATED PLAN / WU-012 REPAIRS IMPLEMENTED` | overall architecture, rationale and rollout |
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
- lifecycle-specific exact semantic artifact validation before compact checkpoint adoption;
- exact Production Profile/source/PDF quality binding;
- exact Publication Preview/PDF/Freeze/Release identity;
- GitHub Release side effects/reconciliation.

### 5.3 Humans own exactly two normal production gates

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not additional routine Human Gates.

Exception Gate is used only when a genuine unresolved editorial/publication/compatibility decision cannot be derived safely from repository authority. Retryable deterministic failures and normal reviewed tool upgrades are not Exception Gates.

The Core-v2 post-completion five-point audit is a **change-management acceptance rule**, not a third edition Human Gate.

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
11. Retrospective Period may use an internal `SP-...` source identity while public release slug/tag/title/asset identity comes from the exact Production Profile `survey_root` authority.
12. A bounded Retrospective Period cannot initialize before its configured period end.

## 7. Provenance and toolchain-evolution model

Retain:

- immutable accepted Raw bytes;
- exact accepted research artifact authority where used;
- subject/entity binding and material-discovery disposition traceability;
- exact reviewed Architecture identity;
- exact Production Profile binding for quality applicability;
- exact Publication Preview/Freeze/Release byte chain;
- explicit Human approval records;
- exact Release reconciliation/idempotency.

Corrected by WU-012 and the post-completion re-audit:

- initialization implementation identity remains historical provenance, not an edition-wide execution lock;
- every material checkpoint records actual implementation/tool and current contract basis;
- newer reviewed generic tooling may be adopted later in the edition;
- a reviewed `main` repair is first integrated into the edition work branch; the integrated branch head is the execution identity recorded by the checkpoint;
- `scripts/survey_agent_tool_v2.py` provides the narrow agent-first runtime bridge for legacy Screening/Evidence helpers that still carry historical pin checks internally;
- accepted boundaries affected by a tool/schema change are revalidated or migrated selectively rather than replaying unrelated stages;
- compatibility ambiguity fails closed and may require an Exception Gate;
- compact local checkpoints must carry a `CORE_STAGE_CONTRACT` deterministic result that binds exact State/Profile/current-tool/current-contract/artifact authority;
- a same-named file is never sufficient proof of stage validity.

Do not run an unintegrated second checkout of `main` against edition artifacts and then claim the edition work branch itself contained that toolchain.

## 8. Canonical orchestration model

Normal local/model-assisted production is:

```text
Profile + Production State + applicable guidance
-> ChatGPT research/editorial work
-> canonical stage artifacts
-> scripts/survey_stage_validation_v2.py over the exact intended stage artifacts
-> applicable ChatGPT research/editorial/visual review
-> compact Stage Checkpoint with exact artifact SHA + CORE_STAGE_CONTRACT + implementation/contract basis
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

Generic repairs implemented in the pre-audit candidate:

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
- AUD-039 `FIXED_GENERIC` — compact checkpoint semantic stage authority
- AUD-040 `FIXED_GENERIC` — practical reviewed-tool adoption after initialization
- AUD-041 `FIXED_GENERIC` — all-changes-first fixed-head final-audit rule
- AUD-042 `FIXED_GENERIC` — exact Production Profile-bound Quality applicability
- AUD-043 `FIXED_GENERIC` — Retrospective Period public release identity
- AUD-044 `FIXED_GENERIC` — bounded Period completion guard
- AUD-045 `FIXED_GENERIC` — canonical pre-audit status synchronization and audit-stable result handoff wording

Intentional deferrals remain:

- AUD-031 `DEFERRED` — machine Series engine is premature; living Foundations authority is sufficient to start real work.
- AUD-033 `DEFERRED` — exhaustive synthetic future-edition fixture matrix is unnecessary; small structural tests + real Pilots are the chosen evidence strategy.

Repair Set `REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, until real W33/SP001 verification editions exist.

## 11. Pre-audit validation boundary

Earlier green heads remain historical evidence only. In particular, former synchronized head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` is not current final-review evidence, and fixed-head attempt `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` was invalidated by AUD-045.

This candidate tree deliberately does **not** commit a final exact-head PASS. The required external validation sequence is:

1. all five cross-regression families pass on one unchanged candidate head;
2. that exact head is frozen for review;
3. Weekly viability, Special viability, generality, historical Issue recurrence prevention, and control proportionality are audited from zero in order;
4. any candidate-tree mutation invalidates the entire audit;
5. an unchanged all-PASS result is recorded in PR/Human-review metadata with exact head SHA and CI run IDs.

The five required cross-regression families are:

1. Survey Production Core v2 CI;
2. Screening contract CI;
3. Evidence contract CI;
4. Pipeline contract tests;
5. Weekly pipeline spine + committed Raw integrity.

## 12. Pre-audit handoff and production boundary

PR #310 remains draft and unmerged. W33, W34, SP001, SP002 and SP003 remain unstarted.

The repository-side pre-audit handoff is complete only when this Authority, Worklog, Repair Set, implementation and tests agree. Once they do, freeze the exact branch head, obtain five-family green CI, and run the mandatory five-point audit without changing the candidate.

If any audit point requires a repository change:

```text
record/classify finding
-> audit INVALIDATED
-> repair + synchronize
-> rerun five-family CI
-> freeze new head
-> rerun all five acceptance points from point 1
```

If all five pass on an unchanged head, record that exact-SHA result in PR/Human-review metadata and present the candidate for Human full-candidate review. Do not commit a post-audit PASS document into the audited tree.

Do not start any Pilot before explicit Human approval and merge.
