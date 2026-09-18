# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://openai.com/index/gpt-6-astra/
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-03
- retrieval: webfetch markdown of OpenAI GPT-6 Astra launch announcement; stored verbatim as returned. Page retrieval shows no explicit date display; 2026-09-03 is edition-attributed launch date.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

GPT-6 Astra: A new generation of intelligence | OpenAI

[Skip to main content](#main)

[](/)

-   [Research](/research/index/)
-   Products
-   [Business](/business/)
-   [Developers](/api/)
-   [Company](/about/)
-   [Foundation(opens in a new window)](https://openaifoundation.org)

Log in[Try ChatGPT(opens in a new window)](https://chatgpt.com/)

-   Research
-   Products
-   Business
-   Developers
-   Company
-   [Foundation(opens in a new window)](https://openaifoundation.org)

[Try ChatGPT(opens in a new window)](https://chatgpt.com/)Login

OpenAI

![A luminous particle spiral forming the number six against a black background.](https://images.ctfassets.net/kftzwdyauwt9/H9Mf4UPiWGb0N25sLJHUu/6d971b8e12cbab3db48c94617d703b5d/poster.webp?w=3840&q=90&fm=webp)

GPT

Astra

# GPT-6 Astra: A new generation of intelligence

## A new generation of intelligence

We’re introducing GPT‑6 Astra, the world’s most intelligent and aligned model.

GPT‑6 Astra brings together years of research and big bets across pre-training, reinforcement learning, and alignment. Astra is state-of-the-art on computer use, browsing, software engineering, cybersecurity, science, and professional work. Astra saturates FrontierMath Tier 4 with a 98% score, having already helped [solve long-standing open problems⁠](https://openai.com/index/ten-advances-in-mathematics/) in mathematics. Astra also saturates ARC-AGI-3 with a 99.9% score and ExploitBench with a 100% score. It also sets a new frontier on computer and browser use, handling the most demanding professional work with unmatched speed, accuracy, and judgment.

GPT‑6 Astra is rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API, Microsoft Azure, and AWS Bedrock.

Terminal-Bench Science 0.1ARC-AGI-3FrontierMath Tier 4 (v2)Terminal-Bench 4.0AutomationBench

> “On ARC-AGI-3, Astra surpassed our human action-efficiency baseline on 96% of levels, effectively reaching human parity on the benchmark. Not only is this the best model we’ve ever tested, but it also represents a meaningful step change in frontier-model performance - not only in its ability to navigate and solve novel environments, but also in how efficiently it learns to do so.”

Greg Kamradt, ARC Prize Foundation

Astra is our most aligned model, with substantial improvements in understanding user intent and model behavior—you can delegate tasks with greater confidence in Astra’s judgment. As one way that we test this, we built a new evaluation informed by the Hugging Face incident that evaluates whether a model facing a difficult or impossible task will go beyond its intended scope. Compared to GPT‑5.6 Sol, which without production safeguards went beyond the authorized target 48% of the time, GPT‑6 Astra did this in 0% of cases.

## The world’s best computer use model

GPT‑6 Astra marks a new frontier in the speed, accuracy, and safety of computer use. It can take care of tedious tasks like filling out online forms, updating customer records in a CRM, and organizing your calendar. It can conduct online research and draft summaries in your email or in your document editor. It can analyze scientific data, generate plots, create a website, and run frontend QA checks to make sure all the features on that site work. It can help you autonomously install and test software, and troubleshoot problems you see on screen. These improvements are also reflected in our state-of-the-art evaluation results.

Agents’ Last ExamScreenSpot-ProOSWorld

These improvements also result in significant efficiency gains in real knowledge-work tasks. In latency simulations on OSWorld 2.0, Astra achieves higher computer-use performance in about 47% less time per task than GPT‑5.6 Sol, scoring 72.6% at roughly 40 minutes per task, compared with 65.7% at roughly 75 minutes.[3](#citation-bottom-3)

Alongside Astra, we are also updating the Codex harness to significantly improve the speed of computer use. Combined with Astra’s efficiency, this translates to a 1.9x faster task completion compared to the current GPT‑5.6 Sol experience, on the Mind2Web benchmark.

> “We’re integrating GPT‑6 Astra into Devin’s harness on launch day, where it delivers state-of-the-art performance on our internal testing benchmark. Its excellent computer use, writing, and codebase understanding improved testing right out of the box: videos are noticeably easier to follow, and reports are clearer and more concise”

Silas Alberti, SVP Research, Cognition

## A step change in professional work

GPT‑6 Astra pairs advances in computer use with targeted training for professional environments, to help tackle complex work tasks. It combines the intelligence required for complex problems with the ability to carry out multistep workflows and produce polished documents, spreadsheets, and presentations.

BenchCADBrowseCompOpenScore String QuartetsDesign Tasks (Internal)Data Science Tasks (Internal)

## Coding

GPT‑6 Astra is the best model for software engineering to date.

> “GPT‑6 Astra delivers state-of-the-art performance on our internal coding benchmarks and shows a clear step forward in trading intuition evaluations compared with GPT‑5.6 Sol. When used for agentic coding, GPT‑6 Astra communicates in a way that’s easier for developers to follow and produces code that requires less iteration to reach production quality.”

John Crepezzi, AI Assistants, Jane Street

Terminal-Bench 4.0FrontierCode 1.1 ExtendedDeepSWEArtificial Analysis Coding AgentDatabase Migration Tasks (Internal)

With Astra, we’re introducing a new way for Codex to preserve and retrieve context when the context window fills. In Codex, Astra can keep notes across context windows, preserving accumulated details without repeatedly compressing them into a single summary. Earlier context windows remain searchable, so Astra can find requirements or test results from previous messages and tool outputs. You can enable this experimental feature in your [Codex config.toml,⁠(opens in a new window)](https://learn.chatgpt.com/docs/config-file/config-reference) and it will become the default for Astra in the coming weeks.

## Advancing scientific discovery

> “The story is: end of one era, start of another.”

Greg Burnham, EpochAI

GPT‑6 Astra is a major advance for scientific discovery, mathematics, and health. Today, we’re sharing two further results on the gaps between prime numbers.[9](#citation-bottom-9), [10](#citation-bottom-10)

Astra also sets new records across a suite of math and science evaluations.

GPQA DiamondHealthBench ProfessionalLifeSciBenchGeneBench ProMedChemBench

## Cybersecurity

As we discussed in our [safety update⁠](/index/path-to-astra/), Astra is a significant jump in cyber capabilities and meets the [Critical threshold](/index/path-to-astra/) in cybersecurity under our [Preparedness Framework](/index/updating-our-preparedness-framework/). Its ability to identify and develop zero-day exploits can help defenders find and patch weaknesses, but it also creates a need for stronger safeguards.

We first tested the model without production safeguards on ExploitBench and ExploitGym. On ExploitBench, Astra achieved a perfect score of 100%, compared with 78.5% for GPT‑5.6 Sol. On ExploitGym, Astra reached a 42.4% success rate, compared with 30.3% for GPT‑5.6 Sol, while using substantially fewer output tokens.[13](#citation-bottom-13)

During the evaluation on internal “ExploitBench (June–August 2026)”, Astra even discovered and used two previously unknown zero-day vulnerabilities. We are disclosing both vulnerabilities to their maintainers.

We also tested Astra on SRE-Bench[15](#citation-bottom-15). Astra solved 88.0% of tasks in a single attempt and 99.2% within four attempts, compared with 55.9% and 68.7% for GPT‑5.6 Sol, respectively.

## Aligning and deploying GPT‑6 Astra responsibly

Astra is our most aligned model. Astra excels at exercising care, respecting task boundaries, and communicating transparently.

In an internal evaluation, Astra never attempted to circumvent a Codex Auto-Review denial. This held even when Auto-review was deliberately configured to be evadable and the task was impossible to complete otherwise.

Our evaluations found Astra’s written reasoning harder to monitor than GPT‑5.6 Sol’s, based on tests that explicitly asked it to evade monitoring. Improving monitorability remains a research priority, and the accompanying [system card⁠(opens in a new window)](https://deploymentsafety.openai.com/gpt-6-astra) details our findings and ongoing work.

## Availability

GPT‑6 Astra is rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API, Microsoft Azure, and AWS Bedrock.

For developers, GPT‑6 Astra will be available in the OpenAI API as `gpt-6-astra` and through Microsoft Azure and Amazon Bedrock.

OpenAI API Standard pricing is $10 per million input tokens and $50 per million output tokens. Separate rates apply to cache reads and writes. Fast mode is available for GPT‑6 Astra in the API and delivers up to 2x the speed of Standard processing at 2x the Standard price.

[truncated for edition-local storage]
