#!/usr/bin/env python3
"""Execution-only adapter for the fresh W33 Core v2 Evidence run.

Two mechanical adaptations are required by the one-shot runner:
- remove its empty ``work/results`` child immediately before the canonical
  append-only package builder checks that the output root is empty;
- run the final Completeness revalidation under the reviewed agent-first
  historical-Screening-basis wrapper merged to main in PR #337.

No Evidence Card, materiality, or editorial decision is changed here.
"""
from __future__ import annotations

import runpy
from pathlib import Path

from scripts import survey_evidence_v2 as ev
from scripts.survey_agent_tool_v2 import current_stage_basis_override

_original_prepare = ev.prepare_evidence_package
_original_completeness = ev.validate_completeness


def _prepare(*args, **kwargs):
    if len(args) >= 5:
        output_dir = Path(args[4])
    else:
        output_dir = Path(kwargs["output_dir"])
    results = output_dir / "results"
    if results.is_dir() and not any(results.iterdir()):
        results.rmdir()
    return _original_prepare(*args, **kwargs)


def _validate_completeness(*args, **kwargs):
    with current_stage_basis_override():
        return _original_completeness(*args, **kwargs)


ev.prepare_evidence_package = _prepare
ev.validate_completeness = _validate_completeness
runpy.run_path("automation/w33_evidence_once.py", run_name="__main__")
