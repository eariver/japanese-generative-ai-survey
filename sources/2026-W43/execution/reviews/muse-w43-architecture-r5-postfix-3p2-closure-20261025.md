# Muse W43 Architecture r5 postfix closure — R4-010/011/012 integrated

Status: `POSTFIX_COMPLETE / SOL_W43_ARCHITECTURE_R5_POSTFIX_INDEPENDENT_RECHECK_READY (pending Sol re-check)`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Starting HEAD `fe02b29ae026d7df3cf52a5a88a1c3c48d6268de` / Tree `769ba06f1dbd0f7c04cc40082a67bea2a8beb8fc` (remote 6-way MATCH pre-write).
Fixed r4 subject of independent audit: `ee206400c9740dd2288b894f31f79a119b7758bc` / Tree `49f55eef6e8fc5beacc1645b62ba0d25e42ccb1d`. Main `041a08df…`/`a134dc36…`, Frozen Core `774dd39a…`/`cd46a6f7a…` unchanged.
Contract: `execution/instructions/sol-w43-architecture-r5-independent-postfix-3p2-integrated-repair-20261025.md`. No ADVANCE/operator/Human/Draft/TeX/PDF/Freeze/Release. Shared Core, accepted r4 Evidence/Views, 51 Materiality, Completeness LIMITED, State/Checkpoints/Gates unchanged.

## 1. Dispositions

| ID | Sev | Disposition | Canonical change | Source authority | Residual |
|---|---|---|---|---|---|
| R4-010 runner generated_at future | P2 MUST_FIX | FIXED (new real provenance; history preserved) | r4 `2026-10-25T12:00:00Z` anomaly (3h19m12s after r4 commit 08:40:48Z) preserved untouched in NEW immutable `execution/history/selection-architecture-r4/` (README documents it; 7 SHAs verified). r5 input/runner/audit use contemporaneous invocation `2026-10-25T09:22:08Z` (recorded `date -u`, run 09:22:34Z→09:23:24Z UTC, commit after). Rebound input-r5 `5b7b6c1b…`, audit-r5, arch/summary SHAs. Matrix/Selection/Attention hashes carried. | Clock: `date -u` UTC method logged (run-start/run-stop). Commit chronology: r5 generated_at < runner stop < final commit (verified post-commit). Runner validates field presence only, not chronology (adjudicated). | None blocking. Old r4 timestamp NOT rewritten (history is the record). |
| R4-011 Elo +47 vs +50 | P2 MUST_FIX | FIXED (versioned crosswalk, no universal delta) | P4 §4.3: blog-snapshot +47 vs product/PR +50 with 1139−1089=50 verified, comparison/version/snapshot + AA UNKNOWN, unification ban. Boundaries: version/snapshot split + MUST-NOT against single-truth +47/+50. | Blog (rendered 2026-10-25): +47, 12.45s/277.80s, 26.5x/96.2%. Product page (rendered 2026-10-25): 1139 vs 1089 = +50; table AA-Video-I2V v1.1 preliminary, 10s 16:9 720p/768p avg. PR Oct19 15:46 ET (rendered 2026-10-25): 1139/4,868 votes, 1089→1139 = +50. AA originals unarchived, vendor-attributed. | Publisher revision history / AA snapshot deltas UNKNOWN (reported). |
| R4-012 keyframes availability | P2 MUST_FIX | FIXED (UNRESOLVED conflict, qualified claim) | P4 §4.1: text/image = launch-confirmed; keyframes = Oct19 PR asserts availability + blog link vs Oct18 FAQ "Two at launch" → UNRESOLVED_VENDOR_DOC_CONFLICT, W43 live/schema/GA NOT_VERIFIED. Boundaries + DRAFT MUST-NOT against GA-certain prose. | Blog: keyframes link present. Product FAQ (rendered 2026-10-25): "Two at launch: text to video and image to video. Information updated as of October 18, 2026." PR (rendered 2026-10-25): "text-to-video, image-to-video, and keyframes-to-video … through a unified API", available Oct 19, 2026. No dated schema/live-call/GA proof retrieved. | Endpoint truth at W43 cutoff remains UNRESOLVED (reported). |
| ISA-004 source binding | carry | CLARIFIED (no overclaim) | P4 §4.2: PR = PRNewswire-distributed publisher-authored first-party (not third-party bench); 10.95s leg raw = RENDERED_ONLY; "22x" headline = lower-bound style, not called false; 26.5x/96.2% marked input-incompatible; recomputed 25.37x/22.31x/95.52% kept with apparatus UNKNOWN. Boundaries: source-type split rewritten (SECONDARY→publisher first-party). | Same three rendered sources + arithmetic recomputation (25.3699/22.3133/95.5184%). No new raw archive; independent measurement NOT_DONE. | 10.95s raw unarchived; apparatus UNKNOWN carried. |

No `BLOCKED_R5_RUNNER_PROVENANCE` / `BLOCKED_R5_SOURCE_AUTHORITY` / `SELECTION_REVIEW_REQUIRED`: r5 run is real with logged UTC provenance; fal sources are publisher-authored as claimed (rendered, not byte-archived — explicitly marked); no upstream Evidence/Selection invalidation found.

## 2. r4 → r5 strict field diff (canonical JSON)

