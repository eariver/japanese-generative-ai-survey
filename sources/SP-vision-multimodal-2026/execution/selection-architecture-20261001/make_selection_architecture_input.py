#!/usr/bin/env python3
"""Generate TS-003 interactive Selection/Architecture input (111 assignments + 15 packages)."""
import json
from datetime import datetime, timezone

ISSUE = "SP-vision-multimodal-2026"
OUT = "sources/SP-vision-multimodal-2026/execution/selection-architecture-20261001/interactive-selection-architecture.json"

PUB_P = "LONGFORM_SPECIAL:primary-narrative"
PUB_S = "LONGFORM_SPECIAL:supporting-context"
PUB_E = "LONGFORM_SPECIAL:evaluation-contract"
PUB_C = "LONGFORM_SPECIAL:capability-context"
ARC_T = "THEMATIC:transition-anchor"
ARC_L = "THEMATIC:lineage-context"
ARC_E = "THEMATIC:evaluation-authority"
ARC_D = "THEMATIC:deployment-context"
ARC_P = "THEMATIC:predecessor-context"

# did: (usage, pub_role, arch_role, rationale)
A = {
# P01 learned representation (context-capped)
"VM-D001": ("SUPPORTING", PUB_S, ARC_P, "Neocognitron origin context; anti-abrupt-start background, short treatment."),
"VM-D002": ("SUPPORTING", PUB_S, ARC_P, "LeNet predecessor context with access barrier; existence proof for the scaling break, not a mechanism anchor."),
"VM-D003": ("PRIMARY", PUB_P, ARC_T, "AlexNet large-scale supervised + GPU-scaling break; required D01 anchor."),
"VM-D004": ("PRIMARY", PUB_P, ARC_T, "ResNet residual-optimization break with detection/segmentation transfer; required D01 anchor."),
# P02 detection
"VM-D005": ("PRIMARY", PUB_P, ARC_T, "R-CNN region-proposal origin + pre-train/fine-tune paradigm."),
"VM-D006": ("PRIMARY", PUB_P, ARC_T, "Faster R-CNN two-stage capstone; anchor/NMS machinery reference."),
"VM-D007": ("PRIMARY", PUB_P, ARC_T, "YOLO one-stage operating-point origin; latency/accuracy trade-off reference."),
"VM-D008": ("SUPPORTING", PUB_S, ARC_L, "SSD non-YOLO one-stage branch; thin lineage-completeness node."),
"VM-D009": ("SUPPORTING", PUB_S, ARC_L, "RetinaNet dense-imbalance treatment; thin lineage-completeness node."),
"VM-D010": ("PRIMARY", PUB_P, ARC_T, "DETR set-prediction transition removing anchors/NMS; base of grounding detectors."),
"VM-D011": ("PRIMARY", PUB_P, ARC_T, "DINO detector: DETR capstone and Grounding DINO substrate (name-disambiguated)."),
"VM-D012": ("PRIMARY", PUB_P, ARC_T, "YOLO-World: open-vocabulary detection at a real-time operating point; D02-D07B bridge."),
# P03 segmentation
"VM-D013": ("PRIMARY", PUB_P, ARC_T, "FCN dense-prediction origin with classifier-transfer contract."),
"VM-D014": ("SUPPORTING", PUB_S, ARC_L, "U-Net segmentation-role node; diffusion-backbone history excluded (TS-002)."),
"VM-D015": ("PRIMARY", PUB_P, ARC_T, "Mask R-CNN instance-segmentation bridge between box and dense lineages."),
"VM-D016": ("SUPPORTING", PUB_S, ARC_L, "Panoptic contract node; definition + citation depth."),
"VM-D017": ("PRIMARY", PUB_P, ARC_T, "SAM promptable task/model/data system; first vision-foundation event with dual reading."),
"VM-D018": ("PRIMARY", PUB_P, ARC_T, "SAM 2 streaming-memory bridge from dense perception to temporal state."),
# P04 spatial substrate (hard cap)
"VM-D019": ("PRIMARY", PUB_P, ARC_T, "MiDaS relative-depth support node with zero-shot-transfer eval contract."),
"VM-D020": ("PRIMARY", PUB_P, ARC_T, "OpenPose keypoint/association support node; why classification features cannot drive action."),
"VM-D021": ("PRIMARY", PUB_P, ARC_T, "Visual Genome relational structure + region-language grounding-data predecessor."),
"VM-D022": ("PRIMARY", PUB_P, ARC_T, "DUSt3R calibration-free geometric-state support node; D04-D09/D13 bridge."),
# P05 document intelligence
"VM-D023": ("PRIMARY", PUB_P, ARC_T, "LayoutLM text+layout pre-training origin."),
"VM-D024": ("PRIMARY", PUB_P, ARC_T, "LayoutLMv3 unified masking successor."),
"VM-D025": ("PRIMARY", PUB_P, ARC_T, "Donut OCR-free branch; Nougat/GOT lineage predecessor."),
"VM-D026": ("PRIMARY", PUB_P, ARC_T, "Pix2Struct screenshot-parsing transition with D12 handoff."),
"VM-D027": ("PRIMARY", PUB_P, ARC_T, "Nougat specialist pole (open architecture) with failure profile; no numeric ranking."),
"VM-D028": ("PRIMARY", PUB_P, ARC_T, "GOT OCR-2.0 specialist pole with token-policy exhibit; no numeric ranking."),
"VM-D029": ("SUPPORTING", PUB_S, ARC_L, "Qwen3-VL-Embedding retrieval sub-lane anchor (preprint status bound)."),
"VM-D108": ("SUPPORTING", PUB_E, ARC_E, "DocVQA structure-reading eval with ANLS discipline."),
"VM-D109": ("SUPPORTING", PUB_E, ARC_E, "ChartQA visual+logical chart eval with relaxed-accuracy semantics."),
# P06 visual foundations
"VM-D030": ("PRIMARY", PUB_P, ARC_T, "ViT convolution-to-sequence break; fusion precondition."),
"VM-D031": ("SUPPORTING", PUB_S, ARC_L, "DeiT data-efficiency/recipe bridge in the architecture-vs-scale debate."),
"VM-D032": ("SUPPORTING", PUB_S, ARC_L, "Swin hierarchy node for vision-Transformer completeness."),
"VM-D033": ("PRIMARY", PUB_P, ARC_T, "MAE masked label-free pretraining anchor."),
"VM-D034": ("PRIMARY", PUB_P, ARC_T, "DINO self-supervised anchor with emergent boundaries (name-disambiguated)."),
"VM-D035": ("PRIMARY", PUB_P, ARC_T, "DINOv2 scaled foundation features; SAM-contrast pole."),
"VM-D036": ("PRIMARY", PUB_P, ARC_T, "SigLIP sigmoid-loss alignment + encoder-reuse lineage into Qwen (G06 citation residual)."),
# P07A alignment
"VM-D037": ("SUPPORTING", PUB_S, ARC_P, "Show-and-Tell captioning predecessor; anti-CLIP-abruptness context."),
"VM-D038": ("SUPPORTING", PUB_E, ARC_E, "VQA task predecessor and language-prior-shortcut origin shared with D10."),
"VM-D039": ("PRIMARY", PUB_P, ARC_T, "CLIP language-addressability break with preserved bag-of-words limitation."),
"VM-D040": ("SUPPORTING", PUB_S, ARC_L, "ALIGN noisy web-scale scaling variant."),
# P07B grounding (full chain)
"VM-D041": ("PRIMARY", PUB_P, ARC_T, "Flickr30k Entities phrase-localization task origin."),
"VM-D042": ("PRIMARY", PUB_P, ARC_T, "RefCOCO REC contract home (locator corrected at intake)."),
"VM-D043": ("PRIMARY", PUB_P, ARC_T, "OVR-CNN OVD formulation origin; recognition/localization disentanglement."),
"VM-D044": ("PRIMARY", PUB_P, ARC_T, "ViLD CLIP-distillation transfer with LVIS-rare protocol entry."),
"VM-D045": ("PRIMARY", PUB_P, ARC_T, "RegionCLIP region-pretraining pole with domain-shift diagnosis."),
"VM-D046": ("PRIMARY", PUB_P, ARC_T, "Detic vocabulary-supervision pole (ID corrected at intake)."),
"VM-D047": ("PRIMARY", PUB_P, ARC_T, "GLIP detection-as-grounding reformulation + grounding-data practice."),
"VM-D048": ("PRIMARY", PUB_P, ARC_T, "MDETR modulated multi-task detector (early-fusion pole)."),
"VM-D049": ("PRIMARY", PUB_P, ARC_T, "OWL-ViT minimal-head late-fusion pole."),
"VM-D050": ("PRIMARY", PUB_P, ARC_T, "Grounding DINO tight-fusion unification with REC evaluation norm."),
"VM-D051": ("PRIMARY", PUB_P, ARC_T, "OWL-ST/OWLv2 web-scale self-training scaling with label-space binding."),
"VM-D052": ("PRIMARY", PUB_P, ARC_T, "LSeg pixel-text alignment origin for the OVS branch."),
"VM-D053": ("PRIMARY", PUB_P, ARC_T, "X-Decoder generic+referring unification without pseudo-labeling."),
"VM-D054": ("SUPPORTING", PUB_S, ARC_L, "OpenSeg image-level-label scaling variant (bounded, not equal-depth)."),
"VM-D055": ("SUPPORTING", PUB_S, ARC_L, "ODISE diffusion-backbone OVS pole with TS-002 crossover flag."),
"VM-D056": ("PRIMARY", PUB_E, ARC_E, "LVIS rare-split eval home for open-vocabulary measurement."),
# P08 bridges
"VM-D057": ("SUPPORTING", PUB_S, ARC_P, "Frozen precursor context for frozen-component design space."),
"VM-D058": ("PRIMARY", PUB_P, ARC_T, "Flamingo few-shot gated-cross-attention bridge with inherited-LM limits."),
"VM-D059": ("PRIMARY", PUB_P, ARC_T, "BLIP-2 frozen-frozen Q-Former bridge; compute-efficiency exhibit."),
"VM-D060": ("PRIMARY", PUB_P, ARC_T, "InstructBLIP instruction-tuning systematization bridging BLIP-2 and LLaVA."),
"VM-D061": ("SUPPORTING", PUB_S, ARC_L, "MiniGPT-4 open minimal-alignment bridge function."),
"VM-D062": ("PRIMARY", PUB_P, ARC_T, "LLaVA visual instruction tuning anchor with machine-generated data contract."),
"VM-D063": ("SUPPORTING", PUB_S, ARC_L, "Molmo v1 open-data thesis origin + pointing interface; Molmo 2 predecessor."),
# P09 fusion/omni
"VM-D064": ("SUPPORTING", PUB_S, ARC_L, "Qwen2.5-VL dynamic-resolution/time-encoding predecessor."),
"VM-D065": ("PRIMARY", PUB_P, ARC_T, "Qwen3-VL open architecture case: interleaved-MRoPE, DeepStack, timestamp alignment (vendor measures quarantined)."),
"VM-D066": ("PRIMARY", PUB_P, ARC_T, "Qwen3-Omni open input/fusion case: TM-RoPE absolute-time sync; generation side excluded."),
"VM-D067": ("PRIMARY", PUB_P, ARC_T, "Whisper speech-input encoder precedent (input-side only)."),
"VM-D068": ("PRIMARY", PUB_P, ARC_T, "BEATs general-audio SSL input contract via acoustic tokenizers."),
"VM-D069": ("PRIMARY", PUB_P, ARC_T, "CLAP audio-side addressability; explicit CLIP-parallel."),
"VM-D070": ("PRIMARY", PUB_P, ARC_T, "InternVL3 native-joint-pretraining paradigm contrast (anti-Qwen-only anchor)."),
"VM-D071": ("PRIMARY", PUB_P, ARC_T, "Molmo 2 grounding/video comparator with openness gradient (Qwen dependence disclosed)."),
"VM-D072": ("SUPPORTING", PUB_C, ARC_D, "Gemini 3.1 Pro closed capability/eval/deployment comparator; never architecture."),
"VM-D073": ("SUPPORTING", PUB_C, ARC_D, "Gemini 3.6 Flash efficiency-pole comparator; capability facts only."),
"VM-D074": ("SUPPORTING", PUB_S, ARC_D, "Qwen3-VL repo inspectability/deployment exhibit (commit binding deferred)."),
"VM-D075": ("SUPPORTING", PUB_S, ARC_D, "Qwen3-Omni repo streaming-omni deployment exhibit (commit binding deferred)."),
"VM-D076": ("SUPPORTING", PUB_S, ARC_D, "InternVL repo + data-release openness exhibit (file-level scope deferred)."),
"VM-D077": ("SUPPORTING", PUB_S, ARC_D, "molmo2 full-stack openness exhibit (license mix deferred, PARTIAL kept)."),
# P10 reasoning/failure
"VM-D078": ("SUPPORTING", PUB_E, ARC_E, "MMMU comprehensive-reasoning eval home; scaffold ablations required."),
"VM-D079": ("SUPPORTING", PUB_E, ARC_E, "POPE polling screen complementary to control-pair diagnosis."),
"VM-D080": ("PRIMARY", PUB_E, ARC_E, "HallusionBench control-pair failure-attribution diagnosis (language vs vision)."),
"VM-D081": ("SUPPORTING", PUB_E, ARC_E, "MMBench bilingual CircularEval anchor with judge-dependence note."),
"VM-D082": ("SUPPORTING", PUB_E, ARC_E, "MathVista visual-math node with attribution caveats."),
# P11 video/streaming
"VM-D083": ("SUPPORTING", PUB_S, ARC_P, "Kinetics action-recognition predecessor; frame-repeat baseline."),
"VM-D084": ("SUPPORTING", PUB_S, ARC_P, "Something-Something ordering-sensitive predecessor."),
"VM-D085": ("PRIMARY", PUB_P, ARC_T, "Ego4D egocentric/AV/trajectory data predecessor shared with VLA ancestry."),
"VM-D086": ("SUPPORTING", PUB_E, ARC_E, "Video-MME duration-x-modality breadth eval."),
"VM-D087": ("SUPPORTING", PUB_E, ARC_E, "LongVideoBench referred-context reasoning eval (distinct contract)."),
"VM-D088": ("PRIMARY", PUB_E, ARC_E, "StreamingBench streaming-eval contract (timestamped + omni-source + proactive)."),
"VM-D089": ("PRIMARY", PUB_P, ARC_T, "Flash-VStream open streaming-system anchor (memory, async queries, latency/VRAM)."),
"VM-D111": ("SUPPORTING", PUB_E, ARC_E, "VSI-Bench video-based spatial-intelligence eval (PARTIAL depth; debiased subset deferred)."),
# P12 computer use
"VM-D090": ("PRIMARY", PUB_P, ARC_T, "OSWorld real-OS environment + grounding-bottleneck thesis."),
"VM-D091": ("PRIMARY", PUB_P, ARC_T, "OSWorld 2.0 state-management thesis + token-cost curves (strictest binding in volume)."),
"VM-D092": ("PRIMARY", PUB_P, ARC_T, "SeeClick/ScreenSpot pure element-localization accuracy distinct from task success."),
# P13 VLA
"VM-D093": ("PRIMARY", PUB_P, ARC_T, "SayCan planner-side grounding without joint representation."),
"VM-D094": ("PRIMARY", PUB_P, ARC_T, "RT-1 scaled trajectory/data-regime predecessor."),
"VM-D095": ("PRIMARY", PUB_P, ARC_T, "PaLM-E embodied joint-representation break."),
"VM-D096": ("PRIMARY", PUB_P, ARC_T, "Open X-Embodiment cross-embodiment data contract (X01 exhibit)."),
"VM-D097": ("PRIMARY", PUB_P, ARC_T, "RT-2 VLA formulation origin (action tokens + co-fine-tuning)."),
"VM-D098": ("PRIMARY", PUB_P, ARC_T, "OpenVLA open-weights inspection pole (G01 independent-eval gap preserved)."),
"VM-D099": ("SUPPORTING", PUB_C, ARC_D, "Gemini Robotics 2 closed capability/deployment endpoint (planner-policy split noted)."),
"VM-D100": ("SUPPORTING", PUB_E, ARC_D, "On-Device 2 card-scoped evaluation + deployment case with stated limits."),
# P14 world models
"VM-D101": ("PRIMARY", PUB_P, ARC_T, "Ha/Schmidhuber historical formulation anchor with non-ancestry guard."),
"VM-D102": ("PRIMARY", PUB_P, ARC_T, "DreamerV3 latent-dynamics counterweight with task-return exhibit."),
"VM-D103": ("PRIMARY", PUB_P, ARC_T, "I-JEPA predictive-representation pole origin."),
"VM-D104": ("PRIMARY", PUB_P, ARC_T, "V-JEPA feature-prediction-only video SSL counterweight (ID corrected)."),
"VM-D105": ("PRIMARY", PUB_P, ARC_T, "Genie generative-interactive pole origin (open paper)."),
"VM-D106": ("SUPPORTING", PUB_C, ARC_D, "Genie 3 closed capability + deployment-pointer with 5 stated limits; never architecture."),
"VM-D107": ("SUPPORTING", PUB_C, ARC_D, "Genie 3 model-page deployment-fact companion locator."),
# P15 evaluation/convergence
"VM-D110": ("PRIMARY", PUB_E, ARC_E, "OCRBench v2 localization+reasoning text eval with private-set discipline (v1 superseded)."),
}

