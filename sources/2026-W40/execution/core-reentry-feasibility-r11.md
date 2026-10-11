# W40 r11 Core re-entry feasibility — post-EVIDENCE_REVIEWED upstream amendment (read-only verdict + staged plan)

Status: STAGED_R11 / READ_ONLY_VERDICT / NO_CORE_CHANGE / NO_STATE_CHANGE
State (verified this run): EVIDENCE_REVIEWED; next_action stage:selection;
checkpoints discovery/screening/evidence/materiality/completeness = passed,
selection/architecture/draft/validation/publication_preview/freeze/release = pending;
human_gates architecture_review/publication_preview = pending, provenance null;
terminal_reason null. Reviewed main afdb3df3faa20af3bb5798be429bba8dbd2100b1.
Core files read (NOT edited): scripts/survey_production_v2.py (transition_state),
scripts/survey_human_gate_v2.py (invalidate_pending_gate, _current_pending_gate),
config/survey-production-v2.json (stage_plan, gate_at_state, invalidation boundaries).

## 1. Verdict: NO lawful frozen-Core route exists ⇒ CORE_REENTRY_CONTRACT_GAP

Three independent locks, each sufficient to block:

1. `transition_state` (survey_production_v2.py:935-952) permits EXACTLY one forward
   step (`target_index == current_index + 1`), else
   `non-monotonic transition refused`. There is NO backward transition
   (EVIDENCE_REVIEWED → CANDIDATES_NORMALIZED) and no upstream-checkpoint rewrite
   operation. Manual State rewind is forbidden by contract and would break
   checkpoint-provenance binding.
2. `invalidate_pending_gate` (survey_human_gate_v2.py:1103-1133 + 364-409) cannot
   operate at EVIDENCE_REVIEWED:
   - `_current_pending_gate` resolves the pending Gate via
     `orchestration.gate_at_state`, which maps ONLY ARCHITECTURE_ESTABLISHED →
     ARCHITECTURE_REVIEW and RELEASE_CANDIDATE → PUBLICATION_PREVIEW. At
     EVIDENCE_REVIEWED it raises `current lifecycle 'EVIDENCE_REVIEWED' has no
     configured pending Human Gate`.
   - Even if reached, it requires `terminal_reason == HUMAN_GATE_REACHED`
     (actual: null) and, for ARCHITECTURE_REVIEW, `machine_checkpoints.architecture
     == passed` (actual: pending). Architecture checkpoint is pending by design
     (Selection not yet complete), so the "pending-Gate invalidation" path Sol r10
     already ruled out remains closed.
3. `stage_plan` forward path EVIDENCE_REVIEWED → SELECTION_COMPLETE
   (handler stage:selection, checkpoint selection) consumes the CURRENT accepted
   upstream as-is; it provides NO upstream-supersession semantics. Running Selection
   now would either (a) enshrine the now-stale TIME_UNRESOLVED HOLDs, or
   (b) silently contradict accepted Evidence/Views/Ledger — both unlawful.

Therefore: Accepted Discovery 37 / Screening 37 / Evidence 35 (set 0a62346f…) /
Views 35 (file 51887616…/set 1effd744…) / Materiality 37 rows / Completeness and the
EVIDENCE_REVIEWED checkpoint MUST stay frozen until a reviewed Core enhancement or a
separately authorized edition-local rebuild contract exists. This unit changes NONE
of them. Label: CORE_REENTRY_CONTRACT_GAP (confirmed, not hypothesized).

## 2. Precise impact IF Sol authorizes adoption (Plan B) — what would need new SHA-indexed versions

All of the following are DESCRIBED here, NOT executed:

- Discovery: 2 records (`w40-hold-astabrief-20261002`, `w40-hold-autosynthdata-20261002`)
  need amended locator/refs (add HF org article URIs as primary article-event
  authority with JSON-LD clocks; keep allenai.org + Gym records as related, not
  replaced) → new `discovery-accepted-v2.json` version + checkpoint re-attestation.
- Screening: 2 rows INSPECT→KEEP (article-event eligibility proven) with rewritten
  rationales distinguishing article event from weight/code release.
