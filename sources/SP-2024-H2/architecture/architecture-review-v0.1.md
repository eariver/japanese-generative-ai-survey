# SP-2024-H2 Architecture Review v0.1

Status: **AWAITING HUMAN GATE 1 — ARCHITECTURE APPROVAL**

This is the first Human Gate for the 2024-H2 half-year retrospective Special. Reader-facing drafting has **not** started.

## 1. Coverage and reconstruction boundary

- Special: `SP-2024-H2`
- Coverage: `2024-07-01T00:00:00Z` through `2024-12-31T23:59:59Z`
- Retrospective as-of: `2026-08-14T11:35:00Z`
- Method: `CURATED_PRIMARY_SOURCE_RECONSTRUCTION`
- Community/X historical reaction research: disabled by half-year retrospective policy
- Source policy: first-party release, engineering, research, API changelog, or official model-card sources

This retrospective reconstructs what was objectively released, previewed, published, or made available during the covered half-year. Current living pages may be used to recover dated 2024 events, but later deprecation labels, replacement products, adoption outcomes, or 2025 ecosystem standardization are not back-projected into the 2024 record.

## 2. Intake, screening, and Evidence status

| Stage | Count |
|---|---:|
| Source intake candidates | 36 |
| Screened accept | 34 |
| Evidence records | 34 |
| Held | 2 |
| Rejected | 0 |
| Approx. objective chronology events | 34 |

The accepted set spans OpenAI, Meta, Anthropic, Google, Qwen/Alibaba, Mistral AI, DeepSeek, xAI, and Stability AI. It is intentionally material-event oriented rather than exhaustive.

### Limitations

1. The reconstruction does not claim exhaustive capture of every 2024-H2 model, paper, benchmark, integration, or regional rollout.
2. Vendor/project benchmark, performance, cost, adoption, and superlative statements remain attributed claims; they have not been independently reproduced.
3. Living pages are normalized to their explicitly dated 2024 event. Current deprecation/replacement status is metadata, not evidence that the same status existed in 2024.
4. Historical X/community reaction research is disabled. xAI is represented by its first-party product page, not social-observation evidence.
5. Two items are held rather than inferred: the December 12 Grok-2 product-update duplicate, and Gemini 2.0 Flash Thinking Experimental because a stable item-level release date/page was not retained in this intake.

## 3. Cross-period normalization and identity rules

- `SearchGPT prototype` (2024-07-25) and `ChatGPT search` (2024-10-31) are related but distinct lifecycle events. The 2024-12-16 logged-in-user expansion is a chronology detail.
- `o1-preview` / `o1-mini` (2024-09-12), full `o1` product availability / `o1 pro mode` (2024-12-05), and `o1-2024-12-17` API availability are distinct events.
- Llama 3.1, 3.2, and 3.3 are distinct family releases. Llama 3.2 vision and 1B/3B edge models must not be collapsed into one generic “Llama H2” event.
- Pixtral 12B and Pixtral Large are distinct releases.
- Gemini 2.0 Flash, Project Mariner, Jules, and Deep Research may share the December 11 announcement surface but are not the same artifact or availability state.
- Qwen2.5 and QwQ-32B-Preview are separate identities: broad foundation-model family vs experimental reasoning model.
- DeepSeek-V3’s 2024-12-26 availability is in scope. DeepSeek-R1’s public release is a 2025-H1 event and must not be back-projected into H2.
- “Open” is decomposed into open weights, code availability, license terms, hosted API availability, training/data transparency, and local/edge deployability.

## 4. Candidate Selection result

Candidate Selection is an internal checkpoint and is complete; it is **not** a Human Gate.

| Role | Count |
|---|---:|
| FEATURE_CORE | 9 |
| SECTION_CORE | 10 |
| SUPPORTING_EVIDENCE | 10 |
| CHRONOLOGY | 3 |
| PAPER_WATCH | 2 |
| **Total** | **34** |

### FEATURE_CORE story units

