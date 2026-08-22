# Survey Production Core v2 — Compilation System Improvement Plan

Status: `WU-012 REPAIRS IMPLEMENTED / AUDIT-STABLE PRE-AUDIT CANDIDATE`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Production source of truth until merge: current `main`  
Operator-model authority: `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Objective

Survey Production Core v2 exists to help an upper-tier ChatGPT reasoning model compile the Japanese Generative AI Technical Survey accurately, efficiently and reproducibly across sessions.

It is **not** an external autonomous publishing engine. ChatGPT performs open-ended research/editorial reasoning; repository-owned guidance, schemas, scripts, tests and workflows support deterministic/repetitive/provenance-sensitive work.

```text
user target + requested stopping Human Gate
-> ChatGPT reads repository authority/Profile/State
-> ChatGPT researches, judges materiality/completeness, selects and drafts
-> deterministic helpers protect crisp invariants
-> exact stage artifacts + compact provenance checkpoint
-> continue autonomously
-> stop only at requested Human Gate or genuine Exception Gate
```

Core priority remains:

```text
Correctness > Traceability > Coverage > Speed
```

But “traceability” does not justify ceremony whose cost exceeds its protection.

## 2. Acceptance priorities

Before merge, evaluate in this strict order:

1. **Weekly viability** — future Weekly issues can be compiled reliably.
2. **Special viability** — Retrospective Period, stand-alone Thematic, SP-001–003 style work and Generative AI Foundations can be compiled reliably.
3. **Generality** — no overfit to W33/W34/SP001–003; later Weekly and unforeseen Specials remain generic.
4. **Historical Issue recurrence prevention** — known Human Review failures have durable prevention ownership.
5. **Control proportionality** — only after 1–4, remove/avoid unnecessary gates, ceremony and brittle validators.

Lower-numbered priorities win on conflict.

## 3. Core/Profile architecture

```text
Survey Production Core v2
  + Research / Editorial Profile
      WEEKLY
      RETROSPECTIVE_PERIOD
      THEMATIC
  + Publication Profile
      WEEKLY_MAGAZINE
      LONGFORM_SPECIAL
  + optional living Series guidance
      Generative AI Foundations etc.
