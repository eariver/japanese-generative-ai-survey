# Special Layout Policy

Status: adopted as the default reader-facing layout direction after the first `SP-2026-M07` Visual Review iteration.

## 1. Relationship to the Weekly house style

The Japanese Generative AI Technical Survey series uses a two-column narrative body as its primary magazine identity. Special editions should preserve that identity unless a specific approved Issue Architecture requires otherwise.

For normal Special issues, use a **mixed layout**:

- narrative article body: **two columns**;
- front matter and Monthly/Period Signals: **one column**;
- wide comparison tables and theme-synthesis matrices: **one column, full width**;
- Source-backed Technical Notes / Claim Boundary-heavy reference material: **one column, full width**;
- bibliography / References & Source Notes: **one column**.

This is intentionally different from an all-two-column rule. Technical Notes contain long model names, paper titles, chronology fields, source URLs, and attribution boundaries that become fragile or hard to scan in narrow columns.

## 2. Page count is not a justification for column choice

Do not choose one-column layout merely to inflate a Special to its planned page budget. Page targets are editorial planning constraints, not a density target.

If returning narrative prose to two columns materially reduces page count, restore depth by using already-collected Evidence more completely: comparison matrices, chronology, threat-model separation, runtime-layer maps, or other reader-facing synthesis. Do not use blank pages, exaggerated spacing, or repeated prose as page padding.

If the issue remains substantially below the approved page range after selected Evidence has been represented at an appropriate depth, return to the editorial architecture rather than manipulating typography.

## 3. Evidence-backed supplemental synthesis

A post-draft layout revision may add reader-facing synthesis when Visual Review shows that accepted Evidence was compressed too aggressively in the narrative article.

Such synthesis must:

- reference only Evidence already assigned to that approved article package unless the Evidence gate is explicitly reopened;
- preserve vendor/project/author attribution classes and recorded limitations;
- avoid internal pipeline terminology in reader-facing prose;
- be stored as a reviewed editorial artifact and SHA-bound into the source manifest;
- leave accepted Article Draft TeX and Technical Notes immutable when the revision is only re-expressing already-selected material;
- explicitly record whether new external Evidence was introduced.

## 4. July 2026 application

For `SP-2026-M07`, the initial long-form one-column revision was useful for validating that all selected Evidence could be rendered cleanly, but it weakened visual continuity with the Weekly issue and moved too much information into Technical Notes.

The next release-candidate revision therefore uses:

- two-column narrative articles;
- one-column full-width theme synthesis for Frontier Models, Multimodal, Inference & Serving, Agents, and Agent Safety & Security;
- one-column Technical Notes;
- Paper Watch kept intentionally compact unless its selected Evidence justifies additional treatment.

The additional synthesis is restricted to already-selected July Evidence. No new topic is introduced merely to preserve a page count.
