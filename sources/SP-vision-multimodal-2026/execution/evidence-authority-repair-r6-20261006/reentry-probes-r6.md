# Re-entry probes r6 (read-only, zero writes)

- ARCHITECTURE_REVIEW pending gate: FAIL-CLOSED
  - HumanGateError: ARCHITECTURE_REVIEW decision requires pending ARCHITECTURE_ESTABLISHED Human Gate
- PUBLICATION_PREVIEW pending gate: FAIL-CLOSED
  - HumanGateError: PUBLICATION_PREVIEW decision requires pending RELEASE_CANDIDATE Human Gate
- boundary allowlist readout: INFO
  - ARCHITECTURE_REVIEW allows ['ISSUE_INITIALIZED', 'DISCOVERY_COLLECTED', 'CANDIDATES_NORMALIZED', 'EVIDENCE_REVIEWED', 'SELECTION_COMPLETE']; CANDIDATES_NORMALIZED allowed=True but invocation requires a pending gate (probes 1-2 closed)

Conclusion: no pending Human Gate at DRAFT_COMPLETE can authorize a formal revision; forward advance cannot move backward (record.from_state must equal current lifecycle). Owner Exception consumed per run-specific authorization.
