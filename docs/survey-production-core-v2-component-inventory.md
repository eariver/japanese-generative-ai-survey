# Survey Production Core v2 — Component Inventory and Ownership Map

Status: `PHASE 0 OUTPUT / working architecture inventory`  
Established: 2026-08-22 JST  
Improvement branch: `refactor/survey-production-core-v2`  
Inspected `main`: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Purpose

This document records the Phase 0 process archaeology for the Survey Production Core v2 improvement program.

Its purpose is to answer four questions before contract normalization or refactoring begins:

1. Which production capabilities are already genuinely shared between Weekly and Special?
2. Which behavior belongs to a research/editorial Profile rather than the shared Core?
3. Which publication/release mechanics should be separated from research/editorial behavior?
4. Which historical repair paths contain useful regression knowledge but should not define the future hot path?

This is an ownership/disposition map, not a deletion plan. A component classified `REMOVE/ARCHIVE` is only a future consolidation candidate after caller, workflow, test, replay, and frozen-provenance dependencies have been replaced or explicitly isolated.

---

## 2. Classification vocabulary

### 2.1 Ownership

- `CORE` — edition-agnostic production mechanism: provenance, Screening, Evidence, Selection/Architecture contracts, traceability, structured drafting, orchestration mechanics, generic validation.
- `WEEKLY_PROFILE` — rolling editorial-window semantics, carry-over, Late Breaking/current momentum, Weekly-specific chronology and editorial behavior.
- `PERIOD_PROFILE` — bounded retrospective-period semantics, period coverage/completeness, hindsight/cutoff interpretation, period synthesis.
- `THEMATIC_PROFILE` — research-question-driven scope, open/current-as-of temporal policy, lineage/branch/competitor completeness.
- `PUBLICATION_PROFILE` — reader-facing document assembly/layout, build/preflight, Visual QA, exact PDF identity, Freeze/Release mechanics where publication format matters.
- `SERIES_LAYER` — cross-volume research architecture, reusable evidence corpus, lineage graph, volume dependencies and research debt.
- `LEGACY_REPLAY` — historical compatibility, frozen-edition reconstruction, or repair-chain implementation not intended to remain on the future production hot path.

A component may have a primary owner and one or more hooks supplied by another layer.

### 2.2 Disposition

- `RETAIN` — already suitable as a canonical mechanism or stable base.
- `GENERALIZE` — keep the mechanism but remove edition-specific assumptions or expose Profile hooks.
- `MERGE` — multiple implementations/contracts should converge into one authoritative mechanism.
- `REMOVE/ARCHIVE` — retire from the future hot path after its invariants and replay dependencies are preserved elsewhere.
- `ADD` — capability is materially missing from the current architecture.

---

## 3. Executive finding

The most important Phase 0 finding is that **Survey Production Core v2 is not a greenfield Core**.

A substantial generic Core already exists incrementally inside the current Weekly implementation and is already reused by Special. In particular, the repository has shared schemas and shared Python implementations for:

```text
collector provenance
  -> Raw integrity
  -> Screening
  -> Evidence Tasks / Evidence Runs / Evidence Cards
  -> Candidate materialization / comparison
  -> Candidate Selection
  -> Architecture Input / Architecture validation
  -> Draft Packages / structured Article Draft Results
  -> Evidence / attribution validation
  -> bibliography generation / merge
  -> synthesis contracts
```

Special often wraps these common mechanisms rather than reimplementing them. Therefore the correct v2 strategy is:

> **Promote, normalize, and orchestrate the existing shared mechanisms; do not replace proven generic contracts merely to obtain a new directory or version name.**

The largest fragmentation is not in Evidence schemas. It is in:

- state/orchestration policy;
- temporal/research-scope semantics;
- Human Gate contracts;
- Workflow wrappers and branch/path resolution;
- finalization/publication assembly;
- accumulated Special repair/layout/revision chains;
- completeness/materiality tracking that is not yet end-to-end.

---

## 4. High-level component map

