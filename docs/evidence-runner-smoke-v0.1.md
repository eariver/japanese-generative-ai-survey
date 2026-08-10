# Evidence Runner Smoke Test v0.1

Date: 2026-08-10

Status: automation smoke evidence only. This document does **not** reopen or modify the frozen 2026-W32 editorial selection.

## Purpose

Exercise the transition:

`Screening -> duplicate grouping -> Evidence Task -> primary-source verification`

using a real retained screening group from the W32 source-intake replay.

## Input screening group

`duplicate_group: llama.cpp-deepseek-v4-support`

Retained screening items:

1. `github-release:ggml-org/llama.cpp@b10228`
2. `github-release:ggml-org/llama.cpp@b10231`
3. `github-release:ggml-org/llama.cpp@b10232`

All three were screened `KEEP` in the interactive GPT-5.6 Sol smoke run.

## Primary sources inspected

- llama.cpp release b10228: https://github.com/ggml-org/llama.cpp/releases/tag/b10228
- llama.cpp PR #25784: https://github.com/ggml-org/llama.cpp/pull/25784
- llama.cpp release b10231: https://github.com/ggml-org/llama.cpp/releases/tag/b10231
- llama.cpp PR #26458: https://github.com/ggml-org/llama.cpp/pull/26458
- llama.cpp release b10232: https://github.com/ggml-org/llama.cpp/releases/tag/b10232
- llama.cpp PR #26459: https://github.com/ggml-org/llama.cpp/pull/26459
- DeepSeek official model repository: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
- DeepSeek official API change log: https://api-docs.deepseek.com/updates/

## Grouping resolution

**Accepted as an unconfirmed editorial series for Evidence work.**

The three llama.cpp releases are separate implementation events, but they share a coherent technical theme: local/runtime enablement for DeepSeek V4 and its speculative-decoding / architecture-specific execution paths.

This does not mean they should become three article items. It means they can be verified together before editorial selection.

## Verified facts

### b10228 / PR #25784

- Release b10228 was published on 2026-08-02 and is titled `DeepseekV4 MTP + DSpark`.
- PR #25784 was merged into llama.cpp on 2026-08-02.
- The PR adds runtime work for DeepSeek V4 speculative decoding, including DSpark.
- The PR explicitly notes that the 2026-07-31 DeepSeek checkpoint should use DSpark rather than an MTP module shipped with the checkpoint.
- The PR contains contributor-reported performance measurements. Those measurements are project/contributor claims, not independent benchmark evidence.

### DeepSeek-V4-Flash-0731

- DeepSeek's official model repository identifies `DeepSeek-V4-Flash-0731` as the official DeepSeek-V4-Flash release and says it supersedes the preview release.
- DeepSeek states that the checkpoint has the same model structure as its DSpark variant and includes a speculative-decoding module.
- DeepSeek documents DSpark serving for both vLLM and SGLang.
- The SGLang instructions state that no separate speculative draft model path is required because target and draft weights come from the same checkpoint.
- DeepSeek's API change log dates the API update to 2026-07-31 and says the 0731 model keeps the same architecture and size as the preview and was re-post-trained.

### b10231 / PR #26458

- Release b10231 was published on 2026-08-02.
- PR #26458 was merged on 2026-08-02.
- The change makes `dspark-` files resolve as speculative sidecars.
- It documents `-hfd` handling, explicit `-md` disabling discovery, and automatic preference of DSpark over dflash when no type is requested because the DSpark sidecar carries the extra Markov head.

### b10232 / PR #26459

- Release b10232 was published on 2026-08-02.
- PR #26459 was merged on 2026-08-02.
- It implements DeepSeek V4 hyper-connection operations for Metal: `GGML_OP_DSV4_HC_COMB`, `GGML_OP_DSV4_HC_PRE`, and `GGML_OP_DSV4_HC_POST`, plus Metal dispatch/support plumbing.

## Claims that remain bounded

The smoke test intentionally does **not** promote the following to verified general facts:

- that every llama.cpp backend is end-to-end verified for DeepSeek V4;
- that release-asset availability for a backend proves DeepSeek V4 correctness/performance on that backend;
- that the PR #25784 contributor benchmarks generalize beyond their tested hardware/configuration;
- that the Metal implementation has a verified Apple-hardware performance gain from the sources inspected here;
- that every DeepSeek V4 configuration requires the same hyper-connection execution path.

These remain Evidence limitations or unresolved verification targets.

## Automation findings

1. `duplicate_group` was useful: three high-frequency llama.cpp releases collapsed into one coherent Evidence investigation rather than three candidate stories.
2. `duplicate_group` must remain unconfirmed until primary-source inspection.
3. Full backend support is a separate verification question from a merged implementation or published binary asset.
4. OSS project/contributor benchmark claims require attribution and must not become independent performance facts.
5. Evidence Tasks should be stored one-file-per-task so the exact task bytes can be SHA-256-bound to an Evidence Run.

## Outcome

The Evidence Task / Evidence Card design is suitable to proceed to automated task generation and provider-agnostic Evidence Runs.

The next implementation boundary is to merge validated Evidence Runs into a candidate-ready queue while keeping `CANDIDATE`, `HOLD`, `REJECT`, and `INSPECT_MORE` separate from final human Candidate Selection.
