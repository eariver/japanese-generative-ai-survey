#!/usr/bin/env python3
"""Fill Special Japanese Technical Notes from reviewed overrides plus safe fallback summaries."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import special_reader_notes_ja as notes


def load_json(path: Path) -> dict[str, Any]:
    value=json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value,dict):
        raise ValueError(f'{path}: expected object')
    return value


def fallback(artifact: str, kind: str, evidence_class: str) -> str:
    if kind == 'limitation':
        return f'「{artifact}」の扱いでは、一次資料で確認できる範囲、提供時点、評価条件を維持し、記載範囲を超えて一般化しない。'
    if evidence_class == 'PRIMARY_FACT':
        return f'「{artifact}」について、一次資料で確認できる公開・提供・機能・時系列上の事実を要約した項目。'
    if evidence_class in {'VENDOR_CLAIM','PROJECT_CLAIM','AUTHOR_CLAIM'}:
        return f'「{artifact}」について、提供元・プロジェクト・著者側の評価または説明として記録された項目。独立再現された結果を意味しない。'
    return f'「{artifact}」について、一次資料と時系列から導いた編集上の整理。根拠となる事実と推論を区別して扱う。'


def run(repo_root: Path, issue_id: str, summary_path: Path, overrides_dir: Path) -> dict[str, Any]:
    repo_root=repo_root.resolve()
    summary_path=(repo_root/summary_path).resolve() if not summary_path.is_absolute() else summary_path.resolve()
    overrides_dir=(repo_root/overrides_dir).resolve() if not overrides_dir.is_absolute() else overrides_dir.resolve()
    doc=load_json(summary_path)
    if doc.get('issue_id') != issue_id:
        raise ValueError('summary issue mismatch')

    index: dict[tuple[str,str,str],dict[str,Any]]={}
    artifact_by_task: dict[str,str]={}
    for record in doc.get('records') or []:
        task=record['evidence_task_id']; artifact_by_task[task]=record['artifact_name']
        for key,kind in (('claims','claim'),('limitations','limitation')):
            for item in record.get(key) or []:
                index[(task,kind,item['item_id'])]=item

    applied=0
    if overrides_dir.is_dir():
        for path in sorted(overrides_dir.glob('part-*.json')):
            part=load_json(path)
            if part.get('issue_id') != issue_id:
                raise ValueError(f'{path}: issue mismatch')
            for tr in part.get('translations') or []:
                key=(tr.get('evidence_task_id'),tr.get('kind'),tr.get('item_id'))
                item=index.get(key)
                if item is None:
                    raise ValueError(f'{path}: unknown translation target {key}')
                if tr.get('source_text_sha256') != item.get('source_text_sha256'):
                    raise ValueError(f'{path}: source hash mismatch for {key}')
                text=tr.get('text_ja')
                if not isinstance(text,str) or not text.strip():
                    raise ValueError(f'{path}: empty Japanese translation for {key}')
                item['text_ja']=text.strip(); applied+=1

    fallback_count=0
    for (task,kind,_item_id), item in index.items():
        if not str(item.get('text_ja') or '').strip():
            item['text_ja']=fallback(artifact_by_task[task],kind,item.get('evidence_class',''))
            fallback_count+=1
    doc['status']='READY'
    notes.verify_source_text(repo_root,issue_id,doc)
    errors=notes.validate_summary(doc)
    if errors:
        raise ValueError(f'reader notes validation failed: {errors}')
    notes.write_json(summary_path,doc)
    return {'schema_version':'1.0','issue_id':issue_id,'status':'READY','translation_override_count':applied,'fallback_count':fallback_count,'item_count':len(index)}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',default='.')
    p.add_argument('--issue-id',required=True)
    p.add_argument('--summary',required=True)
    p.add_argument('--overrides-dir',required=True)
    a=p.parse_args()
    report=run(Path(a.repo_root),a.issue_id,Path(a.summary),Path(a.overrides_dir))
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
