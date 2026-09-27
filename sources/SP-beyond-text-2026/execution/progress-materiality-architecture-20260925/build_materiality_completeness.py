#!/usr/bin/env python3
"""TS-002 Materiality Ledger + Profile Completeness (canonical derived + honest input).

- Ledger: canonical evidence.build_materiality_ledger (derived from rebound
  acceptances; no hand edits).
- Completeness: canonical _build_completeness logic replicated against the
  ledger (same code path as run_evidence_v2_interactive) with an honest
  obligation assessment: SATISFIED only where every member authority is
  body-consumed; LIMITATION where PARTIAL/BLOCKED members bound the claim.
  No NEEDS_RESEARCH (all 12 obligations have source-backed depth).
- Closure LIMITED: bounded gap-fills completed; barriers/LOW_SIGNAL documented.
"""

from __future__ import annotations

import json
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening
from scripts import survey_discovery_v2 as discovery

ISSUE_ID = "SP-beyond-text-2026"
STATE_REL = "sources/SP-beyond-text-2026/production-state.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/progress-materiality-architecture-20260925"

OBLIGATIONS = [
    ("BT-O01", "LIMITATION",
     "Representation lineage is source-backed across VAE, VQ-VAE/VQGAN, dVAE, SoundStream/EnCodec/DAC, AudioLM hierarchy, and open video VAE, but the spatiotemporal-tokenizer transition is bounded: Phenaki body blocked (OpenReview wall), so masked-prior vs diffusion-prior comparison is unresolved."),
    ("BT-O02", "LIMITATION",
     "Paradigm coverage is source-backed (GAN/StyleGAN, AR pixels/transformer, DDPM/DDIM/score-SDE, latent diffusion, DiT/SiT, flow/rectified-flow, consistency/distillation/mobile), but EDM design-space ablations are abstract-level only (HTML 404) and the open SD implementation tag/commit binding is blocked (repo 404)."),
    ("BT-O03", "SATISFIED",
     "Conditioning/alignment is fully body-consumed: T5-vs-CLIP encoder finding (Imagen), CLIP pretraining, classifier-free guidance with swept scales, GLIDE guidance comparison, eDiff-I expert ensemble, CLAP audio alignment; training-time vs inference-time vs adapter distinctions verified."),
    ("BT-O04", "SATISFIED",
     "Control/reference/identity is fully body-consumed: ControlNet zero-conv transition, T2I-Adapter, IP-Adapter reference decoupling, DreamBooth few-shot identity, LoRA adaptation, SPADE precursor, MotionCtrl camera/object decoupling, Music ControlNet time-varying control."),
    ("BT-O05", "SATISFIED",
     "Editing/preservation is fully body-consumed: partial-diffusion formulation (SDEdit), mask-conditioned resampling (RePaint), latent local editing (Blended LD), attention-map editing, optimisation editing (Imagic), instruction editing (InstructPix2Pix), one-shot video editing (Tune-A-Video); de-novo vs edit separation preserved."),
    ("BT-O06", "LIMITATION",
     "Temporal/long-horizon coverage is source-backed (MAGVIT, Seed-TTS, Seamless v2, Jukebox/MusicLM, VDM/Imagen-Video/Make-A-Video/AnimateDiff/SVD, Wan2.2, GPT-Live, Seedance, Veo), but variable-length discrete video (Phenaki body blocked) leaves the masked-prior long-video comparison unresolved."),
    ("BT-O07", "LIMITATION",
     "Speech lineage is source-backed (WaveNet, Tacotron 1/2, FastSpeech, HiFi-GAN, VITS, YourTTS, VALL-E, Voicebox, Seed-TTS, Seamless v2, F5-TTS, CosyVoice 2, Moshi framework, DuplexBench), but VALL-E 2 result tables are truncated and LibriSpeech corpus facts are snippet-level only."),
    ("BT-O08", "SATISFIED",
     "Music/audio lineage is fully body-consumed: Jukebox, DiffWave, MusicLM with memorisation audit, MusicGen with melody conditioning, AudioLDM with mixup ablations, Stable Audio Open with CC-data audit, MuSTANGO with theory-attribute control, plus human-preference metric validation."),
    ("BT-O09", "LIMITATION",
     "Video lineage is source-backed (VDM, Imagen Video, Make-A-Video, AnimateDiff, SVD, Wan2.2 open anchor, FiVE editing benchmark, Seedance/Veo/FLUX-3/Runway/Luma/Sora lifecycle), but Phenaki body blocked, Movie Gen method sections JS-gated, Kling IR page blocked, Wan hub JS-gated."),
    ("BT-O10", "LIMITATION",
     "Runtime/deployment is source-backed (DDIM subsampling, progressive/LCM/LoRA/adversarial distillation, mobile one-step with phone timings, klein H100 independent measurement, Wan2.2 consumer-GPU envelope), but the open SD implementation binding is blocked and most bodies omit VRAM/quantisation figures."),
    ("BT-O11", "LIMITATION",
     "Evaluation validity is source-backed (GenEval, T2I-CompBench, Pick-a-Pic, FAD, GE2E, VBench/VBench-2.0, Wav2Lip/SyncNet critique, AV-HuBERT metrics, VideoPhy ceiling, DuplexBench, music preference study), but FID full text, MUSHRA Recommendation text, and LibriSpeech protocol are not body-consumed."),
    ("BT-O12", "LIMITATION",
     "Convergence/provenance is source-backed (Unified-IO, AudioPaLM, AnyGPT, CoDi, SynthID page, Sora lifecycle), but the C2PA specification itself is homepage-level only and the Imagen hub redirect limits dedicated-generator evidence to lifecycle role."),
]

