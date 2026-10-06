#!/usr/bin/env python3
"""Apply all spec revisions to fresh compact-input.json -> compact-input-rev1.json.

Every old-string replacement is asserted to match exactly once in its package scope.
New/changed blocks, decks, must_cover maps, boundaries texts, only_claims recorded.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r5-20261006"
sys.path.insert(0, str(EXECDIR))

import revise_p15 as R15
import revise_mid as MID
import revise_rest as REST

FRESH = SRC / "execution/fresh-draft-121-r5-20261006/compact-input.json"
OUT = EXECDIR / "compact-input-rev1.json"


def apply_simple(pkg: dict, fixes: list[tuple[str, str]], label: str) -> int:
    n = 0
    for old, new in fixes:
        hits = [b["block_id"] for b in pkg["blocks"] if old in b["text"]]
        if len(hits) != 1:
            raise ValueError(f"{label} match count !=1 in {pkg['package_id']}: {old[:60]!r} -> {hits}")
        for b in pkg["blocks"]:
            if b["block_id"] == hits[0]:
                b["text"] = b["text"].replace(old, new)
        n += 1
    return n


def main() -> int:
    data = json.loads(FRESH.read_text(encoding="utf-8"))
    pkgs = {p["package_id"]: p for p in data["packages"]}
    counts = {}

    for pid, hl in REST.HEADLINE_FIXES.items():
        pkgs[pid]["headline"] = hl
    for pid, deck in REST.DECK_FIXES.items():
        pkgs[pid]["deck"] = deck
    pkgs["P10"]["deck"] = MID.P10_DECK
    pkgs["P15"]["deck"] = R15.P15_DECK

    counts["rest_text"] = apply_fixes_all(pkgs)
    counts["p10_text"] = apply_simple(pkgs["P10"], MID.P10_FIXES, "P10")
    counts["p11_b9"] = apply_simple(pkgs["P11"], MID.P11_B9_FIXES, "P11B9")
    counts["p11_b8"] = apply_simple(pkgs["P11"], MID.P11_B8_FIXES, "P11B8")
    counts["p12_b3"] = apply_simple(pkgs["P12"], MID.P12_B3_FIXES, "P12B3")
    counts["p12_b7"] = apply_simple(pkgs["P12"], MID.P12_B7_FIXES, "P12B7")
    counts["p09"] = 0
    for fixes, label in [(MID.P09_B4_FIXES, "P09B4"), (MID.P09_B7_FIXES, "P09B7"),
                         (MID.P09_B9_FIXES, "P09B9"), (MID.P09_B11_FIXES, "P09B11"),
                         (MID.P09_B5_FIXES, "P09B5")]:
        counts["p09"] += apply_simple(pkgs["P09"], fixes, label)

    # P10: replace b6, add b7
    p10 = pkgs["P10"]
    nb = []
    for b in p10["blocks"]:
        if b["block_id"] == "p10-b6":
            nb.append(dict(MID.P10_B6_NEW))
        else:
            nb.append(b)
    nb.append(dict(MID.P10_B7_NEW))
    p10["blocks"] = nb
    p10["must_cover_map"] = dict(MID.P10_MUST_COVER)

    # P11: add b10
    p11 = pkgs["P11"]
    assert not any(b["block_id"] == "p11-b10" for b in p11["blocks"])
    p11["blocks"] = list(p11["blocks"]) + [dict(MID.P11_B10_NEW)]
    p11["must_cover_map"] = dict(MID.P11_MUST_COVER)

    # P12: add B8
    p12 = pkgs["P12"]
    assert not any(b["block_id"] == "P12-B8" for b in p12["blocks"])
    p12["blocks"] = list(p12["blocks"]) + [dict(MID.P12_B8_NEW)]
    p12["must_cover_map"] = dict(MID.P12_MUST_COVER)

    # P06: B06 text + ids + only_claims
    p06 = pkgs["P06"]
    for b in p06["blocks"]:
        if b["block_id"] == "P06-B06":
            b["text"] = MID.P06_B06_NEW_TEXT
            b["discovery_ids"] = list(MID.P06_B06_IDS)
            b["only_claims"] = {k: list(v) for k, v in MID.P06_B06_ONLY.items()}
    assert any(b.get("only_claims") for b in p06["blocks"])

    # P09: B10 text
    p09 = pkgs["P09"]
    hit = [b for b in p09["blocks"] if b["block_id"] == "p09-b10"]
    assert len(hit) == 1
    hit[0]["text"] = MID.P09_B10_NEW_TEXT

    # P15: full replacement
    p15 = pkgs["P15"]
    p15["blocks"] = [dict(b) for b in R15.P15_BLOCKS]
    p15["must_cover_map"] = dict(R15.P15_MUST_COVER)

    # boundaries texts for all 16
    for pid, text in REST.BOUNDARIES_TEXT.items():
        pkgs[pid]["boundaries_text"] = text
    assert set(REST.BOUNDARIES_TEXT) == set(pkgs)

    data["draft_version"] = "fresh-121-r5-rev1"
    data["runner"] = {
        "provider": "Muse",
        "model": "Muse Spark (Work execution role; not a Sol/Human decision)",
        "invocation": ("TS-003 Draft content revision r5-rev1 from Architecture r5 APPROVED "
                       "(starting HEAD eafb68eaf6a009be33c003877d2dbc9360f0129b): bounded Draft CONTENT revision, "
                       "no Discovery reopen; P15 rebuilt as cross-package synthesis over 40 mapped authorities "
                       "(edition-local overlay); P10 D111/D112 three-role chain; P12 token/context economics; "
                       "P11 SAM3/D115 supporting role; P06 SigLIP2-Qwen binding via D065 claim-3; "
                       "P09 Molmo2 license/data-term separation; LongVideoBench 6678 fix; reader-facing Japanese cleanup; "
                       "no TeX/PDF; DRAFT_COMPLETE held"),
        "generated_at": "2026-10-06T06:00:00Z",
        "run_reference": None,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False, indent=2))
    print("packages:", sorted(pkgs))
    return 0


def apply_fixes_all(pkgs: dict) -> int:
    total = 0
    per_pkg: dict[str, list] = {}
    for pid, scope, old, new in REST.TEXT_FIXES:
        per_pkg.setdefault(pid, []).append((old, new, scope))
    for pid, fixes in per_pkg.items():
        pkg = pkgs[pid]
        for old, new, scope in fixes:
            hits = [b["block_id"] for b in pkg["blocks"]
                    if old in b["text"] and (scope is None or b["block_id"] == scope)]
            if len(hits) != 1:
                raise ValueError(f"REST fix match !=1 in {pid} scope={scope}: {old[:70]!r} -> {hits}")
            for b in pkg["blocks"]:
                if b["block_id"] == hits[0]:
                    b["text"] = b["text"].replace(old, new)
            total += 1
    return total


if __name__ == "__main__":
    raise SystemExit(main())
