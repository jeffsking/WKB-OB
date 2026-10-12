#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ima_sync_state.py — IMA → Obsidian 知识管道 · 同步层账本与枚举器（第 1 批）

职责：
  init       从本地 RAW/ + WIKI source 页反推，建初始账本（media_id ↔ 路径）
  enumerate  MCP 递归枚举 IMA + file_number 剪枝 + 移动检测 → 更新账本
  status     一行摘要

设计依据：.tools/IMA_DAILY_PIPELINE_DESIGN_v2_2026-10-11.md §3 / §4

铁律（不可破）：
  - RAW/ 只读，绝不写入
  - 账本只是同步层状态；「是否已编译」一律以 wkb_dedup.py scan 为准
  - source_page_hint 非权威，仅缓存线索（§3.6.1）
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".tools"
STATE = TOOLS / "_ima_sync_state.json"
RAW = ROOT / "RAW"
WIKI_SOURCES = ROOT / "WIKI" / "sources"

KB_ID_MCP = "001a693ee6c0644e"
KB_ID_REST = "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="

MIRROR_PREFIX = "ima_sync/个人知识库/WKB/"
AUDIO_ORIGINAL_MAX_MB = 50  # §5.1


# ---------------------------------------------------------------- 工具函数

def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


# 账本 kb_path 的统一口径：一律带镜像前缀（与 init 从本地反推的口径一致）
# 坑：Agent 侧 MCP 枚举常给「文件夹链+文件名」的相对名，若直接与账本比对
#     会把 18 条全部误报为「移动」并污染 moves 历史。必须归一（2026-10-11 实测）。
_CONTAINER = "个人知识库/WKB/"


def norm_kb_path(p: str) -> str:
    """把任意口径的 kb_path 归一为 `ima_sync/个人知识库/WKB/...`（不带 RAW/ 前缀）。"""
    if not p:
        return p
    p = p.replace("\\", "/").strip().lstrip("/")
    if p.startswith("RAW/"):
        p = p[4:]
    if p.startswith("ima_sync/"):
        return p
    return MIRROR_PREFIX + p


def parse_fm_media_id(path: Path):
    """从 front matter 读 media_id。"""
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:1500]
    except Exception:
        return None
    m = re.search(r'^media_id:[ \t]*["\']?([^"\'\n\r]+)', head, re.M)
    return m.group(1).strip() if m else None


def parse_fm_field(path: Path, field: str):
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:2000]
    except Exception:
        return None
    m = re.search(rf'^{field}:[ \t]*(.+)$', head, re.M)
    if not m:
        return None
    # 剥离 YAML 引号（坑：extract_status: "ok" 会带引号 → 与 'ok' 比对恒失败）
    return m.group(1).strip().strip('"').strip("'")


# ---------------------------------------------------------------- init

