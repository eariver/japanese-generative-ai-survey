# W42 Muse r15 — Architecture-depth recovery and primary-source-verified editorial rebuild

Date: 2026-10-18 JST
Status: `EXECUTION_AUTHORITY / SOL_R14_REQUEST_CHANGES / FROZEN_CORE_IMMUTABLE / R15_EVIDENCE_FIRST_EDITORIAL_REBUILD`
Repository: `eariver/japanese-generative-ai-survey`
Use **existing** branch `weekly/2026-W42-v2-work` ONLY.

## 0. Fail-closed identity guard before writes

The Sol dispatch gives a current **Expected Starting Remote HEAD** and **Expected Starting Tree** produced when this contract was committed. Read-only check the actual remote branch HEAD+Tree and require exact equality to the dispatch values. Also check:

- reviewed `main` HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`, Tree `801de813319f08777ab1581a5e8875fc1ac5df19`
- Frozen Core `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

A mismatch, missing tree, or unverified prerequisite => **STOP/ZERO WRITES** and report exact expected/actual. No newly created, repair/review/fallback or backup branch; no force push/rebase/reset/commit rewrite. Check remote unchanged before non-force push. Protected: all shared roots; main and Frozen Core; W42 canonical discovery, evidence, views, materiality, completeness, selection, architecture, canonical Draft v10.0/Synthesis, approvals, gate/checkpoints, Production State, and historical r11–r14 proposal/proof bytes. No fake human approvals or stage bypasses.

Allow r15 edition-local, PROPOSED/NONCANONICAL files under `sources/2026-W42/execution/editorial-revision-r15/`, if mature `.../preview-r15/`, `.../sessions/`, and an accurate append-only execution index update. All previous r14 and earlier output remains intact. Frozen Core CLI may be invoked read-only on new proposals; never edit its implementation or input authorities.

## 1. Read order / authoritative distinction

1. `sources/2026-W42/execution/reviews/sol-w42-r14-external-review-disposition-20261018.md` (this is Sol acceptance of Human-delivered separate external report, NOT the full raw report).
2. `sources/2026-W42/execution/reviews/sol-w42-r13-external-review-disposition-20261018.md`.
3. r15 current instruction and r14 Muse session, validation, source matrix, original-source reading sidecars, reader JSON/MD, all seven proposed Draft Results, citation ledger/bibliography map, TeX/PDF/build manifest, page PNG index/log.
4. Accepted 7-chapter Architecture and Human Architecture r1 approval; 28 selected (16 PRIMARY, 12 SUPPORTING) with authentic source/evidence references, including completeness LIMITED / VERIFIED0. Canonical Draft v10.0 is immutable.
5. Layout reference W41 in read-only fashion. r14 proof is NOT a formal Publication Preview.

Current fixed r14 audit HEAD `781ce7653c00cadb59f245ec5c7342a0088da52a`, Tree `9b67b93cc108fd012f7fbe0dce6db02f6236db4b`. Current state at dispatch: `DRAFT_COMPLETE`, architecture approved, publication pending.

## 2. Unit A — Architecture-depth gap analysis (mandatory BEFORE drafting)

Produce `editorial-revision-r15/architecture-coverage-and-depth-gap-r15.md` and structured `source-claim-matrix-r15.json` covering **all seven chapters and all 28 already-selected items**. For each PRIMARY item distinguish:

- approved Architecture subsection, claims presently published in r14 draft (exact block IDs), and what technical question the chapter promises but currently fails to answer;
- actual model/system design and data/control flow, method/setup, measured observable and denominator/units, comparator/baseline/confound, numeric uncertainty, negative/failure cases, deployment/reproducibility boundaries, and license/usage boundaries when applicable;
- direct original primary URL + section/table/figure/license clause + original document version/commit/access date and how that claim maps to bibliography and TeX;
- source-evidence status: VERIFIED_FROM_PRIMARY_TEXT / PUBLISHER_REPORT_ONLY / SECONDARY / SOURCE_INACCESSIBLE / UNKNOWN; distinguish read by agent from independent reproduction (NONE unless demonstrated);
- specific non-redundant reader analysis to add and estimate of depth gap by planned Chapter sections and existing **article-body** surface rather than PDF total.

