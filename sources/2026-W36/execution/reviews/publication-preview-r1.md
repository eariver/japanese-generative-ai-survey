# Human Publication Preview — 2026-W36 r1 (PENDING, no decision recorded)

## Reviewed authority

- Edition: `2026-W36` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `c4ab045548ebf279209862bf62bd6f9725082fb8` (exact W36-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r1 bytes under review):
  - `sources/2026-W36/publication/v2/publication-candidate-v2.json` (candidate SHA `0c4ea873…`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W36/main.pdf` (12 pages, 360121 bytes, SHA `b5893f48…`)
  - `sources/2026-W36/publication/v2/reader-manuscript-v2.json`
  - `sources/2026-W36/publication/v2/quality-regression-bundle-v2.json` (3 deterministic PASS)
  - `sources/2026-W36/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W36/publication/v2/visual-review-v2.json` (2 PASS)
- Architecture approval provenance: r2 `APPROVED` (reviewed `3e1e0fc3`, record `gates/reviews/architecture-r2.json`, snapshot `gates/reviews/approvals/architecture-r2.json`)
- Full r1 dossier: `execution/reviews/publication-preview-r1-dossier.md` (required reading)

## Human decision

`PENDING` — no r1 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`.

## Requested changes

None (no r1 review performed yet).

## Regeneration boundary

None selected (no r1 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core defect repaired in this run; `main` and Production Line untouched and unmerged by design.
