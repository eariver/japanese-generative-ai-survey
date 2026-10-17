# W42 primary bundle — Microsoft Maia 300 + NVIDIA Nemotron 3.5 (search-confirmed official, 2026-10-17)

Collector run: `20261017T063300Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-17T06:48:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. Microsoft Maia 300 (announced Oct 12, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- Official: https://news.microsoft.com/maia-2026/ ; https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/ (Oct 12, Guthrie); https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ (Oct 12, Borkar/Dighe).
- X: @satyanadella 2026-10-12 13:03 UTC in-window; @Azure/@Microsoft same window.
- Claims (vendor, search-confirmed):
  - 3rd-gen inference-first accelerator; inference-first architecture for long-context/decode-heavy agentic workloads.
  - System: TSMC N2P chiplet + 8x HBM4 = 288 GB @ 18 TB/s, 950W TDP (per StorageReview; treat press-spec pending official paper).
  - Rack: 96 accelerators, 167 kW, 27.6 TB HBM, 1.7 PB/s aggregate; superpod 12,288 via 2-tier Ethernet.
  - Efficiency (vendor): +40% tokens/MW vs leading GPU systems (unnamed GPU/config — cannot independently test, Maia internal-only); up to 7x rack token throughput vs Maia 200; >2.5x perf/W.
  - Timeline: Maia 200 in production (Copilot/MAI); Foundry/GitHub migration by EOY; Maia 300 production 2027; multi-GW Maia as primary inference.
  - Detail: Ignite Nov 2026 forthcoming; technical paper referenced.
- Timestamp: IN-WINDOW (Oct 12). Status: CAPTURED_BUT_UNCONSUMED (full architecture blog + paper not read). Evidence must fetch technical paper + distinguish vendor vs measured.

## 2. NVIDIA Nemotron 3.5 Super VL + Bolt (released Oct 15, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- Official blog: https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/ (2026-10-15T15:00:24Z).
- Developer: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/ (2026-10-15T15:00:00Z).
- Model card: build.nvidia.com/nvidia/nemotron-3-5-super-vl-120b-a12b/modelcard (NVFP4 GA 10/15/2026).
- Tech report: research.nvidia.com Nemotron 3.5 Super and Lightning (dated 2026-10-14, report itself pre-release but model GA Oct 15).
- X: @NVIDIAAI 2026-10-15 15:09 UTC in-window.
- Claims (vendor, search-confirmed):
  - 120B total / 12B active MoE hybrid Mamba-2–Transformer + C-RADIO vision; 1M context; text/image/doc/video in / text out; MTP speculative decoding; NVFP4 KV.
  - Positioning: fastest open agentic model in class (5x faster than next best — vendor); 51.78% SWE-bench Pro (post-trained Super, 4.6x fewer active than 3 Ultra); 2.34x/1.90x vs Qwen3.5/3.8 Flash-Next interactive (vendor).
  - Throughput: up to 4,856 out tok/s/GPU GB200 (vendor); 99.62% median accuracy recovery NVFP4 vs BF16 (vendor).
  - Artifacts: base/BF16/NVFP4 + LiLiCorr/DFlash/DSpark drafters; datasets on HF (agentic/tool/finance/45 VL sets); cookbook GitHub; NIM/OpenRouter/HF/ModelScope.
  - Bolt siblings: Bolt 74B-A9B 24GB (GA now) + Bolt E4B 4GB (Oct 23); edge/desktop coverage.
  - License: OpenMDW-1.1 per model card (verify full text in Evidence; not Apache/MIT).
- Timestamp: IN-WINDOW (Oct 15). Status: CAPTURED_BUT_UNCONSUMED (report/card not fully read). Evidence must read report + card + license.

## 3. NVIDIA OCP/Vera Rubin + SMLIB (Oct 12) — LOCATOR ONLY
- Daily X 10-13 cites @NVIDIAAIInfra 2026-10-12 15:01 UTC in-window; Vera Rubin NVL72 rack/tray to OCP + SMLIB NURBS open-source.
- Body not fetched here. Evidence gap.

## Gaps
- No independent benchmarks; vendor efficiency/throughput claims only.
- Maia paper, Nemotron report PDF, model cards, licenses: must be consumed in Evidence, not Discovery.
