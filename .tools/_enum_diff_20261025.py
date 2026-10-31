#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全量枚举 vs 账本 差异分析（2026-10-25 周度对账）。

比对口径：
  · 枚举侧 = .tools/_ima_enum_full_<date>.json 的 items（media_id 集合）
  · 账本侧 = .tools/_ima_sync_state.json 的 items（media_id 集合）

输出四类：
  only_in_enum   IMA 有、账本无  → 账本漏登（应转 discovered）
  only_in_ledger 账本有、IMA 无  → IMA 侧已消失（只报，不删账本）
  common         两边都有
另附：枚举总数 vs 账本总数 vs RAW 实体数 三口径对照。

只读，不写账本。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "20261025"
ENUM = os.path.join(ROOT, ".tools", f"_ima_enum_full_{DATE}.json")
STATE = os.path.join(ROOT, ".tools", "_ima_sync_state.json")


def main():
    if not os.path.isfile(ENUM):
        print(f"[!] 枚举产物不存在：{ENUM}")
        return 1
    e = json.load(open(ENUM, encoding="utf-8"))
    s = json.load(open(STATE, encoding="utf-8"))

    e_items = e.get("items", [])
    e_map = {it["media_id"]: it for it in e_items if it.get("media_id")}
    l_map = s.get("items", {})

    only_enum = sorted(set(e_map) - set(l_map))
    only_ledger = sorted(set(l_map) - set(e_map))

    # 账本侧已终态却不在枚举里的（更值得关注：可能 IMA 侧被删）
    by_stage = {}
    for mid in only_ledger:
        st = l_map[mid].get("stage")
        by_stage.setdefault(st, []).append(mid)

    # RAW 实体数（判重锚口径）
    raw_n = 0
    for r, d, fs in os.walk(os.path.join(ROOT, "RAW")):
        if "attachments" in r or ".obsidian" in r:
            continue
        raw_n += sum(1 for f in fs if f.endswith(".md"))

    out = {
        "date": DATE,
        "enum": {k: v for k, v in e.items() if k not in ("items", "folders", "root")},
        "enum_items": len(e_map),
        "ledger_items": len(l_map),
        "raw_md_files": raw_n,
        "only_in_enum": len(only_enum),
        "only_in_ledger": len(only_ledger),
        "only_in_ledger_by_stage": {k: len(v) for k, v in by_stage.items()},
        "only_in_enum_detail": [
            {"media_id": m, "title": e_map[m].get("title"),
             "media_type": e_map[m].get("media_type"),
             "kb_path": e_map[m].get("kb_path")} for m in only_enum],
        "only_in_ledger_detail": [
            {"media_id": m, "stage": l_map[m].get("stage"),
             "raw_path": l_map[m].get("raw_path"),
             "kb_path": l_map[m].get("kb_path")} for m in only_ledger],
    }

    print(json.dumps({k: v for k, v in out.items()
                      if not k.endswith("_detail")}, ensure_ascii=False, indent=1))
    print("\n--- only_in_enum（账本漏登）前 20 ---")
    for x in out["only_in_enum_detail"][:20]:
        print(f"  [{x['media_type']}] {str(x['title'])[:60]}  ::  {str(x['kb_path'])[:60]}")
    print("\n--- only_in_ledger（IMA 侧无）前 20 ---")
    for x in out["only_in_ledger_detail"][:20]:
        print(f"  [{x['stage']}] {str(x['raw_path']).split('/WKB/')[-1][:70]}")

    p = os.path.join(ROOT, ".tools", f"_enum_diff_{DATE}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n→ {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
