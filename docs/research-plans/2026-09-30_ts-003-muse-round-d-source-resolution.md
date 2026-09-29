# TS-003 Vision & Multimodal AI — Muse Round D source resolution

Status: `ROUND_D_SOURCE_RESOLUTION / PRE_DISCOVERY / NOT_PRODUCTION_AUTHORITY`

Date: `2026-09-30 JST`

Branch: `planning/ts-003-vision-multimodal-preresearch-20260930`

Companion: `docs/research-plans/2026-09-30_ts-003-muse-round-d-targeted-followup.md` (R1–R10 findings).

**This file lists ONLY sources actually checked during Round D.** Unlike the Round B ledger, no entry
here is `NOT_ACCESSED`. Access vocabulary used honestly:

- `ABSTRACT_FETCH` — arXiv abs page fetched and abstract + submission history read in Round D.
- `SEARCH_ABSTRACT` — abstract + core claims verified via web-search result content in Round D
  (no direct page fetch; full-text claims beyond the abstract are NOT established).
- `OFFICIAL_PAGE_READ` — vendor/lab page fetched and read in Round D (capability/deployment facts
  only; never architecture).
- `MODEL_CARD_READ` — vendor model card fetched and read in Round D (scoped eval/limitation facts).
- `CARRIED_†` — NOT listed here. Prior-round IDs referenced in the main report carry † and must be
  re-bound at Discovery intake; they are excluded from this file by construction.

Confidence: `HIGH` (canonical ID + abstract match), `MEDIUM` (ID highly likely, minor version
detail to bind at intake). Version/date notes record submitted/revised dates seen at check time
(CV2-DM-013). TS-001/002 overlap notes reuse the Round B matrix shorthand.

---

## R1 — D04 allow-list

1. MiDaS — Ranftl et al. — 2019 (TPAMI 2022) — PREPRINT/PAPER + OFFICIAL_REPO (`isl-org/MiDaS`) —
   primary — https://arxiv.org/abs/1907.01341 —
   access: `SEARCH_ABSTRACT` — relevant claim: scale/shift-invariant monocular depth;
   multi-dataset Pareto-mixing; zero-shot cross-dataset transfer — confidence: HIGH —
   version: v1 Jul 2019 (journal 2022) — overlap: TS-001 absent / TS-002 partial (control signals).
2. OpenPose — Cao et al. — 2018 (TPAMI 2019; CVPR 2017 precursor) — PREPRINT/PAPER — primary —
   https://arxiv.org/abs/1812.08008 —
   access: `SEARCH_ABSTRACT` — relevant claim: PAF bottom-up multi-person 2D pose; 135 keypoints
   incl. foot/hand/face; realtime — confidence: HIGH — overlap: absent/absent.
3. Visual Genome — Krishna et al. — 2016 (IJCV 2017) — PREPRINT/PAPER + DATASET — primary —
   https://arxiv.org/abs/1602.07332 —
   access: `SEARCH_ABSTRACT` — relevant claim: 108K images, dense objects/attributes/relations,
   WordNet-canonicalized scene graphs; region-description grounding — confidence: HIGH —
   overlap: absent/absent.
4. DUSt3R — Wang et al. — 2023 (CVPR 2024) — PREPRINT/PAPER + OFFICIAL_REPO (`naver/dust3r`) —
   primary — https://arxiv.org/abs/2312.14132 —
   access: `SEARCH_ABSTRACT` — relevant claim: camera-free pointmap regression unifying
   mono/binocular; global alignment; Transformer init — confidence: HIGH — overlap: absent/partial.

## R2 — D07B lineage

5. Flickr30k Entities — Plummer et al. — ICCV 2015 — PAPER + DATASET — primary —
   https://openaccess.thecvf.com/content_iccv_2015/html/Plummer_Flickr30k_Entities_Collecting_ICCV_2015_paper.html —
   access: `SEARCH_ABSTRACT` — relevant claim: 244k coreference chains / 276k boxes; phrase
   localization task definition — confidence: HIGH — overlap: absent/absent.
6. OVR-CNN (OVD formulation) — Zareian et al. — CVPR 2021 — PREPRINT/PAPER — primary —
   https://arxiv.org/abs/2011.10678 —
   access: `SEARCH_ABSTRACT` — relevant claim: OVD task coinage; V2L caption pretraining
   (grounding/MLM/ITM) → Faster R-CNN transfer; recognition/localization disentanglement —
   confidence: HIGH — version: v2 Mar 2021 — overlap: absent/absent.