| Capability | Current representative surfaces | Primary ownership | Disposition | Phase 0 conclusion |
|---|---|---|---|---|
| Raw collector provenance | `source_intake.py`, `raw_provenance.py`, collector schemas | `CORE` | `RETAIN` | already generic and SHA/provenance-oriented |
| Source discovery execution | `source_intake.py` + wrappers | `CORE` + Profile hooks | `GENERALIZE` | generic engine exists; query/window/completeness policy belongs to Profile |
| Screening contracts | shared `screening-*` schemas/scripts | `CORE` | `RETAIN` | already Weekly/Special compatible |
| Evidence contracts | shared Evidence schemas/scripts | `CORE` | `RETAIN` | already substantially canonical |
| Candidate materialization/matrix | generic candidate scripts | `CORE` | `RETAIN` | comparison mechanics are reusable; materiality semantics need Profile input |
| Candidate Selection | `candidate_selection_gate.py` + shared schema | `CORE` | `GENERALIZE` | internal auditable checkpoint; Human interaction policy must normalize |
| Architecture Input/validation | generic architecture scripts/schema | `CORE` | `RETAIN` + `GENERALIZE` | generic basis exists; editorial constraints/profile policy need explicit hook |
| Architecture proposal application | Weekly/Special orchestration wrappers | `CORE` + Profiles | `MERGE` | common mechanics with duplicated edition-specific state/branch wrappers |
| Draft Packages / Article Draft Result | shared schemas/build/validate/render scripts | `CORE` | `RETAIN` | one of the strongest existing Core areas |
| Issue synthesis | shared synthesis schema/validator; edition finalizers | `CORE` + Profile + Publication | `GENERALIZE` | shared contract exists, but Weekly/Special assembly semantics diverge |
| Final source assembly | `finalize_weekly_issue.py`, `finalize_special_validated_draft.py` | `PUBLICATION_PROFILE` + Profile hooks | `MERGE`/`GENERALIZE` | common invariants mixed with Weekly/Special reader-format policy |
| TeX/PDF build & log checks | Weekly/Special build workflows/scripts | `PUBLICATION_PROFILE` | `GENERALIZE` | build invariants are shared; templates/page policy differ |
| Visual QA | Special mature checks/repair history; Weekly visual review | `PUBLICATION_PROFILE` | `GENERALIZE` | shared render-first QA contract should absorb learned Special guards |
| Freeze / Release identity | `release_identity.py`, issue-only workflows | `PUBLICATION_PROFILE` | `RETAIN` + `MERGE` | issue-only identity helper already shared; workflows/docs still drift |
| Pipeline state lifecycle | Weekly/Special state schemas/scripts | `CORE` + Profile state | `MERGE` | lifecycle/machine-gate spine overlaps; temporal fields and Human policy differ |
| Human Gate engine | mature Special model vs older Weekly model | `CORE` | `MERGE` | target: Architecture Review + Publication Preview + on-demand Exception Gate |
| Autonomous advance-to-gate | policy in docs, no generic controller | `CORE` | `ADD` | major liveness gap |
| Materiality Ledger | partial dispositions across stages | `CORE` + Profile completeness | `ADD` | Issue #166 requires explicit end-to-end traceability |
| Completeness audit | Period supplemental/coverage mechanisms; Weekly carry-over | Profiles | `GENERALIZE`/`ADD` | mechanism common, semantics profile-specific |
| Temporal policy abstraction | Weekly resolver + Special explicit coverage | Profiles | `ADD` | thematic scope is currently forced into bounded windows |
| Weekly carry-over | carry-over ledger scripts/workflows | `WEEKLY_PROFILE` | `RETAIN` | must remain a profile hook, not leak into Core |
| Period consistency | `special_period_consistency*` | `PERIOD_PROFILE` | `RETAIN` + `GENERALIZE` | useful bounded-period guard, not global Core despite historical filename |
| Thematic lineage completeness | no complete current implementation | `THEMATIC_PROFILE` | `ADD` | SP001 requires this |
| Reusable Evidence corpus | edition-local evidence dominates | `SERIES_LAYER` + `CORE` | `ADD` | required for Foundations-style repeated source use |
| Series architecture / lineage graph | Foundations planning doc only | `SERIES_LAYER` | `ADD` | must remain separate from per-edition state |
| Review Finding / Repair Set | Issues + edition repair scripts | `CORE` quality layer | `ADD` | Pilot feedback needs structured classification path |
| Historical repair chains | many versioned `revise_special_*` scripts/workflows | `LEGACY_REPLAY` | `REMOVE/ARCHIVE` later | extract invariants/tests first; do not delete in Phase 0 |

---

## 5. Shared schemas: existing Core to retain

The current `schemas/` directory already contains a broad common vocabulary. Tests explicitly verify that important shared schemas accept both Weekly IDs and Special IDs.

### 5.1 Raw / discovery / Screening

Representative shared schemas:

- `collector-instruction.schema.json`
- `collector-run.schema.json`
- `raw-source-index.schema.json`
- `source-intake-acceptance.schema.json`
- `screening-record.schema.json`
- `screening-run-package.schema.json`
- `screening-batch-result.schema.json`

