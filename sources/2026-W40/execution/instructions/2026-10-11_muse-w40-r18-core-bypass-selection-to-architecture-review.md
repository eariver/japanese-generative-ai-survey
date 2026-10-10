# Muse W40 r18 — Authorized 28-item ordinary Selection → Architecture Review (Core #562 separate)

Status: `SOL_EXECUTION_AUTHORITY / EXISTING_W40_ONLY / BOUNDED_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`
Existing work branch ONLY: `weekly/2026-W40-v2-work`
Exact starting SHA + Tree: supplied by outer Sol handoff AFTER this file is committed.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`.
Sol route correction/approval: `sources/2026-W40/execution/reviews/sol-w40-plan-a-28-item-forward-continuation-20261011.md`.
Old Core problem: #562 / CV2-DM-022; **separate task**, NOT a blocker for this scoped 28-item forward route.

## 0. Safety / mandatory guards

Start entirely read-only. Compare exact remote existing W40 HEAD+Tree to outer SHA+Tree; remote main HEAD to `afdb3df3faa20af3bb5798be429bba8dbd2100b1`; state blob and checkpoint authorities to prior accepted history. Confirm `EVIDENCE_REVIEWED`, next `stage:selection`, Selection/Architecture pending, Human Architecture and Preview Gates pending with null provenance, exception inactive. Verify actual byte SHA of Matrix r10 `f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6`, Selection r13 `dc0247781b0401e62eb8b17980050769b743f2aa313ffda3f5b5704235db0cb1`, Completeness `f83b2d94d8ac4b89634e890ee6026dbc302c70741e38b822373ebc4bfb4632a1`, Ledger `ce63f3a950a0267b03dd39a4f94016f2e3f39038783d48314e0f1e8a770bdf05`; prior accepted Discovery37/Screening37/Evidence35/Views35 and Gate/provenance SHA unchanged.

ANY mismatch ⇒ ZERO WRITES and return expected/actual. No new branches/fallback, reset, rebase, force, synthetic Human decisions. No shared Core/schema/config/workflow/main/other-edition changes; no Evidence/Views/Materiality/Completeness/Discovery/Screening mutation. No Issue changes. No unsafe custom state JSON edits or manual checkpoint spoofing.

## 1. Ordinary 28-item Selection

Authoritative review-only inputs:
- `execution/selection/selection-preview-r13.json`
- `execution/selection/candidate-matrix-r10-staging.json`
- `execution/selection/selection-validation-r13.md`
- `execution/reviews/sol-w40-plan-a-28-item-forward-continuation-20261011.md`
- `execution/SOL_W40_SELECTION_COMPAT_REVIEW_HANDOFF-r12.md`.

Preflight: validate **actual** Selection r13 with frozen Core `validate_selection` and repository schema (do not weaken or mock). Verify counts 35 = 28 SELECTED(20 PRIMARY/8 SUPPORTING) + 4 HOLD + 3 REJECT, explicit ID/usage/roles, Matrix and accepted source hashes; no shadow fallback.

Under normal existing Core stage `EVIDENCE_REVIEWED → SELECTION_COMPLETE`, materialize canonical `candidate-matrix` / `candidate-selection` as expected by the Action Spec/Checkpoint validation. Stage Selection through approved normal Orchestrator/Operator Bridge and exact checkpoint attestation; **not** by treating the staging preview path as already canonical. Confirm State transition only via real `survey_production_v2.transition_state` / official bridge after passing Core validators. If canonical contents require a different wrapper/path/identity, investigate and use only existing Core builder validated mechanism; on incompatible contracts STOP, do not rewrite accepted Authority or create a validator bypass.

State after successful stage should be `SELECTION_COMPLETE` with exact pinned selection checkpoint and unchanged old accepted evidence.

## 2. Build substantive Architecture, reach Human review

Using the canonical Selection and the previously independently audited 28 mappings, author a **real**, sufficiently developed issue Architecture:

- `execution/architecture-coverage-r14.json`, `architecture-boundaries-r15.json`, `architecture-boundaries-validation-addendum-r16.json`, `architecture-boundaries-roundtrip-digests-r17.json`, `architecture-staged-outline-r16.md`.
- P1 frontier; P2 reasoning; P3 tools/decision; P4 DevDay; P5 safety; P6a ContextLM+Olmo-core systems/method; P6b AgentPerf+OpenTTS+RL Hub; P7 multimodal/serving; P8 limited digest. P6a+P6b share canonical `WEEKLY:training-eval-infra` role; no fake roles.
- 28 IDs EXACT, 20 PRIMARY and 8 SUPPORTING; preserve all 113 original `remaining_boundaries` literal memberships in each destination `boundaries` array (105 unique across packages). Include meaningful, specific thesis/goals and must-cover items for all selected candidates; correct exact package IDs/roles, source claims and attribution. Build independently valid page/resource plan rather than placeholder fields or a small-page-count cap.
- Deep staged source prose: `execution/technical-prep-r15/p6a-deep-draft.md`, `p6b-deep-draft.md`, `execution/technical-prep-r16/contextlm-eq5-primary-note.md` and accepted independent audit constraints. Reviewer must be able to determine from Architecture whether methods/comparisons/limitations are substantive, not mere buzzwords.
- AstaBrief/AutoSynthData are **HOLD**, `architecture_usage:NONE`; their noncanonical supplemental research stays completely outside official Architecture packages, reader manuscript and ordinary publication. Preserve original hosted timestamps as a note, do NOT claim they were out-of-window. No second official PDF, appendix or automatic publication companion.

Create canonical `architecture-v2.json`, `architecture-review-summary-v2.json`, and architecture-review-attention through existing Core/Stage flow, with all Core schema/validators and checkpoint attestation **actually PASS**. Do not reuse prior placeholder in-memory validation as fresh substantive acceptance.

Proceed through `SELECTION_COMPLETE → ARCHITECTURE_ESTABLISHED` via standard legal Core stage only after each artifact/validation satisfies the unchanged reviewed main. If Core requires canonical package name/number constraints differing from staged 9 editorial groups, adapt editorial grouping without altering 28/113 mappings or inventing schema roles; if impossible report and STOP for Sol.

## 3. Stop and deliver fresh Human Architecture Review

Stop immediately when `ARCHITECTURE_ESTABLISHED`, machine checkpoint `architecture:passed`, new review summary/attention artifacts and Human Architecture Gate `pending` ready. Human decision MUST stay absent (`null` provenance). No Human approval/rejection fabrication, Draft, publication candidate, Freeze, Release, Core repair, or external supplement.

Produce exact reviewer-readable packet with real target paths, SHA-256/commit refs, per-package 28 ID mapping, 113 Boundary exact check, depth checklist, accepted prior staging and explicit two-HOLD omission disclosure. Include factual risk that this 28-item official W40 temporarily omits two technically MATERIAL in-window announcements awaiting Core #562 — noncanonical notes are NOT a published supplement. A Human may reject Architecture on editorial sufficiency, but no hidden bypass of Core rules is permitted.

Terminal: `FRESH_HUMAN_ARCHITECTURE_REVIEW_PENDING` on success; otherwise `SOL_REVIEW_REQUIRED_WITH_EXACT_BLOCKER`. Use only normal commits, non-force pushes on existing W40 branch; final readback HEAD/Tree, changed paths, exact parent chain, reviewed main/state/checkpoints, no modification of prior accepted upstream. Mandatory no new branch, no force/rewrite.

## 4. If gate or stage is blocked

Fail closed. Precisely explain validator contract, expected/actual hashes, and smallest *edition-local* fix if any; never switch to Core maintenance because of a guessed blocker. Do not authorize an unreviewed Core patch, manual checkpoint manipulation or a misrepresented supplement. Await Sol's targeted remediation instruction only if genuine blocker is reproduced.
