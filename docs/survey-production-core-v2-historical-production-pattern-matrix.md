# Survey Production Core v2 — Historical Production Pattern Matrix

Status: `PHASE 2B OUTPUT / corpus-wide positive and negative pattern audit`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Companion: `docs/survey-production-core-v2-historical-invariants.md`

## 1. Purpose

The first Phase 2 pass concentrated on high-value Human Review findings and repair regressions. That was useful but failure-driven. This Phase 2B artifact explicitly covers all fifteen completed Retrospective Specials and adds the other half of the knowledge-distillation task:

> identify stable production/editorial patterns that worked and should survive v2, not only defects that once failed.

The corpus is:

- Monthly: `2026-M01` through `2026-M07` — 7 editions;
- Half-year: `2024-H1`, `2024-H2`, `2025-H1`, `2025-H2` — 4 editions;
- Annual: `2020-Y`, `2021-Y`, `2022-Y`, `2023-Y` — 4 editions.

Total: **15 frozen Retrospective Specials**.

Historical PDFs/releases remain immutable. This matrix is an architectural learning artifact, not a correction backlog.

## 2. Audit method and limits

For every edition, Phase 2B inspected the final release manifest and classified the edition's format-level production role. Where the repository has a clearly attributable Human Review/repair lineage, representative findings are recorded. The matrix also compares canonical Monthly/Half-year/Annual production guidance with the final artifacts.

This audit intentionally distinguishes:

- `POSITIVE_PATTERN` — behavior worth retaining/generalizing;
- `FAILURE_LESSON` — historical defect whose invariant should survive;
- `EVOLUTION_EVIDENCE` — evidence that a later contract is the result of production learning;
- `LEGACY_VARIANCE` — frozen historical behavior that need not constrain future hot-path production.

The final internal `source_version` is reported as provenance/history depth, **not as a quality score**. A higher revision number means more immutable revision steps occurred, not that the final edition is worse.

Where no unique issue is singled out for one edition, the row does not invent one. Stable format behavior and final provenance still count as corpus evidence.

## 3. Corpus overview

| Edition | Form | Final source | Pages | Final public identity / authorization | Main retained lesson |
|---|---|---:|---:|---|---|
| SP-2026-M07 | Monthly | v0.8 | 36 | legacy revisioned tag; post-Freeze gates remained | starting point of modern reader-facing Special QA and proof that gate/release contract still needed simplification |
| SP-2026-M06 | Monthly | v0.9 | 32 | issue-only / Freeze approval | reader-facing Technical Notes must preserve Evidence fidelity while being Japanese editorial prose |
| SP-2026-M05 | Monthly | v0.12 | 33 | issue-only / Freeze approval | mixed layout + breakable Technical Notes works when local page-break quality is guarded |
| SP-2026-M04 | Monthly | v0.10 | 38 | issue-only / Freeze approval | TOC, bibliography metadata, mixed-layout and final-synthesis content are independent publication invariants |
| SP-2026-M03 | Monthly | v0.10 | 34 | issue-only / Freeze approval | final retrospective synthesis is required editorial content, not optional decoration |
| SP-2026-M02 | Monthly | v0.6 | 33 | issue-only / exact-byte Publication Preview | strong evidence that two Human Gates + exact-byte authorization is the mature interaction model |
| SP-2026-M01 | Monthly | v0.6 | 29 | issue-only / exact-byte Publication Preview | mature Monthly flow with reader-facing TOC/pagination repair and exact-byte release authority |
| SP-2024-H1 | Half-year | v0.17 | 48 | issue-only / exact-byte Publication Preview | longitudinal synthesis can justify longer output; page count is an output, not a quota |
| SP-2024-H2 | Half-year | v0.12 | 44 | issue-only / exact-byte Publication Preview | source-specific wording is insufficient without subject/entity binding and identifier preservation |
| SP-2025-H1 | Half-year | v0.4 | 28 | issue-only / exact-byte Publication Preview | strongest evidence that broad intake and materiality/completeness are separate contracts |
| SP-2025-H2 | Half-year | v0.8 | 30 | issue-only / exact-byte Publication Preview | source-specific Technical Notes and compact References must fail closed rather than emit generic boilerplate |
| SP-2020-Y | Annual | v0.19 | 27 | issue-only / exact-byte Publication Preview | annual production can remain one issue while reconstructing sparse early-year evidence under explicit boundaries |
| SP-2021-Y | Annual | v0.8 | 36 | issue-only / exact-byte Publication Preview | annual story-unit/trajectory method generalizes beyond dense current-year source ecosystems |
| SP-2022-Y | Annual | v0.10 | 37 | issue-only / exact-byte Publication Preview | Annual Profile can preserve objective chronology while synthesizing ecosystem-scale change |
| SP-2023-Y | Annual | v0.15 | 41 | issue-only / exact-byte Publication Preview | compact sourced chronology + annual trajectory synthesis is valuable; empty wrappers and unsourced chronology links are not |

