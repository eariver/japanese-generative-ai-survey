# Weekly Survey GitHub Release Process

Status: operational release design for frozen weekly survey PDFs.

## 1. Objective

A frozen weekly survey should be distributable as a GitHub Release with:

- a stable release tag;
- the verified PDF as a Release asset;
- `SHA256SUMS.txt`;
- machine-readable `RELEASE_METADATA.json`;
- an auditable link back to the exact PDF-producing source commit and freeze record.

The public Release is downstream of the existing Freeze Gate. A successful TeX build alone never authorizes publication.

## 2. Important distinction: Release tag vs frozen source commit

The Release tag is deliberately a **release-control anchor**, not the authoritative pointer to the PDF-producing source tree.

GitHub rejects creation of a tag at some historical commits through `GITHUB_TOKEN` when that historical commit adds or modifies `.github/workflows/` relative to the current default branch. The token would need repository `Workflows: write`, which the Actions `GITHUB_TOKEN` cannot be granted for this case.

Therefore the release design records two different commits:

```text
release_tag -> release_anchor_commit on the current default branch

RELEASE_METADATA.json / release-manifest.json
    -> frozen_source_commit
    -> exact PDF SHA-256
```

The contents of the survey are identified by `frozen_source_commit + pdf_sha256`, not by assuming that the Release tag itself points to the source commit.

This separation is intentional and must not be collapsed later for convenience.

## 3. Per-issue release manifest

Each frozen issue has:

```text
sources/<issue>/release-manifest.json
```

It records at least:

- issue and revision;
- frozen source commit;
- canonical Release tag/name;
- PDF asset filename;
- expected PDF SHA-256;
- page count;
- freeze record;
- the source of the PDF binary.

For W32 the exact binary comes from the already validated frozen Actions Artifact because that issue was frozen before reproducible PDF timestamps were introduced.

For later issues, `pdf_source.mode = rebuild` may be used once the normal build has been frozen with the repository's reproducible timestamp policy.

## 4. Workflow modes

Use:

```text
Actions -> Release frozen weekly survey
```

The workflow has three modes.

### `validate`

Read-only with respect to tags and Releases.

1. Validate `release-manifest.json` and the freeze record.
2. Obtain the exact frozen PDF, either from the recorded Actions Artifact or by reproducible rebuild.
3. Verify its SHA-256 against the frozen manifest.
4. Upload a temporary `weekly-release-validation-*` Actions Artifact.

This is the safest first operation for every frozen issue.

### `draft`

Creates a GitHub Draft Release after the same PDF validation.

1. Determine the repository default branch.
2. Ask the GitHub Releases API/CLI to create the new Release tag from that **current default branch**, avoiding a historical-workflow tag write.
3. Resolve and record the actual tag commit as `release_anchor_commit`.
4. Attach:
   - the verified PDF;
   - `SHA256SUMS.txt`;
   - `RELEASE_METADATA.json`.
5. Download the PDF from the new Draft Release and verify its SHA-256 again.
6. Leave the Release as a Draft.

`RELEASE_METADATA.json` contains both `release_anchor_commit` and `frozen_source_commit` so the distinction remains machine-readable.

### `publish`

Publishes **an existing Draft only**. It never creates a new Release.

Before changing Draft state it:

1. downloads the PDF, checksum, and `RELEASE_METADATA.json` from the Draft itself;
2. verifies the PDF digest against the frozen manifest;
3. verifies the recorded frozen source commit;
4. verifies that the current Release tag still resolves to the recorded `release_anchor_commit`;
5. only then changes the Release from Draft to published.

This means publication does not depend on the original Actions Artifact still being within its retention window, provided the Draft was created while the artifact was available.

## 5. W32 special case

W32 frozen PDF:

```text
source commit:
6fa5d5d74bdcd063458a6f3e97197a32051f77a1

PDF SHA-256:
6507d866476820931af62daa29975698e3ee6849800cf2ce15706680e4f57c21

frozen Actions run:
31350762039

frozen Artifact ID:
9048888577
```

The PDF contains a build-time CreationDate/PDF ID, so a later rebuild is not assumed to be byte-for-byte identical. The Release workflow therefore retrieves that exact frozen Artifact and verifies the digest before Draft creation.

## 6. Reproducible PDFs for later issues

The normal weekly build sets:

```text
SOURCE_DATE_EPOCH=<source commit timestamp>
FORCE_SOURCE_DATE=1
```

and records `main.pdf.sha256` beside the PDF in the Actions Artifact.

The intended later-issue freeze process is:

```text
frozen source commit
    -> reproducible LuaLaTeX build
    -> verified PDF SHA-256
    -> release-manifest.json
```

A future issue should use `pdf_source.mode = rebuild` only after byte-for-byte reproducibility has actually been demonstrated for that issue.

## 7. Immutable Releases

GitHub Immutable Releases are recommended once the Draft/Publish workflow is proven operational for the repository.

With immutability enabled, after publication:

- the tag associated with the Release cannot be moved or deleted while the Release exists;
- Release assets cannot be replaced or deleted;
- GitHub creates a release attestation that can be verified with `gh release verify` and `gh release verify-asset`.

The recommended sequence remains:

```text
validate -> draft -> inspect -> publish
```

because immutability applies after publication, not while a Release is still a Draft.

## 8. Assistant workflow execution

Routine workflow execution may be initiated through the repository's `automation-control` branch and `.github/workflows/assistant-control.yml`.

The control channel allowlists only known workflows/inputs. A public Release `publish` request additionally requires `publish_authorized=true` in the control request; operational validation and Draft creation do not imply permission to publish publicly.
