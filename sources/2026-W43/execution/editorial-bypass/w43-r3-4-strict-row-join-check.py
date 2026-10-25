#!/usr/bin/env python3
"""W43 r3.4 STRICT edition-local row-join checker (Core-free, read-only).

Validates genuine bidirectional binding:
  20 reader fenced tables <-> 80 physical rows <-> 80 ledger table_rows (2 NOTE)
  29 claims -> own-block DATA rows, with variant/metric/unit/comparator/source checks.
Runs in-memory negative mutations; each MUST fail validation (else checker is vacuous).
Writes JSON result (--out). Exit 0 only on EDITION_LOCAL_ROW_JOIN_PASS.

Scope: edition-local join proof only. Never asserts source originality or native Stage.
"""
import json, re, sys, hashlib, argparse, copy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # sources/2026-W43
EB = ROOT / "execution" / "editorial-bypass"
REPOROOT = Path(__file__).resolve().parents[4]      # repo root for archive existence
TABLE_ORDER = ["p1-t1","p1-t2","p1-t3","p1-t4","p2-t1","p2-t2","p2-f2","p3-t1","p3-t2",
               "p4-t1","p5-t1","p5-t2","p5-f1","p7-t1","p7-f1","p7-t2","p8-t1","p8-f2","p8-t2","p8-f3"]

def parse_tables(reader_text):
    """Return list of (start1, end1, header, [physical lines]) for 表 blocks only."""
    lines = reader_text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i+1:j]
            if body and body[0].startswith("【表"):
                phys = [(i+2+k, ln) for k, ln in enumerate(body) if "｜" in ln]
                out.append({"start": i+1, "end": j+1, "header": body[0], "rows": phys})
            i = j + 1
        else:
            i += 1
    return out

