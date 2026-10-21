# W42 r15.1 — Sol editorial disposition of independent Architecture/depth review

Date: 2026-10-18 JST
Status: `SOL_EDITORIAL_DISPOSITION / R15_INDEPENDENT_REQUEST_CHANGES_ADOPTED / NO_PUBLICATION_AUTHORITY`
Original audit: `20261018134400_SolReview.md`, user-delivered Google Drive GPT-Sol_Review file. The audit was interrupted before its reply was returned; the Human additionally supplied a subsequent read-only clarification/reverification response. The latter reinforces but **does not constitute a second independent full audit**. Neither source is claimed to be committed here; this document is the **operative Sol ruling**, not a verbatim copy or new external audit.

## 1. Audited identity and status

Repo `eariver/japanese-generative-ai-survey`; branch `weekly/2026-W42-v2-work`.
Fixed audited r15.1 HEAD `523dbf757d0168c98096947e861e28197dff73b0`; Git Tree `06663d373dd1af43a206850296220e729b86ffae` as independently read from Git Data by auditor.
r15 start HEAD/Tree `031f5361b1134c815d739d84517b0203afcd4c30`/`75c698c553a6bf10ad4abb7345c484473e210660`.
Reviewed main HEAD/Tree `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`/`801de813319f08777ab1581a5e8875fc1ac5df19`.
Frozen Core v2 HEAD/Tree `774dd39a951c9ac3818e83dfffd4c7666efb0a20`/`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
Sol has independently rechecked current HEADs, branch no-divergence, and canonical `production-state.json` blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`: `DRAFT_COMPLETE`, architecture Human approved, publication preview pending. No Core/main/canonical changes authorized.

Audit findings: r15.1 technical quality `REQUEST_CHANGES`, 7 chapters/28 items substantial coverage `PARTIAL`, further source retrieval `NECESSARY`, Muse 9,400 chars / 6–7 body pages estimate `PARTIALLY_SUPPORTED` direction only, approved Architecture allocation `REVISIT_RECOMMENDED` but NOT amended, next `MORE_RESEARCH` followed by `DIAGNOSTIC_RENDER`.

## 2. Adopted findings and exact repair priority

**HIGH (first, source-confirmed before new prose/render)**
- F-01 P1 `t1-11/t1-23` Argon Minecraft: draft contradictory random-world versus `固定種`. Original https://arxiv.org/html/2610.22319 describes randomly generated Easy world; use precise source section, distinguish trial setup, resets, failure, seeds and count denominators. Naturalize `程序`, `229通`, `605死`; no preselected/fixed-seed invention.
- F-02 P2 `t2-03/t2-11/t2-14/t2-20` Maia rack: **24 trays × 4 accelerators = 96 accelerators per 167-kW rack**, NOT 96 trays. This is independently cross-checked against https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ (rack-scale architecture). Fix every body/table/sidecar instance and date/rollout scope. Do not transform vendor comparisons against unnamed baselines into independent measures.
- F-03 P7 `t7-05/t7-09/t7-17` ASPIRE: publicly accessible **real-robot skill-transfer** experiment https://research.nvidia.com/labs/gear/aspire/ and https://github.com/NVlabs/ASPIRE/blob/main/README.md. Distinguish simulations versus physical robot tasks, with-vs-without simulation-learned skills, output/total tokens until first successful code, held-out success rate of the first-success code, n/task constraints and vendor self-evaluation status. **Do not make up data hidden in interactive figures** or call it third-party reproduction.
- F-04 P6 `t6-06/t6-08/t6-21/t6-23`: Earth AI original https://arxiv.org/html/2610.15750v1 Table 4/5, 4 configurations × 2 models × three repetitions; distinguish same-model/same-benchmark planner incremental effect from tool availability and separate cross-model comparisons. Pro tool-only 50.8±1.7 → full 47.6±2.7 (−3.2pp); Flash 52.2±5.4 → full 62.7±2.5 (+10.5pp). Include informative Table-5 domain negative cases (e.g., Site Selection) **only after reading original table**. Mean±SD, evaluator, failures-included cost and saturation. Keep paper-versus-repository GeoKTools 220/210; templates 18/19 & 74/72, and CBGB 44 scored vs 45 curated **unresolved and attributed to exact source/version**. Test splits remain withheld; no claim of public test release.

