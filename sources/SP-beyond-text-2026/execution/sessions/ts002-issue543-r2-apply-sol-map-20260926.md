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

## Next steps (same session)

1. Commit + push (FF only; allowlist audit before push).
2. CI PDF rebuild + artifact audit.
3. build/advance validation (frozen Core only) + rendered-PDF broad scan + all-page visual QA + candidate.
4. Final Core immutability audit + report. Stop at PUBLICATION_PREVIEW pending. No approval/Freeze/Release/merge. Issue #543 stays open.