Ownership: `CORE`  
Disposition: `RETAIN`

The schema-level decision should be preserved: issue identity is data, not a reason to fork the Screening vocabulary.

### 5.2 Evidence

Representative shared schemas:

- `evidence-task.schema.json`
- `evidence-execution-package.schema.json`
- `evidence-run.schema.json`
- `evidence-card.schema.json`

Ownership: `CORE`  
Disposition: `RETAIN`

Existing strengths to preserve:

- exact task/prompt SHA binding;
- source-reference integrity;
- stable event identity;
- separate claim/metric/limitation evidence;
- provenance around model/provider/tool execution;
- resumable accepted runs;
- explicit candidate/hold/inspection/reject outcomes.

### 5.3 Selection / Architecture

Representative shared schemas:

- `candidate-selection-decision.schema.json`
- `issue-architecture-plan.schema.json`

Representative scripts:

- `materialize_candidate_records.py`
- `build_candidate_matrix.py`
- `candidate_selection_gate.py`
- `build_architecture_input.py`
- `validate_issue_architecture.py`

Ownership: `CORE`  
Disposition: `RETAIN` with Profile hooks / Human Gate normalization

The algorithms already separate deterministic comparison from editorial role assignment. v2 should not regress into an opaque ranking score.

### 5.4 Drafting / synthesis

Representative shared schemas/scripts:

- `article-draft-package.schema.json`
- `article-draft-result.schema.json`
- `build_draft_packages.py`
- `validate_article_draft.py`
- `render_article_draft_tex.py`
- `merge_generated_bibliography.py`
- `issue-synthesis-result.schema.json`
- `validate_issue_synthesis.py`

Ownership: `CORE` for structured semantic contracts; `PUBLICATION_PROFILE` for final rendering/layout decisions.  
Disposition: `RETAIN` / `GENERALIZE` at assembly boundary.

This layer is already aligned with the v2 objective that models produce structured editorial results rather than unconstrained final LaTeX.

---

## 6. Shared Python implementations already used by Special

### 6.1 Source Intake

`scripts/source_intake.py` is the generic collector engine.

`scripts/special_source_intake.py` is already a specialization layer over that engine. It adds retrospective-window behavior such as monthly arXiv partitioning and explicit coverage-audit warnings while using the shared intake implementation.

Classification:

- generic fetch/run/provenance machinery: `CORE / RETAIN`;
- bounded-period partition/query policy: `PERIOD_PROFILE / GENERALIZE`;
- current Special wrapper itself: compatibility/profile adapter; may disappear from the future hot path after a first-class profile interface exists.

Important constraint:

> A broad intake execution is a discovery seed, not proof of completeness.

This is already acknowledged by the Special wrapper and must become a general Core/Profile contract through the Materiality/completeness work.

### 6.2 Screening and Evidence runners

Representative generic scripts:

- `prepare_screening_run.py`
- `validate_screening_result.py`
- `merge_screening_results.py`
- `accept_screening_results.py`
- `build_evidence_tasks.py`
- `prepare_evidence_run.py`
- `validate_evidence_run.py`
- `merge_evidence_runs.py`
- `accept_evidence_results.py`

Special adapters such as `prepare_special_evidence_run.py` explicitly delegate to the canonical generic implementation and mainly adjust issue-ID/path context.

Classification:

- generic runners: `CORE / RETAIN`;
- edition-specific wrappers: `GENERALIZE`, then remove from future hot path where profile resolution can supply the difference directly.

### 6.3 Selection and Architecture

`apply_special_selection_and_propose_architecture.py` directly imports and uses:

- `build_candidate_matrix`
- `candidate_selection_gate`
- `build_architecture_input`
- `validate_issue_architecture`

The wrapper supplies Special-specific page constraints, reviewed editorial grouping, Special state transition checks, and filesystem paths.

Classification:

- matrix/selection/input/validation mechanics: `CORE / RETAIN`;
- page budget / allowed package policy: Profile or Publication Profile hook;
- state/path/branch orchestration: `CORE / MERGE` through a profile resolver;
- the Special wrapper: transitional adapter, not evidence that a separate Selection/Architecture engine is required.

---

## 7. Pipeline state and lifecycle

Weekly and Special state schemas use essentially the same coarse lifecycle and machine-gate vocabulary, but encode different temporal and Human Gate assumptions.

### 7.1 Shared candidate Core

