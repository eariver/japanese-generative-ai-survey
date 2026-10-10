# Collector raw — Independent A–L negative-space sweep log (Muse r2 gap-fill, 2026-10-10Z)

- collector_id: secondary-websearch
- collector_run_id: w40-primary-20261010-muse-r2
- retrieved_at: 2026-10-10T03:06:46Z
- window: [2026-09-25T22:00Z, 2026-10-02T22:00Z) UTC
- method: webfetch (6 Sol-cited first-party pages + H models license page) + websearch (HF blog week, AstaBrief/AutoSynthData time corroboration, open-model/training/agent lanes) + HF blog index enumeration.
- artifact_class: CLAIM_LEVEL_DERIVED_NOTE (sweep log, not source capture)

## Queries executed (r2; r1 queries preserved, not repeated as new)

1. Direct fetch `hcompany.ai/newsroom/holo4` + `huggingface.co/blog/Hcompany/holo4` + `hcompany.ai/research/models` -> CONFIRMED Sep 28 day-only; license split 27B noncommercial / 35B-A3B Apache-2.0; benchmarks publisher-reported.
2. Direct fetch `allenai.org/blog/olmocore3` -> CONFIRMED Oct 1 day-only; MoE training infra (DDP/expert/pipeline/dist-opt), 2.7x + trillion-scale tests; NOT foundation weights.
3. Direct fetch `huggingface.co/blog/open-tts-leaderboard` -> CONFIRMED Sep 30 day-only; WER/CER/TTFA/RTFx/SIM platform, NOT new speech model; human-preference disclaimer kept.
4. Direct fetch `huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source` -> CONFIRMED Sep 29 day-only team blog; paper arXiv 2606.18037 Aug 27 pre-window; team blog != independent result.
5. Direct fetch `allenai.org/blog/astabrief` + `huggingface.co/blog/allenai/astabrief` -> Oct 2 DAY ONLY both; NO clock time -> TIME_UNRESOLVED HOLD; Qwen3-8B/SFT47K/DPO6K/51.1s vs 178.5s/Apache-2.0 card header.
6. Direct fetch `huggingface.co/blog/ServiceNow-AI/autosynthdata` -> Oct 2 DAY ONLY; NO clock time -> TIME_UNRESOLVED HOLD; Hybrid/ITSM figures publisher-reported.
7. `Hugging Face blog week September 28 October 2 2026 model release` -> HF blog index enumerates AutoSynthData Oct 2 / Olmo-core Oct 1 / OpenTTS Sep 30 (day-only corroboration); third-party huggingface.blog mirror is retrospective commentary, NOT primary authority.
8. `AstaBrief 8B October 2 2026 publication time AllenAI` -> Ai2 Oct newsletter + Unite.AI/DataPhoenix/Neuron/NxCode all day-level Oct 2; NO exact time found. TIME_UNRESOLVED stands.
9. `AutoSynthData ServiceNow October 2 2026 paper EnterpriseOps Gym` -> XNews/Remio/DataPhoenix/AI-Brainer all day-level Oct 2; Gym paper Mar 2026 background; NO exact time. TIME_UNRESOLVED stands.
10. HF model-release scan (transformers v5.17.0 Sep 25: HYV4/VibeVoice/NeoMME/Fun-ASR-Nano/Kimi Linear/Canary-1B-v2/NeuCodec; v5.16.x Aug: Qwen4-Exp/GLM-5.3-Flash/ESMC) -> library support entries, NOT W40-window model premieres; no new frontier base LLM beyond r1 thin-lane finding. Transformers support != model release date.

## Revised lane matrix (r1 -> r2 deltas)

- A proprietary: unchanged STRONG (Sonnet/GPT-6.1/Argon/dots bundle). No new frontier chat model in r2 sweep.
- B open weights: THIN -> MODERATE (Holo4 35B-A3B Apache-2.0 + AstaBrief 8B open day-level-TIME_UNRESOLVED are material open-weight events even though NO frontier general base LLM appeared; narrowly true base-LLM observation separated from broad open-work claim per Sol).
- C coding/agent harness: STRONG -> STRONGER (Holo4 GUI/code/MCP/API + Olmo-core MoE training infra as harness-adjacent + ProvenanceGuard MCP verification + AutoSynthData curriculum TIME_UNRESOLVED).
- D image/OCR: unchanged MODERATE (FLUX Image Oct 1).
- E video/temporal: unchanged THIN-MODERATE (no new foundation video in r2 sweep).
- F audio/speech: THIN -> MODERATE (Open TTS Leaderboard platform Sep 30 is material eval-lane fill; still NO new TTS foundation model; Nemotron ASR tutorial stands).
- G serving/quant/local: unchanged MODERATE (Olmo-core MXFP8/training throughput is training infra, not serving runtime; no new inference runtime).
- H hardware: unchanged MODERATE (no new hardware in r2 sweep; DGX still TIME_UNRESOLVED).
- I eval/repro: MODERATE -> STRONGER (OpenTTS objective metrics + ProvenanceGuard 281-trace/361-claim + AstaBrief SQABench/DeepScholarBench + AutoSynthData Gym results, all publisher-reported needing attribution; independent reproduction still scarce).
- J safety/cyber: STRONG (ProvenanceGuard adds source-aware verification; still team-blog relay, paper pre-window).
- K retrieval/memory/enterprise: MODERATE -> STRONGER (ProvenanceGuard MCP attribution + AstaBrief cited reports + AutoSynthData verifier/task-gen TIME_UNRESOLVED + Context LMs).
- L open-world: MODERATE (Holo4 Task Factory 10k + Olmo-core trillion-scale + TTS platform are the open-world fills; no other paradigm unknown-unknown on current evidence).

## Negative results (honest stops, r2)

- NO exact clock time found for: Holo4 (Sep 28), Olmo-core (Oct 1), OpenTTS (Sep 30), ProvenanceGuard blog (Sep 29), AstaBrief (Oct 2), AutoSynthData (Oct 2). All date-day-only -> published_at NULL per SC-D02.
- NO_SOURCE_FOUND (r2 sweep): additional frontier base LLM beyond r1; new TTS/speech foundation model; new video foundation model; new inference runtime; new Oct 2 hardware ordinary beyond DGX-HOLD.
- NOT_NEW_IN_WINDOW: ProvenanceGuard paper Aug 27 (blog is the W40 event); EnterpriseOps-Gym paper Mar 2026; transformers library support entries (Sep 25/Aug) are not model premieres.
- LOW_MATERIALITY: huggingface.blog retrospective commentary (Sep 2026-written archive, not primary); community pretraining-VRAM experiment (Sep 26, throughput/evidence limits); LeRobot humanoid workflow (Sep 25, robotics tangential).
