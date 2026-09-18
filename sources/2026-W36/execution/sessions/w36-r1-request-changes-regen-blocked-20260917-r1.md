# Session — W36 Publication Preview r1 REQUEST_CHANGES regen (blocked before Preview r2)

- Issue: `2026-W36` (WEEKLY + WEEKLY_MAGAZINE)
- Branch: `weekly/2026-W36-v2-work`
- Execution contract: `execution/requests/sol-w36-publication-preview-r1-request-changes-issues-434-500-501-502-20260917.md`
- Human decision: `REQUEST_CHANGES` (Publication Preview r1); boundary `DRAFT_COMPLETE`; changes #434/#500/#501/#502
- Started at Exact Starting SHA: `1ab688e9973ab0a7bea72f892650fb3f258a2a00` (tree `429cd33c`, parent `acb82c`)
- Starting Guard: all read-only checks PASS (remote W36 HEAD/tree/parent, main `5acbff85`/`451fd7c6`, Production Line `774dd39a`/`cd46a6f7a`, lifecycle `RELEASE_CANDIDATE`, next `PUBLICATION_PREVIEW`, r1 `PENDING`, reviewed prod `c4ab0455`, PDF `b5893f48`/360121B/12p, candidate `0c4ea873`, Architecture r2 `APPROVED` vs `3e1e0fc3`)
- Issues read: #434 (body + 6 comments), #500/#501/#502 (bodies + handling-plan comments)
- Ended: `DRAFT_COMPLETE` / `stage:reader-publication-validation`, BLOCKED — see defect record `execution/defects/w36-r2-reader-surface-suppression-plumbing-blocker-20260917.md`
- Session status: `STOPPED_AT_BLOCKER` (no Freeze/Release; no r2 decision generated)

## Commits pushed (normal, non-force)

1. `a8d5c89b3` — r1 REQUEST_CHANGES recorded via canonical `survey_human_gate_v2.py request-publication-preview-revision` (revision 1, reviewed `c4ab0455`, boundary `DRAFT_COMPLETE`); checkpoints `DRAFT_COMPLETE`/`VALIDATED_DRAFT` invalidated; Architecture approval preserved.
2. `188f5acc0` — #502 `community-observation.md` alone (exact 15 accepted X URLs verified byte-identical to accepted r4 ledger; reader-auditable metadata + context-only boundary; no internal IDs/status/revisions/paths). Immutable citation target; must remain in history unsquashed.
3. `7a92004d5` — reader-facing repair (#434 full semantic boundary pass; #500 GLM boundary/no-same-week across article/synthesis/source-notes/bib; #501 full-surface natural technical Japanese from Draft evidence meanings; #502 `w36community` immutable blob URL + leakage-free notes; `not consumed`/`edition-local storage`/HOLD/PARTIAL wording converted throughout bib).
4. WIP (this session, blocked): rebuilt r2 publication authority + new CI PDF + this record set. Message marks BLOCKED explicitly; nothing downstream of the blocker is claimed.

## Work performed (detail)

- Gate record verified: `gates/reviews/publication-r1.json` (r1/REQUEST_CHANGES/`c4ab0455`/`DRAFT_COMPLETE`), state `DRAFT_COMPLETE`, next `stage:reader-publication-validation`.
- Manifest URL verified live at commit `188f5acc0` (15 URLs, no internal tokens).
- Repair proofread file-by-file against frozen Draft package English meanings (e.g. one-click full-frame debugging, environment-level agent telemetry, in-house RL framework, ~67GB disk plus deletable C files, high-risk accounts, trusted defenders, Wiz recall); claim strength/attribution/vendor bounds preserved; no new facts.
- Post-repair audits: all 14 representative/internal phrases absent; `scan-file` PASS on 10/10 TeX files; bib required 1 audited suppression (false positive, see defect record).
- CI run `35229849238` success (head `7a92004d5`); artifact `10501440128` (`sha256:b91ee21e...`); PDF pinned: 12p/359906B/`abbbe4eb...`; text extraction clean (25806 chars, all sections, repaired wording present).
- Draft freeze re-confirmed (6 package + 6 result SHAs unchanged; architecture SHA unchanged).
- Rebuilt: manuscript (20/20), identifier-preservation, pdf-preflight (run `35229849238`), subject-entity-binding (18/18 keys), quality bundle (3 deterministic PASS), surface input (17 blocks from repaired TeX), surface semantic review (5 checks PASS, digest-validated), surface gate (`PASSED`, 1 SUPPRESSED; `validate-gate` PASS).
- Semantic (11 rows) and visual (2 rows) review contents authored from exact-new-byte reads but NOT bound (canonical binder blocked); kept in this record only, not as authority files.
- Core defect handling: no shared-Core path modified; defect recorded edition-locally; generic #434/#500/#501/#502 pipeline implications left on their Issues per contract (Issues not closed).

## Ending remote state

- Work branch head: WIP commit on top of `7a92004d5` (read back after push).
- `main` and `production/survey-core-v2` untouched (guards re-verified read-only before each push).
- Normal endpoint NOT reached (`RELEASE_CANDIDATE` / Preview r2 `PENDING` pending Core repair).

## Exact stop reason

`BLOCKED_SHARED_CORE_DEFECT`: canonical DRAFT_COMPLETE validation cannot pass with the mandated #502 permalink present, because frozen-Core file-based reader-surface suppressions are inert (object loads but never matches; array crashes loader) and review builders/validators expose no suppression passthrough. Recorded, committed, pushed; STOP without Freeze/Release and without generating a Human r2 decision.
