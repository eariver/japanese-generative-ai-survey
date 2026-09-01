---
issue_id: "2026-W32"
candidate_id: paper-prweaver
evidence_type: full-paper-review
review_status: full-reviewed
primary_source: "https://arxiv.org/abs/2608.02693"
publication_date: "2026-08-03"
claim_authority: author-reported-security-benchmark-results
---

# PRWeaver — Full Paper Evidence Review

## Paper
**PRWeaver: Evaluating LLM-Based Code Auditors against Long-Horizon Malicious Pull Requests**  
arXiv:2608.02693

## Research question
PRWeaver asks whether LLM-based code-review/auditing agents can detect a malicious capability that is deliberately distributed across a sequence of individually plausible pull requests, especially when benign work is interleaved or fused into the reviewed context.

The central security concept is **compositional / long-horizon review failure**: locally understandable diffs can combine into a security violation whose consequence is harder for an auditor to maintain across review context.

## Benchmark construction
The authors build attacks against pinned revisions of real repositories and require executable validation.

Each accepted attack is decomposed into an ordered component chain and rendered under four conditions:
- R0: monolithic attack in one PR;
- R1: attack components split into dependency-ordered PRs;
- R2: genuine upstream benign PRs interleaved between malicious components;
- R3: each malicious component fused with a genuine upstream change and a coherent combined PR description.

Crucially, R2/R3 alter presentation/context while preserving the planted malicious mechanism.

## Admission / validation criteria
The paper applies strong functional checks:
- every prefix must build and pass relevant host tests;
- the exploit PoC must remain inactive before the complete chain;
- the full chain must reproduce the monolithic PoC outcome;
- leave-one-out removal of each malicious component must disable the exploit without breaking the repository;
- renderings are rejected for flaky PoCs, unstable builds, lost anchors or semantically interfering carrier changes.

Two human reviewers also judge production reachability, PoC/impact match, plausibility of PR boundaries/carriers and metadata consistency. The paper reports 94.1% raw pre-adjudication agreement and Cohen's kappa 0.87.

Primary locator: Benchmark Validation section.

## Benchmark scale and composition
The released benchmark contains:
- **208 execution-validated attacks**;
- **832 matched renderings** (four per attack);
- **10 repositories**.

Language distribution is heavily skewed:
- Python: 195 attacks;
- TypeScript: 13 attacks.

Repository counts include Pretix (60), Django (46), Flask (22), Wagtail (19), django-allauth (14), Bottle (14), Vendure (13), Flaskr (7), Werkzeug (7), DRF (6).

Primary locator: Table 1.

## Auditor evaluation
The paper evaluates OpenCodeReview, Claude Code and GitHub Copilot Code Review across multiple model configurations. A controlled comparison fixes Claude Haiku 4.5 across all three auditor frameworks to isolate workflow effects.

## Key author-reported findings
### Decomposition alone has limited effect
Across systems, R1 changes detection rate by only roughly **0–5 percentage points** relative to monolithic R0 in the reported six-system comparison.

### Interleaving and coherent carrier fusion hurt more
At R2 with N=16 interleaved benign PRs, detection rate falls by **5–13 points** relative to R1; R3 carrier fusion produces a **10–18 point** reduction in the reported comparison.

### Active review-window composition matters more than repository history alone
With Haiku 4.5 fixed, per-PR detection across N={0,8,16,24} changes:
- OpenCodeReview: 60%, 57%, 55%, 50%
- Claude Code: 71%, 70%, 65%, 60%
- Copilot Code Review: 62%, 64%, 56%, 54%

Under whole-window review, the reported detection rates fall much more sharply from N=0 to N=24:
- OpenCodeReview: 56% → 16%
- Claude Code: 67% → 22%
- Copilot: 61% → 22%

The authors therefore argue that the strongest degradation comes when benign and attack-bearing PRs jointly occupy the **active reviewed context**, rather than merely existing in repository history.

Primary locator: §R2 Across Review Settings / Figure 5.

## History-access ablation
At N=16, hiding repository-history inspection reduces detection only moderately:
- OpenCodeReview: 55% → 44%
- Claude Code: 65% → 61%
- Copilot: 56% → 52%

The authors interpret this as evidence that history access helps, but cannot by itself explain the much larger whole-window degradation.

## Interpretation boundary
The paper does not identify a single internal LLM mechanism responsible for the failure. It demonstrates a review-context boundary condition and gives qualitative examples where auditors identify relevant code changes but fail to synthesize their combined security consequence.

## Generalization caveats from review
The paper's strongest claims should travel with these benchmark boundaries:
- 10 repositories, overwhelmingly Python;
- malicious chains are synthesized and execution-validated rather than naturally observed attacks;
- review outcomes depend on specific auditor interfaces, prompts/models and context presentation;
- detection-rate changes characterize this benchmark and are not universal rates for all repositories/security tasks.

## Evidence assessment
### Supported by the paper
- The benchmark enforces executable/leave-one-out validity rather than relying only on textual vulnerability labels.
- Simple PR decomposition is much less damaging than interleaving/fusion in the reported tests.
- Whole-window context can degrade detection substantially even when relevant history is available.
- Auditor workflow contributes materially in addition to underlying model capability.

### Author-reported metrics only
All detection/evasion rates are benchmark results and have not been independently reproduced here.

## Safe editorial statements
- PRWeaver tests security failures that emerge **across pull requests**, not merely within one diff.
- In the authors' benchmark, benign interleaving and coherent carrier fusion reduce detection more than splitting an attack into multiple PRs by itself.
- The steepest reported degradation occurs when benign and malicious changes share the active review window, suggesting that context organization is a security property of coding-agent review systems.

## Do not claim
- “LLM code reviewers miss 80% of real malicious PRs.”
- “Longer context inherently makes auditors worse.”
- “Repository history is useless.”
- “The benchmark proves a particular model architecture is fundamentally incapable of compositional security review.”

## Editorial significance before selection
Strong Agent Security candidate because it moves the unit of evaluation from single diff/repository snapshot to longitudinal review context. It can complement product-level agent security material without depending on a vendor launch.