Common concepts suitable for one Core state model:

```text
ISSUE_INITIALIZED
DISCOVERY_COLLECTED
CANDIDATES_NORMALIZED
EVIDENCE_REVIEWED
SELECTION_COMPLETE
ARCHITECTURE_ESTABLISHED
DRAFT_COMPLETE
VALIDATED_DRAFT
RELEASE_CANDIDATE
FROZEN
```

Common machine checkpoints include Raw preservation, candidate inventory, Evidence normalization, Selection, Architecture, draft, claim/chronology validation, build, visual review, and Freeze.

Ownership: `CORE`  
Disposition: `MERGE`

### 7.2 Weekly-only state

Weekly calendar/state currently owns:

- Friday 18:00 `America/New_York` cutoff;
- cutoff-to-cutoff editorial window;
- intake split boundary;
- previous collection anchor as provenance continuity;
- rolling issue resolution.

Ownership: `WEEKLY_PROFILE`  
Disposition: `RETAIN`, extracted from generic state semantics.

### 7.3 Retrospective-only state

Special currently owns:

- explicit `coverage.start/end`;
- `retrospective_as_of`;
- edition kind;
- historical-granularity configuration.

For bounded Retrospective Period editions these are valid `PERIOD_PROFILE` semantics.

The current mistake is requiring equivalent bounded-window fields for all Thematic editions.

### 7.4 Human Gate drift inside state

Weekly's state schema still encodes explicit Human Selection/Freeze gates, whereas current Special state encodes:

- Architecture Review Human Gate;
- Publication Preview Human Gate;
- Selection as internal checkpoint;
- Visual Review/Freeze/Release as deterministic transitions authorized by exact Publication Preview bytes;
- on-demand Exception Gate.

Ownership: `CORE`  
Disposition: `MERGE` during Phase 1.

The target state model must distinguish machine checkpoints from user-interaction gates instead of letting edition history define both with the same flags.

---

## 8. Temporal and completeness policy: Profile territory

### 8.1 Weekly Profile

Retain as profile semantics:

- rolling editorial window;
- cutoff/currentness;
- `LATE_BREAKING` treatment;
- `HOLD_OUT` / `WATCHLIST` carry-over obligations;
- momentum/community context;
- reader-facing `why this week`.

Representative current components:

- `weekly_pipeline.py`
- `initialize_weekly_carryover_ledger.py`
- `validate_weekly_carryover_ledger.py`
- `generate_grok_trend_run.py`

Disposition: primarily `RETAIN`, with orchestration decoupling.

### 8.2 Retrospective Period Profile

Retain/generalize:

- explicit bounded coverage;
- present-day retrospective interpretation separated from event period;
- period-specific coverage audit;
- chronology and temporal-skew validation;
- cross-month / half-year / annual synthesis rules;
- explicit unresolved coverage limitations.

Representative current components:

- `special_period_consistency.py`
- `special_period_consistency_core.py`
- `special_period_consistency_retrospective.py`
- `special_source_intake.py`
- `collect_special_supplemental_sources.py`
- half-year / annual policy docs and validation/repair tests.

Disposition: `RETAIN` and `GENERALIZE` into a clear Period Profile.

Important naming correction:

> `special_period_consistency_core.py` is not global Survey Core merely because its historical filename says `core`; its assumptions are period-oriented and belong to the Period Profile.

### 8.3 Thematic Profile

Current implementation is incomplete as a true thematic research profile.

Required `ADD` capabilities:

- research question + explicit inclusion/exclusion contract;
- temporal policy independent from bounded coverage;
- seed source discovery;
- backward/forward reference expansion;
- parallel and competing approach discovery;
- lineage/transition/branch coverage audit;
- explicit unresolved lineage questions;
- topic-specific materiality dimensions without topic-specific code forks.

Thematic completeness should answer whether the research question can be responsibly answered, not whether every month or vendor lane is populated.

---

## 9. Materiality and end-to-end traceability

Issue #166 identifies a missing cross-stage invariant.

Current stages have rich local dispositions, but the repository does not yet provide one canonical ledger proving that a material discovery cannot silently disappear between:

```text
Source Intake
  -> Screening
  -> Evidence / duplicate / hold / explicit exclusion
  -> Candidate Selection
  -> Architecture
  -> Draft / chronology / synthesis / explicit reader-facing exclusion
```

### 9.1 New Core component

Provisional name: **Materiality Ledger**.

Ownership: `CORE`  
Disposition: `ADD`

Core responsibilities:

- stable source/discovery identity;
- one explicit disposition at each required transition;
- duplicate/lifecycle links rather than silent deletion;
- explicit material exclusion rationale;
- hold/uncertainty state;
- downstream selected/architecture/use references;
- machine detection of silent drop;
- Architecture Review compression summary.

### 9.2 Profile responsibilities

Profiles define what completeness means and which materiality dimensions must be audited.

Examples:

- Weekly: window + carry-over/current momentum obligations;
- Period: time, actor, technical layer, first-party source, unresolved period gaps;
- Thematic: lineage branches, major transitions, competitors, counterexamples, missing primary sources;
- Foundations Series: volume lineage obligations relative to the shared graph.

The Core should not hard-code one universal checklist that turns Thematic research into a vendor/month matrix.

---

## 10. Entity attribution and claim correctness

Issue #191 demonstrates that source-specific extraction can still be wrong when facts are not bound to the correct subject/entity.

The failure mode is generic:

```text
correct source
+ nearby correct number/feature
+ wrong subject binding
= incorrect Evidence-backed-looking claim
```

Ownership: `CORE` Evidence/claim validation  
Disposition: `ADD`/strengthen existing validation

Required invariant:

- extracted parameter counts, context lengths, licenses, architecture terms, benchmark values, or other technical attributes must be bound to the intended entity/subject;
- comparator/related-product values must retain comparator identity;
- proximity alone cannot promote a token/value into the target entity's attribute;
- regression fixtures from the historical Mistral/Jamba/Ministral findings should survive even after the repair scripts that first fixed them leave the hot path.

---

## 11. Draft finalization and publication boundary

Weekly and Special both consume shared structured drafts, but finalization currently mixes semantic validation with edition-specific source assembly.

### 11.1 Weekly finalization

`finalize_weekly_issue.py`:

- re-verifies article assembly;
- inserts package labels;
- renders deferred frontmatter;
- copies generated bibliography;
- writes final `main.tex` and a hash-bound source manifest;
- explicitly does not Freeze.

Useful shared invariants:

- exact byte/hash verification;
- source manifest;
- deterministic frontmatter rendering;
- dynamic package labels/references;
- generated bibliography integrity;
- Freeze remains downstream.

### 11.2 Special finalization

`finalize_special_validated_draft.py`:

- revalidates approved Architecture and accepted structured drafts;
- constructs post-draft synthesis from exact article bytes;
- checks chronology against Special coverage;
- rejects reader-facing workflow jargon;
- renders article/source/bibliography state;
- advances only semantic validation, leaving PDF/Visual/Freeze downstream.

Useful shared invariants:

- exact accepted-draft binding;
- synthesis may not introduce new external facts;
- reader-facing prose must not expose internal pipeline state;
- semantic validation precedes Publication Preview.

Profile-specific behavior:

- Weekly `This Week`/cover synthesis policy;
- Retrospective cross-period/final synthesis policy;
- Special page/layout structure.

Classification:

- semantic/hash/bibliography/fact-boundary machinery: `CORE / RETAIN or GENERALIZE`;
- document assembly/template/page policy: `PUBLICATION_PROFILE`;
- chronology/synthesis requirements: research Profile hooks;
- the two large finalizer scripts should eventually share primitives rather than being mechanically merged into one conditional-heavy function.

---

## 12. Publication, Visual QA, Freeze, and Release

### 12.1 Release identity

`scripts/release_identity.py` already represents a shared issue-only identity policy for Weekly and Special.

Ownership: `PUBLICATION_PROFILE`  
Disposition: `RETAIN`

The current problem is surrounding legacy documentation/workflows that still encode revision-oriented release paths.

### 12.2 Publication Preview / exact bytes

The current Special path provides the strongest existing contract:

```text
exact publication candidate PDF
  -> SHA-bound Human Publication Preview approval
  -> machine Visual Review record
  -> Freeze
  -> work PR merge
  -> exact artifact verification
  -> issue-only Release
```

Ownership of the gate mechanics: `CORE`  
Ownership of PDF/build/release realization: `PUBLICATION_PROFILE`

Disposition: `GENERALIZE` from the Special implementation and normalize Weekly to the same user-interaction contract unless Phase 1 discovers a concrete Weekly exception.

### 12.3 Preflight and render-first QA

`preflight_final_issue.py` currently has a Weekly-shaped input/manifest contract but enforces broadly useful publication invariants:

- source hash/byte integrity;
- section ordering/label references;
- stale literal internal page references;
- citation ↔ bibliography integrity;
- reader-facing prose vs pipeline jargon.

