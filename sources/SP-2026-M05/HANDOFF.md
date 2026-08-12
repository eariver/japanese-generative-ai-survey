# SP-2026-M05 HANDOFF

Status: `RELEASE_CANDIDATE`

## Gates

- Raw Sources Preserved: passed
- Candidate Inventory: passed
- Evidence Normalized: passed
- Candidate Selection: passed
- Issue Architecture: passed
- Article Draft: passed
- Claim & Chronology Validation: passed
- LaTeX Build: passed
- **Human Visual Review: pending**
- **Freeze: pending**

No Human Visual Review, Freeze, merge, publication, or release approval is inferred by this checkpoint.

## Granularity review

May was explicitly compared with the June and July Specials before Selection was advanced. The May proposal was retained rather than reduced: `FEATURE_CORE=3` plus `SECTION_CORE=12` gives 15 core Evidence items, while Supporting Evidence and Paper Watch are folded into thematic packages. This matches the June Special's editorial grain more closely than forcing May down to July's smaller Evidence count.

## Current revised Preview candidate

- Source version: `v0.12`
- Source manifest: `surveys/special/2026-M05/revisions/v0.12/source-manifest.json`
- Source manifest SHA-256: `a8cf95072e662b8a4fcf4d480b09bd711da444b0b02e25a9a044906f8a4de94d`
- Layout mode: `balanced-multicol-adaptive-spacing-with-may-chronology-review-repairs-seven-selective-tails`
- Build workflow run: `31552757234`
- Artifact ID: `9124899681`
- Artifact digest: `sha256:67b843fffbbc160f379eb2ef9859dffe817e097316f4b1beaba627ca7ddbca05`
- PDF page count: `33`
- PDF SHA-256: `23cf50e1ea0b8cbf7caa9451dea04764459c8768feaba478fd79e839dbfb6241`
- TeX log gate: clean (`[]`)
- Allowed page range: 32–40

## Pre-release review repairs

The revised Preview addresses review Issues #50, #54, and #55 before Human Visual Review.

- **#50 — Technical Notes language:** the SHA-bound Japanese reader-facing layer is applied to all 81 claim/limitation items, including `一次情報で確認できる事実`. Vendor/Project/Author attribution and evidence boundaries remain visible. Evidence cards and Draft Packages remain immutable.
- **#54 — reader-facing taxonomy:** raw/partially translated schema enums are not rendered as magazine labels. Theme-at-a-glance and detail cards use reader-facing labels, and the third-party evaluation playbook is rendered as `評価ガイダンス` rather than `安全性事象`. Validation rejects raw-enum re-exposure.
- **#55 — Technical Notes page continuations:** source heading + URL remain together, paragraph widow/orphan controls remain active, and only seven tails that actual renders showed could become URL-only or limitation/source-only continuations are grouped from final attributed claim through source. The other 19 cards remain normally breakable.

## Post-repair self-check

`pre-human-self-check-v0.12.json` records the completed self-check. All 33 pages were rendered and inspected after the final repair.

Explicitly rechecked boundaries include:
- p18 FlashInfer — source stays with the card;
- p21–23 Agent Safety — ClawTrojan and AgentREVEAL/Relevance tails are substantive and no URL-only tail remains;
- p25–26 Capability & Evaluation — discrete geometry and evaluation-playbook tails are coherent before Paper Watch;
- p27–29 Paper Watch — AgenticVBench, measurement-bias, and final Representation Forcing tails are coherent, and the final synthesis begins naturally on p29.

The final v0.12 inspection found no clipping, overlap, broken glyph, undefined citation/reference, overfull/underfull hbox, missing-character issue, isolated Claim Boundary page, accidental blank page, or Issue #40-style structural whitespace regression. Final bibliography whitespace is natural end-of-document whitespace.

Intermediate v0.6–v0.11 candidates were withheld from Human Visual Review when self-checks found remaining #55 tails, ineffective list-local guards, or the v0.8 global-grouping whitespace regression. They were not treated as approved candidates.

The next Human Gate is **Preview / Human Visual Review**. Freeze remains a later, separate Human Gate.
