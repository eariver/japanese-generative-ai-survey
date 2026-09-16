# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://deepmind.google/models/model-cards/gemini-3-8-flash
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-02
- retrieval: webfetch markdown of Google DeepMind model card "Gemini 3.8 Flash"; stored verbatim as returned. Page header shows Published 2 September 2026.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

Published 2 September 2026

# Gemini 3.8 Flash

Model Cards are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time to time; for example, to include updated evaluations as the model is improved or revised.

Published: September, 2026

## Model Information

### Description

Gemini 3.8 Flash is the next iteration in the Gemini 3 model family, building on Gemini 3.7 Flash, delivering performance advancements across software engineering and agentic knowledge workflows. It continues to support customizable effort levels to control the mix of quality, cost and latency.

### Model dependencies

Gemini 3.8 Flash is based on Gemini 3.7 Flash.

### Inputs

Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M.

### Outputs

Text, with a 64K token output.

### Architecture

Gemini 3.8 Flash is based on Gemini 3.7 Flash. For more information about the model architecture for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card.

---

## Model Data

### Training Dataset

Gemini 3.8 Flash is based on Gemini 3.7 Flash.

---

## Distribution

Gemini 3.8 Flash is distributed in the following channels; respective documentation shared in line:

-   [Gemini app](https://gemini.google/about/)
-   [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
-   [Google AI Studio](https://aistudio.google.com/)
-   [Gemini API](https://ai.google.dev/gemini-api/docs/models)
-   [Google AI Mode](https://search.google/ways-to-search/ai-mode/)
-   [Google Antigravity](http://antigravity.google/docs)

---

## Evaluation

### Approach

Gemini 3.8 Flash was evaluated across a range of benchmarks, including coding, knowledge work, multimodal capabilities, long-context, computer use, scientific reasoning. Additional benchmarks and details on approach, results and their methodologies can be found at: deepmind.com/models/evals-methodology/gemini-3-8-flash.

### Results

Results as of September, 2026 are listed below (excerpt):

Input price $/1M tokens, no caching: $0.75 ($1.50 regular). Output price $/1M tokens: $3.75 ($7.50 regular).

DeepSWE v1.1 Long-horizon software engineering: 73.7% (3.8 Flash) vs 65.3% (3.7 Flash); Claude Opus 5 74.0%; GPT-5.6 Sol 72.7%; GPT-5.6 Terra 69.6%.

GDPVal-AA v2 Knowledge work Elo: 1545 (3.8 Flash) vs 1482 (3.7 Flash).

Vals Finance Agent v2 Financial analyst tasks: 61.4% (3.8 Flash) vs 59.0% (3.7 Flash).

Harvey's Legal Agent Benchmark Complex legal workflows, All pass rate: 10.0% (3.8 Flash) vs 8.8% (3.7 Flash).

Terminal-bench 2.1 Agentic terminal coding: 89.4% (3.8 Flash) vs 85.8% (3.7 Flash).

Terminal-bench 4.0 General agent capabilities: 19.1% (3.8 Flash) vs 11.2% (3.7 Flash); Claude Opus 5 51.8%.

GDP.PDF Expert PDF document comprehension, All pass rate: 35.0% (3.8 Flash) vs 34.0% (3.7 Flash); GPT-5.6 Sol 40.0%.

CharXiv Reasoning Information synthesis from complex charts, No tools: 86.2% (3.8 Flash) vs 84.5% (3.7 Flash).

LVBench Long video understanding: 87.8% agentic / 87.1% static (3.8 Flash) vs 85.4% (3.7 Flash).

HLE-Verified Multidisciplinary expert reasoning: 54.9% (3.8 Flash) vs 53.6% (3.7 Flash).

OSWorld-2.0 Agentic computer use, Partial score batch tool enabled: 59.0% (3.8 Flash) vs 50.6% (3.7 Flash); Claude Opus 5 75.4%.

BioMysteryBench Bioinformatics research workflows, Human Solvable 88.8% / Human Difficult 56.5% (3.8 Flash).

LABBench2 Biology real-world research tasks: 86.2% (3.8 Flash) vs 82.1% (3.7 Flash).

## Intended Usage and Limitations

### Benefit and Intended Usage

Gemini 3.8 Flash is well-suited for users, developers, and enterprises, designed for cost-effective scaling of general-purpose, production-ready agents. Some use cases include: software engineering, agent tasks, and complex knowledge workflows.

### Known Limitations

Gemini 3.8 Flash may exhibit some of the general limitations of foundation models, such as hallucinations. In addition to this, we are continually working to improve jailbreak resistance and have recently strengthened the mitigations across Frontier Safety. There may also be occasional slowness or timeout issues. At times, the model might use more tokens to maximize performance, especially at higher effort levels.

The knowledge cutoff date for Gemini 3.8 Flash is March 2026 – users can expect updated information for some domains while in others they may experience the model's knowledge is limited to January 2025 (in line with the Gemini 3 Model Family).

## Ethics and Content Safety

Overall, Gemini 3.8 Flash performs similarly to Gemini 3.7 Flash across both safety and tone, with low unjustified refusals. Safety performance across non-English languages regressed slightly relative to 3.7 Flash.

Evaluation: Text to Text Safety -0.4pp (lower is better); Multilingual Safety +5.4pp (lower is better); Image to Text Safety 0.0pp; Tone +0.2pp (higher is better); Unjustified-refusals +1.1pp (lower is better).

We conduct manual red teaming by specialist teams who sit outside of the model development team. For child safety evaluations, Gemini 3.8 Flash satisfied required launch thresholds. For content safety policies generally, including child safety, we saw similar or improved safety performance compared to Gemini 3.7 Flash.

### Frontier Safety Assessment

Gemini 3.8 Flash is part of the Gemini 3 series of models. We evaluated Gemini 3.7 Flash as outlined in our latest Frontier Safety Framework (April-2026), and found that it did not reach any Tracked or Critical Capability Levels (T/CCLs). Our assessments have shown that Gemini 3.8 Flash does not have meaningful new capabilities or material increases in performance with respect to the domains outlined in our Frontier Safety Framework compared to Gemini 3.7 Flash; therefore, based on Gemini 3.7 Flash results, we are confident that Gemini 3.8 Flash is also unlikely to reach any T/CCLs.

[truncated for edition-local storage: navigation boilerplate and footer omitted; core model card content preserved verbatim]
