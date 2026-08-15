# 2026-W33 Cross-Candidate Comparison Matrix v0.1

Status: **evidence-ready / Grok r3 reconciled / pre-selection**  
Issue: `2026-W33`  
Evidence run: `4ac76d074b415f0fb3106c88503f23c03fa990aaef0e8dbbf0707a1616c18bd3`  
Grok r3 review: `sources/2026-W33/grok/reviews/x-trend-sensor-2026-08-15-v0.4-r3-review.md`  
Candidate Selection Gate: **pending**

This matrix supersedes `candidate-matrix-pre-r3-v0.1.md`. It compares the accepted Base Intake/Evidence state after the final r3 trend-sensor reconciliation. It does not itself select the issue contents.

## Comparison vocabulary

### Verification depth
- `V3_PRIMARY_VERIFIED`: first-party/project source inspected; event identity and chronology are comparison-ready. Quantitative/vendor/project claims remain attributed.
- `V2_PRIMARY_PARTIAL`: durable first-party/project source exists, but claim-level review is incomplete.
- `V2_ABSTRACT_ONLY`: paper identity/chronology and abstract are available; full-paper method/result review has not been completed.
- `V1_INSPECT_REQUIRED`: source remains an index/discovery snapshot requiring item-level inspection.
- `V0_REJECTED_IDENTITY_OR_EVENT`: claimed identity/event failed primary-source reconciliation.

### Readiness
- `READY`: sufficient for cross-candidate comparison.
- `READY_WITH_CAVEAT`: comparison-ready with an explicit attribution/chronology boundary.
- `SUPPORTING`: verified evidence best consumed by another candidate.
- `WATCH`: valid secondary signal without enough reason for substantive standalone coverage.
- `HOLD`: preserve but do not promote without additional work.
- `EXCLUDE_W33`: r3/discovery claim failed primary-source reconciliation or lacks a valid W33 event.

## Comparison matrix

| Candidate / evidence unit | Objective W33 relation | Verification | X / r3 result | Readiness | Remaining boundary |
|---|---|---|---|---|---|
| **GPT-5.6-Cyber / Daybreak Red** | OpenAI Aug 10 model/access event | `V3_PRIMARY_VERIFIED` | Not dependent on Grok ranking | `READY_WITH_CAVEAT` | Benchmark, vulnerability, capability-threshold and reduced-refusal statements remain OpenAI claims; controlled-access context must travel with them |
| **SGLang v0.5.17** | project release Aug 8 | `V3_PRIMARY_VERIFIED` | not separately ranked by r3 | `READY_WITH_CAVEAT` | Performance/resource/hardware claims remain project-reported; substantial overlap with vLLM/FlashInfer |
| **vLLM v0.27.0–v0.27.1** | project series Aug 10–11 | `V3_PRIMARY_VERIFIED` | not separately ranked by r3 | `READY_WITH_CAVEAT` | Project-reported gains; consolidate with adjacent serving-stack work rather than duplicate it |
| **FlashInfer v0.6.17** | project release Aug 11 | `V3_PRIMARY_VERIFIED` | not separately ranked by r3 | `READY_WITH_CAVEAT` | Production-readiness/kernel-performance claims remain project-reported; overlaps vLLM/SGLang |
| **Transformers v5.15.0 / Muse Glimmer** | HF release Aug 10 | `V3_PRIMARY_VERIFIED` for HF event | r3 `ACCEPT_TREND_LEAD` | `READY_WITH_CAVEAT` | Exact Meta-origin announcement and model-level claims are not upgraded beyond the verified HF project record |
| **ComfyUI v0.31.0–v0.33.1 media integrations** | releases Aug 8–13; material v0.32.0 integrations Aug 11 | `V3_PRIMARY_VERIFIED` for ComfyUI event | r3 Lane D `CANDIDATE_NOT_SELECTED`; LTX claim reframed to integration/adoption | `WATCH / READY_WITH_CAVEAT` | Does not prove same-week underlying model launch, quality, or broad X momentum |
| **Daybreak Cyber Partner Program expansion** | OpenAI Aug 10 | `V3_PRIMARY_VERIFIED` | n/a | `SUPPORTING` | Same underlying Daybreak deployment story; do not double-count as separate article |
| **Daybreak on AWS** | first-party feed Aug 11 | `V2_PRIMARY_PARTIAL` | n/a | `SUPPORTING/HOLD` | Deployment chronology is plausible/first-party, but detailed mechanics were not claim-level reviewed |
| **OpenAI Ultrafast mode for GPT-5.6 Sol** | first-party feed Aug 13 | `V2_PRIMARY_PARTIAL` | n/a | `HOLD` | Feed reports up-to-14x / up-to-750-output-tok/s; full article/API details were not available to this review, so do not promote performance specifics yet |
| **TensorRT-LLM v1.3.0rc24** | prerelease Aug 12 | `V2_PRIMARY_PARTIAL` | n/a | `HOLD` | Release-candidate status, known issues, and heavy overlap with stronger serving candidates |
| **llama.cpp W33 rolling releases** | many builds inside W33 | `V2_PRIMARY_PARTIAL` | n/a | `WATCH/HOLD` | High-frequency stream with no single dominant event; preserve selected reasoning/recurrent-state changes only as context |
| **W33 retained paper pool** | arXiv submissions inside W33 | `V2_ABSTRACT_ONLY` | Lane I `NONE_FOUND_CONFIRMED` for X momentum; Lane D no selected X trend | `HOLD` | No paper has full-paper evidence; abstract-level author claims cannot support a feature/deep dive |

