---
issue_id: "2026-W32"
evidence_type: technical-primary-source-screening
created_at: "2026-08-09T23:47:00+09:00"
status: screening-complete
social_evidence: "sources/2026-W32/evidence/social/x-community-reaction-normalized-v0.1.md"
---

# W32 Technical Evidence — Verified Candidates v0.1

This file records primary-source screening for the seven main candidates retained after Grok trend discovery. Technical facts, vendor claims, social observations, and pending claims are deliberately separated.

## Status vocabulary

- `VERIFIED_PRIMARY`: supported directly by a primary source.
- `VENDOR_CLAIM`: claimed by the vendor/author but not independently validated here.
- `SOCIAL_OBSERVATION`: observed on X; not a technical-fact proof.
- `PENDING`: requires further verification before publication.

---

## T1 — OpenAI Astra / Ten advances in mathematics and theoretical computer science

**Artifact / Event:** OpenAI publication describing ten mathematical/theoretical-CS results achieved by an internal Astra model.  
**Event date:** 2026-08-01  
**Event type:** RESEARCH_RESULT / PAPER_PUBLICATION  
**Editorial status:** STRONG_LEAD_CANDIDATE

### Primary source
- https://openai.com/index/ten-advances-in-mathematics/

### VERIFIED_PRIMARY
- OpenAI published the result set on 2026-08-01.
- OpenAI states that the ten results each resolve or make substantial progress on a long-standing open problem.
- OpenAI attributes the results to an internal version of Astra, described as its next major model.
- OpenAI states that the solution-search token volume would cost roughly USD 2,000 at Sol API rates.
- OpenAI states that humans prepared the arguments into manuscripts with the same model, after which the model formalized each argument into a Lean certificate.

### VENDOR_CLAIM / interpretation boundary
- Whether each result should ultimately be regarded by the relevant mathematical community as a full resolution, major advance, or something narrower requires domain review beyond OpenAI's own characterization.

### SOCIAL_OBSERVATION
- Main-window X discussion included excitement over the concrete problem list, interest in Lean-checkable formalization and cost, and skepticism around research taste, human contribution and proof details.

### PENDING
- Independent expert assessment of mathematical novelty and correctness across all ten results.
- Detailed separation of model-generated mathematical argument, human manuscript preparation, and formalization workflow.

### Safe editorial core
OpenAI公開情報として、Astra内部版による10件の数学・理論CS成果、Lean certificate化、Sol API換算での探索コスト概算を紹介できる。成果の最終的な数学的評価はOpenAIの主張と独立評価を分離して記述する。

---

## T2 — Qwen3.8-Max-Preview

**Artifact / Event:** Alibaba Cloud Model Studio exclusive preview debut of Qwen3.8-Max-Preview.  
**Event date:** 2026-07-19  
**Event type:** MODEL_PREVIEW / PRODUCT_AVAILABILITY  
**Editorial status:** INCLUDE; chronology must precede W32 X momentum

### Primary sources
- https://modelstudio.alibabacloud.com/intl/blog/model-studio-token-plan-individual/
- https://x.com/Alibaba_Qwen/status/2085299356190802058  (official later ranking/amplification post; social/vendor claim)

### VERIFIED_PRIMARY
- Alibaba Cloud Model Studio states that Qwen3.8-Max-Preview debuted on 2026-07-19 through the Model Studio Token Plan for Individual.
- Alibaba describes it as the latest and most capable Qwen model at that time.
- The official Model Studio page describes text reasoning plus vision understanding and use cases including full-stack development, data analysis and office workflows.
- It was initially positioned as a preview available through the Token Plan rather than a normal pay-as-you-go model endpoint.

### VENDOR_CLAIM
- Official X/Model Studio communications and later community discussion claim strong agentic/coding ranking performance.
- Parameter-count, architecture, independent benchmark position and future open-weight licensing details must not be treated as independently verified merely because they were repeated on X.

### SOCIAL_OBSERVATION
- Main-window X discussion emphasized agent/coding rankings, open-weight expectations and multimodal tests. A practitioner migration claim appeared post-cutoff.

### PENDING
- Capture a primary model card / technical report if released.
- Confirm total/active parameter counts from a durable primary technical source.
- Confirm exact open-weight release timing and license rather than relying on expectation posts.
- Independently verify benchmark harness differences.

### Safe editorial core
Qwen3.8-Max-Previewは7月19日に既にpreview debutしており、W32では新規モデル誕生ではなく、agent/coding評価やopen-weight期待を中心とした再注目として扱う。

---

## T3 — DeepSeek-V4-Flash-0731

