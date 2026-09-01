# W33 Luna validated-draft provenance repair through Publication Preview session

- Issue: `2026-W33`
- Branch: `weekly/2026-W33-v2-work`
- Exact starting SHA: `fc2a275c7507a56db42ec77641d0fe2cd322d1f0`
- Start guard: remote branch HEAD matched the exact starting SHA before the
  first GitHub write.
- Reviewed-main Core authority: `6267de3f6876f491950139757bfdf1085fc07bdc`

## Scope and authority

This session performed only the handoff-authorized visual-review provenance
repair, canonical validation advancement, Publication Candidate materialization,
and the second canonical advancement to the Publication Preview Human Gate.
The reader prose, TeX source, exact PDF bytes, semantic content, layout,
Evidence attribution, limitations, and review conclusions were not changed.

No Web, Google Drive, raw-source, or fresh Evidence was introduced, and no
additional candidate or Architecture placement was added beyond the one
handoff-authorized canonical Publication Candidate. No shared Core, config,
schema, style, workflow, or non-edition authority was modified. No Publication
Preview decision, freeze, release, or merge was performed.

## Exact visual-review repair

The only content repair was in
`sources/2026-W33/publication/v2/visual-review-v2.json`:

1. PDF SHA-256 `4f1028c221101cd21cf300a3916c9d4b7cf589b5f672a0f97f61aa6afc992243`
   -> `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`.
2. Workflow run `33398104252` -> `33403175661`.
3. Artifact ID `9760255099` -> `9762175041` (both occurrences).
4. Repository PDF blob `9c0de61f6469e2f40ca81c293a541f4669f95bbc`
   -> `c17f1b77434351e49793b11f2ce82815ecb5693e`.

No other stale identifier was present. The repaired visual-review file
SHA-256 is
`2b9ab544fb99e37b83232b65dc865e22213bf29f28a069e002d854b3c5888c2b`, and its
canonical `review_sha256` is
`259928d873761f5c8b5fd3c7cc9c3294784876294181cc73de7dc023cec540be`.
Its reader-manuscript, source, PDF, page-count, and two-page-column review
bindings remain unchanged; the 11-page visual conclusion remains `PASS`.

Repair commit: `74308af9157c8d026ad9d5251bd4f2d57fbc644b`, parent
`fc2a275c7507a56db42ec77641d0fe2cd322d1f0`.

## Canonical validation advancement

The complete current-Core `DRAFT_COMPLETE` contract returned `PASS` before
the transition. The canonical operator bridge then executed exactly once:

- request:
  `sources/2026-W33/execution/requests/w33-validated-draft-advance-20260831-r1.json`
- request SHA-256:
  `5a9138cb21a03dc568dae74bab032c7d362df41a0ee17fcbde53f4c015b52b06`
- request/event commit: `67a1fb8bf900dbee15224f5a39e98b9496770fdd`
- workflow run: `33406632302`
- preflight job: `99535711753` (`PASS`)
- execute job: `99535868081` (`PASS`)
- bridge Actions commit: `cf5355d76b8ea2d7b1f5fc097bbaf8f3c80a40e3`
- transition: `DRAFT_COMPLETE -> VALIDATED_DRAFT` (exactly once)
- validation checkpoint SHA-256:
  `18b540e2b964b8969fcd23cea07a64106f23962b1090afe7f68645d2065396cf`
- post-validation Production State SHA-256:
  `8d2f44d0eeb420d59be8312beba9ca5f686988d30f808076f89930dbcb8317dc`

The bridge receipt and Core stage contract were `PASS`; the validation
checkpoint was materialized and prior checkpoint authorities were preserved.

## Publication Candidate

The canonical Publication Candidate was generated and validated solely from
the existing reviewed Reader Manuscript, validated source, exact repository
PDF, Quality Regression Bundle, Semantic / Editorial Review, and repaired
Exact-PDF Visual Review:

- path: `sources/2026-W33/publication/v2/publication-candidate-v2.json`
- file SHA-256: `e97b5d9005cd4636014ec722cc995296dd77aa7b89f7a9096190bdb44cad1bf1`
- `candidate_sha256`:
  `e837dc1e450caab3dc56ce2785c3ae94373a41388e0bc3c85f82b2f3ed38b7bd`
- status: `READY_FOR_PUBLICATION_PREVIEW`
- bound PDF SHA-256:
  `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`
- bound PDF page count: 11
- candidate materialization commit:
  `e3b12db2f80a67b098e1cd615d532655d43e407d`

The candidate contains no new prose, review conclusion, Evidence, source, PDF,
candidate, or Architecture placement.

## Canonical Publication Preview gate advancement

The canonical operator bridge executed exactly once from the validated state:

- request:
  `sources/2026-W33/execution/requests/w33-publication-candidate-advance-20260831-r1.json`
- request SHA-256:
  `850671f0b0d1931210b21a8c3794aa788ea23819ebc541a3ab83708992d67034`
- request/event commit: `d747fd9097fcf092e34291d08e664590da878819`
- workflow run: `33406966068`
- preflight job: `99536821977` (`PASS`)
- execute job: `99536976975` (`PASS`)
- bridge Actions commit:
  `4055fb4e2da36d09e792ae6d4e469ef8c7dd7d14`
- transition: `VALIDATED_DRAFT -> RELEASE_CANDIDATE` (exactly once)

The canonical Core stage contract and bridge receipt returned `PASS`. The
release-candidate checkpoint has `checkpoints: []`, and no additional
checkpoint, approval record, or human decision was created.

## Final state and stop boundary

The final canonical Production State has SHA-256
`b726b244584156a9a2fb3e89e32935cc7d583060c41ec9ce07372fc2d2278965` and:

- lifecycle: `RELEASE_CANDIDATE`
- `next_action`: `PUBLICATION_PREVIEW`
- `terminal_reason`: `HUMAN_GATE_REACHED`
- `human_gates.publication_preview`: `pending`
- publication preview approval provenance: `null`
- validation checkpoint: `passed`
- freeze: `pending`
- release: `pending`
- exception gate: inactive

Architecture approval remains the existing Owner-approved authority. No
Publication Preview `APPROVED` or `REQUEST_CHANGES` decision was evaluated or
recorded.

## Changed-path inventory from the exact starting SHA

- `sources/2026-W33/execution/bridge-runs/w33-publication-candidate-advance-20260831-r1/core-stage-contract.json`
- `sources/2026-W33/execution/bridge-runs/w33-publication-candidate-advance-20260831-r1/receipt.json`
- `sources/2026-W33/execution/bridge-runs/w33-publication-candidate-advance-20260831-r1/reviews.json`
- `sources/2026-W33/execution/bridge-runs/w33-validated-draft-advance-20260831-r1/core-stage-contract.json`
- `sources/2026-W33/execution/bridge-runs/w33-validated-draft-advance-20260831-r1/receipt.json`
- `sources/2026-W33/execution/bridge-runs/w33-validated-draft-advance-20260831-r1/reviews.json`
- `sources/2026-W33/execution/requests/w33-publication-candidate-advance-20260831-r1.json`
- `sources/2026-W33/execution/requests/w33-validated-draft-advance-20260831-r1.json`
- `sources/2026-W33/execution/sessions/w33-luna-publication-preview-gate-20260831-r1.md`
- `sources/2026-W33/orchestration/v2/checkpoints/DRAFT_COMPLETE.json`
- `sources/2026-W33/orchestration/v2/checkpoints/VALIDATED_DRAFT.json`
- `sources/2026-W33/production-state.json`
- `sources/2026-W33/publication/v2/publication-candidate-v2.json`
- `sources/2026-W33/publication/v2/visual-review-v2.json`

The reader source, exact PDF, and all semantic/layout authorities outside the
repaired visual-review provenance remain byte-identical to the supplied
starting authority.

Normal successful stop:

`PUBLICATION_PREVIEW_GATE_READY_FOR_OWNER_REVIEW`
