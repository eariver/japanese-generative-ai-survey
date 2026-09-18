# Human Publication Preview — 2026-W36 r2 (PENDING, no decision recorded)

## Reviewed authority

- Edition: `2026-W36` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `315d72805668ddf6d3f5d22085c0cad82aeee26c` (exact W36-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r2 bytes under review):
  - `sources/2026-W36/publication/v2/publication-candidate-v2.json` (candidate SHA `8103f341bafa3ccc2f52c8b7d25024e7dc9b3843998c221fbcac99b0437e93b1`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W36/main.pdf` (12 pages, 359750 bytes, SHA `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`)
  - `sources/2026-W36/publication/v2/reader-manuscript-v2.json` (manifest SHA `199d450cc6bf266b45e7d8f1f30e954b2bba07842e063f4d156d145affd95292`)
  - `sources/2026-W36/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `702cd3b4ed63d81bb2d6a212310af0adb133e62adf894573c320220bd4f0788a`, 3 deterministic PASS)
  - `sources/2026-W36/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W36/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W36/publication/v2/reader-surface-gate-v2.json` (gate SHA `d0bdb619df1aa619dff7228edaa9f97c385647976170d475d60d5d539687b526`, PASSED with 0 findings and 0 suppressions)
- Blocker-avoidance change from blocked r2 state: `w36community` bibliography URL switched from GitHub blob permalink (`blob/188f5acc.../surveys/weekly/2026-W36/community-observation.md`) to public Issue comment permalink (`https://github.com/eariver/japanese-generative-ai-survey/issues/502#issuecomment-5716020666`); active path suppression file removed; `surveys/weekly/2026-W36/community-observation.md` preserved as audit artifact.
- Architecture approval provenance: r2 `APPROVED` (reviewed `3e1e0fc3b802bf388e56486c638acba35b7bc2ae`, record `gates/reviews/architecture-r2.json`, snapshot `gates/reviews/approvals/architecture-r2.json`)
- Publication Preview r1 remains auditable as `REQUEST_CHANGES` (record `gates/reviews/publication-r1.json`, boundary `DRAFT_COMPLETE`); r1 repairs for #434/#500/#501/#502 preserved.
- Full r2 dossier: `execution/reviews/publication-preview-r2-dossier.md` (required reading)

## Human decision

`PENDING` — no r2 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r2 review performed yet).

## Regeneration boundary

None selected (no r2 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run (`RSG-LEX-INTERNAL-PATHS` unchanged, no suppression plumbing fix, no exception, no validation bypass); `main` and Production Line untouched and unmerged by design.
