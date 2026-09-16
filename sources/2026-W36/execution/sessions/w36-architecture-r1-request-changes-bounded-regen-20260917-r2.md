# Survey Production session — w36-architecture-r1-request-changes-bounded-regen-20260917-r2

Issue: `2026-W36`
Started: `2026-09-17T00:50:00+09:00 JST`

## Starting authority

- Branch: `weekly/2026-W36-v2-work`
- Exact Starting SHA: `d30949b0ba9d892505d9f2c5100da57171e273f1` (remote HEAD/tree verified read-only pre-write; parent `0295bd08`; main `5acbff85`/tree `451fd7c6` + Production Line `774dd39a`/tree `cd46a6f7a` guards PASS)
- Execution contract: Human/Sol review authority supplied by execution request (r1 `REQUEST_CHANGES`, boundary `SELECTION_COMPLETE`, RC-1 + RC-2)
- Human decision: `REQUEST_CHANGES` (r1, imported authority; not Muse-produced); regeneration boundary `SELECTION_COMPLETE`
- State at start: `ARCHITECTURE_ESTABLISHED` / `ARCHITECTURE_REVIEW` / `HUMAN_GATE_REACHED`, Architecture Review pending; Selection r1 authority 18/1 (SHA `735b1f5c`, matches r1 gate basis)
- Reviewed `main` / Production Line: `5acbff85` / `774dd39a` (both untouched throughout)

## Actions actually performed

- Recorded r1 `REQUEST_CHANGES` via canonical `survey_human_gate_v2.py request-architecture-revision` (revision 1, reviewed `0295bd08`, boundary `SELECTION_COMPLETE`; reviewed-by Human Owner; reviewed-at `2026-09-16T15:51:32Z`; instruction file as review-reference). Machine record: `gates/reviews/architecture-r1.json` + review index. State returned to `SELECTION_COMPLETE`; r1 Architecture triple + SELECTION_COMPLETE checkpoint invalidated by the machinery.
- Verified Selection/Matrix byte-identity post-recording (`735b1f5c` / `6eeae3f2`, unchanged).
- Confirmed the RC-1 defect in r1 thesis (`moved to own` in architecture/summary/dossier; packages already pledge-bounded).
- Regenerated Architecture ONLY with RC-1 thesis fix (preferred wording); identical assignments, 6 packages/membership/roles/order/goals; Selection/matrix bytes never rewritten (verified identical post-regen).
- Rebuilt review summary via the runner-identical canonical path (same builder + basis override; READY_FOR_ARCHITECTURE_REVIEW) + attention via canonical builder (byte-identical to r1, as expected from unchanged upstream); `architecture-check` PASS.
- Verified no stale completed-acquisition language in regenerated surfaces; corrected thesis present in architecture + summary.
- Stage-validated (`architecture-stage-validation-r2.json` PASS) + advanced to `ARCHITECTURE_ESTABLISHED` / `ARCHITECTURE_REVIEW` / `HUMAN_GATE_REACHED`.
- RC-2: preserved r1 pre-gate file byte-identical; added provenance classification note; r2 dossier cites only imported authority + Worker/Operator validation, never the worker file as Sol review.
- Updated r1 shell (decision recorded), created r2 shell PENDING + r2 12-element dossier, r2 checkpoint, session/index updates. No Draft generated. No upstream rerun. No new research. No Core repair activity.

## External handoff

- None. No Drive use. No connector search/install.

## Deterministic execution transport

- Direct exact local CLI throughout. No force push, reset, rewrite, fallback/alternate branches.

## Deviations / failures

- None. One tooling note (not a Core defect): standalone `review-summary` CLI fails post-rollback on historical screening state-sha basis; the runner-identical path (same builder under the runner's basis override) succeeds — used for r2 summary. No Core repair; edition-local procedure only.

## End state

- Lifecycle: `ARCHITECTURE_ESTABLISHED`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `ARCHITECTURE_REVIEW` (Human r2 decision only)
- Review target: r2 Gate inputs + dossier at the exact pushed commit recorded in `architecture-r2.md`
- Session status: `COMPLETE_AT_GATE`