## 4. Monthly editions — production evolution

### 4.1 SP-2026-M07

Final provenance:
- source version `v0.8`;
- 36 pages;
- legacy release tag contained public revision identity (`special/2026-M07/v0.1`);
- Freeze did not yet authorize merge/public Release automatically.

Positive patterns observed in subsequent review:
- normal published prose had largely separated internal production metadata from reader-facing narrative;
- the edition made `why this Special` clear enough to pass later retrospective review;
- source-bound Technical Notes already provided useful traceability that could be refined rather than removed.

Failure/evolution lessons:
- isolated Claim Boundary/large-blank layout behavior demonstrated why render-first Visual QA is necessary;
- Technical Notes still exposed pipeline-centric vocabulary and needed a reader-facing rendering boundary;
- canonical release source was reproducible in the manifest but not sufficiently discoverable from the top-level survey path;
- revisioned public identity plus post-Freeze Human stops proved unnecessarily complex once exact-byte approval became available.

Future ownership:
- reader/internal separation → `CORE + PUBLICATION_PROFILE`;
- Technical Notes reader rendering → `PUBLICATION_PROFILE`;
- canonical source discoverability → `PUBLICATION_PROFILE`;
- legacy release identity/gate sequence → `LEGACY_VARIANCE`, not a v2 requirement.

### 4.2 SP-2026-M06

Final provenance:
- source version `v0.9`;
- 32 pages;
- issue-only identity;
- Freeze approval still used as release authorization.

Positive patterns:
- Technical Notes had already moved away from raw repository/provenance dumps toward a reader-facing technical appendix;
- attribution classes (`Vendor claim`, `Author claim`, `Project claim`) remained useful evidence boundaries;
- exact source/PDF provenance remained intact while reader-facing wording could be improved separately.

Failure lesson:
- Evidence fidelity does not require English source-derived sentences to be copied into a Japanese publication. Reader-facing explanation should be natural Japanese while technical names and claim attribution remain precise.

Future ownership:
- reusable factual Evidence stays unchanged;
- language/editorial presentation belongs to Publication/editorial rendering rather than mutation of Evidence records.

### 4.3 SP-2026-M05

Final provenance:
- source version `v0.12`;
- 33 pages;
- issue-only identity;
- Freeze approval authorization.

Positive patterns:
- modern Special mixed-layout identity had become established: ordinary narrative in local balanced two-column flow, wide/reference-heavy material full-width;
- Technical Notes cards were allowed to break rather than being made globally unbreakable, avoiding large structural whitespace;
- final retrospective synthesis existed and later served as the positive comparison when M03/M04 lost it.

Failure lessons:
- internal taxonomy/event enums cannot simply be printed as reader labels;
- breakable cards need local orphan/widow quality rules: source heading + first URL together, no one-line continuation tail, no isolated limitation fragment;
- a fix that makes cards unbreakable globally would regress blank-page/large-gap behavior.

