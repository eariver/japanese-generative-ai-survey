# J-GAS W43 — Sol editorial r3.5 bounded P1 semantic claim-closure execution contract

Status: `EDITORIAL_SOL_EXECUTION_AUTHORITY / INDEPENDENT_R34_REQUEST_CHANGES / R32-FULL-003_P1_OPEN / PDF_PREVIEW_STOP`
Date: 2026-10-26 JST
Repository: `eariver/japanese-generative-ai-survey` · Existing branch only: `weekly/2026-W43-v2-work`
Commissioner: editorial Sol. Executor: Muse Worker. Independent Sol is a separate read-only reviewer; Human Owner retains Human Gate authority.

## 0. Strict execution guards — mismatches mean ZERO WRITES

Before any repository modification, inspect all **remote** branch HEAD and Git root Tree pairs and compare them to the dispatch values from editorial Sol. At authoring time (BEFORE this contract commit), the pairs are:

| Ref | HEAD | Root Tree |
|---|---|---|
| `weekly/2026-W43-v2-work` | `b6101733bb136116649cb129a592e52a96e7a38c` | `6bfa64ad4e4ca169e6106d9c33ee68e18820d99f` |
| `main` | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| `production/survey-core-v2` | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

**Important:** the Work pair above is the PRE-CONTRACT parent. This file's creation itself advances Work exactly once. The Muse dispatch will state the **new contract commit's HEAD and Tree**, which replace the Work pair above as the authoritative six-way start guard. Muse must check exact work HEAD+Tree, main HEAD+Tree, frozen HEAD+Tree from that dispatch; if even one differs, stop **with zero writes** and report actual versus expected. Verify the contract commit's sole parent is exactly `b6101733bb136116649cb129a592e52a96e7a38c` and its only diff is this contract file. Fetch/ff-only permitted when local clean and behind. No new/fallback/review/repair branch, no reset/rebase/force-push. Commit normally and push non-force, verify read-back.

Never change `main`, Frozen Core v2, shared Core paths, accepted Evidence/Views, Selection, Architecture r6, r1–r3.4 historical artifacts, production state, any Human Gate, or reviewed Human approval. All new production is strictly `sources/2026-W43/execution/` edition-local and Core-free.

## 1. Binding independent audit and precise stopping decision

The genuine separate independent Sol r3.4 bounded audit is stored in Google Drive `GPT-Sol_Review`, report URL:
`https://drive.google.com/file/d/1jRqM0m1aVJBkaga3zi3kHYpUNuQwr4ZU/view?usp=drivesdk`.

Exact reviewed Muse r3.4 subject:
- HEAD `1a4cfedb95692ae481c241594e24231680a9a01d`
- Tree `a79c26efcbb8c7a2a6555c485b243be6c9746a18`
- Independent disposition: `REQUEST_CHANGES`, P0=0, **one P1 remains OPEN** (`R32-FULL-003`).
- `R32-FULL-001` and `R32-FULL-002` are FIXED; P2 `004`–`010` are either FIXED or QUALIFIED_WITH_LIMITATION.
- `20 SUBSTANTIVE_COMPLETE / 11 PARTIAL` is still the prior Architecture-31 requirement baseline; no upgrade to 31/31.

This contract authorizes ONLY a **one-finding, bounded r3.5 repair of R32-FULL-003**. Do not re-open fixed MemT/Patch/FAQ corrections, make new research stories, revise approved Architecture/Selection, or claim r3.4 independent PASS. No TeX/PDF, no preview gate, no Stage promotion, no Freeze/Release.

Prior independent r3.4 contract is also at `sources/2026-W43/execution/audits/independent-sol-w43-r34-ten-finding-closure-audit-request-20261026.md`. Read r3.4 fixed reader/ledger/manifest/checker and the independent report in full; the latter's §4.1–4.3 enumerates the acceptance tests. If the auditor's Google Drive source is temporarily inaccessible, use its frozen findings reproduced here; report the access limitation and never invent a report read.

## 2. The two confirmed data-level misjoins to correct

### 2.1 COBOL enterprise share `40%+` (p7-f1)

