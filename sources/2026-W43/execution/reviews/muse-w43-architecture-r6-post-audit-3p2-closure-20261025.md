# Muse W43 Architecture r6 post-audit closure — R5-N01/N02/N03 governed correction

Status: `CORRECTION_COMPLETE / SOL_W43_ARCHITECTURE_R6_CORRECTION_READY_FOR_SOL_REVIEW (pending Sol re-check)`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Starting HEAD `b7445700dd852024ac27f1feaed58a61de9a9a42` / Tree `e5cd33332af5aa52ba6358d3296510ee2ac44d6b` (remote 6-way MATCH pre-write).
Fixed established r5 subject: `6f961295c6743248c2bccb34e15cb84116bf4de7` / Tree `6a1f716b024cf742162a95dfb0bace227ee29f5e`. Main `041a08df…`/`a134dc36…`, Frozen Core `774dd39a…`/`cd46a6f7a…` unchanged.
Contract: `execution/instructions/sol-w43-architecture-r6-post-stage-3p2-governed-regeneration-20261025.md`. No ADVANCE/operator-bridge/Human/Draft/TeX/PDF/Freeze/Release. No Human REQUEST_CHANGES or approval generated (operator invalidation records `human_decision=false`).

## 1. Operator invalidation (frozen, pre-regeneration)

- Preconditions verified: `human_gates` pending/null, `terminal_reason=HUMAN_GATE_REACHED`, Architecture checkpoint passed, no Human review records, prior bridge receipts intact.
- Command: `survey_human_gate_v2.py invalidate-pending-gate --state sources/2026-W43/production-state.json --gate ARCHITECTURE_REVIEW --regeneration-boundary EVIDENCE_REVIEWED --reason 'Independent Sol fixed-r5 pre-Human Architecture audit REQUEST_CHANGES; R5-N01/N02/N03' --operator-reference '<adjudication + original audit>' --expected-work-branch-head b7445700… --invalidated-commit-sha b7445700…` → exit 0 (11:09:29Z→11:09:31Z UTC).
- Record: `execution/operator-invalidations/architecture-invalidation-0001.json`, id `operator-invalidation:2026-W43:architecture:1:96072b976bfde34f`, sequence 1. Frozen post-write `validate_operator_invalidation_record` PASS; agent state resumable, no errors.
- Effect: State `ARCHITECTURE_ESTABLISHED/HUMAN_GATE_REACHED` → `EVIDENCE_REVIEWED`, next `stage:selection`, terminal null; Selection+Architecture checkpoints pending; both Human Gates pending/null. Superseded canonical Matrix/Selection/Architecture/Summary/Attention + both planning checkpoints + interactive input removed (7 r5 files preserved byte-identical in history). Prior receipts, stage contracts, accepted Evidence/Views/Materiality/Completeness untouched.

## 2. Dispositions

| ID | Sev | Disposition | Canonical change | Source authority | Residual |
|---|---|---|---|---|---|
| R5-N01 P4 §4.2 brackets | P2 MUST_FIX | FIXED (separate equations) | `速度倍率＝旧基準時間/新候補時間 — 277.80/10.95≈25.37x[PR]、277.80/12.45≈22.31x[blog/製品頁]；所要時間削減率＝(旧基準時間−新候補時間)/旧基準時間×100 — (277.80−12.45)/277.80×100≈95.52%(分母=旧基準277.80秒)`. Old `[t_baseline/t_candidate、分母=新候補秒…]` bracket (ratio gloss on the percent) removed. | Recomputed: 25.3699 / 22.3133 / 95.5184%. Publisher-measured, not independent timing (kept). | None blocking. |
| R5-N02 P8 §8.2 labels | P2 MUST_FIX | FIXED (uninverted, source-attributed) | `GitHub release 15:18:14Z(GitHub API published_at、確認2026-10-25)/npm registry 15:21:49Z(registry time["1.0.0"]、確認2026-10-25)`. Old inverted `registry 15:18:14Z/release 15:21:49Z` removed. Selection rationale (already correct) left byte-identical. | GitHub release API `published_at=2026-10-22T15:18:14Z` (fetched 2026-10-25); npm `time["1.0.0"]=2026-10-22T15:21:49.491Z` (fetched 2026-10-25). Crosswalk filed. Oct23 blog stays day-only. | None blocking. |
| R5-N03 P6 §6.1 CVE | P2 MUST_FIX | FIXED (wording narrowed) | `CVE ゼロ(報告≠証明)` → `当該発行者ページの確認範囲でCVE識別子を特定できず、CVE付与の有無は未検証`. No registered-count claim, no nonexistence proof. | Patch page rendered scope + no CVE-registry cross-check (stated). Matrix-inherited provenance notes (`Zero CVE- strings` page observation) untouched — Evidence immutable. | None blocking. |

