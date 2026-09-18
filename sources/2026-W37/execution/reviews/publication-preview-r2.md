# Human Publication Preview — 2026-W37 r2 (PENDING, no decision recorded)

## Reviewed authority

- Edition: `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `74400d716e703c12efee97707ff0ee97d47f98a8` (exact W37-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r2 bytes under review):
  - `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `8f74d379ccf7df181b8fbe0890d4774573f6c273c046ec44f15a80a184b3ab6b`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W37/main.pdf` (11 pages, 309850 bytes, SHA `c2298653e959388f359c5dadf0121e28684950343e874c2305179b4c0aa5f4fe`)
  - `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `0113bab9947a1c2e4f3e2ebb6d782172147af53eff6b98e18c371322f44c5f36`)
  - `sources/2026-W37/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `1219cf6a9168df97ff478bd334f483408ede4fda9270d7cc2ff875c6ba773737`, 3 deterministic PASS)
  - `sources/2026-W37/publication/v2/semantic-editorial-review-v2.json` (11 PASS, Worker/Agent provenance)
  - `sources/2026-W37/publication/v2/visual-review-v2.json` (2 PASS, Worker/Agent provenance)
  - `sources/2026-W37/publication/v2/reader-surface-gate-v2.json` (gate SHA `89d5397f4c2fa49f5e1c6a97809857c17cafbe5b4f0767b8c6bc450155ff3f5a`, PASSED with 0 findings and 0 suppressions)
- Architecture approval provenance: Human Architecture r1 `APPROVED` preserved (reviewed `55e700a34765654cd2ced0c2a454d4fb3433dd4f`, Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`, record `gates/reviews/architecture-r1.json`, snapshot `gates/reviews/approvals/architecture-r1.json`)
- Human Preview r1 `REQUEST_CHANGES` preserved historically (record `gates/reviews/publication-r1.json`, rev 1, boundary `ARCHITECTURE_ESTABLISHED`, reviewed `8057a468897f67d3a11bd9287f6f56f0485877ce`)
- Full r2 dossier: `execution/reviews/publication-preview-r2-dossier.md` (required reading)

## Human decision

`PENDING` — no r2 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r2 review performed yet).

## Regeneration boundary

None selected (no r2 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