In r3.4 ledger, a `metric="enterprise share"`, `value="40%+"`, `model_variant="COBOL (field)"` claim is bound to `p7-f1-01` (reader L385). Physical row `COBOL ｜10.9→72.1｜...｜hidden byte-parity...` never prints `40%+`. The prose L381 and `p7-t2-03` mention 40%, but **a different paragraph/table does not prove the claimed local row**.

Repair by making the claim's **physical target row** explicitly print and qualify the enterprise share value (including the correct claim purpose and evidence provenance), OR, if moving the claim to a legitimately printed other table/ledger block, carry the entire claim into that block, retain stable claim identity and own-block relation, and preserve the count 29. Choose the minimal unambiguous result. Do not treat COBOL prevalence as benchmark performance, acceptance-test success, or independently measured usage. If no traceable accepted evidence supports the exact 40%+ semantics, demote/remove the unverifiable claim with explicit 29-claim reconciliation and a `P1_OPEN` stop; **never invent a source**.

### 2.2 Scoped TanStack npm published clock `2026-10-22T15:21:49Z` (p8-f2)

In r3.4, `metric="registry clock"` belongs to `p8-f2-03`, whose reader L486 prints only `registry／releaseの時刻`, while `p8-f2-01` at L484 actually prints `GH 15:18:14Z／npm 15:21:49Z`. Fix the *actual claim ↔ printed physical row* target (normally moving npm claim to a row that expressly displays npm time, or properly printing the date/time on its current row). For exact-value tests print full timestamp or define documented display-normalization including date if already clearly in table context. Preserve **GitHub 15:18:14Z vs npm 15:21:49.491Z as separate origins**, with npm registry response **RAW_NOT_ARCHIVED**, full scoped URL `https://registry.npmjs.org/@tanstack%2Fai`, and source-clock provenance. Do not promote GH's saved `published_at` into an archived npm original.

Both examples must be tested as *negative pre-fix fixtures* against the revised checker and actually cause FAIL for **semantic missing-in-physical-row** reasons, not an unrelated file-hash/header/count failure.

## 3. Make the r3.5 edition-local checker genuinely semantic and adversarial

Create **new versioned r3.5 files**; never overwrite r3.4 assets. Retain and improve r3.4's 20 physical fenced tables / 80 physical rows (78 DATA, 2 NOTE), 3 distinct figure rows, 96 ledger blocks, 13 sanctioned aliases, and 29 claims, except a justified explicitly reconciled deviation requiring Sol decision. Preserve reader-friendly text without technical operator IDs.

Hard mandatory acceptance checks:

