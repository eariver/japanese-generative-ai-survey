# W42 Sol Independent Evidence Authority Review r6 — CONDITIONAL RESEARCH PASS

Date: 2026-10-17 JST
Reviewed remote HEAD: `68d5d6a36b6ef5913b152153a54a64a2aae516fb`
Branch: `weekly/2026-W42-v2-work`
Reviewed main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`
Frozen Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
Verdict: **`SOL_EVIDENCE_RESEARCH_DEPTH_PASS_WITH_REPAIRS / CORE_EVIDENCE_ACCEPTANCE_NOT_YET_GRANTED`**.

## 1. What passes independent review

- Accepted Discovery (50 records, 49 substantive + Grok provenance-only ledger) and Screening (50; 29 KEEP includes provenance ledger, 16 INSPECT, 5 MAYBE) remain unchanged, `CANDIDATES_NORMALIZED`. Shared Core/main unchanged; neither Human Gate touched.
- The r6 `evidence-cards-r6.PROPOSED.json` contains exactly 49 substantive candidate cards and 151 distinct claim strings: min 1, median 3, max 8, up from 68 r4 claims. Zero cards lack claims. Source-kind tally: VENDOR 140, INDEPENDENT 4, SECONDARY 7. These are **research claim-label counts**, not 151 independently confirmed facts.
- Muse Wonder now includes newly read Prometheus/Harvey/FocusBench/SWE-Marathon/OOD/safety primary research claims. Argon Minecraft paper arXiv:2610.22319 (submitted Oct 15 2026 per arXiv) is now tied to four-agent method and limitations. The original X demo isn't misclassified as independent benchmark.
- r6 derived corpus documents full text for **two** license files (FLUX Kommunity, Beam Apache 2.0); three license families' **operative terms** (Muse, OpenMDW-1.1, LFM Open 1.0); two Apache-tag-only models (Granite and MiniCPM). Do not describe these as seven full LICENSE-file reads.
- Read substantive methods for PAT, Earth AI, VERID/aptamer/epitope wet-lab papers, Nemotron report, Beam safety; additional Sakana/Amazon/Minecraft account and independent critical review, with declared boundaries. Extensive bounded retries improved Fish, ASPIRE, Decider, NVIDIA OCP and other INSPECT candidates. No fabricated independent reproduction is claimed.
- 50th Grok-X ledger is explicitly non-editorial. `SOL_RESEARCH_SATURATION_PASS` for the high-material corpus *subject to accurate unresolved citations and bounded HOLDs*. Do not re-run general research merely to increase counts.

## 2. Required precision repairs BEFORE formal Core Evidence acceptance

**E42-R6-A — Not all 151 claims have resolvable source URIs.** Direct inspection finds **20** claim-source entries not expressed as exact HTTP(S) URLs. Some are valid internal provenance hints (`grok:weekly-x-2026-W42.md#...`, `x:<user>/status/...`), but others are `analyst-note`, `developer.nvidia.com citation`, a malformed `https://3druck.com SMLIB article 2026-10-13`, or other non-dereferenceable shorthand. Convert every external source to exact retrievable URL where possible; internal evidence to exact repo file path/hash + appropriate separate editorial provenance; don't use analyst interpretation as primary/vendor authority. Make per-claim trace valid under REAL Core schema. Preserve faithful raw report and no fake direct original X validation.

**E42-R6-B — Contradictory stale limitations.** The r6 cards still say `Research blog ... pending` (Wonder) despite resolved research-body target; `report PDF` pending (Nemotron) despite tech-report extraction; `license text` pending (FLUX) despite full license read; wet-lab card still says `3 PDFs unfetched` even though all three were extracted; MiniCPM `license UNCONFIRMED` needs distinguish tag-confirmed vs FILE-unverified. Reconcile every limitations/verification-target pair against real read statuses. Never hide genuinely unread full methods/reports.

**E42-R6-C — Four authority states misapplied to whole candidates.** Of 13 `AUTHORITY_CAPTURED_BUT_UNCONSUMED` candidate labels, examples Claude perf, NVIDIA OCP, LeChonk and AWS Bedrock already contain extracted bounded claims from read official pages/posts. Under governance §4.2, the consumed part is `AUTHORITY_CONSUMED`, while distinct unresolved primary target may be linked-but-unretrieved or retrieval-failed. Record per-source/per-claim state, not one blanket candidate state based on any remaining gap. `NOT_FOUND` for harness-17 is research-specific and may remain. The missing primary-source metadata must not be disguised as captured.

**E42-R6-D — Derivation-kind and license status precision.** The paper, primary marketing, actual LICENSE, third-party review and Sol editorial inference are different classes. Correct `VENDOR` kinds for purely editorial `analyst-note` claims. An embedded X summary does not itself independently validate a vendor result. **OpenMDW-1.1**: license terms are permissive, but OSI approval cannot be asserted based merely on the license name/Linux Foundation authorship. OSI's August 2026 public license-review correspondence shows a *submission for approval*, not a completed approval decision. Validate current approval before using `OSI-approved`, else state `OSI approval not established`. Beam Apache 2.0 is a license status, not a guarantee every training artifact or model is wholly open-source.

**E42-R6-E — Edition Views remain generic.** r6 49 `edition-views` are formulaic (`r6 AUTHORITY_CONSUMED, N linked claims; no selection implied`) and not usable as substantive reader-facing comparison/disposition. Regenerate meaningful technical views from accepted candidate evidence before Materiality/Selection. Include practical model tradeoffs, performance methodology, agent safety, original research novelty, and causal implications — not just counts.

## 3. Remaining justified limits

- No independent reproduce-on-hardware measurements were performed; report vendor measurements as vendor results, independent publications as independently authored review (not necessarily independent reproducibility).
- Some source full-license bytes, eval appendices and model repo first-party LICENSE files remain unavailable; mark precise file-level boundaries.
- Some low-evidence X leads or outside-window papers remain HOLD/CONTEXT only. Avoid elevating without fresh source.
- Core Evidence is **pending** and 49 r6 cards are local `PROPOSED_NOT_ACCEPTED__LOCAL_SHAPE_NOT_CORE_SCHEMA`; the research PASS is not a validation of schema, stage or machine VERIFIED outcomes.

## 4. Authorized next execution boundary

A consolidated Muse unit may **first repair E42-R6-A..E and locally revalidate complete claim/authority/source chains**, then use frozen Core v2 to prepare and *conditionally* accept Evidence ONLY if full Core schema, factual/provenance and mandatory stage guards genuinely PASS. If the corrections fail, stop with exact error and keep Core Evidence pending. Do not waive or auto-promote sourceless claims.

After lawful Evidence acceptance, Muse may build substantive Materiality and Completeness assessment packages and explicit, non-binding Selection proposals. These require an independent Sol **materiality and positive/negative selection review** before Architecture; the executor must not infer its own final editorial authority. Stop `SOL_MATERIALITY_SELECTION_REVIEW_READY`, or earlier if a real gate blocks. No Architecture acceptance, Human Architecture Gate, Draft/TeX/PDF, Publication Preview or release.

Rationale: preserve meaningful research progress, avoid another narrow authority-retrieval loop, but do not allow source/provenance ambiguities to become accepted evidence or generic edition views to dictate Architecture.