- Evidence: 2 tasks (`evidence:2026-W40:7609eae99dabda8b`,
  `evidence:2026-W40:ba72657afb68a868`) need re-consumption records (article body
  method/benchmark extraction already staged in r11 ledger/counterfactual, but must be
  re-run through Core Evidence builders) → new evidence-accepted set SHA + 2 Card
  updates (AstaBrief: Apache-2.0 weights / cc-by-nc-4.0 data / 2025-baseline caveats;
  AutoSynthData: method-only, Gym distinguished, gate/limit table).
- Views: 2 views HOLD→MATERIAL with rewritten editorial content/authority.
- Materiality ledger: 2 rows HOLD→MATERIAL with source-specific rationales
  (article-event clock + method substance + release-absence caveats).
- Completeness: re-validation (task bindings unchanged in count; rationales updated).
- Candidate Matrix + Selection package: 35-row matrix staging rebuild (frozen-derived),
  proposal 35 assignments 28→30 SELECTED, dossier revision (P6a extension), Core
  `validate_selection` preview re-run — all as NEW staged versions, old SHAs preserved
  in lineage.
- Checkpoints needing supersession under any lawful design: evidence, materiality,
  completeness (re-attestation with old-SHA lineage); State stays EVIDENCE_REVIEWED
  throughout (NO backward transition; the amendment is a same-state upstream
  supersession, not a rewind).

## 3. Minimal reviewed Core enhancement proposal (NOT implemented)

A narrow, review-gated "pre-Architecture upstream supersession" contract, e.g.:

- New Core operation `supersede_upstream_at_evidence_reviewed` (or equivalent),
  callable ONLY when: lifecycle == EVIDENCE_REVIEWED; selection/architecture pending;
  human_gates pending with null provenance; terminal_reason != HUMAN_GATE_REACHED;
  Sol scope adjudication (SCOPE_CHANGE_REVIEW_REQUIRED) recorded; regeneration
  boundary ∈ {CANDIDATES_NORMALIZED, EVIDENCE_REVIEWED}.
- Guards (exact SHA/byte/branch): caller supplies `expected_work_branch_head`,
  `base_accepted_SHAs` (old discovery/screening/evidence/views/ledger/completeness),
  `authority_diff_allowlist` (only the affected record/row/task/view IDs above);
  Core verifies: work-branch head matches; base SHAs equal current checkpoint
  provenance; builder reruns are deterministic (double-build identical); new
  artifacts carry `supersedes: <old-SHA>` lineage and old bytes stay reachable;
  validators (evidence/materiality/completeness) PASS on new versions; State
  lifecycle UNCHANGED, history appended with `supersession` (not a transition).
- Alternatively (no Core change): a Sol-authorized, Human-visible "edition-local
  rebuilding contract" executed via the operator bridge as a bounded ADVANCE_STAGE
  variant with the same guards — but this STILL needs Human/Core review because
  current Core has no such variant; do NOT invent one unilaterally.
- What is explicitly NOT proposed: generic backward transitions, manual State edits,
  pending-Gate invalidation misuse, synthetic Human reviews, or shared-Core hotfix
  in this unit.

## 4. Safe execution plan (for Sol approval; NOT executed now)

1. Sol records r11 scope adjudication (adopt Plan B / Plan A-with-rewritten-HOLDs /
   reject-with-reasons).
2. Reviewed Core maintenance lands §3 (or an equivalent authorized contract) on main
   via the normal Core review path (separate from W40 production).
3. A new bounded Muse run (r12 or named re-entry run) with an exact outer
   Starting SHA/Tree re-reads the r11 ledger/counterfactual as INPUT, regenerates
   ONLY the §2 allowlisted artifacts deterministically, and stops at Sol Evidence/
   Materiality re-review — still EVIDENCE_REVIEWED, still no Selection acceptance.
4. Sol re-reviews upstream deltas (old-SHA vs new-SHA diff), then authorizes Selection
   continuation (EVIDENCE_REVIEWED → SELECTION_COMPLETE) on the new basis.

Residual: until (2) exists, ANY canonical upstream edit — however small or well-meant —
is unlawful, including "just fixing two HOLD rows". This unit performs none.
