# TS-003 r1 → r2 Evidence semantic-fidelity repair report

Issue: `SP-vision-multimodal-2026` | Date: `2026-09-30 UTC` | Lifecycle: `CANDIDATES_NORMALIZED` (unchanged)

Authority: Sol Evidence Semantic Review r1 (F1–F5) + repair request §§4–11.
r1 input: `execution/screening-evidence-20260930/evidence-interactive-input.json`
r2 input: `execution/evidence-semantic-repair-r1-20260930/evidence-interactive-input-r2.json`
r1 acceptance: `evidence/v2/accepted/3b183719...` (immutable history, untouched)
r2 acceptance: `evidence/v2/accepted/3f6be211...` (new append-only result set)
r2 views: `evidence/v2/views/accepted/73c06689...`

Changed records: **61 of 111** (50 byte-identical). Status changes: **none**
(VERIFIED 106 / PARTIAL 5 preserved — no VERIFIED-count optimization).
PRIMARY_FACT claims: r1 had 46 synthesis-mislabeled instances → r2 has **0**.

## Defect classes repaired

### SOURCE_BINDING (F1) — repo facts removed from paper-bound cards
- VM-D065: deleted repo deployment-surface claim (FP8/vLLM/Visual Agent/1M context); those facts live only in repo-bound VM-D074. Paper claims 1–2 kept (report-supported upgrades/pillars).
- VM-D066: removed unbound "Apache 2.0" term; kept report-supported Thinker-Talker/TM-RoPE/audio/latency/benchmark claims.
- VM-D070: moved 3.5-line currency note to repo-bound VM-D076; paper card carries no currency claim.
- VM-D071: paper card no longer cites README-derived facts; findings rewritten to report-body sections.
- VM-D075: corrected false Apache-2.0 implication → weights license is `license:other` per HF release tag (sha 26291f79, 2025-09-22); code license unbound.
- VM-D074: added exact license bindings (code Apache 2.0 via repo LICENSE; weights Apache 2.0 via HF tag sha 0c351dd0, 2025-10-15).
- VM-D076: received the 3.5-currency note (repo-bound, correct home); stays PARTIAL.
- Verification findings in all four paper cards rewritten to name consumed body sections; no finding cites a repository as evidence.

### LICENSE_SCOPE (F2) — Molmo buckets separated with fresh bindings
- Paper's own tripartite labeling adopted: "Open weights, Open data (no distillation), Open code" (report tables) — no undifferentiated Apache claim.
- Paper's self-disclosed closed dependencies added (closed-data SigLIP 2 encoder even in Olmo variant; closed text-only LLMs for data generation; MathVista/MMMU + 10min+ data gaps) — strengthens honesty, all paper-supported.
- Repo card VM-D077 buckets: code Apache 2.0 (repo LICENSE verified); weights Apache 2.0 (HF tag license:apache-2.0, sha e28fa285, 2026-01-23); 9 released datasets available (HF tags) BUT per-dataset terms unbound → PARTIAL preserved, no contradiction with paper card.

### CONSUMPTION_DEPTH (F3) — findings name body content
- 19 paper-card verification findings rewritten to state complete-body consumption with char counts and named sections/mechanisms (e.g., DETR loss equations + ablations; SayCan formulation; OpenVLA 970K scale; OSWorld 2.0 phenomena taxonomy).
- PARTIAL records (D001/D002/D076/D077/D111) keep explicit barriers; aggregate accounting matches per-card semantics.

### EVIDENCE_CLASS (F4) — synthesis PRIMARY_FACT → INFERENCE
- 46 claims reclassified across 45 records (list in §11-check output: zero PRIMARY_FACT remain).
- All carry the synthesis context: edition-level analytical judgment, not a literal source statement.
- Genuine source facts untouched (mechanism/results claims stay AUTHOR/VENDOR/PROJECT).

### LINEAGE_WORDING (F5) — D101 made source-safe
- "Terminological origin" removed; "Dreamer, not Genie" exclusivity removed.
- Replacement: major historical anchor + branch-separated lineage (Dreamer latent-dynamics, JEPA predictive-representation, Genie interactive-generative) with no-direction ancestry assertions; Ha→Genie non-ancestry preserved.
- Limitations updated; no history-of-the-term expansion performed.

