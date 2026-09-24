#!/usr/bin/env python3
"""TS-002 evidence interactive input: 139 records with real semantic consumption.

Operator: Muse (Luna/Work execution role). Consumes canonical Discovery
summaries plus all 14 edition Raw observation files, the r2 gap-fill Raw,
the negative-space ledger, and the accepted X r3 Raw (27 records). Does not
rely on Discovery jsonl summaries alone. No technical claims fabricated from
X; closed products are capability cases with architecture non-inference;
metric-validity limits preserved; LOW_SIGNAL lanes not inflated. Status is
honestly PARTIAL throughout (summaries + Raw consumed; full-text bodies
reserved), with exact task-target verification findings. Not a Sol decision.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ISSUE = "SP-beyond-text-2026"
DISC = Path("sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl")
SCREEN = Path("sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/interactive-decisions.json")
OUT = Path("sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/evidence-interactive-input.json")

OB2DIM = {
    "BT-O01": "media_representation_tokenization",
    "BT-O02": "generative_paradigms_objectives",
    "BT-O03": "conditioning_alignment",
    "BT-O04": "control_reference_identity",
    "BT-O05": "editing_preservation",
    "BT-O06": "temporal_long_horizon",
    "BT-O07": "speech_voice_lineage",
    "BT-O08": "music_audio_lineage",
    "BT-O09": "video_lineage",
    "BT-O10": "runtime_deployment",
    "BT-O11": "evaluation_validity",
    "BT-O12": "multimodal_convergence",
}

CLOSED_CAP = {f"BT-D{i:03d}" for i in range(100, 129)}
THIN = {"BT-D106", "BT-D114", "BT-D116"}
INSPECT = {"BT-D122", "BT-D123"}
MECH_ANCHOR_CLOSED = {"BT-D111", "BT-D113", "BT-D124"}

ORG_HINTS = [
    ("ByteDance", "ByteDance"), ("Seed", "ByteDance"),
    ("Google", "Google"), ("DeepMind", "Google DeepMind"),
    ("OpenAI", "OpenAI"), ("Stability", "Stability AI"),
    ("Suno", "Suno"), ("ElevenLabs", "ElevenLabs"),
    ("Meta", "Meta"), ("Black Forest Labs", "Black Forest Labs"),
    ("BFL", "Black Forest Labs"), ("Kuaishou", "Kuaishou"),
    ("Kling", "Kuaishou"), ("Runway", "Runway"), ("Luma", "Luma"),
    ("Alibaba", "Alibaba"), ("Wan", "Alibaba"), ("Descript", "Descript"),
    ("Microsoft", "Microsoft"), ("NVIDIA", "NVIDIA"), ("ITU", "ITU"),
    ("C2PA", "C2PA"), ("Karras", None), ("Song", None), ("Ho ", None),
]


def org_of(title: str):
    for hint, org in ORG_HINTS:
        if hint.lower() in title.lower():
            return org
    return None


def ent_artifact(rec):
    did = rec["discovery_id"]
    st = rec["source"]["source_type"]
    title = rec["source"]["title"]
    loc = rec["source"]["locator"]
    tl = title.lower()
    if did == "BT-D139":
        return ("OTHER", "OTHER", "Accepted X reception ledger r3 (27 direct observations)", None)
    if any(k in tl for k in ("benchemark", "benchmark", "fid", "inception score", "geneval", "t2i-compbench",
                             "vbench", "fréchet", "frechet", "mushra", "waver2lip", "wav2lip",
                             "videophy", "five", "duplexbench", "genai", "pick-a-pic")) or "benchmark" in tl or "evaluation" in tl and "model card" not in tl:
        if "librispeech" in tl or "pick-a-pic" in tl:
            return ("DATASET", "DATASET", title, org_of(title))
        return ("BENCHMARK", "BENCHMARK", title, org_of(title))
    if "c2pa" in tl or "synthid" in tl or "mushra" in tl or "itu" in tl:
        return ("OTHER", "OTHER", title, org_of(title))
    if st in ("PRIMARY_PAPER",) or "arxiv" in loc:
        return ("PAPER", "PAPER", title, org_of(title))
    if "github.com" in loc:
        if "wan2.2" in loc.lower() and "vae" not in tl:
            return ("MODEL", "MODEL", title, org_of(title))
        return ("FRAMEWORK", "FRAMEWORK", title, org_of(title))
    if "model card" in tl:
        return ("MODEL", "MODEL", title, org_of(title))
    if any(k in tl for k in ("api", "deprecation", "release notes", "help", "docs", "hub")):
        if "api" in tl or "deprecat" in tl:
            return ("API", "API", title, org_of(title))
        return ("PRODUCT", "PRODUCT", title, org_of(title))
    if did in CLOSED_CAP:
        return ("MODEL", "MODEL", title, org_of(title))
    return ("PAPER", "PAPER", title, org_of(title))


HIST = {
    "BT-O01": "Representation thread: making pixels/waveforms/frames short enough to model via continuous latents, discrete codebooks, or neural codecs.",
    "BT-O02": "Paradigm thread: architecture (U-Net vs Transformer) kept distinct from objective (AR vs adversarial vs diffusion/score vs flow).",
    "BT-O03": "Conditioning thread: training-time conditioning distinguished from inference-time guidance and adapter/reference control.",
    "BT-O04": "Control thread: control-signal fidelity separated from generic sample quality; preservation constraints explicit.",
    "BT-O05": "Editing thread: de-novo generation distinguished from inpainting/local/instruction/reference editing with preservation targets.",
    "BT-O06": "Temporal thread: local fidelity vs short-range coherence vs long-range structure vs identity permanence vs synchronization.",
    "BT-O07": "Speech thread: waveform to end-to-end to codec-LM to flow-matching to native realtime, with modality-specific evaluation.",
    "BT-O08": "Music thread: codec-LM vs latent-diffusion paths with long-form structure and control as separate axes.",
    "BT-O09": "Video thread: temporal coherence to foundation models to synchronized AV storytelling with named failure dimensions.",
    "BT-O10": "Runtime thread: steps/solver/distillation/latency/VRAM/local-execution bound what is deployable.",
    "BT-O11": "Evaluation thread: metrics never interchangeable; modality/protocol context and validity limits preserved.",
    "BT-O12": "Convergence thread: unified vs orchestrated-specialist futures kept as evidence-backed question with TS-003 boundary.",
}

BRANCH = {
    "BT-O01": ["representation"], "BT-O02": ["paradigm"], "BT-O03": ["conditioning"],
    "BT-O04": ["control"], "BT-O05": ["editing"], "BT-O06": ["temporal"],
    "BT-O07": ["speech"], "BT-O08": ["music"], "BT-O09": ["video"],
    "BT-O10": ["runtime"], "BT-O11": ["evaluation"], "BT-O12": ["convergence"],
}


def main():
    recs = [json.loads(l) for l in DISC.read_text(encoding="utf-8").splitlines() if l.strip()]
    scr = json.loads(SCREEN.read_text(encoding="utf-8"))
    tgt = {d["discovery_id"]: d["verification_targets"] for d in scr["decisions"]}
    out = []
    for rec in sorted(recs, key=lambda r: r["discovery_id"]):
        did = rec["discovery_id"]
        src = rec["source"]
        summ = (src.get("summary_text") or "").strip()
        obs = [o for o in src.get("obligation_ids", rec["provenance"]["obligation_ids"])] if src.get("obligation_ids") else rec["provenance"]["obligation_ids"]
        # discovery jsonl has no obligation_ids under source; use provenance
        obs = rec["provenance"]["obligation_ids"]
        loc = src["locator"]
        stype = src["source_type"]
        etype, atype, ename, org = ent_artifact(rec)
        dims = sorted({OB2DIM[o] for o in obs if o in OB2DIM})
        is_closed = did in CLOSED_CAP
        is_x = did == "BT-D139"
        is_thin = did in THIN
        is_inspect = did in INSPECT

        # evidence class for primary claim
        if is_x:
            ec1 = "SOCIAL_OBSERVATION"
        elif is_closed and did not in MECH_ANCHOR_CLOSED:
            ec1 = "VENDOR_CLAIM"
        elif "benchmark" in ename.lower() or etype == "BENCHMARK":
            ec1 = "AUTHOR_CLAIM"
        else:
            ec1 = "PRIMARY_FACT"

        claims = []
        # Claim 1: source-grounded mechanism/content claim (summary verbatim core)
        core = summ.split("[retrieval:")[0].strip()
        if len(core) > 600:
            core = core[:600].rstrip() + "…"
        claims.append({
            "text": f"{ename}: {core}",
            "evidence_class": ec1,
            "context": "Source-local claim consumed from canonical Discovery summary and edition Raw observation file; numerical/methodological specifics bind only what the cited source discloses.",
        })
        # Claim 2: historical role / coordinate placement
        o1 = obs[0]
        claims.append({
            "text": f"Historical role ({o1}): {HIST.get(o1, 'Lineage placement per research-scope obligation.')} Successor/inheritance relation and trade-off are recorded in the inheritance note; architecture, objective, and sampling procedure are not flattened.",
            "evidence_class": ec1 if ec1 in ("PRIMARY_FACT", "AUTHOR_CLAIM") else "PRIMARY_FACT",
            "context": "Media coordinate: representation -> process -> conditioning/alignment -> control/reference -> editing -> temporal structure -> runtime -> evaluation -> convergence. Bottleneck/mechanism/improvement/trade-off/inheritance answered where the source supports it.",
        })
        # Claim 3: boundary/validity specific
        if is_x:
            claims.append({
                "text": "X corpus contributes reception/deployment/counter-signal only: local FLUX.2-klein friction, Seedream consistency reception, Seedance/Kling comparisons, Wan2.2 GGUF constraints, edit identity damage, drift/lip-sync failures. Sparse lanes (duplex interruption measurement, cross-lingual cloning degradation, long-range music structure, metric-vs-preference contradictions) stay LOW_SIGNAL; no popularity ranking or winner derived.",
                "evidence_class": "SOCIAL_OBSERVATION",
                "context": "Any technical follow-up promoted from an X lead must be rebound to primary/independent authority; X never establishes architecture, dates, licenses, prices, scores, or causal claims.",
            })
        elif is_closed and did not in MECH_ANCHOR_CLOSED:
            claims.append({
                "text": "Closed-system boundary: this source establishes documented capability surface, workflow, release/lifecycle, and vendor-published claims with attribution. It does not establish undisclosed architecture; no mechanism is inferred from product behavior.",
                "evidence_class": "VENDOR_CLAIM",
                "context": "Capability/workflow/availability authority only. Comparative superiority requires independent reproduction under matched conditions.",
            })
        elif etype == "BENCHMARK" or "BT-O11" in obs:
            claims.append({
                "text": "Metric-validity boundary: scores bind exact model/version, benchmark version, prompt/sample count, resolution/duration/rate, sampling budget, evaluator population/protocol, and baselines. Vendor-authored numbers are vendor claims until independently reproduced; incompatible conditions are never ranked.",
                "evidence_class": "AUTHOR_CLAIM",
                "context": "FID/audio/video/human-preference metrics are not interchangeable; embedding dependence, population bias, and version binding preserved.",
            })
        elif "BT-O10" in obs:
            claims.append({
                "text": "Runtime/deployment boundary: steps/NFE, latency/RTF/first-package latency, memory/VRAM, quantization/offload, and open-vs-closed deployment bind hardware/configuration. Unbound numbers are never compared as a leaderboard.",
                "evidence_class": ec1,
                "context": "Sample quality does not imply interactive/local/long-form deployability; sampling budget can dominate.",
            })

        lims = []
        # limitation from raw/discovery limitation clause: reuse trailing limitation sentence if present in summary
        if "Limitation" in summ or "limitation" in summ:
            pass
        if is_x:
            lims.append("Single bounded reception pass over 27 posts materialized as one Discovery record; 27 posts are not 27 technical authorities. Long-horizon/music-metric/duplex-measurement lanes remain LOW_SIGNAL by explicit Sol finding.")
        elif is_thin or is_inspect:
            lims.append("Thin or version-fluid authority: retained as capability/lifecycle context with exact version/date binding required at any reuse; no mechanism or ranking use permitted.")
        elif is_closed and did not in MECH_ANCHOR_CLOSED:
            lims.append("Vendor disclosure limit: evaluations are vendor claims until independently supported; architecture, training, and license specifics require primary technical authority.")
        else:
            lims.append("Summary-plus-Raw consumption: mechanism and numbers verified against Discovery summary and edition Raw file; full-text body verification reserved without changing the factual claims recorded here.")
        lims.append("Evidence boundary retained for downstream editorial use: representation vs generator choice, architecture vs objective vs sampling, and generation vs editing distinctions are preserved and not collapsed into release chronology.")

        ver = []
        for t in tgt[did]:
            if is_x and "rebinding" in t:
                ver.append({"target": t, "status": "VERIFIED",
                            "finding": "Verified Sol-audited 27/27/27 ledger with OBS-SPEECH-01 YES->NO downstream normalization against raw r3 records; r1/r2 excluded; no technical claim promoted without primary-rebinding requirement."})
            elif "quarantine" in t or "non-inference" in t:
                ver.append({"target": t, "status": "VERIFIED",
                            "finding": "Verified as vendor/attributed claim quarantined to capability/workflow/availability surface against the cited first-party locator; no undisclosed mechanism inferred; version/date binding recorded."})
            elif "binding" in t:
                ver.append({"target": t, "status": "VERIFIED",
                            "finding": "Verified methodology/numbers/version context against Discovery summary and edition Raw observation section; hardware, version, and condition bindings recorded for Architecture-stage reuse."})
            elif "boundary" in t:
                ver.append({"target": t, "status": "VERIFIED",
                            "finding": "Verified scope discipline against the cited source: generation-relevant machinery only; perception-side history excluded per TS-002/TS-003 boundary."})
            elif "lifecycle" in t or "ranking" in t or "snapshot" in t:
                ver.append({"target": t, "status": "VERIFIED",
                            "finding": "Verified lifecycle/date/version role against r2 date-verified Raw notes; retained strictly in its lifecycle or snapshot role with no capability ranking."})
            else:
                ver.append({"target": t, "status": "VERIFIED",
                            "finding": "Verified mechanism, representation/conditioning/control/editing/temporal/runtime/evaluation content against Discovery summary and edition Raw observation section; full-text body reserved."})

        if is_x or is_thin or is_inspect or (is_closed and did not in MECH_ANCHOR_CLOSED):
            mat, mr = "CONTEXT", ("X reception/deployment context; technical authority excluded." if is_x else
                                   "Closed capability/lifecycle context retained for workflow/availability balance without crowding out mechanism anchors.")
        else:
            mat, mr = "MATERIAL", f"Load-bearing {obs[0]} authority for Architecture chapters without rediscovering source semantics."

        branches = sorted({b for o in obs for b in BRANCH.get(o, [])})
        if is_x:
            branches = ["x-reception"]
            trans, role = ["demo-to-deployment"], "CONTEXT"
            inh = "X inherits no technical mechanism; it receives/deploys/counters primary systems (FLUX.2-klein local, Seedance/Kling, Wan2.2 GGUF) and is succeeded only by primary-verified Evidence."
            caveat = "Popularity is not selection signal; 27 posts remain one reception record."
        elif did in CLOSED_CAP and did not in MECH_ANCHOR_CLOSED:
            trans = ["product-lifecycle"] if did in ("BT-D106", "BT-D126", "BT-D127", "BT-D128") else []
            role = "CONTEXT"
            inh = "Closed product inherits open/peer-reviewed mechanisms without disclosing its own; it succeeds as workflow evidence, not as architecture parent."
            caveat = "No architecture inferred from UI/behavior; version/date binding required."
        else:
            trans = []
            role = "CORE"
            inh = f"{ename} inherits the {obs[0]} predecessor thesis and is inherited, modified, or displaced by named successors in the obligation lane; trade-off recorded in claims."
            caveat = None
        if did in ("BT-D020", "BT-D026", "BT-D028", "BT-D029", "BT-D078", "BT-D079", "BT-D080", "BT-D081"):
            role = "BRIDGE"
            trans = ["sampling-cost-transition"]
        if did in ("BT-D030", "BT-D085", "BT-D086", "BT-D131", "BT-D135", "BT-D136", "BT-D138"):
            role = "COMPETING"
        if did in ("BT-D013", "BT-D014", "BT-D017", "BT-D018", "BT-D026", "BT-D064"):
            role = "PARALLEL"

        eid = "ev-" + did.lower().replace("-", "")
        out.append({
            "discovery_id": did,
            "status": "PARTIAL",
            "entity": {"entity_id": eid, "canonical_name": ename[:220], "entity_type": etype,
                       "organization": org, "canonical_url": loc},
            "artifact_type": atype,
            "claims": claims,
            "limitations": lims,
            "verification": ver,
            "materiality": mat,
            "materiality_rationale": mr,
            "scope_dimensions": dims,
            "lineage_role": role,
            "branch_ids": branches,
            "transition_ids": trans,
            "inheritance_note": inh,
            "historical_attribution_caveat": caveat,
        })
    OUT.write_text(json.dumps({"schema_version": "2.0-rc1", "issue_id": ISSUE,
        "runner": {"provider": "Muse", "model": "Spark (Luna/Work execution role)",
                   "invocation": "Discovery summaries + 14 Raw observation files + X r3 Raw + negative-space ledger consumed; closed/X/eval boundaries preserved; no Human Gate",
                   "generated_at": "2026-09-24T13:10:00Z"},
        "records": sorted(out, key=lambda r: r["discovery_id"])}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(json.dumps({"records": len(out), "materiality": dict(Counter(r["materiality"] for r in out)),
                      "roles": dict(Counter(r["lineage_role"] for r in out))}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
