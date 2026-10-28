# Muse W43 core-free preview r6 session (2026-10-27)

Start (ff-only sync, no reset/rebase/force):
`9f79ccb81b361e0bbc712a30d342833ba25ee2a9` / Tree
`4344d696dfba96f84992ce3fe173b18f10e1e0bb` (origin verified 6/6 with
reviewed main `041a08df…` / `a134dc36…` and Frozen `774dd39a…` /
`cd46a6f7a…`; pre-contract parent `598a9e80b…` / `e6b7f1f5…` confirmed).
Contract:
`sources/2026-W43/execution/instructions/sol-w43-core-free-preview-r6-independent-r5-p1-and-print-p2-closure-20261027.md`
(95 lines, read in full; independent `20261027011100_SolReview.md` itself
is not committed in-repo — the contract §1 adjudication summary is the
working authority, recorded as a limitation in the handoff).

## Phase A — full visible prose/figure/code/recap proof (PASS)

New edition-local validator
`execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py`
(SHA256 `7c09cdce18ea6da21880e0d8a4660a7480e7da38bdd5d6447bc03404179c7d18`):
no hardcoded repo paths (`--repo-root` / explicit paths / `--staged-dir`
mirror replay all PASS), six pinned input hashes bind the actually-tested
strings (mutants distinguished from missing inputs), ordered 1:1 segment
mapping (71 prose paras + 8 quotes + 3 figures + 5 code blocks + 5 recap
paras + 20 tables/80 rows/307 cells + 18 notes + 29 claims + 36 bibitems).

- Clean `R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED` 36/36, exit 0
  (`full-segment-join-clean-r6.json`
  `f6cc3c1ebcb72f0f54871cd4bc8317d60eada2709e2fadbe2acbd71e678de90e`;
  r3-role baseline `b74d215e5b4e1826d08b6ee7be53de9c71d8f57122e89a474d9b4417f436ec63`).
- Negatives `NEGATIVES_PASS` 38/38, exit 0
  (`5569991376d1ba1afb11b8b63d17981d7f5d4c94a033e3b65e4951f2a5918852`),
  incl. exact TeX-side `N-AUD-RECAP-SEMANTIC-REVERSAL` replay (old table/
  cell/claim/citation/qualifier scope stays green = the P1 point),
  `N-PRINT-NOTE-LEAK`, per-input hash corruptions x6, and the deduped
  carry-over scope (single TeX row-swap kept).
- Identity record `six-input-identity-and-mutant-binding-r6.json`
  (`acf9ba733e7f104a6614878559670e93443ce6cba632ef623ae428fb360c3805`):
  6/6 pins match; tested==disk for the r3 subject.
- Evidence docs: `source-to-projection-to-tex-segment-map-r6.md`,
  `portable-runbook-r6.md`, `reference-claim-tier-curation-r6.md`
  (13+2 stay CURATED_REVIEW_REQUIRED, no upgrades),
  `architecture-11-partial-disposition-r6.md` (independent recount:
  diagnosis rows 18/13 vs header claim 20/11; Human approval carries no
  per-row tiers; no promotion/demotion — Sol adjudication pending).

Terminal: `MUSE_W43_R6_FULL_VISIBLE_FIDELITY_CONFIRMED` → Phase B entered.

## Phase B — print-only r6 PDF (PASS, worker-level)

- Copied r3 projection/sty byte-identical; `main.tex` = r3 minus exactly
  the one production-note line (diff 1 line, `print-only-diff-r6.md`;
  new TeX SHA `7c052f05…`, 90920 bytes).
- `lualatex` x2 (LuaHBTeX 1.24.0, TeX Live 2026, TinyTeX user install —
  same engine/version as the r3 build record), exit 0/0, 0 errors,
  0 overfull/underfull. `main.pdf` 482659 bytes, 22 A4 pages, raw SHA
  `113b179a…`, blob `0342d2b5…`; `main.log` kept, aux/toc removed.
- r6-role clean on the REAL new files: 36/36 PASS (note absent,
  allowlisted once); old r3/r5 subjects untouched and separately pinned
  in `build-manifest-r6.json`.
- Links/fonts/extraction from actual PDF bytes: 44 annots (36 http,
  0 malformed), 15 embedded subsets, all required strings + 5 recap cores
  extracted, production note absent.
- 22 PNGs (150 dpi) + 3 contact sheets; worker inspected p-01/07/14/16/
  18/19/20/21/22: no tofu/overlap/clipping/empty-body; recap note gone;
  5 paras intact; dense tables + bib legible
  (`physical-page-and-table-qa-r6.md`).
- Independent audit REQUEST (only) regenerated, pinning the new r6
  hashes + historical r3/r5 subjects
  (`independent-sol-r6-print-semantic-visual-audit-request.PROPOSED.md`).

Terminal: `MUSE_W43_R6_CORE_FREE_PDF_READY_FOR_INDEPENDENT_REAUDIT`.

## Invariants

r1/r2/r3/r4/r5 bytes, r3.5 reader/ledger/manifest, Architecture r6,
Selection, Evidence, State, Gates, audit reports/contracts, reviewed main,
Frozen Core v2, shared roots: all untouched. No new branch/Stage/Freeze/
Release. Normal FF commit on the existing work branch only, allowed paths
only (r6 dir + handoff + this session + index append).
