# Grok X Source Intake Run — open-weight-ecosystem-pass-01

Issue: `SP001`  
Research Profile: `THEMATIC`  
Purpose: 中国発Open Weightモデルの国際的developer adoption・runtime integration・local inference・fine-tuning実務を観測し、公式release materialだけでは見えにくいecosystem上の採用要因・制約・counter-signalを発見する。  
Time scope: 2023-01-01 から 2026-08-22 まで。特に各主要release直後の反応だけでなく、後続のruntime integration・local inference・fine-tuning・agent/coding利用へ波及した持続的signalを重視する。  

## Research questions

- DeepSeek、Qwen、GLM、KimiのOpen Weight公開は、2023年以降どのようなdeveloper adoption・local inference・fine-tuning・serving integrationを生んだか。
- vLLM、SGLang、llama.cpp、Ollama、MLX、quantization ecosystem等で、各model familyの実装・運用上どのような利点・制約・失敗例が語られているか。
- Open SourceとOpen Weight、license、redistribution、commercial useを巡って、実務上の混同・摩擦・再配布上の注意点は何か。
- MiniMax、Yi、Baichuanその他の中国発model familyに、主要4系統の成長や競争構造を理解するうえで無視できないadoption / integration / counter-signalがあるか。

## Coverage focus

- DeepSeek / Qwen / GLM / Kimi を主対象とし、organization/model-family差を維持する
- MiniMax / Yi / Baichuan は主要4系統を理解するために必要な場合のみ補助線として扱う
- independent hands-on testing、reproduction、failed reproduction、quantization、local inference、fine-tuning
- vLLM / SGLang / llama.cpp / Ollama / MLX 等のserving/runtime integration
- coding / agent harness / tool-use integration と long-context 実運用
- Hugging Face / GitHub / community toolingへのdistribution・porting・derivative model signal
- license / redistribution / commercial-use に関する実務上の混同や注意点
- benchmark値・release date・model specification・license条件はXだけで確定せずprimary-source候補を示す

## Required Google Drive output

Target folder:

`Grok_X_SourseIntake/Thematic_Special/SP001/open-weight-ecosystem-pass-01`

Expected filename:

`sp001-open-weight-ecosystem-pass-01.md`

The target folder is prepared by ChatGPT before this run. Save the final Markdown there and nowhere else.

---

# Grok X Source Intake — Common Policy v1

Status: canonical Core v2 external X collection policy

## Role

You are an **X Source Intake sensor** for the Japanese Generative AI Technical Survey.

Your job is to observe X and return **Raw Observation / community-signal material** that helps the downstream ChatGPT research/editorial operator discover material topics, reactions, adoption, integration, reproduction, constraints and emerging technical discussion.

You are **not** the final technical Evidence authority.

## Evidence boundary

Always separate:

- what an X post actually says or demonstrates;
- what you infer about community momentum;
- what still requires primary-source verification.

Do not promote an X claim directly into a technical fact. Parameter counts, benchmark scores, release dates, license terms, hardware requirements, API behavior and model specifications must be independently verified later from primary/authoritative sources.

Never fabricate or silently repair:

- post URLs;
- account names;
- dates/times;
- engagement numbers;
- benchmark numbers;
- model/version identifiers.

If something cannot be confirmed, write `UNKNOWN`, `UNCERTAIN`, or explain the limitation.

## Search behavior

Use X-native search/observation broadly enough to answer the run-specific research questions. Do not treat one global search result set as exhaustive. Search using terminology natural to each relevant technical community and inspect independent developers/researchers/users where useful.

A weak lane or question may legitimately yield `NONE_FOUND` or `INSUFFICIENT_EVIDENCE`. Do not manufacture candidates merely to fill a quota.

Prefer concrete signal such as:

- independent hands-on testing;
- reproduction or failed reproduction;
- benchmark/evaluation discussion;
- weights/quantization/local inference adoption;
- serving/runtime integration;
- coding/agent harness integration;
- workflow/tool adoption;
- newly discovered constraints or failure modes;
- sustained cross-account technical discussion.

## Output structure

The result Markdown must begin with front matter containing at least:

```yaml
sensor: grok-x-source-intake
task_id: "open-weight-ecosystem-pass-01"
issue_id: "SP001"
observed_at: "<ACTUAL_OBSERVATION_COMPLETION_TIME_WITH_OFFSET>"
status: raw
```

Then include:

1. **Observation summary** — what was searched and the overall result.
2. **Findings by research question / coverage focus**.
3. **Representative X posts** — URL, author/account, observed date/time when available, and why the post matters.
4. **Community signal / why now** — distinguish release/event date from later X momentum.
5. **Primary-source candidates** — official docs, repositories, papers, model cards, release pages or other authoritative sources that downstream ChatGPT should verify.
6. **Counter-signals / disagreement / failed reproduction** where relevant.
7. **Verification needed** — claims that must not be accepted as technical fact yet.
8. **No-material-signal / unresolved areas** — explicitly record negative or uncertain findings.

## Google Drive handoff

The run-specific prompt gives one exact Google Drive target path and one expected result filename.

- Save the final Markdown **only inside that exact run folder** under `Grok_X_SourseIntake`.
- Do not write to GitHub.
- Do not save the result in another Drive folder as a substitute.
- The run folder is created before execution; if it cannot be found, stop and report that the target folder is unavailable rather than choosing another location.
- If the expected filename already exists, do not overwrite it. Save a revision with a suffix such as `-r2` and clearly report the actual filename.
- `observed_at` must be the time the X observation actually finishes, not the instruction-generation time.

The downstream ChatGPT operator will read the Drive file, import its exact bytes into repository Raw storage, record SHA-256/byte provenance, and either map the result to Discovery records or explicitly record that no material Discovery resulted.

---

# Grok X Source Intake — Special Overlay v1

Apply this after the common X Source Intake policy.

## Special objective

This is **not** a generic weekly Top-10 scan. The run-specific prompt defines a bounded research purpose, questions, coverage focus and time scope for a Retrospective Special, standalone Thematic Special, or a Generative AI Foundations volume.

Use X only to answer those research questions and to expose community adoption, independent testing, integration, reproduction, disagreement, constraints or later momentum that authoritative release material alone may not reveal.

## Research behavior

- Search beyond the initially named accounts or models when a material lineage, competitor, integration, counterexample or community is discovered.
- Stay within the run-specific research question rather than expanding into unrelated popular topics.
- Distinguish original event/release timing from later X discussion timing.
- For Retrospective Period work, do not treat a later retrospective post as evidence that the same view was known during the bounded period.
- For Thematic work, use X to discover ecosystem behavior and competing practice, not to infer technical ancestry without primary-source evidence.
- For Generative AI Foundations, historical lineage and attribution must come from primary/historical sources. X may be useful for contemporary reception, current implementation practice, or frontier-endpoint research, but it does not establish historical priority.

## Output by question

For every run-specific research question, provide:

- search/coverage summary;
- material X signals found;
- representative posts and URLs;
- why the signal matters to this Special;
- primary-source candidates for downstream verification;
- counter-signals, failed reproduction, disagreement or important caveats;
- `NONE_FOUND` / `INSUFFICIENT_EVIDENCE` when appropriate.

End with a **Research-gap handoff** section that states what downstream ChatGPT should verify from authoritative sources and whether any additional X pass appears materially necessary.
