# Public release identity policy

Effective for releases after the already-published legacy issues `2026-W32` and `SP-2026-M07`.

## Decision

A published survey is identified by its **issue number only**. Routine public semantic versions such as `v0.1` / `v0.2` are no longer used.

Freeze is the point at which the issue becomes its unique final edition. The frozen source/PDF bytes are authoritative, and the normal publication path does not revise them after Release.

### Canonical public names

Weekly example `2026-W33`:

- tag: `weekly/2026-W33`
- Release title: `Japanese Generative AI Technical Survey — 2026-W33`
- PDF asset: `Japanese_Generative_AI_Technical_Survey_2026-W33.pdf`

Special example `2026-M06`:

- tag: `special/2026-M06`
- Release title: `Japanese Generative AI Technical Survey Special — 2026-M06`
- PDF asset: `Japanese_Generative_AI_Technical_Survey_Special_2026-M06.pdf`

## Internal revisions are provenance, not public versions

Internal source revisions (`source_version`, for example `v0.8`) may continue to exist while drafting and Visual QA iterate. They are useful for deterministic provenance, comparison, and recovery, but must not appear in the public Release tag/title/asset name.

Likewise, compatibility fields such as a pipeline-state `revision` may remain internal until the state schema is separately simplified. They do not define public identity.

## Corrections after publication

The normal model is one frozen Release per issue. Post-Release modification is exceptional rather than a routine version increment.

If a material factual or integrity defect is discovered after publication:

1. preserve the original Release and provenance;
2. open an explicit correction/erratum decision;
3. require human approval for the correction path;
4. clearly label the exceptional corrected artifact or erratum rather than silently replacing the published bytes.

A new `v0.x` Release must not be used as an ordinary editing mechanism.

## Legacy releases

The following existing public identities remain unchanged:

- `weekly/2026-W32/v0.2`
- `special/2026-M07/v0.1`

Historical tags/manifests must not be rewritten merely to match this newer naming policy.
