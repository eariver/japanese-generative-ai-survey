# 2026-W33 Pre-Selection Comparison Matrix v0.1

Status: **EVIDENCE_REVIEWED / GROK_R3_PENDING**  
Issue: `2026-W33`  
Evidence run: `4ac76d074b415f0fb3106c88503f23c03fa990aaef0e8dbbf0707a1616c18bd3`  
Candidate Selection Gate: **not approved / not entered**

This is a pre-selection comparison aid built from the accepted Base Source Intake and Evidence run. It intentionally stops before Candidate Selection. The supplemental Grok r3 reconciliation remains mandatory before X-derived ranking, Lane D closure, Lane I closure, or final selection decisions.

## Comparison vocabulary

### Verification depth

- `V3_PRIMARY_VERIFIED`: first-party/project source inspected; event identity and chronology are comparison-ready. Vendor/project performance claims remain attributed.
- `V2_PRIMARY_PARTIAL`: first-party source or first-party feed exists, but claim-level review is incomplete.
- `V2_ABSTRACT_ONLY`: paper identity/chronology and abstract are available; methodology/results have not received full-paper review.
- `V1_INSPECT_REQUIRED`: source is an index/discovery snapshot and needs item-level inspection.

### Readiness

- `READY`: evidence is sufficient for cross-candidate comparison.
- `READY_WITH_CAVEAT`: comparison-ready, but a specific chronology/source/claim boundary must travel with it.
- `HOLD`: do not promote until the named evidence gap matters enough to resolve.
- `SUPPORTING`: verified material that should normally be merged into another candidate rather than counted as a separate story.
- `R3_PENDING`: candidate identity/ranking depends materially on the Grok r3 X-trend reconciliation.

## Candidate-ready Base Intake evidence

| Candidate | Objective W33 event | Verification | Readiness | Editorial comparison note |
|---|---|---|---|---|
| **GPT-5.6-Cyber / Daybreak Red** | OpenAI first-party release/access expansion, Aug 10 | `V3_PRIMARY_VERIFIED` | `READY_WITH_CAVEAT` | Strong safety/security candidate. Treat reduced refusals, cyber benchmark results, vulnerability findings, and Preparedness assessment as OpenAI claims. Controlled-access architecture is part of the technical story, not incidental policy context. |
| **SGLang v0.5.17** | project release, Aug 8 | `V3_PRIMARY_VERIFIED` | `READY_WITH_CAVEAT` | Material serving-stack release: Kimi K3/MiniMax-H3 support, Rust frontend, session-aware cache, DeepSeek-V4 MoE path. Quantitative gains remain project-reported. Overlaps heavily with vLLM/FlashInfer. |
| **vLLM v0.27.0–v0.27.1** | project series, Aug 10–11 | `V3_PRIMARY_VERIFIED` | `READY_WITH_CAVEAT` | Major serving release plus narrow patch. Kimi K3/Qwen3.5, PyTorch/Triton stack, FA4, DeepSeek-V4, Model Runner V2, fault tolerance and Rust control-plane work form one series. |
| **FlashInfer v0.6.17** | project release, Aug 11 | `V3_PRIMARY_VERIFIED` | `READY_WITH_CAVEAT` | MoE expert-parallel serving and Blackwell/Kimi K3/MiniMax-M3 kernel work. Best compared as a component of the same inference-stack movement as vLLM/SGLang. |
| **ComfyUI v0.31.0–v0.33.1 media integration series** | project releases, Aug 8–13; material additions in v0.32.0 | `V3_PRIMARY_VERIFIED` | `READY_WITH_CAVEAT / R3_PENDING` | Concrete W33 integration activity for Qwen-Image 3.0 Pro, LTX 2.5, Grok-Imagine-Image-2.0 and MiniMax-H3 fixes. This proves integration/adoption, not underlying model launch chronology or X momentum. |
| **Transformers v5.15.0 / Muse Glimmer model addition** | HF project release, Aug 10 | `V3_PRIMARY_VERIFIED` | `READY_WITH_CAVEAT / R3_PENDING` | HF release notes independently anchor Muse Glimmer as a new model addition and describe a dense 30B multimodal model. Exact Meta first-party announcement and W33 X momentum still belong to r3 reconciliation. |

