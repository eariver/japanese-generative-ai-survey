# 2026-W32 Cross-Candidate Comparison Matrix

Status: pre-editorial comparison  
Issue: `2026-W32`  
Editorial structure: **not decided**

This matrix compares the 35 screening records before any article or section architecture is selected. It is not a ranking and does not imply inclusion.

## Comparison vocabulary

### Temporal position
- `MAIN_EVENT`: objective event/publication falls inside the main collection window.
- `PRE_WINDOW_RELEVANCE`: artifact predates the window but W32 relevance or community momentum may justify consideration.
- `POST_CUTOFF`: objective event or collected reaction is after the editorial cutoff.
- `CHRONOLOGY_ONLY`: useful as an event record even if weak as a weekly article.
- `TIMING_UNRESOLVED`: discovery note and primary chronology are not yet reconciled.

### Verification depth
- `V3_PRIMARY_SCREENED`: durable primary source captured; core event identity and chronology are usable for comparison.
- `V2_PRIMARY_NEEDS_DEEP_REVIEW`: primary paper/docs captured but methodology, benchmark, or important claims need deeper reading.
- `V1_DISCOVERY_ONLY`: plausible discovery remains but primary evidence for the collected W32 claim is incomplete.
- `V0_NOT_CONFIRMED_OR_CONTRADICTED`: the collected W32 claim is not supported by the primary sources found so far, or a different event explains it better.

### Comparison readiness
- `READY`: sufficient evidence to compare against other candidates; this does **not** mean selected for publication.
- `READY_WITH_CAVEAT`: comparable, but timing, claim boundaries, or social evidence must remain explicit.
- `DEEP_REVIEW`: retain, but a paper/methodology review is needed before quantitative use.
- `HOLD`: do not promote until a specific evidence gap is resolved.
- `WATCH`: retain as secondary context without forcing promotion.
- `REJECT_W32`: preserve for provenance but do not treat as a valid W32 candidate under current evidence.

## Matrix

