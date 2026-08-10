# Special Retrospective Editorial Policy

Status: adopted editorial baseline as of 2026-08-11 JST.

This document records the default temporal cadence and volume-sizing policy for retrospective editions of the Japanese Generative AI Technical Survey Special series. It is deliberately explicit so future sessions do not reconstruct the cadence from the Weekly calendar or from an obsolete algorithmic rule.

## 1. July 2026 Special volume policy

`SP-2026-M07` is a **single-volume Special**.

Special editions are allowed to be materially longer than Weekly issues because their purpose is synthesis over a wider period rather than a weekly digest. For July 2026:

- target length: **32 pages**;
- normal hard ceiling: **40 pages**;
- do not pre-emptively split the issue into multiple volumes;
- do not silently exceed 40 pages after Issue Architecture is approved;
- if a coherent architecture cannot fit within 40 pages, return to **Candidate Selection before Issue Architecture approval** and reduce, consolidate, or explicitly redesign scope;
- a multi-volume split is therefore an exceptional editorial redesign, not an automatic response to page pressure.

The reason for preferring one larger volume is editorial coherence: the July candidates appear to describe one connected monthly transition across frontier models, multimodality, inference/serving, agents, and agent safety. The 40-page ceiling protects claim/chronology checking, LaTeX consistency, visual review, and final release inspection from becoming unbounded.

Human gates remain unchanged. Candidate Selection, Issue Architecture, visual review, Freeze, and public Release cannot be inferred from page-budget compliance.

## 2. Default retrospective cadence

The retrospective back-catalogue is intentionally **not** a uniform monthly series. Temporal resolution decreases with historical distance so the project does not create many low-density volumes merely because a calendar partition exists.

### Monthly editions

Create one monthly retrospective for each of:

- 2026/01
- 2026/02
- 2026/03
- 2026/04
- 2026/05
- 2026/06
- 2026/07

August 2026 onward is covered by the Weekly series and should not be duplicated by the default retrospective cadence.

### Half-year editions

Use natural calendar halves:

- 2024/前半 — 2024-01-01 through 2024-06-30
- 2024/後半 — 2024-07-01 through 2024-12-31
- 2025/前半 — 2025-01-01 through 2025-06-30
- 2025/後半 — 2025-07-01 through 2025-12-31

This replaces the earlier November/May-anchored design. Natural January-June / July-December halves are easier to understand and avoid forcing either a short boundary volume or an arbitrary February/August cadence.

### Annual editions

Use one annual retrospective for each of:

- 2020
- 2021
- 2022
- 2023

**2023 is intentionally annual in the default plan.** It is acknowledged as a dense year, with multiple major model families and products appearing during the year, but density alone is not yet sufficient reason to double the volume count. The project should first measure actual Source Intake, Evidence, and Candidate density. If a future 2023 run demonstrates that a coherent annual Issue Architecture cannot be produced within a reasonable Special page budget, 2023 may be explicitly revised into half-year editions. It must not be split merely in anticipation.

## 3. 2010s and earlier

Historical coverage before 2020 is **deferred** rather than automatically scheduled.

The 2010s contain foundational events whose significance is now primarily historical. If this period is addressed later, prefer broad historical volumes or thematic Specials instead of annual or monthly cadence. Plausible future blocks include:

- 2015-2019 — GAN expansion, attention/Transformer-era developments, AlphaGo-era milestones, early GPT lineage;
- 2010-2014 — ImageNet/AlexNet-era deep-learning acceleration, word embeddings, and the original GAN proposal.

These blocks are examples, not approved editions. Five-year versus ten-year treatment is intentionally left for a later editorial decision.

## 4. Thematic Special escape hatch

Calendar cadence is a default compression policy, not a prohibition on detail.

When a historical subject deserves finer treatment than its default period volume can support, create a **THEMATIC Special** rather than increasing the default cadence for the entire era. This is especially appropriate for a technology, model family, incident, benchmark transition, or ecosystem shift whose causal/technical story benefits from concentrated Evidence review.

## 5. Machine-readable authority

The machine-readable source of truth for this cadence is:

`config/special-pipeline.json` → `historical_granularity`

`python scripts/special_pipeline.py history-plan` must enumerate the exact approved retrospective periods rather than extrapolating additional periods algorithmically.

The July 2026 page policy is additionally pinned in:

`specials/2026-M07/edition.json`

Any future cadence or page-policy change should update this document, the machine-readable configuration, and relevant contract tests in the same PR.

## 6. Current July 2026 operational checkpoint

At the time this policy was adopted, `SP-2026-M07` had completed reviewed Source Intake, complete Screening, and complete Evidence acceptance. The lifecycle had reached **EVIDENCE_REVIEWED** and Candidate Selection remained an explicit pending Human Gate.

The working editorial direction is a single expanded Special, with the Evidence-backed candidates consolidated into a small number of coherent editorial packages rather than one article per Evidence candidate.
