# W42 r17 validation report (frozen validators + diagnostic + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition. No Human Gate operation.

## Frozen CLI validations (all PASS, real receipts)

- `survey_drafting_v2_base.py draft-check` (canonical package × r17 v17.0 proposal): P1–P7 `{"passed": true, "errors": []}` (7/7, single run post-repair; command `PYTHONPATH=. python3 scripts/survey_drafting_v2_base.py draft-check --package sources/2026-W42/draft/v2/packages/PX/draft-package.json --result sources/2026-W42/execution/editorial-revision-r17/proposals/PX/draft-result-r17.PROPOSED.json`).
- r17: 136 paragraphs / 25,085 paragraph-only chars / 28,281 P+T+N / 28,412 PTN / 7 tables (2,255 chars) / 7 notes (941 chars) / headings 131 chars. Per-chapter P1 3,654 / P2 3,803 / P3 4,570 / P4 3,688 / P5 2,858 / P6 3,609 / P7 2,903. Deltas r16→r17: +0 paras / +253 P / +268 PTN (precision qualifications; P6 −64 dedup; no padding).
- `synthesis-input` rebuilt via frozen CLI from 7 r17 pairs → `proposed-profile-synthesis-input.json` (input-SHA `e1d4f477eac09ae4176fc5eee13df3e42bf48d4aef7cd504e27096de32651d15`); result v2.0 re-stamped (runner `muse-w42-r17-final-editorial-bibliography-layout-repair`, 2026-10-18T06:30:00Z); `synthesis-check` PASS.
- Production State read-only: `DRAFT_COMPLETE`, architecture approved, publication pending (blob verified unchanged at commit; no stage validation run).

## F16 dispositions (bounded repairs, regressions held)

See `finding-closure-matrix-r17.md` for old/new + verification + unknowns. F16-01..08 PASS (bounded), F16-09 MEASURED. Translationese zero P1–P7/TeX. 90/90 parser-valid, 177/177 ledger-valid, 7/90 HTTP-verified (rest UNVERIFIED). Table-7 in-body p17, no orphan. Bibliography readable, alias cross-refs, no invented titles.

## Diagnostic render (NONCANONICAL, not a candidate)

- `diagnostic-r17/main.pdf`: 21 pages, 512,182 bytes, SHA256 `6b673a9329ec02d41cf22f6a6a634a315d8d5ad480f6d7274c5f5c7b4ffb5b8e` (deterministic SOURCE_DATE_EPOCH=2026-10-18T06:30:00Z, final two runs byte-identical); TeX 97,014 bytes (`ee28a6c1…`); log 77,227 bytes (`75aa811d…`); 136/136 paragraphs verified in TeX; 90/90 bib keys cited; LuaHBTeX 1.24.0; 0 warnings (excl. pkg info) / 0 overfull / 0 underfull / 0 errors / 0 missing glyphs; HaranoAji + LM fonts.
- Visual: 21 PNGs @150dpi + 3 split contact sheets (each fetchable, vs r16 12.5MB single); every page opened (review-pages-r17.md). Cover stamped; body p2–p17 (Table-7 p17 in-body with text, ex-orphan eliminated); bib p18–p21 readable (B57 ASPIRE URL ASPI/RE carry p19→p20 minor noted). No clipped glyphs, no isolated table page, no cross-chapter floats.
- Effective body 15.5–17 vs 26.5 plan → structural gap, measured (see pageplan brief). No false PASS. preview-r15 untouched (STALE).

## Canonical invariants (verified at commit)

- `production-state.json` blob unchanged; checkpoints/approvals/review-index unchanged; canonical Draft/Synthesis v10.0 unchanged; accepted Evidence/Views/Materiality/Selection/Architecture untouched; r11–r16 execution bytes untouched (blob spot-checks); main + Frozen Core untouched.

## Remaining explicit unknowns

Aptamer Methods thresholds (DIRECT_FETCH_TOOL_LIMIT); ASPIRE figure values; Earth repo SHA; Vals methodology/rate card; Maia paper/baseline; Nemotron PDF bytes; HF per-artifact licenses; METR downstream; independent reruns; 83/90 HTTP UNVERIFIED; B57 2-char URL carry. Pagination decision belongs to Sol/Human (options A/B/C).
