# Repowise benchmark repository methodology

- Source URL: https://github.com/repowise-dev/repowise-bench
- Source/page title: repowise-bench
- Retrieved at (UTC): 2026-08-30T10:16:12Z
- Explicit benchmark date stated by the source: the README does not give a single publication date; referenced runs are under `results/bakeoff_2026_08/`.

## Source-local observations

- The repository describes itself as the evidence and rerun harness behind the numbers published by Repowise, with public repositories, pinned commits, scripts, raw outputs, and losing rows retained.
- Its README describes a field comparison for retrieval/file coverage and agent-loop work, including a project-reported 0.876 versus 0.610 file-coverage comparison on a sealed n=42 set and -31.6% output tokens on n=43 agent questions. These are benchmark-repository claims, not independent reproduction in this capture.
- The README documents failure controls: it records raw responses and served tool lists, checks extractors against known-correct/known-wrong cases, and warns that a dead arm or broken extractor can look like a zero.
- The repository README says the head-to-head and agent-loop comparisons use pinned data/configuration and that the underlying reports contain sample sizes, methods, caveats, and losing rows.

## Attribution and limitations

- All benchmark identities, numbers, and methodology descriptions above are project-reported by Repowise.
- The repository documents that some runs require an OpenAI key, paid coding-agent subscriptions, or other accounts; a checkout alone does not reproduce every row.
- This capture establishes the project's benchmark methodology and audit posture only. It does not independently rerun or validate the reported performance.
