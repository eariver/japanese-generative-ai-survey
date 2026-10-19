# W42 r29 independent semantic/visual audit request (PROPOSED, no outcome)

To: separate independent Sol (not the r29 builder)
From: Muse Spark (W42 r29 canonical build worker)
Date: 2026-10-20 JST
Boundary: `STOP_AT_INDEPENDENT_REVIEW / NO_STAGE_NO_GATE`

## 1. Exact audit targets (use committed bytes only)

- TeX: `surveys/weekly/2026-W42/main.tex` SHA256 `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3` (96790 bytes)
- PDF: `surveys/weekly/2026-W42/main.pdf` SHA256 `8c7a06e7e71e5945a2845e87e029ed9d33dcc168e8597ce055238fcc126d79f9` (505102 bytes, 21 pages)
- Style: `surveys/weekly/2026-W42/preview.sty` SHA256 `f0492fb6b2b9085f282a12120885b20271ec11b0fab56d8848d6f0ee474d534d`
- Manifest: `sources/2026-W42/publication/v2/reader-manuscript-v2.json` content digest `78d9928ded5ec663c7f25a028135fa05cf5411a2ecc0a0c1bb407eb9f02708e0`
- Pages: `sources/2026-W42/execution/publication-build-r29/pages/p-01.png`..`p-21.png` + 3 contact sheets + `main.log` + `build-manifest-r29.json`
- Provenance: `canonical-build-provenance-and-diff-r29.md`; fidelity: `reader-fidelity-and-bibliography-parity-r29.md`; print ledger: `physical-print-page-and-table-ledger-r29.md`; coverage: `reader-manifest-and-architecture-coverage-r29.md`

Basis (immutable, not re-audited here): r18 Reader blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`; r26 diagnostic TeX blob `ffdd45742c16fc2f19fd21805479ca9d8373f30b` / PDF `c76f4a6e9...` / style `f0492fb6...`; Architecture r1 approved; Route A ~21pp acceptance; r26 CONTENT=PASS / PRINT=PASS_WITH_LIMITATIONS (for r26 bytes only).

## 2. Formal questions

Semantic/editorial:

1. Does the 21-page canonical PDF preserve all 7 chapters / 28 topics / 157 blocks / 7 tables (27 rows / 110 cells) / 150 nonTABLE inclusions / 90 keys / 19 aliases / 177 ledger rows without substantive change?
2. Are B citation resolution (729 uses / 90 distinct / 0 missing), 71 URLs, B28/B57/B74/B90, 17 secondary badges, and all listed caveats intact?
3. Is the neutral cover (`週刊Technical Survey`, no diagnostic stamp, no APPROVED/RELEASED claim) editorially appropriate? Does any cover/metadata change alter meaning?
4. Does architecture coverage (27 requirements → Sections 1–7) truthfully locate each must-cover? Are FINAL_SYNTHESIS (Sec 7 tail) and WEEKLY_COMMUNITY_MOVEMENT (Secs 1–3 X-post discipline) genuinely placed?
5. Are previously closed r25 blockers (T2 LFM2.5, T3 Nemotron) still closed in canonical PDF text + PNGs?

Visual/print:

6. Are all 7 tables caption+rows on same physical page within own chapter, with no orphan caption, footer collision, or sentence bisection?
7. Is chapter order P1→P7 intact with no story interrupted by full-width tables? Is terminal P7/bibliography B90 readable to end with no missing glyphs/URL clipping?
8. Are residual whitespace (p03/p11/p13, lighter p05/p18) within Route A acceptance? Any new pagination regression vs r26 page map?
9. Compiler: 0 errors/warnings confirmed in `main.log`; do PNGs show any unlogged visual defect?

Process:

10. Confirm no `ADVANCE_STAGE`, Candidate, Gate, Freeze, Release, or State mutation is warranted at this boundary; confirm build remains `DRAFT_COMPLETE / PUBLICATION_UNAPPROVED`.

## 3. Previously closed errors (must remain closed)

- r25 BLOCKER-01 (T2 short form) and BLOCKER-02 (T3 `未開封`) were closed by independent r26 audit; r29 preserves exact restored cells (see fidelity report).
- r22 top-float bisection, r24 caption orphan + Decider clip: not recurring per r29 PNGs (to be independently confirmed).

## 4. Explicit non-claims

This request creates no `semantic-review`, `visual-review`, `reader-surface-gate`, or `quality-regression-bundle` PASS; no Publication Candidate; no Bridge request; no Human Gate decision. The builder's deterministic checks are not an independent review. Await your separate read-only audit verdict on the exact hashes above.
