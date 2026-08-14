# Half-year Retrospective Special production guide

Status: canonical editorial guidance for `HALF_YEAR` Retrospective Period Specials  
Established: 2026-08-14

## Purpose

Half-year Retrospective Specials use the current Special pipeline, Evidence model, provenance rules, Human Gates, Freeze model, and issue-only Release identity. The six-month coverage window changes editorial granularity, not the publication system.

Operational precedence is: current `main` code/config/schema/workflows, then `docs/special-human-gates.md` and `docs/special-editions.md`, then this guide. Repository state remains authoritative across chat sessions.

## Period and bootstrap

The requested half-year is resolved from the `HALF_YEAR` entries in `config/special-pipeline.json`. Six-month windows are taken from that configuration rather than inferred from older editions.

A production session first inspects:

- `specials/<slug>/edition.json`
- `sources/SP-<slug>/pipeline-state.json`
- `surveys/special/<slug>/`

An existing edition resumes from its recorded lifecycle state. A new edition receives a schema-valid manifest and initialized pipeline state using the current Special implementation.

Monthly editions are not a prerequisite. Existing monthly Evidence may be reused when valid, but monthly Selection roles, package structure, and thesis are not inherited automatically.

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

## Source Intake completeness and coverage audit

The reusable Source Intake collectors are a **broad discovery baseline, not a completeness proof**. Their configured arXiv categories, GitHub repository watchlist, and official-page watchlist inevitably lag changes in the ecosystem and may be uneven for older periods. A collector run that returns `success` means the configured sources were collected successfully; it does **not** mean that every material event in the covered period was found.

For a half-year retrospective, the following rules are mandatory before Candidate Selection and Architecture:

1. Run the canonical Source Intake with all enabled base collectors for the exact six-month window. A hand-curated event list, search result list, or reconstructed chronology may not replace this base intake.
2. Preserve the complete normalized intake through Screening. Do not pre-compress Source Intake to the events already expected to become editorial candidates.
3. Perform a **period-specific coverage audit** after base collection and before declaring Evidence reconstruction complete. The audit asks whether the intake materially covers the actors and technical surfaces that were active in that period, rather than assuming the current static watchlists are sufficient.
4. Audit at least these source planes where applicable:
   - major foundation/model vendors and open-weight model families active during the period;
   - multimodal image/audio/video model releases and generation systems;
   - reasoning, tool-use, search, agent/action, API and protocol surfaces;
   - serving, inference, quantization, local/edge and framework/runtime milestones;
   - retrieval, evaluation, safety/alignment and control-layer work;
   - material first-publication research papers relevant to the eventual technical synthesis.
5. Compare the base intake against period-specific known actors/events discovered from primary-source indexes, existing monthly provenance when available, and targeted first-party historical search. This comparison is discovery-oriented; it does not predetermine Selection roles.
6. When the audit finds a material gap, add a **supplemental primary-source gap-fill** with immutable provenance and feed the added records through the same Screening/Evidence boundary. Supplemental curated sources augment the base intake; they never substitute for it.
7. If a material source surface cannot be reconstructed reliably, retain that as an explicit coverage limitation. Absence from the configured collectors or a current index page is not evidence that the event did not occur.

There is intentionally no fixed minimum record count: source density varies by period. However, a retrospective Source Intake that is only a small hand-selected list of expected headline events is presumptively incomplete and must not be presented as the complete intake.

The repository should retain enough provenance to distinguish:

- base collector records;
- supplemental gap-fill records;
- duplicates or lifecycle-linked observations normalized later;
- unresolved coverage gaps.

Architecture Review may only describe Source Intake as complete after this coverage audit. The review must report base-intake count, supplemental/gap-fill count, Screening/Evidence counts, and material residual limitations separately.

## Half-year normalization and Selection

Before Architecture, the complete audited six-month Evidence pool is normalized across month boundaries. The review distinguishes:

- repeated references to the same objective event;
- model/product family continuation;
- announcement, preview, beta, GA, deprecation, and shutdown lifecycle events;
- model release, API availability, and framework/runtime integration;
- paper initial publication/submission and later revisions;
- same-name artifacts with distinct identities, such as model release, app release, system card, or API rollout;
- conflicting chronology metadata, favoring the most specific reliable primary source.

Distinct lifecycle events remain distinct chronology events even when narrative treatment groups them into one story.

Candidate Selection is performed again at half-year scale. Monthly `FEATURE_CORE`, `SECTION_CORE`, `SUPPORTING_EVIDENCE`, `PAPER_WATCH`, `CHRONOLOGY`, or hold decisions are inputs rather than binding classifications.

