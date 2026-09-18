# Human Publication Preview — 2026-W37 r4 (PENDING, no decision recorded)

## Reviewed authority

- Edition: `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `07da54bfe3c1bc186abf7016486a4a6768f322c5` (exact W37-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r4 bytes under review):
  - `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `0f7c5af2dd069412b54aced39c43366975548ed50e2358bf3b7264775fb59f04`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W37/main.pdf` (11 pages, 309187 bytes, SHA `09dea4e7fe7eecc6c4dae39a308899849ac84e598f9251b3d415e24b7ee3e268`)
  - `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `8fd688d75309ae54ce23d843903a97e69926df37cfeee1e51be070c12377207c`)
  - `sources/2026-W37/publication/v2/quality-regression-bundle-v2.json` (3 deterministic PASS, Worker/Agent preflight)
  - `sources/2026-W37/publication/v2/semantic-editorial-review-v2.json` (11 PASS, Worker/Agent provenance)
  - `sources/2026-W37/publication/v2/visual-review-v2.json` (2 PASS with all-page #508 inspection, Worker/Agent provenance)
  - `sources/2026-W37/publication/v2/reader-surface-gate-v2.json` (PASSED with 0 findings and 0 suppressions)
- Architecture approval provenance: Human Architecture r1 `APPROVED` preserved (reviewed `55e700a34765654cd2ced0c2a454d4fb3433dd4f`, Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`, record `gates/reviews/architecture-r1.json`, snapshot `gates/reviews/approvals/architecture-r1.json`)
- Prior Preview decisions preserved: r1 `REQUEST_CHANGES` (record `gates/reviews/publication-r1.json`, reviewed `8057a468`, boundary `ARCHITECTURE_ESTABLISHED`); r2 `REQUEST_CHANGES` (record `gates/reviews/publication-r2.json`, reviewed `74400d71`, boundary `ARCHITECTURE_ESTABLISHED`); r3 `REQUEST_CHANGES` (record `gates/reviews/publication-r3.json`, reviewed `8dfb83499`, boundary `DRAFT_COMPLETE`)
- Full r4 dossier: `execution/reviews/publication-preview-r4-dossier.md` (required reading)

## Human decision

`PENDING` — no r4 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r4 review performed yet).

## Regeneration boundary

None selected (no r4 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run (generic Weekly pagination hardening carried forward under Issue #508); `main` and Production Line untouched and unmerged by design.