No `BLOCKED_OPERATOR_INVALIDATION` / `BLOCKED_R6_NATIVE_REGENERATION` / `SELECTION_REVIEW_REQUIRED`: invalidation satisfied all frozen guards; TanStack publisher metadata independently confirmed both timestamps; no upstream Evidence/Selection invalidation found.

## 3. r5-established → r6 strict field diff (canonical JSON)

- Input: `selection-architecture-input-r5.json` (`5b7b6c1b…`) → `selection-architecture-input-r6.json` (`208b526b…`). Assignments 32/32 byte-identical (19/1/12; PRIMARY 12 / SUPPORTING 7 / NONE 13). Architecture section only: `runner.generated_at` 09:22:08Z→11:10:19Z + invocation; P4 §4.2 (N01); P8 §8.2 (N02); P6 §6.1 (N03). All other packages byte-identical text.
- Matrix `16a6bbfe…` → IDENTICAL (r3/r4/r5). Selection `50decd86…` → IDENTICAL. Attention `7c3e4deb…` → IDENTICAL (68/68, limit 100).
- Architecture `6b1b655b…` → `7d8f0ea5c8600acab5f19c36ed578011fe2af861ea3a445324fc2f081928c302`. Summary `ff21e7ae…` → `38c17eccff14e96e16596fc928152d18e67810572cd5e1cd466407def9100b74` (arch-SHA binding only). Audit `94912953…` → `d27adb843bf0c724a9bf342c33b6ca465d620f51ddafa7b408c5dcb92965783e` (input + arch/summary SHAs NEW; matrix/selection/attention carried).
- Packages 8/8 IDs; must-covers 31/31 (5+6+4+3+3+3+3); 19/19 unique placements, no HOLD/REJECT placed; 5 LIMITED; all prior ISA/R4 constraints and nonstandard-clock notes preserved.

## 4. Native run transcript (scratch @b7445700 + invalidated EVIDENCE_REVIEWED state bytes, detached, no branch)

1. `cp input-r6 → scratch; cp invalidated production-state.json → scratch (EVIDENCE_REVIEWED/stage:selection verified); rm 7 proposal outputs (scratch only)`; `runner start 2026-10-25T11:10:48Z (UTC)`.
2. `run_selection_architecture_v2_interactive.py --repo-root $SCRATCH --state … --input selection-architecture-input-r6.json` → exit 0, `{selected_count: 19, architecture_package_count: 8, review_readiness: READY_FOR_ARCHITECTURE_REVIEW}`; stop 11:10–11:11Z UTC (runner start/stop logged).
3. Matrix/Selection byte-identical r3/r4/r5; arch/summary NEW; default attention superseded; `build_attention(limit=100)` → 68/68 unique, overflow 0, truncated false, `7c3e4deb…` IDENTICAL; `validate_attention` PASS.
4. Audit reconciled by recomputing exact output SHAs (no fake provenance).
5. `survey_stage_validation_v2 --artifact candidate-matrix --artifact candidate-selection` (EVIDENCE_REVIEWED→SELECTION_COMPLETE) → exit 0, PASS, State untouched. Architecture bridge precheck NOT run (`NOT_RUN_CURRENT_STATE` — no forged SELECTION_COMPLETE).
6. Post-commit chronology: r6 `generated_at` 11:10:19Z ≤ runner stop ≤ final commit (see §6) — no future anomaly.

## 5. Negative tests (scratch)

- 9 ISA + 3 R4 negatives re-run: all 15 checks PASS (排他, TTS bans, params, price/per-request, +47/+50 split, keyframes UNRESOLVED + no-GA-certain, 6 measurement words in bans only, reversed absent, correct present, `CVEゼロ` gone, 19/19, 8/31).
- 3 new R5: (a) ratio vs percent denominators separated with correct labels → PASS; (b) 1139−1089=50 verified, inverted label string count 0, correct source-attributed labels present → PASS; (c) `CVE ゼロ` count 0, qualified wording present, no registered-count claim → PASS.
- PR publisher-first-party + RENDERED_ONLY + 22x lower-bound notes preserved.

## 6. Hashes, chronology, and state

- New r6: Matrix `16a6bbfe…` (=), Selection `50decd86…` (=), Architecture `7d8f0ea5…`, Summary `38c17ecc…`, Attention `7c3e4deb…` (=), Input-r6 `208b526b…`, Audit-r6 `d27adb84…`.
- r5-established history: 7 SHAs in `execution/history/selection-architecture-r5-established/SHA256SUMS` (+ README), cmp-verified; r3/r4 immutable.
- Final commit (author/committer, JST→UTC): recorded at push/read-back; generated_at 11:10:19Z predates it. State post-commit: EVIDENCE_REVIEWED (invalidated planning state), Selection/Architecture pending, both Human Gates pending — the two trusted bridges must be re-executed sequentially after Sol review (unchanged content + r6 content, separate Issue #448 executions + receipts).
- P4 page 3.0 unchanged (no source-justified re-budget); honest depth, no padding.
