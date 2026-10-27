# W43 r8 N10 old-vs-new replay (ordinary-prose semantic inversion)

Date: 2026-10-27 JST. Isolated memory/temp replay; no r7 repository mutation.

## N10 definition (independent audit, P2)

- OLD (r7 `main.tex` l34, P1 two-column ordinary prose): `MoonshotのKimi K3.1 Proは10月23日の告知とAPI提供が先行し、重み配布は11月4日の将来予定である。`
- MUTANT: `MoonshotのKimi K3.1 Proは10月23日の告知後、API提供も重み配布もすべて終了した。`
- Effect: scientific inversion (future distribution → all terminated), tables/codes/bib unchanged, critical marker counts unchanged.

## Pre-fix: original r7 `check_mutation` blind spot (ACTUAL)

Command (in-memory, same logic as `sources/2026-W43/execution/core-free-preview-r7/r7-reader-surface-semantic-join.py:check_mutation`):

- `base = r7 TeX`, `mut = base.replace(OLD, MUTANT)`
- `causes = check_mutation(base, mut)`

ACTUAL result (2026-10-27 run):
- `causes = []` (empty, no failure cause)
- Qualifier counts unchanged: `未検証` 23→23, `未実行` 8→8, `発行元測定` 14→14, `独立再現なし` 10→10, `未取得` 33→33
- `parse_r7_tables` identical, `parse_recap_r7` identical, `parse_verbatims` identical, `parse_bibkeys` identical
- Verdict: NOT DETECTED (old checker PASSes a material semantic inversion). Root cause: `check_mutation` only compares tables/recap/verbatim/bibkeys + qualifier counts + meta/layout/proof; ordinary P1–P8 narrative prose never compared. The saved r7 `run_negatives` N10 stub (`swap_rows` returning input unchanged) never actually mutates, compounding the gap.

Old r7 negatives claim `NEGATIVES_PASS 9/9` therefore does not cover N10.

## Post-fix: new r8 checker N10 rejection (ACTUAL, same checker as clean)

Checker: `sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py` (`R8_EXACT_FIDELITY_PASS` 27/27 clean; `R8_NEGATIVES_PASS` 12/12).

- Expected = immutable fixed r7 TeX (`9791a545…`, 97572 bytes) + exactly A/B/C substitutions (97447 bytes).
- Mutant temp copy = clean r8 TeX with ONLY N10 OLD→MUTANT applied (verified `mut != base`).
- Full clean logic run on mutant (no oracle shortcut): `S-exact-bytes` FAIL, `S-visible-body-identity` FAIL, `S-prose-count` 77 vs 77 but `S-prose-identity` FAIL (1/77 paras differ) → cause `PROSE_FIDELITY_LOSS`.

ACTUAL negatives run (2026-10-27):
- `N10-prose-semantic-inversion: PASS (expected ['PROSE_FIDELITY_LOSS'], got ['PROSE_FIDELITY_LOSS'])`
- Clean verdict `R8_EXACT_FIDELITY_PASS` (27/27) vs mutant correctly FAILs clean (would be `FAIL`, not `PASS`), proving detection is genuine, not stale/malformed-input pass.
- All 12 negatives use THE SAME full r8 checker as clean; no global token bag, count-only oracle, missing-paragraph skip, or excessive normalization. N10 detected even though all counts/keywords unchanged.

## Additional 11 negatives (same-checker, temp copies, all PASS = correctly rejected)

- qualifier reversal (Nemotron effective): `PROSE_FIDELITY_LOSS`
- FLUX unverified FAQ→confirmed contradiction: `PROSE_FIDELITY_LOSS` + `READER_META_LEAK` (B whitelist broken — correct)
- numeric cell 2.8T→9.9T: `PROSE_FIDELITY_LOSS` + `ROW_CELL_CLAIM_LOSS`
- clock GH/npm swap: `PROSE_FIDELITY_LOSS` + `ROW_CELL_CLAIM_LOSS`
- adjacent prose paragraph swap: `PROSE_FIDELITY_LOSS`
- figure body mutation: `PROSE_FIDELITY_LOSS` + `ROW_CELL_CLAIM_LOSS`
- code token `gpt-6-luna`→`gpt-9-omega`: `PROSE_FIDELITY_LOSS` + `ROW_CELL_CLAIM_LOSS`
- recap paragraph mutation: `PROSE_FIDELITY_LOSS` + `ROW_CELL_CLAIM_LOSS`
- bib key deletion `tanstack-npm`: `PROSE_FIDELITY_LOSS` + `ROW_CELL_CLAIM_LOSS`
- unknown operator sentence insertion (`編集承認ゲート通過済み`): `PROSE_FIDELITY_LOSS` (detected; meta-pattern extension left to Sol)
- proof `NOT A PUBLICATION PREVIEW`→`APPROVED PUBLICATION`: `PROSE_FIDELITY_LOSS` + `DOC_PROOF_STATUS_MISSING`

Full JSON: `r8-fidelity-negatives.json` (`35a6687f2406b5a15213c329bdf64bf42d99c4a6a9c04f7f8991348e4477f28f`). Clean JSON: `r8-fidelity-clean.json` (`6257b330b6196cace402b0e849e9cbd36da211cdec5165dc4e80466c91d2fdea`).
