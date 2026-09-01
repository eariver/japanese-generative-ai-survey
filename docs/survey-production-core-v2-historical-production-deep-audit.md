# Survey Production Core v2 — Historical Production Deep Audit

Status: `PHASE 2C OUTPUT / edition-level production-lineage audit`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Companions:
- `docs/survey-production-core-v2-historical-invariants.md`
- `docs/survey-production-core-v2-historical-production-pattern-matrix.md`

## 1. Purpose

The first all-edition pattern matrix proved that all fifteen frozen Retrospective Specials had been represented, but a second audit found that representation depth was uneven. In particular, some Annual rows summarized editorial success without preserving important final-state repair lineage.

This Phase 2C audit therefore uses the frozen edition state itself as the primary historical-production record.

For every edition it inspects at minimum:

- final `pipeline-state.json` lifecycle and Human Gate provenance;
- approved Architecture identity/approval basis recorded by state;
- final validated source revision;
- revision/repair lineage visible in final state;
- issue references explicitly recorded by the final state where present;
- chronology/synthesis behavior where applicable;
- exact PDF/source/control provenance;
- positive behavior to retain;
- failure/repair interaction to convert to invariant/regression knowledge;
- behavior that is only legacy variance.

This remains an architectural learning exercise. Frozen releases are not being rewritten.

## 2. Audit rule

A row is not considered audited merely because the release manifest, page count, or final source version was found.

Minimum evidence for an edition row is:

```text
final pipeline state
  + Architecture approval identity
  + final source revision / repair signal
  + exact publication provenance
  + positive and negative production lesson
```

If the final state directly records an Issue/repair chain, the audit retains it. If a known cross-edition Issue was discovered after the release, it is identified as a later audit lesson rather than retroactively pretending the frozen state contained it.

## 3. Corpus-wide evidence table