Ownership: `PUBLICATION_PROFILE`  
Disposition: `GENERALIZE`

Special-specific QA accumulated additional guards through many review/repair cycles. Those guards should be classified into:

1. generic publication invariant → move to canonical preflight/Visual QA;
2. Period/Thematic editorial invariant → Profile validator;
3. layout-template compatibility → Publication Profile;
4. exact historical revision behavior → `LEGACY_REPLAY`.

---

## 13. Workflow orchestration

The `.github/workflows/` inventory shows that workflow duplication is materially higher than schema duplication.

Examples include parallel Weekly/Special flows for:

- preparing Screening;
- applying interactive Screening/Evidence;
- preparing Evidence;
- importing reviewed Source Intake;
- Selection/Architecture;
- draft acceptance/finalization;
- PDF build;
- Freeze/release.

Each wrapper repeatedly performs some combination of:

- issue ID parsing;
- branch/ref resolution;
- state/lifecycle validation;
- path discovery;
- checkout/fetch setup;
- artifact verification;
- calling a generic Python primitive.

### 13.1 Target disposition

Ownership: `CORE` orchestration + Profile hooks  
Disposition: `MERGE`/`GENERALIZE`

Do not immediately replace every workflow with one monolithic YAML file. First create a canonical Python-level orchestration/profile resolver, then make workflows thin dispatch/control surfaces.

Likely Core abstractions:

- edition descriptor/profile resolver;
- canonical source root/work branch/survey root resolution;
- state transition API;
- gate/authorization API;
- artifact SHA/provenance resolver;
- `advance-to-gate` controller.

Profile hooks can then enforce Weekly carry-over or Period coverage without duplicating generic checkout/artifact logic.

### 13.2 Assistant control

`.github/workflows/assistant-control.yml` is an existing safety/control surface for allowlisted workflow dispatch.

Ownership: `CORE` operational control  
Disposition: `RETAIN`, then update only after canonical workflows are known.

Do not expand allowlists opportunistically during refactoring; the control surface should follow settled production entrypoints.

---

## 14. Liveness / advance-to-gate

The repository policy already expects a production session to proceed autonomously through deterministic stages until the requested Human Gate or a genuine Exception Gate.

There is not yet one authoritative controller that makes this expectation executable.

Ownership: `CORE`  
Disposition: `ADD`

Provisional interface:

```text
advance-to-gate --edition <id> --target architecture_review
advance-to-gate --edition <id> --target publication_preview
```

Core state should expose enough information to answer:

- current stage;
- next deterministic action;
- requested terminal Human Gate;
- whether a true editorial Exception is required;
- why execution stopped.

Normal terminal reasons:

```text
HUMAN_GATE_REACHED
EXCEPTION_GATE_REQUIRED
COMPLETE
```

A retryable CI/collector/build failure is not itself a user stop.

---

## 15. Legacy repair and revision chains

### 15.1 Observed structure

The Special history contains long families of versioned repair scripts and workflows, including half-year and annual review/layout/reference/source-specific chains.

A concrete example is the half-year repair path:

- v34 imports v27 and v33, mutates imported globals, calls a prior revision, then restores globals;
- v33 imports v4, v6, and v32, monkey-patches functions/globals, calls v32, then restores them.

This is not merely dead historical code: dedicated tests still exercise late repair behavior and historical failure modes.

### 15.2 Classification

Repair implementation chains:

- ownership: `LEGACY_REPLAY`;
- disposition: eventual `REMOVE/ARCHIVE` from future hot path.

Regression cases and learned invariants:

- ownership: `CORE`, Profile, or `PUBLICATION_PROFILE` depending on defect;
- disposition: `RETAIN` and migrate into stable validators/tests.

### 15.3 No Phase 0 deletion

No repair-chain deletion is authorized by this inventory alone.

Before retiring a chain:

1. identify all workflows/callers/imports;
2. identify tests that encode its historical bug fixes;
3. classify each test as generic/profile/publication/legacy replay;
4. port generic/profile/publication invariants to canonical implementations;
5. preserve exact replay path only where there is a real audit/reconstruction requirement;
6. prove new production does not depend on the old chain.

Artifact immutability does not require hot-path implementation immutability.

---

## 16. Tests and quality-contract ownership

The test suite is a major knowledge asset, especially for Special repair history.

### 16.1 Retain as Core regression families

Examples of generic concerns that should survive refactoring:

- Screening one-decision-per-input completeness;
- task/prompt/hash integrity;
- Evidence source-reference integrity;
- Candidate Selection completeness;
- Architecture primary/supporting assignment integrity;
- Draft Evidence/attribution boundary validation;
- bibliography dedup/conflict validation;
- internal reader-jargon guards;
- exact source/PDF SHA binding;
- entity/subject attribution correctness;
- silent material-drop detection once added.

### 16.2 Retain as Profile regression families

Weekly:

- cutoff/DST/window semantics;
- carry-over obligations;
- Late Breaking/post-cutoff behavior.

Period:

- event date/coverage consistency;
- chronology mapping;
- period synthesis/comparison requirements;
- historical hindsight boundary.

Thematic:

- lineage branch coverage;
- historical attribution / modern terminology boundary;
- competing/parallel approach coverage.

### 16.3 Legacy variance

Exact historical typography, revision ancestry, or one-edition corrective reconstruction may remain `LEGACY_REPLAY` tests rather than blocking future canonical production.

Phase 2 must label this distinction explicitly rather than deleting tests because a repair script is old.

---

## 17. Components to add

Phase 0 identifies the following missing or insufficiently explicit components.

| New component | Owner | Why required |
|---|---|---|
| Edition/Profile descriptor | `CORE` | one canonical resolver for paths, profile, temporal policy, publication profile |
| Generic state/gate API | `CORE` | remove duplicated Weekly/Special lifecycle manipulation |
| `advance-to-gate` controller | `CORE` | make autonomous-to-Human-Gate policy executable |
| Materiality Ledger | `CORE` | detect silent drop across Intake → reader-facing result |
| Completeness Contract interface | Profiles | let Weekly/Period/Thematic define different completion semantics |
| Research temporal policy | Profiles | separate rolling/bounded/open/current-as-of scope |
| Architecture Review summary contract | `CORE` + Profile | expose intake compression, holds, limits, material exclusions at Human Gate 1 |
| Subject/entity binding validation | `CORE` | prevent Issue #191-style wrong attribution |
| Review Finding / Repair Set schema | `CORE` quality layer | convert Pilot Human Review into reusable defect classification |
| Contract identity | `CORE` | record `quality_contract_version` / `pipeline_contract_sha` |
| Reusable Evidence corpus | `CORE` + `SERIES_LAYER` | reuse source facts without copying editorial interpretation |
| Edition-specific Evidence View | `CORE` | bind reusable facts to a specific research question/materiality role |
| Series lineage/dependency graph | `SERIES_LAYER` | support multi-volume evolving Foundations architecture |
| Series research debt / unresolved questions | `SERIES_LAYER` | prevent per-volume state from losing cross-volume uncertainty |

---

## 18. Preliminary ownership by repository surface

### 18.1 Docs

| Surface | Ownership | Disposition |
|---|---|---|
| `editorial-specification.md`, style guide | `CORE`/Publication policy | `GENERALIZE` authority references during Phase 1 |
| `weekly-pipeline-design-v0.1.md` | `WEEKLY_PROFILE` + historical Core design | `MERGE`/partly supersede |
| `weekly-pipeline-implementation-status.md` | implementation history | `RETAIN` as status/history, not sole contract |
| `special-editions.md` | Period/Thematic profile policy | `GENERALIZE` |
| `special-human-gates.md` | candidate Core gate contract | `GENERALIZE` to all production |
| `half-year-retrospective-specials.md` | `PERIOD_PROFILE` | `RETAIN` |
| `annual-retrospective-specials.md` | `PERIOD_PROFILE` | `RETAIN` |
| `release-identity-policy.md` | `PUBLICATION_PROFILE` | `RETAIN` as current identity authority |
| `weekly-release-process.md` | publication implementation + legacy drift | `MERGE`/update in Phase 1 |
| `thematic-special-backlog.md` | editorial planning, not pipeline | `RETAIN` |
| `generative-ai-foundations-special-series.md` | `SERIES_LAYER` design input | `RETAIN` |

### 18.2 Config

| Surface | Ownership | Disposition |
|---|---|---|
| `config/weekly-pipeline.json` | `WEEKLY_PROFILE` + some Core policy | `GENERALIZE` |
| `config/special-pipeline.json` | Period/Thematic + some Core policy | `GENERALIZE` |
| prompt configs | `CORE` semantic stage + Profile variants | `RETAIN`, normalize ownership later |
| collector configuration | `CORE` engine + Profile query policy | `GENERALIZE` |

### 18.3 Schemas

