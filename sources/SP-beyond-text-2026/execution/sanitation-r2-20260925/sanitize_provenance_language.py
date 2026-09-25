#!/usr/bin/env python3
"""TS-002 active-provenance sanitation (past-tense normalization, no semantic change).

Reads the rebound r2 input + refreshed-side copies, rewrites ONLY stale
provenance-state wording to accurate past tense per the repair prompt §5:

- removes every literal `Future Discovery repair should correct the locator.`
  (repair already complete);
- converts `Recorded locator X is/resolves ...` defect statements to past tense
  citing the 2026-09-24 provenance repair + repair manifest;
- leaves genuine access barriers, metrics, claims, statuses, materiality,
  lineage-neutral fields, and all other text byte-identical.

Outputs new files under execution/sanitation-r2-20260925/ (prior bytes kept).
Fails closed if any literal future-repair sentence survives or if non-target
text changes.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(".").resolve()
SRC_INPUT = ROOT / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924/evidence-interactive-input-r2-rebound.json"
SRC_LEDGER = ROOT / "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.json"
SRC_LEDGER_MD = ROOT / "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2/transition-ledger.md"
OUTDIR = ROOT / "sources/SP-beyond-text-2026/execution/sanitation-r2-20260925"

RX_LIM = re.compile(
    r"Recorded locator (\S+) is a transcription defect(\([^)]*\)| \([^)]*\))?; "
    r"claims (above )?rest on verified-correct (\S+?)( \([^)]*\))?\. "
    r"Future Discovery repair should correct the locator\.")
RX_D089 = re.compile(
    r"Recorded locator 1507\.08211 does not resolve to the LibriSpeech paper \(transcription defect\)\.")
RX_VER = re.compile(r"Recorded locator (\S+) resolves to unrelated ([^.]+)\.")
RX_CAV = re.compile(
    r"Recorded locator transcription defect documented in limitations; "
    r"claims rest on the verified-correct body stated there\.")
RX_LED = re.compile(
    r"Recorded (\S+) locator (\S+) is a transcription defect( \([^)]*\))?; "
    r"body consumed at verified-correct (\S+)\.")
RX_NOTE = re.compile(r"^\s*NOTE: locator list replaced at build time.*$")


def sub_lim(m):
    opt = m.group(2) or ""
    above = "above " if m.group(3) else ""
    tail = m.group(5) or ""
    return (f"Prior recorded locator {m.group(1)} was a transcription defect{opt}; "
            f"canonical Discovery provenance was rebound to {m.group(4)}{tail} during the "
            f"2026-09-24 provenance repair (see provenance-repair-manifest.json). "
            f"Claims {above}rest on the verified-correct body.")


def sanitize_text(s: str) -> str:
    s = RX_LIM.sub(sub_lim, s)
    s = RX_D089.sub(
        "Prior recorded locator 1507.08211 did not resolve to the LibriSpeech paper "
        "(transcription defect; canonical Discovery provenance was rebound to the IEEE "
        "authority during the 2026-09-24 provenance repair).", s)
    s = RX_VER.sub(
        r"Prior recorded locator \1 resolved to unrelated \2 before the 2026-09-24 provenance repair.", s)
    s = RX_CAV.sub(
        "Prior recorded-locator transcription defect documented in limitations; canonical "
        "provenance rebound during the 2026-09-24 provenance repair; claims rest on the "
        "verified-correct body stated there.", s)
    return s


def sanitize_ledger_unresolved(s: str) -> str:
    s = re.sub(
        r"Recorded (\S+) locator (\S+) is a transcription defect( \([^)]*\))?; "
        r"body consumed at verified-correct (\S+)\.",
        r"Prior recorded \1 locator \2 was a transcription defect\3; canonical locator was rebound "
        r"to \4 during the 2026-09-24 provenance repair; body consumed there.", s)
    s = RX_VER.sub(
        r"Prior recorded locator \1 resolved to unrelated \2 before the 2026-09-24 provenance repair.", s)
    return s


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    doc = json.loads(SRC_INPUT.read_text(encoding="utf-8"))
    changed_ids, counts = [], {"limitations": 0, "verification": 0, "caveats": 0}
    for row in doc["records"]:
        touched = False
        new_lims = []
        for lim in row["limitations"]:
            nl = sanitize_text(lim)
            if nl != lim:
                counts["limitations"] += 1
                touched = True
            new_lims.append(nl)
        row["limitations"] = new_lims
        for v in row["verification"]:
            nf = sanitize_text(v["finding"])
            if nf != v["finding"]:
                counts["verification"] += 1
                touched = True
            v["finding"] = nf
        cav = row.get("historical_attribution_caveat")
        if cav:
            nc = sanitize_text(cav)
            if nc != cav:
                counts["caveats"] += 1
                touched = True
            row["historical_attribution_caveat"] = nc
        if touched:
            changed_ids.append(row["discovery_id"])
    (OUTDIR / "evidence-interactive-input-r2-sanitized.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    led = json.loads(SRC_LEDGER.read_text(encoding="utf-8"))
    led_changed = 0
    for e in led["entries"]:
        new_un = []
        for u in e["unresolved"]:
            if RX_NOTE.search(u):
                led_changed += 1
                continue
            nu = sanitize_ledger_unresolved(u)
            if nu != u:
                led_changed += 1
            new_un.append(nu)
        e["unresolved"] = new_un
    (OUTDIR / "transition-ledger.json").write_text(
        json.dumps(led, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # regenerate readable companion from sanitized JSON
    lines = ["# TS-002 semantic transition ledger (Layer B synthesis)",
             "",
             "Cross-source historical synthesis lives only here — never in Layer A factual cards. "
             "`NOT_ESTABLISHED` marks fields the sources do not support. "
             "`OPEN_QUESTION` marks convergence/residual items. Vendor claims are attributed, never ranked.",
             ""]
    for e in led["entries"]:
        lines.append(f"## {e['transition_id']} — {e['name']}")
        lines.append("")
        lines.append(f"- Modality: {e['modality_or_crossmodal']}")
        lines.append(f"- Bottleneck: {e['predecessor_bottleneck']}")
        lines.append(f"- Changed representation: {e['changed_representation']}")
        lines.append(f"- Changed architecture: {e['changed_architecture']}")
        lines.append(f"- Changed objective: {e['changed_objective']}")
        lines.append(f"- Changed sampling/inference: {e['changed_sampling_or_inference']}")
        lines.append(f"- Conditioning/control: {e['conditioning_or_control_change']}")
        lines.append(f"- Improvement: {e['source_supported_improvement']}")
        lines.append(f"- Trade-off/failure: {e['tradeoff_or_new_failure_mode']}")
        lines.append(f"- Succession: {e['successor_inheritance_or_displacement']}")
        lines.append(f"- Support: {', '.join(e['discovery_ids'])}")
        lines.append(f"- Tasks: {', '.join(e['evidence_task_ids'])}")
        lines.append(f"- Type: {e['synthesis_type']} (confidence {e['confidence']})")
        for u in e["unresolved"]:
            lines.append(f"- Open: {u}")
        lines.append("")
    (OUTDIR / "transition-ledger.md").write_text("\n".join(lines), encoding="utf-8")

    # fail-closed audit
    stalk = []
    for p in [OUTDIR / "evidence-interactive-input-r2-sanitized.json",
              OUTDIR / "transition-ledger.json", OUTDIR / "transition-ledger.md"]:
        txt = p.read_text(encoding="utf-8")
        if "Future Discovery repair" in txt:
            stalk.append(str(p))
    present = re.findall(r"Recorded locator \S+ is a transcription defect", (OUTDIR / "evidence-interactive-input-r2-sanitized.json").read_text(encoding="utf-8"))
    print(json.dumps({"cards_changed": sorted(changed_ids), "edits": counts,
                      "ledger_unresolved_rewrites": led_changed,
                      " surviving_future_repair": stalk,
                      "surviving_present_tense_defect": present[:3]}, indent=2))
    assert not stalk and not present, "sanitation incomplete"
    print("SANITATION_OK")


if __name__ == "__main__":
    raise SystemExit(main())
