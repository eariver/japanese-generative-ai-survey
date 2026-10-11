# W40 Sol Selection Review r10 — SCOPE CHANGE REVIEW REQUIRED

Date: 2026-10-10 JST
Status: SOL_SELECTION_SCOPE_CHANGE_REVIEW_REQUIRED
Repository: eariver/japanese-generative-ai-survey
Work branch: weekly/2026-W40-v2-work
Reviewed Muse r10 HEAD: 4dd18ffb11bf5ce402f4c0770572a73d52f81d0a
Reviewed Tree: 4ef46ebe692e3e265224a63684ea2c4664c2bbff
Reviewed main: afdb3df3faa20af3bb5798be429bba8dbd2100b1
W40 half-open UTC window: [2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)

## A. Execution and structural findings — PASS

Muse r10 directly descends from starting commit 9b8f8e8cd6a19c25f1ca4a3c79a1d2efb74a7b4c via one nonforce fast-forward commit. All 16 changed files are W40-local. Main, shared Core, canonical Discovery, Screening, Evidence, Views, Materiality, Completeness, State and Human Gates remained unchanged. State EVIDENCE_REVIEWED, next stage:selection.

S01 closed: 35 reviewer assignments = 28 SELECTED (20 PRIMARY / 8 SUPPORTING), 1 INSPECT (DGX), 4 HOLD, 2 REJECT. Two sweeps EXCLUDED, outside 35 assignments.

S02 closed for PREVIEW ONLY: r10 created a 35-row Core-derived Candidate Matrix staging file with real upstream SHA basis, 35-ID crosswalk and a separately labeled Core-schema-compatible reviewer-only Selection preview. Muse recorded Core validation PASS. This is NOT canonical Selection Acceptance and the review-only selection status ESTABLISHED is not a stage approval.

A01 editorial depth substantially improved: split P6a training methods/systems (Context Language Models, Olmo-core 3) from P6b evaluation/execution systems (AgentPerf, Open TTS, RL Environments). P2 distinguishes Holo4 general agent weights from Japanese ELYZA. P5 separates safety mechanisms, P7 separates modality/observability, P8 short enterprise digest. No Architecture file yet.

E01 focused primary reading improved: Olmo-core 3 technical report was partly read via segmented extraction (methods, parallelism, benchmarks); CLM appendices, ProvenanceGuard v2 later sections and MCP Auth README consumed. Still bounded: Olmo report cells/ablations/code unconsumed, FLUX 3 Image SKU weights/license unpinned, MCP Auth per-document details unopened. No accepted Card changed, no material contradiction proven. P6 narrative must retain limits.

## B. Critical independent finding SC-T11 — first-party hosted organizational announcements

Muse r10 time-investigation file contains two exact publication instants **reported by the hosting publisher platform** but rejected these solely because the clock was not from an independent corporate-domain server. This disqualification is too strict: an issuer may publish an original first-person announcement through its verified organization account hosted on another platform.

AstaBrief: https://huggingface.co/blog/allenai/astabrief
- Official allenai organization account, by Kyle Wiggers / Ai2Comms; first-person Ai2 model release article and direct links to AstaBrief model/data.
- Muse records Hugging Face page JSON-LD datePublished 2026-10-02T15:19:50.340Z and dateModified 15:22:07.584Z. Both are before W40 end 22:00Z.
- Source platform post time is primary evidence of THIS issuer-authored announcement, whether or not separate allenai.org post has a precise clock. It does NOT independently prove the first moment model weight files were obtainable or when corporate-site article was first posted.
- Independent publisher-item capture: https://wesearch.press/s/open-sourcing-astabrief-the-fast-report-generation-model-in-e81b1dea (15:19:50Z posting; observed 16:25:50Z), only corroboration to original platform metadata.

AutoSynthData: https://huggingface.co/blog/ServiceNow-AI/autosynthdata
- First-person ServiceNow CoreAI methodology announcement on official ServiceNow-AI organization account.
- Muse reads platform JSON-LD datePublished/dateCreated 2026-10-02T04:01:31.290Z, dateModified 04:05:48.837Z, earlier than W40 end.
- Independent publisher-item capture at 04:05:43Z: https://wesearch.press/s/autosynthdata-generating-training-data-for-enterprise-agents-56c490db.
- This proves a plausible first-party dated public METHOD ANNOUNCEMENT only. It does not prove standalone AutoSynthData code, weight, dataset or service release; distinguish the separate EnterpriseOps Gym dataset.

Sol independently opened both original Hugging Face organizational articles, verified authorship/first-person technical prose and directly checked the external time corroboration. The precise JSON-LD strings are supplied by Muse r10; obtain raw original bytes/SHA again before canonical usage. First-party hosting-clock publication timing is valid to investigate as edition eligibility and cannot be rejected categorically.

Both accepted r9 HOLD rationales rested substantially on allegedly unproven Oct2 hour. AstaBrief science report generation and AutoSynthData environment-validated, capability-gap-driven synthetic curriculum are technically substantial. These findings require an explicit candidate materiality/Selection scope decision; NOT an automatic claim that both are SELECTED, nor an automatic accepted upstream mutation.

## C. SC-T12 — two Cloudflare items not yet admitted

Cloudflare Web Search API and Pi Durable Harness official changelog dates show Oct2, but specific first-publication hour remains unresolved. RSS 13:00/00:00 may be default slots, not proof. Retain unadmitted without altering canonical Discovery.

## D. Core re-entry safety

Reviewed main survey_human_gate_v2.py invalidate_pending_gate requires Architecture checkpoint passed for Architecture Gate invalidation. W40 has only EVIDENCE_REVIEWED and Architecture pending, so this operation CANNOT be used now. Normal survey_production_v2.py transition_state forbids backward transitions. No manual State rewind, canonical Acceptance overwrite or synthetic Human review may be used to promote held items.

Until lawful Core-governed post-Evidence upstream amendment is identified and approved, freeze current 37/37/35/35 chain, 29 MATERIAL / 4 HOLD / 2 CONTEXT view and existing Stage. Create a versioned staged counterfactual, exact SHA impact and valid re-entry feasibility report. If no existing sanctioned route exists, report CORE_REENTRY_CONTRACT_GAP requiring reviewed Core maintenance, not undocumented edits.

## E. Decision

S01/S02 and editorial A01/A02: PASS for reviewer-only proposal.
E01: SUBSTANTIVE PARTIAL PASS with declared unread limits.
T01 for AstaBrief and AutoSynthData: CHANGE OF SCOPE MUST BE ADJUDICATED, not blanket TIME_UNRESOLVED.
Cloudflare N01: not yet eligible.
Selection Acceptance: HOLD, since new evidence may alter official HOLD/Materiality and article themes.

Terminal: SOL_SELECTION_SCOPE_CHANGE_REVIEW_REQUIRED. Next bounded Muse r11 contract: sources/2026-W40/execution/instructions/2026-10-10_muse-w40-hf-publication-timing-and-core-reentry-r11.md. No Selection acceptance, SELECTION_COMPLETE, Architecture or Human action is authorized.
