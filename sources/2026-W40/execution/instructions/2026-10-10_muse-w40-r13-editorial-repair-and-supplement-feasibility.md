# Muse W40 r13 — Audit repair, DGX disposition, current-Core supplement legality, deep Architecture preparation

Status: `SOL_BOUNDED_EXECUTION_REQUEST / EDITION_LOCAL_ONLY / STOP_AT_SOL_R13_REVIEW`
Date: 2026-10-10 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W40-v2-work`
Exact Starting HEAD and Tree: MUST come from the outer Sol handoff after this instruction commit.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Sol r12 disposition: `sources/2026-W40/execution/reviews/sol-w40-r12-independent-audit-disposition-20261010.md`
Core debt: [Issue #562](https://github.com/eariver/japanese-generative-ai-survey/issues/562) / `CV2-DM-022` in `docs/core-v2-deferred-maintenance-summary.md`.

## 0. Binding limits and goal

Human direction: **Shared Core v2 bugs are fixed in a separate maintenance task**. Weekly/Special production MUST NOT patch shared Core. Continue edition-local work and test lawful compatibility; do not wait idle for the Core task where editorial drafting remains possible.

Sol accepts independent r12 `REVISION_REQUIRED`. r12 28 SELECTED / 35 assigned, basis SHA and change-only logic are preserved as validated review-only artifacts, **not formal Selection Acceptance**. r13 is an editorial repair and current-Core publication-feasibility investigation, NOT a machine-stage progression task.

### Mandatory read-only starting guards

Before any write, confirm:
- remote work branch HEAD == exact outer Starting SHA, HEAD tree == exact outer Starting Tree;
- remote main HEAD == `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (unless outer prompt explicitly gives another reviewed main);
- production-state remains `EVIDENCE_REVIEWED`, next `stage:selection`, selection/architecture checkpoints and both Human Gates pending, Gate provenance null;
- accepted 37 Discovery/37 Screening/35 Cards/35 Views/37 Materiality + Completeness and all checkpoint SHAs match pre-r13.
Failure: ZERO WRITES; report expected/actual and stop.

No new/review/fallback branches; no reset/rebase/force/history rewriting. Normal commits and non-force push ONLY. No `scripts/`, `schemas/`, `config/`, `.github/`, `main`, other editions, or shared Core docs modifications. No direct State/checkpoint/Human Gate edits; no stage transitions, no Selection Acceptance, no issue updates, no human/owner authority impersonation.

## 1. Detailed editorial corrections (F03–F05)

Create `execution/editorial-supplement/r13/` revised **noncanonical** technical notes and source ledger; preserve r12 notes as immutable review evidence.

AstaBrief:
- Distinguish ~47K usable SFT examples, public 39.5K SFT Mix, filtering on citation-density (0.25 threshold *only when verified from actual dataset card*), and whether 39.5K is exactly a subset/training set. Do NOT invent a causal 47K→39.5K lineage if original source does not prove it.
- Distinguish ~6K DPO comparison pairs versus public 6,622 dataset rows. Name judge models (GPT-4.1 and DeepSeek-R1), reported human preference correlation/agreement (95%) only if primary sources show exact conditions and sample size.
- Keep 51.1s vs 178.5s specific to Fast vs Thinking in Asta, ~3.5× end-to-end vs generation-time speed wording, 2025-vintage baseline/eval and no current-SOTA claim.
- Preserve weights Apache-2.0 vs dataset CC-BY-NC-4.0; identify any independently documented third-party generative-output provider terms.
- Keep grounding, citation density, precision and scope drift technically distinct.

AutoSynthData:
- Correct soundness = invalid/unsuccessful trajectories cannot be accepted as successes; completeness = all valid alternative solutions must not be excluded. Include clear positive/negative acceptance/rejection examples.
- Add Hybrid experiment settings: 2,000 samples / ~18h / best epoch 5; compare symmetrically to ITSM 1,994 / 66h, keep measured metrics, target/teacher and limitations separate. Do not conflate +7.2 percentage points vs 35% relative.
- Replace unqualified 'NO standalone pipeline...' with 'not independently identified in bounded checked sources at retrieval time'; do not convert 401/negative search to proof of no implementation.
- Preserve TARGET/MULTIPLY, solver-band gate, verifier tests, bounded retry, SFT-only and EnterpriseOps Gym distinction.

Source ledger:
- When possible independently retrieve original issuer-org hosted HF HTML and parse `datePublished/dateCreated/dateModified` plus `rel=canonical` and issuer/author/host relation; capture request method/URL/access date/canonical, SHA256/byte framing and minimum quoted JSON-LD excerpt as **new edition-local raw evidence**, not canonical replacement.
- If unavailable, explicitly mark raw/second-level clock independently unverified; preserve audited day-level source facts. Do not assert model uploads or new standalone repository release at the article time.
- Separate checked facts from claims only repeated by publisher.

