# SP-2026-M03 — Candidate Selection proposal v0.1

Status: **PENDING HUMAN APPROVAL**. This is an editorial working proposal only. It does **not** approve Candidate Selection, change the pipeline gate, or approve Issue Architecture.

Basis:
- accepted Evidence run: `3e77733c01d893050196aaf946600ebe8f2a08b5a973cc6903a075b2008f306c`
- accepted Candidate surface: 57 `CANDIDATE` records
- M03-only clustering: `preselection-m03-only-clustering-v0.1.md`
- later-month continuity was deliberately excluded from promotion/demotion decisions

## Proposed role counts

| Role | Count | Meaning in this proposal |
|---|---:|---|
| FEATURE_CORE | 4 | issue-defining anchor evidence |
| SECTION_CORE | 11 | primary evidence anchoring a major section |
| SUPPORTING_EVIDENCE | 13 | distinct evidence used to deepen or qualify a core theme |
| PAPER_WATCH | 5 | research worth surfacing concisely without carrying a main section |
| CHRONOLOGY | 3 | material month chronology retained without a full article treatment |
| HOLD_OUT | 21 | verified Candidate not selected for the 32–40 page issue because of overlap, narrowness, or lower marginal editorial value |
| **Total** | **57** | |

Positive editorial roles total 36 evidence items. `HOLD_OUT` is not a rejection and does not revise Evidence; it remains available if a later architecture revision exposes a genuine coverage gap.

Core count is 15: Inference/Serving/Systems 4; Safety/Security/Control 4; Frontier Models/Developer Platform 3; Multimodal/Generation 2; Agents/Runtime/Long-horizon 2; Reasoning/Evaluation/Training 0. The smaller Reasoning/Evaluation cluster is retained through Paper Watch rather than promoted to a main section merely for symmetry.

## 1. Inference / Serving / Systems — 15

| Candidate | Proposed role | Rationale |
|---|---|---|
| Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models | SUPPORTING_EVIDENCE | Distinct multimodal-serving architecture that broadens the systems section beyond text-only serving. |
| TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition | PAPER_WATCH | Methodologically useful decomposition of inference overhead, but narrower than the runtime/project anchors. |
| Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity | HOLD_OUT | Relevant heterogeneous-serving result, but overlaps the selected multimodal-serving/system-efficiency evidence under the page budget. |
| NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL | SECTION_CORE | Concrete MoE communication-layer development; strong independent systems anchor. |
| Parallelizing Tool Execution and LLM Generation for Low-Latency Agent Serving | SECTION_CORE | Directly connects tool execution with serving latency and gives the systems section an agent-serving mechanism rather than only generic inference. |
| The Workload-Router-Pool Architecture for LLM Inference Optimization: A Vision Paper from the vLLM Semantic Router Project | SUPPORTING_EVIDENCE | Useful architectural synthesis for routing/pool design, but as a vision paper it should support rather than anchor the section. |
| TCM-Serve: Modality-aware Scheduling for Multimodal Large Language Model Inference | HOLD_OUT | Good scheduling example, but marginal coverage overlaps Cornserve and the selected multimodal/system evidence. |
| KVSculpt: KV Cache Compression as Distillation | HOLD_OUT | Technically relevant KV-cache optimization, but one of several similar March efficiency papers; lower marginal value in a constrained issue. |
| IsoQuant: Hardware-Aligned SO(4) Isoclinic Rotations for LLM KV Cache Compression | HOLD_OUT | Specialized compression technique; retain in Evidence but not enough independent editorial weight for the main issue. |
| Understand and Accelerate Memory Processing Pipeline for Large Language Model Inference | SUPPORTING_EVIDENCE | Provides a useful systems-level memory-processing abstraction that complements cache/routing/runtime evidence. |
| VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference | HOLD_OUT | Relevant long-context acceleration result, but secondary to selected runtime, routing, communication, and memory evidence. |
| TensorRT-LLM v1.2.0 | CHRONOLOGY | Stable March project release establishes the production-runtime chronology without requiring separate feature treatment. |
| vLLM v0.18.0 | SECTION_CORE | Material project release with gRPC serving and runtime changes; strong primary-repository anchor. |
| vLLM v0.17.0 | HOLD_OUT | Earlier March vLLM release is valid chronology but v0.18.0 gives the stronger single project anchor and avoids version-by-version listing. |
| TensorRT-LLM v1.3 release-candidate series | FEATURE_CORE | Dense March series spanning KV cache, routing, quantization, hardware support, and MoE serving; best single anchor for the infrastructure story while preserving RC status. |

