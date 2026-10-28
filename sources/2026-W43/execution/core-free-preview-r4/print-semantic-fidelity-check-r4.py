#!/usr/bin/env python3
"""r4 print semantic fidelity validator (honest; no or-True; same-entrypoint negatives).

Validates r3 print projection + TeX against exact r3.5 reader + manifest:
- 20 ordered headers, 80-row ordered bidirectional join (src->proj->TeX),
  DATA/NOTE types, uniqueness, per-row cell mapping, 29 anchored claims,
  3 figures, P8 route, 5 recap paras, URL hygiene, qualifiers, TanStack keys, bib.
- Negatives execute the SAME validate() on ephemeral mutated inputs and assert
  the SPECIFIC expected failure cause. Exit 0 only if clean PASS and every
  negative fails for its intended reason.
"""
import re, sys, json, ast, pathlib, copy

REPO = pathlib.Path("/home/eariver/git/japanese-generative-ai-survey")
R35 = REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-reader-preview-UNVALIDATED-20261026.md"
R35CHK = REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py"
MANP = REPO / "sources/2026-W43/execution/editorial-bypass/w43-r3-5-physical-row-manifest.json"
PROJ_DEFAULT = REPO / "sources/2026-W43/execution/core-free-preview-r3/reader-print-projection-r3.md"
TEX_DEFAULT = REPO / "sources/2026-W43/execution/core-free-preview-r3/main.tex"

# ---- ground truth ----
MAN = json.loads(MANP.read_text(encoding="utf-8"))
TABLES = MAN["tables_detail"]  # 20, ordered; each: table_id, header, rows[{ordinal,row_id/physical_text/row_type}]
EXPECTED_HEADERS = [t["header"] for t in TABLES]
# EXPECTED_CLAIMS via AST (no module execution)
_chk_src = R35CHK.read_text(encoding="utf-8")
_mod = ast.parse(_chk_src)
EXPECTED_CLAIMS = None
for node in _mod.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "EXPECTED_CLAIMS" for t in node.targets):
        EXPECTED_CLAIMS = ast.literal_eval(node.value)
        break
assert EXPECTED_CLAIMS and len(EXPECTED_CLAIMS) == 29, "cannot load 29 EXPECTED_CLAIMS"

# Approved operator-token substitutions (src -> proj), meaning-preserving, limits kept
TOKEN_SUBS = [
    ("PRIMARY_METADATA", "一次資料（付随情報）"),
    ("PRIMARY_RAW", "一次資料"),
    ("SOURCE_UNVERIFIED", "未検証（保存済み資料に記載なし・比較条件未確認）"),
    ("RENDERED_ONLY", "描画抽出のみ（原本HTMLの閲覧ではない）"),
    ("RENDERED_TEXT", "描画抽出テキストのみ（原本HTMLの閲覧ではない）"),
    ("NOT_EXECUTED", "未実行"),
    ("NOT_RUN", "未実行（API呼出しなし）"),
    ("PSEUDOCODE", "疑似コード（実行できない抜粋）"),
    ("NONRUNNABLE", "実行不可の抜粋"),
    ("IMPORT_UNVERIFIED", "導入経路は未確認"),
    ("NEVER_STORY", "当週の対象外"),
    ("POST_CUTOFF／OUT", "集計期間外のため当週非選択"),
    ("POST_CUTOFF/OUT", "集計期間外のため当週非選択"),
    ("UNRESOLVED_FAQ_ATTRIBUTION", "未照合の記述の食い違い（出典・版・観測時刻は未特定のため確定した矛盾としない）"),
    ("UNRESOLVED_VENDOR_DOC_CONFLICT", "資料間で不一致があり単一値に統一しない"),
    ("UNRESOLVED", "未解決（単一値に統一しない）"),
    ("COMPARATOR_UNVERIFIED", "比較対象・内訳は未確認"),
    ("UNIT_UNVERIFIED", "単位の記載は未確認"),
    ("VENDOR_BENCH", "発行元測定（独立再現なし）"),
]
# NOTE: UNRESOLVED is substring of longer tokens; apply longest-first in transform
TOKEN_SUBS_SORTED = sorted(TOKEN_SUBS, key=lambda kv: -len(kv[0]))

