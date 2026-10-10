# SOL W40 r15 handoff — boundary preservation + technical depth repair (REVIEW REQUIRED)

Status: `SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_REQUIRED`
Date: 2026-10-10 JST
Branch (existing only): `weekly/2026-W40-v2-work` — normal commits + non-force push ONLY.
Authorizing inputs: `execution/instructions/2026-10-10_muse-w40-r15-boundary-preservation-and-technical-depth-repair.md`
+ `execution/reviews/sol-w40-r14-independent-audit-disposition-20261010.md`
(independent r14 `REVISION_REQUIRED`; F01–F08 adopted; bounded r15 authorized).

## 1. Git authority (exact bytes)

- Starting remote HEAD read-only pre-write (ls-remote + GH API, zero writes):
  `1b9f3f1dc451189759495fbd17779f9412d17ccf` == outer Exact Starting SHA
  (parent = r14 `d95479721…`); tree `e86bddad0fd1bf507da50d825285e0a5dbffda10` ==
  Expected Tree; remote main == `afdb3df3faa20af3bb5798be429bba8dbd2100b1` ==
  reviewed main; HEAD == main. ALL MATCH → proceeded.
- Local 1-behind aligned fetch + FF-only. Pre-write guards PASS: `EVIDENCE_REVIEWED`,
  next `stage:selection`, Selection/Architecture pending, Gates pending/null, exception
  inactive; 37/37/35/35/37 + checkpoint SHAs; r13 preview `dc024778…` + r10 matrix
  `f07b1166…` byte-matched (§0.5).
- Prohibitions kept: no branches/rewrites; no `scripts/`/`schemas/`/`config/`/
  `.github/`/Core/`main`/other-edition/upstream/State/checkpoint/Issue/Gate writes;
  no Human/release decisions; r14 artifacts immutable (r15 successors/addenda only).
- W40-local commits only (§7); final HEAD/Tree + remote readback in outer report.

## 2. Changed paths (W40-local only)

NEW: `execution/architecture-boundaries-r15.json` (SHA `1736737e…`);
`execution/architecture-boundaries-validation-r15.json` (PASS);
`execution/architecture-staged-outline-r15.md`;
`execution/technical-prep-r15/p6a-deep-draft.md` + `p6b-deep-draft.md`;
`execution/editorial-supplement/r15/evidence-source-provenance-correction.md` +
`retrieval-manifest-r15.json`;
this handoff `execution/SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_HANDOFF.md`;
`execution/sessions/muse-w40-r15-20261010.md`.
MODIFIED: `execution/index.md` (entry appended; history kept).
r14 files untouched.

## 3. F01 — boundary preservation (top priority; EVIDENCE-GRADED)

- Recomputed from Matrix bytes: 28 SELECTED → **113 raw candidate-to-boundary
  relationships** (Gemini 7; 9×5; 17×4; 9×3 — distribution in validation JSON).
- `architecture-boundaries-r15.json`: 28 entries (exact verbatim strings, no
  normalization) + 9 package aggregates (dedup within package): raw 113 →
  unique 105 (P4 −3, P5 −2 identical-string dedups, explained, no semantic
  substitution, no cross-package merge). Mapping from accepted coverage-r14.
- `architecture-boundaries-validation-r15.json`: independent second-pass from source
  bytes — 28/28 IDs, 20P/8S, assignment/Matrix/coverage equality, 0 HOLD/REJECT,
  PRIMARY-single/SUPPORTING-≥1, exact-string equality per entry, per-package
  membership equality, source-SHA binds, per-package raw→unique table —
  **literal-membership missing = 0/113**, status PASS.
- Actual Core rule applied: unmodified reviewed-main `validate_architecture`
  (envelope + 5-SHA basis + placement/usage + literal `boundaries` membership +
  status/shape) executed DIRECTLY against an ephemeral in-memory PROPOSED object
  built from the staging → **0 errors**. Disclosed limits: placeholder
  thesis/goals/empty-must-cover/page-plan (membership-rule probe, not semantic
  Architecture); in-memory only, never written; NOT a formal Architecture PASS
  (no Human review, no checkpoint, no downstream chains tested).
