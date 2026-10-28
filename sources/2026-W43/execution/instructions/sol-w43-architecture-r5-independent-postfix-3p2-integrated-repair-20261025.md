# W43 Sol → Muse — Architecture r5 bounded integration of independent post-fix P2 findings

Status: `SOLE_ACTIVE_EXECUTION_CONTRACT / R5_PROVENANCE_AND_FLUX_CORRECTION / HARD_STOP_BEFORE_STAGE`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
EXISTING branch ONLY: `weekly/2026-W43-v2-work`
**Exact starting 6-way authority comes from Sol's final dispatch AFTER this contract is committed. This file's own parent SHA is not permission to use a stale HEAD.**

## 0. Read-only six-way start guard — mandatory before ANY repository write

Compare remote work HEAD AND root Tree to exact values in Sol dispatch; independently compare remote reviewed `main` HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`; Frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch -> **STOP_ZERO_WRITES**, report six actual vs expected. Existing branch only, ordinary commit and non-force push, no reset/rebase/cherry-pick/force/new/fallback/review/repair branches or history rewrite. Do not work from the fixed audited r4 SHA as though it were current remote HEAD.

Read in order:
1. `sources/2026-W43/execution/audits/independent-sol-w43-architecture-r4-postfix-review-result-20261025.md` (TEXT-NORMALIZED of independently submitted original, raw SHA `2a4b54078e6da63d5b03d25f7c2e67d5ae2f5880c82b40d6f17d219b061c21f2`, 19,491 bytes; NOT byte-identical GitHub copy).
2. `sources/2026-W43/execution/reviews/sol-w43-architecture-r4-postfix-independent-adjudication-20261025.md` (binding editorial disposition, R4-010/011/012 all ACCEPT P2 MUST_FIX).
3. r4 closure/crosswalk/risk register; current r4 input/architecture/review-summary/attention/audit; preserved r3 7-file history and SHA256SUMS.
4. accepted r4 Evidence, Views, supplement raw, r4 Materiality 51, Completeness LIMITED, actual State `EVIDENCE_REVIEWED`, Selection/Architecture checkpoints and both Human Gates pending.
5. Frozen native `scripts/run_selection_architecture_v2_interactive.py`, architecture/attention validators, stage validation contracts, known issues #568/#569 — **read only**.

## 1. R4-010 — create trustworthy r5 runner metadata without rewriting old history

- Preserve **all seven** current r4 canonical/proposed JSON bytes before modification in NEW edition-local `sources/2026-W43/execution/history/selection-architecture-r4/` plus `README.md`, `SHA256SUMS`, direct content byte-identity readback. This history records the original `2026-10-25T12:00:00Z` meta anomaly as historical fact; do not “correct” the past silently. r3 archive remains immutable.
- Inspect any real runner command logs, system clock/timezone, Git commit metadata, `generated_at` field definition. State whether a trustworthy original r4 execution time is actually recoverable; do NOT invent a new *historical* r4 run time.
- When performing a real r5 run, capture a real UTC wall-clock start with timezone and clock method (e.g., recorded `date -u` command output plus runner start/stop log) and use that **contemporaneous r5 invocation** time for new `runner.generated_at`; separately keep `observed_at` for source reads. No fixed 12:00Z guesses. Check chronology against final first-containing commit author/committer timestamps; should not postdate that commit absent a documented semantics exception.
- Current r4 `interactive input`, `execution/compat/selection-architecture-input-r4.json`, runner audit share this metadata: regenerate as **r5** authoritative proposal with consistent hashes and explain old/new fields and native provenance. Do NOT retroactively amend immutable r4 history. No handcrafted native machine outputs.
- If no real/provable new r5 run or time clock evidence, STOP `BLOCKED_R5_RUNNER_PROVENANCE`, no Stage or fake PASS.

## 2. R4-011 — Elo provenance conflict, P4 §4.3

- Independently read and record EXACT URLs, published/updated time if genuinely observed, edition-local `observed_at` and data type (first-party page rendered versus original preserved bytes) for:
  `https://fal.ai/blog/introducing-flux-3-max-by-fal` — +47 Elo;
  `https://fal.ai/flux-3-max` — 1,139 vs 1,089 = +50 Elo;
  `https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html` — publisher-issued PR, Oct 19 2026 15:46 ET, +50 Elo, 10.95 seconds.
- In P4 §4.3: distinguish publisher blog snapshot +47 from publisher page/PR +50 with exact comparison target/snapshot/version and UNKNOWN underlying AA changes. Do not use a single unqualified improvement. Do not invent AA vote date/original beyond claimed 4,868, mark original arena page not independently archived and vendor-attributed.
- Audit `1139 - 1089 = 50`. Preserve vendor preference-rating provenance versus latency method as separate dimensions.

## 3. R4-012 — keyframes-to-video release status conflict, P4 §4.1

- Record fal blog's keyframes link; fal product FAQ “Two at launch” (text-to-video and image-to-video, information updated as of Oct 18); and **fal-issued PR Oct19 explicitly describing text, image AND keyframes-to-video availability**.
- Create a source/version/observation/status crosswalk with columns announcement, link, documented API schema, actual API call, general-availability, regional/cutoff proof. Mark schema/live/general availability NOT_VERIFIED absent actual dated evidence. Do not merge FLUX 3 base keyframe endpoints into FLUX 3 Max availability.
- Replace ambiguous `text/image/keyframes` unconditional §4.1 wording with qualified claim: text/image confirmed publisher statement; keyframes asserted by Oct19 PR and linked in blog, but contradicts Oct18 product FAQ, `UNRESOLVED_VENDOR_DOC_CONFLICT` and no independently verified W43 live call. Carry boundary and DRAFT MUST-NOT, so no reader-facing false endpoint certainty.