Future ownership:
- provenance enum vs reader label separation → `CORE structured fields + PUBLICATION_PROFILE mapping`;
- card break quality → `PUBLICATION_PROFILE` coupled regression set;
- final retrospective synthesis requirement → `PERIOD_PROFILE`.

### 4.4 SP-2026-M04

Final provenance:
- source version `v0.10`;
- 38 pages;
- issue-only identity;
- Freeze approval authorization.

Positive patterns:
- long-form Special can remain navigable and coherent near forty pages when mixed layout, Technical Notes, References and thematic chapters have distinct reader-facing roles;
- final repairs demonstrated that TOC, source metadata and layout are separately testable publication concerns.

Failure lessons:
- TOC heading with zero entries is a hard navigation failure even if PDF bookmarks exist;
- known source titles must survive Evidence → bibliography; a repeated `Primary source 1` fallback is not an acceptable reader bibliography;
- ordinary narrative must not silently regress to one-column layout because a revision builder changed global layout state;
- final retrospective synthesis can be silently dropped by a later immutable repair revision unless it is manifest-bound and validated.

Future ownership:
- TOC non-empty/depth rules and mixed layout → `PUBLICATION_PROFILE`;
- bibliography metadata preservation → `CORE + PUBLICATION_PROFILE`;
- required final synthesis and revision survival → `PERIOD_PROFILE + CORE manifest validation`.

### 4.5 SP-2026-M03

Final provenance:
- source version `v0.10`;
- 34 pages;
- issue-only identity;
- Freeze approval authorization.

Positive pattern:
- the issue-level technical narrative remained valid enough that the missing final synthesis could be repaired without replacing the complete issue architecture.

Failure/evolution lesson:
- feature-level Theme Synthesis is not a substitute for an issue-level Retrospective Synthesis. A Period Special must close the covered period by explaining cross-feature relationships, unresolved boundaries and what the period means as a whole.

Future ownership:
- required issue-level Retrospective Synthesis → `PERIOD_PROFILE`;
- source-manifest binding so revisions cannot drop it → `CORE`.

### 4.6 SP-2026-M02

Final provenance:
- source version `v0.6`;
- 33 pages;
- issue-only identity;
- exact Publication Preview PDF approval authorized Visual Review record, Freeze, merge and public Release.

Positive patterns:
- state provenance records Architecture approval, structured Draft result set, post-draft Synthesis, claim/chronology audit, source manifest, exact PDF SHA, Publication Preview approval and deterministic Freeze chain;
- the Human interaction model was reduced to Architecture Review + Publication Preview without removing strict machine checkpoints;
- mixed-layout and list repairs could be expressed as immutable later source revisions while retaining accepted semantic Evidence/draft content;
- page count was allowed to change naturally after layout correction rather than being treated as a target.

Failure lessons:
- ordinary narrative one-column regression must be caught generically;
- source-side manual bullets must not combine with renderer list markers to produce duplicated bullets.

Future ownership:
- two Human Gates and exact-byte approval → `CORE`;
- immutable source/PDF binding → `CORE + PUBLICATION_PROFILE`;
- mixed layout/list normalization → `PUBLICATION_PROFILE`.

### 4.7 SP-2026-M01

Final provenance:
- source version `v0.6`;
- 29 pages;
- issue-only identity;
- exact Publication Preview authorization.

Positive patterns:
- mature Monthly issue could finish below an earlier nominal page floor without padding when content/layout coherence was better;
- exact-byte Publication Preview authority was preserved;
- reader-facing TOC was treated as designed navigation rather than a dump of every generated subsection.

Failure lesson:
- mechanically exposing `Theme at a glance` and repeated subsection entries created a nearly empty TOC continuation page. TOC depth is a publication policy and page count must not protect low-information pages.

