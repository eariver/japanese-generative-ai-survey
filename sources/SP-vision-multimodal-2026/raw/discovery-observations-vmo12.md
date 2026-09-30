# Discovery observations — VM-O12 D11 video/temporal/streaming

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: VStream-QA (inside Flash-VStream) is cited-predecessor context, not a separate anchor; offline long-context (256K-class) and online streaming never share a metric column.

## VM-D083 — The Kinetics Human Action Video Dataset (Kay et al.)
- Locator: https://arxiv.org/abs/1705.06950
- Source type: `arxiv_primary` | Published: `2017-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12` | Modality: `video` | Role: `predecessor-node`
- X axes: `X01`
- Claim notes: Action-recognition predecessor; frame-repeat vs temporal-modeling baseline. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment; action-classification scope only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D084 — Something-Something V2 (Goyal et al.)
- Locator: https://arxiv.org/abs/1706.04261
- Source type: `arxiv_primary` | Published: `2017-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12` | Modality: `video` | Role: `predecessor-node`
- X axes: `X01`
- Claim notes: Temporal-ordering-sensitive predecessor; ordering/causality probe origin. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short treatment.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D085 — Ego4D (Grauman et al.)
- Locator: https://arxiv.org/abs/2110.07058
- Source type: `arxiv_primary` | Published: `2021-10` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12`, `VM-O14` | Modality: `video` | Role: `data-predecessor`
- X axes: `X01`
- Claim notes: Egocentric + audio-visual + trajectory-adjacent data (3,000h); feeds D11 temporal and D13 data ancestry. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Data-scope claims; modeling claims need system sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D086 — Video-MME (Fu et al.)
- Locator: https://arxiv.org/abs/2405.21075
- Source type: `arxiv_primary` | Published: `2024-05` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12`, `VM-O16` | Modality: `video` | Role: `eval-anchor`
- X axes: `X04`
- Claim notes: 900 videos / 254h / 2,700 QA; 11s-1h durations; subtitles + audio modalities; expert annotation. Distinct: duration x modality breadth. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: v3 May 2025; version-bind at Evidence.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D087 — LongVideoBench (Wu et al.)
- Locator: https://arxiv.org/abs/2407.15754
- Source type: `arxiv_primary` | Published: `2024-07` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12`, `VM-O16` | Modality: `video` | Role: `eval-anchor`
- X axes: `X04`
- Claim notes: 3,763 videos + subtitles; 6,678 QA; referring-reasoning task (retrieve + reason over referred long context); frame-count sensitivity finding. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Distinct: referred-context retrieval-reasoning; not interchangeable with duration-breadth benches.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D088 — StreamingBench (Lin et al.)
- Locator: https://arxiv.org/abs/2411.03628
- Source type: `arxiv_primary` | Published: `2024-11` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12`, `VM-O16`, `VM-O10` | Modality: `video-audio` | Role: `eval-anchor`
- X axes: `X02`, `X04`
- Claim notes: 900 videos / 4,500 QA / 18 tasks; timestamped mid-stream queries; omni-source incl. audio; proactive output; best 67.07% vs human 91.66% (author-measured). Streaming-eval contract. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Offline-converted evaluation for most models; true online-system scores need Flash-VStream-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- repo: https://github.com/THUNLP-MT/StreamingBench

## VM-D089 — Flash-VStream (Zhang et al.)
- Locator: https://arxiv.org/abs/2406.08085
- Source type: `arxiv_primary` | Published: `2024-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12` | Modality: `video` | Role: `system-anchor`
- X axes: `X02`, `X03`
- Claim notes: Memory-based real-time online video understanding; async-query handling; latency/VRAM reductions; VStream-QA companion bench. Covers online input + bounded memory + persistent state. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Author-reported latency/VRAM; deployment figures beyond that are a gap.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open) + EVALUATION_CASE (author-measured)`

## VM-D111 — VSI-Bench (Yang et al.)
- Locator: https://arxiv.org/abs/2412.14171
- Source type: `arxiv_primary` | Published: `2024-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O12`, `VM-O16` | Modality: `video` | Role: `eval-authority`
- X axes: `X04`
- Claim notes: 5,131 QA over 288 egocentric videos (ScanNet/++/ARKitScenes); 8 tasks (configurational/measurement/spatiotemporal); MCA + MRA; blind baselines; 2,363 debiased subset; CoT-degradation + cognitive-map-gain findings; CVPR 2025. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Exact ID bound at intake (resolves Round D MEDIUM); debiased subset is the shortcut-control exhibit.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- dataset: https://huggingface.co/datasets/nyu-visionx/VSI-Bench