1. **T1 table identity**: explicit fixed table ID/order **and exactly matching 20 reader table header strings**, including the proper header-to-manifest identity. A different/missing/swapped table header must FAIL even if 80 data rows unchanged.
2. **T2 row bijection**: full UTF-8 physical text SHA256, line number, ordinal, `row_id` ↔ 80 manifest rows ↔ 80 ledger rows, exactly, no duplicates/gaps; for all 80 compare manifest and ledger `row_type` (DATA/NOTE). Validate the 13 exact, explicitly enumerated sanctioned aliases to their expected reader physical labels; a self-declared arbitrary alias must not bypass matching. Exclude NOTE from claims and keep figure lines separate.
3. **C claim-to-physical semantic mapping**: **exactly 29 claims**, stable unique IDs (compare enumerated expected set to r3.4, account for any explicitly approved transformations), and an independently reviewed expected mapping `claim_id -> owning block -> physical row -> variant/product -> metric -> printed value/display normalization -> unit/comparator -> intended URL -> evidence tier`. Validate EVERY claim, not only sample anchors and nonempty fields. The physical row must actually show or unambiguously encode its own claimed value (with an allowed, narrow, documented lexical representation map), its correct variant and measure; matching a generic token in notes/URL/clock may not excuse missing physical value. Never prove a source from URL presence alone. Treat `40%+` as prevalence, not COBOL test accuracy; require npm date/time and role separation. Check cross-block, NOTE, wrong variant, wrong metric, false price unit, mismatched comparator and wrong source URL/class. Guard expected mappings against circular generation from the same mutable ledger; pin to an audited independent specification or clearly reviewable expected baseline.
4. **C source/provenance honesty**: distinguish archived original raw, archived rendered extraction, accepted-derived/evidence-only, URL-only and `ARCHIVE_UNAVAILABLE / RAW_NOT_ARCHIVED`. When source raw bytes exist, validate claimed source path and actual relevant text, rather than mere `Path.exists()`. Where raw not stored, report `UNVERIFIED` and do not claim original-source closure. Retain corrected MemT 66x storage scope, Patch stage4/5, scoped npm URL, Voxtral uncertain WER/price units, DeepInfer pseudocode status, DeepSeek MIT licensing caveat, P4 FAQ unknowns.
5. **Unambiguous digests**: log SHA256 of **exact reader file bytes**, **exact ledger file bytes**, **exact manifest file bytes**; if normalized JSON semantic hash is additionally useful, give it a different field e.g. `ledger_canonical_json_sha256` rather than naming it `ledger_sha256`. Bind test result to exact paths and computed hashes so future audits can reproduce.
6. **True negative coverage**: on an ephemeral **separate test copy** (no historical/repo write), mutate the **actual physical reader content**, not just the manifest, in 4 cases: delete/duplicate/swap/mutate one table row; mutate one actual table header; remove one claim (29→28); change one claim's value to a different number **without changing its row**; change product variant, metric, source URL, source provenance classification and unit; change one ledger row_type DATA↔NOTE; incorrect NOTE target; unscoped TanStack npm URL; false price unit confirmation; include both original COBOL and npm counterexamples. Each test must fail for its **specific intended semantic reason**, with its own visible test case ID/error, not just any incidental guard failure. Preserve 9 original tests where useful but do not mistake them for full coverage.
7. **No vacuous PASS**: acceptance JSON must itemize all 20 table headers, all 80 rows, all 29 claims, source classes and counterexamples, include POSITIVE actual test exit code, NEGATIVE tests and observed failures. On any failed required assertion mark `ROW_JOIN_OPEN` / `P1_OPEN`, not `PASS`. `EDITION_LOCAL_ROW_JOIN_PASS` is scoped to edition-local join only, never Core v2 validated Stage, guaranteed external provenance, or independent Sol sign-off.

NOTE: A genuinely semantically matched claim may have an unresolved *source-originality* limitation when accurately labeled; this does not require inventing unattainable raw evidence. Ensure such qualifications are recorded rather than silently converted to raw-primary.

## 4. Deliverables and invariants

Only in `sources/2026-W43/execution/`:
- `editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md`
- `editorial-bypass/w43-r3-5-citation-confidence-ledger.json`
- `editorial-bypass/w43-r3-5-physical-row-manifest.json`
- `editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py`
- `editorial-bypass/w43-r3-5-semantic-join-result.json`
- `editorial-bypass/w43-r3-5-source-crosswalk-delta.md`
- `editorial-bypass/w43-r3-5-editorial-qa.md`
- concise `SOL_W43_CORE_FREE_EDITORIAL_R3_5_P1_REPAIR_HANDOFF.md` and session worklog, index entry.

The handoff must include remote verified final exact HEAD and Tree, parent chain, full changed-path list, all checks and negative tests, **2 concrete row/claim repairs**, digest types, and all independently unresolved limitations. Report whether actual original independent 10 findings were altered (they must not be except the target prospective P1); preserve r3.4 FIXED/QUALIFIED outcomes as reported, but do NOT self-claim external independent closure.

No modifications to original r3.2–r3.4 assets, Core, Stage, architecture decision, Selection, review authority or PDF/Human Gate. Keep eight article packages, five paragraphs of recap after P8 (not P9), 19 SELECTED (12 primary+7 supporting), 31 Architecture requirements (independent evidence baseline 20 COMPLETE/11 PARTIAL). Do not add content simply to pad PDF volume.

## 5. Terminal stop and next review

Required terminal status **`MUSE_W43_R35_SINGLE_P1_SEMANTIC_CLAIM_REPAIR_READY_FOR_SOL_RECHECK`**, with no Preview, no Freeze/Release. After Muse completion, editorial Sol conducts r3.5 direct recheck; when no local unresolved P1 remains, obtain **another separate one-finding read-only independent closure audit** of `R32-FULL-003` at fixed r3.5 HEAD/Tree. Only an independent no-P0/P1 disposition permits preparation of Core-free NONCANONICAL PDF preview, which will itself require reader-visible QA and explicit Human review. No native State promotion/Release without a distinct governance decision.
