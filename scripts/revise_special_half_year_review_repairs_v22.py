#!/usr/bin/env python3
"""Add bounded FlashAttention-3 Hopper kernel signals."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from scripts import revise_special_half_year_review_repairs_v21 as base
from scripts import revise_special_half_year_review_repairs_v16 as event_layer
impl = event_layer.impl
_EXTRA_SIGNAL_PATTERNS_V22 = (
    ("Hopper TMA / WGMMA活用", r"\bHopper\b.{0,500}\b(?:TMA|WGMMA)\b|\b(?:TMA|WGMMA)\b.{0,500}\bHopper\b"),
    ("warp-specializationでcomputeとdata movementをoverlap", r"warp[- ]specialization.{0,220}overlap.{0,220}(?:computation|compute).{0,120}data movement|overlap.{0,220}(?:computation|compute).{0,120}data movement.{0,220}warp[- ]specialization"),
    ("block-wise matmulとsoftmaxをinterleave", r"interleave block[- ]wise matmul and softmax operations"),
    ("FP8向けincoherent processing", r"incoherent processing.{0,220}\bFP8\b|\bFP8\b.{0,220}incoherent processing"),
)
def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = impl._SIGNAL_PATTERNS
    impl._SIGNAL_PATTERNS = _EXTRA_SIGNAL_PATTERNS_V22 + previous
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict): result["flashattention3_signal_contract"] = "HOPPER_KERNEL_SCOPE_V1"
        return result
    finally:
        impl._SIGNAL_PATTERNS = previous

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--repo-root",default="."); p.add_argument("--special-slug",required=True); p.add_argument("--issue-id",required=True); p.add_argument("--source-version",required=True); a=p.parse_args()
    print(json.dumps(build(Path(a.repo_root).resolve(),a.special_slug,a.issue_id,a.source_version),ensure_ascii=False,indent=2)); return 0
if __name__ == "__main__": raise SystemExit(main())
