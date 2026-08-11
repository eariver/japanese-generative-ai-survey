# Special Visual QA Checklist

Use this checklist on the actual PDF candidate before Human Visual Review approval. TeX-log cleanliness and automated source checks do not replace page-by-page inspection.

## Page integrity

- [ ] No text, heading, table, or box overlaps another element.
- [ ] No clipped text or missing glyphs.
- [ ] No accidental blank page.
- [ ] No page is occupied almost entirely by a small isolated Claim Boundary / callout / box.
- [ ] No large whitespace region is caused solely by `clearpage`, column-mode switching, or an overly aggressive space guard.

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
- [ ] Primary URLs remain readable/clickable.
- [ ] Vendor/project/author claim attribution and limitations remain visible.
- [ ] Claim and limitation explanations use natural Japanese sentence structure by default.
- [ ] Model/API/benchmark/framework/paper-defined terms may remain English where translation would reduce precision; this is not treated as a language defect.
- [ ] A full English source sentence appears only when intentionally presented as an original quotation and is clearly distinguished from the Japanese reader-facing summary.
- [ ] Japanese rendering has not weakened attribution, numerical setup, threat-model, simulation, or other evidence boundaries.

## Release-source discoverability

Before Freeze:

- [ ] `CURRENT_RELEASE.md` will identify the canonical frozen source root.
- [ ] The top-level Special directory cannot be mistaken for the canonical frozen source without seeing a warning/navigation pointer.
- [ ] Release notes will point to the canonical source and release manifest.
- [ ] If an already-frozen issue has an erratum, the erratum is recorded separately; the frozen PDF is not silently replaced.

Record any failed item as a Visual Review revision request. Freeze only after the rendered PDF passes this checklist and the human reviewer approves it.
