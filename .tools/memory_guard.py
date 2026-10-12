#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
memory_guard.py — 记忆/日志防静默覆盖巡检（只读）

背景：2026-10-11 实测发生两次记录被 `>` 覆盖（memory/2026-10-11.md 17:41 丢失追加一~六）。
本工具每日比对记录的"体量基线"，一旦发现当天文件异常缩短（疑似被覆盖）即报警。

设计原则：
- 只读，绝不修改任何被守护文件
- 基线存 .tools/_memory_baseline.json，首次运行自动建立
- 报警条件：文件行数/字节数较上次记录"显著下降"（默认跌幅 > 20% 或行数减少 >= 5 行）
- 追加式文件的健康signature = 行数只增不减

用法：
  python .tools/memory_guard.py check          # 巡检并报告（默认）
  python .tools/memory_guard.py check --quiet  # 无异常时静默
  python .tools/memory_guard.py baseline       # 强制刷新基线（人工确认记录已恢复后使用）
"""

import json
import os
import sys
import hashlib
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / ".tools" / "_memory_baseline.json"
MEMDIR = ROOT / ".workbuddy" / "memory"

# 被守护的文件/目录（追加式，行数只应增长）
GUARDED_FILES = [
    ROOT / "log.md",
    ROOT / "index.md",
    ROOT / "AGENTS.md",
]
GUARDED_DIRS = [MEMDIR]

# 报警阈值
SHRINK_PCT = 0.20   # 体量下降超过 20% 报警
SHRINK_LINES = 5    # 或行数减少 >= 5 行报警


def snapshot():
    """采集当前所有被守护文件的体量指纹。"""
    snap = {}
    files = list(GUARDED_FILES)
    for d in GUARDED_DIRS:
        if d.exists():
            files.extend(sorted(d.rglob("*.md")))
    for f in files:
        if not f.exists():
            continue
        try:
            data = f.read_bytes()
            text = data.decode("utf-8", errors="ignore")
            lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
            snap[str(f.relative_to(ROOT)).replace("\\", "/")] = {
                "bytes": len(data),
                "lines": lines,
                "sha1": hashlib.sha1(data).hexdigest()[:12],
            }
        except Exception as e:
            snap[str(f.relative_to(ROOT)).replace("\\", "/")] = {"error": str(e)}
    return snap


def load_baseline():
    if BASELINE.exists():
        try:
            return json.loads(BASELINE.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None


def save_baseline(snap):
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    payload = {"updated": datetime.now().isoformat(timespec="seconds"), "files": snap}
    BASELINE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def check(quiet=False):
    cur = load_baseline()
    now = snapshot()
    if cur is None:
        save_baseline(now)
        print(f"[首个基线已建立] 守护 {len(now)} 个文件 → {BASELINE.relative_to(ROOT)}")
        return 0

    prev = cur.get("files", {})
    alerts, news, grows = [], [], 0

    for path, info in now.items():
        if "error" in info:
            alerts.append(f"  ✗ {path} — 读取失败: {info['error']}")
            continue
        p = prev.get(path)
        if p is None:
            news.append(f"  + {path} (新增 {info['lines']} 行)")
            continue
        if info["lines"] > p["lines"]:
            grows += 1
        # 覆盖检测
        down_lines = p["lines"] - info["lines"]
        if p["lines"] > 0:
            down_pct = (p["bytes"] - info["bytes"]) / p["bytes"] if p["bytes"] else 0
        else:
            down_pct = 0
        if down_lines >= SHRINK_LINES or down_pct > SHRINK_PCT:
            alerts.append(
                f"  ⚠ {path}\n"
                f"      上次: {p['lines']} 行 / {p['bytes']} B (sha1 {p['sha1']})\n"
                f"      现在: {info['lines']} 行 / {info['bytes']} B (sha1 {info['sha1']})\n"
                f"      变化: 行数 -{down_lines} ({-down_pct*100:+.1f}%)  ← 疑似被覆盖/截断"
            )

    # 文件整体消失
    for path in prev:
        if path not in now:
            alerts.append(f"  ⚠ {path} — 文件已消失（上次 {prev[path]['lines']} 行）")

    if alerts:
        print("=" * 60)
        print(f"记忆覆盖告警 · {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("=" * 60)
        for a in alerts:
            print(a)
        print()
        print(f"提示：确认非误报后跑 `python .tools/memory_guard.py baseline` 刷新基线。")
        if news and not quiet:
            print()
            print(f"同期新增 {len(news)} 个文件，增长 {grows} 个（正常）：")
            for n in news[:20]:
                print(n)
        return 2

    if not quiet:
        print(f"[OK] 记忆巡检通过 · {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"     守护 {len(now)} 个文件 · 增长 {grows} · 新增 {len(news)} · 无覆盖迹象")
    save_baseline(now)
    return 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    quiet = "--quiet" in sys.argv
    if cmd == "baseline":
        save_baseline(snapshot())
        print(f"[基线已刷新] {BASELINE.relative_to(ROOT)}")
        return 0
    elif cmd == "check":
        return check(quiet=quiet)
    else:
        print(__doc__)
        return 1


if __name__ == "__main__":
    sys.exit(main())
