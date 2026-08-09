# 2026-W32 Cross-Candidate Comparison Matrix v0.2

Status: **evidence-ready pre-editorial comparison**  
Issue: `2026-W32`  
Editorial structure: **not decided**

This matrix supersedes `candidate-matrix.md` for current comparison state. It does not rank articles or imply inclusion.

## Comparison vocabulary

### Temporal position
- `MAIN_EVENT`: objective event/publication falls inside the main collection window.
- `PRE_WINDOW_RELEVANCE`: artifact predates the window, but W32 technical/community relevance may justify consideration.
- `POST_CUTOFF`: objective event is after the editorial cutoff and belongs to Late Breaking/follow-up handling.
- `CHRONOLOGY_ONLY`: valid event whose primary value is chronology/small update coverage.
- `TIMING_UNRESOLVED`: chronology remains unresolved.

### Verification depth
- `V4_FULL_REVIEWED`: paper/methodology reviewed beyond abstract/metadata; claims and limitations have locators/boundaries.
- `V3_PRIMARY_SCREENED`: durable primary source captured; core event identity/chronology are comparison-ready.
- `V2_PRIMARY_NEEDS_DEEP_REVIEW`: primary source exists but key methodology/claims still need deeper review.
- `V1_DISCOVERY_ONLY`: discovery remains but the specific W32 claim lacks adequate primary evidence.
- `V0_NOT_CONFIRMED_OR_CONTRADICTED`: collected W32 claim is unsupported or explained by a different event.

### Comparison readiness
- `READY`: sufficient evidence for cross-candidate comparison with no major unresolved identity/timing issue.
- `READY_WITH_CAVEAT`: comparison-ready, but explicit claim/timing/source boundaries must travel with it.
- `HOLD`: do not promote until a specific evidence gap is resolved.
- `WATCH`: secondary/contextual signal; retain without forcing promotion.
- `REJECT_W32`: preserve provenance, but do not treat as a valid new W32 candidate.

## Matrix

