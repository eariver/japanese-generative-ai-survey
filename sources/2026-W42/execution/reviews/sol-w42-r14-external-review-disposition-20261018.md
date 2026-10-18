# W42 r14 external independent review — Sol editorial disposition

Date: 2026-10-18 JST
Status: `SOL_EDITORIAL_DISPOSITION / EXTERNAL_REQUEST_CHANGES_ADOPTED / NO_PUBLICATION_AUTHORITY`
Source original: `20261018114652_SolReview.md` provided directly by Human Owner from a separate independent read-only session, stored outside repository on Google Drive. This is an **operative editorial disposition**, not a copy of the original full report, a second independent audit, a Human approval, or formal Core Stage evidence.

## 1. Audited identity and scope

Repository: `eariver/japanese-generative-ai-survey`
Existing branch: `weekly/2026-W42-v2-work`
Audited r14 HEAD/Tree: `781ce7653c00cadb59f245ec5c7342a0088da52a` / `9b67b93cc108fd012f7fbe0dce6db02f6236db4b`
r14 start HEAD/Tree: `36ebeaed4b462eb613875de56558c874e38a5f4a` / `4f1e82f15513d7f81afe6ebc64579e44e29e40f9`
r13 HEAD/Tree: `5520e8f5b1f3c07686873cdf75a7086761bdea14` / `a72302edbf2fbad6cf714e4db9dbdcec48519c2c`
Reviewed main HEAD/Tree: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / `801de813319f08777ab1581a5e8875fc1ac5df19`
Frozen Core v2 HEAD/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Independent audit verdict **REQUEST_CHANGES**. Reviewer read Git objects, compared 2 commits/47 changed files under `execution/`, checked preserved older r13 blobs, opened **all 17 PNG pages and both contact sheets**, byte-verified PDF and full LuaLaTeX log SHA256, checked critical NVIDIA and Earth AI primary sources. The reviewer did not independently rebuild TeX nor exhaustively check 153 source claims.

Sol read-only rechecked current branch HEAD `781ce7653c00cadb59f245ec5c7342a0088da52a`, unchanged main/Core HEADs and `sources/2026-W42/production-state.json` (lifecycle `DRAFT_COMPLETE`, architecture_review `approved`, publication_preview `pending`). Exact final r14 Git Tree above is from the independent auditor's direct Git Data inspection; Sol's available GitHub connector does not expose Tree in fetch_commit. No change of canonical Draft v10.0, accepted Evidence, Selection, Architecture, Human Gate or checkpoints is authorized.

## 2. Final adoption of r14 findings

### Major — MUST REPAIR before Reader/Publication

- **F-01 Earth GRA 4×2 false-positive inference:** r14 P6 `t6-06`–`t6-09` / PDF p12 emphasizes Gemini 3.8 Flash tool-only 52.2±5.4 → full GRA 62.7±2.5 (+10.5 pp), but omits Gemini 3.1 Pro tool-only **50.8±1.7 → full GRA 47.6±2.7 (−3.2 pp)**. Primary arXiv 2610.15750v1 Table 4/5; 3 repetitions mean±SD. State explicitly that planner effect is **model-dependent**, not universal, and represent full 4 configurations × 2 models with precise table-level citations. GeoKTools Pro example 84.5±1.4 →81.6±1.4 is another negative.
- **F-02 public benchmark split conflict:** paper gives GeoKTools 305, 85 dev/220 test; public repository README says 85 dev + **210 withheld test**. Treat this as unresolved document/version/snapshot discrepancy, not an editorial choice of convenient number. Verify source versions and archive an exact URL/commit and access date; explain what was actually released (development data vs withheld tests vs evaluator/code). Independently recheck CBGB sample count and its section/version. Never state nonpublic tests were released.
- **F-03 PDF p15 blank space:** P7 table and closing occupy a small part of page; r13 isolated table root warning fixed, but substantial page white space remains. Strengthen P7 grounded analysis **first**, then adjust flow, never insert padding.
- **F-04 PDF p16→17 bibliography split:** B48 long URL breaks at page transition; p17 begins with dangling `-challenges`; B49–B59 alone plus marker/large empty area. The r14 manifest's `14 entries` tail does not match auditor's observed actual placement. Repair entry-level page break/readability and report true page numbers; keep every bibliography reference. Do not silently delete links.
- **F-05 Architecture depth:** approved 28 selected entries (PRIMARY16/SUPPORTING12), seven chapters, 26.5-page planned article body, 28-page total magazine target, 30-page maximum. r14 has 112 paragraphs / 20,479 paragraph-only characters; proof 17 pages includes cover + only ~13.5 densely used article pages + bibliography/short p15. The delta between PDF page count and planned article-body allocation is **not** a literal missing-page count, but substantive method/comparison/negative/reproducibility coverage demonstrably fails. Editorial correction must be a full **Architecture-depth recovery** rather than successive 1k-character cosmetic increments. If credible primary-source detail is unavailable, stop and request Sol/Human decision; no architecture downscoping by Muse.

