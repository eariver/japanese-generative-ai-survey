# W43 Sol → Muse chronology/authority feasibility r1 — recover October 23 cutoff integrity without changing Frozen Core or State

Status: `BOUNDED_READ_ONLY_AUTHORITY_RESEARCH_WITH_EDITION_LOCAL_REPORT / NOT_AN_EVIDENCE_REGENERATION / STOP_AT_SOL_AUTHORITY_DECISION`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing W43 work branch ONLY: `weekly/2026-W43-v2-work`
**Exact six Starting HEAD/Root Tree preflight values are supplied in Sol's dispatch AFTER this contract and index are committed**: work HEAD+Tree, reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / root Tree `a134dc36a407d08ab1de416324229b3955e0325a`, frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / root Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch → **ZERO WRITES STOP**, report expected/actual. No new branch/fallback/repair/review branch, rebase/reset/force or history rewrite.

## 0. Mission and authority

The user supplied independent review `20261025152137_SolReview.md`, raw SHA256 `310d28ca5b677f6403886525d46863cffa38126ed371c9e82cf5aeb812102f90`, copied (text-normalized, NOT byte-identical) into W43 `execution/audits/independent-sol-w43-evidence-r3-reaudit-result-20261025.md`. Independent disposition **REQUEST_CHANGES**, original W43-IA-001..015 now **PASS 10 / LIMITED 5 / FAIL 0**; new **P1 IA-016**, P2 IA-017/018 and nine day-only artificial midnight normalization risks. Sol authority `execution/reviews/sol-w43-evidence-r3-independent-reaudit-adjudication-20261025.md` is binding.

Current Production State **`CANDIDATES_NORMALIZED`** (Discovery and Screening machine checkpoints PASSED; Evidence/Materiality/Completeness PENDING; real Human Gates PENDING). 51 accepted Screening decisions and r3 32 Evidence/32 Views/21 supplement sources form a trusted historical chain. Prior accepted immutable files must remain immutable. **This work is an investigation, NOT approval to advance or invalidate Stage.**

Purpose: establish (A) exactly which October 23 events precede cutoff, (B) what Core-approved options exist to resolve upstream accepted Screening provenance, and (C) which single bounded repair contract can be approved *after Sol decides*. Do not prematurely "fix" by hacking r3 View, accepted Discovery/Screening, State/checkpoint or Core.

## 1. Mandatory precise source/temporal investigation (bounded)

W43 hard UTC window `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)` (America/New_York EDT Oct16 18:00 to Oct23 18:00); exclusive right edge.

Read actual 51 accepted Discovery/Screening decisions (not reconstruct), all 32 r3 Evidence Cards, Views, `materiality-ledger-v2.json`, `profile-completeness-v2.json`, existing `collectors/primary/runs/` and X raw. Focus at minimum on:
- `w43-primary-github-metrics-20261023`: official Changelog `https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode/` JSON-LD `2026-10-23T16:42:03-07:00 = 23:42:03Z` (OUT by **1h42m03s**), `dateModified=23:43:37Z`. r3 source and Card themselves record exact OUT clock while View `MAIN_EVENT`; day-only accepted Discovery says `Fresh in-window lead`. Read the actual archived 107700B HTML and exact metadata. Search **separate** authenticated first-party API availability / original release changelog **before Oct23 22:00Z**. Same source post-date, SEO search index timestamp, post's EDT calendar day or unverified social reaction is not proof of IN. If none proven: `OUT_OF_WINDOW_PRIMARY_PUBLICATION`, keep after-window signal distinguishably staged for W44; *do not* mislabel as current W43 item. Capture exact first-party URL, date source type, raw/ref SHA, and counterclaims.
- `w43-primary-github-teams-20261023`: official `https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams/`. Inspect original HTML JSON-LD datePublished/modified+timezone, any signed GitHub release/repository action/Teams App manifest. Judge independent W43 before-cutoff event. Do not assume similar to Metrics.
- `w43-primary-nemotron-e4b-20261023`: actual NV/HF model card, repo earliest content/tag/model-files upload, API announcement and timestamp; distinguish Git commit/revision time from public access availability.
- `w43-primary-tanstack-20261023`: TanStack AI 1.0 official blog `https://tanstack.com/blog/tanstack-ai-1-0`, package registry metadata and GitHub tagged release/publish time, independent author/X post if legitimate and edition-approved. Day-only blog alone IN is UNRESOLVED.
- `w43-r2-openai-securing-20261023`: primary OpenAI official publish clock versus external feed `10:00Z` secondary; identify exact subject and earliest first-party event, avoid asserting in-window based only on date.
- `w43-primary-kimi-20261023`: first-party X post `2026-10-23T17:15:24Z` IN; distinguish separate Kimi blog DATE_ONLY, Nov 4 weights FUTURE.
- `w43-support-vercel-ollama-20261017`: resolve audit's `Oct23 Card` vs Oct17 ID mismatch: actual official distributions/tags/version and event identity.
- Every other candidate with `published_at` on cutoff-day Oct23 but no clock. Produce one per-Discovery-ID table, including accepted Screening decision, inherited reason, publisher source/date and independent *earliest definite* event time, timezone, revision metadata, precision, UTC window classification **IN/OUT/UNRESOLVED**, and action. Include non-DROP and DROP records if Oct23 relevant; retain 12 W42 carry and 19 DROP denominators.

