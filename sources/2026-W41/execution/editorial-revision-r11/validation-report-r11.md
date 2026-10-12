# W41 r11 validation report (official validators + fidelity + invariants)

Date: 2026-10-13 JST. No Core/shared-root/main/W40 change. No canonical overwrite.

## Official CLI validations

- `survey_drafting_v2.py draft-check` (canonical package × r11 proposal): P1–P6 all
  `{"passed": true, "errors": []}` (schema, identity, stable refs, attribution).
- `synthesis-check` (proposed input × proposed result): `passed: true`.
- Proposed synthesis input built via official `synthesis-input` CLI from the 6 proposal
  pairs (embeds current proposal SHAs — verified current, no staleness).
- `validate_agent_state` before/after: PASS / PASS. State remains DRAFT_COMPLETE.

## Coverage / dispositions (validator-enforced)

- must_cover 27/27 mapped to explaining blocks (exact-once, no blanket).
- Boundaries disposed exactly once per package (P1:2, P2:13, P3:13, P4:4, P5:7, P6:3);
  OMISSION used only for legacy trace (P4×1) and provenance metadata
  (timestamps/excerpt-granularity: P2×3, P3×3, P4×2, P5×3), each with rationale.

## Preview fidelity

- `reader-preview-r11.json`: 66 paras, 14,555 body chars, 4 tables (P1/P3/P5×2),
  full blocks, change table per package, proposal SHAs, unresolved boundaries.
- Body equality vs proposals: 6/6 exact match (programmatic).

## Canonical invariants (all preserved)

- `production-state.json`: DRAFT_COMPLETE, unmodified (SHA unchanged).
- Draft checkpoint `ARCHITECTURE_ESTABLISHED.json`: SHA unchanged.
- Architecture approval + review index: SHA unchanged.
- Canonical results P1–P6 + canonical synthesis in/out: SHAs unchanged (verified).
- Evidence/Materiality/Selection/Architecture: untouched. TeX/PDF: absent.
  Publication Preview: not started.

## Proposal SHAs (v11.0, REVISED)

- P1 `b447caec…` (12p), P2 `e3a716eb…` (12p), P3 `354095a7…` (16p),
  P4 `fc755aef…` (5p), P5 `8653652b…` (12p+2t), P6 `382efd63…` (9p).
- Synthesis input `5273d76d…`, result `3e0efa8a…`.

(End of file)
