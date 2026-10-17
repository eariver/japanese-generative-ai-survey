# W42 r9 — Sol independent editorial claim-to-source corrections

Date: 2026-10-17 JST
Reviewed branch HEAD: 4a1cb6b9df5a7b64bacdcd881af201e7bf0d28a1.
Status: SOL_EDITORIAL_ERRATA / MANDATORY_FOR_DRAFT / NON_CORE_ARTIFACT.
Source under review: execution/claim-to-source-crosswalk-r9.md (Muse r9). This overlay **takes precedence over Muse's draft-usage labels** for the affected individual claims; the original r9 crosswalk is retained verbatim as historical evidence. This overlay does not overwrite frozen Core, accepted Evidence/Views, Materiality, Selection, machine checkpoints or Architecture. It is not a machine-validation waiver nor a Human gate approval.

## A. Independently reproduced finding

Parsed all **117 individual selected-claim** entries from the r9 crosswalk. They point to **62 distinct best URLs across 28 hostname domains**, while accepted Cards often overbind multiple sources to a claim. Six **FIRST_PARTY_VENDOR** entries are incorrectly labeled PROMOTABLE_AS_INDEPENDENT. One further AUTHOR_CLAIM has only an NVIDIA blog pointer for a purported independent EXO Labs analysis whose original method/details were not fetched. Four FIRST_PARTY_VENDOR entries are labeled PROMOTABLE_AS_VERIFIED_TEXT; three of these are not LICENSE-file texts and give inappropriate boilerplate about quoting legal clauses (LFM performance, Nemotron product/future, AI Scan product advisory). A mixed Wonder C7 entry uses a social evidence class yet links vendor pricing, an independent-sounding AA index score and Grok observations into one paragraph. One ASPIRE repository existence card has generic license-file drafting instructions inappropriate for a generic GitHub repo URL.

The source-type annotation or schema PASS never independently establishes the truth of performance benchmarks or the identity of an external evaluator. Follow the exact correction table. A source's first-party vendor status means **the vendor said it**, not that a non-vendor reproduced it.

## B. Mandatory per-claim corrections to r9 crosswalk

| Pkg / discovery ID / claim | Original wrong draft-use interpretation | Correct reviewed disposition |
|---|---|---|
| P1 gemini4-argon C1 | Independent | **VENDOR_CLAIM** from official Google release; pricing, availability, deployment figures attributed to Google; a Vals rank quoted *by Google* is NOT independently checked Vals evidence until the evaluator's own dated result/method is fetched. |
| P2 lfm25 C2 | Independent | **VENDOR_SELF_DISCLOSURE** (reward-hacking report from Liquid AI), not independent red-team verification. State mitigation is vendor-described, not independently validated. |
| P3 beam C3 | Independent | **VENDOR_SAFETY_EVALUATION** from Reflection's own report. Any cited OSF/third-party assurance is vendor-reported until actual third-party methods/outcome are separately retrieved. |
| P3 nemotron35 C6 | Independent (EXO Pareto) | **NON_PROMOTABLE_AS_INDEPENDENT**; the stated EXO evaluation details were unfetched, and the best URL is an NVIDIA blog. Omit any independent Pareto number or positive result from draft. May state at most 'NVIDIA references an external comparison which this issue did not verify', but this is usually not newsworthy. No materiality/role change. |
| P5 anthropic-unintended C4 | Independent | **VENDOR_INCIDENT_DISCLOSURE** from Anthropic; URL-shortener operator account could be independently corroborated only for the precisely corroborated subevent upon retrieving its original account, not all surrounding claims. |
| P5 anthropic-unintended C5 | Independent | **VENDOR_INCIDENT_SELF_ASSESSMENT** from Anthropic: minimal impact/no customer access must be written as 'Anthropic says/according to its investigation', never independently verified. |
| P2 lfm25 C4 | Verified legal text | **VENDOR_PRODUCT_BENCHMARK+PRICING** from Liquid AI blog. Bench, throughput and price claims are vendor-reported with exact stack, hardware, batch and timestamp; no 'quote operative license terms' boilerplate here. |
| P3 nemotron35 C5 | Verified legal text | **VENDOR_PRODUCT_AVAILABILITY / LIMITED_LICENSE_EVIDENCE**. NVIDIA blog describes Bolt shipment/future date; Super VL license FILE remains unopened. Do not claim official license file full-text verified. |
| P4 ai-scan C2 | Verified legal text | **FIRST_PARTY_PRODUCT_DOCUMENTATION**: GitHub changelog grounds advisory-only/eligibility/limits; not third-party verification or a license-file quotation. |
| P1 muse-wonder C7 | Undifferentiated vendor citation for mixed social/price/rank | **SPLIT or OMIT unsupported subclauses**. Official Meta dev page supports stated pricing/access only; AA Index 52/56 needs the AA evaluator's own exact method/dated page to be used as independent ranking; Grok X #4/#15 supports reported post existence, NOT benchmark magnitude or original authorship. No uncited combined independent ranking. |
| P7 aspire C1 | Generic 'quote LICENSE operative terms' | **REPOSITORY_EXISTENCE+AUTHOR_CLAIM**. Public NVlabs/ASPIRE GitHub URL supports repository existence, not automatic completeness of license ownership for every third-party component. Present June 30 paper as old context and Oct 16 X report as announcement with qualified post-authorship. |

