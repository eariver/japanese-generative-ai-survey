# Survey Production session — w39-r3-request-changes-resume-r4-20260929-r1

Issue: `2026-W39`
Started: `2026-09-28T17:06:51Z` (remote preflight guards PASS; local fast-forwarded to remote `5885aef9585cfbae776c02898ec6315a9c1dcb18`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `5885aef9585cfbae776c02898ec6315a9c1dcb18` / tree `481414f3387c9eee4b6b4bfbb7c36c86e7855d6a` (all §3 guards PASS: request in commit, ancestors, main/frozen verified; r3 shell binds r3 authority with PENDING)
- Reviewed remote `main`: `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`
- Production Line: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- Execution contract: `execution/requests/sol-w39-publication-preview-r3-human-request-changes-through-r4-20260929.md`
- Human decision in contract: Publication Preview r3 `REQUEST_CHANGES`, boundary `DRAFT_COMPLETE` (explicit Human direction)
- Lifecycle at start: `RELEASE_CANDIDATE` (r3-pinned, consistent); r3 decision PENDING
- No Drive access; no connector searched/installed. No merge commit; no reset/rebase/force/squash.

## Actions actually performed

- Recorded Human Publication Preview r3 REQUEST_CHANGES via canonical `request-publication-preview-revision` (rev 3, boundary DRAFT_COMPLETE, reviewed `4463e80e`, wall-clock reviewed_at); publication-local invalidation only; Architecture approval preserved; state returned to DRAFT_COMPLETE.
- Four-file union audit (BASE 178 + SUPPLEMENT 180 + R2_RESIDUAL 37 + R3_RESIDUAL 14 + 計り方 = 406 forms); r3-reviewed bytes searched (191 forms hit / 383 instances / 215 ZERO_HIT).
- Repaired all 14 r3-supplement residuals in TeX (wording-only; facts/numbers/dates/attribution/citations unchanged); corrected stale surface-input blocks before downstream binding.
- Final-byte seed-external scan over exact final TeX (after all edits): full reread found no new coined/metaphorical/Chinese-like/identity-destroying wording, no new typo; 文脈資料/カーネルの持ち込み absence reconfirmed; compound-aware verification (bad total 0).
- New generic defects requiring successor supplement: 0 (r3 supplement already exists and covers this run).
- r4 ledger: 383 occurrences (17 reader REPLACE / 46 reader RETAIN / 1 URL retain / 215 ZERO_HIT / 319 FROZEN_INTERNAL_NON_READER) + companion.
- Rebuilt via CI (run 36456312074, artifact 10986695131); four-surface byte identity independently demonstrated (repo == sidecar == artifact == artifact-sidecar == 19767148, 331169 B, 12 pp). IDENTITY PASS.
- Regenerated manuscript (31/31) + deterministic QA + bundle + surface input + Worker surface-semantic PASS + lexical gate PASSED 0/0 + Worker semantic-editorial 11/11 + visual 2/2 (extraction re-check on exact final bytes) + fresh candidate READY (`d399c25c`).
- Validated + advanced DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (HUMAN_GATE_REACHED, next PUBLICATION_PREVIEW) with zero drift errors.
- Fresh Publication Preview r4 shell + 14-section dossier; PENDING; no decision recorded or inferred. No Freeze/Release.

## External handoff

- None. Repository-local execution per contract.

## Deterministic execution transport

- Direct exact local CLI throughout (no operator bridge). Normal commits + non-force pushes + remote read-backs; prior-SHA verified before each write group.

## Deviations / failures

- No Core defect; no build failure; no validation-report deletion; shared-Core changed paths = 0.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Review target: r4 Candidate + Candidate-bound PDF at reviewed commit `eb3bb84fa72af02f30d8dfe888304c5988479013` in `publication-preview-r4.md`
- Session status: `COMPLETE_AT_GATE`
