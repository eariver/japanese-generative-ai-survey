# W40 r21 → fresh Human Publication Preview handoff

Status: `FRESH_HUMAN_PUBLICATION_PREVIEW_PENDING / W40_R21_READY_FOR_SOL_AND_OWNER_PDF_REVIEW` candidate
Date: 2026-10-11 JST
Branch: `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Owner authorization: `execution/human-authorization/2026-10-11_owner-w40-r20-architecture-approved.md`
Contract: `execution/instructions/2026-10-11_muse-w40-r21-owner-approved-through-publication-preview.md`

## Exact review identity

- Lifecycle: `RELEASE_CANDIDATE`; next `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Production State: `sources/2026-W40/production-state.json` (`93a65f7ca8e7c7b85c005ad83c5909965a307e4dcb8cf05e8efb33ca561089fe`)
- Architecture Review: approved (r1, Human Owner, provenance `953f682a…`); Publication Preview: pending/null
- Checkpoints: discovery/screening/evidence/materiality/completeness/selection/architecture/draft/validation passed; publication_preview/freeze/release pending
- Candidate: `sources/2026-W40/publication/v2/publication-candidate-v2.json` (`157c464481392b66387cb5b0cb7ba4d0bde53cffacc9d404aac1eede17ab15b2`, `READY_FOR_PUBLICATION_PREVIEW`)

## Approval record (r20 Architecture, Owner-explicit)

- Approval `953f682a…` binding exact r20 triple (Arch `a9b5c118…` / Summary `32f39de0…` / Attention `70ac43bd…`); reviewed commit `3711d777f`; recorded at real UTC `2026-10-10T19:26:43Z`; references pinned (memo `4b203ce8…`, Sol PASS `84add0c8…`, r20 erratum `564799ed…`).

## Reader publication (exact bytes)

- Source: `surveys/weekly/2026-W40/main.tex` + 12 sections + `references.bib` (28/28 citations resolve) + `jgaisurvey.sty` + 4-row community ledger.
- PDF: `surveys/weekly/2026-W40/main.pdf` — 12 pages, 370741 bytes, SHA-256 `f93d15f838cddf9489cc7ed6e73f3eb2cbe551044ac84a45cc41441fabf202ab` (CI run `38081205472`, artifact `11680681821`, digest `sha256:6b412756…`, built from `291d526f`; `.sha256` file committed alongside).
- Manuscript `b7720c55…`; quality bundle (3 deterministic QA PASS); semantic review 11/11; visual review 2/2 (12/12 pages inspected, no overflow/clipping); surface gate PASSED; stage validations + checkpoints for DRAFT_COMPLETE and VALIDATED_DRAFT.
- Blob URL: `https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`
- Raw URL: `https://raw.githubusercontent.com/eariver/japanese-generative-ai-survey/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`

## Coverage and depth (28 across 9 packages)

- P1 frontier pricing (3P), P2 open reasoning with licenses/SHAs/tables (2P), P3 separated decision surfaces (3P), P4 changelog-verbatim product surface (2P+1S), P5 five independent safety subsections with v2 pin (3P+2S), P6a equations/denominators/baselines/negatives at full depth (2P), P6b scopes/protocols/chronology/pins (2P+1S), P7 vendor-demo bounds (3P+2S), P8 agreement-vs-terms digest (2S). No page cap; 113 boundaries honored; HOLDs/REJECTs outside chapters; stale sentence never repeated.
- Risk: 28-item scope omits two material announcements (disclosed with reason); vendor figures publisher-measured; day-only dates; tutorial/reference bounds; unretrieved appendices/reports stated.

## Human decision options (after PDF review)

- `APPROVED` → record against the reviewed commit below; continue to Freeze.
- `REQUEST_CHANGES` → supply requested changes + one allowed boundary (`ARCHITECTURE_ESTABLISHED` or later preserves Architecture approval; earlier boundary reopens Architecture per dependency rule).

Reviewed commit for decision (final HEAD after push): branch `weekly/2026-W40-v2-work`; chain includes approval, draft, TeX, PDF, QA, and candidate commits from exact start `8695430b`. Exact Final HEAD/Tree reported at handoff delivery.