PACKAGES = [
("P01", "Learned visual representation and transfer", "What changed when handcrafted features gave way to learned reusable hierarchies at ImageNet scale, and what optimization break made very deep representation transferable.", ["VM-D003", "VM-D004"], ["VM-D001", "VM-D002"],
 ["VM-O01 context-capped scope holds; no pre-deep CV expansion", "X01 large-scale supervised contract visible", "TS-001 efficiency vocabulary reused, not retold"],
 ["Pre-deep history stays context-only; scaling-recipe reading over novelty reading", "No transfer claims beyond successor evidence"], 1),
("P02", "Detection and structured localization", "Why image-level classification is insufficient once object identity must pair with location; from region proposals through operating points to set prediction and the open-vocabulary bridge.", ["VM-D005", "VM-D006", "VM-D007", "VM-D010", "VM-D011", "VM-D012"], ["VM-D008", "VM-D009"],
 ["VM-O02 lineage complete incl. DINO-name disambiguation", "Anchors/NMS read as fossilized machinery DETR removes", "X02 box in/out contracts explicit"],
 ["One-stage history not reduced to one product family; version-bound YOLO claims only"], 2),
("P03", "Dense perception and promptable vision", "Why boxes are insufficient for dense region/pixel structure; semantic/instance/panoptic distinctions and the promptable-foundation transition with its video bridge.", ["VM-D013", "VM-D015", "VM-D017", "VM-D018"], ["VM-D014", "VM-D016"],
 ["VM-O03 distinctions preserved; U-Net segmentation-role only", "SAM dual reading carried; SAM 2 as architecture pointer not system case"],
 ["No TS-002 diffusion-backbone retelling; panoptic at contract depth"], 3),
("P04", "Spatial and geometric substrate (support-capped)", "What geometry/spatial state is absent from labels, what 2D/2.5D/3D state later reasoning assumes, and what survives tokenization — four nodes only.", ["VM-D019", "VM-D020", "VM-D021", "VM-D022"], [],
 ["D04 four-node hard cap holds (MiDaS/OpenPose/VisualGenome/DUSt3R)", "X02 spatial-state contracts feed D10/D12/D13"],
 ["No NeRF/3DGS/SLAM/MVS/3D-detection/SMPL/benchmark-zoo expansion; successors add no new contract"], 4),
("P05", "OCR to Document Intelligence", "From glyph recognition to layout/structure/symbolic understanding; specialist vs generalist interfaces compared qualitatively; the native-multimodal OCR-bottleneck test.", ["VM-D023", "VM-D024", "VM-D025", "VM-D026", "VM-D027", "VM-D028"], ["VM-D029", "VM-D108", "VM-D109"],
 ["VM-O05 normal weight; NO_CROSS_MODEL_NUMERIC_COMPARISON holds (G03)", "Retrieval bounded sub-lane only; screenshot/UI hands off to P12 by paragraph"],
 ["Specialist failure profiles (repetition/language/structure) over rankings; resolution/token policies bound"], 5),
("P06", "Transformer and self-supervised visual foundations", "Separating token formulation, architecture, pretraining objective and distillation mechanism; scale-vs-recipe debate and encoder reuse into VLMs.", ["VM-D030", "VM-D033", "VM-D034", "VM-D035", "VM-D036"], ["VM-D031", "VM-D032"],
 ["VM-O06 lineage complete; G06 SigLIP2 citation residual bounded", "TS-001 owns generic attention efficiency; TS-003 owns representation contract"],
 ["No generic Transformer-efficiency retelling; recipe reading preserved"], 6),
("P07A", "Image-level vision-language alignment", "From fixed class ontology to natural-language-addressable image semantics via paired pretraining; zero-shot transfer as the break.", ["VM-D039"], ["VM-D037", "VM-D038", "VM-D040"],
 ["D07A metric identity (zero-shot/retrieval) never merged with D07B localization metrics", "X01 image-text pair contracts visible; bag-of-words limit recorded as D07B motivator"],
 ["Captioning/VQA predecessors prevent CLIP ex-nihilo; generation detail stays TS-002"], 7),
("P07B", "Open-vocabulary perception and grounding", "From arbitrary language concepts to boxes/masks/coordinates/evidence: the minimum non-redundant chain from phrase localization through web-scale self-training plus the OVS branch.", ["VM-D041", "VM-D042", "VM-D043", "VM-D044", "VM-D045", "VM-D046", "VM-D047", "VM-D048", "VM-D049", "VM-D050", "VM-D051", "VM-D052", "VM-D053", "VM-D056"], ["VM-D054", "VM-D055"],
 ["D07B full chain preserved (never CLIP + Grounding DINO only); D07A/D07B metric split enforced", "LVIS-rare/ODinW/RefCOCO/phrase-Recall@K identities kept distinct", "GLIP/OWL-ViT/Grounding-DINO IDs rebound at intake; unseen claims label-space-bound"],
 ["Redundancy calls stand (distillation vs pretraining vs vocabulary vs reformulation vs fusion vs scaling); OWOD stays footnote"], 8),
("P08", "Bridging pretrained vision and language systems", "How separately pretrained components became usable VLMs: projector/resampler/Q-Former/cross-attention strategies, frozen-component economics, and visual instruction tuning.", ["VM-D058", "VM-D059", "VM-D060", "VM-D062"], ["VM-D057", "VM-D061", "VM-D063"],
 ["Bridge generations kept distinct (no generic vision-encoder+LLM sentence)", "Frozen-component tradeoff reused from TS-001 vocabulary; durable modularity evidenced by Qwen stack"],
 ["InstructBLIP/MiniGPT-4 gap filled; precursor stays one line"], 9),
("P09", "Native and omni multimodal fusion", "How image/video/audio become model-consumable token/state sequences: resolution, resampling, fusion depth, time alignment, and context/memory/latency consequences; input-side audio only.", ["VM-D065", "VM-D066", "VM-D067", "VM-D068", "VM-D069", "VM-D070", "VM-D071"], ["VM-D064", "VM-D072", "VM-D073", "VM-D074", "VM-D075", "VM-D076", "VM-D077"],
 ["Two technically distinct open families (InternVL3 paradigm contrast, Molmo 2 grounding comparator); no Qwen-only narrative", "Audio chain Whisper/BEATs/CLAP/omni-sync with synthesis excluded (TS-002)", "Vendor latency/token figures config-bound (CV2-DM-020); X03 fields multimodal-specific only"],
 ["M-RoPE lineage thread; Thinker-Talker streaming subordinated to input/fusion side"], 10),
("P10", "Multimodal reasoning and failure decomposition", "Decomposing composite scores into perception, OCR, grounding, language-prior, reasoning, hallucination and scaffold effects; control-pair diagnosis as the signature instrument.", ["VM-D080"], ["VM-D078", "VM-D079", "VM-D081", "VM-D082"],
 ["No benchmark as general intelligence; language-prior vs evidence-use separation per score", "Polling vs control-pair vs CircularEval vs visual-math kept distinct; judge/contamination disciplines travel"],
 ["Thinking-variant ablations required for attribution; tool-assisted perception where material"], 11),
("P11", "Video understanding, temporal state and streaming", "From frame repetition to genuine temporal state: ordering, causal/physical reasoning, long-video memory, online streaming state, and audiovisual understanding; offline vs online never share a column.", ["VM-D085", "VM-D088", "VM-D089"], ["VM-D083", "VM-D084", "VM-D086", "VM-D087", "VM-D111"],
 ["Offline long-context vs online streaming contracts separated", "Frame-count sensitivity and async-query/memory policies recorded", "VSI-Bench PARTIAL depth carried with debiased-subset deferral"],
 ["VStream-QA as cited predecessor; SAM 2 memory as architecture pointer"], 12),
("P12", "Computer Use as actionable digital grounding", "From screenshots to element grounding to coordinate/tool action to persistent task state; interface contracts compared; long-horizon state over click accuracy.", ["VM-D090", "VM-D091", "VM-D092"], [],
 ["Bounded endpoint; OSWorld 1.0 vs 2.0 distinct contracts (grounding vs state-management thesis)", "Screenshot-loop token costs via TS-001 vocabulary; safety audits as eval metadata only"],
 ["No general agent-architecture survey; web-phase predecessors stay context"], 13),
("P13", "Vision-Language-Action and embodied interfaces", "Seven-node minimum chain from planner-side grounding through action tokenization to open implementation and card-scoped deployment; representation/action interface only.", ["VM-D093", "VM-D094", "VM-D095", "VM-D096", "VM-D097", "VM-D098"], ["VM-D099", "VM-D100"],
 ["Hard cap holds: no kinematics/dynamics/gait/hardware/locomotion/safety-policy content", "G01 independent-eval scarcity preserved as limitation; vendor pages never architecture"],
 ["SayCan planner-side role sharpens (not duplicates) PaLM-E joint break"], 14),
("P14", "Predictive representations and world models", "Four-pole terminology contract: historical formulation, latent dynamics, non-generative prediction, generative interactive environment; state/target/conditioning/pixel-latent-reward/use bound per case.", ["VM-D101", "VM-D102", "VM-D103", "VM-D104", "VM-D105"], ["VM-D106", "VM-D107"],
 ["Terminology split enforced; non-ancestry guard (no Ha-to-Genie technical ancestry)", "Photorealism-only exhibits stay TS-002 references; G02 control-oriented-measures gap preserved", "Anti-collapse row required per exhibit"],
 ["Genie 3 capability-capped with 5 stated limits; Waymo pointer pending primary source"], 15),
("P15", "Measurement, limits and convergence", "Task-identity-preserving evaluation synthesis: what each contract measures and misses, condition binding, vendor-vs-independent separation, and the unified-vs-modular convergence verdict with supervision-timeline synthesis.", ["VM-D110"], [],
 ["Methodology-first: distinct contracts only, no catalogue, no cross-family ranking", "OCRBench v2 private-set discipline + recognition-vs-spotting gap as signature exhibits", "X01 timeline synthesis and convergence verdict live here, not as predetermined unity"],
 ["All other eval authorities support their home packages; convergence stays an open evidence-backed question"], 16),
]


