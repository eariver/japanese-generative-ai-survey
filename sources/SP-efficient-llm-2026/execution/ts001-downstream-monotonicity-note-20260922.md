# TS-001 reissue downstream monotonicity note

Date: `2026-09-22`
Author role: Muse (Luna/Work execution role).

Inherited Production State history carries `recorded_at` values ahead of the
executing system wall clock (last history entry `2026-09-22T18:00:00Z` vs
system clock `~2026-09-22T17:04:00Z`). This is pre-existing State provenance,
not edition work. Stage advances therefore use explicit monotonicity-preserving
`--recorded_at` values strictly after the last history entry:

- `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE`: `2026-09-22T18:30:00Z`
- later advances: strictly increasing from there.

No shared-Core change. Deterministic CORE_STAGE_CONTRACT reports retain actual
wall-clock `recorded_at`; only the Stage Checkpoint / history entries carry the
monotonicity-preserving timestamps.
