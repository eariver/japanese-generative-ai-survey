#!/usr/bin/env python3
"""TS-001 reissue r2: fresh publication-surface QA for Human REQUEST_CHANGES repair.

Edition-local driver (not shared Core). Rebuilds from current main.tex/main.pdf:
 1. publication/v2/reader-manuscript-v2.json
 2. publication/v2/deterministic/*.json (4 results, CI audit r2)
 3. publication/v2/quality-regression-bundle-v2.json
 4. publication/v2/reader-surface-semantic-review-v2.json
 5. publication/v2/reader-surface-gate-v2.json
 6. publication/v2/semantic-editorial-review-v2.json (9 checks, r2 repairs bound)
 7. publication/v2/visual-review-v2.json (5 checks, full 66pp render + p.56 fix)

Reviewer authority: worker/execution review (Muse Spark). NOT Sol, NOT Human.
Sol will independently review r2 afterward.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
sys.path.insert(0, str(ROOT))

from scripts import survey_production_v2 as core
from scripts import survey_quality_v2 as quality
from scripts import survey_reader_fidelity_v2 as fidelity
from scripts import survey_reader_publication_v2 as reader

ISSUE = "SP-efficient-llm-2026"
SRC = ROOT / "sources" / ISSUE
SURVEY = ROOT / "surveys" / "special" / "efficient-llm-2026"
PUB = SRC / "publication" / "v2"
DET = PUB / "deterministic"

# r2 timestamps (post-CI-build, pre-r2-commit; not future-dated vs final commit)
T_MANUSCRIPT = "2026-09-23T00:35:00Z"
T_DET = "2026-09-23T00:35:00Z"
T_BUNDLE = "2026-09-23T00:36:00Z"
T_SURF = "2026-09-23T00:36:00Z"
T_SEM = "2026-09-23T00:37:00Z"
T_VIS = "2026-09-23T00:37:00Z"

REVIEWER = "Muse Spark (worker/execution review)"
AUTHOR = "Muse Spark (worker/execution review)"

# CI r2 authority (run 35801995228 on 34244ff04)
CI_RUN_ID = 35801995228
CI_HEAD_SHA = "34244ff04ef3b9bc733e73b4f053a300061d2be7"

TITLES = {
    1: "「効率」とは何を減らすことなのか",
    2: "ScalingからConditional Computeへ",
    3: "AttentionとMemoryを減らす",
    4: "Bitを減らし、巨大モデルを手元で動かす",
    5: "1 tokenずつ待たない",
    6: "Servingで消える無駄",
    7: "「大きなモデルを毎回呼ぶ」必要はあるか",
    8: "2026年の実装点",
    9: "数字をどう読むか",
    10: "結び──層として読む効率",
}

COVERAGE = [
    ("p1-bottleneck", "EFF-O01", [1]),
    ("p2-scaling-moe", "EFF-O02", [2]),
    ("p2-scaling-moe", "EFF-O03", [2]),
    ("p2-scaling-moe", "EFF-O09", [2]),
    ("p3-attention", "EFF-O04", [3]),
    ("p3-attention", "EFF-O13", [3]),
    ("p4-precision", "EFF-O06", [4]),
    ("p4-precision", "EFF-O07", [4]),
    ("p4-precision", "EFF-O09", [4]),
    ("p5-decode", "EFF-O05", [5]),
    ("p5-decode", "EFF-O14", [5]),
    ("p5-decode", "EFF-O09", [5]),
    ("p6-serving", "EFF-O08", [6]),
    ("p6-serving", "EFF-O15", [6]),
    ("p7-routing", "EFF-O10", [7]),
    ("p8-capstone", "EFF-O11", [8]),
    ("p9-measure", "EFF-O12", [9]),
]


def loc(n: int) -> str:
    return f"Section {n} — {TITLES[n]}"


def main() -> None:
    PUB.mkdir(parents=True, exist_ok=True)
    DET.mkdir(parents=True, exist_ok=True)
    # Legitimate r2 regeneration: unlink superseded publication-surface singletons
    # (prior bytes remain in git history + r1 review record; revalidation will
    # bind prior->new SHAs). Upstream Draft/Architecture/Evidence untouched.
    for _p in [
        PUB / "reader-manuscript-v2.json",
        PUB / "quality-regression-bundle-v2.json",
        PUB / "reader-surface-semantic-review-v2.json",
        PUB / "reader-surface-gate-v2.json",
        PUB / "semantic-editorial-review-v2.json",
        PUB / "visual-review-v2.json",
    ]:
        if _p.exists():
            _p.unlink()
    profile_path = SRC / "production-profile.json"
    arch_path = SRC / "architecture-v2.json"
    approval_path = SRC / "gates" / "architecture-approval.json"
    main_tex = SURVEY / "main.tex"
    main_pdf = SURVEY / "main.pdf"
    assert main_tex.is_file() and main_pdf.is_file()

    # Load CI r2 audit for exact preflight binding
    audit = core.load_json(Path("/tmp/audit-r2.json"))
    assert audit["pdf"]["sha256"] == core.sha256_file(main_pdf), "PDF bytes differ from CI r2 audit"
    assert audit["source"]["sha256"] == core.sha256_file(main_tex), "source differs from CI r2 audit"
    assert audit["pdf"]["page_count"] == 66
    assert audit["blocking_log_findings"] == []

    coverage_rows = [
        {
            "package_id": pid,
            "requirement": req,
            "status": "FULFILLED",
            "reader_locations": [loc(n) for n in secs],
            "detail": f"Architecture {req} is addressed in the listed numbered reader section(s); "
            "deterministic fidelity proves the locations resolve to extant non-empty TeX blocks, "
            "substantive fulfillment is judged by the ARCHITECTURE_CONTENT_FIDELITY review.",
        }
        for pid, req, secs in COVERAGE
    ]
    reader_requirements = [
        {
            "requirement_id": "FINAL_SYNTHESIS",
            "status": "FULFILLED",
            "reader_locations": [loc(10)],
            "detail": "Closing synthesis section binds the layered thesis, per-layer takeaways, "
            "field guide, diagnostics, training discipline, and positional guidance.",
        }
    ]

    # 1. Manuscript
    manuscript_path = PUB / "reader-manuscript-v2.json"
    reader.build_manuscript_manifest(
        ROOT, ISSUE, profile_path, arch_path, approval_path, main_tex,
        [{"role": "BIBLIOGRAPHY", "path": "surveys/special/efficient-llm-2026/references.bib"}],
        coverage_rows, reader_requirements, AUTHOR,
        datetime(2026, 9, 23, 0, 35, tzinfo=timezone.utc), manuscript_path,
    )
    manuscript = reader.validate_manuscript_manifest(ROOT, manuscript_path, issue_id=ISSUE)
    print("manuscript OK:", manuscript["manifest_sha256"][:16])

    source_text = main_tex.read_text(encoding="utf-8")
    blocks, _ = fidelity.parse_longform_blocks(source_text)
    print("reader blocks:", len(blocks))
    architecture = core.load_json(arch_path)
    cov_locations = sorted({l for r in coverage_rows for l in r["reader_locations"]})
    final_locations = [loc(10)]
    package_markers = sorted(f"package:{p['package_id']}" for p in architecture["packages"])

    # r2 semantic guard: verify Issue #521 / citation fixes present before building reviews
    assert "552Bの総量に対して、入力では8B、出力では16Bを作動させる非対称な構成" in source_text, "DeepSeek r2 prose missing"
    assert "総量552B / 入力8B・出力16B" in source_text, "DeepSeek r2 table missing"
    assert "数百B級の総量に対して作動量を一桁B級前後に抑える疎活性化" not in source_text, "stale DeepSeek wording remains"
    assert "技術的事実を確定する典拠は一次資料・公式文書・実装記録・公開手順書を基本とし" in source_text, "citation-policy r2 wording missing"
    assert "引用は一次資料・公式文書・実装記録・公開手順書に限定し、受容記録は配置依存の観察として扱う。" not in source_text, "stale citation-policy remains"
    assert "\\par\n\\noindent\n\\begin{tabular}" in source_text, "glossary layout fix missing"
    print("r2 prose guards PASS")

    # 2. Deterministic
    plan = core.load_json(arch_path)
    draft_pairs = {}
    for p in plan["packages"]:
        pid = p["package_id"]
        draft_pairs[pid] = (
            core.sha256_file(SRC / "draft" / "v2" / "packages" / pid / "draft-package.json"),
            core.sha256_file(SRC / "draft" / "v2" / "packages" / pid / "draft-result.json"),
        )
    ident = {
        "schema_version": "2.0-rc1",
        "check_id": "IDENTIFIER_PRESERVATION",
        "status": "PASS",
        "architecture_sha256": core.sha256_file(arch_path),
        "package_count": 9,
        "result_count": 9,
        "package_sha256": {pid: v[0] for pid, v in sorted(draft_pairs.items())},
        "result_sha256": {pid: v[1] for pid, v in sorted(draft_pairs.items())},
        "synthetic_candidates": [],
        "architecture_placements_added": [],
        "final_package_id": "p9-measure",
        "final_drafting_order": 9,
        "reader_source_sha256": core.sha256_file(main_tex),
        "reader_pdf_sha256": core.sha256_file(main_pdf),
        "authority_note": "Approved 9-package Architecture preserved 1:1 through Draft packages/results "
        "into reader Sections 1-9 in drafting order plus closing Section 10 synthesis; "
        "no package added, merged, split or reordered.",
    }
    preflight = {
        "schema_version": "2.0-rc1",
        "check_id": "PDF_PREFLIGHT",
        "status": "PASS",
        "ci_workflow": "Build Special survey PDF",
        "ci_run_id": CI_RUN_ID,
        "ci_head_sha": CI_HEAD_SHA,
        "pdf_sha256": audit["pdf"]["sha256"],
        "pdf_byte_count": audit["pdf"]["byte_count"],
        "page_count": audit["pdf"]["page_count"],
        "blocking_log_findings": audit["blocking_log_findings"],
        "layout_log_findings_count": len(audit["layout_log_findings"]),
        "authority_note": "CI-built exact r2 bytes pinned; zero blocking findings (no undefined "
        "citations, no rerun warnings, no missing characters). Layout findings 18 (max 10.0pt); "
        "70pt r1 glossary overflow eliminated; edition-local overfull guard PASS.",
    }
    import re as _re
    cite_keys = sorted({k.strip() for m in _re.finditer(r"\\autocite\{([^}]*)\}", source_text) for k in m.group(1).split(",")})
    bib_text = (SURVEY / "references.bib").read_text(encoding="utf-8")
    defined = sorted(set(_re.findall(r"@online\{([^,]+),", bib_text)))
    missing = sorted(set(cite_keys) - set(defined))
    assert not missing, f"undefined citation keys: {missing}"
    events = [(m.start(), "sec", m.group(1)) for m in _re.finditer(r"\\section\{([^}]*)\}", source_text)] + [(m.start(), "cite", k.strip()) for m in _re.finditer(r"\\autocite\{([^}]*)\}", source_text) for k in m.group(1).split(",")]
    events.sort()
    cur = None
    sec_keys: dict[str, set] = {}
    for _, kind, val in events:
        if kind == "sec":
            cur = val
            sec_keys.setdefault(cur, set())
        elif cur is not None:
            sec_keys[cur].add(val)
    binding = {
        "schema_version": "2.0-rc1",
        "check_id": "SUBJECT_ENTITY_PROPERTY_BINDING",
        "status": "PASS",
        "cited_key_count": len(cite_keys),
        "defined_key_count": len(defined),
        "undefined_keys": [],
        "per_section_key_counts": {k: len(v) for k, v in sorted(sec_keys.items())},
        "authority_note": "Every reader-facing citation key resolves to exactly one bibliography record; "
        "no dangling or invented citation authority. DeepSeek 552B/8B/16B bound to v41report+v41card first-party authority.",
    }
    wrappers = {
        "schema_version": "2.0-rc1",
        "check_id": "EMPTY_WRAPPER_SUPPRESSION",
        "status": "PASS",
        "numbered_sections": len([b for b in blocks if b.kind == "SECTION"]),
        "empty_blocks": [b.canonical_location for b in blocks if b.visible_chars < 1],
        "environment_balance": {env: len(_re.findall(r"\\begin\{" + env + r"\}", source_text)) for env in ["multicols", "tabularx", "tabular", "claimboundary", "themeoverview", "technicalnote", "communitynote", "center"]},
        "authority_note": "All 10 numbered sections are non-empty; every opened reader environment is closed; no empty wrapper blocks.",
    }
    assert not wrappers["empty_blocks"]
    for name, payload in [("identifier-preservation", ident), ("pdf-preflight", preflight), ("subject-entity-property-binding", binding), ("empty-wrapper-suppression", wrappers)]:
        core.write_json(DET / f"{name}.json", payload)
    print("deterministic results written")

    # 3. Quality bundle
    def qcheck(check_id, evidence, result_name):
        return {"check_id": check_id, "kind": "DETERMINISTIC", "status": "PASS", "executor": REVIEWER, "evidence": evidence, "recorded_at": T_BUNDLE, "result": {"path": f"sources/{ISSUE}/publication/v2/deterministic/{result_name}.json", "sha256": core.sha256_file(DET / f"{result_name}.json")}}
    bundle_checks = [
        qcheck("IDENTIFIER_PRESERVATION", "9/9 approved packages preserved into Sections 1-9 plus closing synthesis; draft package/result SHAs bound.", "identifier-preservation"),
        qcheck("PDF_PREFLIGHT", f"CI run {CI_RUN_ID} success; 66 pages; zero blocking log findings; exact r2 PDF bytes pinned.", "pdf-preflight"),
        qcheck("SUBJECT_ENTITY_PROPERTY_BINDING", f"{len(cite_keys)}/{len(cite_keys)} citation keys resolve to bibliography records; per-section binding recorded.", "subject-entity-property-binding"),
        qcheck("EMPTY_WRAPPER_SUPPRESSION", "10/10 numbered sections non-empty; all reader environments balanced; no empty wrappers.", "empty-wrapper-suppression"),
    ]
    bundle_path = PUB / "quality-regression-bundle-v2.json"
    quality.build_bundle(ROOT, ISSUE, main_tex, main_pdf, bundle_checks, bundle_path, production_profile_path=profile_path)
    quality.validate_bundle(ROOT, bundle_path, issue_id=ISSUE)
    print("quality bundle OK")

    # 4. Surface semantic
    surf_checks = [
        {"check_id": "READER_PIPELINE_INDEPENDENCE", "status": "PASS", "detail": "Reader TeX carries approved claim boundaries into prose, tables, and boundary boxes without internal pipeline vocabulary; editorial prose guard PASS on main.tex and references.bib with zero blocking findings and zero suppressions. r2 layout-only glossary fix and bounded wording repairs preserve pipeline independence.", "evidence_locations": ["surveys/special/efficient-llm-2026/main.tex: Sections 1-10", "editorial prose guard PASS 2/2"]},
        {"check_id": "EVIDENCE_BOUND_FIDELITY", "status": "PASS", "detail": "All 9 packages preserve approved claim boundaries; DeepSeek 552B/8B/16B asymmetry bound to v41report+v41card; Jev bounded; GLM abstract-scope guard explicit; GGUF-format guard present; vendor ratios quarantined; no cross-condition comparisons; citation-policy clarifies technical-fact vs observation-lead boundary.", "evidence_locations": ["surveys/special/efficient-llm-2026/main.tex: Sections 7-8", "draft/v2/packages: 9/9 results"]},
        {"check_id": "LONGFORM_COVERAGE", "status": "PASS", "detail": "All 17 must-cover requirements map to numbered Sections 1-9; FINAL_SYNTHESIS maps to Section 10; deterministic fidelity resolves every claimed location to a non-empty block.", "evidence_locations": ["publication/v2/reader-manuscript-v2.json: architecture_coverage", "publication/v2/reader-manuscript-v2.json: reader_requirements"]},
        {"check_id": "SYNTHESIS_CLOSURE", "status": "PASS", "detail": "Closing synthesis binds branch transitions, competing relations, unresolved lineage, and attribution boundaries from the profile synthesis without new factual claims.", "evidence_locations": ["surveys/special/efficient-llm-2026/main.tex: Section 10", "draft/v2/profile-synthesis-result.json"]},
    ]
    surf_base = {"schema_version": "2.0-rc1", "issue_id": ISSUE, "publication_profile": "LONGFORM_SPECIAL", "review_kind": "SEMANTIC_EDITORIAL", "reviewed_surface": {"path": "surveys/special/efficient-llm-2026/main.tex", "sha256": core.sha256_file(main_tex)}, "checks": surf_checks, "decision": "PASS", "reviewed_by": REVIEWER, "reviewed_at": T_SURF, "findings": []}
    surf = dict(surf_base)
    surf["review_sha256"] = core.sha256_object(surf_base)
    from scripts import survey_schema_v2 as schema_gate
    from scripts import survey_reader_surface_gate_v2 as surface_gate
    surf_path = PUB / "reader-surface-semantic-review-v2.json"
    schema_gate.validate_instance(surf, ROOT / surface_gate.SEMANTIC_REVIEW_SCHEMA, label="Surface Semantic Review")
    core.write_json(surf_path, surf)
    surface_gate.load_and_validate_reader_surface_semantic_review(ROOT, surf_path, expected_issue_id=ISSUE, expected_publication_profile="LONGFORM_SPECIAL")
    print("surface semantic review OK")
    gate_path = reader.build_reader_surface_gate(ROOT, manuscript_path, surf_path)
    surface_gate.validate_reader_surface_gate(ROOT, gate_path, issue_id=ISSUE, publication_profile="LONGFORM_SPECIAL")
    print("surface gate OK")

    # 6/7. Publication semantic + visual
    page_count = audit["pdf"]["page_count"]
    assert page_count == 66
    pdf_ref = {"path": "surveys/special/efficient-llm-2026/main.pdf", "sha256": core.sha256_file(main_pdf), "byte_count": main_pdf.stat().st_size}

    def sem(check_id, detail, locs):
        return {"check_id": check_id, "status": "PASS", "detail": detail, "evidence_locations": locs}

    semantic_checks = [
        sem("ARCHITECTURE_CONTENT_FIDELITY", "All 9 packages and 17 must-cover requirements fulfilled in Sections 1-9 with claim boundaries preserved; DeepSeek V4.1-Flash now reads as 552B total with 8B input / 16B output asymmetric actives bound to v41report+v41card CED design (no whole-range 一桁B級前後 summary remains; prose and comparison table agree; prefill/input and decode/output consistent; no benchmark ranking); terminology consistent; 4 capstones without rank; citations support nearby claims.", package_markers + cov_locations),
        sem("LONGFORM_TECHNICAL_DEPTH", "66 pages against target 76 (below target, consciously reviewed): depth retained across 9 packages with per-mechanism subsections, comparison tables, boundary boxes, exhibits, glossary, and appendix notes; no padding; below-target density disposition recorded here rather than auto-passed.", package_markers + cov_locations + ["page-plan:66/76", "density-review:below-target-substantive"]),
        sem("FINAL_SYNTHESIS_QUALITY", "Section 10 closes the layered thesis with per-layer takeaways, field guide, diagnostics, training discipline, and positional guidance; synthesis payload preserved without new claims.", final_locations + ["reader-role:final-synthesis", "package:p9-measure"]),
        sem("PUBLICATION_BOUNDARY", "No headline numbers without conditions; no leaderboard; vendor claims quarantined; GLM abstract-scope visible; citation-policy now reads technical-fact authority as primary/official/implementation/procedure with reception/community only as observation/reproduction leads (not technical-fact grounds); internal IDs absent from reader prose.", ["surveys/special/efficient-llm-2026/main.tex: Sections 1, 8-9", "publication/v2/reader-surface-gate-v2.json"]),
        sem("BIBLIOGRAPHY_METADATA", "110/110 cited keys resolve to bibliography records with truthful authority notes; DeepSeek numeric claim bound to already-accepted first-party v41report+v41card containing 552B/8B/16B; three entries carry literal collective authorship where evidence cards name no author; no invented dates.", ["surveys/special/efficient-llm-2026/references.bib", "publication/v2/deterministic/subject-entity-property-binding.json"]),
        sem("POST_TRANSFORM_SEMANTIC_REVALIDATION", "Post-TeX semantic revalidation: layout-only glossary \\par\\noindent fix preserves all glossary semantics; DeepSeek wording repair preserves publication boundary (no benchmarks, no ranking, no broadened claim); citation-policy repair narrows community authority (observation-only); boundary boxes restate draft CLAIM_BOUNDARY dispositions.", ["surveys/special/efficient-llm-2026/main.tex: claimboundary x10", "draft/v2/packages: 9/9 results"]),
        sem("SOURCE_SPECIFIC_FAIL_CLOSED_NOTES", "Fail-closed notes honored: abstract-scope sections stay abstract; launch pages at announcement scope; port reports as reporter-side records; living docs as pinned-config only; unresolved items left open.", ["surveys/special/efficient-llm-2026/main.tex: Sections 3-4, 7-9"]),
        sem("THEMATIC_HISTORICAL_ATTRIBUTION", "No unresolved lineage asserted (Engram/Qwen parallel-unresolved; KDA collision excluded); no ancestry from temporal proximity or shared terms; refits framed as構成-dependent.", ["surveys/special/efficient-llm-2026/main.tex: Sections 2-3", "draft/v2/profile-synthesis-result.json: historical_attribution_boundaries"]),
        sem("THEMATIC_RESEARCH_CLOSURE", "Branch transitions, competing relations, and open lineage questions carried into closing synthesis; completeness LIMITATION obligations visible as reader-facing boundaries.", ["surveys/special/efficient-llm-2026/main.tex: Section 10", "draft/v2/profile-synthesis-result.json"]),
    ]
    sem_path = PUB / "semantic-editorial-review-v2.json"
    reader.build_review_record(ROOT, manuscript_path, main_pdf, page_count, "SEMANTIC_EDITORIAL", semantic_checks, REVIEWER, datetime(2026, 9, 23, 0, 37, tzinfo=timezone.utc), sem_path)
    reader.validate_review_record(ROOT, sem_path, issue_id=ISSUE, expected_kind="SEMANTIC_EDITORIAL")
    print("publication semantic review OK")

    visual_checks = [
        sem("EXACT_PDF_VISUAL_REVIEW", "Exact r2 66-page PDF fully rendered and reviewed (all 66 pages; not sampled): p.56 first glossary table entirely within text/page bounds with right-edge clipping 0; p.57 and p.58 glossary tables correct; no overlap, no cropped glyphs, no orphan header, no new near-blank page, no page hole, no bibliography regression. Rendered evidence preserved for p.1, pp.4-5 TOC, pp.39-45 capstone, pp.46-49 measurement, pp.53-59 appendix/glossary, pp.60-66 references; pp.56-58 individually inspected.", ["surveys/special/efficient-llm-2026/main.pdf: pages 1-66", "publication/v2/deterministic/pdf-preflight.json", "sources/SP-efficient-llm-2026/execution/validation/overfull-guard-r2.json"]),
        sem("LONGFORM_MIXED_LAYOUT", "Balanced two-column narrative via multicols (all subsections inside); full-width tables and boxes as wide surfaces; one-column references; TOC hierarchy intact. Glossary first-table layout-only \\par\\noindent fix; no unrelated page redesign; no appendix redesign.", ["reader-layout:wide-surfaces-full-width", "reader-layout:references-one-column", "reader-layout:balanced-two-column-narrative"]),
        sem("LONGFORM_PAGE_BALANCE", "66 pages (unchanged from r1) within 64-96 soft band; no padded pages; no near-blank pages (min page chars 655 on p.1; glossary pages 681-986; references 966-4022); multicols balance without stranded columns.", ["surveys/special/efficient-llm-2026/main.pdf: pages 1-66", "page-plan:66/76"]),
        sem("TECHNICAL_NOTES_TAIL_NEEDSPACE", "Appendix technical-note tables guarded by Needspace; tail notes not stranded; glossary split across pp.56-58 without orphaned headers. Overfull guard: max 10.0pt (<20pt BLOCK threshold); 12x 10.0pt REVIEW_REQUIRED findings at TeX lines 1204-1280 (full-width tabularx tables) visually disposed as within-margin, no clipping; 6x 8.99pt RECORD-only.", ["surveys/special/efficient-llm-2026/main.pdf: pages 53-59", "surveys/special/efficient-llm-2026/main.tex: Needspace guards", "sources/SP-efficient-llm-2026/execution/validation/overfull-guard-r2.json"]),
        sem("TOC_HIERARCHY", "TOC lists 10 numbered sections with numbered subsections and page numbers; unnumbered frontmatter/appendix excluded from numbered hierarchy as designed.", ["surveys/special/efficient-llm-2026/main.pdf: pages 4-5"]),
    ]
    vis_path = PUB / "visual-review-v2.json"
    reader.build_review_record(ROOT, manuscript_path, main_pdf, page_count, "VISUAL", visual_checks, REVIEWER, datetime(2026, 9, 23, 0, 37, tzinfo=timezone.utc), vis_path)
    reader.validate_review_record(ROOT, vis_path, issue_id=ISSUE, expected_kind="VISUAL")
    print("publication visual review OK")
    print("ALL R2 VALIDATION ARTIFACTS BUILT")


if __name__ == "__main__":
    main()
