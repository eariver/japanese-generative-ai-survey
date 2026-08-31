# W33 Publication Preview Issue #433 Sol Re-review — r1

- Issue: `2026-W33`
- Human Gate: `PUBLICATION_PREVIEW`
- Reviewed candidate commit: `e372578bb8c3a0664a4145887c136ea1f335ce6d`
- Publication Candidate status: `READY_FOR_PUBLICATION_PREVIEW`
- Exact PDF SHA-256: `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`
- Controlling quality issue: `#433` — reader-facing internal editorial/pipeline metadata leakage and under-transformed publication prose
- Sol decision: `REQUEST_CHANGES_CONFIRMED / ISSUE_433_REMAINS_OPEN_IN_CURRENT_READER_TRANSFORMATION / REGENERATE_FROM_DRAFT_COMPLETE`

## Executive finding

The current 11-page W33 candidate is materially better than the original six-page candidate described by Issue #433, but it does not satisfy the underlying publication-transformation acceptance criteria.

The current candidate has already corrected several original symptoms:

- the severe six-page over-compression is gone;
- Serving & Runtime contains concrete release-level technical substance;
- Inference Systems Deep Dive contains useful mechanism-level descriptions;
- Agent Reliability synthesizes six papers by failure layer rather than listing titles;
- Multimodal & Media has substantive reader-facing content;
- old `[V/M]`, `[P/C]`, `[V/C]` reference tags are no longer exposed;
- the exact PDF is visually sound after the page-8 column-balance repair.

Those improvements must be preserved.

However, Issue #433 is fundamentally about the separation between public technical-magazine prose and repository production metadata. That defect remains visible in multiple current reader-facing sections.

## Remaining defects

### 1. Week in Review still exposes repository workflow concepts

`surveys/weekly/2026-W33/sections/70-week-in-review.tex` contains reader-visible phrases equivalent to:

- prior six chapters' already-placed material being cross-edited;
- no new `candidate` or `source` being added;
- `HOLD/REJECT` not being revived;
- `Profile Completeness` being `LIMITED`.

These are production-state explanations, not reader-facing technical synthesis. The final chapter should preserve the underlying uncertainty without exposing how Selection/Completeness/Core represented it internally.

### 2. Source Notes still acts as repository provenance documentation

`surveys/weekly/2026-W33/sections/99-source-notes.tex` exposes production vocabulary such as:

- `technical evidence` / `technical authority`;
- `Evidence identity`;
- `Issue Synthesis`;
- already-placed material / additional candidate/source mechanics;
- `Profile Completeness`;
- `HOLD/REJECT`.

A public reader needs source class, attribution, and limitations, not the repository's internal object model.

### 3. Front matter and early chapters retain editorial-process framing

The front matter and the Frontier/Cyber chapters still contain formulations such as:

- what was "confirmed" for W33;
- dedicated event vs chronology/index records;
- what the "article" does;
- what the "confirmed material" establishes;
- community signal not being technical authority.

The underlying boundaries are valid, but they should be transformed into direct reader-facing statements about availability, timing, access scope, safeguards, and uncertainty.

### 4. Weekly Community Movement does not yet report the movement

The current block mainly explains why X/community material is context-only. Issue #433 requires the publication to tell the reader what was actually observed within the accepted bounded community material. It may remain broad and explicitly non-authoritative, but it must be an observation rather than a methodological note.

No fresh research is authorized. The rewrite must use only the accepted Draft Results and already-bound citation/source metadata.

### 5. Raw internal intake path remains reader-visible

The `w33-community` bibliography entry still points at an internal repository raw-intake path under `Grok_X_SourseIntake/.../grok-x-result.md`.

That path is valid repository provenance but is not appropriate as a reader-facing source URL. Remove the raw path from publication output. If there is no already-known reader-safe public URL in the accepted authority, omit the URL rather than inventing one.

## Correct publication model

Issue #433's three-layer separation remains the controlling model:

1. **Reader prose** — direct technical-magazine explanation of what changed and why it matters.
2. **Reader-facing source/claim limitations** — source class, attribution, measurement/access uncertainty, independent-reproduction limits, and other information that helps a reader assess claim strength.
3. **Repository-only provenance** — candidate IDs, Evidence identities, Selection state, materiality/completeness state, HOLD/REJECT dispositions, package placement, Core checkpoints, bridge/run mechanics, raw ingestion paths, and other production metadata.

The current candidate still leaks layer 3 into layers 1 and 2.

## Regeneration scope

The minimum valid boundary is `DRAFT_COMPLETE`.

Frozen and protected from change:

- Production Profile;
- Discovery / Screening / Evidence / Materiality / Completeness / Selection authorities;
- Architecture and Architecture approval;
- all seven Draft Packages;
- all seven Draft Results;
- Weekly Profile Synthesis Input/Result.

May be regenerated as necessary after the canonical Human Gate rollback:

- `surveys/weekly/2026-W33/**` reader-facing source, bibliography, and exact PDF;
- `sources/2026-W33/publication/v2/**` reader/publication validation authorities;
- edition-local execution/session records required by the bounded repair.

## Required semantic/editorial review after repair

A replacement candidate is not acceptable merely because canonical validators pass. Luna must explicitly inspect the final reader source for Issue #433 classes of leakage and record a fail-closed self-review.

At minimum, the final public TeX/References must be searched and semantically reviewed for inappropriate uses of:

- `candidate`;
- `HOLD` / `REJECT`;
- `Profile Completeness` / `Completeness` as production state;
- `Evidence identity` / `Evidence Card`;
- `Issue Synthesis`;
- `materiality`;
- `Screening` / `Discovery` as pipeline stages;
- `must-cover` / package placement;
- `Core v2` / checkpoint / bridge;
- raw `Grok_X_SourseIntake` paths;
- editorial-process phrases such as "記事では", "確認資料", or equivalent formulations when they merely explain production mechanics.

The word `source` is not intrinsically forbidden. It is acceptable in ordinary reader language such as "一次資料" or "公開資料". The prohibited form is discussion of repository source objects, adding/removing sources, or source identity as pipeline mechanics.

## Reader-content requirements

- Preserve the current strong technical depth in sections 3–6 unless a local wording change is needed for consistency.
- Rewrite sections 0, 1, 2, 7, and 99 as the principal repair surface.
- Keep Week in Review as an independent cross-package synthesis, but state uncertainty in reader language only.
- Make Weekly Community Movement describe actual bounded observed interest/discussion. Do not imply that community discussion proves performance or technical facts.
- Source Notes may become a concise reader-facing `Sources & limitations` section.
- References must contain reader-facing bibliographic identity and public URLs where already available. Internal/raw intake paths must not appear.
- Do not pad to 18 pages. The soft target is not a quota; natural expansion is allowed up to the 24-page hard maximum.

## Gate consequence

The Owner has explicitly requested correction. Publication Preview revision 1 must therefore be materialized through canonical Core operation `REQUEST_PUBLICATION_PREVIEW_REVISION` with:

- `expected_revision = 1`
- `regeneration_boundary = DRAFT_COMPLETE`
- reviewed artifacts = current Publication Candidate / exact candidate PDF
- exact reviewed repository commit bound to the request-only commit parent

After rollback and repair, stop at `DRAFT_COMPLETE` with a replacement reader/publication validation candidate ready for Sol review. Do **not** advance to `VALIDATED_DRAFT`, build a new Publication Candidate, or re-enter Publication Preview before Sol verifies that Issue #433 is actually resolved.
