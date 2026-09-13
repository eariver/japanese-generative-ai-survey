# W34 Sol Screening handoff — agent-first wrapper retry r1

Status: **NEEDS_SOL_REVIEW**

The required agent-first State preflight passed:

- State: `DISCOVERY_COLLECTED / stage:screening`
- `survey_agent_control_v2.validate_agent_state()`: `PASS`
- helper implementation SHA: `7375afc11dc7a8cf3d9e1ba6f6a135252a42bbf2`

The canonical `scripts/survey_agent_tool_v2.py` wrapper then failed before package creation while reading the existing immutable event-level input:

```text
'utf-8' codec can't decode byte 0xaa in position 1: invalid start byte
```

The committed input bytes are SHA-256 `a15ddbde1bc3b35ab158d68a50313294091aa33f2d942d2e24d3d578f5344321`, whereas the prior expansion diagnostic records expected SHA-256 `5dbdcbfd70dc1e4605560dc06fc89e940141116b0bf9bf8eefaef6f8bf9f2332`. The input was not modified or rebuilt in this retry.

The crosswalk still records `W34-C001`–`W34-C105` exactly once, all 105 parent bindings resolve to the accepted 40-record graph, and all 36 Raw paths exist. DailyX/Grok/carry-over traceability is preserved. No Screening decisions, results, acceptance, or lifecycle advancement were created. Production State and the accepted Discovery graph remain byte-identical.

Please review the committed event-input integrity anomaly before authorizing another package attempt. The retry cannot certify a prepared package or claim `READY_FOR_SOL_SCREENING` until the immutable input is validly readable.
