# W41 r14 validation report (official validators + fidelity + invariants)

Date: 2026-10-13 JST. No Core/shared-root/main/W40 change. No canonical overwrite.

## Official CLI validations

- `survey_drafting_v2.py draft-check` (canonical package × r14 proposal): P1–P6 all
  `{"passed": true, "errors": []}`.
- `synthesis-input` rebuilt from r14 pairs via official CLI; `synthesis-check`
  (proposed input × proposed result): `passed: true` (SHA-fresh, verified current).
- `validate_agent_state` before/after: PASS / PASS. State remains DRAFT_COMPLETE.

## Coverage / dispositions (validator-enforced)

- must_cover 27/27 mapped to explaining blocks (P5[0] includes p13/t3 substance).
- Boundaries 42/42 disposed exactly once (2+13+13+4+7+3); OMISSION only for P4 legacy
  trace (×1) and provenance metadata (×11), each with rationale.

## Preview fidelity

- `reader-preview-r14.json`: 67 paras, 16,166 body chars, 5 tables, full blocks, change
  table, proposal SHAs, unresolved boundaries. Body equality vs proposals: 6/6 exact.

## Canonical invariants (verified unchanged)

- `production-state.json`, draft checkpoint, approval, review index, canonical results
  P1–P6, canonical synthesis in/out: all SHAs unchanged (working-tree diff clean for
  these paths). Evidence/Materiality/Selection/Architecture untouched. No TeX/PDF.
  Publication Preview not started.

## Proposal SHAs (v14.0, REVISED)

- P1 `ffa57786…` (12p), P2 `87bb7d16…` (12p), P3 `5ff9d8b0…` (16p),
  P4 `55b1039c…` (5p), P5 `b5ebe134…` (13p+3t), P6 `d62d87b8…` (9p).
- Synthesis input `8ff447f7…`, result `5114ebd0…`.

(End of file)
