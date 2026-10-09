# TS-003 Vision & Multimodal — Human Architecture Review dossier (r1)

Status: `ARCHITECTURE_DOSSIER / HUMAN_REVIEW_SURFACE / NO_HUMAN_DECISION`

Date: `2026-10-01`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

Lifecycle: `ARCHITECTURE_ESTABLISHED` — selection `passed`, architecture `passed`,
Human Architecture Review `pending`, draft `pending`, Publication Preview `pending`.

This dossier proposes an Architecture. It records no Human decision.

## 1. Review identity

- Edition: TS-003 Vision & Multimodal (THEMATIC / LONGFORM_SPECIAL).
- Revision: Architecture r1 (first Architecture presentation for this issue).
- Canonical artifacts (working tree at dossier time):
  - `candidate-matrix-v2.json` sha256 `1cb6f3a8b86f7e21f510a144baf8c3897f1661dca19739e292ee5cfe91c3a35a`
  - `candidate-selection-v2.json` sha256 `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`
  - `architecture-v2.json` sha256 `7e112f84db8d56d23099a46825eebb50c8289219e11e38e042b58bf1e4df4201`
  - `architecture-review-summary-v2.json` sha256 `8b3cb66684cd254a78d8049f18c2c6b14a10a13d49a52633d0f8704bc62ba060`
  - `architecture-review-attention-v2.json` sha256 `c5a1917788b6da842997b076f46d220c541dba4a1ca4d09a68f7cd0d1d4ca07d`
- Supervisory authority: Sol Materiality/Completeness Review r1
  (`execution/sol-materiality-completeness-review-r1.md`, PASS, authorizes Selection→Architecture).
- Execution authority: `execution/requests/sol-ts003-selection-through-architecture-review-20261001.md`.
- Machine readiness: `READY_FOR_ARCHITECTURE_REVIEW` (deterministic only; not a recommendation).

## 2. Research coverage

- Discovery: 111 records (VM-D001–VM-D111), 111 locators; 16 obligation arcs VM-O01–VM-O16.
- Screening: KEEP 103 / MAYBE 3 / INSPECT 5 / DROP 0
  (acceptance `71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67`).
- Evidence: r5 active only — 106 VERIFIED / 5 PARTIAL
  (accepted `4182d7d5…`, views `e3d0b3b3…`); r1–r4 are history.
- Materiality: 101 MATERIAL / 10 CONTEXT. Completeness: LIMITED
  (13 SATISFIED / 3 LIMITATION: O06-G06, O14-G01, O15-G02 / 0 NEEDS_RESEARCH).
- Residual gaps carried as G01–G06 (see §12).

## 3. Evidence quality (authority-consumption read-back)

- All 111 candidates SELECTED with per-record rationale and explicit
  PRIMARY/SUPPORTING usage, publication role and architecture role.
- PRIMARY records carry mechanism-level treatment; SUPPORTING records are
  context/lineage/eval/deployment nodes with bounded depth.
- Five PARTIAL records are carried honestly with barriers recorded in package
  boundaries (LeNet paywall/abstract-level; DeiT/Swin concurrent-framing;
  Open X-Embodiment/VSI-Bench/Molmo-2 deferred depth).
- Vendor/model-report performance is attributed vendor evidence throughout;
  independent-eval scarcity (G01) is preserved as a limitation, not papered over.
- No cross-task or cross-protocol numeric rankings; G03 binding hold
  (`NO_CROSS_MODEL_NUMERIC_COMPARISON`).

## 4. Candidate map (Selection disposition)

- SELECTED 111/111: 72 PRIMARY, 39 SUPPORTING. HOLD 0, INSPECT 0, excluded 0.
- Nothing was body-blocked: every accepted record has a bounded place, including
  all 10 CONTEXT records as short-treatment background.
