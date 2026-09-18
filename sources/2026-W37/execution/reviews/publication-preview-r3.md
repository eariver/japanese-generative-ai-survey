# Human Publication Preview — 2026-W37 r3 (PENDING, no decision recorded)

## Reviewed authority

- Edition: `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `8dfb83499f839907d180d9a06bd155cc12fb27d6` (exact W37-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r3 bytes under review):
  - `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `e7f18eb2584c2c4575e15bd2be59abc5e8c9a687b238285343139c81332e53f1`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W37/main.pdf` (11 pages, 309033 bytes, SHA `9e957ca2d48dd95091e0013c0f2d23f1570ad9fac89b131365259f1c8e948e56`)
  - `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `bde308b051872808b6db995a8c792f8c4fde9ebacd6fc0e3ab68033f8937d1eb`)
  - `sources/2026-W37/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `7b2b474aa146f6deee818d04d7071d360cecdc86fe48373bed10b9b2ad0a3ef0`, 3 deterministic PASS)
  - `sources/2026-W37/publication/v2/semantic-editorial-review-v2.json` (11 PASS, Worker/Agent provenance)
  - `sources/2026-W37/publication/v2/visual-review-v2.json` (2 PASS, Worker/Agent provenance)
  - `sources/2026-W37/publication/v2/reader-surface-gate-v2.json` (gate SHA `d250d98c8eb23ba860b03a3eb30a98e1194461220af999f624f852cac67eefdf`, PASSED with 0 findings and 0 suppressions)
- Architecture approval provenance: Human Architecture r1 `APPROVED` preserved (reviewed `55e700a34765654cd2ced0c2a454d4fb3433dd4f`, Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`, record `gates/reviews/architecture-r1.json`, snapshot `gates/reviews/approvals/architecture-r1.json`)
- Prior Preview decisions preserved: r1 `REQUEST_CHANGES` (record `gates/reviews/publication-r1.json`, reviewed `8057a468897f67d3a11bd9287f6f56f0485877ce`, boundary `ARCHITECTURE_ESTABLISHED`); r2 `REQUEST_CHANGES` (record `gates/reviews/publication-r2.json`, rev 2, reviewed `74400d716e703c12efee97707ff0ee97d47f98a8`, boundary `ARCHITECTURE_ESTABLISHED`)
- Full r3 dossier: `execution/reviews/publication-preview-r3-dossier.md` (required reading)

## Human decision

`PENDING` — no r3 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r3 review performed yet).

## Regeneration boundary

None selected (no r3 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
