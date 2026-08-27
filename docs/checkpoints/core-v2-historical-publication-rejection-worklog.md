# Core v2 historical Publication Preview rejection — worklog

## Trigger

SP001 Publication Preview Human review on Issue #400 explicitly requested changes to the exact reviewed candidate lineage. After the reader-substantive-fidelity Core repair was merged to `main` at `beb78b9d04df2d2fdfe5c6bcf7304682bfbd528d`, the canonical `REQUEST_PUBLICATION_PREVIEW_REVISION` request was admitted by the trusted operator bridge but failed during execution.

Operator run `33090510734` / run #108 passed trust preflight and failed only when the Human Gate runtime revalidated the historical reviewed Publication Candidate under the newly strengthened current Reader Manifest validator. The historical manifest labels the final-synthesis location as `Section 6.3 — なぜ恒常的なfrontier構成要素になったのか`, while the reviewed TeX contains that reader block as a subsection. The new exact traceability validator correctly rejects that historical candidate.

## Defect

`REQUEST_CHANGES` and `APPROVED` both used the same `_reviewed_artifacts()` path. For Publication Preview, that path always called current `publication.validate_candidate()` before recording either decision.

That creates a validator-upgrade deadlock: a Human may need to reject an exact historical candidate because a newer validator exposes a defect, yet the rejection cannot be recorded because the same newer validator rejects the historical candidate before the Human decision can be persisted.

This is a Core Human Gate backward-compatibility defect. It is not SP001-specific and must not be repaired by mutating the reviewed candidate or weakening Publication Preview approval.

## Repair

Branch: `fix/core-v2-historical-publication-rejection`

The Human Gate reviewed-artifact collector now has an explicit `require_current_candidate_validity` control.

- Normal approval paths keep the default `True` behavior and still require full current `publication.validate_candidate()` success.
- `REQUEST_CHANGES` uses `False` so an exact historical candidate can be rejected after validator or Candidate-schema evolution.
- The rejection path requires a parseable JSON object, exact issue/profile identity, a durable PDF authority, and exact PDF SHA-256, then relies on the existing reviewed-commit durability check to prove exact reviewed State/Candidate/PDF bytes are committed and reachable from the canonical work branch. It deliberately does not require current Candidate schema or substantive-validation success because either may be the reason the historical bytes are being rejected.
- Regeneration-boundary validation, immutable review records/indexes, stale-revision protection, selective invalidation, and all approval semantics remain unchanged.

## Regression coverage

A Human Gate round-trip regression test now simulates a historical Publication Candidate that both the current `publication.validate_candidate()` path and the current Candidate schema would reject.

The test proves both sides of the responsibility split:

1. Publication Preview `APPROVED` still fails under the rejecting current validator.
2. Publication Preview `REQUEST_CHANGES` succeeds for the same exact reviewed commit and records the exact candidate/PDF hashes before rolling back to the requested regeneration boundary.

## SP001 consequence

After this Core maintenance is fully audited, explicitly Human-approved, and merged, SP001 can retry the already explicit Issue #400 `REQUEST_CHANGES` decision without altering the reviewed candidate bytes. The expected regeneration boundary remains `ARCHITECTURE_ESTABLISHED`, preserving the approved Architecture while regenerating Draft, synthesis, reader source, semantic/visual review, and a new exact Publication Preview candidate.

SP001 Freeze/Release remains prohibited until the regenerated exact PDF receives explicit Human Publication Preview approval.

## Remaining maintenance steps

1. Run diagnostic CI on the exact current branch head.
2. Perform the required pre-freeze full-PR cross-check against current `main`.
3. Freeze one candidate SHA.
4. Run all seven final-audit points from zero on that exact SHA.
5. Present the 7/7 candidate for explicit Human Core-maintenance approval; do not merge before approval.
6. After merge, retry SP001 Human rejection recording and continue SP001 regeneration.
