# Special Visual QA Checklist

Use this checklist on the actual PDF candidate before Human Visual Review approval. TeX-log cleanliness and automated source checks do not replace page-by-page inspection.

## Page integrity

- [ ] No text, heading, table, or box overlaps another element.
- [ ] No clipped text or missing glyphs.
- [ ] No accidental blank page.
- [ ] No page is occupied almost entirely by a small isolated Claim Boundary / callout / box.
- [ ] No large whitespace region is caused solely by `clearpage`, column-mode switching, or an overly aggressive space guard.
- [ ] A page count below the 32-page soft editorial target is not treated as a defect by itself; do not retain low-density pages or add padding merely to reach the target.

## Contents / navigation

- [ ] The printed Contents is reader-facing and normally section-level for Retrospective Specials.
- [ ] Repeated internal subentries such as `Theme at a glance` are not mechanically exposed in the Contents.
- [ ] Theme Synthesis / cross-comparison subheads appear in the Contents only when deliberately promoted as navigation units, not simply because they use `\addcontentsline` internally.
- [ ] The Contents does not spill onto a continuation page containing only a few lines and otherwise large blank space.
- [ ] The first chapter begins naturally after the Contents; page-count targets do not justify preserving an otherwise avoidable sparse TOC page.

## Issue identity and period consistency

Check issue-defining fields against `specials/<slug>/edition.json`, not against memory or a previous Special.

- [ ] Cover / public issue identity matches the intended Special slug.
- [ ] Survey setup coverage start/end matches the edition manifest.
- [ ] `Retrospective scope` names the manifest-derived target month/period.
- [ ] Chronology heading and final synthesis period label, when present, describe the intended period.
- [ ] A previous Special's month label has not survived in a copied heading, table header, or scope box.
- [ ] Adjacent-month references in ordinary article prose are judged semantically; legitimate pre-window/post-window chronology is not treated as a defect merely because another month name appears.

The automated period-consistency guard checks structured identity fields. Human Visual Review should still verify that those labels read naturally in the rendered page and that other prominent month labels have not been copied over accidentally.

## Mixed-layout transitions

- [ ] Full-width chapter heading → two-column narrative is visually separated.
- [ ] Two-column narrative ends in balanced columns without creating a page hole.
- [ ] Narrative → Theme Synthesis transition is natural.
- [ ] Theme Synthesis → closing Claim Boundary → Technical Notes is inspected as one continuous boundary.
- [ ] Technical Notes do not force a new page merely because the appendix begins.
- [ ] Later chapter starts are adaptive: same-page when useful space remains, next-page when it does not.
- [ ] Final synthesis → References does not create an unnecessary sparse page.

## Reader-facing Technical Notes

- [ ] No `Selection済みEvidence`, `normalized claim`, `Source-bound record`, or equivalent production-language leakage.
- [ ] Full repository Evidence IDs are not printed as normal magazine prose.
- [ ] Machine role/event labels are reader-facing.
- [ ] Raw schema enums such as `OTHER`, `OFFICIAL_PUBLICATION`, `PRODUCT_UPDATE`, or partially translated forms such as `モデル_RELEASE` are not exposed in the PDF.
- [ ] `Theme at a glance` and the corresponding Technical Notes card use the same reader-facing taxonomy.
- [ ] Reader-facing type labels are semantically appropriate to the source; for example, evaluation guidance is not presented as a safety incident merely because the material discusses safeguards.
- [ ] Primary URLs remain readable/clickable.
- [ ] Vendor/project/author claim attribution and limitations remain visible.
- [ ] Claim and limitation explanations use natural Japanese sentence structure by default, including `一次情報で確認できる事実` entries.
- [ ] Model/API/benchmark/framework/paper-defined terms may remain English where translation would reduce precision; this is not treated as a language defect.
- [ ] A full English source sentence appears only when intentionally presented as an original quotation and is clearly distinguished from the Japanese reader-facing summary.
- [ ] Japanese rendering has not weakened attribution, numerical setup, threat-model, simulation, or other evidence boundaries.
- [ ] A page does not begin with only a URL or a tiny remainder of the preceding Technical Notes card.
- [ ] `一次資料` and at least its first URL stay together across page boundaries.
- [ ] A limitation paragraph does not leave only its final line at the top of the next page.
- [ ] Large Technical Notes cards may still break naturally; widow/orphan prevention must not make the whole card unbreakable or recreate large structural whitespace.

## References / Source Notes

- [ ] Every bibliography entry uses the already-pinned reader-facing source/paper/release title when that metadata exists.
- [ ] Paper entries can be identified by paper title without relying on the raw arXiv URL alone.
- [ ] Generic `Primary source N` titles are used only as an explicit fallback when selected Evidence truly lacks a usable canonical title; a whole References section of such placeholders is a failure.
- [ ] Owner/authors, URL, visited date, and verification/source-note traceability remain present where available.
- [ ] Long titles and URLs wrap naturally without clipping or overfull text.

## Release-source discoverability

Before Freeze:

- [ ] `CURRENT_RELEASE.md` will identify the canonical frozen source root.
- [ ] The top-level Special directory cannot be mistaken for the canonical frozen source without seeing a warning/navigation pointer.
- [ ] Release notes will point to the canonical source and release manifest.
- [ ] If an already-frozen issue has an erratum, the erratum is recorded separately; the frozen PDF is not silently replaced.

Record any failed item as a Visual Review revision request. Freeze only after the rendered PDF passes this checklist and the human reviewer approves it.
