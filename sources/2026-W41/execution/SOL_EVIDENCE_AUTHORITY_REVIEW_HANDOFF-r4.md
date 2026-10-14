# W41 Sol Evidence Binding Review handoff r4 (pre-acceptance)

Status: `SOL_EVIDENCE_BINDING_REVIEW_READY` (REVIEW_PENDING — no acceptance, no Sol PASS forged)
Date: 2026-10-12 JST
Branch: `weekly/2026-W41-v2-work` (existing only; no new branch, no force, no rewrite)
Starting HEAD `62c0efc825eeca30d690daf3ada62a430822a9fa` / Tree `6d9ffb83d816fb7f71062c450035defd522484a0` (verified read-only; instruction parent a43a497c; r3 fa7f7a5b in ancestry)
Reviewed main `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8` / Tree `31c0adc5b57761e5073d100554279a8adc5a18f4`; Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` (shared roots untouched)
Sol authority: `execution/reviews/sol-w41-evidence-authority-consumption-r1-20261012.md` (PARTIAL_PASS, SC-E41-01..04)
Ending HEAD `399a37c9d114176d0e5dbcaac9402f20f613e11e` / Tree `5c941e2efb41baa82bf2f81d4c5b47620cf3a841` (r4 commit, pushed; `origin/weekly/2026-W41-v2-work` == HEAD).

## 1. Compatibility projection (SC-E41-01) — PROVEN under unmodified Core

- 9 r1 failures reproduced exactly (`unsupported source_type ... SECONDARY_OBSERVATION`).
- Ledger `execution/compat/evidence-source-class-projection-r4/projection-ledger.json`: map SECONDARY_OBSERVATION→SECONDARY for exactly the 9 (agr, nemotron, drex, ndi, elevenlabs, tencent, pixelcanary, tbcvideo, elyza); 27 passthrough byte-identical; old/new SHA per row; unknown-type rejection; DOUBLE_BUILD_IDENTICAL_PASS; negative BOGUS injection FAIL_CLOSED_PASS.
- Compat task_authority_sources 36/36 PASS with zero Core modification/override. Builders checked in (`build_projection_r4.py`, `build_r2_package.py`) for reproducibility.
- Discovery/Screening canonicals unchanged (37/37 checkpoints intact). Core repair still deferred/separate; projection approval remains Sol's decision.

## 2. Authority supplement (SC-E41-02) — 8 entries, Core-validated

- Manifest `external/evidence-supplement/evidence-authority-supplement-r4.json` (build+validate PASS): 7 raw excerpt files with SHA/bytes.
- Bindings: nanobanana→DeepMind card; synthid→Google blog; drex→nace.ai docs; mistral→docs pin (52B); egemma→launch blog (Apache-2.0/HF); textgrain→blog full body (direct read); decisions+ultrafast→changelog excerpts (direct reads).
- accessed_at are bundle-level r3 retrieval-window instants (per-page minute unproven — disclosed); published_at null where only day-granularity known (day in relation).

## 3. Rebuilt 36 cards/views (SC-E41-03/04) — Core-validated, NOT accepted

- Derived package `evidence/v2/packages/r2` (36 tasks; basis+double-build PASS; authority 36/36 PASS unmodified).
- Cards `evidence/v2/results/r2/` 36/36 (`validate_evidence_card` PASS): 3 VERIFIED / 21 PARTIAL / 12 NEEDS_MORE; 21 MATERIAL / 13 HOLD / 2 CONTEXT.
- Fixes: primary claims cite PRIMARY_OFFICIAL supplements (lineage src-1 retained, never sole); clef weight-repo-status→UNRESOLVED; decisions VERIFIED scoped to changelog; Drex Sep24/28 pre-window origins explicit; day-only/month-only HOLDs kept; W40 HOLDs kept; no forced VERIFIED.
- Views `evidence/v2/views/r2/` 36/36 validated (provisional binding; NOT acceptance outputs).
- Source-coverage: DIRECT (textgrain blog, changelog ×2 bodies) / DELEGATED (bundle verbatims) / LOCATOR_ONLY or FAILED (PDF, JS-gated, timeouts, missing WG/1.0 docs) per card contexts.
- r1 assets untouched. No accept_evidence_results, no views acceptance, no ledger, no EVIDENCE_REVIEWED, no Selection/Architecture/Human Gate.

## 4. State / blockers

- State `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; discovery+screening passed; evidence/materiality/completeness pending; gates pending.
- Blockers for Sol: (a) projection semantics approval; (b) NEEDS_MORE gap-fill vs HOLD; (c) unread bodies (PDF/card/portal/WG/1.0); (d) delegated re-verification; (e) vendor-only benchmarks; (f) clean rerun after Core repair before any acceptance.
- Changed paths: execution/compat/…r4 (4 files), external/evidence-supplement/r4 (7) + manifest, evidence/v2/packages/r2 (37), results/r2 (37), views/r2 (36), execution session/handoff/index, validation report. Nothing outside sources/2026-W41.
