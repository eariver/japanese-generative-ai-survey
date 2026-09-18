# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://www.anthropic.com/claude-fable-and-mythos-5-1
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-01
- retrieval: webfetch markdown of Anthropic announcement introducing Claude Fable 5.1 and Claude Mythos 5.1; stored verbatim as returned.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

Introducing Claude Fable 5.1 and Claude Mythos 5.1 \\ Anthropic

September 2026

# Claude Fable 5.1 and Mythos 5.1

We’re introducing Claude Fable 5.1 and Claude Mythos 5.1. They’re the world’s most advanced models for coding and knowledge work—and their research capabilities offer an early glimpse of how AI models will contribute to scientific progress.

Claude Fable 5.1 and Claude Mythos 5.1 are the same model, but with different levels of safeguards. Fable 5.1 is generally available, while Mythos 5.1 is available only through our trusted access programs; its safeguards are specifically designed to support work in cybersecurity and the life sciences.

Alongside its increased capabilities, Fable 5.1 takes important steps towards addressing the feedback we’ve received from customers on price, data retention, and safeguards.

**Price.** Fable 5.1 will cost an estimated 25% less than Fable 5 for typical workloads, wherever usage is billed by token. This is because we’re reducing our pricing on cache reads. For highly agentic work, the savings will often be much larger—up to approximately 45%.

**Data retention.** Our new system of Enterprise Frontier Safeguards (EFS) gives customers complete privacy (the same as a zero data retention policy) while still being state-of-the-art at preventing adversarial use. EFS works by storing data in cloud infrastructure controlled entirely by the customer, not Anthropic. It will be made available to enterprise customers in phases, beginning later this fall. Until EFS is available, eligible customers will be able to use Fable 5.1 with zero data retention.

**Safeguards.** We’ve improved our safeguards to reduce false positives. In cybersecurity, our newest safeguards block 60% fewer false positives than before. In part, this is because Fable 5.1 can now be used to discover software vulnerabilities—though not to develop exploits for them. In biology, we’ve established an access program, developed in partnership with the US government, to enable access to Claude Mythos 5.1’s advanced biology capabilities.

## A new performance frontier

Claude Fable 5.1 sets a new standard for coding, knowledge work, and long-running problem-solving tasks. Fable 5.1 is capable of much higher performance than its predecessor, Fable 5. And when set to Low or Medium effort, Fable 5.1 achieves results similar to or better than Fable 5’s at a much lower cost.

Benchmarks (Fable 5.1 vs Fable 5, Opus 5, GPT-5.6 Sol):

- Agentic scientific research, Terminal-Bench-Science 0.1: Fable 5.1 52.6%, Fable 5 24.7%, Opus 5 29.0%, GPT-5.6 Sol 22.4%
- Agentic coding, Terminal-Bench 4.0: Fable 5.1 55.8% / Mythos 5.1 60.9%, Fable 5 42.0%, Opus 5 52.3%, GPT 37.3%
- Knowledge work, GDPval-AA v2: Fable 5.1 1853, Fable 5 1723, Opus 5 1824, GPT-5.6 Sol 1711
- Computer use, OSWorld 2.0 partial: 77.9% vs 72.9% (Fable 5) vs 75.4% (Opus 5); strict: 41.7% vs 36.1% vs 39.6%
- Multidisciplinary reasoning, Humanity's Last Exam: 60.9% no tools (vs 57.8% / 56.6%), 65.0% with tools (vs 63.8% / 63.6%)
- Business workflows, AutomationBench: 31.4% vs 17.1% (Fable 5) vs 26.9% (Opus 5) vs 19.6%
- Agentic coding, CursorBench 3.2.0: 73.4% vs 70.5% vs 70.0% vs 67.2%

Fable 5.1 avoids shortcuts that result in poorer-quality work, and it’s smart enough to fix the root causes of software issues. Example: in testing by Millennium, Fable 5.1 found the cause of a rare crash that none of its engineers (or any other model) had explained after several years.

## Scientific research

**Molecular design.** Mythos 5.1 proved able to design very high-affinity binders. On three targets (EGFR, Nipah G, 15-PGDH), binding affinities were 10 times higher than the best designs submitted to Adaptyv Bio’s protein design competitions. Hit rate reached nearly 50% across 12 targets (typical: 10–15%).

**Computational analysis and modeling.** Claude Fable 5.1 trained a neural network to create a new, high-resolution elevation map of a third of the planet Venus, based on NASA Magellan radar images. Details down to 2–3 km (vs 10–20 km), heights up to 25% more accurate. Map released under Creative Commons via Zenodo.

**Computational biology.** Mythos 5.1 sped up seven open-source deep learning models by up to 2.5x (identical outputs) via custom GPU kernels and caching, cutting estimated genome-wide GPU costs 30–60%.

## Safety, security, and alignment

- Chemical/biological: Mythos 5.1 greater than Mythos 5 but still below next Responsible Scaling Policy risk tier; deployed with same safeguards as Mythos 5.
- Cyber: strongest cyber capabilities of any released Anthropic model, lower risk category of Frontier Compliance Framework; no critical-severity jailbreak found.
- Agentic safety: refusal rates comparable to Mythos 5/Sonnet 5/Opus 5; most robust to date on external prompt-injection benchmark.
- Alignment: better aligned than Mythos 5 on most metrics; less likely to access out-of-scope resources, use motivated reasoning, or ignore constraints; lower reward-hacking rate.
- Enterprise Frontier Safeguards (EFS): customer-controlled cloud storage, customer-led human review by default; rollout starting fall 2026 on Claude Code/Enterprise/Platform, Bedrock, Google Agent Platform, Microsoft Foundry.
- Biology safeguards fire 85% less often for benign elementary biology/medical queries; cyber safeguards average ~60% fewer interventions per session.
- Anti-distillation: new API accounts cannot manually edit Claude’s prior context while preserving prior thinking transcript.

## Trusted access for Claude Mythos 5.1

- Cyber Verification Program (CVP) for defensive security work; Mythos-class access coming soon.
- Life Sciences Verification Program (LSVP) with US government partnership; first participants enrolled.

## Compliance with the EU AI Act

Signed Code of Practice on Transparency of AI-Generated Content; invisible watermark in outputs of models released after Aug 2, 2026; detection API in private preview for eligible organizations.

## Cost and availability

Available today on all platforms including AWS, Google Cloud, Azure. API id: `claude-fable-5-1`. Cache reads now $0.25/MTok (75% less). Typical workloads ~25% cheaper than Fable 5; highly agentic up to ~45% cheaper. Otherwise $10/M input, $50/M output. Mythos 5.1 for vetted US cyberdefense/life-science organizations, expanding with US government coordination.

[truncated for edition-local storage]
