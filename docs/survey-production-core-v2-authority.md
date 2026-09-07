# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL POST-INTEGRATION CORE AUTHORITY / SOL-LUNA REVIEW GOVERNANCE AMENDMENT / PRE-AUDIT CANDIDATE`
Established: 2026-08-22 JST  
Current maintenance branch: `fix/core-v2-sol-luna-review-governance-20260907`
Prior integration PR: `#484` — `Survey Production Core v2: pre-Human Evidence regeneration repair` — merged into `main`
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`
Mandatory research/review governance: `docs/survey-production-core-v2-sol-luna-review-governance.md`

## 1. Purpose and current boundary

This index identifies the live semantic authority for Survey Production Core v2 while preserving earlier design/audit documents as historical reasoning.

Current `main` is the production source of truth at `d54f9c7b3a7cef064c6701ab864daab27118cdce`, tree `b47b416f9520fd3a4f76769f8b8918f25893645c`, after Human-reviewed PR #484 integration. Earlier structural-recovery and pre-incident baselines remain historical execution evidence only. Repository reality outranks stale historical wording in older records.

The current maintenance branch is a separate shared-Core documentation/governance amendment. It does not modify an edition production branch and does not by itself authorize integration into `main`.

Historical candidate audits are not reusable as current approval evidence:

- `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` was invalidated by AUD-039 through AUD-044;
- `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` was invalidated by AUD-045;
- `705937af2eb45d5ba361fe748d7a622110bcb27c` completed the then-current five-point audit, but was invalidated by AUD-046 after the Owner clarified the required Grok/X Source Intake architecture;
- `c565a3254ad303bd276edee55b2b1e6e0a1c91a7` reached the pre-audit freeze boundary, but its subsequent audit was invalidated by a current-facing six-point wording contradiction in this authority; its CI/audit evidence is historical only and is not reusable for the replacement candidate;
- AUD-047 added autonomous progression / stop discipline as an independent acceptance dimension. The canonical final audit has since been fixed at seven points, with Human Gate round-trip viability as Point 7.

Any new Core candidate tree follows the same fixed-head audit invalidation discipline. Exact final PASS evidence belongs in PR/Human-review metadata keyed to one unchanged candidate SHA; do not mutate the candidate merely to record that PASS.

## 2. Fundamental operating model

**ChatGPT is the primary research/editorial operator.**

Within ChatGPT-operated production, the supervisory and execution roles are deliberately separated:

- the **Sol supervisor/reviewer role** owns research sufficiency, semantic authority consumption, materiality, Selection judgment, Architecture responsibility, and Human-facing review;
- the **Luna/Work execution role** owns bounded execution, bulk retrieval, exact-byte capture/provenance, normalization, task-local evidence work, deterministic regeneration, and delegated gap-fill execution.

The names describe current operating roles. If model/product names change, the semantic separation remains mandatory.

Normal production is:

```text
user supplies target + requested stopping Human Gate
-> ChatGPT reads repository authority/Profile/State
-> research execution + Source Intake
-> Sol Discovery completeness review
-> Screening / Evidence execution + iterative authority gap fill
-> Sol Evidence authority-consumption review
-> Sol materiality / Selection review
-> Architecture preparation under Sol-owned semantics
-> Sol Architecture review + Human-facing dossier
-> exact stage validation/checkpoint
-> Human ARCHITECTURE_REVIEW
```

The operating default is **continuous autonomous progression**. Source Intake, Screening, Evidence, Completeness/materiality, Selection, Architecture preparation, drafting/synthesis, deterministic QA, semantic/visual repair, CI retry, generic repair and ordinary Drive result import are not user decision points.

Mandatory Sol supervisory reviews are internal production quality controls, not additional Human Gates. Continuous progression does not authorize an execution agent to bypass them.

A production session may interrupt Human-facing progression only for:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`;
3. a genuine Owner-level Exception Gate that repository authority cannot safely resolve;
4. unavoidable manual Grok instruction/result transport when the external Grok execution itself cannot be crossed directly.

The fourth item is operational transport, not editorial approval and not another Human Gate. Once a valid Grok result is available in the configured Drive run folder, ChatGPT imports it and resumes automatically without another routine confirmation.

Scripts, schemas, execution agents and GitHub workflows support ChatGPT. They are not the editorial intelligence and must not replace qualitative reasoning with ceremonial machine state. `READY_FOR_ARCHITECTURE_REVIEW`, deterministic PASS, or Luna/Work completion are never sufficient by themselves for a Human approval recommendation.

