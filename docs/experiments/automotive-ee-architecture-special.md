# Cross-domain Special experiment: Automotive E/E Architecture

Status: experimental proof of concept  
Experiment branch: `experiment/automotive-ee-architecture-special`  
As of: 2026-08-18 JST

## 1. Question

Can the Special pipeline originally built for the Japanese Generative AI Technical Survey be reused to produce an evidence-first thematic survey in another technical domain, using recent automotive electrical/electronic (E/E) architecture as the test subject?

The answer from this first pass is **yes at the lifecycle/editorial layer, but not yet as a drop-in collector configuration**.

## 2. Trial scope

The experiment uses a three-year window:

- 2023-08-18 through 2026-08-18;
- edition kind: `THEMATIC`;
- topic: automotive E/E architecture evolution;
- intended output style: the same evidence-first, architecture-before-drafting Special style;
- current stopping point: experimental Architecture Proposal, before reader-facing drafting.

The topic is decomposed into five technical layers rather than treating "SDV", "zonal", and "centralized" as interchangeable labels:

1. physical E/E topology and I/O placement;
2. central/HPC compute and mixed-criticality consolidation;
3. in-vehicle networking and deterministic communication;
4. runtime/service/data abstraction;
5. cloud-to-edge development, integration, and validation lifecycle.

## 3. What reused cleanly

### 3.1 Thematic edition semantics

`special_pipeline.py` already supports `edition_kind = THEMATIC`, an explicit coverage window, `topic_scope`, optional community research, the existing lifecycle states, and the two normal Human Gates.

No new lifecycle was needed for an automotive topic.

### 3.2 Evidence-first editorial method

The following Special principles transfer directly:

- preserve primary evidence before synthesis;
- separate source claims from independently established facts;
- normalize candidates before architecture;
- make Candidate Selection auditable but not a separate Human Gate;
- stop at Architecture Review before reader-facing drafting;
- bind later publication to deterministic provenance.

These are domain-independent and appear to be the most valuable reusable part of the current system.

### 3.3 Supplemental primary-source collector shape

The existing edition-scoped supplemental source plan is also reusable. The experimental plan is stored at:

`/sources/SP-automotive-ee-architecture-2023-2026/coverage/supplemental-source-plan-v0.1.json`

It contains 18 first-party/primary sources and can be consumed by the current supplemental HTTP collector shape because every item has an `SP-*` issue ID, `supplemental-*` item ID, HTTPS URL, title, coverage-gap rationale, and in-window publication timestamp.

## 4. What did not generalize cleanly

### 4.1 Series identity is hard-coded to Generative AI

The current manifest validator requires:

`Japanese Generative AI Technical Survey Special`

as the exact `series_title`.

The experiment therefore keeps that string as a compatibility shim even though the subject is automotive E/E architecture. This is the clearest first refactoring target if cross-domain publication is adopted.

Recommended change: move publication identity/branding out of the lifecycle validator and into a domain or series profile.

### 4.2 Base discovery collectors are domain-specific

The current AI Source Intake is optimized around broad arXiv CS categories, AI project GitHub releases, and an AI official-page watchlist.

That is not sufficient for automotive E/E architecture. The important evidence is distributed across at least these lanes:

- `PAPER`: arXiv and peer-reviewed technical literature;
- `STANDARD_BODY`: AUTOSAR, IEEE 802.x, ISO-related first-party material where public;
- `INDUSTRY_SPEC`: OPEN Alliance, CAN in Automation, similar technical consortia;
- `CONSORTIUM`: COVESA, SOAFEE and comparable architecture/interoperability initiatives;
- `OSS_FOUNDATION`: Eclipse SDV/S-CORE and other shared implementation foundations.

For this domain, an arXiv-only pipeline would systematically lag the architecture actually being standardized and implemented.

### 4.3 Source strength needs a domain-aware taxonomy

A standards release, an arXiv survey, an OEM/Tier1 architecture presentation, and a consortium blueprint are all primary sources in the provenance sense, but they support different claim strengths.

A reusable pipeline should therefore distinguish at least:

- normative specification fact;
- implementation/project fact;
- author research result;
- organization/vendor architecture claim;
- independent reproduction/measurement.

The AI pipeline already has the editorial idea of claim attribution, but automotive makes this distinction unavoidable because public production-vehicle architecture detail is often mixed with supplier marketing.

### 4.4 Some schemas still expose Weekly/AI historical assumptions

The shared architecture schema still carries Weekly naming and a weekly issue-ID pattern, while existing Special architecture artifacts use `SP-*` identifiers. The Special workflow currently works around that boundary operationally, but a genuinely domain-neutral pipeline should have one Special-compatible architecture contract rather than relying on historical schema naming.

## 5. Source Intake result

The experimental plan currently contains 18 sources. It intentionally mixes research and standards/implementation evidence rather than maximizing paper count.

