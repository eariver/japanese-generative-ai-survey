# Portable independent replay runbook (r7)

Goal: let the independent auditor re-execute every replayable r7 check
without Muse's checkout, read-only, no network, no Core dependencies.

## Staged layout (checkout-free)

```
STAGED/
  r6-main.tex        # fixed r6 TeX (bytes of r6 commit path)
  r7-main.tex        # new r7 main.tex (this namespace)
  r7-preview.sty
  r6-baseline.json   # r6-baseline-replay-clean-r7witness.json (this namespace)
```

## Single commands (from repo root `eariver/japanese-generative-ai-survey`)

```bash
# 1. r6 historical baseline (proves r3.5→r6 carried scope; --out isolates writes!)
python3 sources/2026-W43/execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py \
  --repo-root . --tex-role r6 --mode clean \
  --test-tex sources/2026-W43/execution/core-free-preview-r6/main.tex \
  --test-pdf sources/2026-W43/execution/core-free-preview-r6/main.pdf \
  --out /tmp/r6replay
# expect: R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED, RC=0.
# NOTE: omitting --test-tex/--test-pdf validates r3 defaults and FAILS S07c
# (worker methodology trap, documented in build-manifest-r7.json §method).
# NOTE: omitting --out OVERWRITES immutable r6 JSONs (validator writes
# beside itself by default); worker did this once and restored via
# `git checkout --` (recorded, not hidden).

# 2. r7 surface validator (proves r6→r7 delta is whitelist+layout only)
python3 sources/2026-W43/execution/core-free-preview-r7/r7-reader-surface-semantic-join.py \
  --repo-root . --mode clean
# expect: R7_READER_SURFACE_PASS 18/18, RC=0.
python3 sources/2026-W43/execution/core-free-preview-r7/r7-reader-surface-semantic-join.py \
  --repo-root . --mode negatives
# expect: NEGATIVES_PASS 9/9, RC=0.

# 3. PDF rebuild + bytes
export PATH="$HOME/.TinyTeX/bin/x86_64-linux:$HOME/.local/bin:$PATH"
(cd sources/2026-W43/execution/core-free-preview-r7 && \
  lualatex -interaction=nonstopmode -halt-on-error main.tex && \
  lualatex -interaction=nonstopmode -halt-on-error main.tex)
sha256sum sources/2026-W43/execution/core-free-preview-r7/main.pdf
# expect: 5d01f49677c25e156da350c023ca5374cb72759b93eba21f049ea86d8dd9f93e (22p)
```

Input hashes pinned: reader `6f07cb49…`, ledger `6fd9d6fe…`, manifest
`85d94d74f…`, r3 projection `63ad2617…`, r3 TeX `bb0e7e1d…`, r3 PDF
`d0fa8b56…`, r6 TeX `7c052f05…`, r6 PDF `113b179a…` (identity record
`r6-baseline-replay-identity-r7witness.json`, 6/6 match at replay time).

## Known non-replayable here

- r6 38-negatives harness asserts the r3 production note present
  (`assert base_tex.count(PRODUCTION_NOTE_TEX) == 1`) → crashes against
  note-absent r6 files. Historical committed 38/38 stands as r6 evidence;
  NOT re-executed, NOT claimed. Fresh r7 9-negatives above replace coverage
  for the r6→r7 delta.
- Drive audit report (HTTP 401): transcription in contract §1 applied instead.
- Worker visual QA is bounded (11/22 full-res + 22/22 sheets + text layer);
  auditor must newly inspect every r7 page. Worker PASS ≠ independent PASS.
