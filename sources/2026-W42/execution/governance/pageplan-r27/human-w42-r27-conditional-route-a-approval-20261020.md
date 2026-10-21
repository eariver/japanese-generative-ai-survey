# J-GAS W42 — Human Owner conditional approval of Route A

Date: **2026-10-20 JST** (conversation date; exact clock-second / permalink not available, none invented)
Status: `HUMAN_OWNER_DECISION / ROUTE_A_CONDITIONALLY_APPROVED / R1_ARCHITECTURE_PRESERVED / R28_HANDLER_FEASIBILITY_ONLY / NO_GATE_ACTION`
Repository: `eariver/japanese-generative-ai-survey`
Human-presented Sol governance review HEAD: `d3632e046d2b3bc859f327085209a5a8409e67d4`
Human-presented root Tree: `20356b04224b163ceffb2d7c1ec48ef2e420c338`
Decision context:
- `sources/2026-W42/execution/reviews/sol-w42-r27-governance-route-disposition-CONDITIONAL-20261019.md`
- `sources/2026-W42/execution/governance/pageplan-r27/sol-human-route-decision-addendum-CONDITIONAL.PROPOSED.md`
- `sources/2026-W42/execution/governance/pageplan-r27/human-pageplan-route-decision-packet-r27.PROPOSED.md`

## 1. Exact Human decision and scope

Immediately after Sol presented the question **「この条件で経路Aを承認しますか？」** including the explicit precondition that handler/validator routing be proven in a read-only/noncanonical step before any formal Reader/Publication advance, the Human Owner replied, **verbatim**:

> はい、承認します。

This is an affirmative decision **about that immediately preceding Route A proposal**. It is not a free-standing approval of unpresented downstream artifacts. Review time is recorded as 2026-10-20 JST without invented seconds.

Decision: `ROUTE_A / CONDITIONAL_APPROVED / EDITION_LOCAL_PAGE_COUNT_ACCEPTANCE`.

## 2. Authorized editorial page-plan reconciliation (not an r2 Gate)

Human accepts the independently audited **r26 diagnostic issue structure** as a legitimate **approximately 21-page** planning/printing baseline: cover 1, physical article/body 17, bibliography 3. The issue has 7 chapters / 28 selected items, all 7 tables (27 rows / 110 cells), 150 preserved non-table Reader blocks, 90 bibliography keys / 19 aliases / 177 citation ledger rows. CONTENT=PASS, PRINT=PASS_WITH_LIMITATIONS from the independent r26 audit. The notable pre-table whitespace on p03/p11/p13 and lighter residual spacing is accepted as an editorial limitation, *not* evidence of content deletion and *not* a requirement to force 28 pages. Actual occupied area and per-chapter fractional allocations remain UNMEASURED. Do not equate 17 physical body pages with a measured new P1–P7 budget.

Human-approved formal **Architecture r1 remains exact-byte authoritative**: 26.5 planned article allocation, `page_plan.target_pages=28` advisory goal, `page_plan.max_pages=30` upper limit, original 7 package coverage. **No r2 is authorized or issued.** The human-approved Option B is now reconciled as an edition-local editorial acceptance of approximately 21 pages without rewriting the r1 Architecture. If the future canonical PDF varies in pages or quality, it requires its own review and byte-exact validation; this acceptance does NOT pre-approve any future Candidate.

## 3. Explicit condition precedent: frozen Core v2 dispatch proof

The next authorized execution is ONLY a read-only-on-canonical / edition-local-proposal **handler-and-validator routing feasibility preflight**. Frozen `config/survey-production-v2.json` defines at `DRAFT_COMPLETE`:
- `handler: stage:reader-publication-validation`
- `validator: validate:reader-publication`
- `next_state: VALIDATED_DRAFT`.

The default `scripts/survey_handlers_v2.py` registry in the reviewed main AND the State-pinned implementation does not register these two names; it registers different `semantic-publication` names. Registry names are not interchangeable without explicit, verified authoritative registration and semantic behavior. The frozen orchestrator fails closed on missing handler/validator.

Authorize a bounded Muse study of any pre-existing Core-compatible adapter or registered module / operator bridge, using read-only source inspection and noncanonical isolated dry-runs. **No stage execution against W42's canonical State is permitted.** If a valid existing route cannot be demonstrated without unauthorized shared-Core/config changes, the worker must STOP and submit evidence for separately reviewed Core-maintenance triage. No hand-written attestation, Gate, shim alias or rule bypass is authorized.

## 4. Matters expressly NOT approved

This decision does **not** authorize:
- canonical Reader manuscript creation or replacement, validated-source production, Publication Candidate, stage transition to VALIDATED_DRAFT/RELEASE_CANDIDATE, Human Publication Preview;
- edit of `architecture-v2.json` or Architecture r2, active r1 Gate/review index, `production-state.json`, Draft, existing diagnostics, or shared frozen Core/config/handlers;
- publication approval, Freeze, Release, forced page-count matching, or editorial re-research;
- new/fallback branches, `reset --hard`, rebase, force push or any rollback; r26 one-time local-reset Deviation does not apply to later work.

The separate r26 Human Owner reset-deviation acceptance remains recorded, limited to r26 with local effects `UNVERIFIED`.

Next specific contract:
`sources/2026-W42/execution/instructions/2026-10-20_muse-w42-r28-handler-routing-feasibility-noncanonical.md`.

Terminal for this Human decision: `HUMAN_W42_ROUTE_A_CONDITIONAL_APPROVED / R28_ROUTING_PREFLIGHT_AUTHORIZED / NO_CANONICAL_ADVANCE`.