7. ViLD — Gu et al. — 2021 (ICLR 2022) — PREPRINT — primary —
   https://arxiv.org/abs/2104.13921 —
   access: `SEARCH_ABSTRACT` — relevant claim: CLIP/ALIGN distillation into two-stage detector
   (ViLD-text + ViLD-image); LVIS-rare 16.1→26.3 APr; open code (tpu repo) — confidence: HIGH —
   overlap: absent/absent.
8. RegionCLIP — Zhong et al. — CVPR 2022 — PREPRINT/PAPER + repo (`microsoft/RegionCLIP`) —
   primary — https://arxiv.org/abs/2112.09106 —
   access: `SEARCH_ABSTRACT` — relevant claim: CLIP image→region domain-shift diagnosis; pseudo
   region-text pretraining; COCO-novel 31.4 vs OVR 22.8 — confidence: HIGH — overlap: absent/absent.
9. Detic — Zhou et al. — ECCV 2022 — PREPRINT/PAPER + repo (`facebookresearch/detic`) — primary —
   https://arxiv.org/abs/2201.02605 —
   access: `SEARCH_ABSTRACT` — relevant claim: image-level (ImageNet-21K) classifier training via
   max-size-proposal assignment; open-vocabulary LVIS gains — confidence: HIGH —
   notes: CORRECTS Round B guess `2201.12280` — overlap: absent/absent.
10. MDETR — Kamath et al. — ICCV 2021 — PREPRINT/PAPER + repo (`ashkamath/mdetr`) — primary —
    https://arxiv.org/abs/2104.12763 —
    access: `SEARCH_ABSTRACT` — relevant claim: DETR modulated by raw text; 1.3M-pair pretraining;
    phrase grounding + REC + RES(PhraseCut) + GQA-adjacent — confidence: HIGH —
    version: v2 Oct 2021 — overlap: absent/absent.
11. OWL-ST / OWLv2 — Minderer et al. — NeurIPS 2023 — PAPER (proceedings canonical) + PREPRINT —
    primary — https://arxiv.org/abs/2306.09683 ;
    https://proceedings.neurips.cc/paper_files/paper/2023/hash/e6d58fc68c0f3c36ae6e0e64478a69c0-Abstract.html —
    access: `SEARCH_ABSTRACT` — relevant claim: N-gram machine label space; 1B+ self-training;
    LVIS-rare 31.2→44.6%; code+checkpoints — confidence: HIGH — overlap: absent/absent.
12. LSeg — Li et al. — ICLR 2022 — PREPRINT — primary — https://arxiv.org/abs/2201.03546 —
    access: `SEARCH_ABSTRACT` — relevant claim: pixel-text contrastive alignment; zero-shot
    unseen-category segmentation — confidence: HIGH — overlap: absent/absent.
13. X-Decoder — Zou et al. — CVPR 2023 — PAPER (open-access canonical) — primary —
    https://openaccess.thecvf.com/content/CVPR2023/papers/Zou_Generalized_Decoding_for_Pixel_Image_and_Language_CVPR_2023_paper.pdf —
    access: `SEARCH_ABSTRACT` — relevant claim: unified generic + referring segmentation + VL tasks;
    no pseudo-labeling; 7-dataset open-vocab SOTA — confidence: HIGH — overlap: absent/absent.
14. OpenSeg — Ghiasi et al. — ECCV 2022 — PAPER — primary — (resolve proceedings URL at intake) —
    access: `SEARCH_ABSTRACT` — relevant claim: image-level-label scaling variant of OVS —
    confidence: MEDIUM — role: named variant, not a separate node — overlap: absent/absent.
15. ODISE — Xu et al. — CVPR 2023 (Highlight) + repo (`NVlabs/ODISE`) — PREPRINT/PAPER — primary —
    https://arxiv.org/abs/2303.04803 —
    access: `SEARCH_ABSTRACT` — relevant claim: frozen diffusion + discriminative backbones for
    open-vocabulary panoptic segmentation — confidence: HIGH —
    notes: TS-002-crossover flag — overlap: absent/partial.

## R3 — Second open VLM

16. InternVL3 — Zhu et al. (Shanghai AI Lab et al.) — Apr 2025 — PREPRINT ("Technical Report") +
    OFFICIAL_REPO (`OpenGVLab/InternVL`) + data (`OpenGVLab/InternVL-Data`) — primary —
    https://arxiv.org/abs/2504.10479 —
    access: `ABSTRACT_FETCH` — relevant claim: native joint multimodal+text pretraining; V2PE;
    SFT+MPO; 1B–78B family; 78B 72.2 MMMU (vendor-measured) — confidence: HIGH —
    version: v3 Apr 2025 — overlap: TS-001 partial / TS-002 partial.
