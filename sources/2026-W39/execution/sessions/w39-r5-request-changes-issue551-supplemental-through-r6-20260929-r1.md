# Survey Production session — w39-r5-request-changes-issue551-supplemental-through-r6-20260929-r1

Issue: `2026-W39` (+ GitHub Issue #551)
Started: `2026-09-29T00:44:43Z` (remote preflight guards PASS; local fast-forwarded to remote `aa4c1b68af3983bc5ff40f3b1749afb68d551eb4`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `aa4c1b68af3983bc5ff40f3b1749afb68d551eb4` / tree `b554e386684b712bc7981a51c356835a83a4bf7d` (all guards PASS: request in commit, main/frozen verified, r5 shell binds r5 authority with PENDING)
- Reviewed remote `main`: `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`
- Production Line: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- Execution contract: `execution/requests/sol-w39-publication-preview-r5-issue551-supplemental-request-changes-through-r6-20260929.md`
- Human decision in contract: Publication Preview r5 `REQUEST_CHANGES`, boundary `DRAFT_COMPLETE` (explicit Human direction via Issue #551 thread, incl. Sol residual + supplemental audit comments, all read in full)
- Lifecycle at start: `RELEASE_CANDIDATE` (r5-pinned, consistent); r5 decision PENDING
- No Drive access; no connector searched/installed. No merge commit; no reset/rebase/force/squash.

## Actions actually performed

- Recorded Human Publication Preview r5 REQUEST_CHANGES via canonical `request-publication-preview-revision` (rev 5, boundary DRAFT_COMPLETE, reviewed `342adad3`, wall-clock reviewed_at); publication-local invalidation only; Architecture approval preserved; state returned to DRAFT_COMPLETE. (One timestamp incident: future reviewed_at estimated from JST arithmetic instead of measured; Core fail-closed refusal worked; tree restored and re-recorded with measured wall clock. No committed bytes affected.)
- Repaired the two blocking findings, wording-only, invariants preserved:
  1. Source-boundary contradiction: 99-source-notes Community observation boundary now states the general context-only rule PLUS the narrow source-role+binding-specific exception (official first-party post explicitly cited in body for its exact announcement fact; ledger membership alone never elevates; independent/community rows stay context-only). Ledger header carries the same exception. Raw rows/URLs/timestamps/classes/roles/counts untouched.
  2. Claude Code date: 99-source-notes now reads Sep 25; full-surface sweep (Claude Code/graceful stop/9月23日/9月25日/both cite keys) confirms Sep 25 consistently for the behavior-change event; tier secondary caveat unchanged.
- Regression guard: 4-corpus search over final TeX (compound-aware bad total 0); r5 PASS items intact (ART, Cursor, Opus typical-workload + 最大2.5倍, DolphinBench v1/v2, Claude Code binding); terminology repairs intact.
- Final-byte seed-external reread of all changed lines post-edit: no new defects, no new typos. New generic defects: 0.
- Regenerated publication chain from repaired TeX: manuscript (31/31) + deterministic QA + bundle + surface input + Worker reviews + gate PASSED 0/0 + candidate READY (`b042be85`).
- Pinned CI PDF from run `36504726702` (TeX byte-identical to built commit): four-surface identity independently demonstrated (repo == sidecar == artifact == artifact-sidecar == eb0e4923, 335817 B, 12 pp). IDENTITY PASS.
- Validated + advanced DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (HUMAN_GATE_REACHED, next PUBLICATION_PREVIEW) with zero drift errors.
- Fresh Publication Preview r6 shell + 14-section dossier; PENDING; no decision recorded or inferred. No Freeze/Release.

## External handoff

- None. Repository-local execution per contract. (Issue #551 execution comment to post per §13.)

## Deterministic execution transport

- Direct exact local CLI throughout (no operator bridge). Normal commits + non-force pushes + remote read-backs; prior-SHA verified before each write group.

## Deviations / failures

- Wall-clock timestamp slip on first gate recording (see above): Core fail-closed behavior worked as designed; corrected immediately.
- No Core defect; no build failure; no validation-report deletion; shared-Core changed paths = 0.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Review target: r6 Candidate + Candidate-bound PDF at reviewed commit `98cffa3bbaf36801de1d7bcb8b2449cc0bb0b9d6` in `publication-preview-r6.md`
- Session status: `COMPLETE_AT_GATE`