| Edition | Final state evidence | Gate/release evidence | Final production lineage evidence | Deep-audit conclusion |
|---|---|---|---|---|
| SP-2026-M01 | `sources/SP-2026-M01/pipeline-state.json` | mature Architecture + exact-byte Publication Preview; issue-only Release | v0.6; Issues #55/#78/#122/#123; mixed local two-column narrative + full-width synthesis/notes; 29 pages below soft target | TOC depth, note-tail layout, bibliography metadata and exact-byte release can be repaired independently without padding |
| SP-2026-M02 | `sources/SP-2026-M02/pipeline-state.json` | mature two-gate model | v0.6; Issues #106/#110; standfirst preservation + bullet normalization; exact control commit recorded | full-width standfirst and local multicol narrative are separate publication invariants; renderer/source bullet ownership must be unambiguous |
| SP-2026-M03 | `sources/SP-2026-M03/pipeline-state.json` | legacy multi-Human-gate state; Freeze authority remained separate | v0.10; explicit retrospective synthesis correction; local final-synthesis spacing guard | final issue synthesis must be a manifest-bound semantic requirement; gate evolution is empirical, not theoretical |
| SP-2026-M04 | `sources/SP-2026-M04/pipeline-state.json` | legacy Selection/Visual/Freeze Human gates | v0.10; Issue #55 final note-tail repair; long revision lineage includes TOC/reference/layout work | generic Technical Notes tail policy must be regression-coupled with TOC, bibliography and mixed-layout invariants |
| SP-2026-M05 | `sources/SP-2026-M05/pipeline-state.json` | legacy Selection/Visual/Freeze gates | v0.12; Issues #50/#54/#55; seven render-confirmed selective Technical Notes tails | local break repair must not become whole-card unbreakability; reader taxonomy and layout are distinct from factual Evidence |
| SP-2026-M06 | `sources/SP-2026-M06/pipeline-state.json` | legacy gate model, issue-only release | v0.9; final Visual preflight corrected five July-specific labels in June; chronology and synthesis revisions before Freeze | template/revision reuse can leak semantic labels from another edition; reader-facing scope labels must derive from canonical edition/profile state |
| SP-2026-M07 | `sources/SP-2026-M07/pipeline-state.json` | oldest modern monthly gate/release shape: Selection/Visual/Freeze/Public Release Human flags; revisioned Freeze record | v0.8; render-first Needspace rollback after nearly empty page | gate/release complexity and global spacing guards are legacy variance; render-first QA is durable |
| SP-2024-H1 | `sources/SP-2024-H1/pipeline-state.json` | mature two-gate exact-byte model | v0.17; 47 references; chronology; Issues #153/#54/#191; repeated reference compaction; subject/component/variant binding repair; rejected v0.16 superseded before build | correctness repair must preserve prior fixes as a coupled set; reference compression and entity binding can require many revisions without changing publication identity |
| SP-2024-H2 | `sources/SP-2024-H2/pipeline-state.json` | mature two-gate model; Architecture approval explicitly authorized autonomous work to Publication Preview | audited 5,955-record intake; 85-task Evidence; v0.12; Issue #191 V3 component/variant/property binding; compact chronology retained | strong evidence that broad research, long-form synthesis and exact entity binding must coexist; source-specific prose alone is not enough |
| SP-2025-H1 | `sources/SP-2025-H1/pipeline-state.json` | mature two-gate model | frozen run records 31 curated primary sources / 31 Evidence; v0.4; event-only Technical Notes tail repair | final state demonstrates coherent publication from a narrow reconstruction; later Issue #166 audit demonstrates that publication plausibility did not prove research completeness |
| SP-2025-H2 | `sources/SP-2025-H2/pipeline-state.json` | mature two-gate model | v0.8; Issue #54 final taxonomy/casing repair; preceding known #139/#140 lineage around source-specific fallback and reference boilerplate | reader labels must be human-facing without mutating Evidence; fallback must fail closed; reference density is publication policy |
| SP-2020-Y | `sources/SP-2020-Y/pipeline-state.json` | mature two-gate model | v0.19; chronology 28 events; many reference-pagination revisions v0.11–v0.18 explicitly semantic-neutral; final Issue #55 tail repair | sparse historical period can remain compact; layout iteration should be provably semantic-neutral and identifier/URL stable |
| SP-2021-Y | `sources/SP-2021-Y/pipeline-state.json` | mature two-gate model | v0.8; chronology 45 events; final Issues #122/#55 compact TOC + targeted Needspace relaxation | annual synthesis/chronology works, but long-form navigation and note-tail rules remain coupled publication regressions |
| SP-2022-Y | `sources/SP-2022-Y/pipeline-state.json` | mature two-gate model | v0.10; chronology 59 events; explicit issue refs #54/#78/#122/#139/#140/#191/#271/#272; direct entity binding + `needspace` dependency repair | strongest single-edition proof that entity, bibliography, TOC, fallback, empty-wrapper, chronology-source and layout fixes interact and require a regression set |
| SP-2023-Y | `sources/SP-2023-Y/pipeline-state.json` | mature two-gate model | v0.15; chronology 75 events / 3 unresolved dates; #140 final reference compaction; #139/#191 residual repair; earlier annual review lineage includes chronology-source/empty-wrapper concerns | objective chronology can scale while unresolved dates remain unknown; compact source mapping and subject binding must survive final compaction |

## 4. Edition notes

### 4.1 SP-2026-M01

Evidence:
- final state is `FROZEN`;
- Architecture approval explicitly added an independent closing synthesis;
- final source is v0.6, 29 pages;
- final layout revision cites Issues #55, #78, #122 and #123;
- Publication Preview approval binds exact PDF SHA and authorizes Visual Review, Freeze, merge and Release;
- build records the control commit and style hash.

Positive pattern:
- a Monthly can fall below an earlier soft page target after removing low-information layout without being incomplete by definition;
- TOC, references, Technical Notes and synthesis can be repaired while accepted semantic drafts remain fixed.

Regression lesson:
- page-count controls must not incentivize a low-density TOC continuation;
- source title metadata must survive Evidence → References;
- note-tail protection must remain local rather than creating blank pages.

