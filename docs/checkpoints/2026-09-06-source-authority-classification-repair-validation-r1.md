# Survey Production Core v2 — bounded source-authority classification repair

Status: `REPAIR_COMPLETE_READY_FOR_FRESH_SOL_PREFREEZE_CROSSCHECK`

This record covers PR #484 conversation contract `5559672118`. It is a
bounded authority repair record, not a freeze, Seven-point audit, merge
authorization, Human approval, or W34 production record.

## Fixed-head scope and write boundaries

- Repository: `eariver/japanese-generative-ai-survey`
- Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
- Exact starting maintenance SHA: `fb2ee8d488cb2ad240539d94005f6d59dd47c21b`
- Main: `d8fa79ef2affacec49a47e6fc88018fb99f36899`
- Main tree: `b6c1b2cbc13165e64ac1d88d4d36b7515f7494da`
- W34 read-only fixture: `df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`
- Target PR: `#484`, draft/open/unmerged

Only the existing maintenance branch is in scope. `main` and W34 were treated
as read-only. No new branch, force push, reset, rewrite, rebase, merge, Human
decision, freeze, Seven-point audit, or sidecar execution was performed.

## Bounded implementation

`scripts/survey_evidence_v2.py` now resolves `source_type` through an exact,
reviewed map only. The lexical fallback that promoted arbitrary labels to
authority classes was removed. Unsupported or empty values fail with a clear
`unsupported source_type for Evidence authority` error.

The retained explicit taxonomy is:

| Source values | Derived class |
| --- | --- |
| `PRIMARY_OFFICIAL`, `official-feed-item`, `official-index`, `official-index-snapshot`, `official-page`, `first_party_release_or_docs`, `first_party_official`, `government_security_authority`, `vendor_technical`, `official_publisher_page`, `first_party_product_release`, `first_party_product_changelog`, `first_party_product_docs`, `first_party_announcement`, `first_party_vendor_blog`, `first_party_product_release_notes`, `first_party_product_announcement`, `first_party_safety_publication`, `first_party_product_safety_publication`, `first_party_technical_example`, `vendor_technical_blog`, `vulnerability_authority_api`, `industry_rights_authority`, `government_security_mirror` | `PRIMARY_OFFICIAL` |
| `PRIMARY_PAPER`, `paper`, `arxiv_primary`, `primary_research_record`, `primary_research_pdf`, `first_party_research_publication`, `official_conference_paper` | `PRIMARY_PAPER` |
| `PRIMARY_REPOSITORY`, `github-release`, `github_release_api_response`, `github-repository`, `official_project_repo`, `repository_release`, `first_party_repository` | `PRIMARY_REPOSITORY` |
| `SOCIAL`, `dailyx_x_observation`, `x-community-signal`, `grok_x_observation_corrected_r2` | `SOCIAL` |
| `SECONDARY`, `SECONDARY_INVESTOR_ACCOUNT`, `prior-week-authority`, `sol_working_set_observation`, `carryover_recheck`, `sol_discovery_working_record` | `SECONDARY` |

This includes the exact source vocabulary required by the canonical fixtures
and the exact W34 fixture. No free-form authority-looking spelling is an
implicit alias.

`validate_evidence_card()` now requires every task-bound Card source,
including ordinary Discovery-origin sources, to equal the authority-derived
`source_class`. Existing locator/task binding and stricter Supplement exact
field binding remain unchanged.

## Regression probes

- `not-an-official-source`, `vendor-rumor`, `research-commentary`,
  `not-a-repository`, `github-discussion`, and `totally-arbitrary-source`:
  rejected as unsupported; no lexical promotion.
- Canonical `PRIMARY_OFFICIAL`, `PRIMARY_PAPER`, `PRIMARY_REPOSITORY`,
  `SOCIAL`, and `SECONDARY`: classified correctly.
- Supplement class mismatch: rejected.
- Discovery-origin class overstatement without a Supplement: rejected.
- Discovery-origin class overstatement in a package that also contains a
  Supplement: rejected.
