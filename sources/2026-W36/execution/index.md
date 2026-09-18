# Survey Production execution index — 2026-W36

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W36/production-state.json`.

## Current authority

- Issue / edition: `2026-W36`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W36-v2-work`
- Start-of-run reviewed `main`: `5acbff8528890ed9fc324c0227e6c4e43067c438`
- Run started: `2026-09-16T14:04:14Z`; resumed from accepted Grok r4: `2026-09-17T00:08:00+09:00 JST`
- Requested stop: `PUBLICATION_PREVIEW` (via NO_CORE_CHANGE resume contract `requests/sol-w36-resume-r2-with-issue-comment-citation-no-core-change-20260917.md`; STOP at fresh Preview r2 PENDING)
- Production Profile: `sources/2026-W36/production-profile.json`
- Production State: `sources/2026-W36/production-state.json`
- Current State SHA-256: see `production-state.json` (lifecycle `RELEASE_CANDIDATE`, fresh Publication Preview r2 PENDING at reviewed authority `315d72805`)
- Current lifecycle: `RELEASE_CANDIDATE`
- Current terminal reason: `HUMAN_GATE_REACHED` (fresh Human Publication Preview r2 pending)
- Current next action: `PUBLICATION_PREVIEW`
- Formal Discovery: `accepted` (count = 19; graph `9c55b223`)
- Core changes: `0`
- Human decisions: `2` recorded canonically (Architecture Review r2 `APPROVED`; Publication Preview r1 `REQUEST_CHANGES` revision 1, reviewed `c4ab0455`, boundary `DRAFT_COMPLETE`); Publication Preview r2 PENDING (no decision recorded or inferred)
- Pinned Production Line: `production/survey-core-v2 @ 774dd39a951c9ac3818e83dfffd4c7666efb0a20` (untouched)
- W36 branch basis: `weekly/2026-W36-v2-work` from exact main `5acbff85` (remote read-back verified)
- Canonical ordinary window: ET `[2026-08-28T18:00:00-04:00, 2026-09-04T18:00:00-04:00)` /
  UTC `[2026-08-28T22:00:00Z, 2026-09-04T22:00:00Z)` /
  JST `[2026-08-29T07:00:00+09:00, 2026-09-05T07:00:00+09:00)`, end-exclusive

## Human Gates

- Architecture Review: `approved` (r1 `REQUEST_CHANGES` preserved; r2 `APPROVED` recorded canonically revision 2, reviewed `3e1e0fc3`)
- Publication Preview: `r1 REQUEST_CHANGES recorded` (revision 1, reviewed `c4ab0455`, boundary `DRAFT_COMPLETE`); r2 shell PENDING at reviewed authority `315d72805` (no r2 decision recorded or inferred)
- Detailed review records: `execution/reviews/architecture-r1.md` (REQUEST_CHANGES r1), `execution/reviews/architecture-r1-dossier.md` (r1), `execution/reviews/architecture-r2.md` (APPROVED r2), `execution/reviews/architecture-r2-dossier.md` (r2), `execution/reviews/publication-preview-r1.md` (r1 shell), `execution/reviews/publication-preview-r1-dossier.md` (r1), `execution/reviews/publication-preview-r2.md` (r2 PENDING shell), `execution/reviews/publication-preview-r2-dossier.md` (r2); canonical `gates/reviews/architecture-r1.json`, `gates/reviews/architecture-r2.json` (+ immutable snapshot), `gates/reviews/publication-r1.json`, `gates/review-index.json`

## Publication Candidate

- Current Human review target: Publication Preview r2 at reviewed authority `315d72805668ddf6d3f5d22085c0cad82aeee26c`
- Candidate SHA-256: `8103f341bafa3ccc2f52c8b7d25024e7dc9b3843998c221fbcac99b0437e93b1`
- PDF SHA-256: `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1` (12 pages, 359750 bytes, `surveys/weekly/2026-W36/main.pdf`)
- Prior r1 target (auditable): reviewed `c4ab045548ebf279209862bf62bd6f9725082fb8`, candidate `0c4ea873…`, PDF `b5893f48…` (12 pages, 360121 bytes)

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Grok run ID: `weekly-x-2026-W36`
- Repository task authority: `sources/2026-W36/external/x/weekly-x-2026-W36/grok-task.md`
- Latest Drive task-file path/reference: `Grok_X_SourseIntake/Weekly/2026-W36/weekly-x-2026-W36/grok-task.md`
- Intended Drive result folder: `Grok_X_SourseIntake/Weekly/2026-W36/weekly-x-2026-W36`
- Expected result filename: `grok-x-result.md`
- Accepted result: `grok-x-result-r4.md` (24219B / `a94f543d`; observed `2026-09-16T14:51:00Z`; manifest
  `sources/2026-W36/external/x/x-source-intake-v2.json` COMPLETE, SUCCESS / DISCOVERY_RECORDED)
- Canonical X accounting: 15 unique / 12 ordinary (3 official + 9 independent, 8 accounts) / 0 background / 3 late-breaking; 7 new r4 URLs