17. Molmo 2 — Clark et al. (Ai2) — Jan 2026 (v4 Apr 2026) — PREPRINT + repos (`allenai/molmo2`) —
    primary — https://arxiv.org/abs/2601.10611 ; blog https://allenai.org/blog/molmo2 (not fetched;
    abstract record rests on arXiv) —
    access: `ABSTRACT_FETCH` — relevant claim: open weights+data (Apache 2.0); no closed-VLM
    synthetic data; video pointing/tracking; 8B video-counting 35.5 vs Qwen3-VL 29.6, pointing F1
    38.4 vs Gemini 3 Pro 20.0 (author-measured); fully-open Olmo variant — confidence: HIGH —
    version: v4 Apr 2026 — overlap: partial/partial.
18. Molmo / PixMo (v1) — Deitke et al. (Ai2) — Sep 2024 (CVPR 2025) — PREPRINT/PAPER — primary —
    https://arxiv.org/abs/2409.17146 —
    access: `SEARCH_ABSTRACT` — relevant claim: open-data thesis origin; PixMo-Points (2D pointing
    → grounding/counting); fully-open MetaCLIP+OLMo variant — confidence: HIGH —
    role: predecessor context for Molmo 2 — overlap: partial/partial.

## R4 — Document specialist vs generalist

19. Nougat — Blecher et al. (Meta) — Aug 2023 — PREPRINT + repo (`facebookresearch/nougat`) —
    primary — https://arxiv.org/abs/2308.13418 —
    access: `SEARCH_ABSTRACT` — relevant claim: Donut-lineage Swin encoder-decoder; markup output
    (text+math+tables); arXiv/PMC/IDL-derived pairs; own-test markup agreement vs GROBID/pdf-text —
    confidence: HIGH — overlap: absent/absent.
20. GOT (OCR-2.0) — Wei et al. — Sep 2024 — PREPRINT — primary —
    https://arxiv.org/abs/2409.01704 —
    access: `SEARCH_ABSTRACT` — relevant claim: 580M encoder-decoder (1024²px→256 tokens; 8K
    decoder); formatted outputs; region-prompt/dynamic-resolution/multi-page; own OCR-2.0 suites —
    confidence: HIGH — version: v1 Sep 2024 — overlap: absent/absent.
21. DocVQA — Mathew et al. — 2020 (WACV 2021) + leaderboard (docvqa.org) — PREPRINT/PAPER +
    BENCHMARK — primary — https://arxiv.org/abs/2007.00398 —
    access: `SEARCH_ABSTRACT` — relevant claim: 50K Q / 12.7K images; ANLS metric; human 94.36%;
    structure-sensitivity gap — confidence: HIGH — overlap: absent/absent.
22. ChartQA — Masry et al. — 2022 (Findings ACL) + repo (`vis-nlp/ChartQA`) — PREPRINT/PAPER +
    BENCHMARK — primary — https://arxiv.org/abs/2203.10244 —
    access: `SEARCH_ABSTRACT` — relevant claim: 9.6K human + 23.1K generated visual+logical QA;
    relaxed-accuracy; real-world charts — confidence: HIGH — overlap: absent/absent.

## R5 — Streaming (+ R9 long-video/streaming eval)

23. Flash-VStream — Zhang et al. — Jun 2024 (v2) — PREPRINT (+code/models/data stated) — primary —
    https://arxiv.org/abs/2406.08085 —
    access: `ABSTRACT_FETCH` — relevant claim: memory-based real-time online video understanding;
    async-query handling; latency/VRAM reductions; VStream-QA bench — confidence: HIGH —
    version: v2 Jun 2024 — overlap: absent/partial.
24. StreamingBench — Lin et al. — Nov 2024 — PREPRINT + repo (`THUNLP-MT/StreamingBench`) —
    primary — https://arxiv.org/abs/2411.03628 —
    access: `ABSTRACT_FETCH` — relevant claim: 900 videos / 4,500 QA / 18 tasks; timestamped
    mid-stream queries; omni-source; proactive output; best 67.07% vs human 91.66%
    (author-measured) — confidence: HIGH — overlap: absent/partial.
25. Video-MME — Fu et al. — May 2024 (v3 May 2025) — PREPRINT — primary —
    https://arxiv.org/abs/2405.21075 —
    access: `ABSTRACT_FETCH` — relevant claim: 900 videos / 254h / 2,700 QA; 11s–1h; subtitles +
    audio; expert annotation — confidence: HIGH — version: v3 May 2025 — overlap: absent/partial.
