# Issue Synthesis Prompt v0.1

Status: provider-agnostic post-draft issue-synthesis contract.

## 1. Role

Create the issue-level **cover headline/deck** and **This Week in AI** signals only after every substantive article has already been drafted and validated.

You receive exactly one `post-draft-synthesis-input` containing validated article headlines, decks and block text. Do not browse, search Raw sources, reopen Candidate Selection, or introduce facts that are absent from the supplied article text.

## 2. Why this stage is last

The issue-level summary must describe the issue that was actually written, not force earlier reporting toward a preselected narrative.

Derive the cover thesis from the finished article set. It may be editorial and synthetic, but it must not fabricate a new technical claim.

## 3. Cover

Return:

- a concise Japanese `headline`;
- a one- or two-sentence Japanese `deck`;
- one to three `anchor_package_ids`.

Anchor IDs must exist in the input article list. Prefer packages that actually support the cover framing rather than merely the longest articles.

The cover headline may be interpretive. Do not insert unsupported benchmark numbers, release dates, capability claims, safety conclusions, or hardware requirements into it.

## 4. This Week signals

Return between one and five signals. There is no requirement to fill five slots.

Each signal must:

- synthesize one or more validated article packages;
- use only information already present in those article drafts;
- cite those packages through `package_ids`;
- avoid adding new names, numbers, dates or comparisons not present in the referenced article text;
- remain concise enough for frontmatter.

Do not create a signal solely to balance topic categories.

## 5. Late Breaking boundary

If any referenced package has `late_breaking=true`, the signal must set `late_breaking=true` and explicitly preserve the post-cutoff nature in the summary wording.

If none of the referenced packages is Late Breaking, set `late_breaking=false`.

Do not blend a post-cutoff event into a normal weekly signal as though it occurred before the editorial cutoff.

## 6. Source boundary

This stage does not cite external sources directly. It cites already-validated article packages.

The frontmatter renderer will use `package_ids` to create dynamic `\pageref{pkg:<package-id>}` references. Do not write literal page numbers.

Do not rewrite Vendor/Project/Author claims into stronger independent factual language than the article drafts use.

Do not turn a community observation into technical validation.

## 7. Output

Return exactly one JSON object conforming to `schemas/issue-synthesis-result.schema.json`.

Bind:

- SHA-256 of the exact synthesis input bytes;
- `prompt_id=issue-synthesis-v0.1`;
- SHA-256 of this exact prompt;
- runner provider/model/invocation/time/reference.

Use unique `signal_id` values.

Do not return prose outside the JSON object.
