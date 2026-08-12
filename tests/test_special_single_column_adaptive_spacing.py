from __future__ import annotations
import hashlib, json, tempfile, unittest
from pathlib import Path
from scripts.revise_special_single_column_adaptive_spacing import build

def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

class SingleColumnAdaptiveSpacingTests(unittest.TestCase):
    def make_repo(self, *, already_adaptive: bool=False, validated_draft: bool=False):
        td=tempfile.TemporaryDirectory(); root=Path(td.name); issue='SP-TEST'; slug='test'; src=root/'surveys/special'/slug/'revisions/v0.1'; (src/'sections').mkdir(parents=True); (src/'technical-notes').mkdir()
        a1=src/'sections/10-a.tex'; a2=src/'sections/20-b.tex'; n1=src/'technical-notes/10-a-notes.tex'; n2=src/'technical-notes/20-b-notes.tex'
        for p,t in ((a1,'a\n'),(a2,'b\n'),(n1,'na\n'),(n2,'nb\n')): p.write_text(t,encoding='utf-8')
        if already_adaptive:
            body='\\clearpage\n\\input{sections/10-a}\n\\input{technical-notes/10-a-notes}\n\\Needspace{0.45\\textheight}\n\\bigskip\n\\input{sections/20-b}\n\\input{technical-notes/20-b-notes}\n\\Needspace{0.35\\textheight}\n\\bigskip\n\\printbibliography[title={References / Source Notes}]\n'
        else:
            body='\\clearpage\n\\input{sections/10-a}\n\\input{technical-notes/10-a-notes}\n\\clearpage\n\\input{sections/20-b}\n\\input{technical-notes/20-b-notes}\n\\clearpage\n\\printbibliography[title={References / Source Notes}]\n'
        main=src/'main.tex'; main.write_text('\\documentclass{jlreq}\n\\usepackage{jgaisurvey}\n'+body,encoding='utf-8')
        manifest=src/'source-manifest.json'; articles=[{'package_id':'a','article_section_path':'sections/10-a.tex','article_section_sha256':sha(a1),'technical_notes_path':'technical-notes/10-a-notes.tex','technical_notes_sha256':sha(n1)},{'package_id':'b','article_section_path':'sections/20-b.tex','article_section_sha256':sha(a2),'technical_notes_path':'technical-notes/20-b-notes.tex','technical_notes_sha256':sha(n2)}]
        dump(manifest,{'source_version':'v0.1','layout':{'body_mode':'single-column long-form'},'main_tex':{'path':'main.tex','sha256':sha(main)},'articles':articles,'theme_synthesis':[]})
        if validated_draft:
            lifecycle='VALIDATED_DRAFT'; gates={'claim_and_chronology_validation':'passed','latex_build':'pending','visual_review':'pending','freeze':'pending'}; provenance={'validated_issue_source':{'path':manifest.relative_to(root).as_posix(),'sha256':sha(manifest),'source_version':'v0.1'}}
        else:
            lifecycle='RELEASE_CANDIDATE'; gates={'latex_build':'passed','visual_review':'pending','freeze':'pending'}; provenance={'validated_issue_source':{'path':manifest.relative_to(root).as_posix(),'sha256':sha(manifest),'source_version':'v0.1'},'latex_build':{'pdf_sha256':'x'}}
        state=root/'sources'/issue/'pipeline-state.json'; dump(state,{'lifecycle_state':lifecycle,'gates':gates,'provenance':provenance})
        marker=root/'sources'/issue/'editorial/layout-revision-v0.2.json'; dump(marker,{'issue_id':issue,'revision':'v0.2','constraints':{'new_external_evidence_allowed':False,'selected_evidence_only':True,'reader_content_changed':False},'layout_changes':{'single_column_adaptive_chapter_starts':True}})
        return td,root,issue,slug,state,a1,a2,n1,n2

    def test_replaces_later_clearpages_and_declares_needspace(self):
        td,root,issue,slug,state,a1,a2,n1,n2=self.make_repo(); self.addCleanup(td.cleanup)
        report=build(root,slug,issue,'v0.2'); self.assertEqual(report['article_boundary_replacements'],1); self.assertTrue(report['needspace_package_added'])
        revised=root/'surveys/special'/slug/'revisions/v0.2/main.tex'; text=revised.read_text(encoding='utf-8')
        self.assertIn('\\usepackage{needspace}',text); self.assertIn('\\clearpage\n\\input{sections/10-a}',text); self.assertIn('\\Needspace{0.45\\textheight}\n\\bigskip\n\\input{sections/20-b}',text); self.assertNotIn('\\clearpage\n\\printbibliography',text)
        self.assertEqual((root/'surveys/special'/slug/'revisions/v0.2/sections/10-a.tex').read_bytes(),a1.read_bytes())
        new_state=json.loads(state.read_text(encoding='utf-8')); self.assertEqual(new_state['lifecycle_state'],'VALIDATED_DRAFT'); self.assertEqual(new_state['gates']['latex_build'],'pending')

    def test_recovers_already_adaptive_validated_draft_by_adding_dependency(self):
        td,root,issue,slug,state,a1,a2,n1,n2=self.make_repo(already_adaptive=True,validated_draft=True); self.addCleanup(td.cleanup)
        report=build(root,slug,issue,'v0.2'); self.assertEqual(report['article_boundary_replacements'],0); self.assertTrue(report['needspace_package_added'])
        text=(root/'surveys/special'/slug/'revisions/v0.2/main.tex').read_text(encoding='utf-8')
        self.assertIn('\\usepackage{needspace}',text); self.assertEqual(text.count('\\Needspace{0.45\\textheight}'),1); self.assertEqual(text.count('\\Needspace{0.35\\textheight}'),1)
        self.assertEqual((root/'surveys/special'/slug/'revisions/v0.2/sections/20-b.tex').read_bytes(),a2.read_bytes())

if __name__=='__main__': unittest.main()
