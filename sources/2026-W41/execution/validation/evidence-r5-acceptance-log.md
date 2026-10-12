# W41 r5 acceptance validation log (frozen Core, exit statuses)

Date: 2026-10-12 JST. No Core/shared-root modification. No monkeypatch of source-class mapping in r5 runtime.

- r5 guarded builder regen → byte-identical to reviewed r4 r2 package (36 tasks + package.json): IDENTICAL_PASS
- r5 double-build (two tmp dirs): IDENTICAL_PASS
- negatives (tenth injection / missing member / unknown type): 3/3 FAIL_CLOSED_PASS
- validate_evidence_package_basis (r2): PASS
- task_authority_sources 36/36 (unmodified Core): PASS
- supplement manifest revalidate (8 entries, raw SHA/bytes): PASS
- interactive r5 input validate (36 records + completeness obligations): PASS
- validate_evidence_card 36/36 with repo_root: PASS (3 VERIFIED / 21 PARTIAL / 12 NEEDS_MORE)
- validate_edition_view 36/36 (accepted-SHA rebuilt): PASS
- accept_evidence_results → evidence/v2/accepted/717ea04a51bda4ab8b1d652d9ca92122e6f67431815c5bd910de15e2bad522db/evidence-accepted.json (36): PASS; validate_evidence_acceptance: PASS
- accept_edition_views → views/accepted/e0a6c921efec0037ffcc3c6708866b22845eb22fe30cf6ae403539c971aac2dc/edition-views-accepted.json (36): PASS; validate_edition_views_acceptance: PASS (36)
- build_materiality_ledger → execution/materiality-ledger-r5.PROPOSED.json (37 rows: 21/13/2/1): PASS (Core-built+validated)
- profile completeness PROPOSED (overall LIMITED): schema PASS; full validate_profile_completeness PASS under agent-tool override + current impl (7741e7d20); without override it reports the known historical screening state-basis drift only.
- r2-vs-r5 card diff audit: non-revised 28 cards differ ONLY in runner-timestamp fields (temporal.observed_at, sources.accessed_at default); substantive edits confined to the 8 supplemented records.
- Non-regression: r1 assets, canonical Discovery/Screening, State, gates untouched (git allowlist verified).
- STOP: no EVIDENCE_REVIEWED transition, no Materiality/Completeness checkpoint PASS, no Selection/Architecture/Draft/PDF/Human Gate.
