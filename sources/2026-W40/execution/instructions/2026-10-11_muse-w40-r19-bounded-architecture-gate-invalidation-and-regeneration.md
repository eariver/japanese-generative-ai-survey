# Muse W40 r19 — Bounded official pending Architecture-Gate invalidation + Architecture-only regeneration

Status: `PREPARED_SOL_EXECUTION_REQUEST / R19_ARCHITECTURE_ONLY / HUMAN_APPROVAL_FORBIDDEN / STOP_AT_FRESH_HUMAN_REVIEW`
Date: 2026-10-11 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing work branch ONLY: `weekly/2026-W40-v2-work`
Expected exact Starting HEAD and Tree: **specified by outer Sol prompt AFTER this instruction commit**.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`.
Authoritative Sol review disposition: `sources/2026-W40/execution/reviews/sol-w40-r18-independent-architecture-audit-disposition-20261011.md`.
Human-supplied independent r18 verdict: `BOUNDED_REVISION_REQUIRED`, 7 adopted findings R18-F01..F07.
Source canonical r18 commit: `c81296e1598a68f2879ea32c90d731ef1f418047`.

## 0. Exact Safety Preflight, STOP on mismatch

Before any write: read remote W40 HEAD+Tree and main, require equal outer expected values and `afdb3df3faa20af3bb5798be429bba8dbd2100b1` respectively. Git checkout must be exactly same commit, clean tracked worktree; fetch + `merge --ff-only` permitted to catch up only if it reaches exact Start. No branch creation/rebase/reset/force. Verify State `ARCHITECTURE_ESTABLISHED`, next `ARCHITECTURE_REVIEW`, terminal `HUMAN_GATE_REACHED`; Selection & Architecture checkpoints `passed`, both Human Gates `pending` with null provenance, exception inactive, Draft pending. Existing `gates/review-index.json` must be missing or contain **zero** Human reviews; no approved Gate or prior Human decision. Confirm no concurrent W40 change and operator invalidation record sequence/state.

Verify prior accepted authorities **BYTE-FOR-BYTE** unchanged vs r18: Discovery37, Screening37, Evidence Cards35 (29 VERIFIED/6 PARTIAL), Views35, Materiality Ledger37, Completeness (LIMITED), canonical Candidate Matrix SHA256 `f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6`, canonical Candidate Selection SHA256 `b7d20be2fb273ba3c4a0ab66bb8818452591000805be90f9bcd75ce565bee225`, and `orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json` SHA256 `817075850a9390f735f9a9a4a35ebc9d391793b3ecd7907ba7d2308ebadfa678`. r18 Architecture SHA256 `d732aedadcd576e484a86fc25041090b426ac7de707e376ff3750842bf3a26af`, Summary `dc5f29de42f6590cc664b790190ee9a963402b5d51ec7d70a5d8fc2833548bcc`, Attention `70ac43bdd0da014009f99abaf3aff00db8bdfbd9e44940ba087abf4cb5949319`, State SHA256 `4292270c31638b39f4631e5aec5b249b7055e360b311969762c3ad31d9538fb4` should match exact current bytes.

If ANY identity/basis/Gate/permissions mismatches → **ZERO WRITES**, report expected vs actual, STOP. If no lawful operator invalidation can be proven, STOP without fallback. Core/schema/config/workflows/main/other edition/Issue #562 must never change. No Human review approval/rejection.

## 1. Official operator invalidation (not Human REQUEST_CHANGES)

Do **not** write to `production-state.json` or delete canonical Architecture/Checkpoint paths by hand. Use unchanged reviewed main `scripts/survey_human_gate_v2.py::invalidate_pending_gate` (or official equivalent operator CLI) with:
- `gate=ARCHITECTURE_REVIEW`;
- `regeneration_boundary=SELECTION_COMPLETE` (verified allowed in config);
- `operator_reference`: SHA-pinned Sol independent r18 audit-disposition document;
- `reason`: corrections R18-F02-F06 in canonical Architecture, R18-F01 derived source-summary erratum; 28-item selection and accepted upstream unchanged;
- `expected_work_branch_head` and `invalidated_commit_sha`: exact checked current checkout W40 HEAD.

The checked Core function validates the current Gate, records old State/inputs/SHA/commit, removes ONLY superseded Architecture ownership and downstream checkpoint authority, records `human_decision:false`, rewinds State to `SELECTION_COMPLETE` with 28-item Selection still `passed` and Architecture `pending`; it validates resumable agent-first state and restores previous local files on failure. Verify resulting operator record, its schema/source SHA anchors, state, and deletion list. **No synthetic Human Review Record**, no `request_architecture_revision`. Keep historical r18 commit bytes reachable; don't edit/overwrite old Git history.

Normal non-force commit and remote readback of the operator invalidation BEFORE generating new canonical Architecture. If remote moves, STOP (no speculative resolution branch).

## 2. Architecture-only new content, preserve official Selection

Do NOT run `scripts/run_selection_architecture_v2_interactive.py::run` to repeat both stages: it requires `EVIDENCE_REVIEWED` and would overwrite Selection/Matrix/input archive. Keep unchanged `candidate-matrix-v2.json`, `candidate-selection-v2.json`, `orchestration/v2/interactive/selection-architecture-input.json` (historical), Selection Checkpoint. From `SELECTION_COMPLETE`, generate ONLY the current canonical `architecture-v2.json`, then derive `architecture-review-summary-v2.json` by unchanged `survey_architecture_v2_base.build_architecture_review_summary` and `architecture-review-attention-v2.json` by unchanged Review Attention builder, with agent-first stage basis resolving actual accepted source paths. Use original r18 canonical as *historical model*, including identical 9 package IDs/memberships and 113 verbatim Candidate-boundary relationships. Write new bytes only once previous Core invalidation removed their singleton paths; stage-specific scratch material under `execution/` may be used.

**Seven bounded fixes, no wider rearchitecture:**

- **F02 AgentPerf/OpenTTS separation:** In P6b `purpose`, place single-user trajectory-based serving, 14 speculative configs, bandwidth roofline comparison under AgentPerf ONLY; TTFA objective measurement (50 English prompts, batch1, exclude first3 warm-ups, median, H200 default) belongs to OpenTTS ONLY. No cross-source attribution.
- **F03 Olmo/OpenTTS script chronology:** Delete “scripts temporal split with commit history as dated negative” from P6a Olmo `must_cover_requirements`. Under P6b OpenTTS require explicit `2026-09-30 blog promised future eval scripts; first confirmed repo eval scripts commit 2026-10-07T14:53:41Z; NOT available within W40 Oct2 22:00Z cutoff` (as scoped to the inspected repo, not universal proof of non-publication anywhere).
- **F04 ContextLM dispatch ambiguity:** Remove the unexplained `dispatch` tail from ContextLM must-cover; require expert routing/dispatch solely as an Olmo MoE technical mechanism in the Olmo line.
- **F05 OpenTTS scripted-availability ambiguity:** Replace `Spaces app + scripts` with clear app/benchmark available in W40 and **eval-script future as-of-Sep30** vs verified Oct7. Preserve macro English WER, multilingual CER, RTFx, TTFA, SIM, human-preference-not-measured.
- **F06 explicit draft binding:** Strengthen exact P6a/P6b `must_cover_requirements` with factual scope/denominators and source references: ContextLM Eq.3 prefix reuse FLOPs vs latency, SCR/BCP relative gains and mutually distinct baselines, skill-evolution Eq.5 (fixed model weights; train/dev/held-out) vs Eq.6 RL parameter updates (fewer than 2 successes => efficiency term 0 only); Olmo-core expert parallel/distributed mechanisms and **47B measurement vs 1.2T routing vs 2.38T capacity** non-equivalence, MXFP8 B300×4 +21% and 103→95 GiB vendor settings, negatives; AgentPerf bandwidth theoretical roofline (NOT no-spec baseline) and local single-user/production-concurrent distinction; OpenTTS measurement protocol + commit history; RL Hub framework tag pin != taskset revision pin. Distinguish observed/publisher numbers and unretrieved appendices/reports, avoid creating new fact claims. Bind technical details to `execution/technical-prep-r15/p6a-deep-draft.md`, `p6b-deep-draft.md`, and `execution/technical-prep-r16/contextlm-eq5-primary-note.md` in appropriate review-packet method/evidence map, not unsupported keywords.
- **F01 Review Summary false stale limitation:** unchanged Core's `build_architecture_review_summary` mechanically copies `profile-completeness-v2.json` legacy `AstaBrief/AutoSynthData ... TIME_UNRESOLVED`. DO NOT hand-edit accepted Completeness, generated Summary or Attention. Create `execution/reviews/w40-r19-architecture-review-surface-erratum.md`, tie SHA of new Summary and source immutable Completeness, explicitly state resolved original issuer blog JSON-LD article times (15:19:50.340Z & 04:01:31.290Z respectively) vs still-unverified first model/code/dataset release dates; canonical HOLD is due #562 authority mismatch, not an old timestamp. Add it as MANDATORY first-read part of new Human Gate review packet; acknowledge the derived Summary continues to contain stale historical limitation.
- **F07 execution index:** update top “Current Authority” block (State SHA + lifecycle `ARCHITECTURE_ESTABLISHED`, next `ARCHITECTURE_REVIEW`, terminal `HUMAN_GATE_REACHED`) after the new gate actually materializes. Label prior `EVIDENCE_REVIEWED` and old State SHA as HISTORICAL instead of “Current”. Keep append-only audit trail in later sections.

All other P1–P5/P7/P8 package purposes/requirements, 28 IDs and 113 literal boundaries remain preserved. 4 HOLD (including AstaBrief/AutoSynthData), 3 REJECT remain outside packages; no noncanonical supplements as regular book content, no separate PDF/release. No arbitrary page cap; concrete technical depth is required.

## 3. Validation, stage and new Human Gate

After regeneration, run schema checks, frozen `survey_architecture_v2.validate_architecture`, `build_architecture_review_summary` equivalence, review-attention validation; separately recalculate 28 SELECTED = 20 PRIMARY+8 SUPPORTING, package IDs/membership, all 113 original literal relationships/105 unique strings from original Matrix to regenerated Architecture, zero HOLD/REJECT contamination. Compare old→new canonical Architecture at JSON pointers; allowed changes ONLY F02–F06 and their clearly justified editorial dependencies, plus newly derived Summary/Attention/checkpoints (must not quietly change unrelated package fields). Explicitly test that P6a/P6b method/scopes are preserved and not compressed.

Create NEW `execution/validation/architecture-stage-validation-r2.json` (do not overwrite r1), execute real agent-first Core stage validation `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED`, build checkpoint using original Core, then advance with checkpoint only after all checks PASS. New `orchestration/v2/checkpoints/SELECTION_COMPLETE.json` replacing the invalidated superseded singleton is permissible ONLY through official reattestation. Expected end: lifecycle `ARCHITECTURE_ESTABLISHED`, Selection+Architecture passed, pending Human Architecture and Preview Gates with null provenance, terminal `HUMAN_GATE_REACHED`. Old State/checkpoint/Architecture versions remain Git-reachable.

If useful run legacy `validate-state` diagnostically, but record **exact command, return code, stdout/stderr**, label historical legacy vs current agent-first checks; do not represent legacy as passed or edit shared Core as a workaround. Fail closed if governing agent-first validation fails.

Make ordinary existing-branch commits, non-force push with remote readback. Final deliverable: `execution/SOL_W40_R19_ARCHITECTURE_REVIEW_HANDOFF.md`, `execution/sessions/muse-w40-r19-20261011.md` (adjust to actual date), bounded changes/diff report, clear 7-finding status, proof of operator invalidation, new State/Architecture/Review Summary/Attention/checkpoint exact SHA256, Git HEAD/Tree, index correction, review-surface erratum and strong 28/113/105 evidence. Owner may review fresh Architecture; **do not record Human Gate decision, Draft/Freeze/Release**.

Terminal on success: `FRESH_HUMAN_ARCHITECTURE_REVIEW_PENDING / R19_SOL_INDEPENDENT_REVIEW_REQUIRED`; otherwise `SOL_REVIEW_REQUIRED_WITH_EXACT_BLOCKER`, no unauthorized workaround.