Future ownership:
- TOC hierarchy/pagination → `PUBLICATION_PROFILE`;
- page budget as planning envelope, not quota → `PROFILE + PUBLICATION_PROFILE`.

## 5. Half-year editions — longitudinal research patterns

Canonical Half-year guidance captures the stable positive design that emerged from production:

- broad Source Intake is a discovery baseline, not completeness proof;
- base intake and supplemental gap fill remain distinguishable but share the same Screening/Evidence path;
- monthly classifications are inputs, not inherited decisions;
- six monthly recaps are inferior to longitudinal story units;
- Half-year value comes from cross-month comparison, half-year reclassification, cross-layer synthesis and explicit Half-year Synthesis;
- objective chronology events remain independently identifiable even when narrative stories combine them;
- page count is an output.

### 5.1 SP-2024-H1

Final provenance:
- source version `v0.17`;
- 48 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive patterns:
- a Half-year issue may legitimately exceed the Monthly planning envelope when the audited evidence and longitudinal synthesis require it;
- final exact-byte publication semantics remained identical despite larger scope;
- the same core production model can support longer period granularity without inventing a separate release system.

Corpus implication:
- publication machinery should not encode a 32/40-page assumption as correctness;
- length/coherence is a Profile/Architecture decision.

### 5.2 SP-2024-H2

Final provenance:
- source version `v0.12`;
- 44 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive patterns:
- source-specific Technical Notes and primary-source-backed facts are the correct direction;
- immutable repair revisions and final exact-byte release provenance allow correctness fixes without mutating earlier review artifacts.

Failure lessons:
- source-specific extraction can still be false when comparator/related-product attributes are not bound to the subject entity;
- reader-facing localization/taxonomy mapping must never mutate structured identifiers such as `MODEL_CARD.md`, URLs, API/model IDs or repository paths.

Future ownership:
- subject/entity binding → `CORE Evidence/claim correctness`;
- identifier byte preservation → `CORE + PUBLICATION_PROFILE`.

### 5.3 SP-2025-H1

Final provenance:
- source version `v0.4`;
- 28 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive pattern:
- architecture-level interpretation remained broadly sound even when later Source Intake audit found material ecosystem omissions. This demonstrates that narrative plausibility and coverage completeness are different axes.

Critical failure lesson:
- an earlier curated reconstruction used 31 sources; rerunning broad intake for the same half-year produced 6,015 Screening inputs and exposed material omissions including model, protocol, agent, serving, multimodal and framework developments.

Future ownership:
- collector success cannot imply completeness;
- every material discovery requires a disposition;
- base and supplemental sources must join one Materiality trace;
- Architecture Review must expose research compression, exclusions/holds and residual limitations.

This is the primary historical justification for `Materiality Ledger + Profile Completeness Result`.

### 5.4 SP-2025-H2

Final provenance:
- source version `v0.8`;
- 30 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive patterns:
- Half-year synthesis reuses existing Evidence rather than requiring duplication of every underlying source card;
- References can be compact while preserving title/owner/URL/visited-date traceability.

Failure lessons:
- generic Technical Notes fallback text that says only “the primary source confirms facts” provides the appearance of evidence without source-specific information and must fail closed;
- repeating identical bibliography boilerplate on every entry creates low-information pages and should be factored to section-level explanation;
- chronology/Evidence traceability should use mappings rather than duplicating all Technical Notes cards.

Future ownership:
- source-specific fail-closed rendering → `CORE + PUBLICATION_PROFILE`;
- bibliography density/layout → `PUBLICATION_PROFILE`;
- deduplicated chronology/source mapping → `PERIOD_PROFILE + CORE provenance`.

## 6. Annual editions — year-scale compression patterns

Canonical Annual guidance records a mature positive editorial model:

```text
Event -> Story unit -> Annual trajectory -> Annual thesis
```

