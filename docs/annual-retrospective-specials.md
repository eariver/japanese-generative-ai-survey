# Annual Retrospective Special production guide

Status: canonical editorial guidance for `ANNUAL` Retrospective Period Specials  
Established: 2026-08-16

## Purpose

Annual Retrospective Specials use the current Special pipeline, Evidence model, provenance rules, Human Gates, Freeze model, and issue-only Release identity. A twelve-month coverage window changes editorial compression and synthesis depth, not the publication system.

Operational precedence is: current `main` code/config/schema/workflows, then `docs/special-human-gates.md` and `docs/special-editions.md`, then this guide. Repository state remains authoritative across chat sessions.

## Period and bootstrap

The requested year is resolved from the `ANNUAL` entries in `config/special-pipeline.json`. Calendar-year windows are taken from that configuration rather than inferred from older editions.

A production session first inspects:

- `specials/<slug>/edition.json`
- `sources/SP-<slug>/pipeline-state.json`
- `surveys/special/<slug>/`

An existing edition resumes from its recorded lifecycle state. A new edition receives a schema-valid manifest and initialized pipeline state using the current Special implementation.

Monthly or half-year editions are not prerequisites. Existing lower-granularity Evidence may be reused when valid, but their Selection roles, package structure, taxonomy, and thesis are not inherited automatically.

## Human Gates

The normal gate sequence is shared with current Specials:

```text
Source Intake / coverage audit / Screening / Evidence
  -> Candidate Selection (internal checkpoint)
  -> Architecture Proposal
  -> HUMAN GATE 1: Architecture Review
  -> Drafting / Validation / Layout / Build
  -> Publication Preview PDF
  -> HUMAN GATE 2: Publication Preview
  -> Visual Review record / Freeze / Merge / Release
```

Candidate Selection is reviewed together with Architecture rather than as a separate user stop. Exception Gates follow `docs/special-human-gates.md` and are reserved for genuinely new editorial/publication decisions.

## Source Intake completeness and annual coverage audit

The reusable Source Intake collectors are a broad discovery baseline, not a completeness proof. A collector run that returns `success` proves only that the configured source surfaces were collected successfully. It does not prove that a full calendar year has been reconstructed evenly or comprehensively.

For an annual retrospective, the following rules are mandatory before Candidate Selection and Architecture:

1. Run the canonical Source Intake with all enabled base collectors for the exact twelve-month window. A hand-curated chronology may not replace this base intake.
2. Preserve the complete normalized intake through Screening. Do not pre-compress Source Intake to expected headline events.
3. Perform a period-specific coverage audit after base collection and before declaring Evidence reconstruction complete.
4. Audit at least these source planes where applicable:
   - major foundation/model vendors and open-weight model families active during the year;
   - multimodal image/audio/video model releases and generation systems;
   - reasoning, tool-use, search, agent/action, API and protocol surfaces;
   - serving, inference, quantization, local/edge and framework/runtime milestones;
   - retrieval, evaluation, safety/alignment and control-layer work;
   - material first-publication research papers relevant to the eventual technical synthesis.
5. Compare the base intake against period-specific known actors/events discovered from primary-source indexes, existing lower-granularity provenance when available, and targeted first-party historical search.
6. When the audit finds a material gap, add supplemental primary-source gap-fill with immutable provenance and feed those records through the same Screening/Evidence boundary.
7. If a material source surface cannot be reconstructed reliably, retain that as an explicit coverage limitation.

Annual coverage audits must additionally test for **within-year temporal skew**. The year should be inspected in coarse diagnostic slices such as calendar quarters or evidence-derived phases so that a dense collector surface in one portion of the year does not conceal weak reconstruction elsewhere. These diagnostic slices are audit instruments only; they do not create quarterly publication units.

The review should retain enough provenance to distinguish:

