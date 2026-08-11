# Freeze approval and publication policy

Effective: 2026-08-11 13:39 JST.

## Decision

For Japanese Generative AI Technical Survey issues, Human Freeze approval is the final editorial publication gate.

After Freeze approval, automation may complete the remaining mechanical publication steps without requesting a second Human Release approval, provided that it does not change the frozen source or PDF bytes.

The authorized downstream sequence is:

1. create and SHA-bind the Freeze record;
2. mark the exact frozen release manifest as release-authorized by that Freeze approval;
3. merge the frozen work PR using a history-preserving normal merge;
4. re-download the exact frozen PDF artifact;
5. verify the frozen PDF SHA-256 and source-manifest SHA-256;
6. create the predetermined tag/title/asset name;
7. publish the GitHub Release and attach release provenance metadata.

## Human gates that remain

- Candidate Selection
- Issue Architecture
- Visual Review
- Freeze

Freeze approval therefore means: **the reviewed bytes are final and may be merged and publicly released if all deterministic integrity checks pass.**

## Non-negotiable constraints

- Freeze approval never authorizes editing the frozen source or PDF.
- A hash mismatch, missing artifact, changed release manifest, merge conflict, or failed release verification must stop publication rather than regenerate or silently repair the issue.
- `unattended_public_release=false` remains true: publication is still grounded in an explicit human Freeze approval.
- The publication workflow must preserve exact provenance for source manifest, PDF artifact/run, PDF SHA-256, tag, release anchor commit, and approval reference.
- Weekly and Special editions use the same editorial principle. Individual runners may differ, but they must not reintroduce a separate editorial Release approval after a valid Freeze approval.

## Transition note

`SP-2026-M07 v0.1` was frozen under the previous policy, which still required a separate Release approval. The user explicitly supplied that Release approval on 2026-08-11 and simultaneously changed the policy above for future issues. Its frozen source/PDF are not rewritten to retrofit the new policy; a separate release-authorization record bridges the legacy Freeze record to the new publisher.
