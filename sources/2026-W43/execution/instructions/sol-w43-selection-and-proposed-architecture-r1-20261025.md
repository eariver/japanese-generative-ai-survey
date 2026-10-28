# W43 Sol → Muse Selection r1 + proposed Architecture for Sol audit (Frozen Core unchanged)

Status: EXECUTION_CONTRACT / SELECT_AND_PROPOSE_ARCHITECTURE / STOP_BEFORE_OPERATOR_STAGE_ADVANCE
Date: 2026-10-25 JST
Repository: eariver/japanese-generative-ai-survey
Branch: EXISTING weekly/2026-W43-v2-work ONLY.
EXACT six-source starting HEAD + root Tree will be dispatched by Sol after this contract and index are committed. Read-only preflight W43 remote HEAD/root Tree == dispatch; reviewed main HEAD 041a08dfef3112643cbf85b4a86a7b6f9128aed6, root Tree a134dc36a407d08ab1de416324229b3955e0325a; Frozen production/survey-core-v2 HEAD 774dd39a951c9ac3818e83dfffd4c7666efb0a20, Tree cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481. Any mismatch: ZERO WRITES STOP exact expected/actual. NO new/fallback/review/repair branch, reset, rebase, force-push or history rewrite.

## 1. Read exact authority first

- Trusted W43 operator receipt: sources/2026-W43/execution/bridge-runs/sol-w43-evidence-r4-advance-20261025/receipt.json; checkpoint sources/2026-W43/orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json; State sources/2026-W43/production-state.json MUST be EVIDENCE_REVIEWED, next stage:selection, checkpoints discovery/screening/evidence/materiality/completeness PASSED, selection/architecture pending, Human Architecture Review and Publication Preview both PENDING.
- Sol Evidence r4 independent review: sources/2026-W43/execution/reviews/sol-w43-evidence-r4-postcutoff-independent-acceptance-20261025.md (PASS_WITH_LIMITATIONS, NOT Human Gate). Muse evidence r4 proof and precise cutoff/source crosswalk and original independent r3 audit are mandatory. Original r1/r2/r3 content-addressed packages immutable.
- Current trusted r4 Evidence acceptance: sources/2026-W43/evidence/v2/accepted/fb6e5900b09ee77453aeaaf904d76fb56091fc977d61f82e4154e6f3787cf72b/evidence-accepted.json (32 PARTIAL).
- Current trusted Views: sources/2026-W43/evidence/v2/views/accepted/482a084e172d20450afe45c84933f69a0074a8244f823ae8b2589279d7d3858e/edition-views-accepted.json (20 MATERIAL / 10 CONTEXT / 2 NON_MATERIAL).
- Canonical materiality-ledger-v2.json 51 rows (19 Screening DROP EXCLUDED, 20 MATERIAL, 10 CONTEXT, 2 NON_MATERIAL); profile-completeness-v2.json LIMITED, current relevance+technical significance LIMITATION, carry-over SATISFIED. Kimi/Flint cite actual individual supplemental sources only, never fused Discovery pseudo-URL.
- Original Discovery 51 + Screening 51; 12 W42 carry incl 11 EXCLUDED and one CONTEXT; Grok/X sensor binder NON_MATERIAL NEVER_STORY with only two pinned post IDs. Github Metrics Oct23 23:42:03Z is **OUT AFTER CUTOFF** and r4 POST_CUTOFF/NON_MATERIAL; never a W43 new story, can be editorial W44 pointer only.
- Frozen first-party code/scripts schemas: scripts/run_selection_architecture_v2_interactive.py, scripts/survey_architecture_v2.py + base, scripts/survey_agent_tool_v2.py (current_stage_basis_override), scripts/survey_agent_control_v2.py, scripts/survey_stage_validation_v2.py; schemas candidate-matrix-v2, candidate-selection-v2, issue-architecture-v2, architecture-review-summary-v2; review-attention and applicable Profile extension contracts. W42 reviewed r9 Selection/Architecture method is reference for execution mechanics ONLY, not evidence/issue content. Frozen Issues #568/#569 remain open.

