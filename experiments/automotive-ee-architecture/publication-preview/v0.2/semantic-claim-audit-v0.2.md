# Semantic claim / subject-property audit — Publication Preview v0.2

Scope: P01–P08 reader-facing text, including the post-Architecture official-source coverage supplement.

Review basis: prior Issue #191 failure mode (`subject -> component/variant -> property`), claim-class boundaries, and the existing validated baseline structured drafts.

## Findings

- **P01 central/zonal:** BMW, Volvo, and Continental are named separately. BMW's four HPCs, four zones, wiring reduction and zonal-controller description remain bound to BMW Neue Klasse; Volvo's two core computers/OTA remain bound to EX90; Continental's HPC/ZCU responsibilities remain bound to Continental. No value is flattened across OEMs.
- **P02 mixed criticality:** numerical cost/latency results remain explicitly tied to the cited case study; RISC-V World ID counts remain tied to the RISC-V isolation proposal rather than generalized to all HPCs.
- **P03 network:** IEEE 802.1DG status, CiA CAN XL public description, OPEN Alliance 10BASE-T1S scope, and the academic dynamic-TSN measurements stay separate. ISO 11898-1:2024 normative clauses are not reconstructed.
- **P04 service/data:** the VSS paragraph is explicitly phrased as a release-series evolution; it does not imply that every listed feature belongs to every release. vSomeIP 3.7.0 and 3.7.5 properties remain release-bound. AUTOSAR Adaptive Platform service/API/runtime facts are separated from R24-11 release-event topics and from the ROS 2 collaboration paper.
- **P05 open platform:** S-CORE release/maturity statements remain bound to S-CORE. AUTOSAR CAPI is presented as a separate ecosystem; `automotive-grade`, `certification-ready`, interoperability and production-oriented wording are labelled as AUTOSAR/partner project claims, not independent certification evidence.
- **P06 lifecycle:** Mercedes-Benz CLA/MB.OS is used only as a first-party production/lifecycle signal. It is not used to infer the internal vehicle network topology, update failure rate, or safety certification.
- **P07 assurance:** ASIL optimization metrics, RISC-V isolation, DNSSEC/DANE/DANCE service identity, and DENSO/SOAFEE deterministic-runtime claims remain separate subjects with separate limitations.
- **P08 synthesis:** cross-OEM material is explicitly introduced as an editorial synthesis of differently scoped public descriptions and is not presented as proof of a single reference architecture. Baseline standard/project/research limitations remain visible in the final Claim Boundary.

## Result

**PASS with explicit supplement boundary.** No remaining bag-of-tokens or adjacent-component property transfer was identified in the revised reader-facing source. The original P01–P08 structured bodies retain their prior 8/8 structural validation reports; the post-Architecture coverage supplement is separately source-bound in `supplemental-source-audit-v0.2.json` and is not falsely represented as having passed the unchanged production Article Draft validator.