| ID | Kind | Objective timing / W32 relation | Verification | X / community evidence | Overlap / relation | Readiness | Remaining work |
|---|---|---|---|---|---|---|---|
| `openai-astra` | research/model event | 2026-08-01; `MAIN_EVENT` | V3 | Medium, all representative posts main-window | Same underlying model as Astra cyber late candidate | READY_WITH_CAVEAT | Independent mathematical expert assessment; model-vs-human attribution |
| `qwen3.8-max-preview` | model preview | Preview debuted 2026-07-19; `PRE_WINDOW_RELEVANCE` via W32 agent/coding/open-weight discussion | V3 | Medium; 3 main + 1 follow-up | Qwen family; separate from Image 3.0 and speculative 27B item | READY_WITH_CAVEAT | Durable technical report/model card; exact weights/license; independent benchmark harness |
| `deepseek-v4-flash-0731` | model/API update + weights | 2026-07-31; immediately pre-window; collected X reaction is post-cutoff | V3 | Medium but `POST_CUTOFF` only in Reaction Pass | Links naturally to inference/serving stack | READY_WITH_CAVEAT | Independent benchmark reproduction; keep API/weights chronology separate if needed |
| `minimax-h3` | multimodal/video model | 2026-07-31; `PRE_WINDOW_RELEVANCE`, local ecosystem accelerates around cutoff | V3 | High overall; 1 main + 3 post-cutoff | Strong overlap with SGLang v0.5.17 serving support | READY_WITH_CAVEAT | Exact weights timestamp; independent quality tests; representative VRAM/perf; core-model vs prompt-rewriter artifacts |
| `kimi-k3` | open-weight multimodal agentic model | July 2026 release; `PRE_WINDOW_RELEVANCE`, W32 local-inference signal | V3 | Medium; viral main signal + post-cutoff caveats | Strong overlap with SGLang v0.5.17; Kimi retrospective; alleged Copilot integration | READY_WITH_CAVEAT | Reproduce/inspect pure-C low-memory engine before treating ~8.24 GB claim as fact |
| `claude-tag` | persistent team-agent product/ecosystem | Product announced 2026-06-23; W32 value is ecosystem/governance reaction | V3 | Medium; 4 main-window posts | Related to broader agent-productization theme, not a W32 launch | READY_WITH_CAVEAT | Verify any specific Aug 3 migration/default-switch claim before using it |
| `mistral-shieldstral` | safety paper/model | 2026-07-28; `PRE_WINDOW_RELEVANCE` | V2 | Low–Medium | Safety cluster with SparSEEty/PRWeaver/OpenAI cyber | DEEP_REVIEW | Paper review for methodology/benchmarks; model-card/license if separately released |
| `grok-imagine-video-1.5` | video model | GA 2026-06-16; claimed W32 resurgence not substantiated | V3 for product, V0 for W32 momentum | `INSUFFICIENT_X_EVIDENCE` | Separate from xAI Image items | REJECT_W32 | None unless new W32-specific evidence appears |
| `qwen-image-3.0` | image model | W32 availability/integration signal; detailed chronology not yet normalized here | V1–V2 | Low–Medium; main signal mostly official, independent testing sparse | Qwen family but technically distinct from Qwen3.8-Max | WATCH | Capture durable Alibaba primary model page and exact release/preview chronology |
| `nvidia-voicechat` | voice model | Announced at GTC 2026 in March; not an August launch | V3 | Not relevant for W32 | None | REJECT_W32 | Preserve as false-positive provenance |
| `meta-muse-code-spark-1.2` | coding/model discovery note | Initial note said 2026-08-05; current Meta primary search finds Muse Spark 1.1 (Jul 9), not the collected `Muse Code + Spark 1.2` event | V0 | None collected | Possible conflation with Muse Spark 1.1 / Meta agentic coding capabilities | HOLD | Find exact Meta primary URL if this event truly exists; otherwise reclassify/reject |
| `openai-gpt-5.6-w32-update` | model availability/update discovery note | GPT-5.6 GA is 2026-07-09; no separate Aug 6 OpenAI update confirmed in current primary search | V0 for claimed W32 update; V3 for Jul 9 GA | None collected | Broadly overlaps model/coding landscape but not a new W32 event yet | HOLD | Identify exact Aug event/source or reclassify as earlier chronology |
| `kimi-k3-github-copilot` | model integration discovery note | Claimed Aug 6 GA not confirmed on GitHub Changelog in current primary search | V1 | None collected | Same Kimi K3 artifact; avoid double counting unless integration confirmed | HOLD | Exact GitHub changelog/docs URL required |
| `github-copilot-cloud-agent-w32` | coding-agent product update | Initial W32 note conflicts with primary changelog chronology; several relevant features are June/July | V1 | None collected | Agent/coding cluster | HOLD | Identify the exact Aug update rather than aggregating prior cloud-agent features |
| `google-agent-evaluation-flywheel` | agent-evaluation methodology/skill | Google Cloud docs updated 2026-07-24; W32 may be discovery/relevance rather than a new release | V3 for existence | None collected | Evaluation methodology cluster; related conceptually to paper/eval coverage | READY_WITH_CAVEAT | Decide temporal relevance; inspect skill/repo if implementation details will be described |
| `anthropic-skill-plugin-security-scanning` | agent security product discovery note | Claimed W32 event not confirmed in current Anthropic primary search | V1 | None collected | Agent-security cluster | HOLD | Exact Anthropic release-note/docs source required |
| `openai-external-cyber-eval-boundary-event` | cyber evaluation/security incident | Official OpenAI/Hugging Face evaluation incident published 2026-07-21; collected Aug framing remains unresolved | V3 for Jul 21 incident; V1 for claimed W32 framing | None collected | Safety/cyber cluster; distinguish from Astra Critical claim | WATCH | Reconcile original discovery note with Jul 21 incident; only promote if W32-specific development exists |
| `github-spark-retirement` | product retirement discovery note | No GitHub Spark retirement found; GitHub did announce other retirements (e.g. Models, Copilot Billing Preview) | V0 | None | Possible name/event conflation | REJECT_W32 | Preserve provenance; restore only with exact GitHub primary source |
| `claude-opus-4.1-api-retirement` | API/model retirement discovery note | No current Anthropic primary retirement notice captured | V1 | None | Chronology-only if confirmed | HOLD | Anthropic model-deprecation source with retirement date required |
| `xai-grok-voice-think-fast-2.0-alias-switch` | alias/default switch | Announced Jul 29; `grok-voice-latest` routes to Think Fast 2.0 starting 2026-08-05 | V3 | None required | Chronology-oriented product/API event | READY | No deep work needed unless model differences are discussed |
| `xai-imagine-image-2.0` | image model/update discovery note | Claimed Aug 7 item not found in current xAI release notes/news; xAI has earlier Imagine image updates | V1 | None | Image generation cluster | HOLD | Exact xAI primary announcement required |
| `sglang-v0.5.17` | OSS serving release | 2026-08-08; `POST_CUTOFF` | V3 | Not separately collected in Reaction Pass | Directly integrates Kimi K3 and MiniMax H3; strongest systems bridge between those candidates | READY_WITH_CAVEAT | Treat as Late Breaking; optionally inspect Kimi/H3 cookbooks for deployment specifics |
| `paper-livemem` | paper | arXiv 2608.02515, 2026-08-03; `MAIN_EVENT` | V2 | None | Memory/long-running inference; distinct from serving papers | DEEP_REVIEW | Full technical review recommended before using evaluation claims |
| `paper-llm-serving-in-the-wild` | paper | arXiv 2608.03036, 2026-08-04; `MAIN_EVENT` | V2 | None | Systems/serving cluster; descriptive empirical study | DEEP_REVIEW | Targeted full review of dataset construction, repository sampling, taxonomy; less need for line-by-line math review |
| `paper-when-does-disaggregation-pay` | paper | arXiv 2608.03741, 2026-08-04; `MAIN_EVENT` | V2 | None | Systems/serving cluster; complements SGLang and serving-in-the-wild | DEEP_REVIEW | Full review required because throughput gains depend on simulation assumptions/hardware model |
| `paper-sparseety` | paper | arXiv 2608.02995, 2026-08-04; `MAIN_EVENT` | V2 | None | Safety/security + serving optimization | DEEP_REVIEW | Full review required: threat model, TDX assumptions, oracle construction, BLEU metric and attack practicality |
| `paper-prweaver` | paper | arXiv 2608.02693, 2026-08-03; `MAIN_EVENT` | V2 | None | Agent/code-review security | DEEP_REVIEW | Full review required for benchmark construction, attack validity and review-context conditions |
| `paper-from-social-coding-to-agentic-coding` | paper | arXiv 2608.03585, 2026-08-04; `MAIN_EVENT` | V2 | None | Agent adoption / OSS sociology; complements Claude Tag/open-agent governance theme | DEEP_REVIEW | Full review required before using quantitative conclusions because results come from multi-agent simulation initialized with real GitHub data |
| `claude-opus-5-community-demos` | social use-case signal | Underlying model available in GitHub Copilot Jul 24; W32 signal is downstream demos | V2 for underlying model; social evidence not normalized in Reaction Pass | v0.2 social signal only | Agent/coding cluster | WATCH | Focused Reaction Evidence pass only if this is promoted beyond a small community note |
| `local-ai-worlds-fair-track` | community theme | Recording/event resurfacing around W32 per v0.2 | V1 | v0.2 social signal only | Broad Local AI narrative; overlaps Kimi/H3 without being a model event | WATCH | Official event/video source and dates required before factual treatment |
| `grok-build-harness-open-source` | agent harness claim | xAI Grok Build beta/model are official from May; claimed Aug 7 open-source-harness event not yet verified | V1 | v0.2 social signal | Agent harness theme | HOLD | Exact official repo/license/event source required |
| `kimi-k3-open-weight-retrospective` | social narrative | No distinct new artifact; community retrospective | V3 for underlying model, narrative-only for candidate | v0.2 social signal | Duplicate context around Kimi K3 | WATCH | Merge as context if useful; not standalone technical event |
| `repowise-agent-tool-efficiency` | agent tooling discovery | W32 social/tool claim not primary-screened | V1 | v0.2 social signal | Agent harness/context-efficiency theme | HOLD | Actual repo/docs, ownership, method and numeric savings claims |
| `openai-astra-cyber-critical-late` | late-breaking safety claim | Claimed post-cutoff Astra cyber Critical concern; current OpenAI primary search has not located the matching public announcement | V1 | v0.2 Late Breaking signal | Same Astra model as math/science event, but separate safety claim if confirmed | HOLD | Exact OpenAI primary source or Preparedness artifact required; do not infer from GPT-5.6 cyber material |
| `qwen3.8-27b-local-expectation-late` | late-breaking social claim | Speculative future weights/local performance claim | V1 | Social-only | Qwen3.8 family; high duplication risk | HOLD | Official Qwen confirmation of model/weights plus independent local measurements |

