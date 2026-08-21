# Survey Production Core v2 — Historical Invariant and Regression Catalog

Status: `PHASE 2 OUTPUT / knowledge distillation`  
Established: 2026-08-22 JST  
Improvement branch: `refactor/survey-production-core-v2`  
Inspected `main`: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Purpose

This document distills the useful knowledge contained in completed Special production, Weekly evolution, Human Review Issues, repair scripts, and regression tests into durable future-production invariants.

It deliberately does **not** reproduce the historical repair chain as the new architecture.

The transformation is:

```text
Human Review finding
  -> edition repair
  -> follow-up regression or side effect
  -> durable invariant
  -> canonical Core / Profile / Publication ownership
  -> stable regression fixture
```

A closed Issue does not imply that its current implementation is already suitable for Survey Production Core v2. Conversely, an open historical Issue does not imply that old frozen releases must now be corrected.

The user has explicitly chosen **future-system improvement rather than a reissue campaign**. Historical editions are therefore treated as learning/regression evidence unless separately authorized for correction.

---

## 2. Classification

### 2.1 Owner

- `CORE` — source/evidence/claim/state/orchestration correctness shared by all edition types.
- `WEEKLY_PROFILE` — rolling-window, carry-over, Late Breaking, current-week editorial semantics.
- `PERIOD_PROFILE` — bounded retrospective period, chronology, period-wide synthesis/completeness.
- `THEMATIC_PROFILE` — research-question/lineage semantics.
- `PUBLICATION_PROFILE` — reader-facing rendering, TeX/PDF/layout, references, Visual QA, release artifact integrity.
- `SERIES_LAYER` — cross-volume research architecture.
- `LEGACY_REPLAY` — exact historical reconstruction or compatibility behavior that does not belong to future hot-path production.

### 2.2 Current implementation status

- `IMPLEMENTED_GENERIC` — currently enforced by a generic/shared implementation suitable as a v2 base.
- `IMPLEMENTED_SPECIAL` — implemented materially in Special-specific code/tests and must be promoted/generalized.
- `PARTIAL` — some checks exist but the complete invariant is not enforced end-to-end.
- `MISSING` — no adequate canonical enforcement exists.
- `LEGACY_ONLY` — behavior exists only as historical repair/replay logic and should not be promoted directly.

### 2.3 Historical edition treatment

- `PASS` — historical evidence demonstrates the intended behavior.
- `PASS_WITH_LEGACY_VARIANCE` — historical artifacts may differ but no correction is requested.
- `HISTORICAL_GAP` — historical issue exposed the missing invariant; preserve the evidence without rewriting frozen output.

---

## 3. Catalog summary