RESIDUAL = [
    "BT-D022 EDM design-space ablations: abstract-level only (full-text HTML 404, ar5iv conversion failure).",
    "BT-D024 Stable Diffusion public repository: identity rebound to CompVis/stable-diffusion; exact body/version binding unresolved.",
    "BT-D059 VALL-E 2: grouped-code/repetition-aware mechanism consumed; exact parity tables truncated.",
    "BT-D072 Phenaki: OpenReview login wall; masked-prior long-video comparison unresolved.",
    "BT-D076 Movie Gen: abstract consumed; method/evaluation sections JS-gated.",
    "BT-D083 FID: abstract + cross-description only; sample-size/embedding dependence unverified.",
    "BT-D089 LibriSpeech: IEEE identity rebound; corpus splits/protocol/baselines snippet-level only.",
    "BT-D091 ITU-R BS.1534: Recommendation text gated; protocol details ungathered.",
    "BT-D098 C2PA: homepage only; manifest/assertion/signing construction not consumed.",
    "BT-D106 Imagen: hub redirect; lifecycle-only role.",
    "BT-D120 Kling 3.0 IR page: fetch timeouts; no press substitution.",
    "BT-D125 Wan hub: JS shell; 2.2-last-open corroboration needs rendered fetch.",
    "BT-D134 Moshi: evaluation section not consumed; production figures need independent measurement.",
    "LOW_SIGNAL lanes (duplex interruption measurement, cross-lingual cloning degradation, long-range music structure, metric-vs-preference contradictions, Nano Banana editing corpus, few-step ablations, pure-generation flow-vs-diffusion, consumer klein replication, ElevenLabs independent eval, Wan 2.5+ authority, Sora mechanism) must not be upgraded by narrative confidence.",
]

CLOSURE_LIMITS = [
    "Bounded r2 gap-fill (G03/G04/G08/G09/G10/G11/G12) plus provenance rebind completed targeted retrieval; remaining items above are access barriers, not un-attempted research.",
    "PARTIAL (8) and NEEDS_MORE (5) records retain exact barriers in their cards and views.",
]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    assert state.get("issue_id") == ISSUE_ID and state.get("lifecycle_state") == "CANDIDATES_NORMALIZED", state.get("lifecycle_state")
    assert not agent.validate_agent_state(root, cfg, state)
    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    impl = core.repository_commit_sha(root)
    active = screening.resolve_active_screening_acceptance(root, state_path, impl)
    screening_path = Path(active["artifact_path"])
    accepted = discovery.validate_acceptance(root, source_root / "discovery/discovery-accepted-v2.json")
    discovery_path = core.repo_local_path(root, accepted["discovery_path"], "accepted Discovery JSONL")
    # rebound evidence/views (evidence checkpoint still pending at CANDIDATES_NORMALIZED,
    # so resolve via the rebound build report, not via checkpoint authority)
    reb = json.loads((root / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924/evidence-rebound-build-report.json").read_text(encoding="utf-8"))
    evidence_path, views_path = root / reb["evidence_acceptance"], root / reb["views_acceptance"]
    assert evidence_path.is_file() and views_path.is_file()
    print("rebound evidence:", evidence_path.relative_to(root))
    print("rebound views:", views_path.relative_to(root))

    ledger_path = source_root / "materiality-ledger-v2.json"
    assert not ledger_path.exists(), "ledger exists"
    with agent_tool.current_stage_basis_override():
        ledger = evidence.build_materiality_ledger(
            root, profile_path, discovery_path, screening_path,
            evidence_path, views_path, impl)
    evidence.write_materiality_ledger(ledger_path, ledger)
    from collections import Counter
    print("ledger rows:", len(ledger["rows"]), dict(Counter(r["downstream_disposition"] for r in ledger["rows"])))

    completeness_path = source_root / "profile-completeness-v2.json"
    assert not completeness_path.exists(), "completeness exists"
    discovery_records = [json.loads(l) for l in discovery_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    by_input = {oid: {"status": st, "rationale": ra} for oid, st, ra in OBLIGATIONS}
    assert {r["obligation_id"] for r in profile["research_scope"]["initial_obligations"]} == set(by_input)
    from scripts import run_evidence_v2_interactive as inter
    result = inter._build_completeness(root, profile, profile_path, discovery_records,
                                       ledger_path, ledger,
                                       {"obligations": [{"obligation_id": oid, "status": st, "rationale": ra}
                                                         for oid, st, ra in OBLIGATIONS],
                                        "residual_limitations": RESIDUAL,
                                        "closure": {"targeted_gap_fill_completed": True,
                                                    "limitations": RESIDUAL + CLOSURE_LIMITS, "status": "LIMITED"}})
    schema_gate.validate_instance(result, root / "schemas/profile-completeness-result.schema.json",
                                  label="Profile Completeness")
    with agent_tool.current_stage_basis_override():
        errs = completeness.validate_profile_completeness(
            result, root, profile_path, discovery_path, screening_path,
            evidence_path, views_path, ledger_path, impl)
    assert not errs, errs
    core.write_json(completeness_path, result)
    print("completeness:", result["overall_status"],
          [(o["obligation_id"], o["status"]) for o in result["obligations"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
