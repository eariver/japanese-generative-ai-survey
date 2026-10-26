# W43 Sol editorial — Core-free PDF Preview r2: bibliography integrity + volume adjudication

Status: `EDITORIAL_SOL_R1_PRINT_REVIEW_REQUEST_CHANGES / R35_SEMANTIC_P1_CLOSED / NONCANONICAL_PREVIEW_ONLY / HUMAN_PDF_GATE_PENDING`
Date: 2026-10-26 JST. Executor: Muse Worker. Repo `eariver/japanese-generative-ai-survey`. Existing branch ONLY `weekly/2026-W43-v2-work`.

## 0. Mandatory guarded execution; zero writes on mismatch

This contract will itself advance W43 branch by exactly one normal commit. **The separate Sol dispatch's exact post-contract HEAD/Root Tree pair** is the only valid execution starting Work pair. The following represent the pre-contract parent only:

| ref | HEAD | root Tree |
|---|---|---|
| W43 WORK *pre-contract* | `071016d02f2a34a74e27d55fc0f72a3bb7d1d75b` | `b5b2691748555190269baed6cbcc0ef560f40c60` |
| main | `041a08dfef3112643cbf85b4a86a7b6f9128aed6` | `a134dc36a407d08ab1de416324229b3955e0325a` |
| production/survey-core-v2 | `774dd39a951c9ac3818e83dfffd4c7666efb0a20` | `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` |

First remote read-only six-way guard against dispatch post-contract W43 HEAD/Tree and the above main/Core values; if any mismatch, ZERO WRITES with expected/actual. Confirm contract commit parent exactly `071016d0...` and its only diff this file. No new/fallback/review/repair branch, no reset/rebase/force, no PR/main/Core writes. Clean behind only via ff-only. Normal non-force push with new expected-start ref compare and remote readback.

## 1. Binding state; confirmed editorial findings

Muse r1 preview content commit (fixed review subject):
HEAD `071016d02f2a34a74e27d55fc0f72a3bb7d1d75b` / Root Tree `b5b2691748555190269baed6cbcc0ef560f40c60`.
Normal FF parent `fa42353625009a86562e4466f879c9647c3f13f7`. Exactly 39 changed paths confined to `sources/2026-W43/execution/` (preview files, handoff, session, index). main and Frozen Core unchanged.

r1 placed a real noncanonical PDF under `sources/2026-W43/execution/core-free-preview-r1/main.pdf`, declared SHA256 `fd88cb7c80805192364d80bcde3b48bbd0488896296c7f4e2d4076425a8b2a9b`, 480229 bytes, 22 A4 pages, 22 PNGs and three contact sheets; compiler log says clean, all 20 tables, 3 figures, 36 bibliography entries. Muse claims all-page visual PASS; **editorial Sol has NOT independently opened PDF binary/page images** in this environment because GitHub text connector does not transfer binary and external fetch was blocked. NEVER substitute tool/log read for actual independent visual inspection.

The independent r3.5 *textual* audit (20261026231458_SolReview.md) remains **PASS_WITH_LIMITATIONS**, original P1 `R32-FULL-003=FIXED`, remaining P0/P1=0. The r1 PDF source-to-TeX inspection does NOT reopen that independent P1 and does NOT authorize formal Core-native Stage or Gate.

**Confirmed print defects in actual r1 `main.tex` bibliography:** labels/source-confidence parenthetical descriptions were blindly truncated midword rather than safely edited. Examples:
- `MEMT-README`: `[FIRST_PARTY (24行: 保存容量約66倍削減=128K・full-context KV cache比、速度で]` — loses crucial `速度ではない` clarification.
- `voxtral-card-units`: cuts off after `Small/Re`, obscuring UNIT_UNVERIFIED.
- `deepinfer-import-scope`: cuts off after `IMPORT...=IMP`, obscuring import unverified.
- `patch-rendered`: cuts `upstream validat` before full 5-stage boundaries.
- `tanstack-gh`: cuts `...npm time[1.0.0] ... で裏づけ。別ソ`. The r3.3 crosswalk's GH source note is itself ambiguously worded; MUST NOT claim archived GitHub release raw proves npm registry timestamp. GitHub release raw proves **GH `published_at` 15:18:14Z only**; npm `time[1.0.0]` 15:21:49.491Z is accepted crosswalk-derived, `RAW_NOT_ARCHIVED`, scoped `https://registry.npmjs.org/@tanstack%2Fai`. Reader body must preserve this separation.
- `decisions-guide-1025` cuts after `no post-cutoff` and `decisions-ts-ref-1025` after `observation-time detail`, potentially confusing observed post-window documentation with W43 event.

