# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL POST-INTEGRATION CORE AUTHORITY / PRE-HUMAN EVIDENCE-REGENERATION REPAIR / PRE-AUDIT CANDIDATE / PRE-SOL REVIEW`
Established: 2026-08-22 JST  
Current maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
Integration PR: `#484` — `Survey Production Core v2: pre-Human Evidence regeneration repair` (`draft` / `open` / `unmerged`); this branch is the normal draft integration review surface and must not be merged by this task
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Purpose and current boundary

This index identifies the live semantic authority for Survey Production Core v2 while preserving earlier design/audit documents as historical reasoning.

Current `main` is the production source of truth at the current structural-recovery HEAD `2adcffdc8741605cd56a984e9fc509b6066172e1`. That HEAD is a transparent structural-recovery descendant of `d8fa79ef2affacec49a47e6fc88018fb99f36899`, which is itself a structural-recovery descendant of the pre-incident reviewed semantic/tree baseline `a9f121f0d65591f52b53515712d7c0bae573b2ef`. All three commits resolve to exact tree `b6c1b2cbc13165e64ac1d88d4d36b7515f7494da`, with zero changed files and zero content delta between the reviewed tree states. The exact current main SHA is authoritative for repository reality; `d8fa79ef2affacec49a47e6fc88018fb99f36899` remains historical execution/base evidence for the completed repair runs, and `a9f121f0d65591f52b53515712d7c0bae573b2ef` remains the pre-incident reviewed baseline. The historical implementation PR #310 and post-integration repair PR #452 are already merged. This file is the current Core authority for the maintenance candidate branch above; it does not authorize a merge or substitute for later fixed-head audit and Human review. The source-authority candidate `5b1f72c78127dd4bb50f3bfc1e4678a54114c432` remains semantically unchanged by this reconciliation.

Historical candidate audits are not reusable as current approval evidence:

- `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` was invalidated by AUD-039 through AUD-044;
- `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` was invalidated by AUD-045;
- `705937af2eb45d5ba361fe748d7a622110bcb27c` completed the then-current five-point audit, but was invalidated by AUD-046 after the Owner clarified the required Grok/X Source Intake architecture;
- `c565a3254ad303bd276edee55b2b1e6e0a1c91a7` reached the pre-audit freeze boundary, but its subsequent audit was invalidated by a current-facing six-point wording contradiction in this authority; its CI/audit evidence is historical only and is not reusable for the replacement candidate;
- AUD-047 added autonomous progression / stop discipline as an independent acceptance dimension. The canonical final audit has since been fixed at seven points, with Human Gate round-trip viability as Point 7. The next final audit must be a fresh seven-point audit on one later unchanged head.

The candidate tree intentionally stops at an **audit-stable pre-freeze state**. Exact final PASS evidence belongs in PR/Human-review metadata keyed to one unchanged candidate SHA; do not mutate the candidate merely to record that PASS.

## 2. Fundamental operating model

**ChatGPT is the primary research/editorial operator.**

Normal production is:

```text
user supplies target + requested stopping Human Gate
-> ChatGPT reads repository authority/Profile/State
-> ChatGPT plans and performs research/editorial work
-> Source Intake uses conventional collectors + direct research + applicable Grok/X external collection
-> deterministic helpers protect crisp/repetitive/provenance-sensitive invariants
-> canonical stage artifacts are produced
-> exact semantic stage validation + applicable ChatGPT review
-> one compact Stage Checkpoint
-> Production State advances
-> ChatGPT continues immediately toward the requested Gate
```

The operating default is **continuous autonomous progression**. Source Intake, Screening, Evidence, Completeness/materiality, Selection, Architecture preparation, drafting/synthesis, deterministic QA, semantic/visual repair, CI retry, generic repair and ordinary Drive result import are not user decision points.

