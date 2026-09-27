# Survey Production session — ts002-architecture-provenance-sanitation-r2-20260925

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`
Branch: `special/beyond-text-2026-work` (existing only; no new/fallback/repair/review branches)
Execution authority: `docs/prompts/2026-09-25_muse-ts-002-architecture-provenance-sanitation-r2.md`
Sol authority: `execution/sol-architecture-review-r1-20260925.md`
  (`REQUEST_CHANGES / ACTIVE_PROVENANCE_SANITATION_REQUIRED`; architecture design itself PASS)

## Start guards (read-only, all PASS before any write)

- Remote work HEAD `38e32e910329db088151ab4f1d1680c34e226591` == Exact Starting SHA.
- Remote work tree `f8e1581c7fe892591bdeff86ce6d2c7367a09eb7` == Expected Starting Tree.
- Remote main HEAD `0bbb02b3c5963403860897daec2feaf61e82589a` == Reviewed main SHA.
- Remote main tree `e4ddde5ed5059d303b818f54e27204369b256bcb` == Expected main Tree.

## Stale-language count before sanitation (active artifacts only)

- Rebound Evidence results `29804dcf…`: 21 files with the literal
  `Future Discovery repair should correct the locator.`
- `candidate-matrix-v2.json`: 21 `remaining_boundaries` (derived from card limitations).
- `architecture-v2.json`: 21 package/inherited boundaries (Sol observed 11; full count 21).
- Transition ledger: 12 unresolved entries in present-tense defect wording (no literal
  future instruction, but past-tense normalization required by A1).
- Historical surfaces (r1/r2/rebound result-sets, prior inputs, repair manifest, Sol
  reviews, session reports, builder scripts) intentionally excluded and preserved.

## Evidence cards changed by ID (22)

BT-D004, D015, D033, D034, D039, D042, D043, D044, D048, D049, D053, D059, D068,
D069, D073, D074, D081, D084, D095, D096, D097 (limitation + verification + caveat
past-tense rewrite) + BT-D089 (locator-does-not-resolve → past tense).
D024/D062 wordings already completed-tense; statuses untouched (D062 VERIFIED kept).

## Provenance wording policy (applied mechanically, audited)

- `Recorded locator X is a transcription defect … Future Discovery repair should
  correct the locator.` → `Prior recorded locator X was a transcription defect;
  canonical Discovery provenance was rebound to Y during the 2026-09-24 provenance
  repair (see provenance-repair-manifest.json). Claims above rest on the
  verified-correct body.`
- Verification `resolves to unrelated` → `resolved … before the 2026-09-24 repair`.
- Caveats → past-tense rebound statements. Genuine access barriers kept verbatim.
- No claim, metric, status, materiality, or lineage-neutral field altered
  (byte-diff proof: only limitations/verification/caveat differ; 22 records).

## Hashes

- Old active Evidence: `29804dcf…` (result-set SHA, preserved untouched).
- New active Evidence: `f8e273fd…` (result-set SHA `1fb07f81…`).
- New Views: `ccf08af2…`. Ledger `e28cfbad…`. Completeness `e518b19b…`.
- Matrix resealed (boundaries clean). Selection `a249b307…` (counts identical).
- Architecture `b496de50…` (design identical; boundaries clean).
- Review summary re-derived (READY), attention re-derived.
- Dossier: `execution/architecture-review-dossier-r2.md` (fresh; r1 preserved).

## Invariant count checks (all hold)

Discovery 139; Screening 134/3/2/0; Evidence 126/8/5; Materiality 109/25/5;
Completeness LIMITED 4/8; Selection 134/5; ledger 43 (41 multi-task);
Architecture 14 packages; page plan 80/96; gate pending.

## Remaining PARTIAL / NEEDS_MORE

PARTIAL (8): BT-D022, D059, D076, D083, D089, D098, D106, D134.
NEEDS_MORE/HOLD (5): BT-D024, D072, D091, D120, D125.
No promotion beyond D062 (actual v2 body).

## Validator receipt

`execution/sanitation-r2-20260925/validation-sanitation-r2.json`: 19/19 PASS
(scope note: historical reports/manifests excluded from the literal-phrase scan).

## Final HEAD / tree

Local HEAD at commit: this commit (parent `38e32e91…`, direct fast-forward).
Final remote HEAD/tree after push: equal to this commit (verified post-push).

## Draft and later stages

NOT entered. No manuscript prose; internal artifacts are not publication prose.

## Operational meaning

`ARCHITECTURE_REVIEW / AWAITING_HUMAN_ARCHITECTURE_DECISION_R2`

Session status: `COMPLETE`
