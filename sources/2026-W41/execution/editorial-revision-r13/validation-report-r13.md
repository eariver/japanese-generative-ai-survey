# W41 r13 validation report (official validators + fidelity + invariants)

Date: 2026-10-13 JST. No Core/shared-root/main/W40 change. No canonical overwrite.

## Official CLI validations

- `survey_drafting_v2.py draft-check` (canonical package × r13 proposal): P1–P6 all
  `{"passed": true, "errors": []}`.
- `synthesis-input` rebuilt from r13 pairs via official CLI; `synthesis-check`
  (proposed input × proposed result): `passed: true` (SHA-fresh, verified current).
- `validate_agent_state` before/after: PASS / PASS. State remains DRAFT_COMPLETE.

## Coverage / dispositions (validator-enforced)

- must_cover 27/27 mapped to explaining blocks (P5[0] now includes p13/t3 substance).
- Boundaries 42/42 disposed exactly once (2+13+13+4+7+3); OMISSION only for P4 legacy
  trace (×1) and provenance metadata (×11), each with rationale.

## Preview fidelity

- `reader-preview-r13.json`: 67 paras, 16,075 body chars, 5 tables, full blocks, change
  table, proposal SHAs, unresolved boundaries. Body equality vs proposals: 6/6 exact.

## Canonical invariants (verified unchanged)

- `production-state.json`, draft checkpoint, approval, review index, canonical results
  P1–P6, canonical synthesis in/out: all SHAs unchanged (working-tree diff clean for
  these paths). Evidence/Materiality/Selection/Architecture untouched. No TeX/PDF.
  Publication Preview not started.

## Proposal SHAs (v13.0, REVISED)

- P1 `228c1a40…` (12p), P2 `b31355a3…` (12p), P3 `1ddcb712…` (16p),
  P4 `936fb194…` (5p), P5 `ef9316b7…` (13p+3t), P6 `f9a0484e…` (9p).
- Synthesis input `77eee03d…`, result `7435346d…`.

(End of file)
