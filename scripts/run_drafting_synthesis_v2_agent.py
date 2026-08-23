#!/usr/bin/env python3
"""Run the interactive Core v2 Drafting/Synthesis surface with canonical historical-basis validation.

Drafting revalidates accepted Screening and Evidence packages created at earlier lifecycle
boundaries. Those immutable packages intentionally retain the Production State SHA from
their creation stage. The agent-first stage validator already uses
``current_stage_basis_override`` for exactly this reason; this wrapper gives the
interactive Drafting generator the same reviewed validation semantics without weakening
any package-content hash checks.
"""
from __future__ import annotations

import runpy
from pathlib import Path

from scripts import survey_agent_tool_v2 as runtime_tool


def main() -> int:
    target = Path(__file__).with_name("run_drafting_synthesis_v2_interactive.py")
    with runtime_tool.current_stage_basis_override():
        runpy.run_path(str(target), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
