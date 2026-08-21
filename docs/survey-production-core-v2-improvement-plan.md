# Survey Production Core v2 — Compilation System Improvement Plan

Status: `WORKING PLAN / implementation guide`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Base `main`: `2086b396d2f30103d9292b722891be436cd28db5`  

## 1. Purpose

This document defines the working direction for redesigning and consolidating the compilation system of the Japanese Generative AI Technical Survey.

The objective is not to create a new Special-only pipeline. The objective is to distill the strongest mechanisms already learned from both the Weekly pipeline and the fifteen completed Retrospective Special editions into a shared production architecture that can support several different editorial modes without erasing their differences.

The target architecture is:

```text
Survey Production Core v2
  + Research / Editorial Profile
  + Publication Profile
  + optional Series Research Layer
```

The system must support at least:

- rolling Weekly issues;
- bounded Retrospective Period Specials, including future monthly / half-year / annual editions if needed;
- cross-temporal Thematic Specials;
- multi-volume thematic research series such as `Generative AI Foundations`;
- reproducible publication, review, Freeze, and Release provenance;
- cross-session autonomous progression to an explicitly requested Human Gate.

The design priority remains:

```text
Correctness > Traceability > Coverage > Speed
```

The purpose of this work is to improve the future production system. It is not a campaign to rewrite or re-release already frozen historical editions.

---

## 2. Revalidation conclusion

The direction described in this plan was revalidated against current `main` before this branch was created.

The conclusion is that the proposed architecture is appropriate, with several explicit constraints recorded below.

### 2.1 Why a shared Core is justified

Weekly and Special already implement substantially overlapping production stages:

```text
Source Intake / Discovery
  -> Screening / normalization
  -> Evidence verification
  -> Candidate comparison / Selection
  -> Architecture
  -> structured drafting
  -> claim / chronology / attribution validation
  -> deterministic rendering / PDF build
  -> visual review
  -> Freeze / Release provenance
```

Weekly currently has the more mature generic Screening, Evidence, structured Draft Package, Evidence-reference, attribution, bibliography, and deterministic rendering contracts.

Special currently has the more mature two-Human-Gate model, autonomous progression expectation, retrospective synthesis discipline, render-first Visual QA, repair history, and accumulated Human Review lessons.

Therefore reuse should be bidirectional. `Survey Production Core v2` is a convergence of Weekly and Special knowledge, not a Special pipeline reused by Weekly.

### 2.2 Why Profiles are necessary

The research problem is materially different among edition classes.

A Weekly issue asks what is materially relevant inside a rolling current editorial window and must preserve carry-over / late-breaking semantics.

A Retrospective Period issue asks what is necessary to reconstruct a bounded period and must test temporal, actor, technical-layer, and chronology coverage.

A Thematic issue asks what is necessary to answer a research question across an open or differently bounded history and must test lineage, branch, transition, and competing-approach coverage.

A multi-volume Foundations series additionally has evolving series architecture, cross-volume dependencies, repeated source reuse, and a lineage graph that cannot be reduced to one edition state.

These differences should be expressed as Profiles or an outer Series layer, not as edition-specific repair scripts inside the common Core.

### 2.3 Current implementation proves that temporal policy must be separated from thematic scope

The current Special manifest validator accepts `RETROSPECTIVE_PERIOD` and `THEMATIC`, but both are still required to provide `coverage.start`, `coverage.end`, and `coverage.retrospective_as_of`, and the current plan turns both into explicit collection windows.

That is natural for `2025-H1` or `2023-Y`, but artificial for topics such as:

- Perceptron to modern neural learning;
- GAN to Diffusion;
- the history of Chinese Generative AI ecosystems;
- Vision / Multimodal AI across several decades.

The v2 contract must therefore separate the research question from temporal policy.

A target model is:

```text
research_scope
├─ question
├─ inclusion
├─ exclusion
├─ scope_dimensions
└─ temporal_policy
```

Candidate temporal policies include:

```text
ROLLING_WINDOW
BOUNDED_PERIOD
OPEN_HISTORY_AS_OF
CURRENT_STATE_AS_OF
```

The exact schema may change during implementation, but the separation itself is an invariant.

### 2.4 Current contract drift justifies normalization before refactoring

Current repository documents do not describe one perfectly unified contract.

