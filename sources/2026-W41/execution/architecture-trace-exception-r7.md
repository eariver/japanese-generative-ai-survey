# W41 Architecture trace exception r7 (SC-M41-02 / S41-B)

Status: `EDITION_LOCAL / MACHINE_TRACE_LABEL / NON_READER`
Date: 2026-10-12 JST
Binding exclusion: `execution/nanobanana-legacy-negative-exclusion-r6.md`
Label: `LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE`

## Machine trace location (exact, literal, required by Core)

- File: `sources/2026-W41/architecture-v2.json`
- Package: `P4` (Image model brief: Nano Banana 2.1)
- Array: `packages[3].boundaries[]`
- Literal string (byte-exact from Matrix `remaining_boundaries`, itself verbatim
  from immutable accepted Card limitation-1):
  `Pricing/license absent; docs page unfetched; rollout post nonexistent.`
- Offending span: `rollout post nonexistent` (unsupported categorical absence;
  see exclusion overlay §1).

## Why it is preserved literally

Frozen `survey_architecture_v2_base.validate_architecture` requires every
selected candidate's Matrix `remaining_boundaries[]` membership to appear
exactly and fully in the destination package `boundaries[]`. Removing or
rewording this string would fail Core validation (`missing Evidence boundaries`)
or constitute silent erasure of accepted-Evidence audit text. It is therefore
preserved as a *legacy unverified evidence-text trace* in the machine array only.

## Reader-surface prohibition (binding)

This string MUST NEVER appear as a factual claim in:
`packages[].title`, `packages[].purpose`, `packages[].must_cover_requirements`,
review summary narrative, attention prose, Draft JSON, reader manuscript, TeX,
PDF, or any Sol/Human-facing claim summary. Verified r7: title/purpose/
must_cover across P1–P6 contain zero hits (grep audit in session log); the only
hit in `architecture-v2.json` is the P4 boundaries trace above.

The only admissible narrative for the blog-absence point in all reader surfaces:
`matching issuer blog post not found among pages checked on 2026-10-12`
(P4 purpose + must_cover[2], exclusion overlay §2).

If any frozen Core generator copies this trace string into a mandatory
human-reader surface as an endorsed claim and it cannot be separated, STOP per
contract §4 and request versioned Evidence reacceptance; do not forge acceptance.

(End of file)
