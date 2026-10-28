# J-GAS W43 r8 — Independent Sol re-audit request (PROPOSED, not a report)

Date: 2026-10-27 JST. Status: `MUSE_W43_R8_META_P1_AND_PROSE_FIDELITY_READY_FOR_INDEPENDENT_REAUDIT` (worker claim, NOT independent PASS).
Repository: `eariver/japanese-generative-ai-survey`, branch `weekly/2026-W43-v2-work` (expected post-commit HEAD/Trees to be read back after push).
Executor: **independent Sol**, separate from editorial Sol and Muse Worker.
Submission: Google Drive folder `GPT-Sol_Review`, filename `yyyyMMddHHmmss_SolReview.md` (external, read-only audit; no repo mutation).

## Fixed r8 subject (to be pinned by exact SHA/Tree after worker push)

- Relative r8 path: `sources/2026-W43/execution/core-free-preview-r8/`
- r8 TeX: 97447 bytes, raw SHA256 `4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d`
- r8 PDF: 487351 bytes, raw SHA256 `abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`, 22 A4 pages
- r8 style: `0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44` (byte-identical to r7)
- Fixed r7 pins: HEAD `3b1178ff5140ff03f4291701c346a6329a228a1b`, TeX `9791a545…` / PDF `5d01f496…`
- Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`
- Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

## What changed (authorised only)

r7→r8 TeX diff is ONLY A (Flint table p04), B (FLUX prose p11 whole paragraph), C (bib [recap] p22). See `meta-closure-and-semantic-diff-r8.json`. `preview.sty` identical. 20 tables/80 rows/307 cells (1 cell whitelisted), 3 figures, 5 code, 5 recap, 36 bib, 77 prose paras, 29 anchors, 11 TOC titles preserved. Build logs now tracked (`main-tex-log.txt` + 2 stdout txt); r7 `main.log` gap closed.

## Independent tasks (read-only; do not mutate repo/Gates/State/Core/Release)

1. Verify exact r8 SHA/Tree, remote HEAD/Tree, protected refs; distinguish fixed subject from branch tip. If unverifiable, `AUDIT_PIN_NOT_VERIFIED`.
2. Recompute raw hashes for r8 PDF/TeX/style/logs/pages; corroborate Git blob IDs.
3. Inspect ALL 22 r8 pages at readable/full resolution (new PNGs `p-01..p-22.png`); supply p01–p22 matrix with image hashes; confirm A p04 / B p11 / C p22 corrected, old strings absent, no clipping/corruption/wrapping/TOC mismatch; check long Decisions JSON, 5 recap, bib, both proof marks.
4. Full print-surface meta sweep (article/table/source notes/bib/cover); verify 3 closures + no new leaks; distinguish genuine caution from workflow language.
5. Replay `r8-exact-fidelity-check.py` clean (expect 27/27) + negatives (expect 12/12) via `portable-independent-replay-r8.md` staged-dir; add ≥1 novel adversarial mutant beyond saved 12 with actual result; state static vs executed.
6. If able, isolated-temp LuaLaTeX rebuild (no repo writes): capture exits/log, compare visual/semantic (not byte-identical).
7. Verify PDF annots (28 unique http vs 36 keys), official Decisions Guide, `%2F` npm URL, A4 boxes, Unicode, 14 embedded fonts; state `NOT_VERIFIED` where unsupported.
8. Architecture/bib governance bounds (no authority change); distinguish worker claim vs auditor-executed vs inspected vs unverified.

Terminals: `INDEPENDENT_W43_R8_PDF_PASS` / `SEMANTIC_PASS_VISUAL_BLOCKED` / `REQUEST_CHANGES` / `INCONCLUSIVE`. Report externally to Drive, verify readback, give exact URL. No freeze/release/PR/merge; Human PDF Gate PENDING; Core-native Draft BLOCKED.