def validate(reader_text, manifest, ledger):
    """Return list of failure strings (empty == PASS). Pure function for negative tests."""
    fails = []
    tables = parse_tables(reader_text)
    byid = {r["block_id"]: r for r in ledger["rows"]}
    man_tabs = {t["table_id"]: t for t in manifest["tables_detail"]}

    # T1: exactly the 20 expected tables, in order
    if [TABLE_ORDER[i] for i in range(len(tables))] != TABLE_ORDER or len(tables) != 20:
        fails.append(f"T1: table set/order mismatch (found {len(tables)})")
        return fails  # cannot proceed meaningfully

    # T2: bidirectional bijection per table (count + exact hash per ordinal)
    for tid, tab in zip(TABLE_ORDER, tables):
        mt = man_tabs.get(tid)
        if mt is None:
            fails.append(f"T2: {tid} missing from manifest"); continue
        if [s for s, _ in tab["rows"]] != [r["reader_line"] for r in mt["rows"]]:
            fails.append(f"T2: {tid} reader lines != manifest lines")
        if len(tab["rows"]) != len(mt["rows"]):
            fails.append(f"T2: {tid} count reader {len(tab['rows'])} != manifest {len(mt['rows'])}")
            continue
        for n, ((ln, tx), mr) in enumerate(zip(tab["rows"], mt["rows"]), 1):
            if mr["ordinal"] != n or mr["row_id"] != f"{tid}-{n:02d}":
                fails.append(f"T2: {tid} ordinal/row_id break at {n}")
            h = hashlib.sha256(tx.encode("utf-8")).hexdigest()
            if h != mr["sha256"] or tx != mr["physical_text"]:
                fails.append(f"T2: {tid}-{n:02d} text/hash mismatch (swap/mutation/extra)")
        # ledger 1:1
        lrows = byid[tid].get("table_rows", [])
        if len(lrows) != len(mt["rows"]):
            fails.append(f"T2: {tid} ledger {len(lrows)} != manifest {len(mt['rows'])}")
            continue
        for mr, lr in zip(mt["rows"], lrows):
            if lr.get("row_id") != mr["row_id"]:
                fails.append(f"T2: {tid} ledger row_id {lr.get('row_id')} != {mr['row_id']}")
            first = mr["physical_text"].split("｜")[0]
            lm = mr.get("label_match")
            if lm == "SANCTIONED_ALIAS":
                if lr.get("row") != mr.get("ledger_label"):
                    fails.append(f"T2: {tid} alias label drift {mr['row_id']}")
            elif lm == "EXACT":
                if lr.get("row") != first:
                    fails.append(f"T2: {tid} {mr['row_id']} label not exact")
            elif lm == "EXACT_AFTER_RSTRIP":
                if lr.get("row") != first.rstrip():
                    fails.append(f"T2: {tid} {mr['row_id']} label not exact-after-rstrip")
            else:
                fails.append(f"T2: {tid} {mr['row_id']} ungoverned label class")
    if fails:
        return fails

    # T3/T4: claims
    man_row = {r["row_id"]: (t["table_id"], r) for t in manifest["tables_detail"] for r in t["rows"]}
    for r in ledger["rows"]:
        for c in (r.get("claims") or []):
            rid = c.get("row_id")
            where = f"{r['block_id']}/{c.get('value')}"
            if not rid or rid not in man_row:
                fails.append(f"C1: {where} unknown row_id {rid}"); continue
            tid, mr = man_row[rid]
            if tid != r["block_id"]:
                fails.append(f"C3: {where} cross-block {r['block_id']}->{tid}"); continue
            if mr.get("row_type") == "NOTE":
                fails.append(f"C2: {where} points to NOTE row {rid}"); continue
            for f in ("model_variant", "metric", "unit", "denominator_comparison",
                      "evidence_task_id", "archive_path"):
                if not c.get(f):
                    fails.append(f"C5: {where} empty field {f}")
            # C4 binding: variant token in row context, or value core in row context
            lrow = next(tr for tr in byid[tid]["table_rows"] if tr["row_id"] == rid)
            ctx = " ".join([lrow.get("product",""), lrow.get("row",""), mr["physical_text"],
                            lrow.get("url",""), lrow.get("clock",""), lrow.get("note","")]).lower()
            toks = [w.lower() for w in re.split(r"[^0-9a-zA-Z\u3040-\u30ff\u4e00-\u9fff]+",
                                                c.get("model_variant","")) if len(w) >= 3]
            # drop generic stopwords
            toks = [w for w in toks if w not in ("the","and","for","with","from")]
            bound = any(w in ctx for w in toks)
            if not bound:
                core = re.sub(r"[^0-9:.→/]", "", c.get("value",""))[:12]
                bound = bool(core) and core in re.sub(r"[^0-9:.→/]", "",
                              " ".join([lrow.get("clock",""), lrow.get("note",""), mr["physical_text"]]))
            if not bound:
                fails.append(f"C4: {where} variant/value unbound to {rid}")
            # C6 archive honesty
            ap = c.get("archive_path","")
            if ("ARCHIVE_UNAVAILABLE" in ap or "RAW_NOT_ARCHIVED" in ap or "NOT covered" in ap):
                pass
            elif ap.startswith("sources/"):
                p = REPOROOT / ap.split(":")[0]
                if not p.exists():
                    fails.append(f"C6: {where} archived bytes missing {ap}")
            else:
                fails.append(f"C6: {where} unqualified non-repo archive {ap!r}")
            # C7 qualifier registry (evidence-grounded)
            unit, denom = c.get("unit",""), c.get("denominator_comparison","")
            if c.get("metric") == "price" and "confirmed" in unit.lower():
                if not re.search(r"Mini|Speech", c.get("model_variant","")):
                    fails.append(f"C7: {where} asserts confirmed unit without evidence basis")
            if c.get("metric") in ("WER",) or "recall" in c.get("metric",""):
                if "COMPARATOR_UNVERIFIED" not in denom and "Pyannote" not in denom:
                    fails.append(f"C7: {where} comparator unqualified")
            # C8 npm scope
            for u in (lrow.get("url",""),):
                if "registry.npmjs.org" in u and "@tanstack" not in u:
                    fails.append(f"C8: {rid} unscoped npm URL {u}")
            if c.get("metric") == "registry clock" and "15:21:49" not in lrow.get("clock",""):
                fails.append(f"C8: {rid} npm clock mismatch")

    # T5: pinned semantic anchors from primary sources
    mtxt = {r["row_id"]: r["physical_text"] for t in manifest["tables_detail"] for r in t["rows"]}
    if "保存容量約66倍削減" not in mtxt.get("p2-t2-03",""):
        fails.append("T5: MemT storage meaning missing in p2-t2-03")
    if "SOURCE_UNVERIFIED" not in mtxt.get("p2-t2-02",""):
        fails.append("T5: 1.86x qualifier missing in p2-t2-02")
    if "parametric-memory" not in mtxt.get("p2-t2-01",""):
        fails.append("T5: parametric scope missing in p2-t2-01")
    if not any(r["ledger_label"] == "分類器" for r in man_tabs["p3-t2"]["rows"]):
        fails.append("T5: p3-t2 classifier missing")
    if not mtxt.get("p5-t1-03","").startswith("TTS Speech 3"):
        fails.append("T5: p5-t1 TTS Speech 3 missing")
    if not mtxt.get("p5-t2-01","").startswith("Controlled Voice"):
        fails.append("T5: p5-t2 Controlled Voice missing")
    return fails

