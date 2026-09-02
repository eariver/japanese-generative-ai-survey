# W33 Luna Session — Publication Preview r2 Recovery and r3 Gate

## Scope

This session resumed from the history-preserving structural recovery at the exact
Starting SHA below. It executed the existing Owner decision's single
Publication Preview r2 correction and stopped at the next pending Human Gate.
No new Human decision was made.

- Repository: eariver/japanese-generative-ai-survey
- Branch: weekly/2026-W33-v2-work
- Exact Starting SHA: df7e12cad39141aa10134daec6bc96dadb9c391c
- Canonical lifecycle-operation ending SHA: 9fe3363f68dde53bb73d2db635e5147b74a36c0b

## Recovery provenance

- Original Owner-reviewed repository HEAD: 6361b6ea2066e6c64007587511d591dbfbcfa73b
- Original Owner-reviewed candidate_sha256:
  d8edb38eb1c84476e24219caeae7a1fd4fac5bb3b39f1c0cee3bf9940b1e312b
- Original Owner-reviewed PDF SHA-256:
  13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce
- History-preserving structural repair / retained review surface:
  df7e12cad39141aa10134daec6bc96dadb9c391c
- Pre-incident Sol authority HEAD: 644f69a588ea95fcd08556b8adba7c26fce0ad40
- Recovered good tree: eb1719edf44b36a3292e34fa405b91fa8b9f0ae9
- Production State/Candidate/PDF review-surface identity: PASS

The original Owner decision record was not modified. The operator SHA rebind to
df7e12c was required because the trusted operator requires
reviewed_repository_commit_sha to equal the request-only commit parent. This is
a recovery/transport binding to the exact retained review surface, not a new
substantive Owner review and not a change to the original decision's reviewed
HEAD.

## Phase 1 — canonical r2 rollback

A fresh request was created at
sources/2026-W33/execution/requests/w33-publication-preview-revision-20260901-r2-recovery1.json.

- Request-only commit: 0655674e27cc0b0c37690c78e9ebc95460939b40
- Parent: df7e12cad39141aa10134daec6bc96dadb9c391c
- Request blob: c8134027672d4c06163dd1f9709fe556efbbf391
- Full-tree construction and one-path diff: PASS
- Operator run: 33527754049
- Preflight job: 99922845010 — PASS
- Execute job: 99923068707 — PASS
- Operator output commit: 57f6ac57128e0a571481c269b58f6f0d21e398c7
- Publication Preview r2 materialization: PASS
- Rollback: RELEASE_CANDIDATE -> DRAFT_COMPLETE, exactly once
- Validation became pending; Publication Preview stayed pending/null;
  Architecture stayed active; freeze and release stayed pending

The historical rollback and malformed request were not rerun. The recovered
failed-attempt ancestry was preserved.

## Phase 2 — exact source repair

After rollback, only
surveys/weekly/2026-W33/references.bib was changed. The exact one-line
replacement was:

- old count before: 1
- old count after: 0
- new count after: 1
- new source-repair commit: b3ccf172c1820e5c9382f70440636183c571faa7
- references.bib SHA-256: 81c91d1038f0d59559c1b5023c78ae18c02caac3b35f7feb0e135dabbf63fe79
- main.tex SHA-256: 44ef2580c072c7295d052311fca2a9a3a5bf165c7eab19a1375b1f729e8e55a0