## 3. Authority precedence

For Survey Production Core v2 improvement and production work, use:

```text
1. repository reality
2. this authority index
3. docs/survey-production-core-v2-sol-luna-review-governance.md
4. docs/survey-production-core-v2-final-audit-rule.md
5. docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md
6. docs/survey-production-core-v2-session-bootstrap.md
7. docs/survey-production-core-v2-issue-prevention-checklist.md
8. docs/checkpoints/survey-production-core-v2-worklog.md
9. docs/survey-production-core-v2-improvement-plan.md
10. whole-system audit + explicit remediation status
11. historical/current-main implementation docs used as evidence
```

`docs/survey-production-core-v2-wu012-preapproval-closure.md` remains historical evidence only. Its former PASS conclusion does not override later Findings.

## 4. Current document map

| Document | Current status | Role |
|---|---|---|
| `docs/survey-production-core-v2-sol-luna-review-governance.md` | `CANONICAL PRODUCTION GOVERNANCE` | Sol/Luna responsibility split, mandatory supervisory checkpoints, full Architecture Review dossier |
| `docs/survey-production-core-v2-final-audit-rule.md` | `CANONICAL PRE-MERGE REVIEW RULE` | all-changes-first/fixed-head seven-point audit and invalidation semantics |
| `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md` | `AUTHORITATIVE OPERATOR-MODEL RE-AUDIT` | corrected ChatGPT/tool boundary |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL PRE-AUDIT WORK STATUS` | implementation status and external final-validation handoff |
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE CONSOLIDATED PLAN / REPAIRS IMPLEMENTED` | architecture, rationale and rollout |
| `docs/survey-production-core-v2-session-bootstrap.md` | `CANONICAL AGENT-FIRST SESSION BOOTSTRAP` | short-request start/resume and autonomous progression |
| `docs/survey-production-core-v2-issue-prevention-checklist.md` | `CANONICAL PRODUCTION PREVENTION CHECKLIST` | recurring defect ownership and mandatory review checks |
| `docs/survey-production-core-v2-x-source-intake.md` | `CANONICAL EXTERNAL SOURCE INTAKE SUBFLOW` | Grok/X applicability, Drive handoff, Raw import and disposition |
| `docs/generative-ai-foundations-special-series.md` | `ACTIVE LIVING SERIES RESEARCH AUTHORITY` | Foundations outer-series guidance |
| `docs/checkpoints/survey-production-core-v2-audit-findings/` | `ACTIVE MACHINE-READABLE AUDIT EVIDENCE` | Findings/Repair Sets |

## 5. Responsibility boundaries

### 5.1 Sol supervisor/reviewer owns

- target resolution from repository authority;
- Source Intake/search strategy and expansion;
- independent Discovery completeness review and negative-space sweep;
- research saturation/closure judgment;
- X/Grok applicability where Profile policy permits judgment;
- Grok run purpose/questions/coverage/time scope;
- authoritative-source gap-fill strategy;
- reading substantive captured primary bodies for important candidates;
- classifying authority as not found, retrieval failed, captured-but-unconsumed, or consumed;
- semantic Screening/Evidence interpretation;
- research completeness/materiality judgment;
- review of high-signal unselected candidates;
- Candidate Selection and omission rationale;
- Architecture thesis, package choice/order, page allocation, and counterfactual alternatives;
- Human-facing Architecture Review dossier and approval recommendation;
- drafting and synthesis supervision;
- historical attribution/significance;
- Weekly `why this week`, Watchlist, Late Breaking and carry-over semantics;
- editorial and visual review;
- classification/generalization of new findings.

Structured records make these decisions resumable and reviewable; they do not turn them into deterministic truth claims.

### 5.2 Luna/Work execution agent owns or assists

- bounded source retrieval and retry execution;
- exact-byte capture, hashing and provenance recording;
- bulk candidate normalization/materialization;
- task-local Evidence execution under the accepted task contract;
- Evidence Authority Supplement materialization when authorized;
- targeted gap-fill execution requested by Sol;
- deterministic stage regeneration and checkpoint preparation;
- provisional Materiality/Selection/Architecture artifacts when explicitly requested;
- read-back, path/identity validation and execution records.

Luna/Work does not own the final judgment that research is sufficient, captured authority was semantically consumed, an item is immaterial, Selection is editorially adequate, or Architecture is ready for Human approval.