- PRIMARY concentrates on: transition anchors (AlexNet, ResNet, Faster R-CNN,
  DETR, DINO-detector, YOLO-World, FCN, Mask R-CNN, SAM/SAM 2, ViT, MAE, DINO,
  DINOv2, SigLIP, CLIP, full D07B chain, Flamingo/BLIP-2/InstructBLIP/LLaVA,
  Qwen3-VL/Omni, InternVL3, Molmo 2, Ego4D, OSWorld 1.0/2.0, SeeClick/ScreenSpot,
  SayCan→OpenVLA chain, Ha/DreamerV3/I-JEPA/V-JEPA/Genie, HallusionBench, OCRBench v2).
- SUPPORTING carries: predecessors (Neocognitron, LeNet, Show-and-Tell, Kinetics,
  Something-Something, Frozen), lineage branches (SSD, RetinaNet, U-Net-role,
  Panoptic-contract, ALIGN, OpenSeg, ODISE, MiniGPT-4, Molmo-v1, Qwen2.5-VL),
  eval breadth (VQA, MMMU, POPE, MMBench, MathVista, Video-MME, LongVideoBench,
  VSI-Bench, DocVQA, ChartQA), deployment exhibits (repos, Gemini closed poles,
  Genie 3, Gemini Robotics 2, On-Device 2).

## 5. Negative space

- No accepted record was excluded; negative space is therefore about depth caps,
  not omissions: OWOD stays a footnote; NeRF/3DGS/SLAM/MVS/3D-detection/SMPL and
  a benchmark zoo are refused under the D04 hard cap; generic Transformer
  efficiency stays TS-001; generation detail stays TS-002; agent-architecture
  generality, kinematics/dynamics/locomotion/safety-policy stay out of P12–P14.
- Alternative rejected: an 80-page symmetric survey compressing each lane to
  equal depth (rejected: endpoint recency would displace perception/grounding
  history; Sol §9 requires depth over symmetry).

## 6. Editorial thesis

TS-003 completes the three-volume arc — TS-001 computes intelligence, TS-002
generates the world, TS-003 perceives, grounds, reasons about, predicts and acts
in it — by reconstructing partially independent technical lineages that converge
late, organized as interacting problem layers (representation, recognition,
localization/structure, language alignment, grounding, fusion, temporal/spatial
state, reasoning, action/prediction) rather than a single model chronology.
Cross-cutting test: what representation of the world is sufficient for the next
computation. Convergence (unified vs modular) stays an open evidence-backed
question answered in Part V, not a predetermined unity narrative.

## 7. Architecture packages (16, drafting order 1–16)

| Pkg | Title | P / S | Thesis |
|-----|-------|-------|--------|
| P01 | Learned visual representation and transfer | 2 / 2 | Scaling + residual-optimization break; recipe reading |
| P02 | Detection and structured localization | 6 / 2 | Proposals → operating points → set prediction → open-vocabulary bridge |
| P03 | Dense perception and promptable vision | 4 / 2 | Boxes → dense structure → promptable foundation; SAM dual reading |
| P04 | Spatial/geometric substrate (support-capped) | 4 / 0 | Four-node hard cap: MiDaS/OpenPose/VisualGenome/DUSt3R |
| P05 | OCR → Document Intelligence | 6 / 3 | Specialist vs generalist interfaces, qualitative only |
| P06 | Transformer + self-supervised foundations | 5 / 2 | Token/architecture/objective/mechanism separation; encoder reuse |
| P07A | Image-level VL alignment | 1 / 3 | CLIP break with preserved bag-of-words limit |
| P07B | Open-vocabulary perception and grounding | 14 / 2 | Full minimum non-redundant chain; metric split from P07A |
| P08 | Pretrained vision-language bridges | 4 / 3 | Projector/Q-Former/cross-attention generations; frozen economics |
| P09 | Native and omni fusion | 7 / 7 | Resolution/fusion-depth/time-sync; input-side audio only |
| P10 | Multimodal reasoning and failure decomposition | 1 / 5 | Control-pair diagnosis; score decomposition |
| P11 | Video, temporal state, streaming | 3 / 6 | Offline long-context vs online streaming contracts separated |
| P12 | Computer Use (bounded endpoint) | 3 / 0 | Grounding bottleneck → state-management thesis |
| P13 | VLA / embodied interfaces (hard-capped) | 6 / 2 | Seven-node chain; card-scoped deployment only |
| P14 | Predictive representations and world models | 5 / 2 | Four-pole terminology contract; non-ancestry guard |
| P15 | Measurement, limits and convergence | 1 / 0 | Methodology-first synthesis; X01 timeline; convergence verdict |

