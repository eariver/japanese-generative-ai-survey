# 2026-W32 Draft Validation v0.1

Status: **validated draft; editorial polish remains**  
Validated: 2026-08-10  
Draft root: `surveys/weekly/2026-W32/main.tex`

This report records the first whole-issue validation pass after every package in `issue-architecture-v0.1.md` had been drafted.

## 1. Citation-to-claim audit

Mechanical bibliography audit after the final citation pass:

- unique citation keys used by the issue: **36**;
- bibliography entries: **36**;
- missing bibliography keys: **0**;
- unused bibliography entries, excluding the intentionally `\nocite`d repository entry: **0**;
- unresolved LaTeX citations/references: **0**.

Citation locality was tightened where a paragraph could otherwise be detached from the source that supported its concrete claim. Corrections included:

- Astra's concrete mathematical-result examples;
- the Astra claim-boundary box;
- the opening Qwen / DeepSeek / Kimi chronology summary;
- the closing model/open-weight synthesis and SGLang follow-through;
- Shieldstral comparison limitations;
- Astra Critical-threshold wording;
- H3's Jul-31 artifact / W32 momentum summary;
- Qwen Image 3.0's W32 official integration signal.

No factual claim was changed solely to satisfy the citation audit; these edits make existing evidence chains more local and auditable.

## 2. Chronology consistency

The same artifact/event was searched across all section files for date/status divergence.

Validated cross-section chronology:

- OpenAI Astra mathematics/theoretical-CS event: **2026-08-01**;
- OpenAI Astra cyber/Preparedness update: **2026-08-07, post-cutoff / Late Breaking**;
- MiniMax H3 announcement: **2026-07-31**;
- MiniMax H3 public-weight/local-workflow activity: treated separately from the Jul-31 announcement; exact first-public weight timestamp remains unresolved;
- SGLang v0.5.17: **2026-08-08, post-cutoff / Late Breaking**;
- Qwen3.8-Max-Preview debut: **2026-07-19**, W32 relevance is renewed evaluation/open-weight expectation rather than a W32 launch;
- DeepSeek-V4-Flash-0731 update: **2026-07-31**;
- Claude Tag: **2026-06-23**, pre-window relevance;
- Google Agent Quality Flywheel: **2026-06-30**, pre-window methodology relevance;
- Grok Build open-source event: **2026-07-15**, pre-window relevance;
- Grok Voice moving-alias switch: announced Jul 29, effective **2026-08-05**.

No blocking chronology conflict was found in the drafted issue.

The hard-coded cross-reference `p.3--4` from the Astra Cyber Late Breaking note was checked against the rendered PDF; the Astra Lead Story does occupy pages 3--4 in v0.1.

## 3. Main vs Post-Cutoff validation

The standard cutoff remains:

`2026-08-07 18:00 America/New_York`

Post-cutoff information is not silently backdated into the Main-window narrative.

- Astra Cyber is explicitly Late Breaking.
- SGLang v0.5.17 is explicitly Late Breaking.
- H3 hands-on community activity that occurred after cutoff remains marked as follow-up/social observation.
- DeepSeek Reaction-Pass evidence collected for the 0731 update is not treated as Main-window community evidence.

## 4. Evidence-class validation

The visual/editorial evidence classes remain distinct:

- ordinary cited prose: primary/technical evidence or clearly identified editorial synthesis;
- `claimboundary`: vendor/author claims, benchmark/setup boundaries, simulation/threat-model limitations;
- `communitynote`: X/community observations only;
- `latebreaking`: post-cutoff event/follow-up.

The Reaction Pass is not used to establish model capability as fact.

## 5. TeX / PDF validation

Local build command chain:

`latexmk -> LuaLaTeX -> biber -> LuaLaTeX`

Result:

- build exit status: **pass**;
- PDF pages: **14**;
- paper size: **A4 on all pages**;
- unresolved citations/references: **0**;
- Overfull boxes: **0**;
- Underfull boxes: **0**;
- missing glyph warnings: **0**;
- encrypted: **no**;
- openable by PyMuPDF: **yes**;
- likely scanned: **no**;
- XFA: **no**;
- Japanese and Latin fonts are embedded.

The complete PDF was rendered to page images after the final citation pass and reviewed as a 14-page contact sheet. No clipping, broken glyphs, obvious overlaps, or broken section transitions were observed.

## 6. Page-budget decision

Editorial Specification gave an initial target of approximately 16 pages and a provisional maximum of approximately 24 pages. The v0.1 draft is **14 pages**.

This is accepted for validation rather than padding the issue with weak or duplicate material. The page target remains a planning aid, not a quota. Expansion should occur only if editorial review identifies evidence-rich material that is currently under-explained.

## 7. Terminology / prose consistency

A mechanical terminology scan found no blocking ambiguity in model names, event names, or chronology. Technical English is intentionally retained where it maps directly to source terminology (for example `weights`, `serving`, `harness`, `context`, `benchmark`).

One notation inconsistency was normalized during validation:

- `2x RTX 5090` -> `2×RTX 5090`.

The issue still uses a deliberately mixed Japanese/English technical register. A later prose-polish pass may reduce unnecessary English mixing, but this is not treated as a factual-validation blocker.

## 8. Remaining known boundaries

The draft is validated, not frozen. Remaining substantive boundaries are already visible in the text:

- independent mathematical assessment of Astra's ten results remains outside the current evidence layer;
- MiniMax H3's exact first-public weight timestamp remains unresolved;
- vendor/author benchmark results remain attributed and setup-bound;
- X reaction evidence is representative evidence collection, not a sentiment census;
- community implementation claims such as Kimi K3 low-RAM inference remain community claims unless independently reproduced.

## 9. CI visibility limitation

The repository contains `.github/workflows/build-weekly-survey.yml` for a TeX Live 2026 LuaLaTeX build and PDF artifact upload. The current GitHub connector can inspect workflow artifacts/jobs when a run ID is known, but does not expose listing of push-triggered workflow runs used here. Therefore this validation records the local reproducible build as passed; GitHub Actions run visibility remains an operational follow-up rather than a document-content blocker.

## Gate

`2026-W32` is now suitable for **editorial/prose review and final claim review**. New candidate discovery is not required before that review unless a selected claim is deliberately expanded beyond its current evidence boundary.
