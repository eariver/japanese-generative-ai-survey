# r6 portable runbook (Phase A verifier + evidence)

Validator: `sources/2026-W43/execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py`
`--help` lists all inputs. No hardcoded repository paths. No network.
No Core dependencies beyond edition-local immutable originals + the r3.5
strict claim checker (read-only AST import).

## Canonical invocations (from any working directory)

All commands below were executed with exit codes as recorded. Replace
`$REPO` with the checkout under test (read-only use is sufficient).

### 1. Clean full-join (r3 print subject, tex-role r3)

```
python3 $REPO/sources/2026-W43/execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py \
  --repo-root $REPO --mode clean --tex-role r3 \
  --out $REPO/sources/2026-W43/execution/core-free-preview-r6
# exit 0
# verdict R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED, 36/36 checks PASS
# writes full-segment-join-clean-r6.json + six-input-identity-and-mutant-binding-r6.json
```

### 2. Negatives (same entrypoint, in-memory mutants, hash-bound)

```
python3 $REPO/sources/2026-W43/execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py \
  --repo-root $REPO --mode negatives \
  --out $REPO/sources/2026-W43/execution/core-free-preview-r6
# exit 0
# verdict NEGATIVES_PASS, 38/38 cases PASS
# (37 expect-fail with asserted cause + old-scope-blindness where mandated,
#  1 R6-TEX-PRINT-ONLY-DELETE control expecting ALL_PASS)
# writes full-segment-join-negatives-r6.json
```

### 3. Offline staged replay (independent auditor without repo layout)

Mirror the seven required relative paths under `$STAGE` (see manifest in
`six-input-identity-and-mutant-binding-r6.json`, key `inputs.*.path`),
then:

```
python3 <script> --staged-dir $STAGE --mode clean --tex-role r3 --out $STAGE_OUT
# exit 0, verdict R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED, 36 checks
python3 <script> --staged-dir $STAGE --mode negatives --out $STAGE_OUT
# exit 0, verdict NEGATIVES_PASS, 38 cases
```

Missing inputs fail loudly (`MISSING_INPUT` naming the absent role);
nothing is invented. Ephemeral mutants are distinguished from absent paths
(`MUTATED_INPUT` hash binding vs `MISSING_INPUT`).

### 4. r6 print-subject verification (after Phase B writes real r6 files)

```
python3 <script> --repo-root $REPO --mode clean --tex-role r6 \
  --test-tex $REPO/sources/2026-W43/execution/core-free-preview-r6/main.tex \
  --test-pdf $REPO/sources/2026-W43/execution/core-free-preview-r6/main.pdf \
  --out <r6dir>
# H00 still pins the six immutable ORIGINAL inputs (r3 TeX/PDF by their
# committed paths); the new r6 pair is the tested subject, hash-recorded
# separately, and must satisfy the full join with exactly the
# AUTHORIZED_PRINT_ONLY_DELETION allowlist.
```

## Check accounting (counted, not estimated)

- Clean: 36 checks — H00 H01 S01 S02h-rp S02h-pt S03a S03b S04a S04b S05
  S06 S07a S07b S07c S08a S08b S08c S08d S08e S09a S09b S10 S11a S11b S12
  S13a S13b S13c S13d S13e S13f S13g S13h S13i S14 S15.
  (r5 reported 22 clean checks with a '24' handoff typo; this log counts
  the actual 36 and does not reuse the wrong number.)
- Negatives: 38 cases =
  8 mandated full-scope (N-AUD-RECAP-SEMANTIC-REVERSAL exact TeX-side replay,
  N-RECAP-PROJ-DIVERGENCE companion, N-PARA-DELETE, N-FIG-EDGE, N-CODE-ENV,
  N-PARA-SWAP, N-TEX-RECAP-DESTROY, N-TEX-ONLY-ALTER),
  21 carried table/cell/claim/url/qualifier scope (single TeX row-swap
  deduplicated per contract; N-claim-rows-swap retained),
  6 per-input hash corruptions (one per pinned input),
  3 r6-state (R6-TEX-PRINT-ONLY-DELETE control, N-PRINT-NOTE-LEAK,
  N-R6-TEX-ALTER).

## Failure semantics

- Any clean FAIL ->
  `MUSE_W43_R6_FULL_VISIBLE_FIDELITY_BLOCKED` (exit 1), no Phase B.
- Any negative not detected ->
  `NEGATIVES_FAIL` (exit 1); the checker is not coverage-adequate.
- Clean PASS + negatives PASS is fidelity proof only, never an
  independent acceptance, Human approval, Stage, Freeze, or Release.

## Byte provenance of this run

Recorded `sha256sum` outputs (recompute to verify):

- validator `full-reader-visible-segment-join-r6.py`:
  `7c09cdce18ea6da21880e0d8a4660a7480e7da38bdd5d6447bc03404179c7d18`
  (recompute after any edit; outputs below bind to the exact script bytes)
- `full-segment-join-clean-r6.json` (r6-role on real r6 files):
  `f6cc3c1ebcb72f0f54871cd4bc8317d60eada2709e2fadbe2acbd71e678de90e`
  `full-segment-join-clean-r6-baseline-r3.json` (r3-role baseline):
  `b74d215e5b4e1826d08b6ee7be53de9c71d8f57122e89a474d9b4417f436ec63`
  `full-segment-join-negatives-r6.json`: `5569991376d1ba1afb11b8b63d17981d7f5d4c94a033e3b65e4951f2a5918852`
  `six-input-identity-and-mutant-binding-r6.json`: `acf9ba733e7f104a6614878559670e93443ce6cba632ef623ae428fb360c3805`
  (see also the session notes at commit time:
  `sessions/muse-w43-core-free-preview-r6-20261027.md`).

Python: 3.14.4 (stdlib only: argparse/ast/difflib/hashlib/json/pathlib/re).
No third-party packages, no TeX engine required for Phase A.
