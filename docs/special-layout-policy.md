# Special Layout Policy

Status: adopted as the default reader-facing layout direction after the first `SP-2026-M07` Visual Review iterations.

## 1. Relationship to the Weekly house style

The Japanese Generative AI Technical Survey series uses a two-column narrative body as its primary magazine identity. Special editions should preserve that identity unless a specific approved Issue Architecture requires otherwise.

For normal Special issues, use a **mixed layout**:

- chapter / feature heading: **one column, full width**;
- narrative article body: **two columns**;
- front matter and Monthly/Period Signals: **one column**;
- wide comparison tables and theme-synthesis matrices: **one column, full width**;
- Source-backed Technical Notes / Claim Boundary-heavy reference material: **one column, full width**;
- bibliography / References & Source Notes: **one column**.

This is intentionally different from an all-two-column rule. Technical Notes contain long model names, paper titles, chronology fields, source URLs, and attribution boundaries that become fragile or hard to scan in narrow columns. Long chapter headings also must not be constrained to a single narrow column because they can collide with the adjacent column.

Within the two-column narrative, subsection headings require deliberate separation from the preceding paragraph. A clean TeX log is not sufficient evidence that a heading is visually separated. The layout layer should explicitly terminate the preceding paragraph and add modest vertical separation. Avoid aggressive `Needspace` guards inside `multicols`: render-first testing on the July Special showed that such a guard can create an almost empty page even when substantial physical space appears to remain.

## 2. Column-mode transitions must not waste a page

Do not implement a normal article-to-synthesis transition as a global `twocolumn -> clearpage -> onecolumn` switch. That pattern can freeze a partially used left column while leaving the right column and most of the page empty.

The default Special implementation should use a balanced local multi-column environment for narrative prose:

1. render the chapter heading full-width;
2. enter a local two-column narrative flow;
3. balance the two narrative columns at the end of the article;
4. return to full-width synthesis / Technical Notes on the same page when sufficient space remains;
5. use a minimum-space guard for wide full-width tables or synthesis panels so they move cleanly to the next page rather than being cramped at the bottom.

Chapter boundaries should also be **adaptive rather than mechanically page-breaking**. The first major feature may start on a fresh page, but later chapters should start in the remaining space when there is enough room for the heading and a meaningful amount of narrative. If the remaining page is too short, move the chapter cleanly to the next page. The same principle applies to the final retrospective synthesis and to References: do not create a largely blank page solely because a new structural unit follows.

The goal is not to maximize text density. It is to make whitespace deliberate: enough separation to signal structure, but not large unused regions caused only by TeX mode switches or unconditional `clearpage` commands.

## 3. Page count is not a justification for column choice

Do not choose one-column layout merely to inflate a Special to its planned page budget. Page targets are editorial planning constraints, not a density target.

If returning narrative prose to two columns materially reduces page count, restore depth by using already-collected Evidence more completely: comparison matrices, chronology, threat-model separation, runtime-layer maps, cross-chapter synthesis, or other reader-facing analysis. Do not use blank pages, exaggerated spacing, or repeated prose as page padding.

If the issue remains substantially below the approved page range after selected Evidence has been represented at an appropriate depth, return to the editorial architecture rather than manipulating typography.

## 4. Evidence-backed supplemental synthesis

A post-draft layout revision may add reader-facing synthesis when Visual Review shows that accepted Evidence was compressed too aggressively in the narrative article.

Such synthesis must:

- reference only Evidence already assigned to the approved issue unless the Evidence gate is explicitly reopened;
- when it is article-local, normally remain inside that article package's Evidence set;
- preserve vendor/project/author attribution classes and recorded limitations;
- avoid internal pipeline terminology in reader-facing prose;
- be stored as a reviewed editorial artifact and SHA-bound into the source manifest;
- leave accepted Article Draft TeX and Technical Notes immutable when the revision is only re-expressing already-selected material;
- explicitly record whether new external Evidence was introduced.

A final retrospective chapter may synthesize relationships across multiple approved packages without reopening Candidate Selection when the human Visual Review explicitly requests that synthesis and no new external Evidence is introduced. Such a chapter must distinguish structural/editorial relationships from demonstrated causality.

## 5. July 2026 application

For `SP-2026-M07`, the initial long-form one-column revision was useful for validating that all selected Evidence could be rendered cleanly, but it weakened visual continuity with the Weekly issue and moved too much information into Technical Notes.

The release-candidate direction therefore uses:

- full-width chapter headings;
- balanced two-column narrative articles implemented as a local multi-column flow;
- explicit paragraph termination plus modest vertical separation before narrative subsection headings, without a `Needspace` guard inside `multicols`;
- one-column full-width theme synthesis for Frontier Models, Multimodal, Inference & Serving, Agents, and Agent Safety & Security;
- one-column Technical Notes;
- adaptive later chapter starts instead of unconditional new-page breaks;
- Paper Watch kept intentionally compact unless its selected Evidence justifies additional treatment;
- a final retrospective synthesis chapter that revisits all six themes and explains their structural relationships using only already-selected July Evidence;
- References allowed to follow the final synthesis naturally rather than being forced onto a new page when sufficient space remains.

The additional synthesis is restricted to already-selected July Evidence. No new topic is introduced merely to preserve a page count, and cross-chapter relationships are editorial synthesis rather than claims of direct causation.
