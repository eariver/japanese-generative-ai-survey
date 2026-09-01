# 2026-W32 v0.2 Freeze Record

Status: **FROZEN_RELEASE_CANDIDATE**

## Build provenance

- Workflow run: `31350762039`
- Job: `93340968221`
- PDF-producing source commit: `6fa5d5d74bdcd063458a6f3e97197a32051f77a1`
- Artifact ID: `9048888577`
- Artifact name: `japanese-generative-ai-survey-2026-W32`
- Artifact ZIP digest: `sha256:7dd0ffa07eac2ba6b42a2f2e724f7473c68d36fb96339c822d987179dcd78342`
- Extracted `main.pdf` SHA-256: `6507d866476820931af62daa29975698e3ee6849800cf2ce15706680e4f57c21`
- Artifact expiry reported by GitHub Actions: `2026-08-24T02:50:05Z`

## CI result

All workflow steps passed:

1. Checkout repository
2. Compile 2026-W32 with LuaLaTeX
3. Validate final TeX log
4. Upload PDF artifact

The final-log validation gate checks for unresolved references/citations, rerun requests, Overfull/Underfull boxes, and missing glyphs before artifact upload.

## PDF preflight

- Pages: **16**
- Page size: **A4 on all 16 pages**
- Encrypted: **false**
- Openable: **true**
- Fonts: HaranoAji and Latin Modern fonts embedded
- PDF version: 1.7
- Creator: LuaLaTeX / LuaHBTeX 1.24.0 (TeX Live 2026)

## Visual review

All 16 pages of the CI-produced artifact were rendered and reviewed.

Checked for:

- clipped or overlapping text
- broken/missing glyphs
- malformed callout boxes
- section-heading hierarchy and column flow
- unintended blank pages
- Cover / Contents balance
- Late Breaking chronology presentation
- Watchlist / Source Notes transition
- References overflow and URL wrapping

No freeze-blocking visual defects were found.

### Regression check from r1 to r2

The previous CI artifact and r2 were rendered and pixel-compared.

- Pages 1–12: unchanged
- Pages 15–16: unchanged
- Pages 13–14: changed as expected after replacing the stale hard-coded Astra page reference with `\\label` / `\\pageref`

The final r2 PDF resolves the reference as `今号 p.3`; the obsolete `p.3--4` text is absent.

## Editorial gate

Prior gates already passed:

- candidate inventory / source normalization
- primary-source verification
- paper review
- candidate selection
- issue architecture
- citation-to-claim audit
- chronology audit
- high-risk claim review
- editorial prose polish

**Decision:** 2026-W32 v0.2 is suitable to freeze as the release candidate. Future content changes should create a new revision rather than silently modifying this frozen state.
