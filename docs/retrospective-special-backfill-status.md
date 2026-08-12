# Retrospective Special Backfill Status

Status: active cross-session checkpoint  
Updated: 2026-08-12

## Purpose

This file is the minimal bootstrap checkpoint for continuing the historical Retrospective Period Special series in a new chat/session without relying on prior conversation history.

The repository is the source of truth. For production rules, always use the current `main` branch rather than copying old one-off workflows or inferring obsolete release behavior from earlier releases.

## Current position

Completed monthly Retrospective Period Specials:

- `SP-2026-M07`
- `SP-2026-M06`
- `SP-2026-M05`

**Next edition:** `SP-2026-M04`

Coverage for the next edition:

```text
2026-04-01T00:00:00Z -> 2026-04-30T23:59:59Z
```

After M04, continue backward one calendar month at a time through the monthly tier defined in `docs/special-editions.md`.

## New-session bootstrap

When asked to start the next historical Special, use this order:

1. Read `docs/special-editions.md` for the current Special lifecycle, identifiers, coverage rules, Human Gates, Freeze authority, and issue-only Release identity.
2. Read this file to determine the next historical edition. Do not infer the next month from chat history.
3. Read the latest completed issue handoff, currently `sources/SP-2026-M05/HANDOFF.md`, as the most recent end-to-end production reference.
4. Use the current shared scripts/workflows on `main`. Do not reuse M05/M06 one-shot helper workflows as canonical production interfaces.
5. Initialize the next edition manifest and work branch, then perform Source Intake -> Screening -> Evidence using the normal Special pipeline.
6. Stop at Human Gates unless the user explicitly authorizes a later gate. Do not infer Candidate Selection, Architecture, Visual Review, or Freeze approval from prior editions.
7. Before Preview, apply current reader-facing Technical Notes, period-consistency, layout, and full-page Visual QA controls already integrated into `main`.
8. Freeze remains the final Human publication gate. After Freeze, normal work-PR merge and exact frozen source/PDF SHA verification may proceed to the issue-only GitHub Release without a separate Human public-Release approval.

## Current production baseline

The most recent completed edition is `SP-2026-M05`.

Its final state records the current production expectations:

- Source Intake / Screening / Evidence provenance is retained and SHA-bound.
- Candidate Selection and Issue Architecture remain explicit Human Gates unless the user changes the gate plan for that edition.
- Preview candidates must pass TeX/log checks and full-page render self-review before Human Visual Review.
- Pre-release review findings must be repaired in a new immutable source revision and self-checked again before approval.
- Public Release identity is issue-only: `special/<slug>`.
- Internal source revisions are provenance only and are not public Release versions.

## Backfill transition

The long-range cadence remains defined only by `docs/special-editions.md`. This checkpoint records progress, not policy. When the monthly tier is exhausted, consult that document for the transition to the coarser historical tier before initializing another edition.