Reviewed and retain **valid** verified-text use only for genuinely consumed license terms with correct tiers: LFM family terms from publisher site (24B model file not checked); Beam Apache 2.0 full repo LICENSE file; FLUX Kommunity full license file; Muse operative terms from model page/mirror rather than original full LICENSE byte archive. Granite/MiniCPM Apache tags remain TAG-only. The **one genuine independent evaluator URL** in selected crosswalk is Vals' own GLM-Legal page (AUTHOR_CLAIM; methodology/repro limits still apply), not six self-disclosed vendor items.

## C. Corrected editorial promotion accounting

The original 117 crosswalk entries are **not 117 independently verified facts**. One entry (Nemotron/EXO C6) is explicitly **NON_PROMOTABLE_AS_INDEPENDENT**; other mixed or mismatched entries can be reported only after segmentation/qualification. There are 116 potentially publishable source-linked claim entries after the EXO omission, **conditioned on attribution and draft-level source checks**, not 116 fully verified claims. Do not repeat the r9 footer '0 NON_PROMOTABLE' without this erratum.

Do not alter Sol's established selection: 28 SELECTED, 5 INSPECT, 7 HOLD, 10 REJECT, seven packages. No original machine artifact rewrite. If new full-body or method sources change whether a selected centerpiece is actually justified, flag Sol for a fresh review before drafting that centerpiece.

## D. One attention-list overflow

Frozen Architecture Attention has 51 total items, display limit 50, overflow 1. Independently compared all 22 non-selected Selection assignments: the omitted display row is REJECT Qwen-Image-2.1-Turbo, excluded as an out-of-window weight release with only press-level in-window API mentions and no fresh technical event. This decision **is present in Candidate Selection and Architecture Review Summary**; overflow is a display cap, not a lost assignment. Explicitly mention the 51/50 cap and the omitted item's outcome in Human dossier.

## E. Draft acceptance instructions

1. Treat Muse r9 crosswalk as **unreviewed except as amended here**, and resolve each claim to its best direct URL, source author and publication date.
2. Vendor results always carry evaluator/benchmark conditions; a third party must be genuinely primary to be labeled independent. Composite claims must be split by authority.
3. No numeric or license condition beyond reviewed evidence: quote terms only against actual read license texts, not tag-only metadata; do not claim OpenMDW-1.1 OSI approved.
4. Reader-facing Japanese must not mechanically translate English Architecture headings; translate technical concepts precisely and allocate explanatory substance without padding.
5. Materiality/Architecture remain accepted as machine artifacts, but Human Architecture approval is a **separate** explicit decision pending now. This errata is not approval.
