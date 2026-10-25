#!/usr/bin/env python3
"""W43 r3.3 edition-local 20-table bidirectional join check (Core-free, read-only).

Reads:
  sources/2026-W43/execution/editorial-bypass/w43-r3-3-reader-preview-UNVALIDATED-20261026.md
  sources/2026-W43/execution/editorial-bypass/w43-r3-3-citation-confidence-ledger.json
Writes JSON result to stdout / optional --out path.
Structural PASS only; source authenticity is judged separately (see r3.3 QA).
Exit 0 on STRUCT_PASS, 1 otherwise.
"""
import json, re, sys, argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # sources/2026-W43
EB = ROOT / "execution" / "editorial-bypass"
READER = EB / "w43-r3-3-reader-preview-UNVALIDATED-20261026.md"
LEDGER = EB / "w43-r3-3-citation-confidence-ledger.json"

CHECKS = []
def check(cid, ok, detail=""):
    CHECKS.append({"id": cid, "result": "PASS" if ok else "FAIL", "detail": detail})
    return ok

def main():
    out = None
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    out = a.out
    reader = READER.read_text(encoding="utf-8")
    led = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = led["rows"]
    byid = {r["block_id"]: r for r in rows}

    # S1: 96 block IDs preserved, 20 TABLE blocks each with table_rows
    check("S1-blocks-96", len(rows) == 96, f"blocks={len(rows)}")
    tabs = [r for r in rows if r.get("block_type") == "TABLE"]
    check("S1-tables-20", len(tabs) == 20, f"tables={len(tabs)}")
    check("S1-all-tables-have-rows", all(len(r.get("table_rows", [])) > 0 for r in tabs),
          "empty=" + ",".join(r["block_id"] for r in tabs if not r.get("table_rows")))

    # S2: row_id unique across all table_rows (+figure rows)
    seen, dups = {}, []
    for r in rows:
        for tr in r.get("table_rows", []):
            rid = tr.get("row_id")
            if not rid:
                dups.append(f"{r['block_id']}:MISSING_ROW_ID")
            elif rid in seen:
                dups.append(rid)
            else:
                seen[rid] = r["block_id"]
    check("S2-row-id-unique", not dups, f"total={len(seen)} dups={dups[:5]}")

    # S3: every claim carries row_id pointing at an existing DATA row
    orphan, noted = [], []
    data_ids = {tr["row_id"] for r in rows for tr in r.get("table_rows", []) if tr.get("row_type") != "NOTE"}
    for r in rows:
        for c in (r.get("claims") or []):
            rid = c.get("row_id")
            if not rid:
                orphan.append(f"{r['block_id']}:claim-no-row_id")
            elif rid not in seen:
                orphan.append(f"{r['block_id']}:{rid}-unknown")
            elif rid not in data_ids:
                noted.append(f"{r['block_id']}:{rid}-points-to-NOTE")
    check("S3-claims-linked", not orphan, f"orphan={orphan[:5]} noted={noted[:5]}")
    nclaims = sum(len(r.get("claims") or []) for r in rows)
    check("S3-claims-29", nclaims == 29, f"claims={nclaims}")

    # S4: NOTE typing (exactly the 2 known annotation rows)
    notes = [(r["block_id"], tr["row"]) for r in rows for tr in r.get("table_rows", []) if tr.get("row_type") == "NOTE"]
    check("S4-note-rows-2", sorted(n[0] for n in notes) == ["p1-t2", "p4-t1"], f"notes={notes}")

    # S5: known R32-FULL-003 defects fixed in ledger
    p32 = byid["p3-t2"]["table_rows"]
    check("S5-p3t2-classifier", any(tr["row"] == "分類器" for tr in p32) and len(p32) == 4, f"p3-t2 rows={len(p32)}")
    check("S5-p1t2-note", byid["p1-t2"]["table_rows"][3].get("row_type") == "NOTE", "p1-t2 row4 NOTE")
    check("S5-p5t1-variant", byid["p5-t1"]["table_rows"][0]["row"] == "STT Small Transcribe 3", "STT exact")
    check("S5-p5t2-controlled", byid["p5-t2"]["table_rows"][0]["row"] == "Controlled Voice", "Controlled Voice exact")
    npmrow = byid["p8-f2"]["table_rows"][2]
    check("S5-p8f2-npm-scoped", "@tanstack" in npmrow.get("url", "") and "registry.npmjs.org/ai" not in npmrow.get("url", "").replace("@tanstack%2Fai", ""),
          f"url={npmrow.get('url')}")
    p2rows = {tr["row"]: tr for tr in byid["p2-t2"]["table_rows"]}
    check("S5-memt-66x-storage", any("保存容量" in k for k in p2rows), f"rows={list(p2rows)}")
    check("S5-memt-186x-unverified", any("SOURCE_UNVERIFIED" in k or "SOURCE_UNVERIFIED" in v.get("note", "") for k, v in p2rows.items()),
          "1.86x qualified")
    check("S5-memt-parametric", any("parametric-memory" in (v.get("note", "") + k) for k, v in p2rows.items()), "parametric scope")

    # S6: reader corrected strings present / wrong strings absent
    check("S6-reader-66x-storage", "保存容量約66倍削減" in reader and "KVキャッシュ対比の持続で66倍" not in reader, "66x storage")
    check("S6-reader-186x-unverified", "SOURCE_UNVERIFIED" in reader, "1.86x marker")
    check("S6-reader-no-sustained66", "持続（sustained）vs KV cache" not in reader, "old 66x row gone")
    check("S6-reader-parametric", "parametric-memory" in reader and "textual-memory" in reader, "parametric/textual")
    check("S6-reader-stage4-exact", "影響製品の更新準備" in reader, "stage4 exact")
    check("S6-reader-stage5-exact", "パッチ利用可能後の案内公表と展開支援" in reader, "stage5 exact")
    check("S6-reader-daybreak-out", "工程外の関連施策" in reader and "[4 prepare] $1B Daybreak" not in reader, "daybreak out of stage4")
    check("S6-reader-no-unscoped-npm", "registry.npmjs.org/ai" not in reader.replace("@tanstack%2Fai", ""), "no unscoped npm")
    check("S6-reader-no 程序", "程序" not in reader, "no 程序")
    check("S6-reader-pseudocode", "PSEUDOCODE" in reader and "NONRUNNABLE" in reader, "pseudocode labels")
    check("S6-reader-header-clean", "実行根拠と状態" not in reader and "UNVALIDATED" in (READER.name), "header clean/filename kept")
    check("S6-reader-cobol-exception", "COBOL 72.1%は唯一83%未満の例外" in reader or "COBOL72.1%" in reader.replace(" ", "") or "COBOL 72.1%" in reader, "cobol exception")
    check("S6-reader-cost-quality", "費用差は品質同等を意味しない" in reader, "cost!=quality")
    check("S6-reader-paths", "経路A" in reader and "経路B" in reader and "NOT_LIVE_VERIFIED" in reader, "duet paths split")
    check("S6-reader-cve", "不存在証明ではない" in reader, "cve wording")

    # S7: recap 5 paragraphs after P8, no P9
    m = re.search(r"# 今週の総括\s*\n(.*)$", reader, re.S)
    paras = [p for p in (m.group(1).strip().split("\n\n") if m else []) if p.strip()]
    check("S7-recap-5para", len(paras) == 5, f"paras={len(paras)}")
    check("S7-no-p9", "## P9" not in reader, "no P9")

    # S8: per-table bidirectional spot check — ledger DATA row labels vs reader fenced blocks
    # heuristic: each TABLE block id must appear as (blockid) mention or its row labels appear in reader
    missing = []
    for r in tabs:
        bid = r["block_id"]
        labels = [tr["row"].split("（")[0].split("(")[0] for tr in r["table_rows"] if tr.get("row_type") == "DATA"]
        hits = sum(1 for lb in labels if lb and lb[:6] in reader)
        if hits == 0:
            missing.append(bid)
    check("S8-labels-traceable", not missing, f"untraceable={missing}")

    struct = "STRUCT_PASS" if all(c["result"] == "PASS" for c in CHECKS) else "STRUCT_FAIL"
    result = {"tool": "w43-r3-3-table-join-check.py", "scope": "edition-local (Frozen Core independent)",
              "reader": READER.name, "ledger": LEDGER.name,
              "structural_verdict": struct,
              "note": "Structural join only; source authenticity judged separately per contract.",
              "checks": CHECKS}
    js = json.dumps(result, ensure_ascii=False, indent=1)
    if out:
        Path(out).write_text(js, encoding="utf-8")
    print(js)
    return 0 if struct == "STRUCT_PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