## Pipeline aggregates (r1)

- Discovery: 19 (BASE 19)
- Screening: 19 KEEP / 0 DROP (result set `f55a2285`)
- Evidence: 13 VERIFIED / 6 PARTIAL (set `1c0efd9f`); views `aab96ba6`
- Materiality: 18 MATERIAL / 1 CONTEXT; Completeness: LIMITED (3/3 SATISFIED)
- Selection: 18 SELECTED / 1 HOLD; Architecture r2: 6 packages, READY_FOR_ARCHITECTURE_REVIEW (RC-1 thesis corrected; packages/membership unchanged; matrix/selection byte-identical)
- Carry-over: zero formal inherited obligations (W35 RELEASED scanned; no carry roles); no W35 copy; Grok SELECTED never copied

## Deviations

- None blocking. Four issue-local vocabulary defects repaired edition-locally with full downstream regeneration (verification status enum, PROJECT entity/artifact types, missing closure, target-string mismatch, exception rules). No Core defect; no repair branch. Issue #497 + known release-workflow CLI defect intentionally untouched.

## Shared Core defects

- `defects/w36-r2-reader-surface-suppression-plumbing-blocker-20260917.md` (BLOCKING, recorded 2026-09-17): mandated #502 immutable blob permalink trips frozen-Core `RSG-LEX-INTERNAL-PATHS`; file-based audited suppressions are inert (object loads but never matches; array crashes loader) and review builders/validators expose no suppression passthrough. No Core repair branch or PR exists (Core frozen for this run).

## Pre-Discovery research preparation

- `sessions/w36-pre-discovery-research-prep-20260916-r1.md` (non-authoritative input only):
  all 12 lanes breadth-scanned; lanes F/I `NONE_FOUND`/`UNCERTAIN` pending Grok + first-party
  recheck; post-cutoff Late Breaking separated (vLLM 0.29.0, AgentAudit, Anthropic 09-09
  assessment, Gloo Code GA).

## Sessions

- `sessions/w36-sol-initialize-through-architecture-review-20260916-r1.md`
- `sessions/w36-pre-discovery-research-prep-20260916-r1.md` (non-authoritative preparation input)
- `sessions/w36-sol-resume-grok-r4-through-architecture-review-20260917-r1.md` (r4 through Architecture Review; COMPLETE_AT_GATE)
- `sessions/w36-architecture-r1-request-changes-bounded-regen-20260917-r2.md` (r1 REQUEST_CHANGES bounded regen; COMPLETE_AT_GATE)
- `sessions/w36-r2-approved-through-publication-preview-20260917-r1.md` (r2 APPROVED through Publication Preview r1 pending; COMPLETE_AT_GATE)
- `sessions/w36-r1-request-changes-regen-blocked-20260917-r1.md` (r1 REQUEST_CHANGES regen for #434/#500/#501/#502; STOPPED_AT_BLOCKER before Preview r2 — see Shared Core defects)
- `sessions/w36-resume-r2-issue-comment-citation-20260918.md` (NO_CORE_CHANGE resume via Issue #502 comment citation, suppression-free regen; COMPLETE_AT_GATE at Preview r2 PENDING)

## Instruction authority

- `requests/w36-sol-initialize-through-architecture-review-20260916-r1.md`
- `requests/sol-w36-resume-from-grok-r4-through-architecture-review-20260917.md` (execution contract for the r1 run)
- `requests/sol-w36-architecture-review-r1-request-changes-20260917.md` (Human/Sol review authority supplied by execution request; r1 decision + RC-1/RC-2 + SELECTION_COMPLETE boundary)
- `requests/sol-w36-architecture-review-r2-approved-through-publication-preview-20260917.md` (execution contract for the r2-APPROVED-through-Preview run; Human r2 APPROVED + Publication Preview mission, no Freeze/Release)
- `requests/sol-w36-publication-preview-r1-request-changes-issues-434-500-501-502-20260917.md` (execution contract for the r1-REQUEST_CHANGES regen run; Human Preview r1 REQUEST_CHANGES + DRAFT_COMPLETE boundary for #434/#500/#501/#502, no Freeze/Release)
- `requests/sol-w36-resume-r2-with-issue-comment-citation-no-core-change-20260917.md` (execution contract for this NO_CORE_CHANGE resume run; Issue #502 comment citation, suppression removal, DRAFT_COMPLETE boundary through fresh Preview r2 PENDING, no Freeze/Release)

## Provenance correction (RC-2)

- `execution/decisions/sol-w36-supervisory-reviews-20260917-r1.md` preserved byte-identical as worker-generated pre-gate check (not independent Sol authority)
- Classification: `execution/decisions/w36-worker-pregate-review-provenance-20260917-r2.md`; r2 dossier cites imported authority + Worker/Operator validation only

## Final disposition

`HUMAN_GATE_REACHED` (fresh Human Publication Preview r2 PENDING at reviewed authority `315d72805`; Architecture Review r2 APPROVED; r1 `REQUEST_CHANGES` preserved auditable; no r2 decision recorded or inferred; no Freeze; no Release)