For example, the current public release identity policy makes post-legacy Weekly and Special releases issue-only, while older Weekly release documentation still describes revisioned tags and revision-bearing public identity.

Likewise, the legacy Weekly pipeline design uses Candidate Selection and Freeze as explicit Human Gates, while current Special production has converged on Architecture Review and Publication Preview.

Therefore the first implementation activity must be contract normalization. Code consolidation must not begin by choosing one stale document and mechanically generalizing it.

### 2.5 Materiality traceability is a Core concern, but completeness semantics are profile-specific

Issue #166 demonstrates that broad Source Intake alone does not prove coverage. Thousands of intake records can still collapse into a narrow known-event narrative if material discoveries silently disappear between stages.

The common Core must therefore enforce end-to-end disposition / traceability for material information.

However, the definition of `material` and the completeness audit differ by Profile:

| Profile | Primary completeness question |
|---|---|
| Weekly | Did the editorial window and carry-over obligations receive adequate current coverage? |
| Retrospective Period | Were the bounded period's material temporal / actor / technical-layer gaps resolved or explicitly retained as limitations? |
| Thematic | Are the important conceptual branches, transitions, competitors, and counterexamples required to answer the research question covered? |
| Foundations Series | Can the volume responsibly explain its lineage segment and its relationship to the current series graph? |

The Core owns the mechanism. Profiles own the semantics.

### 2.6 Multi-volume research requires reusable evidence without reusable interpretation becoming dogma

The Foundations series is explicitly a directed graph of research lineages rather than a single chronological ladder. A source such as the Transformer paper may legitimately appear in several volumes for different reasons.

Copying separate independent Evidence Cards into every volume would invite factual drift. Reusing the entire previous editorial interpretation would create a different failure: historical significance would become inherited without being re-evaluated for the new research question.

The target separation is therefore:

```text
Canonical Source
      ↓
Reusable Evidence
      ↓
Edition-specific Evidence View
      ↓
Edition-specific editorial interpretation
```

Reusable facts may include source identity, hashes, bibliographic metadata, verified method facts, verified experiment facts, and directly supported limitations.

Edition-specific interpretation includes why a source matters to the current question, its lineage role, Core / Bridge / Context classification, inheritance / abandonment claims, and reader-facing synthesis.

Principle:

> Facts may be reused. Historical significance and lineage interpretation remain question-specific and evidence-backed.

---

## 3. Additional constraints adopted by this plan

### 3.1 The improvement branch is not the production source of truth

`refactor/survey-production-core-v2` is the design and implementation branch for this improvement program.

Existing repository policy says current `main` is the operational source of truth for production sessions. That rule should remain intact.

Therefore:

1. design and implementation work occurs on this improvement branch;
2. coherent v2 candidate changes are reviewed and merged to `main`;
3. W33 and SP001 production sessions start from the resulting current `main`;
4. production sessions must not be told to silently treat this long-lived feature branch as canonical policy.

This prevents cross-session ambiguity and preserves the repository as the resumable state authority.

### 3.2 W33 is not a migration-compatibility test

An existing `weekly/2026-W33-work` branch contains substantial old-pipeline work and currently records a legacy `RELEASE_CANDIDATE` state.

That work is useful as comparison material, but the ability to migrate or resume that exact state under v2 is **not** a primary acceptance criterion.

The intended W33 role is:

> **Weekly Profile First Production Validation**

The new Pipeline should be judged on whether it can produce a correct, traceable, complete, reviewable W33 issue under the new contract.

Legacy W33 artifacts may be compared for:

- Source Intake / coverage;
- Screening and Evidence depth;
- material candidates discovered or missed;
- Selection and Architecture choices;
- claim boundaries;
- article structure;
- final PDF quality.

They are not presumed to be valid v2 inputs. If any legacy artifact is reused, it must independently satisfy the new provenance and contract requirements. Complete automatic legacy-state migration remains a low-priority compatibility feature, not a design driver.

### 3.3 W34 eligibility is not a reason to bypass the feedback loop

The W34 editorial window becomes eligible for compilation after **2026-08-22 07:00 JST**.

This means W34 may start after that point; it does not mean it should be compiled before W33 feedback has been evaluated and incorporated.

The intended sequence is:

```text
W33 production validation
  -> findings returned to this improvement effort
  -> Core / Weekly Profile corrections
  -> W34 production validation
```