- `architecture-staged-outline-r15.md` references (not duplicates) the SHA-bound
  arrays per package with roles + content requirements + COND exclusion.

## 4. F02/F03/F04 — P6a repair (primary-verified)

- Eq.6 CORRECTED with exact symbols from ar5iv rendering of v1 (retrieved r15):
  `A_i^{eff}=clip((c̄_g−c_i)/c̄_g,−1,1)` for `i∈G_g^+` else 0; `<2 successes →
  A_i^{eff}=0 ∀`; "only re-ranks among successful trajectories by inference cost";
  `A_i=A_i^{out}+w_eff A_i^{eff}` ("both correct and efficient") → total keeps
  `A_i^{out}`; the "→0 overall" reading is retracted with the error named.
- Eq.1 (`c_{t+1}=c_t⊕f^{LM}_θ(c_t)`) / Eq.2 (`c_{t+1}=f^{CLM}_θ(c_t)`) / Eq.3
  (prefill-from-first-mismatch + decode; ≠ wall time ≠ hit-rate) / Eq.4 (`;s`)
  quoted; Eq.5 full text UNVERIFIED (role only). Path-based file ops: unrestricted
  updates + Bash sync (claim-1 scope; deeper op semantics UNVERIFIED); harness→intrinsic
  shift; SCR mechanism + empirical-preservation limit.
- Metrics separated per paper: BCP 59.4% +11.4% RELATIVE (Codex-style) / −21.5%
  (Codex) / −28.9% (MEM1); TB2.1 70% (§5) vs 29.5%-fewer (intro) both kept;
  TBLite 73.7/67.0 @91%; EdgeBench/swarm/RL/Table-2 rows with denominators;
  35.9 POINTS (no %/pp conversion); RL +0.4 points / −38.8% same-recipe.
  Controlled conditions: Mini-SWE backbone, out-of-box, Qwen3.6-27B/32K/100-turn.
- Licenses per artifact+revision: paper CC BY 4.0 (arXiv PDF metadata, v1) / repo
  CC BY-NC 4.0 (LICENSE raw-fetched r15, main-as-of-2026-10-10, commit unpinned).
- Olmo-core 3: MXFP8 CONTROLLED (B300×4, uniform expert load, +21% vs BF16,
  103→95 GiB, FF+inter-expert gains, where-it-helped-only scope); DDP-resident
  dispatch explanation from blog quotes (rowwise/grouped-GEMM/resident-routing);
  47B measured vs 1.2T-random-routing-858 vs 2.38T-short-capacity separated;
  4 negatives with mechanism/attempt/failure/limits; infra-not-weights kept.
  Tech Report body NOT retrieved (landing 200/shell, no PDF link) — stated, unfilled.

## 5. F05/F06/F07 — P6b repair (primary-verified)

- AgentPerf: roofline reading CORRECTED ("above the bandwidth-constraint roofline",
  successful-configs-scoped, NOT vs speculative-off); 14 configs ALL speculative
  (MTP/DFlash/DSpark) + official/self-built distinction VERIFIED; metric/HW/model/
  quant/replay/prefill/tool-skip/price table; local-single-user vs production
  AA-AgentPerf (concurrent/SLO/MW, 2026-06-12) separated with quote; living-pin rule.
- OpenTTS: macro-average WER (Seed+CV3 English), CJK CER + cross-language macro,
  RTFx/TTFA/SIM per announcement; TTFA protocol clause-by-clause (batch 1 / 50 CV3
  prompts / same HW+voice / 3 warm-up dropped / median / H200 + growing CPU);
  Qwen3-ASR-1.7B + WavLM deps; proxy/MOS disclaimers; leaders named WITHOUT
  unconsumed WER values. TEMPORAL SPLIT with commit history: article "will soon
  open-source" (Sep 30) vs repo created Sep 15 vs eval scripts landed Oct 7
  (1645e63016f0) → cutoff-time script absence is a DATED NEGATIVE (2b2cd31257d2 HEAD
  Oct 9); no backdating.
