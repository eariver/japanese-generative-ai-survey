# Discovery observations — VM-O14 D13 VLA (HARD CAP)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Locomotion gaits, control theory, manipulation-hardware surveys refused; Gemini Robotics ER-2 planner-policy split noted as capability-level only; independent (non-vendor) VLA eval is a carried EVIDENCE_GAP.

## VM-D093 — Do As I Can, Not As I Say / SayCan (Ahn et al.)
- Locator: https://arxiv.org/abs/2204.01691
- Source type: `arxiv_primary` | Published: `2022-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `predecessor-node`
- X axes: `X02`
- Claim notes: Frozen-LLM planning x affordance value functions (planner-side grounding, NOT joint representation); 101 real kitchen tasks, 84%/74%; CoRL 2022 (PMLR v205). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Planner-side only; joint-embedding break needs PaLM-E-side sources.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D094 — RT-1 (Brohan et al.)
- Locator: https://arxiv.org/abs/2212.06817
- Source type: `arxiv_primary` | Published: `2022-12` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `predecessor-node`
- X axes: `X01`
- Claim notes: Large-scale real-robot demonstration-token corpus (kitchen tasks); data-regime predecessor for trajectory conditioning. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); data-scope claims only.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D095 — PaLM-E (Driess et al.)
- Locator: https://arxiv.org/abs/2303.03378
- Source type: `arxiv_primary` | Published: `2023-03` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `predecessor-node`
- X axes: `X02`
- Claim notes: Embodied joint representation: continuous sensor observations into the LM embedding space (the VLM-into-body break). [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D096 — Open X-Embodiment (O'Neill et al.)
- Locator: https://arxiv.org/abs/2310.08864
- Source type: `arxiv_primary` | Published: `2023-10` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `data-predecessor`
- X axes: `X01`
- Claim notes: Cross-embodiment data contract (X01 exhibit); multi-robot skill-transfer substrate. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); dataset claims, not policy claims.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent

## VM-D097 — RT-2 (Brohan/Zitkovich et al.)
- Locator: https://arxiv.org/abs/2307.15818
- Source type: `arxiv_primary` | Published: `2023-07` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `anchor`
- X axes: `X01`, `X02`
- Claim notes: VLA formulation origin: actions as text tokens; web-scale VL transfer into control via co-fine-tuning. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); formulation role fixed by Round C.
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- Current-case role: `ARCHITECTURE_CASE`

## VM-D098 — OpenVLA (Kim et al.)
- Locator: https://arxiv.org/abs/2406.09246
- Source type: `arxiv_primary` | Published: `2024-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `current-case`
- X axes: `X02`, `X04`
- Claim notes: Open-weights VLA implementation; inspection/ARCHITECTURE pole; CoRL 2024. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: ID verified at intake (API title match); independent-eval scarcity is a carried gap.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 absent
- Current-case role: `ARCHITECTURE_CASE (open)`

## VM-D099 — Gemini Robotics 2 (DeepMind)
- Locator: https://deepmind.google/models/gemini-robotics/
- Source type: `first_party_release_or_docs` | Published: `2026-07` | Access: `MODEL_CARD_OR_PAGE_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `current-case`
- X axes: `X02`, `X04`
- Claim notes: Whole-body humanoid VLA + planner-policy split (ER 2 + VLA) in production form; private-preview distribution. [retrieval: OFFICIAL_PAGE_VERIFIED; full-body consumption at Evidence stage]
- Limitation: NEVER architecture authority; page facts only; no latency/price/token facts published.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 absent
- Current-case role: `CAPABILITY_CASE + DEPLOYMENT_CASE`

## VM-D100 — Gemini Robotics On-Device 2 model card (DeepMind)
- Locator: https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/
- Source type: `first_party_release_or_docs` | Published: `2026-07` | Access: `MODEL_CARD_OR_PAGE_VERIFIED`
- Obligations: `VM-O14` | Modality: `vision-language-action` | Role: `current-case`
- X axes: `X02`, `X03`, `X04`
- Claim notes: On-device Gemma + Robotics 1.5 tech; text/image/proprioception-in, actions-out; trusted-testers-only; stated bi-arm-primary scope + high-DoF limits; layered-safety recommendation. [retrieval: MODEL_CARD_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Card-scoped eval only; OOD/whole-body outside scope (stated).
- TS-001/TS-002 overlap: TS-001 partial / TS-002 absent
- Current-case role: `CAPABILITY_CASE + EVALUATION_CASE (card-scoped) + DEPLOYMENT_CASE`
