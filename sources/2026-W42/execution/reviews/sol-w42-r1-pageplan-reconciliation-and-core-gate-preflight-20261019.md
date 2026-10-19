# J-GAS W42 — Sol r1 page-plan reconciliation, Core gate path feasibility

Date: 2026-10-19 JST
Status: `SOL_EDITORIAL_GOVERNANCE_ANALYSIS / R26_PROCESS_DEVIATION_HUMAN_ACCEPTED / PAGEPLAN_ROUTE_REVIEW_REQUIRED / NONCANONICAL`
Repository: `eariver/japanese-generative-ai-survey`
Predecision W42 HEAD: `9a43d3c9a8995ab2de2ce009e0677a980405d093`, Tree `78468299a842e0c79d4637a61309ec41ee212f56`
Audited r26 diagnostic HEAD: `2981b30b783e858737fc69cf439afbbfe19d5105`, Tree `617a52200d82575b91a3cd345037daad2e8fbbbd`

## 1. Bound page-plan facts; scope / quality

Human-approved Architecture r1 source: `sources/2026-W42/architecture-v2.json` Git blob `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`; `page_plan.target_pages=28`, `max_pages=30`, notes define package body allocations **P1 4.0 / P2 2.5 / P3 5.0 / P4 4.0 / P5 3.0 / P6 4.5 / P7 3.5**, sum **26.5 body**. The original r1 approval record and review index are ACTIVE approved, not a pending Architecture Gate. The old page-plan is a design target, with instructions not to pad or silently cut explanatory depth.

Independently audited r26 NONCANONICAL diagnostic: PDF SHA256 `c76f4a6e975039ec813e17909bd62768303c48c2e7018588c07e6bab7fe780c0`; physical **21 pages = cover1 (p01) + body17 (p02–18) + bibliography3 (p19–21)**. Seven chapters P1–P7, 28 selected items, seven full-width tables (27 rows,110 cells), 150 non-table Reader blocks retained; 90 bibliography keys,19 aliases,177 ledger lines. Independent `CONTENT=PASS`, `PRINT=PASS_WITH_LIMITATIONS`; p03/p11/p13 whitespace is an acceptable-looking editorial residual, occupied area UNMEASURED. Real body uses shared physical pages between chapters; precise per-package page-equivalent consumption has NOT been measured. **17 physical body pages is not a measured seven-way fractional allocation.** Do not assert new P1–P7 fractional quotas without a disclosed allocation model and evidence.

Prior Human Option B expressed preference for a shorter, content-complete issue, about 17 planned body pages with unchanged 7 chapters/28 selections, not formal Architecture r2 approval. Sol tentative overall target 21, max 23 remains PROPOSED. Reader r18 and physical r26 full source equality were independently confirmed. No padding, deleting coverage, or re-research is warranted to force 28pp.

## 2. Core v2 gate limitation directly observed at reviewed main

Frozen `scripts/survey_human_gate_v2.py`:
- `_validate_gate_pending` requires `state.lifecycle_state == GATE_STATES[gate]` AND `state.human_gates[gate] == pending`.
- `request_architecture_revision` delegates to `request_changes(..., gate=ARCHITECTURE_REVIEW)`, which invokes the above pending-gate check.
- `record_architecture_approval` likewise invokes the pending-gate check.
- `_validate_review_index_semantics` rejects new reviews after an ACTIVE Architecture `APPROVED` unless a valid later Publication Preview `REQUEST_CHANGES` with upstream regeneration boundary has formally reopened Architecture.
- A Publication Preview `REQUEST_CHANGES` requires that Publication Preview itself be the CURRENT pending Gate; W42 remains `DRAFT_COMPLETE`, Architecture already approved and Publication Preview still pending but **NOT at** `PUBLICATION_PREVIEW` lifecycle.

Accordingly **DO NOT directly overwrite `architecture-v2.json`, append an `architecture-r2` review record, hand-write Gate receipts, or run `request-architecture-revision` from DRAFT_COMPLETE.** The frozen Core cannot simply materialize a new formal Architecture r2 approval at the current lifecycle. This is a governance routing/validation issue, NOT authorization to modify shared Core.

## 3. Bounded alternative routes for next deliberation (NOT decided here)

**Route A — preserve active r1 Gate, add Human editorial page-count acceptance for the actual diagnostic plan:** investigate whether current Core publication validators treat r1 `target_pages=28` as an advisory target and `max_pages=30` only as a ceiling, permitting a content-complete 21pp formal Reader/Publication Candidate without changing previously approved Architecture. Human would explicitly acknowledge the measured page-plan deviation as a distinct edition-local decision. Do not assume this is Core-compliant until validator/quality-contract checks have been executed read-only. If legal, this minimizes invalidation and preserves original research authority.

**Route B — formal r2 Gate revision through a Core-supported lifecycle reopening:** identify if a safe legitimate route exists at an actual pending downstream Gate to issue Human `REQUEST_CHANGES` with Architecture-regeneration boundary, and precisely which canonical checkpoints, approved Gate records, Draft/Reader and evidence would be superseded. No artificial/fake Publication Gate, and no write solely to manufacture eligibility. This is potentially much more disruptive; an explicit subsequent Human decision is needed even if possible.

**Route C — STOP / exception request:** if neither route can be proven allowed by frozen Core, do not silently weaken schema/Gates or treat PROPOSED JSON as approved; document blocker and request Human governance direction.

Do not conflate Human's accepted r26 local-reset Deviation with authorization for Route A/B. No formal r2 choice has been taken. Do not invent package allocations or metadata solely to hit a 21pp target.

## 4. Immediate next unit

One bounded Muse r27 **read-only proof and edition-local PROPOSED review packet**, contract:
`sources/2026-W42/execution/instructions/2026-10-19_muse-w42-r27-pageplan-governance-preflight-review-packet.md`.
It must trace actual Core validators and approved r1 Gate chain, compare possible Route A/B under exact immutable inputs, generate reviewable route and optional schema-compatible page-plan proposal outside canonical, then stop for **separate Human decision**. No changes to frozen Core, formal Architecture, Reader, Production State, Human Gates, or Publication Candidate.

Current terminal: `SOL_W42_PAGEPLAN_GOVERNANCE_PREFLIGHT_READY / NO_CANONICAL_ADVANCE`.