For the **nine** supplement r3 `T00:00:00Z` values inferred from day-only publisher pages (auto-mode, Decisions, FLUX×2, Kimi, Nemotron, Patch, Flint×2): inspect exact Core supplement schema and semantics. Label source timestamp as `DATE_ONLY_PLACEHOLDER_NOT_OBSERVED_CLOCK` in new **diagnostic**, without changing existing accepted JSON; flag if schema itself would forbid nullable published_at and specify supported option. Do not convert day precision to false real time, especially near cutoff.

Archive newly read public-source data ONLY if essential for documentary evidence; writing allowance restricted below. Never forge SHA, event clock, raw byte preservation, source type, full page read or external screenshot.

## 2. Mandatory frozen-Core authority and safe restoration feasibility (READ ONLY, no experiments against canonical State)

Read verbatim:
- `scripts/survey_production_v2.py::transition_state` (exactly one forward transition), State provenance validations and allowed LIFECYCLE;
- `scripts/survey_core_execution_bridge_v2.py::execute_request` operator kinds, `_advance_stage` preconditions; actual operator request schema file from repository; trusted Issue #448 bridge scope;
- `scripts/survey_human_gate_v2.py::invalidate_pending_gate` preconditions and config `operator_pending_gate_invalidation_boundaries`, Human pending state requirement and Architecture checkpoint precondition;
- `scripts/survey_agent_control_v2.py` stage checkpoint, `survey_agent_tool_v2.py` agent-first adapter, `survey_stage_validation_v2.py` Screening and Evidence stage contracts, `scripts/survey_discovery_v2.py`, `survey_screening_v2.py`, frozen profile/State schema.
- Existing W34 historical operator invalidation docs: `docs/checkpoints/2026-09-05-core-v2-pre-human-evidence-regeneration-repair-validation-r1.md` is for an **unpresented Human Architecture Gate**, NOT automatically available at present W43 pre-gate. Review known frozen #568/#569 to avoid erroneous reuse.
- W43 exact trusted receipts `execution/bridge-runs/sol-w43-discovery-advance-20261025`, `...screening-advance-20261025` and their Stage Checkpoints. The current immutable accepted Discovery/Screening tree and SHA authority cannot be discarded in a merely derived new Evidence Card without explicit provable safe basis.

**Evaluate three repair designs with exact accept/reject verdict and cited function/schema guards**:
A. Native approved operator rewind / invalidation (does it exist at `CANDIDATES_NORMALIZED`? Default observed **NO**, prove or refute);
B. Core-valid forward-only append-only editorial provenance correction + exclusion for OUT event **without** changing accepted Discovery/Screening. Verify whether any built-in schema/Stage validator accepts a discrepancy record and resolves the inherited `Fresh in-window lead` claim. Do not presume that switching to `CONTEXT` or `NON_MATERIAL` cures trusted source authority;
C. If A/B unsupported, proposal for a **separately reviewed Core maintenance / new operator authority** with actual human/operator control, exact frozen change isolation and trust provenance, or explicit BLOCKED state until a supported workflow is available. **Do not implement Core changes now**, and do not create a workaround stage/review branch.

