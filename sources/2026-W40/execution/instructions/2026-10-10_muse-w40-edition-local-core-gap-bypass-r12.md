# Muse W40 r12 — Edition-local Core-gap bypass / forward Selection preview

Status: `SOL_BOUNDED_EXECUTION_REQUEST / EDITION_LOCAL_ONLY / STOP_AT_SOL_SELECTION_REVIEW`
Date: 2026-10-10 JST

Repository: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W40-v2-work`
This instruction's exact starting HEAD/Tree MUST be given by Sol in the outer execution prompt after this instruction commit.
Reviewed `main`: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Historical r11 Sol verdict: `SOL_W40_SCOPE_PLAN_B_APPROVED / CORE_REENTRY_CONTRACT_GAP / SELECTION_ACCEPTANCE_HOLD`
Relevant Issue: https://github.com/eariver/japanese-generative-ai-survey/issues/562

## 0. Governing editorial decision and boundary

User directs that fixes for shared Core v2 defects be handled by an **independent Core maintenance task**, not in Weekly/Special production. Production must continue using **edition-local compatibility procedures**, where contract-compliant; no Core code/schema/config/workflow changes, no manual checkpoint or State rewrites, and no fabricated Human decision.

Sol still judges AstaBrief and AutoSynthData original Oct 2 issuer articles **in-window and technically MATERIAL** (the previously accepted `TIME_UNRESOLVED` rationale has been superseded by newer research). Plan B remains the desired eventual complete editorial scope. **Current frozen canonical authority, however, still classifies them HOLD**, and frozen Core will reject their promotion to SELECTED without valid upstream supersession. Do not silently classify these discoveries as ineligible or pretend they have been accepted.

The bounded temporary route is therefore:
1. Use unchanged canonical 37 Discovery / 37 Screening / 35 Evidence Cards / 35 Views / 37 Materiality rows / existing LIMITED Completeness to create a correct and Core-valid **28 SELECTED (20 PRIMARY + 8 SUPPORTING)** Selection preview.
2. Correct **only the selection-preview rationale** for the two HOLD assignments: explain that the canonical HOLD is temporarily retained due to lack of a lawful same-State authority amendment, despite independently verified in-window original hosted articles. Do not repeat the false "no precise original article timestamp exists" inference.
3. Author separate W40 edition-local, **non-canonical supplemental technical material** for the two events with independent original-source traceability and clear "NOT CORE-SELECTED / NOT PART OF FORMAL ARCHITECTURE" labels. This is a staging/review asset, not an accepted Core chapter or a Release PDF appendix.
4. Submit the valid provisional Selection and supplement to Sol. **Stop before any formal Selection Acceptance or Stage advancement in this r12 unit.** Only after independent Sol decision may a separately authorized run perform the standard canonical Selection transition and subsequent Architecture.
5. If legal Core constraints are tighter than expected, report precise validator results and stop without bypassing the constraints.

This route is a **temporary edition-level compatibility path**, not a Core #562 repair, and does not substitute the separate Core maintainer's work.

## 1. Exact Git safety and negative permissions

Before ANY repository write, verify read-only:
- remote existing W40 HEAD == exact outer Starting SHA, and HEAD tree == exact outer Starting Tree;
- remote `main` HEAD == `afdb3df3faa20af3bb5798be429bba8dbd2100b1` unless the outer execution prompt supplies a newer explicitly reviewed main;
- current production lifecycle `EVIDENCE_REVIEWED`, next_action `stage:selection`, Selection/Architecture checkpoints pending, both Human Gates pending with null provenance, no active Human decision;
- upstream canonical blobs/checkpoint identities unchanged relative to Sol r11.

Mismatch => ZERO WRITES, report expected/actual. Use **only existing branch**, normal commits and non-force push. No new branch, fallback/repair branch, reset, rebase, force/history rewrite. No direct State JSON edits, acceptance/checkpoint replacement, unauthorized Selection Acceptance, Architecture Gate, Publication Gate, exception gate, or GitHub Issue changes. Do not edit `.github/`, `config/`, `schemas/`, `scripts/`, `main`, shared Core docs, or other editions.

## 2. Selection preview — 28 existing Core-valid items

Read r10 `selection-preview-r10.json`, `candidate-matrix-r10-staging.json`, `candidate-id-crosswalk-r10.json`, `count-report-r10.json` and original accepted upstream as immutable source of truth; read r11 ledger, scope adjudication and counterfactual for corrections.

Rebuild a NEW, **review-only** `selection-preview-r12.json` and semantic dossier, with 35 assignments exactly and counts recomputed from the NEW actual JSON. Preserve the 28 preexisting SELECTED, roles and all other dispositions unless Sol explicitly authorizes a separate change. For AstaBrief and AutoSynthData keep `disposition: HOLD`, `architecture_usage: NONE`, no roles, and explain the publication-date finding, canonical limitation and pending edition-local supplement. No fictitious "out-of-window" verdict.

Do not use old r10 proposal's slug IDs as Core candidate IDs; derive/check the accepted 35 matrix, ID and SHAs using the reviewed-main Core. Run existing Core schema/validator **without modifications** against the preview and disclose any semantic conflict between source truth and canonical HOLD. No fake override, no manually recalculated SHA masquerading as acceptance.

## 3. Technical supplement, separate from canonical architecture

Create an edition-local `execution/editorial-supplement/r12/` collection with:
- independently sourced AstaBrief report-generation technical note (base, post-training SFT/DPO, Asta report pipeline and cited grounding, 51.1/178.5s publisher conditions, 2025-era baseline limitations; model/data licenses at artifact level; article timestamp vs older weight availability);
- AutoSynthData failure-driven synthetic-curriculum technical note (teacher/target, target/multiply, positive/negative verification and repair bounds, Hybrid/ITSM publisher-only SFT observations, EnterpriseOps Gym separated from missing standalone pipeline implementation);
- evidence-source ledger with exact official URLs, original hosted `datePublished`, source retrieval/access status, author/platform distinction and explicit unresolved claims;
- a manifest tying both technical notes to original canonical Evidence task IDs, Discovery IDs, r11 Sol decision, Core r10 matrix IDs, and publication restrictions.

This material is not approved as a main-magazine chapter. It must not appear as a PRIMARY/SUPPORTING candidate in the formal r12 preview or canonical Architecture; no claim that Core accepted it. No post-window contamination or automatic future-week event recategorization. Editorial status: `SUPPLEMENTARY_RESEARCH_READY_FOR_SOL_REVIEW / NON_CANONICAL`.

## 4. Preserve depth and onward capability

Build a **staged architecture outline only** for the frozen 28 selected items: P1 frontier largest, P2a/P2b substantive, P3 distinct mechanisms, P4 nonduplicated DevDay spine, P5 split threat/control families, P6a ContextLM and Olmo-core 3 method/systems depth, P6b AgentPerf/OpenTTS/RL-environments, P7 modalities/observability, P8 brief digest. Do not flatten methodology into shallow headlines or force a page cap. Do NOT formally create/accept Architecture in this unit.

Explain how the two supplemental notes can be either (a) incorporated after independent reviewed Core supersession or (b) presented as **clearly separate, human-reviewed publication supplement** later, only if its publication process is independently authorized. Never imply that an unselected candidate passed ordinary Architecture checks.

## 5. Terminal output

Provide `SOL_W40_SELECTION_COMPAT_REVIEW_HANDOFF-r12.md`, r12 Selection Core validation output, machine count audit, separate technical/source ledger, the staged Architecture plan, a change-only file list, exact Starting/Final HEAD+Tree, reviewed main HEAD, state/checkpoint/Human Gate readback, and risk/remaining Core discrepancy register.

Terminal status: `SOL_SELECTION_COMPAT_REVIEW_REQUIRED`. STOP. No advance to `SELECTION_COMPLETE` before subsequent independent Sol review. This contract does not ask the Core maintainer to change anything.