The new note is: “Paper metadata; baseline and evaluation details could not be
confirmed from the available primary material.” Main.tex, every sections/*.tex
file, section order, tables, boundary boxes, Week in Review, Sources &
limitations, all other bibliography entries, and upstream authorities were
unchanged.

## CI and exact PDF

- Workflow: Build weekly survey PDF
- Run: #184 / 33528219144 — success
- Build job: 99924586054 — success
- Artifact: 9808729265
- Artifact archive SHA-256:
  5bf351dd7de2a1f0f5fcdfcc009048dbfe46672c7d0b3f8f71539641d26a89b5
- Final TeX warning gate: PASS
- Final PDF SHA-256:
  1885762325c33b575dd6e789dc53f7ed1c30483a9928b6dbf9537ad0e05661f5
- PDF size: 274472 bytes
- PDF page count: 11
- Repository pin commit: b8f90c5f5e140a2f49045919ccbb2b33cc3bf390
- Pinned PDF Git blob: 01a1b98bbaf547c631aaea9d4eb2d8963a278a74
- Bundled checksum and independent digest: PASS

The exact artifact bytes were pinned without mutation.

## Review and validation

All 11 pages passed visual review: no clipping, overlap, missing glyph,
broken column, blank/duplicate page, page-flow regression, or bibliography
truncation. Page 8 has content in both columns. Sources & limitations, Week in
Review, References, and References [27] were readable; [27] contains the new
reader-facing note.

The Issue #433 semantic/editorial review passed:

- remaining VoiceDesigner finding: resolved
- existing Issue #433 repairs: no regression
- substantive reader content: unchanged
- fresh factual claims: 0
- fresh sources/Evidence: 0
- new candidate or Architecture placement: 0
- Weekly Community Movement remains bounded context-only
- Week in Review remains an independent cross-package synthesis

The fail-closed reader scan found zero occurrences in reader source/PDF of:
candidate, Evidence identity, Profile Completeness, LIMITED, Screening, HOLD_OUT,
DROP, materiality, SOCIAL_OBSERVATION, Core v2, accepted capture,
Grok_X_SourseIntake, HOLD, and REJECT.

Regenerated current validation authorities and SHA-256 values:

| Authority | SHA-256 |
|---|---|
| reader-manuscript-v2.json | ce5df090e5255cad819508a9397ac894bbbc24de9b2fb0d0be075ab4e9918e13 |
| deterministic/identifier-preservation.json | 88892cd76baf32c1e57add813ee6521846f3be50cfdfe30dd1cb32c4d6985122 |
| deterministic/pdf-preflight.json | 65b7c7d891dd3447fce9fefc6deb4c84d1d054f1e9b5b356729685d6aab18f73 |
| deterministic/subject-entity-property-binding.json | 194d5d6b145c9ca89fa45ca1878014c1f82356dbe36d3c20a973db2526efab76 |
| quality-regression-bundle-v2.json | d399a64349ac1666713cfdce44e2c088bcf9154ebae761a84ccf8a5bcc8117c6 |
| semantic-editorial-review-v2.json | 01dda1340422bdc07155ec74740c8a2be610ae691a6dc71a97d823780645c10d |
| visual-review-v2.json | c38d80bb815d3884b57feb0ab1a05faa76c1630167b76bd4f62b2a4bfc69eade |

The validation-authority commit was b4685c16e37693f6f1e136f0617d78df1b21367e.
DRAFT_COMPLETE stage-contract validation: PASS.

## Canonical advancement and candidate

DRAFT_COMPLETE -> VALIDATED_DRAFT was executed exactly once.

- Request-only commit: 4e9c0a93701116f6b1bfa548097167cd6dec8c9f
- Operator run: 33530402788
- Preflight: 99931810629 — PASS
- Execute: 99931976043 — PASS
- Output commit: 50969c5ef6454b896995f5b109a4578690e9da30
- Core stage contract, receipt, and Luna review: PASS

A replacement
sources/2026-W33/publication/v2/publication-candidate-v2.json was generated
from the repaired current authorities and validated.

- Candidate file SHA-256: aa223f35eb12af7f1046b612aa44354d02bcf0a8e6f8d31b0ba39b7bd05aa021
- candidate_sha256: f3e0ae94ae51e7b5f5374d68c66ecaf688f0d7d43c5db85bc656925a6d07333e
- Candidate Git blob: c28883eef72f24012060b8d27a1947c99d08b1a5
- Candidate PDF binding: 1885762325c33b575dd6e789dc53f7ed1c30483a9928b6dbf9537ad0e05661f5
- Candidate validation: PASS

VALIDATED_DRAFT -> RELEASE_CANDIDATE was executed exactly once.

- Request-only commit: f5ef3e94276eb52b35bdac6dffa3ce7a2c170837
- Operator run: 33530784696
- Preflight: 99933104271 — PASS
- Execute: 99933262744 — PASS
- Output commit / canonical operation ending SHA:
  9fe3363f68dde53bb73d2db635e5147b74a36c0b
- Core stage contract, receipt, and candidate review: PASS

## Final state and stop boundary

At the canonical operation ending SHA:

- lifecycle_state = RELEASE_CANDIDATE
- next_action = PUBLICATION_PREVIEW
- terminal_reason = HUMAN_GATE_REACHED
- validation = passed
- human_gates.publication_preview = pending
- human_gate_provenance.publication_preview = null
- freeze = pending
- release = pending

No Publication Preview r3 Human decision or approval record was created. Issue
#433 was not closed. No freeze, release, merge, reset, revert, rewrite, or new
branch was performed. Luna used force=false for branch ref updates; no force
ref update was used.

Reader-facing change was limited to surveys/weekly/2026-W33/references.bib;
the derived exact surveys/weekly/2026-W33/main.pdf was repinned. The
Publication Candidate and all validation authorities were regenerated from the
current repaired source/PDF; stale pre-repair authorities were not reused.

Result: PUBLICATION_PREVIEW_R3_GATE_MATERIALIZED