## 2. Safety / Security / Control — 14

| Candidate | Proposed role | Rationale |
|---|---|---|
| The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense | HOLD_OUT | Relevant defense architecture, but the selected first-party prompt-injection material plus empirical security studies already cover the threat at higher editorial leverage. |
| Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs | PAPER_WATCH | Distinct autoresearch/adversarial-evaluation angle worth surfacing, but not necessary as a section anchor. |
| The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities | SUPPORTING_EVIDENCE | Strong empirical support for configuration as a security variable; complements rather than duplicates prompt-injection guidance. |
| “Elementary, My Dear Watson.” Detecting Malicious Skills via Neuro-Symbolic Reasoning across Heterogeneous Artifacts | HOLD_OUT | Concrete malicious-skill defense, but narrower than the selected privilege, prompt-injection, and monitoring evidence. |
| A Security Analysis of the OpenClaw AI Agent Framework | HOLD_OUT | Valuable framework-specific taxonomy, but its scope is narrower and risks overweighting one runtime relative to the broader March security surface. |
| Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers | SECTION_CORE | Cross-surface, stage-level prompt-injection measurement provides a strong empirical section anchor. |
| Evaluating Privilege Usage of Agents with Real-World Tools | SUPPORTING_EVIDENCE | Adds authorization/least-privilege evidence distinct from prompt injection and monitoring. |
| Covert Visual Prompt Injection against Commercial Multimodal Large Language Models | HOLD_OUT | Important multimodal attack variant, but page-budget overlap is high once general prompt injection and multimodal security boundaries are covered. |
| Improving instruction hierarchy in frontier LLMs | SECTION_CORE | First-party research on trusted-instruction priority links model behavior directly to prompt-injection resistance and steerability. |
| Reasoning models struggle to control their chains of thought, and that’s good | SUPPORTING_EVIDENCE | Adds CoT monitorability as a separate safety-control mechanism without making it a full section. |
| Designing AI agents to resist prompt injection | FEATURE_CORE | First-party agent-system design guidance directly addresses risky actions, sensitive data, and execution boundaries; strongest practical security anchor. |
| Monitoring internal coding agents for misalignment | SECTION_CORE | Concrete deployment-monitoring evidence at the intersection of coding agents, CoT, and operational safety. |
| Codex Security research preview | SUPPORTING_EVIDENCE | Material application-security agent launch; supports the shift from passive code generation to security-sensitive agent work while vendor effectiveness claims remain bounded. |
| Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? | HOLD_OUT | Useful methodological CoT result, but lower marginal value once CoT-Control and coding-agent monitoring are retained. |

## 3. Frontier Models / Developer Platform — 9

| Candidate | Proposed role | Rationale |
|---|---|---|
| GPT-5.3 Instant: Smoother, more useful everyday conversations | CHRONOLOGY | Establishes the early-March OpenAI model chronology but is superseded editorially by GPT-5.4 within the same month. |
| GPT-5.4 | FEATURE_CORE | Central March frontier-model release with coding, computer use, tool search, and long-context positioning; primary model anchor. |
| GPT-5.4 mini and nano | CHRONOLOGY | Important same-family extension into smaller/faster and subagent-oriented roles; concise chronology is sufficient. |
| Claude Sonnet 4.6 | SECTION_CORE | Independent frontier-model release from another major vendor with coding, computer-use, long-context, and agent-planning relevance. |
| GLM-5-Turbo | SUPPORTING_EVIDENCE | Adds a non-Western vendor model explicitly positioned for long-chain agent workloads and tool/multi-agent execution. |
| Gemini API March 2026 model and tool updates | SECTION_CORE | Dense first-party March chronology across models, multimodal embeddings/generation, live audio, and tool composition; strong developer-platform anchor. |
| Alibaba Model Studio March 2026 model updates | SUPPORTING_EVIDENCE | Concrete Qwen Image 2.0 and other March lifecycle entries broaden vendor and multimodal coverage. |
| Transformers v5.3.0 | HOLD_OUT | Ecosystem release is valid but lower editorial leverage than vendor/model/runtime anchors; avoid version-listing pressure. |
| Transformers v5.4.0 | HOLD_OUT | Same rationale as v5.3.0; retain in Evidence rather than spend scarce issue space on sequential framework releases. |

## 4. Multimodal / Generation — 9

