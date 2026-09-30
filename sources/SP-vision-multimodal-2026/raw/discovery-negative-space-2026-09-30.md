# Discovery negative-space ledger — SP-vision-multimodal-2026

Issue: `SP-vision-multimodal-2026` | Run: `vision-multimodal-discovery-r1` | Date: `2026-09-30 UTC`

Status: `RAW_LEDGER / PRE_SCREENING`. Low-yield areas are recorded explicitly; none silently omitted.

## OUT_OF_SCOPE (refused by Round E §6; named here so absence is not mistaken for omission)

- O01-NS01: Full handcrafted/pre-deep CV history (SIFT/HOG mechanism, pre-LeNet eras). Context names only.
- O04-NS01: NeRF / 3D Gaussian Splatting / full 3D reconstruction history. Genie 3 vendor framing positions emergent consistency against explicit-3D methods, reducing TS-003 need.
- O04-NS02: Classical SLAM/SfM pipelines, full MVS survey, 3D object detection, SMPL-class human mesh, depth-benchmark zoos.
- O09/O10-NS01: TTS / voice cloning / music / audio generation history (TS-002-owned). Wav2CLIP/AudioCLIP superseded by CLAP for the addressability question.
- O13/O14-NS01: Kinematics, dynamics, gait, actuators, locomotion theory, manipulation-hardware surveys, general robotics safety/policy.
- O05-NS01: Medical / autonomous-driving / remote-sensing vertical surveys (no generic mechanism point established).
- O15-NS02: Full model-based-RL encyclopedia beyond the four-pole contract; photorealism-only exhibits (TS-002).
- O16-NS01: Dropped benchmark anchors: MLVU/LVBench/InfiniBench, TextVQA/ST-VQA, BLINK (image-only), OCRBench v1 (superseded by v2), ODinW standalone, MMEB-V2 standalone.

## CONTEXT_ONLY (named in raw lane notes, no standalone record)

- O07-NS01: DeViSE (Frome et al., NIPS 2013) — joint visual-semantic space predecessor; covered by VQA-era narrative. No separate locator bound (arXiv 1312.5624 is a physics-paper collision; NIPS hash not bound at intake).
- O12-NS01: VStream-QA (inside Flash-VStream) — cited predecessor of StreamingBench.
- O13-NS01: Mind2Web-class web-phase agents (web-phase != OS-phase); candidate arXiv ID 2307.06048 collides with an unrelated paper — no record created rather than a wrong one.
- O13-NS02: Set-of-Mark prompting; vendor computer-use deployments (Gemini 2.5 Computer Use / Claude / Operator-class) as deployment pointers pending exact 2026 authority at Evidence.
- O14-NS01: Gemini Robotics ER-2 planner-policy split (capability-level only).
- O15-NS01: Genie 2 (predecessor context of Genie 3); PILCO/PlaNet minimum context; Waymo World Model deployment pointer pending primary source.
- O08-NS01: OWOD unknown-aware detection (footnote); GoldG composition details deferred to Evidence.

## EVIDENCE_GAP (carried to Sol review; must not be repaired by vendor claims)

- G01: Independent (non-vendor) VLA evaluation scarcity (OpenVLA-community evals to sweep at Evidence).
- G02: Transferable control-oriented world-model benchmark — none found.
- G03: Same-protocol document specialist-vs-generalist head-to-head (GOT/Nougat on identical DocVQA/ChartQA splits) — not found; NO_CROSS_MODEL_NUMERIC_COMPARISON stands.
- G04: Real-deployment latency/VRAM figures beyond author-reported (Flash-VStream, omni streaming).
- G05: Independent reproduction of Qwen3-VL/Omni, InternVL3, Molmo 2 vendor-measured benchmarks.
- G06: SigLIP2 exact citation binding (via Qwen-report references at Evidence).

## LOW_YIELD (none remaining)

- Streaming/online video: RESOLVED by Flash-VStream + StreamingBench (no LOW_YIELD_CONFIRMED).
- Second open VLM: RESOLVED by InternVL3 + Molmo 2 (no NO_SECOND_OPEN_VLM_MEETS_BAR).
