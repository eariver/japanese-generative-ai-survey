# Muse Architecture r2 depth/basis reconciliation (SA-001..006)

Status: `SUBSTANTIVE_R2_READY_FOR_SOL_AUDIT / NO_STAGE_ADVANCE`
Date: 2026-10-25. Basis: EVIDENCE_REVIEWED, Gates pending. Frozen Core unchanged; r1/r2 proposals unadvanced (no Stage authority).

## Reviewed authority

- Sol r1 audit `reviews/sol-w43-selection-r1-architecture-editorial-review-20261025.md` (Selection PASS_WITH_LIMITATIONS; Architecture REQUEST_CHANGES SA-001..006).
- Contract `instructions/sol-w43-architecture-r2-depth-and-terminology-repair-20261025.md` (retain 19, deepen narrative, 68/68 attention, isolated regen).
- r1 snapshot `execution/history/selection-architecture-r1/` (matrix `16a6bbfe…`, selection `50decd86…`, architecture `89391d1b…`, summary `7bf44371…`, attention `1dc4ebe8…` (50/68 truncated), input `20394528…`, audit `73e600b5…`).

## Human decision

- NONE. Summary `READY_FOR_ARCHITECTURE_REVIEW` is mechanical readiness only, not Human approval. No ADVANCE, invalidation, revision, Draft, PDF.

## Requested changes (SA-001..006 closure)

- **SA-001 P1 factual headline**: thesis/P1 title no longer presuppose landed Kimi weights. P1 title `公開予定の重みと、すでに動かせるモデル:Kimi の API 先行と Flint/Nemotron の重み・ライセンス`; thesis `公開予定の重み(Kimi は API 先行・重み Nov4 FUTURE)と、すでに動かせるモデル…`; `オープンウェイト` vs `オープンソース` distinguished (OpenMDW ≠ OSI). P1 boundaries carry Nov4 FUTURE + no weight-bytes claim.
- **SA-002 P1 budget math**: single verified table — allocations P1 5.0+P2 6.0+P3 4.5+P4 3.0+P5 4.5+P6 4.0+P7 4.5+P8 3.5=35.0 + front matter/references/index 2.0 = 37.0; target 38 / max 44 (estimates, not PDF guarantee). Old 30/34 + r1 note mismatch (P1 4.0/P2 5.0 vs actual 5.0/4.0) superseded; arithmetic exact.
- **SA-003 P1 depth**: all 8 packages carry numbered subsections (§1.1–§8.3), named tables/figures with inputs/axes + evidence links, per-topic mechanisms/steps, denominators/workloads/harnesses/hardware, baselines/contradictions, deployment/weights/license/status, uncertainties; DEPTH_LIMITED + downscope rule where primary body absent (no invented equations, no padding). Priority P2 (6.0pp, environ @9bd9cf24 + MoS/34B/1.86x/66x + license split), P5 (4.5pp, FLEURS/cpWER/recall + Voice Code Bench + AA cited/unfetched + protocol), P7 (4.5pp, 700+ vs 11/blinded 75%/wet-lab + MultiLangBench/COBOL parity/suite), P8 (3.5pp, 400Q/codSuite/Harness/registry), P3/P6 retained with permission/5-stage depth; P4 kept as critical-methods single (10.95 traceable via PR note, contradiction explicit).
- **SA-004 P2 terminology**: `Corde: Kimi` removed; `手元で動く符号化` → `手元で動く符号生成モデル`; `辺境訓練の囲い` → `先端モデルの学習環境の隔離`; `安全積上げ` → `安全対策の積層`; `権限境界`/`脆弱性の協調開示`/`ローカル推論` used; English IDs preserved; no invented taxonomies.
- **SA-005 P2 full attention**: frozen `build_attention(limit=100)` in scratch → 68/68 (`limit 100, shown 68, overflow 0, truncated false`, SHA `7c3e4deb…`), `validate_attention` PASS; runner default-50 replaced only in scratch, audit SHA reconciled (edition-local metadata). Reviewer cover: 19 DROP screening+materiality dedup noted; ALL Human-critical items (P1 cutoff, licenses, zero repros, ambiguity, HOLD, 5 LIMITED) kept in summary/attention, no truncation reliance.
- **SA-006 P2 citation/limits**: per-claim Source ID→URL→passage/bytes/measurement-class in crosswalk + package must_cover/boundaries; Kimi X/blog split, Flint article/HF, DeepInfer 9bd9cf24, MemT PDF/README, Patch rendered-only GPT-5.6, FLUX 10.95/12.45/277.80/26.5, Securing RSS vs page, TanStack product vs blog, Ming/Eleven AA unfetched, Duet/1Password coming-soon; per-package MUST-NOT lists; zero independent repro + 5 LIMITED retained; no Evidence r4 edits.

## Regeneration boundary

