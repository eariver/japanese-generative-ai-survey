# SOL_W43_CORE_FREE_PDF_PREVIEW_R1_HANDOFF

Status: `MUSE_W43_CORE_FREE_PDF_PREVIEW_R1_READY_FOR_SOL_VISUAL_REVIEW`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work` (existing only, no new branch).
Sole contract: `sources/2026-W43/execution/instructions/sol-w43-core-free-preview-r1-tex-pdf-visual-qa-20261026.md`

## 0. Guards (read-only, zero-write on mismatch — all PASS)

- Dispatch Work HEAD `fa42353625009a86562e4466f879c9647c3f13f7` / Tree `bf5582b2ffd8ebcf23a75896234d67c66dd89618` == `origin/weekly/2026-W43-v2-work` (fetch + `rev-parse HEAD` + `HEAD^{tree}`).
- Pre-contract parent `8c61ecd56aaa662209ef8cb83fdcfb0bc2c9bcd4` / Tree `845f6cbde32d99bade83c591d586c1f206d697fd` verified via API; dispatch parent == `8c61ecd…`, diff `--name-only` == contract file only.
- Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a` == `origin/main` (ls-remote + API + local object).
- Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` verified via API + local object.
- Local was 2-behind (`bc6b1c…` r3.5 repair, parent of `8c61ecd…`) → `fetch` + `merge --ff-only` → `fa4235…` (clean, no reset/rebase/force). `git status` clean before writes.
- r3.5 audit-fixed source pinned before print: reader `6f07cb49…`, ledger `6fd9d6fe…`, manifest `85d94d74…` — all exact-byte match, no stop needed.

## 1. Bounded outputs (NEW edition-local only)

- `execution/core-free-preview-r1/reader-print-projection-r1.md` (`e1a49da9…`, 72862B) + `print-projection-diff-r1.md` (`8643207c…`): P1–P8 + 5-para recap, 19 selected, 20/80/29, 3 figures preserved; title cleaned, 19 operator-token classes → natural Japanese, internal-path backticks → `保存済み一次資料`, limits retained.
- `execution/core-free-preview-r1/main.tex` (`0d8a8a09…`, 87205B, 897 lines, 20 tables / 3 figures / 36 bibitems) + `preview.sty` (`28a663bc…`, W42 r15 pattern, W43 version comment) + `main.pdf` (`fd88cb7c…`, 480229B, 22 pages, A4, LuaLaTeX 1.24.0, Subject/Keywords `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`, 0 warnings) + `main.log` (`8e29b6e7…`).
- `execution/core-free-preview-r1/build-manifest-r1.json` (+ `build-commands-and-limitations-r1.md`): exact SHAs/sizes, compiler/commands/exit codes, 22-page split, volume note (22 vs 38 target, W42 final 21 precedent, no padding).
- `execution/core-free-preview-r1/reader-to-print-fidelity-and-citations-r1.md` (`909af6f…`): 20 headers / 80 rows (78 DATA+2 NOTE) / 3 figures / 29 claims / 36 citation keys → bibliography URLs, tiers 5/24/0.
- `execution/core-free-preview-r1/physical-page-and-table-qa-r1.md` + `pages/p-01.png`..`p-22.png` (150dpi) + `contact-sheet-01..03.png`: every page inspected, no critical defects; p-22 bibliography tail sparse (expected).
- `execution/core-free-preview-r1/independent-visual-review-request-r1.PROPOSED.md` (request only, no forged PASS).
- This handoff + `execution/sessions/muse-w43-core-free-preview-r1-20261026.md` + `execution/index.md` append-only entry.

Full changed-path list vs `fa4235…`: the above + session + index (no other paths; `git status`/`diff --name-only` to confirm at commit).

## 2. Checks (all PASS, exit 0)

- r3.5 strict checker rerun: `EDITION_LOCAL_ROW_JOIN_PASS`, T1 20 headers, T2 80 bijection (78/2, 13 aliases), C 29 semantic (COBOL 40%+ prevalence + npm full timestamp incl.), T5 anchors, 24/24 negatives, TIER 5/24/0.
- TeX builds (4 runs total, final 2 clean): exit 0, 22 pages, 0 Illegal/Overfull/Errors after figure `\\[` → `\par` and URL/SHA breakability fixes (documented, content-neutral).
- PDF metadata: Title neutral weekly, Subject/Keywords exact `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` (detokenize-preserved), Creator LuaLaTeX, 22 pages.
- No unauthorized path changes (edition-local + handoff/session/index only).

## 3. Volume / limitations (honest, not closed)

- Honest 22 pages (cover 1, TOC 1, body P1–P8+recap 18, bib 2) vs Architecture approx 38 / max 44 / estimate ~37. Consistent with W42 final 21 pages. Architecture page_plan itself says target is estimate not guarantee and forbids padding. No padding applied; single-column honest density. Sol adjudicates volume.
- All §3 factual guards preserved (MemT storage, 1.86x SOURCE_UNVERIFIED, Patch stages, FAQ UNRESOLVED, Voxtral/DeepInfer/DeepSeek qualifications, GH vs npm separation, window `[2026-10-16T22:00:00Z,2026-10-23T22:00:00Z)`).
- Residuals: independent Sol did not run negatives; expected-map not exhaustive; raw snapshots unavailable; no reproduced benchmarks. No promotion to verified raw.

## 4. Final HEAD/Tree (push/read-back verified)

Parent chain: `bc6b1c… (r3.5)` → `8c61ecd… (audit request)` → `fa4235… (preview contract, start)` → `<preview-r1 commit>`.
Exact repair-commit HEAD/Tree recorded at commit/push/read-back (non-force, `rev-parse HEAD`, `HEAD^{tree}`, `origin/weekly/2026-W43-v2-work` read-back). Handoff cannot contain its own hash; reproducibility via starting HEAD/Tree + exact file-byte SHAs above + result JSON.
PDF Git object verification / stable commit-pinned URL in session report after push/read-back (unavailable before push).

`MUSE_W43_CORE_FREE_PDF_PREVIEW_R1_READY_FOR_SOL_VISUAL_REVIEW`
