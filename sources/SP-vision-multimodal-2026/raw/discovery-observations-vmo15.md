# Discovery observations — VM-O15 D14 world models (TERMINOLOGY-SPLIT)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Genie 2 is predecessor context of Genie 3 (vendor page lineage); model-based-RL dynamics minimum context (PILCO/PlaNet) one line; Waymo World Model is a DEPLOYMENT pointer pending primary-source binding at Evidence; transferable control-oriented world-model benchmark: NONE FOUND (EVIDENCE_GAP).

## VM-D101 — World Models (Ha & Schmidhuber)
- Locator: https://arxiv.org/abs/1803.10122
- Source type: `arxiv_primary` | Published: `2018-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O15` | Modality: `latent-dynamics` | Role: `terminological-origin`
- X axes: `X02`
- Claim notes: Term origin (VAE latent + RNN hidden + MDN); planning-by-evolution in dream. NOT Genie's technical ancestor (non-ancestry statement required). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); historical term source only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial

## VM-D102 — Mastering Diverse Domains through World Models / DreamerV3 (Hafner et al.)
- Locator: https://arxiv.org/abs/2301.04104
- Source type: `arxiv_primary` | Published: `2023-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O15` | Modality: `latent-dynamics` | Role: `counterweight-pole`
- X axes: `X02`
- Claim notes: RSSM latent dynamics for planning + training (Atari/DMC/Minecraft); task-return gains, not visual fidelity. Non-generative pole anchor. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); control-oriented measures are the exhibit.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open)`

## VM-D103 — Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture / I-JEPA (LeCun et al.)
- Locator: https://arxiv.org/abs/2301.08243
- Source type: `arxiv_primary` | Published: `2023-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O15` | Modality: `predictive-representation` | Role: `counterweight-pole`
- X axes: `X01`
- Claim notes: Predictive representation without generation; JEPA-pole origin for the V-JEPA succession. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); image-side pole, video succession needs V-JEPA record.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D104 — Revisiting Feature Prediction / V-JEPA (Bardes et al.)
- Locator: https://arxiv.org/abs/2404.08471
- Source type: `arxiv_primary` | Published: `2024-02` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O15` | Modality: `predictive-representation` | Role: `counterweight-pole`
- X axes: `X01`
- Claim notes: Feature-prediction-only video SSL (no pixels/text/negatives/reconstruction); VideoMix2M 2M videos; frozen K400 81.9 / SSv2 72.2 / IN1K 77.9. Diffusion-pixel decoder is post-hoc probe only (encoder frozen). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID corrected at intake (Round B guess 2307.07420 wrong).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open)`
- repo: https://github.com/facebookresearch/jepa

## VM-D105 — Genie: Generative Interactive Environments (Bruce et al.)
- Locator: https://arxiv.org/abs/2402.15391
- Source type: `arxiv_primary` | Published: `2024-02` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O15` | Modality: `interactive-generative` | Role: `pole-origin`
- X axes: `X02`
- Claim notes: Latent-action interactive environment from unlabelled video; generative-interactive pole origin. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- Current-case role: `ARCHITECTURE_CASE (open)`

## VM-D106 — Genie 3 (DeepMind blog)
- Locator: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
- Source type: `first_party_vendor_blog` | Published: `2025-08` | Access: `OFFICIAL_PAGE_VERIFIED`
- Obligations: `VM-O15` | Modality: `interactive-generative` | Role: `current-case`
- X axes: `X02`, `X04`
- Claim notes: Real-time 24fps/720p interactive worlds; minutes-scale consistency; 1-min visual memory; promptable world events; SIMA training use; 5 stated limitations; research-preview gating. [retrieval: OFFICIAL_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: No paper/weights: NEVER architecture authority; vendor framing (NeRF/3DGS contrast) is attributed, not adopted.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- Current-case role: `CAPABILITY_CASE + DEPLOYMENT-pointer`

## VM-D107 — Genie 3 model page (DeepMind)
- Locator: https://deepmind.google/models/genie/
- Source type: `first_party_release_or_docs` | Published: `2025-08` | Access: `MODEL_CARD_OR_PAGE_VERIFIED`
- Obligations: `VM-O15` | Modality: `interactive-generative` | Role: `current-case`
- X axes: `X04`
- Claim notes: Product-form capability/deployment pointer companion to the blog record; same role cap. [retrieval: OFFICIAL_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Same cap as VM-D106; kept as separate locator for deployment-fact binding.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 partial
- Current-case role: `CAPABILITY_CASE + DEPLOYMENT-pointer`
