# Weekly Survey GitHub Release Process

Status: operational release policy for frozen weekly issues  
Applies after: human/reviewer Freeze Gate

## 1. Purpose

A frozen weekly issue may be published as a GitHub Release with:

- a Git tag fixed to the frozen source commit;
- the exact frozen PDF as a Release asset;
- `SHA256SUMS.txt` for independent digest verification;
- release notes containing source/freeze provenance.

The Release is a distribution surface. The repository TeX/Bib/Evidence tree remains the Source of Truth.

## 2. Tag convention

Weekly release tags use:

```text
weekly/<issue-id>/<revision>
```

Example:

```text
weekly/2026-W32/v0.2
```

The tag must resolve to the PDF-producing frozen source commit recorded in:

```text
sources/<issue>/release-manifest.json
```

A tag is never moved to a later commit merely because operational metadata was added after freeze.

## 3. Release manifest

Each releasable frozen revision records at least:

- issue ID / revision;
- frozen source commit;
- canonical release tag/title;
- release PDF filename;
- expected PDF SHA-256;
- page count;
- freeze record;
- PDF source mode.

Supported PDF source modes:

### `actions-artifact`

Used when the exact frozen PDF bytes are available only from the already validated GitHub Actions artifact.

The manifest pins:

- workflow run ID;
- artifact ID;
- artifact name;
- expected PDF SHA-256.

The release workflow verifies all of those before using the PDF.

### `rebuild`

Preferred for future issues after reproducible-PDF controls are enabled.

The workflow checks out the frozen source commit, sets a deterministic `SOURCE_DATE_EPOCH`, rebuilds with the pinned TeX Live version, and requires the resulting PDF SHA-256 to match the frozen digest.

## 4. Why W32 uses the frozen Actions artifact

The W32 v0.2 PDF was frozen before deterministic PDF timestamps were introduced.

Inspection of the frozen file showed a build-time `CreationDate` / `ModDate` and PDF identifier. Therefore source equality alone is not sufficient to assume a later build will be byte-identical.

For W32, the release manifest deliberately points to the exact validated Actions artifact from:

```text
run      31350762039
artifact 9048888577
```

The release workflow downloads that artifact and checks:

```text
SHA-256 = 6507d866476820931af62daa29975698e3ee6849800cf2ce15706680e4f57c21
```

before any tag or GitHub Release write.

The pinned W32 Actions artifact currently expires on 2026-08-24, so W32 should at least be promoted to a GitHub Release draft before that artifact expires. Once the verified PDF is attached to the draft, the draft Release becomes the durable staging copy for publication.

## 5. Future reproducible PDF policy

`Build weekly survey PDF` now exports:

```text
SOURCE_DATE_EPOCH=<source commit timestamp>
FORCE_SOURCE_DATE=1
```

before LuaLaTeX compilation and records `main.pdf.sha256` beside the PDF artifact.

For new issues, the expected workflow is:

1. build with deterministic timestamp inputs;
2. visual/citation/freeze review;
3. record the frozen PDF SHA-256 in `release-manifest.json`;
4. later rebuild the same frozen commit under the same TeX Live/toolchain;
5. require byte-for-byte digest equality before Release publication.

The TeX Live version remains part of release provenance.

## 6. GitHub Actions workflow

Use:

```text
Actions -> Release frozen weekly survey -> Run workflow
```

Inputs:

```text
issue_id
revision
mode = validate | draft | publish
confirmation = <issue>@<revision>
```

Example:

```text
issue_id      2026-W32
revision      v0.2
mode          validate
confirmation  2026-W32@v0.2
```

### `validate`

Safe/no-write release smoke test.

It:

- validates the frozen release manifest;
- obtains the exact frozen PDF according to `pdf_source`;
- verifies the PDF SHA-256;
- emits the proposed PDF, `SHA256SUMS.txt` and Release Notes as an Actions artifact.

It creates no tag and no GitHub Release.

### `draft`

After `validate` passes, this mode:

- creates or verifies the canonical frozen source tag;
- creates a GitHub Draft Release if none exists;
- attaches the verified PDF and `SHA256SUMS.txt`;
- refuses to overwrite an already-published Release;
- if the Draft already exists, downloads its PDF asset and verifies the frozen digest instead of clobbering it.

This is the human inspection point before publication.

### `publish`

This mode requires:

- the canonical tag already exists and resolves to the frozen source commit;
- a Draft Release already exists;
- the Draft PDF asset matches the frozen SHA-256;
- `SHA256SUMS.txt` is present.

Only then does it change the Draft to a published Release and mark it Latest.

`publish` is intentionally not a one-click shortcut from no Release to public Release; `draft` must occur first.

## 7. Immutable Releases

GitHub supports repository-level Immutable Releases.

When enabled, immutability is enforced after publication:

- the Git tag associated with a published Release cannot be modified or deleted while the Release exists;
- published Release assets cannot be modified or deleted;
- GitHub can provide a cryptographically signed release attestation covering the Release assets.

This project should enable Immutable Releases before routine public publication, after the first Draft/Publish workflow has been validated. Draft Releases remain mutable until publication, which matches the project's desired review process.

When immutability is enabled, the workflow attempts `gh release verify` after publication. Failure of this optional verification step does not undo an otherwise successful release; the release digest has already been independently checked before publication.

## 8. Security / permission model

The Release workflow is `workflow_dispatch` only.

It requires:

```yaml
permissions:
  contents: write
  actions: read
```

`actions: read` is required when the frozen PDF is downloaded from a prior Actions artifact. `contents: write` is required to push the release tag and manage the GitHub Release.

The workflow does not create a Release by targeting an arbitrary old commit through the Releases API. It first creates/verifies an explicit Git tag at the frozen source commit and then creates the Release using `--verify-tag`.

## 9. Failure semantics

Publication must fail when:

- confirmation does not match issue/revision;
- manifest is not frozen;
- tag points to a different commit;
- pinned Actions artifact metadata is wrong or expired;
- rebuilt/frozen PDF SHA-256 differs from the manifest;
- an existing Draft contains a different PDF asset;
- `publish` is requested before a Draft exists;
- `SHA256SUMS.txt` is missing from the Draft.

A failed release operation must not silently replace assets with `--clobber`.

## 10. Revision policy

Once a weekly Release is published, substantive content corrections create a new survey revision and a new tag, for example:

```text
weekly/2026-W32/v0.3
```

Do not silently replace the PDF behind `weekly/2026-W32/v0.2`.
