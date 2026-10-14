# W41 r17 validation report (official validators + fidelity + invariants)

Date: 2026-10-14 JST
Authority: `SOL_W41_R16_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_READER_ACCURACY_REPAIR`
No Core/shared-root/main change. No canonical overwrite.

## Official CLI validations

- `draft-check` (canonical package × r17 proposal): P1–P6 all PASS (6/6).
  P1 `f30b4c1afa2d…`, P2 `296d6eeecdf9…`, P3 `3b18bf4f3253…`,
  P4 `03875d88d188…`, P5 `714134390b1b…`, P6 `c6e448e51676…`.
- `synthesis-input` rebuilt via CLI; `synthesis-check`
  (input `b9baa39dcec5…` × result `df0f020d0670…`): PASS.
- State `DRAFT_COMPLETE`, Preview `pending`; only new r17 + publication/v2
  additions + W41 TeX tree change (canonicals untouched).

## Coverage / dispositions

- must_cover 27/27; boundaries 42/42 (carried rationales intact).
- Refs/modes unchanged r16→r17 (S17 NOT encoded as Card refs).
- basis binds canonical SHA + prompt SHA; no invented IDs; no disposition changes.

## Preview fidelity

- `reader-preview-r17.json` (`ddb0145ad48b…`): 67 paras, 16398 body chars,
  5 tables. Body equality vs r17 proposals: 6/6 exact.

## Canonical invariants

- production-state, checkpoints, approval, review index, canonical results/
  synthesis SHAs unchanged. Evidence/Materiality/Selection/Architecture untouched.

## Diff ↔ ledger match

- Mechanical r16→r17 diff: exactly P1 p5/t1/p9/p12 (prompt-length); all else
  identical. Ledger records all 4 with Before/After, reason, Source, Audit ID.

(End of file)
