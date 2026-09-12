# Core v2 post-VALIDATED_DRAFT publication-surface revalidation — canonical worklog

Maintenance branch: `fix/core-v2-post-validated-draft-publication-revalidation-20260912`
Authority: `EXECUTION_AUTHORITY / SHARED_CORE_MAINTENANCE / INVESTIGATE_FIRST / FIX_GENERIC_REVALIDATION_GAP_IF_CONFIRMED / STOP_AT_HUMAN_FULL_CANDIDATE_REVIEW` (2026-09-12 JST)
Reviewed main: `658ae823987431e1f1098243dc2f88cfc0d4864a` / tree `63790316a41c7369a72063503695d30609291694`
W34 read-only fixture: `weekly/2026-W34-v2-work@f50d229162b7402c504c0978f72dab4b33052f5e` / tree `7d479840545094883bdd5b5273cdc86aa1f69b38`
Role: maintenance execution (Luna/Work equivalent); Sol/Human review separate, never claimed here.

## 1. Guards (fresh remote reads, pre-write)

1. remote `main` HEAD `== 658ae823...` — PASS
2. remote `main` tree `== 63790316...` — PASS
3. remote maintenance branch absent — PASS (created locally from exact reviewed main only after PASS)
4. remote W34 `f50d2291...` / tree `7d479840...` — PASS
5. W34 parent `96e0f14e...` — PASS

Recovery note: a prior local attempt was interrupted before any write (branch created locally, never pushed; no commits). Per recovery instruction all guards were re-verified from zero against remote source of truth, prior local state discarded (branch deleted + recreated, worktree removed + recreated).

## 2. Defect reproduction (fresh, read-only, disposable worktree at fixture)

Command (semantics exactly per instruction §5):

```text
survey_stage_validation_v2
  --state sources/2026-W34/production-state.json
  --artifact publication-candidate=sources/2026-W34/publication/v2/publication-candidate-v2.json
```

Result: exit 2, verbatim:

```text
Production State invalid before stage validation: Stage Checkpoint artifact drift:
publication-pdf; quality-regression-bundle; reader-manuscript; semantic-review; visual-review
```

Responsible call chain (reviewed-main bytes, identical on this branch):

```text
scripts/survey_stage_validation_v2.py:506 validate_stage
  -> :517 agent.validate_agent_state()                      [fails BEFORE :532 stage semantics]
scripts/survey_agent_control_v2.py:261 validate_agent_state
  -> :196 _validate_checkpoint_record  (for provenance key "validation")
  -> :227-230 per-artifact SHA comparison vs DRAFT_COMPLETE.json rows
        -> "Stage Checkpoint artifact drift: {name}"
```

Advance path equally blocked: `build_stage_checkpoint` (:626) and
`advance_with_checkpoint` (:682 + final :726 `validate_agent_state`) both gate on
`verify_agent_state_basis` (:532).

## 3. Investigation verdict: Case B — no sanctioned path exists

Traced control flow (not filename search) for every §6 concept:

1. `advance-stage` — forward-only; basis-blocked post-regeneration. ✗
2. Operator pending-gate invalidation (`survey_human_gate_v2.py:1097 invalidate_pending_gate`):
   `operator_pending_gate_invalidation_boundaries[PUBLICATION_PREVIEW] == []` → any
   boundary raises; plus explicit guard (`:1124-1126`) refuses when Architecture is
   approved (W34 is). Doubly blocked. ✗
3. Human-gate revision/supersede (`survey_human_gate_v2.py:725+` supersede machinery):
   requires a Human decision (nonexistent; generating one is prohibited). ✗