def cmd_init(args):
    """从本地反推建账本。"""
    if STATE.exists() and not args.force:
        print(f"[!] 账本已存在：{rel(STATE)}")
        print("    如需重建请加 --force（会备份旧账本）")
        return 1

    if STATE.exists():
        bak = STATE.with_suffix(f".bak-{datetime.now():%Y%m%d%H%M%S}.json")
        STATE.rename(bak)
        print(f"[备份] 旧账本 → {rel(bak)}")

    print("[init] 扫描本地 RAW/ima_sync ...")
    items = {}
    missing_mid = 0
    scanned = 0

    for f in RAW.rglob("*.md"):
        scanned += 1
        mid = parse_fm_media_id(f)
        if not mid:
            missing_mid += 1
            continue
        try:
            kb_path = str(f.relative_to(RAW)).replace("\\", "/")
        except ValueError:
            continue
        items[mid] = {
            "title": parse_fm_field(f, "title") or f.stem,
            "media_type": None,
            "kb_path": kb_path,
            "create_ts": None,
            "first_seen": today(),
            "last_seen": today(),
            "stage": "discovered",
            "raw_path": rel(f),
            "full_path": None,
            "source_page_hint": None,
            "moves": [],
        }

    # RAW_FULL 侧有正文的标 synced
    raw_full = ROOT / "RAW_FULL"
    synced = 0
    if raw_full.exists():
        for f in raw_full.rglob("*.md"):
            mid = parse_fm_media_id(f)
            if mid and mid in items:
                st = parse_fm_field(f, "extract_status")
                if st in ("ok", "empty", "original-only"):
                    items[mid]["stage"] = "synced"
                    items[mid]["full_path"] = rel(f)
                    synced += 1

    # WIKI source 页反查 source_page_hint（非权威，仅线索）
    hinted = 0
    if WIKI_SOURCES.exists():
        # 先建 RAW 路径 → media_id 反查表
        path2mid = {}
        for mid, it in items.items():
            if it.get("raw_path"):
                path2mid[it["raw_path"]] = mid
        for f in WIKI_SOURCES.glob("*.md"):
            sp = parse_fm_field(f, "source_path")
            if not sp:
                continue
            sp = sp.strip('"\'')
            if sp in path2mid:
                mid = path2mid[sp]
                items[mid]["source_page_hint"] = rel(f)
                if items[mid]["stage"] == "synced":
                    items[mid]["stage"] = "compiled"
                hinted += 1

    state = {
        "version": 2,
        "kb_id_mcp": KB_ID_MCP,
        "last_full_scan": now_iso(),
        "last_enumerate": None,
        "_warning": (
            "source_page_hint 仅为加速排查的缓存线索，非权威。"
            "判定『是否已编译』一律以 wkb_dedup.py scan 为准（见设计 §3.6.1）。"
        ),
        "folders": {},
        "items": items,
    }
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[init] 扫描 .md 文件 {scanned} 个（无 media_id {missing_mid}）")
    print(f"[init] 账本条目 {len(items)} · synced {synced} · compiled {hinted}")
    print(f"[init] 已写入 {rel(STATE)}")

    # 交叉验证
    print()
    print("[交叉验证] 调用 wkb_dedup.py scan ...")
    return crosscheck(len(items))


def crosscheck(ledger_count):
    """跑 wkb_dedup.py scan，与账本条目数比对。"""
    dedup = TOOLS / "wkb_dedup.py"
    if not dedup.exists():
        print("[!] 未找到 wkb_dedup.py，跳过交叉验证")
        return 0
    try:
        r = subprocess.run(
            [sys.executable, str(dedup), "scan"],
            capture_output=True, text=True, encoding="utf-8", timeout=300,
        )
    except Exception as e:
        print(f"[!] wkb_dedup.py 执行失败：{e}")
        return 0

    out = r.stdout or ""
    m_compiled = re.search(r"已编译\s*:\s*(\d+)", out)
    m_raw = re.search(r"RAW 条目数.*?:\s*(\d+)", out)
    compiled = int(m_compiled.group(1)) if m_compiled else None
    raw_n = int(m_raw.group(1)) if m_raw else None

    print(f"    wkb_dedup: 已编译 {compiled} / RAW 条目 {raw_n}")
    print(f"    账本条目: {ledger_count}")
    print("    注：两者『compiled』口径不同——wkb_dedup 按 source 页计（含 merged 指针页、"
          "跨条目合并页），账本按 media_id↔source_path 一对一计。条目数对齐即为通过。")

    if raw_n and ledger_count:
        dev = abs(ledger_count - raw_n) / raw_n
        if dev > 0.05:
            print(f"    ⚠ 偏差 {dev*100:.1f}% > 5%，需排查后继续")
            return 2
        print(f"    ✓ 偏差 {dev*100:.2f}% 在容忍范围内")
    return 0


# ---------------------------------------------------------------- enumerate

def mcp_call_direct(tool, params):
    """直接提示：MCP 调用需在本 Agent 会话内完成，脚本只负责账本合并。"""
    raise NotImplementedError