### Minor — repair in the same unit

- **F-06:** P6 repeated Flash 3→52→63 and aptamer 8-clone caveats; consolidate, replace with source-grounded Pro negative, population/method details.
- **F-07:** add original NVIDIA Training Recipe Stage-2 RL MTP Boosting Table 8 URL to bibliography and a claim-specific locator for t3-06/07; map Earth Table 4/5, aptamer figures/methods and vital licenses/benchmarks directly at claim/row level rather than broad repeated cite bundles.
- **F-08:** limit long citation trails (P1/P3/P6/P7), avoid repetitive boilerplate and translationese (e.g., `Gemini模型`, `追試の入口`), without deleting necessary uncertainty notices.

### Repaired and held as regression safeguards

NVIDIA MTP = **average acceptance length**, SPEED-Bench qualitative split, draft length 7, temperature 0 greedy 4.287→4.718, temperature 1 sampled 3.787→4.612. Under greedy, other compared models can exceed 4.718. Wet-lab 0/167→54/208→131/311 are per-round screening results; eight clones later measured separately. License rights remain document/file-specific (LFM/Beam/etc). Full r14 main.log verified and zero warnings; exact PDF SHA256 `9dfc15969fab490de44305df6618abeb4b37312cc445f0fae019cfad0bb7a2ee` and log SHA256 `2139a802d0fe6c121f8518a8ad77540ef5bf792678c7a5e4b88a133cb2c39f47` independently match. r13 historical bytes and frozen Core/State/Gates unaffected.

## 3. Editorial ruling — change workflow, not just text

r12→r13 paragraph chars +1,028; r13→r14 +1,286 while editorial proof went 19→17 pages after removing repetitive sources/repairing layout. **No invented paragraph-length quota** and no whitespace/typographic manipulation to force 28 pages.

r15 must first reconstruct an Architecture-to-evidence coverage matrix for all seven chapters with actual source-specific method, comparison controls, denominators, negative cases, replicability/rights and limitations. Then do substantial bounded original-source reading and manuscript revision; only re-render if genuinely supported content and claim localization are mature. Otherwise terminal `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED` with quantified gaps and options for Sol/Human. The approved 28-page target and seven-chapter Architecture are **not amended** by this decision.

r15 proposal and any generated PDF remain NONCANONICAL. Canonical Draft v10.0 and accepted architecture remain invariant; Human Architecture r1 stays approved; Publication Preview remains pending. No formal VALIDATED_DRAFT/Reader/Publication/Freeze/Release transition.

## 4. Next authority

Exact r15 execution contract:
`sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r15-architecture-depth-recovery-and-source-verified-editorial-rebuild.md`

Muse must confirm dispatch-supplied latest remote HEAD+Tree, main/Core HEAD+Tree read-only, no new/fallback/review branches, edition-local execution-only changes, normal commits and non-force push, and stop at `SOL_W42_R15_EDITORIAL_REVIEW_READY` or a truthful named blocker. Sol will assess technical/editorial maturity and decide when a targeted new independent audit is warranted. No Muse self-certification.
