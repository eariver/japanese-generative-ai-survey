# W40 layout repair → fresh Human Publication Preview handoff

Status: `FRESH_HUMAN_PUBLICATION_PREVIEW_PENDING` candidate (layout-only round complete; no further cycle opened)
Date: 2026-10-11 JST
Branch: `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Owner authorization: `execution/human-authorization/2026-10-11_owner-w40-r23-publication-preview-request-changes-r3.md` (explicit approval, rev 3, DRAFT_COMPLETE, layout-only)
Prior canonical (r23, superseded, Git-reachable): candidate `4be71507…`, PDF `82f7af37…` (466496B/14pp)

## Exact review identity

- Lifecycle: `RELEASE_CANDIDATE`; next `PUBLICATION_PREVIEW`; terminal `HUMAN_GATE_REACHED`
- Production State: `sources/2026-W40/production-state.json` (`47dfe274bfb10a29a522a133969a1bee88b9aa4c624b4427aa43fc1329583d99`)
- Architecture Review: approved (r1, preserved through r1–r3 Preview revisions); Publication Preview: r3 REQUEST_CHANGES recorded, new Preview pending/null
- Candidate: `sources/2026-W40/publication/v2/publication-candidate-v2.json` (`fd5ee590822d38b0ed4b00d5813cb5360ab2dcee3f4d501bae3eaa16bea3f49d`, `READY_FOR_PUBLICATION_PREVIEW`)

## Gate revision

- `gates/reviews/publication-r3.json` (PUBLICATION_PREVIEW / REQUEST_CHANGES / rev 3 / boundary DRAFT_COMPLETE, Human Owner, real UTC record, SHA-pinned auth); index holds ARCHITECTURE-r1 APPROVED + PREVIEW-r1/r2/r3 REQUEST_CHANGES.

## LAYOUT-01〜03 Before/After

- LAYOUT-01 (p.3 orphan): BEFORE §2 head/title stranded at column end with body on p.4 → AFTER head/title/deck together at p.4 column top (verified on 150dpi render).
- LAYOUT-02 (p.4 split): BEFORE boundary box broken across columns with table wedged inside → AFTER box unbroken in one column, table above (verified).
- LAYOUT-03 (p.9 split): BEFORE §9 title split across left/right columns → AFTER head/title together (verified).
- Control: 3× `\Needspace` + comments only (2 files, +6/−0); prose/citations/numbers/tables/equations byte-identical in meaning (surface SHA identical to r23).

## Full regression (14/14 pages at 150dpi)

- Cover/contents/frontmatter clean; all 9 package spreads intact; tables (P1/P2/P6a/FLUX), equations (P6a), week-in-review, source-notes, references [1]–[28] all clean; no new orphans, splits, overlaps, gaps, clipping, or missing glyphs.

## Reader publication (exact bytes)

- PDF: `surveys/weekly/2026-W40/main.pdf` — 14 pages, 466,202 bytes, SHA-256 `52b752bda7e3a37957ced7f815a4a2cc56bd8883c4579505e76057174e918ca6` (CI run `38137417169`, artifact `11701871676`, digest `sha256:36270949…`, built from layout commit; `.sha256` committed alongside).
- Fresh manuscript/surface/bundle/semantic/visual/gate + validations r4 + checkpoints (DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE).
- Blob URL: `https://github.com/eariver/japanese-generative-ai-survey/blob/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`
- Raw URL: `https://raw.githubusercontent.com/eariver/japanese-generative-ai-survey/weekly/2026-W40-v2-work/surveys/weekly/2026-W40/main.pdf`

## Invariants and residuals

- 28/28 placed (20P/8S), 31/31 must-covers, 113/113 boundaries, zero HOLD/REJECT chapters; Draft/Synthesis/Evidence/Selection/Architecture/Core untouched; legacy `validate-state` exit 1 (pre-existing semantics; governing agent-first PASS).
- Residual: none new; r23 residual constraints (two omitted announcements, vendor-measured figures, day-only dates, unretrieved appendices, VSS delivery unverified) carry over unchanged.

## Human decision options (after PDF review)

- `APPROVED` → record against the reviewed commit below; continue to Freeze.
- `REQUEST_CHANGES` → new explicit instruction required (no automatic cycle).

Reviewed commit for decision (final HEAD after push): branch `weekly/2026-W40-v2-work`; chain includes auth, gate record, layout controls, PDF, QA, and candidate commits from exact start `fd679a3e`. Exact Final HEAD/Tree reported at handoff delivery.
