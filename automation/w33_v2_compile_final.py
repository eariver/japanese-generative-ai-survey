#!/usr/bin/env python3
"""Final fail-closed execution layer for the W33 session compiler.

This keeps the earlier session history intact while applying validator-discovered
corrections before the transformed compiler is executed.
"""
from pathlib import Path

INNER = Path("automation/w33_v2_compile_current.py")
source = INNER.read_text(encoding="utf-8")
anchor = "# Execute transformed source as the canonical session compiler input."
if source.count(anchor) != 1:
    raise RuntimeError("current W33 compiler wrapper execution anchor drift")

fixes = r'''
# Weekly Edition View uses the Core v2 enum CARRY_OVER; cutoff-day uncertainty is OTHER.
replace_once(
    "'window_relation': 'CARRY_OVER_DISPOSITION' if did == 'w33-carryover-ledger' else 'MAIN_EVENT',",
    "'window_relation': 'CARRY_OVER' if did == 'w33-carryover-ledger' else ('OTHER' if did == 'w33-grok46-copilot' else 'MAIN_EVENT'),",
    "Weekly window_relation enum",
)

'''
source = source.replace(anchor, fixes + anchor, 1)
exec(compile(source, "automation/w33_v2_compile_final.py::<corrected-current-wrapper>", "exec"), {"__name__": "__main__", "__file__": str(INNER)})
