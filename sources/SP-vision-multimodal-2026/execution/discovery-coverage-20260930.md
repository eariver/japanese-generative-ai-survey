# TS-003 Discovery coverage accounting — Sol completeness review surface

Issue: `SP-vision-multimodal-2026` | Run: `vision-multimodal-discovery-r1` | Date: `2026-09-30 UTC`

Scope authority: Round E (`2d68e07cda25d54b31770f53a510cbedb58390e7`); execution contract
(`7ca9e20e046bd4a582e1e112f76564c4e9015bb2`). Raw corpus: `raw/discovery-observations-vm*.md`
(15 lane files) + `raw/discovery-negative-space-2026-09-30.md`. Canonical records:
`discovery/discovery-v2.jsonl`; deterministic acceptance: `discovery/discovery-accepted-v2.json`.

## 1. Totals

- Total Discovery records: **111** (VM-D001..VM-D111, all `BASE` pass 0)
- Unique locators: **111** (no duplicates; sharing expressed via multi-obligation tagging)
- Multi-obligation records: **23** (e.g. SigLIP O06+O07, LVIS O08+O16, StreamingBench O10+O12+O16)
- Deterministic acceptance: **PASS** — `validate_acceptance` rebuilt graph matches
  (`record_count 111`, graph `cf6730f0f55eeaba`, X manifest `NOT_REQUIRED/COMPLETE` bound)

## 2. VM-O01..VM-O16 coverage (record count = unique records touching the obligation)

| Obligation | Lane / weight | Records | Coverage verdict |
|---|---|---|---|
| VM-O01 | D01 learned representation / CONTEXT_CAPPED | 4 | SUFFICIENT (context cap respected; predecessor + 2 anchors) |
| VM-O02 | D02 detection | 8 | SUFFICIENT (region -> one-stage -> set-prediction -> OV bridge) |
| VM-O03 | D03 segmentation | 6 | SUFFICIENT (dense -> instance -> panoptic -> promptable + video bridge) |
| VM-O04 | D04 spatial substrate / HARD_CAP | 4 | SUFFICIENT AT CAP (allow-list exact; refusals ledgered) |
| VM-O05 | D05 document intelligence / NORMAL | 10 | SUFFICIENT (pipeline -> OCR-free -> specialists -> retrieval sub-lane -> eval) |
| VM-O06 | D06 ViT/self-supervised | 7 | SUFFICIENT (token formulation + label-free + encoder reuse) |
| VM-O07 | D07A alignment / FULL | 5 | SUFFICIENT (captioning + VQA-task + CLIP/ALIGN + shared SigLIP) |
| VM-O08 | D07B grounding / FULL | 19 | SUFFICIENT (full 12-step chain + OVS branch + LVIS; NOT compressed to CLIP+DINO) |
| VM-O09 | D08 bridging / FULL | 7 | SUFFICIENT (frozen precursor -> Flamingo/BLIP-2 -> instruction bridge -> LLaVA) |
| VM-O10 | D09 fusion/omni / FULL | 17 | SUFFICIENT (Qwen chain + audio-input chain + 2nd families + closed pole + repos) |
| VM-O11 | D10 reasoning/failure / FULL | 9 | SUFFICIENT (MMMU + polling + control-pair + bilingual + visual-math + OCRBench-v2) |
| VM-O12 | D11 video/streaming / NORMAL | 9 | SUFFICIENT (action/event/ego predecessors + 3 video evals + streaming system+eval) |
| VM-O13 | D12 computer use / BOUNDED | 3 | SUFFICIENT AT CAP (grounding eval + short-horizon + long-horizon; web-phase is context) |
| VM-O14 | D13 VLA / HARD_CAP | 9 | SUFFICIENT (7-node minimum chain + current endpoint + card; robotics refused) |
| VM-O15 | D14 world models / TERMINOLOGY_SPLIT | 7 | SUFFICIENT (4 poles incl. both counterweights; Genie role-capped) |
| VM-O16 | D15 evaluation / METHODOLOGY_FIRST | 12 | SUFFICIENT (retain-set via shared records; distinct contracts only) |

No obligation has fewer than its Round E minimum; capped lanes (O01/O04/O13) are held at cap deliberately.

