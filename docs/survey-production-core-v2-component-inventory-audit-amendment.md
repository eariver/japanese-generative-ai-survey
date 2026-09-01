# Survey Production Core v2 — Component Inventory Audit Amendment

Status: `PHASE 0 CORRECTION / authoritative amendment`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Base inventory: `docs/survey-production-core-v2-component-inventory.md`

## 1. Purpose and authority

This document corrects the Phase 0 inventory after a pre-implementation audit found that the original inventory overstated how semantically profile-neutral the existing shared pipeline is.

Where this amendment conflicts with the original Phase 0 inventory, **this amendment controls for Phase 3 implementation planning**. The original document remains useful as process archaeology and should not be rewritten to erase the earlier conclusion.

The key correction is:

> Existing Weekly/Special sharing is mechanically substantial, but the semantic path from Screening through Synthesis still contains Weekly vocabulary and assumptions. v2 must reuse primitives, not automatically retain the current semantic contracts as Core.

## 2. Corrected classification rule

Use four levels instead of treating a shared filename or Special-compatible regex as proof of a shared Core:

- `GENERIC_PRIMITIVE` — hash/provenance/normalization/reference mechanics can be reused without importing Weekly editorial meaning.
- `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` — useful mechanism, but current schema/prompt/validator embeds Weekly or Period semantics and must be generalized or receive a v2 sibling contract.
- `PROFILE_ADAPTER` — explicitly Weekly/Period/Thematic behavior.
- `PUBLICATION_PROFILE` — reader-facing structure/layout/release realization.
- `LEGACY_COMPATIBILITY` — wrappers/monkey patches/revision paths needed only for old state or exact replay.

`shared file format != shared semantic Core` is now a Phase 0 invariant.

## 3. Pilot-critical semantic path

| Stage | Current evidence | Corrected classification | v2 action |
|---|---|---|---|
| Raw provenance / accepted collector bytes | immutable Raw/hash/index machinery | `GENERIC_PRIMITIVE` | `RETAIN` |
| Source discovery execution | common engine; query/window/supplemental policy supplied around it | `GENERIC_PRIMITIVE + PROFILE_ADAPTER` | retain engine; expose profile research-expansion hooks |
| Screening | current result requires Weekly `why_now` and fixed A–L lanes; Special wrappers widen Weekly ID assumptions | `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | v2 profile-neutral decision contract/prompt; legacy v1 accepted only for replay |
| Evidence | factual source/claim/metric structure is strong, but `why_now_confirmed`/editorial recommendation belong to Weekly relevance | `GENERIC_PRIMITIVE + CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | separate factual Evidence from Edition Evidence View |
| Candidate Matrix | requires Weekly editorial window/timing relation | `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | profile-aware v2 matrix; timing adapter only for Weekly |
| Candidate Selection | schema is titled Weekly, Weekly-only issue IDs and editorial roles; legacy Human approval fields | `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | generic internal Selection; role vocabulary validated by Profile |
| Architecture Input/Plan | current plan is titled Weekly, Weekly-only ID pattern, `LATE_BREAKING`, `X_COMMUNITY`, `WATCHLIST_CHRONOLOGY`, `this_week_summary_written_last` | `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | v2 Architecture contract with generic packages plus Profile/Publication fields |
| Special Architecture wrapper | imports Weekly matrix/selection/architecture and injects `this_week_summary_written_last=True`, `late_breaking` fields | `LEGACY_COMPATIBILITY + PROFILE_ADAPTER` | do not use as proof of generic Architecture; retire from future hot path after v2 path works |
| Draft Package | current schema accepts Weekly ID only and requires `late_breaking` / `this_week_summary_forbidden` | `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | v2 Draft Package with generic evidence/coverage constraints; Weekly annotations moved to profile extension |
| Article Draft Result | accepts Weekly/Special IDs but requires `late_breaking_acknowledged`; block enum includes `LATE_BREAKING_NOTE` | `GENERIC_PRIMITIVE + CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | preserve Evidence-ref/attribution mechanics; make Weekly presentation semantics optional/profile-owned |
| Draft validator | strong exact package/prompt/evidence validation, but hard-checks Late Breaking and This Week constraints | `GENERIC_PRIMITIVE + CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | split generic evidence/coverage validator from Weekly extension validator |
| Issue Synthesis | common file accepts Weekly/Special IDs but requires `this_week_signals` and `late_breaking` | `CORE_CANDIDATE_WITH_PROFILE_POLLUTION` | v2 synthesis envelope + Profile-defined synthesis payload |
| Finalization | exact accepted-draft/bibliography/prose-boundary logic mixed with Monthly/Half-year/Annual/Weekly assembly | `GENERIC_PRIMITIVE + PROFILE_ADAPTER + PUBLICATION_PROFILE` | extract semantic/hash primitives; keep layout/required synthesis in Profiles |
| PDF/Visual/Freeze/Release | exact-byte provenance is generic; layout/pagination rules are publication-specific | `GENERIC_PRIMITIVE + PUBLICATION_PROFILE` | keep exact-byte authority in Core, format QA in Publication Profile |