Unless explicit Human/Sol instructions provide the necessary semantic decisions, Luna/Work must not silently collapse `Discovery -> Evidence -> Selection -> Architecture -> Human Gate` into one unreviewed execution chain.

### 5.3 Grok owns

- X-native search/observation for the exact run-specific task;
- representative posts, community signal, counter-signal and primary-source leads;
- writing the final Raw Observation Markdown only into the instructed Drive run folder.

Grok does not write to GitHub and is not publication-grade authority for model specifications, benchmark values, dates, license terms or historical priority.

### 5.4 Deterministic tools own or assist

- issue/date/window/Profile bootstrap;
- schemas/structure/paths/hashes;
- X Source Intake manifest/Profile-policy validation;
- exact Grok prompt/instruction authority and imported Raw hashes/byte counts;
- X-run completion and Discovery/no-material accounting;
- Raw immutability/provenance;
- IDs/URLs/source refs;
- duplicate/missing/disposition accounting;
- subject/entity/property binding;
- targeted period-label checks;
- bibliography/render/build/preflight;
- lifecycle-specific exact semantic stage validation;
- exact Production Profile/source/PDF quality binding;
- exact Publication Preview/PDF/Freeze/Release identity;
- GitHub Release side effects/reconciliation.

GitHub Actions does not need private Drive access. ChatGPT performs account-specific Drive transport; repository/CI validates imported bytes and stable path-level authority.

### 5.5 Human responsibility

The only normal Human Gates are:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

The Human receives a complete Architecture Review dossier before being asked to decide. Candidate Selection and Sol supervisory checkpoints remain internal. Visual Review, Freeze, merge and Release are not routine Human Gates.

An Exception Gate is justified only for a genuine unresolved Owner decision. Retryable tool/network failures, ordinary search refinement, weak-source replacement, wording/layout repair, CI retry, generic defect repair and ordinary Grok-result transport are not Exception Gates.

## 6. Core/Profile principles

1. `shared file format != shared semantic Core`.
2. Weekly semantics remain Weekly/Profile-owned.
3. bounded-period semantics remain Period/Profile-owned.
4. Thematic research scope/lineage semantics remain Thematic/Profile-owned.
5. Publication-format/layout rules remain Publication Profile-owned.
6. Weekly Grok/X Source Intake is required by Profile; a quiet X week may produce no material Discovery but the scan cannot be silently skipped.
7. Retrospective Period and Thematic X applicability is an explicit ChatGPT `REQUIRED` / `NOT_REQUIRED` research judgment with rationale.
8. Foundations uses the living series memo and the `GENERATIVE_AI_FOUNDATIONS` Drive category when X is material.
9. X/Grok is Discovery/community-signal input, not direct technical Evidence authority.
10. Frozen historical releases remain immutable.
11. Completed W33/SP001 production runs are historical validation evidence, not generic design templates; any new post-integration validation must be fresh and explicitly scoped.
12. W33/SP001-specific editorial scope must not leak into generic Core code.
13. Retrospective Period may use internal `SP-...` source identity while public release identity derives from exact Profile `survey_root`.
14. A bounded Retrospective Period cannot initialize before its configured period end.
15. Routine internal stages must proceed without repeated Human confirmation.
16. Execution-agent output and deterministic PASS never replace independent Sol semantic review.
17. Primary-source binding is distinct from primary-source semantic consumption.
18. A sparse issue is valid only after completeness, authority-consumption, and compression review; no story quota is required, but incomplete research cannot be rationalized as a quiet week.
19. The first Human presentation of every Architecture revision must satisfy the full dossier contract unless the Human explicitly waives it for that revision.

## 7. X/Grok Source Intake and Google Drive handoff

The configured Drive root folder name is exactly:

`Grok_X_SourseIntake`

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

Canonical behavior:

```text
ChatGPT decides/derives X applicability
-> defines run-specific task(s)
-> renders exact Grok instruction + prompt
-> provisions exact Drive run folder
-> Grok observes X and writes Markdown only there
-> ChatGPT reads returned file
-> imports exact bytes into repository Raw
-> maps material signal to Discovery OR records NO_MATERIAL_DISCOVERY
-> Discovery Acceptance binds completed X manifest SHA
-> Sol completeness review tests the combined intake basis
-> continue automatically through Screening/Evidence
```