For each design give: exact permissible Core API/operation; required new vs superseded historical artifacts; whether Machine Checkpoint State provenance needs re-attestation; effects on 51 accepted Screening and 32 Evidence; parent/child authority graph hashes and regeneration order; fail-closed tamper tests; whether true user approval required. If unsupported, flag `NOT_SUPPORTED_UNDER_FROZEN_CORE`; never sneak a new mechanism into W43 edition files or manufacture a Human Gate revision.

## 3. IA-017/IA-018, residual P2 (do not churn evidence)

- Kimi and Flint inherited fused `src-1.url`: provide exact `claim_id → actual supplement source_id → source URL and evidence excerpt` for reader-facing citations, retaining immutable old discovery locator as discovery-only; indicate whether the frozen Card schema would still carry it internally. No Core/accepted edits.
- IA-018 numbers: actual `interactive-evidence-r2.json`→`r3.json`: **19 substantive field changes / 13 rationale-only**; all 32 accepted Card result SHA differ due package/basis. Audit worker misleading `20/12`, propose append-only erratum.
- Remaining 5 LIMITED from independent audit remain bounded as limitations unless contrary primary source exists. Do NOT broaden to AM-Bench v1/v2 full research, benchmark replication, redrafting or Selection. Grok stays NON_MATERIAL, no article from partial X sensor.

## 4. Narrow allowed write set; exact stop

Allowed files on SAME existing W43 branch ONLY after exact six-SHA/Tree preflight: **new edition-local diagnostic markdown**:
- `sources/2026-W43/execution/source-intake/w43-cutoff-oct23-event-clock-audit-r1-20261025.md`
- `sources/2026-W43/execution/reviews/muse-w43-prehuman-upstream-authority-feasibility-r1-20261025.md`
- `sources/2026-W43/execution/SOL_W43_UPSTREAM_AUTHORITY_DECISION_HANDOFF-r1.md`
- `sources/2026-W43/execution/sessions/muse-w43-cutoff-authority-feasibility-r1-20261025.md`
- `sources/2026-W43/execution/index.md` (append only with true HOLD state)
- OPTIONAL **additional edition-local archived raw** solely of authentically fetched official public Oct23 timestamps, with exact SHA manifest and source IDs; do not mutate pre-existing raw. If publication evidence is fully covered by existing repository raw, avoid duplicate archive.
No edits to `scripts/`, `schemas/`, `tests/`, `config/`, `.github/`, `AGENTS.md`, `production-state.json`, `production-profile.json`, `orchestration/`, `screening/`, `discovery/`, `evidence/v2/accepted/`, `evidence/v2/views/accepted/`, `external/evidence-supplement/`, `materiality-ledger-v2.json`, `profile-completeness-v2.json`, prior audit reviews, prior sessions, Grok X raw, W42, main or Frozen Core. No operator Bridge or issue comment, no Human Gate decision, no Stage advance, no Selection/Architecture/TeX/PDF/Freeze/Release.

If unable to prove a safe canonical fix, report `AUTHORITY_RESTORATION_UNSUPPORTED_UNDER_FROZEN_CORE` and stop with exact code evidence and proposed separate review contract; never claim Screening formally repaired. If later discovery shows a safe path, **DO NOT EXECUTE IT YET**, only document preconditions for independent Sol approval.

Commit only edition-local permitted files normally and non-force push existing branch; final remote HEAD/Root Tree readback. Stop exactly `SOL_W43_CUTOFF_AND_AUTHORITY_DECISION_READY_R1`. Output per-ID clock table with proof, assessment A/B/C, remaining true P1 blockers, tested vs reported validators, recommendation that **does not pretend Human Gate approval**.