Each package carries `must_cover_requirements`, claim `boundaries` (auto-propagated
per-candidate remaining boundaries), and drafting order. `selected_exceptions: []`.

## 8. Page allocation

Target 104 / max 120. Front matter 4; Parts I–III (P01–P11) 68; Part IV endpoints
(P12–P14) 16 (~15%); Part V evaluation/convergence (P15) 12; back matter 4.
Endpoints capped regardless of recency; no lane compressed to token paragraphs.

## 9. Counterfactual alternatives considered

- (a) Single famous-model ladder `CNN → YOLO → ViT → CLIP → VLM → VLA → World Model`:
  rejected — collapses independent lineages, implies false inevitability (Sol §4).
- (b) Merging P07A/P07B into one alignment package: rejected — destroys the
  metric-contract separation (zero-shot/retrieval vs localization) the evidence
  requires.
- (c) Expanding P04 into a 3D-vision survey: rejected — violates the accepted
  D04 four-node cap and displaces the book's spine.
- (d) Qwen-only current-system narrative: rejected — InternVL3 native-joint
  paradigm contrast and Molmo 2 grounding comparator are structurally required.

## 10. Obligation and cross-cutting coverage

- VM-O01–VM-O16: all 16 arcs have PRIMARY load-bearing authority (see §4/§7).
- X01 (data/supervision): P01, P02 (GLIP/OWL-ST grounding-data practice), P07B,
  P09 (openness gradient), P13 (OXE contract), P15 timeline synthesis.
- X02 (objective/interface): P02–P05, P07A/B, P12–P13 interface contracts.
- X03 (efficiency/token/memory/latency): TS-001 vocabulary reused; P08 (frozen
  economics), P09 (context/memory/latency), P11 (streaming state), P12 (token costs).
- X04 (reliability/claim strength): P10 failure decomposition, G01–G06 limits,
  vendor-vs-independent separation, contamination/judge disciplines.

## 11. G01–G06 carry-forward

G01 independent VLA eval scarcity; G02 world-model control-oriented measures;
G03 cross-model numeric comparison ban; G04 deployment-claim limits;
G05 contamination/judge opacity; G06 SigLIP2 citation residual (bounded).
None marked resolved; all constrain claims in P09–P15 boundaries.

## 12. Known limitations and risks for Human inspection

1. Completeness is LIMITED (O06-G06, O14-G01, O15-G02) — accepted, not hidden.
2. Five PARTIAL records bound mechanism detail at abstract level.
3. Qwen3-VL/Omni vendor measures quarantined; repo commit binding deferred.
4. Closed systems (Gemini 3.x, Genie 3, Gemini Robotics 2) are capability/
   deployment comparators only — never architecture sources.
5. Waymo driving pointer still pending a primary source (flagged, non-blocking).
6. D12–D14 weight (~15%) is a judgment call: enough for the interface transition,
   deliberately not the spine — Human should confirm this balance.
7. P15 carries the convergence verdict as an open question; Human should confirm
   the verdict stays evidence-backed rather than narrative-driven at Draft.

## 13. Sol review finding (Work-recorded; Sol decision authority separate)

Work records deterministic PASS (Selection + Architecture stage validation,
checkpoints `selection`/`architecture`). Substantive Sol Architecture review and
the Human decision remain outside Work authority. No recommendation is recorded
here on behalf of Sol or Human.

## 14. Human decision options

After reviewing this dossier and the bound artifacts, the Human may choose:

- `APPROVED`
- `REQUEST_CHANGES` (with requested changes and one allowed pre-Architecture
  regeneration boundary per governance)

Silence is not a decision. Work has stopped at this Gate: `NO_DRAFT`,
`NO_HUMAN_DECISION`.
