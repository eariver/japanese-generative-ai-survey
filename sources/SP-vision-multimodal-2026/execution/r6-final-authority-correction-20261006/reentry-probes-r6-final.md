# Re-entry probes r6-final (read-only, zero writes)

- ARCHITECTURE_REVIEW pending-gate predicate: PASS-PENDING
  - Gate is pending at ARCHITECTURE_ESTABLISHED; a formal request_changes invocation would still require an explicit Human REQUEST_CHANGES decision + boundary, which this run must NOT fabricate. Formal revision via Human decision path is therefore CLOSED to the worker.
- operator invalidate_pending_gate (ARCHITECTURE_REVIEW): FAIL-CLOSED
  - HumanGateError: Human Gate review index has review after active APPROVED decision: ARCHITECTURE_REVIEW
- boundary allowlist readout: INFO
  - ARCHITECTURE_REVIEW revision allows ['ISSUE_INITIALIZED', 'DISCOVERY_COLLECTED', 'CANDIDATES_NORMALIZED', 'EVIDENCE_REVIEWED', 'SELECTION_COMPLETE']; operator invalidation allows ['ISSUE_INITIALIZED', 'DISCOVERY_COLLECTED', 'CANDIDATES_NORMALIZED', 'EVIDENCE_REVIEWED', 'SELECTION_COMPLETE']; CANDIDATES_NORMALIZED allowed=True in both, but probes 1-2 close formal invocation.
- shared-Core modification: CLOSED
  - Shared roots (AGENTS.md/config/schemas/scripts/.github/docs core) are read-only; no Core change is authorized in this run.

Conclusion: no formal supported mechanism can make the correction without fabricating a Human decision (request_changes) or violating the operator-invalidation no-records precondition (r1-r5 history exists). Forward advance cannot move backward. Consume the run-specific Owner Exception (this task message §0-§2) via Core-controlled machinery only; manual state/checkpoint edits prohibited.
