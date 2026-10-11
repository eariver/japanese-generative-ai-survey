# W40 r22 → fresh Human Publication Preview handoff

Status: `FRESH_HUMAN_PUBLICATION_PREVIEW_PENDING` candidate
Date: 2026-10-11 JST
Branch: `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Owner authorization: `execution/human-authorization/2026-10-11_owner-w40-r21-publication-preview-request-changes.md` (explicit REQUEST_CHANGES, Core v2 immutable)
Contract: `execution/instructions/2026-10-11_muse-w40-r22-authorized-human-preview-draft-rewrite.md`
Prior canonical (r21, superseded, Git-reachable): candidate `157c4644…`, PDF `f93d15f8…` (369980B/12pp)

## Exact review identity

- Lifecycle: `RELEASE_CANDIDATE`; next `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Production State: `sources/2026-W40/production-state.json` (`2128a9a4947db515c2a4c8d44c49b83492b28f57124bad838c1e3bf8ef207dba`)
- Architecture Review: approved (r1, Human Owner, provenance intact); Publication Preview: r1 REQUEST_CHANGES recorded, new Preview pending/null
- Checkpoints: discovery through validation passed; publication_preview/freeze/release pending
- Candidate: `sources/2026-W40/publication/v2/publication-candidate-v2.json` (`2cb17796ee620c0da4e9ed7142cb70c4d1975b728109a61d88e7cbd40c570017`, `READY_FOR_PUBLICATION_PREVIEW`)

## Gate revision (formal Human decision, not operator action)

- `gates/reviews/publication-r1.json` (PUBLICATION_PREVIEW / REQUEST_CHANGES / rev 1 / boundary ARCHITECTURE_ESTABLISHED, Human Owner, real UTC record, SHA-pinned refs); index holds ARCHITECTURE-r1 APPROVED + PREVIEW-r1 REQUEST_CHANGES; State rewound with approval preserved; 3 downstream checkpoints lawfully removed. No operator invalidation (config-forbidden at Preview).

## Substantive rewrite (r21 → r22)

- Draft: 29 → 40 content blocks with 4 tables (P1 price/availability, P2 Holo4/ELYZA, P6a metrics, P7 FLUX resolution) and 3 display equations (P6a Eq.3/Eq.5-objective/efficiency term); conventional Japanese with preserved English terms; VSS Oct1 9am PDT in-window scheduling correction (delivery unverified); P3 Sep29/Oct1 chronology fixed; full Sonnet/Argon cards; ELYZA SHAs; stale sentence never repeated.
- 31-row ledger (`execution/reviews/w40-r22-must-cover-31-ledger.md`): every requirement links block IDs with real quotes (26 prose, 4 prose+table, 1 prose+equation); no file-path-only fulfilment.
- Supersession report (`execution/w40-r22-supersession-and-cleanup-report.md`): old→new SHAs for all replaced singletons with Git retention; packages macroscopic bytes unchanged (re-derived identical); r21 archive preserved.

## Reader publication (exact bytes)

- Source: rewritten main.tex + 12 sections + references.bib (28/28 resolve, VSS note corrected) + style + 4-row ledger.
- PDF: `surveys/weekly/2026-W40/main.pdf` — 14 pages, 451,313 bytes, SHA-256 `c0b2fe1e4517bec8b3f85a4a518ed258be0de93b45f3e99c22ad75f93aae9704` (CI run `38124492838`, artifact `11696099301`, digest `sha256:4bfb58cd…`, built from `ea647933a`; `.sha256` committed alongside).
- Manuscript; surface input + surface semantic PASS; deterministic identifier/preflight/binding; bundle 3/3; publication semantic 11/11 (spot passages + r21 differences); visual 2/2 (14/14 pages inspected, no overflow/clipping); surface gate; three stage validations + checkpoints.
- Blob URL: `https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`
- Raw URL: `https://raw.githubusercontent.com/eariver/japanese-generative-ai-survey/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`

## Coverage and residual constraints

- 28/28 placed (20P/8S), 31/31 must-covers exposited, 113/113 boundaries honored, zero HOLD/REJECT chapters; approved Architecture/Selection/upstream untouched; Core #562 separate.
- Residual: 28-item scope omits two material announcements (disclosed); vendor figures publisher-measured; day-only dates; tutorial/reference bounds; unretrieved appendices/reports stated; VSS delivery unverified; legacy `validate-state` exit 1 (pre-existing semantics; governing agent-first PASS).
- 370,741-byte narrative corrected: actual r21 PDF was 369,980 bytes (canonical authority was always correct).

## Human decision options (after PDF review)

- `APPROVED` → record against the reviewed commit below; continue to Freeze.
- `REQUEST_CHANGES` → supply requested changes + one allowed boundary; Core records r2 and returns there.

Reviewed commit for decision (final HEAD after push): branch `weekly/2026-W40-v2-work`; chain includes gate record, rewrite, TeX, PDF, QA, and candidate commits from exact start `98b020d8`. Exact Final HEAD/Tree reported at handoff delivery.
