# W42 Sol independent r11 Japanese Draft revision audit — CONDITIONAL PASS / R12 CORRECTION REQUIRED

Date: 2026-10-18 JST  
Reviewed exact Muse r11 HEAD: `7de15dc5f4288842fbda00d040e8e413ff0f8a63`  
Branch: `weekly/2026-W42-v2-work`  
Reviewed main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` unchanged  
Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` unchanged

**Disposition:** `SOL_R11_EDITORIAL_SUBSTANTIAL_IMPROVEMENT / CONDITIONAL_PASS_WITH_PRE_TEX_REPAIRS / NO_CANONICAL_DRAFT_SUBSTITUTION / NO_VALIDATED_DRAFT_OR_PUBLICATION_GATE_APPROVAL`.

## A. Machine integrity and fixed architecture PASS

Independent remote diff from r11 starting HEAD `d7af8e9bc0289440c0fd2c50eeb2592d5f6794e4` has one normal commit, 18 changed files: 17 newly added edition-local r11 proposal/review artifacts and edition index update. No shared `scripts/`, `schemas/`, `config/`, `.github/`, canonical Draft/State/Checkpoint/Gate/Architecture/Evidence replacements. Actual State remained `DRAFT_COMPLETE` with real Human Architecture r1 `approved`, Publication Preview `pending`, validation pending. Canonical r10 Draft SHA remains the accepted Draft; r11 proposals are **NOT_CANONICAL**.

Muse reports unchanged frozen `draft-check` 7/7 PASS, `synthesis-check` PASS; Sol inspected actual proposed structures/claim refs/source ledger, but independent CLI execution was not available to this connected GitHub review. The exact formal stage acceptance is NOT repeated or superseded by r11.

## B. Independent substantive revisions

Independently parsed all seven proposed `draft-result-r11.PROPOSED.json` files, 82 PARAGRAPH, seven TABLE, seven NOTE, seven HEADING, seven still-valid machine-only CLAIM_BOUNDARY. **17,004 characters of PARAGRAPH body** (compared to 21,418 in r10); reader-visible paragraphs+tables/notes/headings are approximately 20k. Per paragraph counts/chars: P1 13/2,873, P2 12/2,306, P3 13/3,047, P4 13/2,682, P5 11/2,062, P6 10/2,106, P7 10/1,928.

Real improvement:
1. P3 `q3-n1` correctly says **Apache License 2.0 IS OSI-approved** while differentiating actual model license coverage, Beam read LICENSE file, Granite/MiniCPM tag-only evidence, and custom license status. Official source: https://opensource.org/license/apache-2.0.
2. Revised reader preview has seven chapters, **zero visible CLAIM_BOUNDARY** and no raw internal `No r7 finding` / `AUTHORITY_CONSUMED` notes; the seven machine boundary records remain in the proposed Core-shaped results. Audited structure 103 reader blocks (82 PARAGRAPH + 7 TABLE + 7 NOTE + 7 HEADING).
3. The most obvious editorial instruction sentences and duplicate restatements were removed. P5 table/headline now both define four **局面** instead of a 3-vs-4 conflict. P7 adds an explicit comparison TABLE and names **Z.ai, not Vals**, as author of the selected chart omitting six higher-ranked candidates. P4 Hangul and P5 simplified-Chinese errors no longer present in visible texts.
4. P6 body mostly describes author research results and numbers instead of claiming the editorial team archived the actual full PDFs. The 91 W42 r8 supplements remain short, derived notes; this is not a change in original source archive status.
5. Proposed r11 `citation-repair-ledger-r11.json` maps all 96 factual reader blocks (82+7+7), 89 VENDOR_REPORTED and 7 MIXED independent-anchored. There are 59 distinct string URL values in its `narrowed_source_urls` when including seven misclassified internal paths; unlike the previous report, this is **NOT** yet a clean exact-external-URL-only crosswalk.

## C. Three remaining mandatory publication-content repairs (R12)

**R11-F01 — License tier contradiction; cannot print as written.**
- `P2 q2-07`: `「条文全文が確認できる確認水準」` for **LFM Open License v1.0**. Accepted r6 research records **3 operative-terms-only cases** including LFM, not full original LICENSE file inspection. This paragraph materially upgrades the original evidence class without new source bytes. Correct to `発行者公開の主要条項を確認した水準。対象モデルのLICENSE原文ファイル・個別weightは未確認` (or more precise direct evidence if genuinely obtained, with real raw bytes/URL).
- `P3 q3-03`: `「出力制限・収益上限・表示義務がない」` juxtaposes with its own P3 comparison table's Apache notice/attribution/modified-state rules. Distinguish **no custom mandatory 'Built-with Model' promotional badge** from ordinary Apache 2.0 license/NOTICE/copyright and modified-file obligations. The paragraph as written plausibly implies no attribution duties. Official OSI Apache text §4 explicitly requires attribution/notice preservation and license copy under the conditions. P3 `q3-t1` and `q3-n1` already partially correct: align paragraph and table exactly.
- P3 `q3-02/q3-t1` and P2 model-specific license status must distinguish source-publisher operative terms from the actual artifact-wide model/third-party applicability. Never claim independent legal review; no automatic OSI approval for a bespoke model license.