- base collector records;
- supplemental gap-fill records;
- duplicates or lifecycle-linked observations normalized later;
- unresolved coverage gaps;
- material within-year temporal skew discovered during the audit.

There is intentionally no fixed minimum record count. Event density varies greatly by year. Architecture Review may describe Source Intake as complete only after the annual coverage audit and must report base-intake count, supplemental/gap-fill count, Screening/Evidence counts, and material residual limitations separately.

## Year-wide normalization

Before Architecture, the complete audited annual Evidence pool is normalized across the entire year. The review distinguishes:

- repeated references to the same objective event;
- model/product family continuation;
- announcement, preview, beta, GA, deprecation, and shutdown lifecycle events;
- model release, API availability, and framework/runtime integration;
- paper initial publication/submission and later revisions;
- same-name artifacts with distinct identities;
- conflicting chronology metadata, favoring the most specific reliable primary source.

Distinct lifecycle events remain distinct chronology events even when narrative treatment groups them into a broader story.

Candidate Selection is performed again at annual scale. Monthly or half-year `FEATURE_CORE`, `SECTION_CORE`, `SUPPORTING_EVIDENCE`, `PAPER_WATCH`, `CHRONOLOGY`, hold, or exclude decisions are inputs rather than binding classifications.

## Story units and annual trajectories

Annual retrospectives require one additional editorial compression layer beyond the half-year method.

Use three nested units:

1. **Event** — an objective dated release, publication, availability transition, repository milestone, paper publication, deprecation, or comparable occurrence.
2. **Story unit** — a lifecycle or family-level narrative that may combine multiple related events while preserving each event in chronology.
3. **Annual trajectory** — a year-scale technical direction that combines multiple story units into a coherent structural change across time, layers, organizations, or deployment constraints.

Compression should therefore follow:

```text
Event -> Story unit -> Annual trajectory -> Annual thesis
```

Do not manufacture trajectories merely to reduce chapter count. A valid trajectory must be supported by multiple Evidence-backed observations and should explain a meaningful change that becomes clearer at year scale than at event scale.

## Architecture principles

Each annual edition derives its own trajectory names, cluster names, chapter count, phase boundaries, and editorial thesis from contemporaneous Evidence. Taxonomy from another year or from a later half-year edition is not a template for historical interpretation.

An annual Architecture should support both historical record and year-scale structural analysis. Where supported by Evidence, it includes four functions:

1. **Cross-period comparison** — compare evidence-derived phases of the year rather than mechanically writing twelve monthly recaps.
2. **Annual reclassification** — identify technical categories or relationships that become visible only when the whole year is considered together.
3. **Cross-layer synthesis** — explain interactions among model design, training, inference, tooling, deployment, multimodality, data, safety, and product/API surfaces where one layer changes constraints in another.
4. **Annual synthesis** — state how the technical design space changed from the beginning to the end of the year, what did not change, and what remained unresolved at the coverage boundary.

Phase boundaries are analytical outputs, not preset quarters. Calendar quarters may be used during coverage auditing, but reader-facing phases should be evidence-derived when a phase structure is useful.

## Architecture Review contract

The first Architecture Review should present at least:

- exact coverage and retrospective-as-of date;
- base Source Intake count, supplemental gap-fill count, annual coverage-audit status, Screening/Evidence counts, and material limitations;
- within-year temporal-skew audit and any weakly reconstructed intervals;
- year-wide normalization results and important identity/lifecycle decisions;
- material chronology conflicts and claim boundaries;
- Selection role counts;
- proposed story units and annual trajectories;
- major clusters and proposed packages;
- primary/supporting Evidence assignments;
- approximate reader-facing chronology event count;
- evidence-derived phase candidates where useful;
- cross-period comparison, annual reclassification, and cross-layer synthesis candidates;
- editorial-thesis candidates;
- provisional page allocation and notable hold/exclude decisions;
- an explicit assessment of whether the year remains editorially coherent as one volume.

Reader-facing drafting begins only after Architecture approval.

