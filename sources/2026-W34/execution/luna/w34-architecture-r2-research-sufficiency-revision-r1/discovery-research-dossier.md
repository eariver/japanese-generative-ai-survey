# W34 fresh Discovery research-sufficiency dossier

Status: `SOL_DISCOVERY_REVIEW_REQUIRED`

This dossier records Luna/Work execution evidence for the fresh W34 Discovery
refresh requested after Architecture Review r2. It is not a Sol completeness
decision, a Materiality decision, a Selection decision, or an Architecture
recommendation.

## 1. Fixed scope and execution identity

- Issue: `2026-W34`
- Research question: `What materially changed in generative AI for 2026-W34, and why does it matter now?`
- Window: `[2026-08-14T18:00:00-04:00, 2026-08-21T18:00:00-04:00)`
- Cutoff timezone: `America/New_York`
- Equivalent UTC window: `[2026-08-14T22:00:00Z, 2026-08-21T22:00:00Z)`
- Execution area: `sources/2026-W34/execution/luna/w34-architecture-r2-research-sufficiency-revision-r1/`
- Human Architecture Review r2 decision: `REQUEST_CHANGES`
- Regeneration boundary: `ISSUE_INITIALIZED`
- Existing X/Grok intake was reused; no second Grok run was executed.

The prior canonical Discovery bytes were snapshotted under `prior-authority/`
before the mutable canonical Discovery path was superseded. The prior accepted
graph remains available in git history and in that snapshot; no prior execution
record was edited.

## 2. Source surfaces exercised

| Surface | Source class and method | W34 coverage observed | Result and limits |
|---|---|---|---|
| Existing weekly X/Grok and DailyX | Reused exact repository Raw and `x-source-intake-v2.json`; no recollection | Existing weekly Grok manifest and DailyX files retained | Existing community/high-recall signal was not treated as primary technical Evidence; a second Grok run was not required. |
| arXiv | Repository-owned `scripts.source_intake` using six Atom category queries: `cs.AI`, `cs.CL`, `cs.LG`, `cs.CV`, `cs.DC`, `cs.CR` | Six Raw Atom responses; `2,296` unique entries in the W34 query window | Collector `success`. Category sweeps are broad and not exhaustive of all research venues; the abstract-level leads below still need paper-level Evidence. |
| GitHub releases | Repository-owned GitHub Releases collector across `sgl-project/sglang`, `vllm-project/vllm`, `ggml-org/llama.cpp`, `huggingface/transformers`, `NVIDIA/TensorRT-LLM`, `flashinfer-ai/flashinfer`, and `Comfy-Org/ComfyUI` | `648` releases returned; `5` W34 matches | Collector `success`. The watchlist is curated and is not a complete GitHub search. Matches were one Transformers release and four FlashInfer nightlies; the prior Discovery already contained those source families. |
| Official provider and project pages | Repository-owned official-page collector against 22 configured pages | `17` pages fetched; `5` failed | Collector `partial`. Successful pages covered OpenAI, Anthropic, Google/DeepMind, Meta, Mistral, Qwen, DeepSeek, Stability AI, Cohere, NVIDIA, AI2, Apple, Runway, Kimi, MiniMax, and Z.ai. |
| Repository prior corpus | Existing W34 working-set inventory, Raw index, crosswalks, and accepted Discovery graph | Prior accepted graph and source bindings were read before refresh | Prior event-level inventory remains `105`; prior downstream Screening input remains `110`. This run does not regenerate or reinterpret Screening. |

Official-page failures were recorded exactly as follows: Alibaba Model Studio
timed out; x.ai/news returned HTTP 403; Microsoft Azure AI blog timed out; AWS
Machine Learning blog timed out; IBM AI announcements timed out. These failures
are coverage observations for Sol, not evidence that those channels contained no
W34 developments.

Fresh Source Intake files and collector provenance are under:

`source-intake/sources/2026-W34/collectors/`

The overall Source Intake report is intentionally recorded as `partial`; no
claim of exhaustive Source Intake completeness is made here.

## 3. Prior versus fresh Discovery delta

| Measure | Prior | Fresh | Delta |
|---|---:|---:|---:|
| Canonical Discovery graph records | 40 | 55 | +15 |
| Sol event-level pre-Screening inventory | 105 | 105 retained as prior baseline | no downstream expansion in this run |
| Prior records copied into fresh input | 40 | 40 | semantic content retained |
| Newly materialized Discovery leads | 0 | 15 | +15 |
| Fresh duplicate consolidations | — | 0 | none |
| Prior candidate chronology reclassified | — | 0 | none |

The fresh graph is a source/provenance Discovery graph, not a story count. The
15 added records are all `origin=GAP_FILL`, `research_pass=2`, and carry
`technical_claims_accepted=false` and `selection_not_performed=true`. No prior
candidate was changed semantically by this Discovery refresh. The existing
Transformers/FlashInfer GitHub signals were re-observed but not duplicated as
new candidate records.

