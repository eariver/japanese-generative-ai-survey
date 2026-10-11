# W40 r22 — authoritative supersession and cleanup report (Human Preview r1 revision)

Status: `SUPERSESSION_RECORD / HUMAN_REVISION_R1 / NO_CORE_CHANGE`
Date: 2026-10-11 JST
Authority: Owner `PUBLICATION_PREVIEW / REQUEST_CHANGES` r1 (`gates/reviews/publication-r1.json`, boundary `ARCHITECTURE_ESTABLISHED`, Architecture approval preserved)
Scope: working-tree singleton replacement at identical canonical paths. NO Git history rewrite, no force, no Core/schema/config/workflow change.

## Retained history (old bytes reachable, never rewritten)

- r21 canonical: commits `832808af9` (candidate), `6f02481a0` (QA+PDF), back to `98b020d8` (r22 start).
- r22 gate commit `4307b354` records the official revision (old State/checkpoint bytes in ancestors).
- r22 base for old-byte reads below: `4307b3543048a510acf0e5dccaadfa6a0d8eddaa` (== `98b020d8` content for all listed paths).

## Old → new SHA-256 (first 16 hex; full values in stage reports)

| Path | r21 (old) | r22 (new) |
|---|---|---|
| draft P1..P8 results | 8f507ce3 / 4363ff50 / 85c75ba4 / 84c2f3af / 4406a9db / 574614d5 / 7858c503 / 7b00e3cf / c51a9dcc | 13d98eaa / 9fb19052 / 85fc2a79 / fa22ed60 / b94cb88e / 67962201 / 3b9c5ed9 / 8437d99e / 59d148f3 |
| profile-synthesis-result | b09a99ef | 38fca983 |
| reader-manuscript | b7720c55 | 08247734 |
| quality bundle | 081e170c | f9a4e353 |
| semantic review | d1f6f777 | 11777ac2 |
| visual review | c714d770 | 04db6ebd |
| surface gate | 291fff03 | 7b62f277 |
| publication candidate | 157c4644 | 2cb17796 |
| main.pdf (369980B/12pp) | f93d15f8 | c0b2fe1e (451313B/14pp) |

Unchanged (pinned, NOT superseded): draft-package ×9 (re-derived byte-identical), candidate-matrix, candidate-selection, architecture, review summary/attention, accepted Evidence/Views/Materiality/Completeness, Selection checkpoint, Architecture approval, r21 archive input (r22 input archived at NEW path `interactive-drafting-synthesis-input-r22.json`).

## Regeneration method (all unchanged Core, all validators PASS)

1. Official `request-publication-preview-revision` (Human, r1, ARCHITECTURE_ESTABLISHED) — only Core-side deletions are the 3 downstream checkpoints.
2. Draft results rebuilt from r22 prose specs via unchanged runner `_draft_result` + `validate_draft_result` (9/9 PASS); packages asserted byte-identical, kept.
3. Synthesis input rebuilt (binds new results), synthesis result validated; TeX rewritten from new prose (not compressed derivative); CI PDF built twice with log gate clean; visual QA 14/14 pages.
4. Manuscript/surface/bundle/reviews/gate/candidate rebuilt via unchanged builders; three official stage validations + checkpoints + advances (DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE).
5. `build_candidate` divergent-overwrite refusal honored: old file removed from worktree first, then fresh builder write (old bytes in Git ancestors per table above).

## Residual constraints

- HOLDs (AstaBrief/AutoSynthData + 2 carryovers) and REJECTs stay outside chapters; Core #562 separate.
- Accepted Evidence/Architecture bytes keep the old VSS post-window inference; reader prose uses the bounded in-window correction note (packet erratum).
- Legacy `validate-state` exit 1 (pre-existing agent-first/legacy semantics; governing agent-first PASS).