If W33 evaluation is still in progress after the W34 window becomes available, correctness of the validation sequence takes priority over starting W34 immediately.

### 3.4 W33 / SP001 compilation occurs in separate production sessions

This improvement effort is the design, control, and evaluation context.

Actual edition compilation should occur in separate sessions so that Source Intake, Evidence, drafting, and Human Review history for an edition do not overwhelm the architectural work.

The feedback loop is:

```text
This improvement effort
  -> publish v2 candidate to main
  -> W33 production session
  -> SP001 production session
  -> collect findings / results
  -> return findings to this improvement effort
  -> classify and repair
  -> publish updated contracts to main
  -> W34 / SP002 / SP003 validation sessions
```

The production session completes the issue. This improvement effort decides whether a production finding is edition-local, profile-specific, Core-level, or evidence for a new regression invariant.

---

## 4. Target architecture

```text
                    Survey Production Core v2

 ┌──────────────────────────────────────────────────────┐
 │ Orchestration / state / advance-to-gate             │
 │ Raw provenance / Source registry                    │
 │ Screening / Evidence contracts                     │
 │ Materiality & end-to-end traceability               │
 │ Generic Architecture contract                      │
 │ Structured drafting                                │
 │ Claim / citation / attribution validation          │
 │ Bibliography / rendering / PDF preflight            │
 │ Visual QA / repair contract                        │
 │ Review Finding / Repair Set                        │
 │ Freeze / Release provenance                        │
 │ Quality contract / regression corpus               │
 └─────────────────────────┬────────────────────────────┘
                           │
              ┌────────────┼─────────────┐
              │            │             │
          Weekly       Period        Thematic
          Profile      Profile       Profile
              │            │             │
              │       ┌────┴────┐        │
              │    Monthly Half Annual   │
              │                          │
              └──────────────┬───────────┘
                             │
                     Publication Profile
                     Weekly / Long-form
                             │
                  ┌──────────┴──────────┐
                  │                     │
             standalone              Series
             Thematic            Foundations etc.
                                      │
                              Series Research Layer
                              shared evidence corpus
                              lineage graph
                              volume dependencies
```

Research / Editorial Profile and Publication Profile should remain conceptually separate. Editorial scope should not be coupled to layout solely because today's Weekly and Special products happen to use different visual forms.

---

## 5. Core ownership and Profile ownership

### 5.1 Survey Production Core v2

The common Core should own mechanisms whose correctness does not depend on the edition's research question:

- immutable Raw provenance;
- canonical source identity and source registry;
- collector / acquisition provenance;
- Screening contracts and completeness accounting;
- deterministic Evidence tasks and reusable Evidence records;
- stable Evidence references;
- Materiality Ledger / disposition traceability;
- generic Architecture input/output validation;
- structured Draft Packages and Draft Results;
- source / subject / entity attribution checks;
- claim, metric, limitation, citation, chronology-reference integrity;
- bibliography generation and URL integrity;
- reader-facing normalization of internal pipeline vocabulary;
- deterministic rendering and source assembly;
- PDF preflight;
- Visual QA infrastructure;
- immutable derived repair semantics;
- Review Finding / Repair Set records;
- exact PDF SHA binding;
- Freeze / Release provenance and exact-asset verification;
- quality-contract versioning;
- regression fixtures;
- orchestration / liveness / `advance-to-gate` behavior;
- generic Human Gate and Exception Gate mechanics.

### 5.2 Weekly Profile

Weekly-only or Weekly-dominant semantics include:

- Friday 18:00 `America/New_York` cutoff;
- canonical rolling editorial window;
- issue ID derivation;
- front / back intake partitioning when useful;
- current relevance / `why this week`;
- X trend and community momentum semantics;
- Late Breaking;
- carry-over ledger and explicit re-evaluation obligations;
- current-significance Selection axes;
- Weekly-specific reader-facing architecture such as Lead / Watchlist / Late Breaking when evidence supports them.

### 5.3 Retrospective Period Profile

Period-specific semantics include:

- explicit bounded coverage window;
- `retrospective_as_of`;
- period chronology;
- temporal coverage audit;
- actor / model family / runtime / framework / protocol / agent / multimodal / safety / research-plane coverage as appropriate;
- period-specific synthesis obligations;
- monthly, half-year, annual granularity rules;
- half-year cross-period comparison and reclassification;
- annual story units, trajectories, phase analysis, and year-level synthesis.

