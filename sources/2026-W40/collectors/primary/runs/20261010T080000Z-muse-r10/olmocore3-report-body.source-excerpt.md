# SOURCE EXCERPT (bounded) — Olmo-core 3 technical report PDF text (E01 first priority)

- artifact_class: COPYRIGHT_BOUNDED_EXCERPT
- source_url: https://allenai.org/papers/olmocore3 (serves report PDF; curl followed to PDF bytes)
- retrieved_at: 2026-10-10T08:54:32Z (curl + pdftotext; PDF metadata below, NOT byte-identical PDF archived)
- access_mode: full PDF text extracted locally (570,369 chars); bounded excerpt archived
- redistribution: bounded quotation only
- PDF metadata: Title `Supercharging Olmo-core for Efficient and Scalable MoE Training`; Authors Tianhua Tao,
  Akshita Bhagia, Dirk Groeneveld, Pete Walsh, Tyler Romero, Yashas Samaga, Jacob Morrison, Iz Beltagy,
  Taira Anderson, Noah A. Smith, Hannaneh Hajishirzi (UW/Ai2); LaTeX pdfTeX; CreationDate Oct 1 14:36:19 2026 JST;
  Code: Olmo-core; Date October 2026.

## Bounded quotes (methods/conditions found in report BODY — upgrades blog-only reporter level)

> `We switch from the Fully Sharded Data Parallel (FSDP) used by previous Olmo-core versions to a
> parallelization architecture built on Distributed Data Parallel (DDP). On top of it, we add Expert
> Parallelism (EP), Pipeline Parallelism (PP), a distributed optimizer`
> `On NVL8 B300 nodes, the stack supports training configurations from 12.9 billion to 1.2 trillion total
> parameters on up to 512 GPUs, reaching 858 useful-model TFLOP/s/GPU at 1.2 trillion with MXFP8 and per-layer
> recompute; an experimental capacity test with the optional DeepEP v2 backend reaches 2.38 trillion.`
> `Combining both paths gives the highest throughput, about 21% above the BF16 reference` (MXFP8; rank-0 profiles
> Fig.59; MXFP8 targets 65% of BF16 kernel time)
> `we identify a failure pattern we call Token Gerrymandering, in which the MoE router learns to hack the
> load-balancing loss, and find that overlapping communication with computation can slow the overlapped kernels`
> Report structure consumed (ToC-verified): §§2–7 parallelism/DDP/EP/PP/hardware-mapping, §§8–13 sync-free/grouped-GEMM/
> routing/MXFP8/checkpoints/recompute, §14 production throughput matrix, §15 optimization lessons (PCIe offload limits,
> wave/two-batch overlap, MegaMoE kernel, Wgrad layout, CUDA graphs), §§16–20 LR scaling/sparsity/upcycling/GEMM timing/
> shared expert — section bodies beyond the quotes above NOT line-consumed.

## Explicitly unread / reporter-level remainder

- §14 run-matrix cell values, §16–20 ablations, appendices, figure values: NOT consumed (ToC-verified existence only).
- Blog-only 2.7× micro-benchmark (52k vs 19.4k tok/s/GPU, 8×B300) NOT located in report text — stays blog-level.
- Code repo internals not opened. No independent reproduction.
