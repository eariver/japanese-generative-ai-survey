# r8 independent verification runbook (capability-aware; read-only)

Date: 2026-10-27 JST. For a SEPARATE independent environment with direct Git checkout/filesystem. GitHub connector-only audit is INSUFFICIENT for the prescribed executions — a connector can read blobs but cannot run the Python checker, re-render the PDF, or parse annotations/fonts. Do not report independent replay without execution.

## Prerequisites

- Git checkout of `eariver/japanese-generative-ai-survey` at an ancestry including fixed r8 `953a9d331972fdae237da4bd0f1019b17168a118` (Tree `dfafff50c946e3d0abc051eb419797de283b192a`); verify `git rev-parse` + protected main `041a08df…`/`a134dc36…` + Frozen `774dd39a…`/`cd46a6f7a…`.
- Python 3.x (Muse used 3.14.4; any 3.10+ with stdlib suffices — checker + sidecar are stdlib-only).
- For PDF byte work: Python `pymupdf` (fitz) + `poppler` (`pdfinfo`, `pdffonts`), Ghostscript for rendering (optional).
- For rebuild (optional): LuaHBTeX 1.24.0 / TeX Live 2026 (`lualatex`). Rebuild is useful but NOT required to match deterministic PDF SHA (producer nondeterministic); visual/semantic reproducibility suffices.

## 1. Authenticate pins (read-only)

```bash
git rev-parse 953a9d331972fdae237da4bd0f1019b17168a118^{tree}
sha256sum sources/2026-W43/execution/core-free-preview-r8/main.pdf         # expect abd5b99b…
sha256sum sources/2026-W43/execution/core-free-preview-r8/main.tex         # expect 4ed553e5…
sha256sum sources/2026-W43/execution/core-free-preview-r8/main-tex-log.txt # expect 2242237a…
git ls-files -s sources/2026-W43/execution/core-free-preview-r8/build-manifest-r8.json  # blob 227dbabb…
gh api repos/eariver/japanese-generative-ai-survey/git/commits/be17e9944818442181975fa66b51912d2e7db8d8 --jq '{sha,tree:.tree.sha}'
# expect tree 2429f675db817cc38333182734ed6338f1eabc68 (40 chars; manifest field has 39-char typo, see sidecar P2-01)
```

## 2. Original checker replay (27/27 + 12/12)

```bash
python3 sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --repo-root . --mode clean
# expect R8_EXACT_FIDELITY_PASS 27/27 exit 0
python3 sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --repo-root . --mode negatives
# expect R8_NEGATIVES_PASS 12/12 exit 0
```

Isolated staged-dir alternative (no repo writes):

```bash
mkdir -p /tmp/p2stage/sources/2026-W43/execution/core-free-preview-r7 /tmp/p2stage/sources/2026-W43/execution/core-free-preview-r8
cp <repo>/sources/2026-W43/execution/core-free-preview-r7/main.tex /tmp/p2stage/sources/2026-W43/execution/core-free-preview-r7/main.tex
cp <repo>/sources/2026-W43/execution/core-free-preview-r8/main.tex /tmp/p2stage/sources/2026-W43/execution/core-free-preview-r8/main.tex
cp <repo>/sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py /tmp/p2stage/sources/2026-W43/execution/core-free-preview-r8/
python3 <repo>/sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --staged-dir /tmp/p2stage --mode clean
python3 <repo>/sources/2026-W43/execution/core-free-preview-r8/r8-exact-fidelity-check.py --staged-dir /tmp/p2stage --mode negatives
```

## 3. Sidecar strict taxonomy replay (P2-02)

```bash
python3 sources/2026-W43/execution/r8-p2-qa-closure/r8-p2-negative-taxonomy-sidecar.py --repo-root . --mode all
# expect SIDECAR_STRICT_PASS 5/5 exit 0:
#  clean-strict PASS; operator-baseline INFO ['PROSE_FIDELITY_LOSS'];
#  strict-operator PASS BOTH ['PROSE_FIDELITY_LOSS','READER_META_LEAK'];
#  N10 PASS; N13 PASS (anchor count == 1 verified inside)
```

Record actual terminal JSON, per-case `expected_all_required` vs `actual_causes`, mutant SHA/bytes, exit codes. If Python is unavailable, label that case NOT_RERUN (never fake a replay).

## 4. PDF byte re-verification (P2-03 + links/fonts)

```bash
pdfinfo sources/2026-W43/execution/core-free-preview-r8/main.pdf   # 22 pages, A4
pdffonts sources/2026-W43/execution/core-free-preview-r8/main.pdf  # 14 embedded subsets
python3 - <<'PY'
import fitz
doc=fitz.open('sources/2026-W43/execution/core-free-preview-r8/main.pdf')
print('pages', len(doc))
print('annots', sum(len(p.get_links()) for p in doc))
print('unique_uris', len({l.get('uri') for p in doc for l in p.get_links() if l.get('kind')==2}))
print('今週の総括 pages:', [i for i,p in enumerate(doc,1) if '今週の総括' in p.get_text()])
PY
# expect: 22 pages; 75 annots; 28 unique http; recap ONLY p20; bib heads ONLY p21
gs -dBATCH -dNOPAUSE -sDEVICE=png16m -r150 -sOutputFile=/tmp/r8-%02d.png sources/2026-W43/execution/core-free-preview-r8/main.pdf
# compare /tmp/r8-*.png with committed pages/p-*.png (image SHA in r8-p2-physical-page-anchors.json); note nondeterministic dates do not affect layout
```

## 5. Novel mutant (independent must add ≥1)

Design a scientifically material change outside saved 12+N13 (e.g. outside-table P2/P5/P8 qualifier-preserving, row/fig/bib totals unchanged), run through the SAME sidecar strict path on a temp copy, record expected vs actual causes + exit code. Spelling variants do not count.

## 6. Reporting boundary

- No GitHub writes; final report to Drive `GPT-Sol_Review/yyyyMMddHHmmss_SolReview.md` only.
- Distinguish: (a) auditor actually executed (with command + exit code + hashes), (b) image-only / static review, (c) NOT_RERUN (tooling absent). Never upgrade (b)/(c) to a PASS.
- Terminals: `INDEPENDENT_W43_R8_PDF_PASS` / `SEMANTIC_PASS_VISUAL_BLOCKED` / `REQUEST_CHANGES` / `INCONCLUSIVE`.
