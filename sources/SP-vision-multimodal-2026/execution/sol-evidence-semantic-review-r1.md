# TS-003 Vision & Multimodal AI — Sol Evidence Semantic Review r1

Status: `SOL_EVIDENCE_SEMANTIC_REVIEW_R1 / REQUEST_CHANGES / BOUNDED_EVIDENCE_REPAIR`

Date: `2026-09-30 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-vision-multimodal-2026`

Reviewed branch: `special/vision-multimodal-2026-work`

Reviewed HEAD: `6c4aa7712d96055402d21c09432dec3a7b179a11`

Reviewed tree: `4923d4d79a5ef44b231581e3c2be23c57cc80518`

Reviewed main: `d6381568cc897a47d6de992189e20339350342b7`

Reviewed main tree: `83ce3a216d852a1c32d0138f9c56fadefa800666`

Reviewed Production Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Reviewed Core tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Decision: **REQUEST_CHANGES**.

The Screening result is acceptable and must be preserved. The Evidence package is substantially deeper than Discovery and shows good source-role discipline in many lanes, but it is not yet safe to advance into Materiality/Completeness because a bounded set of claim-to-source semantic-fidelity defects remains in the current-system layer. The defects are repairable inside Evidence; Discovery and Screening do not need to be rerun.

---

## 1. What passed

The following are accepted and should not be rebuilt from scratch.

- Screening is canonically accepted over all 111 Discovery records: `KEEP 103 / MAYBE 3 / INSPECT 5 / DROP 0`.
- Lifecycle is correctly at `CANDIDATES_NORMALIZED`; Screening checkpoint is `passed`.
- 111 Evidence Cards and 111 Edition Views were built and accepted by the canonical Evidence validators.
- Reported Evidence status is `VERIFIED 106 / PARTIAL 5` with explicit barriers rather than fabricated closure.
- VM-O01 through VM-O16 remain represented.
- D07A and D07B remain separate.
- D04 remains capped.
- offline long-video and online streaming remain separate.
- VLA and World Model remain bounded endpoints rather than expanding into generic robotics/world-model surveys.
- vendor-only current systems are generally quarantined as capability/deployment/evaluation claims rather than undisclosed architecture authority.
- G01-G05 remain unresolved instead of being filled by weak authority; G06 remains only partially advanced.
- main and frozen Production Core remain unchanged.
- Materiality Ledger, Profile Completeness, Selection and Architecture were not run.

Representative historical cards such as AlexNet, ResNet, R-CNN and the grounding lineage contain useful mechanism, bottleneck, transition and limitation detail. The repair below should therefore be surgical.

---

## 2. Blocking finding F1 — repo-derived claims are attached to paper-only Evidence bindings

Several current-system paper Cards contain claims or verification text that explicitly says a repository README was consumed, while the Card's `sources` array binds only the arXiv paper. This violates the claim-to-source fidelity requirement represented by CV2-DM-020.

### Confirmed example: VM-D065 Qwen3-VL

Accepted Card:

`evidence/v2/accepted/.../results/task-4b3f237d9498fe166a31.json`

The Card binds only:

`https://arxiv.org/abs/2511.21631`

as `src-1`.

However claim 3 says, in substance, that the deployment surface is `repo-verified`, including FP8 variants, Transformers/vLLM support, Visual Agent GUI operation and repo-expanded context. Its context explicitly says the Qwen3-VL README was consumed, yet the claim still cites only the arXiv source.

The corresponding repository already exists as a separate Discovery/Evidence record (`VM-D074`). Repository-specific deployment facts belong there unless the paper itself establishes them.

### Confirmed example: VM-D066 Qwen3-Omni

Accepted Card:

`evidence/v2/accepted/.../results/task-3fd5e0dbb8baa816fce5.json`

The Card binds only:

`https://arxiv.org/abs/2509.17765`

but the claim context and verification finding explicitly say the Omni README was also consumed. Again, the repo is represented separately (`VM-D075`).

### Required repair