### 4.2 SP-2026-M02

Evidence:
- final state uses the mature two-Human-Gate contract;
- final source v0.6 records Human Visual Review Issues #106/#110;
- correction preserves standfirsts as full-width blocks and normalizes manual bullet markers;
- exact PDF SHA and control commit are recorded.

Positive pattern:
- document structure can explicitly separate full-width chapter heading/standfirst from balanced local two-column body.

Regression lesson:
- document builders must preserve all semantic/article blocks when doing layout reconstruction;
- renderer list markers and source-side manual markers must not both own the same bullet.

### 4.3 SP-2026-M03

Evidence:
- final state still has Human Selection, Architecture, Visual Review and Freeze flags;
- final state records an explicit `retrospective_synthesis_correction` generated from selected Evidence only with no later-period facts;
- v0.10 final revision is a local spacing guard around that synthesis.

Positive pattern:
- final issue-level synthesis can be repaired from accepted Evidence without replacing feature architecture.

Regression/evolution lesson:
- final retrospective synthesis is mandatory semantic content, not decoration;
- the later two-gate model is justified by concrete earlier gate friction.

### 4.4 SP-2026-M04

Evidence:
- legacy multi-gate state;
- final v0.10 reason is a generic Issue #55 note-tail repair after render inspection;
- provenance history shows many earlier immutable source revisions rather than mutation in place.

Positive pattern:
- immutable review revisions plus exact hashes make iterative publication correction auditable.

Regression lesson:
- local tail fixes must be tested against earlier TOC/reference/layout corrections; latest revision builders cannot reconstruct only the most recently changed concern.

### 4.5 SP-2026-M05

Evidence:
- final v0.12;
- build records review issues #50/#54/#55;
- final reason states seven render-confirmed selective grouped tails on a stable earlier base;
- provenance history shows progressive layout revisions rather than one monolithic repair.

Positive pattern:
- Technical Notes may remain breakable while preserving reader continuity.

Regression lesson:
- taxonomy label cleanup and layout repair must not alter structured provenance fields;
- one-card/one-page protection is too strong; use localized continuation quality rules.

### 4.6 SP-2026-M06

Evidence:
- final v0.9;
- final visual-preflight reason explicitly finds five July-specific Theme Synthesis column labels inside the June Special;
- state keeps exact build/control provenance.

Positive pattern:
- pre-Human render inspection catches semantic publication defects not found by schema validation.

Regression lesson:
- edition labels, month names and reader-facing scope text must be generated from canonical state/profile, not copied from a neighboring edition/template;
- this is a generic `derived reader scope identity` invariant, not a June-only typo repair.

### 4.7 SP-2026-M07

Evidence:
- state retains the older Human-gate shape including public Release flag;
- final v0.8 removes only the subsection `Needspace` that caused a nearly empty page;
- final Freeze still records a release revision.

Positive pattern:
- render-first QA can isolate the smallest safe layout change.

Legacy variance:
- revisioned public/Freeze identity and extra Human stops should remain historical evidence, not future Core semantics.

### 4.8 SP-2024-H1

Evidence:
- mature two-gate state;
- approved Architecture explicitly includes a three-page concluding synthesis;
- final v0.17 restores an OpenELM subject boundary after v0.16 while preserving LongRoPE, Command R/R+ and DeepSeek corrections;
- final state names a shared V3 subject/component/variant/property binding contract;
- references progressed through title enrichment, compaction, multicol/ragged-right/common-urldate revisions;
- final PDF 48 pages despite a much larger planning envelope.

Positive pattern:
- a longer Half-year issue can remain coherent when synthesis is evidence-driven and chronology/references are separately compacted.

Regression lesson:
- a later entity-binding repair can regress another subject; validation must cover the set of previously repaired entities, not only the current symptom;
- rejected intermediate source revisions should remain immutable but must not become build authority.

### 4.9 SP-2024-H2