| Invariant | Short name | Owner | Current status | Phase 3 priority |
|---|---|---|---|---|
| INV-SRC-001 | Broad intake is not completeness | `CORE` + Profiles | `MISSING` | `P0` |
| INV-SRC-002 | Every material discovery has explicit disposition | `CORE` | `MISSING` | `P0` |
| INV-SRC-003 | Gap-fill/supplemental discoveries join the same trace | `CORE` + Profiles | `PARTIAL` | `P0` |
| INV-ID-001 | Canonical identifiers are byte-preserved | `CORE` + Publication | `IMPLEMENTED_SPECIAL` | `P0` |
| INV-EVD-001 | Technical facts are subject/entity-bound | `CORE` | `IMPLEMENTED_SPECIAL` | `P0` |
| INV-EVD-002 | Reader-facing technical claims are source-specific or fail closed | `CORE` + Publication | `IMPLEMENTED_SPECIAL` | `P1` |
| INV-EVD-003 | Known source metadata is preserved into bibliography | `CORE` + Publication | `PARTIAL` | `P1` |
| INV-TMP-001 | Canonical temporal scope drives reader-facing scope labels | `PERIOD_PROFILE` + Publication | `IMPLEMENTED_SPECIAL` | `P1` |
| INV-TMP-002 | Material chronology events retain source mapping | `PERIOD_PROFILE` + Core | `IMPLEMENTED_SPECIAL/PARTIAL` | `P1` |
| INV-TMP-003 | Unresolved event dates are not guessed | `CORE` + Profiles | `PARTIAL` | `P1` |
| INV-ARC-001 | Required retrospective final synthesis exists and survives revisions | `PERIOD_PROFILE` + Publication | `IMPLEMENTED_SPECIAL/PARTIAL` | `P1` |
| INV-ARC-002 | Architecture Review exposes research compression/materiality | `CORE` + Profiles | `MISSING` | `P0` |
| INV-RDR-001 | Reader prose is separated from pipeline/editorial metadata | `CORE` + Publication | `PARTIAL` | `P0` |
| INV-WKL-001 | Weekly item has a reader-facing why-this-week | `WEEKLY_PROFILE` | `PARTIAL` | `P1` |
| INV-WKL-002 | One substantive home per Late Breaking event | `WEEKLY_PROFILE` | `PARTIAL` | `P1` |
| INV-WKL-003 | Watchlist is reader-facing observation, not production TODO | `WEEKLY_PROFILE` | `PARTIAL` | `P1` |
| INV-PUB-001 | Empty optional wrappers are suppressed | `PUBLICATION_PROFILE` | `IMPLEMENTED_SPECIAL` | `P1` |
| INV-PUB-002 | Breakable cards avoid orphaned low-information continuations | `PUBLICATION_PROFILE` | `IMPLEMENTED_SPECIAL/PARTIAL` | `P1` |
| INV-PUB-003 | Layout repair must not create blank-page/isolated-box regression | `PUBLICATION_PROFILE` | `IMPLEMENTED_SPECIAL` | `P1` |
| INV-PUB-004 | Published artifact exposes exact canonical source provenance | `PUBLICATION_PROFILE` | `PARTIAL` | `P1` |
| INV-PUB-005 | Publication approval/freeze/release preserve exact bytes | `CORE` + Publication | `IMPLEMENTED_GENERIC/SPECIAL` | `P0` |
| INV-REP-001 | Generic fixes become stable validators/tests, not patch-chain dependencies | `CORE quality` | `MISSING` as process | `P0` |
| INV-REP-002 | Repair sets are regression-compatible as a set | `CORE quality` | `MISSING` as process | `P1` |
| INV-REP-003 | Frozen historical artifacts remain immutable | `CORE` + Publication | `IMPLEMENTED_GENERIC` | `P0` |

`P0` here means required before W33/SP001 first-production validation or required to make their findings interpretable. `P1` means required in the first v2 stabilization track, and may be implemented before or during the Pilot feedback cycle depending on existing coverage.

---

# 4. Source Intake and Materiality

## INV-SRC-001 — Broad intake is not completeness

Origin: Issue #166, SP-2025-H1 source-intake audit.

Historical failure:

- the original curated reconstruction used 31 sources;
- later broad re-intake produced 6,015 Screening inputs;
- several material model/product/protocol/runtime/media events had been absent from the original reconstruction;
- the overall high-level interpretation could remain plausible while ecosystem/event coverage was materially incomplete.

Invariant:

> Successful collector execution, a large intake count, or a curated set does not by itself establish research completeness.

Core responsibility:

- distinguish collector/run completion from research-completeness state;
- preserve intake identity and downstream traceability.

Profile responsibility:

- define which coverage dimensions must be satisfied or explicitly unresolved.

Weekly examples: editorial-window lanes, carry-over obligations, current material developments.

Period examples: time/actor/technical-layer/first-party-source coverage.

Thematic examples: lineage branches, transitions, competitors, counterexamples, primary-source gaps.

Current status: `MISSING` as one canonical cross-profile completeness contract.

Phase 3 action:

- add a `Completeness Contract` interface/profile result distinct from collector success;
- prevent Architecture Review readiness when required completeness obligations are neither satisfied nor recorded as residual limitations.

Historical treatment: `HISTORICAL_GAP`; no automatic reissue.

---

## INV-SRC-002 — Every material discovery has an explicit downstream disposition

Origin: Issue #166.

Invariant:

```text
material discovery
  -> Evidence candidate
  OR duplicate/lifecycle link
  OR explicit non-material/exclusion rationale
  OR HOLD/uncertainty
```

and if selected/material:

```text
Selection
  -> Architecture placement
  -> reader-facing narrative/chronology/synthesis
  OR explicit final omission rationale
```