26. LongVideoBench — Wu et al. — Jul 2024 — PREPRINT — primary —
    https://arxiv.org/abs/2407.15754 —
    access: `ABSTRACT_FETCH` — relevant claim: 3,763 videos + subtitles; 6,678 QA; referring-
    reasoning task; frame-count sensitivity — confidence: HIGH — overlap: absent/partial.

## R6 — Audio-input chain

27. BEATs — Chen et al. (Microsoft) — Dec 2022 (ICML 2023) + code/models — PREPRINT/PAPER —
    primary — https://arxiv.org/abs/2212.09058 —
    access: `ABSTRACT_FETCH` — relevant claim: iterative acoustic-tokenizer SSL (discrete-label
    prediction, not reconstruction); AudioSet-2M 50.6% mAP audio-only; ESC-50 98.1%
    (author-measured) — confidence: HIGH — overlap: absent/partial.
28. CLAP — Elizalde et al. (Microsoft) — Jun 2022 (ICASSP 2023) — PREPRINT/PAPER — primary —
    https://arxiv.org/abs/2206.04769 —
    access: `ABSTRACT_FETCH` — relevant claim: contrastive language-audio pretraining; 128k pairs;
    16 tasks/8 domains zero-shot + 5 supervised SOTAs (author-measured) — confidence: HIGH —
    overlap: absent/partial.

## R7 — VLA chain (only the Round-D-verified node; remainder †-carried, see main report)

29. SayCan — Ahn et al. — Apr 2022 (CoRL 2022; PMLR v205, 2023) + site/code
    (`say-can.github.io`) — PREPRINT/PAPER — primary — https://arxiv.org/abs/2204.01691 —
    access: `SEARCH_ABSTRACT` — relevant claim: frozen-LLM planning × affordance value functions;
    101 real kitchen tasks; 84% planning / 74% execution; grounding ≈ doubles baseline —
    confidence: HIGH — venue: PMLR v205 (CoRL 2023 proceedings) — overlap: absent/absent.

## R8 — World-model counterweights (plus R10 vendor reads)

30. V-JEPA — Bardes et al. (Meta FAIR) — Feb 2024 + repo (`facebookresearch/jepa`) — PREPRINT —
    primary — https://arxiv.org/abs/2404.08471 —
    access: `ABSTRACT_FETCH` — relevant claim: feature-prediction-only video SSL (no pixels/text/
    negatives/reconstruction); VideoMix2M 2M videos; frozen K400 81.9 / SSv2 72.2 / IN1K 77.9 —
    confidence: HIGH — notes: CORRECTS Round B guess `2307.07420` — overlap: absent/partial.
31. Genie 3 — DeepMind — blog 2025-08-05 + model page — OFFICIAL_PAGE — official (vendor) —
    https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ ;
    https://deepmind.google/models/genie/ —
    access: `OFFICIAL_PAGE_READ` — relevant claim: 24fps/720p real-time; minutes consistency;
    1-min visual memory; promptable world events; SIMA training use; 5 stated limitations;
    research-preview gating — confidence: HIGH (for page facts; architecture undisclosed) —
    role cap: CAPABILITY + DEPLOYMENT-pointer ONLY — overlap: absent/partial.

## R9 — Eval cleanup (beyond R4/R5 entries above)

32. OCRBench v2 — Fu et al. — Jan 2025 — PREPRINT — primary —
    https://arxiv.org/abs/2501.00321 —
    access: `SEARCH_ABSTRACT` — relevant claim: 23 tasks / 31 scenarios / 10K verified QA /
    6 metric types + 1,500-image private set; five limitation classes; spotting/localization gaps —
    confidence: HIGH — notes: v1 (Sci China 2024; preprint `2305.07895`) SUPERSEDED — overlap:
    absent/absent.
33. HallusionBench — Guan et al. — Oct 2023 (CVPR 2024) + repo (`tianyi-lab/HallusionBench`) —
    PREPRINT/PAPER — primary — https://arxiv.org/abs/2310.14566 —
    access: `SEARCH_ABSTRACT` — relevant claim: 346 images (165 + 181 human-edited) / 1,129 Q;
    control-pair language-vs-vision failure attribution; GPT-4V 31.42% pair-accuracy
    (author-measured) — confidence: HIGH — notes: CORRECTS Round B guess `2311.07312` — overlap:
    absent/absent.