## 4. Fresh Discovery leads for independent review

These are plausible W34 leads only. They are deliberately not labeled
`MATERIAL`, `SELECTED`, or `PRIMARY`.

### Official provider/project surfaces

| Discovery ID | Lead | Observed chronology | Lane | Later depth needed |
|---|---|---|---|---|
| `w34-refresh-kimi-code-cli-v038-v037` | Kimi Code CLI v0.38.0 and v0.37.0 release notes | Aug 18 and Aug 20, date-only official release notes | Developer tooling / agent infrastructure | Read candidate-level release notes and verify which changes have concrete user-facing technical effect. |
| `w34-refresh-openai-replit-gpt56-luna` | Replit expands access to software creation with GPT-5.6 Luna | Aug 19 official RSS item | Developer tooling / model distribution | Retrieve and consume the linked article body; separate customer report from product/API change. |
| `w34-refresh-openai-defenders-window` | The Defender’s Window | Aug 17 official RSS item | AI security / cyber | Retrieve and consume the linked article body; determine whether it describes an in-window technical development or policy context. |
| `w34-refresh-cohere-culture-funnel` | The Culture Funnel: You can’t align what isn’t in the data | Aug 19 Cohere research index item | Training data / alignment research | Inspect methods and claims; keep research findings distinct from operational product changes. |
| `w34-refresh-apple-grpo-beyond-english` | GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings | Aug 18 Apple ML Research index date | Training / reasoning / multilingual | Retrieve paper body and assess whether it is a W34 research publication relevant to the survey question. |
| `w34-refresh-apple-human-like-behaviors-llms` | Examining Human-Like Behaviors in LLMs | Aug 19 Apple ML Research index date | Model behavior / evaluation | Retrieve paper body and methods; no behavioral conclusion is accepted at Discovery. |
| `w34-refresh-apple-scaling-laws-mixture-pretraining` | Scaling Laws for Mixture Pretraining Under Data Constraints | Aug 20 Apple ML Research index date | Training / data mixture / scaling | Retrieve paper body and verify technical contribution and W34 relevance. |

The official-page Raw bindings are exact current snapshots, but index pages are
not necessarily historical archives. Date-only entries therefore remain
chronology-qualified leads until candidate-level Evidence.

### arXiv research and systems surfaces

| Discovery ID | Lead | Published at | Lane | Later depth needed |
|---|---|---|---|---|
| `w34-refresh-arxiv-k-bench` | K-Bench: measuring model performance on real scientific agent requests | `2026-08-21T20:06:08Z` | Evaluation / scientific agents | Read the paper and inspect dataset, judge design, and claim boundaries. |
| `w34-refresh-arxiv-saem` | SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning | `2026-08-21T20:26:32Z` | MoE inference / serving | Verify runtime implementation and measured improvements; one abstract retrieval is not sufficient. |
| `w34-refresh-arxiv-refine` | REFINE: A Multi-Agent LLM Approach for Evidence-Guided Code Refactoring | `2026-08-21T17:44:40Z` | Developer tooling / agentic code | Inspect evaluation design, model versions, and reproducibility. |
| `w34-refresh-arxiv-sec-opd` | SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation | `2026-08-21T16:14:07Z` | Agent security / prompt injection | Inspect threat model, adaptive attack setup, and defensive evidence. |
| `w34-refresh-arxiv-aid-guard` | AID-Guard: Stateful Authorization for Delegated Agent Effects | `2026-08-21T14:31:29Z` | Agent security / authorization | Inspect protocol assumptions and prototype evaluation before treating it as a development. |
| `w34-refresh-arxiv-llama-mobile` | Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs | `2026-08-21T14:10:31Z` | VLM inference / edge deployment | Inspect hardware, benchmark scope, and model/license facts. |
| `w34-refresh-arxiv-memory-augmentation` | Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning | `2026-08-21T16:22:36Z` | Reasoning efficiency / retrieval | Inspect the paper's compression and evaluation claims. |
| `w34-refresh-arxiv-algorithm-dispatch` | Data-Driven Dynamic Algorithm Dispatch with Large Language Models | `2026-08-21T19:37:46Z` | LLM systems / algorithm discovery | Inspect the case study and whether it is materially connected to generative-AI practice. |

The arXiv Raw bindings are category Atom responses from the fresh collector.
The collector summary reports publication and update times; later Evidence must
use the paper itself and must not treat an abstract or a repository index as a
complete technical authority.

## 5. Negative-space observations for Sol

1. Five configured official channels were unavailable in this run: Alibaba Model
   Studio, x.ai, Microsoft Azure AI, AWS Machine Learning, and IBM AI
   announcements. The AWS/Azure/cloud-service lane is therefore still a real
   coverage gap even though prior W34 working-set locators exist.
