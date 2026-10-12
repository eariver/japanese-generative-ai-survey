# J-GAS W41 — Sol Independent Evidence Authority Binding Review r2 (Muse r4)

Date: 2026-10-12 JST
Status: `BINDING_TECHNICAL_CONDITIONAL_PASS / DETERMINISTIC_R5_HYGIENE_BEFORE_ACCEPTANCE`
Repository: `eariver/japanese-generative-ai-survey`
Work branch: `weekly/2026-W41-v2-work`

## Exact reviewed identity and stage

- HEAD `241a1cd5a7d3809b6a052628509a35445ad57c83`; Tree `97818cb482c3f5a2b3d6abbea4bf3639eb51e7b7`.
- Starting Muse r4 instruction `62c0efc825eeca30d690daf3ada62a430822a9fa`; exact compare: **2 normal commits; 161 W41-local changed files; ZERO shared Core, main, W40 or other-edition changes**.
- Remote main HEAD `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8` / Tree `31c0adc5b57761e5073d100554279a8adc5a18f4`.
- Remote frozen Core HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- State `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; Discovery/Screening PASSED; Evidence/Materiality/Completeness pending; both Human Gates pending. No Evidence/View acceptance or stage advance.

## 1. Positive findings

1. **Source-class projection semantics are defensible:** the only nine immutable r1 source_type `SECONDARY_OBSERVATION` records are mapped in derived Evidence Tasks to existing frozen Core `SECONDARY`. This neither upgrades an observation to an issuer fact nor changes canonical 37 Discovery or 37 Screening authorities. The projection ledger lists all 36 tasks, 9 projected and 27 passthrough with original/derived hashes. The frozen Core mapping lacks the original type, confirming W41 edition-local compatibility need. Muse reports deterministic double-build, unknown-type negative validation, frozen-Core `task_authority_sources` 36/36, and package basis PASS.
2. **Source Supplements have real archived bytes:** 8 source entries / 7 actual excerpt files. Sol independently recomputed **all seven UTF-8 byte lengths and SHA-256 values** against the committed manifest: **7/7 exact PASS**. Supplement original issuer locators are task-ID and Discovery-ID scoped. A shared changelog raw excerpt legitimately covers two distinct task-bound source entries.
3. **Card provenance references corrected:** Sol inspected all **36** versioned r2 Evidence Cards. All claim/metric/limitation `source_ids` resolve to source entries present on the same Card (no missing ID), and eight previously unbound original issuer source claims now have `supplement-src-*` entries (Nano Banana 2.1, SynthID, Nace Drex, Mistral, EmbeddingGemma 2, textGrain, Decisions beta, Ultrafast). Edition-local preview r2 has 36 Tasks, 36 Cards, 36 Views, with declared VERIFIED3/PARTIAL21/NEEDS_MORE12, MATERIAL21/HOLD13/CONTEXT2. Sol did not execute Core's CLI or independently fetch every external first-party site, so reported Core code-run PASS remains Muse-executed, while hash/reference checks above were Sol-independent.
4. **Risk containment:** Clef-omni weight download validation is now UNRESOLVED, while the issuer blog is timestamp-pinned in-window; Decisions beta verified status is limited to the issuer changelog feature, not unresolved price. Mistral 49B X statement vs 52B docs preserved; StepFun, Microsoft Decision-1 and Tencent temporal/availability uncertainties, and four W40 inherited HOLDs remain bounded.

## 2. Exact remaining acceptance hygiene

**SC-E41-05 — r2 regeneration builder is NOT restricted to authorized nine (MANDATORY).**
`sources/2026-W41/execution/compat/evidence-source-class-projection-r4/build_projection_r4.py` has an explicit nine-ID allowlist and refuses unexpected tenth source. But the actual `build_r2_package.py` uses the unqualified condition `if st == "SECONDARY_OBSERVATION": ... "SECONDARY"`. This would silently project any additional unreviewed Discovery source in a future regeneration, notwithstanding the current exact-nine contents. Before Evidence acceptance, harden the exact r2 builder (or a versioned r5 builder) to enforce exactly the nine allowed `(Discovery ID, Evidence Task ID, original source_type)` combinations; abort on tenth/unexpected type, missing expected member, or any non-source_type change beyond the eight explicit supplement bindings. Show new negative-injection FAIL_CLOSED, deterministic double-build, and byte-equality of regenerated r2 package + Tasks against the currently reviewed files. **Do not modify canonical Discovery/Screening or frozen Core.**

**SC-E41-06 — bounded editorial/source precision (MANDATORY).**
- The Nano Banana Card says **"no blog post exists"**, whereas evidence supports at most **"no matching blog post found in the checked issuer pages"**. Downgrade categorical absence claims and do not cite a positive model card as sole proof of exhaustive negative search; explicitly label the negative search observation.
- r4 supplement `accessed_at` entries show exact minute-level times, while the provenance notes disclose these are **bundle-level windows, not individual fetch instants**. Verify log provenance of each recorded minute; if exact minute is not demonstrated, preserve a separately visible `BUNDLE_WINDOW_ESTIMATE / PER_PAGE_UNKNOWN` caveat in final per-source ledger/Card, and do not report exact per-page retrieval proof. No fabricated timestamp replacement or Core schema change.
- Source excerpts include editorial `NOTE` statements and partial issuer quotes, not full-byte HTML; retain `BOUNDED_EXCERPT`, keep quotes versus reviewer annotations distinguishable. textGrain method-level paper assertions require actual technical-report consumption; otherwise restrict accepted Card to documented blog-level facts. This does not demand a new broad research sweep.
- Preserve product release versus service preview, vendor measurements versus reproduced benchmarks, weights promised versus downloaded, and posted X clock versus independently evidenced original article time.

## 3. Conditional decision / bounded authorization

Decision: `EVIDENCE_R4_SOURCE_BINDING_TECHNICAL_PASS / ACCEPTANCE_CONDITIONED_ON_SC-E41-05_06`.

Authorize a **single bounded deterministic r5 cleanup** before formal Evidence acceptance. If and only if:
- r2 source-class projection is proven exact-nine fail-closed and deterministic under unmodified Core;
- real source supplement manifest validity, 36/36 source/Task/Card bound checks, raw SHA/byte accuracy and revisioned Cards are all freshly validated without source-class monkeypatch or unspecified state-identity overrides;
- Nano Banana negative-search wording and timestamp/provenance labeling are corrected without new unsupported claims;
then Muse may create canonical 36-card Evidence Acceptance and 36 accepted Edition Views using existing Core machinery and record actual accepted SHA identities. Prepare a Materiality/Completeness proposal, not a fake PASS.

**Do not advance** `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` or mark Materiality/Completeness checkpoints PASS in this r5 unit; Core transition is combined and requires a fresh independent Sol Materiality/Completeness review of accepted Cards and scope. No Selection/Architecture/Draft/PDF/Human Gate. If any Core validator fails or exact-nine projection cannot be established, STOP `EVIDENCE_ACCEPTANCE_BLOCKED` and report precise error; Core repair is a separate deferred task and no silent workaround is permitted.
