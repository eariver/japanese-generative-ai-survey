# Human Publication Preview — 2026-W37 r1 (PENDING, no decision recorded)

## Reviewed authority

- Edition: `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `8057a468897f67d3a11bd9287f6f56f0485877ce` (exact W37-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r1 bytes under review):
  - `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `1dfb87957cbab69e30c08a45c66e72b28c72d74d1272a3c3815ab6844445bef6`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W37/main.pdf` (10 pages, 301238 bytes, SHA `08ceb5e9c90b2bf25541bb61e6b14e5b2cdc7fe48635d85c5ab798606b88fd4d`)
  - `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `a4c6990287fd9bfb284b7354b460fe7708d007dfed36a46a69a6e90171aacdb8`)
  - `sources/2026-W37/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `004446ea53df70dd0a2db409b4d7a5d4892a70f3291be10892de6f9be99f73dc`, 3 deterministic PASS)
  - `sources/2026-W37/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W37/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W37/publication/v2/reader-surface-gate-v2.json` (gate SHA `dae3dc38ca0c7f753db1e8fb86b51f685921ab4f9aa7a79e0308568673909d62`, PASSED with 0 findings and 0 suppressions)
- Architecture approval provenance: Human review r1 `APPROVED` for r2 content (reviewed `55e700a34765654cd2ced0c2a454d4fb3433dd4f`, record `gates/reviews/architecture-r1.json`, snapshot `gates/reviews/approvals/architecture-r1.json`)
- Full r1 dossier: `execution/reviews/publication-preview-r1-dossier.md` (required reading)

## Human decision

`PENDING` — no r1 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r1 review performed yet).

## Regeneration boundary

None selected (no r1 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
