# SOURCE EXCERPT (bounded) — Context Language Models full text via ar5iv (paper body READ)

- artifact_class: COPYRIGHT_BOUNDED_EXCERPT
- source_url: https://ar5iv.org/html/2609.37725 (HTML rendering of arXiv 2609.37725v1; CC-BY-4.0 per PDF metadata)
- retrieved_at: 2026-10-10T05:27:24Z (Muse webfetch text; ar5iv rendering, NOT the PDF bytes)
- access_mode: webfetch-read full text §§1–6 + References + Appendix A (partial; output truncated ~48KB); bounded excerpt archived
- redistribution: bounded quotation only (CC-BY-4.0 paper; excerpts attributed)
- claim_location_anchors: title/authors/affiliations; Abstract; §1 Bitter Lesson framing; Eq.1–2 (append vs model-controlled transition); Fig.3 qualitative behaviors; §4.1 context-as-file + Bash + multi-agent files; prefix-reuse FLOPs Eq.3; §4.2 skill evolution Eq.4–5 + GRPO Eq.6 (success-gated efficiency); §4.3 SCR + Fig.4; §5.1 BCP/TB2.1/TBLite/Table 1 math; EdgeBench-10/Software World Fig.8; §5.2 steering/Fig.9-10/RL Table 2; §5.3 SCR 65%; §6 safety (compaction-summary prompt-injection persistence, OpenAI 2026b); code URL; funding

## Bounded quotes (methods/conditions)

> `c_{t+1}=f^{CLM}_{θ}(c_t)` vs append-only `c_{t+1}=c_t⊕f^{LM}_{θ}(c_t)` (Eq.1–2); `We mirror the LM's live context as a directly editable file ... using general Bash commands`
> `prefix-reuse FLOPs` = prefill(unmatched suffix from first prefix mismatch) + decode(new tokens) (Eq.3)
> `A^{eff}_i = clip((c̄_g − c_i)/c̄_g, −1, 1)` for successful trajectories, 0 otherwise (Eq.6, success-gated efficiency; <2 successes → all 0)
> `We evaluate all methods out of the box without training` (Qwen3.6-27B 32K, 100-turn cap; BCP/TB2.1/TBLite)
> `On BCP, CLMs outperform all baselines, scoring 59.4% ... exceeding Codex-style summarization by 11.4% relative ... 21.5% and 28.9% fewer prefix-reuse FLOPs than summarization and MEM1`
> `match ... Codex-style summarization, on TB2.1 while using only 70% of its prefix-reuse FLOPs, and exceed it on TBLite (73.7% against 67.0%)`
> `CLM reaches 44.6 using 179 prefix-reuse PFLOPs per trial, versus 42.3 and 437 PFLOPs for summarization` (EdgeBench-10 Qwen3.6-27B; Claude 4.6 Sonnet 51.0/50.4 vs 42.3)
> `CLM achieves 65% greater downstream speedup over the initial releases` (Software World swarm, same spend; extrinsic held-out packages)
> `After RL, it gains 13.7 points to 42.5%, matching the trained summary harness while using 1.34 versus 2.19 PFLOPs per question` (Qwen3.5-9B OpenResearcher; Table 2: Summary 34.7→42.1/4.01→2.19; CLM 28.8→42.5/1.52→1.34)
> `SCR effectively reduces cache re-prefilling, matching standard SGLang serving with 65.0% of its empirical prefix-reuse FLOPs` (BCP Qwen3.6-27B; §5.3: −35% server compute matched perf)
> `Editable context can become another channel through which prompt injections or self-generated instructions persist across turns` (§6; cites OpenAI 2026b compaction-summary injections)
> `Code: https://github.com/facebookresearch/context-language-models`; authors UW/Meta/MIT/Trillium (Shao, Shen, Yin, Li, Wang, Ivison, Poovendran, Lambert, Xiao, Lewis, Yih, Zettlemoyer, Koh)

## Retrieval method note (honest)

- Direct `https://arxiv.org/pdf/2609.37725` fetch returned BINARY PDF bytes (unreadable as text; metadata confirmed: Title/authors/CC-BY-4.0/arXivID v1) → method failure for PDF-byte consumption, recovered via ar5iv HTML rendering of the same v1 paper.
- Verification target renamed: `arxiv-2609-37725-fulltext-ar5iv` (VERIFIED) + explicit `PDF bytes NOT consumed` limitation.

## Explicitly unread portions

- Figures/images (Fig.1–11 render as garbled math/placeholders in HTML text extraction); equation rendering partially garbled (reconstructed above from context).
- Output truncated before Appendices B–F (SCR impl details, FLOPs accounting, full setups, ablations); Appendix A (extended related work) partial.
- Code repo not opened; no reproduction.
