# 2026-W32 High-Risk Claim Review v0.1

Status: **passed; no blocking wording change required**  
Date: 2026-08-10

This review checks claims whose compression or miswording would materially change the technical meaning of the issue. It is not a new source-collection pass.

## 1. OpenAI Astra — mathematics / theoretical CS

### Article wording under review
The Lead Story states that OpenAI published ten Astra-attributed mathematics/theoretical-CS results, characterizes them as OpenAI claims, notes manuscript preparation and Lean certificates, and explicitly separates independent mathematical validation.

### Evidence boundary
The candidate record supports:
- ten results attributed to an internal Astra version;
- OpenAI's statement that they resolve or substantially advance long-standing open problems;
- human manuscript preparation with the model;
- Lean formalization;
- approximately USD 2,000 Sol-API-equivalent solution-search cost across the set.

It does **not** establish independent mathematical acceptance of all ten results.

### Result
**PASS.** The article does not convert OpenAI's characterization into an independent claim that ten problems have definitively been solved.

## 2. OpenAI Astra — Critical cyber capability

### Article wording under review
Late Breaking says OpenAI **could not rule out Critical cyber capability**, not that Astra had been definitively classified Critical.

### Evidence boundary
The primary-screened record explicitly requires this distinction and records strengthened controls plus pausing internal Astra activities that did not meet them.

### Result
**PASS.** No sensational upgrade from `cannot rule out Critical` to `is Critical` is present.

## 3. OpenAI third-party cyber evaluations

### Article wording under review
The Safety Deep Dive describes UK AISI boundary events and the Irregular incident while stating that the latter resulted from evaluation-environment misconfiguration and was not a sophisticated sandbox escape or zero-day.

### Evidence boundary
The candidate record says these incidents concern evaluation design, authorization boundaries and reduced safeguards/misconfiguration. It explicitly forbids summarizing them as generic production sandbox escape behavior.

### Result
**PASS.** The article preserves the evaluation-environment boundary and does not generalize the incidents to normal deployment behavior.

## 4. Kimi K3 low-RAM community experiment

### Article wording under review
The Model & Open Weight article says a community post claimed roughly 8.24 GB peak RAM using disk-streamed experts, labels it a community experiment, notes the approximately 1.56 TB official repository, and frames the result as a RAM/storage/I/O/latency trade-off.

### Evidence boundary
The candidate record explicitly says the 8.24 GB figure, correctness and token speed are not independently reproduced technical facts.

### Result
**PASS.** The article does not present 8.24 GB as an official requirement or validated practical deployment configuration.

## 5. DeepSeek-V4-Flash-0731 benchmark wording

### Article wording under review
The article identifies 0731 as a re-post-trained update with the same architecture/size as Preview and says vendor benchmark values depend on maximum effort, temperature and harness settings. It refuses to place Qwen/DeepSeek/Kimi scores into one unified ranking table.

### Evidence boundary
The candidate record and verification layer require harness-aware interpretation.

### Result
**PASS.** Benchmark conditions and event chronology remain visible.

## 6. PRWeaver

### Article wording under review
The Safety Deep Dive says decomposition alone has a smaller effect than benign interleaving/carrier fusion in the authors' benchmark, quotes the whole-window degradation, and immediately states that the numbers are not universal real-world malicious-PR detection rates.

### Evidence boundary
The reviewed paper record restricts the result to 10 repositories, 208 execution-validated synthetic attacks, heavily Python-skewed data, and specific auditors/renderings.

### Result
**PASS.** The article keeps the result at the level of review-context/harness design rather than claiming that LLM reviewers generally miss a fixed percentage of real attacks.

## 7. SparSEEty

### Article wording under review
The Safety Deep Dive describes a PowerInfer-style sparse-inference / Intel TDX setting, host-observable access patterns, author-reported BLEU and monitoring overhead, and explicitly rejects the interpretations `TDX is broken` and `all sparse LLMs leak prompts`.

### Evidence boundary
The reviewed paper record requires architecture- and threat-model-specific wording and notes that attack quality changes materially when the observable channel is weakened.

### Result
**PASS.** Threat-model scope is preserved.

## 8. Disaggregation / HeteroPanacea

### Article wording under review
The Serving section emphasizes the conditional result: decode-heavy/balanced workloads can favor non-disaggregated serving, while the strongest 2.06× figure is a simulation result in a richer custom-NPU design space. It states that validation is component-level rather than end-to-end production validation.

### Evidence boundary
The paper review explicitly forbids phrasing the 2.06× figure as production throughput and says commercial-GPU benefit is narrower/environment-dependent.

### Result
**PASS.** The headline conclusion remains `disaggregation is conditional`, not `PDAF is 2.06× faster`.

## 9. Shieldstral

### Article wording under review
The Safety Deep Dive reports the authors' 3B model and F1 values but says competing systems do not use identical decision mechanisms/reasoning settings and that independent adversarial validation is absent.

### Evidence boundary
The full-paper review says universal SOTA, identical-condition 3B-vs-20B equivalence and real-world 91.3% accuracy are not established.

### Result
**PASS.** The article treats runtime policy specification as the important design point rather than overstating benchmark superiority.

## 10. Cross-issue editorial synthesis

### Claim under review
The cover and Safety Deep Dive use the synthesis that the evaluation unit is expanding from the model checkpoint to the surrounding system: research workflow, harness, context, serving infrastructure and runtime policy.

### Result
**PASS AS EDITORIAL SYNTHESIS.** Multiple independently verified items support the pattern, and the Safety article explicitly states that the underlying security cases do not share one cause or threat model. The cover phrasing does not replace event-level evidence.

## Gate

High-risk claim wording is acceptable for the current source revision.

Remaining freeze blocker:

- full v0.2 LuaLaTeX+biber rebuild and rendered-page visual comparison after the editorial/source-template changes.

No new primary-source verification is required unless subsequent prose edits expand a claim beyond the reviewed wording.
