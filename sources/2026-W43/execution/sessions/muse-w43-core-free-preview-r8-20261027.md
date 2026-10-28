# Muse W43 core-free preview r8 session — 2026-10-27

Branch: `weekly/2026-W43-v2-work`. Start: `88a6ffbb1…` / `e50ff33f…` (remote-verified 6-way; local FF-only from `3b1178ff…`).

Contract: `sources/2026-W43/execution/instructions/sol-w43-core-free-preview-r8-independent-r7-meta-and-prose-replay-closure-20261027.md` (84 lines; parent `be17e994…` verified, single-file diff).

## Steps

1. Guard: `ls-remote` work/main + `rev-parse` trees + frozen object + pre/post-contract checks — all PASS. Drive 401 recorded.
2. Sweep: r7 TeX A/B/C located (l81/l440/l985); r8 built by exact replacement; diff = 3 only; full visible-region + PDF-text sweep — 0 Architecture, no extra meta, protective marks kept.
3. N10: old `check_mutation` reproduced `[]` (qualifiers/tables/recap/verbatim/bib identical) — blind spot. New checker implements `expected = r7+ABC`, full byte/visible/prose identity + 20/80/307, 3 figs, 5 code, 5 recap, 36 bib, 29 anchors, TOC, qualifiers, meta, proof, layout; clean 27/27, negatives 12/12, staged-dir PASS.
4. Build: TinyTeX lualatex ×2 (PATH `~/.TinyTeX/bin/x86_64-linux`) exit 0/0 in r8 dir; PDF 22p 487351B `abd5b99b…`; `main.log` 78170B → tracked `main-tex-log.txt` (`2242237a…`) + 2 stdout txt; aux/toc/out removed; `.log` ignored / `.txt` tracked verified; 2 overfull vbox benign.
5. Render: `gs png16m r150` 22 PNGs + 3 PIL sheets; PyMuPDF text: A p04 / B p11 / C p22, old 0 hits, proof present; links 75/28 unique/0 malformed, fonts 14 embedded, A4 boxes, Unicode ok.
6. QA: all 22 PNGs viewed full-res — no clipping/corruption/wrapping/TOC mismatch; Decisions JSON, 5 recap, bib, marks ok. Raw JSONs + manifest + carryover + PROPOSED re-audit request written.
7. Handoff + this session + index append; final FF non-force commit/push + remote readback (to be recorded in final report).

Terminal: `MUSE_W43_R8_META_P1_AND_PROSE_FIDELITY_READY_FOR_INDEPENDENT_REAUDIT`. No BLOCKED conditions. No State/Gate/Core/main/r1–r7 mutation.
