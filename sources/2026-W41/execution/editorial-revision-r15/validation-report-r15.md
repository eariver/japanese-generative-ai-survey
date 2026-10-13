# W41 r15 validation report (official validators + fidelity + invariants)

Date: 2026-10-14 JST
Authority: `SOL_W41_R14_AUDIT_ACCEPTED / EDITORIAL_REPAIR_AND_READER_PROOF`
No Core/shared-root/main/W40 change. No canonical overwrite.

## Official CLI validations

- `survey_drafting_v2.py draft-check` (canonical package × r15 proposal):
  P1–P6 all `{"passed": true, "errors": []}` (6/6 PASS).
  - P1 `202c90b77b1a…`, P2 `03c1487c2b6e…`, P3 `587283f4370e…`,
    P4 `2d5b5b87658a…`, P5 `c29f7febdd8d…`, P6 `ed95fd791775…`.
- `synthesis-input` rebuilt from r15 pairs via official CLI;
  `synthesis-check` (proposed input `6df8a3bb57bf…` × proposed result
  `516f51d4f61f…`): `passed: true` (SHA-fresh, verified current).
- `validate_agent_state` equivalent: Production State `DRAFT_COMPLETE`,
  `publication_preview: pending`; working tree shows only new
  `execution/editorial-revision-r15/` (canonicals untouched).

## Coverage / dispositions (validator-enforced, architecture-bound)

- must_cover 27/27 mapped to explaining blocks (P5[0] still maps
  p2/p3/t2/p13/t3 with quality substance; no requirement dropped or invented).
- Boundaries 42/42 disposed exactly once (2+13+13+4+7+3); OMISSION only for P4 legacy
  trace (×1) and provenance metadata (×11), each with rationale (carried from r14).
- Evidence refs/modes unchanged r14→r15 for all 6 packages
  (P1 24, P2 26, P3 42, P4 7, P5 26, P6 19 refs; attribution modes intact).
- basis binds exact canonical package SHA + prompt SHA (`b6873133…`); no invented
  source IDs/experiments; no disposition changes; Grok+HOLDs+INSPECTs absent from prose.

## Preview fidelity

- `reader-preview-r15.json` (`15d0ebe66970…`): 67 paras, 16121 body chars,
  5 tables, full blocks. Body equality vs r15 proposals: 6/6 exact
  (P1 16, P2 17, P3 22, P4 7, P5 19, P6 13 blocks).
- Totals delta r14→r15: paras 67→67, chars 16166→16121 (-45 from minimal
  editorial strips/restoration), tables 5→5.

## Canonical invariants (verified unchanged)

- `production-state.json` (`DRAFT_COMPLETE`, preview pending),
  draft checkpoint `ARCHITECTURE_ESTABLISHED`, architecture approval,
  review index, canonical results P1–P6
  (`b1f48362…/7b906ff7…/8ff378d5…/69c61908…/3832bb17…/1cbf2823…`),
  canonical synthesis in/out (`9b4a9fb6…/c953a432…`): all SHAs unchanged
  (working-tree diff clean for these paths; `git status` shows only new r15 dir).
  Evidence/Materiality/Selection/Architecture untouched. No TeX/PDF in this Phase.
  Publication Preview not started.

## Proposal SHAs (v15.0)

- P1 `202c90b77b1a…` (16 blocks, NO_BODY_CHANGE), P2 `03c1487c2b6e…` (17, NO_BODY_CHANGE),
  P3 `587283f4370e…` (22, p9 strip), P4 `2d5b5b87658a…` (7, p3 rewrite),
  P5 `c29f7febdd8d…` (19, p2/p3/p13/t1), P6 `ed95fd791775…` (13, NO_BODY_CHANGE).
- Synthesis input `6df8a3bb57bf…`, result `516f51d4f61f…`.

## Body diff ↔ ledger full match

- Mechanical r14→r15 block-text diff yields exactly 6 changed blocks:
  P3/p9, P4/p3, P5/p2, P5/p3, P5/p13, P5/t1.
- `change-ledger-r15.md` records all 6 with exact Before/After, reason, Source,
  Audit ID, verdict; P1/P2/P6 recorded as NO_BODY_CHANGE (version bump only).
- r13→r14→r15 chain verified: r15 P5/p3 body equals r13 P5/p3 body;
  r14 ledger P5/p3 error separately superseded by `r14-ledger-corrigendum-r15.md`
  (r14 file preserved).

## Guard checks (carried + delta)

- Legacy spans: 0 in reader fields/preview/synthesis-result; 1 lawful P4 machine trace.
- Over-assertions (テキスト除外, 今日落とせる, GrokのX告知は, 試算に使える, 値札付き,
  パートナー由来に限定): 0.
- Internal metadata (revision/audit/deadline/acquisition process, 取得済み,
  記事の時計, 確認した見出し): 0 remaining in changed blocks (verified by diff).
- Relative dates (non-W41-clear): 0. P5 SynthID scope, textGrain numbers/quality table,
  P3 MoE values, P4 Legacy Negative Guard all preserved.

(End of file)
