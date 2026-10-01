# TS-003 Sol Draft Review r1

Status: `SOL_DRAFT_REVIEW_R1 / REQUEST_CHANGES / READER_SURFACE_AND_PROSE_REPAIR`

Date: `2026-10-01 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed Draft authority commit:

`d1053e957d92cddd9d2759ec9713db59c66263ad`

Reviewed tree:

`d69fe46574d0d922e8a1e2c4c4a69e2719f4ddae`

Decision:

`REQUEST_CHANGES`

The deterministic Draft stage is valid and the approved Architecture/Evidence boundary is preserved, but Draft r1 is not editorially ready for reader-publication validation. The blocking defects are predominantly reader-surface defects that Core v2 does not currently detect.

## 1. What passed

- Human Architecture Review r2 is canonically recorded as APPROVED.
- Architecture r1 REQUEST_CHANGES history is preserved.
- Lifecycle advanced canonically to `DRAFT_COMPLETE`; draft checkpoint passed.
- 16 Draft Package / Draft Result pairs and profile synthesis exist.
- Architecture, Selection, Materiality, Completeness, Evidence r5 and Views were not changed.
- G01-G06 and the five PARTIAL Evidence limitations remain represented.
- main and frozen Production Core are unchanged.
- P07B/P09/P15 follow the intended thematic grouping rather than a simple one-paper-one-paragraph catalogue.
- The terminology preflight correctly rejects many over-translated kanji forms.
- The Worker detected and repaired several obvious lexical defects before terminalization.

These passes do not override the findings below.

## 2. Blocking finding F1 — systemic repetition and padding

Draft r1 treats the Architecture page allocation too much like a character quota. This produces repeated sentences, repeated conclusions and semantically empty restatement.

Independent scan of reader-facing non-CLAIM_BOUNDARY prose found:

- 16 packages total;
- 135 repeated-sentence occurrences across the volume;
- P15 alone: 555 sentences / about 13.7k reader characters;
- P15 alone: 93 duplicate-sentence occurrences across 91 distinct repeated sentences.

Examples in P15 include exact repetitions such as:

- `語らないものを見積もってはならない。`
- `届かないことをもって、どちらかを退けることもできない。`

The problem is broader than exact duplicates. Many paragraphs repeat the same proposition several times with small wording changes.

Architecture page budgets are editorial allocation targets, not filler quotas. Semantic depth must come from distinct supported mechanisms, transitions, limitations and comparisons. Repetition must not be used to reach an estimated page count.

## 3. Blocking finding F2 — unnatural rhetorical substitution for technical Japanese

The Human specifically requested protection against Core-blind Japanese reader-surface defects. Draft r1 avoids some excessive kanji translation but replaces it with another systematic defect: repeated metaphorical or literary paraphrases that are unnatural in a technical survey.

Examples include recurring use of:

- `網` for neural network;
- `処方` for recipe/method;
- `運ぶ` for carrying a claim, limitation or representation between sections;
- `構え` as a generic substitute for architecture/method/stance;
- `証し` for evidence/support;
- `躾` for methodological discipline;
- `棚` for evidentiary categories;
- `務め` / `仕事` as rhetorical closing filler;
- `凱歌`, `束ねの妙` and similar literary phrasing.

The independent scan found in P15 alone:

- `躾`: 29
- `構え`: 28
- `証し`: 33
- `束ね`: 17
- `棚`: 10
- `仕事`: 22
- `務め`: 17

This is not a preference for formal vs casual Japanese. It materially harms precision and makes the text read as generated rhetorical prose rather than a technical survey.

Use established technical vocabulary directly: network/CNN, method, training recipe, evidence/root basis, limitation, validation, attribution, architecture, deployment, etc., according to the edition terminology map.

## 4. Blocking finding F3 — excessive restatement weakens information density

Several long blocks contain a sound initial technical explanation followed by many short restatements that add no new supported proposition.

P01 and especially P15 show this pattern clearly. Examples include repeated chains of:

- `〜ことが、〜になる。`
- `〜してはならない。`
- `〜を守る。`
- `〜の条件になる。`
- `〜の務めだ。`

This defeats the purpose of the Architecture depth classes. FULL_MECHANISM_TREATMENT means deeper mechanism explanation, not repeating an editorial conclusion.

Draft r2 must prefer fewer, denser paragraphs where each sentence contributes at least one distinct function: mechanism, evidence, comparison, limitation, transition or synthesis.

## 5. Blocking finding F4 — source-role language can become ambiguous

P15 b7 includes:

`著者の手で測った分だけが、独立の証しになる。`

Even if the intended “authors” are independent benchmark authors rather than the model vendor, the reader-facing sentence is ambiguous and can be read as saying author-reported results are inherently independent.

Draft r2 must name the evaluator class explicitly:

- vendor-measured;
- model-paper-author-measured;
- benchmark-author independently evaluated;
- third-party reproduction;

as applicable to the bound Evidence.

Do not use bare `著者` as a proxy for independence.

## 6. Blocking finding F5 — raw Architecture boundary strings leak into reader-facing blocks

Draft r1 auto-generates CLAIM_BOUNDARY blocks containing raw English Architecture boundary strings, internal codes such as G01-G06, PARTIAL labels, and production-oriented phrasing.

This is a reader-surface defect.

The active Core drafting contract already distinguishes:

- `EXPLICITLY_STATED` when a boundary should be reader-facing;
- `RESPECTED_BY_OMISSION` when the correct behavior is simply not to make an unsupported claim.

Draft r2 must not dump every Architecture boundary string verbatim into reader prose.

For each boundary:

1. classify whether the reader genuinely needs to see it;
2. use `RESPECTED_BY_OMISSION` for internal drafting guards where omission is sufficient;
3. where `EXPLICITLY_STATED` is needed, write a concise natural-Japanese reader-facing limitation while retaining the exact Architecture boundary in structured metadata.

If current Core validation makes this impossible without changing approved Architecture, fail closed and report the tooling limitation. Do not change Architecture autonomously.

## 7. P09 numeric comparisons

The P09 paper-internal head-to-head comparisons are not automatically prohibited. A same-source/same-protocol comparison may be used when it supports a technical distinction and remains explicitly attributed.

However:

- do not turn the section into an authored leaderboard;
- do not compare numbers across incompatible tasks/protocols;
- retain only numbers that materially support the approved mechanism/grounding argument;
- bind the evaluator/source and conditions visibly.

This is a drafting constraint, not a request to reopen Evidence.

## 8. Required repair scope

This is a bounded Draft-only repair.

Preserve byte/content authority upstream:

- Discovery;
- Screening;
- Evidence r1-r5 and active Evidence/Views;
- Materiality;
- Completeness;
- Candidate Matrix;
- Candidate Selection;
- Architecture r2;
- Human Architecture approval;
- Draft Packages.

Do not perform new research.

Revise:

- all 16 canonical Draft Results as Draft r2;
- profile synthesis as required by revised results;
- reader-facing boundary handling;
- terminology/language QA;
- Draft review report.

The reviewed Draft r1 remains immutable in Git history at commit `d1053e957d92cddd9d2759ec9713db59c66263ad`.

## 9. Draft r2 editorial acceptance criteria

Draft r2 must satisfy all of the following before returning for Sol review:

- zero exact duplicate reader-facing sentence inside each package, excluding unavoidable fixed names/quotes;
- no repeated filler chains used to meet page/character targets;
- page allocation treated as a target, never a character quota;
- natural Japanese technical prose across all 16 packages;
- no systemic metaphor substitutions such as `網`, `証し`, `躾`, `棚`, `構え`, `運ぶ` when an ordinary technical expression is clearer;
- established English/katakana terms retained where they improve precision;
- each FULL_MECHANISM section explains distinct mechanism/transition content rather than repeated conclusion;
- P07B/P09/P15 remain substantive and synthesis-led;
- source-role/evaluator identity unambiguous;
- G01-G06 and PARTIAL limitations preserved semantically without exposing internal workflow labels unnecessarily;
- raw English Architecture boundary text not dumped into reader prose;
- no cross-task ranking;
- no new sources;
- Core Draft validation passes after revision;
- edition-local language QA independently passes.

A substantially shorter Draft is acceptable if the removed text was repetition. Do not re-pad it to recover the r1 character count. If genuine technical depth becomes insufficient after deduplication, report the shortage rather than manufacture prose.

## 10. State boundary

Current canonical lifecycle `DRAFT_COMPLETE` is valid.

Draft r2 repair must not advance to reader-publication validation, Publication Preview, Freeze or Release before fresh Sol Draft Review.

Do not manually rewrite production-state lifecycle to simulate a rollback.

If the frozen Core cannot validate a revised Draft while remaining at `DRAFT_COMPLETE`, stop fail-closed and report the tooling limitation.

Terminal target:

`TS-003 DRAFT_R1_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R2_READER_SURFACE_REPAIR_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R2`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
