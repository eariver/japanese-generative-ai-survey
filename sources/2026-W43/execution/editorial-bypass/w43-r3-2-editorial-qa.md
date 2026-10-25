# W43 Core-free editorial QA r3.2 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work`.
r3.2 preview: `execution/editorial-bypass/w43-r3-2-reader-preview-UNVALIDATED-20261026.md`
Ledger: `execution/editorial-bypass/w43-r3-2-citation-confidence-ledger.json` (96 IDs preserved; SHA256 `2ea2b70b4df5a2e2134dc6d9423abe2f713a125b1821e1ba3d80761e23e2e79c`)
Crosswalk: `execution/editorial-bypass/w43-r3-2-source-crosswalk.md` (36 keys incl. voxtral-card-units + deepinfer-import-scope)
Basis: independent `20261026005634_SolReview.md` (34,589B, `fbbc9cb3…`, unread in-session — standing limitation) via binding adjudication + receipt; r3.1 subject `9d3a3de06…`.
Method: 4-point bounded repair only (P1-A01/P2-A02/P2-A03/P2-A04). No breadth expansion, no guessing.

## 1. Four-point closure

| ID | Verdict | Evidence |
|---|---|---|
| P1-A01 5表行別出典 | FIXED | 20/20 tables carry non-empty `table_rows[]` (79 sub-rows); 5 new tables carry 29 value-claims with unit/denominator/model/evidence/archive; row labels machine-verified against displayed rows (ASCII/全角表記ゆれ9件を exact 化); row-quality counted separately (§2) |
| P2-A02 FAQ暫定 | FIXED | p4-p2/p4-p7 → `UNRESOLVED_FAQ_ATTRIBUTION` (+`UNVERIFIED_CONTRARY_DESCRIPTION` in ledger/crosswalk); no verified official-vs-official claim; PR/blog first-party kept where verified; live/schema/GA UNKNOWN; arithmetic/Elo untouched; Architecture label legacy-held, no rewrite |
| P2-A03 Voxtral単位 | FIXED | p5-f1 rewritten per value: WER内訳・recall内訳=COMPARATOR_UNVERIFIED, cpWER対照Pyannote=明示, Small/Realtime/agent単価=UNIT_UNVERIFIED, Mini $0.0035/分・Speech $13/100万字=確認; counts: 50+ STT / 35+ Realtime+40+方言 / 40+標本 / TTS UNRESOLVED; §5.1/§5.2 stay PARTIAL (see §4) |
| P2-A04 コード hygiene | FIXED | p2-f1 labeled 構成の抜粋／疑似使用例・NOT_EXECUTED・IMPORT_UNVERIFIED; no fabricated import; not a copy-paste program; reader body grep-clean of operator meta (filename keeps UNVALIDATED; full provenance in QA/sidecars); 2 micro-trims of duplicated clauses (p3-p8 coming-soon clause, p4-p6 AA clause — both retained in notes/tables, no uncertainty lost) |

No P1 row lacked accepted-Evidence trace → no SOURCE_BLOCKED stop needed. No P0.

## 2. 20-table exact row counts (content + layout separated)

| Table | Data rows | Claims | Content | Layout |
|---|---|---|---|---|
| p1-t1 | 4 | — | OK | DRAFT_TEXT |
| p1-t2 | 4 | — | OK | DRAFT_TEXT |
| p1-t3 | 3 | — | OK | DRAFT_TEXT |
| p1-t4 | 3 | — | OK | DRAFT_TEXT |
| p2-t1 | 5 | — | OK | DRAFT_TEXT |
| p2-t2 | 4 | — | OK | DRAFT_TEXT |
| p3-t1 | 4 | — | OK | DRAFT_TEXT |
| p3-t2 | 3 | — | OK | DRAFT_TEXT |
| p4-t1 | 5 | — | OK | DRAFT_TEXT |
| p5-t1 | 4 | — | OK | DRAFT_TEXT |
| p5-t2 | 4 | — | OK | DRAFT_TEXT |
| p7-t1 | 4 | — | OK | DRAFT_TEXT |
| p7-t2 | 4 | — | OK | DRAFT_TEXT |
| p8-t1 | 4 | — | OK | DRAFT_TEXT |
| p8-t2 | 4 | — | OK | DRAFT_TEXT |
| p2-f2 | 4 | 4 (license, unit n/a) | OK | DRAFT_TEXT |
| p5-f1 | 4 | 9 (units qualified) | OK | DRAFT_TEXT |
| p7-f1 | 6 | 8 (series split) | OK | DRAFT_TEXT |
| p8-f2 | 3 | 4 (independent clocks) | OK | DRAFT_TEXT |
| p8-f3 | 3 | 4 (per-artifact license) | OK | DRAFT_TEXT |

