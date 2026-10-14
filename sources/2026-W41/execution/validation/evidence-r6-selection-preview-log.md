# W41 r6 validation log (frozen Core, exit statuses + SHA identities)

Date: 2026-10-12 JST. No Core/shared-root modification. No Evidence Card rewrite.
Implementation context HEAD at Core execution: `a8fe41a19ac18a981fe2f4d27272ae7a5cf89311`.

## SC-M41-01 (one View correction, 35 byte-identical)

- r6 input `evidence/v2/views/r6/` (36 files) copied from accepted `e0a6c921…`:
  35 byte-identical PASS, exactly one changed
  (`view-3d8a1c751c0ff84fd96f.json`: `bece65e1…` → `3b4bc871…`) PASS.
  Negative gate (any other changed file/field aborts): PASS.
- Field gate: task ID + evidence SHA
  (`7654b400ddcec68a785481a1b33e96bad12069a666462fe8de4620a3da3cd18a`)
  preserved; `MATERIAL→CONTEXT`, `MAIN_EVENT→OTHER`, rationale replaced per
  contract; all other keys/scopes identical: PASS.
- `validate_edition_view` 36/36 with frozen Core: PASS.
- `accept_edition_views` (same Evidence Acceptance 36, agent-tool
  historical-basis override for package state SHA only) →
  `evidence/v2/views/accepted/cd661097ccfb2c4e3960a334d2aab39b629fc656436593186011fe416f0a04b2/edition-views-accepted.json`
  (36 views: 20 MATERIAL / 13 HOLD / 3 CONTEXT): PASS.
- `validate_edition_views_acceptance` (same override): PASS.
  Evidence accepted SHA unchanged (`717ea04a…` set; acceptance file
  `66053742…`); profile SHA `f22a1291…` unchanged.

## SC-M41-02 (exclusion overlay + grep baseline)

- Overlay `execution/nanobanana-legacy-negative-exclusion-r6.md`
  (`LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE`, task `e9e13879f1c0fcf8`,
  4 verbatim legacy locations, admissible replacement, grep patterns, audit
  procedure, 8-supplement caveats preserved): created.
- Baseline: new accepted views + r6 input NO_HITS (forbidden); accepted Card
  historical hits retained (immutable, excluded from reader surfaces).
- Corrected finding: `derive_candidate_matrix` verbatim copies Card
  limitations into Matrix `remaining_boundaries` (internal audit, 1 faithful
  hit at matrix:1168); Selection assignments NO_HITS (admissible only).
  `NO_READER_SURFACE_BLOCK` recorded in overlay §5; no STOP, no Card rewrite.

## SC-M41-03/04 (Materiality / Completeness)

- `build_materiality_ledger` (frozen, override) →
  `execution/materiality-ledger-r6.PROPOSED.json` SHA
  `51890f067daf8d5f850a3166204d0a7bc6e4073ab11d1842f241155aee9f2997`
  (37 rows: 20 MATERIAL / 13 HOLD / 3 CONTEXT / 1 EXCLUDED; 36 bindings;
  Grok `w41-grok-x-ledger-20261011` now CONTEXT): PASS.
- Canonical promotion (byte-identical): `sources/2026-W41/materiality-ledger-v2.json`
  SHA `51890f06…`: PASS.
- Completeness r6 `execution/profile-completeness-r6.PROPOSED.json` SHA
  `f3d5a122534b74409bce69f3eaec03f51e23e299e610721ac0b80e6d3d4508d8`
  (overall LIMITED; SATISFIED/LIMITATION/SATISFIED; 10 residuals): schema PASS;
  `validate_profile_completeness` bare run reports only known historical
  screening state-basis drift; override PASS (narrowly documented, no source/
  SHA/acceptance/completeness check disabled).
- Canonical promotion: `sources/2026-W41/profile-completeness-v2.json` SHA
  `f3d5a122…`: PASS.
- Dossier `execution/materiality-editorial-dossier-r6.md` (20-candidate depth,
  6 themes, thin/comparator calls, counterfactual HOLDs, intake truthfulness):
  created (non-schema editorial, Sol-facing).

## Stage (CANDIDATES_NORMALIZED → EVIDENCE_REVIEWED)

- `survey_stage_validation_v2.validate_stage` →
  `execution/validation/evidence-stage-validation-r6.json` (from
  CANDIDATES_NORMALIZED to EVIDENCE_REVIEWED, PASS; artifacts
  evidence `66053742…` / views `371a565e…` / ledger `51890f06…` /
  completeness `f3d5a122…`): PASS.
- `agent.build_stage_checkpoint` →
  `orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json`
  (checkpoints evidence/materiality/completeness, impl `a8fe41a1…`): PASS.
- `agent.advance_with_checkpoint` → lifecycle EVIDENCE_REVIEWED
  (evidence/materiality/completeness passed; discovery/screening remain passed;
  selection+downstream pending; both Human Gates pending): PASS.

## Selection preview (PROPOSED_NOT_ACCEPTED)

- `derive_candidate_matrix` → `execution/candidate-matrix-r6.PROPOSED.json`
  SHA `0d56de2b8b1b0417ce7f0cac34283a4549e6e91ca5279016aa826416e9f98d25`
  (36: 20/13/3; VERIFIED 3 / PARTIAL 21 / NEEDS_MORE 12):
  `validate_candidate_matrix` PASS.
- Selection preview `execution/candidate-selection-r6.PROPOSED.json` SHA
  `3bedcb4acbb80647539ef3a318fd6ce654e31a540d9a6e76e55d2361ab729033`
  (20 SELECTED / 13 HOLD / 2 INSPECT / 1 REJECT): `validate_selection` PASS.
- Narrative `execution/selection-preview-r6.md` (lead, 6-theme grouping,
  citations, alternatives, HOLD/CONTEXT disposition, honest depth, no TeX):
  created. No `candidate-matrix-v2.json` / `candidate-selection-v2.json`
  canonicals; no SELECTION_COMPLETE; no Architecture/Draft/PDF/Human Gate.

## Stop

Terminal: `SOL_SELECTION_MATERIALITY_PREVIEW_REVIEW_READY`.
All required Core validations PASS; no new substantive Evidence contradiction;
no forbidden advance. Sol independent Selection review is the next required step.

(End of file)