Audit **all current/role-bearing Evidence Cards**, not just these two, for this exact defect class.

For every claim:

1. identify the exact bound source(s);
2. remove facts that come from an unbound source; or
3. move those facts to the existing Evidence Card whose task authority actually binds that source; or
4. if the current canonical Evidence contract supports multiple authority sources for that task, bind them canonically rather than merely mentioning them in prose.

Do not solve this by adding an untracked URL to claim text.

Paper Cards should be paper-supported. Repository Cards should carry repository/deployment/release-surface facts. Vendor/model-card Cards should remain role-capped.

---

## 3. Blocking finding F2 — Molmo 2 openness/licensing wording conflates release openness with data licensing

`VM-D071` states:

`Open weights+data (Apache 2.0)`

while the separate repository Evidence `VM-D077` is correctly `PARTIAL` and explicitly records that the training-data license mix, including academic/non-commercial third-party material, is not yet bound.

These two surfaces are semantically inconsistent.

### Required repair

Re-read the Molmo 2 paper and repository licensing surfaces and separate, at minimum:

- model weights license;
- code/repository license;
- released data availability;
- individual dataset/data-mixture licensing or usage constraints.

Do not apply `Apache 2.0` to `weights+data` as one undifferentiated statement unless the exact authority establishes that all relevant data is covered by that license.

If the dataset/license mix remains unresolved, preserve `PARTIAL` and phrase the paper Card narrowly enough that it does not contradict the repository Card.

---

## 4. Blocking finding F3 — Evidence `verification` and coverage accounting overstate full-body consumption for some current sources

The edition-wide coverage surface says that 95 arXiv sources received full-HTML body consumption. Yet several accepted current-system Cards describe their actual basis as variants of:

- `Full report abstract + repo README consumed`
- `Full abstract + repo README consumed`

Examples include Qwen3-VL, Qwen3-Omni and Molmo 2.

That wording is materially different from a full-paper semantic read.

### Required repair

For each retained current arXiv technical report/model paper:

- if the full paper body was actually semantically consumed, update the Card/input so the claim context names the relevant paper sections/mechanisms rather than saying only `abstract + README`;
- if only the abstract plus repository surface was consumed, downgrade the relevant verification/status honestly to `PARTIAL` and update the aggregate accounting;
- do not label an Evidence Card `VERIFIED` merely because the locator exists and an abstract was read if the load-bearing mechanism claim requires the body.

This repair is especially important for architecture cases in VM-O09/VM-O10/VM-O12/VM-O14/VM-O15.

The goal is not to force every source to `VERIFIED`; honest `PARTIAL` is acceptable.

---

## 5. Blocking finding F4 — editorial synthesis is sometimes mislabeled as `PRIMARY_FACT`

Some useful editorial judgments are encoded as if they were source-established primary facts.

Confirmed examples:

- VM-D050 Grounding DINO: `Non-redundancy with GLIP: fusion design vs reformulation — different contracts, both kept.`
- VM-D066 Qwen3-Omni: `Boundary enforced: Talker/Code2Wav synthesis detail is TS-002-side...`
- similar lineage/selection/boundary statements may occur elsewhere.

These are edition-level analytical conclusions, not literal facts established by the cited paper.

### Required repair

Audit Evidence Cards for claims where `evidence_class = PRIMARY_FACT` but the statement is actually:

- Sol/Muse scope policy;
- cross-paper comparison;
- lineage synthesis;
- non-redundancy judgment;
- TS-001/TS-002/TS-003 ownership boundary;
- selection/materiality rationale.

Reclassify such statements to the appropriate inference/synthesis class supported by the current schema, or move them to edition-view annotations where that is the proper home.

Do not weaken genuine paper facts. The purpose is to distinguish source facts from editorial synthesis.

---

## 6. Blocking finding F5 — `World Models` historical wording overclaims origin and exclusivity

`VM-D101` currently includes:

- a `terminological origin` framing; and
- the limitation `technical continuation runs through Dreamer, not Genie`.