## 4. Concrete profile-pollution evidence

### 4.1 Screening

Current Screening semantics are not profile-neutral because `why_now` and fixed topic lanes are part of the result contract. Special interactive screening also demonstrates a compatibility smell by widening Weekly issue-ID regexes in-process rather than using a first-class edition resolver.

Implication:
- keep complete-one-decision-per-input, prompt/hash binding, append-only acceptance;
- replace Weekly relevance fields with profile-neutral scope tags and later Edition Evidence View annotations.

### 4.2 Selection / Architecture

Current `candidate-selection-decision.schema.json` and `issue-architecture-plan.schema.json` are Weekly contracts despite their relatively generic filenames.

The Architecture contract currently encodes publication/editorial concepts including:
- Weekly-only issue ID;
- `LATE_BREAKING`;
- `X_COMMUNITY`;
- `WATCHLIST_CHRONOLOGY`;
- `this_week_summary_written_last`.

The Special wrapper has historically filled these fields for Special production, which proves mechanical reuse but not semantic neutrality.

Implication:
- v2 Architecture requires a generic package envelope;
- research roles come from Research Profile;
- page/layout roles come from Publication Profile;
- Weekly fields must not be fabricated for Thematic editions.

### 4.3 Drafting

The current Draft Package requires Weekly-only issue identity and Weekly publication semantics. The Draft Result is more reusable in its evidence-linking design, but its mandatory Late Breaking fields still prevent it from being the clean universal contract.

The strongest primitives to preserve are:
- immutable Draft Package SHA binding;
- exact prompt SHA binding;
- `EVENT / CLAIM / METRIC / LIMITATION` references;
- must-cover/boundary coverage;
- attribution mode validation;
- all Architecture-included Evidence must be materially used or explicitly handled.

Weekly-only presentation controls must move to a Weekly extension.

### 4.4 Synthesis

`issue-synthesis-result.schema.json` uses a shared issue-ID pattern but requires `this_week_signals`. This is a direct example of a mechanically shared file that is not a semantic Core contract.

v2 should use:

```text
Synthesis Envelope
  + Profile-defined synthesis payload
```

Examples:
- Weekly: This Week signals / carry-over-facing synthesis;
- Period Monthly: month-level retrospective synthesis;
- Half-year: cross-month / cross-layer synthesis;
- Annual: Event -> Story unit -> Annual trajectory -> Annual thesis;
- Thematic: branch/transition/competing-approach synthesis.

## 5. Revised reuse strategy

The original advice "promote existing shared mechanisms rather than rebuild everything" remains correct only at the primitive level.

Corrected strategy:

```text
existing implementation
    ↓ decompose
GENERIC_PRIMITIVE               PROFILE/PUBLICATION SEMANTICS
    ↓ retain/test                        ↓ explicit adapters/contracts
profile-neutral v2 envelope
    ↓
Weekly / Period / Thematic
```

Do **not**:
- copy every existing schema into a `v2` namespace without semantic cleanup;
- rename Weekly fields and leave their assumptions intact;
- make Thematic production fill dummy `late_breaking`, `this_week`, or rolling-window values;
- use Special monkey-patching as the long-term compatibility layer.

## 6. Consequence for Phase 3 work units

The previous WU-005–010 plan was incomplete. Before Pilot, implementation must cover the semantic path through at least:

1. Profile/State/contract identity;
2. research discovery/expansion;
3. Screening;
4. factual Evidence + Edition Evidence View;
5. Materiality/Completeness;
6. Candidate Matrix/Selection;
7. Architecture;
8. Draft Package/Draft validation;
9. Profile Synthesis;
10. Architecture Review Summary and later Publication Preview basis;
11. executable orchestration;
12. Pilot finding/repair-set capture.

Thematic SP001 is not considered a valid pilot if the path reaches Architecture by filling Weekly-only fields with inert/default values.

## 7. WU-001A exit decision

WU-001A is complete when this amendment is committed because the previously missed profile pollution is now explicitly mapped through Architecture, Drafting, and Synthesis, and the corrected classification is sufficient to amend the minimum vertical-slice implementation plan.

The historical inventory remains valid evidence of what is shared mechanically; this amendment defines what may actually be promoted as semantic Core.
