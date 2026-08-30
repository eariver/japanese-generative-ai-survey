# Repowise Flask SWE-QA v3 benchmark

- Source URL: https://github.com/repowise-dev/repowise-bench/blob/master/BENCHMARK_REPORT_FLASK_V3.md
- Source/page title: flask SWE-QA v3: the coherent token-reduction story
- Retrieved at (UTC): 2026-08-30T10:16:12Z
- Explicit report date stated by the source: not stated on the report page.

## Source-local observations

- The report presents a v3 rerun comparing a bare arm with Repowise full/lean MCP surfaces on short read-only Q&A and a Repowise arm with `distill` on long Bash-enabled investigations.
- For short tasks (aggregate n=6), the report gives C0_bare 10.5 tool calls and 2.8 files read, C2_full 7.7 calls and 1.3 files, and C2_lean 7.7 calls and 1.7 files. It reports cost deltas of -4% for full and -25% for lean, with judge scores 8.77, 8.70, and 8.83 respectively.
- For long tasks (aggregate n=5), it reports C0_long_bare at 21.0 tool calls, 2.6 files read, and 641,553 cache-read tokens versus C2_long at 15.0 calls, 1.2 files, and 377,683 cache-read tokens (-41%), with a -26% cost delta and judge scores 9.24 versus 9.08.
- The report attributes the short-task cost difference to the curated four-tool surface (1,884 schema tokens versus 4,520 for nine tools) and the long-task difference to command-output compression via `repowise distill` plus fewer file reads.
- The report documents the arms, task shapes, tool-surface change, and the use of the current Repowise code plus pinned fixes in the benchmark setup. Within each comparison the arms are evaluated in the same reported task/harness setup; the companion reproduction README states that every arm receives a byte-identical prompt.

## Attribution and limitations

- Every number above is project-reported; no independent rerun is claimed here.
- The report says n is small (5 long, 6 short) and results are directional. It also notes that absolute cache-write/cost values are sensitive to prompt caching, while tool calls, files read, and cache-read tokens are more robust.
- Judge-score differences are not a general quality result; the project documents judge-noise and focuses the story on work reduction. Retrieval/work reduction must not be promoted to general task success.