```

Core owns reusable mechanisms. Research Profiles own edition semantics. Publication Profiles own reader-facing publication behavior. A living Series document may coordinate volumes without becoming another workflow engine.

### Weekly owns

- current-window/cutoff significance;
- carry-over and Late Breaking;
- Watchlist semantics;
- `why this week`.

### Retrospective Period owns

- bounded completed-history scope;
- chronology/period labels;
- retrospective coverage and synthesis.

### Thematic owns

- explicit research question;
- open-history/current-state scope;
- lineage/branch/competitor expansion;
- thematic completeness.

### Foundations Series

`docs/generative-ai-foundations-special-series.md` remains the living series architecture. A machine Series engine is intentionally deferred until real cross-volume work demonstrates repeated cost or drift that would justify it.

## 4. Responsibility boundary

### ChatGPT owns

- Source Intake/search strategy and expansion;
- source quality and primary-source gap fill;
- semantic Screening/Evidence interpretation;
- completeness/materiality judgment;
- Candidate Selection and Architecture;
- drafting/synthesis;
- historical attribution/significance;
- Weekly/Special editorial semantics;
- semantic and visual review;
- classification/generalization of new findings.

### Deterministic tools own/assist

- cutoffs/windows/date/profile bootstrap;
- schemas/formats/paths/hashes;
- Raw immutability and provenance;
- IDs/URLs/source refs;
- duplicate/missing/disposition accounting;
- subject/entity/property binding;
- targeted period-label checks;
- bibliography/render/build/preflight;
- exact semantic stage-artifact validation;
- exact Production Profile-bound quality applicability;
- exact Publication Preview/PDF/Freeze/Release identity;
- release reconciliation/idempotency.

A tool may validate an artifact created by ChatGPT. It does not replace qualitative judgment merely to produce a PASS field.

## 5. Human / Exception Gates

Normal production Human Gates remain exactly:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not extra routine Human Gates.

Exception Gate is reserved for unresolved editorial/publication/compatibility choices that repository authority cannot safely decide. Search refinement, ordinary QA failures, CI retry and clean reviewed-tool upgrades are not Human Gates.

The Core-v2 five-point final audit is a **change-management acceptance rule**, not a third production Human Gate.

## 6. Cross-session resume / State

Repository state, not chat history, must be sufficient for continuation. A new session should recover:

- target/Profile/work branch;
- Production State and lifecycle;
- accepted stage artifacts;
- current Human/Exception Gate;
- research limitations/findings;
- implementation/contract used at each material checkpoint.

Initialization implementation identity is historical provenance, not a permanent execution lock.

## 7. Controlled toolchain evolution

The desired repair loop is:

```text
reusable defect found during edition
-> generic repair reviewed/merged on main
-> integrate that reviewed repair into edition work branch
-> work branch now actually contains the toolchain to be used
-> revalidate/migrate only accepted boundaries affected by the change
-> next Stage Checkpoint records actual integrated branch head + current contract
-> continue
```

Do not execute an unintegrated second checkout of `main` against edition files and claim that tooling as work-branch provenance.

Legacy Screening/Evidence helpers retain historical pin checks internally. `scripts/survey_agent_tool_v2.py` is a narrow allowlisted bridge that first validates current agent-first State/current work-branch implementation and then adapts only that obsolete execution-pin expectation.

Compatibility ambiguity that could change accepted meaning or Human-approved authority fails closed and may become an Exception Gate.

## 8. Compact local orchestration with semantic authority

WU-010R/WU-011’s historical local chain:

```text
Action Spec -> Handoff Request -> Handoff -> Action Result -> Validation Attestation
```

is not the canonical hot path.

Current local path:

```text
ChatGPT produces exact intended stage artifacts
-> run scripts/survey_stage_validation_v2.py
-> deterministic CORE_STAGE_CONTRACT result binds exact State/Profile/current tool/current contract/artifacts
-> perform applicable ChatGPT review
-> compact Stage Checkpoint includes exact artifact authorities + CORE_STAGE_CONTRACT + review evidence
-> controller independently reconciles the deterministic report
-> State advances one lifecycle step
```

Canonical `stage_plan[*].handoff_required=false`. Legacy Handoff code remains compatibility/audit material only.

`CORE_STAGE_CONTRACT` validates semantic/content-addressed authority, not just filenames. Draft stage additionally requires paired `draft-package:<id>` / `draft-result:<id>` authorities.

Richer request/receipt/reconciliation remains justified at external irreversible boundaries such as public Release.

## 9. Source Intake / Completeness / Materiality

Issue #166 established that collector success or source count does not prove completeness, and material discoveries must not disappear downstream.

### ChatGPT completeness review records

- what was searched/investigated;
- material findings/branches;
- targeted gap-fill;
- negative search results where meaningful;
- residual uncertainty/limitations;
- why an obligation is satisfied, limited, not applicable, or still needs research.

No universal source/story/page quota is introduced.

### Deterministic traceability retains

- exact Discovery/Raw identity;
- every material discovery disposition;
- supplemental/gap-fill joining the same trace;
- stable subject/entity binding.

## 10. Historical Issue recurrence model

Every recurring defect family gets one primary owner:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

Examples:

- #166 material drop -> deterministic disposition accounting + ChatGPT completeness review;
- #191 entity rebinding -> structured Evidence + deterministic entity/role checks;
- #49 wrong period label -> designated deterministic Period check;
- #9 why-this-week / Late Breaking / Watchlist/internal metadata -> Weekly ChatGPT editorial checklist plus reliable leakage checks;
- #55 Technical Notes tail/orphan -> ChatGPT rendered-page review rather than global pagination hard-code;
- release/PDF drift -> deterministic exact-byte authority.

`docs/survey-production-core-v2-issue-prevention-checklist.md` is the production-facing checklist.

## 11. Quality model

Quality uses:

```text
DETERMINISTIC
AGENT_SEMANTIC
AGENT_VISUAL
```

Only deterministic rows require executable result authority.

Post-completion AUD-042 repair strengthens applicability:

- `quality.build_bundle` requires an exact Production Profile path;
- the bundle hashes/binds that Profile;
- research/publication Profile identities and applicable checks derive only from those bytes;
- issue-ID inference is removed;
- Profile drift invalidates the bundle;
- Publication Candidate must match its coupled Quality bundle’s publication Profile.

Thus `RETROSPECTIVE_PERIOD` cannot silently receive Thematic checks.

## 12. Weekly viability design

Weekly viability rests on generic issue/cutoff derivation, Profile-owned semantics, adaptable ChatGPT research, issue-agnostic provenance and the Issue Prevention Checklist.

No Core behavior branches on W33. W33 remains a first **real post-merge validation edition**, not a template.

The current-main Weekly production spine remains protected by the required cross-regression family before merge.

## 13. Special viability design

### Retrospective Period

`scripts/survey_period_v2.py` supports configured month/half-year/year plus explicit custom bounded periods through one generic `RETROSPECTIVE_PERIOD` Profile.

Post-completion AUD-044 repair requires:

```text
as_of >= bounded period end
```

before Profile creation/initialization, preventing incomplete future retrospectives.

### Stand-alone Thematic

Thematic scope comes from an explicit research question and canonical planning authority. SP001 materializes TS-001 planning authority instead of duplicating narrow topic content in bootstrap config.

### Generative AI Foundations

Each volume uses normal Thematic production while `docs/generative-ai-foundations-special-series.md` remains outer living research architecture. AUD-031 intentionally defers a separate machine Series engine.

## 14. Publication / release identity

Quality/Publication binds exact Production Profile, source and PDF authority.

Post-completion AUD-043 separates internal source identity from public publication slug:

```text
internal issue_id = SP-2025-H2
Profile survey_root = surveys/special/2025-H2
public release tag = special/2025-H2
public title/asset slug = 2025-H2
```

`scripts/survey_profiled_freeze_v2.py` derives public identity from exact Profile `survey_root` basename. The Release workflow rederives the same identity from State-bound Profile and rejects divergence.

Ordinary Thematic `SP001` and Weekly `2026-W35` naturally remain `special/SP001` and `weekly/2026-W35`.

Exact Publication Preview / Visual / Freeze / Manifest / Merge Verification / Release Record byte authority remains unchanged in principle.

## 15. Generality strategy

Pre-merge genericity is structural rather than an exhaustive synthetic universe:

- arbitrary valid completed Weekly ID;
- arbitrary bounded Period spec;
- arbitrary Thematic question/spec;
- no generic code branch on W33/SP001/TS-001;
- Research/Publication behavior selected by Profile;
- living series guidance can resolve evolving Foundations volumes.

AUD-033 intentionally defers exhaustive hypothetical future-edition fixture matrices. Real W33/SP001 followed by W34/SP002/SP003 provide stronger post-merge semantic evidence.

## 16. WU-012 repair status

`FIXED_GENERIC`:

- AUD-027, 028, 029, 030
- AUD-032, 034, 035, 036
- AUD-037, 038
- **AUD-039** exact semantic stage authority
- **AUD-040** practical current-tool adoption
- **AUD-041** all-changes-first fixed-head final-audit rule
- **AUD-042** exact Production Profile-bound Quality / Candidate consistency
- **AUD-043** Retrospective public Special identity
- **AUD-044** bounded Period completion guard
- **AUD-045** audit-stable canonical status synchronization

Intentional `DEFERRED`:

- AUD-031 — machine Series engine;
- AUD-033 — exhaustive synthetic future-edition matrix.

`REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, until real W33/SP001 verification editions occur.

