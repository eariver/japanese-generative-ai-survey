# W40 r21 — Human Publication Preview REQUEST_CHANGES authorization

Status: `HUMAN_OWNER_EXPLICIT_REQUEST_CHANGES / CORE_V2_FROZEN / DRAFT_REWRITE_AUTHORIZED`
Human decision: **2026-10-11 JST**, precise in-chat timestamp not asserted.
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W40-v2-work`
Owner-reviewed r21 candidate content commit: `832808af95df29547d7050452fdac7bb3df80f2e`
Existing branch at decision: `7ca317615076d287945b56c09184cb7cab4609cd`, Tree `bc41ecaca42ae8371bf55bc3e35b072dec52b8e6`.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, Tree `fe3f07c653f255f67087b4b46d006f8943df7115`.

## Human decision (verbatim, this conversation)

Following Sol r21 editorial audit, an independently performed read-only Chat Sol High audit `SUBSTANTIVE_REWRITE_REQUIRED`, the Owner was asked whether to formally request changes and return to the approved Architecture for Draft regeneration. The Owner answered:

> はい、推奨案で進めましょう。私からの要望は Core v2 を不変としてWeekly号を完成させることです。

This is an **explicit Human Owner PUBLICATION_PREVIEW `REQUEST_CHANGES`** for the existing r21 Publication Candidate, authorizing a new Draft from the already approved Architecture, preserving the approved 28-item Selection and **not modifying Core v2**. This markdown is source evidence for the official Human Gate operation, not a forged official Gate record. The exact time of the in-chat message is unknown; use the real execution UTC timestamp when invoking the Core CLI.

## Human-required changes

1. Substantially rewrite, not lightly proofread, the nine editorial Package Drafts **P1 P2 P3 P4 P5 P6a P6b P7 P8**, plus profile synthesis, frontmatter and Week in Review. Replace unnatural calques/metaphors with accurate and conventional Japanese and preserve technical English when needed. No page cap; do not pad.
2. Demonstrate actual reader-facing fulfilment of each of **31 approved must-cover requirements** using individual paragraph, formula, comparison table or definition, not a file-path-only `FULFILLED` checkbox. Restore explanatory mechanism, denominators, method, baselines, evaluation, licensing, source attribution, limits and why technically significant.
3. P1 all vendor price cards; P2 license/variant/benchmark comparison plus actual ELYZA SHAs; P3 mechanism and 9/29 vs 10/1 chronology; P4 computer use approval/sign-in and product constraints; P5 five independent safety topics with functioning/threat/eval; P6a ContextLM Eq3/5/6, GRPO vs fixed-weight skill, Olmo MoE expert routing/grouped GEMM/MXFP8 and separated experiments/negatives; P6b definitions and measurement protocol/roofline/reproducibility; P7 FLUX pricing tied to resolution, VSS measurements, ASR WER context, Relay/Ross bounds; P8 concise natural digest.
4. Preserve 28 Selected (20 PRIMARY/8 SUPPORTING), 4 HOLD/3 REJECT, 9 groups, **113 original Candidate-boundary relations / 105 package-level entries / 97 globally distinct Boundary strings**, and the specific approved r20 Architecture Human review authority. Core #562 and material HOLD candidates remain separate; no companion edition.
5. Correct reader-facing VSS 3.3 **Oct 1 9am PDT livestream scheduled INSIDE W40 window**, despite inherited source/Evidence/Architecture's incorrect `post-window` classification. Official NVIDIA forum announcement September 29: `https://forums.developer.nvidia.com/t/livestream-10-1-at-9-00-am-pt-build-visual-ai-agents-from-a-prompt-with-nvidia-cosmos-and-vss-3-3/384706`; its contemporaneous announcement identifies an *upcoming* Oct 1 session, **not confirmed post-event results**. Preserve approved Architecture bytes and original Evidence as provenance, use the dedicated editorial correction note and explicitly mark the false inherited clause as superseded for reader prose; do not pretend the Architecture originally said the correct thing. If reviewed Core cannot legally support this limited post-Architecture erratum, **STOP** and report the need for a separate Owner-authorized earlier regeneration boundary instead of silently changing Architecture.
6. Recheck PDF source, exact bytes, pagination and table/TeX layout. Prior canonical r21 PDF is SHA-256 `f93d15f838cddf9489cc7ed6e73f3eb2cbe551044ac84a45cc41441fabf202ab`, **369,980 bytes**, 12 pages in recorded QA; worker reports claiming 370,741 bytes are stale.
7. All new machine gates/QA must accurately represent the semantics of the actual rewritten text; do not repeat previous false-positive `31/31 FULFILLED` and Semantic `PASS` without granular review.

## Execution authority and exact stopping boundary

Human expressly requests completion of **the Weekly issue**, not bypassing Human Publication Preview or authorizing Freeze/Release. The approved action is:

`PUBLICATION_PREVIEW / REQUEST_CHANGES / revision 1 / regeneration_boundary ARCHITECTURE_ESTABLISHED`, provided no previous preview review exists, through unchanged Core `scripts/survey_human_gate_v2.py request-publication-preview-revision`. This preserves Architecture APPROVED in Core, resets downstream Draft/Validation, and should be a separate formal normal FF commit before content changes. Verify all state and authority bytes first.

Then production proceeds through formal Draft, validation, candidate steps and terminates at **fresh Human Publication Preview pending** for Sol/Owner PDF review. Any required deviation upstream of Architecture, Core/schema/config bugfix, new branch, force, Freeze/Release, or Human Preview approval requires separate explicit authority. Core v2 is strictly immutable throughout.

Execution contract: `execution/instructions/2026-10-11_muse-w40-r22-authorized-human-preview-draft-rewrite.md`. The docs-only Sol commit adding this evidence does **NOT** change `production-state.json` or record the actual Human Gate; Muse must use the Core CLI and verify output.
