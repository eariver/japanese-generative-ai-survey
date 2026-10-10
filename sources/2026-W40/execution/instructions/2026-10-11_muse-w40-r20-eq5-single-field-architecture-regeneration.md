# Muse W40 r20 — Eq.5 single-field official Architecture regeneration

Status: `SOL_BOUNDED_EXECUTION / ARCHITECTURE_ONLY_EQ5 / ZERO_CORE_WRITES / STOP_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`
Date: 2026-10-11 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W40-v2-work`
Exact starting remote HEAD + Tree: **specified in outer Sol instruction after this document is committed**.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`.
Sol decision: `sources/2026-W40/execution/reviews/sol-w40-r19-independent-audit-adoption-and-r20-scope-20261011.md`
Previous canonical Muse r19: `c26c983bff02245fffa5543fea8aa86291f80807`.
Target: `R19-F01` only in canonical Architecture; `R19-F02` was **already corrected by Sol** in `execution/index.md` before this task. Re-verify exact index value during preflight.

## 0. Mandatory exact preflight / zero-write abort

Before touching files, read-only verify remote W40 HEAD/Tree EXACTLY equal to the outer supplied values, remote main HEAD exactly `afdb3df3faa20af3bb5798be429bba8dbd2100b1`; clean worktree and checkout on exact existing W40 branch (no reset/rebase/force/new/fallback/repair branches).

Verify current production State raw bytes SHA-256 `c5cd881153c60f1e6a50743995fc0a68f22ebda901723a3eae38dc293d1d6ce6`, `ARCHITECTURE_ESTABLISHED`, next `ARCHITECTURE_REVIEW`, terminal `HUMAN_GATE_REACHED`, `selection=passed`, `architecture=passed`, all other pre-draft machine stages passed, `draft=pending`, `ARCHITECTURE_REVIEW` and `PUBLICATION_PREVIEW` Human gates both pending with null provenance, exception inactive. Confirm `gates/review-index.json` missing or zero actual Human reviews, no Human Gate approval/denial, no active exception.

Pin exactly current canonical Matrix SHA-256 `f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6`, Selection `b7d20be2fb273ba3c4a0ab66bb8818452591000805be90f9bcd75ce565bee225`, prior Architecture `305a42d6e66b03c6226f17c0e5bbf578c6672a2594425dbde50502f24174d0b9`, prior Review Summary `37ce43b2facdcf8839303a8a4e25a71f7f28a075ad6e97157670885106764d51`, Review Attention `70ac43bdd0da014009f99abaf3aff00db8bdfbd9e44940ba087abf4cb5949319`, current official Selection checkpoint `817075850a9390f735f9a9a4a35ebc9d391793b3ecd7907ba7d2308ebadfa678`, current Architecture checkpoint `71388dbcbe0156e8908066a4d78309e9159dfcfe5dec8a14a46e101f47551d3b`; verify accepted Evidence35, Views35, Discovery37, Screening37, Ledger37, Completeness, `profile-completeness-v2.json` SHA `f83b2d94d8ac4b89634e890ee6026dbc302c70741e38b822373ebc4bfb4632a1` unchanged. Ensure `execution/operator-invalidations/architecture-invalidation-0001.json` valid and present; new `0002` absent.

Verify index's current-state value is now the correctly fixed 64-char `c5cd881153c60f1e6a50743995fc0a68f22ebda901723a3eae38dc293d1d6ce6`. If remote diverged, a Human review appeared, supplied SHA mismatches, gate state changed, or exact existing branch cannot be used: **ZERO WRITES and STOP with expected vs actual**. No shared Core, scripts, schemas, config, workflow, main, issue, other editions, accepted upstream, Candidate Matrix/Selection, old r15-r19 audit and preparation files modified. Never fabricate or record Human `APPROVED`/`REQUEST_CHANGES`.

## 1. Official operator pending Gate invalidation: seq 0002

Use unmodified, reviewed-main `scripts/survey_human_gate_v2.py::invalidate_pending_gate` through its actual official CLI or exact function interface. Prior normal seq1 record must remain intact. Gate `ARCHITECTURE_REVIEW`; regeneration boundary `SELECTION_COMPLETE`; explicit nonempty reason `R19-F01 ContextLM Eq.5 verified status mislabeled UNVERIFIED; preserve 28 selected + 113 Boundaries`; `operator_reference` must name and SHA-pin the above Sol review disposition; `expected_work_branch_head` and `invalidated_commit_sha` must be the actual **outer exact starting W40 HEAD** (Sol docs-only commit), NOT Muse r19 canonical parent.

This is OPERATOR invalidation of a **not-yet-human-reviewed** pending Gate, `human_decision:false`. It must independently verify current exact Gate surface and SHAs, record superseded State/Architecture/Summary/Attention/Checkpoint refs, remove old singleton Architecture/Summary/Attention/`orchestration/v2/checkpoints/SELECTION_COMPLETE.json` via Core, and set State `SELECTION_COMPLETE`, Selection passed/provenance unchanged, Architecture pending/provenance null, Gates pending/null. Validate agent-first resumability and full record schema. On failure, abort/rollback, not manual repairs.

