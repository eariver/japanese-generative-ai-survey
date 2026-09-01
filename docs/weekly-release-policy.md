# Weekly publication path

## Current policy

For Weekly issues published after the legacy `2026-W32` issue, public Release identity is the issue ID only.

Use:

- publisher: `.github/workflows/release-weekly-survey-issue-only.yml`
- tag: `weekly/<issue-id>`
- title: `Japanese Generative AI Technical Survey — <issue-id>`
- PDF: `Japanese_Generative_AI_Technical_Survey_<issue-id>.pdf`

Example for W33:

- `weekly/2026-W33`
- `Japanese Generative AI Technical Survey — 2026-W33`
- `Japanese_Generative_AI_Technical_Survey_2026-W33.pdf`

The frozen release manifest must use `release_identity_mode=ISSUE_ONLY`, must not contain a public `revision`, and must carry `public_release_authorized=true` with `release_authorization.mode=FREEZE_APPROVAL`.

Freeze remains the final Human publication gate. The publisher only executes that approval after re-verifying the frozen source/PDF provenance.

## Legacy workflow

`.github/workflows/release-weekly-survey.yml` is retained only to preserve/reason about the already-published W32 versioned release contract. It must not be selected for W33 or later normal publication.

W32 remains:

- `weekly/2026-W32/v0.2`

Do not rename or rewrite that historical Release.

## Corrections

A normal issue has one public Release. If a serious post-publication factual or integrity defect requires correction, use an explicitly approved exceptional correction/erratum path. Do not resume routine `v0.x` numbering.