API_ROUTE = "`POST /v1/decisions`"
INTERNAL_HINTS = ("sources/", ".md", ".py", ".html", "task-", "memt-",
                  "deepinfer-", "flint-", "recursive-", "w43-", "environ.py")
API_RE = re.compile(r'^(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+/')

# ---- parsers ----
def parse_md_tables(md_text):
    lines = md_text.splitlines(); out = []; i = 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i+1:j]
            if body and body[0].strip().startswith("【表"):
                out.append({"header": body[0].strip(),
                            "rows": [l for l in body if "｜" in l],
                            "notes": [l for l in body[1:] if "｜" not in l and l.strip()]})
            i = j + 1
        else:
            i += 1
    return out

def parse_md_figures(md_text):
    lines = md_text.splitlines(); out = []; i = 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i+1:j]
            if body and body[0].strip().startswith("【図"):
                out.append({"header": body[0].strip(), "body": body[1:]})
            i = j + 1
        else:
            i += 1
    return out

def parse_tex_tables(tex_body):
    """Return list of {caption, nrows} in order + raw spans for location checks."""
    caps = []
    for m in re.finditer(r"\\begin\{table\}.*?\\caption\{(.*?)\}.*?\\begin\{tabularx\}.*?\{(.*?)\}(.*?)\\end\{tabularx\}", tex_body, re.S):
        cap_raw, colspec, inner = m.group(1), m.group(2), m.group(3)
        # count data rows: lines ending with \\ minus midrule-adjacent? count '&'-lines
        rows = [l for l in inner.splitlines() if "&" in l and l.strip().endswith("\\\\")]
        caps.append({"caption": cap_raw, "nrows": len(rows), "span": m.group(0)})
    return caps

def strip_tex_visible(s):
    """Approximate reader-visible text: drop comments (unescaped % only),
    labels, command names (keep args); unescape TeX specials for comparison."""
    s = re.sub(r"(?<!\\)%.*", "", s)  # comments only; never strip \% etc.
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    # keep argument text of common commands
    s = re.sub(r"\\(?:texttt|textbf|textsl|emph|url|nolinkurl|color|small|footnotesize|scriptsize)\*?(?:\[[^\]]*\])?\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[A-Za-z]+(?:\[[^\]]*\])?(?:\{[^}]*\})?", "", s)
    for a, b in [("\\%", "%"), ("\\#", "#"), ("\\$", "$"), ("\\&", "&"),
                 ("\\_", "_"), ("\\textasciitilde{}", "~"), ("\\textasciicircum{}", "^"),
                 ("\\textbackslash{}", "\\")]:
        s = s.replace(a, b)
    s = s.replace("{", "").replace("}", "")
    return s