34. ScreenSpot (in SeeClick, Cheng et al.) — Feb 2024 (ACL 2024) + repo (`njucckevin/SeeClick`) —
    PREPRINT/PAPER — primary — https://arxiv.org/abs/2401.10935 —
    access: `SEARCH_ABSTRACT` — relevant claim: 600+ screenshots / 1,200+ instructions;
    mobile+desktop+web; text + icons/widgets; grounding-pretraining → downstream-agent gains —
    confidence: HIGH — version: v2 Feb 2024 — overlap: absent/absent.
35. VSI-Bench — Yang et al. — Dec 2024 (CVPR 2025) + HF (`nyu-visionx/VSI-Bench`) — PREPRINT/PAPER —
    primary — (CVPR open-access + project page verified via search; bind exact arXiv ID at intake) —
    access: `SEARCH_ABSTRACT` — relevant claim: 5,131 QA over 288 egocentric videos
    (ScanNet/++/ARKitScenes); 8 tasks (configurational/measurement/spatiotemporal); MCA + MRA;
    blind baselines; 2,363 debiased subset (Nov 2025); CoT-degradation + cognitive-map-gain findings —
    confidence: MEDIUM (exact arXiv ID unbound — intake task) — overlap: absent/partial.

## R10 — Capstone role matrix inputs (beyond entries above)

36. Qwen3-VL Technical Report — Bai et al. — Nov 2025 (v2) — PREPRINT (42pp) + repo
    (`QwenLM/Qwen3-VL`) — primary — https://arxiv.org/abs/2511.21631 —
    access: `ABSTRACT_FETCH` — relevant claim: interleaved-MRoPE; DeepStack; text-timestamp video
    alignment; 256K interleaved context; dense+MoE family — confidence: HIGH —
    version: v2 Nov 2025 — overlap: partial/partial.
37. Qwen3-Omni Technical Report — Xu et al. — Sep 2025 — PREPRINT + repo (`QwenLM/Qwen3-Omni`) —
    primary — https://arxiv.org/abs/2509.17765 —
    access: `ABSTRACT_FETCH` — relevant claim: Thinker–Talker MoE; TM-RoPE 80ms absolute-time;
    from-scratch audio encoder; 234ms first-packet (theoretical); 36 audio/AV benches; Apache 2.0 —
    confidence: HIGH — overlap: partial/partial.
38. OSWorld 2.0 — Yuan et al. — Jun 2026 (v2 Jul 2026) — PREPRINT (68pp) — primary —
    https://arxiv.org/abs/2606.29537 —
    access: `ABSTRACT_FETCH` — relevant claim: 108 long-horizon workflows; 1.6h median; ~318 vs
    ~30 tool calls; best 20.6% binary / 54.8% partial; token-cost curves; safety audits —
    confidence: HIGH — version: v2 Jul 2026 — overlap: partial/absent.
39. Gemini Robotics On-Device 2 model card — DeepMind — Jul 2026 — MODEL_CARD — official (vendor) —
    https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/ —
    access: `MODEL_CARD_READ` — relevant claim: VLA on on-device Gemma + Robotics 1.5 tech;
    text/image/proprioception-in, actions-out; trusted-testers-only; sim+on-robot eval;
    OOD + high-DoF limits stated; bi-arm-primary safety scope; layered-safety recommendation —
    confidence: HIGH (for card facts) — role cap: CAPABILITY + EVALUATION(card-scoped) +
    DEPLOYMENT ONLY — overlap: partial/absent.

---

## Check-method note (honesty record)

- `ABSTRACT_FETCH` (12): entries 16, 17, 23, 24, 25, 26, 27, 28, 30, 36, 37, 38 — arXiv abs pages
  fetched in Round D; abstract + submission history read; full-text claims NOT established.
- `SEARCH_ABSTRACT` (23): all other numbered entries — abstracts and core claims verified via
  Round D web-search content; venue/repo cross-checks included where shown.
- `OFFICIAL_PAGE_READ` (1): entry 31. `MODEL_CARD_READ` (1): entry 39.
- Entry 35 carries MEDIUM confidence solely because its exact arXiv ID was not bound during Round D;
  venue (CVPR 2025) + HF dataset + project page were verified. Intake must bind the ID.
- No FULL_TEXT reads were performed in Round D (planning scope). Full-text read-back is a
  Discovery/Evidence responsibility.
- Three Round B ID guesses were corrected by Round D verification (Detic, V-JEPA, HallusionBench);
  one supersession recorded (OCRBench v1 → v2). No other Round B IDs were re-opened.