- RL-Hub: SUPPORTING/tags/separation/current-vs-future retained; framework pins
  (`harbor==0.21.0`, `openenv[harbor]==0.7.0`, TB-2.1@2.1.0) kept as Sep-28 snapshots;
  taskset git revisions NOT published/retrieved → NOT_REPRODUCIBLY_PINNED (pins ≠
  total reproducibility); missing inputs enumerated.

## 6. F08 — provenance (delimited, not inflated)

- Addendum + `retrieval-manifest-r15.json` (allowlisted bounded artifact: URL/method/
  minute/SHA/excerpt-pointer; full HTML excluded for comments-personal-data +
  dynamic-copyright + r11 policy). mtimes RE-READ stable, labeled
  MUSE_LOCAL_MTIME_REPORTED / NOT_INDEPENDENTLY_REPRODUCED; minute precision, mtime ≠
  HTTP time; BYTE_DIFFERENCE-only retained; three clocks separate; auditor CAN
  re-fetch strings/counts but NOT mtimes/ms-extraction. NOT-verified list (4 items).

## 7. Finding matrix (no blanket closure)

| ID | Status | Anchor |
|---|---|---|
| F01 | CORRECTED (staging+rule evidence) | boundaries-r15 (`1736737e…`) + validation PASS (0/113) + ephemeral Core PROPOSED 0-errors (disclosed limits) + outline-r15 |
| F02 | CORRECTED | p6a draft §1 Eq.6 symbols + RL-signal meaning; error named |
| F03 | CORRECTED | p6a draft §1 (Eq.1–4 roles, Eq.3 accounting, SCR, separated metrics, per-artifact licenses) |
| F04 | CORRECTED | p6a draft §2 (MXFP8 controlled config, dispatch, negatives, measurement separation; report gap stated) |
| F05 | CORRECTED | p6b draft §1 (roofline, 14-speculative, local-vs-production) |
| F06 | CORRECTED | p6b draft §2 (aggregation, TTFA protocol, deps, temporal split with commits) |
| F07 | CORRECTED (pinning) / STILL_OPEN (reproduction inputs) | p6b draft §3 (NOT_REPRODUCIBLY_PINNED for taskset revisions; missing inputs listed) |
| F08 | CORRECTED (wording+artifact) | provenance addendum + retrieval-manifest-r15.json; 4-item NOT-verified list |

Preserved r14 PASS areas (not reopened, no new evidence): 28-ID Role map, AutoSynthData
verifier triad/gates/limit, supplement topology analysis. #562 stays separate Core task.

## 8. P6a/P6b primary-source consumption (exact)

Retrieved r15: ar5iv 2609.37725 HTML 417,994 B (equations/abstract/§5 verified);
Ai2 blog 1,166,521 B (mechanisms/MXFP8/negatives verified); AA article 355,778 B
(roofline/configs verified); HF OpenTTS blog 323,513 B (aggregation/protocol/scripts
wording verified); GH API repo facts (OpenTTS scripts commits/license) + raw CLM
LICENSE (BY-NC text). NOT retrieved: arXiv PDF bytes (r4 FAILED; ar5iv substitutes
same v1); ar5iv figures/Appendices B–F/code; Tech Report body (shell only); CLM repo
commit pin; AA config enumeration/pins; OpenTTS WER values/Space internals/audio;
RL taskset revisions/selection/substrate. Each is marked UNVERIFIED or
NOT_REPRODUCIBLY_PINNED in the drafts — nothing filled from recollection.

## 9. Unchanged attestations + terminal

- Untouched Core `validate_selection` DIRECTLY re-executed on preview-r13 (this run,
  `scripts/` etc. unmodified): result in outer report. State/Gates/Core read back
  unchanged (§1). No shared-Core writes.
- Commits: FF children of `1b9f3f1dc…`, non-force push, remote readback verified
  (outer report).
- Terminal: `SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_REQUIRED`. NO Selection
  Acceptance, Stage transition, canonical Architecture/checkpoint, Human Gate, Freeze,
  public release, ad hoc supplement, Core fix. STOP.