Evidence:
- final state records audited Source Intake count 5,955 and accepted Evidence count 85 before Architecture;
- Architecture approval explicitly authorizes autonomous progress to Publication Preview;
- final v0.12 supersedes v0.11 for Issue #191 family/variant/property and model/Stack/API attribution failures;
- final exact-byte Publication Preview authorizes release.

Positive pattern:
- high intake volume can be compressed through Evidence/Selection while preserving long-form synthesis.

Regression lesson:
- broad intake does not remove the need for entity-bound claims;
- subject → component → variant → property hierarchy needs structural validation rather than proximity heuristics.

### 4.10 SP-2025-H1

Evidence:
- frozen state records a 31-source curated reconstruction and 31 Evidence records;
- final source v0.4 fixes event-only Technical Notes remainders;
- the final publication itself can be coherent and exact-byte approved.

Later audit evidence:
- Issue #166 later compared this reconstruction with a broad run of roughly 6,015 Screening inputs and found material omissions.

Positive pattern:
- narrative coherence and publication correctness can be assessed independently from completeness.

Critical regression lesson:
- **a plausible Architecture/PDF is not evidence that Source Intake was complete**;
- v2 must expose Materiality/Completeness before Architecture Review.

### 4.11 SP-2025-H2

Evidence:
- mature two-gate exact-byte state;
- final v0.8 is a presentation-only Issue #54 taxonomy/casing repair;
- final state preserves accepted Evidence, dates, drafts, synthesis and reference compaction.

Related lineage retained from Human Review corpus:
- Issue #139: generic source-summary fallback must fail closed;
- Issue #140: repeated reference boilerplate creates low-information pages.

Positive pattern:
- a presentation-only revision can be constrained not to change Evidence/accepted semantics.

Regression lesson:
- provenance enum → reader label mapping is a Publication concern;
- source-specificity and compactness must not trade away factual attribution.

### 4.12 SP-2020-Y

Evidence:
- mature two-gate state;
- chronology contains 28 resolved events;
- final source v0.19;
- reference-pagination revisions v0.11–v0.18 repeatedly assert no semantic/reference/URL identity change;
- final v0.19 re-applies Issue #55 note-tail invariant after source-specific enrichment;
- exact control commit and source/PDF hashes are recorded.

Positive pattern:
- historical low-density periods do not require artificial source/page minima;
- visual/reference compaction can be explicitly semantic-neutral.

Regression lesson:
- a later source enrichment can reintroduce an old layout failure; layout regressions must run after content enrichment, not only once before it.

### 4.13 SP-2021-Y

Evidence:
- mature two-gate state;
- chronology 45 events;
- final v0.8 explicitly fixes Issue #122 low-density TOC continuation and Issue #55 Technical Notes tail using targeted `Needspace` relaxation;
- exact implementation/control commit is recorded.

Positive pattern:
- Annual story/trajectory synthesis can coexist with a selected objective chronology.

Regression lesson:
- TOC hierarchy and local note-tail controls remain relevant even after annual semantic structure is stable;
- global layout protection must be replaced by narrow local controls.

### 4.14 SP-2022-Y

Evidence:
- mature two-gate state;
- chronology 59 events;
- final source mode is `annual-direct-entity-binding-plus-latex-dependency-repair`;
- v0.9 repair explicitly references Issues #54/#78/#122/#139/#140/#191/#271/#272;
- v0.10 adds a `needspace` LaTeX dependency repair before exact-byte Publication Preview;
- control commit is recorded.

Positive pattern:
- one Annual can preserve chronology, Technical Notes, references and higher-order synthesis under a shared publication model.

Regression lesson:
- this edition demonstrates that reader taxonomy, bibliography metadata, TOC hierarchy, fallback rejection, entity binding, empty-wrapper suppression, chronology-source mapping and layout dependency are not independent one-off patches;
- they form a coupled long-form regression family.

### 4.15 SP-2023-Y

Evidence:
- mature two-gate state;
- chronology 75 events with 3 unresolved dates explicitly retained;
- final v0.14 reference compaction references Issue #140;
- final v0.15 residual repair references Issues #139/#191;
- final exact-byte PDF is 41 pages.