- Llama 3.1 405B / open frontier scale and system layer
- OpenAI o1-preview / inference-time reasoning
- Llama 3.2 / vision + edge bifurcation
- Claude 3.5 Sonnet computer use / GUI action surface
- Model Context Protocol / external-system protocol layer
- Gemini 2.0 Flash Experimental / native tool use and agentic model direction
- DeepSeek-V3 / large MoE efficiency and open-weight deployment
- Sora Turbo / video generation research-preview → product transition
- Qwen2.5 / broad open-weight family and model-size spectrum

## 5. Proposed editorial thesis

> 2024年後半は、生成AIの競争軸が「より大きい基盤モデル」だけでは説明できなくなり、推論時に計算を増やす reasoning、検索・GUI・外部データへ接続する action/tool layer、open-weight・小型化・quantizationによる deployment choice、音声・画像・動画を横断する multimodality へ分岐した半年だった。したがって本号はモデル順位表ではなく、model capability・inference-time compute・execution surface・deployment form・control boundaryを分離し、モデル単体から execution / deployment stack へ評価単位が移り始めた過程として再構成する。

The thesis is retrospective but not outcome-retroactive: later 2025 adoption of agent protocols or reasoning systems may motivate why the period matters, but cannot be written as if that later outcome was already established in 2024.

## 6. Proposed package architecture

| Order | Package | Type | Pages | Primary Evidence |
|---:|---|---|---:|---|
| 1 | 2024年後半の技術地図と読み方 | FRONTMATTER | 4 | — |
| 2 | Open-weight Frontierが「最大」から「選べる配備」へ | LEAD | 8 | Llama 3.1, Qwen2.5, Llama 3.2, DeepSeek-V3 |
| 3 | Inference-time Computeが競争軸になる | FEATURE | 8 | o1-preview, QwQ-32B-Preview |
| 4 | 回答から接続・操作へ | FEATURE | 8 | Claude computer use, MCP, Gemini 2.0 |
| 5 | Multimodalityが入力理解からRealtime・生成Mediaへ広がる | FEATURE | 8 | Qwen2-VL, Realtime API, Sora, Veo 2 |
| 6 | Small・Edge・Long Context | COMPARISON | 6 | GPT-4o mini, Ministral, quantized Llama 3.2 |
| 7 | Execution Surfaceの拡大にControlが追いつく | DEEP_DIVE | 5 | Contextual Retrieval, Mistral Moderation |
| 8 | Half-year Synthesis — Model単体からExecution / Deployment Stackへ | SECTION | 5 | cross-package synthesis |
| 9 | Detailed Chronology | WATCHLIST_CHRONOLOGY | 5 | all 34 accepted events |
| 10 | References and Evidence Notes | REFERENCES | 3 | all accepted primary sources |
|  | **Planned** |  | **60** | target 64 / hard max 96 |

### Why this grouping

The structure deliberately avoids a vendor-by-vendor or month-by-month digest. The cross-month comparison is the point of the half-year Special:

1. **Open/deployment** compares frontier scale, family breadth, local deployment and MoE efficiency as separate choices.
2. **Reasoning** isolates inference-time compute as a new axis rather than treating o1 as merely another model release.
3. **Action/connectivity** separates search, GUI action, protocol and native tool use instead of flattening them into “agents.”
4. **Multimodal/media** separates understanding, realtime transport, generation and action.
5. **Efficiency/edge** compares cost, memory, locality and long context rather than raw benchmark rank.
6. **Control/grounding** keeps retrieval, moderation and alignment evidence distinct from capability claims.

## 7. Primary/supporting Evidence by package

### Open/deployment
Primary: `meta-llama31`, `qwen25`, `meta-llama32`, `deepseek-v3`  
Supporting: `mistral-large2`, `mistral-ministral`, `meta-llama33`, `qwen25-coder`

### Reasoning
Primary: `oa-o1preview`, `qwen-qwq-preview`  
Supporting/chronology: `oa-o1mini`, `oa-o1-pro`, `oa-o1-api`

