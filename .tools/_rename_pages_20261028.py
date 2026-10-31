#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-28 页名语义化：把本批 8 页从「源文件名」改为语义页名，并三处同步。

铁律（2026-10-26 教训）：
  · 只替换 `[[旧名` 形式的 wikilink，**绝不碰 source_path / source_paths 里的 RAW 路径**；
  · 改名后同步 front matter `title`、账本 source_page_hint；
  · 改前备份到 .tools/_rename_backup_20261028/。
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SRC = "WIKI/sources"
STATE = ".tools/_ima_sync_state.json"
BAK = ".tools/_rename_backup_20261028"

RENAMES = {
    "会议纪要_HighSpeedConverting_20261027":
        "High Speed Converting Meeting 南京 2026-10-27（COCO V6 成型工艺与设备方向）",
    "Key point for COCO V6 engineer":
        "Key point for COCO V6 engineering plan（Bryan 五阶段路线）",
    "blizzard_activetech_explained":
        "Blizzard & ActiveTech 技术说明（在线无绒薄芯体平台）",
    "Gate0-Gate2_决策清单_ND33vs北京_20261028":
        "ND33 改造 · Gate 0–Gate 2 分期能力清单 v2.1（Capability Staging List）",
    "Gate0_基线口径确认书_20261028":
        "Gate 0 基线口径确认书（ND33-COCOV6-G0-001）",
    "ND33_12项输入清单_20261028":
        "ND33 评估 · 12 项输入清单（认领版·群发短版）",
    "ND33改造评估推进计划_20261028":
        "ND33 改造可行性评估·推进计划（20261028）",
    "决策包模板_ND33_20261113":
        "ND33 改造决策包 · 模板 v1.0（20261113 评审）",
}


def main():
    os.makedirs(BAK, exist_ok=True)
    done = []
    for old, new in RENAMES.items():
        op = os.path.join(SRC, old + ".md")
        np_ = os.path.join(SRC, new + ".md")
        if not os.path.isfile(op):
            print(f"  ! 缺文件 {op}")
            continue
        shutil.copy2(op, os.path.join(BAK, old + ".md"))
        txt = open(op, encoding="utf-8").read()
        # 只改 front matter 的 title 行
        txt = re.sub(r'^title:.*$', f'title: "{new}"', txt, count=1, flags=re.M)
        open(np_, "w", encoding="utf-8").write(txt)
        os.remove(op)
        done.append((old, new))
        print(f"  → {new}")

    # 全库替换 wikilink（只动 [[...]] 形态，禁触 RAW 路径）
    touched = 0
    for dirpath, _dirs, files in os.walk("WIKI"):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            txt = open(fp, encoding="utf-8").read()
            orig = txt
            for old, new in done:
                txt = txt.replace(f"[[{old}]]", f"[[{new}]]")
                txt = txt.replace(f"[[{old}|", f"[[{new}|")
            if txt != orig:
                open(fp, "w", encoding="utf-8").write(txt)
                touched += 1
    # 顶层索引
    for extra in ("index.md", "wikilinks.md"):
        if os.path.isfile(extra):
            txt = open(extra, encoding="utf-8").read()
            orig = txt
            for old, new in done:
                txt = txt.replace(f"[[{old}]]", f"[[{new}]]")
                txt = txt.replace(f"[[{old}|", f"[[{new}|")
            if txt != orig:
                open(extra, "w", encoding="utf-8").write(txt)
                touched += 1

    # 账本 hint 同步
    st = json.load(open(STATE, encoding="utf-8"))
    hint_fix = 0
    for mid, it in st["items"].items():
        h = (it.get("source_page_hint") or "").replace("\\", "/")
        base = os.path.basename(h)[:-3] if h.endswith(".md") else ""
        if base in RENAMES:
            it["source_page_hint"] = f"WIKI/sources/{RENAMES[base]}.md"
            hint_fix += 1
    json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"[rename] 改名 {len(done)} · 受影响文件 {touched} · 账本 hint 修正 {hint_fix}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
