#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""账本多登明细取证：对 only_in_ledger 逐条给出 media_id / kb_path / 是否 .md.md 幽灵锚 /
RAW vs RAW_FULL 双侧落地情况 / 建议处置类别。只读。"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, ".tools", "_ima_sync_state.json")
RECON = os.path.join(ROOT, ".tools", "kb_pipeline_recon", "2026-10-25_recon.json")


def main():
    s = json.load(open(STATE, encoding="utf-8"))
    items = s.get("items", {})
    by_raw = {}
    for mid, it in items.items():
        rp = (it.get("raw_path") or "").replace("\\", "/")
        if rp:
            by_raw.setdefault(rp, []).append((mid, it))

    rec = json.load(open(RECON, encoding="utf-8"))
    only = rec["ledger_vs_raw"]["only_in_ledger"]

    rows = []
    for p in only:
        hits = by_raw.get(p, [])
        mid = hits[0][0] if hits else None
        it = hits[0][1] if hits else {}
        raw_ok = os.path.isfile(os.path.join(ROOT, p))
        full = p.replace("RAW/", "RAW_FULL/", 1)
        full_ok = os.path.isfile(os.path.join(ROOT, full))
        # 幽灵锚判定：插件把 .md 追加成 .md.md；或标题被截断（含 ...）
        ghost_mdmd = p.endswith(".md.md")
        trunc = "..." in os.path.basename(p) or "..." in (it.get("title") or "")
        # 目录下是否存在同名但少一层 .md 的实际文件
        cand = p[:-3] if ghost_mdmd else None
        cand_ok = bool(cand) and os.path.isfile(os.path.join(ROOT, cand))
        rows.append({
            "raw_path": p,
            "media_id": mid,
            "media_type": it.get("media_type"),
            "stage": it.get("stage"),
            "kb_path": it.get("kb_path"),
            "title": it.get("title"),
            "raw_exists": raw_ok,
            "rawfull_exists": full_ok,
            "ghost_mdmd": ghost_mdmd,
            "truncated_title": trunc,
            "candidate_real_path": cand,
            "candidate_exists": cand_ok,
        })

    print(json.dumps({
        "total": len(rows),
        "raw_exists": sum(1 for r in rows if r["raw_exists"]),
        "rawfull_exists": sum(1 for r in rows if r["rawfull_exists"]),
        "both_missing": sum(1 for r in rows if not r["raw_exists"] and not r["rawfull_exists"]),
        "ghost_mdmd": sum(1 for r in rows if r["ghost_mdmd"]),
        "ghost_mdmd_with_real_candidate": sum(1 for r in rows if r["candidate_exists"]),
        "truncated_title": sum(1 for r in rows if r["truncated_title"]),
        "rows": rows,
    }, ensure_ascii=False, indent=1))

    out = os.path.join(ROOT, ".tools", "_ledger_extra_20261025.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