Compression is primarily performed at the **story/article-unit** level. A chain such as model release -> API rollout -> framework support -> serving support can form one longitudinal story while retaining its separate chronology events.

## Architecture principles

Each half-year derives its own cluster names, chapter count, and editorial thesis from contemporaneous Evidence. Taxonomy from another period is not a template for historical interpretation.

A half-year Architecture should support both historical record and longitudinal analysis. Where supported by Evidence, it includes four functions:

1. **Cross-month comparison** — the same technical axis compared across early, middle, and late portions of the period.
2. **Half-year reclassification** — categories that become visible only when the six months are considered together.
3. **Cross-layer synthesis** — interactions between technical layers where progress in one layer changes constraints in another.
4. **Half-year Synthesis** — what changed across the period, what did not change, and what remained unresolved at the coverage boundary.

The first Architecture Review should present at least:

- exact coverage and retrospective-as-of date;
- base Source Intake count, supplemental gap-fill count, coverage-audit status, Screening/Evidence counts, and material limitations;
- cross-period normalization results and important identity decisions;
- material chronology conflicts and claim boundaries;
- Selection role counts and proposed cross-period story units;
- major clusters and proposed packages;
- primary/supporting Evidence assignments;
- approximate reader-facing chronology event count;
- cross-month comparison, reclassification, and cross-layer synthesis candidates;
- editorial-thesis candidates;
- provisional page allocation and notable hold/exclude decisions.

Reader-facing drafting begins after Architecture approval.

## Reader-facing drafting

Published issue text is for readers. Internal comments, production-chat instructions, Human Gate discussion, Candidate/Draft Package workflow vocabulary, future compilation plans, and internal QA notes remain outside the issue body.

Reader-visible Source Notes, claim attribution, lifecycle qualification, chronology caveats, and clearly identified editorial inference remain appropriate.

Narrative sections are longitudinal rather than six monthly recaps. Research papers normally appear in the technical chapter they help explain; a separate Paper Watch is used only when the period itself supports that reader-facing structure.

## Layout and page budget

The shared Special layout on current `main` is used. Normal narrative body is two-column. Full-width material is reserved for cases where width improves comprehension, including cover/frontmatter, wide tables, chronology, maps, or diagrams.

Page count is treated as an output rather than a quota. Current schemas require page-budget values, so half-year manifest and Architecture values act as planning/control envelopes. They are not targets to be reached by padding or constraints that justify removing material technical events. Final length is evaluated after drafting and layout.

## Detailed Chronology

The reader-facing chronology preserves material objective events even when the narrative combines them into broader stories. Release, preview/beta/GA transition, deprecation/shutdown, material API availability, important OSS/runtime milestones, and relevant paper initial-publication events normally remain independently identifiable.

The complete Evidence ledger may remain repository provenance; the published chronology is a selected historical index rather than a dump of every Evidence task.

## Validation and SKIP policy

Post-draft validation applies the current Special/monthly check stack wherever checker assumptions match a half-year edition. Genuine claim, Evidence, chronology, TeX, PDF, layout, or provenance defects remain failures.

A checker that is structurally tied to single-calendar-month coverage or monthly article granularity is recorded as `SKIP` rather than as a document failure. The QA record includes the checker name, the incompatible assumption, any equivalent half-year substitute check, its result, and whether later checker generalization is appropriate.

This policy does not weaken a checker that found a genuine defect.

## Evidence and chronology invariants

Primary sources are preferred for objective chronology and lifecycle. Vendor, project, and author claims retain attribution. Availability states retain their contemporary boundaries. Later revisions and later outcomes are not back-projected into the covered period. Uneven source availability is reported as a coverage limitation rather than interpreted as proof of historical absence.

## Session invocation

Special session startup is defined by `docs/special-session-bootstrap.md` and the repository-level `AGENTS.md`. A half-year production session normally needs only the target and stopping gate:

> `<target> SpecialをArchitecture Reviewまで編纂してください。`

If repository identity is not already clear from context:

> `eariver/japanese-generative-ai-survey で <target> SpecialをArchitecture Reviewまで編纂してください。`

The repository expands this short request into the current bootstrap, initialization/resume, pipeline, and Human Gate rules. Do not require the user to restate those rules in each new chat session.

## Non-goals

This guide intentionally defines no fixed chapter count, technical taxonomy, page count, monthly-to-half-year compression ratio, or requirement to create monthly editions first. Those values are outputs of each period's Evidence and Architecture.