def cmd_enumerate(args):
    """
    枚举由 Agent 侧执行 MCP 调用，结果喂给本命令的 --input 合并进账本。
    这样避免在脚本里硬编码 MCP 传输层。
    """
    if not STATE.exists():
        print("[!] 账本不存在，请先跑 init")
        return 1
    if not args.input:
        print("[!] 需 --input <enumerated.json>（由 Agent 调 MCP 枚举后落盘）")
        print()
        print("Agent 侧枚举契约（写入 input.json）：")
        print(json.dumps({
            "root": [{"media_id": "...", "media_type": 99, "title": "Areas",
                       "create_time": "...", "folder_info": {"folder_id": "...",
                       "file_number": "16", "folder_number": "8", "parent_folder_id": ""}}],
            "items": [{"media_id": "...", "media_type": 11, "title": "...",
                        "create_time": "...", "kb_path": "Areas/Meeting Minutes/x.md",
                        "parent_folder_id": "folder_..."}],
        }, ensure_ascii=False, indent=2))
        return 1

    state = json.loads(STATE.read_text(encoding="utf-8"))
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    items = state.setdefault("items", {})
    folders = state.setdefault("folders", {})

    new_items, moved, known = [], [], 0

    for entry in data.get("items", []):
        mid = entry.get("media_id")
        if not mid:
            continue
        kb_path = norm_kb_path(entry.get("kb_path") or "")
        if mid in items:
            known += 1
            old = items[mid].get("kb_path")
            if kb_path and old and kb_path != old:
                # 仅在「相对容器的路径」真变化时才算移动（防标题标点差异误报）
                def _tail(x):
                    return x.split(_CONTAINER, 1)[-1] if _CONTAINER in x else x
                if _tail(kb_path) != _tail(old):
                    items[mid].setdefault("moves", []).append(
                        {"from": old, "to": kb_path, "date": today()})
                    items[mid]["kb_path"] = kb_path
                    moved.append((mid, old, kb_path))
            items[mid]["last_seen"] = today()
        else:
            items[mid] = {
                "title": entry.get("title", ""),
                "media_type": entry.get("media_type"),
                "kb_path": kb_path,
                "create_ts": int(entry["create_time"]) if entry.get("create_time") else None,
                "first_seen": today(),
                "last_seen": today(),
                "stage": "discovered",
                "raw_path": None,
                "full_path": None,
                "source_page_hint": None,
                "moves": [],
            }
            new_items.append(mid)

    for fo in data.get("root", []) + data.get("folders", []):
        fid = fo.get("folder_id") or fo.get("media_id")
        fi = fo.get("folder_info") or {}
        if fid:
            folders[fid] = {
                "path": fo.get("title") or fi.get("name"),
                "file_number": int(fi.get("file_number") or 0),
                "folder_number": int(fi.get("folder_number") or 0),
                "last_checked": today(),
                "pruned": False,
            }

    state["last_enumerate"] = now_iso()
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[enumerate] 新增 {len(new_items)} · 移动 {len(moved)} · 已知 {known}")
    for mid, a, b in moved[:10]:
        print(f"    moved: {a} → {b}")
    print(f"[enumerate] 账本现 {len(items)} 条")
    return 0


# ---------------------------------------------------------------- status

def cmd_status(args):
    if not STATE.exists():
        print("[!] 账本不存在")
        return 1
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})
    from collections import Counter
    c = Counter(it.get("stage") for it in items.values())
    print(f"账本 {rel(STATE)}")
    print(f"  init 时间      : {s.get('last_full_scan')}")
    print(f"  上次枚举       : {s.get('last_enumerate')}")
    print(f"  条目总数       : {len(items)}")
    for k, v in sorted(c.items(), key=lambda x: -x[1]):
        print(f"    {k:15}: {v}")
    print(f"  文件夹记录     : {len(s.get('folders', {}))}")
    print(f"  有 source hint : {sum(1 for i in items.values() if i.get('source_page_hint'))}")
    return 0


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="IMA 同步层账本与枚举器")
    sub = ap.add_subparsers(dest="cmd")

    p_init = sub.add_parser("init", help="从本地反推建初始账本")
    p_init.add_argument("--force", action="store_true", help="重建（备份旧账本）")

    p_enum = sub.add_parser("enumerate", help="合并 MCP 枚举结果进账本")
    p_enum.add_argument("--input", help="Agent 侧枚举落盘的 JSON")

    sub.add_parser("status", help="一行摘要")

    args = ap.parse_args()
    if args.cmd == "init":
        return cmd_init(args)
    if args.cmd == "enumerate":
        return cmd_enumerate(args)
    if args.cmd == "status":
        return cmd_status(args)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