Row-level source quality: 79 sub-rows each carry product+URL/clock+class; 29 value-claims carry metric/unit/denominator/model/evidence/archive. Layout for all 20 remains fenced delimiter text — explicitly NOT typeset, NOT renderer-validated.

## 3. P5 numeric class table (value → class)

| Value | Class | Ground |
|---|---|---|
| WER 4.1/4.0 (Small, FLEURS) | COMPARATOR_UNVERIFIED | card gives numbers, no split/comparator |
| cpWER 18.4/18.6 | SOURCE_REPORTED (comparator explicit) | vs Pyannote 19.0 in card |
| recall 94.6/81.4 | COMPARATOR_UNVERIFIED | two-condition split unspecified |
| sub-500ms / 40+ langs | SOURCE_REPORTED (sample stated) | realtime sample condition |
| Mini $0.0035/min | SOURCE_REPORTED (unit confirmed) | /min in card |
| Small $0.004, Realtime $0.008 | UNIT_UNVERIFIED | /min stated for Mini only |
| Speech $13/M chars | SOURCE_REPORTED (unit confirmed) | /M chars in card |
| agent $0.04/$0.08 | UNIT_UNVERIFIED | no invoice unit in card |
| TTS evals 300/300/377/237 + gemini-3.8-flash | SOURCE_REPORTED (vendor-chosen judge) | card claim-2 |
| 50+ STT / 35+ Realtime / 40+ dialects / 11-lang sample | SOURCE_REPORTED (each named) | card claim-1 + Architecture sample label |
| TTS 35+/9/35/18/22 | UNRESOLVED | conflict stands, no simplification |

## 4. 31-requirement 5-state matrix (independent 26/5 baseline adopted)

`SUBSTANTIVE_COMPLETE=26 / PARTIAL=5 / MENTIONED_ONLY=0 / NOT_ADDRESSED=0 / NOT_VERIFIABLE=0`.
PARTIAL (each with truthful limitation, none coerced): §1.4 (Kimi/Nemotron bench comparators vendor-only by design) · §2.2 (recipes exact but NOT_EXECUTED by design) · §4.1 (keyframes live-proof impossible; now UNRESOLVED_FAQ_ATTRIBUTION) · §5.1 (unified TTS count impossible by design) · §5.2 (comparators/units qualified but unverified).
r3.1 self-report 29/2 is superseded for readiness; the delta reflects stricter independent grading of design-level limits, not new defects. `SOURCE_VERIFIED` (16 VERIFIED_DIRECT rows: recomputed arithmetic + exact clocks + archived-byte reads) tracked separately from `EDIT_CLOSED` (r3.2 wording/row repairs).
19 placements, 5 LIMITED, 68 Attention inherited unchanged. Recap: 5 paragraphs after P8, first-line 報告 wording kept, no P9, no editor note.

## 5. Confidence breakdown (96 rows)

VERIFIED_DIRECT 16 / SOURCE_REPORTED 69 / LIMITED 7 / UNRESOLVED 4. Tiers: FIRST_PARTY 79 / DERIVED_ONLY 14 / UNAVAILABLE 3. None implies replicated vendor benchmarks.

## 6. Reader length, same method (R3-SOL-02 method reused)

r3.1 full 33,155 / prose-only 21,431 → r3.2 full 33,557 / prose-only 21,495 (delta +402 / +64: qualifying clauses + row keys, no padding).
r3.1→r3.2 text diff: FAQ 2 rewrites, p5-f1 4-row rewrite, p2-f1 2 label additions, 2 micro-trims, header update; deleted substantive claims: none.

## 7. Residual risks + invariants

Unchanged from r3.1 (FAQ/AA/URL gaps, vendor-only numbers, DRAFT_TEXT layouts, BLOCKED native Stage, unread original report) plus: p8-f1/p2-f1 NOT_RUN/NOT_EXECUTED; TTL 30m is Oct25 observation, not W43 fact.
r1/r2/r3/r3.1 byte-untouched. State `ARCHITECTURE_ESTABLISHED`, Gates, Architecture/Selection/Evidence, main/Frozen Core, shared roots untouched. No Stage/TeX/PDF/Preview/Release/ADVANCE.