- r1 artifacts snapshotted before any write; scratch detached worktree @`fe6809f5…` removed proposal outputs only in scratch; frozen runner regenerated 32/32/8/READY + default-50; attention rebuilt limit=100; audit reconciled; stage scratch PASS; negatives fail-closed. Exact tested bytes reflected to branch replacing ONLY unadvanced proposal surfaces (matrix/selection byte-identical by invariance; architecture/summary/attention/input/audit updated). Evidence r4/Views/ledger/completeness, Discovery/Screening, raw, State/Checkpoints, Core/main/Gates untouched.

## Shared-Core implication

- No Core edits; issues #568/#569 open. All validations genuine native calls. Core PASS = schema/integrity/placement/basis only; headline/clock/license/bench truth is editorial proof above + crosswalk. Unacknowledged MAIN_EVENT or SELECTED Metrics/Grok would still fail the exact validators used (NON_MATERIAL SELECTED, non-selected placement) — plus decisive semantic supersession.

## r1 vs r2 SHA manifest (canonical files)

- candidate-matrix-v2.json: r1 `16a6bbfe…` → r2 `16a6bbfe…` (IDENTICAL — 32 candidates/roles invariant)
- candidate-selection-v2.json: r1 `50decd86…` → r2 `50decd86…` (IDENTICAL — 19/1/12 + roles invariant)
- architecture-v2.json: r1 `89391d1b…` → r2 NEW (8 packages, fixed titles/purposes/must-cover/boundaries/page plan 38/44)
- architecture-review-summary-v2.json: r1 `7bf44371…` → r2 NEW (READY, 0 errors; still mechanical, not Human)
- architecture-review-attention-v2.json: r1 `1dc4ebe8…` (50/68 truncated) → r2 NEW 68/68 (`7c3e4deb…`, limit 100, untruncated)
- orchestration input: r1 `20394528…` → r2 NEW (same 32 assignments, new architecture; SHA in audit)
- orchestration audit: r1 `73e600b5…` → r2 NEW (reconciled attention SHA)
- Evidence r4/Views/ledger/completeness/Discovery/Screening/raw/State/Checkpoints: UNCHANGED (verified `git status` clean except listed proposal surfaces + history + reports).

## All 32 decisions + 19 placements (Selection invariant)

- SELECTED 19 (all MATERIAL, each placed once): Duet P + 1Password/Automode S (P3); Kimi P + Flint P + Nemotron S (P1); DeepInfer P + MemT P (P2); FLUX P (P4); Voxtral P + Ming/Eleven S (P5); Patch P + Securing P (P6); Bio P + Lowresource P (P7); Decisions P + TanStack/DeepSeek S (P8).
- HOLD 1: moss-trainer (gate: independent GPU/VRAM + release scope).
- REJECT 12: Metrics (POST_CUTOFF OUT) + Grok (NEVER) + 10 CONTEXT (carry, muse-10m, oracle, deprecation, Teams-IN-but-thin, cloud-preview, ambench, moss-api/report, vercel-composite).
- 19 DROP outside Matrix; 12 carries 11 EXCLUDED + 1 CONTEXT-REJECT. No unplaced SELECTED, no selected NON_MATERIAL, no REJECTED/HOLD placement.

## Validators, negatives, stage (transcripts summarized)

- Frozen: matrix/selection/architecture(require_approved=False)/summary-equality/attention validate PASS; input schema PASS; stage `EVIDENCE_REVIEWED→SELECTION_COMPLETE` scratch PASS (impl `fe6809f5…`, no writes); `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED` NOT run (static only).
- Negatives (scratch + canonical logic): Metrics/Grok SELECTED, omitted, role-less, REJECTED placement, duplicated, invalid package, tampered basis — all FAIL_CLOSED. Metrics POST_CUTOFF/NON_MATERIAL + View supersession present (Core-alone MAIN_EVENT would pass schema — documented gap, editorial proof required).
- Runner transcripts: scratch `tmp-r2-run2.sh` exit 0 (19/8/READY), attention `tmp-attn100.sh` exit 0 (68/68), precheck exit 0, negatives exit 0. Isolated worktree removed after reflection (transcripts preserved in session).

## Blockers / remaining 5 LIMITED

- No new P1; 5 LIMITED stand (GCP conflict, fused refs, v1-v2 deltas, live integration, licenses/weights-OSI). Missing: AA originals, full v1-v2 diffs, deployment restrictions, subjective evals, Grok, Kimi/Flint hygiene, TanStack/Securing/Vercel clocks. Thin-section risk flagged (P4 single, Eleven leg, DeepSeek leg) with demote-to-HOLD option for Sol. State EVIDENCE_REVIEWED, Gates pending; stop `SOL_W43_ARCHITECTURE_R2_SUBSTANTIVE_REVIEW_READY`.
