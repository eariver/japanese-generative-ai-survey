# TS-003 Muse execution — bounded Evidence semantic-fidelity repair after Sol r1

Status:

`EXECUTION_AUTHORITY / EVIDENCE_R1_REQUEST_CHANGES / BOUNDED_EVIDENCE_REPAIR_ONLY / STOP_FOR_SOL_R2`

Date: `2026-09-30 JST`

Issue:

`SP-vision-multimodal-2026`

Branch:

`special/vision-multimodal-2026-work`

## 0. Guard authority and precedence

**Do not use a work-branch SHA/tree hardcoded inside this file.**

The exact work-branch HEAD/tree supplied in the Sol launch message are the sole work-branch start guard for this execution. This avoids the self-referential guard defect from the prior request.

Before any write, read-only verify the launch-message values for:

- remote work branch HEAD;
- remote work branch tree;
- remote main HEAD/tree;
- remote `production/survey-core-v2` HEAD/tree.

Also verify canonical edition state:

- issue = `SP-vision-multimodal-2026`;
- lifecycle = `CANDIDATES_NORMALIZED`;
- discovery checkpoint = `passed`;
- screening checkpoint = `passed`;
- materiality/completeness/selection/architecture = `pending`;
- Human Architecture Review = `pending`;
- Human Publication Preview = `pending`.

The current Production State intentionally has the machine `evidence` checkpoint still `pending`, because r1 built and canonically accepted Evidence Cards/Views without advancing the bundled Evidence/Materiality/Completeness stage. That is expected for this repair and is not itself a guard mismatch.

If any launch guard or canonical-state condition differs, perform zero writes, report expected vs actual, and stop.

Do not create another branch. No fallback/repair/review/iteration branch.

No reset, rebase, force push, history rewrite, branch recreation or cherry-pick.

---

## 1. Mandatory authorities

Read in this order:

1. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r1.md`
2. `sources/SP-vision-multimodal-2026/execution/evidence-coverage-20260930.md`
3. current accepted Evidence manifest under `sources/SP-vision-multimodal-2026/evidence/v2/accepted/3b183719.../evidence-accepted.json`
4. current accepted Edition Views under `sources/SP-vision-multimodal-2026/evidence/v2/views/accepted/ed7ebf97.../`
5. current `sources/SP-vision-multimodal-2026/production-state.json`
6. current Screening acceptance and Evidence package/task authority surfaces
7. `sources/SP-vision-multimodal-2026/execution/sol-discovery-completeness-review-r1.md`
8. `docs/research-plans/2026-09-30_ts-003-sol-round-e-scope-closure.md`
9. `docs/core-v2-deferred-maintenance-summary.md`, especially CV2-DM-006, CV2-DM-013, CV2-DM-020
10. current Core v2 Evidence builder/validator/acceptor help and source-binding rules

The Sol Evidence Semantic Review r1 is authoritative over r1 coverage/self-validation summaries.

---

## 2. Mission

Perform a **bounded Evidence-only semantic-fidelity repair** over the existing 111 non-DROP Evidence tasks.

Do not rerun Discovery.

Do not rerun or change Screening judgments.

Do not expand topic scope.

Do not attempt to eliminate honest evidence gaps.

The required sequence is:

1. audit r1 Evidence claims against their exact bound source IDs;
2. repair source-binding contamination and epistemic-class errors;
3. correct Molmo 2 openness/license semantics;
4. normalize full-body/abstract/repository consumption accounting;
5. correct World Models historical/lineage overclaim;
6. regenerate corrected Evidence input as an additive r2 artifact;
7. build a **new append-only canonical Evidence result set** from the same canonical Evidence tasks/package;
8. build corresponding new Edition Views;
9. validate the new Evidence acceptance and Views canonically;
10. write additive r2 coverage/session records;
11. stop for Sol Evidence Semantic Review r2.

Target stop:

`CANDIDATES_NORMALIZED / AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2`

Do not advance Production State into Evidence/Materiality/Completeness.

---

## 3. Immutable r1 history

Do not edit or delete the accepted r1 Evidence artifacts under:

`evidence/v2/accepted/3b183719a90976e48daf540989bb88c660622ce9174451ab37b766d272e94727/`

or the accepted r1 Views under:

`evidence/v2/views/accepted/ed7ebf97becda7dcb4b28f77f0c70e7c44b2bc4d8ac1db47f2341de9cf990cde/`

They are audit history.

Do not overwrite the r1 coverage file.

Use additive r2 execution paths, for example:

`sources/SP-vision-multimodal-2026/execution/evidence-semantic-repair-r1-20260930/`

and:

`sources/SP-vision-multimodal-2026/execution/evidence-coverage-r2-20260930.md`

Exact filenames may follow current repository conventions, but history must remain additive.

---

## 4. F1 — exact claim-to-source binding audit

Audit every current/role-bearing Evidence Card and any other Card whose claim context mentions a source not present in its `sources` array.

At minimum inspect all current 2025–2026 system/model/report/repository records and all four-role tagged records.

### 4.1 Qwen3-VL

In r1, VM-D065 binds only the Qwen3-VL arXiv paper but contains repo-derived deployment facts such as FP8 variants, Transformers/vLLM support, Visual Agent/repository deployment surface and repo-expanded context claims.

Repair by either:

- retaining only facts supported by the bound paper in VM-D065; and
- keeping repository/deployment facts in the existing repo-bound VM-D074 Card;

or by using a formally supported canonical multi-source binding if the existing Evidence task actually authorizes both sources.

Do not cite an unbound README through the paper's `src-1`.

### 4.2 Qwen3-Omni

Apply the same rule to VM-D066 vs VM-D075.

If the technical report itself establishes Thinker-Talker, TM-RoPE, audio encoder, theoretical latency, languages/benchmark scope and licensing, those can remain paper claims with exact section support.

README/repository-only deployment facts belong to VM-D075 unless canonically source-bound.

### 4.3 InternVL / Molmo / other current cases

Apply the same audit to InternVL, Molmo 2, Flash-VStream, current VLA, current Computer Use, current benchmark and current World Model cards.

A claim's `source_ids` must point to the authority actually consumed for that claim.

No prose note such as `repo-verified` substitutes for a source binding.

---

## 5. F2 — Molmo 2 openness and licensing

Re-read the exact Molmo 2 paper/repository/license/data surfaces already admitted by Discovery.

Separate:

- code/repository license;
- model-weight license;
- released data availability;
- third-party dataset/data-mixture license or usage restrictions.

The r1 phrase:

`Open weights+data (Apache 2.0)`

must not survive unless the exact authority proves Apache 2.0 applies to all those objects.

VM-D077 currently records data-license mix as unresolved. Preserve that uncertainty if it remains unresolved.

The repaired VM-D071 and VM-D077 Cards must not contradict each other.

---

## 6. F3 — full-body / abstract / repo consumption honesty

Audit all Evidence Cards whose r1 contexts or verification findings contain phrases like:

- `Full report abstract + repo README consumed`
- `Full abstract + repo README consumed`
- `abstract + sections consumed`

while aggregate coverage calls the underlying arXiv source fully consumed.

For each:

### If full paper body was actually consumed

Bind load-bearing architecture/mechanism statements to the relevant paper sections/content and rewrite the verification finding to say what body content was actually checked.

### If only abstract/repository content was consumed

Mark the Card `PARTIAL` where appropriate and update aggregate status/consumption accounting.

Do not optimize for the VERIFIED count.

The r2 aggregate must exactly agree with per-Card semantics.

---

## 7. F4 — evidence-class normalization

Audit claims marked `PRIMARY_FACT` and separate literal source facts from edition-level synthesis.

Statements that are primarily:

- Sol/Muse scope boundary;
- cross-paper non-redundancy judgment;
- lineage synthesis;
- ownership split between TS-001/002/003;
- selection/materiality rationale;
- statement that two systems represent different contracts;

must not be labeled as source-established `PRIMARY_FACT` unless the cited source actually says that fact.

Use the appropriate current-schema inference/synthesis class or move the content to Edition View annotations (`lineage_role`, `branch_ids`, `transition_ids`, `inheritance_note`, `historical_attribution_caveat`) when that is the correct semantic home.

Known examples to repair/check:

- VM-D050 Grounding DINO vs GLIP non-redundancy;
- VM-D066 TS-002/TS-003 generation boundary;
- VM-D101 non-ancestry/lineage synthesis;
- analogous cross-source comparisons elsewhere.

Do not demote genuine source-supported mechanism/results facts.

---

## 8. F5 — World Models lineage wording

For VM-D101:

- do not call the 2018 Ha & Schmidhuber paper the `terminological origin` unless an admitted source actually proves the term originated there;
- use a source-safe role such as a major historical neural-world-model anchor for this edition;
- do not state that technical continuation runs through Dreamer `not Genie` as an exclusive historical claim;
- instead keep distinct branches: Dreamer as latent-dynamics/model-based-decision continuation; JEPA/V-JEPA as predictive-representation counterweight; Genie as interactive-generative environment branch;
- preserve the non-ancestry guard: no direct Ha→Genie technical ancestry should be implied without evidence.

No broad history-of-the-term research expansion is authorized.

---

## 9. Preserve honest gaps

Do not force-close:

- G01 independent VLA evaluation scarcity;
- G02 control-oriented world-model benchmark absence;
- G03 same-protocol document comparison absence;
- G04 real-deployment latency/VRAM evidence scarcity;
- G05 independent reproduction of current scores;
- G06 SigLIP2 exact citation unless a clean admitted primary binding is available at low cost.

Keep existing PARTIAL access/license cases honest.

---

## 10. No scope expansion / no new Discovery by default

The repair should normally use the already admitted Discovery/Evidence authority surfaces.

Do **not** add new Discovery records merely to make r1 Cards easier to support.

If a claim is unsupported by its task authority, prefer deleting/narrowing/moving that claim to the correctly bound existing Card.

If you believe a genuinely load-bearing missing source makes Evidence impossible to repair without Discovery change, stop before writing such a change and report the exact blocker for Sol. Do not silently expand Discovery.

---

## 11. r2 Evidence quality checks

Before acceptance, run explicit semantic checks over the repaired input:

1. every claim's `source_ids` exist in the Card and support the claim;
2. no context/verification text names an unbound source as supporting evidence;
3. repository facts live in repo-bound Cards unless canonical multi-source binding is real;
4. vendor claims remain vendor/author-attributed;
5. paper-measured scores remain author-measured;
6. editorial synthesis is typed as synthesis/inference, not primary fact;
7. date/version/retrieval semantics remain distinct;
8. D07A/D07B metric identities remain separate;
9. document specialist/generalist invalid ranking remains prohibited;
10. World Model four-pole distinction remains intact;
11. TS-001/TS-002 boundaries remain intact;
12. unresolved gaps remain explicit.

---

## 12. Canonical rebuild

Use the current canonical Evidence machinery and the existing canonical task package.

Create a new corrected r2 Evidence input, then:

- validate every corrected Card against its task authority;
- accept a new append-only Evidence result set;
- validate the new Evidence acceptance;
- build new Edition Views bound to the new Evidence hashes;
- accept and validate the new Views.

Do not mutate r1 accepted results in place.

Do not create Materiality Ledger or Profile Completeness.

Do not advance Production State.

---

## 13. Required r2 review surfaces

Write additive artifacts that let Sol audit the repair without diffing hundreds of files blindly.

At minimum provide:

### A. Repair report

For each changed Discovery ID:

- r1 defect class (`SOURCE_BINDING`, `LICENSE_SCOPE`, `CONSUMPTION_DEPTH`, `EVIDENCE_CLASS`, `LINEAGE_WORDING`, etc.);
- exact r1 statement;
- repaired statement/class/source binding;
- why the repair is source-faithful;
- whether status changed VERIFIED↔PARTIAL.

### B. Source-binding audit table

For all current/role-bearing records:

- Discovery ID;
- Card source URLs/classes;
- claim count;
- whether any claim uses repo/vendor facts;
- exact bound source for those facts;
- result PASS/REPAIRED/UNRESOLVED.

### C. r2 coverage

Include:

- 111 task coverage check;
- VERIFIED/PARTIAL counts;
- VM-O01..VM-O16 coverage;
- full-body / abstract / page / repo depth accounting;
- G01..G06 disposition;
- current source-role summary;
- confirmation that Discovery/Screening are unchanged.

---

## 14. Validation / final state

At end, verify:

- current branch contains the new r2 Evidence acceptance and Views;
- old r1 acceptance/Views unchanged;
- lifecycle remains `CANDIDATES_NORMALIZED`;
- discovery checkpoint remains passed;
- screening checkpoint remains passed;
- evidence machine checkpoint remains pending unless current canonical tooling can record Evidence-only completion **without** entering Materiality/Completeness; do not cross the Sol stop boundary merely to change this field;
- Materiality pending;
- Completeness pending;
- Selection pending;
- Architecture pending;
- no Human Gate decision;
- main unchanged;
- frozen Production Core unchanged;
- no new branch;
- no force/reset/rebase/rewrite.

---

## 15. Required final report

Report:

- exact launch guards and actual values;
- r1 Evidence result-set/view hashes;
- r2 Evidence result-set/view hashes;
- changed Discovery IDs;
- each defect class repaired;
- VERIFIED/PARTIAL before vs after;
- source-binding audit summary;
- Molmo licensing disposition;
- World Models lineage disposition;
- G01..G06 status;
- validator results;
- final remote HEAD/tree;
- lifecycle/checkpoint state;
- explicit confirmation that Discovery/Screening/Materiality/Completeness/Selection/Architecture were not advanced or rerun beyond the authorized boundary.

Terminal state:

`TS-003 EVIDENCE_SEMANTIC_REPAIR_R1_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW_R2`

`CANDIDATES_NORMALIZED`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`
