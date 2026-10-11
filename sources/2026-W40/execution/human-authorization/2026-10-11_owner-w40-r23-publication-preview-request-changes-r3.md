# W40 r23 — Human Publication Preview REQUEST_CHANGES authorization (revision 3, layout only)

Status: `HUMAN_OWNER_EXPLICIT_REQUEST_CHANGES / CORE_V2_FROZEN / LAYOUT_ONLY_REPAIR_AUTHORIZED`
Human decision: **2026-10-11 JST**, precise in-chat timestamp not asserted.
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W40-v2-work`
Owner-reviewed r23 candidate content commit: `fd679a3ec007a0d1cf861ee672caa71dff759f56`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, Tree `fe3f07c653f255f67087b4b46d006f8943df7115`

## Human decision (faithful transcription)

Sol asked:

> 上記条件で、W40 r23 Publication Previewの`REQUEST_CHANGES`（revision 3）をHuman Ownerとして承認しますか？

The Human Owner answered:

> 承認します

This is an **explicit, independent Human Owner PUBLICATION_PREVIEW `REQUEST_CHANGES` (expected revision 3)** for the existing r23 Publication Candidate — not a restatement of any independent auditor's judgment. This markdown is source evidence for the official Human Gate operation, not a forged official Gate record. The exact time of the in-chat message is unknown; use the real execution UTC timestamp when invoking the Core CLI.

## Authorized scope

| Field | Authorized value |
|---|---|
| Gate | `PUBLICATION_PREVIEW` |
| Decision | `REQUEST_CHANGES` |
| Expected revision | `3` |
| Regeneration boundary | `DRAFT_COMPLETE` |
| Reviewed commit | `fd679a3ec007a0d1cf861ee672caa71dff759f56` |
| Reviewed candidate | r23 Publication Candidate (`4be71507…`, PDF `82f7af37…` 466496B/14pp) |
| Scope | PDF p.3, p.4, p.9 layout defects only (LAYOUT-01/02/03) |
| Architecture approval | Preserve (r1 APPROVED) |
| Prior reviews | Preserve r1, r2 records |
| Core v2 | Immutable; no Draft/Synthesis/Evidence/Selection/Architecture/content changes |

No Preview approval, Freeze, Release, merge, new branch, or further rewrite cycle is authorized.

Execution: Muse must use unchanged Core `scripts/survey_human_gate_v2.py request-publication-preview-revision` and verify output.
