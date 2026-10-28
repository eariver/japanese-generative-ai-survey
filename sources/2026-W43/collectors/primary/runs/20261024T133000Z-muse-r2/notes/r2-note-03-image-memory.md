# W43 r2 consumption note 03 — MOSS-Image + MemT-1.0 (DC-04, SUBSTANTIVELY_CONSUMED 2026-10-24)

## MOSS-Image (OpenMOSS) — repo README + arXiv abs + GitHub API meta
- Repo `OpenMOSS/MOSS-Image`: created 2026-10-16T01:18:13Z (OUT, 20h42m before window start), pushed Oct 20. 1.7k stars / 83 forks / 16 commits. License Apache-2.0 (repo file). About: 5B-parameter base DiT, text rendering, layout, efficient fine-tune.
- README News (in-window distribution events, original code/weights OUT):
  - Oct 16: Base + SFT public (code+weights) + day-0 SGLang / vLLM-Omni / ComfyUI — dated Oct 16 but repo created 01:18Z OUT; treat original release as OUT background.
  - Oct 18 IN: KohakuMossTrainer (separate repo, created Oct 18 11:08:53Z IN, 124 stars/9 forks/123 commits): full + LyCORIS (LoRA/LoCon/LoHa/LoKr/DoRA/OFT/BOFT/GLoRA/IA3/DyLoRA/T-LoRA), 6GB cards, sm70–sm120 + Intel Arc, packed varlen (fp32 err 4.7e-6, LPIPS 2.3e-6), ComfyUI/LyCORIS/merged/diffusers exports. License KohakuMoss 1.0 (Apache + name term).
  - Oct 19 IN: technical report arXiv 2610.23374 (submitted Oct 16 12:27:37Z OUT as research; README announcement Oct 19 is IN as distribution event). Citation `ai2026mossimagetechnicalreport`.
  - Oct 20 IN: MOSI API Platform availability + Playground/API.
- Models: MOSS-Image-Base / -SFT (HF + ModelScope) + Comfy-Org quantized; layout JSON (yxyx, abs_centralized, −512..512 on 1024 canvas); 4K prompts; sampler Euler 50/CFG 3/shift 5/layer-22 skip. Community: DiffSynth-Studio, DeBand, 8-step DMD, FP16-fixed, Spectrum.
- Chronology rule applied: Oct 16 code/weights = OUT; Oct 18 trainer / Oct 19 report-announce / Oct 20 API = IN as separate events. Never redatate Oct 16 release into W43.

## MemT-1.0 (MemTensor) — arXiv abs + repo README + GitHub API meta
- Paper arXiv 2610.26825: v1 Oct 19 17:54:35Z IN, v2 Oct 20 14:30:38Z IN (revision). 66pp/15 figs/16 tables. Gated DeltaNet-2 (stable token-level update) + Mixture-of-Storage; 34B training tokens; two-stage (continued pretrain + post-train); Nano + Flash family.
- Repo `MemTensor/MemT-1.0`: created Oct 19 03:29:30Z IN, pushed Oct 20. 382 stars / 17 forks / 2 commits. Family: Nano Qwen3.6-35B-A3B (36B/3B, mem 451M/10M) + Flash DeepSeek-V4-Flash (288B/17B, mem 3.61B/336M). 11 memory benchmarks Flash 1st / Nano 2nd parametric (textual-memory still ahead on long-evidence retrieval); 1.86x end-to-end @128K + 66x persistent storage vs full KV cache; experience-guided agentic coding (procedural experience in native memory, no context bloat). SGLang serve (memt_sglang, snapshots, save/resume).
- Licenses (kept separate): paper CC BY-NC-SA 4.0; repo software PolyForm Noncommercial 1.0.0 (commercial use NOT permitted); weights/datasets/benchmark assets NOT covered (terms with releases). 34B tokens = training data scale, not eval count.