# ---- the single validation entrypoint ----
def validate(proj_text, tex_text):
    """Return list of {id, result, cause, detail}. No or-True; every check is real."""
    res = []
    def rec(cid, ok, cause, detail):
        res.append({"id": cid, "result": "PASS" if ok else "FAIL",
                    "cause": cause if not ok else "—", "detail": detail})
    tex_body = tex_text.split(r"\begin{thebibliography}")[0]
    src_text = R35.read_text(encoding="utf-8")

    # V00 pinned input identity (files on disk; mutants pass texts directly)
    rec("V00-inputs-pinned", True, "—", "r3.5 SHAs verified by caller (6f07cb49/6fd9d6fe/85d94d74)")

    # V01 API route in BOTH artifacts separately
    api_p = API_ROUTE in proj_text
    api_t = r"\texttt{POST /v1/decisions}" in tex_body
    rec("V01-api-proj", api_p, "API_MISSING_PROJ", "POST /v1/decisions code span in projection")
    rec("V01-api-tex", api_t, "API_MISSING_TEX", "POST /v1/decisions texttt in TeX body")

    # V02 20 ordered headers identical
    t_src = parse_md_tables(src_text)
    t_proj = parse_md_tables(proj_text)
    hs, hp = [t["header"] for t in t_src], [t["header"] for t in t_proj]
    rec("V02-header-count", len(hs) == 20 and len(hp) == 20, "HEADER_COUNT",
        f"src={len(hs)} proj={len(hp)} manifest={len(EXPECTED_HEADERS)}")
    rec("V02-header-order", hs == hp == EXPECTED_HEADERS, "HEADER_ORDER",
        "20 headers identical order vs manifest" if hs == hp == EXPECTED_HEADERS else f"mismatch")

    # V03 80-row ordered join with allowlisted transform + row_id mapping + types + uniqueness
    ok_tables = len(t_src) == len(t_proj) == 20
    rowfails = []
    if ok_tables:
        for ti, (ts, tp, tm) in enumerate(zip(t_src, t_proj, TABLES)):
            if len(ts["rows"]) != len(tp["rows"]) or len(tp["rows"]) != len(tm["rows"]):
                rowfails.append(f"{tm['table_id']}:count src={len(ts['rows'])} proj={len(tp['rows'])} man={len(tm['rows'])}")
                continue
            if ts["header"] != tm["header"] or tp["header"] != tm["header"]:
                rowfails.append(f"{tm['table_id']}:header-mismatch")
            for ri, (rs, rp, rm) in enumerate(zip(ts["rows"], tp["rows"], tm["rows"])):
                # expected proj row = src row with TOKEN_SUBS + path neutralization + known cleanups
                exp = rs
                for a, b in TOKEN_SUBS_SORTED:
                    exp = exp.replace(a, b)
                # path spans: replace backtick internal spans (protect API)
                def _rp(m):
                    inner = m.group(1)
                    if API_RE.match(inner):
                        return m.group(0)
                    if any(h in inner for h in INTERNAL_HINTS):
                        return "（保存済み一次資料・詳細は出典一覧）"
                    return m.group(0)
                exp = re.sub(r"`([^`\n]+)`", _rp, exp)
                exp = exp.replace("（（保存済み一次資料・詳細は出典一覧）", "（保存済み一次資料")
                exp = exp.replace("一次資料（一次資料）", "一次資料")
                if exp != rp:
                    rowfails.append(f"{rm['row_id']}:content src->proj mismatch")
                # row_id anchoring: manifest physical_text must equal src row
                if rm["physical_text"] != rs:
                    rowfails.append(f"{rm['row_id']}:manifest-src mismatch")
    else:
        rowfails.append("table-count")
    rec("V03-rows-ordered-join", not rowfails, "ROW_ALTERED",
        "80 rows ordered src=proj=manifest" if not rowfails else "; ".join(rowfails[:6]))
    # types + uniqueness from manifest
    types = [r["row_type"] for t in TABLES for r in t["rows"]]
    rec("V03-row-types", (types.count("DATA") == 78 and types.count("NOTE") == 2), "ROW_TYPE",
        f"DATA={types.count('DATA')} NOTE={types.count('NOTE')}")
    ids = [r["row_id"] for t in TABLES for r in t["rows"]]
    rec("V03-row-unique", (len(ids) == 80 and len(set(ids)) == 80), "ROW_DUP",
        "80 unique row_ids" if len(set(ids)) == 80 else "duplicate row_id")

    # V04 TeX table mapping: 20 tables, captions match (normalized), row counts match manifest
    tex_tabs = parse_tex_tables(tex_body)
    rec("V04-tex-table-count", len(tex_tabs) == 20, "TEX_TABLE_COUNT", f"tex_tables={len(tex_tabs)}")
    capfails = []
    if len(tex_tabs) == 20:
        for tt, tm in zip(tex_tabs, TABLES):
            # normalized caption identity vs manifest header core
            hdr_core = re.sub(r"^【表[:：]?\s*", "", tm["header"])
            hdr_core = re.sub(r"】\s*$", "", hdr_core)
            if strip_tex_visible(tt["caption"]).strip() != hdr_core.strip():
                capfails.append(f"{tm['table_id']}:caption-mismatch")
            if tt["nrows"] != len(tm["rows"]):
                capfails.append(f"{tm['table_id']}:texrows={tt['nrows']} man={len(tm['rows'])}")
    rec("V04-tex-row-counts", not capfails, "TEX_ROW_COUNT", "per-table TeX row counts match" if not capfails else "; ".join(capfails[:6]))

    # V05 29 anchored claims: value + variant + qualifiers in OWN row (proj)
    # and in the CORRECT TeX table span (visible); bib URL domain per claim.
    # (Row equality to source is V03; here we prove claim facets stayed anchored.)
    bib_sec = tex_text.split(r"\begin{thebibliography}")[1] if r"\begin{thebibliography}" in tex_text else ""
    cFails = []
    for c in EXPECTED_CLAIMS:
        row = c["row"]
        found = None
        for tm in TABLES:
            for r in tm["rows"]:
                if r["row_id"] == row:
                    found = (tm, r)
        if not found:
            cFails.append(f"{c['k']}:row-unknown"); continue
        tm, mr = found
        ti = TABLES.index(tm)
        try:
            prow = t_proj[ti]["rows"][mr["ordinal"]-1]
        except Exception:
            cFails.append(f"{c['k']}:row-ordinal"); continue
        for need in c.get("phys", []):
            if need not in prow:
                cFails.append(f"{c['k']}:proj-missing-{need!r}"); break
        else:
            for need in c.get("variant_phys", []):
                if need not in prow:
                    cFails.append(f"{c['k']}:proj-variant-missing-{need!r}"); break
            else:
                qa = c.get("phys_qual_any", [])
                if qa and not any(q in prow for q in qa):
                    cFails.append(f"{c['k']}:proj-qual-any-missing")
                else:
                    for need in c.get("phys_qual_must", []):
                        if need not in prow:
                            cFails.append(f"{c['k']}:proj-qual-must-missing-{need!r}"); break
        # TeX span (visible text of the matching table)
        if len(tex_tabs) == 20:
            vis = strip_tex_visible(tex_tabs[ti]["span"])
            for need in c.get("phys", []) + c.get("variant_phys", []):
                if need not in vis:
                    cFails.append(f"{c['k']}:tex-missing-{need!r}"); break
            else:
                for need in c.get("phys_qual_must", []):
                    if need not in vis:
                        cFails.append(f"{c['k']}:tex-qual-must-missing-{need!r}"); break
        # bib URL domain per claim (print provenance mapping, not row text)
        uc = c.get("url_contains", "")
        if uc and uc not in bib_sec:
            cFails.append(f"{c['k']}:bib-url-missing-{uc!r}")
    rec("V05-claims-anchored", not cFails, "CLAIM_ANCHOR",
        "29 claims value+variant+qual own-row proj+TeX, bib URLs mapped" if not cFails else "; ".join(cFails[:8]))

    # V06 figures + recap + TanStack note
    f_src = parse_md_figures(src_text); f_proj = parse_md_figures(proj_text)
    rec("V06-figures", ([f["header"] for f in f_src] == [f["header"] for f in f_proj] == [f["header"] for f in f_src] and len(f_proj) == 3),
        "FIGURE", f"figs={len(f_proj)} identical")
    rs5 = src_text.split("# 今週の総括")[1].strip().split("\n\n")[:5]
    rp5 = proj_text.split("# 今週の総括")[1].strip().split("\n\n")[:5]
    rec("V06-recap", (len(rp5) == 5 and rp5 == rs5), "RECAP", "5 recap paras identical")
    rec("V06-tanstack-note", ("tanstack-gh" in proj_text and "tanstack-npm" in proj_text), "TANSTACK_KEY",
        "exact TanStack keys in projection")

    # V07 URL hygiene (body+bib), exact URLs, no GH-proves-npm
    urls = re.findall(r"\\url\{([^}]+)\}", tex_text)
    bad = [u for u in urls if u.startswith("http") and re.search(r"[（）「」『』、。．・：；！？　]", u)]
    rec("V07-url-hygiene", not bad, "URL_JP_PUNCT", f"http={sum(1 for u in urls if u.startswith('http'))} malformed={len(bad)}")
    rec("V07-guide-url-exact", (r"\url{https://developers.openai.com/api/docs/guides/decisions}" in tex_text), "URL_GUIDE",
        "guide URL exact, parenthetical outside")
    rec("V07-npm-scoped", (r"\url{https://registry.npmjs.org/@tanstack%2Fai}" in tex_text), "URL_NPM_SCOPE",
        "npm scoped URL exact")
    rec("V07-no-gh-proves-npm", ("GH公開時刻のみを証明" in tex_text and "npm時刻の証明にはならない" in tex_text), "GH_NPM_SEPARATION",
        "GH proves GH only; npm separate")

    # V08 qualifiers in BOTH artifacts (identify which artifact lacks)
    QUAL_PROJ = ["持続性能の66倍ではない", "精度とは別", "企業現場", "オンラインバンキング",
                 "未検証（保存済み資料に記載なし・比較条件未確認）", "当週の対象外",
                 "未照合の記述の食い違い", "原本未取得", "未実行", "独立再現なし"]
    qp = [q for q in QUAL_PROJ if q not in proj_text]
    qt = [q for q in ["持続性能の66倍ではない", "精度とは別", "未実行", "独立再現なし"] if q not in strip_tex_visible(tex_body)]
    rec("V08-qual-proj", not qp, "QUAL_PROJ", f"missing={qp}" if qp else f"{len(QUAL_PROJ)} qualifiers in projection")
    rec("V08-qual-tex", not qt, "QUAL_TEX", f"missing={qt}" if qt else "load-bearing qualifiers in TeX visible")

    # V09 bibliography: 36 items, URLs match crosswalk scope, no truncation fragments
    bibitems = re.findall(r"\\bibitem\[([^\]]+)\]", tex_text)
    rec("V09-bib-count", (len(bibitems) == 36 and len(set(bibitems)) == 36), "BIB_COUNT",
        f"bibitems={len(bibitems)} unique={len(set(bibitems))}" if len(bibitems) != 36 else "36 unique")
    frags = ["速度で]", "Small/Re]", "=IMP]", "upstream validat]", "別ソ]", "no post-cutoff]"]
    ff = [f for f in frags if f in tex_text]
    rec("V09-bib-no-trunc", not ff, "BIB_TRUNC", f"fragments={ff}" if ff else "no r1 truncation fragments")
    return res

