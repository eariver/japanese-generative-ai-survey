# SOL W43 Core-free Preview r6 handoff
(`MUSE_W43_R6_CORE_FREE_PDF_READY_FOR_INDEPENDENT_REAUDIT`)

Date: 2026-10-27 JST. Executor: Muse Worker, existing branch ONLY
`weekly/2026-W43-v2-work` (normal FF commit, no reset/rebase/force).

## Start guard (verified read-only, then ff-only sync)

- Start HEAD `9f79ccb81b361e0bbc712a30d342833ba25ee2a9` / Tree
  `4344d696dfba96f84992ce3fe173b18f10e1e0bb` — 6/6 match after fetch
  (local checkout was one commit behind at `fa1caaed…`; work tree clean,
  `merge-base --is-ancestor` FF_POSSIBLE, `merge --ff-only` only).
- Reviewed main `041a08df…` / `a134dc36…`, Frozen `774dd39a…` /
  `cd46a6f7a…` — match. Pre-contract parent `598a9e80b…` /
  `e6b7f1f5…` — match.
- Contract `…/instructions/sol-w43-core-free-preview-r6-independent-r5-p1-and-print-p2-closure-20261027.md`
  read in full. No new branch/contract/alternate SHA created.

## Phase A (PASS) — what was proven

`execution/core-free-preview-r6/full-reader-visible-segment-join-r6.py`
closes independent P1 AUD-01 and P2 AUD-02 scope defects:
clean 36/36 `R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED` (exit 0),
negatives 38/38 `NEGATIVES_PASS` (exit 0), portable across arbitrary
`--repo-root` and `--staged-dir` replay. Exact TeX-side
`N-AUD-RECAP-SEMANTIC-REVERSAL` replay trips `RECAP_TEX` while the full
old scope stays green; `N-PRINT-NOTE-LEAK` guards the r6 state; six
per-input hash corruptions trip `HASH_MISMATCH`; tested strings are
hash-bound (no stale H00 oracle). Evidence: clean/negatives/identity
JSONs + segment map + runbook. References: 13+2 stay
CURATED_REVIEW_REQUIRED (no upgrades). Architecture: independent recount
18 SUBSTANTIVE / 13 PARTIAL vs the diagnosis header claim 20/11;
Human approval carries no per-row tiers; nothing promoted — Sol ruling
pending (see `architecture-11-partial-disposition-r6.md`).

Limitation: the independent `20261027011100_SolReview.md` file itself is
not committed in-repo; the contract §1 adjudication summary was used as
working authority. The separate independent re-audit must confirm.

## Phase B (worker PASS) — what was built

New noncanonical proof ONLY (r3 PDF never overwritten):
`execution/core-free-preview-r6/` — `main.pdf` (482659 bytes, 22 A4 pp,
SHA256 `113b179a4fab82df28a5d9f1ac1ac6c588ce2a0a253b988ba590944057f76320`,
blob `0342d2b5…`), `main.tex` (r3 minus exactly the p20 production-note
line, SHA `7c052f05…`), identical projection/sty, `main.log` (0 errors,
0 overfull/underfull, lualatex x2 LuaHBTeX 1.24.0/TL2026), 22 PNGs + 3
contact sheets, links/fonts/extraction from real PDF bytes (44 annots,
36 http, 0 malformed; 15 embedded subsets), all-page worker visual QA
(recap note absent, 5 paras intact, no tofu/overlap/clipping), r6-role
clean 36/36 on the real files, and a new independent audit REQUEST
(PROPOSED only) pinning r6 + historical r3/r5 subjects.

Old r3/r5 bytes, r3.5 originals, Architecture/Selection/Evidence/State/
Gates, main, Frozen Core v2: untouched. No Stage/Freeze/Release, no
canonical PDF, no Human approval claimed. Native Draft stays BLOCKED.

## For the separate independent Sol re-audit

Re-run the committed clean + negatives yourself (commands in
`portable-runbook-r6.md`), add at least one novel adversarial mutant,
recompute the r6 hashes from actual bytes, render/inspect every page
yourself (`PDF_VISUAL_AUDIT_BLOCKED` if binary access fails), and deliver
`yyyyMMddHHmmss_SolReview.md` with an explicit terminal. Human PDF Gate
remains PENDING; this handoff is not an approval.
