# J-GAS W42 r30 — Sol independent Publication Readiness audit disposition

Date: 2026-10-20 JST
Status: `SOL_R30_REQUEST_CHANGES_PARTIAL_ADOPTION / PUBLICATION_PREVIEW_WITHHELD / R31_HUMAN_EXECUTION_AUTHORIZATION_PENDING`
Repository: `eariver/japanese-generative-ai-survey`; existing branch: `weekly/2026-W42-v2-work`
Fixed independent audit target: `b33098f32027d52a245fbbeb07586d52fa7ae6f0` / root Tree `a2ace998c38c94a3260371bbe8f8acd4511e6feb`.
Independent report: `20261020215244_SolReview.md`, archived in this commit at `sources/2026-W42/execution/reviews/independent-w42-r30-publication-readiness-REQUEST_CHANGES-20261020.md`; exact supplied SHA-256 `50fcb5cd97018137a01775004a7a659f8a08229b74d66298a80fdad79291a0ec`, 15258 bytes (UTF-8 BOM, CRLF). Reviewer verdict `REQUEST_CHANGES`.

## Editorial findings

- **F-B57 HIGH / ACCEPT, mandatory factual repair.** Direct GitHub commit verification: NVlabs/ASPIRE `7ba73d3bcac8f6b6d4a7d67ed4040988f768d282` ("Public release", 2026-08-21T19:53:37Z) vs `fa00f0ef2bc1d91d594b9aa502c22133c9f538f7` ("ASPIRE v1.0 release", 2026-10-16T03:57:48Z). r30 TeX Section 7 line 759 wrongly presents October 16 as initial repo publication. The week's new event is **v1.0**; background June paper and August repo existence should be distinguished. Correct the Section 7 deck, prose and Table T7 only, including dated X-post claim if the specific post/date cannot be independently shown.
- **F-OP01 HIGH / ACCEPT, genuine process-authority nonconformity.** r30 Bridge Stage transitions used local first-party CLI, not the expressly instructed trusted GitHub Actions operator workflow with request-only preflight. The machine Stage Validator/Checkpoint evidence exists, but workflow admission is **NOT** evidenced; do not retroactively relabel it compliant. A fresh governed revision and workflow-admitted re-advance is preferable to a blanket retrospective exception. Do not rewrite history or manually reset State.
- **B54 ranking / LOW DISCLOSURE.** Vals October 12 Updates supports `79件中7位`; current table/header denominators change as ranking grows. Preserve 79 and annotate as October 12 snapshot. No ranking re-estimate.
- **B54 duration / corrected audit interpretation.** Official Vals Harvey's Legal Agent Benchmark v1 `https://www.vals.ai/benchmarks/hlab-v1` explicitly lists GLM Legal `1h12m` for benchmark duration (=72 min). Keep original 72min; current model card `37m25s` is a different field. No unsupported-number removal.
- **B16 license, r30 21/21 renderer parity, 28/28 Selection ID crosswalk, prior Human Route A whitespace / ACCEPT as already sufficient.** Do not repeat r29 independent whole-document 21-page/110-cell audit, revive Architecture r1, inflate to 28pp, or rewrite Japanese for tone.

## Recovery principle (NOT an approval)

Current State `RELEASE_CANDIDATE / HUMAN_GATE_REACHED`, Preview pending, cannot be approved on the old erroneous PDF. No Human Publication Preview decision, Freeze or Release has been taken.

The User delegated **editorial disposition** of audit recommendations, not automatic consent for a formal Human Gate `REQUEST_CHANGES` mutation or an exception to the operator trust boundary. Seek one explicit Human authorization of an integrated, narrowly scoped correction. The state-pinned Core's `REQUEST_PUBLICATION_PREVIEW_REVISION` from pending `RELEASE_CANDIDATE` to regeneration boundary `DRAFT_COMPLETE` is a suitable first-party mechanism, with genuine Human decision metadata and history retained; requires independently validated operator transport. `operator pending-Gate invalidation` is NOT allowed at Publication Preview (empty allowed boundaries). `publication-surface-revalidation` requires `REVIEWED_CORE_CHANGE` in `VALIDATED_DRAFT`, not this editorial repair.

After authorized revision, surgically update current TeX/Reader/PDF and source-dependent canonical QA/semantic/visual/Reader-Surface/Candidate authorities with new hashes, focused independent delta audit, then use **real trusted workflow-admitted request-only commits** for both Stage transitions. Preserve historical r29/r30 bytes via prior Git commits, evidence reports unchanged, main/Frozen Core/Architecture r1 intact. Stop at newly reached Human Publication Preview, no Release.

Proposed contract: `sources/2026-W42/execution/instructions/2026-10-20_muse-w42-r31-factual-repair-and-governed-preview-recovery.PROPOSED.md`.

Terminal: `W42_SOL_R30_DISPOSITION_REQUEST_CHANGES / R31_INTEGRATED_FIX_PROPOSED / HUMAN_AUTHORIZATION_PENDING`.
