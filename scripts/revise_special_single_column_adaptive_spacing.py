#!/usr/bin/env python3
"""Create an immutable layout-only Special revision with adaptive single-column chapter starts."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil
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
    if state.get('lifecycle_state')!='RELEASE_CANDIDATE': raise ValueError('single-column adaptive spacing requires RELEASE_CANDIDATE')
    if gates.get('latex_build')!='passed' or gates.get('visual_review')!='pending' or gates.get('freeze')!='pending': raise ValueError('single-column adaptive spacing requires built, unapproved release candidate')
    marker_path=repo_root/'sources'/issue_id/'editorial'/f'layout-revision-{source_version}.json'; marker=load_json(marker_path)
    if marker.get('issue_id')!=issue_id or marker.get('revision')!=source_version: raise ValueError('layout marker mismatch')
    constraints=marker.get('constraints') or {}; changes=marker.get('layout_changes') or {}
    if constraints.get('new_external_evidence_allowed') is not False or constraints.get('reader_content_changed') is not False or constraints.get('selected_evidence_only') is not True: raise ValueError('layout marker must be content-neutral and selected-Evidence-only')
    if changes.get('single_column_adaptive_chapter_starts') is not True: raise ValueError('single_column_adaptive_chapter_starts marker is required')

    current=dict(state.get('provenance',{}).get('validated_issue_source') or {}); current_manifest_path=repo_root/str(current.get('path') or '')
    if not current_manifest_path.is_file() or sha(current_manifest_path)!=current.get('sha256'): raise ValueError('current source digest mismatch')
    current_manifest=load_json(current_manifest_path); current_dir=current_manifest_path.parent
    if (current_manifest.get('layout') or {}).get('body_mode')!='single-column long-form': raise ValueError('single-column adaptive spacing expects single-column long-form source')
    out=repo_root/'surveys'/'special'/special_slug/'revisions'/source_version
    if out.exists(): raise ValueError(f'revision already exists: {out}')
    shutil.copytree(current_dir,out)

    main_path=out/'main.tex'; text=main_path.read_text(encoding='utf-8')
    article_inputs=[str(a.get('article_section_path') or '') for a in current_manifest.get('articles') or []]
    if len(article_inputs)<2: raise ValueError('expected multiple article sections')
    replacements=0
    for index, rel in enumerate(article_inputs):
        token='\\clearpage\n\\input{'+rel.removesuffix('.tex')+'}'
        if token not in text: raise ValueError(f'missing article boundary in main.tex: {rel}')
        if index==0: continue
        replacement='\\Needspace{0.45\\textheight}\n\\bigskip\n\\input{'+rel.removesuffix('.tex')+'}'
        text=text.replace(token,replacement,1); replacements+=1
    bib_token='\\clearpage\n\\printbibliography[title={References / Source Notes}]'
    if bib_token in text:
        text=text.replace(bib_token,'\\Needspace{0.35\\textheight}\n\\bigskip\n\\printbibliography[title={References / Source Notes}]',1); replacements+=1
    main_path.write_text(text,encoding='utf-8')

    # All reader content files remain byte-identical; only main.tex pagination policy changes.
    for article in current_manifest.get('articles') or []:
        for path_key, sha_key in (('article_section_path','article_section_sha256'),('technical_notes_path','technical_notes_sha256')):
            target=out/str(article[path_key])
            if sha(target)!=article[sha_key]: raise ValueError(f'reader content changed unexpectedly: {article.get("package_id")} {path_key}')
    for synth in current_manifest.get('theme_synthesis') or []:
        target=out/str(synth['path'])
        if sha(target)!=synth['sha256']: raise ValueError(f'theme synthesis changed unexpectedly: {synth.get("package_id")}')

    new=dict(current_manifest); new['source_version']=source_version; new['status']='VALIDATED_SINGLE_COLUMN_ADAPTIVE_SPACING_REVISION'
    new['derivation']='Layout-only revision of the prior validated single-column source. Reader wording and Evidence are unchanged; later article starts use minimum-space guards instead of unconditional page breaks.'
    new['basis']=dict(current_manifest.get('basis') or {}); new['basis']['previous_source_manifest_path']=current['path']; new['basis']['previous_source_manifest_sha256']=current['sha256']
    new['main_tex']=dict(current_manifest.get('main_tex') or {}); new['main_tex']['sha256']=sha(main_path)
    new['layout']=dict(current_manifest.get('layout') or {}); new['layout']['chapter_start_policy']='first feature on new page; later articles Needspace(0.45 textheight)'; new['layout']['references_start_policy']='Needspace(0.35 textheight)'
    new['layout_revision']={'from_source_version':current_manifest.get('source_version'),'reader_content_changed':False,'new_external_evidence':False,'single_column_adaptive_chapter_starts':True,'article_boundary_replacement_count':len(article_inputs)-1,'references_needspace':True,'article_sections_changed':False,'technical_notes_changed':False,'theme_synthesis_changed':False,'bibliography_data_changed':False}
    manifest_path=out/'source-manifest.json'; write_json(manifest_path,new); manifest_sha=sha(manifest_path)

    hist=state.setdefault('provenance_history',{}); hist.setdefault('validated_issue_source',[]).append(current); prev_build=dict(state.get('provenance',{}).get('latex_build') or {})
    if prev_build: hist.setdefault('latex_build',[]).append(prev_build)
    state['lifecycle_state']='VALIDATED_DRAFT'; state['gates']['latex_build']='pending'; state['gates']['visual_review']='pending'; state['gates']['freeze']='pending'
    prov=dict(current); prov.update({'path':manifest_path.relative_to(repo_root).as_posix(),'sha256':manifest_sha,'source_version':source_version,'layout_revision_sha256':sha(marker_path)})
    state['provenance']['validated_issue_source']=prov; state['provenance'].pop('latex_build',None); state['provenance']['reader_layout_revision']={'source_version':source_version,'layout_revision_path':marker_path.relative_to(repo_root).as_posix(),'layout_revision_sha256':sha(marker_path),'reason':str(marker.get('reason') or 'Reduce avoidable whitespace at single-column chapter boundaries without changing reader content.')}
    write_json(state_path,state)
    return {'schema_version':'1.0','issue_id':issue_id,'special_slug':special_slug,'source_version':source_version,'previous_source_version':current_manifest.get('source_version'),'source_manifest_sha256':manifest_sha,'reader_content_changed':False,'new_external_evidence':False,'article_boundary_replacements':len(article_inputs)-1,'lifecycle_state':state['lifecycle_state'],'latex_build_gate':state['gates']['latex_build']}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo-root',default='.'); p.add_argument('--special-slug',required=True); p.add_argument('--issue-id',required=True); p.add_argument('--source-version',required=True); a=p.parse_args(); print(json.dumps(build(Path(a.repo_root).resolve(),a.special_slug,a.issue_id,a.source_version),ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
