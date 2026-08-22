#!/usr/bin/env python3
"""Execution-only adapter: preserve Core v2 package append-only semantics.

The W33 runner creates an empty work/results directory before calling the
canonical Evidence package builder. The builder correctly requires an empty
output root. Remove only that empty child immediately before the canonical
builder runs; all substantive validation remains in survey_evidence_v2.
"""
from __future__ import annotations

import runpy
from pathlib import Path

from scripts import survey_evidence_v2 as ev

_original = ev.prepare_evidence_package


def _prepare(*args, **kwargs):
    if len(args) >= 5:
        output_dir = Path(args[4])
    else:
        output_dir = Path(kwargs["output_dir"])
    results = output_dir / "results"
    if results.is_dir() and not any(results.iterdir()):
        results.rmdir()
    return _original(*args, **kwargs)


ev.prepare_evidence_package = _prepare
runpy.run_path("automation/w33_evidence_once.py", run_name="__main__")