## Cross-candidate overlap groups

These groups are **comparison aids, not article bundles**.

### A. Scientific reasoning / frontier capability
- `openai-astra`
- `openai-astra-cyber-critical-late` (only if primary confirmation emerges)

### B. Open-weight frontier models and local/serving ecosystem
- `qwen3.8-max-preview`
- `deepseek-v4-flash-0731`
- `minimax-h3`
- `kimi-k3`
- `qwen3.8-27b-local-expectation-late`
- `sglang-v0.5.17`
- `local-ai-worlds-fair-track`
- `kimi-k3-open-weight-retrospective`

### C. Agent / coding productization and harnesses
- `claude-tag`
- `claude-opus-5-community-demos`
- `github-copilot-cloud-agent-w32`
- `google-agent-evaluation-flywheel`
- `grok-build-harness-open-source`
- `repowise-agent-tool-efficiency`
- `meta-muse-code-spark-1.2`
- `kimi-k3-github-copilot`

### D. Multimodal media generation
- `minimax-h3`
- `qwen-image-3.0`
- `grok-imagine-video-1.5`
- `xai-imagine-image-2.0`
- `nvidia-voicechat`

### E. Serving / inference systems
- `sglang-v0.5.17`
- `paper-llm-serving-in-the-wild`
- `paper-when-does-disaggregation-pay`
- `paper-livemem`
- `paper-sparseety`

