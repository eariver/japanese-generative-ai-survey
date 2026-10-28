# SOL W43 Core-free Preview r8 Handoff — P1 meta closure + N10 prose fidelity

Date: 2026-10-27 JST. Executor: Muse Worker, branch `weekly/2026-W43-v2-work` ONLY.
Terminal: `MUSE_W43_R8_META_P1_AND_PROSE_FIDELITY_READY_FOR_INDEPENDENT_REAUDIT`

## Starting guard (all PASS, read-only then FF-only)

- Expected starting HEAD `88a6ffbb1ceffd6cef0ecdf0e2af1d489993bbca` / Tree `e50ff33f8215c50b4f76e4128b05992f18883d0f` — remote `ls-remote` + post-fetch `rev-parse` match; local was 2-behind (`3b1178ff…`), `fetch` + `merge --ff-only` to exact start, no reset/rebase/force/new-branch.
- Reviewed main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a` — match.
- Frozen Core v2 `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` — match.
- Contract guard: pre-contract `be17e9944818442181975fa66b51912d2e7db8d8` / `2429f675db817cc38333182734ed6338f1eabc68`; post-contract parent == pre-contract; diff `be17..88a6` = contract file only.
- Drive report `20261027035724_SolReview.md` (`1G97p7LnH…`) fetch → 401; transcription applied, never claimed as read.

## What was done (bounded, edition-local)

- A/B/C only: r7 `9791a545…` (97572B) → r8 `4ed553e5…` (97447B); diff = 3 replacements (B = 1 paragraph); `preview.sty` identical `0199d86d…`.
- N10 reproduced (old `check_mutation` → `[]`, blind spot proven) + new `r8-exact-fidelity-check.py`: clean 27/27 `R8_EXACT_FIDELITY_PASS`, negatives 12/12 `R8_NEGATIVES_PASS` (N10 `PROSE_FIDELITY_LOSS`), staged-dir replay verified.
- PDF rebuilt lualatex ×2 exit 0/0, 22 A4 pages, 487351B `abd5b99b…`; logs tracked (`main-tex-log.txt` 78170B `2242237a…` + 2 stdout txt); 0 errors, 2 benign overfull vbox (p14–15, visually clean).
- All 22 pages viewed full-res: no clipping/corruption/wrapping/TOC mismatch; A p04 / B p11 / C p22 confirmed, old strings absent; long Decisions JSON, 5 recap, bib, proof marks ok.
- Links/fonts from PDF bytes: 75 annots, 28 unique http (0 malformed CJK), incl. Decisions Guide + `%2F` npm URLs; 14 embedded subsets; A4 boxes; selectable Unicode. 28≠36 expected (shared URLs).

## Evidence (new files only in `core-free-preview-r8/` + handoff + session + index)

`main.tex`, `preview.sty`, `main.pdf`, `main-tex-log.txt` (+ untracked `main.log` same bytes), `compiler-pass1/2.stdout.txt`, `meta-closure-and-semantic-diff-r8.json`, `reader-meta-full-sweep-r8.md`, `r8-exact-fidelity-check.py`, `r8-fidelity-clean.json`, `r8-fidelity-negatives.json`, `n10-old-vs-new-replay-r8.md`, `portable-independent-replay-r8.md`, `build-manifest-r8.json`, `pdf-page-qa-r8.md`, `pdf-links-fonts.md` + `pdf-links-fonts-raw-r8.json`, `architecture-and-reference-carryover-r8.md`, `independent-sol-r8-reaudit-request.PROPOSED.md`, 22 PNGs + 3 sheets.

No write to r1–r7, canonical PDF, Core/shared files, State/Gates/Architecture/Selection/Evidence. No new branch/fallback/reset/rebase/force/Freeze/Release.

## Next

Independent Sol must newly inspect r8 PDF/images + re-run portable replay + add novel mutant (see PROPOSED request). Worker results are not Sol PASS. Human PDF Gate PENDING; Architecture ESTABLISHED; Native Draft BLOCKED.
