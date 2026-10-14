# W41 Nano Banana legacy unverified-negative exclusion overlay r6 (SC-M41-02)

Status: `EDITION_LOCAL / NON_AUTHORITATIVE_OVER_CORE / PUBLICATION_EXCLUSION`
Date: 2026-10-12 JST
Scope: `evidence:2026-W41:e9e13879f1c0fcf8` (w41-x-nanobanana21-20261006, Nano Banana 2.1)
Label: `LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE`

Accepted Evidence 36 Cards remain immutable. This overlay does not rewrite
`sources/2026-W41/evidence/v2/accepted/717ea04a51bda4ab8b1d652d9ca92122e6f67431815c5bd910de15e2bad522db/results/task-1a529893f55caf14d80f.json`,
its accepted manifest, r5 files, or original raw. It is not a grant to override
source truth. Positive DeepMind model-card content remains usable through its
bound supplement source.

## 1. Exact legacy locations (verbatim)

Evidence task: `evidence:2026-W41:e9e13879f1c0fcf8`
Evidence SHA: bound in acceptance `717ea04a…` (card `task-1a529893f55caf14d80f.json`).

1. Card `claims[claim-1].context`:
   `Delegated card read (first-party find, no blog post exists) Bound supplement supplement-src-360435193adc7df6 (r4).`
   Offending span: `no blog post exists`.

2. Card `limitations[limitation-1].text`:
   `Pricing/license absent; docs page unfetched; rollout post nonexistent.`
   Offending span: `rollout post nonexistent`.

3. Card `sources[supplement-src-360435193adc7df6].role`:
   `Post-Screening exact authority supplement: Issuer primary model-card authority: Gemini 3 series / 3.6 Flash base, 1M input, 4K image + 64K text output, 7-channel distribution; vendor SxS Elo; no pricing/license in bytes; no blog post exists.`
   Offending span: `no blog post exists`.

4. r4 supplement manifest `evidence-authority-supplement-r4.json`
   `supplement-src-360435193adc7df6.relation`:
   `Issuer primary model-card authority: Gemini 3 series / 3.6 Flash base, 1M input, 4K image + 64K text output, 7-channel distribution; vendor SxS Elo; no pricing/license in bytes; no blog post exists.`
   Offending span: `no blog post exists`.

Properly narrowed control (ADMISSIBLE, already in accepted Card):
- `claims[claim-2].text`: `No matching blog.google 2.1 rollout post was located among the issuer pages checked (delegated search 2026-10-12); the positive model card is not proof of web-wide absence.`
- `claims[claim-2].context`: `Labeled negative-search observation (NOT exhaustive proof); inference class SOCIAL_OBSERVATION.`
- `verification.targets[first-party-product-page].finding`: `Model card found Oct 6 (was: X-only lead); no matching blog post found in checked pages (negative-search observation, not exhaustive proof).`

## 2. Forbidden vs admissible language

FORBIDDEN (categorical absence, unsupported by positive model card):
- `no blog post exists`
- `rollout post nonexistent`
- `blog post does not exist`
- Any reader-facing sentence asserting web-wide non-existence of an official
  Nano Banana 2.1 rollout/blog post as a proven fact.

ADMISSIBLE (only narrowing, dated, scope-bounded):
- `matching issuer blog post not found among pages checked on 2026-10-12`
- `No matching blog.google 2.1 rollout post was located among the issuer pages checked (delegated search 2026-10-12); the positive model card is not proof of web-wide absence.`
- Positive model-card facts via bound supplement:
  `DeepMind model card (Published 6 Oct 2026): Gemini 3 series / 3.6 Flash-based; 1M input, 4K image + 64K text out; 7-channel distribution; vendor SxS Elo.`
  with vendor-metric caveat (Elo is vendor SxS, arena basis unresolved).

## 3. Downstream exclusion scope

Exclude legacy categorical assertions from ALL of:
- Selection justifications / candidate-matrix rationale / candidate-selection;
- Architecture packages, review summary, attention;
- Draft JSON, reader manuscript, TeX, final PDF;
- Any Sol/Human-facing dossier prose that quotes Card limitation/role verbatim.

Selection preview r6 and all later reader-facing surfaces MUST use only the
admissible narrower language above for the blog-absence point. The positive
model-card technical content (base model, context, output, distribution,
vendor Elo) remains citable through `supplement-src-360435193adc7df6`.

## 4. Reader-output grep audit patterns

Run before any Selection acceptance, Architecture, Draft, or PDF review
(`grep -rn` shown; `rg -n` equivalent where available):

