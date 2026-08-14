# Special Layout Policy

Status: adopted as the default reader-facing layout direction after the first `SP-2026-M07` Visual Review iterations; refined by Issue #40 after the first public Special.

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

## 3. Page count target is soft; reader-facing quality comes first

Do not choose one-column layout, retain low-density navigation pages, or add presentation-only spacing merely to inflate a Special to its planned page budget. Page targets are editorial planning signals, not density requirements.

The default monthly Special publication policy treats **32 pages as the default soft editorial target** and **40 pages as the default hard ceiling**. An edition manifest may define a different page budget when its editorial form requires it, including multi-month retrospective editions. The PDF build must resolve the active edition's `page_budget.target` and `page_budget.max` from the manifest rather than embedding one global numeric ceiling.

A build below its manifest soft target must not fail for page count alone. It should emit/report a below-target condition so Human Review can ask whether Evidence or editorial depth is missing, but the correct response is not to pad the layout. A candidate below the soft target may proceed when Evidence coverage, editorial structure, TeX checks, and Visual QA are satisfactory.

If returning narrative prose to two columns materially reduces page count, restore depth only when the already-collected Evidence genuinely supports more reader-facing analysis: comparison matrices, chronology, threat-model separation, runtime-layer maps, cross-chapter synthesis, or other useful synthesis. Do not use blank pages, exaggerated spacing, repeated prose, unnecessary TOC depth, forced page breaks, or tail-only pages as page padding.

If the issue remains substantially below the planned target after selected Evidence has been represented at an appropriate depth, record that fact for Human Review. Revisit the editorial architecture only when the content itself appears incomplete; do not manipulate typography merely to reach the manifest target. Presentation-only spacing recovery must not be invoked solely to satisfy the soft target.

## 4. Evidence-backed supplemental synthesis

A post-draft layout revision may add reader-facing synthesis when Visual Review shows that accepted Evidence was compressed too aggressively in the narrative article.

Such synthesis must:

- reference only Evidence already assigned to the approved issue unless the Evidence gate is explicitly reopened;
- when it is article-local, normally remain inside that article package's Evidence set;
- preserve vendor/project/author attribution classes and recorded limitations;
- avoid internal pipeline terminology in reader-facing prose;
- be stored as a reviewed editorial artifact and SHA-bound into the source manifest;
- leave accepted Article Draft TeX immutable when the revision is only re-expressing already-selected material;
- explicitly record whether new external Evidence was introduced.

A final retrospective chapter may synthesize relationships across multiple approved packages without reopening Candidate Selection when the human Visual Review explicitly requests that synthesis and no new external Evidence is introduced. Such a chapter must distinguish structural/editorial relationships from demonstrated causality.

## 5. Theme Synthesis / Technical Notes boundary and reader-facing appendix

Issue #40 identified a public-PDF regression in which a small Theme Synthesis Claim Boundary became nearly isolated on a page because the following Technical Notes source began with an unconditional `\clearpage`.

For future Specials:

- a generated Technical Notes file **must not begin with an unconditional `\clearpage`**;
- Theme Synthesis, its closing Claim Boundary, and the following Technical Notes should flow as a continuous full-width sequence unless a natural page break is required;
- do not compensate with aggressive `Needspace` inside `multicols`; the earlier July regression showed that this can create a different almost-empty page;
- Visual Review must explicitly inspect every page for an isolated small box, accidental blank page, or large whitespace region caused only by structural commands;
- a clean TeX log is necessary but not sufficient for Visual acceptance.

Technical Notes are a **reader-facing technical appendix**, not a rendering of repository production metadata. They should retain the material readers need to audit the article—chronology, confirmed facts, vendor/project/author attribution, limitations, and primary URLs—while keeping pipeline state and full Evidence identifiers in repository provenance.

Therefore PDF-facing Technical Notes should normally:

- avoid phrases such as `Selection済みEvidence`, `normalized claim`, and `Source-bound record`;
- translate machine role/event labels into reader-facing labels;
- omit full `evidence:SP-...` identifiers from the magazine body;
- preserve complete IDs and selection state in the Draft Package/source-manifest/repository provenance.

## 6. July 2026 application and legacy boundary

For `SP-2026-M07`, the release-candidate direction used:

- full-width chapter headings;
- balanced two-column narrative articles implemented as a local multi-column flow;
- explicit paragraph termination plus modest vertical separation before narrative subsection headings, without a `Needspace` guard inside `multicols`;
- one-column full-width theme synthesis for Frontier Models, Multimodal, Inference & Serving, Agents, and Agent Safety & Security;
- one-column Technical Notes;
- adaptive later chapter starts instead of unconditional new-page breaks;
- Paper Watch kept intentionally compact;
- a final retrospective synthesis chapter using only already-selected July Evidence;
- References allowed to follow the final synthesis naturally.

The published `SP-2026-M07` source/PDF remains immutable legacy evidence of the first Special. Issue #40 improvements are prospective and must be demonstrated by the next rendered Special before that Issue is closed.