After operation, normal COMMIT and non-force PUSH to existing W40; remote readback exact HEAD/Tree, direct parent FF. This intermediate commit MUST precede any regeneration. Old accepted bytes and r19 canonical remain Git-reachable; no overwrite of invalidation record 0001. If any unexpected move/conflict, STOP.

## 2. Single-field Architecture-only regeneration

**Never run** `scripts/run_selection_architecture_v2_interactive.py` again: it requires `EVIDENCE_REVIEWED` and regenerates Selection. Use existing Core Architecture validator, derivation of Review Summary/Attention, agent-first stage path from `SELECTION_COMPLETE`. Use the exact r19 JSON as the historical baseline; do not alter any `candidate_selection`, IDs, 9 Package IDs, roles, 113 original boundaries, 105 unique strings, all package titles/purposes/thesis, other requirements, page plan, extensions or selected exceptions.

Allowed old→new JSON diff **only one scalar**:
`/packages/5/must_cover_requirements/1` (P6a ContextLM Eq.5/Eq.6).
Maintain its validated existing prefix unchanged and replace precisely the misleading trailing clause
`Eq.5 full update text UNVERIFIED beyond ar5iv sections 4-5 scope per technical-prep-r16/contextlm-eq5-primary-note.md.`
with
`Eq.5 exact optimization objective, variable definitions and fixed-weight training/development/held-out skill-evolution procedure VERIFIED against arXiv:2609.37725v1 §4.2 and execution/technical-prep-r16/contextlm-eq5-primary-note.md (in-context skill optimization, not Eq.6 parameter-learning RL); PDF bytes, figures, appendices B–F, code, unpinned repo revision and unquoted details remain UNVERIFIED.`
Nothing else. Use actual author/paper-scope evidence, no new claims or numeric edits. The **Equation itself is verified** (r16): `s* = argmax_s E_{x∼D}[R(τ(x;s))]`. Eq.5 optimizes in-context skill `s` with frozen weights; Eq.6 trains parameters. Unverified unrelated materials remain clearly bounded.

Build new `architecture-v2.json` from historical model, validate schema and Core `validate_architecture`; derive `architecture-review-summary-v2.json` via unchanged `build_architecture_review_summary` and Attention via unchanged builder. Require `READY_FOR_ARCHITECTURE_REVIEW`, preserve Human `null`, actual derived SHA basis and 28/113/105. Diff old/new must show exactly that ONE canonical Architecture field and no source-order/Boundary drift.

Critical: `architecture-review-summary-v2.json` again derives old accepted Completeness's `TIME_UNRESOLVED` sentence, an inherited factual inconsistency for the *hosted article* event. DO NOT hand-edit old Completeness, Summary or Attention. Create `execution/reviews/w40-r20-architecture-review-surface-erratum.md` (a successor) that explicitly binds the NEW Review Summary SHA-256 and unchanged Completeness SHA-256, quotes and corrects the stale sentence with issuer-blog JSON-LD AstaBrief `2026-10-02T15:19:50.340Z` and AutoSynthData `2026-10-02T04:01:31.290Z`, distinguishes article vs weight/code/dataset clocks, HOLD caused by separate Core #562 gap. **MANDATORY FIRST-READ** of the new Human Review packet. Keep prior r19 erratum immutable and historical; do not present its old Summary-SHA binding as current.

## 3. New Stage evidence, index accuracy, terminal Gate

Run actual Core schema/architecture/review/attention validators; new Stage `CORE_STAGE_CONTRACT` output under `execution/validation/architecture-stage-validation-r3.json` (do not overwrite r1/r2), source/claim and one-field diff evidence, agent-first `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED` checkpoint regeneration using only official Core methods, and normal non-force push.

After Stage SUCCESS, current State must be `ARCHITECTURE_ESTABLISHED / ARCHITECTURE_REVIEW / HUMAN_GATE_REACHED`, all pre-draft machine checkpoints `passed`, Draft and downstream pending, both Human Gates pending/null, exception inactive. Verify exact new SHA-256 of remote State. Update `execution/index.md` current State SHA line to this **new** true 64-character digest; do not reintroduce the 66-character bug. Preserve prior State hashes as clearly HISTORICAL, add terminal r20 index entry, preserve all prior Audit docs. Check that the interim docs-only Sol correction of R19-F02 was not lost.

Prepare `execution/SOL_W40_R20_ARCHITECTURE_REVIEW_HANDOFF.md` and session log `execution/sessions/muse-w40-r20-20261011.md` (actual date if different). Include exact start/intermediate/final SHA/Tree and parent chain, operator seq2 record + Stage r3, original/new one-field diff with pointer, 28/113/105 invariant result, new actual Architecture/Review Summary/Attention/State/Checkpoint digests, r20 erratum and correct index SHA, R19-F01/F02 fixed disposition, legacy diagnostic separately (legacy exit1 is not a new blocker), residual source bounds and two canonical HOLD omissions.

Last action is **STOP at fresh pending Human Architecture Review**, terminal `FRESH_HUMAN_ARCHITECTURE_REVIEW_PENDING / R20_INDEPENDENT_FOCUSED_REVIEW_REQUIRED`. No Human Gate decision, Draft, Freeze/Release, companion, Core changes, or new branch. If any official Core operation/validator fails, fail closed with exact blocker, no hand edits or alternative lifecycle transition.