This is a **reader-facing bibliography/source-tier integrity issue introduced during r1 TeX projection**, NOT a fresh scientific assertion or an independently audited r3.5 failure. Print-level changes REQUIRED before Human PDF presentation.

**Volume/editorial open gate**: current r1 is **22 total** pages = cover1 + TOC1 + body/closing 18 + bibliography2. Human approved W43 r6 Architecture target approximately 38, maximum 44, with estimated body+front/back ~37 and eight packages / 31 must-cover. The gap of 16 pages (~42%) cannot be dismissed simply on W42 final 21pp precedent. Padding, giant type, empty pages or unsubstantiated new prose are forbidden. Need evidence-grounded volume/depth/coverage evaluation, not a silent Architecture edit or automatic 38pp inflation.

## 2. Repair in a NEW r2 edition-local namespace

Create ONLY in `sources/2026-W43/execution/core-free-preview-r2/`, plus handoff `execution/SOL_W43_CORE_FREE_PDF_PREVIEW_R2_HANDOFF.md`, one new session worklog, append-only `execution/index.md`. r1 AND all r3.5 source/editorial/audit assets remain immutable. All `production-state.json`, Architecture r6, Selection/Evidence, Human approvals/gates, main and Frozen Core are immutable. Absolutely no canonical `surveys/weekly/2026-W43/main.pdf`, no formal publication/v2/ stage artifact, no Gate transition, no freeze/release.

### A. Bibliography and source classification — mandatory before TeX

- Rebuild all **36 bibliography entries** from r3.3 37-key crosswalk + r3.5 delta, with a positive `bibitem key → exact URL/absent URL → archive existence/source tier → clock precision → printed wording` inventory. For each, prohibit length-based blind truncation, incompletely closed parentheses, fragmentary labels, and text such as `速度で]`, `Small/Re]`, `=IMP]`, `upstream validat]`, `別ソ]`. Use short complete Japanese sentences **that preserve the pertinent negative/uncertainty qualifier**, not raw operator-coded 200-character descriptions. If needed, write a short informative inline tier and a separate explanatory table/caption/notes; no long URL dump or third bibliography page padding.
- Strictly distinguish **actual archived bytes** vs official published URL without bytes vs accepted-derived vs `RAW_NOT_ARCHIVED`/unverified vs post-cutoff supplementary observation. Do not let a public URL or archived GH blob become false proof of a different provider's source. TanStack GH/npm must be separately sourced and limited; MemT storage vs speed; Patch saved `RENDERED_TEXT`, stages4/5; Voxtral comparator/price units; DeepInfer pseudocode `IMPORT_UNVERIFIED`; DeepSeek license bytes unseen.
- No invented source date/URL, no upgrading `FIRST_PARTY` metadata to independently raw-verified just by label. Check that references actually appear in **printed** PDF and link to the right URL where available. Audit 36 labels for duplicates/unused/missing. The TeX source currently uses reader-visible `典拠キー` notes rather than `\\cite`; ensure a reader can reliably map each actual key to an unambiguous bibliography entry and clickable link, or document safe minimal improvement with no claim change.
- The user's accepted r3.5 Reader and all 29 claims, 20 tables / 80 source rows, 3 figures, P1–P8, 19 selected items, five-paragraph standalone recap after P8 MUST remain faithfully projected. No new editorial claims. Preserve raw confidence qualifiers; operator flags translated without meaning loss. Check no QA/internal file paths/asset-version labels leak into cover or publication headline.

