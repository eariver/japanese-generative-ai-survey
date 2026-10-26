# SOL_W43_CORE_FREE_EDITORIAL_R3_5_P1_REPAIR_HANDOFF

Status: `MUSE_W43_R35_SINGLE_P1_SEMANTIC_CLAIM_REPAIR_READY_FOR_SOL_RECHECK`
Date: 2026-10-26 JST. Branch: `weekly/2026-W43-v2-work` (existing only, no new branch).
Sole contract: `sources/2026-W43/execution/instructions/sol-w43-r35-single-p1-semantic-claim-closure-20261026.md`

## 0. Guards (read-only, zero-write on mismatch — all PASS)

- Dispatch Work HEAD `2ec0202bb9c53dba4d8b64b2edfb1b69f117471a` / Tree `1fb36c82fe13d491427654eafd58ff05f2a0fb34`
  == `origin/weekly/2026-W43-v2-work` HEAD/Tree (fetch + `rev-parse HEAD` + `HEAD^{tree}`).
- Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a` == `origin/main`.
- Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
  (object exists, `cat-file -t commit`, fetchable from origin as `FETCH_HEAD`).
- Contract parent check: `2ec0202b^` == `b6101733bb136116649cb129a592e52a96e7a38c` (pre-contract parent per §0),
  `diff --name-only HEAD^ HEAD` == contract file only. Local was 2-behind (`1a4cfed…`) → `merge --ff-only` → `2ec0202b…` (clean, no reset/rebase/force).

## 1. Bounded repairs (2 physical rows, R32-FULL-003 P1 only)

| # | Claim (stable ID, count 29 preserved) | Before (r3.4 misjoin) | After (r3.5 fix, own-block, reader-friendly) |
|---|---|---|---|
| 1 | `p7-f1-01/enterprise-40p`: `40%+ / enterprise share / COBOL (field) / percent of online banking` | Bound to `p7-f1-01` whose physical `COBOL ｜10.9→72.1 ｜… ｜hidden byte-parity…` never printed `40%+`; prose L381 + `p7-t2-03` mentioned 40% but different paragraph/table ≠ local-row proof. r3.4 checker passed vacuously via variant-token `COBOL` match. | Physical `p7-f1-01` now `COBOL ｜10.9→72.1 ｜19/20言語83%以上の例外… ｜hidden byte-parity…・企業現場40%超（オンラインバンキング言及、精度とは別）`. Prints `40%` + prevalence qualifiers (`企業現場`, `オンラインバンキング`, `精度とは別`), keeps accuracy `10.9→72.1` as distinct facet. Claim stays `p7-f1-01` (own-block, stable `claim-3`, count 29). Never treated as benchmark accuracy. Evidence `task-160489… claim-3` (`Enterprise feedback-driven (COBOL 40%+ banking…)`) stays `ARCHIVE_UNAVAILABLE`, not invented. |
| 2 | `p8-f2-03/npm-clock`: `2026-10-22T15:21:49Z / registry clock / TanStack AI 1.0.0 npm` | Bound to `p8-f2-03` whose physical `版固定 ｜registry／releaseの時刻 ｜…` never printed npm time; exact clock lived only in `p8-f2-01` (`GH 15:18:14Z／npm 15:21:49Z`) + ledger clock metadata. r3.4 checker passed via URL/clock token, not physical value. | Physical `p8-f2-03` now `版固定 ｜registry／releaseの時刻（npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠） ｜Metrics 23:42:03ZはOUT ｜GrokはNEVER_STORY`. Prints full `2026-10-22T15:21:49Z` + role separation (`GH …とは別典拠`). Claim stays `p8-f2-03` (own-block, stable `supplement-r4`, count 29). GH vs npm kept separate; scoped `https://registry.npmjs.org/@tanstack%2Fai` + `RAW_NOT_ARCHIVED` preserved; millis `.491Z` in ledger clock, seconds in reader (documented). |

No other values changed. 96 blocks / 20 tables / 80 rows (78 DATA + 2 NOTE) / 29 claims / 13 aliases preserved.
r3.4 assets untouched. Title version label `r3.4→r3.5` only (non-physical).

## 2. Deliverables (NEW r3.5 only, in `sources/2026-W43/execution/`)

