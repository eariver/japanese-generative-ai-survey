# Survey Production session — w39-r2-request-changes-resume-r3-20260929-r1

Issue: `2026-W39`
Started: `2026-09-28T16:17:59Z` (remote preflight guards PASS; local fast-forwarded to remote `8b752519a1b4ce3cd0b855a282f486bbe3fa3209`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `8b752519a1b4ce3cd0b855a282f486bbe3fa3209` / tree `52afa952e5490d0ecd4b4ab70643dff4b822ac31` (all §6 guards PASS: request in commit, ancestors f5997ed4/01724a7d/d95a811a, main/frozen verified)
- Reviewed remote `main`: `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`
- Production Line: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- Execution contract: `execution/requests/sol-w39-publication-preview-r2-human-request-changes-resume-r3-20260929.md`
- Human decision in contract: Publication Preview r2 `REQUEST_CHANGES`, boundary `DRAFT_COMPLETE` (explicit Human direction; resolves prior BLOCKED run's representation gap)
- Current TeX verified byte-identical to preserved repair `01724a7d` before regeneration (no cherry-pick)
- Lifecycle at start: `RELEASE_CANDIDATE` (r2-pinned, consistent); r2 decision PENDING
- No Drive access; no connector searched/installed. No merge commit; no reset/rebase/force/squash.

## Actions actually performed

- Recorded Human Publication Preview r2 REQUEST_CHANGES via canonical `request-publication-preview-revision` (rev 2, boundary DRAFT_COMPLETE, reviewed `d95a811a`, full RC text, wall-clock reviewed_at); publication-local invalidation only (DRAFT_COMPLETE/VALIDATED_DRAFT checkpoints removed; Architecture approval preserved); state returned to DRAFT_COMPLETE.
- Regenerated publication chain from repaired TeX: manuscript (31/31), deterministic QA, bundle, corrected surface input (fixed stale r2-era blocks found during regen), Worker surface-semantic PASS, lexical gate PASSED 0/0, Worker semantic-editorial 11/11 + visual 2/2 (extraction re-check on exact final bytes), candidate READY (`7def181d`).
- Pinned CI PDF from run `36440543369` (TeX byte-identical to built commit): four-surface identity independently demonstrated (repo == sidecar == artifact == artifact-sidecar == 7fac4b5c, 329744 B, 12 pp). IDENTITY PASS.
- Validated + advanced DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (HUMAN_GATE_REACHED, next PUBLICATION_PREVIEW) with zero drift errors.
- Final-byte seed-external scan over exact final TeX: 12 residual forms rechecked, all confined to correct compounds/standard senses (including prior-scan fixes 文脈資料→背景情報 and カーネルの持ち込み→カーネル移植, both confirmed absent); no new generic defects, no new typos.
- Fresh Publication Preview r3 shell + 14-section dossier; PENDING; no decision recorded or inferred. No Freeze/Release.

## External handoff

- None. Repository-local execution per contract.

## Deterministic execution transport

- Direct exact local CLI throughout (no operator bridge). Normal commits + non-force pushes + remote read-backs; prior-SHA verified before each write group.

## Deviations / failures

- Stale surface-input blocks (r2-era wording) found during r3 regen: corrected to r3 wording and regenerated downstream; documented here (r2 dossier did not catch it).
- No Core defect; no build failure; no validation-report deletion; shared-Core changed paths = 0.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Review target: r3 Candidate + Candidate-bound PDF at reviewed commit `4463e80e1e01476adf12586a705006e7bbcda8a6` in `publication-preview-r3.md`
- Session status: `COMPLETE_AT_GATE`
