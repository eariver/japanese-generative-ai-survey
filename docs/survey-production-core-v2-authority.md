# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY / WU-012 + AUD-046 REPAIRS IMPLEMENTED / PRE-AUDIT CANDIDATE`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Purpose

This index identifies the live semantic authority for Survey Production Core v2 while preserving earlier design/audit documents as historical reasoning.

Current `main` remains the production source of truth until PR #310 is explicitly Human-reviewed and merged. This file is authoritative for work on the improvement branch only until that merge.

The 2026-08-22 ChatGPT-first re-audit corrected a material premise mismatch in the first WU-012 audit. A later post-completion audit of former review head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` found AUD-039 through AUD-044. The first subsequent fixed-head final-audit attempt at `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` found AUD-045: this Authority still described those repairs as in progress even though the Worklog and Repair Set already described them as implemented. That audit was therefore invalidated before completion.

A later exact-head audit at `705937af2eb45d5ba361fe748d7a622110bcb27c` completed all five acceptance points, but the Owner then clarified an original production requirement that the audit had not modeled: Weekly must incorporate X through a Grok Source Intake lane, and Specials must be able to use targeted X collection when material. Grok results are handed back through the user-provided Google Drive root `Grok_X_SourseIntake`. This requirement is AUD-046. Because it required candidate-tree changes, the `705937af...` audit is invalidated as final approval evidence under the post-completion audit rule.

The candidate tree intentionally stops at an **audit-stable pre-audit state**. It records that generic repairs are implemented and that exact-head CI/five-point final-audit evidence must be recorded outside the candidate tree in PR/Human-review metadata. This avoids changing the audited SHA merely to commit a PASS result.

## 2. Fundamental operating model

**ChatGPT is the primary research/editorial operator.**

Normal production is:

```text
user supplies target + requested stopping Human Gate
-> ChatGPT reads current repository policy/Profile/State
-> ChatGPT performs research/editorial reasoning
-> Source Intake uses conventional collectors + direct research + applicable Grok/X external collection
-> deterministic helpers perform repetitive/crisp/provenance-sensitive work
-> canonical stage artifacts are produced
-> deterministic stage-contract validation verifies exact semantic artifact authority
-> one compact Stage Checkpoint binds exact stage artifacts + review/tool/contract provenance
-> ChatGPT continues autonomously
-> stop only at the requested Human Gate or a genuine Exception Gate
```

Scripts, schemas and GitHub workflows support this work. They are not the editorial intelligence and must not replace qualitative reasoning with ceremonial machine state.

Grok/X is an external Source Intake sensor, not an additional editorial authority and not a third Human Gate. Grok observes X; ChatGPT defines the research task, provisions the Drive handoff, imports exact returned bytes into repository Raw, interprets the observations, performs authoritative gap-fill, and decides how those observations affect Discovery/Evidence.

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
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE CONSOLIDATED PLAN / REPAIRS IMPLEMENTED` | overall architecture, rationale and rollout |
| `docs/survey-production-core-v2-issue-prevention-checklist.md` | `CANONICAL PRODUCTION PREVENTION CHECKLIST` | historical Issue recurrence and X-intake boundary ownership |
| `docs/survey-production-core-v2-x-source-intake.md` | `CANONICAL EXTERNAL SOURCE INTAKE SUBFLOW` | Grok/X applicability, Google Drive handoff, Raw import and Discovery disposition |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | historical prevention source corpus |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE HISTORICAL CORPUS EVIDENCE` | completed Special corpus and repair interactions |
| `docs/survey-production-core-v2-session-bootstrap.md` | `CANONICAL AGENT-FIRST SESSION BOOTSTRAP` | short-request start/resume behavior |
| `docs/generative-ai-foundations-special-series.md` | `ACTIVE LIVING SERIES RESEARCH AUTHORITY` | outer Series guidance; no machine Series engine required pre-merge |
| `docs/checkpoints/survey-production-core-v2-audit-findings/` | `ACTIVE MACHINE-READABLE AUDIT EVIDENCE` | Findings/Repair Sets |

## 5. Responsibility boundaries

### 5.1 ChatGPT owns

- Source Intake/search strategy and expansion;
- deciding X/Grok applicability where the Profile permits judgment;
- defining run-specific Grok research questions, coverage focus and time scope;
- creating Grok instruction/prompt and provisioning the exact Google Drive run folder;
- reading returned Grok Drive Markdown, importing its exact bytes into repository Raw and deciding Discovery/no-material disposition;
- authoritative-source gap-fill for X-origin leads before technical claims enter Evidence;
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

### 5.2 Grok owns

- X-native search/observation for the exact run-specific research task;
- reporting representative X posts, community signal, counter-signal and candidate primary-source locators;
- writing the final Raw Observation Markdown only into the instructed Google Drive run folder.

Grok does not write to GitHub and is not the publication-grade authority for model specifications, benchmark values, dates, license terms or historical priority.

### 5.3 Deterministic tools own or assist

- issue/date/window calculation;
- bootstrap path/branch/profile construction;
- schema and structural validation;
- X Source Intake manifest/Profile policy validation;
- exact Grok instruction/prompt authority and imported Raw hashes/byte counts;
- X-run completion and Discovery/no-material-disposition accounting;
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

GitHub Actions does not need access to the private Google Drive folder. ChatGPT performs the account-specific Drive handoff through the connected Drive capability; repository/CI validates the imported bytes and stable path-level contract.

### 5.4 Humans own exactly two normal production gates

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not additional routine Human Gates.

If no automated Grok execution integration exists, the Human may act as transport/operator by giving Grok the generated instruction/prompt. That operational handoff is not editorial approval and does not create a third Gate.

Exception Gate is used only when a genuine unresolved editorial/publication/compatibility decision cannot be derived safely from repository authority. Retryable deterministic failures, ordinary Grok result transport and normal reviewed tool upgrades are not Exception Gates.

The Core-v2 post-completion five-point audit is a **change-management acceptance rule**, not a third edition Human Gate.

## 6. Core/Profile principles

1. `shared file format != shared semantic Core`.
2. Weekly semantics remain Weekly/Profile-owned.
3. bounded-period semantics remain Period/Profile-owned.
4. Thematic research scope/lineage semantics remain Thematic/Profile-owned.
5. Publication-format/layout rules remain Publication Profile-owned.
6. Weekly Grok/X Source Intake is required by Profile; a quiet X week may yield no material Discovery, but the scan cannot be silently skipped.
7. Retrospective Period and Thematic X applicability is an explicit ChatGPT research decision with rationale; silence is not `NOT_REQUIRED`.
8. Foundations uses the living series memo as outer research authority; its volumes use the Thematic Profile and a dedicated `Generative_AI_Foundations` Drive category when X is material.
9. X/Grok is Discovery/community-signal input, not direct technical Evidence authority.
10. Frozen historical releases remain immutable.
11. W33 is a first real Weekly validation, not a design template.
12. SP001 is a first real Thematic validation, not a design template.
13. W33/SP001-specific editorial scope must not leak into generic Core code.
14. Retrospective Period may use an internal `SP-...` source identity while public release slug/tag/title/asset identity comes from the exact Production Profile `survey_root` authority.
15. A bounded Retrospective Period cannot initialize before its configured period end.

## 7. X/Grok Source Intake and Google Drive handoff

The configured root folder name is exactly:

`Grok_X_SourseIntake`

Repository authority records only stable folder-name path semantics. Account-specific Drive folder IDs/URLs are resolved at runtime and are not committed.

Persistent categories are:

```text
Weekly
Retrospective_Special
Thematic_Special
Generative_AI_Foundations
```

Each required run uses:

```text
Grok_X_SourseIntake/<category>/<edition-folder>/<run-id>/
```

Canonical Source Intake behavior is:

```text
ChatGPT decides/derives X applicability
-> defines one or more run-specific research tasks
-> renders exact Grok instruction + prompt
-> provisions exact Drive run folder
-> Grok observes X and writes Markdown only there
-> ChatGPT reads the returned Drive file
-> imports exact bytes into repository Raw
-> maps material signal to Discovery OR records NO_MATERIAL_DISCOVERY
-> Discovery Acceptance binds the completed X manifest SHA
-> continue through normal Screening/Evidence/Completeness
```

`AWAITING_GROK` is incomplete Source Intake, not a Production State terminal reason. If the Drive result already exists, ChatGPT imports it and continues. If it is absent and manual transport is required, report the exact prompt/instruction and Drive path without pretending Human approval is required.

## 8. Provenance and toolchain-evolution model

Retain:

- immutable accepted Raw bytes, including exact Grok Drive results after repository import;
- exact X manifest/instruction/prompt/result provenance where X is used;
- exact accepted research artifact authority where used;
- subject/entity binding and material-discovery disposition traceability;
- exact reviewed Architecture identity;
- exact Production Profile binding for quality applicability;
- exact Publication Preview/Freeze/Release byte chain;
- explicit Human approval records;
- exact Release reconciliation/idempotency.

Corrected by WU-012 and the post-completion re-audits:

- initialization implementation identity remains historical provenance, not an edition-wide execution lock;
- every material checkpoint records actual implementation/tool and current contract basis;
- newer reviewed generic tooling may be adopted later in the edition;
- a reviewed `main` repair is first integrated into the edition work branch; the integrated branch head is the execution identity recorded by the checkpoint;
- `scripts/survey_agent_tool_v2.py` provides the narrow agent-first runtime bridge for legacy Screening/Evidence helpers that still carry historical pin checks internally;
- accepted boundaries affected by a tool/schema change are revalidated or migrated selectively rather than replaying unrelated stages;
- compatibility ambiguity fails closed and may require an Exception Gate;
- compact local checkpoints must carry a `CORE_STAGE_CONTRACT` deterministic result that binds exact State/Profile/current-tool/current-contract/artifact authority;
- Discovery Acceptance transitively binds exact completed X Source Intake manifest/imported Raw authority;
- a same-named file is never sufficient proof of stage validity.

Do not run an unintegrated second checkout of `main` against edition artifacts and then claim the edition work branch itself contained that toolchain.

## 9. Canonical orchestration model

Normal local/model-assisted production is:

```text
Profile + Production State + applicable guidance
-> ChatGPT research/editorial work
-> conventional/direct/Grok Source Intake as applicable
-> canonical stage artifacts
-> scripts/survey_stage_validation_v2.py over the exact intended stage artifacts
-> applicable ChatGPT research/editorial/visual review
-> compact Stage Checkpoint with exact artifact SHA + CORE_STAGE_CONTRACT + implementation/contract basis
-> State transition
```

Canonical `config/survey-production-v2.json` sets every `stage_plan[*].handoff_required=false`. The legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery remains historical/compatibility material, not canonical local production authority. Compatibility fixtures may explicitly opt into Handoff behavior only when exercising that legacy path.

The Grok/Drive exchange is an external collection transport, not a resurrection of the legacy local Handoff chain. Richer request/receipt/reconciliation machinery remains justified at truly irreversible external boundaries, especially public Release.

## 10. Historical Issue recurrence model

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

`docs/survey-production-core-v2-issue-prevention-checklist.md` is the production-facing authority; the historical invariant/deep-audit corpus provides its evidence base. AUD-046 adds the explicit X applicability/evidence-boundary/result-disposition family.

## 11. WU-012 finding disposition

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
- AUD-046 `FIXED_GENERIC` — formal Grok/X Source Intake, Google Drive handoff, Profile applicability and Discovery disposition

Intentional deferrals remain:

- AUD-031 `DEFERRED` — machine Series engine is premature; living Foundations authority is sufficient to start real work.
- AUD-033 `DEFERRED` — exhaustive synthetic future-edition fixture matrix is unnecessary; small structural tests + real Pilots are the chosen evidence strategy.

Repair Set `REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, until real W33/SP001 verification editions exist.

## 12. Pre-audit validation boundary

Earlier green/audited heads remain historical evidence only. In particular:

- `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` was invalidated by AUD-039 through AUD-044;
- `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` was invalidated by AUD-045;
- `705937af2eb45d5ba361fe748d7a622110bcb27c` was invalidated by AUD-046 after the Owner clarified the required X/Grok Source Intake architecture.

No PASS verdict from those candidates may substitute for the next all-changes-complete fixed-head audit.

This candidate tree deliberately does **not** commit a final exact-head PASS. The required external validation sequence is:

1. all five cross-regression families pass on one unchanged candidate head;
2. that exact head is frozen for review;
3. Weekly viability, Special viability, generality, historical Issue recurrence prevention, and control proportionality are audited from zero in order, including the X/Grok/Drive Source Intake behavior;
4. any candidate-tree mutation invalidates the entire audit;
5. an unchanged all-PASS result is recorded in PR/Human-review metadata with exact head SHA and CI run IDs.

The five required cross-regression families are:

1. Survey Production Core v2 CI;
2. Screening contract CI;
3. Evidence contract CI;
4. Pipeline contract tests;
5. Weekly pipeline spine + committed Raw integrity.

## 13. Pre-audit handoff and production boundary

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
