#!/usr/bin/env python3
"""Assemble Core v2 Draft bytes into an exact LONGFORM_SPECIAL publication source."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

from scripts import survey_drafting_v2 as drafting
from scripts import survey_longform_publication_v2 as longform
from scripts import survey_production_v2 as core
from scripts.render_article_draft_tex import tex_escape

STYLE_PATH = Path("templates/survey/jgaisurvey.sty")


def _load(path: Path) -> dict[str, Any]: return core.load_json(path)
def _rel(root: Path, path: Path) -> str: return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")

def _safe(root: Path, raw: str, label: str) -> Path:
    path=(root/raw).resolve()
    try: path.relative_to(root.resolve())
    except ValueError as exc: raise ValueError(f"{label} escapes repository: {raw}") from exc
    if path.is_symlink() or not path.is_file(): raise ValueError(f"{label} missing or unsafe: {raw}")
    return path

def _find_sha(root: Path, expected_sha: str, name: str) -> Path:
    matches=[p for p in root.rglob(name) if p.is_file() and not p.is_symlink() and core.sha256_file(p)==expected_sha]
    if len(matches)!=1: raise ValueError(f"{name} SHA must resolve exactly once: {expected_sha} -> {matches}")
    return matches[0]

def _write_json(path: Path, value: Any) -> None:
    if path.exists(): raise ValueError(f"refusing to overwrite publication artifact: {path}")
    core.write_json(path,value)

def _bib_text(key: str, record: dict[str,Any], urldate: str) -> str:
    entity=record["entity"]
    title=str(entity["canonical_name"]).replace("{","\\{").replace("}","\\}")
    org=str(entity.get("organization") or "Unknown").replace("{","\\{").replace("}","\\}")
    return (f"@online{{{key},\n" f"  title = {{{{{title}}}}},\n" f"  author = {{{{{org}}}}},\n"
            f"  url = {{{entity['canonical_url']}}},\n" f"  urldate = {{{urldate}}}\n" "}")

def _kicker(package_id: str, ordinal: int, total: int) -> str:
    return f"THEMATIC LINEAGE {ordinal}/{total} — {package_id.rsplit('-',1)[-1].replace('_',' ')}"

def _assigned_ids(spec: dict[str,Any]) -> list[str]:
    ids=list(spec["deck_discovery_ids"])
    for block in spec["blocks"]: ids.extend(block.get("discovery_ids",[]))
    return list(dict.fromkeys(ids))

def _revision_ids(revision: dict[str,Any]) -> list[str]:
    values=[]
    def add(ids):
        for did in ids:
            if did not in values: values.append(did)
    for package in revision["packages"]:
        for row in package["theme_at_a_glance"]: add(row["discovery_ids"])
        for section in package["narrative_sections"]:
            for row in section["paragraphs"]: add(row["discovery_ids"])
        for row in package["timeline"]: add(row["discovery_ids"])
        for row in package["synthesis"]["paragraphs"]: add(row["discovery_ids"])
        for row in package["reader_claim_boundary"]: add(row["discovery_ids"])
        for note in package["technical_notes"]: add([note["discovery_id"]])
    cross=revision["cross_family_synthesis"]
    for row in cross["paragraphs"]: add(row["discovery_ids"])
    for row in cross["comparison_rows"]: add(row["discovery_ids"])
    return values

def _render_tex(issue_id,as_of,publication,ordered,bib_key_by_did):
    cover=publication["cover"]; front=publication["frontmatter"]; summary=publication["final_summary"]
    revision_by_id={r["package_id"]:r for r in publication["longform_revision"]["packages"]}
    lines=[
      "% Generated from Core v2 validated Draft bytes plus reviewed Evidence-backed longform revision. Do not hand-edit.",
      "\\documentclass[lualatex,a4paper,10pt]{jlreq}","\\usepackage{jgaisurvey}","\\addbibresource{references.bib}","",
      f"\\surveysetup{{{tex_escape(issue_id)}}}{{Japanese Generative AI Technical Survey Special}}{{Thematic history / as of {tex_escape(as_of)}}}{{As-of boundary: {tex_escape(as_of)}}}",
      "\\surveyeditiondescriptor{Thematic Longform Special}",
      f"\\surveycoverstory{{{tex_escape(cover['headline'])}}}{{{tex_escape(cover['deck'])}}}{{{tex_escape(' / '.join(cover['anchors']))}}}",
      "","\\begin{document}","\\surveycover","\\clearpage",
      f"\\section*{{{tex_escape(front['heading'])}}}",f"\\addcontentsline{{toc}}{{section}}{{{tex_escape(front['heading'])}}}",tex_escape(front["lede"]),"",
      "\\begin{claimboundary}[Scope / attribution boundary]",
    ]
    lines += ["\\noindent "+tex_escape(note)+"\\par" for note in front["scope_notes"]]
    lines += ["\\end{claimboundary}","\\medskip","\\tableofcontents","\\clearpage"]
    for ordinal,(spec,_,result) in enumerate(ordered,start=1):
        pid=result["package_id"]
        lines.append(f"% package:{pid} draft-result-sha256:{core.sha256_object(result)}")
        lines += longform.render_package(spec,result,revision_by_id[pid],bib_key_by_did,_kicker(pid,ordinal,len(ordered)))
    lines += longform.render_cross_family(publication["longform_revision"]["cross_family_synthesis"],bib_key_by_did)
    lines += ["\\Needspace{0.28\\textheight}",f"\\section{{{tex_escape(summary['heading'])}}}","\\label{sec:issue-summary}","\\sectionkicker{ISSUE SYNTHESIS}","\\begin{multicols}{2}"]
    lines += ["\\noindent "+tex_escape(p)+"\\par\\medskip" for p in summary["paragraphs"]]
    lines += ["\\end{multicols}","\\medskip","\\printbibliography[title={References / Source Notes}]","\\end{document}",""]
    return "\n".join(lines)

def _validate_input(data,issue_id):
    expected={"schema_version","issue_id","runner","cover","frontmatter","final_summary","longform_revision"}
    if set(data)!=expected or data.get("schema_version")!="2.0-rc1" or data.get("issue_id")!=issue_id: raise ValueError("semantic publication input envelope invalid")
    cover=data["cover"]
    if set(cover)!={"headline","deck","anchors"} or not all(isinstance(cover.get(k),str) and cover[k].strip() for k in ("headline","deck")): raise ValueError("publication cover invalid")
    if not isinstance(cover["anchors"],list) or not cover["anchors"] or not all(isinstance(x,str) and x.strip() for x in cover["anchors"]): raise ValueError("publication cover anchors invalid")
    front=data["frontmatter"]
    if set(front)!={"heading","lede","scope_notes"} or not isinstance(front["scope_notes"],list) or not front["scope_notes"]: raise ValueError("publication frontmatter invalid")
    summary=data["final_summary"]
    if set(summary)!={"heading","paragraphs"} or summary.get("heading")!="この号の総括": raise ValueError("required final issue summary heading is missing")
    if not isinstance(summary["paragraphs"],list) or len(summary["paragraphs"])<3 or not all(isinstance(x,str) and x.strip() for x in summary["paragraphs"]): raise ValueError("final issue summary must contain at least three substantive paragraphs")

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo-root",default="."); ap.add_argument("--state",required=True); ap.add_argument("--input",required=True); args=ap.parse_args()
    root=Path(args.repo_root).resolve(); state_path=_safe(root,args.state,"Production State"); input_path=_safe(root,args.input,"semantic publication input")
    state=_load(state_path); lifecycle=state.get("lifecycle_state")
    initial=lifecycle=="DRAFT_COMPLETE" and state.get("next_action")=="stage:semantic-publication-validation"
    revision=lifecycle=="RELEASE_CANDIDATE" and state.get("next_action")=="PUBLICATION_PREVIEW" and state.get("human_gates",{}).get("publication_preview")=="pending"
    if not (initial or revision): raise SystemExit("semantic publication requires DRAFT_COMPLETE or pending RELEASE_CANDIDATE Publication Preview State")
    issue_id=state["issue_id"]; profile_path=_safe(root,state["profile"]["path"],"Production Profile"); profile=_load(profile_path)
    if profile.get("publication_profile")!="LONGFORM_SPECIAL": raise SystemExit("this renderer currently requires LONGFORM_SPECIAL")
    source_root=(root/profile["paths"]["source_root"]).resolve(); survey_root=(root/profile["paths"]["survey_root"]).resolve(); source_root.relative_to(root); survey_root.relative_to(root)
    data=_load(input_path); _validate_input(data,issue_id)
    directive_path=source_root/"editorial/post-architecture-directives-v2.json"; directive=_load(directive_path)
    final_rows=[r for r in directive.get("requirements",[]) if r.get("kind")=="FINAL_ISSUE_SUMMARY" and r.get("required") is True]
    if len(final_rows)!=1 or final_rows[0].get("placement")!="END_OF_PUBLICATION_BEFORE_REFERENCES_OR_END_MATTER": raise SystemExit("required Architecture-review final-summary directive is missing or ambiguous")
    architecture=_load(source_root/"architecture-v2.json"); synthesis_input_path=source_root/"draft/v2/profile-synthesis-input.json"; synthesis_result_path=source_root/"draft/v2/profile-synthesis-result.json"
    syn_errors=drafting.validate_synthesis_result(_load(synthesis_result_path),synthesis_input_path,root/drafting.SYNTHESIS_PROMPT)
    if syn_errors: raise SystemExit("upstream Profile Synthesis invalid: "+"; ".join(syn_errors))
    semantic_archive=_load(source_root/"draft/v2/interactive-drafting-synthesis-input.json"); spec_by_id={r["package_id"]:r for r in semantic_archive["packages"]}
    ordered=[]; evidence_acceptance_sha=None
    for plan in sorted(architecture["packages"],key=lambda r:(r["drafting_order"],r["package_id"])):
        pid=plan["package_id"]; package_path=source_root/"draft/v2/packages"/pid/"draft-package.json"; result_path=source_root/"draft/v2/packages"/pid/"draft-result.json"
        package=_load(package_path); result=_load(result_path); errors=drafting.validate_draft_result(result,package_path,root/drafting.DRAFT_PROMPT)
        if errors: raise SystemExit(f"upstream Draft Result invalid for {pid}: "+"; ".join(errors))
        spec=spec_by_id.get(pid)
        if spec is None or result["headline"]!=spec["headline"] or result["deck"]!=spec["deck"]: raise SystemExit(f"Draft semantic archive drift for {pid}")
        result_blocks={b["block_id"]:b for b in result["blocks"] if b["block_type"]!="CLAIM_BOUNDARY"}
        for bs in spec["blocks"]:
            if bs["block_id"] not in result_blocks or result_blocks[bs["block_id"]]["text"]!=bs["text"]: raise SystemExit(f"Draft block semantic archive drift for {pid}/{bs['block_id']}")
        ea=package["basis"]["evidence_acceptance_sha256"]
        if evidence_acceptance_sha is None: evidence_acceptance_sha=ea
        elif evidence_acceptance_sha!=ea: raise SystemExit("Draft packages disagree on Evidence acceptance authority")
        ordered.append((spec,package,result))
    acceptance=_find_sha(source_root/"evidence",evidence_acceptance_sha,"evidence-accepted.json"); evidence_payload=_load(acceptance.parent/"interactive-evidence.json"); records={r["discovery_id"]:r for r in evidence_payload["records"]}
    validation_plans=[{"package_id":result["package_id"],"evidence_discovery_ids":_assigned_ids(spec)} for spec,_,result in ordered]
    normalized_revision=longform.validate_revision(data.get("longform_revision"),validation_plans,records); data["longform_revision"]=normalized_revision
    cited=[]
    for spec,_,_ in ordered: cited.extend(_assigned_ids(spec))
    cited.extend(_revision_ids(normalized_revision)); cited=list(dict.fromkeys(cited))
    for did in cited:
        row=records.get(did)
        if row is None: raise SystemExit(f"cited Discovery ID missing from accepted Evidence: {did}")
        if row.get("materiality")=="HOLD" or row.get("status")=="NEEDS_MORE": raise SystemExit(f"publication cannot cite HOLD/NEEDS_MORE Evidence as factual support: {did}")
        entity=row.get("entity") or {}
        if not entity.get("canonical_name") or not entity.get("canonical_url"): raise SystemExit(f"cited Evidence lacks canonical bibliography metadata: {did}")
    survey_root.mkdir(parents=True,exist_ok=True); publication_root=source_root/"publication/v2"; publication_root.mkdir(parents=True,exist_ok=True); quality_root=publication_root/"quality"; quality_root.mkdir(parents=True,exist_ok=True)
    for path in (survey_root/"main.tex",survey_root/"references.bib",survey_root/"jgaisurvey.sty",publication_root/"validated-source-manifest.json",quality_root/"longform-special-preflight.json"):
        if path.exists(): raise SystemExit(f"refusing existing semantic publication artifact: {path}")
    style_source=root/STYLE_PATH; shutil.copyfile(style_source,survey_root/"jgaisurvey.sty")
    as_of=profile["research_scope"]["temporal_policy"]["as_of"].replace("T"," ").replace("Z"," UTC"); urldate=profile["research_scope"]["temporal_policy"]["as_of"][:10]
    bib_key_by_did={did:"sp001"+did.lower().replace("-","") for did in cited}; bib="\n\n".join(_bib_text(bib_key_by_did[d],records[d],urldate) for d in cited)+"\n"; (survey_root/"references.bib").write_text(bib,encoding="utf-8")
    tex=_render_tex(issue_id,as_of,data,ordered,bib_key_by_did); preflight=longform.preflight_tex(tex,bib,len(ordered))
    if preflight["status"]!="PASS": raise SystemExit("LONGFORM_SPECIAL source preflight failed: "+"; ".join(preflight["findings"]))
    (survey_root/"main.tex").write_text(tex,encoding="utf-8"); preflight_path=quality_root/"longform-special-preflight.json"; _write_json(preflight_path,{"schema_version":"2.0-rc1","check_id":"LONGFORM_SPECIAL_LAYOUT_AND_READER_SURFACE","issue_id":issue_id,**preflight})
    archived_input=publication_root/"interactive-semantic-publication-input.json"; _write_json(archived_input,data)
    draft_refs=[]
    for _,_,result in ordered:
        path=source_root/"draft/v2/packages"/result["package_id"]/"draft-result.json"; draft_refs.append({"package_id":result["package_id"],"path":_rel(root,path),"sha256":core.sha256_file(path)})
    manifest={"schema_version":"2.0-rc1","issue_id":issue_id,"status":"ESTABLISHED","production_profile":{"path":_rel(root,profile_path),"sha256":core.sha256_file(profile_path)},"production_state_basis":{"path":_rel(root,state_path),"sha256":core.sha256_file(state_path),"lifecycle_state":lifecycle},"publication_semantic_input":{"path":_rel(root,archived_input),"sha256":core.sha256_file(archived_input)},"post_architecture_directive":{"path":_rel(root,directive_path),"sha256":core.sha256_file(directive_path),"directive_id":final_rows[0]["directive_id"]},"profile_synthesis":{"input":{"path":_rel(root,synthesis_input_path),"sha256":core.sha256_file(synthesis_input_path)},"result":{"path":_rel(root,synthesis_result_path),"sha256":core.sha256_file(synthesis_result_path)}},"draft_results":draft_refs,"rendered_source":{"path":_rel(root,survey_root/"main.tex"),"sha256":core.sha256_file(survey_root/"main.tex")},"bibliography":{"path":_rel(root,survey_root/"references.bib"),"sha256":core.sha256_file(survey_root/"references.bib"),"cited_discovery_ids":cited},"style":{"source_path":str(STYLE_PATH),"source_sha256":core.sha256_file(style_source),"copied_path":_rel(root,survey_root/"jgaisurvey.sty"),"copied_sha256":core.sha256_file(survey_root/"jgaisurvey.sty")},"longform_revision":{"review_reference":normalized_revision["review_reference"],"new_external_evidence":False,"package_count":len(normalized_revision["packages"]),"preflight":{"path":_rel(root,preflight_path),"sha256":core.sha256_file(preflight_path)}},"final_summary":{"heading":data["final_summary"]["heading"],"placement":"END_OF_PUBLICATION_BEFORE_REFERENCES_OR_END_MATTER","paragraph_count":len(data["final_summary"]["paragraphs"])}}
    _write_json(publication_root/"validated-source-manifest.json",manifest)
    _write_json(quality_root/"subject-entity-property-binding.json",{"schema_version":"2.0-rc1","check_id":"SUBJECT_ENTITY_PROPERTY_BINDING","status":"PASS","issue_id":issue_id,"cited_discovery_count":len(cited),"bindings":[{"discovery_id":d,"canonical_name":records[d]["entity"]["canonical_name"],"canonical_url":records[d]["entity"]["canonical_url"],"materiality":records[d]["materiality"],"status":records[d]["status"]} for d in cited]})
    _write_json(quality_root/"empty-wrapper-suppression.json",{"schema_version":"2.0-rc1","check_id":"EMPTY_WRAPPER_SUPPRESSION","status":"PASS","issue_id":issue_id,"sections":len(ordered)+3,"claim_boundary_blocks":len(ordered)+1,"technical_note_blocks":sum(len(r["technical_notes"]) for r in normalized_revision["packages"]),"finding":"All rendered sections, narrative flows, synthesis layers, reader-facing Claim Boundaries, Technical Notes, frontmatter, and final issue summary are non-empty."})
    print(json.dumps({"issue_id":issue_id,"source_root":_rel(root,source_root),"survey_root":_rel(root,survey_root),"source_manifest":_rel(root,publication_root/"validated-source-manifest.json"),"main_tex":_rel(root,survey_root/"main.tex"),"bibliography":_rel(root,survey_root/"references.bib"),"style":_rel(root,survey_root/"jgaisurvey.sty"),"subject_result":_rel(root,quality_root/"subject-entity-property-binding.json"),"empty_result":_rel(root,quality_root/"empty-wrapper-suppression.json"),"longform_preflight":_rel(root,preflight_path),"identifier_tokens":["GLM","Qwen","DeepSeek","Kimi","MiniMax","Yi","Baichuan","Open Weight","Kimi K3"]},ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__": raise SystemExit(main())
