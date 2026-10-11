# Sol W40 Selection r11 — Scope Decision and Core Re-entry Blocker

Decision: **`SOL_W40_SCOPE_PLAN_B_APPROVED / CORE_REENTRY_CONTRACT_GAP / SELECTION_ACCEPTANCE_HOLD`**
Date: 2026-10-10 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing work branch: `weekly/2026-W40-v2-work`
Reviewed Muse r11 HEAD: `5b63d0c9f49610996658afbe072f5c996a92ddb5`
Reviewed Muse r11 Tree: `0c6c67c9a4ef4feeddc23c06e06205c75b43587f`
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Related Core maintenance Issue: https://github.com/eariver/japanese-generative-ai-survey/issues/562

## 1. Git and execution integrity — PASS

- Exact starting authority HEAD `e45a845db406392191a819f5a99b0c68bc36d97c`, Tree `f045911d565c8e7b9243a65af1ee72df0b763d89`, matched read-only before work.
- Muse r11 content commit `b806316402e7fac53381a16910464fcfba0a4bc0` is child of starting HEAD; terminal closure commit `5b63d0c9f49610996658afbe072f5c996a92ddb5` child of content commit. Two normal fast-forward commits, **five** new W40-only files in remote compare. The local one-commit-behind workspace was aligned by `git fetch` + `git merge --ff-only`; no reset, force, rebase or new branch.
- Remote W40 HEAD and reviewed main were re-read by Sol; State still `EVIDENCE_REVIEWED`, next `stage:selection`, both Human Gates pending; Selection and Architecture pending. Accepted Discovery37, Screening37, Evidence35, Views35, Materiality37, Completeness and Stage checkpoint files unchanged.
- Muse r11 handoff and source ledger did not archive verbatim entire HF original HTML; they record original host JSON-LD and content SHA for independent verification. This is a documented content-capture limit rather than proof of missing first-party authority.

## 2. Publication timing — VERIFIED (article event only)

Original organization-authored issuer posts on Hugging Face:

| Subject | Original author/org | Host `datePublished` UTC | W40 status | Scope limits |
|---|---|---|---|---|
| AstaBrief 8B | `allenai` / Ai2Comms Kyle Wiggers | `2026-10-02T15:19:50.340Z` | IN_WINDOW | This is the **announced article**, not proof new model weights uploaded Oct2; HF model repository metadata predates W40; model Apache-2.0 and SFT mix CC-BY-NC-4.0 must be distinguished |
| AutoSynthData | `ServiceNow-AI` organizational authors | `2026-10-02T04:01:31.290Z` | IN_WINDOW | New method announcement, not confirmed standalone pipeline/code/dataset release; EnterpriseOps Gym pre-existing and separate; Hybrid/ITSM performance claims vendor-scoped and SFT-only |

The fixed W40 end-exclusive is `2026-10-02T22:00:00Z`. Both are first-person issuer technical releases via hosted publisher accounts. Muse r11 recorded original raw transport bytes (AstaBrief 169,199 SHA256 `d440b90083303f3d6a4b5906369f312039098996553bf6a91e369c0599e9ea9e`; AutoSynthData 210,484 SHA256 `d84a35e69695bc5b8bc531871d4c7d9a2082037eb2f89eaa32f8dd006ab56a44`); the raw byte records were not themselves committed, so hashes should be rechecked from issuer page when regenerating authoritative records. First-party org and author page, original prose, canonical links and hosting-platform timestamps independently corroborated by Sol. External aggregator observations merely corroborate dates.

**Remove the historical claim that original W40 Oct2 article publication hours are unknown**; it is no longer defensible. This does not establish first-ever weight or code release timing.

## 3. Editorial selection — APPROVE Plan B *as scope and materiality direction*

Sol approves including BOTH item-level original issuer-announcement events in the W40 material Selection set, subject to appropriate canonical Core revision and final role attribution:

- **AstaBrief:** method/system for reproducible cited scientific reports, open weights used in a one-pass Asta pipeline; technical focus on SFT/DPO curation, grounding and pipeline tradeoffs, 51.1 vs 178.5 second publisher-reported end-to-end times; explicit 2025-era comparison baselines, weights/data license split and weight-creation chronology. Do **not** phrase as newly uploaded weights on Oct2 or proven state-of-the-art performance.
- **AutoSynthData:** environment-verifiable failure-driven synthetic training tasks with target/multiply curriculum, sample/batch gates, positive/negative verifier checks, controlled Hybrid+ITSM publisher experiments; code unpublished, separate Gym pre-window. Do **not** claim open-source pipeline or independent replication.