For SUPPORTING items document factual, bounded comparison roles, source confidence, and whether reader section needs additional explanation. Do not treat all 28 as equally long or create 28 new independent stories. No re-selection, 7-chapter architecture change or unapproved scope additions.

Compute exact r14 baseline `112 PARAGRAPH / 20,479 paragraph-only chars` plus chapter P1 2,996; P2 2,761; P3 4,237; P4 3,121; P5 2,388; P6 2,873; P7 2,103. Distinguish JSON paragraph-only, all block text, body/PTN, chapter footnotes/tables, TeX bibliography, and rendered article pages. Cover + bibliography pages must not count as article-body pages. Do not set an arbitrary character quota.

**Do not stop Unit A with only a thin checklist**. Establish the primary-source work queue and prioritized concrete questions/claims to support coherent article sections.

## 3. Unit B — first-party/source-version deep research; factual priority gates

**P0 — must settle before any r15 render**
- **Earth AI GeoExpertQueries:** read Slonim et al. arXiv `2610.15750v1` (https://arxiv.org/html/2610.15750v1), actual Table 4 and 5 and evaluation methodology. Report 3 repeats mean±SD for 4 configurations × Gemini 3.1 Pro / Gemini 3.8 Flash. At minimum explicitly and symmetrically compare GRA-tool-only → full planning:
  - Pro **50.8±1.7 → 47.6±2.7**, **−3.2 percentage points**.
  - Flash **52.2±5.4 → 62.7±2.5**, **+10.5 percentage points**.
  - On GeoKTools Pro, **84.5±1.4 → 81.6±1.4** negative.
  These audit numbers are verification targets only, NOT license to copy them blindly; inspect original table and correct if source disagrees. Mechanism: tool availability is dominant in both, marginal planner effect model-dependent. Preserve error bars, autograder/human validation, failed calls included in costs and test saturation.
- **Earth AI public benchmark source discrepancy:** inspect the arXiv version AND https://github.com/google-research/geospatial-reasoning-benchmarks, document precise README commit/snapshot/version and effective release artifacts. Paper gives `GeoKTools 305 = 85 dev + 220 test`; repo README says `85 dev + 210 withheld test`. Do not 'resolve' by guessing. Distinguish published benchmark dataset overview, dev examples that are actually downloadable, private/withheld test, prompts/evaluator/scoring code available, and version differences. Recheck GeoExpertQueries 25 dev/76 test and CBGB 45 count against cited original sections. If different denominators refer to different scopes and are not reconciled, explain their origin/status side-by-side. Never call withheld tests open.
- **Nemotron Table 8 citation provenance:** independently open https://docs.nvidia.com/nemotron/latest/nemotron/super35/rl/index.html, `MTP Boosting / Table 8`; map the directly read URL and Table 8 in a bibliography key and exact block/claim ledger (r14 B20–B22 PDF report alone is not a shortest direct path). Preserve acceptance *length*, SPEED-Bench qualitative split, draft length 7, greedy temperature 0 4.287→4.718 vs sampled temperature 1 3.787→4.612, and non-universal model dominance.
- **Wet-lab:** verify 0/167→54/208→131/311 screening series and *separate* 8-clone titration, with actual measurement selection, hit thresholds and cited Fig./Methods from primary PDF where accessible. Do not infer same denominator over time or independent reproduction.

**P1 — substantive depth across remaining chapters, NOT another +1k-char incremental pass**
Use all accessible primary papers/technical reports/docs (source whitelist provided by accepted Evidence and properly introduced new versioned editorial sidecars):
- P1 Wonder/Argon/Active Memory/Focus: state persistence/verification checkpoints, long-horizon trial setup, single-run Minecraft limits, demonstrative ray tracer vs controlled benchmark, failure/rollback mechanisms.
- P2 Maia/HBM4/NUMA, prefill/decode: data/control/traffic path, compared physical capacity, bottlenecks and failure/queue cases; separate disclosed measurements from analytical inference. LFM evaluation denominator, runtime/batch/hardware and individual distribution-license clauses.
- P3 Nemotron/Spark/Beam/Granite/MiniCPM/FLUX: mechanism/measurement crosswalk for MTP vs tokens/sec, LiLiCorr/QAD/decode, KV layout/cache, source-appropriate permission levels and dependency clauses. Avoid equating model-card license statements with all deployment/commercial redistribution rights.
- P4 Codex/Scion/HydraFusion, Autofix/AI Scan/Decider: experiment population and CI metrics, WAL/cache contention and recovery, router decisions and cost/failover, separation of agent authority/security scanning gates and operational stop criteria.
- P5 unintended behavior/distillation/NIST ECDSA/METR: study designs, actor/timeline, offense/defense metrics and false positives, ECDSA seed-generation and residual uncertainty, evaluation-participant access vs results.
- P6 aptamer/GRA/Deep Review/SPOT/Rosalind: controlled experiment setups/denominators/baselines, negative results and measured resource costs; avoid duplicate explanations of 3→52→63/8 clones; distinguish provider terms from reproduced lab claims.
- P7 GLM-Legal/Vals/ASPIRE/Glimpse: independent vs vendor metrics, subject populations and methods, sim-to-real external validity/failure modes, API listing vs verified model/task capabilities. Address P7 low depth before page layout.

Read original figures/appendices/Methods where essential; don't infer inaccessible values. Deliver actual textual research synthesis with precisely located evidence and uncertainty, not only a link list. If many source gaps persist, create an `evidence-access-blockers-r15.md` with failed URLs/reason/impact and realistic alternatives without changing frozen Core.

## 4. Unit C — substantial Japanese editorial rewrite

Create fresh edition-local `editorial-revision-r15` seven `draft-result-r15.PROPOSED.json`, reader `.PROPOSED.md/.json`, claim-section crosswalk, bibliography-map, citation repair ledger, block diff vs r14, change ledger, proposed synthesis and checks. Preserve r14 source bytes.

Every substantive technical addition must explain **method → controlled comparison → observed result → counterexample/failure → applicability/limitations** where supported. Use tables selectively to convey dense cross-conditions (not to imitate filler). Do not overcorrect with repetitive formal disclaimers or excessively Sino-Japanese translations. For each approved chapter, document exactly what additional reader-understandable mechanism/evaluation analysis was delivered and what remains absent. Avoid merely expanding launch announcements or adding 1–2 decorative paragraphs per chapter.

Prevent citations that bundle 8–16 URLs at a paragraph end. For each crucial number, table row, license condition or provider/independent benchmark claim add direct `source URL → original section/table/figure/clause → edition-local claim/block → bibliography key → TeX \\cite` route. Modify bibliography count as needed (not required to remain 59): keep prior relevant references, add authoritative originals, avoid duplicate URLs, classify by publisher/vendor/academic/independent truthfully. Full URL strings need not be repeated in reader prose.

Retain protected regression invariants F01/F02/M01/M02/M06 and exact r14 historical versions. Source observations from edition-local sidecars can justify additional PROPOSED prose only when properly cited and scoped; do not retroactively label accepted Evidence VERIFIED or modify original accepted assets.

Validate all seven proposed Draft Results using the **frozen** Draft check, and run proposal Synthesis check without accepting or replacing canonical Draft. Store genuine logs/receipts, including negative outcomes. Measure paragraph/heading/table/note counts under reproducible definitions, r14→r15 net gain and de-dup effects by chapter. **No arbitrary word count or page-fill threshold**: quality and Source→Claim coverage are the gate.

### Editorial preflight / conditional branch BEFORE TeX

Write `editorial-revision-r15/architecture-content-readiness-r15.md` with per-chapter:
- planned Architecture technical subparts vs actually realized reader sections and their evidence;
- originally missing controls/negatives/methods now included with block IDs;
- actual remaining method/denominator/confound/evidence gaps;
- estimated article-body pagination from **real W41/r14 layout metrics, excluding cover/bibliography and p15/p17 whitespace**;
- a defensible judgement whether added primary-source-backed depth can sustain approved **26.5 article pages / target 28 total / max 30** without padding, or if this contract is structurally infeasible with accessible evidence.

A numeric character increase alone is insufficient. The goal is a true substantive magazine issue, not a render quota. If major Architecture sections remain unsupported/empty or research sources are inaccessible and the only way to produce the target is repetition/spacing tricks, **STOP BEFORE RENDER** at `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED`, commit finished evidence+proposals+matrix with truthful deficiencies and present concrete options to Sol/Human. Do not silently rewrite target/page allocation. That is a successful *bounded* transparent stop, not permission to force a PDF.

If substantial real evidence and chapter readiness are demonstrated, proceed with Unit D and provide r15 PDF; if a later post-render gap persists, report it unambiguously, not a false PASS.

## 5. Unit D — conditional real PDF proof and visual QA, only when editorially ready

Only after Unit C readiness:
- new `execution/preview-r15/main.tex`, edition-local style, actual compiled PDF, full LuaLaTeX `main.log` force-added as needed (historical r13 missing log must not be fabricated), complete page PNG set and contact sheets, verified linkable review index, build manifest with actual PDF and log byte lengths + SHA256, build environment/command/fonts and measured warning counts;
- fix r14 **p15 partial** by meaningful P7 analysis plus natural flow, not artificial spacing; fix bibliography `B48` URL broken across p16→17 with entry-safe pagination/wrapping and recheck actual visible entry inventory across all bibliography pages; preserve full references. Use correctly placed chapter-local tables; no cross-chapter table floats, clipped URL/glyph or isolated tail; no claim of visual PASS without actually opening every rendered PNG and contacts;
- leave title/footer `NONCANONICAL EDITORIAL PROOF / NOT A PUBLICATION PREVIEW`; new PDF is NOT human candidate or formal Reader output. Count *total* pages separately from *article body* pages. Never pad 28 pages with typography or duplicative references;
- if technical content remains too short, describe the gap and return decision authority to Sol instead of silently lowering Architecture goals.

## 6. Mandatory deliverables, verification and STOP

At least:
1. `execution/editorial-revision-r15/architecture-coverage-and-depth-gap-r15.md`
2. `execution/editorial-revision-r15/source-claim-matrix-r15.json`, source-readings/version receipts, claim locator mapping, Earth benchmark source-discrepancy audit and exact 4×2 comparison with SD
3. Seven `draft-result-r15.PROPOSED.json`, reader preview, Synthesis proposal and real frozen-CLI checks (or explicit block if impossible)
4. `execution/editorial-revision-r15/architecture-content-readiness-r15.md` with chapter-specific coverage and honest target assessment
5. If preflight passed: full noncanonical PDF/TeX/log/PNGs/contact sheets/manifest/page index; otherwise a precise no-render reasoning, evidence blockers and priority research next steps
6. `execution/editorial-revision-r15/validation-report-r15.md`
7. `execution/sessions/muse-w42-r15-20261018.md` and append-only `execution/index.md` status.

Recheck remote exact HEAD before commit/push (normal/non-force), commit only edition-local paths, verify remote read-back and no historical r13/r14 blob drift, record final HEAD+Tree and path inventory. Report machine stage still `DRAFT_COMPLETE`, Human architecture approved, Human publication pending. Preserve README/links/negative examples' provenance.

Terminal outcome:
- `SOL_W42_R15_EDITORIAL_REVIEW_READY / NONCANONICAL` if content maturity and optional proof completed; OR
- `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED / R15_EVIDENCE_AND_PROPOSALS_DELIVERED` if evidence cannot support the promised depth; OR
- an explicitly identified technical blocker with no false success claims.

**NEVER** run formal Reader/Publication acceptance, alter canonical Draft/Checkpoint/State/Gate/Core/main, or submit a Human Publication Preview. Sol determines independent-audit scope only after actual r15 results and may seek Human editorial decision if Architecture feasibility is limited.
