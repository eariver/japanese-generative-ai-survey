# Special Visual QA Checklist

Use this checklist on the actual PDF candidate before Human Visual Review approval. TeX-log cleanliness does not replace page-by-page inspection.

## Page integrity

- [ ] No text, heading, table, or box overlaps another element.
- [ ] No clipped text or missing glyphs.
- [ ] No accidental blank page.
- [ ] No page is occupied almost entirely by a small isolated Claim Boundary / callout / box.
- [ ] No large whitespace region is caused solely by `clearpage`, column-mode switching, or an overly aggressive space guard.

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

## Release-source discoverability

Before Freeze:

- [ ] `CURRENT_RELEASE.md` will identify the canonical frozen source root.
- [ ] The top-level Special directory cannot be mistaken for the canonical frozen source without seeing a warning/navigation pointer.
- [ ] Release notes will point to the canonical source and release manifest.

Record any failed item as a Visual Review revision request. Freeze only after the rendered PDF passes this checklist and the human reviewer approves it.