## 3. Historical / current split

- Historical anchors (pre-2024, 61 records): full predecessor-to-successor chains per lane; no abrupt entries (Neocognitron/LeNet context, captioning/VQA predecessors, SayCan/RT-1/PaLM-E/OpenX chain, Ha/Dreamer/JEPA poles).
- Current 2025–2026 cases (16 records + 4 repo records): Qwen3-VL, Qwen3-Omni, InternVL3, Molmo 2 (+v1 predecessor), Gemini 3.1 Pro / 3.6 Flash cards, Qwen3-VL-Embedding, OSWorld 2.0, Flash-VStream, Gemini Robotics 2 + On-Device 2 card, Genie 3 blog+page, OCRBench v2, VSI-Bench.
- Second open VLM family: PRESENT (InternVL3 paradigm contrast + Molmo 2 grounding comparator + 3 repos). No Qwen-only dependence.

## 4. Authority coverage (source_type; all Evidence-map admissible — CV2-DM-016 avoidance by design)

- `arxiv_primary`: 95 (all arXiv IDs re-resolved at intake via API title-match; 3 Round B ID errors corrected)
- `official_conference_paper`: 4 (ICCV 2015, CVPR 2023, ACL D16-1212, NeurIPS proceedings page)
- `official_publisher_page`: 2 (NIPS proceedings page, author-hosted LeNet PDF, Springer DOI)
- `first_party_vendor_blog`: 1 (Genie 3; capability/deployment only)
- `first_party_release_or_docs`: 5 (2 Gemini cards, Gemini Robotics page + card, Genie 3 page)
- `official_project_repo`: 4 (Qwen3-VL, Qwen3-Omni, InternVL, molmo2; commit-version binding deferred to Evidence)
- Secondary/social: 0 (no weak authority used for technical claims; gaps recorded instead)

## 5. X01–X04 coverage (per-record x_axes tags)

