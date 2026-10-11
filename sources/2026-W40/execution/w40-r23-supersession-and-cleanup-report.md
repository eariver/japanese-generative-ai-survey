# W40 r23 — authoritative supersession and cleanup report (Human Preview r2 revision)

Status: `SUPERSESSION_RECORD / HUMAN_REVISION_R2 / NO_CORE_CHANGE`
Date: 2026-10-11 JST
Authority: Owner `PUBLICATION_PREVIEW / REQUEST_CHANGES` r2 (`gates/reviews/publication-r2.json`, boundary `ARCHITECTURE_ESTABLISHED`, Architecture approval preserved)
Scope: working-tree singleton replacement at identical canonical paths. NO Git history rewrite, no force, no Core/schema/config/workflow change.

## Retained history

- r22 canonical: `ae22a5837` (candidate `2cb17796…`, PDF `c0b2fe1e…` 451313B/14pp); Sol review `ee56893d`; r23 gate `88a7a2000`.
- Old bytes below read at base `88a7a200001c4e84b0156f2e609ea38ac8216a9b`.

## Old → new SHA-256 (first 16 hex)

| Path | r22 (old) | r23 (new) |
|---|---|---|
| draft P1/P2/P5/P6a/P6b/P7/P8 results | (7 files changed, P3/P4 untouched) | re-validated via unchanged `validate_draft_result` 7/7 |
| profile-synthesis-input | rebound (binds new result SHAs) | payload text identical |
| profile-synthesis-result | rebound (new input SHA) | payload text identical |
| reader-manuscript | — | rebuilt (31 must-cover map, new TeX SHAs) |
| publication-candidate | `2cb17796ee620c0d` | `4be71507d2e7eba8` |
| main.pdf (451313B/14pp) | `c0b2fe1e4517bec8` | `82f7af378d614a21` (466496B/14pp) |

Unchanged (pinned): draft-package ×9 (re-derived identical, kept), candidate-matrix/selection, architecture/summary/attention, accepted Evidence/Views/Materiality/Completeness, Selection checkpoint, Architecture approval, r22 archives (r23 input NOT archived as file — edits applied via asserted block-replacement script `/tmp/opencode/w40-r23/edit_draft.py`; old bytes in Git ancestors per table).

## Regeneration method (unchanged Core, all validators PASS)

1. Official `request-publication-preview-revision` r2 (Human, ARCHITECTURE_ESTABLISHED) — Core-side deletions are the 3 downstream checkpoints only.
2. Draft blocks rewritten via asserted old→new replacement + `validate_draft_result`; packages asserted byte-identical, kept.
3. Synthesis input rebuilt, result re-validated (payload identical); TeX rewritten from new prose; CI PDF built 3× (1 log-gate failure on Overfull hbox → SHA shortening + Eq.3 display fix → success); visual QA 14/14 pages at 150dpi.
4. Manuscript/surface/bundle/reviews/gate/candidate rebuilt via unchanged builders (surface input now sourced from CURRENT draft results, not the r22 archive); three official stage validations + checkpoints + advances.
5. `build_candidate` divergent-refusal honored via remove-then-build.

## Residual constraints

- HOLDs/REJECTs outside chapters; Core #562 separate; VSS delivery unverified; legacy `validate-state` exit 1 (pre-existing semantics; governing agent-first PASS).
