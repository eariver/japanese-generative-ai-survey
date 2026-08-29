# 2026-W33 Sol Selection semantic review r1

Status: `ACCEPT / SELECTION_SEMANTICS_FROZEN / APPROVED_FOR_CORE_ADVANCEMENT`

Issue: `2026-W33`
Branch: `weekly/2026-W33-v2-work`
Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
Luna exact starting SHA: `63ebd6ce57c7d8867a45e5cadd4f0dd37d8b772a`
Luna canonical final SHA reviewed: `12d27ecacf8330e39338eb17eeecf85a9aa8c7d0`
Luna candidate commit: `d1dbfd1d58d61d11acf863e3845d7828adf9301a`
Luna session: `sources/2026-W33/execution/sessions/w33-luna-selection-20260830-r1.md`

## Decision

Sol accepts the exact W33 Candidate Matrix and Candidate Selection produced by Luna and freezes them as the Selection semantic authority for the next deterministic Core transition.

No Selection semantic repair, upstream Evidence repair, new source collection, or Exception Gate is required before advancing from `EVIDENCE_REVIEWED` to `SELECTION_COMPLETE`.

The next worker task is deterministic Selection advancement only. Architecture reasoning must not begin until that transition is verified by Sol.

## Git and task-boundary verification

The reviewed worker range is exactly:

`63ebd6ce57c7d8867a45e5cadd4f0dd37d8b772a -> 12d27ecacf8330e39338eb17eeecf85a9aa8c7d0`

GitHub comparison shows:

- ahead: 2
- behind: 0
- changed paths: exactly 3

The only changed paths are:

1. `sources/2026-W33/candidate-matrix-v2.json`
2. `sources/2026-W33/candidate-selection-v2.json`
3. `sources/2026-W33/execution/sessions/w33-luna-selection-20260830-r1.md`

The candidate commit changed only Matrix and Selection. The final bookkeeping commit changed only the Luna session record.

No Production State, upstream Discovery/Screening/Evidence/View/Materiality/Completeness authority, shared Core, Architecture, Draft, publication, or Human Gate artifact changed.

The branch HEAD at review time is the reported canonical final SHA `12d27ecacf8330e39338eb17eeecf85a9aa8c7d0`.

## Production State verification

Production State remains unchanged through the worker task:

- path: `sources/2026-W33/production-state.json`
- SHA-256: `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`
- lifecycle: `EVIDENCE_REVIEWED`
- next action: `stage:selection`
- Evidence: passed
- Materiality: passed
- Completeness: passed
- Selection: pending
- Architecture: pending
- Architecture Review: pending
- terminal reason: null

This is the correct pre-advancement state.

## Candidate Matrix verification

Accepted Matrix:

`sources/2026-W33/candidate-matrix-v2.json`

Luna-reported SHA-256:

`1b660291564bda5f30debd86bb6911eb53edf06e8f735710f84652d972c4d198`

The Matrix binds the already frozen authorities exactly:

- Production Profile: `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`
- Profile Completeness: `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`
- Materiality Ledger: `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`
- Evidence acceptance: `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`
- Edition View acceptance: `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`

Structural result:

- candidates: 37
- materiality: MATERIAL 25 / CONTEXT 6 / HOLD 6
- Evidence: VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0

Luna derived the Matrix through the r2-required `current_stage_basis_override()` route and independently re-derived exact equality at both the starting implementation identity and canonical candidate commit. This is consistent with the current agent-first Core design for accepted historical Screening/Evidence packages.

Sol finds no Matrix drift or semantic mutation.

## Candidate Selection verification

Accepted Selection:

`sources/2026-W33/candidate-selection-v2.json`

Luna-reported SHA-256:

`9c6997d2ed3921a847db5e001ec9377189bb25d5475454593f23016308557005`

Selection version:

`w33-selection-luna-r1`

Distribution:

- SELECTED: 28
  - PRIMARY: 21
  - SUPPORTING: 7
- HOLD: 6
- REJECT: 3
- INSPECT: 0

Every Matrix candidate is assigned exactly once. Core Selection validation passed. All selected candidates are eligible under frozen Materiality/Evidence status. All non-selected candidates use `architecture_usage=NONE` and null roles.

## Semantic review findings

### 1. Fixed HOLD set is correct

The six current unresolved candidates remain HOLD, as required by the Sol rubric:

- RepoWise agent-tool efficiency re-check
- MiniMax news index
- GitHub Copilot cloud-agent W33 re-check
- GPT-5.6 W33 update re-check
- Kimi K3 GitHub Copilot availability re-check
- Claude Opus 4.1 API retirement re-check

These remain unresolved obligations rather than being converted into artificial REJECT outcomes. This preserves the accepted Profile Completeness limitation and carry-over provenance.

### 2. Single-home and duplicate handling is correct

The proposal does not inflate dedicated events and index/channel records into duplicate PRIMARY stories.

Accepted examples:

- GLM-5.3 dedicated record is PRIMARY; the post-cutoff Z.ai index entry is REJECT.
- Gemini 3.7 Flash dedicated record is PRIMARY; its API chronology index is SUPPORTING chronology.
- Grok 4.6 dedicated record is PRIMARY; its news-index record is SUPPORTING chronology.
- GPT-5.6-Cyber / Daybreak Red is the PRIMARY cyber-access development; Bedrock and partner/governance records are SUPPORTING channel/context material.
- FlashInfer is SUPPORTING serving infrastructure rather than a second main serving story.
- X community evidence is SUPPORTING context only and is explicitly excluded from technical authority.

This satisfies the single-home requirement without silently discarding useful context.

### 3. REJECT decisions are acceptable

The three REJECT decisions are semantically justified:

- Z.ai post-cutoff index duplicate: no distinct W33 technical event.
- Transformers v5.15.0: valid and material, but lower marginal editorial value after stronger runtime/model selections; Selection may reject a MATERIAL item on marginal-value grounds.
- Open Evaluation Agent: unresolved novelty separation from earlier ACL work makes independent placement more likely to double-count than add a clean W33 contribution.

No rejected candidate is being rejected because of a schema shortcut or unsupported factual assertion.

### 4. PARTIAL candidates preserve their boundaries

The Selection rationales do not erase accepted Evidence limitations. In particular:

- GPT-5.6 Sol Ultrafast remains a preview/service-tier development with preview-versus-GA and performance-measurement boundaries.
- GLM-5.3 remains bounded to the captured coding/cyber framing; detailed benchmark/cyber/local-weight timing claims are not promoted.
- GPT-5.6-Cyber / Daybreak remains an authorized security-testing/access development, not proof of general model/API availability.
- VoiceDesigner remains a research signal with baseline/evaluation/novelty questions preserved.
- vendor/project/author claims remain attributed downstream.

Selection does not upgrade PARTIAL Evidence into independent verification.

### 5. The selected count is high but not itself a defect

`SELECTED 28` and `PRIMARY 21` are deliberately treated as an Architecture input pool, not a commitment to 28 standalone articles or 21 standalone sections.

Current Core permits multiple PRIMARY candidates inside one Architecture package. Therefore count alone is not grounds for Selection repair.

However this creates a binding Architecture-stage constraint:

- Architecture must consolidate papers, serving/runtime releases, model/channel records, and related agent-evaluation work into a small set of coherent packages.
- A PRIMARY candidate denotes factual centrality inside a package, not an entitlement to a standalone page.
- SUPPORTING records must remain subordinate to their selected home or issue-level synthesis.
- Architecture must not mechanically turn the 28 selected assignments into 28 article slots.

This constraint is part of the Sol handoff to the later Architecture policy stage.

### 6. Breadth is acceptable without quota balancing

The selected pool retains non-redundant material across:

- model/API availability and control surfaces;
- coding/agents/evaluation/security;
- serving/runtime/local inference;
- multimodal/media/voice tooling and research;
- systems/reliability research.

The mix is broad because the accepted W33 authority is broad, not because the worker filled a category quota.

## Deterministic validation accepted from Luna

The Luna session records PASS for:

- Matrix schema validation;
- fresh deterministic Matrix equality;
- Selection schema validation;
- `selection-check`;
- exact 37-assignment coverage;
- eligibility/HOLD/context-support checks;
- current-stage contract validation for `EVIDENCE_REVIEWED -> SELECTION_COMPLETE`;
- `git diff --check`;
- Production State byte identity.

Sol's repository review found no contradiction with those deterministic results.

## Frozen Selection semantic package

The exact next-stage semantic authority is:

1. Candidate Matrix
   - path: `sources/2026-W33/candidate-matrix-v2.json`
   - SHA-256: `1b660291564bda5f30debd86bb6911eb53edf06e8f735710f84652d972c4d198`
2. Candidate Selection
   - path: `sources/2026-W33/candidate-selection-v2.json`
   - SHA-256: `9c6997d2ed3921a847db5e001ec9377189bb25d5475454593f23016308557005`

They are frozen byte-for-byte for the next deterministic Core transition.

## Authorized next transition

Sol authorizes exactly:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

Current-stage artifacts:

- `candidate-matrix` = `sources/2026-W33/candidate-matrix-v2.json`
- `candidate-selection` = `sources/2026-W33/candidate-selection-v2.json`

Expected post-transition control:

- lifecycle: `SELECTION_COMPLETE`
- next action: `stage:architecture`
- Selection checkpoint: passed
- Architecture checkpoint: pending
- Architecture Review: pending
- terminal reason: null

No Architecture artifact or Architecture reasoning is authorized inside this advancement task.

## Stop condition

After deterministic Selection advancement, stop for Sol.

Expected worker status:

`SELECTION_COMPLETE_READY_FOR_SOL_ARCHITECTURE_POLICY`
