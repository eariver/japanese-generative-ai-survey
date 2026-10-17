# W42 r14 validation report (frozen validators + TeX proof + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition.

## Frozen CLI validations (all PASS, real receipts)
- `survey_drafting_v2_base.py draft-check` (canonical package × r14 proposal): P1–P7 all `{"passed": true, "errors": []}` (schema, identity, stable refs, attribution, must-cover, boundaries).
- Proposal SHAs v14.0 REVISED: P1 `a24274b4…`, P2 `7f76ea07…`, P3 `356f5827…`, P4 `d4722c4f…`, P5 `8770b609…`, P6 `ddcd20f9…`, P7 `f14e20b8…`; 112 paragraphs / 20,479 paragraph-only chars / 23,601 body chars / 7 tables / 7 notes. Per-chapter paragraph chars P1 2,996 / P2 2,761 / P3 4,237 / P4 3,121 / P5 2,388 / P6 2,873 / P7 2,103.
- Counter reconciliation (committed bytes, same definitions throughout): r11 82/17,004 → r12 92/18,165 (+10/+1,161) → r13 103/19,193 (+11/+1,028) → r14 112/20,479 (+9/+1,286). Body(PTN) chars: r11 20,082 / r12 21,281 / r13 22,315 / r14 23,601. All-block text (incl. headings/boundaries): r11 25,183 / r12 26,369 / r13 27,403 / r14 28,689.
- `synthesis-input` built via frozen CLI from the 7 proposal pairs; proposed synthesis result written with verified-UTC `generated_at`; `synthesis-check` `passed: true`.
- `validate_agent_state`: PASS (State untouched at DRAFT_COMPLETE).

## M01–M06 / m01–m05 gates
- M01 (MTP): Table-8 numbers quoted with SPEED-Bench/draft-7/greedy/sampled conditions from first-party S3a/S3b reads; programmatic scan for `受理率` returns zero.
- M02 (denominators): screening rounds vs 8-clone confirmation separated; FAP scope stated.
- M06 (timestamps): correction notice stands; r14 stamps verified UTC (recorded above); r12/r13 bytes untouched.
- m01–m05 + EDIT-02/03/04: scans clean (`practice`/`成果ゼロ`/`記事の作法`/`三層モデル` misuse/`専門身体`/literal metadata/AA-INDEX-as-rank all zero).
- F01/F02 held: license tiers intact; 0 non-http URLs in 153 ledger rows; bundle refs excluded from all proposal blocks.

## Reader preview fidelity
- `reader-preview-r14.PROPOSED.json/.md`: 112 paragraphs / 7 tables / 7 notes; zero CLAIM_BOUNDARY; zero machine-trace/Hangul/simplified ghosts; single documented exception (none remaining; SRFT retained as named method with ledger note from r12).
- Citation ledger: 153 rows (126 block + 27 table-row) with per-claim best URL, source classes, direct bib keys; bibliography map 59 unique URLs (45 primary / 9 secondary / 4 paper / 1 independent).
- TeX body = preview block text verbatim; ONLY documented deltas are appended `\cite` markers + per-row table cites + bibliography. Crosswalk files bind every marker.

## TeX/PDF proof (non-canonical, edition-local)
- 17 pages, log fully clean (see manifest). All 17 pages + 2 contact sheets committed with hashes; `review-pages-r14.md` renderable index with per-page density/cite/table checklist.
- `main.log` committed via `git add -f` + remote blob read-back (PDF-03 closed with evidence, not assertion).

## Canonical invariants (all preserved)
- `production-state.json`: DRAFT_COMPLETE, architecture approved, publication pending (SHA unchanged).
- Draft checkpoint `ARCHITECTURE_ESTABLISHED.json`, approval, review index, r1 record/snapshot: unchanged.
- Canonical Draft Results/Packages/Synthesis (v10.0): SHAs unchanged (read-only validator inputs).
- Accepted Evidence/Views/Materiality/Selection/Architecture: untouched. r11/r12/r13 proposals preserved as history. No TeX in canonical paths; Publication Preview not started.

## Remaining explicit unknowns (not hidden)
- Nemotron full 79pp PDF bytes (S3a/S3b pages read instead); greedy/temperature details beyond Table 8 not claimed.
- Maia unnamed baseline values; independent hardware repro; METR three-tier internals; Vals full methodology.
- 28pp target gap: honest 17 pages at magazine density; `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED` remains open for Sol (deepen with new primary reads vs amend plan) — no silent downscope, no padding.