**R11-F02 — Seven bad 'source URL' entries still point to unrelated internal bundle.**
Independently parsed the 96 r11 citation rows and checked exact W42 r6 bundle body. Seven rows erroneously include the **local file path**
`sources/2026-W42/collectors/evidence/runs/20261017T100000Z-muse-r6/ev-bundle-09-ocp-changelog-minecraft-r6.md` inside the field **`narrowed_source_urls`**:
- P4 `q4-07` (AI Scan) and `q4-08` (AutoFix/AI Scan).
- P5 `q5-06`, `q5-08`, `q5-10` (METR/evaluation policy).
- P6 `q6-06`, `q6-10` (Rosalind).
The referenced r6 bundle is explicitly titled **OCP/docs, Claude changelog, Minecraft follow-up**; exact term search shows **0 METR, 0 Rosalind, 0 AI Scan, 0 Autofix**. This is a definite semantic provenance error, not just a non-http syntax problem. Remove unrelated bundle from each; bind each clause to the existing precise official URL(s) actually supporting it, or classify as unsupported. Separate internal worklog links, if still useful, into a clearly named **internal_provenance_paths** field that must not be mistaken for external source links, and only when genuinely relevant. Underlying ACCEPTED r10 Evidence and official Stage stay untouched.

**R11-F03 — Page plan and substantive density not yet demonstrated.**
The approved Architecture plans 26.5pp article body, target **28 pages**, max **30**, but r11 has **17,004 paragraph characters** across seven sections, plus seven substantive tables/notes (~20k reader-visible characters total). Muse's own estimation in `publication-adoption-feasibility-r11.md` is **18–22 page-equivalents** before introductory/bibliography matter; this is an estimate, not actual TeX pagination. P5 has 2,062 paragraph chars and P7 1,928 despite 3/3.5 allocated pages. The user specifically objected to thin PDFs and requested deep technical coverage rather than a page-count-driven outline. **Do not stretch with margins/whitespace, oversized tables or generic 'one more paragraph' padding.** Either:
(a) add genuine source-backed methodological explanations/bench denominators/limitations/unique technical comparisons in evidence-rich chapters P2/P3/P4/P5/P6/P7, or
(b) produce an honest 18–22page TeX baseline and justify changing **only a proposed layout target**; any material Architecture page-plan change (particularly max 30/7 packages) needs renewed appropriate Sol/Human review, not a silent revision.
The proposed volume alone cannot prove or disprove completeness until a real layout proof exists. A bounded TeX/PDF **pre-publication preview** may be authorized after F01/F02 and independent manuscript fidelity QA, stopping before any formal publication-stage transition.

## D. Smaller editorial refinements

- A few formulaic repetitive 'conditions are the point' closings persist (P2 `q2-10`, P5 `q5-07/q5-08`, P7 `q7-07`). Not automatic blockers, but actual methods and causal significance should outweigh commentary about writing.
- Some `qN-10` / `qN-11` end-of-array after `qN-12/13` remain due closing-order IDs; IDs are opaque, but verify reader flow, not numerical order.
- P3 proposed headline and in-chapter HEADING exactly repeat; de-duplicate when typesetting if style permits.
- R11 may refer to an official MetR/Anthropic evaluators page, but even an official source does not retroactively prove METR independently published results. The editorial scope remains program/policy only.
- The citation ledger's all-candidate Task `evidence_refs` remain broad; publication TeX requires exact paragraph/table bibliographic keys resolved against real URLs. Vendor and independent Vals study are separate sources. No EXO scores, unsupported AA or X-only accusations.

## E. Frozen Core adoption route: genuinely possible but unproven

Independently inspected exact frozen:
- `scripts/survey_stage_validation_v2.py`: DRAFT_COMPLETE→VALIDATED_DRAFT requires `reader-manuscript`, `validated-source` (main.tex), `publication-pdf`, `quality-regression-bundle`, `semantic-review`, `visual-review`, `reader-surface-gate`. The stage's `_merge_artifacts` rejects replacement of accepted upstream Draft artifact paths.
- `scripts/survey_reader_publication_v2.py:build_manuscript_manifest`: binds Profile, Architecture, Architecture Approval, canonical `surveys/weekly/2026-W42/main.tex` bytes, support files, must-cover, reader requirements; it does NOT bind the r10 Draft paragraph-text SHA.
- Frozen `survey_weekly_semantic_publication_v2.py` auto renderer requires canonical r10 `draft-result.json` and exact text of r10 semantic archive and *also* expects State `next_action=stage:semantic-publication-validation`, whereas current W42 stage plan says `stage:reader-publication-validation`. Hence DO NOT use a shim to force the auto renderer onto r11 content or falsely claim it passed. Generic canonical authoring may use revised r11 content as **editorial input** without replacing accepted machine Draft, but all mandatory reader stage gates and PDF fidelity still need actual execution.
- This suggests a lawful **separate authoring route** to TeX from r11 after F01/F02, but it is not an independently proven 100% passing frozen Core publication pipeline. No stage advance, no Gate or PDF authority yet.

## F. Sol decision and next bounded task

**r11 editorial improvement passes at a conditional level, but pre-publication textual integrity is NOT fully passed.** Authorize **r12 targeted amendment + layout proof** without touching Core or accepted Draft. Complete exact F01, F02, plus meaningful density evaluation/F03 and TeX feasibility, then stop for independent Sol reader/PDF review. It is permissible to build **staged, clearly PREVIEW/NOT_APPROVED TeX/PDF** only after F01/F02 pass and if no canonical gate/checkpoint/State overwrite. Do not advance `VALIDATED_DRAFT` or record Publication Preview approval automatically.

Full Human Architecture r1 remains APPROVED. No reason to repeat full Discovery/Evidence/Selection/Architecture or to obtain a second Human Architecture approval for citation-language fixes without scope change.