def main() -> int:
    import os
    assert set(A) == {f"VM-D{i:03d}" for i in range(1, 112)}, "assignments must cover 111"
    prim = [d for d, v in A.items() if v[0] == "PRIMARY"]
    supp = [d for d, v in A.items() if v[0] == "SUPPORTING"]
    assert len(prim) + len(supp) == 111
    # placement coverage: every ID exactly once across packages
    placed = []
    for pid, title, purpose, pp, ss, reqs, bounds, order in PACKAGES:
        assert pp and not (set(pp) & set(ss)), pid
        placed += pp + ss
    assert sorted(placed) == sorted(A), f"placement mismatch: {len(placed)}"
    # usage/placement consistency
    by_place = {}
    for pid, title, purpose, pp, ss, reqs, bounds, order in PACKAGES:
        for d in pp:
            by_place.setdefault(d, []).append(("PRIMARY", pid))
        for d in ss:
            by_place.setdefault(d, []).append(("SUPPORTING", pid))
    for d, spots in by_place.items():
        assert len(spots) == 1, (d, spots)
        assert spots[0][0] == A[d][0], (d, spots, A[d][0])
    print(f"PRIMARY={len(prim)} SUPPORTING={len(supp)} packages={len(PACKAGES)}")
    orders = [o for *_, o in PACKAGES]
    assert sorted(orders) == list(range(1, 17)) or sorted(orders) == list(range(1, 16)), orders

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    assignments = []
    for did in sorted(A):
        usage, pub, arch, rationale = A[did]
        assignments.append({
            "discovery_id": did, "disposition": "SELECTED", "rationale": rationale,
            "architecture_usage": usage, "publication_role": pub, "architecture_role": arch,
            "profile_extensions": {},
        })
    packages = []
    for pid, title, purpose, pp, ss, reqs, bounds, order in PACKAGES:
        packages.append({
            "package_id": pid, "title": title, "purpose": purpose,
            "primary_discovery_ids": pp, "supporting_discovery_ids": ss,
            "must_cover_requirements": reqs, "boundaries": bounds,
            "drafting_order": order, "profile_extensions": {}, "publication_extensions": {},
        })
    doc = {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE,
        "runner": {
            "provider": "Muse",
            "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
            "invocation": ("Operator Selection/Architecture judgments under Sol request Sections 3-9: "
                           "16-arc preservation, D04 cap, D07A/D07B separation, endpoint bounds, "
                           "role discipline, eval-contract separation, no count optimization"),
            "generated_at": now,
        },
        "assignments": assignments,
        "architecture": {
            "editorial_thesis": ("TS-003 completes the three-volume arc — TS-001 computes intelligence, TS-002 "
                "generates the world, TS-003 perceives, grounds, reasons about, predicts and acts in it — "
                "by reconstructing partially independent technical lineages that converge late, organized as "
                "interacting problem layers (representation, recognition, localization/structure, language "
                "alignment, grounding, fusion, temporal/spatial state, reasoning, action/prediction) rather "
                "than a single model chronology. The cross-cutting test throughout is what representation of "
                "the world is sufficient for the next computation: what each stage preserves, discards, "
                "localizes, tokenizes, grounds, reasons over, predicts or acts upon."),
            "architecture_goals": [
                "Preserve all 16 accepted technical arcs without collapsing them into a famous-model ladder.",
                "Keep image-level alignment and open-vocabulary grounding as distinct contracts, metrics and packages.",
                "Hold the D04 four-node support cap and refuse 3D-vision-textbook expansion.",
                "Keep D12-D14 as bounded convergence endpoints (about 15% weight), not the book's spine.",
                "Make X01-X04 visible inside load-bearing packages with a Part V synthesis, not an appendix.",
                "Enforce evaluation-contract separation: no catalogue, no cross-task ranking, vendor attribution always.",
                "Prefer technically distinct current cases over similar families; never infer architecture from pages/demos.",
            ],
            "page_plan": {"target_pages": 104, "max_pages": 120,
                          "notes": ("Front matter 4; Parts I-III (P01-P11) 68; Part IV endpoints (P12-P14) 16; "
                                    "Part V evaluation/convergence (P15) 12; back matter 4. Depth over brevity; "
                                    "endpoint packages capped regardless of recency; no lane compressed to token "
                                    "paragraphs to meet a cap.")},
            "packages": packages,
            "selected_exceptions": [],
            "profile_extensions": {},
            "publication_extensions": {},
        },
    }
    os.makedirs("sources/SP-vision-multimodal-2026/execution/selection-architecture-20261001", exist_ok=True)
    out = "sources/SP-vision-multimodal-2026/execution/selection-architecture-20261001/interactive-selection-architecture.json"
    with open(out, "w") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote:", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