A material record may not disappear simply because a later stage processed fewer records.

Current status: `MISSING` end-to-end. Individual stages already have local dispositions, but there is no canonical cross-stage ledger.

Phase 3 action:

- implement the first **Materiality Ledger** schema/validator;
- require stable source/discovery keys and stage-by-stage dispositions;
- detect silent drop as a hard validation failure.

Historical treatment: `HISTORICAL_GAP`.

---

## INV-SRC-003 — Supplemental/gap-fill research joins the same evidence path

Origin: Issue #166 and current retrospective supplemental-source tooling.

Invariant:

> A supplemental discovery used to close a coverage gap is not a side note. It must enter Screening/materiality/Evidence under the same traceability requirements as base intake.

Existing implementation:

- retrospective tooling distinguishes broad intake and supplemental gap-fill;
- tests exist around supplemental collection and Screening metadata;
- no single Core ledger proves all supplemental material reached a disposition.

Current status: `PARTIAL`.

Phase 3 action:

- make intake origin (`BASE`, `SUPPLEMENTAL`, future profile-specific origin) metadata in the Materiality Ledger;
- validate that origin does not alter the obligation to receive a disposition.

---

# 5. Identifier and structured-field safety

## INV-ID-001 — Canonical URLs/paths/IDs are byte-preserved through reader normalization

Origin: Issue #172.

Historical failure:

A correct GitHub path containing `MODEL_CARD.md` became a noncanonical localized path such as `モデル_CARD.md` in Technical Notes and the PDF link annotation.

Invariant:

The following structured identifiers are not prose-localization targets:

- URL / URI;
- repository path / filename;
- model ID / API ID;
- code / command / schema identifier;
- citation target;
- canonical source key.

Localization/taxonomy transformation must operate on explicitly prose/label fields only.

Renderer validation should compare the canonical source URL with both visible source linkage and PDF/link target when practical.

Current status: `IMPLEMENTED_SPECIAL`; Special-specific identifier-preservation and canonical-note-URL tests exist.

Phase 3 action:

- promote the invariant into a generic structured-field/renderer validation utility;
- retain Special historical cases as fixtures without preserving Special-only repair ancestry.

Historical treatment: `PASS_WITH_LEGACY_VARIANCE`.

---

# 6. Evidence and claim correctness

## INV-EVD-001 — Technical attributes are explicitly subject/entity-bound

Origin: Issue #191, following the source-specific repair prompted by Issue #139.

Historical failure sequence:

```text
generic Technical Notes fallback (#139)
  -> source-specific extraction introduced
  -> nearby comparator/related-model values were mistaken for target attributes (#191)
```

Examples included:

- Mistral Large 2 receiving values/features belonging to Codestral/Llama comparison context;
- Jamba 1.5 receiving Llama comparison parameter scales or a deployment-specific context figure as model properties;
- Ministral 3B/8B receiving category/comparator sizes as target specifications.

Invariant:

> Correct source + nearby correct value is insufficient. The value/feature must be bound to the intended subject, component, variant, or comparator relation.

Required behavior:

- target-entity property is explicit;
- comparator value retains comparator identity;
- related product/historical reference/navigation/table neighbor is not silently promoted;
- proximity-only extraction is fail-closed for publication-quality facts.

Current status: `IMPLEMENTED_SPECIAL` with a substantial late half-year entity-binding checker and many Special-specific tests. The present implementation is tightly coupled to half-year Technical Notes manifests/revision contracts and therefore is not yet the generic v2 guard.

Phase 3 action:

- extract a generic `subject/entity binding` evidence validation primitive;
- make Edition/Profile renderers consume structured bound facts instead of reparsing prose where possible;
- port Mistral/Jamba/Ministral fixtures into the generic regression suite.

Historical treatment: `PASS_WITH_LEGACY_VARIANCE`.

---

## INV-EVD-002 — Reader-facing technical notes are source-specific or fail closed

Origin: Issue #139.

Historical failure:

Generic placeholder prose such as “一次資料で確認できる公開・提供・機能・時系列上の事実を要約した項目” was published as if it were a technical point, sometimes duplicated within one card.

Invariant:

- no generic contentless fallback may appear as a source-backed technical fact/claim;
- each reader-facing technical claim must expose at least one concrete source-specific fact, claim, or limitation;
- duplicate identical bullets within a card are invalid;
- insufficient Evidence causes reduction/omission/HOLD, not invented completion.

Current status: `IMPLEMENTED_SPECIAL`; numerous Special reader-facing-note/fallback checks exist.

Phase 3 action:

- promote the fail-closed semantic rule into the common structured-draft/publication validator;
- keep publication templates free to vary while the semantic requirement remains Core-owned.

---

## INV-EVD-003 — Known bibliographic metadata is preserved into reader-facing References

Origin: Issue #78.

Historical failure:

References collapsed many distinct known sources into repeated generic `Primary source 1` entries even though Technical Notes/Evidence already held recognizable titles.

Invariant:

> Downstream rendering must not discard known source identity merely because a fallback bibliography field exists.

Where known, preserve:

- title;
- source owner/authors;
- publication/release date;
- canonical URL;
- visited/access date where the publication style requires it;
- evidence-boundary/source-note metadata.

A generic fallback is allowed only when source metadata is genuinely unavailable.

Current status: `PARTIAL`; shared bibliography generation exists and Special repairs/tests address historical fallback behavior, but Phase 3 should verify that one canonical source-metadata model drives both Weekly and long-form output.

Phase 3 action:

- add regression ensuring known Evidence metadata cannot degrade to a generic placeholder at render time;
- verify bibliography/Technical Notes use the same canonical source identity.

---

# 7. Temporal and period correctness

## INV-TMP-001 — Canonical temporal scope drives reader-facing scope labels

Origin: Issue #49.

Historical failure:

SP-2026-M06 correctly covered June, while a copied reader-facing Retrospective scope box said July.

Invariant:

- cover issue label;
- survey setup/scope box;
- chronology heading;
- final synthesis period label;
- other structurally designated period labels

must derive from or validate against the edition/profile temporal contract.

Do **not** reject legitimate references to adjacent months in narrative chronology; validation targets structural scope fields, not arbitrary month strings in prose.

Current status: `IMPLEMENTED_SPECIAL` in period-consistency repair/validation logic.

Phase 3 action:

- retain as `PERIOD_PROFILE` validation;
- make renderer consume normalized profile temporal metadata rather than edition-specific string substitution.

Historical treatment: `HISTORICAL_GAP`; frozen provenance remains unchanged.

---

## INV-TMP-002 — Material chronology events retain lightweight source mapping

Origin: Issue #272.

Invariant:

A reader-facing material chronology event must map to the primary source(s) establishing its date/identity while remaining a compact chronology rather than an Evidence-card dump.

Event identity remains distinct among, for example:

- initial paper publication/submission;
- release;
- preview;
- API availability;
- product availability;
- policy/control milestone.

Current status: `IMPLEMENTED_SPECIAL/PARTIAL`; annual repair path addressed this shape, but it is not yet a general chronology/lineage contract.

Phase 3 action:

- define a structured chronology event representation with evidence/source refs;
- let Period Profile render date-oriented chronology;
- allow Thematic Profile to reuse the same provenance primitive for lineage/timeline nodes when useful.

---

## INV-TMP-003 — Unresolved event dates are not guessed

Origin: Issue #272 and existing Evidence chronology boundaries.

Invariant:

> Missing date precision is retained as uncertainty rather than replaced by a convenient guessed date.

The exact date/event type used in chronology must be supported by the relevant source/evidence record.

Current status: `PARTIAL` in current Evidence/chronology validators.

Phase 3 action:

- retain as generic Evidence event-time rule;
- make Profile chronology renderers respect precision/uncertainty fields.

---

# 8. Architecture and synthesis

## INV-ARC-001 — Required retrospective final synthesis exists and survives derived revisions

Origin: Issue #95.

Historical failure:

Some Monthly Retrospective editions reached References directly after the last article/Technical Notes while another edition contained the expected cross-article final synthesis. A shared revision builder could also reconstruct `main.tex` without preserving a pre-existing synthesis input.

Invariant for `PERIOD_PROFILE`:

- a cross-article final retrospective synthesis is required unless Architecture explicitly makes a valid exception;
- synthesis is based only on approved/accepted Evidence and article output;
- finalization artifacts/source manifest track synthesis path/content digest;
- derived layout/review revisions preserve the synthesis rather than reconstructing around it accidentally;
- pre-Publication validation fails if a required synthesis is absent.

Current status: `IMPLEMENTED_SPECIAL/PARTIAL`; the historical repair path exists, but the v2 requirement must live in Period Profile rather than a revision builder.

Phase 3 action:

- add Profile-declared required semantic surfaces to generic finalization/preflight;
- keep synthesis bytes/hash in final source manifest.

Historical treatment: `HISTORICAL_GAP`; Issue #95's historical correction proposal is not automatically executed by this redesign.

---

## INV-ARC-002 — Architecture Review exposes how broad research became the proposed issue

Origin: Issue #166.

Invariant:

Human Gate 1 must expose enough compression/materiality information to audit:

- how much research entered the pipeline;
- what was kept/held/excluded/merged;
- which major completeness obligations were found;
- where material items landed;
- what limitations remain;
- how those decisions support the issue thesis/architecture.

Current status: `MISSING` as a unified Architecture Review contract.

Phase 3 action:

- define an Architecture Review Summary schema fed by Materiality Ledger + Profile completeness result + Selection/Architecture;
- make absence/incompleteness block Architecture Review readiness.

---

# 9. Reader-facing editorial boundary

## INV-RDR-001 — Reader-facing prose is separate from internal pipeline/editorial metadata

Origin: Weekly Issue #9; Special Issue #40 and later reader-facing repairs.

Invariant:

Reader-visible material may expose claim-strength concepts that help interpretation, but should not expose workflow internals as publication prose.

Reader-useful examples:

- Claim Boundary;
- Community Observation;
- editorial cutoff/time boundary;
- uncertainty/limitations.

Internal/provenance examples:

- Candidate Inventory;
- Reaction Pass as a pipeline stage name;
- `primary verification status` implementation terminology;
- “昇格させる” / next-production TODO;
- internal Selection/Draft Package state.

Current status: `PARTIAL`; `preflight_final_issue.py` and Special reader-facing checks cover important leakage patterns, but vocabulary is still distributed among edition-specific postprocessors/tests.

Phase 3 action:

- create one generic reader-facing forbidden/internal-token policy with Profile-provided exceptions where genuinely reader-relevant;
- prefer structured field separation over regex cleanup after prose generation.

---

# 10. Weekly-specific editorial invariants

## INV-WKL-001 — Pre-window/background material has a reader-facing `why this week`

Origin: Weekly Issue #9.

Invariant:

A Weekly article that substantially relies on older artifacts must explain the current trigger/momentum/structural reason for inclusion or be presented as an explicitly different editorial form such as background/deep-dive.

Current status: `PARTIAL`; current Weekly selection/architecture semantics distinguish event/trend chronology, but the reader-facing obligation remains a W33 validation target.

Phase 3 action:

- add Weekly Profile architecture/draft requirement for `why_this_week` when selected material is outside/older than the normal event window or when relevance is trend-driven.

---

## INV-WKL-002 — One substantive home per Late Breaking event

Origin: Weekly Issue #9.

Historical failure:

One post-cutoff SGLang event received substantive treatment in multiple sections, creating repetition.

Invariant:

A `LATE_BREAKING` event has one primary substantive reader-facing placement. Other relevant articles use compact cross-reference/context rather than repeating the full explanation.

Current status: `PARTIAL`.

Phase 3 action:

- Weekly Profile Architecture validator detects multiple primary placements of the same late-breaking `event_id`.

---

## INV-WKL-003 — Watchlist is a reader-facing observation surface, not production TODO

Origin: Weekly Issue #9.

Invariant:

Published Watchlist describes:

- current observed state;
- what remains unconfirmed;
- what future evidence would change evaluation / what readers should watch.

It does not describe Candidate Inventory promotion or internal next-issue workflow.

Current status: `PARTIAL`.

Phase 3 action:

- encode Watchlist output fields in Weekly Profile instead of deriving prose from internal status labels.

---

# 11. Publication and visual-quality invariants

## INV-PUB-001 — Empty optional reader-facing wrappers are suppressed

Origin: Issue #271.

