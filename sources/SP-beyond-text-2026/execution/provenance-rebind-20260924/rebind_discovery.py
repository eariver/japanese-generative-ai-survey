#!/usr/bin/env python3
"""TS-002 provenance rebind: repair 24 verified transcription-defect locators.

Source of truth for corrections: source-body-access-ledger.json corrected_body_id
(r2 body-verified) + operator-supplied v2/IEEE/CompVis identities (each re-verified
read-only: arXiv API title match, GitHub API repo identity).

- 21 arXiv IDs -> https://arxiv.org/abs/<corrected_body_id> (locator only).
- BT-D062 -> 2312.05187 + title + published_at 2023-12 (v2 body consumed in r2 repair).
- BT-D089 -> IEEE 7178964 + title (stays PARTIAL; no promotion).
- BT-D024 -> CompVis/stable-diffusion + title (published_at stays 2022-08).

Old locators are preserved in the repair manifest (no silent substitution).
Discovery research is NOT rerun: only locator/title/published_at fields change.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_schema_v2 as schema_gate

ROOT = Path(".").resolve()
DISC = ROOT / "sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl"
OUTDIR = ROOT / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924"
SCHEMA = ROOT / "schemas/survey-discovery-record.schema.json"

ARXIV_FIX = {
    "BT-D004": "2012.09841", "BT-D015": "1812.04948", "BT-D033": "2112.10741",
    "BT-D034": "2211.01324", "BT-D039": "2208.12242", "BT-D042": "2312.03641",
    "BT-D043": "2311.07069", "BT-D044": "2108.01073", "BT-D048": "2210.09276",
    "BT-D049": "2211.09800", "BT-D053": "1712.05884", "BT-D059": "2406.05370",
    "BT-D068": "2407.14358", "BT-D069": "2311.08355", "BT-D073": "2209.14792",
    "BT-D074": "2307.04725", "BT-D081": "2311.17042", "BT-D084": "1606.03498",
    "BT-D095": "2306.12925", "BT-D096": "2402.12226", "BT-D097": "2305.11846",
}

# verified-correct titles (arXiv API, 2026-09-24) for records whose title named the wrong paper
TITLE_FIX = {
    "BT-D095": "AudioPaLM: A Large Language Model That Can Speak and Listen (Rubenstein et al.)",
    "BT-D096": "AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling (Zhan et al.)",
    "BT-D097": "CoDi: Any-to-Any Generation via Compositing Diffusion (Tang et al.)",
}

D062 = {
    "locator": "https://arxiv.org/abs/2312.05187",
    "title": "Seamless: Multilingual Expressive and Streaming Speech Translation (SeamlessM4T v2 family) (Meta)",
    "published_at": "2023-12",
    "basis": "Operator-supplied v2 identity, re-verified read-only via arXiv API title match (2023-12-08) + v2 body consumed FULL in r2 repair (UnitY2/PRETSSEL/EMMA sections). Recorded 2308.11596 is the v1 family paper; v1 facts are NOT carried over.",
    "mismatch": "Recorded locator 2308.11596 resolves to SeamlessM4T v1, not the v2/expressive/streaming source the record title claims.",
    "body": "2312.05187 full-text HTML §§1-9 + App (v2/UnitY2, Expressive/PRETSSEL, Streaming/EMMA, eval tables, limits).",
}
D089 = {
    "locator": "https://ieeexplore.ieee.org/document/7178964",
    "title": "Librispeech: An ASR Corpus Based on Public Domain Audio Books (Panayotov et al., ICASSP 2015)",
    "published_at": "2015-04",
    "basis": "Operator-supplied primary identity (DOI 10.1109/ICASSP.2015.7178964). Recorded arXiv locator 1507.08211 resolves to an unrelated math paper (verified via abs page). Full body not obtained: PARTIAL retained, no promotion.",
    "mismatch": "Recorded locator https://arxiv.org/abs/1507.08211 resolves to an unrelated math paper, not the LibriSpeech corpus paper.",
    "body": "openSLR/ICASSP-citation snippets only (as in r2); ICASSP PDF binary unparseable via webfetch.",
}
D024 = {
    "locator": "https://github.com/CompVis/stable-diffusion",
    "title": "Stable Diffusion public implementation (CompVis/stable-diffusion)",
    "published_at": "2022-08",
    "basis": "GitHub API identity re-verified read-only: full_name CompVis/stable-diffusion, description 'A latent text-to-image diffusion model', created 2022-08-10T14:36:44Z, default branch main (sole branch), no tags. Replaces non-resolving Stability-AI/stablediffusion locator (webfetch 404 + api 404). published_at 2022-08 consistent with creation date.",
    "mismatch": "Recorded locator https://github.com/Stability-AI/stablediffusion returns 404 (page + raw README + api.github.com/repos 404 as of access date).",
    "body": "Repository body still blocked (GitHub 404 via webfetch for the old locator; new-locator body fetch is out of scope for provenance rebind — record stays NEEDS_MORE).",
}


def main() -> None:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    lines = DISC.read_text(encoding="utf-8").splitlines()
    recs = [json.loads(l) for l in lines if l.strip()]
    assert len(recs) == 139, f"expected 139 records, got {len(recs)}"
    by_id = {r["discovery_id"]: r for r in recs}
    manifest_rows = []

    def rebind(did, new_loc, basis, mismatch, body, new_title=None, new_pub=None):
        r = by_id[did]
        old_loc = r["source"]["locator"]
        old_title = r["source"]["title"]
        old_pub = r["source"].get("published_at")
        assert old_loc != new_loc, f"{did}: locator unchanged"
        manifest_rows.append({
            "discovery_id": did,
            "old_locator": old_loc,
            "corrected_locator": new_loc,
            "old_title": old_title,
            "new_title": new_title if new_title is not None else old_title,
            "old_published_at": old_pub,
            "new_published_at": new_pub if new_pub is not None else old_pub,
            "correction_basis": basis,
            "observed_mismatch": mismatch,
            "body_actually_consumed": body,
            "repair_timestamp": now,
        })
        r["source"]["locator"] = new_loc
        if new_title is not None:
            r["source"]["title"] = new_title
        if new_pub is not None:
            r["source"]["published_at"] = new_pub

    for did, correct in ARXIV_FIX.items():
        r = by_id[did]
        old_loc = r["source"]["locator"]
        new_loc = f"https://arxiv.org/abs/{correct}"
        rebind(did, new_loc,
               f"source-body-access-ledger.json corrected_body_id={correct} (r2 body-verified FULL"
               + (", tables truncated" if did == "BT-D059" else "")
               + "), re-verified read-only via arXiv API title match on repair date.",
               f"Recorded locator {old_loc} resolves to an unrelated paper (verified via abs page); "
               f"record title claims the {correct} paper.",
               f"{correct} full-text HTML body consumed in r2 campaign"
               f" ({'partial: §§1-3 + §4.1 only' if did == 'BT-D059' else 'full sections per access ledger'}).",
               new_title=TITLE_FIX.get(did))

    rebind("BT-D062", D062["locator"], D062["basis"], D062["mismatch"], D062["body"],
           new_title=D062["title"], new_pub=D062["published_at"])
    rebind("BT-D089", D089["locator"], D089["basis"], D089["mismatch"], D089["body"],
           new_title=D089["title"], new_pub=D089["published_at"])
    rebind("BT-D024", D024["locator"], D024["basis"], D024["mismatch"], D024["body"],
           new_title=D024["title"], new_pub=D024["published_at"])

    assert len(manifest_rows) == 24, len(manifest_rows)
    for r in recs:
        schema_gate.validate_instance(r, SCHEMA, label=f"Discovery {r['discovery_id']}")
    DISC.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in recs) + "\n", encoding="utf-8")
    manifest = {"schema_version": "1.0", "issue_id": "SP-beyond-text-2026",
                "method": "VERIFIED_PROVENANCE_REBIND (no silent substitution; old locators preserved here)",
                "rows": sorted(manifest_rows, key=lambda x: x["discovery_id"])}
    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "provenance-repair-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rebound": len(manifest_rows),
                      "discovery_lines": len(recs)}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
