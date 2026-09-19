# Human Publication Preview dossier — 2026-W37 r4 (PENDING)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Date: `2026-09-19`
Revision: `r4` (Human r1/r2/r3 REQUEST_CHANGES preserved; r4 awaits independent Sol review and Human visual judgment)

This dossier was assembled by the worker from frozen Draft r3 authority plus the narrow #508 layout repair. It is not an independent Sol review and not a Human decision.

## 1. Exact review identity

- Edition `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`.
- Reviewed commit `07da54bfe3c1bc186abf7016486a4a6768f322c5` (State + Candidate + Candidate-bound PDF).
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next `PUBLICATION_PREVIEW`.
- Candidate `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `0f7c5af2dd069412b54aced39c43366975548ed50e2358bf3b7264775fb59f04`, file SHA `2adc7b2423ee1bb2b5d2553e4f80ae03189f1ecbfa47d8673b93e99a3b649dac`).
- PDF `surveys/weekly/2026-W37/main.pdf` (11 pages, 309187 bytes, SHA `09dea4e7fe7eecc6c4dae39a308899849ac84e598f9251b3d415e24b7ee3e268`, CI run `35386367629`, artifact `10564545188`).
- Manuscript `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `8fd688d75309ae54ce23d843903a97e69926df37cfeee1e51be070c12377207c`).
- Human Preview r3 `REQUEST_CHANGES` (record `gates/reviews/publication-r3.json`, rev 3, reviewed `8dfb83499`, boundary `DRAFT_COMPLETE`, reviewed_at actual `2026-09-19T04:20:33+09:00`).

## 2. Human Preview r3 record

- Path `sources/2026-W37/gates/reviews/publication-r3.json`, revision `3`, decision `REQUEST_CHANGES`, reviewed `8dfb83499`, boundary `DRAFT_COMPLETE`.
- reviewed_at `2026-09-19T04:20:33+09:00` (actual timezone-aware wall-clock, verified ≤ its commit time at read-back).
- Post-decision State: lifecycle `DRAFT_COMPLETE`, Arch approved with byte-valid provenance, draft checkpoint passed/preserved, validation+preview pending, no Architecture reopen.

## 3. Architecture approval preservation

- `gates/architecture-approval.json` (SHA `1a9d27454cfd5a8dd4840be3ef7ccd59ca389145e4970281f47cc24c1f4d33d9`), snapshot and `architecture-v2.json` (SHA `81e87a64`) untouched.
- Frozen upstream unchanged: Discovery 14, Screening 13/1, Evidence 11/2, Materiality 12/1/1, Selection 12/1, Architecture 7 packages.

## 4. Draft r3 authority preserved unchanged

- Draft r3 bytes/authority from the r3 run reused verbatim (no Draft regeneration; boundary `DRAFT_COMPLETE` keeps the draft checkpoint).
- No fresh research, no content expansion/shortening, no unrelated wording cleanup.

## 5. Issue #508 root cause as observed

- Reproduced from exact r3 PDF (`9e957ca2`, 11 pages): p.7 body ends after the next-watch subsection text; the trailing breakable Claim Boundary box found ~0 remaining column room and moved wholly to p.8; the `\balance` + `\clearpage` + `\onecolumn` transition then left p.8 with only that box (221 extracted chars) before Sources & Limitations on p.9.
- An intermediate `\nopagebreak` keep attempt demonstrably had no layout effect (rebuilt PDF kept the identical break; then reverted).

## 6. Exact layout-only change

- File: `surveys/weekly/2026-W37/sections/60-week-in-review.tex` only.
- Preimage SHA (committed r3): `964aecfada416a20ddd770d624ec3176c17209466472b42dac71264f2f61df58`.
- Change: +4 lines (3 comment lines documenting layout-only intent + one `\clearpage`) before `\subsection*{次に何を見るべきか}`; the ineffective keep attempt was fully reverted (net diff vs r3 is exactly those 4 lines).
- Effect: the closing subsection (heading + 2 paragraphs) travels with the summary box onto p.8; p.7 ends at the balanced community-note pause; p.8 holds substantive closing content + box.
- No reader-visible prose added/removed/altered; main.tex transition, all other sections, Bib, style untouched.

