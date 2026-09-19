# Human Publication Preview — 2026-W38 r1 (PENDING, no decision recorded)

Generated: `2026-09-19T15:10:14+09:00` (`2026-09-19T06:10:14Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W38` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61` (exact W38-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r1 bytes under review):
  - `sources/2026-W38/publication/v2/publication-candidate-v2.json` (candidate SHA `43c7d33a457d74b04cbba571e006453f8cea27f4dab134e6265bb55f115ce409`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W38/main.pdf` (11 pages, 344241 bytes, SHA `767f4d98c366ae3c7247da635a6ea0b68753f58327104287ab4fb9d8ec9a2543`, CI run `35425249262`, artifact `10577998030`)
  - `sources/2026-W38/publication/v2/reader-manuscript-v2.json` (manifest SHA `a8ce6e54182dca707c753e68b2b61fae35ca3eae19e9cc29cd0e8a9149c8309c`)
  - `sources/2026-W38/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `2b3d786fd02a54a979cb50c9fda552a1dd97265712c3e0eb38f3fb3fc0ec4097`, 3 deterministic PASS)
  - `sources/2026-W38/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W38/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W38/publication/v2/reader-surface-gate-v2.json` (gate SHA `22743e6b25350e21af2f9bd1390439c3a50e0dfb23a43e7071800ee4b19db05c`, PASSED with 0 findings and 0 suppressions)
- Architecture approval provenance: Human review r1 `APPROVED` for r2 content (reviewed `56b6d3d65c5b4105a410e61a22eb083e66fa344c`, reviewed_at `2026-09-19T05:46:14Z`, record `sources/2026-W38/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W38/gates/reviews/approvals/architecture-r1.json`)
- Timestamp authority: pre-Human correction ledger `sources/2026-W38/execution/provenance/w38-execution-time-correction-20260919.md` plus downstream monotonicity note `sources/2026-W38/execution/provenance/w38-downstream-monotonicity-note-20260919.md` (Stage history `recorded_at` values at/after `ARCHITECTURE_ESTABLISHED` are monotonicity-preserving, not actual wall-clock times; lifecycle identities remain authoritative)
- Full r1 dossier: `sources/2026-W38/execution/reviews/publication-preview-r1-dossier.md` (required reading)

## Human decision

`PENDING` — no r1 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r1 review performed yet).

## Regeneration boundary

None selected (no r1 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