## Verified supporting evidence

| Item | Verification | Role | Boundary |
|---|---|---|---|
| **Daybreak Cyber Partner Program expansion** | `V3_PRIMARY_VERIFIED` | `SUPPORTING` | Same Aug 10 deployment story as GPT-5.6-Cyber. Do not double-count as a second core candidate. Partner/customer outcome quotations are not independent validation. |

## High-interest HOLD pool

These records remain preserved and comparison-visible but were deliberately not upgraded to candidate-ready evidence in the Base pass.

| Item / group | Current depth | Why HOLD | Reopen condition |
|---|---|---|---|
| **OpenAI Ultrafast mode for GPT-5.6 Sol** | `V2_PRIMARY_PARTIAL` | First-party RSS item confirms title/date and summarizes up-to-14x / up-to-750-output-tok/s service-tier claims, but the full article was not available to the current claim-level review. | Inspect durable first-party article/API documentation before using performance or hardware-provider specifics as article claims. |
| **Daybreak models on AWS** | `V2_PRIMARY_PARTIAL` | First-party feed establishes Aug 11 deployment chronology; likely supporting material for Daybreak rather than a separate feature. | Inspect the underlying OpenAI/AWS first-party details if deployment mechanics become editorially material. |
| **TensorRT-LLM v1.3.0rc24** | `V2_PRIMARY_PARTIAL` | Broad model/media support and DeepSeek-V4-related work, but it is a release candidate with a substantial known-issues surface and overlaps the stronger serving-stack candidates. | Promote only if a distinct technical mechanism or hardware/runtime angle survives cross-candidate comparison. |
| **llama.cpp W33 rolling releases** | `V2_PRIMARY_PARTIAL` | High-frequency build stream; selected changes include reasoning-effort handling and recurrent-state work, but no single build currently dominates the week. | Promote a grouped chronology/system item only if r3 or later evidence shows distinct W33 significance. |
| **OpenAI builder guide / secondary first-party items** | `V2_PRIMARY_PARTIAL` | Useful supporting documentation but weaker as independent W33 events. | Promote only if it establishes a unique technical change not covered by a stronger candidate. |

## Paper pool: evidence boundary and targeted shortlist

The retained paper tasks are currently `V2_ABSTRACT_ONLY` and therefore `HOLD`. Their titles, dates, and abstract-level author claims are preserved, but they have **not** been promoted to full-paper evidence. No paper should become a headline/deep-dive solely from the abstract-level run.

If Candidate Selection later needs a paper-led deep dive, the strongest targeted-review shortlist from the current pool is:

| Paper | Lane | Why it may matter | Required before promotion |
|---|---|---|---|
| **Intern-S2-Preview: Scientific Agentic Foundation Model** (`2608.13505`) | scientific agents | Scientific multimodal reasoning/tool-use/long-horizon agent model | Full-paper architecture, training/evaluation setup and benchmark-boundary review |
| **LycheeMemory V2** (`2608.12990`) | agent memory | Long-term memory with semantic segment-level consolidation | Full method/retrieval-cost/quality trade-off review |
| **StreamTTT** (`2608.13416`) | streaming VLM / memory | Separates recent KV context from long-range fast-weight memory | Full training/evaluation and online-update boundary review |
| **CommitKV** (`2608.07855`) | agent serving / memory | Lifecycle-aware KV-cache compression for multi-turn agents | Full eviction/commit mechanism and benchmark setup review |
| **OpScale** (`2608.13499`) | serving | Operator-level provisioning/autoscaling rather than model-level scaling | Full system model, workload assumptions, SLO and cost evaluation review |
| **LLMVisor** (`2608.08382`) | serving | Real-time per-request latency attribution for multi-tenant serving | Full attribution model and evaluation/generalization review |
| **HPSD** (`2608.13205`) | video generation | Hybrid-policy self-distillation for unified text/image-to-video diffusion | Full objective/training/evaluation and baseline comparison review |
| **Fingerprinting Text-to-Image Diffusion Models via Collapsed Generation** (`2608.11732`) | image/security | Model fingerprinting via collapse-prone generation conditions | Full threat model, robustness and false-positive review |