## 2. Selection editorial discipline — no automatic 20-article conversion

Derive the EXACT Core 32 Candidate Matrix from live State-pinned r4 authority and resolve all 32 Discovery IDs. Explicit 32 assignments SELECTED/HOLD/REJECT/INSPECT with nuanced per-ID source-backed positive and negative editorial rationale; no forced selected count. SELECTED requires PRIMARY or SUPPORTING and allowed Profile/Publication role namespace. Every NON_MATERIAL **must not be SELECTED**; especially:
- Github Metrics POST_CUTOFF/NON_MATERIAL: REJECT from W43; preserve historical source correction, W44 pointer only, NEVER W43 MAIN_EVENT.
- Grok sensor binder NON_MATERIAL/OTHER: REJECT, NEVER article nor unsupported corroboration.
- 19 Screening DROP remain excluded from Matrix/Selection; every W42 carry explicitly disposed, with allowed CONTEXT candidate as support only if truly relevant.
Evaluate each original 20 MATERIAL, not all guaranteed articles: true development significance, technical novelty, first-party consumption depth, reader explanatory value, in-window temporal identity, contradiction, duplication/cross-family overlap, available measurements/method/hardware/harness, licensing, deployment state, independent vs publisher-run experiment. CONTEXT records can be supplementary or rejected; HOLD/INSPECT if unclear, not forced into narrative. The two NON_MATERIAL excluded even if algorithm suggests. Document explicit reasons for reject/hold/inspect beyond mechanical labels.
Ensure independent audit P1 corrections remain intact: Google Cloud SELECT ENTERPRISE PRIVATE PREVIEW (not GA); Flint 512K supported vs 256K recommended and exact vendor speed context; DeepInfer environment variables; GitHub Metrics no article, proper request_count; FLUX conflicted clocks and speed ratios; Patch the Planet GPT-5.6 Sol with real article; MemT paper vs README license and quantitative baselines; science/Ming not independently reproduced. Remaining five audit LIMITED tracked; no source class inflation.

## 3. Architecture PROPOSED for content density and a real Human review

Build a coherent magazine reading path from the selected set; avoid both fragmented headlines and compressed shallow summaries. Group related research by mechanistic contribution rather than company press releases. Each package must have:
- Clear reader question / why now; primary and supporting candidate_ids (all must be SELECTED) and explicit source-bound mechanistic explanation.
- Meaningful must-cover requirements: architecture/training/inference/agent/security mechanisms, comparisons with baselines and denominator/hardware/harness limits, deployment/licensing/geography/availability, counterclaims/open uncertainties and reader significance as the topic demands. Enumerate critical technical detail that must appear later in Japanese prose, not just one paragraph per topic.
- Positive/negative contribution and limits per source; no fake independent benchmark claims, no premature weights availability, no unsupported OSI claim, no fused source URI.
- Volume plan with defensible technical density (a longer issue is preferable to a sparse one), but do NOT pad, prescribe arbitrary mandatory page counts or sacrifice evidence-bound accuracy. Architecture page plan must follow source-backed article depth; give projected package word/page budget as an **estimate**, not a later guarantee.
- Draftable cross-package synthesis is permitted only if frozen validator permits (at most ONE empty PRIMARY/SUPPORTING placement package, must be last in drafting order, other package has factual placements); avoid empty placeholder package simply to reach a target count.
- Human-readable natural Japanese descriptions without unnecessary Sino-Japanese neologisms or mistranslation. Retain precise technology identifiers, standard English loanwords, training/benchmark baselines.
- Every SELECTED candidate has at least one legitimate architecture placement OR a truthful Core-valid selected_exception with explicit limitation and approval attention. Other non-selected do NOT sneak into core primary packages.
- Explicit reviewer questions: cutoffs, missing original AA leaderboard, Oracle/AM-Bench substantive v2 deltas, deployment restrictions, subjective evaluations, old 5 LIMITED, materiality/Completeness LIMITED, Grok provenance, Kimi/Flint source split, and sections that would be thin without actual full paper body.

