#!/usr/bin/env python3
"""Build rebound r2 input: prior r2 records + new canonical URLs + v2 D062 card.

Only BT-D062 semantic payload changes (v2 body). All other 138 records keep
r2 meaning; canonical_url follows the rebound Discovery locator.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(".").resolve()
PDIR = ROOT / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924"
PRIOR = PDIR / "prior-authority/evidence-interactive-input-r2.json"
DISC = ROOT / "sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl"

D062_V2 = {
    "status": "VERIFIED",
    "entity": {"entity_id": "evr2-btd062",
               "canonical_name": "Seamless: Multilingual Expressive and Streaming Speech Translation (SeamlessM4T v2 family) (Meta)",
               "entity_type": "PAPER", "organization": "Meta",
               "canonical_url": "https://arxiv.org/abs/2312.05187"},
    "artifact_type": "PAPER",
    "claims": [
        {"text": "The source defines UnitY2: non-autoregressive FastSpeech2-style decoder with hierarchical subword-to-character-to-unit upsampling, unsupervised multilingual character-to-unit aligner as duration teacher, and span-based glancing; 3x speech-to-speech speed-up, decoupling length for partial-input streaming.",
         "evidence_class": "PRIMARY_FACT",
         "context": "v2 body §§3-4; v1 UnitY facts are NOT carried over."},
        {"text": "The source defines expressive transfer: Prosody-UnitY2 (phrase-level rate/pauses) plus PRETSSEL (utterance-level voice/style) with an expressivity encoder on source mel plus a textless acoustic model reconstructing 80-dim mel from reduced XLS-R-10k units as target-units-plus-source-mel prompt into HiFi-GAN.",
         "evidence_class": "PRIMARY_FACT", "context": "v2 body §4."},
        {"text": "The source defines SeamlessStreaming: v2 fine-tuned with Efficient Monotonic Multihead Attention per-head stepwise policy with numerically-stable parallel alpha, latency-plus-variance regularization, emission threshold plus non-autoregressive text-to-unit chunking; evaluated by average lagging/length-adaptive lagging/ending offset.",
         "evidence_class": "PRIMARY_FACT", "context": "v2 body §5."},
        {"text": "Reported numbers (v2-Large 2.3B, Fleurs): speech-to-text BLEU X-to-English 26.6 vs v1 24.1 (+10%) vs cascade 22.7 (+17%); speech-to-speech ASR-BLEU X-to-English 29.7 vs 25.8 (+15%), English-to-X 26.1 vs 20.9 (+25%); expressive mDRAL gains over v2 base; streaming threshold-0.5 speech-to-text X-to-English BLEU 20.0/lag 1.68 vs offline 23.7, speech-to-speech ASR-BLEU 22.1/offset 2.79 s vs 29.7.",
         "evidence_class": "PRIMARY_FACT", "context": "v2 body §§6-7 tables/conditions."},
    ],
    "limitations": [
        "Performance varies by race/accent/gender with ASR gaps propagating to expressive/streaming; distant/low-resource/zero-shot worse; short-form general-domain research-only, long-form degrades, not certified.",
        "Expressive sensitivity preserves noise lowering clarity/sound quality; residual added toxicity/bias plus voice-phishing/deepfake misuse only partly damped by watermark.",
        "Long-form/domain-specific/certified efficacy, full elimination of gender/toxicity/noise-propagation gaps, and visual/sign-gesture integration not established.",
    ],
    "verification": [{"target": "Evidence-stage full-body verification", "status": "VERIFIED",
                      "finding": "v2 source body consumed (abs + HTML §§1-9 + App: v2/UnitY2, Expressive/PRETSSEL, Streaming/EMMA, eval tables, limits). No v1 fact carried over as v2 fact."}],
    "materiality": "MATERIAL",
    "materiality_rationale": "Source-bound factual authority; reuse bound to stated conditions.",
}


def main() -> None:
    doc = json.loads(PRIOR.read_text(encoding="utf-8"))
    recs = {}
    for line in DISC.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            recs[r["discovery_id"]] = r
    assert len(recs) == 139
    out = []
    changed = []
    for row in doc["records"]:
        did = row["discovery_id"]
        new = dict(row)
        new_loc = recs[did]["source"]["locator"]
        if new["entity"].get("canonical_url") != new_loc:
            new["entity"] = dict(new["entity"], canonical_url=new_loc)
            changed.append(did)
        if did == "BT-D062":
            keep = {"discovery_id", "scope_dimensions", "lineage_role", "branch_ids",
                    "transition_ids", "inheritance_note"}
            new.update({k: row[k] for k in keep})
            new.update(D062_V2)
            new["historical_attribution_caveat"] = (
                "Recorded locator 2308.11596 is the v1 family paper; claims above rest on the "
                "verified-correct v2 body 2312.05187 consumed in the rebind repair.")
        out.append(new)
    assert len(out) == 139 and len({r["discovery_id"] for r in out}) == 139
    from scripts import survey_production_v2 as core
    from scripts import run_evidence_v2_interactive as inter
    profile = core.load_json(ROOT / "sources/SP-beyond-text-2026/production-profile.json")
    for r in out:
        inter._validate_record(r, profile)
    (PDIR / "evidence-interactive-input-r2-rebound.json").write_text(json.dumps({
        "schema_version": "2.0-rc1", "issue_id": "SP-beyond-text-2026",
        "runner": doc["runner"], "records": sorted(out, key=lambda r: r["discovery_id"])},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(json.dumps({"records": len(out), "url_updated": len(changed),
                      "status": dict(Counter(r["status"] for r in out))}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