The Profile must remain available after the historical backfill project is complete so future bounded retrospectives can still be produced without restoring old repair chains.

### 5.4 Thematic Profile

Thematic-specific semantics include:

- explicit research question;
- `why this Special` rationale;
- inclusion / exclusion boundaries;
- open-history or current-state temporal policy;
- seed-source strategy;
- backward / forward source expansion;
- original / canonical paper discovery;
- parallel and competing approaches;
- bridge technologies;
- lineage / conceptual gap audit;
- Core / Bridge / Context classification when useful;
- inheritance, abandonment, convergence, and retrospective-analogy distinctions;
- historical attribution discipline;
- completeness based on the research question rather than calendar density.

### 5.5 Series Research Layer

A multi-volume series needs outer state beyond one edition:

```text
Series Research Layer
├─ series manifest / architecture version
├─ shared source and evidence corpus
├─ lineage graph
├─ volume dependencies
├─ cross-volume evidence usage
├─ merge / split / resequence planning
├─ unresolved lineage questions / research debt
└─ dated frontier snapshots
```

Series state must not become a mandatory third Human Gate for every volume.

Major series-level structure changes may receive a separate Series Architecture Review when genuinely useful, but normal volume production should still use the standard production Human Gates.

---

## 6. Core production invariants

The following are target invariants to be distilled from existing Weekly/Special behavior and historical defects.

### 6.1 Immutable provenance

Accepted Raw source bytes are immutable. Derived records must preserve source identity and input hashes.

No later stage may rewrite Raw material merely to simplify processing.

### 6.2 No silent material drop

Every item entering the canonical Source Intake / completeness-audit surface receives an explicit downstream disposition.

A material item must be traceable through a path such as:

```text
Source / discovery record
  -> Screening disposition
  -> Evidence / duplicate target / explicit exclusion / HOLD
  -> Selection disposition
  -> Architecture use / chronology / explicit exclusion
  -> reader-facing use or structured rationale for omission
```

Unclassified disappearance is a validation failure.

### 6.3 Collector success is not completeness

A successful collector run proves acquisition execution, not editorial coverage.

Every Profile defines a completeness contract and residual limitations. The pipeline must be able to say `coverage incomplete` without pretending that a large record count is proof of completeness.

### 6.4 Architecture owns synthesis requirements

Cross-article or cross-period synthesis must be represented at Architecture time when the edition requires it.

It must not be bolted on after drafting merely to repair a missing narrative closure.

### 6.5 Structured Evidence before prose

Drafting consumes verified Evidence / Edition Evidence Views rather than treating raw discovery output as authoritative facts.

Claims, metrics, limitations, attribution modes, and subject/entity binding must remain machine-checkable where feasible.

### 6.6 Subject / entity attribution is mandatory

Source-specificity is insufficient if a value is attributed to the wrong subject.

Comparator values, related models, tables, navigation text, or neighboring products must not silently become properties of the target entity.

This invariant generalizes lessons such as Issue #191.

### 6.7 Internal production vocabulary does not leak into published prose by default

Traceability remains in repository provenance, Claim Boundaries, Source Notes, and machine records.

Reader-facing prose should describe uncertainty and evidence boundaries naturally rather than exposing Candidate Inventory, Screening state, Reaction Pass, Draft Package, or internal promotion terminology without reader value.

### 6.8 Render-first QA remains mandatory

Source-level validity does not guarantee a readable publication.

The production candidate must be rendered and inspected for clipping, overlap, hierarchy, pagination, References behavior, blank sections/pages, stale page references, and unexpected layout regressions.

### 6.9 Frozen publications remain immutable

Historical and newly frozen public artifacts are not rewritten by pipeline cleanup.

Post-release correction remains an explicit exceptional path.

### 6.10 Repair knowledge must outlive repair code

A historical repair should survive as some combination of:

- an invariant;
- canonical implementation;
- regression fixture;
- quality-contract rule;
- historical lineage note.

It should not survive solely because a versioned edition-specific repair script remains on the future hot path.

### 6.11 Deterministic stages must not become accidental Human Gates

Once a production session has a target Human Gate, deterministic intermediate states do not justify returning control to the user.

A controller should eventually expose a generic concept such as:

```text
advance-to-gate --target <gate>
```

with terminal reasons such as:

```text
HUMAN_GATE_REACHED
EXCEPTION_GATE_REQUIRED
COMPLETE
```

Retryable technical failures are recovery conditions, not editorial gates.

---

## 7. Human Gate target model

The preferred normal production interaction model for v2 is:

```text
Issue initialization
  -> Source Intake
  -> Screening / Evidence
  -> Candidate Selection (internal auditable checkpoint)
  -> Architecture Proposal
  -> HUMAN GATE 1: Architecture Review
  -> Drafting / validation / layout / build
  -> exact publication candidate PDF
  -> HUMAN GATE 2: Publication Preview
  -> deterministic Visual Review record
  -> Freeze
  -> merge
  -> exact artifact verification
  -> Release
  -> Complete
```

An Exception Gate is raised only when a genuinely new editorial or publication decision is required.

This is already the normal Special model. Applying the same interaction model to Weekly is a target of Contract Normalization and W33 validation, not an excuse to discard Weekly's stronger existing Evidence/Architecture mechanics.

Publication Preview approval must remain bound to exact PDF bytes / SHA-256. Freeze and Release remain auditable state transitions rather than additional routine Human Gates.

---

## 8. Historical corpus and legacy policy

### 8.1 Fifteen Retrospective Specials are the historical learning corpus

The completed corpus is:

- Monthly: `2026-M01` through `2026-M07` — 7 editions;
- Half-year: `2024-H1`, `2024-H2`, `2025-H1`, `2025-H2` — 4 editions;
- Annual: `2020-Y` through `2023-Y` — 4 editions.

Total: 15 editions.

These editions are used to reconstruct defect / repair / invariant history and to build regression assets.

They are not automatically scheduled for corrective re-release.

### 8.2 Future period production and legacy exact replay are separate requirements

The system must preserve the ability to create a **new** bounded Retrospective Period issue later.

Examples could include another monthly issue, a future half-year issue, an additional annual issue, or a custom bounded retrospective if explicitly designed later.

That future-production capability should use:

```text
Survey Production Core v2
  + Retrospective Period Profile
```

This does not require retaining every historical `revise_*_vN.py` chain as canonical production code.

Legacy exact replay, where needed, can rely on:

- frozen commits;
- tags / Releases;
- source/PDF hashes;
- release / freeze provenance;
- isolated compatibility tooling only when necessary.

### 8.3 Existing W33 old-pipeline work is comparison evidence

The old W33 work branch should be preserved until the new W33 validation and comparison are complete.

Do not make it the base branch of the v2 implementation effort and do not require v2 to reproduce its internal state transitions.

---

## 9. Pilot validation program

The v2 system should be validated through real production rather than declared complete after static refactoring.

### 9.1 Validation roles

| Edition | Role |
|---|---|
| Fifteen completed Retrospective Specials | historical learning / regression corpus |
| W33 | first Weekly Profile production validation |
| SP001 | first Thematic Profile production validation |
| W34 | Weekly fix verification and second-week generalization |
| SP002 | Thematic generalization validation #2 |
| SP003 | Thematic generalization validation #3 |

The next three Special productions are referred to in this plan as `SP001` through `SP003` because that is the intended production sequence. Current planning documents name the scoped backlog entries `TS-001` through `TS-003`. The exact canonical production slugs / identifiers and their mapping must be fixed explicitly during Contract Normalization or production promotion rather than silently assumed in code.

### 9.2 W33 acceptance focus

W33 tests whether the new Core + Weekly Profile can execute a real Weekly issue end-to-end with acceptable quality.

Primary questions include:

- Was Source Intake broad enough for the Weekly completeness contract?
- Were carry-over obligations handled explicitly?
- Did material information survive Screening / Evidence / Selection / Architecture?
- Did the new Human Gate model provide enough review information without unnecessary stops?
- Did structured drafting preserve claim and attribution boundaries?
- Did publication machinery produce a clean reader-facing PDF?
- Did autonomous progression stop only at the requested gate or genuine Exception Gate?

Comparison against the old W33 branch is useful but secondary.

### 9.3 SP001 acceptance focus

SP001 tests the new Core + Thematic Profile against a real cross-temporal research question.

Primary questions include:

- Can scope be expressed without an artificial bounded period?
- Does Source Intake expand through the relevant lineage / ecosystem rather than merely search recent news?
- Can completeness be argued using concept / lineage / actor / competing-approach coverage?
- Can the Materiality Ledger explain what was included, merged, held, or excluded?
- Does Architecture represent the research question rather than reproduce a period-retrospective structure?
- Are hindsight and historical attribution handled correctly?
- Does reusable Evidence help without importing prior editorial interpretation as fact?

### 9.4 W34 acceptance focus

W34 verifies that fixes derived from W33 work on a different weekly source set.

The purpose is not merely to publish another issue. It is to test that:

- W33 defects do not recur;
- fixes did not create new regressions;
- the Weekly Profile generalizes across weeks;
- the Core did not accidentally become W33-specific.

### 9.5 SP002 / SP003 acceptance focus

SP002 and SP003 test whether one Thematic Profile can absorb materially different research structures without creating theme-specific repair pipelines.

If one edition requires a new mechanism, the improvement effort must ask whether it is:

- a genuine Core capability;
- a generic Thematic Profile capability;
- a Publication Profile capability;
- a Series-layer capability;
- or an edition-local editorial decision.

A file or module that exists only because one theme could not fit the general contract is a design smell unless the distinction is editorially real and explicitly modeled.

---

## 10. Production-session feedback contract

Production sessions should record findings, but should not prematurely decide that every problem is a Core defect.

A target finding record is conceptually:

```yaml
finding_id:
edition:
stage:

observed_problem:
expected_behavior:
actual_behavior:

evidence:
  artifacts: []
  hashes: []
  review_reference:

production_impact:
workaround_used:
human_intervention_required:
semantic_change_required:
provenance_impact:

provisional_classification:
  edition_local_candidate: false
  profile_defect_candidate: false
  core_defect_candidate: false
  publication_defect_candidate: false
  series_layer_candidate: false

candidate_generic_fix:
regression_candidate:
```

The exact schema should be implemented only after existing review / issue mechanisms are inventoried.

The control / improvement effort performs the final classification:

```text
EDITION_LOCAL
WEEKLY_PROFILE_DEFECT
PERIOD_PROFILE_DEFECT
THEMATIC_PROFILE_DEFECT
PUBLICATION_PROFILE_DEFECT
SERIES_LAYER_DEFECT
CORE_DEFECT
QUALITY_CONTRACT_DEFECT
REGRESSION_REQUIRED
```

The production edition receives the safe repair necessary to continue. Generic repair is implemented in the correct shared layer and protected by regression tests.

---

## 11. Work phases

### Phase 0 — Cross-Pipeline Process Archaeology

Inventory current Weekly and Special production surfaces from current `main`:

- documentation;
- configuration;
- schemas;
- scripts;
- workflows;
- tests;
- renderer / bibliography / release modules;
- assistant-control allowlists;
- historical repair chains;
- relevant issue / Human Review history.

Classify every material component as:

```text
RETAIN
GENERALIZE
MERGE
REMOVE_OR_ARCHIVE
ADD
```

Also classify target ownership:

```text
CORE
WEEKLY_PROFILE
PERIOD_PROFILE
THEMATIC_PROFILE
PUBLICATION_PROFILE
SERIES_LAYER
LEGACY_REPLAY
```

Before removal or replacement, inspect imports, callers, workflows, tests, historical replay requirements, and current production entrypoints.

**Exit condition:** a component map exists and no major production path is being refactored from assumption alone.

### Phase 1 — Contract Normalization

Reconcile distributed Weekly and Special policy into explicit shared and profile contracts.

Target contract set may include:

- Survey Production / Quality Contract;
- Human Gate / liveness contract;
- Weekly Profile Contract;
- Retrospective Period Profile Contract;
- Thematic Profile Contract;
- Publication Profile Contract;
- Series Research Contract.

Resolve known drift, including:

- issue-only public Release identity vs older revisioned Weekly release documentation;
- Weekly legacy Human Gates vs the target Architecture Review / Publication Preview interaction model;
- current Thematic edition definition vs explicit-window-only manifest semantics;
- duplicated or conflicting state meanings.

Introduce contract identity such as:

```text
quality_contract_version
pipeline_contract_sha
```

**Exit condition:** a new implementation can answer which contract owns each production rule.

### Phase 2 — Historical Knowledge Distillation

Use the fifteen completed Specials, W32/W33-era Weekly evolution, and relevant review issues to reconstruct:

```text
Human finding
  -> local repair
  -> generalized repair
  -> regression / side effect
  -> guard
  -> current invariant
```

Distinguish:

```text
EDITION_LOCAL_REPAIR
GENERIC_CONTRACT_DEFECT
POST_RELEASE_CORRECTION
```

Historical differences should be recorded as:

```text
PASS
PASS_WITH_LEGACY_VARIANCE
HISTORICAL_GAP
```

Do not turn historical comparison into an automatic re-release backlog.

**Exit condition:** important recurring repairs have an explicit intended invariant or an explicit reason to remain local/legacy.

### Phase 3 — Core v2 Candidate Design and Minimum Viable Implementation

Implement the smallest coherent vertical slice needed to run W33 and SP001 under the new architecture.

Priority capabilities:

- common orchestration / state concepts;
- profile interfaces;
- Materiality Ledger / traceability;
- normalized Screening / Evidence contracts;
- generic Architecture interface;
- structured drafting / validation reuse;
- publication core reuse;
- Human Gate / Exception Gate mechanics;
- contract version identity;
- finding / regression mechanism sufficient for Pilot feedback.

Avoid a big-bang rewrite. Prefer adapters around proven current code before replacing it.

**Exit condition:** both Weekly and Thematic candidate profiles can be initialized and advanced to Architecture Review through one coherent Core contract.

### Phase 4 — First external production validation

After the v2 candidate is reviewed and merged to `main`, use separate production sessions for:

1. W33;
2. SP001.

These sessions must use current `main` as source of truth.

The improvement branch does not substitute for production policy.

**Exit condition:** each Pilot either completes its intended Human Gate / publication path or produces a clearly recorded Exception / defect that blocks further progress.

### Phase 5 — Cross-Pilot evaluation and first consolidation

Return W33 and SP001 findings to this improvement effort.

For every finding:

1. reproduce / inspect the evidence;
2. classify scope;
3. decide whether the production workaround is acceptable or must be replaced;
4. implement the repair in the narrowest correct layer;
5. add a regression fixture when deterministic recurrence is possible;
6. update contracts if the defect reveals an underspecified invariant.

The value of evaluating W33 and SP001 together is that it prevents one Pilot from defining the Core in its own image.

**Exit condition:** Pilot defects are either fixed, explicitly accepted as edition-local, or left as documented blocking design questions.

### Phase 6 — Second production validation

After first-consolidation changes are merged to `main`:

- compile W34 using the revised Weekly Profile;
- compile SP002 and SP003 using the revised Thematic Profile.

Verify fix persistence and cross-edition generalization.

**Exit condition:** the same generic defect does not require repeated edition-specific repair, and no major Profile requires a hidden fork of the Core.

### Phase 7 — Stabilization and consolidation

Only after representative production validation:

- mark the Core contract stable;
- consolidate documentation;
- remove or archive superseded hot-path repair chains;
- retain necessary legacy replay adapters;
- normalize workflows and state schemas;
- consolidate regression suites;
- document future Weekly / Period / Thematic / Series startup procedures;
- update `AGENTS.md` and session bootstrap documents to point at the new canonical architecture.

**Exit condition:** future sessions can discover one clear source of truth and no longer need historical chat context or version-chain archaeology to know how to compile an edition.

---

## 12. Migration and consolidation principles

### 12.1 Do not optimize for exact legacy-state migration

Compatibility with already frozen artifacts matters. Compatibility with every intermediate legacy state does not.

A legacy state adapter is justified only if it reduces real production or audit risk more than it increases Core complexity.

### 12.2 Prefer vertical replacement over parallel permanent pipelines

During migration, adapters and compatibility layers are acceptable.

The end state should not be:

```text
weekly_pipeline_v1
special_pipeline_v1
special_period_v2
special_thematic_v2
weekly_v2
+ many issue repair scripts
```

The end state should converge on shared Core mechanisms with explicit Profiles.

### 12.3 Do not delete historical provenance to simplify code

Frozen source, release manifests, audit artifacts, tags, and hashes remain historical records even after their producing implementation is retired.

### 12.4 Do not preserve obsolete runtime code merely because provenance is immutable

Publication immutability is an artifact/provenance property, not a requirement that every historical repair implementation remain a canonical future dependency.

### 12.5 Main remains authoritative during a long-running improvement branch

