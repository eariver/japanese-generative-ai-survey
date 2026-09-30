# TS-003 Drafting Language Policy — Japanese technical prose

Status: `EDITION_LOCAL / MANDATORY_MANUAL_DRAFTING_GUARD`

Date: `2026-10-01 JST`

Issue: `SP-vision-multimodal-2026`

Reader title: `Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`

## 1. Purpose

This policy supplements the frozen Survey Production Core v2 for TS-003 Drafting.

The current Core v2 Draft validator primarily guards evidence/reference/schema boundaries. It does not by itself guarantee natural Japanese technical prose. An older editorial prompt explicitly allowed technical English where it preserves precision and warned against translation for translation's sake; this edition restores that principle as a mandatory manual guard.

The highest-priority Human instruction is:

> **Do not over-translate technical terminology into dense or invented Sino-Japanese/kanji compounds.**

A Core PASS does not constitute a language-quality PASS.

## 2. Mandatory language principles

### 2.1 No translation for translation's sake

Do not replace an established English or katakana technical term with a rare, invented, overly literal, or excessively kanji-heavy Japanese expression merely to make the prose appear more Japanese.

Prefer, in this order:

1. established Japanese technical usage;
2. established katakana usage;
3. the English technical term when it preserves precision better;
4. a short natural-Japanese explanation on first use when clarification is needed.

If no natural and established Japanese translation exists, keep the English/katakana term. Do not coin a new kanji compound simply to avoid English.

### 2.2 Avoid excessive nominalization and kanji stacking

Prefer ordinary Japanese verbs and causal syntax over long chains of nouns.

Avoid prose dominated by repeated abstract endings such as `〜化`, `〜性`, `〜的`, `〜処理`, `〜機構`, `〜構造`, or multiple consecutive Sino-Japanese nouns when a shorter verb-led sentence is clearer.

Do not mechanically translate English noun phrases into stacked Japanese nouns. Split the sentence or state the action explicitly.

### 2.3 Preserve semantic distinctions

Translation must not collapse distinctions that are load-bearing in TS-003. In particular, keep the following distinct unless the source itself equates them:

- `grounding` vs `alignment`;
- `perception` vs `reasoning`;
- `detection` vs `recognition`;
- `segmentation` vs `detection`;
- `world model` vs `predictive representation`;
- `evaluation` vs `benchmark`;
- `capability` vs `evidence`;
- `architecture` vs `deployment`;
- `vendor claim` vs independent result;
- `offline long-context video understanding` vs `online/streaming understanding`;
- `image-level semantics` vs `region/coordinate grounding`.

If a Japanese rendering would blur one of these distinctions, retain the English term or add the English term at first use.

### 2.4 Use English/katakana deliberately, not excessively

Keeping English is allowed when it protects precision, but reader-facing prose must not become an English-parenthesis catalogue.

Default pattern:

- first important use: natural Japanese explanation + established term/original term when useful;
- later uses: the shortest unambiguous established form.

Do not repeat an English gloss in parentheses every time a term appears.

### 2.5 No invented translations

Do not introduce a new Japanese translation that is not established in the relevant technical literature/community unless the wording is explicitly marked as an explanatory paraphrase rather than a term.

When in doubt, preserve the original term and explain the concept in normal Japanese.

## 3. Reader-facing prose standard

The target is technically rigorous Japanese written by a human technical editor, not grammatically valid but visibly machine-translated Japanese.

Prefer:

- concrete subjects and verbs;
- explicit cause/effect;
- short definitions followed by technical detail;
- comparative sentences that state exactly what changed;
- direct wording such as `〜を入力する`, `〜を予測する`, `〜を座標に対応づける`, `〜では測れない` when that is more natural than an abstract noun phrase.

Avoid:

- unnatural literal-English syntax;
- long pre-nominal modifier chains;
- repeated `〜における` / `〜に対する` / `〜を通じた` constructions when simpler syntax works;
- vague abstract nouns whose referent is unclear;
- inflated academic register used only to sound formal;
- production jargon in reader-facing prose.

## 4. TS-003 terminology discipline

Before full drafting, create an edition-local terminology map:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

It must record at least:

- preferred reader-facing form;
- original English term;
- terms/renderings to avoid when materially ambiguous or unnatural;
- first-use handling where needed;
- notes on semantic boundaries.

The map is not required to translate every term. `KEEP_ENGLISH_OR_KATAKANA` is a valid and often preferable disposition.

Use the same rendering consistently across P01–P15 unless a source-specific distinction requires otherwise.

## 5. Mandatory manual language QA

After Draft r1 is built, generate:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r1.md`

This QA is mandatory even if all Core validators pass.

Review the full reader-facing Draft for at least:

1. excessive kanji/Sino-Japanese translation;
2. invented or nonstandard translations;
3. literal translation artifacts;
4. over-nominalization / noun stacking;
5. English-to-Japanese semantic drift;
6. inconsistent terminology across packages;
7. unnecessary repeated English parentheticals;
8. sentences that are grammatical but do not read like natural Japanese technical prose;
9. ambiguity introduced by translating a load-bearing English distinction;
10. reader-facing leakage of production/internal workflow language.

For every material issue, record location, original wording, proposed correction, and issue class.

Do not silently declare PASS merely because there are few spelling errors. This QA is semantic/editorial.

## 6. Drafting depth and language are joint constraints

Natural Japanese must not be achieved by deleting technical substance.

The Architecture r2 depth classes remain binding:

- `FULL_MECHANISM_TREATMENT`;
- `TRANSITION_NODE_TREATMENT`;
- `BRIEF_CONTEXT_OR_AUTHORITY`.

Especially for P07B, P09, and P15, improve readability by organizing around mechanism/transition/evaluation contract—not by reducing source-supported technical detail to shallow summaries.

## 7. Sol review requirement

Draft r1 is not ready for Publication Preview until Sol performs a separate manual review covering both:

- technical/evidence fidelity;
- Japanese editorial quality under this policy.

A deterministic Core PASS cannot override a Sol `REQUEST_CHANGES` on language quality.

## 8. Binding precedent

The frozen older editorial drafting prompt states that technical English terms may remain where they preserve terminology or precision and that translation for translation's sake should be avoided.

This edition-local policy makes that principle explicit and stronger for TS-003 because the current Core v2 drafting prompt does not encode equivalent Japanese-style detail.

Terminal policy state:

`TS-003_DRAFTING_LANGUAGE_POLICY_ACTIVE`

`CORE_PASS_NOT_LANGUAGE_PASS`

`MANUAL_SOL_LANGUAGE_REVIEW_REQUIRED`
