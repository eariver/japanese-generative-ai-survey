# W34 Issue #491 — shared-Core bibliography urldate note (no Core edit in this task)

Date: 2026-09-13 JST
Status: `EDITION_LOCAL_REPAIR_DONE / CORE_MAINTENANCE_SEPARATE`

## Observation

Active W34 Evidence is correct (`sources[].accessed_at = 2026-09-08…` for all 41 cited discoveries; `temporal.observed_at = 2026-09-08T15:34:01Z`; `official-provenance.jsonl` CAPTURED `2026-09-08…`).
Rendered `references.bib` before r2 was blanket `urldate = 2026-08-21` for all 41.

## Deterministic shared path

- `scripts/survey_weekly_semantic_publication_v2.py:85-101` `_window()` derives `urldate = window_end[:10]` from `production-profile temporal_policy.window_end/cutoff (2026-08-21T18:00:00-04:00)`.
- `:62-76` `_bib_text()` writes that single `urldate` for every entry.
- `:474-479` `main()` generates all bib entries with that value, ignoring per-source `accessed_at`.
- Same blanket pattern in `scripts/run_semantic_publication_v2_interactive_base.py:158-159` (`as_of[:10]`) for Specials.

## Why W34 not blocked

`surveys/weekly/2026-W34/references.bib` is a W34-owned DRAFT_COMPLETE supporting file (pinned in `reader-manuscript-v2.json`, validated at `DRAFT_COMPLETE→VALIDATED_DRAFT`). Correcting its 41 `urldate` values to `2026-09-08` to match stored Evidence is canonical edition-local repair (same layer as r1 TeX normalization), not an ad hoc PDF patch. No Shared Core file changed here.

## Recommended bounded Core maintenance (separate task/branch)

- Carry `accessed_at` through `_records_from_authorities()`; derive per-entry `urldate` from Evidence (policy for multi-source entries + unknown-date representation).
- Add regression: fixture with `window_end != accessed_at` must not yield blanket cutoff `urldate`.
- Revalidate impact across Weekly/Special; do not change W34 audit wording as part of Core fix.

Markers: `W34_ISSUE491_BIB_CORE_NOTE_RECORDED / NO_SHARED_CORE_EDIT`.