## 2. DGX Spark — Sol provisional editorial exclusion resolution (F02)

Review `candidate:2026-W40:071ac2e6d62319fd`, current Evidence, Materiality Matrix, r12 INSPECT rationale and first-party release/availability details.

Sol editorial choice for this run: **REJECT as independent reader-facing technical item**, not because it is outside W40, but because the W40-specific technical substance/priority is insufficient relative to P1–P7; distinguish announced hardware, 64GB SKU, Sync Cluster Assistant, $4,999 third-party offer and Oct 23 **future** availability. Do not conflate preorder with shipment.

Produce **review-only** `selection-preview-r13.json` from r12 by changing exactly DGX's disposition `INSPECT → REJECT` and its rationale only, plus version/summary and any required consistent bookkeeping. Preserve 28 SELECTED (20 PRIMARY / 8 SUPPORTING), 4 HOLD, resulting 3 REJECT, zero INSPECT. No Candidate ID or upstream changes. Check amended REJECT against **unmodified reviewed-main Core** validator and recompute preview/basis SHA/counts from actual bytes; if validator disagrees, STOP at Sol with validator errors, not an override.

This is still *not* authorized as full editorially sufficient Selection, because AstaBrief/AutoSynthData retain canonical HOLD.

## 3. Investigate legality of separate supplement under current Core (F01)

This is a **read-only study of authority and delivery topology** plus edition-local documentation, NOT authorization to create a release, bypass a Human Gate, produce a fake core-accepted appendix, or alter existing publications.

Start with reviewed-main:
- Production and Publication Profile, `config/survey-production-v2.json`;
- `scripts/survey_architecture_v2_base.py` (selected candidate/Architecture traceability);
- `scripts/survey_publication_v2.py` and the actual current publication/visual/source/Freeze/Release validators and workflows;
- existing TS-003 one-off exception records as historical precedent only: not generic permanent authorization.
- r11/r12 Sol decisions, Supplement manifest restrictions, and Issue #562.

Evaluate at least:
A. Independent separately Human-reviewed supplemental document and independent public artifact **without claiming** a Core-approved W40 main-PDF appendix or core Release identity.
B. A true bundled sidecar supplement **if and only if** it is explicitly admissible to present Release/Publication Profile (state exact required evidence and formal Human permissions).
C. If current contracts allow neither without an unauthorized exception, explicit no-available-ordinary-path result; separate Core maintenance path remains pending, but noncanonical drafting may continue.

For each option, provide exact support/contradiction file and contract clauses, document provenance/hashes/review/reader-accessibility model, compatibility risks, reader-facing completeness, explicit Human decision required, and honest process identity. Do not infer legal authority merely because GitHub permits file uploads or because an exception occurred once.

Never publish or add the notes into Core-selected `architecture-v2.json`, ordinary W40 PDF, Release bundle or first-party Source notes during this r13 unit. A provisional method or draft delivery plan is allowed, no actual release.

## 4. Advance noncanonical technical Architecture drafting (F08)

Stage `execution/architecture-staged-outline-r13.md` and bounded technical coverage matrices for 28 canonical selected plus clearly conditional P6a post-training and synthetic curriculum modules. Include source-to-claim, mechanism, metric / denominator / sample size, baseline and timestamp/version, license, external validity and reproducibility. Reserve substantial depth for ContextLM and Olmo-core 3 in P6a, AgentPerf, OpenTTS, RL Environments in P6b; do not collapse content to headlines or impose small page counts.

Include a **material coverage/cross-issue decision table**: 28 selected main issue, 2 provisional MATERIAL Core HOLD supplement subjects, DGX editorial REJECT, other W39 carry-over HOLD. Separate what would actually reach a reader today from what is only staged.

No canonical Architecture artifacts/Stage checkpoints in this unit.

## 5. Output and Sol terminal boundary

Produce `SOL_W40_R13_EDITORIAL_AND_SUPPLEMENT_FEASIBILITY_HANDOFF.md` summarizing:
- exact starting/final remote HEAD and Tree and reviewed-main readback, ancestry/non-force behavior;
- all changed paths (W40-local only), new r13 note/ledger/preview validation SHA and counts;
- explicit closure/remaining status of each F01–F09 from independent audit;
- independent evidence for each extra technical claim, uncertainty and reasons;
- publication supplement Path A/B/C legal-feasibility matrix and dependencies;
- current canonical State/Human Gate exact unmodified readback;
- next lawful editorial and canonical transition conditions.

Stop at `SOL_W40_R13_EDITORIAL_AND_PUBLICATION_FEASIBILITY_REVIEW_REQUIRED`, no formal Selection Acceptance / Stage transition, no architecture checkpoint, no Human Gate/Release actions. Subsequent Sol review determines whether/when 28-item Selection is editorially complete by a separately authorized supplement path.