## Per-record detail (substance-changed IDs; class-only F4 changes summarized above)
### VM-D065
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Deployment surface (repo-verified): Dense+MoE edge-to-cloud, FP8 variants, Transformers/vLLM support; Visual Agent GUI operation; 2D + 3D grounding; context expandable 1M per repo.

### VM-D066
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Thinker-Talker MoE unifying perception+generation across text/image/audio/video; from-scratch audio encoder; TM-RoPE absolute-time 80ms audio-video alignment; 40-min ASR/SLU instances; 119 text / 19 understand / 10 generate languages; 234ms theoretical first-packet streaming; 36 audio/AV benches: open-SOTA 32, overall 22 (beats Gemini-2.5-Pro/Seed-ASR/GPT-4o-Transcribe, author-measured); Apache 2.
- ADDED claim: Thinker-Talker MoE unifying perception+generation across text/image/audio/video; from-scratch audio encoder; TM-RoPE absolute-time 80ms audio-video alignment; 40-min ASR/SLU instances; 19-language speech understanding / 10-language generation; 234ms theoretical first-packet streaming; 36 audio/AV benches with open-SOTA 32 and overall 22 (author-measured, report-stated comparators).
- RECLASSIFIED [PRIMARY_FACT -> INFERENCE]: Boundary enforced: Talker/Code2Wav synthesis detail is TS-002-side; TS-003 carries input encoder + TM-RoPE sync + streaming-input contract only.

### VM-D070
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Currency note (provenance, not substitution): InternVL README shows InternVL3.5 line (report 2508.18265, 241B-A28B-class, training code open-sourced 2025-08-30); Discovery corpus unchanged — recorded here so later stages bind versions explicitly.
- RECLASSIFIED [PRIMARY_FACT -> INFERENCE]: Paradigm contrast vs Qwen staged bridge/extend recipe: native-joint vs staged — the anti-Qwen-only structural exhibit (not popularity).

### VM-D071
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Open weights+data (Apache 2.0), no closed-VLM synthetic data; 7 new video + 2 multi-image datasets (dense video captions, free-form video QA, complex-query tracking, video pointing); packing + message-tree recipe, bidirectional vision-token attention, token-weighting; 8B leads open class on short video/counting/captioning, competitive long-video; video-counting 35.5 vs Qwen3-VL 29.6, pointing F1 3
- ADDED claim: Open release posture in the paper's own tripartite labeling — 'Open weights, Open data (no distillation), Open code' (paper tables): 8B leads open class on short video/counting/captioning, competitive long-video; video-counting 35.5 vs Qwen3-VL 29.6, pointing F1 38.4 vs Gemini 3 Pro 20.0, tracking J&F 56.2 vs 41.1 (author-measured); 9 released datasets (2 pointing/tracking, captions, QA); fully-open Olmo variant; v4 Apr 2026.
- ADDED claim: Paper's self-disclosed closed dependencies: closed-data SigLIP 2 image encoder even in the Olmo variant (no competitive open-data encoder available, paper's call to community) and closed text-only LLMs for data generation; behind on MathVista/MMMU reasoning and 10min+ long-video training data per the paper's own results discussion.
- RECLASSIFIED [PRIMARY_FACT -> INFERENCE]: Comparator role (not paradigm pole): 8B/4B reuse Qwen3 backbones — partial Qwen dependence disclosed; value is openness gradient + grounding-measured video evals.

### VM-D074
- Status: VERIFIED -> VERIFIED
- ADDED claim: License bindings (freshly bound 2026-09-30): code — Apache 2.0 (repo-root LICENSE verified); weights — Apache 2.0 (HF Qwen/Qwen3-VL-8B-Instruct release tag license:apache-2.0, sha 0c351dd0, modified 2025-10-15).
- RECLASSIFIED [PRIMARY_FACT -> INFERENCE]: Inspectability exhibit: three-module stack inspectable in code; weights do not self-establish eval claims.

