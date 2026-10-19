# J-GAS W42 Muse r27 — Architecture r1 page-plan governance-route preflight + Human review packet

Date: 2026-10-19 JST
Status: `SOL_EXECUTION_AUTHORITY / HUMAN_R26_DEVIATION_ACCEPTED_ONCE / READ_ONLY_CANONICAL / EDITION_LOCAL_PROPOSALS_ONLY / STOP_AT_HUMAN_ROUTE_REVIEW`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W42-v2-work`

## 0. Exact guard, immutable scope

Sol dispatch supplies Exact Starting Remote HEAD and Expected Root Tree identifying the commit containing THIS contract. FIRST verify both full SHAs, reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / tree `801de813319f08777ab1581a5e8875fc1ac5df19`, frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`, r26 audited HEAD `2981b30b783e858737fc69cf439afbbfe19d5105` / tree `617a52200d82575b91a3cd345037daad2e8fbbbd`. Any mismatch => ZERO WRITES STOP with actual SHA. Recheck remote lease before push; existing branch normal FF commit, non-force only. No new/fallback/review branches; no reset/rebase/force, no overwriting local uncommitted changes. A stale local checkout is a STOP or separately created clean checkout from a verified remote (never hard reset the existing workspace).

Protected BYTE-EXACT: shared Core; canonical W42 Discovery/Screening/Evidence/Views/Materiality/Completeness/Selection/Architecture `architecture-v2.json`, r1 approved Gate/review index/snapshots, Draft, Reader and W42 `production-state.json`, existing stage artifacts and checkpoints; r18 Reader blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`; all execution evidence r11–r26 and Human r26 Deviation acceptance. No delete/invalidate/replay/canonization/Publication/Freeze/Release/Human Gate action; NO newly created formal Gate event. New writes ONLY under `sources/2026-W42/execution/governance/pageplan-r27/`, one NEW session `execution/sessions/muse-w42-r27-20261019.md`, and truthful append-only `execution/index.md`.

## 1. Mandatory source read and evidence

Read these before any conclusion:
1. `execution/governance/human-w42-r26-local-reset-deviation-acceptance-20261019.md`, `execution/reviews/sol-w42-r1-pageplan-reconciliation-and-core-gate-preflight-20261019.md`; r26 independent PASS_WITH_LIMITATIONS and Worker session.
2. r1 exact Architecture `architecture-v2.json`, Human approval basis `execution/human-architecture-approval-basis-r1.md`, `gates/architecture-approval.json`, `gates/reviews/architecture-r1.json`, `gates/review-index.json`, `production-state.json`, review summary and attention, profile/quality contracts.
3. r26 fixed `execution/diagnostic-r26/build-manifest-r26.json`, diagnostic 21-page PDF/TeX, `execution/typeset-repair-r26/option-b-pageplan-r26.PROPOSED.md`, r18 Reader; preserve source/print audit result.
4. Frozen Core v2 `scripts/survey_human_gate_v2.py`, `scripts/survey_agent_control_v2.py`, `scripts/survey_publication_*v2.py` and relevant config/schema validators (find exact paths in repo; do NOT guess commands or edit implementation).

## 2. Objective: determine lawful governance reconciliation BEFORE asking Human to approve a route

Core check A: Is the approved r1 `page_plan.target_pages=28` a HARD lower bound or planning target? Is `max_pages=30` upper cap? Do relevant Reader/Publication validators accept 21 honest physical pages with unchanged r1 Architecture if Human separately records edition-local deviation? Show exact source function/contract key and, where possible, a NONMUTATING dry-run against copies of current files; no stage transition, no candidate authorization or fabricated PASS. Separately identify whether 17 physical body pages ≠ 17 planned body budget matters to validators or human promises. If route A is compliant, specify exactly what Human decision/edition-local record, if any, is required; how to move through normal `DRAFT_COMPLETE -> validation -> Publication Preview pending` without touching r1 Gate.

Core check B: Show proof `request-architecture-revision`/approval from current `DRAFT_COMPLETE` fails pending-Gate check, and review-index forbids a second active approval. Determine whether and when the documented Publication Preview `REQUEST_CHANGES` cross-Gate Architecture reopen can validly apply, what it would invalidate (Draft, checkpoints, canonical plans, Reader, current r1 approval provenance), and what human choices would be necessary; do NOT invoke this route, fake a Publication candidate or mutate Gate. A pending publication flag in state is NOT proof publication Gate is currently actionable.

Route C: if neither can be validated, return precise governance blocker and potential edition-local noncanonical alternative or escalate to Human rather than mutate Core.

**This is not another r28 PDF iteration**: do not re-research, reword Reader, pad/shorten body, alter 7 chapters/28 selections/7 full tables/90 B keys. Existing independent content and physical quality PASS_WITH_LIMITATIONS stands.

## 3. Prepare a truthful, reviewable Human page-plan packet

Document:
- exact r1 body allocations P1=4.0,P2=2.5,P3=5.0,P4=4.0,P5=3.0,P6=4.5,P7=3.5, subtotal26.5, overall target28/max30;
- actual r26 21 physical = cover1+body17+bib3, no invented per-P physical fractional allocations, since chapter boundaries share pages; indicate page spans by chapter and table locations.
- independent r26 7 tables/27 rows/110 cells/150 nonTABLE + all citations/90 bib/19 alias/177 ledger, no content lost; documented p03/p11/p13 whitespace (area UNMEASURED), avoiding fake density gain.
- Option B editorial preference and Sol tentative issue21/max23, not a Human architecture approval.
- if a **PROPOSED** Architecture page-plan candidate is prepared, maintain all r1 packages/candidates/goals/claims/evidence/basis byte-compatible except explicitly proposed page allocation/notes/targets and record exact JSON-patch/diff. Do not label candidate as Gate approved. Any proposed per-package fraction must be tagged planning estimate derived from a documented budget rule, NOT independently measured actual footprint; if evidence inadequate, omit package fractions instead of claiming measurements.

Produce a clear Route A/B/C recommendation with implications for canonical authority, edition evidence, approval provenance, data loss risk, and earliest valid Core-backed next operation. Route A is editorially preferable IF validated; do NOT pick it by convenience before Core checks.

## 4. Evidence and terminal

Write versioned noncanonical deliverables ONLY:
- `execution/governance/pageplan-r27/core-v2-architecture-gate-route-compatibility-r27.md`: actual functions, preconditions, dry-run evidence and no invalid writes;
- `execution/governance/pageplan-r27/r1-versus-r26-physical-page-budget-and-coverage-r27.md`: architectural and published facts with scope of measurement;
- `execution/governance/pageplan-r27/human-pageplan-route-decision-packet-r27.PROPOSED.md`: route comparison/recommendation, exact human questions, explicit fact/unknown separation;
- optionally `execution/governance/pageplan-r27/architecture-r2-pageplan.PROPOSED.json` and corresponding `*.diff` ONLY if faithful schema/authority feasibility, not a canonical write;
- `execution/sessions/muse-w42-r27-20261019.md`, truthful index append.
No new canonical architecture or approval; no fake Gate. Pass only if proof-backed Route A/B/C human packet:
`SOL_W42_R27_HUMAN_PAGEPLAN_ROUTE_REVIEW_READY / NONCANONICAL`.
If Core preflight cannot establish a compliant path or needed materials are inaccessible, terminal
`R27_PAGEPLAN_GOVERNANCE_ROUTE_BLOCKED` with precise missing evidence, no further write.

Normal non-force FF push and final SHA/tree/readback. Sol will present to Human Owner and await a SEPARATE decision before any canonical/Publication operation. Independent CONTENT/PRINT QA will NOT be repeated in this unit.
