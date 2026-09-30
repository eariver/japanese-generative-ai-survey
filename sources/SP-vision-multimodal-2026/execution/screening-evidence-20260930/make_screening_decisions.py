#!/usr/bin/env python3
"""TS-003 screening judgments: 111 explicit per-record dispositions.

Operator: Muse (Work execution role) applying the Sol Screening-through-Evidence
request Sections 3.1-3.3 against the THEMATIC Production Profile research
question and Round E scope. Preserves historically/load-bearing transition
nodes (no recency/popularity filter), D07A/D07B separation, D04 hard cap,
D12-D14 endpoint bounds, the full D07B grounding chain, two-family current
open-VLM coverage, streaming vs offline-long-context separation, and all six
G01-G06 gaps (negative space survives Screening). Not a Sol decision. Sol
reviews the Evidence outcome via a fresh Evidence Semantic Review.
"""

from __future__ import annotations

import json
from pathlib import Path

ISSUE_ID = "SP-vision-multimodal-2026"
OUT = Path("sources/SP-vision-multimodal-2026/execution/screening-evidence-20260930/interactive-decisions.json")

FULL = "Evidence-stage full-body verification"

# id: (decision, confidence, reason, scope_tags, verification_targets, duplicate_group)
J = {
# VM-O01 (context-capped; pre-AlexNet context + transition preserved)
"VM-D001": ("INSPECT", "medium", "Neocognitron origin context for learned hierarchies; paywalled journal page needs content binding at Evidence; context depth only per D01 cap.", ["VM-O01"], [FULL, "paywall content binding"], None),
"VM-D002": ("KEEP", "high", "LeNet end-to-end CNN origin; anti-abrupt-start predecessor context.", ["VM-O01"], [FULL, "author-PDF content binding"], None),
"VM-D003": ("KEEP", "high", "AlexNet large-scale supervised + GPU scaling break; required D01 anchor.", ["VM-O01"], [FULL, "proceedings-page content binding"], None),
"VM-D004": ("KEEP", "high", "ResNet residual-optimization break with detection/segmentation transfer; required D01 anchor.", ["VM-O01"], [FULL], None),
# VM-O02 (classification -> two-stage -> one-stage -> set prediction -> OV bridge)
"VM-D005": ("KEEP", "high", "R-CNN region-proposal detection origin; required D02 anchor.", ["VM-O02"], [FULL], None),
"VM-D006": ("KEEP", "high", "Faster R-CNN two-stage capstone with RPN; anchor/NMS machinery reference.", ["VM-O02"], [FULL], None),
"VM-D007": ("KEEP", "high", "YOLO one-stage operating-point origin; latency/accuracy trade-off reference.", ["VM-O02"], [FULL], None),
"VM-D008": ("MAYBE", "medium", "SSD non-YOLO one-stage branch; retained thin for lineage completeness, short treatment.", ["VM-O02"], [FULL], None),
"VM-D009": ("MAYBE", "medium", "RetinaNet dense-imbalance treatment; retained thin for lineage completeness, short treatment.", ["VM-O02"], [FULL], None),
"VM-D010": ("KEEP", "high", "DETR set-prediction transition removing anchors/NMS; required D02 anchor.", ["VM-O02"], [FULL], None),
"VM-D011": ("KEEP", "high", "DINO detector: DETR-lineage capstone and Grounding DINO base; DINO-name disambiguation enforced.", ["VM-O02", "VM-O08"], [FULL, "DINO detector vs self-supervised disambiguation"], None),
"VM-D012": ("KEEP", "high", "YOLO-World GLIP-formulation open-vocabulary YOLO; D02->D07B bridge case.", ["VM-O02", "VM-O08"], [FULL], None),
# VM-O03 (boxes -> dense -> panoptic -> promptable)
"VM-D013": ("KEEP", "high", "FCN dense-prediction origin; required D03 anchor.", ["VM-O03"], [FULL], None),
"VM-D014": ("KEEP", "high", "U-Net segmentation-role node; TS-002 diffusion-backbone role explicitly excluded.", ["VM-O03"], [FULL, "TS-002/TS-003 boundary: segmentation role only"], None),
"VM-D015": ("KEEP", "high", "Mask R-CNN instance-segmentation bridge; required D03 anchor.", ["VM-O03"], [FULL], None),
"VM-D016": ("MAYBE", "medium", "Panoptic contract node (definition + citation depth); retained for semantic/instance unification contract.", ["VM-O03"], [FULL], None),
"VM-D017": ("KEEP", "high", "SAM promptable task/model/data system; first vision-foundation event; dual reading carried.", ["VM-O03"], [FULL], None),
"VM-D018": ("KEEP", "high", "SAM 2 streaming-memory bridge D03->D11; architecture pointer, not a system case.", ["VM-O03", "VM-O12"], [FULL], None),
# VM-O04 (hard cap: exact 4 nodes)
"VM-D019": ("KEEP", "high", "MiDaS relative-depth support node; zero-shot-transfer eval contract; X01 mixing exhibit.", ["VM-O04"], [FULL], None),
"VM-D020": ("KEEP", "high", "OpenPose keypoint/association support node; why classification features cannot drive action.", ["VM-O04"], [FULL], None),
"VM-D021": ("KEEP", "high", "Visual Genome relational-structure + region-language support node; grounding-data predecessor.", ["VM-O04", "VM-O08"], [FULL], None),
"VM-D022": ("KEEP", "high", "DUSt3R learned geometric-state support node; calibration-free pointmap contract.", ["VM-O04"], [FULL], None),
# VM-O05 (glyph -> layout/symbolic; specialist vs generalist qualitative)
"VM-D023": ("KEEP", "high", "LayoutLM text+layout pre-training origin; required D05 anchor.", ["VM-O05"], [FULL], None),
"VM-D024": ("KEEP", "high", "LayoutLMv3 unified text-layout-image successor; required D05 node.", ["VM-O05"], [FULL], None),
"VM-D025": ("KEEP", "high", "Donut OCR-free branch; Nougat/GOT lineage predecessor.", ["VM-O05"], [FULL], None),
"VM-D026": ("KEEP", "high", "Pix2Struct screenshot-parsing transition; UI-as-document bridge with D12 handoff.", ["VM-O05"], [FULL], None),
"VM-D027": ("KEEP", "high", "Nougat specialist pole (open ARCHITECTURE_CASE); markup contract; no numeric ranking.", ["VM-O05"], [FULL, "NO_CROSS_MODEL_NUMERIC_COMPARISON"], None),
"VM-D028": ("KEEP", "high", "GOT OCR-2.0 specialist pole (open ARCHITECTURE_CASE); resolution/token policy exhibit.", ["VM-O05"], [FULL, "NO_CROSS_MODEL_NUMERIC_COMPARISON"], None),
"VM-D029": ("KEEP", "high", "Qwen3-VL-Embedding retrieval sub-lane anchor; document-RAG interface; preprint status to confirm at Evidence.", ["VM-O05", "VM-O10"], [FULL, "preprint version/status binding"], None),
# VM-O06 (token formulation + label-free representation; no efficiency retell)
"VM-D030": ("KEEP", "high", "ViT convolution-to-sequence break; fusion precondition; required D06 anchor.", ["VM-O06"], [FULL], None),
"VM-D031": ("KEEP", "high", "DeiT data-efficiency/recipe bridge; architecture-vs-scale debate exhibit.", ["VM-O06"], [FULL], None),
"VM-D032": ("KEEP", "high", "Swin hierarchy node; lineage completeness.", ["VM-O06"], [FULL], None),
"VM-D033": ("KEEP", "high", "MAE masked label-free pretraining anchor; required D06 node.", ["VM-O06"], [FULL], None),
"VM-D034": ("KEEP", "high", "DINO self-supervised anchor with emergent boundaries; DINO-name disambiguation enforced.", ["VM-O06"], [FULL, "DINO detector vs self-supervised disambiguation"], None),
"VM-D035": ("KEEP", "high", "DINOv2 all-purpose-features anchor; SAM-contrast pole.", ["VM-O06"], [FULL], None),
"VM-D036": ("KEEP", "high", "SigLIP alignment-variant + encoder-reuse lineage into Qwen3-VL/Omni; SigLIP2 citation binding at Evidence (G06).", ["VM-O06", "VM-O07"], [FULL, "G06 SigLIP2 citation binding"], None),
# VM-O07 (fixed ontology -> language-addressable; metrics never merged with O08)
"VM-D037": ("KEEP", "high", "Show and Tell captioning predecessor; anti-CLIP-abruptness context.", ["VM-O07"], [FULL], None),
"VM-D038": ("KEEP", "high", "VQA task predecessor and language-prior-shortcut origin; D10 control shared.", ["VM-O07", "VM-O11"], [FULL], None),
"VM-D039": ("KEEP", "high", "CLIP addressability break + zero-shot transfer; TS-003 angle is addressability, conditioning reused by reference.", ["VM-O07"], [FULL, "bag-of-words limitation preserved"], None),
"VM-D040": ("KEEP", "high", "ALIGN noisy web-scale scaling point; variant node.", ["VM-O07"], [FULL], None),
# VM-O08 (full grounding chain; never CLIP + Grounding DINO only)
"VM-D041": ("KEEP", "high", "Flickr30k Entities phrase-localization task origin; required D07B node.", ["VM-O08"], [FULL], None),
"VM-D042": ("INSPECT", "medium", "RefCOCO REC contract home; ACL locator content binding needed at Evidence (arXiv ID corrected at intake).", ["VM-O08"], [FULL, "ACL D16-1212 content binding"], None),
"VM-D043": ("KEEP", "high", "OVR-CNN OVD formulation origin; recognition/localization disentanglement.", ["VM-O08"], [FULL], None),
"VM-D044": ("KEEP", "high", "ViLD CLIP-distillation transfer; LVIS-rare protocol entry.", ["VM-O08"], [FULL], None),
"VM-D045": ("KEEP", "high", "RegionCLIP region-pretraining pole (distinct from ViLD distillation); domain-shift diagnosis.", ["VM-O08"], [FULL], None),
"VM-D046": ("KEEP", "high", "Detic vocabulary-scaling pole; ID corrected at intake.", ["VM-O08"], [FULL], None),
"VM-D047": ("KEEP", "high", "GLIP detection-as-grounding reformulation + GoldG practice; required D07B anchor.", ["VM-O08"], [FULL, "GoldG composition at Evidence"], None),
"VM-D048": ("KEEP", "high", "MDETR modulated multi-task detector; early-fusion pole.", ["VM-O08"], [FULL], None),
"VM-D049": ("KEEP", "high", "OWL-ViT minimal-head late-fusion pole; architecture-minimal contrast.", ["VM-O08"], [FULL], None),
"VM-D050": ("KEEP", "high", "Grounding DINO tight-fusion unification; detection + REC framework.", ["VM-O08"], [FULL], None),
"VM-D051": ("KEEP", "high", "OWL-ST/OWLv2 web-scale self-training scaling; X01 exhibit; label-space sensitivity bound.", ["VM-O08"], [FULL, "unseen-claim label-space binding"], None),
"VM-D052": ("KEEP", "high", "LSeg pixel-text alignment origin for OVS branch.", ["VM-O08"], [FULL], None),
"VM-D053": ("KEEP", "high", "X-Decoder generic+referring unification without pseudo-labeling.", ["VM-O08"], [FULL], None),
"VM-D054": ("KEEP", "high", "OpenSeg image-level-label scaling variant; bounded variant status.", ["VM-O08"], [FULL], None),
"VM-D055": ("KEEP", "high", "ODISE diffusion-backbone OVS pole; TS-002 crossover flagged.", ["VM-O08"], [FULL, "TS-002/TS-003 boundary: diffusion backbone crossover"], None),
"VM-D056": ("KEEP", "high", "LVIS rare-split eval home for OVD; shared with O16.", ["VM-O08", "VM-O16"], [FULL], None),
# VM-O09 (bridge strategies must not flatten)
"VM-D057": ("KEEP", "high", "Frozen precursor context; frozen-component design-space origin.", ["VM-O09"], [FULL], None),
"VM-D058": ("KEEP", "high", "Flamingo few-shot gated-cross-attention bridge; required D08 anchor.", ["VM-O09"], [FULL], None),
"VM-D059": ("KEEP", "high", "BLIP-2 frozen-frozen + Q-Former bridge; compute-efficiency exhibit.", ["VM-O09"], [FULL], None),
"VM-D060": ("KEEP", "high", "InstructBLIP instruction-tuning bridge; Sol-map gap fill.", ["VM-O09"], [FULL], None),
"VM-D061": ("KEEP", "high", "MiniGPT-4 open instruction-bridge function; alignment-stage exhibit.", ["VM-O09"], [FULL], None),
"VM-D062": ("KEEP", "high", "LLaVA visual-instruction-tuning anchor; X01 instruction-stage exhibit.", ["VM-O09"], [FULL], None),
"VM-D063": ("KEEP", "high", "Molmo v1 open-data thesis origin; PixMo-Points grounding interface; Molmo 2 predecessor.", ["VM-O09", "VM-O10"], [FULL], None),
# VM-O10 (fusion mechanics + audio-input chain + two-family current coverage)
"VM-D064": ("KEEP", "high", "Qwen2.5-VL M-RoPE/dynamic-resolution predecessor; fusion position-encoding thread.", ["VM-O10"], [FULL], None),
"VM-D065": ("KEEP", "high", "Qwen3-VL open ARCHITECTURE_CASE: DeepStack, interleaved-MRoPE, timestamp alignment, 4-stage recipe; vendor measures quarantined.", ["VM-O10"], [FULL, "vendor-claim quarantine", "config-bound token claims"], None),
"VM-D066": ("KEEP", "high", "Qwen3-Omni open input/fusion ARCHITECTURE_CASE: TM-RoPE absolute-time sync; generation side subordinated to TS-002.", ["VM-O10"], [FULL, "vendor-claim quarantine", "generation-side exclusion"], None),
"VM-D067": ("KEEP", "high", "Whisper speech-input encoder precedent; input-side role only.", ["VM-O10"], [FULL], None),
"VM-D068": ("KEEP", "high", "BEATs general-audio SSL input contract; discrete-label prediction.", ["VM-O10"], [FULL], None),
"VM-D069": ("KEEP", "high", "CLAP audio-side addressability; explicit CLIP-parallel.", ["VM-O10"], [FULL], None),
"VM-D070": ("KEEP", "high", "InternVL3 second-family paradigm contrast (native joint pretraining, V2PE, MPO); anti-Qwen-only anchor.", ["VM-O10"], [FULL, "vendor-claim quarantine", "3.5-series currency check"], None),
"VM-D071": ("KEEP", "high", "Molmo 2 grounding/video comparator (open, Apache 2.0); Qwen dependence disclosed.", ["VM-O10", "VM-O11"], [FULL, "vendor-claim quarantine"], None),
"VM-D072": ("KEEP", "high", "Gemini 3.1 Pro closed CAPABILITY/EVALUATION/DEPLOYMENT case; never architecture authority.", ["VM-O10", "VM-O11"], [FULL, "vendor-claim quarantine", "version+date binding"], None),
"VM-D073": ("KEEP", "high", "Gemini 3.6 Flash efficiency-pole comparator; capability/deployment facts only.", ["VM-O10"], [FULL, "vendor-claim quarantine"], None),
"VM-D074": ("KEEP", "high", "Qwen3-VL repo inspectability exhibit; commit/version binding at Evidence.", ["VM-O10"], [FULL, "repo commit/version binding"], None),
"VM-D075": ("KEEP", "high", "Qwen3-Omni repo streaming-omni deployment exhibit; commit/version binding at Evidence.", ["VM-O10"], [FULL, "repo commit/version binding"], None),
"VM-D076": ("INSPECT", "medium", "InternVL repo + data-release openness exhibit; data-release file-level scope to verify at Evidence.", ["VM-O10"], [FULL, "data-release scope verification"], None),
"VM-D077": ("INSPECT", "medium", "molmo2 full-stack openness exhibit; training-data license mix to bind at Evidence.", ["VM-O10"], [FULL, "data license mix binding"], None),
# VM-O11 (decomposition; no general-intelligence scores)
"VM-D078": ("KEEP", "high", "MMMU comprehensive-reasoning eval home; scaffold ablations required.", ["VM-O11"], [FULL], None),
"VM-D079": ("KEEP", "high", "POPE polling screen; cheap hallucination instrument complementary to control pairs.", ["VM-O11", "VM-O16"], [FULL], None),
"VM-D080": ("KEEP", "high", "HallusionBench control-pair failure attribution; ID corrected at intake.", ["VM-O11", "VM-O16"], [FULL], None),
"VM-D081": ("KEEP", "high", "MMBench bilingual CircularEval anchor; judge-dependence travels with scores.", ["VM-O11"], [FULL], None),
"VM-D082": ("KEEP", "high", "MathVista visual-math node; ID verified at intake; attribution needs ablations.", ["VM-O11"], [FULL], None),
# VM-O12 (temporal state; offline vs streaming never share a column)
"VM-D083": ("KEEP", "high", "Kinetics action-recognition predecessor; frame-repeat baseline.", ["VM-O12"], [FULL], None),
"VM-D084": ("KEEP", "high", "Something-Something ordering-sensitive predecessor.", ["VM-O12"], [FULL], None),
"VM-D085": ("KEEP", "high", "Ego4D egocentric/AV/trajectory data predecessor; shared with VLA data ancestry.", ["VM-O12", "VM-O14"], [FULL], None),
"VM-D086": ("KEEP", "high", "Video-MME duration×modality breadth eval anchor.", ["VM-O12", "VM-O16"], [FULL], None),
"VM-D087": ("KEEP", "high", "LongVideoBench referred-context reasoning eval; distinct from duration breadth.", ["VM-O12", "VM-O16"], [FULL], None),
"VM-D088": ("KEEP", "high", "StreamingBench streaming-eval contract (timestamped + omni-source + proactive).", ["VM-O12", "VM-O16", "VM-O10"], [FULL], None),
"VM-D089": ("KEEP", "high", "Flash-VStream open streaming-system anchor (memory, async queries, latency/VRAM).", ["VM-O12"], [FULL, "deployment figures beyond author-reported are G04"], None),
# VM-O13 (bounded endpoint; state-management thesis)
"VM-D090": ("KEEP", "high", "OSWorld real-OS env + grounding-thesis benchmark; short-horizon contract.", ["VM-O13"], [FULL], None),
"VM-D091": ("KEEP", "high", "OSWorld 2.0 long-horizon state-management thesis + cost curves; strictest binding in volume; v2 status to confirm at Evidence.", ["VM-O13", "VM-O16"], [FULL, "model+thinking+tool+steps+release binding"], None),
"VM-D092": ("KEEP", "high", "SeeClick/ScreenSpot pure element-localization accuracy; icon slice is the hard part.", ["VM-O13", "VM-O16"], [FULL, "successor currency check"], None),
# VM-O14 (minimum VLA chain; representation/action interface only)
"VM-D093": ("KEEP", "high", "SayCan planner-side grounding without joint representation; predecessor contract.", ["VM-O14"], [FULL], None),
"VM-D094": ("KEEP", "high", "RT-1 trajectory/data-regime predecessor.", ["VM-O14"], [FULL], None),
"VM-D095": ("KEEP", "high", "PaLM-E embodied joint-representation break.", ["VM-O14"], [FULL], None),
"VM-D096": ("KEEP", "high", "Open X-Embodiment cross-embodiment data contract; X01 exhibit.", ["VM-O14"], [FULL], None),
"VM-D097": ("KEEP", "high", "RT-2 VLA formulation origin (action tokens + co-fine-tuning).", ["VM-O14"], [FULL], None),
"VM-D098": ("KEEP", "high", "OpenVLA open-weights inspection pole; independent-eval scarcity carried (G01).", ["VM-O14"], [FULL, "G01 independent VLA eval scarcity"], None),
"VM-D099": ("KEEP", "high", "Gemini Robotics 2 closed CAPABILITY/DEPLOYMENT endpoint; planner-policy split noted capability-level only.", ["VM-O14"], [FULL, "vendor-claim quarantine"], None),
"VM-D100": ("KEEP", "high", "On-Device 2 card-scoped EVALUATION + deployment case; stated OOD/high-DoF limits preserved.", ["VM-O14"], [FULL, "card-scope limits preserved"], None),
# VM-O15 (four poles; pixel-only exhibits refused)
"VM-D101": ("KEEP", "high", "Ha & Schmidhuber term origin with explicit non-ancestry to Genie.", ["VM-O15"], [FULL, "non-ancestry statement"], None),
"VM-D102": ("KEEP", "high", "DreamerV3 latent-dynamics counterweight; task-return exhibit.", ["VM-O15"], [FULL], None),
"VM-D103": ("KEEP", "high", "I-JEPA predictive-representation pole origin; video succession via V-JEPA.", ["VM-O15"], [FULL], None),
"VM-D104": ("KEEP", "high", "V-JEPA feature-prediction-only video SSL counterweight; ID corrected at intake.", ["VM-O15"], [FULL], None),
"VM-D105": ("KEEP", "high", "Genie generative-interactive pole origin.", ["VM-O15"], [FULL], None),
"VM-D106": ("KEEP", "high", "Genie 3 closed CAPABILITY + DEPLOYMENT-pointer; 5 vendor limitations recorded; never architecture.", ["VM-O15"], [FULL, "vendor-claim quarantine", "NeRF/3DGS framing attributed not adopted"], None),
"VM-D107": ("KEEP", "high", "Genie 3 model-page deployment-fact companion locator; same role cap.", ["VM-O15"], [FULL, "vendor-claim quarantine"], None),
# VM-O16 (retain-set via shared records; distinct contracts)
"VM-D108": ("KEEP", "high", "DocVQA structure-reading eval; ANLS discipline.", ["VM-O05", "VM-O16"], [FULL], None),
"VM-D109": ("KEEP", "high", "ChartQA visual+logical chart eval; synthetic predecessors are context.", ["VM-O05", "VM-O16"], [FULL], None),
"VM-D110": ("KEEP", "high", "OCRBench v2 localization+reasoning over visual text; private-set discipline; v1 dropped.", ["VM-O05", "VM-O11", "VM-O16"], [FULL], None),
"VM-D111": ("INSPECT", "medium", "VSI-Bench spatial-intelligence eval; exact ID bound at intake; HF dataset + debiased subset binding at Evidence.", ["VM-O12", "VM-O16"], [FULL, "dataset + debiased-subset binding"], None),
}


def main() -> int:
    import datetime
    decisions = []
    for did in sorted(J):
        decision, confidence, reason, scope_tags, verification_targets, duplicate_group = J[did]
        decisions.append({
            "discovery_id": did,
            "decision": decision,
            "reason": reason,
            "scope_tags": scope_tags,
            "verification_targets": verification_targets,
            "duplicate_group": duplicate_group,
            "confidence": confidence,
        })
    assert len(decisions) == 111, f"expected 111 decisions, got {len(decisions)}"
    doc = {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "runner": {
            "provider": "Muse",
            "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
            "invocation": "edition-local make_screening_decisions.py (explicit per-record judgments under Sol Screening-through-Evidence request Sections 3.1-3.3)",
            "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "decisions": decisions,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    from collections import Counter
    print("decisions:", len(decisions), dict(Counter(d["decision"] for d in decisions)))
    print("wrote:", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
