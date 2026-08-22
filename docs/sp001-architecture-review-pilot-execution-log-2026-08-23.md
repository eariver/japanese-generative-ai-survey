# SP-001 Architecture Review pilot execution log — 2026-08-23

This document records work actually performed while compiling **SP-001** on `special/SP001-v2-work` up to the first Human Gate. It is an execution log, not a replacement for the authoritative Core v2 artifacts under `sources/SP001/`.

## Goal and authority

- Issue: `SP001`
- Research Profile: `THEMATIC`
- Publication Profile: `LONGFORM_SPECIAL`
- Work branch: `special/SP001-v2-work`
- Target Human Gate: `ARCHITECTURE_REVIEW`
- Production Profile / Production State under `sources/SP001/` were treated as the authoritative edition state.
- Work was continued autonomously until either an Exception Gate became necessary or the Architecture Review Human Gate was reached.

No Exception Gate was required.

## Pipeline stages completed

### Discovery and Screening

The accepted Discovery set contains **24 records**. Screening preserved every record with an explicit disposition; no candidate was silently dropped.

The later Architecture Review Summary records the Discovery origin counts as:

- BASE: 5
- SUCCESSOR_EXPANSION: 12
- GAP_FILL: 3
- PARALLEL_EXPANSION: 2
- COMPETING_EXPANSION: 1
- BRIDGE_EXPANSION: 1

Research expansion reached pass 4. Screening totals were:

- KEEP: 18
- MAYBE: 2
- INSPECT: 4

The four INSPECT records were deliberately carried into Evidence rather than promoted or discarded prematurely.

### Evidence, Edition Views, Materiality, and Completeness

The final successful interactive Evidence run was GitHub Actions run `32585938749`.

Accepted Evidence totals:

- VERIFIED: 14
- PARTIAL: 6
- NEEDS_MORE: 4
- Total: 24

Materiality totals:

- MATERIAL: 18
- CONTEXT: 2
- HOLD: 4

The four HOLD records are:

- `SP001-D004`: early Kimi 2023 launch/context lead; secondary-source qualified
- `SP001-D022`: X runtime-adoption signal
- `SP001-D023`: X license-friction signal
- `SP001-D024`: X enterprise-origin-policy signal

The X records were not allowed to support runtime performance/prevalence, legal conclusions, or generalized enterprise-policy prevalence.

Profile Completeness closed as **LIMITED**, not READY and not INCOMPLETE. Thematic closure recorded:

- expansion passes: 4
- final-pass new sources: 3
- final-pass new material obligations: 4
- final-pass new material obligations open: 0
- targeted gap fill: completed
- open material obligations: 0

Residual limitations preserved into closure:

1. Kimi's October 2023 launch/context-window chronology remains secondary-source qualified until a stronger first-party archival source is added.
2. X runtime-adoption, license-friction, and enterprise-origin-policy observations remain HOLD and cannot support performance, legal, or prevalence claims.
3. Cross-family benchmark ranking is intentionally excluded where model versions, benchmark conditions, or evaluation methods are incompatible.

Evidence/Materiality/Completeness stage adoption completed successfully in run `32586075487`, advancing Production State to `EVIDENCE_REVIEWED`.

### Candidate Selection

A deterministic Candidate Matrix was derived from the accepted upstream artifacts. All **24 candidates** received exactly one Selection assignment:

- SELECTED: 20
- HOLD: 4

The same four weak/uncorroborated records (`D004`, `D022`, `D023`, `D024`) remained HOLD with `architecture_usage=NONE`.

The selected structure preserves:

- GLM, Qwen, DeepSeek, and Kimi as distinct central lineages
- MiniMax M2.7 as a material competing frontier branch rather than a fifth co-equal central family
- Yi-1.5 and Baichuan-M3 as supporting bridges/context
- the exact Kimi K3 License as a primary cross-cutting Open Weight/licensing boundary

The combined Selection/Architecture generation run `32586822727` passed generation, Selection-stage revalidation, proposed Architecture validation, Architecture Review readiness, and artifact persistence.

Selection stage adoption run `32586977713` passed deterministic stage validation and advanced Production State to `SELECTION_COMPLETE`.

### Proposed Issue Architecture

The proposed Architecture contains seven draft packages:

1. **前史と分岐点：大規模モデルから主要4系統へ**
2. **GLM：公開・ローカル展開からARCと長文脈servingへ**
3. **Qwen：family/platform拡張からhybrid reasoningとagentic codingへ**
4. **DeepSeek：MLA/MoE効率化からreasoning RLとagentic servingへ**
5. **Kimi：long-context RLからopen agentic MoE・native multimodalへ**
6. **並行する競争線：MiniMax、Yi、Baichuanが示す別経路**
7. **Open Weightは一枚岩ではない：distribution、local deployment、license境界**

Page plan:

- target: 34 pages
- maximum: 42 pages

The architecture runner automatically propagated every selected candidate's Evidence `remaining_boundaries` into its package boundaries, so source limitations are not lost during editorial placement.