Representative anchors include:

- research on centralization potential and its limits;
- research on zonal architecture and centralized mixed-criticality HPC;
- AUTOSAR R23-11, R24-11, and R25-11 evolution;
- IEEE 802.1DG-2025 automotive TSN profile;
- OPEN Alliance 10BASE-T1S work;
- CAN XL / ISO 11898-1:2024 context;
- COVESA SDV Alliance and vSomeIP material;
- SOAFEE deterministic/cloud-native blueprints;
- Eclipse S-CORE as a shared automotive-grade core-stack initiative.

This set is deliberately a **proof-of-concept intake, not a completeness claim**. A production pass should add systematic SAE/IEEE literature discovery, OEM/Tier1 implementation evidence, and a coverage audit before Candidate Selection is considered canonical.

## 6. Experimental Architecture Proposal

The proposal is stored at:

`/sources/SP-automotive-ee-architecture-2023-2026/architecture/issue-architecture-v0.1.json`

The proposed editorial thesis is:

> The 2023-2026 transition is not simply ECU reduction or "centralization". It is a coordinated redesign of physical placement, compute consolidation, mixed-criticality isolation, deterministic networking, service/data interfaces, and the cloud-to-vehicle development lifecycle. Zonal controllers and central HPC are complementary layers, and the SDV transition is best understood as a redesign of hardware/software/network/lifecycle decoupling boundaries.

The proposed 48-page structure is:

1. 車載E&Eを読むための5層モデル — 4 pages
2. ECUの数ではなく配置を変える — DomainからZonal + Central Computeへ — 8 pages
3. HPC統合の本当の難所 — Mixed Criticality・Isolation・Resource Governance — 8 pages
4. 車内ネットワークはEthernet一色になるのか — TSN・10BASE-T1S・CAN XLの役割分担 — 9 pages
5. SignalからService/Data Contractへ — AUTOSAR・SOME/IP・VSSの抽象化境界 — 8 pages
6. 車載ソフト開発環境そのものがE&Eの一部になる — Cloud-to-Edge・Virtual Validation・Open Core — 7 pages
7. 2026年夏の到達点 — Centralize Everythingではなく責務境界の再設計 — 4 pages

## 7. Preliminary technical finding

The trial already suggests a useful synthesis:

- **Physical topology is becoming zonal**, because wiring, I/O aggregation and physical locality matter.
- **Compute is becoming more centralized**, because ADAS, cockpit, connectivity and cross-domain functions benefit from HPC-class resources and shared execution environments.
- **Those two trends happen together rather than replacing one another.** A future vehicle can be physically zonal while computationally centralized.
- **The hard problem moves from ECU count to isolation and determinism.** Mixed-criticality scheduling, fault containment, timing, security and resource interference become first-class architecture constraints.
- **Ethernet becomes the backbone/fabric, but not necessarily the only bus.** IEEE 802.1DG gives automotive TSN a formal profile, 10BASE-T1S pushes Ethernet toward edge/multidrop roles, while CAN XL expands the CAN design space.
- **Software architecture is moving from specification-only interoperability toward shared implementations and portable contracts.** AUTOSAR CAPI, COVESA projects and Eclipse S-CORE are evidence of that shift.
- **Development architecture is converging with vehicle architecture.** Cloud parity, virtual hardware, SIL/digital twins and continuous deployment are increasingly part of the E/E design assumptions rather than downstream tooling choices.

## 8. Recommended pipeline generalization

Do not fork the entire pipeline per domain. Preserve one shared evidence/lifecycle engine and introduce a small domain profile layer.

A future profile could carry:

```text
domain_id
series_title / branding
source_lanes
base collector configuration
source-strength taxonomy
terminology / screening vocabulary
claim-attribution rules
rendering front-matter identity
```

Candidate Selection, Architecture Review, Drafting, validation, Publication Preview, Freeze and Release should remain shared.

For automotive E/E specifically, the next collector work should be:

1. targeted arXiv/query collector rather than broad AI CS-category ingestion;
2. standards/consortium watchlists with immutable page/spec snapshots;
3. DOI/SAE/IEEE metadata intake where licensing permits metadata and source-link preservation;
4. optional OEM/Tier1 implementation lane with stronger attribution boundaries;
5. topic-specific coverage audit before Architecture Review.

## 9. Conclusion

The experiment supports the original hypothesis: the Special pipeline is more general than the current repository name and AI-specific collectors suggest.

The **core reusable asset is not the AI source list; it is the evidence-first lifecycle, provenance discipline, selection/architecture separation, and Human Gate model**. Automotive E/E architecture is a strong second domain because it stresses exactly the parts that should become configurable: evidence lanes, claim strength, terminology, and series identity.

The branch should remain experimental until the series/domain-profile boundary and canonical automotive Source Intake strategy are decided.