**MEDIUM (same unit)**
- F-05 Wet-lab `t6-02/03/12/18`: original https://www.gstatic.com/science-ai/agentic_aptamer_sandbox.pdf Methods: screen 131/311 and eight selected-clone subsequent assays are DIFFERENT populations/measurements. Verify hit thresholds, selection path and measurement where source accessible; else precisely mark not read/unknown. Keep MSA false-improvement and separate VERID/epitope scopes.
- F-06 technical repeats P2 `t2-14/20,t2-10/17,t2-08/21`, P4 `t4-03/21,t4-06/07/23`, P5 `t5-06/08/19`, P7 `t7-02/18,t7-07/19`: merge if no new mechanism, baseline or measurement; preserve core facts and role coverage.
- F-07 citation URLs: `bibliography-map-r15.json` B69/B73/B88 contain commentary appended within URL strings; remove from URL and store in separate provenance field. Identify URL aliases (B62/B65/B86/B87), validate direct source/section/table/clause against claim and TeX; don't mistake all `http` strings for valid URLs. LFM https://www.liquid.ai/lfm-license §2/3/4/5/11; $10M threshold is **annual revenue of the Legal Entity**, not profit or model-only turnover. Check per-weight-license scope separately.
- F-08 Architecture and pagination: approved seven chapters, 28 selection, body-plan 26.5 pages, magazine target 28 and max 30; existing PDF 18pp is **old v15.0**. Actual r15.1 visual page count UNKNOWN. Prev Muse `36,800−27,415≈9,400 chars` and `6–7 body pages short` are not reliable exact deficits; cover/bib floats matter and 26.5−15/16 would be 10.5–11.5 if matched like units. Do not make silent target change or claim render already done.
- F-09 count baseline: r15.1 `136 PARAGRAPH/24,162 paragraph chars/7 TABLE/7 NOTE`. Plain sum of block.text for PARAGRAPH+TABLE+NOTE **27,284** vs Muse PTN **27,415** (131-char unexplained difference). Record both + exact algorithms and source of difference; don't label either fraudulent without tracing.
- F-10 Japanese: replace translationese `程序`, `地球引擎`, `台座再配布`, `定数旗依存`, `再現符号`, `未開`, etc. Preserve original nuance, no excess Sino-Japanese or repetitive generic warnings.

**Regression invariants**: NVIDIA SPEED-Bench native MTP **average acceptance length**, not acceptance rate; draft length 7; temp 0 native 4.287→4.718 vs sampled temp 1 3.787→4.612; wet-lab denominator separation; Beam/LFM/Muse model weight license evidence levels; vendor vs independent attribution; issue cutoff chronology; the Earth Pro negative; r13/r14/r15 history; formal lifecycle.

## 3. Editorial ruling

The full audit shows **specific fact errors and publicly accessible missed methods**, so neither a Human Architecture amendment nor acceptance of the current manuscript is appropriate yet. Adopt option **A: preserve approved Architecture while performing bounded source/depth correction**, then actual diagnostic pagination measurement. Option **B: revision of only page allocations** may be brought back for Human decision **after** improved manuscript and measured article-body vs nonbody page breakdown; no architecture schema/page plan edits now. Option **C: structure/reselection** unnecessary at this stage.

Old Architecture was approved under 43 PARTIAL/7 NEEDS_MORE/0 VERIFIED Evidence and Completeness LIMITED; 26.5 body pages/28 total were not backed by reliable page-density accounting, especially cover + bib already ~3 pages. That is an editorial uncertainty, **not** authority to revoke Human r1 or rewrite it.

No fake min/max character quota; assess new facts/methods/controlled comparisons and their source correctness independently from total pages. Diagnostic TeX must be generated from exact updated proposal bytes in an isolated temp workspace. For independent reviewer access, an explicitly stamped immutable **NONCANONICAL DIAGNOSTIC ONLY** copy and all-page PNGs may be archived under `execution/diagnostic-r16/`; this is NOT the formal Reader/Publication Preview path, must never be used as a Human Gate candidate, and does not change canonical Draft/State.

## 4. Next execution

Authorized bounded unit `sources/2026-W42/execution/instructions/2026-10-18_muse-w42-r16-bounded-source-depth-repair-and-diagnostic-render.md`.
Existing W42 branch only, exact dispatch SHA/Tree before writes, normal commits/non-force push, ZERO WRITES on mismatch, all r16 changes under W42 `execution/`, no frozen Core/shared roots/canonical Draft/Architecture/State/Gate/checkpoint changes. Terminal `SOL_W42_R16_DIAGNOSTIC_EDITORIAL_REVIEW_READY / NONCANONICAL` or truthfully reported block. No formal Reader/Publication/Freeze/Release.
