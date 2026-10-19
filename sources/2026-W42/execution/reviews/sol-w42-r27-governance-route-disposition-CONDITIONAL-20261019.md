# J-GAS W42 r27 — Sol governance review: Route A CONDITIONAL, handler dispatch unresolved

Date: 2026-10-19 JST
Status: `SOL_EDITORIAL_GOVERNANCE_REVIEW / R27_PACKET_ACCEPTED_WITH_EXECUTION_QUALIFICATION / ROUTE_A_CONDITIONAL / HUMAN_DECISION_PENDING / CANONICAL_UNCHANGED`
Repository: `eariver/japanese-generative-ai-survey`
Reviewed fixed Worker r27 HEAD: `794892d5773c844d1150399438f4c0ee2299d204`
Reviewed root Tree: `42ff7140e7fe8d3f6b1993df3bc6fa552dab8683`
Reviewed main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / tree `801de813319f08777ab1581a5e8875fc1ac5df19`; Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
Prior Human Owner r26 local reset deviation is explicitly accepted ONCE, local effects UNVERIFIED and no future policy change.

## 1. Verified completed scope

Remote W42 r27 advanced exactly ONE fast-forward commit from `c150addf646951da85a7ac8c426264f8c03612d7`. Seven changed paths exclusively under W42 `execution/` (r27 governance proposal and session plus append-only index). No canonical Architecture, Core, Gate, State, Reader, Publication, Freeze, or Release mutation. Worker terminal is `SOL_W42_R27_HUMAN_PAGEPLAN_ROUTE_REVIEW_READY / NONCANONICAL`. Worker session says isolated clean worktree used without local reset; the report establishes no new adverse process exception. No repeat independent CONTENT/PRINT QA has been conducted by this editorial Sol.

## 2. Substantive page-plan conclusion ACCEPTED

Formal Human-approved Architecture r1: body subtotal 26.5 planning pages, target 28 and max 30, seven packages and 28 selections. Independently audited r26 diagnostic actual 21 pages = 1 cover + 17 physical body + 3 bibliography, 7 tables/27 rows/110 cells, 150 nonTABLE blocks, full 90 B keys/19 aliases/177 ledger, CONTENT PASS and PRINT PASS_WITH_LIMITATIONS. The 17 physical pages do NOT establish per-package fractional allocations, and there are aesthetic residual spaces (unmeasured) p03/p11/p13. No padding, content deletion or claim re-expansion warranted simply to hit r1's planned page target.

Frozen Code source corroborates: `survey_reader_fidelity_v2.validate_review_depth` returns for non-`LONGFORM_SPECIAL`, so W42 `WEEKLY_MAGAZINE` has no below-target hard failure there; `survey_architecture_v2_base` only validates positive target/max and max >= target; `survey_publication_v2` and `survey_reader_publication_v2` validate exact Candidate/review/PDF page-count and authority bindings, not a 28pp quota. Therefore r1 itself does not prohibit the actual 21-page plan. A Human edition-local acceptance can preserve r1 approval history; the 21pp diagnostic must STILL be rebuilt/bound as formal Reader/Candidate under normal validation and reviewed independently at publication time.

No lawful direct Architecture r2 from current DRAFT_COMPLETE: `survey_human_gate_v2._validate_gate_pending` requires current `ARCHITECTURE_ESTABLISHED` and pending architecture Gate; active approved r1 prohibits a fabricated second approval in review index. A proper cross-Gate reopen would need a genuine `RELEASE_CANDIDATE` Publication Preview REQUEST_CHANGES and would invalidate downstream canonical authority. Route B is overkill for page-count only.

## 3. NEW SOL EXECUTION QUALIFICATION — BOTH configured identities missing

Directly inspected reviewed-main frozen code:
- `config/survey-production-v2.json`: stage `DRAFT_COMPLETE` explicitly pins `handler = stage:reader-publication-validation`, `validator = validate:reader-publication` to transition `VALIDATED_DRAFT`.
- `scripts/survey_handlers_v2.py:register_handlers()`: registers `stage:semantic-publication-validation` and `validate:semantic-publication`, but **NEITHER of the configured `reader-publication` identities**.
- `scripts/survey_orchestrator_v2.py:execute_action` resolves `registry.get(spec["handler"])` and `registry.get(spec["validator"])`; fails closed if either is not callable (`registered handler unavailable` or `registered semantic validator unavailable`).
- `survey_orchestrator_v2.py` permits explicit `--handler-module` registration, so a separately supported adapter/registered module MIGHT exist, but none has been proven end-to-end compatible here. Do not assume a handler alias, silently change approved config, amend frozen Core or run without validator. The r27 Worker packet flagged only the validator in places; **both names are absent from the reviewed default registry**.

Thus Route A is **PAGE-TARGET / VALIDATOR-RULE COMPATIBLE**, but NOT YET `NORMAL_STAGE_DISPATCH_PROVEN`. A conditional Human authorization for Route A should require an additional bounded read-only adapter/operator routing preflight (or stop for Core maintenance authority if unavailable) before any canonical stage write. If unsupported, terminal explicit `HANDLER_ROUTING_BLOCKED` rather than fabricate a stage action/attestation. This new observation does not invalidate independent r26 Content/Print PASS_WITH_LIMITATIONS.

## 4. Human choice and permission boundary

Sol recommends **Route A, conditionally**: accept W42's measured issue ~21pp under r1 advisory target 28/max30 and known layout residuals; retain r1 exact bytes/approval; authorize bounded noncanonical handler/validator routing feasibility proof before any production transition. Only if a properly supported frozen-Core-compatible route is demonstrated may the Worker seek explicit, separately contracted authorization to create canonical Reader/Validation/Candidate. The user's previously accepted r26 Deviation does NOT authorize any of this new work. Alternative: Route B cross-Gate reopen, or stop for Core maintenance. Human decision must be requested and recorded as distinct edition-local governance evidence. There is NO formal human page-plan approval yet.

Human decision addendum: `sources/2026-W42/execution/governance/pageplan-r27/sol-human-route-decision-addendum-CONDITIONAL.PROPOSED.md`.