**Artifact / Event:** Official DeepSeek-V4-Flash API release/update, versioned as DeepSeek-V4-Flash-0731.  
**Event date:** 2026-07-31  
**Event type:** MODEL_UPDATE / API_PUBLIC_BETA / WEIGHTS_RELEASE  
**Editorial status:** INCLUDE; social reaction collected here is post-cutoff

### Primary sources
- https://api-docs.deepseek.com/updates/
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731

### VERIFIED_PRIMARY
- DeepSeek's changelog records a 2026-07-31 DeepSeek-V4-Flash update and states that the official API release entered public beta.
- DeepSeek explicitly names `DeepSeek-V4-Flash-0731` and states that it keeps the same architecture and size as the preview version and was re-post-trained.
- The update applies to the Flash API; DeepSeek states that V4-Pro API and App/Web models were unchanged by that update.
- DeepSeek publishes agent benchmark results and states the public code-agent tasks used DeepSeek Harness minimal mode, max effort, temperature 1.0 and top_p 0.95.
- An official DeepSeek Hugging Face repository exists for `deepseek-ai/DeepSeek-V4-Flash-0731`.
- The Hugging Face model card identifies it as the official release superseding the preview, documents local serving via vLLM/SGLang, and licenses the repository/model weights under MIT.

### VENDOR_CLAIM
- Benchmark superiority over V4-Pro Preview and comparisons with proprietary models are vendor-reported results and require harness-aware interpretation.

### SOCIAL_OBSERVATION
- The representative Reaction-Pass posts were all after the W32 editorial cutoff; they discuss cost/performance, ARC-AGI/coding examples and relative capability ceilings.

### PENDING
- Independent benchmark reproduction under comparable harness and reasoning-effort settings.
- Separate API-update chronology from weight-release chronology if the exact public-weight timestamp is needed to the hour.

### Safe editorial core
DeepSeek-V4-Flash-0731は実在する7月31日の公式更新版であり、previewと同一architecture/sizeへの再post-trainingでagent能力を強化したとDeepSeekが説明している。今回取得したX reactionはCutoff後なので、記事内ではイベント事実とコミュニティ反応の時間帯を分離する。

---

## T4 — MiniMax H3

**Artifact / Event:** MiniMax H3 general omni-modal generative model release.  
**Event date:** 2026-07-31  
**Event type:** MODEL_RELEASE / MULTIMODAL_GENERATION  
**Editorial status:** STRONG_MULTIMODAL_CANDIDATE

### Primary source
- https://minimaxi.com/blog/minimax-h3

### VERIFIED_PRIMARY
- MiniMax formally announced H3 on 2026-07-31.
- MiniMax describes H3 as a general omni-modal generative model that understands multimodal context composed of text, images, video and audio.
- MiniMax states H3 can produce video with native stereo audio and supports up to 15-second, 2K output.
- MiniMax describes unified tasks including text-to-image, text-to-video, image/video/audio reference and editing, multi-shot modeling, and joint audio generation.
- At launch, MiniMax said it planned to open model weights within the following few days, subject to applicable laws and regulations.
- MiniMax itself acknowledges remaining limitations, including multimodal-context understanding headroom, model-scale limitations and image-detail quality in some scenes.

### SOCIAL_OBSERVATION
- Before cutoff, MiniMax's official X activity emphasized open weights / ComfyUI-oriented usage.
- Immediately after cutoff, independent posts showed ComfyUI timing tests, distilled LoRA workflows, prompt-rewriter GGUF tooling and multi-shot + audio examples.

### PENDING
- Exact timestamp and repository for the actual public-weight release.
- Independent quality/consistency comparison.
- Hardware/VRAM requirements for representative local workflows.
- Distinguish core-model quantization from prompt-rewriter / LoRA ecosystem artifacts.

### Safe editorial core
H3は7月31日の発表そのものに加え、Cutoff直後にlocal/ComfyUI workflowの検証へ関心が移ったことが今号らしいポイント。GGUFについてはH3本体ではなく周辺prompt-rewriter artifactのEvidenceと分ける。

---

## T5 — Kimi K3

**Artifact / Event:** Moonshot AI Kimi K3 open-weight native multimodal agentic model.  
**Event date:** 2026-07 (exact release timestamp to retain from primary model history when needed)  
**Event type:** OPEN_WEIGHT_MODEL_RELEASE  
**Editorial status:** INCLUDE; local-inference angle suitable for Community Watch

### Primary source
- https://huggingface.co/moonshotai/Kimi-K3/blob/main/README.md

### VERIFIED_PRIMARY
- Moonshot describes Kimi K3 as an open-weight native multimodal agentic model.
- Official model card reports 2.8T total parameters and 104B activated parameters.
- The model card reports a 1,048,576-token context length and native text/image/video understanding.
- Full weights are released under the Kimi K3 License.
- The model card documents MXFP4 weights / MXFP8 activations from quantization-aware training and recommends vLLM, SGLang and TokenSpeed for deployment.
- The official Hugging Face repository is approximately 1.56 TB in stored model artifacts.