- X01 data/supervision/post-training: 60 records (incl. OWL-ST self-training, Qwen staged recipes, OpenX/Ego4D trajectory data, instruction-tuning nodes)
- X02 objective/interface contract: 62 records (every transition's in/out contract in raw notes)
- X03 token/memory/latency economics: 15 records (fusion/tokenizer/resampling/loop/on-device costs; TS-001 vocabulary reused, never retold)
- X04 reliability/claim strength: 32 records (failure-attribution evals, vendor-claim isolation, 4-role tagging on all 24 role-bearing current records)

## 6. TS-001 / TS-002 overlap matrix (accounting, not duplication)

| Shared object | TS-001 angle (owned) | TS-002 angle (owned) | TS-003 treatment in this Discovery |
|---|---|---|---|
| Transformer/attention | efficiency (FlashAttention/MLA/etc.) | backbone where relevant | token-formulation/fusion use only (O06/O10 raw notes) |
| ViT | token efficiency | generation backbone | representation history (O06 records) |
| CLIP | deployment/compute | conditioning machinery | addressability transition (O07); conditioning reused by reference |
| VAE/tokenizer | memory/compute | shortening-for-generation spine | understanding-side token budgets (O10) |
| Video | context/runtime | generation/motion/consistency | observed-video state/reasoning (O12); generated-vs-observed split enforced |
| Audio | runtime only | synthesis history | input/fusion/reasoning only (O10 chain); generation refused |
| Quantization/MoE/serving | core subject | deployment | multimodal-specific fields only (X03 tags) |
| World model | efficiency if material | generated world as media | predictive/action-conditioned state (O15 four-pole) |
| Agent/action | routing/specialization | workflows around generation | perception-grounded action (O13/O14) |
| Evaluation method | condition-binding discipline | fidelity/alignment method | understanding-side identities + binding discipline imported (O16) |

## 7. Current-case source-role matrix (summary; exact sources in records)

- ARCHITECTURE_CASE (open, inspectable): Nougat, GOT, Qwen3-VL(+repo), Qwen3-Omni-input/fusion(+repo), InternVL3(+repo+data), Molmo 2(+repo), Flash-VStream, RT-2, OpenVLA, DreamerV3, V-JEPA, Genie, Qwen3-VL-Embedding.
- CAPABILITY_CASE (closed): Gemini 3.1 Pro, Gemini 3.6 Flash, Gemini Robotics 2, Genie 3 (blog+page).
- DEPLOYMENT_CASE: above closed cases + 4 open repos + OSWorld 2.0 env + On-Device 2 (trusted-testers).
- EVALUATION_CASE (author/vendor-measured, conditions bound): Qwen3-VL, Qwen3-Omni, InternVL3, Molmo 2, Gemini 3.1 Pro, OSWorld 2.0, Flash-VStream, On-Device 2 (card-scoped), Qwen3-VL-Embedding.
- No cell filled from product pages/demos for architecture. No cross-model numeric ranking constructed.

## 8. Evaluation authority map (retain-set; distinct contracts)

DocVQA (structure reading, ANLS) / ChartQA (visual+logical, relaxed-acc) / OCRBench v2 (localization+reasoning, private set; v1 dropped) / POPE (polling) + HallusionBench (control-pair attribution) / ScreenSpot (element localization) / OSWorld 1.0 (short-horizon) + 2.0 (state-management economics) / Video-MME (duration×modality) / LongVideoBench (referred-context reasoning) / StreamingBench (streaming contract) / VSI-Bench (spatial intelligence + debiased subset) / LVIS-rare (OVD home). No cross-family ranking tables.

## 9. Negative space / LOW_YIELD / EVIDENCE_GAP

See `raw/discovery-negative-space-2026-09-30.md`. Headline: zero LOW_YIELD (streaming + 2nd-VLM resolved); 6 EVIDENCE_GAPs carried (independent VLA eval; control-oriented world-model bench; same-protocol doc head-to-head; deployment latency beyond author-reported; independent reproduction of 2026 vendor scores; SigLIP2 citation binding).

## 10. Access status & provenance

- Re-resolution method: arXiv API id_list title-match (95/95 matched; 4 collisions/gaps corrected: DeViSE→context, RefCOCO→ACL, Detic/V-JEPA/HallusionBench/MathVista/VSI-Bench IDs fixed); HTTP-200 checks for all 16 non-arXiv locators (proceedings, anthology, NIPS, author PDF, DOI, vendor pages/cards, HF dataset, 19 GH repos).
- Retrieval honesty: abstract/page-level capture (`retrieval_status` per record); full text explicitly deferred to Evidence (`evidence_boundary` per record). No FULL_TEXT claim anywhere.
- Date discipline (CV2-DM-013): `published_at` per record (venue months for proceedings); vendor card dates bound (2026-02/2026-07/2025-08); repo records use null `published_at` + `REPOSITORY_VERIFIED` (commit binding at Evidence).
- Terminology discipline (CV2-DM-006): canonical names preserved; DINO detector/ss disambiguated in VM-D011/VM-D034.
- Claim-strength discipline (CV2-DM-020): 24 role-bearing records carry explicit role caps; vendor numbers labeled author/vendor-measured with binding requirements.

## 11. Unresolved gaps (for Sol completeness review)

G01 independent VLA eval scarcity; G02 control-oriented world-model bench absent; G03 same-protocol doc comparison absent; G04 deployment latency beyond author-reported; G05 independent reproduction of 2026 vendor scores; G06 SigLIP2 citation binding. Plus intake-verified notes: InternVL3.5 currency, ScreenSpot-successor currency, newer streaming systems sweep, repo commit binding, vendor page drift.

## 12. Anti-collapse checks ( lane integrity )

- [x] D07B is a 14-record chain + eval, not CLIP + Grounding DINO.
- [x] D07A/D07B never share a metric column.
- [x] D04 is 4 nodes; refusals named.
- [x] D13 ends at the representation/action interface; no control/hardware content.
- [x] D14 carries both non-generative poles; pixel-only exhibits would be TS-002 refs (none admitted).
- [x] D09/D11 audio is input/fusion/reasoning only; no synthesis mechanism.
- [x] No Qwen-only current narrative (InternVL3 + Molmo 2 + repos).
- [x] Streaming vs offline long-context never share a metric column.
- [x] No benchmark count inflation (retain-set only; drops named).
