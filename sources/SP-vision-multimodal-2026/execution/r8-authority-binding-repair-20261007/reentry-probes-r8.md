# Re-entry probes r8 (read-only, zero writes)

- ARCHITECTURE_REVIEW request_changes path: FAIL-CLOSED
  - HumanGateError: ARCHITECTURE_REVIEW decision requires pending ARCHITECTURE_ESTABLISHED Human Gate (formal revision needs an explicit Human REQUEST_CHANGES decision + boundary, which the worker must NOT fabricate)
- PUBLICATION_PREVIEW request_changes path: FAIL-CLOSED
  - HumanGateError: PUBLICATION_PREVIEW decision requires pending RELEASE_CANDIDATE Human Gate
- operator invalidate_pending_gate: FAIL-CLOSED
  - HumanGateError: Human Gate review index has review after active APPROVED decision: ARCHITECTURE_REVIEW
- forward advance direction: CLOSED
  - advance requires record.from_state == current lifecycle; DRAFT_COMPLETE can only advance to reader-publication-validation, never rewind.
- shared-Core modification: CLOSED
  - Shared roots are read-only during edition production; no Core change authorized.

Conclusion: no formal supported mechanism can make the correction without fabricating a Human decision, hand-editing lifecycle/checkpoints, or modifying shared Core. Consume the run-specific Owner Exception (§0) via Core-controlled machinery only.
