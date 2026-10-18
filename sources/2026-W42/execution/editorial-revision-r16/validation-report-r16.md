# W42 r16 validation report (frozen validators + diagnostic + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition. No Human Gate operation.

## Frozen CLI validations (all PASS, real receipts)
- `survey_drafting_v2_base.py draft-check` (canonical package × r16 v16.0 proposal): P1–P7 `{"passed": true, "errors": []}` — initial copy, after F-10 fixes, after P3 未開封 fixes (3 consecutive full passes).
- r16: 136 paragraphs / 24,832 paragraph-only chars / 28,144 body-PTN / 7 tables / 7 notes. Per-chapter P1 3,639 / P2 3,575 / P3 4,570 / P4 3,688 / P5 2,856 / P6 3,673 / P7 2,831.
- Reconciliation r14→r15.1→r16 (same definitions): 112/20,479/23,601 → 136/24,162/27,415 → **136/24,832/28,144** (+670/+729 vs r15.1; +24/+4,353 vs r14). F-09 resolved: P+T+N 28,013 + HEADING 131 (20/17/15/21/28/10/20) = PTN 28,144 — the r15.1 "131 unexplained" was headings by definition.
- `synthesis-input` rebuilt via frozen CLI from 7 r16 pairs; result v2.0 (input-SHA `00ef3a3b86e4d94a320e2d04d7d42d7bd11c9267b320d8368c98d3f5b449e637`, runner re-stamped); `synthesis-check` PASS.
- Production State read-only: `DRAFT_COMPLETE`, architecture approved, publication pending (blob verified unchanged at commit; no stage validation run).

## F-01–F-10 dispositions (all repaired, regressions held)
- F-01 Minecraft random world (no fixed seed) + denominators + list-price costs + natural Japanese. F-02 24-tray·96-accelerator (4 body + 1 table instances) + applicability. F-03 ASPIRE real-robot evidence + FIGURE_VALUES_UNRESOLVED + dating. F-04 symmetric 4×2 + Table-5 domains + unresolved splits. F-05 Methods BLOCKED, M02 held, nothing invented. F-06 six pair-groups split by recorded purpose (no deletions). F-07 B69/B73/B88/B86 normalized, B62/B65/B86/B87 aliases, +B89/B90, 177-row ledger (+B60/B61 direct cites wired), TeX from ledger. F-08 point estimates retracted, measured ranges published. F-09 headings accounting. F-10 zero remaining (固定種なし negation retained once as explicit guard).
- Regressions: MTP length/draft-7/temp-split, denominator separation, license tiers, vendor-vs-independent, chronology, Pro negative, r13–r15 history, lifecycle.

## Diagnostic render (NONCANONICAL, not a candidate)
- `diagnostic-r16/main.pdf`: 21 pages, 506,978 bytes, SHA256 `e2919ec...8ac`; TeX 91,280 bytes (`a81b44...`); log 77,225 bytes (`1384c9...`); 136/136 paragraphs verified in TeX; 90/90 bib keys cited; LuaHBTeX 1.24.0; 0 warnings/overfull/underfull/errors/missing-glyphs; 21 PNGs @150dpi + contact sheet, every page opened (review-pages-r16.md).
- Layout: cover 1 + body p2–p18 (17; p18 Table-7-only sparse by float-flush hygiene, recorded) + bib p19–p21 (3). Old r14 p15-partial / p16→17 B48 classes absent. `preview-r15/main.pdf` untouched (STALE v15.0).
- Effective body 15.5–17 vs 26.5 plan → structural gap ~9–11 pages at current density (measured range; see reconciliation). No false PASS.

## Canonical invariants (verified at commit)
- `production-state.json` blob unchanged; checkpoints/approvals/review-index unchanged; canonical Draft/Synthesis v10.0 unchanged; accepted Evidence/Views/Materiality/Selection/Architecture untouched; r11–r15 execution bytes untouched (blob spot-checks); main + Frozen Core untouched.

## Remaining explicit unknowns
- Aptamer Methods thresholds; ASPIRE figure values; Earth repo SHA; Vals methodology/rate card; Maia paper/baseline; Nemotron PDF bytes; HF per-artifact licenses; METR downstream; independent reruns. Pagination decision belongs to Sol/Human (options A/B/C in reconciliation).