```text
grep -rn "no blog post exists" sources/2026-W41/execution/selection-preview-r6* sources/2026-W41/candidate-* sources/2026-W41/architecture* sources/2026-W41/publication/ surveys/weekly/2026-W41/ 2>/dev/null || echo NO_HITS
grep -rn "rollout post nonexistent" sources/2026-W41/ surveys/weekly/2026-W41/ 2>/dev/null | grep -v "evidence/v2/accepted/717ea04a" | grep -v "external/evidence-supplement" | grep -v "execution/reviews/sol-w41-materiality" | grep -v "execution/instructions/2026-10-12_muse-w41-materiality-correction" | grep -v "nanobanana-legacy-negative-exclusion-r6" || echo NO_READER_HITS
grep -rn "blog post does not exist" sources/2026-W41/ surveys/weekly/2026-W41/ 2>/dev/null || echo NO_HITS
grep -rn "nonexistent" sources/2026-W41/candidate-* sources/2026-W41/architecture* 2>/dev/null || echo NO_HITS
```

Expected: ZERO hits in any reader-facing Selection/Architecture/Draft/TeX/PDF
artifact. Hits in this overlay, the Sol r5 review, the r6 contract, or quoted
`LEGACY_` audit prose are audit evidence, not violations. Any unexpected hit
in a proposed reader surface blocks Architecture/Draft progression until the
prose is narrowed to §2 admissible language.

Audit procedure:
1. Run the four patterns above over the exact Candidate-bound tree under review.
2. Record command, exit status, and hit list (or `NO_HITS`) in the Selection
   preview validation log and later Architecture/Draft QA logs.
3. If a hit is in a Core-mandatory auto-emitted field that cannot be excluded
   without changing accepted Card bytes, STOP per contract §3 and propose a
   separate versioned Card reacceptance; no silent erasure or Core patch.

## 5. Core auto-surface check (r6, corrected after matrix derivation)

Checked frozen Core paths for automatic claim-text emission:
- `build_materiality_ledger` emits only `Screening=<decision>; Edition View=<status>`
  structural rationale plus disposition/IDs/hashes; it does not copy Card
  `claims[].context`, `limitations[].text`, or supplement `role`/`relation`.
- `validate_profile_completeness` checks obligation coverage/hashes; no claim text.
- Stage validation (`survey_stage_validation_v2`) binds artifact SHAs; no claim text.
- Selection machinery (`validate_candidate_matrix`/`validate_selection`) binds
  ledger/completeness/matrix/selection SHAs; Selection assignment rationales
  are author-written, not auto-copied from Cards. CORRECTION: `derive_candidate_matrix`
  DOES verbatim copy Card `limitations[].text` + unresolved/contradictions into
  Matrix `remaining_boundaries[]` by Core design (internal audit trail, not
  reader prose). r6 Matrix therefore contains one faithful internal hit:
  `execution/candidate-matrix-r6.PROPOSED.json:1168` reproduces limitation-1
  `rollout post nonexistent` verbatim from the immutable accepted Card.

Result: `NO_READER_SURFACE_BLOCK`. The verbatim Matrix boundary is internal
Sol-audit evidence (it proves the limitation was not silently erased), not a
reader-facing assertion. All author-written Selection rationales (r6 preview),
the dossier, and all downstream reader surfaces use only §2 admissible
language (verified NO_HITS in `candidate-selection-r6.PROPOSED.json`). The
safeguard in §3–§4 IS enforceable without a versioned Card reacceptance:
no reader surface auto-emits the legacy phrase, and no accepted Card/Raw byte
was changed. No STOP required; this correction is recorded here rather than
by silent erasure. If any future Architecture/Draft/TeX/PDF authoring copies
the Matrix boundary verbatim into reader prose, §4 blocks progression until
narrowed.

## 6. Preserved supplement-access provenance caveats (8 entries)

Per `execution/source-intake/w41-supplement-access-provenance-r5.md` (unchanged):
all 8 `accessed_at` are BUNDLE_WINDOW_ESTIMATE / PER_PAGE_UNKNOWN; no per-page
HTTP log; all raw are BOUNDED_EXCERPT (bounded verbatim + reviewer PROVENANCE
header/NOTEs), not full-byte HTML/PDF. Nano Banana supplement
`supplement-src-360435193adc7df6` accessed_at `2026-10-12T00:36:00Z` is a bundle
window estimate; its raw `nanobanana-model-card-r4.source-excerpt.md` (1055 B)
is a delegated verbatim excerpt. textGrain PDF unread; X authorship
unverified; delegated excerpts not full HTML. These caveats carry forward into
Selection preview and Completeness r6 residuals.

(End of file)