| ID | Kind | Objective timing / W32 relation | Verification | X / community evidence | Readiness | Remaining boundary |
|---|---|---|---|---|---|---|
| `openai-astra` | research/model event | 2026-08-01 `MAIN_EVENT` | V3 | Medium; all representative posts main-window | READY_WITH_CAVEAT | Independent mathematical assessment; model-vs-human contribution |
| `qwen3.8-max-preview` | model preview | 2026-07-19 `PRE_WINDOW_RELEVANCE` | V3 | Medium; 3 main + 1 follow-up | READY_WITH_CAVEAT | Technical report/architecture, weights/license, benchmark harness |
| `deepseek-v4-flash-0731` | model/API update + weights | 2026-07-31, immediate pre-window | V3 | Medium but Reaction Pass is post-cutoff only | READY_WITH_CAVEAT | Independent benchmark reproduction |
| `minimax-h3` | omni-modal generation model | 2026-07-31 `PRE_WINDOW_RELEVANCE`; local ecosystem accelerates around cutoff | V3 | High overall; 1 main + 3 post-cutoff | READY_WITH_CAVEAT | Exact weight timestamp, independent quality/VRAM tests, core-vs-ecosystem artifact boundary |
| `kimi-k3` | open-weight multimodal agentic model | July release; W32 local-inference signal | V3 | Medium; main viral signal + follow-up caveats | READY_WITH_CAVEAT | Reproduce/inspect low-memory pure-C community engine before factualizing resource claims |
| `claude-tag` | persistent team-agent product/ecosystem | 2026-06-23 `PRE_WINDOW_RELEVANCE` | V3 | Medium; 4 main-window posts | READY_WITH_CAVEAT | Any claimed Aug-3 migration/default mechanics require separate primary support |
| `mistral-shieldstral` | safety paper/model | 2026-07-28 `PRE_WINDOW_RELEVANCE` | **V4** | Low–Medium | READY_WITH_CAVEAT | Author-reported benchmark setup; independent/adversarial validation absent |
| `grok-imagine-video-1.5` | video model | GA 2026-06-16; W32 resurgence unsubstantiated | V3 product / V0 W32 momentum | `INSUFFICIENT_X_EVIDENCE` | REJECT_W32 | Reopen only with W32-specific technical evidence |
| `qwen-image-3.0` | image model | W32 availability/integration signal, weak independent testing | V1–V2 | Low–Medium | WATCH | Durable primary chronology and deeper independent testing |
| `nvidia-voicechat` | voice model | March 2026, not Aug launch | V3 | Not W32-relevant | REJECT_W32 | False-positive provenance only |
| `meta-muse-code-spark-1.2` | alleged coding/model event | alleged 2026-08-05 not found; verified related Spark 1.1 is Jul 9 | V0 | None | REJECT_W32 | Reopen only with exact Meta primary source |
| `openai-gpt-5.6-w32-update` | alleged model availability update | GPT-5.6 GA is Jul 9; distinct Aug event unresolved | V1 | None | HOLD | Exact Aug OpenAI event/source or reclassify as earlier chronology |
| `kimi-k3-github-copilot` | alleged integration | claimed Aug integration not yet primary-confirmed | V1 | None | HOLD | Exact GitHub Changelog/docs source |
| `github-copilot-cloud-agent-w32` | alleged coding-agent update | collected W32 shorthand conflicts with June/July chronology | V1 | None | HOLD | Identify exact Aug update rather than aggregate old features |
| `google-agent-evaluation-flywheel` | agent-evaluation methodology | docs updated Jul 24; W32 may be relevance rather than launch | V3 | None | READY_WITH_CAVEAT | Temporal relevance; implementation details only if promoted |
| `anthropic-skill-plugin-security-scanning` | security-review context | actual Claude Code Automated Security Reviews date Mar 16 | V3 for old artifact / V0 W32 claim | None | REJECT_W32 | Can remain background context, not new W32 event |
| `openai-external-cyber-eval-boundary-event` | safety/evaluation incidents | **2026-08-04 `MAIN_EVENT`** | **V3** | no focused Reaction Pass | **READY_WITH_CAVEAT** | Keep reduced-safeguard/misconfiguration context; do not call production sandbox escape |
| `github-spark-retirement` | alleged product retirement | no matching primary event found | V0 | None | REJECT_W32 | Reopen only with exact GitHub primary source |
| `claude-opus-4.1-api-retirement` | alleged retirement | primary retirement notice still unresolved | V1 | None | HOLD | Exact Anthropic deprecation source/date |
| `xai-grok-voice-think-fast-2.0-alias-switch` | API alias/default switch | announced Jul 29; alias switch effective Aug 5 | V3 | None required | READY | Chronology/small-update candidate |
| `xai-imagine-image-2.0` | alleged image-model event | alleged Aug 7 event not found in xAI primary material | V0 | None | REJECT_W32 | Reopen only with exact xAI primary source |
| `sglang-v0.5.17` | OSS serving release | **2026-08-08 `POST_CUTOFF`** | **V3** | not separately collected | **READY_WITH_CAVEAT** | Late Breaking; model-specific deployment claims from official release/cookbooks |
| `paper-livemem` | memory/inference paper | 2026-08-03 `MAIN_EVENT` | **V4** | none | READY_WITH_CAVEAT | Lossy state, finite tested horizon, author-reported benchmarks |
| `paper-llm-serving-in-the-wild` | empirical serving paper | 2026-08-04 `MAIN_EVENT` | **V4 targeted** | none | READY_WITH_CAVEAT | Python/public-GitHub sampling; repo counts ≠ market share |
| `paper-when-does-disaggregation-pay` | serving-systems paper | 2026-08-04 `MAIN_EVENT` | **V4** | none | READY_WITH_CAVEAT | Simulation/component validation, hardware/workload-dependent gains |
| `paper-sparseety` | serving/security paper | 2026-08-04 `MAIN_EVENT` | **V4** | none | READY_WITH_CAVEAT | Architecture/threat-model-specific side channel; not generic TDX/sparsity failure |
| `paper-prweaver` | coding-agent security paper | 2026-08-03 `MAIN_EVENT` | **V4** | none | READY_WITH_CAVEAT | 10-repo mostly-Python benchmark; synthesized executable attack chains |
| `paper-from-social-coding-to-agentic-coding` | socio-technical simulation paper | 2026-08-04 `MAIN_EVENT` | **V4** | none | READY_WITH_CAVEAT | Multi-agent simulation; quantitative CA-vs-NoCA effects are not real-world causal measurements |
| `claude-opus-5-community-demos` | social use-case signal | underlying model predates window; W32 downstream demos | V2 underlying / social not normalized | v0.2 signal only | WATCH | Focused Reaction Pass only if promoted |
| `local-ai-worlds-fair-track` | community theme | event/recording resurfacing around W32 | V1 | v0.2 signal only | WATCH | Official event/video/date before factual use |
| `grok-build-harness-open-source` | coding-agent harness OSS | **2026-07-15 `PRE_WINDOW_RELEVANCE`** | **V3** | v0.2 W32 resurfacing only | READY_WITH_CAVEAT | Underlying open-source event is Jul 15; downstream GUI/extensions still social unless checked |
| `kimi-k3-open-weight-retrospective` | social narrative | no distinct new artifact | V3 underlying model | v0.2 signal | WATCH | Merge as context, not standalone event |
| `repowise-agent-tool-efficiency` | agent tooling discovery | W32 social/tool claim not primary-screened | V1 | v0.2 signal | HOLD | Repository/docs, method, numeric claims |
| `openai-astra-cyber-critical-late` | safety/capability event | **2026-08-07 `POST_CUTOFF`** | **V3** | v0.2 Late Breaking discovery | **READY_WITH_CAVEAT** | Say “cannot rule out Critical”, not “classified Critical”; keep separate from HF/AISI incidents |
| `qwen3.8-27b-local-expectation-late` | speculative local/model claim | post-cutoff social expectation | V1 | social-only | HOLD | Official model/weights/license + independent local measurements |

