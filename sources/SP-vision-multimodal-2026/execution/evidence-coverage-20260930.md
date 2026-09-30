# TS-003 Evidence coverage — Sol Evidence Semantic Review surface

Issue: `SP-vision-multimodal-2026` | Date: `2026-09-30 UTC` | Lifecycle: `CANDIDATES_NORMALIZED`

Authority: Sol Screening-through-Evidence request Sections 1–10 (+ guard addendum v2).
Input: `execution/screening-evidence-20260930/evidence-interactive-input.json` (111 records).
Outputs: `evidence/v2/accepted/3b183719.../evidence-accepted.json` (111 Cards) +
`evidence/v2/views/accepted/ed7ebf97.../edition-views-accepted.json` (111 Views).
NOT built: Materiality Ledger, Profile Completeness, any state advance beyond CANDIDATES_NORMALIZED.

## 1. Screening dispositions (input basis)

KEEP 103 / MAYBE 3 (SSD, RetinaNet, Panoptic — thin completeness nodes, retained) /
INSPECT 5 (Neocognitron paywall, LeNet PDF encoding, RefCOCO ACL binding, InternVL data scope, molmo2 license mix, VSI-Bench depth — 6 items over 5 records: D076+D077+D111+D001+D002+D042) /
DROP 0. Non-DROP Evidence tasks: 111.

## 2. Evidence units and per-obligation coverage

111 Cards / 111 Views, one per Discovery record (no merges, no splits):

| Obligation | Cards | Status split | Notes |
|---|---|---|---|
| VM-O01 | 4 | 2 VERIFIED / 2 PARTIAL | PARTIAL = paywalled Neocognitron abstract + font-encoded LeNet PDF (barriers recorded, not bypassed) |
| VM-O02 | 8 | 8 VERIFIED | Full DETR ablation depth; DINO-name discipline in cards |
| VM-O03 | 6 | 6 VERIFIED | SAM dual reading + SAM 2 bridge recorded |
| VM-O04 | 4 | 4 VERIFIED | Cap held; MiDaS mixing + DUSt3R stated limits recorded |
| VM-O05 | 10 | 10 VERIFIED | Specialist failure profiles (Nougat repetition/language, GOT own-suite scope); NO numeric ranking |
| VM-O06 | 7 | 7 VERIFIED | Recipe debate (DeiT) + encoder reuse (SigLIP); G06 preserved |
| VM-O07 | 5 | 5 VERIFIED | CLIP break + bag-of-words limit preserved as D07B motivator |
| VM-O08 | 19 | 19 VERIFIED | Full 12-step chain with redundancy calls; RefCOCO locator corrected; OWL-ST label-space binding |
| VM-O09 | 7 | 7 VERIFIED | Bridge strategies kept distinct (Q-Former vs instruction-aware vs single-projection) |
| VM-O10 | 17 | 15 VERIFIED / 2 PARTIAL | PARTIAL = InternVL/molmo2 repo depth (scope/license items carried) |
| VM-O11 | 9 | 9 VERIFIED | Polling vs control-pair vs CircularEval vs visual-math kept distinct |
| VM-O12 | 9 | 9 VERIFIED | Offline vs streaming contracts separated (StreamingBench dual role explicit) |
| VM-O13 | 3 | 3 VERIFIED | Grounding-vs-task-success contract separation; 2.0 thesis shift recorded |
| VM-O14 | 9 | 8 VERIFIED / 1 PARTIAL-adjacent | All VERIFIED; G01 preserved in OpenVLA card; card limits verbatim-class |
| VM-O15 | 7 | 7 VERIFIED | Four poles with anti-collapse rows; non-ancestry statement in Ha card |
| VM-O16 | 12 | 11 VERIFIED / 1 PARTIAL | PARTIAL = VSI-Bench (abstract + viewer depth; debiased analysis deferred) |

## 3. X01–X04 semantic coverage (what Evidence establishes)