Both can have substantial P6a methodology coverage without shrinking ContextLM/Olmo-core 3 or P6b. Muse proposed two extra PRIMARY and Plan B **30 SELECTED (22 PRIMARY/8 SUPPORTING), 1 INSPECT DGX, 2 HOLD W39 carryovers, 2 REJECT**. Sol approves **provisional material inclusion** and P6a expansion, not the final exact PRIMARY/SUPPORTING allocation or 30-item count until Core matrix and Selection are valid on amended authority. Provisional upstream Views would be **31 MATERIAL/2 HOLD/2 CONTEXT**; two screening-original INSPECT rows must be preserved unless actual contract demands otherwise. Two research-sweep DROPs remain separate EXCLUDED.

This is not a new wider 12-lane Discovery sweep or promotion of Cloudflare Web Search/Pi Durable (still unadmitted without original hour).

## 4. Core re-entry analysis and correction of impact assumptions

Muse's `execution/core-reentry-feasibility-r11.md` correctly identifies **`CORE_REENTRY_CONTRACT_GAP`**:

- `scripts/survey_production_v2.py::transition_state` disallows backward/nonmonotonic transitions.
- `scripts/survey_human_gate_v2.py::invalidate_pending_gate` requires a reached pending Human Gate / Architecture checkpoint already passed; impossible at current `EVIDENCE_REVIEWED`.
- No documented same-state upstream Acceptance supersession from Stage `EVIDENCE_REVIEWED`.

Do NOT force-retrofit pre-Architecture W40 by manually editing State/checkpoints or invoking pending-Gate invalidation. Preserve immutable original acceptances and their source SHA graph.

**Important minimization opportunity:** The r11 feasibility report assumes it is necessary to amend both Discovery and Screening. Reviewed `survey_architecture_v2_base.py::derive_candidate_matrix` derives candidate classes from accepted **Evidence/Card + Edition Views + Materiality** and `validate_selection` forbids SELECTED if `row.materiality=HOLD`; it does not directly prohibit a selected candidate merely because earlier Screening was `INSPECT`. Reviewed `survey_evidence_v2.validate_edition_view` can allow `MATERIAL` Views when the Evidence Card status is PARTIAL (though true source sufficiency still required). So the minimal safe route **may** be two first-party source supplement bindings, two Evidence Card/source/chronology revisions (if actually needed), two Views HOLD→MATERIAL, two Materiality row corrections, revised Completeness and exact SHA reattestation **without** changing original accepted Discovery 37 or Screening 37. This must be proved by the actual frozen Core validators and governance, not presumed. If a correct functional contract requires modifying Screening/Discovery, version and guard those as explicit larger-scope migrations.

A Core enhancement must support **append-only, SHA-bound, same-State reattestation** at `EVIDENCE_REVIEWED` before Selection/Human Gate, with old→new authoritative identities, fail-closed branch/State/approved Sol scope, exact ID allowlist, deterministic validation and no implicit Human approval. The existing `refactor/survey-production-core-v2` remote branch is **1,244 commits behind** the reviewed main, therefore is **not a safe default Core implementation target**. No new Core implementation branch authorized within the W40 contract.

The separate Core maintenance request has been filed as **Issue #562**: https://github.com/eariver/japanese-generative-ai-survey/issues/562. Shared Core remains unchanged and its older taxonomy defect CV2-DM-016 remains independent OPEN_CORE.

## 5. Next action and stopping boundary

Core maintenance must first receive a separately authorized, current, reviewed existing branch and exact Starting SHA/Tree, with normal review/PR integration. No shared Core fix inside weekly W40 without explicit authority. Once a reviewed Core-safe same-state supersession operation exists on main, a bounded W40 execution can:

1. Re-read exact accepted 37/37/35/35 and source/event claims; validate two original hosted source anchors and SHA.
2. Materialize minimal new versioned Evidence Card/Views/Materiality/Completeness with old↔new traceability, double-build and exact Core acceptance/checkpoint supersession.
3. Sol independently re-review changes, especially previously PARTIAL/HOLD role, Source relation/claim certainty and article-event vs weights/code.
4. Rebuild genuine Candidate Matrix and Selection **PREVIEW ONLY** under amended basis, then independently authorize formal Selection/Architecture transition.

**Selection Acceptance remains BLOCKED** pending the safe Core path. Present findings to user; do not claim W40 finished or take Human Gate action.
