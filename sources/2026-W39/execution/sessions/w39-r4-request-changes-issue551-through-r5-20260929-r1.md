# Survey Production session — w39-r4-request-changes-issue551-through-r5-20260929-r1

Issue: `2026-W39` (+ GitHub Issue #551)
Started: `2026-09-28T18:22:16Z` (remote preflight guards PASS; local fast-forwarded to remote `a4a495b1fe95025c114604523cae7e0310db3def`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `a4a495b1fe95025c114604523cae7e0310db3def` / tree `c3d7b5ec95b7bb6a64b357cedbf9f32eb4e69c30` (all guards PASS: request in commit, main/frozen verified, r4 shell binds r4 authority with PENDING)
- Reviewed remote `main`: `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`
- Production Line: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- Execution contract: `execution/requests/sol-w39-publication-preview-r4-issue551-request-changes-through-r5-20260929.md`
- Human decision in contract: Publication Preview r4 `REQUEST_CHANGES`, boundary `DRAFT_COMPLETE` (explicit Human direction via Issue #551)
- Lifecycle at start: `RELEASE_CANDIDATE` (r4-pinned, consistent); r4 decision PENDING
- No Drive access; no connector searched/installed. No merge commit; no reset/rebase/force/squash.

## Actions actually performed

- Recorded Human Publication Preview r4 REQUEST_CHANGES via canonical `request-publication-preview-revision` (rev 4, boundary DRAFT_COMPLETE, reviewed `eb3bb84f`, wall-clock reviewed_at); publication-local invalidation only; Architecture approval preserved; state returned to DRAFT_COMPLETE. (One timestamp-provenance incident: first attempt used a past reviewed_at and Core correctly refused with resumability error; restored tree and re-recorded with wall clock. No committed bytes affected.)
- Mandatory source read-back before editing (all five groups, no escalation needed):
  - ART: bound primary source re-read — RT known from prior jumbo-phage studies; novelty is system-level (RT + partner gene + long repeat array; short-RNA expression validated; function unknown). Consistent with accepted Evidence; repair proceeds.
  - Cursor: collector method note confirms evals-as-proxy strength (fast/useful proxy; may overrepresent hard problems). Repair proceeds.
  - Claude Code: first-party @ClaudeDevs X status URL present in accepted Raw ledger (ordinary Sep 25 19:04 UTC) — no new source needed; behavior claim rebound to it, tier split stays on framed secondary.
  - Opus: bound primary source re-read confirms typical-workload 40% (`at default settings…on typical workloads`) and `up to 2.5x speed`. Repair proceeds.
  - DolphinBench: accepted Evidence already distinguishes v1 Sep 21 / v2 Sep 22. Repair proceeds.
- Repaired reader surface (all occurrences incl. frontmatter/synthesis/source-notes; wording-only; invariants preserved): ART system-novelty wording; Cursor proxy strength; Claude Code first-party binding + new bib entry; Opus typical-workload + 最大2.5倍 (3 surfaces); DolphinBench v1/v2 dates (2 surfaces).
- Four-corpus regression guard re-run over final TeX (12 forms, compound-aware bad total 0); final-byte seed-external reread (all sections post-edit): no new defects, no new typos. New generic defects: 0.
- Regenerated publication chain from repaired TeX: manuscript (31/31) + deterministic QA + bundle + corrected surface input + Worker reviews + gate PASSED 0/0 + candidate READY (`18b9ab48`).
- Pinned CI PDF from run `36465420944` (TeX byte-identical to built commit): four-surface identity independently demonstrated (repo == sidecar == artifact == artifact-sidecar == d81e47c4, 335104 B, 12 pp). IDENTITY PASS.
- Validated + advanced DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (HUMAN_GATE_REACHED, next PUBLICATION_PREVIEW) with zero drift errors.
- Fresh Publication Preview r5 shell + 14-section dossier; PENDING; no decision recorded or inferred. No Freeze/Release.

## External handoff

- None. Repository-local execution per contract. (Issue #551 execution comment still to post per contract §11.)

## Deterministic execution transport

- Direct exact local CLI throughout (no operator bridge). Normal commits + non-force pushes + remote read-backs; prior-SHA verified before each write group.

## Deviations / failures

- Wall-clock timestamp discipline incident on first gate recording (see above): Core fail-closed behavior worked as designed; corrected immediately.
- No Core defect; no build failure; no validation-report deletion; shared-Core changed paths = 0.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Review target: r5 Candidate + Candidate-bound PDF at reviewed commit `342adad3400bd6dee07fb920441f8e259f18eb15` in `publication-preview-r5.md`
- Session status: `COMPLETE_AT_GATE`
