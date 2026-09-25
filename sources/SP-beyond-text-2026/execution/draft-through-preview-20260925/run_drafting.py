#!/usr/bin/env python3
"""TS-002 drafting-synthesis under Core-canonical stage-basis override.

Accepted immutable Screening/Evidence packages retain the State SHA from the
boundary where they were created; Production State has legitimately advanced
(ARCHITECTURE_ESTABLISHED + Human approval). Core provides
survey_agent_tool_v2.current_stage_basis_override for exactly this: all other
package basis checks rerun, only historical State-SHA drift is admitted for
content-addressed acceptances. Same precedent as
progress-materiality-architecture-20260925/build_materiality_completeness.py.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path


def main() -> int:
    root = Path(".").resolve()
    sys.path.insert(0, str(root))
    from scripts import survey_agent_tool_v2 as agent_tool

    sys.argv = [
        "run_drafting_synthesis_v2_interactive.py",
        "--state",
        "sources/SP-beyond-text-2026/production-state.json",
        "--input",
        "sources/SP-beyond-text-2026/execution/draft-through-preview-20260925/interactive-drafting-input.json",
    ]
    with agent_tool.current_stage_basis_override():
        try:
            runpy.run_path(
                str(root / "scripts/run_drafting_synthesis_v2_interactive.py"),
                run_name="__main__",
            )
        except SystemExit as exc:
            code = exc.code
            if code is None:
                return 0
            if isinstance(code, int):
                return code
            raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