- Exact-class Discovery-origin Card: accepted.
- Explicit task-bound Supplement Card: accepted.

The Evidence test module passed: `12 tests`.

## Preserved controls

The existing zero-byte Supplement repair remains covered, including schema and
runtime rejection, non-zero positive path, exact byte-count/SHA, repository
path/symlink confinement, unknown/DROP/wrong-task/ambiguous binding rejection,
immutable accepted runs, checkpoint-bound active Evidence/View resolution,
profile-specific interactive Evidence, operator pending-Gate invalidation,
and the no-Human-decision boundary. Workflow count remains `7`; Human Gate
count remains `2`.

## Fresh W34 exact read-only regression

The candidate Core was overlaid into a new disposable detached checkout at
`weekly/2026-W34-v2-work@df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`.
The remote W34 branch and `main` were not written.

W34 Discovery source types encountered and explicitly mapped were:
`arxiv_primary`, `carryover_recheck`, `dailyx_x_observation`,
`github_release_api_response`, `grok_x_observation_corrected_r2`,
`official_project_repo`, `official_publisher_page`,
`sol_discovery_working_record`, and `sol_working_set_observation`.
The post-Screening Supplement used the explicit first-party, repository,
research, conference, vulnerability, rights-authority, and government-mirror
values listed in the taxonomy above. No unknown W34 value was accepted through
lexical fallback.

The regression performed:

1. confirmed pending Architecture Review and zero Human records;
2. invalidated `ARCHITECTURE_REVIEW -> CANDIDATES_NORMALIZED` through the
   operator path;
3. validated 62 exact task-bound Supplement entries, with all Raw bodies
   non-zero and 60 unique Raw SHA-256 values;
4. generated and accepted a new Evidence run and Edition View while retaining
   the historical accepted directories;
5. resolved active Evidence/View only from the passed checkpoint provenance;
6. validated Materiality, Completeness, Selection, and Architecture; and
7. ended at `ARCHITECTURE_ESTABLISHED`,
   `next_action = ARCHITECTURE_REVIEW`,
   `terminal_reason = HUMAN_GATE_REACHED`, with both Human Gates pending and
   Human provenance null.

Fresh acceptance artifacts and hashes:

- Evidence acceptance:
  `evidence/v2/accepted/3ccf9ccfb318bcd7c5115166c20f7cf35171e0b8f833df94d9e652c25d6a6281/evidence-accepted.json`
  SHA-256 `bd0c94aea7b00460855432d240c2676decd7136b585921b2133d53f12738c9ce`
- Edition View acceptance:
  `evidence/v2/views/accepted/9f65aa5a8a032824566f4eabff6dab8ffb74beef6394d84a796bbeccbfedce97/edition-views-accepted.json`
  SHA-256 `81ee1d4b4eaa5a6b70ca5812d9de7e8b08c688a630694d61b752b6319f5f3f77`

Evidence counts were `VERIFIED 32 / PARTIAL 27 / NEEDS_MORE 14 / REJECTED 7`.
Edition View counts were `MATERIAL 1 / CONTEXT 31 / HOLD 41 /
NON_MATERIAL 7`. Completeness remained `LIMITED`. Selection was
`SELECTED 1 / HOLD 64 / INSPECT 15`; the mechanism regression produced one
Architecture package titled `Verified developer-tooling change`.

The W34 operator invalidation record validated successfully, with gate
`ARCHITECTURE_REVIEW` and boundary `CANDIDATES_NORMALIZED`. Human records
created: `0`.

## Validation status

- Focused Evidence/source-authority tests: `12/12 PASS`.
- Affected Core regression: `311 tests, 6 skipped — PASS`.
- Syntax/compile and `git diff --check`: PASS, with only the pre-existing
  untouched `SyntaxWarning` in `scripts/normalize_special_legacy_partial_enums.py`.
- Full Python suite and fresh ending-head CI are recorded in the completion
  handoff after the normal branch commit/push.

Ending branch SHA and fresh workflow run IDs are intentionally supplied by the
completion handoff, because they are properties of the final pushed commit.