`AWAITING_GROK` is incomplete Source Intake, not a production terminal reason. If manual transport is needed, expose the exact prompt/instruction and Drive path. Do not ask for unrelated approval. If the Drive result already exists, import it immediately and continue.

## 8. Provenance and toolchain evolution

Retain:

- immutable accepted Raw bytes, including imported Grok result bytes;
- exact X manifest/instruction/prompt/result provenance where used;
- exact accepted research artifact authority;
- material-discovery disposition traceability;
- exact active Evidence/View authority reviewed by Sol;
- concise Sol completeness/authority-consumption/compression review evidence where applicable;
- exact reviewed Architecture identity;
- exact Production Profile binding for quality applicability;
- exact Publication Preview/Freeze/Release byte chain;
- explicit Human approval records;
- exact Release reconciliation/idempotency.

Initialization implementation identity is historical provenance, not an edition-wide execution lock. A newer reviewed generic repair may be used later only after integration into the edition work branch. Revalidate/migrate affected accepted boundaries selectively, then record the actual integrated branch head/current contract in the next Stage Checkpoint.

Compact checkpoints must carry `CORE_STAGE_CONTRACT` validation binding exact State/Profile/current tool/current contract/artifacts. Discovery Acceptance transitively binds the completed X Source Intake manifest and imported Raw authority. A same-named file is never sufficient proof of validity.

Root Discovery authority is the formally accepted Discovery set; the effective downstream Discovery basis may be that root or a mechanically validated derived Screening expansion. A derived basis is legal only when every accepted root remains accounted for and all parent, Raw, source-identity, obligation, issue, and duplicate-ID invariants pass.

Historical Screening acceptances are immutable content-addressed evidence; the active Screening acceptance is only the exact `screening-acceptance` artifact adopted by the passed State-bound Screening Stage Checkpoint. Directory count, mtime, digest order, and latest-file heuristics are never authority.

After Screening advancement, Evidence, Materiality, Completeness, Selection, and Architecture follow the same active Screening/effective Discovery authority chain. Production editions do not repair shared Core in place; Core repairs are reviewed on a dedicated maintenance branch before edition use.

The 2026-09-05 pre-Human repair adds three generic authority distinctions without changing the lifecycle or Human Gate count:

- an unpresented, still-pending Human Gate surface may be invalidated by an explicit operator operation at a configured safe regeneration boundary; this is not Human `REQUEST_CHANGES`, creates no Human review record, does not increment Human revision, and never crosses an active Human approval boundary;
- post-Screening primary authority may enter Evidence only through an exact, edition-local **Evidence Authority Supplement** manifest whose Raw bytes, SHA-256, byte count, issue/task identity, and Screening basis validate; Screening decisions and accepted Screening history remain unchanged;
- active Evidence and Edition View acceptance is resolved from the passed State-bound Evidence Stage Checkpoint and its exact named artifacts, with the View acceptance cross-bound to that exact Evidence acceptance. Historical accepted runs remain immutable and are not selected by directory order, mtime, or latest heuristics.

The 2026-09-07 governance amendment adds a further semantic distinction: **authority capture/binding is not authority consumption**. Sol must inspect whether relevant substantive bytes were actually converted into bounded Evidence claims before relying on unresolved/materiality/Selection outcomes.

## 9. Canonical orchestration model

Normal local production is:

```text
Profile + Production State + applicable guidance
-> Source Intake / Discovery execution
-> Sol Discovery completeness review
-> Screening
-> Evidence verification + iterative gap-fill execution
-> Sol authority-consumption review
-> additional gap fill when required
-> Sol materiality / Selection review
-> Architecture preparation under Sol-owned semantics
-> Sol full Architecture Review dossier
-> scripts/survey_stage_validation_v2.py + exact checkpoint
-> Human ARCHITECTURE_REVIEW
-> after approval, reader-facing authorship / QA
-> Human exact-byte PUBLICATION_PREVIEW
```

Canonical `config/survey-production-v2.json` keeps `stage_plan[*].handoff_required=false`. Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery is compatibility/audit material, not the canonical local hot path. Grok/Drive transport and Sol supervisory checkpoints do not resurrect that legacy chain or create new Human Gates.

For Architecture Review, `READY_FOR_ARCHITECTURE_REVIEW` establishes lifecycle readiness only. The Human-facing dossier must additionally show research coverage, authority consumption, important unselected candidates, omissions, alternatives, limitations, and Sol findings before approval is requested.

