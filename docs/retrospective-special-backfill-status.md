# Retrospective Special Backfill Bootstrap

Status: stable cross-session bootstrap contract  
Updated: 2026-08-12

## Purpose

This file defines the minimal bootstrap behavior for starting or resuming a historical Retrospective Period Special in a new chat/session without relying on prior conversation history.

The repository is the source of truth. For production rules and implementation details, always use the current `main` branch rather than copying old one-off workflows or inferring obsolete behavior from earlier releases.

**This file is intentionally not a per-edition progress ledger. It does not record a `next edition`, a `latest completed edition`, or a `latest handoff`, and it does not need to be updated when each Special is completed.**

## Target selection contract

The target period is supplied explicitly by the user's task prompt.

Examples:

- `Specialの2026年3月分` -> `SP-2026-M03`
- `Specialの2025年12月分` -> `SP-2025-M12`

Do not infer the target month from:

- the most recently completed Special;
- gaps in the historical sequence;
- previous chat history;
- this bootstrap document.

For a monthly Retrospective Period Special, derive the exact UTC calendar-month coverage from the user-specified month and record it in the edition manifest. If the requested target is outside the monthly tier, consult `docs/special-editions.md` for the applicable historical granularity before initializing the edition.

## New-session bootstrap

When asked to start or continue a historical Special, use this order:

1. Read `docs/special-editions.md` for the current Special lifecycle, identifiers, coverage rules, Human Gates, Freeze authority, and issue-only Release identity.
2. Resolve the requested target period from the user's prompt. The prompt is authoritative for which edition to work on.
3. Inspect the current `main` repository state for the resolved slug, especially:
   - `specials/<slug>/edition.json`
   - `sources/SP-<slug>/pipeline-state.json`
   - `surveys/special/<slug>/`
4. If the target edition already exists, resume from its repository-recorded lifecycle state and provenance. Do not reinitialize or infer state from chat history.
5. If the target edition does not exist, initialize its edition manifest and canonical work branch, then perform Source Intake -> Screening -> Evidence using the normal Special pipeline.
6. Use the current shared scripts/workflows on `main`. Historical M05/M06 or other one-shot helper workflows are not canonical production interfaces.
7. Stop at Human Gates unless the user explicitly authorizes that gate. Do not infer Candidate Selection, Architecture, Visual Review, or Freeze approval from prior editions.
8. Before Human Visual Review, apply the current reader-facing Technical Notes, taxonomy normalization, period-consistency, layout, TeX/log, and full-page Visual QA controls integrated into `main`.
9. Visual-review findings must be repaired through a new immutable source revision and re-built/re-reviewed; do not mutate an already reviewed candidate in place.
10. Freeze remains the final Human publication gate. After Freeze, the canonical issue-only flow may merge the normal work PR and publish only after exact frozen source/PDF SHA verification succeeds.

## Production invariants

These expectations apply regardless of which historical month the user selects:

- Source Intake / Screening / Evidence provenance is retained and SHA-bound.
- Candidate Selection and Issue Architecture are explicit Human Gates unless the edition's approved gate plan says otherwise.
- Preview candidates must pass strict TeX/log checks and full-page render self-review before Human Visual Review.
- Reader-facing output must not leak internal machine enums or pipeline vocabulary.
- Technical Notes cards remain breakable, while the current generic tail policy prevents source-only or tiny limitation/source page-top continuations.
- References, TOC, mixed-layout behavior, and other reader-facing formatting must use the current shared implementation on `main`, not edition-specific copied fixes.
- Pre-release review findings are repaired immutably and self-checked again before approval.
- Public Release identity is issue-only: `special/<slug>`.
- Internal source revisions are provenance only and are not public Release versions.

## Progress discovery

Do not maintain a duplicated completed-edition list in this file.

When historical progress matters, derive it from repository state instead:

- edition manifests under `specials/` identify initialized editions;
- `sources/SP-<slug>/pipeline-state.json` identifies the authoritative lifecycle state for an edition;
- a `FROZEN` state plus the corresponding issue-only GitHub Release identifies a completed published edition.

This keeps new sessions correct even if editions are produced out of chronological order or the user intentionally skips to another target month.

## Backfill transition

The long-range cadence is defined only by `docs/special-editions.md`. The user may explicitly choose any valid target period. When the requested period crosses from the monthly tier into a coarser historical tier, consult that policy before constructing the edition manifest rather than relying on a manually maintained `next edition` pointer.
