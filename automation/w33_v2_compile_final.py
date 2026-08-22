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

# Weekly completeness is LIMITED whenever residual limitations are retained.  The
# Grok cutoff-day ambiguity is intentionally retained rather than fabricated away.
replace_once(
    "'overall_status': 'READY',",
    "'overall_status': 'LIMITED',",
    "Weekly completeness overall_status",
)
replace_once(
    "'The imported Grok r3 raw is a discovery/community sensor only; three representative high-salience false positives are preserved as explicit DROP decisions.',",
    "'The imported Grok r3 raw is a discovery/community sensor only; two representative high-salience false positives are preserved as explicit DROP decisions.',\n                'Grok 4.6 has first-party GitHub rollout evidence, but the Aug 14 changelog page does not establish an exact publication time relative to the 18:00 EDT cutoff; it remains HOLD/INSPECT rather than being silently placed inside or outside W33.',",
    "Weekly completeness residual limitations",
)

'''
source = source.replace(anchor, fixes + anchor, 1)
exec(compile(source, "automation/w33_v2_compile_final.py::<corrected-current-wrapper>", "exec"), {"__name__": "__main__", "__file__": str(INNER)})
