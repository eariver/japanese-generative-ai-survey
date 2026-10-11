# SOL W40 r16 handoff — bounded documentation + Eq.5 repair (REVIEW REQUIRED)

Status: `SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_REQUIRED`
Date: 2026-10-10 JST
Branch (existing only): `weekly/2026-W40-v2-work` — normal commits + non-force push ONLY.
Authorizing inputs: `execution/instructions/2026-10-10_muse-w40-r16-bounded-documentation-and-eq5-repair.md`
+ `execution/reviews/sol-w40-r15-independent-audit-disposition-20261010.md`
(independent r15 `BOUNDED_REVISION_REQUIRED`; A01–A05 adopted; bounded r16 authorized).

## 1. Git authority (exact bytes)

- Starting remote HEAD read-only pre-write (ls-remote + GH API, zero writes):
  `109ddbddd8c00f81f58302d261750cfd26e14f2e` == outer Exact Starting SHA
  (parent = r15 `305aafa8a…`); tree `13258c731f72f5b624c48ccb2953b77fcd6da596` ==
  Expected Tree; remote main == `afdb3df3faa20af3bb5798be429bba8dbd2100b1` ==
  reviewed main; HEAD == main. ALL MATCH → proceeded.
- Local 1-behind aligned fetch + FF-only. Pre-write guards PASS: `EVIDENCE_REVIEWED`,
  next `stage:selection`, Selection/Architecture pending, Gates pending/null, exception
  inactive; 37/37/35/35/37 + checkpoints; 4 SHAs byte-matched (preview `dc024778…`,
  matrix `f07b1166…`, coverage-r14 `3de8bd56…`, boundaries-r15 `1736737e…`).
- Scope: A01–A05 ONLY. No Discovery/Evidence/Materiality re-run; no 113-structure
  regeneration; r15 drafts retained (Eq.5 note is additive). No `scripts/`/`schemas/`/
  `config/`/`.github/`/Core/`main`/other-edition/upstream/State/checkpoint/Issue/Gate
  writes; no prior-file edits (r15/r14 immutable); no Acceptance/transition/canonical
  Architecture/Gate/Freeze/Release/supplement.
- W40-local commits only (§4); final HEAD/Tree + remote readback in outer report.

## 2. Changed paths (W40-local only)

NEW: `execution/architecture-staged-outline-r16.md` (A01/A05 successor);
`execution/architecture-boundaries-validation-addendum-r16.json` (A03);
`execution/technical-prep-r16/contextlm-eq5-primary-note.md` (A04);
this handoff `execution/SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_HANDOFF.md`;
`execution/sessions/muse-w40-r16-20261010.md`.
MODIFIED: `execution/index.md` (entry appended only).
r15 Boundary JSON, Selection, Matrix, Coverage, r15 drafts: byte-identical, untouched.

## 3. Findings A01–A05 (status + file/anchor + check provenance)

| ID | Status | Disposition + evidence |
|---|---|---|
| A01 | CORRECTED | Package counts rebuilt r16 FROM ACTUAL BYTES (not copied): P1 14/12/2, P2 8/8/0, P3 13/13/0, P4 10/8/2, P5 18/17/1, P6a 10/10/0, P6b 15/15/0, P7 19/16/3, P8 6/6/0, TOTAL 113/105/8 — matches Sol table exactly. r15 outline's wrong raws (12/11/19/16) corrected in `architecture-staged-outline-r16.md`. Source JSON never defective (stated). |
| A02 | CORRECTED | Distribution recomputed r16 from SELECTED Matrix rows: {7:1, 5:9, 4:7, 3:11}, `1×7+9×5+7×4+11×3=113`, 28 candidates. Recorded in addendum `checks.recomputed` + this handoff. r15 handoff's `9×5+17×4+9×3` withdrawn (sums to neither 113 nor 28). r15 handoff file itself untouched (superseded-for-explanation only). |
| A03 | CORRECTED | NEW `architecture-boundaries-validation-addendum-r16.json` (addendum, NOT replacement): input paths+SHAs; method pseudocode (§10 steps); recomputed 28/28, 20P/8S, raw113/unique105, per-package table; `unexpected_package_boundary_strings_count:0` (extras enumerated: none); `missing_literal_memberships_count:0`; `package_boundary_array_duplicates_count:0`; `candidate_boundary_arrays_exact_match:true` (strict ORDERED equality, no normalization); `package_primary_supporting_membership_exact_match:true`; roundtrip: re-derived-twice idempotent TRUE, stored=insertion-order vs rederivation=sorted → `byte_identical:false`, `semantic_set_equal:true` (distinguished, r15 arrays NOT modified, no forced PASS); Core-rule-equivalent ephemeral in-memory PROPOSED re-run on unmodified Core → 0 errors (labeled as only that, NOT formal PASS). Status PASS (all true recomputed). |
| A04 | CORRECTED | NEW `technical-prep-r16/contextlm-eq5-primary-note.md`: ar5iv v1 §4.2 (anchor S4.E5) re-read r16 (417,994 B, SHA `a568b7e1…`, uncommitted transport). Exact transcription `s*=argmax_s E_{x∼D}[R(τ(x;s))]` + paper's definitions (s = in-context instruction/skill doc; τ from Eq.4; R trajectory reward; "everything else fixed" = weights frozen) + loop semantics (training-split rollouts → proposer → development-split select → once on held-out test; assisted/self-evolution) + in-context (Eq.4–5) vs in-weights RL (Eq.6) distinction + Eq.4 relationship (verified, unchanged) + Eq.6/metrics untouched. NO fabrication (alttext + prose quoted). NOT `A04_PARTIAL` (accessible). Small prose patch, not redevelopment; NOT an Architecture section. |
| A05 | CORRECTED | Dedup reconciled r16 by Counter over Matrix bytes: P1−2 ("All benchmark deltas…"×2, "Day-only date."×2), P4−2 ("Day-only date."×3), P5−1 ("Day-only date."×2), P7−3 ("Day-only date."×4); 113−8=105. Recorded in addendum `dedup_breakdown` (strings + multiplicities) + outline-r16. r15's "P4−3/P5−2" withdrawn. |

## 4. Commits + terminal

- Content commit on `weekly/2026-W40-v2-work` (SHA in outer report); FF child of
  `109ddbddd…`, non-force push, remote readback verified.
- Final read-only checks per §5/contract-§97: HEAD/Tree, FF ancestry, allowed paths,
  reviewed main, State blob identical, Matrix/Selection/Coverage-r14/Boundaries-r15
  byte-identical, Gates/checkpoints unchanged, #562 separately OPEN (read, not edited).
- Terminal: `SOL_W40_R16_BOUNDED_DOCUMENTATION_REVIEW_REQUIRED`. NO Selection
  Acceptance, Stage transition, canonical Architecture, Human Gates, publication.
  Final HEAD/Tree, files, A01–A05, re-verification, Eq.5 results: outer report. STOP.
