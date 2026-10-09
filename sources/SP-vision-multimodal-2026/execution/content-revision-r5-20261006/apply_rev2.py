#!/usr/bin/env python3
"""Apply rev2 fixes to compact-input-rev1.json -> compact-input-rev2.json (exact-once)."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r5-20261006"
sys.path.insert(0, str(EXECDIR))
import revise_rev2 as R2


def main() -> int:
    data = json.loads((EXECDIR / "compact-input-rev1.json").read_text(encoding="utf-8"))
    pkgs = {p["package_id"]: p for p in data["packages"]}
    n = 0
    for pid, bid, old, new in R2.FIXES:
        pkg = pkgs[pid]
        targets = [b for b in pkg["blocks"] if (bid is None or b["block_id"] == bid) and old in b["text"]]
        if len(targets) != 1:
            raise ValueError(f"rev2 match !=1 in {pid}/{bid}: {old[:70]!r} -> {[b['block_id'] for b in targets]}")
        targets[0]["text"] = targets[0]["text"].replace(old, new)
        n += 1
    pkgs["P11"]["deck"] = R2.P11_DECK_NEW
    data["draft_version"] = "fresh-121-r5-rev2"
    data["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 final Draft content polish r5-rev2 from Architecture r5 APPROVED "
                       "(starting HEAD 18be8aff5c0d61916d50be3ada165e12bb93a02a): bounded reader-facing repair; "
                       "P15-B02 branching supervision regimes; P09 Molmo2 license/intended-use/data-term separation; "
                       "P07A geo-localization; P07B Flickr unseen-phrase accuracy; P02 DETR matching-cost terms; "
                       "reader language pass (リアルタイム etc.); prose-rhythm variation; P11 chapter-focus note; "
                       "V-JEPA Policy content-based deferral recorded; no upstream reopen; no TeX/PDF; "
                       "DRAFT_COMPLETE held"),
        "generated_at": "2026-10-06T08:00:00Z",
        "run_reference": None,
    }
    (EXECDIR / "compact-input-rev2.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rev2_fixes_applied": n}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
