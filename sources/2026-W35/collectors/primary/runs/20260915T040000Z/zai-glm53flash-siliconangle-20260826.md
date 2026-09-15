# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://siliconangle.com/2026/08/26/z-ai-open-sources-ox-alpha-model-as-glm-5-3-flash/
- observed_at: 2026-09-15T04:15:00Z
- published_at: 2026-08-26 (updated 20:26 EDT)
- retrieval: webfetch text; boilerplate trimmed; substantive claims preserved.
- authority_class: SECONDARY_TECHNICAL (enterprise tech press; Z.ai blog + HF card are verification targets)

# Retrieved content (substantive claims)

Title: Z.ai open-sources 'Ox Alpha' model as GLM-5.3-Flash. By Maria Deutscher.

Z.ai Co. today released the code for GLM-5.3-Flash, a large language model that's 10 times more cost-efficient than its predecessor (vendor claim). The algorithm debuted last week under codename Ox Alpha. OpenRouter launched a free hosted version without disclosing the developer; users speculated Z.ai.

Specs: MoE, 320B parameters total, 18B active per prompt. Requests up to 1M tokens of text/images/video; responses up to 131,072 tokens.

Architecture changes: sparse attention (reviews only most relevant tokens); linear attention (RAM doubles rather than quadruples when prompt doubles; substitutes softmax with more efficient algorithm). Trained on 30T-token dataset; mHC technology to reduce gradient distortion across layers.

Vendor benchmarks: compared vs Claude Opus 4.8, GPT-5.6 Terra, Gemini 3.7 Flash. Highest score on GDPval-AA v2 (knowledge-work eval); second on AutomationBench (cloud-app task completion). All vendor-claimed, need independent reproduction.

GLM-5.3-Flash weights available on Hugging Face (see HF raw + Grok official-post ledger rows).