The bound 2018 Ha & Schmidhuber paper can support its own architecture and its role as an important historical anchor in this edition. It does **not**, by itself, establish that the phrase/concept `world model` originated there. Likewise, `Dreamer, not Genie` is too exclusive for the Round E four-pole design: the intended claim is that Dreamer represents a latent-dynamics/model-based-decision continuation while Genie represents a different interactive-generative branch, with no direct ancestry asserted.

### Required repair

- replace `terminological origin` with a source-safe formulation such as `historical anchor for the modern neural world-model lineage in this edition`, unless an earlier-source investigation is explicitly introduced;
- replace exclusive continuation language with branch-separated wording;
- preserve the important non-ancestry guard: do not imply that Ha/Schmidhuber directly leads to Genie without evidence.

No new full history of the term `world model` is required for this repair.

---

## 7. Non-blocking findings to preserve

The following should **not** be force-closed in r2:

- G01 independent VLA evaluation scarcity;
- G02 transferable/control-oriented world-model benchmark absence;
- G03 same-protocol document specialist/generalist comparison absence;
- G04 deployment latency/VRAM independent evidence scarcity;
- G05 independent reproduction of 2026/current scores;
- G06 exact SigLIP2 citation binding unless a clean primary binding is found at low cost;
- D001/D002 access barriers where the current context-only scope is already sufficient;
- D076/D077 repo/data-license partials unless exact authority is found;
- D111 VSI-Bench partial depth if its eventual use remains bounded to what is verified.

An unresolved gap is preferable to fabricated closure.

---

## 8. Required repair scope

This is an **Evidence-only bounded repair**.

Preserve:

- canonical Discovery corpus and acceptance;
- Screening decisions and acceptance;
- Screening checkpoint/state;
- existing accepted Evidence set as immutable history.

Create a new corrected Evidence result set / Edition Views through canonical append-only builders/acceptors.

Do not modify accepted immutable Evidence artifacts in place.

The repaired Evidence input may be regenerated edition-locally as needed, but source authority must remain within the canonical task bindings unless a formally supported Evidence-source rebinding path is used.

Do not run:

- Materiality Ledger;
- Profile Completeness;
- Selection;
- Architecture;
- Human Gate;
- Drafting;
- publication stages.

Lifecycle should remain `CANDIDATES_NORMALIZED` until Sol r2 semantic review accepts the Evidence package and authorizes the next canonical stage transition.

---

## 9. r2 acceptance criteria

- [ ] Every current/role-bearing Evidence claim is supported by the source IDs actually bound in that Card.
- [ ] Repo-derived deployment/license facts are carried by repo-bound Cards or canonically multi-source-bound tasks, not paper-only bindings.
- [ ] Qwen3-VL/Qwen3-Omni current Cards no longer cite README-derived facts through an arXiv-only `src-1`.
- [ ] Molmo 2 weights/code/data openness and licensing are separated without applying Apache 2.0 indiscriminately to data.
- [ ] Full-body/abstract/README consumption labels are truthful per Card and aggregate accounting is consistent.
- [ ] Architecture-case load-bearing claims are either body-verified or explicitly PARTIAL.
- [ ] Editorial synthesis is not mislabeled `PRIMARY_FACT`.
- [ ] VM-D101 no longer claims unsupported terminological origin or exclusive Dreamer-only continuation.
- [ ] G01-G06 remain explicit unless genuinely resolved.
- [ ] New Evidence acceptance + Edition Views validate canonically.
- [ ] Discovery/Screening are unchanged.
- [ ] lifecycle remains `CANDIDATES_NORMALIZED`; evidence/materiality/completeness/selection/architecture state advances are not run.
- [ ] main and frozen Production Core remain unchanged.

---

## 10. Sol conclusion

The Evidence build is structurally strong and should be repaired, not restarted. The dominant issue is no longer breadth; it is **claim-to-source semantic binding and epistemic labeling in the current-system layer**.

Disposition:

`REQUEST_CHANGES -> bounded Evidence semantic-fidelity repair -> Sol Evidence Semantic Review r2`