| Surface | Ownership | Disposition |
|---|---|---|
| shared collector/Screening/Evidence/Draft schemas | `CORE` | `RETAIN` |
| `weekly-pipeline-state.schema.json` | Core + Weekly Profile | `MERGE` |
| `special-pipeline-state.schema.json` | Core + Period/Thematic policy | `MERGE` |
| `special-edition-manifest.schema.json` | Profile descriptor precursor | `GENERALIZE` |
| `weekly-release-manifest.schema.json` | Publication | `GENERALIZE` to common release/freeze manifest where practical |

### 18.4 Workflows

| Family | Ownership | Disposition |
|---|---|---|
| generic `screening-contract.yml`, `evidence-contract.yml`, pipeline-contract tests | `CORE` | `RETAIN` |
| Weekly/Special prepare/apply/import wrappers | Core orchestration + Profile hooks | `MERGE` after resolver exists |
| Special Architecture approval / Publication Preview flows | Core gate mechanics + Publication | `GENERALIZE` |
| Weekly/Special build flows | Publication | `GENERALIZE` |
| issue-only release contract workflows | Publication | `RETAIN`/`MERGE` |
| old revisioned release workflows | `LEGACY_REPLAY` | future `REMOVE/ARCHIVE` after dependency audit |
| annual/half-year/versioned repair workflows | `LEGACY_REPLAY` | future `REMOVE/ARCHIVE` after invariant extraction |
| edition-named repair/capture workflows | `LEGACY_REPLAY` | isolate/archive after replay decision |

---

## 19. Phase 1 input: contract drifts requiring explicit resolution

The inventory identifies these contract questions for Phase 1 rather than silently deciding them during code edits.

1. **Human Gates** — old Weekly Selection/Freeze vs current Special Architecture Review/Publication Preview.
2. **Public release identity** — issue-only policy vs older revision-oriented Weekly/Special workflows/docs.
3. **State ownership** — shared lifecycle/machine gates vs edition-specific calendar fields.
4. **Thematic scope** — current bounded `coverage` requirement vs open/current-as-of research.
5. **Completeness** — collector success / local stage completion vs profile-defined coverage + materiality traceability.
6. **Candidate Selection status** — auditable internal approval metadata vs separate Human stop.
7. **Architecture role vocabulary** — which roles are Core and which are Weekly/Period/Thematic editorial vocabulary.
8. **Synthesis** — shared structured post-draft synthesis vs profile-required final synthesis forms.
9. **Publication assembly** — common integrity/preflight vs Weekly/long-form templates and page policies.
10. **Visual Review** — machine checkpoint name vs user-interaction gate semantics.
11. **Freeze/Release authorization** — exact Publication Preview bytes as authority vs older standalone approvals.
12. **Production startup** — Special-specific bootstrap vs a generic edition/profile bootstrap.
13. **Contract provenance** — no single current `quality_contract_version` / `pipeline_contract_sha` binding across artifacts.

---

## 20. Phase 0 conclusion

Phase 0 supports the architecture proposed in `docs/survey-production-core-v2-improvement-plan.md`, with one important implementation refinement:

> **Build v2 by converging around the generic mechanisms that already exist, not by creating a second generation of parallel generic modules.**

The preferred migration pattern is:

```text
existing generic shared primitives
       ↓ retain
explicit Core ownership + stable contracts
       ↓
profile resolver / hooks
       ↓
normalized orchestration + state/gates
       ↓
Weekly / Period / Thematic production
```

while the Special repair history follows:

```text
historical repair chain
       ↓ inspect
failure invariant / regression fixture
       ↓ promote
Core / Profile / Publication validator
       ↓
legacy implementation leaves future hot path
```

No current evidence justifies preserving independent Weekly and Special Screening/Evidence engines. Conversely, no current evidence justifies collapsing Weekly rolling semantics, Retrospective bounded-period completeness, and Thematic lineage research into one universal editorial policy.

Phase 1 should therefore normalize authority and contract boundaries before any substantial implementation rewrite.

## 21. WU-001 exit decision

WU-001 exit condition is satisfied when this inventory is committed and checked against current `main` because:

- major current production families have an ownership/disposition classification;
- existing shared Core mechanisms are identified;
- profile-specific temporal/completeness behavior is separated conceptually;
- publication and Human Gate drift is identified for Phase 1;
- repair-chain removal candidates have explicit dependency/regression caveats;
- missing v2 components are listed rather than being hidden inside implementation work.

The next work unit is **Phase 1 contract normalization**, beginning with an authority/drift table and a candidate canonical contract hierarchy.
