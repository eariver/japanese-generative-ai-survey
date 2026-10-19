# W42 r27 — r1 versus r26 physical page budget and coverage (NONCANONICAL facts)

Scope: architectural facts (binding r1) vs published physical facts (audited r26 diagnostic). No new measurement beyond citing audited artifacts; occupied area stays UNMEASURED; no per-package fractions are asserted.

## 1. Binding r1 plan (Architecture APPROVED, Human Owner, 2026-10-17)

Source: `sources/2026-W42/architecture-v2.json` (Git blob `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`; sha256 `10058a40…`; `status` field now records downstream progress, plan bytes unchanged).

- `page_plan.target_pages = 28`, `page_plan.max_pages = 30`.
- notes: *"Sol r8 seven-package design: body subtotal 26.5 pages (P1 4.0, P2 2.5, P3 5.0, P4 4.0, P5 3.0, P6 4.5, P7 3.5) plus 1-2 pages opening/methodology/sources; target ~27-30 pages, not a hard cap."*
- 7 packages P1–P7, 28 selected items (materiality `28/14/7/1`), unchanged goals/claims/evidence/basis.
- Approval: `gates/architecture-approval.json` (Human Owner APPROVED 2026-10-17), review `gates/reviews/architecture-r1.json` r1,
  snapshot `gates/reviews/approvals/architecture-r1.json`; `review-index.json` holds exactly one ACTIVE APPROVED row.

## 2. Measured r26 physical print (independently audited, NOT a plan amendment)

Source: `execution/diagnostic-r26/build-manifest-r26.json`; PDF sha256 `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0`,
21 pages, 508624 bytes; independent verdict `CONTENT=PASS / PRINT=PASS_WITH_LIMITATIONS`
(`execution/reviews/independent-w42-r26-focused-reaudit-PASS_WITH_LIMITATIONS-20261019.md`).

- **21 = cover 1 + body 17 + bibliography 3.** No other decomposition is measured.
- Chapter spans (shared physical pages; from audited `review-pages-r26.md`, all 21 PNGs opened):
  P1 p02–p04 · P2 p04–p06 · P3 p07–p09 · P4 p10–p12 · P5 p12–p14 · P6 p14–p16 · P7 p16–p18.
- Table locations: T1 p04 · T2 p06 · T3 p09 · T4 p12 · T5 p14 · T6 p16 · T7 p17 — each caption + ALL rows + cites same page.
- Content retained: 7 chapters, 28 items, 7 tables (27 rows / 110 cells, 0 mismatches vs r18),
  150/150 nonTABLE blocks, 7 captions, 7 notes, 90 bib keys + 19 aliases, 177 ledger lines, 729 cite uses / 90 unique / 0 unknown.
- Residual whitespace: p03 / p11 / p13 lower-page (pre-table atomicity cost), p05 light, p18 body→bib transition —
  same class as r25, area UNMEASURED, aesthetic limitation not a content blocker (independent auditor).

## 3. Budget reconciliation (facts, not a decision)

| quantity | r1 plan | r26 actual | relation |
|---|---|---|---|
| total issue | target 28 / max 30 | 21 | 21 < 28 target (advisory, "not a hard cap"); 21 within max 30 cap |
| body subtotal | 26.5 (7 fractions) | 17 physical shared pages | NOT comparable as 7 fractions: no measured per-package allocation exists; 17 ≠ a re-budget of 4.0/2.5/5.0/4.0/3.0/4.5/3.5 |
| bib | ~1-2 opening/methodology/sources (plan prose) | 3 (B01–B90, 71+19) | physical count; completeness independently verified |
| coverage | 7 pkgs × must-cover + 28 items | all retained, 0 lost | coverage requirement satisfiable under either route |

**17 physical body pages ≠ 17.0 planned body budget.** The "Option B 17.0" figure was an editorial planning estimate
(Sol tentative overall 21/max 23, Human Option B preference for ~17 body pages), never a measured allocation and never
a Human Architecture approval (Sol disposition + reconciliation docs agree). Repeating "17 = 17" as proof of plan
conformance would be false precision. The honest statement: the 21pp diagnostic is content-complete (independent CONTENT=PASS)
and 7 pages under the advisory target with zero coverage loss.

## 4. What is NOT claimed here

- No density measurement, no per-package consumption, no claim that 21pp "satisfies" the 26.5-body plan.
- No padding/deletion/re-research to force 28pp is warranted (independent auditor + Sol disposition concur).
- The r26 diagnostic PDF is NONCANONICAL and is not a Publication Candidate; its page count binds no future formal Reader.
