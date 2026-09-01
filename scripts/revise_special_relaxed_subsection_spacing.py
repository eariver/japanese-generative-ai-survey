#!/usr/bin/env python3
"""Create an immutable layout-only revision removing multicol-incompatible subsection Needspace while keeping paragraph separation."""
from __future__ import annotations
import argparse, hashlib, json, shutil
from pathlib import Path
from typing import Any

def load_json(path: Path) -> dict[str, Any]:
    value=json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value,dict): raise ValueError(f'{path}: expected object')
    return value

def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path=repo_root/'sources'/issue_id/'pipeline-state.json'; state=load_json(state_path); gates=state.get('gates') or {}
    if state.get('lifecycle_state')!='RELEASE_CANDIDATE': raise ValueError('relaxed subsection revision requires RELEASE_CANDIDATE')
    if gates.get('latex_build')!='passed' or gates.get('visual_review')!='pending' or gates.get('freeze')!='pending': raise ValueError('relaxed subsection revision requires built, unapproved release candidate')
    marker_path=repo_root/'sources'/issue_id/'editorial'/f'layout-revision-{source_version}.json'; marker=load_json(marker_path)
    if marker.get('issue_id')!=issue_id or marker.get('revision')!=source_version: raise ValueError('layout marker mismatch')
    constraints=marker.get('constraints') or {}; changes=marker.get('layout_changes') or {}
    if constraints.get('new_external_evidence_allowed') is not False or constraints.get('reader_content_changed') is not False or constraints.get('selected_evidence_only') is not True: raise ValueError('layout marker must be content-neutral and selected-Evidence-only')
    if changes.get('remove_subsection_needspace') is not True: raise ValueError('remove_subsection_needspace marker is required')

    current=dict(state.get('provenance',{}).get('validated_issue_source') or {}); current_manifest_path=repo_root/str(current.get('path') or '')
    if not current_manifest_path.is_file() or sha(current_manifest_path)!=current.get('sha256'): raise ValueError('current source digest mismatch')
    current_manifest=load_json(current_manifest_path); current_dir=current_manifest_path.parent
    out=repo_root/'surveys'/'special'/special_slug/'revisions'/source_version
    if out.exists(): raise ValueError(f'revision already exists: {out}')
    shutil.copytree(current_dir,out)

    old=r'\par\medskip\Needspace{4\baselineskip}'+'\n'+r'\subsection{'
    new=r'\par\medskip'+'\n'+r'\subsection{'
    layout_records=current_manifest.get('article_layout_bodies') or []
    if not layout_records: raise ValueError('layout-only article bodies are required')
    changed=[]
    for record in layout_records:
        rel=str(record.get('path') or ''); target=out/rel
        if not target.is_file(): raise ValueError(f'layout body missing: {rel}')
        text=target.read_text(encoding='utf-8'); count=text.count(old)
        if count<1: raise ValueError(f'expected guarded subsections not found in {rel}')
        text=text.replace(old,new); target.write_text(text,encoding='utf-8')
        if r'\Needspace{4\baselineskip}' in text: raise ValueError(f'four-baseline Needspace remains in {rel}')
        changed.append({'package_id':record.get('package_id'),'path':rel,'sha256':sha(target),'relaxed_subsection_count':count})

    # All non-layout reader material remains byte-identical to the prior validated revision.
    for article in current_manifest.get('articles') or []:
        section=out/str(article['article_section_path']); notes=out/str(article['technical_notes_path'])
        if sha(section)!=article['article_section_sha256']: raise ValueError(f'accepted article changed: {article["package_id"]}')
        if sha(notes)!=article['technical_notes_sha256']: raise ValueError(f'Technical Notes changed: {article["package_id"]}')
    for synth in current_manifest.get('theme_synthesis') or []:
        target=out/str(synth['path'])
        if sha(target)!=synth['sha256']: raise ValueError(f'Theme Synthesis changed: {synth.get("package_id")}')
    final_info=dict(current_manifest.get('final_synthesis') or {}); final_rel=str(final_info.get('tex_path') or '')
    if final_rel:
        final_path=out/final_rel; prior_sha=str(final_info.get('tex_sha256') or '')
        if prior_sha and sha(final_path)!=prior_sha: raise ValueError('final synthesis changed unexpectedly')

    main_path=out/'main.tex'
    new_manifest=dict(current_manifest); new_manifest['source_version']=source_version; new_manifest['status']='VALIDATED_RELAXED_SUBSECTION_SPACING_REVISION'; new_manifest['derivation']='Layout-only revision of the prior release candidate. Reader wording and Evidence are unchanged. The four-baseline Needspace inserted before narrative subsections is removed while explicit paragraph termination and medskip separation are retained.'
    new_manifest['basis']=dict(current_manifest.get('basis') or {}); new_manifest['basis']['previous_source_manifest_path']=current['path']; new_manifest['basis']['previous_source_manifest_sha256']=current['sha256']
    new_manifest['main_tex']={'path':'main.tex','sha256':sha(main_path)}; new_manifest['article_layout_bodies']=changed
    new_manifest['layout']=dict(current_manifest.get('layout') or {}); new_manifest['layout']['article_subsection_policy']='paragraph termination + medskip before each narrative subsection; no Needspace inside multicol'
    new_manifest['layout_revision']={'from_source_version':current_manifest.get('source_version'),'reader_content_changed':False,'new_external_evidence':False,'relaxed_subsection_spacing':True,'subsection_needspace_removed':True,'accepted_article_sections_changed':False,'theme_synthesis_changed':False,'technical_notes_changed':False,'final_synthesis_changed':False}
    manifest_path=out/'source-manifest.json'; write_json(manifest_path,new_manifest); manifest_sha=sha(manifest_path)

    hist=state.setdefault('provenance_history',{}); hist.setdefault('validated_issue_source',[]).append(current); prev_build=dict(state.get('provenance',{}).get('latex_build') or {})
    if prev_build: hist.setdefault('latex_build',[]).append(prev_build)
    state['lifecycle_state']='VALIDATED_DRAFT'; state['gates']['latex_build']='pending'; state['gates']['visual_review']='pending'; state['gates']['freeze']='pending'
    state['provenance']['validated_issue_source']={'path':manifest_path.relative_to(repo_root).as_posix(),'sha256':manifest_sha,'source_version':source_version,'layout_mode':'balanced-multicol-adaptive-spacing-relaxed-subsection','layout_revision_sha256':sha(marker_path)}
    state['provenance'].pop('latex_build',None); state['provenance']['reader_layout_revision']={'source_version':source_version,'layout_revision_path':marker_path.relative_to(repo_root).as_posix(),'layout_revision_sha256':sha(marker_path),'reason':'Render-first QA of v0.7 found a nearly empty page caused by Needspace inside multicol. Keep paragraph separation and remove only the problematic subsection Needspace.'}
    write_json(state_path,state)
    return {'schema_version':'1.0','issue_id':issue_id,'special_slug':special_slug,'source_version':source_version,'previous_source_version':current_manifest.get('source_version'),'source_manifest':manifest_path.relative_to(repo_root).as_posix(),'source_manifest_sha256':manifest_sha,'layout_body_count':len(changed),'relaxed_subsection_count':sum(x['relaxed_subsection_count'] for x in changed),'reader_content_changed':False,'new_external_evidence':False,'lifecycle_state':state['lifecycle_state'],'latex_build_gate':state['gates']['latex_build']}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--special-slug',required=True); p.add_argument('--issue-id',required=True); p.add_argument('--source-version',required=True); a=p.parse_args(); print(json.dumps(build(Path(a.repo_root).resolve(),a.special_slug,a.issue_id,a.source_version),ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
