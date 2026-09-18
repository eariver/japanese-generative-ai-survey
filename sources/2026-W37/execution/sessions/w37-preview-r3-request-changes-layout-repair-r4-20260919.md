# Survey Production session — w37-preview-r3-request-changes-layout-repair-r4-20260919

Issue: `2026-W37`
Started: `2026-09-19 JST` (inline instruction: Human Preview r3 REQUEST_CHANGES / Issue #508 layout-only repair through fresh Preview r4)

## Starting authority

- Branch: `weekly/2026-W37-v2-work`
- Exact Starting SHA: `ec3e18255150e1b7876b9d762d5036d28228dc58` (HEAD message `W37: record independent Sol Publication Preview r3 PASS with timestamp correction`; remote HEAD/tree verified read-only; main `6aa385cb` + Production Line `774dd39a` guards PASS; State RELEASE_CANDIDATE/PUBLICATION_PREVIEW/HUMAN_GATE_REACHED with Arch approved + Preview pending, Freeze/Release pending; index exactly arch r1 + preview r1 + preview r2, no preview r3; r3 candidate `e7f18eb2`/PDF `9e957ca2`/309033B/11p/CI `10559799086`)
- Human decision: `REQUEST_CHANGES — visual layout only` (Publication Preview r3, Issue #508: Week in Review trailing Claim Boundary isolated on near-empty p.8); reviewed `8dfb83499f839907d180d9a06bd155cc12fb27d6`; boundary `DRAFT_COMPLETE`; expected rev `3` (verified from index, not inferred)
- Sol r3 verdict `PASS_WITH_PROVENANCE_CORRECTION / READY_FOR_HUMAN_PUBLICATION_PREVIEW` noted; Human visual review supersedes on layout

## Actions actually performed

- Recorded Human Preview r3 `REQUEST_CHANGES` via canonical `request-publication-preview-revision` (rev 3, actual wall-clock `2026-09-19T04:20:33+09:00`, verified ≤ commit `6e2dc912` at 04:23:29); Architecture approval preserved; State to `DRAFT_COMPLETE` with draft checkpoint passed/preserved. No `invalidate-pending-gate`, no `revalidate-publication-surface`.
- Reproduced #508 from exact r3 PDF (p.8 = 221-char box only; p.7 column room ~0). Read Issue #40 precedent (transition-flow principle; no blind Needspace; Weekly two/one-column identity).
- Applied edition-local layout-only repair in `sections/60-week-in-review.tex`: preimage SHA `964aecfa`; a `\nopagebreak` keep attempt demonstrably had no effect (rebuilt PDF identical break; reverted); final repair is +4 lines (comments + `\clearpage` before closing subsection) carrying the subsection with its box. No prose changed; lexical gate PASSED.
- Pushed repair (commit `507ef3cb`); CI run `35386367629` success; pinned exact PDF (11 pages, 309187 bytes, SHA `09dea4e7`, artifact `10564545188`).
- Content identity r3→r4: normalized text similarity 0.9999 (page-number noise only); headings/order/box/sources/bib/keys/X URLs unchanged.
- Rendered all 11 pages (pdftoppm) + full extraction inspection: p.8 resolved (subsection + box); no blank pages; no new large holes; no overlap/clipping/glyph/orphan defects; two-column/one-column identity preserved.
- Rebuilt manuscript, deterministic checks + bundle, surface, Worker/Agent rs-sem (5 PASS), Worker/Agent sem-ed (11 PASS), Worker/Agent visual (2 PASS with explicit #508 checks), gate PASSED — all with actual UTC build time `2026-09-18T19:38:25Z`.
- Validated `DRAFT_COMPLETE -> VALIDATED_DRAFT` and advanced; built new candidate (`0f7c5af2`); validated and advanced `VALIDATED_DRAFT -> RELEASE_CANDIDATE`. Machine-transition recorded_at values remain Core-monotonic by necessity (`00:33Z`/`00:34Z`) and are disclosed in r4 dossier, not presented as wall-clock.
- Production commit `07da54bf` (State + Candidate + PDF). Verified new review-record timestamps ≤ commit time `04:39:18+09:00`.
- Created fresh Preview r4 shell/dossier PENDING referencing `07da54bf`; no r4 decision; no Freeze/Release.
- No fresh research. No Draft change. No Core change (Issue #508 generic hardening carried forward). `main` untouched.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Terminal reason: `HUMAN_GATE_REACHED`
- Session status: `COMPLETE_AT_GATE`