The former synchronized head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` is not current approval evidence because its post-completion audit found AUD-039–044. The later fixed-head attempt `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` is likewise invalid as final evidence because AUD-045 required another candidate-tree repair.

## 17. Mandatory final candidate rule

Owner-required review discipline is canonical in `docs/survey-production-core-v2-final-audit-rule.md`.

The candidate tree deliberately remains a stable pre-audit snapshot:

```text
all repository-side repairs/synchronization complete
-> obtain five-family cross-regression on one exact head
-> freeze that exact head
-> audit all five acceptance priorities from zero on that unchanged SHA
```

During the final audit the candidate tree is immutable.

If any point finds a defect requiring a repository change:

```text
audit = INVALIDATED
-> complete every required repair/synchronization
-> rerun cross-regression
-> freeze new head
-> rerun all five points from point 1
```

There is no “recheck only the failed point” after candidate mutation.

The final PASS is recorded outside the candidate tree in PR/Human-review metadata, keyed to exact audited SHA and CI run identities. This prevents a post-audit PASS commit from invalidating its own audit.

## 18. Stable pre-audit exit / rollout boundary

Repository-side candidate preparation is complete when Authority, Worklog, Repair Set, Bootstrap, implementation and tests agree on the pre-audit state. The candidate tree does **not** claim whether a later exact-head final audit has passed; that result is external PR/Human-review metadata.

Pre-audit properties that must remain true:

- ChatGPT-first operator/tool boundary is repository-owned.
- exactly two normal production Human Gates remain.
- compact local orchestration replaces mandatory Handoff ceremony.
- exact semantic `CORE_STAGE_CONTRACT` is required before checkpoint adoption.
- current reviewed toolchain can be integrated and recorded per checkpoint without rewriting initialization provenance.
- Source Intake/completeness remains substantive ChatGPT reasoning.
- Issue Prevention Checklist remains canonical.
- generic Period/Thematic bootstrap exists.
- bounded Period completion guard exists.
- Quality is exact Production Profile-bound.
- Retrospective public Special identity is Profile-derived.
- Foundations living series authority remains sufficient pre-merge.
- AUD-039 through AUD-045 are represented consistently as implemented generic repairs.
- W33/SP001 remain unstarted.

External final-validation sequence:

```text
five-family CI PASS on exact head
-> freeze exact head
-> five acceptance priorities PASS from zero with no candidate mutation
-> record exact SHA + CI run IDs + verdicts in PR/Human-review metadata
-> present that exact candidate for Human full-candidate review
```

After explicit Human approval and merge:

1. merged `main` becomes the production source of truth;
2. run W33 and SP001 as first real verification editions;
3. classify concrete findings and repair only the narrowest correct layer;
4. follow with W34 and SP002/SP003 as second-round generalization evidence;
5. add deferred machinery only if real production demonstrates need.

## References

- `AGENTS.md`
- `docs/survey-production-core-v2-authority.md`
- `docs/survey-production-core-v2-final-audit-rule.md`
- `docs/survey-production-core-v2-session-bootstrap.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`
- `docs/checkpoints/survey-production-core-v2-audit-findings/WU-012-repair-set.json`
- `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`
- `docs/survey-production-core-v2-issue-prevention-checklist.md`
- `docs/survey-production-core-v2-historical-invariants.md`
- `docs/survey-production-core-v2-historical-production-deep-audit.md`
- `docs/thematic-special-backlog.md`
- `docs/generative-ai-foundations-special-series.md`
- `docs/half-year-retrospective-specials.md`
- `docs/annual-retrospective-specials.md`
- historical Human Review Issues recorded by the invariant/deep-audit corpus.