## Cross-candidate overlap groups

These are comparison aids, not article bundles.

### A. Astra / scientific reasoning / critical capability
- `openai-astra`
- `openai-astra-cyber-critical-late`

### B. Open-weight frontier models → serving ecosystem
- `qwen3.8-max-preview`
- `deepseek-v4-flash-0731`
- `minimax-h3`
- `kimi-k3`
- `sglang-v0.5.17`
- `grok-build-harness-open-source` (harness rather than model serving)

### C. Agent/coding systems, evaluation and social organization
- `claude-tag`
- `google-agent-evaluation-flywheel`
- `grok-build-harness-open-source`
- `paper-prweaver`
- `paper-from-social-coding-to-agentic-coding`
- unresolved: `github-copilot-cloud-agent-w32`, `kimi-k3-github-copilot`, `repowise-agent-tool-efficiency`

### D. Inference / serving architecture
- `sglang-v0.5.17`
- `paper-livemem`
- `paper-llm-serving-in-the-wild`
- `paper-when-does-disaggregation-pay`
- `paper-sparseety`

### E. Safety boundary moves from model to environment / infrastructure
- `openai-astra-cyber-critical-late`
- `openai-external-cyber-eval-boundary-event`
- `mistral-shieldstral`
- `paper-sparseety`
- `paper-prweaver`

### F. Multimodal/media generation
- `minimax-h3`
- `qwen-image-3.0`
- rejected W32 signals: `grok-imagine-video-1.5`, `xai-imagine-image-2.0`, `nvidia-voicechat`

## Verification-stage conclusions

1. **Priority-A discovery ambiguity is closed.** Meta Muse/Spark 1.2 and xAI Image 2.0 are unconfirmed and removed from the valid W32 pool; the Anthropic security-review item is a real March feature, not a W32 launch; Astra Critical cyber is a verified Aug-7 Late Breaking event.
2. **OpenAI Aug-4 third-party cyber evaluation incidents are a separate verified W32 event**, not a substitute for the Astra item and not the same as the Jul-21 Hugging Face incident.
3. **SGLang v0.5.17 is a verified Aug-8 Late Breaking release** and provides a concrete bridge from Kimi K3 / MiniMax H3 model releases into serving infrastructure.
4. **Seven paper/model-paper candidates now have full or targeted-full evidence reviews**, so their quantitative claims can be compared with explicit methodology and limitation boundaries.
5. Remaining HOLD items are no longer required to understand the broad W32 topic landscape; they can be resolved only if editorial selection later makes them material.

## Gate to next stage

The current pool is now sufficiently evidence-normalized to begin **Candidate Selection / Issue Architecture** without first promoting the remaining low-confidence HOLD records. Selection must still avoid equating source volume with importance and must preserve Main vs Post-Cutoff separation.