### B. Grounded volume/depth report and editorial stop

- Create `architecture-coverage-and-volume-diagnosis-r2.md` grounded in actual approved `sources/2026-W43/architecture-v2.json`: enumerate **all 31 must-cover IDs**, locate each actual r3.5 reader paragraph/table/figure and **printed r2 PDF page** with a short substantive coverage assessment `SUBSTANTIVE / PARTIAL / NOT_VISIBLE`. Preserve independent prior baseline **20 SUBSTANTIVE_COMPLETE / 11 PARTIAL** unless separately audited; do NOT claim a new 31/31 authoritative audit on Muse say-so. Enumerate P1–P8 pages, useful paragraph/text chars and technical substance, 19 selected placements (12+7) vs printed coverage, unresolved depths per package, bibliography share, empty or sparse pages.
- Compare **actual** new PDF page count to 38 target / 44 max, with evidence why 22 or nearby may/may not represent approved scope. Do not infer that a 21-page W42 prior proves W43's 38-page editorial plan complete. Do NOT arbitrarily add content to reach target, tweak spacing as a proxy for depth, or unilaterally revise Human-approved Architecture; identify specific source-backed opportunities and evidence gaps for Sol/Human to adjudicate separately. If true depth/coverage materially below approved plan, terminal `VOLUME_OR_LAYOUT_REVIEW_REQUIRED` rather than silently `READY`.

### C. Build and visual proof (only if A fully passes)

- Versioned `reader-print-projection-r2.md`, `print-projection-diff-r2.md`, `main.tex`, `preview.sty` as needed, `main.pdf`, actual `main.log`, `build-manifest-r2.json`, bibliography-source-key audit, `reader-to-print-fidelity-and-citations-r2.md`, full-page `pages/p-01.png...` and contact sheets, per-page independent-inspection-ready `physical-page-and-table-qa-r2.md`, `independent-visual-review-request-r2.PROPOSED.md`.
- Exact audit-fixed original Reader `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`, ledger `6fd9d6fe75713376e108a094e03335571bfb248293d00c7ac713d1b0d382e6d4`, manifest `85d94d74f3cf3e9546a8acaf6ed775701817beaaa908b4999f8501a26a3cf111`. Confirm exact bytes. Run r3.5 edition-local checker only (not Core/native Stage), record exit/logs. TeX source-bib-fidelity checks; actual compiler commands/return codes, PDF binary SHA256 and page count.
- Render and inspect **every actual new PDF page**. Concrete focus: full 36-bibitem strings and tiers not clipped, the last bibliography page not blank/overly empty, all 20 tables readable with captions, no verbatim overflow, no font tofu, P8→5-paragraph recap→references, no broken sentences. Verify images and PDF remotely exist and are anchored to final HEAD. Do not declare Sol/independent visual audit executed by Muse.
- If inaccessible/broken tooling, write truthful blocker and STOP; do not claim actual visual inspection without images.

## 3. Gate, exit states and no false positives

A and B mandatory; if bibliography remains truncated or a 29-claim/source-reference regression exists, terminal `MUSE_W43_CORE_FREE_PREVIEW_R2_BLOCKED`.
If bibliography/print corrected and PDF/visual proof complete but 22-ish vs 38 volume still has unresolved **material technical coverage gaps**, terminal **`VOLUME_OR_LAYOUT_REVIEW_REQUIRED`** with exact section/page/31-requirement diagnosis. Do not self-approve via prior W42.
Only if A passes, PDF/source-image complete, B finds no material unexplained gap, stop `MUSE_W43_CORE_FREE_PDF_PREVIEW_R2_READY_FOR_SOL_RECHECK`. In ALL cases Human PDF Gate is PENDING, Stage is `ARCHITECTURE_ESTABLISHED`, Native Draft BLOCKED, no Release or Approval.

Sol will independently read r2 TeX/bibliography/depth coverage, commission separate visual/page reviewer, then ask Human to review actual PDF only if adequate. Any substantive new writing, sourcing, Architecture revision, Core bypass-to-release or native publication requires a separate authorized decision.
