# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://huggingface.co/zai-org/GLM-5.3
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-08-28
- retrieval: webfetch markdown of zai-org/GLM-5.3 Hugging Face model card; stored verbatim as returned. 2026-08-28 is edition-attributed boundary date; page display shows no explicit publication date in retrieved markdown, so date carries uncertainty.
- authority_class: SECONDARY_TECHNICAL

# Retrieved content (verbatim as returned)

zai-org/GLM-5.3 · Hugging Face

[![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) Hugging Face](/)

-   [Models](/models)
-   [Datasets](/datasets)
-   [Spaces](/spaces)
-   [Buckets new](/storage)
-   [Docs](/docs)
-   [Enterprise](/enterprise)
-   [Pricing](/pricing)

-   [Log In](/login)
-   [Sign Up](/join)

# [![](https://cdn-avatars.huggingface.co/v1/production/uploads/62dc173789b4cf157d36ebee/i_pxzM2ZDo3Ub-BEgIkE9.png)](/zai-org) [zai-org](/zai-org) / [GLM-5.3](/zai-org/GLM-5.3)

Like 1.85k

Follow

![](https://cdn-avatars.huggingface.co/v1/production/uploads/62dc173789b4cf157d36ebee/i_pxzM2ZDo3Ub-BEgIkE9.png) Z.ai 20.9k

[Text Generation](/models?pipeline_tag=text-generation) [Transformers](/models?library=transformers) [Safetensors](/models?library=safetensors) [English](/models?language=en) [Chinese](/models?language=zh) [glm_moe_dsa](/models?other=glm_moe_dsa) [conversational](/models?other=conversational) [Eval Results](/models?other=eval-results) [fp8](/models?other=fp8)

arxiv: 2602.15763

License: glm-5.3

[Model card](/zai-org/GLM-5.3) [Files Files and versions xet](/zai-org/GLM-5.3/tree/main) [Community 23](/zai-org/GLM-5.3/discussions)

Deploy

Copy to bucket new

Use this model

### Instructions to use zai-org/GLM-5.3 with libraries, inference providers, notebooks, and local apps.

-   Libraries
-   [Transformers](/zai-org/GLM-5.3?library=transformers)

    How to use zai-org/GLM-5.3 with Transformers:

    \# Use a pipeline as a high-level helper
    from transformers import pipeline

    pipe = pipeline("text-generation", model="zai-org/GLM-5.3")
    messages = \[
        {"role": "user", "content": "Who are you?"},
    \]
    pipe(messages)

    \# Load model directly
    from transformers import AutoTokenizer, AutoModelForCausalLM

    tokenizer = AutoTokenizer.from\_pretrained("zai-org/GLM-5.3")
    model = AutoModelForCausalLM.from\_pretrained("zai-org/GLM-5.3", device\_map="auto")

-   Inference
-   Inference Providers
-   [HuggingChat](/chat/models/zai-org/GLM-5.3)
-   Notebooks
-   [Google Colab](/zai-org/GLM-5.3/colab)
-   [Kaggle](/zai-org/GLM-5.3/kaggle)
-   Local Apps
-   [vLLM](/zai-org/GLM-5.3?local-app=vllm)

    How to use zai-org/GLM-5.3 with vLLM:

    \# Install vLLM from pip:
    pip install vllm
    # Start the vLLM server:
    vllm serve "zai-org/GLM-5.3"

-   [SGLang](/zai-org/GLM-5.3?local-app=sglang)
-   [Docker Model Runner](/zai-org/GLM-5.3?local-app=docker-model-runner)

    docker model run hf.co/zai-org/GLM-5.3

-   [Browse Quantizations](/models?other=base_model:quantized:zai-org/GLM-5.3) to use this model in llama.cpp, Ollama, LM Studio, or any compatible app.

# GLM-5.3

GLM-5.3 uses the same base model as GLM-5.2 — every gain comes from post-training. Compared with GLM-5.2, it is much better at complex coding and long-horizon tasks:

-   Stronger Coding: GLM-5.3 is the most capable open-weights model for coding, with a 50% improvement over GLM-5.2 on our in-house Z.ai Code Bench. It also achieve open-source SOTA on public benchmarks including Terminal Bench 3.0 and Agents' Last Exam.
-   Emergent Cyber Capability: As we scaled post-training, cyber capability developed faster than we expected. GLM-5.3 is state of the art on CyberGym for vulnerability discovery, and its gains are largest further up the exploitation chain, where it more than doubles GLM-5.2 on exploitation benchmarks.

[![bench_53](https://raw.githubusercontent.com/zai-org/GLM-5/refs/heads/main/resources/bench_53_2.png)](https://raw.githubusercontent.com/zai-org/GLM-5/refs/heads/main/resources/bench_53_2.png)

## Benchmark

Benchmark

GLM-5.3

GLM-5.2

Kimi K3

DeepSeek-V4 Pro-0813

Qwen3.8-Max

Opus 4.8

Fable 5 (w/ fallback)

GPT-5.6 Sol

Terminal Bench 2.1

88.2

81.0

88.3

87.9

86.6

85.0

88.0

**88.8**

Terminal Bench 3.0

28.3

4.6

17.4

–

–

21.1

33.7

**34.6**

DeepSWE (v1.1)

66.9

46.2

67.5

62.7

56.6

58.0

69.7

**72.7**

NL2Repo

58.0

48.9

58.0

61.1

55.9

**69.7**

–

–

ProgramBench (Almost Solved)

19.0

9.5

17.5

–

10.5

15.5

**33.0**

23.0

FrontierSWE

78.1

67.5

–

–

–

66.5

**88.2**

–

SWE-Marathon (v1.1)

42.5

19.4

48.1

–

–

**48.8**

33.1

42.5

PostTrainBench

39.8

31.7

32.0

–

–

32.9

**41.8**

36.2

CyberGym

**84.5**

77.2

80.0

83.3

78.5

78.1

83.8

83.6

ExploitGym (2h / 6h)

105 / 130

29 / 39

36 / 70

–

14 / 26

80 / 120

181 / 247

**216 / 293**

ExploitBench

54.4

24.4

32.2

–

28.8

40.0

**78.0**

76.5

Toolathlon Verified

73.0

59.9

**76.5**

74.1

72.5

76.2

74.7

74.9

AutomationBench (v1.0.6)

**48.2**

26.2

46.7

43.2

39.8

41.0

46.2

45.8

Agents' Last Exam (ALE-CLI)

28.5

23.8

27.6

25.7

27.0

25.7

23.8

**28.6**

HLE w/ Tools

62.5

54.7

59.8

60.0

56.2

57.9

63.9

**64.5**

GDPval-AA v2

**1769**

1508

1682

1590

1739

1588

1743

1730

### Serve GLM-5.3 Locally

GLM-5.3 supports deployment with the following frameworks:

-   [SGLang](https://github.com/sgl-project/sglang) — see [cookbook](https://cookbook.sglang.io/autoregressive/GLM/GLM-5.3)
-   [vLLM](https://github.com/vllm-project/vllm) — see [recipes](https://recipes.vllm.ai/zai-org/GLM-5.3)
-   [Transformers](https://github.com/huggingface/transformers)
-   [KTransformers](https://github.com/kvcache-ai/ktransformers)
-   [Unsloth](https://github.com/unslothai/unsloth) — see [guide](https://unsloth.ai/docs/models/GLM-5.3)

### Note

-   GLM-5.3 supports controlling the thinking budget through the `reasoning_effort` parameter, which accepts three levels: `low`, `high`, and `max`. It defaults to `max` if not passed.
-   In the chat template for GLM-5.3, `clear_thinking` defaults to `false` if not passed. For chat scenarios, explicitly pass `clear_thinking=true`.

Downloads last month: 800,511

Safetensors. Model size: 753B params. Tensor type: BF16, F8_E4M3, F32.

Paper: GLM-5: from Vibe Coding to Agentic Engineering, arXiv 2602.15763.

[truncated for edition-local storage]