Historical failure:

A zero-card Technical Notes section still emitted headings, boilerplate and an empty Theme-at-a-glance table, producing almost empty pages.

Invariant:

> If a semantically optional reader-facing section has zero content items, suppress the wrapper as a unit.

This includes headings/table headers/boilerplate that only make sense when items exist.

Required claim/chronology boundaries must remain elsewhere and cannot be used to justify an empty appendix.

Page count is not preserved through filler/padding.

Current status: `IMPLEMENTED_SPECIAL`.

Phase 3 action:

- promote conditional-section rendering into Publication Profile primitives;
- test zero/one/many item cardinalities.

---

## INV-PUB-002 — Breakable cards avoid orphaned low-information continuations

Origin: Issue #55.

Historical failure:

Breakable Technical Notes cards left only a URL, source heading, or final limitation line at the top of the next page.

Invariant:

- page spanning remains allowed for large cards;
- source heading stays with at least one source/link line;
- tiny low-information card tails should not be isolated at the next page top;
- local break quality must be improved without forcing the entire card unbreakable.

Current status: `IMPLEMENTED_SPECIAL/PARTIAL`; extensive Special tail-policy/layout repair tests exist.

Phase 3 action:

- move the stable rule into the long-form Publication Profile;
- keep render-first Visual QA because TeX source/log inspection alone cannot establish visual quality.

---

## INV-PUB-003 — A layout repair must not regress blank-page or whole-box placement quality

Origin: Issues #40 and #55 and subsequent repair iterations.

Invariant:

A fix for one break defect must be evaluated against the coupled layout contract, including:

- accidental blank pages;
- whole-page isolated callout boxes;
- large unnatural whitespace;
- Technical Notes tail or URL-only continuation;
- heading/orphan behavior;
- References wrapping/column quality.

This is not satisfiable through a sequence of independent single-condition patches.

Current status: `IMPLEMENTED_SPECIAL` through multiple targeted regression tests, but knowledge is fragmented across repair generations.

Phase 3 action:

- define a stable Publication Profile visual-regression suite independent of revision numbers;
- use historical layout cases as fixtures;
- retire monkey-patch repair ancestry only after the set passes under canonical rendering.

---

## INV-PUB-004 — Public artifact makes canonical source provenance discoverable

Origin: Issue #40 and release/freeze policy evolution.

Invariant:

A public reader/auditor should be able to identify the source/provenance associated with the exact PDF, including:

- frozen source commit;
- exact PDF digest;
- canonical release/source metadata;
- source path or link through the release/repository surfaces.

Current status: `PARTIAL`; release manifests and metadata are strong, while reader-facing/public source discoverability has evolved across editions.

Phase 3 action:

- include canonical source provenance in Publication Profile release metadata and ensure the public Release surfaces expose it consistently.

---

## INV-PUB-005 — Publication approval, Freeze and Release preserve exact bytes

Origin: mature Special Human Gate/release policy plus earlier Weekly freeze/release work.

Invariant:

Publication Preview approval is bound to exact PDF SHA-256. Visual Review record, Freeze, merge and Release operate on those identical approved bytes or fail.

`release_anchor_commit` and `frozen_source_commit` may be distinct and must both remain explicit.

Current status: `IMPLEMENTED_GENERIC/SPECIAL` in the strongest current release paths.

Phase 3 action:

- retain existing trusted primitives;
- normalize Weekly onto the same two-Human-Gate authority model without weakening digest checks.

---

# 12. Repair-system invariants

## INV-REP-001 — Generic defects become canonical validators/tests, not permanent versioned patch dependencies

Origin: the accumulated `revise_special_*_vN.py` repair families.

Observed risk:

Later scripts import earlier revision scripts, monkey-patch globals/functions, execute another repair, then restore state. This can preserve one historical reconstruction but is unsuitable as the future production architecture.

Invariant:

For a generic defect:

```text
finding
  -> durable invariant
  -> canonical implementation
  -> stable regression fixture
```

The historical repair script may remain for exact replay, but new editions must not require the chain.

Current status: `MISSING` as a completed migration; Phase 0 confirmed long active chains still exist.

Phase 3 action:

- establish canonical replacement points first;
- begin migration with P0 correctness invariants, not cosmetic cleanup.

