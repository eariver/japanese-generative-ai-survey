#!/usr/bin/env python3
"""Repair SP-2025-H1 Publication Preview review findings without mutating Evidence."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil
from copy import deepcopy
from pathlib import Path
from typing import Any
from scripts.special_technical_note_tail_policy import apply_generic_tail_policy, unprotected_tail_titles

NOTE_RE = re.compile(r"\\begin\{technicalnote\}\{(.+?)\}\{.*?\\end\{technicalnote\}", re.DOTALL)
THEME_ROW_RE = re.compile(r"^(.+?)\s*&\s*(.+?)\s*&\s*-\s*&\s*(.+?)\s*\\\\$", re.MULTILINE)
ROW_END = r"\\"

CITE_BY_EVENT = {
"DeepSeek-R1 API release":"src-8f8555b73e1b",
"OpenAI Operator research preview":"src-95b210494c88",
"Qwen2.5-VL open models":"src-dc21f366b638",
"Qwen2.5-Max API availability":"src-8c485019ad8d",
"OpenAI o3-mini":"src-650b567698aa",
"OpenAI Deep Research":"src-8fec3ef3a97d",
"Claude 3.7 Sonnet / Claude Code":"src-a6c92f94a0af",
"GPT-4.5 research preview":"src-3fa7f4cd510b",
"Responses API / built-in tools / Agents SDK":"src-78593f4b387f",
"Gemma 3":"src-1bb16d7254b1",
"Claude web search product preview":"src-6e15bd50b7db",
"DeepSeek-V3-0324 API upgrade":"src-8f8555b73e1b",
"Gemini 2.5 Pro Experimental":"src-421ee9af3f80",
"GPT-4o native image generation":"src-877e7da88408",
"Anthropic interpretability research: Tracing thoughts":"src-fdc10e3226e6",
"Qwen2.5-Omni":"src-de4ffd746276",
"QVQ-Max visual reasoning":"src-8cb736b33646",
"Llama 4 Scout / Maverick":"src-05f285e9757b",
"GPT-4.1 API family":"src-31799a46d8d0",
"GPT-4.5 Preview API retirement announcement":"src-31799a46d8d0",
"OpenAI o3 / o4-mini":"src-bf92f3d905c3",
"Llama API limited preview":"src-fca961b24baf",
"Llama Guard 4 / protection tools":"src-383476bdf62e",
"Qwen3":"src-3e4a3f3b3d83",
"Anthropic web search API":"src-e31c642d34b6",
"OpenAI Codex cloud software engineering agent":"src-e7aef8f1b13b",
"Jules coding agent public beta":"src-8b595b787bad",
"Veo 3 / Imagen 4 / Flow / Lyria 2":"src-e68f8ce96685",
"Responses API remote MCP / tool expansion":"src-9257c39d4172",
"Claude Opus 4 / Sonnet 4":"src-4ec03078d316",
"Gemini 2.5 Pro / Flash GA":"src-53f15d483a2d",
}
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def write(p,v): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def taxonomy(title: str) -> str:
    t=title.lower()
    if "tracing the thoughts" in t: return "Interpretability研究"
    if "guard" in t or "protection" in t: return "Safeguard"
    if "web search api" in t: return "API Tool"
    if "responses api" in t: return "Agent Platform / API"
    if "operator" in t or "deep research" in t or "codex" in t or "jules" in t or "claude code" in t: return "Agent"
    if "web search product" in t: return "製品機能"
    if "veo 3" in t or "imagen 4" in t or "lyria" in t: return "生成Media"
    if "image generation" in t: return "画像生成Model"
    if "api deprecation" in t or "retirement" in t: return "Model Lifecycle"
    if "api" in t: return "API / Model提供"
    if "open models" in t or "llama 4" in t or "qwen3" in t: return "Open-weight Model"
    if "omni" in t or "visual reasoning" in t or "-vl" in t: return "Multimodal Model"
    if any(x in t for x in ("gemini","gpt","claude","deepseek","qwen","o3","o4")): return "Model / Model Family"
    return "公式技術資料"

def repair_notes(path: Path) -> tuple[int,int]:
    original=path.read_text(encoding="utf-8")
    text=original.replace(r"\addcontentsline{toc}{subsection}{Theme at a glance}"+"\n","")
    changes=[]
    for m in NOTE_RE.finditer(text):
        block=m.group(0); title=m.group(1); label=taxonomy(title)
        revised=block.replace(f"種別 & - {ROW_END}", f"種別 & {label} {ROW_END}", 1)
        if revised != block: changes.append((m.start(),m.end(),revised))
    for s,e,r in reversed(changes): text=text[:s]+r+text[e:]
    def row(m):
        title=m.group(1).strip()
        return f"{m.group(1)} & {m.group(2)} & {taxonomy(title)} & {m.group(3)} {ROW_END}"
    text=THEME_ROW_RE.sub(row,text)
    tail=apply_generic_tail_policy(text)
    text=tail.text
    if unprotected_tail_titles(text): raise ValueError(f"{path}: unprotected Technical Notes tail")
    if text != original: path.write_text(text,encoding="utf-8")
    return tail.groups_added, tail.card_count

def repair_chronology(path: Path) -> int:
    text=path.read_text(encoding="utf-8"); changed=0; out=[]
    for line in text.splitlines():
        m=re.match(r"(\s*\\item\s+\d{4}-\d{2}-\d{2}:\s+)(.+)$",line)
        if m:
            event=m.group(2).strip(); key=CITE_BY_EVENT.get(event)
            if key:
                line=m.group(1)+event+rf" \autocite{{{key}}}"; changed+=1
        if line.strip().startswith(r"\autocite{"): continue
        out.append(line)
    path.write_text("\n".join(out)+"\n",encoding="utf-8")
    return changed

def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str,Any]:
    marker_path=repo_root/"sources"/issue_id/"editorial"/f"layout-revision-{source_version}.json"
    marker=load(marker_path); changes=marker.get("layout_changes") or {}
    if changes.get("h1_publication_preview_repairs") is not True: raise ValueError("marker flag missing")
    state_path=repo_root/"sources"/issue_id/"pipeline-state.json"; state=load(state_path)
    if state.get("lifecycle_state")!="RELEASE_CANDIDATE" or state["gates"].get("latex_build")!="passed": raise ValueError("requires built release candidate")
    current=deepcopy(state["provenance"]["validated_issue_source"]); cur_manifest=repo_root/current["path"]
    if sha(cur_manifest)!=current["sha256"]: raise ValueError("source digest mismatch")
    manifest=load(cur_manifest); out=repo_root/"surveys"/"special"/special_slug/"revisions"/source_version
    if out.exists(): raise ValueError("revision exists")
    shutil.copytree(cur_manifest.parent,out)

    analysis_rel=str(changes["half_year_analysis_source_path"]); analysis_src=repo_root/analysis_rel
    analysis_art=load(repo_root/str(changes["half_year_analysis_artifact_path"]))
    if analysis_art.get("selected_evidence_only") is not True or analysis_art.get("new_external_evidence") is not False: raise ValueError("analysis boundary")
    analysis_target=out/"half-year-analysis"/"80-half-year-analysis.tex"; analysis_target.parent.mkdir(exist_ok=True)
    shutil.copyfile(analysis_src,analysis_target)

    groups=cards=0
    for article in manifest.get("articles") or []:
        rel=str(article.get("technical_notes_path") or "")
        if rel:
            p=out/rel; g,c=repair_notes(p); groups+=g; cards+=c; article["technical_notes_sha256"]=sha(p)

    chron=out/"layout-bodies"/"chronology.tex"; mapped=repair_chronology(chron)
    for article in manifest.get("articles") or []:
        if article.get("package_id")=="chronology":
            article["layout_body_sha256"]=sha(chron); article["technical_notes_reader_facing"]=False; article["chronology_source_mapping"]="inline item-level citations"

    refs=out/str((manifest.get("references") or {}).get("path") or "references.bib")
    rtext=refs.read_text(encoding="utf-8")
    rtext,n=re.subn(r"^\s*note\s*=\s*\{Evidence source\.?\}\s*,?\s*$","",rtext,flags=re.MULTILINE)
    rtext=re.sub(r"\n{3,}","\n\n",rtext); refs.write_text(rtext,encoding="utf-8")

    main=out/str((manifest.get("main_tex") or {}).get("path") or "main.tex"); text=main.read_text(encoding="utf-8")
    if r"\usepackage{needspace}" not in text:
        anchor=r"\usepackage{multicol}"
        if anchor not in text: raise ValueError("H1 repair requires multicol package anchor")
        text=text.replace(anchor, r"\usepackage{needspace}"+"\n"+anchor, 1)
    text=text.replace(r"\input{technical-notes/80-chronology-notes}"+"\n","")
    heading=r"\section{Half-year Synthesis — ReasoningからExecution Stackへ}"
    insertion=(r"\Needspace{0.40\textheight}"+"\n"+r"\bigskip"+"\n"+r"\input{half-year-analysis/80-half-year-analysis}"+"\n\n"+r"\Needspace{0.40\textheight}"+"\n"+r"\bigskip"+"\n"+heading)
    text=text.replace(r"\clearpage"+"\n"+heading,insertion,1)
    bib=r"\printbibliography[title={References / Source Notes}]"
    common=(r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。各entryでは識別に必要な資料名、組織、URL、日付を示す。}}\par"+"\n"+r"\smallskip"+"\n"+bib)
    text=text.replace(bib,common,1); main.write_text(text,encoding="utf-8")

    manifest["source_version"]=source_version; manifest["status"]="VALIDATED_H1_PUBLICATION_PREVIEW_REPAIR_REVISION"
    manifest["derivation"]="Publication Preview repair using only already-selected Evidence; accepted Article Drafts and Evidence cards remain immutable."
    manifest["basis"]=dict(manifest.get("basis") or {}); manifest["basis"]["previous_source_manifest_path"]=current["path"]; manifest["basis"]["previous_source_manifest_sha256"]=current["sha256"]
    manifest["main_tex"]={"path":main.relative_to(out).as_posix(),"sha256":sha(main)}; manifest["references"]={"path":refs.relative_to(out).as_posix(),"sha256":sha(refs)}
    manifest["half_year_analysis"]={"path":"half-year-analysis/80-half-year-analysis.tex","sha256":sha(analysis_target),"selected_evidence_only":True,"new_external_evidence":False}
    manifest["layout_revision"]={"from_source_version":current.get("source_version"),"review_issues":[128,153,122,55,54,140],"reader_content_changed":True,"new_external_evidence":False,"accepted_article_claims_changed":False,"evidence_cards_mutated":False,"half_year_analysis_added":True,"chronology_technical_notes_deduplicated":True,"chronology_item_level_source_mapping_count":mapped,"theme_at_a_glance_toc_entries_removed":True,"reader_taxonomy_recovered_from_source_identity":True,"generic_technical_note_tail_policy":True,"technical_note_card_count":cards,"technical_note_tail_groups_added":groups,"references_common_note_removed_count":n}
    manifest.setdefault("layout",{})["toc_depth"]="section"; manifest["layout"]["body_mode"]="mixed: narrative articles two-column; full-width notes; half-year analysis; compact chronology"
    mp=out/"source-manifest.json"; write(mp,manifest); msha=sha(mp)

    hist=state.setdefault("provenance_history",{}); hist.setdefault("validated_issue_source",[]).append(current)
    oldbuild=deepcopy(state["provenance"].get("latex_build") or {})
    if oldbuild: hist.setdefault("latex_build",[]).append(oldbuild)
    state["lifecycle_state"]="VALIDATED_DRAFT"; state["gates"]["latex_build"]="pending"; state["gates"]["visual_review"]="pending"; state["gates"]["freeze"]="pending"
    state["provenance"]["validated_issue_source"]={"path":mp.relative_to(repo_root).as_posix(),"sha256":msha,"source_version":source_version,"layout_mode":"half-year-review-repair","layout_revision_sha256":sha(marker_path)}
    state["provenance"].pop("latex_build",None); state["provenance"]["reader_layout_revision"]={"source_version":source_version,"layout_revision_path":marker_path.relative_to(repo_root).as_posix(),"layout_revision_sha256":sha(marker_path),"reason":marker.get("reason","")}; write(state_path,state)
    return {"schema_version":"1.0","issue_id":issue_id,"source_version":source_version,"source_manifest":mp.relative_to(repo_root).as_posix(),"source_manifest_sha256":msha,"chronology_source_mapping_count":mapped,"technical_note_card_count":cards,"tail_groups_added":groups,"references_common_note_removed_count":n,"lifecycle_state":"VALIDATED_DRAFT"}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--repo-root",default="."); p.add_argument("--special-slug",required=True); p.add_argument("--issue-id",required=True); p.add_argument("--source-version",required=True)
    a=p.parse_args(); print(json.dumps(build(Path(a.repo_root).resolve(),a.special_slug,a.issue_id,a.source_version),ensure_ascii=False,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