If `SELECTED <= 1` while either `non-DROP >= 20` or `VERIFIED >= 10`, a documented Sol compression audit is mandatory.

## 10. Historical Issue recurrence and clarified requirements

The production-facing prevention authority is `docs/survey-production-core-v2-issue-prevention-checklist.md`. Crisp failures should have small reliable deterministic protection; semantic/visual judgment remains explicit Sol/ChatGPT responsibility rather than brittle automation.

AUD-046 adds X applicability/evidence-boundary/result-disposition protection. AUD-047 adds stop-discipline protection: having only two formal Human Gates is insufficient if ChatGPT still repeatedly pauses during routine work.

The 2026-09-07 Human finding adds the following recurring protections:

- do not over-delegate semantic/editorial judgment to Luna/Work;
- do not infer research sufficiency from candidate count, execution completion, or deterministic readiness;
- inspect captured primary bodies for actual semantic consumption;
- independently review strong unselected candidates and negative space;
- perform compression audit for extreme sparse-selection outcomes;
- do not use an abbreviated approval prompt as the first Architecture Review presentation.

## 11. Finding disposition

`FIXED_GENERIC` in the previously integrated Core history:

- AUD-027, AUD-028, AUD-029, AUD-030
- AUD-032, AUD-034, AUD-035, AUD-036
- AUD-037, AUD-038
- AUD-039 — compact checkpoint semantic stage authority
- AUD-040 — practical reviewed-tool adoption
- AUD-041 — all-changes-first fixed-head audit rule
- AUD-042 — exact Production Profile-bound Quality applicability
- AUD-043 — Retrospective public release identity
- AUD-044 — bounded Period completion guard
- AUD-045 — canonical pre-audit status synchronization
- AUD-046 — formal Grok/X Source Intake + Google Drive handoff
- AUD-047 — autonomous progression / stop discipline as an independent acceptance condition

Current governance amendment finding: `IMPLEMENTED_ON_MAINTENANCE_BRANCH / REVIEW_PENDING`.

Intentional `DEFERRED`:

- AUD-031 — machine Series engine remains premature;
- AUD-033 — exhaustive synthetic future-edition matrix remains unnecessary before real Pilots.

Repair Set `REPAIR-WU012-2026-08-22` remains historical implementation evidence. The present Sol/Luna governance amendment is a separate shared-Core candidate and is not final-audit PASS evidence until reviewed/integrated.

## 12. Pre-audit validation boundary

For Core changes requiring the full maintenance audit, the external validation sequence remains:

1. finish all candidate changes, synchronize authority, and obtain exact-head diagnostic CI;
2. freeze that exact head;
3. run all **seven** acceptance points from zero on that unchanged head:
   1. Weekly viability;
   2. Special viability;
   3. Generality;
   4. historical/clarified requirement recurrence prevention;
   5. control proportionality;
   6. autonomous progression / stop discipline;
   7. Human Gate round-trip viability;
4. any candidate-tree mutation invalidates the entire audit;
5. an unchanged all-PASS result is recorded in PR/Human-review metadata with exact head SHA and CI run IDs.

The five CI families remain:

1. Survey Production Core v2 CI;
2. Screening contract CI;
3. Evidence contract CI;
4. Pipeline contract tests;
5. Weekly pipeline spine + committed Raw integrity.

Do not confuse five CI families with seven acceptance points.

Because the current amendment changes shared semantic operating authority, its review must explicitly test that mandatory Sol checkpoints do not become extra Human confirmation gates and that the Human Architecture dossier requirement does not weaken exact-byte/reviewed-commit Gate identity.

## 13. Pre-audit handoff and production boundary

PR #310, PR #452, and PR #484 are historical merged implementation PRs. The current governance amendment is carried only on `fix/core-v2-sol-luna-review-governance-20260907` until reviewed integration.

W33 and released Specials remain immutable historical editions. Active edition production branches must not edit this shared-Core candidate in place.

Once Authority, governance, bootstrap, checklist and implementation expectations agree, freeze the exact branch head, obtain applicable validation, and review the candidate without changing it.

If any audit/review point requires a repository change:

```text
record/classify finding
-> current audit/review candidate INVALIDATED
-> repair + synchronize
-> rerun applicable CI/review
-> freeze new head
-> rerun required acceptance from the beginning
```

Do not commit a post-audit PASS document into an already frozen audited tree merely to record its own PASS.
