#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""日更枚举器（2026-10-18 18:00）——复用周度全量器逻辑，输出日更契约文件。

背景：10-18 09:22 周度对账已跑过一轮全量（1409 条 → 账本 1413），
本次为同一日 18:00 的日更增量，需覆盖 09:22 之后的新增。

REST 限制（2026-10-18 实测）：
  - get_knowledge_list 不返回 media_state（全 None）
  - 不返回 create_time（全 None）
  - 不返回 file_number（全 0）→ 无法按计数/时间剪枝，只能全量递归
故本脚本 = 全量递归 + 日更契约输出（root/items），folder 条目源头剔除。
"""
import json
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _ima_enum_full_20261018 as base  # noqa: E402

ROOT = base.ROOT
DATE = "20261018"
OUT = os.path.join(ROOT, ".tools", f"_ima_enum_{DATE}.json")


def is_folder(e):
    return base.is_folder(e)


def main():
    items, folders = [], []
    root = base.list_folder(None)
    print(f"root: {len(root)}")
    for e in root:
        e["_kb_chain"] = ""
    items.extend(root)

    queue = [(e["media_id"], e.get("title", "")) for e in root if is_folder(e)]
    seen, n = set(), 0
    while queue:
        fid, chain = queue.pop(0)
        if fid in seen:
            continue
        seen.add(fid)
        sub = base.list_folder(fid)
        n += 1
        print(f"  [{n}] {chain or '(root)'}: {len(sub)}", flush=True)
        for e in sub:
            e["_kb_chain"] = (chain + "/" + e.get("title", "")) if chain else e.get("title", "")
        items.extend(sub)
        for e in sub:
            if is_folder(e):
                queue.append((e["media_id"], e.get("_kb_chain", "")))
        time.sleep(base.INTERVAL)

    file_items = []
    for e in items:
        if is_folder(e):
            folders.append({
                "media_id": e.get("media_id"), "title": e.get("title"),
                "chain": e.get("_kb_chain", ""),
                "file_number": e.get("file_number"),
                "folder_number": e.get("folder_number"),
                "parent_folder_id": e.get("parent_folder_id"),
            })
            continue
        chain = e.get("_kb_chain", "")
        title = e.get("title", "")
        file_items.append({
            "media_id": e.get("media_id"),
            "media_type": e.get("media_type"),
            "title": title,
            "create_time": e.get("create_time"),
            "media_state": e.get("media_state"),
            "kb_path": (chain + "/" + title) if chain else title,
            "parent_folder_id": e.get("parent_folder_id"),
        })

    dedup, dup = {}, 0
    for it in file_items:
        if it["media_id"] in dedup:
            dup += 1
            continue
        dedup[it["media_id"]] = it
    all_items = list(dedup.values())

    mt = Counter(str(it.get("media_type")) for it in all_items)
    out = {
        "_mode": "daily-full-rest",
        "_date": DATE,
        "_folders_visited": len(seen),
        "_file_items_raw": len(file_items),
        "_dup_paths": dup,
        "_unique_items": len(all_items),
        "_media_type_hist": dict(sorted(mt.items(), key=lambda x: -x[1])),
        "root": [{"media_id": e.get("media_id"), "title": e.get("title"),
                  "media_type": e.get("media_type"),
                  "folder_info": {"folder_id": e.get("media_id"),
                                  "file_number": e.get("file_number", 0),
                                  "folder_number": e.get("folder_number", 0),
                                  "parent_folder_id": ""}}
                 for e in root if is_folder(e)],
        "items": all_items,
        "folders": folders,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n遍历 {len(seen)} 文件夹 · 文件条目 {len(file_items)} · 去重 {len(all_items)} · 重复 {dup}")
    print(f"类型分布 {out['_media_type_hist']}")
    print(f"→ {OUT}")


if __name__ == "__main__":
    main()
