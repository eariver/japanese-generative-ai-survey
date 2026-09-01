# 2026-W32 Candidate Screening Records

This directory is the pre-editorial candidate inventory for issue `2026-W32`.

## Purpose

One candidate / event / paper / social signal is stored in one Markdown file before article construction begins.

These files are **not article drafts** and are not a final table of contents. They preserve:

- what was originally collected,
- how it was discovered,
- event / publication chronology where known,
- primary sources already captured,
- Grok/X social evidence where relevant,
- conflicts between initial collection notes and later verification,
- unknowns and pending verification,
- current screening state.

## Status semantics

- `candidate`: retain in the pool for later comparison.
- `candidate-social`: retain primarily as community/use-case evidence.
- `candidate-chronology`: valid event primarily useful for chronology / small update coverage.
- `candidate-pending-primary`: promising candidate whose primary source is not yet captured.
- `hold-*`: keep the collected item but do not promote until the stated uncertainty is resolved.
- `watchlist`: weak or secondary signal; retain without forcing inclusion.
- `late-breaking-*`: discovered after the editorial cutoff or treated as post-cutoff follow-up.
- `rejected-for-w32`: preserved for provenance but not considered a valid W32 event under current evidence.
- `low-priority-social`: social narrative retained for completeness but not yet strong enough for standalone technical coverage.

## Evidence separation

These screening records may link to:

- `../grok/raw/` — raw X trend discovery,
- `../grok/reactions/raw/` — raw X reaction collection,
- `../evidence/social/` — normalized social evidence,
- `../evidence/technical/` — primary-source technical screening.

X evidence establishes that a reaction or claim was observed on X. It does not establish that the technical claim inside the post is true.

Paper records marked `abstract-screened` contain author-reported abstract-level claims only; full-paper review is a later step.

## Editorial rule

Do not assign final magazine sections or article priority from these files alone. First complete the inventory, then compare candidates across all source classes, then decide the issue structure.