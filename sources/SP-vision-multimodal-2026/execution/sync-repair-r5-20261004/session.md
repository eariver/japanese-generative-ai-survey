
## Mid-replay finding (2026-10-04): SELECTION_COMPLETE boundary insufficient

- Authorized rewind to SELECTION_COMPLETE executed clean (4 Core-computed paths removed).
- Selection rationale-only edit applied (1 assignment) + `validate_selection` PASS.
- Architecture file rebuilt from HEAD base with P06/P09 sync + basis refresh + `validate_architecture` PASS.
- BLOCKER: surviving `EVIDENCE_REVIEWED.json` checkpoint pins the OLD selection SHA
  (`6112732c...`); edited file drifts → `validate_agent_state: [Stage Checkpoint artifact
  drift: candidate-selection]`. Every downstream Core step (summary build, advance)
  fails closed on this drift.
- Root cause: Core never supports post-checkpoint modification of checkpoint-bound files.
  The EVIDENCE_REVIEWED checkpoint can only be rebuilt from lifecycle EVIDENCE_REVIEWED,
  i.e. a deeper rewind boundary than the authorized SELECTION_COMPLETE.
- No further authority writes beyond the already-authorized staged edits; stopping for
  amended authorization (EVIDENCE_REVIEWED boundary, same machinery/protections) or
  stop-as-blocked. Prior exception NOT stretched implicitly.

## Close-out

- Rewind 1 (SELECTION_COMPLETE) clean. Replay revealed EVIDENCE_REVIEWED checkpoint drift
  (old selection SHA pinned); amended authorization to EVIDENCE_REVIEWED obtained;
  rewind 2 executed (4 Core-computed paths; agent_state CLEAN both times).
- Replay: matrix byte-identical re-derive; selection 112 carried + 1 rationale sync;
  checkpoint rebuild + advance; architecture P06/P09 sync + basis; summaries fresh;
  validation + checkpoint + advance → ARCHITECTURE_ESTABLISHED, r5 PENDING.
- Consistency audit PASS (stale 0 across 4 surfaces; scoped VM-D075 present).
- No Evidence/Completeness/Matrix semantic change; no Draft/TeX/PDF. See execution-report.md.
