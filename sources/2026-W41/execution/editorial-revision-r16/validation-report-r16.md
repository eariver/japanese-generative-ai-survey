# W41 r16 validation report (official validators + fidelity + invariants)

Date: 2026-10-14 JST
Authority: `SOL_W41_R15_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_PUBLICATION_REPAIR`
No Core/shared-root/main/W40 change. No canonical overwrite.

## Official CLI validations

- `survey_drafting_v2.py draft-check` (canonical package × r16 proposal):
  P1–P6 all `{"passed": true, "errors": []}` (6/6 PASS).
  - P1 `7494b44c3dd3…`, P2 `a7337ae2110d…`, P3 `557350f3a0fe…`,
    P4 `957fca91fc34…`, P5 `eebd1b5825b4…`, P6 `c841dcfbdf4d…`.
- `synthesis-input` rebuilt from r16 pairs via official CLI;
  `synthesis-check` (input `689fe5776283…` × result `16e53b887ec2…`): PASS.
- State `DRAFT_COMPLETE`, `publication_preview: pending`; working tree shows only
  new r16 dir + publication/v2 additions + W41 TeX tree (canonicals untouched).

## Coverage / dispositions (validator-enforced, architecture-bound)

- must_cover 27/27; boundaries 42/42 (OMISSION only P4 legacy trace ×1 +
  provenance metadata ×11, with rationale, carried).
- Evidence refs/modes unchanged r15→r16 (supplement S1 NOT encoded as Card refs).
- basis binds canonical package SHA + prompt SHA; no invented IDs; no disposition
  changes; Grok+HOLDs+INSPECTs absent.

## Preview fidelity

- `reader-preview-r16.json` (`c1935ede5dd8…`): 67 paras, 16117 body chars,
  5 tables. Body equality vs r16 proposals: 6/6 exact
  (P1 16, P2 17, P3 22, P4 7, P5 19, P6 13 blocks).

## Canonical invariants (verified unchanged)

- `production-state.json`, draft checkpoint, architecture approval, review index,
  canonical results/synthesis: SHAs unchanged (only new edition-local files added).
  Evidence/Materiality/Selection/Architecture untouched. Publication Preview not started.

## Proposal SHAs (v16.0)

- Diffs r15→r16: P1 (p5/t1/p9/p10/p12/n1 pricing), P5 (p6/p7/n1 cleanup);
  P2/P3/P4/P6 NO_BODY_CHANGE (version bump only).

## Body diff ↔ ledger full match

- Mechanical r15→r16 diff yields exactly 9 changed blocks (P1×6, P5×3).
- `change-ledger-r16.md` records all 9 with Before/After, reason, Source
  (supplement S1 vs Card boundary explicit), Audit ID, verdict.
- r15 files preserved; no overwrite.

## Guard checks (delta)

- Changed blocks free of revision/audit/deadline/acquisition metadata,
  `取得済み`, `一次読み`, `text excluded` categoricals; uncertainties retained.

(End of file)