with a separate selected Detailed Chronology preserving material objective events. Calendar quarters may diagnose Source Intake skew but do not define reader-facing phase structure. Reader-facing phases and trajectories are Evidence-derived. Annual taxonomy is not inherited from a later year.

Other stable annual rules:
- lower-granularity Evidence may be reused, but Selection roles/thesis are re-evaluated;
- broad intake + annual coverage audit + within-year temporal-skew audit precede Architecture;
- later outcomes are not back-projected into the covered year;
- sparse source availability remains an explicit limitation rather than evidence of historical absence;
- one annual issue remains preferred unless Evidence demonstrates a genuine coherence problem.

### 6.1 SP-2020-Y

Final provenance:
- source version `v0.19`;
- 27 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive corpus role:
- demonstrates that the annual method remains viable for an earlier/sparser evidence environment rather than only dense modern release years;
- a smaller final page count can still represent an annual period when event density and evidence warrant it;
- exact-byte publication contract is independent of period age.

Future implication:
- no fixed annual source/page minimum;
- completeness is an audited coverage claim with explicit limitations, not a record-count target.

### 6.2 SP-2021-Y

Final provenance:
- source version `v0.8`;
- 36 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive corpus role:
- confirms the annual Story unit / trajectory method across another historical period without depending on Monthly issues as prerequisites;
- supports re-evaluating source significance at annual scale rather than inheriting later taxonomy.

Future implication:
- Annual Profile is a repeatable specialization of the bounded Period Profile, not an edition-specific script family.

### 6.3 SP-2022-Y

Final provenance:
- source version `v0.10`;
- 37 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive corpus role:
- demonstrates that objective chronology and year-scale ecosystem synthesis can coexist;
- supports retaining event identity through compression rather than treating the annual article as a chronology dump.

Future implication:
- Event identity/provenance belongs to Core/Period state, while Story unit/trajectory construction belongs to Annual Profile semantics.

### 6.4 SP-2023-Y

Final provenance:
- source version `v0.15`;
- 41 pages;
- issue-only identity;
- exact-byte Publication Preview approval.

Positive patterns:
- full-width Detailed Chronology was explicitly useful as a compact historical index;
- unresolved dates were retained as boundaries rather than guessed;
- annual narrative preserved a separate higher-order synthesis instead of simply reproducing the chronology.

Failure lessons:
- chronology events without source/reference mapping lose reader-facing auditability;
- a selected chronology must link to existing source provenance without becoming a duplicate Evidence-card dump;
- empty Technical Notes/`Theme at a glance` wrappers must be suppressed when there are zero cards; template structure is not content.

Future ownership:
- event/source mapping and unknown-date preservation → `CORE + PERIOD_PROFILE`;
- empty wrapper suppression/layout → `PUBLICATION_PROFILE`;
- annual trajectory/synthesis → `ANNUAL specialization of PERIOD_PROFILE`.

## 7. Positive pattern families extracted across the corpus

### PAT-CORE-001 — Exact hashes make immutable iterative review practical

Across later Monthly, all Half-year, and all Annual final releases, internal source revisions coexist with one issue-only public identity and exact PDF/source hashes. Immutable intermediate revisions therefore do **not** require public semantic versions.

Retain:
- exact source manifest SHA;
- exact PDF SHA;
- build artifact identity;
- approval reference;
- freeze/release verification.

### PAT-CORE-002 — Two Human Gates are the mature endpoint of observed gate evolution

The corpus shows a real progression:

```text
M07
  revisioned release + post-Freeze user stops
    ↓
M06/M05/M04/M03
  issue-only identity + Freeze approval
    ↓
M02/M01 and later Half-year/Annual
  Architecture Review
  + exact-byte Publication Preview
  -> deterministic Visual Review / Freeze / merge / Release
```

This is strong empirical support for the Phase 1 normalized two-Human-Gate contract.

### PAT-CORE-003 — Structured Evidence and reader rendering must remain separate

