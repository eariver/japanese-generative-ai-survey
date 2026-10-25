# W43 — independent Sol one-shot comprehensive technical/editorial audit request

Status: `INDEPENDENT_REVIEW_REQUEST / READ_ONLY / NO_MUSE_DISPATCH / NO_HUMAN_GATE`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing work branch: `weekly/2026-W43-v2-work`
Baseline BEFORE this independent-review request: work HEAD `8c068e75f38f3747e614d32ef12400d973a04dae`, root Tree `ab522639126c721efbb5f4d7afadc6c6d30be91d`.
**Authoritative audit-start commit/tree are in the separate Sol dispatch message after this request and index are committed**; the audit must pin to those exact six remote identities.
Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`; root Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core branch `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`; root Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## A. Independence and stop contract

You are **a fresh, independent Sol reviewer**, not the Sol editorial controller who prepared this request and not the Muse author. Conduct a substantive, adversarial, technically informed review of ALL W43 edition-local authority currently present, not a rubber stamp of prior audit conclusions. **Strictly read-only**: no Git commits, branches, issue comments, PR changes, correction files, merge, Core maintenance, Bridge commands, `ADVANCE_STAGE`, State/Checkpoint/Human Gate edits or publication. You may use read-only GitHub tools and public official websites, arXiv/papers and official APIs for verification; do not infer GitHub availability from stale summaries. Review repository at **one pinned exact SHA**, never silently mix branches or revisions. If SHA/Tree changed, report expected/actual and stop before substantive authority claims. Do not run Muse, write an instruction to Muse, or presume any Human Gate approval.

The current **canonical Stage is `CANDIDATES_NORMALIZED`**, Evidence/Materiality/Completeness machine Checkpoints pending, Architecture Review and Publication Preview Human Gates pending. Worker has generated accepted *artifacts* but **has not performed trusted Stage advance**. The existing narrow Muse r3 repair instruction exists at `execution/instructions/sol-w43-evidence-r3-patch-memt-source-integrity-20261025.md`, but its **execution is explicitly ON HOLD pending this independent audit**. Do not treat its narrow scope as an audit limit.

For independence, perform a **blind-first-pass** structural and claim audit from frozen Core contracts + actual primary artifacts **before** reading prior Sol r1/r2 review conclusions or Muse handoff summaries. Then read the history to reconcile discrepancies. Existing notes are leads, not proof. Flag cases where your findings contradict previous Sol, Muse or accepted Core results.

## B. Work products and frozen contracts to inspect

1. Freeze/State: `sources/2026-W43/production-profile.json`, `production-state.json`, `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`, `orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json`, Bridge receipts and operator request commit ancestry; actual immutable/main/frozen-Core identities. Read frozen `scripts/survey_agent_control_v2.py`, `survey_agent_tool_v2.py`, `survey_stage_validation_v2.py`, `survey_evidence_v2.py`, `survey_completeness_v2.py`, materiality modules and actual schemas. Do not assume legacy direct `verify_state_basis` works after Bridge; native agent-first adapter is part of existing frozen Core.
2. 51 accepted Discovery: `sources/2026-W43/discovery/discovery-v2.jsonl`, `discovery/discovery-accepted-v2.json`; X manifest `external/x/x-source-intake-v2.json`, Grok original `external/x/weekly-x-2026-W43/weekly-x-2026-W43.md`. 51 accepted Screening decisions in `screening/v2/accepted/75dd95db5c40b28cc2d9a665dab8a46294e010096095c2bf92aba36d5ed9817d/screening-accepted.json` (expected distribution `KEEP 17 / MAYBE 11 / INSPECT 4 / DROP 19`, verify, don't copy). W43 ordinary UTC window **`[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`**; retain per-event type, W42 carry, OUT vs revised IN, and observation/post-window distinction.
3. Current Evidence r2: `evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/evidence-accepted.json` and **all 32** `results/task-*.json`; `evidence/v2/views/accepted/c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c/edition-views-accepted.json` and **all 32** `views/view-*.json`. Also current `materiality-ledger-v2.json` (expected 51), `profile-completeness-v2.json` (three WEEKLY obligations). Do not assume a Core schema PASS proves truth of a claim or adequacy of Materiality.
4. Source and derived execution: original primary collectors `collectors/primary/runs/`, current r2 collector run `collectors/primary/runs/20261024T191700Z-muse-r2-evidence/`, `external/evidence-supplement/evidence-authority-supplement-r1.json`, `...-r2.json`, actual PDF/raw files, `execution/compat/evidence-source-class-projection/` (r1/r2 builder, tasks, projection ledger, interactive input, runner). Compare r1/r2 historical accepted Evidence/Views and `execution/history/r1/` snapshots for correct immutability and facts.
5. Only AFTER blind initial inspection: `execution/SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r2.md`, `execution/sessions/muse-w43-evidence-authority-r2-20261025.md`, depth records, prior Sol `execution/reviews/sol-w43-evidence-r1-first-party-gaps-and-memt-archive-20261025.md`, `execution/reviews/sol-w43-evidence-r2-factual-provenance-review-20261025.md`, current held r3 instruction, and open Core Issues #568/#569. These documents' factual assertions and numbers are **NOT** automatically authoritative.

## C. Exhaustive audit dimensions — do not stop after known defects

**Coverage matrix is mandatory: every one of the 32 Evidence Tasks/Card IDs and Views receives an explicit audit verdict, source depth assessment, open issues and concrete next action**, plus 19 DROP source dispositions and all 12 W42 carry rows accounted for in a separate completeness check.

### C1. Model/paper/security/agent factual correctness, technical depth

For all **20 MATERIAL** items, read and interrogate ALL major claims and quoted numbers (architecture/parameter sizes, MoE active count, context lengths, memory update semantics, time/speed definitions, training/hardware, license and availability). Confirm which are direct first-party facts vs author/publisher claims vs truly independent reproduction, with a link/citation to actual authoritative original. At minimum examine:
- Kimi K3.1 Pro Oct23 API vs promised Nov4 weight release, exact X publish clock and W43 cutoff (17:15:24Z → 4h44m36s); official model version, benchmark suite, basis, price and claim classes.
- Recursive Flint actual Oct21 model weight/license/card, MoE routing architecture, 125+/150+ tok/s and hardware/quantization/sampling assumptions; separate source date from X chatter.
- DeepSeek V4.1-Flash 1017, DeepInfer inference engine repo creation vs announcement, actual inference-only missing components/hardware, benchmark denominators.
- Nemotron Bolt E4B 64K context, licensing (OpenMDW-1.1 not automatically OSI-open), 8B total vs effective, release artifact.
- MemT GDN-2/MoS mathematical/mechanistic claims, training tokens, reported storage/speed baselines, model names, source bytes and **exact paper vs README license** authority.
- MOSS trainer/research/API event separations, in-window proof and benchmark/license availability.
- Voice/video: Voxtral 3/Eleven/Ming, FLUX 3 Max 10.95 vs 12.45 latency discrepancy, arena/vendor scoring and deployment/pricing.
- Agent platform and permissions: Claude Duet, auto mode Oct22 updated older article (Aug7 original OUT, next-week rollout not completed), 1Password credential-boundary **available vs coming soon**.
- OpenAI: low-resource language, biology agent system, training environment security, Decisions API GA and technical rate/input limits, Patch the Planet PHP disclosure and model attribution (independently read official English/JP), plus actual Google Cloud announcement date/model listing/data controls; avoid conflating vendor marketing with independent fact.
- Examine original official and scientific-paper bodies where possible. If technical material is thin, specifically identify which equations/ablation/harness/standardized benchmark/weight LICENSE bytes would change a claim or publication statement. Do NOT invent local reproductions or fetch dates.

For the **11 CONTEXT** items, test whether technical novelty/provenance genuinely supports CONTEXT rather than MATERIAL or EXCLUDED; if paper revision (AM-Bench/oracle) verify v1→v2 *substantive delta*, not merely updated arXiv date. For the **one NON_MATERIAL Grok audit-binder**, inspect exact X raw/post IDs and forbid it becoming a story or falsely independent corroboration.

### C2. Provenance and artifact graph (all 32)

For every Card claim, trace `statement_id` → `source_ids` → Card `sources[].url` → actual consumed official/paper/raw artifact and exact observed claim passage. Identify alias/pseudo-locator vs real URL, README-only licensing wrongly attached to PDF, source-class inflation, missing archive, mismatched raw bytes/size/SHA/date, circular claim support, sources describing different products/dates, multiple refs falsely represented by one URL. Distinguish rendered page read from raw HTML byte archive. Compare actual r2 supplement `sources` count with worker summaries and test task-binding exactness, original 7-ID projection from unsupported `source_type` into frozen Core classes: **no silent upgrade of X/secondary to primary**; original Discovery and Screening must be unchanged. For every verified/unverified target, check the claimed `VERIFIED` means page/metadata **read** versus actual result reproduced.

### C3. Chronology and issue membership

Check exact beginning/end UTC and each relevant timestamp, archive time vs publication time, release vs paper v2 vs feature next-week rollout vs update vs initial original; the 12 W42 carry actions and 19 DROP decisions. Investigate W43 novel events omitted or overweighted through r2, duplicate-family issue, mere X popularity, after-window Grok run, original Oct15/Oct16 OUT. Cite exact primary timestamps for misdated event; do not substitute an observed_at value for a publication time.

### C4. Editorial Materiality, 51-row ledger and three Completeness obligations

Independently score rationale on documented technical novelty, relevance, depth, independent reproducibility, contradiction, sourcing and reader utility. Avoid forcing all KEEP→MATERIAL, MAYBE→CONTEXT or INSPECT→HOLD; require positive/negative reasoning, rank significance within scope without inventing an article count or exceeding source proof. Check all 51 ledger rows, including 19 excluded, 12 W42 carry and Grok NON_MATERIAL; ensure no hidden gaps among 17 old KEEP and newly upgraded first-party entries. Evaluate `weekly:current-relevance`, `weekly:technical-significance`, `weekly:carry-over` for honesty under `LIMITED` vs closure; explicitly list material missing dimensions and reader risks. Consider editorial structure only as recommendations: **no Selection/Architecture gate claim**, no manuscript.

### C5. Mechanical and Frozen Core boundary

Check all actual SHA/Tree IDs, three key authority graph digests, accepted Evidence r1/r2 history immutability, Core content-addressed package/view/card binding, evidence supplement raw SHA integrity, validation stdout vs alleged PASS, X require_complete `COMPLETE` registration vs `PARTIAL` sensor, duplicate IDs, out-of-window, archive timestamps, missing source identity, 7 derived-only projections and original source types. Trace the exact native adapter scope and known legacy direct-helper Issue #568, source-class #569 without authorizing shared Core edits. A missing runtime execution test must be marked `NOT_EXECUTED`, not PASS. Read-only Core tests against copies are optional if environment supports safely. Do not mutate canonical State, any generated accepted output or source.

## D. Required output and decision format

Deliver a **single self-contained audit report in the separate Sol chat** (not GitHub edits), sufficient for editorial Sol to issue ONE integrated bounded Muse r3 instruction. Include:

1. **Independence declaration + exact six SHA/Tree preflight + permissions**; audit source scope, external sources actually visited, unvisited links/bytes, integrity-verified vs worker-reported tests.
2. **Executive disposition**: `PASS`, `PASS_WITH_LIMITATIONS`, `REQUEST_CHANGES` or `BLOCKED`; state whether trusted `EVIDENCE_REVIEWED` Stage movement is currently permitted (default NO if CR).
3. **All-32 coverage table**: discovery ID, prior Screening KEEP/MAYBE/INSPECT, Evidence status, Materiality, exact source-depth category (`FULL_PRIMARY_READ`, `PARTIAL_PRIMARY_READ`, `METADATA_ONLY`, `SECONDARY_OR_X_ONLY`, `UNVERIFIED`), relevant claim IDs, a reviewer verdict and required action.
4. **Findings register**, grouped severity `P0 BLOCKER`, `P1 MUST_FIX_BEFORE_STAGE`, `P2 EDITORIAL_IMPROVEMENT`; for EACH finding: stable audit ID `W43-IA-###`, discovery/task/card ID, exact file path, claim_id/field, quoted old source/current claim minimal excerpt, primary source URL+section or authoritative bytes/SHA, impact/risk, precise suggested correction, whether it changes factual Card, materiality/View, completeness or just report.
5. **Provenance/source-class crosswalk table** and **31-substantive + 1-Grok editorial assessment**, explicit 51-ledger reconciliation / 12 carries / 19 DROP review, date/event matrix, and true limitations.
6. **Prior Sol/Muse contradiction ledger**, especially assumptions from held r3 instruction that audit independently confirms/rejects, and ALL newly discovered issues that narrow r3 would miss. Do NOT simply list the already known Patch/MemT defects.
7. **Minimal bounded regeneration plan**, proposed affected IDs, which raw primary artifacts require fresh ingestion, exact Core acceptance/Views/Materiality/Completeness stages to rerun, negative integrity tests, and which old artifacts remain immutable. Highlight any uncertain source findings needing a second check rather than inventing definitive correct text.
8. **Human boundary**: no Human architecture/publication review assumed, no Machine `ADVANCE_STAGE`, no writing, no direct Muse instruction from the audit session; stop for editorial Sol to integrate your results.

If resource/tool access limits prevent exhaustive inspection, report **how many of 32** were actually deeply checked; do not label partial sampling `comprehensive PASS`. High-level summaries alone are insufficient; evidence citations and concrete new/old claims are mandatory.

Terminal stop: `INDEPENDENT_SOL_W43_EVIDENCE_COMPREHENSIVE_AUDIT_COMPLETE` (or `INDEPENDENT_AUDIT_INCOMPLETE` with specific unvisited sources).