## r3 rejection / exclusion ledger

Primary-source reconciliation overrides the Trend Sensor ranking. The following r3 identities/events must not be introduced into Candidate Selection merely because Grok ranked or retained them:

| r3 item | Disposition |
|---|---|
| `Grok 4.6` | `EXCLUDE_W33` — exact first-party identity/launch not corroborated; first-party material instead supported Grok 4.5 chronology |
| `Qwen3.8-27B` | `EXCLUDE_W33` — community packaging does not establish exact official model identity/release |
| `Nemotron 3.5 Lightning` | `EXCLUDE_W33` — exact first-party model/release not established |
| `DeepSeek-V4-Pro-0813` | `EXCLUDE_W33` as an Aug-13 event — DeepSeek-V4-Pro exists, but the claimed `0813` W33 release/update was not established |
| `Anthropic August 2026 Risk Report` | `EXCLUDE_W33` — Risk Reports are a real policy mechanism, but the alleged Aug-14 report/event was not established |

Other r3 candidate-pool names such as MAGI-2 Preview / GLM-5.3 do not gain candidate status unless independently supported by the accepted Base/Evidence path.

## Cross-candidate consolidation groups

### A. Controlled cyber capability / deployment boundary
- GPT-5.6-Cyber / Daybreak Red — comparison-ready core
- Daybreak Cyber Partner Program — verified supporting evidence
- Daybreak on AWS — supporting deployment chronology, still partial

Editorial value: the technically interesting unit is not only a stronger cyber model but the combination of specialized capability, reduced refusal behavior for authorized use, differentiated Blue/Red access, and governed distribution.

### B. Serving stack co-evolution
- SGLang v0.5.17
- vLLM v0.27.0–v0.27.1
- FlashInfer v0.6.17
- TensorRT-LLM v1.3.0rc24 — HOLD
- llama.cpp rolling releases — WATCH/HOLD
- optional future paper depth: OpScale / LLMVisor / CommitKV, currently abstract-only

Editorial value: avoid three release-note summaries. The shared story is serving/runtime layers adapting together to new multimodal/MoE architectures, cache/session behavior, kernel formats and control-plane requirements.

### C. Model ecosystem / multimodal integration
- Transformers v5.15.0 / Muse Glimmer — r3 accepted trend lead with HF evidence
- ComfyUI W33 media integrations — verified integration/adoption signal
- LTX 2.5 / Qwen-Image 3.0 Pro / Grok-Imagine-Image-2.0 — mention only as ComfyUI-supported names unless their own primary chronology is separately verified

r3 Lane D result prevents overstating this as a major X-wide image-generation trend.

### D. Memory / multi-agent research
The retained paper inventory contains relevant memory, KV-cache and multi-agent work, including LycheeMemory V2, StreamTTT and CommitKV. r3 Lane I found no strong distinct W33 X momentum, and the papers remain abstract-only. A dedicated section is therefore not justified without a deliberate full-paper promotion.

## Paper-review decision

Two targeted full-review candidates were considered for additional breadth (memory and video generation), but durable full-text/PDF access was not available in the current Evidence execution environment. They therefore remain `V2_ABSTRACT_ONLY / HOLD`. This is a valid negative pipeline outcome; the issue does not need a Paper Watch item merely to fill a category.

## Comparison conclusions

1. **The strongest standalone W33 event is GPT-5.6-Cyber / Daybreak**, because both the technical capability claim and the controlled deployment boundary are first-party and date-specific, with claim attribution preserved.
2. **SGLang, vLLM and FlashInfer form one coherent systems movement.** Their overlap is an editorial advantage if synthesized, but a duplication problem if written as independent release summaries.
3. **Muse Glimmer survives r3; several higher-ranked r3 names do not.** This is exactly why Trend Sensor output cannot substitute for primary-source Evidence.
4. **ComfyUI provides real W33 media-generation integration evidence, but r3 does not support elevating it to a major X-trend claim.** Short section/watchlist treatment is better matched to the evidence.
5. **No paper is selection-ready at full-review depth.** The correct outcome is to omit Paper Watch unless later architecture makes a specific paper sufficiently material to justify a new review pass.
6. The pool is now ready for an explicit **Candidate Selection proposal**, but `candidate_selection` remains a human gate and must not be marked passed automatically.