| Candidate | Proposed role | Rationale |
|---|---|---|
| LongCat-Next: Lexicalizing Modalities as Discrete Tokens | SECTION_CORE | Distinct unified multimodal modeling approach; strong technical anchor independent of the agent narrative. |
| CDH-Bench: A Commonsense-Driven Hallucination Benchmark for Evaluating Visual Fidelity in Vision-Language Models | PAPER_WATCH | Useful multimodal evaluation perspective that can be presented concisely alongside the main generation/model story. |
| Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model | HOLD_OUT | Interesting retrieval/generation unification, but lower marginal value against stronger selected multimodal anchors. |
| ResAdapt: Adaptive Resolution for Efficient Multimodal Reasoning | HOLD_OUT | Efficiency contribution overlaps broader systems/multimodal optimization evidence. |
| DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing | SUPPORTING_EVIDENCE | Adds on-device generation/editing and deployment diversity to the multimodal section. |
| Gen-Searcher: Reinforcing Agentic Search for Image Generation | SUPPORTING_EVIDENCE | Provides a clear bridge between grounded search and image generation without forcing the entire multimodal section into an agent framing. |
| Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism | HOLD_OUT | Relevant long-video memory work, but the selected issue already has strong memory/system and multimodal coverage. |
| Unify-Agent: A Unified Multimodal Agent for World-Grounded Image Synthesis | SECTION_CORE | Strong cross-cutting multimodal-agent pipeline with search, grounding, recaptioning, and synthesis; good second anchor for the cluster. |
| ComfyUI v0.18.0 | HOLD_OUT | Practical workflow release is useful chronology, but less central than the selected model/research evidence under the page budget. |

## 5. Agents / Runtime / Long-horizon Work — 6

| Candidate | Proposed role | Rationale |
|---|---|---|
| ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning | HOLD_OUT | Useful orchestration research, but overlaps systems/resource-management coverage and has lower standalone editorial leverage. |
| Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design | SUPPORTING_EVIDENCE | Adds verification-centric deep-research design as a concrete long-horizon agent pattern. |
| MemFactory: Unified Inference & Training Framework for Agent Memory | SUPPORTING_EVIDENCE | Provides an explicit agent-memory framework and strengthens the long-horizon/runtime dimension. |
| Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents | SECTION_CORE | Directly addresses why short-task success metrics are inadequate for long-horizon agents; strong conceptual section anchor. |
| From model to agent: Equipping the Responses API with a computer environment | FEATURE_CORE | First-party runtime architecture with shell, containers, files, tools, and state; clearest March evidence of model capability being embedded into an execution environment. |
| KAT-Coder-V2 Technical Report | HOLD_OUT | Agentic coding model is relevant, but coding-agent coverage is already strong through GPT-5.4, Codex Security, Responses runtime, and operational monitoring. |

## 6. Reasoning / Evaluation / Training — 4

| Candidate | Proposed role | Rationale |
|---|---|---|
| Rethinking Easy-to-Hard: Limits of Curriculum Learning in Post-Training for Deductive Reasoning | HOLD_OUT | Sound methodological result, but weak connection to the issue’s dominant March clusters relative to the page cost. |
| MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome | PAPER_WATCH | Compactly represents process/outcome evaluation for deep-research agents and complements the long-horizon reliability section. |
| ELT-Bench-Verified: Benchmark Quality Issues Underestimate AI Agent Capabilities | PAPER_WATCH | Strong methodological warning about benchmark quality; useful as a concise evaluation note rather than a main section. |
| Think Anywhere in Code Generation | HOLD_OUT | Interesting reasoning mechanism, but coding/reasoning coverage is already dense and this adds less distinct issue-level value. |

## Editorial consequence if approved

The resulting issue should not be structured as an “agent issue.” The selected evidence supports five main editorial surfaces:
1. Frontier Models / Developer Platform as the chronology backbone;
2. Inference / Serving / Systems as the densest engineering theme;
3. Safety / Security / Control as a co-equal major engineering theme;
4. Multimodal / Generation as an independent substantial theme;
5. Agents / Runtime / Long-horizon as the cross-cutting execution theme.

Reasoning / Evaluation / Training remains visible through Paper Watch and supporting interpretation rather than being inflated into a symmetric main section.

The preferred M03-only thesis remains:

> **2026年3月は、frontier modelの更新が相次ぐ一方、技術的な焦点が推論・配備、安全性、マルチモーダル、エージェント実行へ同時に広がり、モデル単体の性能だけでなく「AIをどう動かし、つなぎ、守るか」が前景化した月だった。**

Only after Human Candidate Selection approval may these roles be translated to the SHA-bound selection decision and applied through the repository workflow.