#!/usr/bin/env python3
"""TS-001 edition-local Overfull hbox guard (NOT shared Core).

Policy (edition-local, r2 acceptance):
  >= 20pt : BLOCK
  10pt <= x < 20pt : REVIEW_REQUIRED (needs explicit rendered visual disposition)
  < 10pt : nonblocking but recorded

r2 acceptance requires MAX_OVERFULL_HBOX < 20pt and every 10-20pt occurrence,
if any, must have an explicit rendered visual disposition.

Usage:
  python3 overfull_hbox_guard.py --log surveys/special/efficient-llm-2026/main.log \
      --out sources/SP-efficient-llm-2026/execution/validation/overfull-guard-r2.json

Exit codes:
  0 : PASS (max < 20pt)
  2 : BLOCK (max >= 20pt)
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

OVERFULL_RE = re.compile(
    r"Overfull\s+\\hbox\s+\((?P<pt>[0-9]+(?:\.[0-9]+)?)pt too wide\)"
    r"(?:\s+in paragraph at lines\s+(?P<lines>[0-9]+--[0-9]+))?"
    r"(?:\s+in alignment at lines\s+(?P<align>[0-9]+--[0-9]+))?"
)


def parse_log(log_path: Path) -> list[dict]:
    text = log_path.read_text(encoding="utf-8", errors="replace")
    findings = []
    for m in OVERFULL_RE.finditer(text):
        pt = float(m.group("pt"))
        # Grab surrounding log context (2 lines before/after) for auditability.
        start = max(0, text.rfind("\n", 0, m.start() - 200))
        snippet = text[start : m.end() + 400].strip().splitlines()[:8]
        findings.append(
            {
                "pt": pt,
                "lines": m.group("lines") or m.group("align") or "",
                "raw": m.group(0),
                "context": snippet,
            }
        )
    return findings


def classify(pt: float) -> str:
    if pt >= 20.0:
        return "BLOCK"
    if pt >= 10.0:
        return "REVIEW_REQUIRED"
    return "RECORD"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    log_path = Path(args.log)
    out_path = Path(args.out)
    findings = parse_log(log_path)
    for f in findings:
        f["disposition"] = classify(f["pt"])
    max_pt = max((f["pt"] for f in findings), default=0.0)
    blocking = [f for f in findings if f["disposition"] == "BLOCK"]
    review = [f for f in findings if f["disposition"] == "REVIEW_REQUIRED"]
    record_only = [f for f in findings if f["disposition"] == "RECORD"]
    payload = {
        "schema": "ts001-edition-local-overfull-guard-v1",
        "issue_id": "SP-efficient-llm-2026",
        "log_path": str(log_path),
        "policy": {
            "block_pt": 20.0,
            "review_required_min_pt": 10.0,
            "note": "Edition-local r2 policy. Generic future threshold is deferred Core maintenance (CV2-DM).",
        },
        "max_overfull_pt": max_pt,
        "counts": {
            "total": len(findings),
            "block": len(blocking),
            "review_required": len(review),
            "record": len(record_only),
        },
        "blocking_findings": blocking,
        "review_required_findings": review,
        "record_findings": record_only,
        "all_findings_sorted_desc": sorted(findings, key=lambda r: r["pt"], reverse=True),
        "acceptance": {
            "max_lt_20pt": max_pt < 20.0,
            "review_required_needs_visual_disposition": len(review) > 0,
        },
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"max_overfull_pt": max_pt, "counts": payload["counts"], "out": str(out_path)}, ensure_ascii=False, indent=2))
    return 2 if max_pt >= 20.0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
