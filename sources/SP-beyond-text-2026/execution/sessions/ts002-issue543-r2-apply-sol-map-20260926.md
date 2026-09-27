# Survey Production session — ts002-issue543-r2-apply-sol-map-20260926

Issue: `#543` r2 — apply Sol authoritative terminology map (Human-authorized r8)
Human authority: Human Owner explicit r8 REQUEST_CHANGES (narrow: apply Sol map r2; not approval; Freeze/Release unauthorized)
Normative map: `execution/terminology-issue543/sol-authoritative-terminology-map-r2-20260926.md` (applied without reinterpretation)
Branch: `special/beyond-text-2026-work` (existing only)

## Starting guards (remote authority, all PASS)

- Remote work HEAD `c54de34669…` / tree `af678a4b…`, main `0bbb02b3…` / tree `e4ddde5e…` via `git ls-remote` + fetch/object readback.
- FF sync only (c00a70c18 → c54de34669: r3 prompt commit).

## Preconditions (§3 contract, read-only PASS)

- lifecycle RELEASE_CANDIDATE; arch approved; pub pending; index ends r7; no r8; candidate 77d6be81 / PDF 94f6b211 (76pp).
- Core immutable values match (impl 95c03bf5…, 4 contract SHAs).

## Canonical r8 record

- `gates/reviews/publication-r8.json` via frozen `request-publication-preview-revision` (expected_revision 8 derived from index max 7).
- Reviewed commit c54de34669, boundary DRAFT_COMPLETE, lifecycle → DRAFT_COMPLETE, arch preserved.

## Sol map application

- ~250 substitutions with exact-count assertions (stages A/B/C + 2 late additions found by audit: 濾波崩壊, 膨張形式).
- SOL-CIT-001: exact split applied (EnCodec/btd007 + DAC Balanced data sampling/btd008). Sole citation delta: autocite 1259→1260 (+1 btd008), keys stay 139.
- L719 heading applied literally per map (redundant phrasing noted in ledger for Sol).
- Uncertain/out-of-scope occurrences left unchanged → `muse-candidates-for-sol-review-r2.md` (C-001…C-012, no Japanese proposals).

## Ledger

- `terminology-decision-ledger.{json,md}`: 141 rows (90 r1 preserved + 51 r2 SOL_AUTHORITATIVE_R2). r1 ESCALATEs marked resolved (S39c partial). JSON/MD synced (all r2 IDs verified in MD).

## Invariants

- autocite sequence identical except +1 btd008 (authorized); keys 139; PARTIAL 12; labels 15; bib byte-identical.
- Sections 116, order unchanged; 6 headings reworded by Sol map.
- Frozen #533/#539 scans PASS; Sol LHS prohibitions all zero.

## Completion (2026-09-26)

- Tex commits 4acdefa1 (map application) + 780ce975 (TeX-mode escapes W^Q/FD_openl3, pixel-identical, ledgered) pushed FF.
- First CI run 36237006666 FAILED (Missing $ at L407 from literal `W^Q`); minimal invisible escapes applied, no term change; rebuild CI run 36237310732 PASS: 77pp (+1 widening, envelope内), 0 blocking, 0 hbox-layout. PDF `e98f769e0dd9a4fe493e57d1827c67fc65a6ef8246210a52624a9225f071a8ba` (1097548 bytes), source-bound to 780ce975.
- Audit `pdf-build-audit-issue543-r8.json`; `build_validation_issue543_r8.py` (incl. Section-9 title fix) all PASS; prose guard PASS.
- `advance_validation_issue543_r8.py`: DRAFT_COMPLETE → VALIDATED_DRAFT. `advance_candidate_issue543_r8.py`: candidate `9d6cd7dddababbad0bcccbf13e0e65d4ea988265113bd6815be6c56208969598` READY_FOR_PUBLICATION_PREVIEW → RELEASE_CANDIDATE, pub pending, HUMAN_GATE_REACHED.
- 139/139 binding revalidated. Rendered-PDF broad scan on exact bytes: zero unexpected residuals (p64 extraction gap proven visual-only); designed residuals at expected levels; new canonical terms verified (one count checked visually).
- All-page text verification: 77 pages, min 442 (p77 tail), no blanks. Visual QA (TOC/renamed headings/speech+video tables/metric+network names/capstone/biblio/tail): no clipping/overflow/broken glyphs. Bibliography regression PASS.
- Core immutability audit PASS (impl + 4 hashes exact). Allowlist audit PASS. Architecture preserved. No approval/Freeze/Release/merge. Issue #543 stays open.