## 4. Improve ISA-004 FLUX source binding without benchmark overclaim

- Oct19 fal-issued PR is a first-party PUBLISHER statement hosted by distributor PRNewswire. It quotes 10.95s/277.80s and 50 Elo; it is not an independent speed study. Its **raw bytes** were not archived in r4; if you capture authentic raw bytes now, put only in NEW W43 edition-local supplementary source intake, with SHA256, captured time, content type and source URL; never mutate accepted r4 Evidence or old raw files. If unavailable, mark `RENDERED_ONLY` and never claim byte-archived.
- Distinguish blog/product 12.45s/277.80s from PR 10.95s/277.80s; recompute 25.37x and 22.31x and 95.52% correctly, explain published “26.5x / 96.2%” inconsistent with shown blog inputs; headline “22x” may be rounded/conservative, not necessarily false.
- Quote apparatus limitations: same sample distribution/GPU/batch/quality/cold-warm UNKNOWN; product lists nominal 10-second 16:9 720p/768p measurement; independent reproduction NOT_DONE. Distinguish AA preliminary 1.139Elo ratings from fal speed measurements.

## 5. Frozen-native regeneration and hard negative tests

- Preserve EXACT 32 candidate Matrix IDs, 32 Selection assignments & 19/1/12, architecture roles and 19 unique placements, 8 package IDs/31 must-covers, 68/68 unique native Attention with limit=100, its SHA preserved when basis unchanged. Preserve 5 LIMITED and existing source contradiction notes (DeepInfer, Voxtral, open weights). r5 is narrow: only runner metadata, P4 necessary passages/purpose/boundaries, and derived hashes/edits; no wholesale rewrites.
- Make `execution/compat/selection-architecture-input-r5.json`. In separate detached scratch checkout pinned at exact verified STARTING commit (no branch), use frozen runner and validation scripts with true r5 timestamps. Run real native `scripts/run_selection_architecture_v2_interactive.py`; refresh native 68/68 Attention via frozen `build_attention(limit=100)`; rebuild audit with exact SHA256 of input and five outputs. Verify old r4 seven JSON snapshots and current r5 outputs hash/binding; both Matrix/Selection MUST remain byte-identical r3 and r4.
- Run frozen actual structural/schema/semantic-invariant validators plus **scratch-only** Selection stage precheck in current EVIDENCE_REVIEWED; Architecture bridge precheck on real SELECTED_COMPLETE/SELECTION_COMPLETE state only if lawful, otherwise `NOT_RUN_CURRENT_STATE`. Never forge a new State for precheck or claim real operator success.
- Explicit nine prior ISA negative tests and three new regressions: (a) `generated_at` must be grounded real r5 invocation (past r4 untouched) and no future vs first-containing commit; (b) reject unqualified +47 or +50 Elo universal claim, check 1139-1089=50; (c) reject assertion that keyframes endpoint was definitely GA at cutoff absent dated proof. Test PR publisher status, original raw vs rendered, no false independent benchmarks. Output PASS/FAIL/NOT_RUN separately by checker.
- Re-evaluate P4 page estimate 3.0 and page plan only if sources justify edits; preserve honest depth and no padding. If newly acquired first-party information invalidates upstream Evidence or Selection rather than Architecture language alone, STOP `SELECTION_REVIEW_REQUIRED` and report exact claim/source; do not edit accepted authority or secretly change Selection.

## 6. Outputs, prohibited actions and stop

Required NEW edition-local artifacts:
1. `execution/history/selection-architecture-r4/{7 snapshots,README.md,SHA256SUMS}`.
2. `execution/compat/selection-architecture-input-r5.json`.
3. `execution/source-intake/w43-r5-fal-official-source-conflict-crosswalk.md` — three first-party sources, URL/time/byte-provenance and 10.95/12.45, 47/50, 2-vs-3 endpoints.
4. `execution/reviews/muse-w43-architecture-r5-postfix-3p2-closure-20261025.md` — each new finding disposition, exact JSON pointers, before/after, native-run commands/exit codes, future-time audit, all SHA256, negative cases, residual LIMITED, original vs normalized audit provenance.
5. `execution/sessions/muse-w43-architecture-r5-postfix-20261025.md`.
6. `execution/SOL_W43_ARCHITECTURE_R5_POSTFIX_INDEPENDENT_RECHECK_HANDOFF.md`, plus `execution/index.md` append.
7. Frozen-native proposed output JSON (Matrix, Selection, Architecture, Summary, Attention, interactive input/audit) regenerated exactly as tested.

Absolutely prohibited: `ADVANCE_STAGE`, operator `/survey-core-execute` or Issue #448 comment, Human approvals, Draft/TeX/PDF, Freeze/Release, Core changes, new branch, force/rewrite, changes to accepted r4 Evidence/Views/51 Materiality/Completeness/Discovery/Screening, Production State, Checkpoints or Gates.

Success stop token: `SOL_W43_ARCHITECTURE_R5_POSTFIX_INDEPENDENT_RECHECK_READY`. Block tokens: `BLOCKED_R5_RUNNER_PROVENANCE`, `BLOCKED_R5_SOURCE_AUTHORITY`, `SELECTION_REVIEW_REQUIRED`, or `STOP_ZERO_WRITES`. Finish by normal commit + non-force push to the existing branch and REMOTE readback exact HEAD/Tree and protected paths. Stop for editorial Sol; this contract itself gives no Stage or independent PASS.
