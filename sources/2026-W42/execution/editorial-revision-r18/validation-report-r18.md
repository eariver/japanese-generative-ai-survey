# W42 r18 validation report (frozen validators + reader-surface gate + diagnostic + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition. No Human Gate operation.

## Frozen CLI validations (all PASS, real receipts)

- `survey_drafting_v2_base.py draft-check` (canonical package × r18 v18.0 proposal): P1–P7 `{"passed": true, "errors": []}` (7/7).
- r18: 136 paragraphs / 25,015 paragraph-only chars (−70 vs r17 from S17-01 leak removal: P1 3,634 / P2 3,803 / P3 4,570 / P4 3,688 / P5 2,858 / P6 3,581 / P7 2,881). Tables 7 / notes 7 / headings unchanged. 90 bibliography keys / 19 aliases / 177 ledger rows (copied audited r17 versions, unchanged evidence info).
- `synthesis-input` rebuilt via frozen CLI from 7 r18 pairs (input-SHA `4cb2b01ae56ab51902ea27b1bded09e6306e164c285115812157cb4e9a3284cb`); result v2.0 re-stamped; `synthesis-check` PASS.
- Production State read-only: `DRAFT_COMPLETE`, architecture approved, publication pending (no stage validation run).

## Independent reader-surface gate (PASS, beyond frozen checks)

- Pattern `t[1-7]-[0-9]{2,}` over r18 reader texts (blocks + headline/deck): 0 hits. File-path / CLAIM_BOUNDARY / accepted_context_notes / frozen-op / placeholder patterns: 0 hits. 7 legitimate external codes accepted with per-hit rationale (Muse-license ×2, Sol-model ×5; see closure doc).
- TeX body (cites/labels stripped): 0 hits. Extracted r18 PDF text: 3 old leak strings absent. Visual p3/p14/p17: no IDs printed.
- Frozen draft-check does NOT cover this class (r17 passed 7/7 with leaks present); gate run independently. Verdict: PASS.

## Diagnostic render (NONCANONICAL, not a candidate)

- `diagnostic-r18/main.pdf`: 21 pages, 511,523 bytes, SHA256 `d42510f975cbfb60db52ef29e55eb6209214512e439d592c578990c934701683` (deterministic SOURCE_DATE_EPOCH, final two runs byte-identical); TeX 96,865 bytes; log 77,225 bytes; 0 warnings (excl. pkg info) / 0 overfull / 0 underfull / 0 errors / 0 missing glyphs; HaranoAji + LM. 136/136 paragraphs in TeX verified (3/3 r18 swaps byte-checked); 90/90 bib keys cited.
- TeX regenerated from exact r18 JSON bytes (r17 layout template + 3 verified paragraph swaps + B57 needspace; documented method, not masquerade). Table 7 in-body p17 kept; no orphan; no drift/clipping/whitespace/body-bib mixing. B57 entry kept together on p20 (intra-entry ASPI/RE wrap readable; page-top orphan gone). Residual: B28 URL `lein` 4-char carry at p19 top (minor, readable, documented).
- Visual: 21 PNGs @150dpi + 3 split contact sheets (~2.2MB each); pages opened for QA (cover, p3/t1-23 fix, p14/t6-08 fix, p17/Table-7 + t7-19 fix, p20/B57, bib boundaries). Body p2–p17 (16pp physical, effective ~15.5–17) + bib p18–p21 (4pp). preview-r15 untouched (STALE); r16/r17 originals untouched.

## Canonical invariants (verified at commit)

- `production-state.json` blob unchanged; checkpoints/approvals/review-index unchanged; canonical Draft/Synthesis v10.0 unchanged; accepted Evidence/Views/Materiality/Selection/Architecture untouched; r11–r17 execution bytes untouched; main + Frozen Core untouched.

## Remaining explicit unknowns

Aptamer Methods (DIRECT_FETCH_TOOL_LIMIT); ASPIRE figure values; Earth repo SHA; Vals methods/rate; Maia baseline; Nemotron PDF bytes; HF per-file licenses; METR downstream; independent reruns; 83/90 HTTP UNVERIFIED (r17); B28 4-char URL carry. Pageplan decision belongs to Sol/Human via PROPOSED brief.