## 4. Exact Core-native production and validation boundary

Use frozen first-party runner scripts/run_selection_architecture_v2_interactive.py with full 32-ID edition-local interactive input and native agent-first adapter. Its canonical outputs are EXACT:
- sources/2026-W43/candidate-matrix-v2.json
- sources/2026-W43/candidate-selection-v2.json (status ESTABLISHED but machine checkpoint still PENDING until trusted Bridge)
- sources/2026-W43/architecture-v2.json (status PROPOSED, human_review all null)
- sources/2026-W43/architecture-review-summary-v2.json (READY_FOR_ARCHITECTURE_REVIEW only if true validation)
- sources/2026-W43/architecture-review-attention-v2.json
- sources/2026-W43/orchestration/v2/interactive/selection-architecture-input.json with expected audit metadata.
All must be genuine unchanged Core derivations and exact SHA-bound to trusted r4 package, LEDGER and Profile; if canonical paths already exist with different authority, STOP without overwrite and report. Run actual frozen Core validate_candidate_matrix and validate_selection; validate proposed architecture, derived review summary, attention; run EVIDENCE_REVIEWED -> SELECTION_COMPLETE Stage scratch precheck ONLY (no checkpoint writes). Future SELECTION_COMPLETE->ARCHITECTURE_ESTABLISHED Stage precheck requires accepted selection Stage: do not pretend it has been run at current State; report static architecture validator distinct from trusted second bridge stage. Agent State before/after unchanged and valid, negative tests: post-cutoff Metrics SELECTED rejected; Grok SELECTED rejected; omitted candidate; missing source; selected without role; architecture candidate not selected, duplicated placements, invalid package, tampered r4 SHA; distinguish Core validator rejection from editorial manual negative test.
No operator request, Issue #448 comment, ADVANCE_STAGE, fake Human Gate/approval, Draft, TeX, PDF, Publication Preview, Freeze, Release. No changes to immutable accepted Evidence/Views/Discovery/Screening, source raw, materiality/completeness, Production State, Checkpoints, main/Frozen Core, shared scripts/config/schema/tests/.github/AGENTS, W42.

## 5. Deliverables and stop

- 32-row editorial disposition table with reasons and original Discovery/Task/Card/View basis, selected roles, missing essential method/source checks; 19 DROP and 12 carry reconciliation.
- Per-package Architecture technical-depth map (proposed sections, key equations/variables or concrete procedure as supported; benchmarks including denominators; source-id/citation exact URLs; anticipated natural Japanese narrative and page/word budget). Quantify how many independent first-party full bodies and secondaries back each article; show notable absences, do not pass a content-starved package.
- Edition-local claim-to-true-primary-source exact per selected claim (not fused old Discovery), including rendered-only vs archived bytes, author/publisher vs independent reproduction and expected publication caution.
- Frozen runner and validator transcript, SHA-256 manifests, negative cases, active State and protected path diff, actual HEAD/Root Tree readback.
- New session sources/2026-W43/execution/sessions/muse-w43-selection-proposed-architecture-r1-20261025.md, handoff sources/2026-W43/execution/SOL_W43_SELECTION_AND_ARCHITECTURE_PROPOSAL_REVIEW_HANDOFF-r1.md, edition-local review packet sources/2026-W43/execution/reviews/muse-w43-selection-architecture-depth-r1.md, source crosswalk sources/2026-W43/execution/source-intake/w43-selection-claim-source-crosswalk-r1.md, index append, interactive archived JSON and its audit.
- NORMAL commits, NON-FORCE push on SAME existing W43 branch; final remote HEAD/Tree exact readback.

Stop EXACT `SOL_W43_SELECTION_AND_ARCHITECTURE_PROPOSAL_REVIEW_READY_R1`. Sol will independently evaluate article selection and proposed architecture, then (only if PASS) execute **two separate trusted bridge operations** sequentially and verify each receipt; still stop at actual pending HUMAN Architecture Review, and only the real owner can approve. If any Core-validation failure, stop BLOCKED with preserved true artifacts/diagnostic; NEVER issue a false READY status.
