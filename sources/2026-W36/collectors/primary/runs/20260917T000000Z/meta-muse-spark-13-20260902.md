# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://research.meta.ai/blog/introducing-muse-spark-1-3
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-02
- retrieval: webfetch markdown of Meta AI Research announcement introducing Muse Spark 1.3; stored verbatim as returned.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

Introducing Muse Spark 1.3 | Meta AI Research

[Skip to main content](#main-content)

# Introducing Muse Spark 1.3

September 2, 2026·3 minute read

We’re excited to release Muse Spark 1.3, which delivers improved performance across agentic and coding tasks. Drawing on what we learned from months of broad adoption of Muse Code and Meta Model API, we’ve also made this model easier to use in real-world settings. Smarter and more practically useful, Muse Spark 1.3 advances our work toward personal superintelligence.

Muse Spark 1.3 with max reasoning is now available on Muse Code and Meta Model API. Get started at [dev.meta.ai](https://dev.meta.ai/).

![Benchmark scorecard comparing Muse Spark 1.3, Muse Spark 1.2, GPT 5.6 Sol (max), and Opus 5 (max) across agent, coding, instruction-following, and long-context evaluations.](/_next/image?url=%2Farticles%2Fintroducing-muse-1-3%2Fbenchmarks%2Fbenchmark-scorecard-v6.webp&w=3840&q=90&dpl=dpl_FmxWpmNgJXA4CjqKtTVmHwyAunDy)

For more details about our evaluations, see [our report](/static/muse-spark-1-3-multimodal-evaluation-methodology).

## Agentic Workflows

Muse Spark 1.3 is designed to better sustain longer-horizon work by collaborating with users and juggling multiple workflows in a single, long thread. When given an open-ended objective, it uses tools to generate its own context across messy and conflicting sources, proactively corrects gaps in its plan, and keeps track of what it has learned to produce a final deliverable. We trained the model across a diverse set of harnesses to generalize to various agentic environments.

Trained to more actively collaborate with the user, Muse Spark 1.3 asks clarifying questions when prompts are ambiguous, invokes help from the user when stuck, and confirms before taking consequential actions. When working on long tasks, it adapts to user preferences, either providing frequent updates or working silently in the background.

Muse Spark 1.3 follows complex, long-form instructions more reliably than earlier Muse Spark models. Across multi-step tasks, it’s better at preserving detailed requirements without dropping constraints or drifting from the requested workflow.

We’ve also improved the multitasking capabilities of Muse Spark 1.3. For example, it now more accurately maps incoming prompts to the correct task within messy, single-threaded contexts, regardless of whether the user is steering past requests or interrupting them.

The model has better awareness of its own capabilities and limitations. We trained Muse Spark 1.3 to have a better sense of what it can and can’t do, what it knows and doesn’t know, and when it hits hurdles instead of hallucinating outcomes.

## Coding

Muse Spark 1.3 was trained on more long-horizon coding tasks and shows improved usability in common engineering workflows. Relative to Muse Spark 1.2, it takes fewer turns where not needed and is less verbose, while having a cleaner overall coding style. In comparisons by Meta engineers, it proved to be significantly faster and more efficient, using ~20% fewer tool calls and ~25% fewer tokens.

## Availability

Muse Spark 1.3 is available today in Muse Code and in Meta Model API.

## Install Muse Code on macOS or Linux:

`curl -fsSL https://dev.meta.ai/install.sh | bash`

[Sign up and start building](https://dev.meta.ai)

## Safety

We’ve improved safety along several axes most relevant to agentic and coding capabilities. Muse Spark 1.3 shows stronger adversarial robustness, with improved resistance to adversarial inputs and prompt injections. On complex agentic tasks, the model has better calibration on what constitutes irreversible actions and proceeds accordingly. Together, these changes reflect better discretion and judgment in long-horizon agentic tasks.

## Looking Forward

We have an exciting roadmap lined up, including bigger models, the Muse Spark open weights release, and more. Stay tuned.