### F. Safety / security / evaluation
- `mistral-shieldstral`
- `paper-sparseety`
- `paper-prweaver`
- `anthropic-skill-plugin-security-scanning`
- `openai-external-cyber-eval-boundary-event`
- `openai-astra-cyber-critical-late`

### G. Chronology / availability / retirement
- `xai-grok-voice-think-fast-2.0-alias-switch`
- `claude-opus-4.1-api-retirement`
- `github-spark-retirement`
- `openai-gpt-5.6-w32-update`

## Primary verification findings added during matrix construction

- Meta primary material currently supports Muse Spark 1.1 (Jul 9), not the collected `Muse Code + Muse Spark 1.2` W32 event.
- OpenAI primary material currently places GPT-5.6 general availability on Jul 9; a separate Aug 6 update from the discovery note has not yet been located.
- Google Cloud documentation confirms the Agent Platform GenAI Evaluation Service flywheel skill and was updated Jul 24.
- xAI release notes confirm `grok-voice-think-fast-2.0` announcement on Jul 29 and the `grok-voice-latest` alias switch effective Aug 5.
- SGLang v0.5.17 was released Aug 8 and explicitly adds day-0 support for both Kimi K3 and MiniMax H3.
- OpenAI has a Jul 21 primary report on a Hugging Face security incident during model evaluation; this does not by itself verify the separately collected W32/Aug boundary-event framing.
- GitHub primary changelog search did not substantiate a GitHub Spark retirement matching the collected W32 note.

## Next comparison step

Before deciding the issue architecture:

1. Resolve `HOLD` items only where the candidate could materially change the issue balance.
2. Perform full/targeted paper reviews according to `sources/2026-W32/paper-review-plan.md`.
3. Recompute the matrix after those reviews.
4. Only then decide which candidates combine into articles, which remain short notes/watchlist, and which are excluded.