## 7. Changed file list (r3 authority → r4 authority)

- `sections/60-week-in-review.tex` (layout commands only)
- Derived/regenerated bindings: `main.pdf` + `main.pdf.sha256`, `publication/v2/*` (manuscript, deterministic ×3, bundle, surface, rs-sem, sem-ed, visual, gate, candidate), stage validations, checkpoints, `production-state.json`
- Gate records: `gates/reviews/publication-r3.json` (Human decision) + `gates/review-index.json`
- Execution provenance: this dossier, r4 shell, session record, execution index update
- Proof of no shared-Core change: `git diff --name-only <r3-start>..HEAD -- .github config schemas scripts templates tests` is empty (verified at read-back).

## 8. r3 → r4 reader-visible text comparison

- Normalized full-text extraction similarity 0.9999 over 19470 chars; the only differences are page-footer number placement noise from repagination. Section headings/order, box text, Sources & Limitations text, bibliography entries/order, citation keys, direct X URLs: all unchanged.
- TeX diff is layout-only (verified `git diff` shows only the 4 added lines).

## 9. Citation / X audit

- 19/19 cited keys resolve, missing 0, unused 0. 8 direct X status URLs retained. X community/context only. No blob/internal-path citations.

## 10. Regression checks

- #434: scope-only limitation language intact; no retrieval-cutoff narration reintroduced (lexical gate PASSED).
- #501: established terms intact; technical-use 模型/符号/代理人/砂場/給仕/引擎/許し/札/訳し/混合専門家/検出子 reintroduction zero (machine-checked + reread).
- #506: all new Worker artifacts use `Worker/Agent (Muse Spark)` exclusively.
- #507: Human r3 record and all new Worker review records use actual wall-clock and were verified ≤ their commit times. Pre-existing future-dated machine-transition history untouched (correction ledger preserved). New machine-transition `recorded_at` values (`00:33Z`/`00:34Z`) remain Core-monotonic by necessity and are disclosed here, not presented as wall-clock.

## 11. New TeX / PDF identity

- TeX: `main.tex` unchanged from r3; `60-week-in-review.tex` layout-only +4 lines.
- PDF: `09dea4e7fe7eecc6c4dae39a308899849ac84e598f9251b3d415e24b7ee3e268`, 309187 bytes, 11 pages, CI run `35386367629`, artifact `10564545188`.

## 12. All-page visual review result (Worker)

- All 11 pages rendered (pdftoppm) and inspected plus full text extraction.
- p.8 defect disposition: resolved — p.8 now carries the closing subsection (heading + 2 paragraphs) plus the summary box; no Claim-Boundary-only page remains.
- No blank pages; no new large structural holes (p.7 ends at a clean balanced section pause; p.8 right column empty as a natural short closing page, same Weekly identity as before); no overlap/clipping/broken glyphs/orphan box; two-column body and one-column Sources/References preserved; section order unchanged; no content lost.

## 13. Candidate / lifecycle

- New candidate SHA `0f7c5af2dd069412b54aced39c43366975548ed50e2358bf3b7264775fb59f04` (`READY_FOR_PUBLICATION_PREVIEW`).
- Lifecycle `RELEASE_CANDIDATE`, next `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`. Human Preview r4 `PENDING`. Freeze/Release not performed.

## 14. Downstream provenance

- Worker created all r4 artifacts with truthful provenance; no Sol/Human authorship claimed. Fresh Preview r4 awaits independent Sol review and Human visual judgment. No r4 decision recorded.
- Generic Weekly pagination hardening remains a shared-Core concern carried forward under Issue #508 (not closed automatically); no generic fixture was added in this run per the Core freeze.
