# W40 r21/r22 — VSS Blueprint 3.3 in-window event chronology correction

Status: `EDITORIAL_FACTUAL_CORRECTION_NOTE / NO_APPROVED_ARCHITECTURE_MUTATION / NO_NEW_CANDIDATE`
Date: 2026-10-11 JST
Affected Candidate: `candidate:2026-W40:055bb2f3f5be21c2`, NVIDIA VSS Blueprint 3.3, P7.

## Observed contradiction

Approved `sources/2026-W40/architecture-v2.json` P7 `must_cover_requirements[1]` ends with `Oct 1 session post-window`; likewise accepted Evidence Task `sources/2026-W40/evidence/v2/accepted/0a62346f0729e768d1b67305dd96e0e99224326c862831abe79e43ced4875e07/results/task-055bb2f3f5be21c2662f.json` claim-3 says `Oct 1 9am PT live session is post-window`.

W40 ordinary cutoff is **October 2, 2026, 18:00 America/New_York = October 2, 2026, 22:00 UTC**. In October, Pacific Daylight Time is UTC-7; NVIDIA's October 1 09:00 PDT = **October 1, 2026, 16:00 UTC**, **inside**, not after, the W40 collection window.

## New first-party verification (current public page independently retrieved)

- Official NVIDIA Developer Forums original announcement authored `amelian`, posted September 29, 2026 19:00 forum time: `https://forums.developer.nvidia.com/t/livestream-10-1-at-9-00-am-pt-build-visual-ai-agents-from-a-prompt-with-nvidia-cosmos-and-vss-3-3/384706`
- NVIDIA Developer Community official event listing: `https://developer.nvidia.com/community`, Thursday October 1, 09:00–10:00 PDT, "Build Visual AI Agents From a Prompt With NVIDIA Cosmos and VSS 3.3".
- These establish **advertised event scheduling**, not that the livestream actually took place, nor that post-event benchmark or video content was independently verified.

## Decision and limits

Human Owner has authorized a Draft rewrite preserving the approved Architecture; do not silently edit the already Human-approved P7 must-cover and accepted r8 Evidence. For new reader-facing prose, make the **correct factually verified** bounded statement: `NVIDIAは10月1日9:00 PDTのライブ配信を事前告知していた。この日時はW40の対象期間内である。配信の実施内容・追加成果は今回独立検証していない。` Do not label the event `post-cutoff`. Preserve evidence integrity by citing this exact edition-local correction along with the original official first-party source; explicitly disclose that the previous downstream classification was erroneous.

This is an additive editorial correction note, like an authority-bound erratum, **not a machine rewrite of canonical Evidence or Architecture**. The correction supersedes **only** the incorrect temporal inference, not the verified release day, product, vendor-demo metrics, limitations, or other P7 must-cover items.

If unchanged Core validators or Publication Gate require reproducing the invalid original post-window statement as a must-cover fact, fail closed, stop and report to Sol/Owner. A deeper Human-authorized `PUBLICATION_PREVIEW` revision with a pre-Architecture boundary is necessary for any change to already approved Architecture. Do not use unofficial operator pending-Gate invalidation.