## Single-volume coherence and Exception Gate

Configured annual periods are presumed to remain annual. High Source Intake or Evidence counts alone do not justify splitting an edition.

A split or cadence change is considered only when the audited Evidence demonstrates that a single annual Architecture cannot reasonably preserve historical meaning. Signals may include:

- two or more largely independent technical eras with no defensible year-scale synthesis;
- a trajectory/package count so high that substantial material would have to be omitted solely to preserve a single-volume form;
- chronology density that cannot be represented as a useful selected historical index without destroying essential lifecycle boundaries;
- page requirements that exceed a reasonable planning envelope even after story-unit and trajectory compression;
- a proposed split that changes publication identity or configured historical cadence.

If those conditions create a genuine editorial decision, raise an Exception Gate under `docs/special-human-gates.md`. Do not silently split the year, and do not treat event count alone as sufficient evidence for splitting.

## Reader-facing drafting

Published issue text is for readers. Internal comments, production-chat instructions, Human Gate discussion, Candidate/Draft Package workflow vocabulary, future compilation plans, and internal QA notes remain outside the issue body.

Narrative sections are trajectory-oriented rather than twelve monthly recaps. Research papers normally appear in the technical chapter they help explain; a separate Paper Watch is used only when the year itself supports that reader-facing structure.

Year-scale hindsight may be used to explain significance, but later outcomes must not be back-projected into the covered year as if they were known contemporaneously.

## Layout and page budget

The shared Special layout on current `main` is used. Normal narrative body is two-column. Full-width material is reserved for cases where width improves comprehension, including cover/frontmatter, wide tables, chronology, phase maps, or diagrams.

Page count is an output rather than a quota. Manifest and Architecture page-budget values are planning/control envelopes, not targets to be reached by padding and not excuses to remove material technical events before annual compression has been attempted.

## Detailed Chronology

Reader-facing chronology preserves material objective events even when the narrative combines them into stories or annual trajectories. Release, preview/beta/GA transition, deprecation/shutdown, material API availability, important OSS/runtime milestones, and relevant paper initial-publication events normally remain independently identifiable.

The complete Evidence ledger may remain repository provenance; the published chronology is a selected historical index rather than a dump of every Evidence task.

Annual narrative compression must therefore not erase chronology resolution.

## Validation and SKIP policy

Post-draft validation applies the current Special/monthly check stack wherever checker assumptions match an annual edition. Genuine claim, Evidence, chronology, TeX, PDF, layout, or provenance defects remain failures.

A checker structurally tied to single-calendar-month or half-year assumptions is recorded as `SKIP` rather than as a document failure. The QA record includes the checker name, incompatible assumption, equivalent annual substitute check where available, its result, and whether later checker generalization is appropriate.

This policy does not weaken a checker that found a genuine defect.

## Evidence and chronology invariants

Primary sources are preferred for objective chronology and lifecycle. Vendor, project, and author claims retain attribution. Availability states retain their contemporary boundaries. Later revisions and later outcomes are not back-projected into the covered period. Uneven source availability is reported as a coverage limitation rather than interpreted as proof of historical absence.

## Session invocation

Special session startup is defined by `docs/special-session-bootstrap.md` and repository-level `AGENTS.md`. An annual production session normally needs only the target and stopping gate:

> `<target> SpecialをArchitecture Reviewまで編纂してください。`

If repository identity is not already clear from context:

> `eariver/japanese-generative-ai-survey で <target> SpecialをArchitecture Reviewまで編纂してください。`

The repository expands this short request into the current bootstrap, initialization/resume, pipeline, annual coverage-audit, trajectory construction, and Human Gate rules.

## Non-goals

This guide intentionally defines no fixed trajectory count, chapter count, technical taxonomy, phase count, page count, Evidence count, or annual-to-half-year compression ratio. Those values are outputs of each year's audited Evidence and Architecture.
