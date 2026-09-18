# Survey Production session — w37-preview-r1-request-changes-regenerate-draft-r2-20260919

Issue: `2026-W37`
Started: `2026-09-19 JST` (replacement request `sol-w37-human-publication-preview-r1-request-changes-no-core-regenerate-draft-20260919.md`; prior operator-invalidation path intentionally rejected by Core, zero writes then)

## Starting authority

- Branch: `weekly/2026-W37-v2-work`
- Exact Starting SHA: `2d94f7a837f36015a973166ae104f905d7cd23e9` (remote HEAD/tree/parent verified read-only pre-write; parent `bc280c43`; main `6aa385cb` + Production Line `774dd39a` guards PASS; State RELEASE_CANDIDATE/PUBLICATION_PREVIEW/HUMAN_GATE_REACHED with Arch approved + Preview pending; no Preview Human record; r1 candidate/PDF authority and Sol REQUEST_CHANGES confirmed)
- Preflight: `human_gate_revision_boundaries.PUBLICATION_PREVIEW` includes `ARCHITECTURE_ESTABLISHED`; `_reopens_architecture == False`; next Preview revision exactly `1`
- Human decision: `REQUEST_CHANGES` (Publication Preview r1, imported authority); reviewed `8057a468897f67d3a11bd9287f6f56f0485877ce`; boundary `ARCHITECTURE_ESTABLISHED`

## Actions actually performed

- Recorded Human Preview r1 `REQUEST_CHANGES` via canonical `request-publication-preview-revision` (rev 1, reviewed `8057a468`, reviewed-at `2026-09-19T03:30:00Z`); preserved Architecture approval bytes; State to `ARCHITECTURE_ESTABLISHED` with Arch approved + Preview pending and Draft+ pending. Did not use `invalidate-pending-gate` or `revalidate-publication-surface`.
- Regenerated 7/7 Draft r2 Results + synthesis in natural technical Japanese from approved Architecture + frozen Evidence (Issue #501 repair; boundaries unchanged); dedicated Worker language QA PASS as `Worker/Agent (Muse Spark)`.
- Validated `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE` and advanced (recorded-at `2026-09-19T04:00:00Z`).
- Regenerated reader TeX r2 + Bib (19 keys incl. 8 direct X URLs); lexical scan PASS on all 12 files.
- Pushed TeX (commit `ba030750`); CI run `35369856431` success; pinned exact PDF (11 pages, 309850 bytes, SHA `c2298653`).
- Rebuilt manuscript, 3 deterministic checks + bundle, structured surface, Worker/Agent reader-surface semantic review (5 PASS), Worker/Agent semantic/editorial review (11 PASS), Worker/Agent visual review (2 PASS), reader-surface gate PASSED.
- Validated `DRAFT_COMPLETE -> VALIDATED_DRAFT` and advanced (recorded-at `2026-09-19T05:00:00Z`).
- Built new candidate (candidate SHA `8f74d379`, file SHA `eea9212f`) and validated `VALIDATED_DRAFT -> RELEASE_CANDIDATE`, advanced (recorded-at `2026-09-19T05:10:00Z`).
- Production commit `74400d71` (State + Candidate + Candidate-bound PDF).
- Created fresh Preview r2 shell/dossier PENDING referencing `74400d71`; no r2 decision; no Freeze/Release.
- No fresh research. No Architecture change. No Core change. No `revalidate-publication-surface`. `main` untouched.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Terminal reason: `HUMAN_GATE_REACHED`
- Session status: `COMPLETE_AT_GATE`