Technical Notes evolution repeatedly demonstrates that repository Evidence should preserve:
- factual wording/source context;
- attribution class;
- identifiers;
- limitations;
- source identity.

Reader-facing publication may:
- render natural Japanese;
- map internal taxonomy to useful labels;
- compact repeated boilerplate;
- choose layout.

It must not mutate structured identifiers or invent facts.

### PAT-PERIOD-001 — Retrospective value is synthesis, not event accumulation

Monthly requires final issue synthesis. Half-year adds cross-month/reclassification/cross-layer synthesis. Annual adds Story units and Annual trajectories.

The progression is not three unrelated publication systems; it is one bounded Period family with granularity-specific synthesis semantics.

### PAT-PERIOD-002 — Narrative compression and chronology preservation are complementary

Half-year/Annual practice consistently supports:
- broad Evidence pool;
- narrative story/trajectory compression;
- separately preserved material objective chronology;
- source mapping rather than duplicate Evidence cards.

Core v2 should never force a choice between readable synthesis and historical traceability.

### PAT-PUB-001 — Mixed layout is a stable long-form publication behavior

After repeated correction, the long-form Special identity converged on:
- full-width frontmatter/headings/wide synthesis/chronology/reference-heavy material;
- local balanced two-column narrative;
- no global column switch that creates blank pages;
- breakable Technical Notes with local orphan controls.

This belongs to the long-form Publication Profile, not Research Core.

### PAT-QUALITY-001 — Visual Review finds defects semantic validation cannot

The corpus repeatedly exposed:
- empty TOC;
- empty wrapper pages;
- one-column regression;
- double bullets;
- isolated card tails;
- low-density bibliography pages;
- missing final synthesis after repair revisions.

Render-first Visual QA remains a required machine/Human-preview precursor; semantic validation alone is insufficient.

### PAT-QUALITY-002 — A repair must be judged against the coupled regression set

Examples:
- generic fallback removal was followed by subject/entity misattribution;
- aggressive page-break protection can fix orphan tails but reintroduce large whitespace/blank pages;
- mixed-layout repair can drop standfirst/synthesis/TOC structure if builders reconstruct documents incompletely.

Stable Core v2 fixes need regression sets, not single symptom checks.

## 8. Negative pattern families that must leave the future hot path

Do not promote these implementation habits:
- edition/revision-specific repair chains as canonical production architecture;
- monkey-patching Weekly regexes/functions/globals to make Special run;
- reconstructing full TeX/source from a partial repair template that can silently drop unrelated semantic sections;
- fixed page floors that preserve low-information pages;
- generic reader-facing fallback prose when Evidence is insufficient;
- unstructured keyword proximity for technical attribute extraction;
- collector success as completeness;
- duplicate Technical Notes as a substitute for chronology-source mapping;
- public revision identity for ordinary post-legacy Survey releases.

Their learned invariants remain valuable; their historical implementation ancestry does not.

## 9. Phase 2B conclusion

The fifteen-edition corpus supports the target architecture more strongly after positive-pattern analysis:

```text
Survey Production Core
  - provenance / identity / exact-byte authority
  - factual Evidence / traceability / claim boundaries
  - generic Human Gate and orchestration semantics
  - quality/regression contract

Retrospective Period Profile
  - bounded coverage/completeness
  - chronology
  - granularity-specific synthesis hooks
      Monthly
      Half-year
      Annual

Long-form Publication Profile
  - mixed layout
  - TOC/References/Technical Notes rendering
  - render-first QA
```

The corpus also confirms that future Thematic production cannot merely inherit the Period model: its completeness mechanism must be research-question/lineage driven rather than calendar-coverage driven.

**WU-003B exit condition is satisfied by this matrix:** all fifteen completed Retrospective Specials have an explicit row; both successful stable behavior and failure/repair lessons are represented; format-level knowledge is separated from exact historical repair implementation.
