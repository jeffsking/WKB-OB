#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 账本对账归一：把 dedup 已确认编译的 synced 陈旧缓存翻为 compiled。

依据 AGENTS.md 与 MEMORY §二：「是否已编译」唯一权威 = wkb_dedup.py scan，账本只是同步层状态。
判据严格：仅当该条 raw_path 在 dedup 索引中命中（即有活跃 source 页登记）才翻；
未命中者一律不动（宁可留噪音，不可制造假已编译）。

幂等：重复运行第二次起改动数为 0。
"""
import importlib.util
import json
import os
import shutil
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
LEDGER = ".tools/_ima_sync_state.json"
TODAY = "2026-10-20"


def load_dedup():
    spec = importlib.util.spec_from_file_location("dd", ".tools/wkb_dedup.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    idx, _ = m.build_index(verbose=False)
    return idx


def main():
    idx = load_dedup()
    d = json.load(open(LEDGER, encoding="utf-8"))
    changed, skipped = [], []
    for mid, v in d["items"].items():
        if v.get("stage") != "synced":
            continue
        rp = v.get("raw_path")
        hits = idx.get(rp, []) if rp else []
        if not hits:
            skipped.append(mid)
            continue
        v["stage"] = "compiled"
        v["stage_source"] = "dedup-reconciled"
        v["stage_updated"] = TODAY
        v["source_page_hint"] = hits[0]
        changed.append(mid)

    if not changed:
        print("[reconcile] 无改动（幂等）")
        return

    bak = LEDGER + ".bak.%s-prereconcile" % TODAY.replace("-", "")
    shutil.copy2(LEDGER, bak)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print("[reconcile] 归一 %d 条 synced -> compiled（dedup 依据命中）" % len(changed))
    print("[reconcile] 跳过 %d 条（dedup 未命中，保持原状）" % len(skipped))
    print("[reconcile] 备份 -> %s" % bak)


if __name__ == "__main__":
    main()
