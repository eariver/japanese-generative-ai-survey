# Survey Production session — w37-preview-r2-request-changes-regenerate-draft-r3-20260919

Issue: `2026-W37`
Started: `2026-09-19 JST` (request `sol-w37-human-publication-preview-r2-request-changes-boundary-repair-r3-20260919.md`)

## Starting authority

- Branch: `weekly/2026-W37-v2-work`
- Exact Starting SHA: `b664baf0e8da0ed34bd5d148c34b313c718ee3a4` (remote HEAD/tree/parent verified read-only; parent `e207f329`; main `6aa385cb` + Production Line `774dd39a` guards PASS; State RELEASE_CANDIDATE/PUBLICATION_PREVIEW/HUMAN_GATE_REACHED with Arch approved + Preview pending; no Preview r2 record; r2 candidate `8f74d379`/PDF `c2298653`/309850B/11p; Sol r2 REQUEST_CHANGES; time-correction ledger present)
- Human decision: `REQUEST_CHANGES` (Publication Preview r2, imported authority); reviewed `74400d716e703c12efee97707ff0ee97d47f98a8`; boundary `ARCHITECTURE_ESTABLISHED`; expected rev `2`
- Preflight: boundary in `human_gate_revision_boundaries.PUBLICATION_PREVIEW`; `_reopens_architecture == False`; next Preview revision exactly `2`

## Actions actually performed

- Recorded Human Preview r2 `REQUEST_CHANGES` via canonical `request-publication-preview-revision` (rev 2, reviewed `74400d71`, actual JST wall-clock `2026-09-19T02:37:47+09:00`); Architecture approval preserved; State to `ARCHITECTURE_ESTABLISHED`. No `invalidate-pending-gate`, no `revalidate-publication-surface`.
- Regenerated 7/7 Draft r3 Results + synthesis narrowly for Issue #434 (retrieval-cutoff narration → verification-scope language); Worker Boundary QA PASS as `Worker/Agent (Muse Spark)` (7 checks incl. #501/#506 maintenance).
- Validated `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE` and advanced. Machine-transition recorded_at values are Core-monotonic by necessity (`00:30Z` series) and disclosed in r3 dossier, not presented as wall-clock; all review records use actual wall-clock.
- Regenerated reader TeX r3 + Bib with same scope-language repair; lexical scan PASS on all 12 files; #501 clean re-verified.
- Pushed TeX (commit `a28800cb`); CI run `35375978076` success; pinned exact PDF (11 pages, 309033 bytes, SHA `9e957ca2`).
- Rebuilt manuscript, 3 deterministic checks + bundle, structured surface, Worker/Agent reader-surface semantic review (5 PASS), Worker/Agent semantic/editorial review (11 PASS), Worker/Agent visual review (2 PASS), reader-surface gate PASSED — all with actual UTC build time `2026-09-18T17:47:29Z`.
- Validated `DRAFT_COMPLETE -> VALIDATED_DRAFT` and advanced; built new candidate (candidate SHA `e7f18eb2`); validated and advanced `VALIDATED_DRAFT -> RELEASE_CANDIDATE`.
- Production commit `8dfb83499` (State + Candidate + Candidate-bound PDF). Verified all new review-record timestamps ≤ commit time `2026-09-19T02:48:03+09:00`.
- Created fresh Preview r3 shell/dossier PENDING referencing `8dfb83499`; no r3 decision; no Freeze/Release.
- No fresh research. No Architecture change. No Core change. `main` untouched.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Terminal reason: `HUMAN_GATE_REACHED`
- Session status: `COMPLETE_AT_GATE`