### VM-D075
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Apache 2.0 omni weights; thinker-only (talker-disabled) mode documented; streaming omni deployment surface with cookbooks/demos; HF trending top-1 2025-09-26 (project-stated).
- ADDED claim: Streaming omni deployment surface with cookbooks/demos; thinker-only (talker-disabled) mode documented; HF trending top-1 2025-09-26 (project-stated). Weights license is license:other per HF Qwen/Qwen3-Omni-30B-A3B-Instruct release tag (sha 26291f79, 2025-09-22) — NOT Apache 2.0; code license unbound.

### VM-D076
- Status: PARTIAL -> PARTIAL
- ADDED claim: Currency note (provenance, not substitution): repo README documents the InternVL3.5 line (report 2508.18265, 241B-A28B-class, training code open-sourced 2025-08-30); Discovery corpus unchanged.

### VM-D077
- Status: PARTIAL -> PARTIAL
- REMOVED claim: Full-stack openness: data prep, pre-training/SFT/long-context-SFT, eval tooling, vLLM inference, checkpoint-to-HF conversion; MolmoPoint pointing-extension documented; HF collections linked.
- ADDED claim: Full-stack openness scope verified at repo depth: data prep, pre-training/SFT/long-context-SFT, eval tooling, vLLM inference, checkpoint-to-HF conversion, MolmoPoint extension, HF collections linked.
- ADDED claim: License buckets (freshly bound 2026-09-30, separated): code — Apache 2.0 (repo-root LICENSE verified); model weights — Apache 2.0 (HF allenai/Molmo2-8B release tag license:apache-2.0, sha e28fa285, 2026-01-23); released data — 9 allenai/Molmo2-* datasets available (HF tags verified) BUT per-dataset license/usage terms unbound; third-party mixture constraints unresolved.

### VM-D101
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Non-ancestry statement: terminological origin, NOT Genie's technical ancestor (§G.5 carried); required verbatim-class in later prose.
- ADDED claim: Edition lineage design: this 2018 paper is a major historical neural-world-model anchor for this edition (dream-training formulation); Dreamer continues the latent-dynamics/model-based-decision branch, JEPA/V-JEPA the predictive-representation branch, Genie the interactive-generative branch; no direct ancestry asserted in any direction, and no Ha-to-Genie technical ancestry implied.
- LIMITATIONS r1: ['Historical term source only; technical continuation runs through Dreamer, not Genie.']
- LIMITATIONS r2: ['Historical term-source scope only; branch-separated lineage (above) replaces any exclusive continuation reading.', 'No broad history-of-the-term investigation performed (out of repair scope per Sol r1).']

### VM-D042
- Status: VERIFIED -> VERIFIED
- REMOVED claim: Locator correction at Evidence: arXiv 1606.03825 is an unrelated physics paper; canonical locator is ACL Anthology D16-1212 (EMNLP 2016).

## Why the repairs are source-faithful

- Removed facts were never deleted from the corpus: every repo/deployment/license fact retains a home in the correctly bound repo card (VM-D074/075/076/077).
- Added license facts come from freshly consumed primary surfaces (repo-root LICENSE files, HF release API with SHAs/dates), not memory.
- Reclassified synthesis was not weakened: the same analytical content now carries the honest epistemic label plus its structural home (lineage_role/branch/transition/inheritance fields unchanged).
- No claim was strengthened beyond its source; two claims were narrowed (Omni license, Molmo data license) where authority did not support the r1 breadth.
- G01–G06 untouched; D001/D002 access barriers untouched; 50 records byte-identical.

## F4 class-only change list (45 records, PRIMARY_FACT → INFERENCE with synthesis context)

VM-D001, D002, D005, D011, D013, D014, D015, D017, D018, D020, D021, D022, D026, D027, D029, D030, D034, D035, D038, D045, D048, D049, D050, D055, D062, D067, D072, D074, D085, D088, D089, D092, D093, D094, D098, D099, D102, D106, D108 (single-claim conversions) + VM-D065/066/070/071 (within substance rewrites above).