Positive pattern:
- large objective chronology remains usable when compact and separated from narrative synthesis;
- unknown dates can remain unresolved without blocking publication when the limitation is explicit.

Regression lesson:
- reference compaction must preserve event/source traceability;
- final source-specific fallback/entity-binding repair must run after publication compaction;
- empty Technical Notes wrappers and chronology-source mapping from the earlier annual review family remain generic Annual/Publication regressions even if not named in the last revision object.

## 5. Cross-edition patterns strengthened by Phase 2C

### DEPTH-PAT-001 — Gate convergence is empirically staged

Observed sequence:

```text
M07 -> M06/M05/M04/M03 -> M02/M01 -> Half-year/Annual
```

moves from multiple Human flags and revision-bearing Freeze toward:

```text
Architecture Review
Publication Preview exact-byte approval
  -> deterministic Visual Review / Freeze / merge / Release
```

Therefore the two-gate Core target is production-learned behavior, not a design preference.

### DEPTH-PAT-002 — Implementation identity belongs in provenance

Across later frozen states, builds repeatedly retain a `control_commit_sha` and style SHA in addition to source/PDF hashes.

v2 must retain this principle at the Core action/state level:

```text
semantic contract identity
+ implementation repository/control identity
+ exact input/output artifact identity
```

A contract SHA alone cannot prove executable equivalence.

### DEPTH-PAT-003 — Repair order matters

Examples:
- source enrichment can reintroduce Issue #55 tails (2020-Y);
- a later entity repair can regress another entity (2024-H1);
- reference/layout compaction must be followed by source/entity checks (2022-Y/2023-Y);
- template reuse can leak another edition's labels (M06).

Therefore regression execution belongs after every material transformation, not only at the stage where the invariant was first invented.

### DEPTH-PAT-004 — Reader scope identity must be derived

M06's July labels inside a June Special show a generic class:

> reader-facing period/profile identity copied from template text can disagree with canonical state.

v2 should generate/validate period labels, date captions, `this week/month/year` markers and other scope labels from Production Profile/State.

### DEPTH-PAT-005 — Source completeness and publication correctness are orthogonal

2025-H1 is the strongest example:
- final PDF can be coherent, validated and exact-byte approved;
- later broad research can still prove that material source coverage was insufficient.

Thus Materiality/Completeness is a pre-Architecture research contract, while publication validation is a later independent contract.

### DEPTH-PAT-006 — Long-form quality is a coupled regression set

2022-Y and 2024-H1 show that the stable set includes at least:
- subject/entity/property binding;
- identifier preservation;
- source-specific fail-closed notes;
- bibliography title/metadata preservation;
- compact but source-mapped chronology;
- empty-wrapper suppression;
- TOC hierarchy;
- note-tail/Needspace behavior;
- semantic section survival across revisions.

No future repair should be accepted by testing only its local symptom.

## 6. Updated implications for Phase 3

Phase 2C adds or strengthens these implementation requirements:

1. Production/action provenance must include implementation repository/control identity, not only contract SHA.
2. Reader-facing temporal/profile labels need canonical-state derivation/validation.
3. Long-form regression fixtures should be organized as coupled suites rather than repair-script ancestry.
4. Completeness must gate Architecture independently of publication correctness.
5. Regression checks must be rerunnable after later transformations such as enrichment, compaction and layout repair.
6. Pilot Finding classification should separate defect scope from whether a regression is required.

## 7. Phase 2C exit decision

WU-003C is complete when this file is committed and cross-checked against all fifteen final `pipeline-state.json` records.

The exit condition is satisfied because:
- all fifteen editions have an edition-level entry;
- every entry identifies its final state path and exact production-lineage signals rather than only page/version metadata;
- Architecture/Gate provenance is represented;
- major final-state repair lineage and explicit Issue references are retained where present;
- positive and negative knowledge are both extracted;
- cross-edition claims are supported by multiple concrete editions;
- no frozen release was modified.
