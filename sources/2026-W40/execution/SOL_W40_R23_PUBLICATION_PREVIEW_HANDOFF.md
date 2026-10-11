# W40 r23 → fresh Human Publication Preview handoff

Status: `FRESH_HUMAN_PUBLICATION_PREVIEW_PENDING` candidate (single bounded round complete; no r24 opened)
Date: 2026-10-11 JST
Branch: `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Owner authorization: `execution/human-authorization/2026-10-11_owner-w40-r22-publication-preview-request-changes.md` (rev 2, bounded scope)
Sol basis: `execution/reviews/sol-w40-r22-focused-publication-editorial-audit-20261011.md`
Prior canonical (r22, superseded, Git-reachable): candidate `2cb17796…`, PDF `c0b2fe1e…` (451313B/14pp)

## Exact review identity

- Lifecycle: `RELEASE_CANDIDATE`; next `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Production State: `sources/2026-W40/production-state.json` (`7be5cbbcb4fdf7d89cff1ffb055d4289f6bd5ebbdf1a151ca7c58d559e76515a`)
- Architecture Review: approved (r1, preserved through both Preview revisions); Publication Preview: r2 REQUEST_CHANGES recorded, new Preview pending/null
- Candidate: `sources/2026-W40/publication/v2/publication-candidate-v2.json` (`4be71507d2e7eba8771bf512eb2cf6f7ded01bc638cadfa4f00602427697d6eb`, `READY_FOR_PUBLICATION_PREVIEW`)

## Gate revision

- `gates/reviews/publication-r2.json` (PUBLICATION_PREVIEW / REQUEST_CHANGES / rev 2 / boundary ARCHITECTURE_ESTABLISHED, Human Owner, real UTC record, SHA-pinned refs); index holds ARCHITECTURE-r1 APPROVED + PREVIEW-r1/r2 REQUEST_CHANGES.

## Bounded changes (old → new)

- P0-01 Gemini: 95%-off detached from intro pair (50% step stated; qualifier isolated as unverified) — prose + P1 table.
- P0-02 AgentPerf: speculative-decoding correction (MTP/DFlash/DSpark) + measurement conditions.
- P0-03 ELYZA: EN scores, base deltas, method specifics, active-params unstated, reconstructed table; overstatements removed.
- P0-04 ContextLM: Eq.3 args (u)/(g) + legend, Eq.5 variable definitions, Eq.6 integrated advantage with efficiency-only <2-success semantics.
- P0-05 Leakage: P7 internal-authority sentences deleted; "受理済み資料" rephrased in P1/P2 TeX; P5 five \subsection* subsections added.
- P1: guard-number meanings, OpenShell/Sentry roles, SynthID assay context, SCR + MoE role division, metric definitions, harbor==0.21.0 example, OCR 10MiB-w/4MiB-w/o. Nothing else touched (P3/P4/frontmatter/synthesis payload unchanged by design).

## 31 must-cover final verdicts

- 31/31 FULFILLED with row-level quotes (`execution/reviews/w40-r23-must-cover-31-ledger.md`): 26 prose, 4 prose+table, 1 prose+equation. P8 concise per Architecture design (documented, not a gap).

## Independent-audit 10 findings disposition

- Sol-adopted R22-F01/F02/F05: FIXED. F03/F04: FIXED bounded (supporting items stay bounded). F06: limited — P4 source-bounded (no invented workflow), others as designed. F07: FIXED via fresh QA.
- Remaining independent-audit items beyond the adopted set: 対応不要 — per Owner scope ceiling (no auto-obligation, no padding, no taste rewrites, no r24 re-audit). No unaddressed P0-class item remains open.

## Reader publication (exact bytes)

- PDF: `surveys/weekly/2026-W40/main.pdf` — 14 pages, 466,496 bytes, SHA-256 `82f7af378d614a21cdd6dabe3e57a491d7ebda1368e21ecf3950e170a48e896b` (CI run `38133771409`, artifact `11700810058`, digest `sha256:7d8644af…`, built from `9303dd11`; `.sha256` committed alongside).
- Manuscript; surface (from CURRENT results) + surface semantic PASS; deterministic 3/3; bundle; publication semantic 11/11; visual 2/2 (14/14 pages at 150dpi); surface gate; three stage validations + checkpoints.
- Blob URL: `https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`
- Raw URL: `https://raw.githubusercontent.com/eariver/japanese-generative-ai-survey/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`

## Residual minor constraints

- 28-item scope omits two material announcements (disclosed); vendor figures publisher-measured; day-only dates; tutorial/reference bounds; unretrieved appendices/reports stated; VSS delivery unverified; P8 concise by design; legacy `validate-state` exit 1 (pre-existing semantics; governing agent-first PASS).

## Human decision options (after PDF review)

- `APPROVED` → record against the reviewed commit below; continue to Freeze.
- `REQUEST_CHANGES` → new explicit instruction required (no automatic r24).

Reviewed commit for decision (final HEAD after push): branch `weekly/2026-W40-v2-work`; chain includes gate record, bounded rewrite, TeX, PDF, QA, and candidate commits from exact start `ee56893d`. Exact Final HEAD/Tree reported at handoff delivery.