4. Historical `fix/core-v2-state-revalidation` (PR #323, merged 2026-08-22): 12-line
   workflow-file fix about State revalidation in a removed control workflow.
   Different concept (no checkpoint/publication authority). Not relevant. ✗
5. `revalidat*/rebind*/supersed*` sweep across scripts/schemas/config: all hits are
   stage-internal result revalidation (evidence runs vs tasks, draft vs packages).
   No post-VALIDATED_DRAFT checkpoint-supersession/publication-rebind object exists. ✗
6. No schema, config surface, workflow, or test defines publication revalidation
   authority. ✗

Conclusion: shared Core v2 design defect. Proceeding with generic bounded repair (Case B).

## 4. Repair design (generic, no W34 special case)

New immutable edition-local authority object, owned by agent control:

- Canonical singleton: `{source_root}/publication/v2/publication-surface-revalidation.json`
  (+ schema `schemas/publication-surface-revalidation.schema.json`).
- Operation `revalidate-publication-surface` (new `survey_agent_control_v2.py`
  subcommand): VALIDATED_DRAFT-only, arch-approved, preview-pending-without-
  provenance, freeze/release-pending, exception-inactive; else fail closed.
- Prior basis defaults to state `checkpoint_provenance["validation"]` record
  (immutable; never rewritten).
- Supersede-eligible rows: prior-record rows with paths under `{source_root}/publication/`
  or the profile `{survey_root}/` (reader surface). Every other checkpoint-bound byte
  must match exactly (full basis check minus superseded roles) — upstream smuggling
  impossible. Stale candidate files tolerated-but-ignored (never trusted; they fail
  natural validation until rebuilt).
- New bytes proven legitimate by re-running EXISTING validators over them:
  manuscript semantics, bundle DETERMINISTIC checks, semantic/visual review family
  completeness + fidelity depth, PDF preflight. Prose semantics stay ChatGPT-owned
  via the review records (same trust model as `build_candidate`).
- Record binds (§8.5): prior checkpoint ref, superseded rows old→new SHAs (+byte
  counts), preserved-upstream row SHAs, reason_class enum (`REVIEWED_CORE_CHANGE`
  only; anything else rejected), executor, recorded_at, core/contract identity,
  deterministic validation summary. Absent→create; present+valid→refuse;
  present+invalid→replace with embedded prior-record chain (history preserved
  inside the chain; old checkpoint file never touched).
- Checker change (only firewall touch): `_validate_checkpoint_record` consults the
  active VALID record — superseded (name,path) rows verify against record SHAs,
  everything else unchanged. Same consultation refactored into ONE shared helper
  used by both agent-control and `survey_stage_validation_v2._prior_artifacts`
  (currently duplicated drift logic). No `--force`-equivalent; no global weakening.
- Post-repair chain works unmodified: `validate_agent_state` → stage validation →
  `advance-stage` → RELEASE_CANDIDATE.

## 5. Implementation log

Changed paths (implementation):
- `schemas/publication-surface-revalidation.schema.json` (new): revalidation record contract.
- `scripts/survey_agent_control_v2.py`: `REVALIDATION_*` consts; `resolve_active_publication_revalidation()` (live re-derivation, fail-closed); `_verify_preserved_provenance()` (all-provenance upstream verification); `revalidate_publication_surface()` (entry/boundary/preserved/QA/record); `revalidate-publication-surface` CLI; `_validate_checkpoint_record` consults the active record for bound-prior rows only; `validate_agent_state` resolves once and passes down (no duplicated errors).
- `scripts/survey_stage_validation_v2.py`: `_prior_artifacts` takes cfg and applies the same active-basis consultation for the bound prior record only.

Design notes: no state-schema change, no state mutation by the operation, no new workflow, no new Human Gate. State file untouched; active basis discovered via canonical record path. Replace-if-invalid carries the embedded prior chain; old checkpoint files never rewritten.

## 6. Test log (T1–T13 per instruction §11)

New suite `tests/test_survey_publication_revalidation_v2.py`: 13/13 PASS on first green run (26.5 s), using synthetic VALIDATED_DRAFT fixtures built through the REAL builders (manuscript/bundle/reviews) so all QA validators execute genuinely:
- T1 legitimate regen → revalidate succeeds, state valid afterward (pre-repair drift asserted first)
- T2 old checkpoint bytes byte-identical before/after
- T3 evidence mutation → `upstream artifact drift` fail-closed
- T4 architecture byte mutation → fail-closed
- T5 draft mutation → `upstream artifact drift` fail-closed
- T6 bundle FAIL check → QA fail-closed
- T7 candidate + PDF mutation → `validate_candidate` raises
- T8 record new SHAs == live files, prior SHAs == old bytes
- T9 preview-approved state → forbidden
- T10 freeze-resolved state → forbidden
- T11 weekly viability + full chain to RELEASE_CANDIDATE (stage validation PASS, advance PASS, preview still pending)
- T12 special-layout survey_root genericity + no-edition-literal tripwire on new code
- T13-shape automated chain on generic fixture (5-drift-error signature pre-repair → full advance post-repair)

T13 full-fidelity disposable proof on exact W34 fixture copy (`f50d2291`, local-only, never pushed):
- `revalidate-publication-surface` → record created
- `validate_agent_state` → PASS (was 5 drift errors)
- `survey_stage_validation_v2 publication-candidate` → PASS (`VALIDATED_DRAFT → RELEASE_CANDIDATE`)
- `advance-stage` → `RELEASE_CANDIDATE`, `next_action PUBLICATION_PREVIEW`, `HUMAN_GATE_REACHED`
- post-advance `validate_agent_state` → PASS; `DRAFT_COMPLETE.json` byte-identical; arch approved, preview pending
- Real W34 branch untouched (remote HEAD still `f50d2291`; proof confined to disposable worktree, since removed).

## 7. Validation / docs / PR / freeze / audit / CI

- Focused suite 13/13; neighboring suites 29/29; full contract 332 tests 0 failures (6 legacy skips); compile clean.
- Docs: authority.md §8 mechanism paragraph; worklog §6 entry; this worklog.
- Draft PR: #489 (open, draft, unmerged).
- Pre-freeze review: 7 paths (2 implementation, 1 schema, 1 test, 3 docs); no W34 artifacts; no workflow drift (7 intact); authority prose matches implementation.
- Freeze: the head resulting from committing this worklog finalization (recorded in PR #489 metadata, not in-tree). No tree mutation after freeze.
- Seven-point audit: PR #489 audit metadata/comment (outside the frozen tree). Exact-head CI: PR checks on the frozen head.
