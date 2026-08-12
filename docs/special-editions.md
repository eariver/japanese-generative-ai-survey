# Japanese Generative AI Technical Survey Special

Status: active design and operations contract  
Established: 2026-08-10

## 1. Purpose

`Japanese Generative AI Technical Survey Special` is the non-weekly companion series to the regular Weekly survey.

The Special series has two edition kinds:

- **Retrospective Period Special** — reconstruct a defined historical period from primary sources using current hindsight;
- **Thematic Special** — reconstruct the technical history or current state of one topic, model family, ecosystem, region, or architectural trend.

The downstream editorial philosophy remains Evidence-first. Special does not become a generic history essay or an unchecked summary simply because the coverage window is historical.

## 2. Relationship to Weekly

Weekly answers primarily: **what became technically important now?**

Special answers primarily: **what happened across this period or theme, and what structure becomes visible when it is reconstructed as a whole?**

Weekly's Friday 18:00 `America/New_York` cutoff remains untouched. Special never relabels or bypasses the Weekly calendar resolver. Every Special fixes its own explicit coverage window in an edition manifest.

The common downstream lifecycle remains:

```text
Source Intake
  -> Screening
  -> Evidence
  -> Candidate Comparison
  -> Human Candidate Selection
  -> Human Issue Architecture approval
  -> Drafting
  -> Claim/chronology validation
  -> TeX/PDF
  -> Human visual review
  -> Human Freeze
  -> normal work-PR merge
  -> exact frozen source/PDF SHA verification
  -> GitHub Release
```

**Freeze is the final Human publication gate.** Freeze binds the exact reviewed source manifest and PDF SHA-256, authorizes the normal work-PR merge, and grants publication authority for the corresponding issue-only Release. There is no additional independent Human public-Release approval after Freeze. Publication still fails closed unless the publisher can re-fetch and verify the exact frozen source and PDF bytes recorded by the Freeze manifest.

## 3. Historical granularity

The default backfill cadence is intentionally coarser as history recedes.

Cross-session bootstrap behavior is documented in [`docs/retrospective-special-backfill-status.md`](retrospective-special-backfill-status.md). The target period is supplied by the user's task prompt; that document intentionally does not maintain a `next edition` pointer or duplicated completion ledger. Repository state remains authoritative for whether the requested edition is new, in progress, frozen, or already released. This document remains the historical-granularity policy source of truth.

### Monthly tier

From **2025-08-01 through 2026-07-31**, create one Retrospective Period Special per calendar month.

This provides exactly one year of monthly history immediately before the Weekly series began in August 2026.

### Half-year tier

From **2022-11-01 through 2025-07-31**, use six-month windows anchored to November and May.

The final window is truncated at 2025-07-31 so it does not overlap the monthly tier:

```text
2022-11 -> 2023-04
2023-05 -> 2023-10
2023-11 -> 2024-04
2024-05 -> 2024-10
2024-11 -> 2025-04
2025-05 -> 2025-07   # transition window
```

### Annual tier

Before **2022-11-01**, annual-scale retrospectives are the default. Exact annual editions are created on demand rather than exhaustively generated in advance.

When an older subject warrants finer resolution, create a **Thematic Special** instead of permanently increasing the default historical cadence.

## 4. Retrospective method

A retrospective edition is written from the present review date, not by pretending the editor is living at the end of the historical period.

The manifest therefore records separately:

- `coverage.start` / `coverage.end` — when the underlying events occurred;
- `retrospective_as_of` — when the evidence was reconstructed and interpreted.

Later outcomes may be used to explain technical significance, but the prose must distinguish contemporary facts from hindsight.

## 5. X / Grok policy

### Weekly

Grok/X remains important because Weekly is specifically observing current momentum and community reaction.

### Retrospective Period Special

Historical Grok/X research is **disabled by default**. The purpose is primary-source reconstruction, not restoration of an old social-media timeline.

Historical X reactions may be added exceptionally as contextual evidence, but they are neither required nor a substitute for primary sources.

### Thematic Special

Grok/X is **optional by default**. Use it when recent community perception, recent experiments, or reaction to a major new event materially helps explain the theme.

In all editions, social observations remain separate from technical facts.

## 6. Reader-facing editorial rules

Issue #9 rules apply to Special as well as Weekly.

Published prose must not leak internal pipeline vocabulary such as Candidate Inventory, Reaction Pass, verification queue, Selection state, or Draft Package state. Reader-visible claim boundaries remain; internal production metadata stays in Source Notes or repository provenance.

Every substantive Special package must have a reader-facing **why this Special** rationale: why that event or artifact is necessary to understand the chosen period/theme.

Watchlist-style sections use reader-facing `現状 / 未確認 / 注視点` semantics rather than editorial queue-management language.

## 7. Canonical identifiers and paths

Machine identifier:

```text
SP-<slug>
```

Example:

```text
SP-2026-M07
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

The public Release title and asset name likewise use the issue identity without an internal source revision. Source revisions such as `v0.12` remain repository provenance used to identify the exact frozen source; they are not public Release versions.

## 8. First edition

The first implementation and end-to-end validation target is:

```text
SP-2026-M07
Japanese Generative AI Technical Survey Special — 2026年7月 Retrospective
Coverage: 2026-07-01T00:00:00Z -> 2026-07-31T23:59:59Z
Community research: DISABLED
```

This edition is both a real publication and the acceptance test for the Special pipeline.
