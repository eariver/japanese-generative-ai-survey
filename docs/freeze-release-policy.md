# Publication Preview, Freeze, and release policy

Effective: 2026-08-13 JST. This supersedes the separate Human Freeze gate for future Special production.

## Decision

For Japanese Generative AI Technical Survey Special issues, **Publication Preview approval is the final normal human publication gate**.

The user is shown the exact PDF intended for public release. Approval of that preview SHA-binds the reviewed PDF and authorizes the remaining deterministic publication sequence, provided that automation does not change the approved source semantics or PDF bytes.

The authorized downstream sequence is:

1. record the Publication Preview approval and the corresponding Visual Review machine-checkpoint record against the exact PDF SHA-256;
2. create and SHA-bind the Freeze record under `PUBLICATION_PREVIEW_APPROVAL` authority;
3. mark the exact frozen release manifest as release-authorized by that Publication Preview approval;
4. merge the frozen work PR using a history-preserving normal merge;
5. re-download the exact frozen PDF artifact;
6. verify the frozen PDF SHA-256 and source-manifest SHA-256;
7. create the predetermined tag/title/asset name;
8. publish the GitHub Release and attach release provenance metadata.

No second Human Visual Review, Human Freeze, or Human Release approval is requested during the normal path.

## Normal Human Gates

Special production has two normal user-interaction gates:

1. **Architecture Review** — after Evidence/Selection work has produced the proposed issue architecture, the user approves the editorial thesis, topic roles, section/package structure, and page allocation. Candidate Selection remains an auditable internal editorial checkpoint but is not a separate user stop.
2. **Publication Preview** — after drafting, validation, layout, and PDF build, the user approves the exact PDF intended for publication. That single approval authorizes Visual Review recording, Freeze, merge, and public Release for the identical approved bytes.

All other pipeline gates remain deterministic validation/state checkpoints rather than routine requests for user approval. For new issue state, `human_gate_required_for_publication_preview=true` while `human_gate_required_for_visual_review=false`, `human_gate_required_for_freeze=false`, and `human_gate_required_for_public_release=false`.

## Exception Gate

An additional user decision is requested only when a new editorial or publication choice is genuinely required. Typical triggers are:

- Evidence is insufficient to form a reasonable Architecture;
- material sources conflict and require editorial judgment;
- the approved Architecture must be materially changed;
- a content-bearing change is required after Publication Preview approval;
- the approved PDF/source provenance cannot be preserved;
- publication scope, identity, or correction policy must deviate from the normal rule.

The following do **not** create a new Human Gate when they can be resolved without changing approved content or provenance:

- retryable collection, build, or CI failures;
- layout-only repair before Publication Preview;
- merge conflicts resolvable while preserving the approved source and PDF;
- mechanical publication retry using the identical frozen bytes.

Recovery workflows must derive their timestamp/reference authority from the already-committed Publication Preview approval record. They must not accept a new Freeze/Release approval reference that could establish a second or conflicting publication authority.

## Public identity after Freeze

For releases after the legacy W32 and SP-2026-M07 publications, **the issue number is the complete public Release identity**. No routine `v0.1` / `v0.2` suffix is assigned after Freeze.

Internal `source_version` values remain for deterministic drafting/build provenance, but they are not public Release versions. Canonical naming and the exceptional correction policy are defined in `docs/release-identity-policy.md`.

## Non-negotiable constraints

- Publication Preview approval never authorizes editing the approved source semantics or PDF bytes after approval.
- A hash mismatch, missing artifact, changed release manifest, or failed provenance verification must stop publication rather than regenerate or silently substitute the issue.
- `unattended_public_release=false` remains true: publication is grounded in explicit Publication Preview approval even though Freeze/merge/Release are automated afterward.
- The publication workflow must preserve exact provenance for Publication Preview approval, source manifest, PDF artifact/run, PDF SHA-256, tag, release anchor commit, and approval reference.
- A deterministic technical recovery may continue under the existing approval only when it preserves the approved content and provenance.
- Post-Release correction is exceptional and explicit; routine version increments must not be used as an editing loop.

## Transition notes

Historical Special issues retain the approval records that existed when they were produced. In particular, SP-2026-M03 used separate Visual Review and Freeze wording during production, and SP-2026-M07 was frozen under an earlier policy. Their frozen records are not rewritten retroactively.

The two-gate interaction model applies prospectively. Existing internal state names such as `candidate_selection`, `visual_review`, and `freeze` are retained for provenance compatibility even when they no longer correspond one-to-one with separate user interaction gates. The old standalone Special Visual Review workflow is removed prospectively; its implementation module remains only as an internal helper for recording the Publication Preview approval.
