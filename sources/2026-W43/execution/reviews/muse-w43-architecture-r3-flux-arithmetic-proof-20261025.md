# Muse Architecture r3 FLUX arithmetic proof (SA-007)

Status: `ARITHMETIC_CORRECTED_R3_READY_FOR_SOL_AUDIT / NO_STAGE_ADVANCE`
Date: 2026-10-25. Pinned start `6c617048bbe8f8cf6e3bfd0707359adc7d957895`. Frozen Core unchanged; r2 Selection/Matrix byte-identical.

## Reviewed authority

- Sol r2 audit `reviews/sol-w43-architecture-r2-arithmetic-independent-review-20261025.md` (Selection PASS_WITH_LIMITATIONS; r2 REQUEST_CHANGES solely SA-007; r1 5/5 SHA MATCH; 68/68 attention; SA-001..006 sufficient with LIMITATIONS).
- Contract `instructions/sol-w43-architecture-r3-flux-arithmetic-20261025.md` (P4 §4.2 fix only; 32/19 invariant; isolated regen; 68/68; no Stage/Human/Draft/PDF).
- r2 snapshot `execution/history/selection-architecture-r2/` (matrix `16a6bbfe…`, selection `50decd86…`, architecture `53f049d0…`, summary `6bc27840…`, attention `7c3e4deb…` 68/68, input `eb169936…`, audit `a1fdd6fd…`).

## Human decision

- NONE. Summary `READY_FOR_ARCHITECTURE_REVIEW` is mechanical only, not Human approval. No ADVANCE, invalidation, revision, Draft, PDF.

## Requested changes (SA-007 closure)

- OLD (r2, INCORRECT HISTORICAL TEXT — must not be copied): `10.95/277.80=25.37x` (false; left side = 0.0394168), `12.45/277.80=22.31x` (false; left side = 0.0448164). Same reversal in r1; r2 repair preserved it — recorded as editorial failure, not new source fact.
- NEW (r3 canonical P4 §4.2 + input-r3): `277.80/10.95≈25.37x`, `277.80/12.45≈22.31x`, `(277.80-12.45)/277.80×100≈95.52%` (denominator = new candidate seconds, numerator = old baseline 277.80s, `t_baseline/t_candidate`). Independent checks: `277.80/10.95=25.3699`, `277.80/12.45=22.3133`, `(277.80-12.45)/277.80×100=95.5184%`. Vendor 26.5x/96.2% remains marked inconsistent with 12.45s/277.80s (attributed marketing, not corrected away, not independently benchmarked). 10.95s stays `PR origin NOT RAW VERIFIED` (no synthesis, no AA/Elo promotion).
- Scope: ONLY P4 §4.2 + dependent `t_baseline/t_candidate` label changed. All 32 assignments, 19 placements, 8 packages/titles/purposes/other must-covers/boundaries/page plan (38/44 est 37.0) UNCHANGED. Other packages' divisions rechecked (P1 20/15, P6 9/20, P7 19/20 are dates/versions, not speedup equations). New r3 reviews/source pages contain zero reversed equations (verified by grep).

## Regeneration boundary

- r2 snapshotted before any write; scratch worktree @`6c617048…` removed proposal outputs only in scratch; frozen runner → Matrix/Selection/Architecture/Summary/default-50 + audit (19/8/READY); Matrix/Selection byte-identical to r2 (SHA `16a6bbfe…` / `50decd86…`); Architecture `53f049d0…→529ce4b3…`, Summary `6bc27840…→26817906…` (P4 text only); Attention rebuilt limit=100 → 68/68 byte-identical `7c3e4deb…` (Selection invariant); audit reconciled (input SHA NEW). Stage scratch precheck `EVIDENCE_REVIEWED→SELECTION_COMPLETE` PASS (impl `6c617048…`, no writes); `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED` NOT run. Exact tested bytes reflected to branch replacing ONLY unadvanced proposal surfaces (matrix/selection copies identical, no-op).

## Shared-Core implication

- No Core edits; issues #568/#569 open. All validations genuine native calls. Core PASS = schema/integrity/placement/basis only. The two arithmetic cases are edition-local semantic negatives (NOT frozen schema rejects — Core schema has no speedup-math rule): reversed strings absent from r3 canonical (verified), correct strings present with numerator/denominator labels. Tampered basis/SHA, missing selected, Metrics/Grok SELECTED, REJECTED/duplicated/invalid placements all fail-closed (transcripts below).