### SOCIAL_OBSERVATION
- A pre-cutoff viral X post claimed a pure-C99 streaming engine could run the multi-trillion-parameter model with approximately 8.24 GB peak RAM by streaming experts from disk.
- Post-cutoff discussion highlighted severe practical constraints such as very large disk usage and very low throughput.

### PENDING
- Inspect and reproduce the community pure-C implementation before treating the 8.24 GB peak-RAM claim, output correctness or token speed as technical facts.
- Confirm exact local-engine checkpoint format and measured disk I/O behavior.

### Safe editorial core
Kimi K3本体の2.8T/104B active・open weights・1M contextは一次情報で扱える。一方「約8GB RAMで動く」はcommunity implementationの未検証claimとして明示し、その実用性議論とセットで紹介する。

---

## T6 — Claude Tag

**Artifact / Event:** Anthropic Claude Tag persistent team-agent product, initially on Slack.  
**Event date:** 2026-06-23  
**Event type:** AGENT_RELEASE / PRODUCT_INTEGRATION  
**Editorial status:** INCLUDE AS W32 REACTION / ECOSYSTEM FOLLOW-UP, not as a new W32 launch

### Primary source
- https://www.anthropic.com/news/introducing-claude-tag

### VERIFIED_PRIMARY
- Anthropic announced Claude Tag on 2026-06-23.
- Anthropic describes Claude joining selected Slack channels as a team member, with access to selected tools/data/codebases.
- Team members can mention `@Claude` and delegate tasks while Claude builds context from relevant channel information and can plan future tasks.
- Anthropic positions Tag as an evolution of Claude Code toward proactive, team-based work.

### SOCIAL_OBSERVATION
- W32 X discussion included Open Tag, an open-source alternative, and broader interest in self-hosting, model choice, data residency, vendor lock-in and governance.

### PENDING
- Verify any claimed August 3 Slack migration/default-switch mechanics from durable Anthropic or Slack release documentation before describing a specific migration event.
- Independent long-term reliability and security evaluation.

### Safe editorial core
Claude Tag自体は6月23日発表。W32では「persistent team agentが collaboration toolへ入ると、self-hosting・model choice・data control・governanceが争点化する」というコミュニティ反応として扱う。

---

## T7 — Mistral Shieldstral

**Artifact / Event:** Shieldstral research/model publication.  
**Event date:** 2026-07-28  
**Event type:** PAPER_PUBLICATION / SAFETY_MODEL  
**Editorial status:** INCLUDE AS PAPER/SAFETY WATCH; community reaction is modest

### Primary source
- https://arxiv.org/abs/2607.25857

### VERIFIED_PRIMARY
- Shieldstral was submitted on 2026-07-28.
- The paper introduces a 3B-parameter policy-adaptive multimodal safety classifier.
- The authors formulate content moderation as binary question answering and consolidate heterogeneous safety datasets into one framework.
- The paper reports approximately 54.1M training/construction samples and claims competitive text-safety performance against models nearly 7× larger plus state-of-the-art multimodal safety classification.

### VENDOR/AUTHOR CLAIM
- Performance comparisons and state-of-the-art claims are claims from the paper and should be distinguished from independent evaluation.

### SOCIAL_OBSERVATION
- X reaction in the collected sample was low-volume and primarily repeated the small size, multimodality, runtime policy flexibility and deployability story.
- No representative independent adversarial evaluation was collected.

### PENDING
- Independent adversarial robustness/moderation evaluation.
- Durable primary model-card/license source if weights are published separately from the paper.

### Safe editorial core
ShieldstralはSafety/Paper Watch向け。論文の技術的提案は紹介できるが、X上の反応規模は小さく、独立adversarial testingを確認したとは書かない。

---

# Editorial screening result

## Strong main-issue candidates
1. OpenAI Astra
2. MiniMax H3
3. Qwen3.8-Max-Preview
4. Kimi K3

## Include with chronology / framing correction
5. DeepSeek-V4-Flash-0731 — real 2026-07-31 official release/update; collected community reaction is post-cutoff.
6. Claude Tag — June launch; W32 relevance is ecosystem/self-host/governance reaction rather than a new launch.
7. Shieldstral — July 28 paper; useful Safety/Paper Watch item, but X reaction is modest.

## Not promoted from the Grok trend list at this stage
- Grok Imagine Video 1.5 — insufficient technical X evidence for W32.
- Qwen Image 3.0 — weak independent W32 community evidence; optional Watchlist only.
