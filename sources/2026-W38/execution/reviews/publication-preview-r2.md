# Human Publication Preview — 2026-W38 r2 (PENDING, no decision recorded)

Generated: `2026-09-19T17:44:27+09:00` (`2026-09-19T08:44:27Z`, actual system wall clock at generation; not copied from Production State, not a rounded stage time).

## Reviewed authority

- Edition: `2026-W38` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`
- Reviewed repository commit SHA: `a55ac5b929221bd133d8a4b819bf960d2104d6c7` (exact W38-branch commit containing State + Candidate + Candidate-bound PDF)
- Lifecycle: `RELEASE_CANDIDATE`; next action `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Gate inputs (exact r2 bytes under review):
  - `sources/2026-W38/publication/v2/publication-candidate-v2.json` (candidate SHA `8aeb4dc4f959096708186ee338e11f518dd5a2f8c31f7a7757ec9f0278bcbe3f`, READY_FOR_PUBLICATION_PREVIEW)
  - `surveys/weekly/2026-W38/main.pdf` (11 pages, 347330 bytes, SHA `3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`, CI run `35432581167`, artifact `10581840234`)
  - `sources/2026-W38/publication/v2/reader-manuscript-v2.json` (manifest SHA `6efcacaa37166f717033da92aae879cad8735278081291235530336e016a008c`)
  - `sources/2026-W38/publication/v2/quality-regression-bundle-v2.json` (bundle SHA `9e4137348a4cf336a673683d98b0beb571277cd9d0d4a3ba831848b5b224208d`, 3 deterministic PASS)
  - `sources/2026-W38/publication/v2/semantic-editorial-review-v2.json` (11 PASS)
  - `sources/2026-W38/publication/v2/visual-review-v2.json` (2 PASS)
  - `sources/2026-W38/publication/v2/reader-surface-gate-v2.json` (gate SHA `c45b0d44a7b17ef76b31c129f0371767e1736efeb776ec87cd5f6ddb63d0e2da`, PASSED with 0 findings and 0 suppressions)
- Regeneration basis: Human Preview r1 `REQUEST_CHANGES` (revision 1, reviewed `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61`, boundary `ARCHITECTURE_ESTABLISHED`, record `gates/reviews/publication-r1.json`) for Issues #511/#512; Architecture approval retained (Human review r1 `APPROVED` for r2 content, reviewed `56b6d3d65c5b4105a410e61a22eb083e66fa344c`)
- #511 correction authority: `sources/2026-W38/collectors/primary/corrections/typesafe-jev-temporal-correction-20260919.md` + `sources/2026-W38/evidence/v2/corrections/typesafe-jev-temporal-correction-r1.json` (blog Sep 14 day-precision; founder Sep 15 announcement bound separately)
- #512 public ledger: `surveys/weekly/2026-W38/community-observation-ledger.md` (25/23/2) mirrored at `https://github.com/eariver/japanese-generative-ai-survey/issues/512#issuecomment-5740537184` and cited in bibliography
- Full r2 dossier: `sources/2026-W38/execution/reviews/publication-preview-r2-dossier.md` (required reading)

## Human decision

`PENDING` — no r2 decision has been recorded. The only valid decisions are `APPROVED` or `REQUEST_CHANGES`. This run does not generate a Human decision.

## Requested changes

None (no r2 review performed yet; r1 requested changes were Issues #511/#512, repaired in this regeneration).

## Regeneration boundary

None selected (no r2 review performed yet). Allowed publication-local boundaries on REQUEST_CHANGES: `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`. Upstream boundary before `ARCHITECTURE_ESTABLISHED` triggers cross-gate Architecture reopen per Core contract.

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
