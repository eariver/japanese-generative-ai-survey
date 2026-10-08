# Re-entry probes r9-attribution (read-only, zero writes)

- ARCHITECTURE_REVIEW request_changes path: OPEN-NEEDS-HUMAN
  - gate is pending at its state, but a revision decision requires an explicit Human REQUEST_CHANGES + boundary, which the worker must NOT fabricate
- PUBLICATION_PREVIEW request_changes path: FAIL-CLOSED
  - HumanGateError: PUBLICATION_PREVIEW decision requires pending RELEASE_CANDIDATE Human Gate
- operator invalidate_pending_gate: FAIL-CLOSED
  - HumanGateError: Human Gate review index has review after active APPROVED decision: ARCHITECTURE_REVIEW
- forward advance to Draft: CLOSED-FOR-THIS-RUN
  - advance to DRAFT_COMPLETE is mechanically possible but explicitly forbidden by the Human-bounded direction (NO_DRAFT_REGEN).
- shared-Core modification: CLOSED
  - Shared roots are read-only during edition production; no Core change authorized.

Conclusion: the only legitimate path is the run-specific Human-bounded direction (Evidence authority correction + downstream rebind, no gate decisions) via Core-controlled machinery only.
