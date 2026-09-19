# W38 downstream timestamp provenance note (monotonicity-preserving Stage history)

Status: `EDITION_LOCAL / APPEND_ONLY_CLARIFICATION / ORIGINAL_BYTES_PRESERVED`

Issue: `2026-W38`

Recorded: `2026-09-19T15:10:54+09:00` (`2026-09-19T06:10:54Z`, actual system wall clock)

Generic tracking: Issue #507 (recurrence remains generic Core work, out of scope for this edition).

## 1. What this note establishes

Three post-approval Stage Checkpoint/history `recorded_at` values in
`sources/2026-W38/production-state.json` are intentionally monotonicity-preserving values,
NOT actual wall-clock event times:

| Transition | `recorded_at` in State/checkpoint | Actual wall-clock window (approx) |
|---|---|---|
| `ARCHITECTURE_ESTABLISHED` → `DRAFT_COMPLETE` | `2026-09-19T06:47:00Z` | circa `2026-09-19T05:53–05:54Z` |
| `DRAFT_COMPLETE` → `VALIDATED_DRAFT` | `2026-09-19T06:48:00Z` | circa `2026-09-19T06:06–06:07Z` |
| `VALIDATED_DRAFT` → `RELEASE_CANDIDATE` | `2026-09-19T06:49:00Z` | circa `2026-09-19T06:08–06:09Z` |

## 2. Why

Production State history inherited invalid future-dated values (`05:47Z`–`06:46Z`) documented in
`execution/provenance/w38-execution-time-correction-20260919.md`. Current Core enforces non-decreasing
history timestamps, so advancing with actual wall-clock times is refused. Each value above is the minimal
`+1 minute` step preserving monotonicity over the inherited invalid history.

## 3. Disposition

`MONOTONICITY_PRESERVING / INVALID_AS_ACTUAL_WALL_CLOCK_TIME`

Lifecycle transition identities, checkpoint bindings, artifact authorities and substantive review findings
are unaffected and remain authoritative. Do not quote the three values above as actual event times.
All review/dossier/provenance records created in this run otherwise carry actual wall-clock times.

## 4. Shared-Core implication

None. No shared-Core modification; generic defect stays tracked by Issue #507.