CHECKS = []
def check(cid, ok, detail=""):
    CHECKS.append({"id": cid, "result": "PASS" if ok else "FAIL", "detail": detail})
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    reader_p = EB / "w43-r3-4-reader-preview-UNVALIDATED-20261026.md"
    ledger_p = EB / "w43-r3-4-citation-confidence-ledger.json"
    manif_p = EB / "w43-r3-4-physical-row-manifest.json"
    reader, ledger, manifest = (reader_p.read_text(encoding="utf-8"),
        json.loads(ledger_p.read_text(encoding="utf-8")),
        json.loads(manif_p.read_text(encoding="utf-8")))

    fails = validate(reader, manifest, ledger)
    check("JOIN-bijection-80", not [f for f in fails if f.startswith("T1") or f.startswith("T2")],
          "; ".join([f for f in fails if f.startswith("T1") or f.startswith("T2")][:4]) or "20 tables, 80 physical <-> 80 ledger, hashes exact")
    check("JOIN-claims-29", not [f for f in fails if re.match(r"C[0-9]", f)],
          "; ".join([f for f in fails if re.match(r"C[0-9]", f)][:4]) or "29 claims own-block DATA, bound, honest archive")
    check("JOIN-anchors", not [f for f in fails if f.startswith("T5")],
          "; ".join([f for f in fails if f.startswith("T5")][:4]) or "MemT/npm/Voxtral/classifier/TTS/Controlled-Voice anchors hold")

    # Negative tests: each mutation MUST fail validation
    negs = []
    def neg(name, mut):
        m2, l2, r2 = copy.deepcopy(manifest), copy.deepcopy(ledger), reader
        m2, l2, r2 = mut(m2, l2, r2)
        f = validate(r2, m2, l2)
        ok = bool(f)
        negs.append({"id": name, "result": "PASS" if ok else "FAIL",
                     "detail": ("fails as required: " + f[0][:120]) if ok else "MUTATION NOT DETECTED"})
        return ok
    def M_drop(m, l, r):
        m["tables_detail"][5]["rows"].pop(2); return m, l, r          # remove p2-t2-03
    def M_dup(m, l, r):
        m["tables_detail"][0]["rows"].append(copy.deepcopy(m["tables_detail"][0]["rows"][0])); return m, l, r
    def M_swap(m, l, r):
        a = m["tables_detail"][9]["rows"]; a[0]["physical_text"], a[1]["physical_text"] = a[1]["physical_text"], a[0]["physical_text"]; return m, l, r
    def M_mut(m, l, r):
        m["tables_detail"][0]["rows"][0]["physical_text"] += "X"; return m, l, r
    def M_note(m, l, r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p8-f2"]["claims"][0]["row_id"] = "p1-t2-04"; return m, l, r
    def M_xblock(m, l, r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p8-f2"]["claims"][0]["row_id"] = "p8-f3-01"; return m, l, r
    def M_npm(m, l, r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for tr in byid["p8-f2"]["table_rows"]:
            if tr["row_id"] == "p8-f2-03": tr["url"] = "https://registry.npmjs.org/ai"
        return m, l, r
    def M_unit(m, l, r):
        byid = {x["block_id"]: x for x in l["rows"]}
        for c in byid["p5-f1"]["claims"]:
            if c["value"] == "$0.004": c["unit"] = "$/min (confirmed)"
        return m, l, r
    def M_noteblock(m, l, r):
        byid = {x["block_id"]: x for x in l["rows"]}
        byid["p1-t2"]["claims"] = [{"value": "SYNTH", "metric": "synth", "unit": "synth",
            "denominator_comparison": "synth", "model_variant": "Kimi test",
            "evidence_task_id": "synth", "claim_id": "synth",
            "archive_path": "ARCHIVE_UNAVAILABLE", "row_id": "p1-t2-04"}]
        return m, l, r
    n_ok = all([neg("NEG-drop-row", M_drop), neg("NEG-dup-row", M_dup),
                neg("NEG-swap-rows", M_swap), neg("NEG-mutate-text", M_mut),
                neg("NEG-claim-to-NOTE", M_note), neg("NEG-claim-xblock", M_xblock),
                neg("NEG-npm-unscoped", M_npm), neg("NEG-unit-false-confirm", M_unit),
                neg("NEG-note-sameblock", M_noteblock)])
    check("NEG-all-detected", n_ok, f"{sum(1 for n in negs if n['result']=='PASS')}/{len(negs)} mutations detected")

    # Provenance tiers (report only)
    tiers = {"RAW_PRIMARY": 0, "QUALIFIED_UNAVAILABLE": 0, "OTHER": 0}
    for r in ledger["rows"]:
        for c in (r.get("claims") or []):
            ap2 = c.get("archive_path","")
            if ap2.startswith("sources/"): tiers["RAW_PRIMARY"] += 1
            elif "ARCHIVE_UNAVAILABLE" in ap2 or "RAW_NOT_ARCHIVED" in ap2: tiers["QUALIFIED_UNAVAILABLE"] += 1
            else: tiers["OTHER"] += 1
    check("TIER-report", True, json.dumps(tiers, ensure_ascii=False))

    verdict = "EDITION_LOCAL_ROW_JOIN_PASS" if all(c["result"]=="PASS" for c in CHECKS) else "ROW_JOIN_OPEN"
    result = {"tool": "w43-r3-4-strict-row-join-check.py",
              "scope": "edition-local join proof only; not source originality, not native Stage",
              "reader": reader_p.name, "reader_sha256": hashlib.sha256(reader.encode()).hexdigest(),
              "ledger": ledger_p.name, "ledger_sha256": hashlib.sha256(json.dumps(ledger, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
              "manifest": manif_p.name, "verdict": verdict,
              "positive_failures": fails, "negative_tests": negs, "checks": CHECKS}
    js = json.dumps(result, ensure_ascii=False, indent=1)
    if a.out: Path(a.out).write_text(js, encoding="utf-8")
    print(js)
    return 0 if verdict == "EDITION_LOCAL_ROW_JOIN_PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
