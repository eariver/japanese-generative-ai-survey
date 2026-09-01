# Repowise benchmark reproduction instructions

- Source URL: https://github.com/repowise-dev/repowise-bench/blob/master/repro/README.md
- Source/page title: Reproducing the bakeoff
- Retrieved at (UTC): 2026-08-30T10:16:12Z
- Explicit reproduction-document date stated by the source: not stated on the page; the referenced pre-registration is identified as committed `83d970b` before its run.

## Source-local observations

- The reproduction README says every published number comes from a run in the repository, with raw output kept under `results/bakeoff_2026_08/`; it lists the cost, wall-clock time, and credential requirements for each claim.
- The retrieval claim uses ContextBench with 112 instances split into a 70-instance development half and a 42-instance sealed half, pinned by instance ID. The README says grading is deterministic against gold spans and uses no LLM judge.
- The agent-loop section documents byte-identical prompts for every arm, an environment-isolated bare-agent control, and explicit harnesses for adoption and judge-agreement checks. It records a 0.69-point judge disagreement noise floor on django and a paired-delta standard deviation of 2.23 on one arm.
- The README explicitly limits interpretation: retrieval is not task success, quality equivalence was not established by a TOST, the hosted rows require subscriptions/keys, and the agent runs use `django/django` or `pallets/flask` at one commit.

## Attribution and limitations

- Reproducibility, split design, paired setup, noise measurements, costs, and limitations are claims documented by the project.
- The local `qwen3:8b` arm is described as reproducible without an account, while other rows require credentials or paid services; no row was independently rerun in this capture.
- The benchmark/repository scope and the distinction between retrieval/work reduction and general task success must travel with any downstream claim.