Other retained papers remain available in the Evidence HOLD set and need not be discarded; this shortlist is only a prioritization aid for potential deep review.

## Cross-candidate overlap groups

### A. Cyber capability + controlled deployment

- GPT-5.6-Cyber / Daybreak Red — core candidate
- Daybreak Cyber Partner Program — supporting evidence
- Daybreak on AWS — supporting deployment chronology if verified further

Editorial question: whether the lead is the specialized model itself or the system-level pattern of granting stronger cyber capability through a controlled-access architecture.

### B. Inference stack co-evolution

- SGLang v0.5.17
- vLLM v0.27.0–v0.27.1
- FlashInfer v0.6.17
- TensorRT-LLM v1.3.0rc24 — HOLD
- selected llama.cpp rolling changes — HOLD
- optional paper depth: OpScale / LLMVisor / CommitKV

Editorial question: avoid three repetitive release summaries. Prefer one package about the stack adapting together to new model architectures, MoE, cache/session behavior, kernel paths and control-plane requirements.

### C. Model ecosystem / multimodal integration

- Transformers v5.15.0 / Muse Glimmer
- ComfyUI media integration series
- possible r3-resolved underlying artifacts: LTX 2.5, Qwen-Image 3.0 Pro, Grok-Imagine-Image-2.0, other Lane-D findings

Editorial question: separate **underlying model release** from **W33 integration/adoption event**. Do not infer the former from ComfyUI support.

### D. Memory / long-running agents

No Base-Intake paper has been full-reviewed yet. Current HOLD shortlist includes LycheeMemory V2, StreamTTT, CommitKV and multi-agent communication work. Grok r3 Lane I is still mandatory before deciding whether W33 had enough community momentum for a dedicated memory/multi-agent section.

## Grok r3 reconciliation bucket — not selection-ready

The following r2-derived items are **not eligible to influence final Candidate Selection until r3 supplies concrete identity/chronology/X traceability or explicitly drops them**:

- Muse Glimmer X momentum / exact Meta primary source
- Qwen3.8-27B identity
- Grok 4.6 identity/launch
- DeepSeek V4 Pro `0813` chronology
- Nemotron 3.5 Lightning exact model identity
- LTX 2.5 underlying release vs W33 integration/adoption
- Qwen3-TTS original release vs genuine W33 resurgence
- Gemini 3.7 Flash exact first-party launch
- DeepSeek Harness provenance and exact repositories/projects
- alleged Anthropic August 2026 Risk Report
- MAGI-2 Preview
- GLM-5.3
- Lane D targeted image-generation/editing pass
- Lane I targeted memory/multi-agent/retrieval pass

`INSUFFICIENT_X_TRACE`, `IDENTITY_UNRESOLVED`, `CHRONOLOGY_UNRESOLVED`, and negative lane results are valid r3 outcomes and must not be converted into weak candidates merely to fill coverage.

## Pre-selection conclusions

1. **Base Intake is sufficient to establish at least three technically coherent W33 packages before using X ranking:** controlled cyber access, inference-stack co-evolution, and multimodal/media integration activity.
2. **The inference candidates should probably be consolidated rather than published as three parallel release summaries.** Their strongest editorial value is the shared adaptation of serving/runtime layers to rapidly changing frontier model architectures.
3. **Muse Glimmer and ComfyUI media integrations remain intentionally caveated.** The Base layer verifies concrete project activity; r3 must still decide the X-trend chronology/importance and resolve underlying first-party identities.
4. **No paper has yet earned full-review depth.** Paper promotion should be demand-driven by Candidate Selection rather than by source volume.
5. **Candidate Selection remains pending.** This matrix does not authorize `SELECTION_COMPLETE` or Issue Architecture. First integrate/review Grok r3, update this comparison state, then present the actual Candidate Selection proposal for human approval.