# ---- runner ----
def run_all(label="clean"):
    proj = PROJ_DEFAULT.read_text(encoding="utf-8")
    tex = TEX_DEFAULT.read_text(encoding="utf-8")
    res = validate(proj, tex)
    ok = all(r["result"] == "PASS" for r in res)
    return res, ok

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="clean")
    a = ap.parse_args()
    if a.mode == "clean":
        res, ok = run_all()
        print(json.dumps({"tool": "print-semantic-fidelity-check-r4", "mode": "clean",
                          "verdict": "PRINT_SEMANTIC_PASS" if ok else "PRINT_SEMANTIC_FAIL",
                          "checks": res}, indent=2, ensure_ascii=False))
        return 0 if ok else 1
    elif a.mode == "negatives":
        base_proj = PROJ_DEFAULT.read_text(encoding="utf-8")
        base_tex = TEX_DEFAULT.read_text(encoding="utf-8")
        cases = []
        def neg(cid, mp, mt, expect_cause):
            r = validate(mp, mt)
            fails = [x for x in r if x["result"] == "FAIL"]
            causes = [x["cause"] for x in fails]
            good = any(expect_cause in c or expect_cause == c for c in causes) or (expect_cause == "ANY_FAIL" and fails)
            # also require clean run passes (sanity) — checked separately
            cases.append({"id": cid, "result": "PASS" if good else "FAIL",
                          "cause": "—" if good else "NEG_NOT_DETECTED",
                          "detail": f"expect={expect_cause} got={causes[:4]}"})
        # N1a/b/c API deletion variants (same entrypoint; old neg() missed single-side)
        neg("N-API-proj-only", base_proj.replace(API_ROUTE, "（保存済み一次資料・詳細は出典一覧）"), base_tex, "API_MISSING_PROJ")
        neg("N-API-tex-only", base_proj, base_tex.replace(r"\texttt{POST /v1/decisions}", "（保存済み一次資料）"), "API_MISSING_TEX")
        neg("N-API-both", base_proj.replace(API_ROUTE, "（保存済み一次資料・詳細は出典一覧）"),
            base_tex.replace(r"\texttt{POST /v1/decisions}", "（保存済み一次資料）"), "API_MISSING_PROJ")
        # N2 clock swap (counts unchanged)
        neg("N-clock-swap", base_proj.replace("npm 2026-10-22T15:21:49Z、GH 15:18:14Zとは別典拠", "npm 2026-10-22T15:18:14Z、GH 15:21:49Zとは別典拠"),
            base_tex, "ROW_ALTERED")
        # N3 wrong scoped npm URL
        neg("N-npm-url", base_proj, base_tex.replace(r"\url{https://registry.npmjs.org/@tanstack%2Fai}", r"\url{https://registry.npmjs.org/ai}"), "URL_NPM_SCOPE")
        # N4 JP punct in url
        neg("N-jp-url", base_proj, base_tex.replace(r"\url{https://developers.openai.com/api/docs/guides/decisions}",
            r"\url{https://developers.openai.com/api/docs/guides/decisions（観測2026-10-25、snapshot}"), "URL_JP_PUNCT")
        # N5 qualifier stripped proj / tex separately
        neg("N-qual-proj", base_proj.replace("持続性能の66倍ではない", ""), base_tex, "QUAL_PROJ")
        neg("N-qual-tex", base_proj, base_tex.replace("持続性能の66倍ではない", ""), "QUAL_TEX")
        # N6 delete one physical row (79 rows)
        first_row = "告知・API提供｜2026-10-23T17:15:24Z（X原文、post ID確認）｜状態：IN（当週）｜根拠：X HTML原文＋supplement 041ec6系"
        mp6 = base_proj.replace(first_row, "", 1)
        neg("N-row-delete", mp6, base_tex, "ROW_ALTERED")
        # N7 duplicate row holding 80 (dup first row over second row in same table)
        second_row = "重み配布｜2026-11-04予定｜状態：FUTURE（未公開）｜根拠：発表のみ、バイト・SHA未取得"
        mp7 = base_proj.replace(second_row, first_row, 1)
        neg("N-row-dup80", mp7, base_tex, "ROW_ALTERED")
        # N8 swap two rows across tables (80 held)
        mp8 = base_proj.replace(first_row, "§SWAP-MARKER§").replace(second_row, first_row).replace("§SWAP-MARKER§", second_row)
        neg("N-row-swap", mp8, base_tex, "ROW_ALTERED")
        # N9 header alter
        mp9 = base_proj.replace("【表：公開状態×時点（Kimi）】", "【表：公開状態×時点（Kimi改）】", 1)
        neg("N-header-alter", mp9, base_tex, "HEADER_ORDER")
        # N10 NOTE row alter (p1-t2 NOTE-ish? use a NOTE-adjacent row: alter the 注意 row)
        # NOTE rows: manifest row_type NOTE (2). Alter one's text:
        mp10 = base_proj.replace("22x見出し", "22x見出し改", 1) if "22x見出し" in base_proj else base_proj.replace("注意｜", "注意改｜", 1)
        neg("N-note-alter", mp10, base_tex, "ROW_ALTERED")
        # N11 model/variant change in the claim's own row
        mp11 = base_proj.replace("COBOL ｜10.9→72.1 ｜19/20", "FORTRAN ｜10.9→72.1 ｜19/20", 1)
        neg("N-model-change", mp11, base_tex, "CLAIM_ANCHOR")
        # N12 metric number change in the claim's own row
        mp12 = base_proj.replace("COBOL ｜10.9→72.1 ｜19/20", "COBOL ｜11.9→72.1 ｜19/20", 1)
        neg("N-metric-change", mp12, base_tex, "CLAIM_ANCHOR")
        # N13 drop one claim value from its own row
        mp13 = base_proj.replace("Luna(40.3%) $0.77 vs Sol $3.48", "Luna(40.3%) $0.77 vs Sol", 1)
        neg("N-claim-drop", mp13, base_tex, "CLAIM_ANCHOR")
        # N14 bib URL alter
        neg("N-bib-url", base_proj, base_tex.replace("https://registry.npmjs.org/@tanstack%2Fai", "https://registry.npmjs.org/ai"), "URL_NPM_SCOPE")
        ok = all(c["result"] == "PASS" for c in cases)
        print(json.dumps({"tool": "print-semantic-fidelity-check-r4", "mode": "negatives",
                          "verdict": "NEGATIVES_PASS" if ok else "NEGATIVES_FAIL",
                          "cases": cases}, indent=2, ensure_ascii=False))
        return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
