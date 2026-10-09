# Re-entry probes r9 (read-only, zero writes)

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

Conclusion: no formal supported mechanism can make the correction without the run-specific Human-bounded revision direction (§0). Consume that direction via Core-controlled machinery only (rewind + bounded replay, no gate decisions).