2. The GitHub sweep covered seven high-value repositories but is explicitly a
   curated watchlist, not a full open-source ecosystem search. Zero W34 matches
   in vLLM, SGLang, llama.cpp, TensorRT-LLM, and ComfyUI must not be read as
   absence from the broader ecosystem.
3. The official pages are current index snapshots retrieved on
   `2026-09-07T16:16:55Z`; they can expose historical date labels, but several
   pages do not provide a stable historical item body. Runway, for example,
   exposed a post-cutoff Aug 20 item at `2026-08-20T23:32:55.990Z`, which was
   not promoted as an in-window lead.
4. The arXiv sweep produced `2,296` unique entries. That high recall reduces
   one kind of negative space but creates a large deduplication and relevance
   review obligation; it is not evidence that all entries are survey-relevant.
5. Search concentration remains higher in large providers and the configured
   arXiv categories than in inaccessible or less-indexed provider channels. No
   count-based completeness conclusion is made.
6. Month-only Google/DeepMind and other index entries were not promoted as new
   candidate-level chronology claims unless an exact date marker was present.
7. Existing X/Grok material remains a community/high-recall signal surface and
   was reused exactly. It does not close the first-party authority gaps above.
8. No Discovery-level chronology reclassification was made for existing
   candidates in this run. The earlier W34 c048 `OTHER -> MAIN_EVENT` correction
   remains historical r1/r2 downstream work; it is not silently re-applied or
   expanded here.

## 6. High-signal candidates needing iterative Evidence depth

The following are priority hints for later Luna/Work execution after Sol has
reviewed Discovery. They are not Materiality or Selection decisions:

- Kimi Code CLI v0.38.0/v0.37.0;
- OpenAI's Replit and Defender’s Window RSS leads;
- Apple GRPO Beyond English and Scaling Laws for Mixture Pretraining;
- arXiv SAEM, K-Bench, REFINE, SecOPD, AID-Guard, Llama-Mobile, Memory
  Augmentation, and Dynamic Algorithm Dispatch;
- existing W34 high-signal provider/repository leads, including GLM-5.3,
  DeepSeek V4 Flash Vision, Mistral Agentic Search, Transformers v5.15.1, and
  FlashInfer, whose primary bodies should be consumed rather than merely bound.

For these leads, a later Evidence pass should not stop at the first failed URL
or a single abstract/index retrieval. It should follow the authority ladder in
the Sol/Luna governance: announcement or release notes, documentation/API or
model card, repository/tag/commit where applicable, and paper/system/security
material where applicable.

## 7. Prior sparse-Architecture sanity check

The fresh Discovery contains plausible alternatives to the former one-item
Architecture. In particular, it now exposes independent developer-tooling,
agent evaluation, inference/runtime, security/authorization, multilingual
training, and edge-deployment leads that were absent from the prior 40-node
accepted Discovery graph. Kimi Code, REFINE, SAEM, K-Bench, SecOPD, AID-Guard,
and Llama-Mobile are concrete examples of alternative technical directions.

This observation does not imply that any of them should become `MATERIAL` or
`SELECTED`, and it does not imply that the former sparse Architecture was wrong
without downstream Evidence. It does show that the old `MATERIAL=1 /
SELECTED=1` result must not be treated as the target for the next stages.

## 8. Canonical materialization and validation

- Fresh input generated by `materialize_fresh_discovery.py`:
  `fresh-discovery-v2.jsonl`
- Fresh Discovery ledger: `fresh-discovery-ledger.json`
- Canonical Discovery JSONL: `sources/2026-W34/discovery/discovery-v2.jsonl`
- Canonical Discovery acceptance:
  `sources/2026-W34/discovery/discovery-accepted-v2.json`
- Core Discovery validation record:
  `validation/discovery-acceptance-validation.json`
- Core stage-contract validation record:
  `validation/core-discovery-stage-validation.json`
- Discovery Stage Checkpoint:
  `sources/2026-W34/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`

The reviewed Core reported:

- X manifest validation: `PASS`;
- Raw-ref normalization and SHA validation: `PASS`;
- Discovery graph validation: `PASS`;
- X integration: `PASS`;
- accepted record count: `55`;
- fresh graph SHA: `af5a500c127cd74ea1c00fa5fe258e9912f2aec27ad30369e2e33b6043ef8bb8`.

## 9. Required supervisory handoff

Sol must independently review the fresh Discovery corpus and negative space
before any Screening or downstream filtering. The handoff must answer whether
the current source coverage is sufficient, which leads require expansion, and
whether the residual official-channel and broad-arXiv limitations are
defensible.

This dossier does not answer those questions. The required next status is:

`SOL_DISCOVERY_REVIEW_REQUIRED`

