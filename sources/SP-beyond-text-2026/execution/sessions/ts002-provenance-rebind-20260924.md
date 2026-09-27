# Survey Production session — ts002-provenance-rebind-20260924

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`
Branch: `special/beyond-text-2026-work` (existing only; no new/fallback/repair/review branches)
Repair authority: operator-supplied Sol r2 verdict
  (`SEMANTIC_DEPTH_PASS / REQUEST_CHANGES_PROVENANCE_REBIND_REQUIRED`;
  transcribed to `execution/sol-evidence-semantic-review-r2-20260924.md`, not operator-authored)
Authoritative repair inputs: r2 repair prompt, r2 session report,
`source-body-access-ledger.json` (corrected_body_id as source of truth),
`transition-ledger.json`, canonical Discovery/Screening/Evidence-r2 artifacts.

## Starting authority (all PASS read-only before any write)

- Remote work HEAD == `1e6679011bf33b0353bfae06cde8991415935abf`
- Remote work tree == `8ba405cd6865c2d4062fe7160eb7473bf5236515`
- Remote main HEAD == `0bbb02b3c5963403860897daec2feaf61e82589a`
- Remote main tree == `e4ddde5ed5059d303b818f54e27204369b256bcb`

## Scope discipline

- No Discovery research, X collection, Screening research, or Evidence semantic
  research rerun. No Materiality / Completeness / Selection / Architecture.
- Semantic payload unchanged except BT-D062 (v2 body only; no v1-fact carryover).

## Repairs (24 Discovery IDs, old locators preserved in repair manifest)

21 arXiv rebinding (`https://arxiv.org/abs/<corrected_body_id>`, each re-verified
read-only via arXiv API title match): BT-D004, D015, D033, D034, D039, D042, D043,
D044, D048, D049, D053, D059, D068, D069, D073, D074, D081, D084, D095, D096, D097.

- BT-D062: locator → `2312.05187`, title → v2 paper title, published_at → `2023-12`;
  v2 body consumed FULL (§§1-9 + App); Evidence card rebuilt from v2 facts only
  (VERIFIED; MATERIAL kept). Full old→new table in `provenance-repair-manifest.json`.
- BT-D089: locator → `https://ieeexplore.ieee.org/document/7178964` (DOI
  10.1109/ICASSP.2015.7178964), title → ICASSP paper title; stays PARTIAL
  (body not obtained; no promotion).
- BT-D024: locator → `https://github.com/CompVis/stable-diffusion`, title updated;
  identity verified via GitHub API (created 2022-08-10, sole branch main, no tags;
  published_at 2022-08 consistent); stays NEEDS_MORE (new-locator body fetch out
  of scope; old-locator 404 documented).

Other PARTIAL / NEEDS_MORE barriers (EDM body, Movie Gen method body, ITU full
text, Kling IR page, JS-gated pages) untouched with boundaries intact.

## Canonical propagation (all via current Core builders/validators; no hand edits)

1. Discovery acceptance rebuilt (canonical `build_acceptance`): 139 records,
   new SHA `4c69de55155a428916001f383f299eb90cfc13262e13558d7fb31ca384fe99a2`.
2. Discovery + Screening checkpoints rebound via replay (prior bytes snapshotted).
3. Screening replayed (same decisions 134/3/2/0): new acceptance `7d608d55…e9`.
4. Evidence task basis rebound via narrow compat rerun (37 projected / 102 passthrough).
5. Evidence factual result-set rebuilt/re-accepted: 139 Cards
   (126 VERIFIED / 8 PARTIAL / 5 NEEDS_MORE — only change vs r2 is D062→VERIFIED
   plus 24 URL rebinds and 3 entity-name alignments), new SHA `29804dcf…`.
6. Edition Views rebuilt/re-accepted: 139, new SHA `336f93d2…`.
7. Transition ledger refreshed (43 entries, 41 multi-task; locators + task IDs rebound).
8. Validators: `validation-rebind.json` 18/18 PASS (17 required + R2 preservation).

r1 (`f01de654…`) and r2 (`048cbd09…`) result-sets preserved untouched (digest +
zero-mutation verified). Shared Core untouched. No branches created; no force /
reset / rebase / rewrite.

## End state

- Lifecycle: `CANDIDATES_NORMALIZED` (screening passed; evidence/materiality/
  completeness pending). Materiality NOT entered.
- Local HEAD at commit: this commit (parent `1e667901…`, direct fast-forward).
- Final remote HEAD/tree after push: equal to this commit (verified post-push).

## Operational meaning

`EVIDENCE_REBOUND / AWAITING_SOL_PROVENANCE_READBACK`

Session status: `COMPLETE`
