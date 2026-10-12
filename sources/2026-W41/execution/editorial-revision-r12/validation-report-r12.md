# W41 r12 validation report (official validators + fidelity + invariants)

Date: 2026-10-13 JST. No Core/shared-root/main/W40 change. No canonical overwrite.

## Official CLI validations

- `survey_drafting_v2.py draft-check` (canonical package × r12 proposal): P1–P6 all
  `{"passed": true, "errors": []}` (schema, identity, stable refs, attribution,
  must-cover exact-once, boundaries exact-once).
- `synthesis-input` rebuilt from r12 pairs via official CLI; `synthesis-check`
  (proposed input × proposed result): `passed: true` (SHA-fresh, no staleness).
- `validate_agent_state` before/after: PASS / PASS. State remains DRAFT_COMPLETE.

## Coverage / dispositions (validator-enforced)

- must_cover 27/27 mapped to explaining blocks (no blanket assignment).
- Boundaries 42/42 disposed exactly once (2+13+13+4+7+3); OMISSION only for P4 legacy
  trace (×1) and provenance metadata (timestamps/excerpt-granularity ×11), each with
  rationale; all substantive boundaries EXPLICITLY_STATED.

## Audit-item verifications (r11 9 items)

- BLOCKER R11-B01: p5 rewritten to excerpt (5 modalities, 3 encoders, MRL truncation +
  practical meaning with non-superiority caveat, 8K/5.5min/29/58, card/eval boundary kept).
- M01: total/active per audit table in p13 (+memory/compute split, FLOPs caveat);
  r11 misstatement corrected and noted in-prose.
- M02: 49B direct attribution removed; secondary-record + 52B-primary wording used.
- M03: t2 note replaced with recommended wording; Synthesis/NOTE checked for bleed (none).
- M04: p5/t1 billing rewritten to recommended wording (cache-read confirmed, units unknown,
  no estimation, formal table required); GPT-6 vs Haiku distinguished; bench objects stay
  unknown (no formal source available).
- M05: reconciliation doc concludes bounded reading RECONCILED; reader prose uses only
  bounded claims (verified by grep); Architecture bytes unchanged.
- m01: relative dates → absolute (P2 ×2, P3 ×5); remaining 今週 usages are W41-clear.
- m02: p9 generalization split per model (GPT-6 vs Haiku confirmed/unconfirmed layers).
- m03: vendor markings at each measurement group's introduction (p2/p3), no redundant tails.

## Preview fidelity

- `reader-preview-r12.json`: 66 paras, 15,009 body chars, 4 tables, full blocks, change
  table, proposal SHAs, unresolved boundaries. Body equality vs proposals: 6/6 exact.

## Canonical invariants (all verified unchanged)

- `production-state.json`, draft checkpoint, approval, review index, canonical results
  P1–P6, canonical synthesis in/out: all SHAs unchanged (working-tree diff clean for
  these paths). Evidence/Materiality/Selection/Architecture untouched. No TeX/PDF.
  Publication Preview not started.

## Proposal SHAs (v12.0, REVISED)

- P1 `6c05b793…` (12p), P2 `41dad63c…` (12p), P3 `16885606…` (16p),
  P4 `6d3b66c0…` (5p), P5 `f5b455ba…` (12p+2t), P6 `50ca02bc…` (9p).
- Synthesis input `5273d76d…`, result `3e0efa8a…`.

(End of file)
