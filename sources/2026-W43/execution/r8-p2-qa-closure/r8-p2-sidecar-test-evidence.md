# r8 P2-02 sidecar test evidence (Muse-executed; NOT independent Sol PASS)

Date: 2026-10-27 JST. All runs local, read-only (no r6/r7/r8 writes; stdout redirected to sidecar files only).

## Locked inputs (immutable)

- r7 TeX `9791a545c1ed363f8abace62c90bdbfe15f31dac4017b80a5109907c35509ea0` (97572B)
- r8 TeX `4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d` (97447B)
- orig checker `r8-exact-fidelity-check.py` `58abfc0dd3fcb38bc1461a540b62ecbce92ab84eddcd5ed60439489e057e5e98`
- Python 3.14.4, stdlib only. Wrapper `r8-p2-negative-taxonomy-sidecar.py` (this sidecar).

## Executed (Muse environment)

1. Original checker clean (fixed r8, for reference; immutable JSON already committed):
   - `python3 sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --repo-root . --mode clean` → `R8_EXACT_FIDELITY_PASS` 27/27, exit 0
   - `… --mode negatives` → `R8_NEGATIVES_PASS` 12/12, exit 0 (incl. `N-operator-insert … got ['PROSE_FIDELITY_LOSS']`)
2. Sidecar strict (new, `r8-p2-sidecar-strict-all.json` `f053e512…`, stderr empty `e3b0c442…`):
   - `python3 sources/2026-W43/execution/r8-p2-qa-closure/r8-p2-negative-taxonomy-sidecar.py --repo-root . --mode all` → `SIDECAR_STRICT_PASS` 5/5, exit 0
   - `clean-strict` PASS (27/27 under the hood, 0 fail causes)
   - `N-operator-insert-original-baseline` INFO, actual old causes `['PROSE_FIDELITY_LOSS']` (measured, not guessed)
   - `N-operator-insert-strict` PASS — mutant `c71ecb7026c9…` (97483B, base 97447B, verified `mut != base`) elicits BOTH `READER_META_LEAK` (via controlled `編集承認ゲート通過済み` taxonomy) AND `PROSE_FIDELITY_LOSS`, ALL required
   - `N10-prose-semantic-inversion-strict` PASS — mutant `a62d0c8ac2b6…` (97426B), `['PROSE_FIDELITY_LOSS']` all-required
   - `N13-ming-vendor-quote-to-independent-measurement-strict` PASS — anchor `発行元引用として扱う` count verified == 1 (P5 l537) → `独立測定結果として扱う`; mutant `9cdfc15533c7…` (97450B), `['PROSE_FIDELITY_LOSS']` all-required; distinct material delta (vendor-handling → independent-measurement claim), tables/rows/figs/bib totals unchanged
   - Per-mode exit codes all 0 (`clean`, `operator-baseline`, `strict-operator`, `n10`, `n13`); staged-dir replay (`/tmp/p2stage` with repo-relative paths) → `SIDECAR_STRICT_PASS` 5/0
3. No-op / malformed guards: every mutant SHA differs from clean `4ed553e5…`; byte counts differ; N13 anchor pre-checked == 1; strict evaluator requires non-empty causes AND all expected (no `any()`-only, no stale-hash pass).

## Awaiting independent execution (NOT_RERUN by Muse)

- Independent runner must re-execute §2 in their own checkout/staged-dir per `r8-independent-verification-runbook.md` and report actual terminal, exit codes, and any divergence. GitHub connector-only audit is insufficient for Python/PDF/LuaLaTeX execution (see runbook). Until then, external terminal legitimately remains INCONCLUSIVE-adjacent; Human PDF Gate stays PENDING.
- Independent must also add ≥1 NEW scientific mutant beyond saved 12+N13 and verify actual detection (not spelling variant).