---

## INV-REP-002 — Repair invariants are validated as a compatible set

Origin: #139 -> #191 and #40 -> #55 style sequences.

Invariant:

A repair is incomplete if it only fixes its own original fixture while violating another accepted invariant.

Examples:

- source-specific extraction must also pass entity-binding correctness;
- orphan prevention must also pass blank-page/whitespace regression;
- reader localization must also preserve identifiers;
- References metadata improvement must preserve URL/source traceability.

Current status: `MISSING` as an explicit quality-contract organization; many pairwise tests exist implicitly.

Phase 3 action:

- group tests by invariant/quality contract rather than by repair-script version;
- introduce canonical regression suites that run together for Core/Profile/Publication.

---

## INV-REP-003 — Frozen historical artifacts are immutable

Origin: release/freeze policy and multiple post-Freeze findings such as #49/#95.

Invariant:

No v2 migration rewrites frozen PDFs/source/release provenance merely to make old editions conform to current contracts.

Historical defects may be recorded as `HISTORICAL_GAP`; an actual correction/reissue is a separate explicitly authorized editorial/publication action.

Current status: `IMPLEMENTED_GENERIC` policy.

Phase 3 action: preserve; ensure migration tooling defaults to non-mutating historical inspection.

---

# 13. Existing regression assets to preserve or promote

The current test suite contains valuable generic and Special-derived fixtures. Phase 3 should migrate ownership without losing them.

## 13.1 Already generic/shared foundations

Representative tests:

- `test_raw_provenance.py`
- `test_source_intake.py`
- `test_accept_source_intake_artifact.py`
- `test_prepare_screening_run.py`
- `test_validate_screening_result.py`
- `test_accept_screening_results.py`
- `test_prepare_evidence_run.py`
- `test_validate_evidence_run.py`
- `test_accept_evidence_results.py`
- `test_build_candidate_matrix.py`
- `test_candidate_selection_gate.py`
- `test_build_architecture_input.py`
- `test_validate_issue_architecture.py`
- `test_build_draft_packages.py`
- `test_validate_article_draft.py`
- `test_validate_issue_synthesis.py`
- `test_preflight_final_issue.py`
- `test_release_identity.py`

These should remain the base Core regression families.

## 13.2 Special-derived generic correctness candidates

Identifier preservation:

- `test_special_reader_identifier_preservation.py`
- `test_special_half_year_canonical_note_urls.py`

Entity binding:

- `test_special_technical_note_entity_binding.py`
- `test_special_technical_note_entity_binding_check.py`
- `test_special_technical_note_entity_binding_zero_count.py`
- `test_special_entity_binding_contract_v3.py`
- `test_special_half_year_entity_binding_v24.py`
- `test_special_half_year_entity_binding_v25.py`
- `test_special_half_year_entity_binding_v27.py`
- `test_special_half_year_generic_capability_binding_v34.py`

Reader-facing source specificity/taxonomy:

- `test_special_reader_facing_notes.py`
- `test_special_event_reader_notes.py`
- `test_special_publication_contract_regressions.py`

These should be reorganized around generic invariant names after equivalent Core/Publication primitives exist.

## 13.3 Publication/layout regression assets

Representative families:

- `test_special_technical_note_tail_policy.py`
- `test_special_technical_note_tail_policy_annual.py`
- `test_special_prebuild_balanced_layout.py`
- `test_special_prebuild_visual_review_repairs.py`
- `test_special_single_column_adaptive_spacing.py`
- `test_special_half_year_reference_multicol.py`
- `test_special_half_year_reference_raggedright.py`
- `test_special_publication_layout_reference_multicol.py`

These belong to long-form Publication Profile quality, not the generic research Core.

## 13.4 Profile-specific assets

Weekly:

- `test_weekly_pipeline.py`
- `test_weekly_carryover_ledger.py`

Retrospective:

- period consistency tests;
- annual/half-year chronology/synthesis tests;
- `test_collect_special_supplemental_sources.py`
- `test_supplemental_screening_metadata.py`

Thematic regression assets are currently much weaker because true Thematic production has not yet been exercised. SP001 is intended to create the first real validation corpus.

---

