# W43 r8 portable independent replay runbook (isolated, no r6/r7 writes)

Date: 2026-10-27 JST. Checker: `sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py` (SHA256 `58abfc0dd3fcb38bc1461a540b62ecbce92ab84eddcd5ed60439489e057e5e98`).

## What it proves

- `R8_EXACT_FIDELITY_PASS` 27/27 clean: actual r8 TeX byte-identical to `expected = immutable r7 TeX (9791a545…, 97572 bytes) + A/B/C only`; visible-body identical; 77 ordinary prose paras identical; 20 tables/80 rows/307 cells; 3 figures; 5 code; 5 recap; 36 bib keys; 29 claim anchors; 11 TOC titles; qualifiers; meta; proof; 32/32 multicols layout.
- `R8_NEGATIVES_PASS` 12/12: same full checker rejects N10 + 11 further mutants on temp copies (see `n10-old-vs-new-replay-r8.md`).

## Isolated replay (no repo mutation)

The checker reads only, writes only stdout JSON (or redirected file you choose). It never writes into `core-free-preview-r6/` or `r7/` namespaces.

Option 1 — in-place repo checkout (read-only plus stdout):

```bash
python3 sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --repo-root . --mode clean
python3 sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --repo-root . --mode negatives
```

Expected: `R8_EXACT_FIDELITY_PASS` 27/27 exit 0; `R8_NEGATIVES_PASS` 12/12 exit 0. JSON `results` list actual causes/exit codes.

Option 2 — staged-dir (fully isolated worktree):

```bash
mkdir -p /tmp/r8stage/sources/2026-W43/execution/core-free-preview-r7 /tmp/r8stage/sources/2026-W43/execution/core-free-preview-r8
cp <repo>/sources/2026-W43/execution/core-free-preview-r7/main.tex /tmp/r8stage/sources/2026-W43/execution/core-free-preview-r7/main.tex
cp <repo>/sources/2026-W43/execution/core-free-preview-r8/main.tex /tmp/r8stage/sources/2026-W43/execution/core-free-preview-r8/main.tex
python3 <repo>/sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --staged-dir /tmp/r8stage --mode clean
python3 <repo>/sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --staged-dir /tmp/r8stage --mode negatives
```

Verified 2026-10-27: staged-dir clean `R8_EXACT_FIDELITY_PASS` 27/27, negatives `R8_NEGATIVES_PASS` 12/12.

Custom TeX path:

```bash
python3 .../r8-exact-fidelity-check.py --repo-root . --tex sources/2026-W43/execution/core-free-preview-r8/main.tex --mode clean
```

## Historical r6 traps (do NOT repeat; r8 checker avoids them by design)

- r6 validator defaults `--out` beside itself: a prior worker run overwrote 2 immutable r6 JSONs (restored via `git checkout --`). r8 checker has no `--out`; it prints JSON to stdout. Redirect explicitly, e.g. `> /tmp/r8-clean.json`, never into `r6/` or `r7/`.
- r6 validator defaults `--test-tex` to r3 file and requires explicit `--test-tex/--test-pdf` for r6 role. r8 checker pins immutable r7 via SHA/bytes (`R-r7-immutable`) and builds expected in-memory; `--tex` only selects the candidate under test.
- r6 38-negatives harness asserts old r3 production note and is NOT re-runnable in r6 role (historical 38/38 stands). r8 12-negatives are self-contained temp-copy mutants via the same full checker; all 12 genuinely introduced (verified `mut != base`) and all correctly rejected.

## Limits (not proven by this join)

- Strict r7→r8 delta only; not independent r3.5 original truth. Prior r6 source→projection→TeX evidence reused only with that limitation.
- Drive audit report unread (401); contract transcription applied.
- PDF visual/font/link facts come from `pdf-page-qa-r8.md` + `pdf-links-fonts-r8.md` (actual PDF bytes), not TeX strings alone.