### Action/connectivity
Primary: `anthropic-computer-use`, `anthropic-mcp`, `google-gemini20`  
Supporting/chronology: `oa-searchgpt`, `oa-chatgpt-search`, `oa-realtime`, `xai-grok2`

### Multimodal/media
Primary: `qwen2-vl`, `oa-realtime`, `oa-sora`, `google-veo2`  
Supporting: `qwen2-audio`, `mistral-pixtral12`, `stability-sd35`, `mistral-pixtral-large`, `google-gemini20`

### Efficient/edge
Primary: `oa-gpt4omini`, `mistral-ministral`, `meta-llama32-quantized`  
Supporting: `meta-llama32`, `qwen25-turbo-1m`, `meta-llama33`

### Control/grounding
Primary: `anthropic-contextual-retrieval`, `mistral-moderation`  
Supporting/Paper Watch: `anthropic-alignment-faking`, `oa-deliberative-alignment`, `meta-llama31`

## 8. Chronology and claim boundaries requiring editorial discipline

- **Preview ≠ GA/product maturity.** o1-preview, computer use public beta, Gemini 2.0 experimental, SearchGPT prototype, and research prototypes must retain those labels.
- **Model ≠ product ≠ API.** o1’s September preview, December ChatGPT product availability, and December API snapshot are different objective events.
- **Tool access ≠ autonomous agent reliability.** Function calling, computer use, MCP, search, and native tool use expand action surfaces but do not by themselves establish reliable end-to-end agency.
- **Open weights ≠ open source.** License restrictions and source/data availability must be stated separately.
- **Context size ≠ effective retrieval/reasoning quality.** Qwen’s 1M context event is an availability/engineering fact, with project benchmark claims attributed.
- **Research evidence ≠ deployed-system guarantee.** Alignment faking and deliberative alignment belong in a bounded research/control section.
- **Later status ≠ event-time status.** Current pages marking Pixtral/Sora or other models deprecated cannot be written as if they were deprecated in 2024.

## 9. Half-year reclassification and cross-layer synthesis

The proposed architecture makes three retrospective reclassifications:

1. **Reasoning becomes an inference layer.** o1/QwQ are read less as isolated model families and more as evidence that inference-time compute became an explicit user/developer tradeoff.
2. **“Agent” is decomposed into execution primitives.** Search, computer control, tool calls and MCP represent different layers; Gemini 2.0 shows those layers beginning to converge, but prototypes remain prototypes.
3. **Open-model competition becomes deployment architecture.** Llama/Qwen/Mistral/DeepSeek are compared by size spectrum, architecture, license, edge/local feasibility and API availability, not a single open-vs-closed binary.

This yields the proposed half-year synthesis: by December 2024, the locus of differentiation had spread from training scale into inference, interfaces, external connectivity and deployment. That is the technical bridge into 2025-H1, while reliability, security, evaluation and reproducibility remain unresolved.

## 10. Held / excluded items

- **HOLD:** `xai-grok2-dec12` — December 12 Grok product/search/Aurora update duplicates the August Grok-2 model story. It can be recovered into chronology if a product-availability transition becomes necessary during drafting.
- **HOLD:** `google-flash-thinking-exp` — Google’s December retrospective identifies Flash Thinking Experimental, but this intake did not retain a stable item-level source/date. Do not infer a chronology date at Architecture stage.
- No items are permanently rejected in v0.1.

## 11. Human Gate 1 decision

Approval of this Architecture authorizes:

- reader-facing Draft Package preparation;
- package-level drafting against only the selected Evidence;
- later deterministic finalization toward Publication Preview.

Approval does **not** authorize changing the Evidence identities, collapsing preview/product/API distinctions, or importing 2025 outcomes as 2024 facts.

**Decision requested:** approve `SP-2024-H2 Architecture v0.1`, or request a material architecture change before drafting.