# 14. Invariants still trapped in legacy implementation

The following types of knowledge are at particular risk during refactoring because they are encoded as revision-specific builders/checks rather than clean shared contracts:

1. exact Technical Notes entity-binding coverage/audit expectations;
2. source-specific fallback prohibition plus duplicate bullet detection;
3. URL/path preservation through localization transforms;
4. annual/half-year reference layout and line-break behavior;
5. Technical Notes tail/break policies;
6. final synthesis preservation across derived source revisions;
7. chronology/reference mapping after annual compression;
8. empty optional-section suppression;
9. interplay among local balanced columns, standfirst extraction, and Technical Notes placement;
10. edition/revision-specific overrides that may represent either a real generic rule or only a historical fixture.

Phase 3 must not delete or bypass the current code paths until their relevant fixtures pass against the replacement implementation.

---

# 15. Phase 3 minimum quality set before W33 / SP001

The following are the highest-priority invariants for first-production validation.

## Required before Pilot start (`P0`)

- `INV-SRC-001` broad intake != completeness;
- `INV-SRC-002` material discoveries cannot silently disappear;
- `INV-SRC-003` supplemental discoveries join the same trace;
- `INV-ID-001` canonical IDs/URLs are preserved;
- `INV-EVD-001` subject/entity binding is generic or safely enforced by the candidate pipeline;
- `INV-ARC-002` Architecture Review exposes materiality/completeness compression;
- `INV-RDR-001` internal pipeline vocabulary cannot leak as ordinary publication prose;
- `INV-PUB-005` exact PDF approval/freeze/release identity remains intact;
- `INV-REP-001` new generic fixes receive stable regression tests rather than new edition repair chains;
- `INV-REP-003` frozen historical artifacts remain untouched.

## Strongly preferred in the first vertical slice (`P1`)

- source-specific Technical Notes fail-closed;
- bibliographic metadata preservation;
- Period final-synthesis declaration/preservation;
- chronology source mapping representation;
- Weekly why-this-week / Late Breaking one-home / reader Watchlist;
- empty optional-wrapper suppression;
- long-form orphan/tail/blank-page regression set;
- canonical source discoverability in releases.

A P1 invariant already enforced safely by current production code may be reused rather than rewritten before the Pilot.

---

# 16. Historical corpus usage rule

The fifteen completed Retrospective Specials are a **knowledge and regression corpus**, not a mandatory byte-for-byte target for v2 rendering.

Use historical editions for:

- known failure fixtures;
- source/evidence coverage comparisons;
- structural expectations such as synthesis/chronology;
- Visual QA regression examples;
- provenance integrity tests.

Do not require new production to reproduce old defects, old page counts, or old repair ancestry.

Historical comparison outcomes may be labeled:

- `PASS` — compatible with current invariant;
- `PASS_WITH_LEGACY_VARIANCE` — old artifact differs for explainable historical reasons;
- `HISTORICAL_GAP` — the artifact demonstrates a defect now covered by a future invariant.

No label itself authorizes a reissue.

---

# 17. Phase 2 conclusion

The repair history does not argue for retaining a large Special-specific production pipeline. It argues for a stronger shared quality contract.

The dominant lessons are:

```text
collect broadly
  != completeness

source-specific
  != correctly attributed

reader-friendly transformation
  != permission to mutate identifiers

successful TeX build
  != visually acceptable publication

single-defect repair
  != regression-safe quality

frozen provenance
  != permanent hot-path implementation ancestry
```

Survey Production Core v2 should therefore preserve the mature generic Evidence/Draft primitives, add end-to-end materiality and contract orchestration, and promote Special-derived correctness/Publication invariants into stable regression suites.

The next step is to design the **minimum vertical slice** that can exercise these decisions on W33 and SP001 without attempting a big-bang rewrite.

## 18. WU-003 exit decision

WU-003 is complete when this catalog is committed and checked because:

- the highest-value recurring Human Review findings are represented as durable invariants;
- each invariant has an owner and current implementation status;
- historical repair implementation is separated from future contract intent;
- known cross-repair side effects are captured as coupled regression requirements;
- a concrete P0/P1 set exists for Phase 3;
- historical editions remain a learning corpus rather than an implicit correction backlog.
