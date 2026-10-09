# Publication Surface Checkpoint Compatibility Restoration — Execution Record (2026-10-03)

- Starting HEAD: `152112d5c2bcf6efbd0e39a437e21f97a4a363e8`
- Starting tree: `95b6f65a69523cf18907c19e20a7c18c46c4c39e`
- Authority: edition-local compatibility restoration only. No content repair,
  no r15, no gate decision, no lifecycle change, no Core change.

## Pre-restoration drift signature (read-only reproduction)

Exactly the seven known drifts, nothing more:

```text
publication-pdf, quality-regression-bundle, reader-manuscript,
reader-surface-gate, semantic-review, validated-source, visual-review
```

`validate_agent_state` returned precisely these seven; no additional drift.

## Restoration sources (exact historical Git bytes, SHA-verified)

- Seven DRAFT_COMPLETE-bound files restored from `59f89f89d9606ddb1328aeff07e4f63c0aae4ae7`
  (all seven byte-hashes match the §5 expected values exactly).
- Publication Candidate: the §6-named commit `4f8b535c38f35879f7ea84b39a5c5f3c08eb966d`
  does **not** carry the checkpoint bytes (its candidate hashes to
  `62033bb3...`, not `fa01ed1e...`). Per §6's byte-identity proviso, the
  candidate was instead restored from `998eb7db0` (Phase 2 materialization),
  whose bytes hash exactly to the VALIDATED_DRAFT-bound
  `fa01ed1e87d060e4ec5b244ce7df2d61efc18508132f5166aec7b79fbb272a4a`.
  No file was reconstructed or regenerated; only `git show` bytes were used.

## Preserved newer work (§7)

Untouched (verified via status: only the eight files above modified):
Evidence r8 + r8 Views, Materiality/Completeness/Matrix/Selection r8,
Architecture v4, r14 reader authority, coverage r14, VM-D112 staged intake,
all execution reports.

## Validations (§8–§9)

- Candidate/PDF exact binding: PASS
  (`candidate.pdf.sha256 == live main.pdf == 78f4cc8c...`).
- `validate_agent_state`: PASS.
- Lifecycle unchanged: `RELEASE_CANDIDATE`, architecture `approved`,
  preview `pending`, next `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`.

## Terminal

Review surface ready for an exact Human Publication Preview REQUEST_CHANGES
decision against the final commit of this restoration. No gate operation was
performed here.
