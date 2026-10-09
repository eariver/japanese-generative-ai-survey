# Coverage-closure artifact — TS-003 late-cutoff expansion (ONE-TIME bounded sweep)

Status: `DISCOVERY_COVERAGE_FROZEN` RECOMMENDED (pending replay + Human r5 review).
Window: late 2024 → cutoff 2026-09-30. Obligations fixed at 16; no new dimensions/packages.

## Admitted (8): each changes a technical contract (criteria 1–5 verified)

- VM-D113 DINOv3 (P06): Gram-anchored dense refinement under long training + frozen
  reusable dense SOTA. Contract: self-distillation refinement for dense longevity.
- VM-D114 SigLIP 2 (P06 home; P07A/P07B/P09 support): staged sigmoid+captioning+
  self-distillation+masked-prediction+curation recipe; multilingual/debiased mixture;
  native aspect/multi-resolution; localization transfer. Contract: alignment-recipe transition.
- VM-D115 SAM 3 (P03 home; P07B/P11 support): promptable concept segmentation
  (NP/exemplar/visual prompts; detector + memory tracker; shared backbone).
  Contract: language-grounded concept interface. SAM 3D excluded; SAM 3.1 successor-context only.
- VM-D116 π₀ (P13): flow-matching continuous action expert on PaliGemma VLM; dexterous
  multi-robot regime. Contract: discrete-token vs flow-matching action interface.
- VM-D117 FAST (P13): DCT frequency-space action tokenization; chunk compression; FAST+.
  Contract: action representation/tokenization transition. Kept separate from π₀.
- VM-D118 AIMv2 (P06): autoregressive prefix-ViT + causal multimodal decoder (objective
  family distinct from masked/contrastive/distillation).
- VM-D119 UGround (P12/P08-scope): universal screenshot grounder; vision-only pixel-action
  interface break (SeeAct-V folded in-card as interface context, not a separate node).
- VM-D120 ScreenSpot-Pro (P12): professional high-res grounding evaluation + cascaded
  inference-time search contract (ScreenSeekeR folded in-card).

## Considered-but-deferred (no independent node required)

- V-JEPA 2 (+AC): same JEPA predictive pole as occupied V-JEPA; MPC deployment is
  application, not a new representation contract → successor-within-pole exclusion.
- Perception Encoder/PLM family: contemporaneous competing recipe explainable within the
  SigLIP 2/DINOv3 representation framing; full second encoder family exceeds bounded scope.
- Cosmos WFM platform: same generative-interactive pole as Genie/Genie 3; platform
  packaging ≠ new representation contract.
- Molmo-1/PixMo, Qwen2.5-VL predecessors: lineage subsets of covered Molmo 2 / Qwen3-VL.
- DINOv3-distilled small models, SigLIP2 WebLI-data specifics: detail/deployment variants.
- ScreenSpot-v2, OSWorld-Verified, OS-Atlas (given UGround+Pro), Veo/Sora successors,
  DROID mixture: bug-fix / subset / same-contract / adjacent-lane exclusions.

## Residual known limitations

- Post-cutoff successors (post-2026-09-30) out of scope by cutoff rule.
- Deferred items above are future-edition context, not Architecture defects.

## Coverage Freeze Rule (this run is the final planned Discovery expansion)

After the 8 admissions above, `DISCOVERY_COVERAGE_FROZEN` is RECOMMENDED. Later
Architecture/Draft reviews must NOT reopen Discovery merely for newer, stronger, more
popular, or more complete successor models. Discovery may be reopened ONLY for a
pre-cutoff omission introducing a genuinely missing technical contract whose absence
materially changes the Architecture thesis. Otherwise record as deferred/future-edition context.
