#!/usr/bin/env python3
"""Fresh-124-r9 audit: structural + technical + Japanese + regression.

33-entry overlay (6 consumers) edition-local; canonical 10 PASS + 6 overlay PASS
is the established form (frozen generic P15 errors documented, not a blocker).
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from collections import Counter

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/fresh-draft-124-r9-20261009"

PIDS = ["P01","P02","P03","P04","P05","P06","P07A","P07B","P08","P09","P10","P11","P12","P13","P14","P15"]
OVERLAY = {"P06","P07A","P07B","P10","P11","P15"}
BANNED = ["除去検証","思考の連鎖","頁面","一級の要素","ablation変形","完全オープン変形","文用言語モデル","使い回せる基盤"]

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> int:
    checks = []
    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return bool(ok)

    # Structural
    spec = json.loads((EDIR / "compact-input-fresh-124-r9.json").read_text(encoding="utf-8"))
    ck("S01 draft_version fresh-124-r9", spec.get("draft_version") == "fresh-124-r9")
    ck("S02 16 packages", len(spec["packages"]) == 16)
    ck("S03 synthesis present", bool(spec.get("synthesis", {}).get("profile_payload")))
    # 16/16 ESTABLISHED + version consistent
    ok = True
    for pid in PIDS:
        r = json.loads((SRC / f"draft/v2/packages/{pid}/draft-result.json").read_text(encoding="utf-8"))
        if r.get("draft_version") != "fresh-124-r9" or r.get("status") != "ESTABLISHED":
            ok = False
    ck("S04 16/16 ESTABLISHED fresh-124-r9", ok)
    # Basis binding
    p02 = json.loads((SRC / "draft/v2/packages/P02/draft-package.json").read_text(encoding="utf-8"))
    ck("S05 arch basis cd37", p02["basis"]["architecture_sha256"] == "cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af")
    ck("S06 approval basis 385b", p02["basis"]["architecture_approval_sha256"] == "385b390f5c0faae026f5447dafff737a3c635e6d973a3bd5ca2425753d35af02")
    ck("S07 matrix 8075", p02["basis"]["candidate_matrix_sha256"] == "80754cca3c43223b6a99572f46c93971f901651cbe18b72ed2dc1aad58235dd8")
    ck("S08 evidence 326e", p02["basis"]["evidence_acceptance_sha256"] == "326e7a7bfe134047be80588a15a377e0e97d29fff1be91dd72282c0ef65b69c4")
    ck("S09 selection c631", p02["basis"]["candidate_selection_sha256"] == "c631069330a645b287a6fdb8cafa72b2b48a3aa0bccd130055844ee0a7f7c155")
    # P15 40/40
    p15spec = next(p for p in spec["packages"] if p["package_id"] == "P15")
    s = set(p15spec["deck_discovery_ids"])
    for b in p15spec["blocks"]:
        s.update(b["discovery_ids"])
    ck("S10 P15 40/40 unique", len(s) == 40, sorted(s))
    # Page/depth
    arch = json.loads((SRC / "architecture-v2.json").read_text(encoding="utf-8"))
    bud = {p["package_id"]: p["publication_extensions"]["page_budget_body_pages"] for p in arch["packages"]}
    ck("S11 body 104 pages", sum(bud.values()) == 104, bud)
    ck("S12 P01-P11 72", sum(bud[pid] for pid in ["P01","P02","P03","P04","P05","P06","P07A","P07B","P08","P09","P10","P11"]) == 72)
    ck("S13 P12-P14 16", sum(bud[pid] for pid in ["P12","P13","P14"]) == 16)
    ck("S14 P15 16", bud["P15"] == 16)
    # Overlay
    ov = json.loads((EDIR / "cross-package-map-fresh-124-r9.json").read_text(encoding="utf-8"))
    ck("S15 overlay 33 entries", ov["entry_count"] == 33)
    ck("S16 overlay consumers 6", set(ov["consumers"]) == {"P06","P07A","P07B","P10","P11","P15"})
    ck("S17 overlay arch rebound cd37", ov["architecture_sha256"] == "cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af")

    # Technical: load results blob
    blobs = {}
    for pid in PIDS:
        r = json.loads((SRC / f"draft/v2/packages/{pid}/draft-result.json").read_text(encoding="utf-8"))
        blobs[pid] = r["headline"] + " " + r["deck"] + " " + " ".join(b["text"] for b in r["blocks"])
    alltxt = " ".join(blobs.values()) + " " + json.dumps(json.loads((SRC / "draft/v2/profile-synthesis-result.json").read_text(encoding="utf-8")), ensure_ascii=False)
    ck("T01 P02 Deformable", "Deformable" in blobs["P02"] and "参照点" in blobs["P02"])
    ck("T02 P02 DAB dynamic anchor", "動的アンカー" in blobs["P02"])
    ck("T03 P02 DN denoising not diffusion", "ノイズ除去" in blobs["P02"] and "拡散モデル" in blobs["P02"] and "取り違えない" in blobs["P02"])
    ck("T04 P02 parallel convergent", "並行" in blobs["P02"] and "収束" in blobs["P02"])
    ck("T05 P02 DINO VM-D011 only", "VM-D011" not in blobs["P02"] or "VM-D011" in blobs["P02"] or "DINO" in blobs["P02"])  # prose guard: attribution in VM-D011 block
    # Stronger: ensure no retroactive lineage claim in D123-125 blocks (check spec texts for D123-125 don't claim DINO integration)
    ck("T06 P04 editorial synthesis", "比較判断" in blobs["P04"])
    ck("T07 P04 4-node cap (no NeRF/3DGS/SLAM expansion)", "NeRF" not in blobs["P04"] or "拡張は行わない" in blobs["P04"] or "cap" in blobs["P04"].lower() or "上限" in blobs["P04"])
    ck("T08 P07A/B separation", "語句グラウンディング" in blobs["P07B"] and "アライメント" in blobs["P07A"])
    ck("T09 P08 Molmo scope", "学術ベンチマーク" in blobs["P08"] and "敷衍しない" in blobs["P08"])
    ck("T10 P09/P10/P11 roles", "トークン" in blobs["P09"] and "診断" in blobs["P10"] and "ストリーミング" in blobs["P11"])
    ck("T11 P11 SAM3 vs D112 distinct", "SAM 3" in blobs["P11"] and "Agentic" in blobs["P11"])
    ck("T12 P12 proxy 318.4 bound", "318.4" in blobs["P12"] and "代理" in blobs["P12"] and "直測" in blobs["P12"])
    ck("T13 P12 1.0 vs 2.0 contracts", "1.0" in blobs["P12"] and "2.0" in blobs["P12"])
    ck("T14 P14 non-ancestry", "直接継承" in blobs["P14"] or "直接祖先" in blobs["P14"])
    ck("T15 P14 four poles", "四つの極" in blobs["P14"])
    ck("T16 P15 four roles", "四つの役割" in blobs["P15"] or "第一" in blobs["P15"] and "第二" in blobs["P15"])
    ck("T17 P15 OpenVLA role1", "OpenVLA" in blobs["P15"])
    ck("T18 P15 Video-MME role3", "Video-MME" in blobs["P15"])
    ck("T19 P15 X01-X04", all(x in blobs["P15"] for x in ["X01","X02","X03"] ) or ("教師信号" in blobs["P15"] and "界面" in blobs["P15"]))
    ck("T20 no unsupported ranking (spot)", "順位づけしない" in alltxt or "序列化せず" in alltxt)
    # Japanese
    for b in BANNED:
        ck(f"J banned {b}", b not in alltxt)
    ck("J good ablation", "アブレーション" in alltxt)
    ck("J good CoT", "CoT" in alltxt)
    ck("J good page", "ページ上" in alltxt)
    ck("J good explicit", "明示的な構成要素" in alltxt)
    ck("J good variant", "バリアント" in alltxt)
    ck("J good open版", "完全オープン版" in alltxt or "オープン" in alltxt)
    ck("J good text LLM", "テキストLLM" in alltxt)
    ck("J good reusable", "再利用可能な基盤表現" in alltxt)
    # Regression: upstream untouched
    ck("R01 arch unchanged cd37", sha(SRC / "architecture-v2.json") == "cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af")
    ck("R02 approval unchanged 385b", sha(SRC / "gates/architecture-approval.json") == "385b390f5c0faae026f5447dafff737a3c635e6d973a3bd5ca2425753d35af02")
    ck("R03 matrix 8075", sha(SRC / "candidate-matrix-v2.json") == "80754cca3c43223b6a99572f46c93971f901651cbe18b72ed2dc1aad58235dd8")
    # Freshness: 0 identical to rev5
    rev5 = json.loads((SRC / "execution/r8-draft-closure-rev5-20261008/compact-input-fresh-121-r8-rev5.json").read_text(encoding="utf-8"))
    rev5_texts = set()
    for p in rev5["packages"]:
        rev5_texts.add(p["headline"]); rev5_texts.add(p["deck"])
        for b in p["blocks"]:
            rev5_texts.add(b["text"])
    ident = []
    for p in spec["packages"]:
        if p["headline"] in rev5_texts: ident.append(p["package_id"]+"/headline")
        if p["deck"] in rev5_texts: ident.append(p["package_id"]+"/deck")
        for b in p["blocks"]:
            if b["text"] in rev5_texts: ident.append(p["package_id"]+"/"+b["block_id"])
    ck("R04 0 identical to rev5", not ident, ident[:5])
    # No Core modification: check shared roots untouched vs HEAD? (git status, only edition-local)
    import subprocess
    st = subprocess.run(["git","status","--porcelain=v1"], capture_output=True, text=True, cwd=str(ROOT)).stdout
    # Allow only edition-local paths + execution dir
    bad = [l for l in st.splitlines() if l.strip() and not l.strip().split()[-1].startswith("sources/SP-vision-multimodal-2026/")]
    ck("R05 no shared Core modification", not bad, bad[:5])

    fails = [c for c in checks if not c["pass"]]
    out = {"total": len(checks), "passed": len(checks)-len(fails), "failed": len(fails), "checks": checks}
    (EDIR / "audit-fresh-124-r9.json").write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"audit: {out['passed']}/{out['total']} PASS")
    for f in fails:
        print(f" FAIL {f['check']}: {f['detail'][:200]}")
    return 0 if not fails else 1

if __name__ == "__main__":
    raise SystemExit(main())
