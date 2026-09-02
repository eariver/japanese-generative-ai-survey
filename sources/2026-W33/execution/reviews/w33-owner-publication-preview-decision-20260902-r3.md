# W33 Owner Publication Preview Decision — r3

- Issue: `2026-W33`
- Gate: `PUBLICATION_PREVIEW`
- Revision: `3`
- Branch: `weekly/2026-W33-v2-work`
- Exact reviewed publication content HEAD: `70c999a87192d2b3674c3f044aa6f50c4c5f95a9`
- Sol verification / pre-decision HEAD: `3b622e6c861f5e098a693de1e42514e7a1a261a0`
- Decision: `APPROVED`
- Remaining findings: `0`
- Reviewed by: `Owner`
- Reviewed at: `2026-09-02 08:17 JST` (`2026-09-01T23:17:00Z`)
- Controlling issue: `#433`

## Owner decision

The Owner explicitly approves Publication Preview r3.

The exact reviewed publication surface is the replacement W33 Publication Candidate produced after the r2 single-boundary correction and independently verified by Sol in:

`sources/2026-W33/execution/reviews/w33-publication-preview-r3-gate-sol-review-20260902-r1.md`

The r2 VoiceDesigner bibliography finding is resolved. No remaining Publication Preview blocker is retained from Issue #433.

## Exact approved publication identity

- Publication Candidate: `sources/2026-W33/publication/v2/publication-candidate-v2.json`
- Candidate payload SHA-256: `f3e0ae94ae51e7b5f5374d68c66ecaf688f0d7d43c5db85bc656925a6d07333e`
- Reader Manuscript SHA-256: `ce5df090e5255cad819508a9397ac894bbbc24de9b2fb0d0be075ab4e9918e13`
- Reader source SHA-256: `44ef2580c072c7295d052311fca2a9a3a5bf165c7eab19a1375b1f729e8e55a0`
- Publication PDF: `surveys/weekly/2026-W33/main.pdf`
- PDF SHA-256: `1885762325c33b575dd6e789dc53f7ed1c30483a9928b6dbf9537ad0e05661f5`
- PDF byte count: `274472`
- PDF page count: `11`

## Accepted review surface

The Owner approval accepts the current 11-page Publication Preview, including:

- the reader-facing article structure and prose;
- the independent Week in Review;
- the source/claim-boundary presentation;
- the reader-facing References;
- the repaired VoiceDesigner source note: `Paper metadata; baseline and evaluation details could not be confirmed from the available primary material.`;
- the current rendered layout and page flow;
- the absence of the previously rejected internal production vocabulary from the reader-facing PDF.

This approval does not authorize a new editorial rewrite while materializing the gate decision.

## Canonical materialization contract

Materialize this Human Gate decision through the trusted Core operator using:

- operation kind: `RECORD_PUBLICATION_PREVIEW_APPROVAL`
- expected revision: `3`
- state path: `sources/2026-W33/production-state.json`
- reviewed by: `Owner`
- reviewed at: `2026-09-01T23:17:00Z`
- review reference: `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260902-r3.md`

The operator requires `reviewed_repository_commit_sha` to equal the request-only commit parent. Therefore the request must bind to the exact commit produced by adding this decision authority record, provided that commit changes only this record and leaves Production State, Candidate, reader source, and PDF bytes unchanged.

This operator transport binding must not be misdescribed as a new substantive Human review surface. The exact publication content reviewed and approved by the Owner remains `70c999a87192d2b3674c3f044aa6f50c4c5f95a9`; the subsequent decision-authority commit adds only this Human decision record.

After canonical approval materialization, further Freeze/Release/merge/issue-closure actions must follow the Core release contract and any additional Human Gate requirements. This decision alone must not be silently broadened beyond Publication Preview approval.