- X01: supervision contracts per transition (ImageNet-scale, caption/V2L, CLIP-distillation, region-pseudo, image-level-label, grounding-data, self-training N-gram, instruction-tuning data, joint/native, preference/MPO, trajectory/cross-embodiment, acoustic-tokenizer, markup pairs).
- X02: interface contracts per record (label/box/mask/text/region/coordinate/action/latent/frame) in claims + lineage branch/transition IDs.
- X03: token/memory/latency consequences where material (resampling, tiling, 256K context, screenshot loops, on-device, streaming first-packet, repo deployment surfaces); TS-001 vocabulary reused, never retold.
- X04: failure attribution (polling vs control-pair vs CircularEval), vendor-claim quarantine on all 24 role-bearing records, contamination/judge-dependence notes, DINO-name and locator disciplines.

## 4. Source-role binding summary

- ARCHITECTURE_CASE (open, inspectable): Nougat, GOT, Qwen3-VL(+repo), Qwen3-Omni input/fusion(+repo), InternVL3(+repo), Molmo 2(+repo), Flash-VStream, RT-2, OpenVLA, DreamerV3, V-JEPA, Genie, Qwen3-VL-Embedding + 60+ historical method records.
- CAPABILITY_CASE (closed): Gemini 3.1 Pro / 3.6 Flash / Robotics 2 / Genie 3 (blog+page) — vendor-attributed, never architecture.
- DEPLOYMENT_CASE: closed endpoints + 4 open repos + OSWorld 2.0 env + trusted-tester distribution facts.
- EVALUATION_CASE: vendor/author-measured scores with condition bindings (Qwen/InternVL/Molmo/Gemini/OSWorld-2.0/Flash-VStream/benchmark baselines).
- No architecture inferred from product pages/demos; no cross-condition ranking constructed.

## 5. Consumption accounting (full-text vs abstract/page-only)

- VERIFIED 106: 95 arXiv full-HTML bodies + 6 proceedings/PDF full bodies (NIPS AlexNet, ICCV Flickr30k, ACL RefCOCO, CVPR X-Decoder, NeurIPS OWL-ST, LeNet-attempted) + 5 vendor/card/repo/HF full-page reads (Genie 3 blog+page, Gemini 3.1/3.6 cards, Robotics hub+card, 4 repo READMEs, HF VSI-Bench viewer).
- PARTIAL 5 with explicit reasons: D001 (paywall abstract), D002 (custom-font-encoded PDF), D076 (data-release file scope), D077 (license mix), D111 (paper body at abstract depth + viewer).
- Retrieval timestamps: 2026-09-30 UTC (repo README/vendor pages re-verified live; arXiv bodies stable versioned preprints).

## 6. G01–G06 disposition

- G01 (independent VLA eval): UNRESOLVED — preserved in OpenVLA card; not repaired by vendor material.
- G02 (control-oriented world-model bench): UNRESOLVED — none found; anti-collapse rows enforced instead.
- G03 (same-protocol doc comparison): UNRESOLVED — NO_CROSS_MODEL_NUMERIC_COMPARISON stands.
- G04 (deployment latency beyond author-reported): UNRESOLVED — preserved in Flash-VStream + omni cards.
- G05 (independent reproduction of 2026 scores): UNRESOLVED — all vendor scores quarantined with attribution.
- G06 (SigLIP2 citation): PARTIALLY ADVANCED — SigLIP mechanism + release verified; SigLIP2 exact citation still unbound.

## 7. Source/date/version corrections found during Evidence

- RefCOCO canonical locator corrected (arXiv collision → ACL D16-1212).
- LeNet author-PDF custom-font encoding barrier documented (PARTIAL, not bypassed).
- InternVL3.5 line noted as provenance (report 2508.18265; no corpus substitution).
- OSWorld 2.0 v2 (Jul 2026), Molmo 2 v4 (Apr 2026), Qwen3-VL v2 confirmed as consumed versions.
- Repo/vendor/HF states bound to 2026-09-30 retrieval; commit-level binding deferred to later stages.

## 8. Validators and checkpoints

- Screening: interactive run accepted (111) → stage validation PASS → checkpoint `DISCOVERY_COLLECTED.json` → CANDIDATES_NORMALIZED.
- Evidence: 111 Cards validated per-card against tasks → accepted (`ba4d8ac2...`) → 111 Views validated → accepted (`22cb813e...`).
- Materiality Ledger / Profile Completeness / state advance: deliberately NOT performed.
- Lifecycle: CANDIDATES_NORMALIZED; screening checkpoint passed; evidence built+validated pending Sol semantic review.