- Input: `selection-architecture-input-r4.json` (`67d0f39f…`) → `selection-architecture-input-r5.json` (`5b7b6c1b…`). Assignments 32/32 byte-identical (19/1/12; PRIMARY 12 / SUPPORTING 7 / NONE 13). Architecture section only: `runner.generated_at` 12:00:00Z→09:22:08Z + invocation; P4 §4.1/§4.2/§4.3 rewritten; 2 stale P4 boundaries replaced + 3 added (net P4 boundaries 4→7). All other 7 packages byte-identical text.
- Matrix `16a6bbfe…` → IDENTICAL. Selection `50decd86…` → IDENTICAL. Attention `7c3e4deb…` → IDENTICAL (68/68, limit 100).
- Architecture `9ab37dd6…` → `6b1b655ba70c2b161db4e3930a8901f6c791564cdb8232efb511998c12423e01`. Summary `c8bb6e2e…` → `ff21e7ae65ff9d48b6140787effa7f7da578f5762eadd2dd9e9bce279dc8e874` (arch-SHA binding only). Audit `ff2267e2…` → `949129535d6a78992157bc14aae017fff9705fb6968f19e22edb1861b003af1c` (input + arch/summary SHAs NEW; matrix/selection/attention carried).
- Packages 8/8 IDs; must-covers 31/31 (5+6+4+3+4+3+3+3); 19/19 unique placements, no HOLD/REJECT placed; 5 LIMITED carried; prior 9 ISA notes (DeepInfer排他, Voxtral UNRESOLVED table, 8B/4B + 39.8B/2.5B, recomputation labels, Decisions per-request/write-billed, 68→ledger, P8 ESTIMATE, 日英併記, status columns) untouched.

## 3. Native run transcript (scratch @fe02b29a, detached, no branch)

1. `cp input-r5 → scratch; rm 7 proposal outputs (scratch only)`; recorded `RUN_START_UTC=2026-10-25T09:22:08Z` via `date -u`, `runner start 2026-10-25T09:22:34Z (UTC)`.
2. `PYTHONPATH=$SCRATCH python3 scripts/run_selection_architecture_v2_interactive.py --repo-root $SCRATCH --state sources/2026-W43/production-state.json --input selection-architecture-input-r5.json` → exit 0, `{"selected_count": 19, "architecture_package_count": 8, "review_readiness": "READY_FOR_ARCHITECTURE_REVIEW"}`; stop `runner stop 2026-10-25T09:23:24Z (UTC)`.
3. Matrix/Selection byte-identical r3/r4; arch/summary NEW; default attention superseded; `build_attention(limit=100)` → 68/68 unique, overflow 0, truncated false, `7c3e4deb…` IDENTICAL; `validate_attention` PASS.
4. Audit reconciled by recomputing exact output SHAs (no fake provenance).
5. `survey_stage_validation_v2 --artifact candidate-matrix=… --artifact candidate-selection=…` (EVIDENCE_REVIEWED→SELECTION_COMPLETE) → exit 0, PASS, impl `fe02b29a…`, State untouched. Second bridge NOT run (`NOT_RUN_CURRENT_STATE`).
6. Post-commit chronology check: r5 `generated_at` 09:22:08Z ≤ runner stop 09:23:24Z ≤ final commit time (see §5) — no future anomaly.

## 4. Negative tests (scratch, separately by checker)

- 9 prior ISA negatives: re-run against r5 arch — (i) simultaneous MTP only in排他/ban contexts; (ii) TTS only unification bans + UNRESOLVED table; (iii) 11-language only ≠support; (iv) no standalone `4B total`/`2.5B total`; (v) only ≠総無料 qualifications; (vi) only per-request; (vii) Metrics/Grok REJECT/NONE + OUT/NEVER_STORY/FUTURE present, zero live-now; (viii) 6 measurement words all in bans/qualifications; (ix) zero 68↔SELECTED conflation. All PASS. (Core validators do NOT check these semantics — edition-local.)
- (a) generated_at: r5 = real 09:22:08Z invocation (≠12:00Z guess), r4 12:00Z preserved untouched in history, generated_at ≤ final commit → PASS.
- (b) Elo: 1139−1089=50 verified; arch contains both +47 (blog snapshot) and +50 (page/PR) with version split + unification ban; no unqualified universal delta → PASS.
- (c) keyframes: arch contains UNRESOLVED_VENDOR_DOC_CONFLICT + Two-at-launch + PR assertion + NOT_VERIFIED; no GA-certain sentence → PASS.
- PR publisher status: arch calls PR publisher-authored via PRNewswire, not third-party bench; raw = RENDERED_ONLY → PASS. No false independent-benchmark claim.

## 5. Hashes, chronology, and state

- New r5: Matrix `16a6bbfe…` (=r4/r3), Selection `50decd86…` (=r4/r3), Architecture `6b1b655b…`, Summary `ff21e7ae…`, Attention `7c3e4deb…` (=r4/r3), Input-r5 `5b7b6c1b…`, Audit-r5 `94912953…`.
- r4 history: 7 SHAs in `execution/history/selection-architecture-r4/SHA256SUMS` (matrix/selection/arch/summary/attention/input/audit + README), cmp-verified; r3 archive immutable.
- Final commit time (author/committer, JST→UTC): recorded at push/read-back; generated_at 09:22:08Z predates it (no R4-010 recurrence). State `EVIDENCE_REVIEWED`, next `stage:selection`, Selection/Architecture pending, both Human Gates pending — verified unchanged post-commit.
- P4 page 3.0 unchanged (no source-justified re-budget); honest depth, no padding.