- `editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md` (r3.4 + title + 2 physical rows)
- `editorial-bypass/w43-r3-5-citation-confidence-ledger.json` (r3.4 + `r3_5_change`, 2 `table_rows` notes clarified, claims identical)
- `editorial-bypass/w43-r3-5-physical-row-manifest.json` (r3.4 + 2 rows `physical_text`/`sha256` updated)
- `editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py` (genuinely semantic, pinned 20 headers + 13 aliases + 29-claim baseline, exact-byte digests, 24 specific-reason negatives incl. physical mutations + COBOL/npm pre-fix)
- `editorial-bypass/w43-r3-5-semantic-join-result.json` (`EDITION_LOCAL_ROW_JOIN_PASS`, exit 0, 24/24 negatives, exact SHAs)
- `editorial-bypass/w43-r3-5-source-crosswalk-delta.md`
- `editorial-bypass/w43-r3-5-editorial-qa.md`
- this handoff + `sessions/muse-w43-core-free-r3-5-20261026.md` + `index.md` entry

Full changed-path list (vs `2ec0202b…`): the 8 above + session + index (10 files). No other paths touched
(`git status --porcelain` clean except these; `git diff --name-only` to confirm at commit).

## 3. Checks (all PASS, exit 0)

- `T1-table-identity-20-headers` PASS — 20 exact headers, order pinned; header-mutate negative FAILs `T1-HEADER-MISMATCH`.
- `T2-row-bijection-80` PASS — 80↔80 SHA/line/ordinal/row_id, DATA/NOTE (78/2) matched, 13 aliases pinned.
- `C-claims-29-semantic` PASS — 29 own-block DATA, every value printed in its own physical row (lexical map documented), variant/metric/unit/comparator/URL/provenance honest; no URL-only proof.
- `T5-anchors` PASS — MemT storage/1.86x/parametric/classifier/TTS/Controlled-Voice + COBOL 40%+ prevalence + npm full timestamp.
- `NEG-all-detected-specific-reason` PASS — 24/24, each for its specific ID (9 preserved r3.4 + 15 true physical/semantic).
  Includes `NEG-COBOL-prefixed-missing-40p → p7-f1-01/enterprise-40p C-VALUE-MISSING` and
  `NEG-npm-prefixed-missing-clock → p8-f2-03/npm-clock C-VALUE-MISSING` (consistent reader+manifest stripped, T2 passes, C fails).
- Pre-fix r3.4 files through r3.5 checker → `P1_OPEN` with exactly the 2 semantic `C-VALUE-MISSING` families (COBOL + npm + qualifiers/roles/dates), proving load-bearing fix.
- `TIER-report` — `RAW_PRIMARY 5 / QUALIFIED_UNAVAILABLE 24 / OTHER 0`.
- Digests are exact file bytes: reader `6f07cb49…1cc5da46d6`, ledger `6fd9d6fe…382e6d4` (canonical `49c1e650…` separate), manifest `85d94d74…26a3cf111` (canonical `e7a98ac4…` separate). Bind to exact paths in result JSON.

## 4. Independently unresolved limitations (honest, not closed)

- 40%+ stays accepted-derived (`task-160489… claim-3`, `ARCHIVE_UNAVAILABLE, page day-only`); no raw HTML archived, no independent harness rerun. Qualified as enterprise feedback, never raw-primary.
- npm registry body `RAW_NOT_ARCHIVED` (GH JSON only); millis `.491Z` in ledger clock, seconds in reader (documented normalization). No promotion of GH `published_at` to archived npm original.
- All r3.4 FIXED/QUALIFIED outcomes preserved as reported; NO self-claim of external independent closure. `EDITION_LOCAL_ROW_JOIN_PASS` is edition-local only.
- No TeX/PDF, no Stage, no Freeze/Release, no Gate change. Eight article packages, 19 SELECTED (12+7), 31 Architecture requirements (20/11 baseline, no upgrade to 31/31).

## 5. Final HEAD/Tree (push/read-back verified)

Parent chain: `1a4cfedb… (r3.4)` → `b6101733… (r3.4 audit request)` → `2ec0202b… (r3.5 contract, start)` → `<r3.5 repair commit>`.
Exact repair-commit HEAD/Tree recorded at commit/push/read-back (non-force, `git rev-parse HEAD`, `HEAD^{tree}`, `origin/weekly/2026-W43-v2-work` read-back).
Handoff file itself cannot contain its own commit hash (circular); reproducibility binds via starting HEAD/Tree above + exact file-byte SHAs in §3 + result JSON.
See session worklog + index entry + User report for exact final HEAD/Tree after push/read-back.

`MUSE_W43_R35_SINGLE_P1_SEMANTIC_CLAIM_REPAIR_READY_FOR_SOL_RECHECK`