Because Weekly / Special production may continue while this effort is active, the branch must periodically revalidate against current `main` before major implementation or merge decisions.

Do not assume the base SHA listed at the top of this document remains current indefinitely.

---

## 13. Initial acceptance criteria for Survey Production Core v2

The Core should not be called stable until the following are true.

### Architecture / contracts

- [ ] Shared Core responsibilities and Profile responsibilities are explicit.
- [ ] Research scope is independent of temporal policy.
- [ ] Weekly, Retrospective Period, and Thematic Profiles are first-class supported modes.
- [ ] Series-level research state is separate from per-edition production state.
- [ ] Human Gate semantics are unambiguous and cross-session resumable.

### Source / Evidence

- [ ] Raw provenance remains immutable.
- [ ] Collector success cannot be mistaken for completeness.
- [ ] Profile-specific completeness audits exist.
- [ ] Material discoveries cannot silently disappear.
- [ ] Selected / material Evidence reaches Architecture and reader-facing use or an explicit exclusion rationale.
- [ ] Subject/entity attribution is validated for extracted technical facts.
- [ ] Reusable source facts are separated from edition-specific interpretation.

### Draft / publication

- [ ] Structured drafting preserves Evidence and attribution boundaries.
- [ ] Reader-facing prose is separated from internal production vocabulary.
- [ ] Bibliography / URL / source-reference integrity is deterministic.
- [ ] PDF build and render-first Visual QA remain mandatory.
- [ ] Publication Preview binds exact PDF bytes.
- [ ] Freeze / Release preserve exact identity and provenance.

### Orchestration

- [ ] A production request can progress autonomously to the requested Human Gate.
- [ ] Retryable technical failures do not become accidental Human Gates.
- [ ] Genuine editorial exceptions are surfaced as Exception Gates.
- [ ] Repository state alone is sufficient for another session to resume.

### Validation

- [ ] W33 has exercised the Weekly Profile under v2.
- [ ] SP001 has exercised the Thematic Profile under v2.
- [ ] W33/SP001 findings have been evaluated in the improvement effort rather than patched only inside editions.
- [ ] W34 verifies the first Weekly repair set on a different week.
- [ ] SP002 and SP003 verify Thematic generalization across different topics.
- [ ] Historical regression fixtures cover material recurring defects from the completed Special corpus.
- [ ] Frozen historical releases remain unchanged.
- [ ] New bounded Retrospective Period editions remain producible without depending on old repair chains.

---

## 14. Immediate next work

After this plan is established, implementation should proceed in the following order:

1. perform Phase 0 inventory from current `main`;
2. build a contract-drift table for Weekly / Special / Release / Human Gate / state semantics;
3. reconstruct the high-value repair lineage and identify invariants already encoded in tests vs only in repair scripts;
4. define the first Survey Core / Profile contracts;
5. design the minimum vertical slice needed for W33 and SP001;
6. implement and test that candidate on this branch;
7. review and merge the candidate to `main` before starting Pilot production sessions.

Do not begin W33 or SP001 under an unpublished branch contract merely to accelerate the schedule. The production sessions should consume repository policy from `main` after the candidate is ready.

---

## 15. Repository references that anchor this plan

The following current repository surfaces are especially relevant and should be re-read during implementation:

- `AGENTS.md`
- `docs/weekly-pipeline-design-v0.1.md`
- `docs/weekly-pipeline-implementation-status.md`
- `docs/weekly-release-process.md`
- `docs/release-identity-policy.md`
- `docs/special-editions.md`
- `docs/special-human-gates.md`
- `docs/special-session-bootstrap.md`
- `docs/half-year-retrospective-specials.md`
- `docs/annual-retrospective-specials.md`
- `docs/retrospective-special-backfill-status.md`
- `docs/thematic-special-backlog.md`
- `docs/generative-ai-foundations-special-series.md`
- `config/weekly-pipeline.json`
- `config/special-pipeline.json`
- `scripts/weekly_pipeline.py`
- `scripts/special_pipeline.py`
- Issue #166 — broad Source Intake -> materiality -> reader-facing traceability
- Issue #191 — source-specific extraction still requires subject/entity binding
- other historical editorial / pipeline issues discovered during Phase 0 and Phase 2

This document is a working guide, not a substitute for re-reading current `main`. If repository policy changes while this branch is active, the change must be evaluated and this plan amended when it materially affects the target architecture.
