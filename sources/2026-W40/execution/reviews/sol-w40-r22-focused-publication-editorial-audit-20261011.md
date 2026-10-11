# W40 r22 — Sol focused Publication Preview editorial audit

Status: `BOUNDED_REVISION_REQUIRED / HUMAN_PUBLICATION_PREVIEW_APPROVAL_HOLD / NO_GATE_DECISION`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`, existing branch `weekly/2026-W40-v2-work`
Exact reviewed r22 final HEAD `ae22a5837fe453b177a3e72dfe948b1b69328b39`, Tree `1429c88abd3af8650674d09ec0d103ab74b28d27`
Reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (unchanged)
Earlier r21 Sol+independent audits: `execution/reviews/sol-w40-r21-publication-preview-editorial-audit-20261011.md`, `execution/reviews/w40-r21-independent-publication-editorial-audit-adoption-20261011.md`.

## A. Official transition and Core freeze independently confirmed

Six normal commits advanced from Sol r22 outer starting SHA `98b020d8ad04cb41c931ae9f563af57b36c2cc0f` to Muse final HEAD. Changed files are only `sources/2026-W40/` and `surveys/weekly/2026-W40/`. There are NO shared Core scripts, config, schema, workflows, main, other editions, or branch operations in the compare. Core v2 remains unchanged.

Official `gates/reviews/publication-r1.json` records Human `PUBLICATION_PREVIEW / REQUEST_CHANGES`, boundary `ARCHITECTURE_ESTABLISHED` and real UTC formal record time, reviewed old Candidate, r1 indexed. Current `gates/review-index.json` has Architecture r1 `APPROVED` and Preview r1 `REQUEST_CHANGES`. Current State is `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`; Architecture approved/provenance intact; Preview pending/null; machine Draft/Validation passed, Freeze/Release pending. No unauthorized Human Preview approval was found.

Canonical Architecture Git blob remains `231a4f588ae567bea2b974a65ff80048a8358015` (raw SHA-256 `a9b5c1182671bb913fbf56972907e19731e5ba4a928deaca9903a0d3a1461a44`). 28 Selected (20 PRIMARY/8 SUPPORTING), 4 HOLD, 3 REJECT, 9 Packages, 31 approved must-cover and Boundary 113 original per-Candidate literal relations /105 architecture entries /97 globally distinct literals unchanged per r22 handoff and upstream equality; no independent exhaustive assertion that every Boundary's **meaning** is adequately communicated.

## B. Real PDF integrity but independent visual examination unavailable

Publication Candidate SHA-256 `2cb17796ee620c0da4e9ed7142cb70c4d1975b728109a61d88e7cbd40c570017` points to `surveys/weekly/2026-W40/main.pdf`, `READY_FOR_PUBLICATION_PREVIEW`, with **14 pages**, **451,313 bytes** and PDF SHA-256 `c0b2fe1e4517bec8b3f85a4a518ed258be0de93b45f3e99c22ad75f93aae9704`.

Sol downloaded complete PDF bytes through GitHub connector `fetch_file(encoding=base64)`, decoded raw original bytes, and independently recalculated exact SHA-256. **MATCH**; Git blob `fe57c12e56558763cff8704f351412a584963eb2`, valid `%PDF-1.7` header, 451,313 bytes. Recorded 14 pages are from candidate/preflight/worker, not an independently rendered-page count. Muse states 14/14 pages visually checked at **60dpi**; Sol could not mount/render every page and therefore **PDF_VISUAL_NOT_INDEPENDENTLY_VERIFIED**. At least 150–200dpi page-by-page inspection, especially tables, math and Japanese glyphs, remains recommended before Human approval.

## C. Actual content scope — meaningful improvement, but insufficient deep explanations

Directly compared all 9 `draft/v2/packages/{P1,P2,P3,P4,P5,P6a,P6b,P7,P8}/draft-result.json` files between r21 Muse commit `832808af95df29547d7050452fdac7bb3df80f2e` and r22 `ae22a5837fe453b177a3e72dfe948b1b69328b39`. Count only `PARAGRAPH.text`; exclude `TABLE`, `CLAIM_BOUNDARY`, headings and metadata.

| Package | r21 chars | r22 chars | Evaluation |
|---|---:|---:|---|
| P1 | 527 | 1191 | Significant improvement: complete Sonnet/Argon card and comparison table |
| P2 | 417 | 654 | Actual model table, both ELYZA SHAs and license split |
| P3 | 535 | 874 | Chronology and API/weight/model classification improved |
| P4 | 454 | 535 | Small rewrite; still product summary rather than actual technical workflow |
| P5 | 651 | 973 | Some expansion but five domains still compressed, only one full section, no separate five subheadings |
| P6a | 1176 | 1687 | Equations + comparison added but mechanism/GRPO and MoE systems still dense |
| P6b | 952 | 1117 | Limited expansion; several metrics are still just named |
| P7 | 769 | 1274 | Table, vendor metric labels and correct event timing improved |
| P8 | 200 | 248 | Supporting-only digest appropriately short |
| **Total** | **5681** | **8553** | **+50.6%**, paragraphs 29 → 36, tables 0 → 4, TeX display equations 1 → 3 |

This demonstrates real authoring and some improved clarity; unlike r21, a full-rewrite finding across *every* section would overstate the remaining problems. Nevertheless, visible TeX has each selected item compressed into very few sentences and some important mechanisms remain uninterpretable. Page count is not a pass/fail quota.

## D. Specific findings on actual TeX (SHA-pinned line numbers)

### R22-F01 / MAJOR / P6a mathematical semantics and explanatory depth

`surveys/weekly/2026-W40/sections/60-training-systems.tex:9–16,20–39`.

Eq.5 skill optimization with frozen model weights is now clearly stated. However the displayed line 14

`FLOPs_prefix-reuse = FLOPs_prefill + FLOPs_decode`

omits the **unmatched-context suffix and newly generated token scope** that the same section's prose and approved r15 technical prep explicitly use for Eq.3. Without specifying arguments/summation bounds, it can be read as total prefill+decode FLOPs rather than prefix-*reuse* FLOPs.

The displayed `A_i^eff = clip((bar c_g - c_i)/bar c_g,-1,1)` on line 15 gives just a component of the Eq.6 success-gated efficiency-GRPO mechanism; r15 technical prep `execution/technical-prep-r15/p6a-deep-draft.md:51–63` says fewer than 2 successful trajectories means **efficiency component zero** and combined advantage `A_i=A_i^out+w_eff*A_i^eff`, not an unconstrained unconditional clipped expression. The prose mentions the fewer-than-2 condition, but readers need properly qualified equation(s) and variables, and a worked distinction between skill evolution under frozen parameters and weight-updating GRPO. Olmo-core 3 DDP / expert routing / grouped GEMM / MXFP8 is still a one-paragraph compressed stack without an explanation of division of roles. Preserve actual source bounds; do not fabricate unopened primary details.

### R22-F02 / MAJOR / Reader-facing internal process leakage (new)

`surveys/weekly/2026-W40/sections/70-multimodal-serving.tex:28`:

`従来の下流分類にあった対象期間後の扱いは誤りであり...承認済みアーキテクチャと受理済み証拠の文言自体は改変しない。`

This discusses **internal editorial state and immutable authority** in ordinary published prose. It contravenes `docs/editorial-style-guide.md §2`, which explicitly keeps repository/checkpoint/editorial metadata OUT of the magazine body. The correct useful reader statement is only that NVIDIA announced a livestream scheduled Oct 1 09:00 PDT (= Oct1 16:00 UTC), **inside W40**, and that delivery/content of the session was not independently verified. Keep approved-Architecture correction/provenance in Source Notes/edition-local erratum, not reader body. The Core Reader Surface Gate PASS missed this semantic leak.

### R22-F03 / MAJOR / P5 five safety scopes still not independently explained

`surveys/weekly/2026-W40/sections/50-safety-provenance.tex:9–17`.

Five items are present, but there are no five distinct article subsections and ProvenanceGuard numbers (281, 138/139, F1 .802/.858 etc.) are still dense, with actual meanings/settings and method order underexplained; OpenShell and Sentry isolation/monitoring boundaries and SynthID Bio assay context remain terse. Owner's r22 content instruction explicitly wanted five individually meaningful subsections. This is not a demand for equal length: supporting safety cases/OAuth should remain bounded.

### R22-F04 / MAJOR / P6b methods & measurement definitions

`surveys/weekly/2026-W40/sections/65-eval-infra.tex:9–15`.

OpenTTS TTFA 50 English prompts/batch 1/three warmups/median/H200, Oct7 script timing, and AgentPerf single-user vs production distinctions are preserved. However `RTFx`, `SIM` are merely named without explaining their actual evaluation semantics (WER and CER only alluded to). AgentPerf's '14 speculative configurations' and bandwidth roofline remain stated, not technically explained; Hub has no concrete runnable reproducibility model beyond missing pins. Add source-bounded definition/one example for reader comprehension; do not imply scripts/benchmarks were independently rerun.

### R22-F05 / MODERATE / P1 discount ambiguity

`surveys/weekly/2026-W40/sections/10-frontier-models.tex:15,25`.

`Gemini 4 Argon導入入力$2/出力$10で95%割引、導入後$4/$20` is copied from original Evidence. The explicit price sequence represents a 50% difference, **not 95%**. This is not proof the source fact is false: 95% may concern some separate promotion. Separate the subjects/units and identify the qualifying base, period and scope from already approved source; if unknowable, state 95% condition unverified and do not attach it to price pair as a mathematical discount. Do not silently change accepted Evidence.

### R22-F06 / MODERATE / content still compressed in other chapters

P4 `surveys/weekly/2026-W40/sections/40-devday-surface.tex:9` still refers to approval/sign-in responsibility in a single abstract sentence; the source changelog was only partly read, so expand within accepted bounds rather than invent an end-to-end workflow. P3/P7 terminology is much improved but still sometimes uses `界面` or opaque shorthand. Keep P8 concise. Frontmatter and synthesis now broadly more natural but several pipeline-derived "今週" statements are generic.

### R22-F07 / QA and visual-quality caveat

The `execution/reviews/w40-r22-must-cover-31-ledger.md` is improved from r21: 31 requirements are linked to quotes and actual blocks/tables. But its all-31 `AUDIT PASS` remains self-evaluated by the same worker, and the gaps above show `FULFILLED` does not imply explanatory adequacy. Core schema/checkpoint correctness is separate from independent semantic editorial review. Muse's 60dpi visual inspection and candidate preflight support structural readyness, not an independently sufficient high-resolution visual PASS.

## E. Disposition and next actions

**Final Sol focused verdict: `BOUNDED_REVISION_REQUIRED / PUBLICATION_PREVIEW_HOLD`.** This is less sweeping than r21: content definitely improved, 4 tables exist, 3 equations exist, Source Boundaries and candidate set structurally appear preserved, and version/time fixes landed. No need to discard r22 and do another full restart of Discovery, Selection, Architecture or entire draft. For publication, first correct the focused MAJOR issues R22-F01–F04 and the ambiguity F05, then visually inspect a new PDF at readable DPI.

Currently there is NO newly authorized Human `REQUEST_CHANGES` for the r22 Publication Preview. The Owner merely reported Muse work completion. Therefore Sol MUST NOT invoke the Core Human Revision Gate or impersonate a new Owner review. Current Gate `pending`, Freeze and Release forbidden. Do not alter Draft/TeX/PDF or official authority from this review.

Recommend a separate blind-first read-only independent Sol High review **if Owner wishes**, or Owner review of the real r22 PDF and findings, before explicit r22 Human Preview disposition. Any formal subsequent revision must use unchanged Core `request-publication-preview-revision` r2, with an authorized valid boundary preserving Architecture approval, by Muse in existing branch. **Core v2 must remain immutable.**

Reader review PDF URL pinned:
`https://github.com/eariver/japanese-generative-ai-survey/blob/ae22a5837fe453b177a3e72dfe948b1b69328b39/surveys/weekly/2026-W40/main.pdf`
