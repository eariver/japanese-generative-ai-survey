# Japanese Generative AI Technical Survey Special

Status: active design and operations contract  
Established: 2026-08-10  
Updated: 2026-08-16

## 1. Purpose

`Japanese Generative AI Technical Survey Special` is the non-weekly companion series to the regular Weekly survey.

The Special series has two edition kinds:

- **Retrospective Period Special** — reconstruct a defined historical period from primary sources using current hindsight;
- **Thematic Special** — reconstruct the technical history or current state of one topic, model family, ecosystem, region, or architectural trend.

The downstream editorial philosophy remains Evidence-first. Special does not become a generic history essay or an unchecked summary simply because the coverage window is historical.

## 2. Current lifecycle and Human Gates

Operational source of truth is current `main`, especially `config/special-pipeline.json`, `scripts/special_pipeline.py`, and `docs/special-human-gates.md`.

Normal production has exactly two Human Gates:

```text
Initialization / resume (no Human Gate)
  -> Source Intake
  -> Screening / Evidence
  -> Candidate Selection (internal checkpoint)
  -> Architecture Proposal
  -> HUMAN GATE 1: Architecture Review
  -> Drafting / validation / layout / PDF build
  -> HUMAN GATE 2: Publication Preview
  -> Visual Review record
  -> Freeze
  -> work-PR merge
  -> exact frozen PDF/source verification
  -> GitHub Release
```

Candidate Selection remains auditable but is not a separate user stop. Publication Preview approval binds the exact PDF SHA-256 and authorizes deterministic Visual Review recording, Freeze, work-PR merge, and public Release for those identical bytes. Freeze and Public Release are therefore machine/provenance transitions rather than additional normal Human Gates.

An on-demand Exception Gate is raised only when a new editorial/publication decision is genuinely required. Deterministic technical recovery that preserves approved content/provenance is not a Human Gate.

## 3. Session bootstrap and initialization

Cross-session startup is defined by `AGENTS.md` and `docs/special-session-bootstrap.md`.

A configured target plus a requested stopping Human Gate is sufficient. For example:

> `eariver/japanese-generative-ai-survey で2024-H2 SpecialをArchitecture Reviewまで編纂してください。`

If the edition is absent, the start request itself authorizes deterministic initialization: create the init branch, create/validate the edition manifest and initial pipeline state, merge the bootstrap PR, create the canonical work branch, and continue to the requested Human Gate. Initialization is not a Human Gate and does not require a separate user confirmation.

If edition state already exists, resume from repository-recorded lifecycle/provenance rather than restarting.

## 4. Historical granularity

Historical cadence is defined exclusively by `config/special-pipeline.json`. Do not infer periods from older releases or from stale historical examples.

Current configured Retrospective Period Specials are:

### Monthly tier

Calendar-month editions for January through July 2026:

```text
2026-M01 ... 2026-M07
```

### Half-year tier

Natural calendar halves for 2024 and 2025:

```text
2024-H1  2024-01-01 -> 2024-06-30
2024-H2  2024-07-01 -> 2024-12-31
2025-H1  2025-01-01 -> 2025-06-30
2025-H2  2025-07-01 -> 2025-12-31
```

Half-year editorial behavior additionally follows `docs/half-year-retrospective-specials.md`.

### Annual tier

Calendar-year retrospectives are configured for 2020 through 2023:

```text
2020-Y ... 2023-Y
```

Annual editorial behavior additionally follows `docs/annual-retrospective-specials.md`. Annual editions preserve event-level chronology while compressing narrative through story units and evidence-backed annual trajectories; high event density alone does not justify splitting a configured year.

History before 2020 is deferred by default and requires an explicit later scope/cadence decision.

## 5. Retrospective method

A retrospective edition is written from the present review date, not by pretending the editor is living at the end of the historical period.

The manifest therefore records separately:

- `coverage.start` / `coverage.end` — when the underlying events occurred;
- `retrospective_as_of` — when the evidence was reconstructed and interpreted.

Later outcomes may be used to explain technical significance, but prose must distinguish contemporary facts from hindsight. Later facts must not be back-projected into the covered period.

## 6. X / Grok policy

### Weekly

Grok/X remains important because Weekly is specifically observing current momentum and community reaction.

### Retrospective Period Special

Historical Grok/X research is **disabled by default**. The purpose is primary-source reconstruction, not restoration of an old social-media timeline.

Historical X reactions may be added exceptionally as contextual evidence, but they are neither required nor a substitute for primary sources.

### Thematic Special

Grok/X is **optional by default**. Use it when recent community perception, recent experiments, or reaction to a major new event materially helps explain the theme.

In all editions, social observations remain separate from technical facts.

## 7. Reader-facing editorial rules

Published prose must not leak internal pipeline vocabulary such as Candidate Inventory, verification queue, Selection state, or Draft Package state. Reader-visible claim boundaries remain; internal production metadata stays in Source Notes or repository provenance.

Every substantive Special package must have a reader-facing rationale for why the event/artifact is necessary to understand the selected period or theme.

For half-year retrospectives, cross-month comparison, half-year reclassification, cross-layer synthesis, and final half-year synthesis are considered during Architecture rather than being bolted on after drafting.

For annual retrospectives, year-wide normalization, story-unit to annual-trajectory construction, evidence-derived phase analysis where useful, annual reclassification, cross-layer synthesis, and final annual synthesis are considered during Architecture rather than being bolted on after drafting.

## 8. Canonical identifiers and paths

Machine identifier:

```text
SP-<slug>
```

Canonical bootstrap branch for a new configured edition:

```text
special/<slug>-init
```

Canonical work branch:

```text
special/<slug>-work
```

Canonical content roots:

```text
specials/<slug>/edition.json
surveys/special/<slug>/
sources/SP-<slug>/
```

Public Release identity is **issue-only**. Release tags use:

```text
special/<slug>
```

Internal source revisions such as `v0.4` remain provenance only; they are not public Release versions.

## 9. Publication integrity

Publication Preview approval is bound to the exact reviewed PDF SHA-256. Freeze and Release must preserve that identity. The publisher re-fetches the approved/frozen artifact and verifies exact bytes before publishing the issue-only GitHub Release.

No unattended public release authority exists before Publication Preview approval.