The generated `architecture-review-summary-v2.json` reports `READY_FOR_ARCHITECTURE_REVIEW` with no readiness errors.

The generated review-attention surface contains **14 items**, with no truncation:

- MATERIALITY:HOLD: 4
- SCREENING:INSPECT: 4
- SCREENING:MAYBE: 2
- SELECTION:HOLD: 4

Architecture stage adoption run `32587091257` passed deterministic stage validation, state transition, resumable-State validation, and persistence.

## Core v2 defects / missing execution surfaces found during the pilot

SP-001 was used as a real production pilot rather than bypassing failed contracts. Problems discovered in generic Core v2 behavior were repaired generically and validated before continuing the edition.

### Historical accepted Screening State basis

Downstream Evidence initially revalidated an accepted Screening package against the **current** Production State SHA rather than allowing the immutable package to retain the historical State SHA from its creation boundary. The accepted package was already content-addressed, so this was a validator error rather than SP-001 data drift.

Repair: PR `#337`.

The repair keeps strict State-SHA validation at Screening creation/acceptance and permits the historical value only for an already accepted, content-addressed package during downstream revalidation.

### Canonical Discovery provenance lost in Completeness derivation

The interactive Evidence runner used compact Discovery acceptance summaries when deriving named-obligation traceability and thematic expansion counters. Those summaries omit the full `provenance` object, producing empty/incorrect closure traceability despite the canonical hash-pinned Discovery JSONL containing the data.

Repair: PR `#340`.

The agent-first adapter now rehydrates the in-memory view from the exact accepted Discovery JSONL after verifying its hash and record count.

### Thematic residual limitations not guaranteed to survive into closure

The Completeness validator correctly requires every residual limitation to remain present in a `LIMITED` Thematic closure, but the interactive runner previously trusted a separately authored closure limitation list and could fail late if one residual limitation was missing.

Repair: PR `#342`.

The agent-first path now deterministically unions residual limitations into closure limitations before authoritative validation.

### Historical accepted Evidence State basis

Selection/Architecture revalidates Evidence after Production State has advanced beyond the Evidence creation boundary. The same historical-State issue found for Screening therefore also applied to accepted Evidence packages.

Repair: PR `#346`.

Only exact `state_sha256` drift is tolerated, only for an accepted content-addressed Evidence package; all other Evidence basis, prompt, task, schema, Screening, Profile, and current-State checks remain strict.

### Missing Core v2 interactive Selection/Architecture execution surface

The repository contained a legacy Special workflow based on `pipeline-state.json`, but SP-001 uses the authoritative Core v2 `production-state.json`. Reusing the legacy path would have violated the current authority model.

Repair/addition: PR `#351`.

Added:

- `scripts/run_selection_architecture_v2_interactive.py`
- `.github/workflows/survey-production-v2-interactive-selection-architecture.yml`
- regression tests for exact Matrix coverage and one-Discovery-per-candidate mapping

The runner derives Candidate Matrix/candidate IDs canonically, resolves semantic decisions by Discovery ID, validates Candidate Selection and PROPOSED Architecture using existing Core v2 validators, generates Review Summary/Attention, archives the exact interactive input, and never records Human approval.

## Important SP-001 execution PRs

Generic Core v2 repairs were merged to `main` and then integrated into the SP-001 work branch before use. Significant SP-001 execution/integration PRs during this continuation included:

- `#335` — execute accepted SP-001 Evidence / Views / Materiality / Completeness
- `#341` — integrate canonical Discovery provenance repair
- `#344` — integrate Thematic closure-preservation repair
- `#345` — synchronize Evidence trigger with reviewed repairs
- `#347` — adopt Evidence stage
- `#349` — integrate historical Evidence basis repair
- `#352` — integrate Core v2 interactive Selection/Architecture surface
- `#354` — execute Candidate Selection and proposed Architecture
- `#355` — adopt Selection stage
- `#357` — adopt Architecture and enter Architecture Review Human Gate

## Evidence execution retries

The failed Evidence runs were retained as diagnostic events rather than hidden:

- `32585076391`: exposed the historical accepted-Screening State-SHA validator defect
- `32585412717`: after that repair, exposed canonical Discovery provenance loss / Thematic closure contract issues
- `32585938749`: successful Evidence/Views/Materiality/Completeness execution after generic repairs

The semantic Evidence input was not weakened to make these runs pass; generic validation/execution defects were repaired instead.

## Final state reached

After PR `#357` and Architecture stage adoption, canonical Production State is:

- lifecycle state: `ARCHITECTURE_ESTABLISHED`
- target gate: `ARCHITECTURE_REVIEW`
- next action: `ARCHITECTURE_REVIEW`
- terminal reason: `HUMAN_GATE_REACHED`
- architecture machine checkpoint: `passed`
- architecture human gate: `pending`
- exception gate: `inactive`

The Issue Architecture remains **PROPOSED** and its `human_review` fields remain null. No Architecture approval record was created and no drafting was started.

This is the intentional stopping point for autonomous compilation.
