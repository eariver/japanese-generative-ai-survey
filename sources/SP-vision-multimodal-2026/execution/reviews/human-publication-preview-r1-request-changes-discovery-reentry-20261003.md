# Human Decision Record — Publication Preview r1 REQUEST_CHANGES (cross-gate re-entry to DISCOVERY_COLLECTED)

- Issue / edition: `SP-vision-multimodal-2026` (TS-003)
- Gate: `PUBLICATION_PREVIEW`, revision: `1` (first Publication Preview review; no prior publication-rN exists)
- Decision: `REQUEST_CHANGES` with upstream regeneration boundary `DISCOVERY_COLLECTED`
- Reviewed branch: `special/vision-multimodal-2026-work`
- Reviewed commit: `e4c1422279852a4cb41db3d455663216b3bd08e4` (exact restored review surface: 38pp Phase-2 Candidate + checkpoint-bound PDF)
- Reviewed by: `Human Owner`
- Human decision timestamp: `2026-10-03T11:46:50Z` (decision received 2026-10-03; UTC)
- Core v2 Freeze: remains in force (no Core change authorized)

## Actual Human decision (verbatim)

Reviewed Commit:

`e4c1422279852a4cb41db3d455663216b3bd08e4`

Decision:

`REQUEST_CHANGES`

Regeneration boundary:

`DISCOVERY_COLLECTED`

Requested change:

VM-D112 Agentic Video Understandingを、TS-003 edition-localの正式なDiscovery / Screening / Evidence pipelineへ投入し、Materiality / Completeness / Selection / Architectureまで再生成・rebindしてください。

このre-entryはVM-D112の正式採否を行うためのbounded re-entryです。

既存のaccepted technical scope、およびEvidence r8で修復済みのVM-D084 / VM-D106 / VM-D091 / VM-D010については、formal regenerationに必要なdeterministic rebindingを除いて後退させないでください。

**Survey Production Core v2のFreezeは解除しません。**

Shared Core、Core scripts、schemas、config、validators、contractsは変更しないでください。Coreの制約を変更・迂回してはなりません。

VM-D112を正式に処理した後、fresh Architectureを生成し、**fresh Human Architecture Reviewで停止**してください。

## Scope clarification (faithful record, no new decision inferred)

This decision is not an approval of any of the following, and none is claimed here:

- Publication Preview APPROVED
- Architecture APPROVED
- Freeze
- Release
- reader r15 generation
- TeX/PDF regeneration
- Core v2 Freeze release

## Provenance

- This record is the `review_reference` for operator request `ts003-pubr1-reqchanges-discovery-20261003`.
- Created edition-locally by the Work execution role as a faithful transcription of the already-given Human decision quoted above. No decision was inferred, and no additional approval was requested.
- Note: a prior turn's preparatory request (`ts003-vm-d112-cross-gate-reentry-20261003`) failed before any gate record was written (bridge rejected on pre-existing checkpoint drift, since restored). Its files remain historical records of that failed attempt. This record and its request are the canonical materialization of the now-explicit Human decision against the exact restored review surface.
