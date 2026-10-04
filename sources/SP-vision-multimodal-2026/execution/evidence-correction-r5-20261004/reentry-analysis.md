# Re-entry mechanism analysis — evidence-correction-r5 (empirical, read-only probes)

Question: which formal Core mechanism moves DRAFT_COMPLETE → CANDIDATES_NORMALIZED
for targeted Evidence correction?

## Investigated mechanisms (all in frozen Core, all fail closed from DRAFT_COMPLETE)

1. `survey_human_gate_v2.request_publication_preview_revision` (local CLI +
   `request-publication-preview-revision` + bridge `REQUEST_PUBLICATION_PREVIEW_REVISION`):
   `_validate_gate_pending` requires lifecycle `RELEASE_CANDIDATE`. Current `DRAFT_COMPLETE`.
   PROBE 1 (this run, no writes): `HumanGateError: PUBLICATION_PREVIEW decision requires
   pending RELEASE_CANDIDATE Human Gate`. Reaching RELEASE_CANDIDATE requires
   reader-publication-validation (TeX/PDF) — explicitly forbidden this run (§16).
2. `survey_human_gate_v2.request_architecture_revision` (+ bridge counterpart):
   requires lifecycle `ARCHITECTURE_ESTABLISHED`. PROBE 2: `HumanGateError:
   ARCHITECTURE_REVIEW decision requires pending ARCHITECTURE_ESTABLISHED Human Gate`.
3. `survey_human_gate_v2.invalidate_pending_gate` (operator pending-gate invalidation):
   `_current_pending_gate` — `gate_at_state` maps only ARCHITECTURE_ESTABLISHED and
   RELEASE_CANDIDATE; DRAFT_COMPLETE has no pending gate. Additionally requires zero
   Human review records (r1–r4 + publication-r1 exist). PROBE 3 fail-closed.
   (Note: its ARCHITECTURE_REVIEW boundary allowlist DOES include CANDIDATES_NORMALIZED —
   the boundary is legitimate; only the invocation preconditions are unmet.)
4. Bridge transport (`survey_core_execution_bridge_v2`): calls the same functions as (1);
   identical guards. Transport adds nothing.
5. `advance_with_checkpoint` / orchestrator advance: forward-only
   (`record.from_state` must equal current lifecycle). No backward use.
6. Legacy `revise_special_interactive_evidence.py`: legacy `pipeline-state.json` track
   (SP-* Special), not Core v2 `production-state.json`. Inapplicable.

## Conclusion

No formal Core mechanism supports an Evidence-correction rewind from DRAFT_COMPLETE:
the DESIGNED cross-gate path assumes defects surface at Publication Preview
(RELEASE_CANDIDATE → recorded Human REQUEST_CHANGES with upstream boundary → rewind).
A factual Evidence defect confirmed pre-validation (DRAFT_COMPLETE) has no designed
re-entry path that simultaneously respects: no hand-edited state/checkpoints (§3),
no fabricated Human decisions (§14), no validation/TeX/PDF advance (§16).

## Recorded positions

- This is documented as a deferred Core process-gap candidate in `core-process-gap.md`
  (NOT fixed this run; shared Core untouched).
- Staged corrections (8 cards, canonical-validated) + replay plan + ledger are complete
  and authorization-independent; they are preserved for the authorized run.
- No state, checkpoint, gate, Matrix, Selection, Architecture, Evidence-store, Draft, TeX,
  or PDF byte was changed by this run. `git status` delta vs starting HEAD is exactly:
  prior-turn uncommitted bytes (untouched) + this run's new execution dir (untracked).
- Next step requires an explicit Human decision on HOW to authorize the rewind
  (Owner Exception vs go-forward-then-rewind vs stop-as-blocked). Asked via operator
  question; no worker-generated decision substituted.