A production session may interrupt that progression only for:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`;
3. a genuine Owner-level Exception Gate that repository authority cannot safely resolve;
4. unavoidable manual Grok instruction/result transport when the external Grok execution itself cannot be crossed directly.

The fourth item is operational transport, not editorial approval and not another Human Gate. Once a valid Grok result is available in the configured Drive run folder, ChatGPT imports it and resumes automatically without another routine confirmation.

Scripts, schemas and GitHub workflows support ChatGPT. They are not the editorial intelligence and must not replace qualitative reasoning with ceremonial machine state.

## 3. Authority precedence

For Survey Production Core v2 improvement work, use:

```text
1. repository reality
2. this authority index
3. docs/survey-production-core-v2-final-audit-rule.md
4. docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md
5. docs/checkpoints/survey-production-core-v2-worklog.md
6. docs/survey-production-core-v2-improvement-plan.md
7. whole-system audit + explicit remediation status
8. WU-011 second-audit closure / earlier amendments
9. historical/current-main implementation docs used as evidence
```

`docs/survey-production-core-v2-wu012-preapproval-closure.md` remains historical evidence only. Its former PASS conclusion does not override later Findings.

## 4. Current document map

| Document | Current status | Role |
|---|---|---|
| `docs/survey-production-core-v2-final-audit-rule.md` | `CANONICAL PRE-MERGE REVIEW RULE` | all-changes-first/fixed-head seven-point audit and invalidation semantics |
| `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md` | `AUTHORITATIVE OPERATOR-MODEL RE-AUDIT` | corrected ChatGPT/tool boundary |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL PRE-AUDIT WORK STATUS` | implementation status and external final-validation handoff |
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE CONSOLIDATED PLAN / REPAIRS IMPLEMENTED` | architecture, rationale and rollout |
| `docs/survey-production-core-v2-session-bootstrap.md` | `CANONICAL AGENT-FIRST SESSION BOOTSTRAP` | short-request start/resume and autonomous progression |
| `docs/survey-production-core-v2-issue-prevention-checklist.md` | `CANONICAL PRODUCTION PREVENTION CHECKLIST` | recurring defect ownership |
| `docs/survey-production-core-v2-x-source-intake.md` | `CANONICAL EXTERNAL SOURCE INTAKE SUBFLOW` | Grok/X applicability, Drive handoff, Raw import and disposition |
| `docs/generative-ai-foundations-special-series.md` | `ACTIVE LIVING SERIES RESEARCH AUTHORITY` | Foundations outer-series guidance |
| `docs/checkpoints/survey-production-core-v2-audit-findings/` | `ACTIVE MACHINE-READABLE AUDIT EVIDENCE` | Findings/Repair Sets |

## 5. Responsibility boundaries

### 5.1 ChatGPT owns

- target resolution from repository authority;
- Source Intake/search strategy and expansion;
- X/Grok applicability where Profile policy permits judgment;
- Grok run purpose/questions/coverage/time scope;
- Google Drive run-folder provisioning;
- reading returned Grok Markdown and importing exact bytes into repository Raw;
- Discovery/no-material disposition of Grok results;
- authoritative-source gap fill for X-origin leads;
- research completeness/materiality judgment;
- semantic Screening/Evidence interpretation;
- Candidate Selection and Architecture;
- drafting and synthesis;
- historical attribution/significance;
- Weekly `why this week`, Watchlist, Late Breaking and carry-over semantics;
- editorial and visual review;
- autonomous repair/retry of internally resolvable failures;
- classification/generalization of new findings.

Structured records make these decisions resumable and reviewable; they do not turn them into deterministic truth claims.

### 5.2 Grok owns

- X-native search/observation for the exact run-specific task;
- representative posts, community signal, counter-signal and primary-source leads;
- writing the final Raw Observation Markdown only into the instructed Drive run folder.

Grok does not write to GitHub and is not publication-grade authority for model specifications, benchmark values, dates, license terms or historical priority.

### 5.3 Deterministic tools own or assist

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

### 5.4 Human responsibility

The only normal Human Gates are:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not routine Human Gates.

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
-> continue automatically through normal Screening/Evidence/Completeness
```

`AWAITING_GROK` is incomplete Source Intake, not a production terminal reason. If manual transport is needed, expose the exact prompt/instruction and Drive path. Do not ask for unrelated approval. If the Drive result already exists, import it immediately and continue.

## 8. Provenance and toolchain evolution

Retain:

- immutable accepted Raw bytes, including imported Grok result bytes;
- exact X manifest/instruction/prompt/result provenance where used;
- exact accepted research artifact authority;
- material-discovery disposition traceability;
- exact reviewed Architecture identity;
- exact Production Profile binding for quality applicability;
- exact Publication Preview/Freeze/Release byte chain;
- explicit Human approval records;
- exact Release reconciliation/idempotency.

Initialization implementation identity is historical provenance, not an edition-wide execution lock. A newer reviewed generic repair may be used later only after integration into the edition work branch. Revalidate/migrate affected accepted boundaries selectively, then record the actual integrated branch head/current contract in the next Stage Checkpoint.

Compact checkpoints must carry `CORE_STAGE_CONTRACT` validation binding exact State/Profile/current tool/current contract/artifacts. Discovery Acceptance transitively binds the completed X Source Intake manifest and imported Raw authority. A same-named file is never sufficient proof of validity.

The current maintenance candidate adds two generic authority distinctions without creating a new lifecycle or Human Gate:

- **root Discovery authority** is the formally accepted Discovery set; the **effective downstream Discovery basis** may be that root or a mechanically validated derived Screening expansion. A derived basis is legal only when every accepted root remains accounted for and all parent, Raw, source-identity, obligation, issue, and duplicate-ID invariants pass.
- **historical Screening acceptances** are immutable content-addressed evidence; the **active Screening acceptance** is only the exact `screening-acceptance` artifact adopted by the passed State-bound Screening Stage Checkpoint. Directory count, mtime, digest order, and latest-file heuristics are never authority.

After Screening advancement, Evidence, Materiality, Completeness, Selection, and Architecture follow the same active Screening/effective Discovery authority chain. Production editions do not repair shared Core in place; Core repairs are reviewed on the dedicated maintenance branch before edition use.

The 2026-09-05 pre-Human repair adds three generic authority distinctions without changing the lifecycle or Human Gate count:

- an unpresented, still-pending Human Gate surface may be invalidated by an explicit operator operation at a configured safe regeneration boundary; this is not Human `REQUEST_CHANGES`, creates no Human review record, does not increment Human revision, and never crosses an active Human approval boundary;
- post-Screening primary authority may enter Evidence only through an exact, edition-local **Evidence Authority Supplement** manifest whose Raw bytes, SHA-256, byte count, issue/task identity, and Screening basis validate; Screening decisions and accepted Screening history remain unchanged;
- active Evidence and Edition View acceptance is resolved from the passed State-bound Evidence Stage Checkpoint and its exact named artifacts, with the View acceptance cross-bound to that exact Evidence acceptance. Historical accepted runs remain immutable and are not selected by directory order, mtime, or latest heuristics.

## 9. Canonical orchestration model

Normal local production is:

```text
Profile + Production State + applicable guidance
-> ChatGPT research/editorial work
-> applicable Source Intake including Grok/X
-> canonical stage artifacts
-> scripts/survey_stage_validation_v2.py
-> applicable ChatGPT research/editorial/visual review
-> compact Stage Checkpoint with exact artifact + CORE_STAGE_CONTRACT + implementation/contract provenance
-> State transition
-> continue immediately unless a Human/Exception Gate or unavoidable manual Grok transport is reached
```

Canonical `config/survey-production-v2.json` keeps `stage_plan[*].handoff_required=false`. Legacy Action Spec / Handoff Request / Handoff / Action Result / Validation Attestation machinery is compatibility/audit material, not the canonical local hot path. Grok/Drive transport does not resurrect that legacy chain.

## 10. Historical Issue recurrence and clarified requirements

The production-facing prevention authority is `docs/survey-production-core-v2-issue-prevention-checklist.md`. Crisp failures should have small reliable deterministic protection; semantic/visual judgment remains explicit ChatGPT responsibility rather than brittle automation.

AUD-046 adds X applicability/evidence-boundary/result-disposition protection. AUD-047 adds stop-discipline protection: having only two formal Human Gates is insufficient if ChatGPT still repeatedly pauses during routine work. The current maintenance candidate additionally closes the generic Screening expansion authority and active-acceptance selection gaps described in the current pre-freeze instruction.

## 11. Finding disposition

`FIXED_GENERIC` in the pre-audit candidate:

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

Intentional `DEFERRED`:

- AUD-031 — machine Series engine remains premature;
- AUD-033 — exhaustive synthetic future-edition matrix remains unnecessary before real Pilots.

Repair Set `REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, until the required post-integration verification editions exist. The current Screening expansion/active-acceptance repair is a separate pre-freeze Core candidate and is not treated as final-audit PASS evidence.

## 12. Pre-audit validation boundary

The required external validation sequence is:

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

## 13. Pre-audit handoff and production boundary

PR #310 and the post-integration repair PR #452 are historical merged implementation PRs. The current repair candidate is carried only on `fix/core-v2-pre-human-evidence-regeneration-20260905`; it must not be merged by this task. W33 is an immutable released edition and SP001 is an immutable released historical edition; W34 is an active production-regression edition used only as an exact read-only temporary fixture in this maintenance task. SP001, SP002, and SP003 remain outside this Core candidate's production scope: SP001 is already released, while SP002/SP003 have no canonical production state or work branch in the reviewed `main`.

Once Authority, Worklog, Repair Set, implementation and tests agree, freeze the exact branch head, obtain the required exact-head CI, and run the mandatory seven-point audit without changing the candidate.

If any audit point requires a repository change:

```text
record/classify finding
-> audit INVALIDATED
-> repair + synchronize
-> rerun five-family CI
-> freeze new head
-> rerun all seven acceptance points from point 1
```

If all seven pass on an unchanged head, record that exact-SHA result in PR/Human-review metadata and present the candidate for Human full-candidate review. Do not commit a post-audit PASS document into the audited tree.

Do not start any new Core-v2 production validation run, or cold-start a completed W33/SP001 edition, before explicit Human approval and merge.
