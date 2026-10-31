#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kb_daily_pipeline.py — IMA → Obsidian 知识管道 · 日更编排器（第 4 批 + 第 5 批 --full）

职责（设计依据 .tools/IMA_DAILY_PIPELINE_DESIGN_v2_2026-10-11.md §6.6）：
  把五个阶段串为单入口，支持单阶段跑、断点续跑、容错（进程被 kill 仍保留已有产物）。

阶段编排：
  A 枚举   ima_sync_state.py enumerate   （Agent 侧 MCP 枚举 → --input 合并；脚本无 MCP 则 SKIP）
  B 落地   kb_sync_handler.py plan/apply （Agent 侧 MCP/原件抓取 → --bodies-dir 落盘）
  C 编译   kb_compiler.py plan/apply/stub（Agent 侧语义提炼 → 落 WIKI/sources）
  R 对账   wkb_dedup.py scan + 账本一致性（仅 --full 模式；周度全量校准）  ← 第 5 批新增
  E 收尾   rebuild_index.py + 报告

模式：
  增量模式（默认）  A→B→C→E   每日 18:00 由 bcaf361b 调用
  全量模式 --full   A→B→C→R→E 每周日 09:00 由周度对账自动化调用
                   · R 阶段强制全量：跑 wkb_dedup scan + 账本三口径交叉校验 + 漂移告警
                   · 全量枚举仍需 Agent 侧 MCP（本脚本无 MCP 传输层，如实标 SKIP）

铁律：
  1. 任何阶段失败/前置缺失 → 继续跑后续能跑的，报告中如实标注；绝不假装完成
  2. 幂等：重复跑同一阶段应为 0 变更
  3. RAW/ 只读，绝不写入
  4. 报告落 .tools/kb_pipeline_daily/<date>.md（追加式小结，不覆盖历史批次的 BATCH*.md）
  5. 对账只提示、不自动改 —— 账本与 wkb_dedup 口径不一致时列分歧，交人工裁定

用法：
  python .tools/kb_daily_pipeline.py run                 # A→B→C→E（本会话能做的全做）
  python .tools/kb_daily_pipeline.py run --full          # A→B→C→R→E（周度全量对账）
  python .tools/kb_daily_pipeline.py run --stage B       # 只跑 B
  python .tools/kb_daily_pipeline.py status              # 各阶段积压概览
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".tools"
REPORT_DIR = TOOLS / "kb_pipeline_daily"
CHECKPOINT = TOOLS / "_kb_pipeline_state.json"
RECON_DIR = TOOLS / "kb_pipeline_recon"          # 第 5 批：对账产物目录
STATE = TOOLS / "_ima_sync_state.json"

PY = sys.executable

STAGES = ["A", "B", "C", "E"]          # 增量模式
STAGES_FULL = ["A", "B", "C", "R", "E"]  # 全量对账模式（第 5 批）

# 对账告警阈值（仅提示，不自动改）
RECON_DEV_WARN = 0.05      # 账本条目数 vs RAW 条目数 偏差 > 5% 报警


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def run_py(script, args, timeout=900):
    """跑子脚本，返回 (rc, stdout, stderr)。异常不抛出，交由调用方容错。"""
    cmd = [PY, str(TOOLS / script)] + args
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", timeout=timeout)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except subprocess.TimeoutExpired:
        return -9, "", f"TIMEOUT after {timeout}s"
    except Exception as e:  # noqa: BLE001
        return -1, "", f"{type(e).__name__}: {e}"


def load_cp():
    if CHECKPOINT.exists():
        return json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    return {"runs": []}


def save_cp(cp):
    cp["updated"] = now_iso()
    CHECKPOINT.write_text(json.dumps(cp, ensure_ascii=False, indent=1), encoding="utf-8")


# --------------------------------------------------------- stages

def stage_A(state):
    """枚举：脚本只有 enumerate（需 Agent 侧 MCP 输入）；无输入则报告 SKIP。"""
    rc, out, err = run_py("ima_sync_state.py", ["status"])
    info = {"rc": rc, "stdout": out, "stderr": err,
            "note": "MCP 枚举需 Agent 会话执行后经 enumerate --input 合并"}
    return "SKIP" if rc != 0 else "OK", info


def archive_staging(d):
    """落盘后把暂存目录归档到 _done/<date>/，避免下次误报 already-done。"""
    if not d.exists():
        return 0
    files = list(d.glob("*.md")) + list(d.glob("*.json"))
    if not files:
        return 0
    dest = d.parent / "_done" / today()
    dest.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in files:
        os.replace(str(f), str(dest / f.name))
        n += 1
    return n


def stage_B(state):
    """落地：plan（脚本可做）→ apply（需 Agent MCP 抓取，暂存目录驱动）。"""
    steps = {}
    rc, out, err = run_py("kb_sync_handler.py", ["plan"])
    steps["plan"] = {"rc": rc, "out": out, "err": err}
    bodies = TOOLS / "_kb_sync_bodies"
    if rc == 0 and bodies.exists() and list(bodies.glob("*.md")):
        rc2, out2, err2 = run_py("kb_sync_handler.py",
                                 ["apply", "--bodies-dir", str(bodies)])
        steps["apply"] = {"rc": rc2, "out": out2, "err": err2}
        steps["archive"] = {"rc": 0, "out": f"归档 {archive_staging(bodies)} 个暂存文件"}
        status = "OK" if rc2 == 0 else "FAIL"
    else:
        steps["apply"] = {"skipped": True,
                          "reason": "无 Agent 抓取暂存（_kb_sync_bodies 为空）"}
        status = "PARTIAL"
    return status, steps


def stage_C(state):
    """编译：plan → apply（暂存页面驱动）→ stub。"""
    steps = {}
    rc, out, err = run_py("kb_compiler.py", ["plan"])
    steps["plan"] = {"rc": rc, "out": out, "err": err}
    pages = TOOLS / "_kb_compile_pages"
    wrote = False
    if rc == 0 and pages.exists() and list(pages.glob("*.md")):
        rc2, out2, err2 = run_py("kb_compiler.py", ["apply"])
        steps["apply"] = {"rc": rc2, "out": out2, "err": err2}
        steps["archive"] = {"rc": 0, "out": f"归档 {archive_staging(pages)} 个暂存页面"}
        wrote = rc2 == 0
    else:
        steps["apply"] = {"skipped": True, "reason": "无 Agent 编译暂存"}
    if wrote:
        rc3, out3, err3 = run_py("kb_compiler.py", ["verify"], timeout=600)
        steps["verify"] = {"rc": rc3, "out": out3, "err": err3}
    return ("OK" if wrote else "PARTIAL"), steps


def stage_E(state):
    """收尾：重建 index.md + 记忆防覆盖巡检。"""
    steps = {}
    rc, out, err = run_py("rebuild_index.py", [], timeout=600)
    steps["rebuild_index"] = {"rc": rc, "out": out, "err": err}
    mg = TOOLS / "memory_guard.py"
    if mg.exists():
        rc2, out2, err2 = run_py("memory_guard.py", ["check"], timeout=300)
        steps["memory_guard"] = {"rc": rc2, "out": out2, "err": err2}
    return ("OK" if rc == 0 else "FAIL"), steps


STAGE_FN = {"A": stage_A, "B": stage_B, "C": stage_C, "E": stage_E}


# --------------------------------------------------- 阶段 R：全量对账（第 5 批）

def _recon_ledger():
    """读账本，返回 (total, {stage: n}, kv_n, raw_registered_n)。"""
    if not STATE.exists():
        return None
    s = json.loads(STATE.read_text(encoding="utf-8"))
    items = s.get("items", {})
    from collections import Counter
    c = Counter(it.get("stage") for it in items.values())
    kv_n = sum(1 for it in items.values() if it.get("kb_path"))
    return len(items), dict(c), kv_n


def _recon_raw_vs_ledger():
    """逐条比对 RAW/ 实体文件与账本 raw_path，报出双边差集。

    这是全量对账的核心价值：抓出「IMA 新增但账本未枚举」与
    「账本登记但 RAW 已删」两类漂移。日更增量靠剪枝发现不了漏枚举。
    """
    if not STATE.exists():
        return None
    s = json.loads(STATE.read_text(encoding="utf-8"))
    ledger = {it["raw_path"].replace("\\", "/")
              for it in s.get("items", {}).values() if it.get("raw_path")}
    raw = set()
    for r, d, fs in os.walk(ROOT / "RAW"):
        if "attachments" in r or ".obsidian" in r:
            continue
        for f in fs:
            if f.endswith(".md"):
                raw.add(os.path.relpath(os.path.join(r, f), ROOT).replace("\\", "/"))

    # 多登细分（2026-10-18 增）：区分「RAW 从未落地」与「RAW 真被删」
    #   成因：IMA 插件未落盘的新条目，Agent 侧按预期路径登记 raw_path 并写 RAW_FULL 镜像
    #   → RAW 侧无文件、RAW_FULL 侧有镜像。这不是删除，是锚点未落地，须插件补齐。
    only_led = sorted(ledger - raw)
    no_anchor, deleted = [], []
    for p in only_led:
        mirror = (ROOT / p.replace("RAW/", "RAW_FULL/", 1))
        (no_anchor if mirror.exists() else deleted).append(p)

    return {
        "ledger_count": len(ledger),
        "raw_count": len(raw),
        "only_in_raw": sorted(raw - ledger),
        "only_in_ledger": only_led,
        "only_in_ledger_no_anchor": no_anchor,   # RAW 未落地但有 RAW_FULL 镜像
        "only_in_ledger_deleted": deleted,       # RAW 与 RAW_FULL 双缺，疑似真删
    }


def _recon_dedup():
    """跑 wkb_dedup.py scan，解析已编译/未编译/RAW 条目数 + 重复登记数。"""
    rc, out, err = run_py("wkb_dedup.py", ["scan"], timeout=600)
    if rc != 0:
        return {"rc": rc, "err": err, "out": out}
    import re as _re
    def grab(pat, default=None):
        m = _re.search(pat, out)
        return int(m.group(1)) if m else default
    return {
        "rc": rc,
        "compiled": grab(r"已编译\s*:\s*(\d+)"),
        "uncompiled": grab(r"真实未编译:\s*(\d+)"),
        "raw_entries": grab(r"RAW 条目数.*?:\s*(\d+)"),
        "dup_live": grab(r"活跃.*?登记.*?:\s*(\d+)"),
        "merged_pages": grab(r"merged 指针页\s*:\s*(\d+)"),
        "raw": out,
    }


def stage_R(state):
    """全量对账（仅 --full）：wkb_dedup scan + 账本三口径交叉校验 + 漂移告警。

    设计铁律：
      · 本阶段**只读不改** —— 只产出对账报告与分歧清单，绝不自动改写账本或 WIKI
      · 账本 compiled 与 wkb_dedup compiled 口径本就不同（账本按 media_id 一对一；
        dedup 按 source 页计，含 merged 指针页/跨条目合并页）→ 只报偏差，不判错
      · 对账产物流水写入 .tools/kb_pipeline_recon/<date>.json 供复查
    """
    steps = {}
    ledger = _recon_ledger()
    dedup = _recon_dedup()

    if ledger is None:
        return "FAIL", {"error": "账本不存在，无法对账"}
    if dedup.get("rc") != 0:
        return "FAIL", {"dedup": {"rc": dedup.get("rc"), "err": dedup.get("err", "")[:300]}}

    total, stages, kv_n = ledger
    raw_n = dedup.get("raw_entries")
    compiled_dedup = dedup.get("compiled")
    uncompiled = dedup.get("uncompiled")

    # ---- 一致性校验（只提示） ----
    drift = []
    if raw_n:
        dev = abs(total - raw_n) / raw_n
        if dev > RECON_DEV_WARN:
            drift.append(f"账本条目 {total} vs RAW 条目 {raw_n}，偏差 {dev*100:.1f}% > "
                         f"{RECON_DEV_WARN*100:.0f}%")
    # 账本 compiled vs dedup compiled：口径不同，偏差仅记录
    ledger_compiled = stages.get("compiled", 0)
    if compiled_dedup is not None:
        gap = compiled_dedup - ledger_compiled
        steps["口径对比"] = {
            "rc": 0,
            "out": (f"账本 compiled={ledger_compiled} · wkb_dedup compiled={compiled_dedup} · "
                    f"差 {gap:+d}（口径不同：dedup 计 merged 指针页/跨条目合并页，属预期）"),
        }
    if uncompiled is not None:
        steps["未编译"] = {"rc": 0, "out": f"wkb_dedup 真实未编译 {uncompiled} 条"}

    # ---- 逐条黑账核对：RAW 实体 vs 账本登记 ----
    cmp = _recon_raw_vs_ledger()
    if cmp:
        only_raw = cmp["only_in_raw"]
        only_led = cmp["only_in_ledger"]
        steps["黑账核对"] = {
            "rc": 0,
            "out": (f"RAW {cmp['raw_count']} vs 账本 {cmp['ledger_count']} · "
                    f"账本漏登 {len(only_raw)} · 账本多登 {len(only_led)}"
                    f"（其中 RAW 锚点未落地 {len(cmp.get('only_in_ledger_no_anchor') or [])}、"
                    f"疑似真删除 {len(cmp.get('only_in_ledger_deleted') or [])}）"),
        }
        if only_raw:
            drift.append(f"账本漏登 {len(only_raw)} 条（IMA 新增未枚举，日更期间产生）")
            for p in only_raw[:5]:
                steps.setdefault("漏登明细", {"rc": 0, "out": ""})
                steps["漏登明细"]["out"] += (" / " if steps["漏登明细"]["out"] else "") + p.split("/WKB/")[-1]
        if only_led:
            na = cmp.get("only_in_ledger_no_anchor") or []
            dl = cmp.get("only_in_ledger_deleted") or []
            if na:
                drift.append(f"RAW 锚点未落地 {len(na)} 条（账本已登记 raw_path、"
                             f"RAW_FULL 有镜像、RAW 侧无文件 → 须等 IMA 插件补齐，"
                             f"非删除，不自动清账本）")
            if dl:
                drift.append(f"账本多登 {len(dl)} 条（RAW 与 RAW_FULL 双缺，疑似已删，"
                             f"交人工裁定）")

    if dedup.get("dup_live"):
        drift.append(f"一条 RAW 被多个活跃页登记（疑似重复编译）：{dedup['dup_live']} 条")

    steps["wkb_dedup_scan"] = {
        "rc": 0,
        "out": (f"已编译 {compiled_dedup} / 未编译 {uncompiled} / RAW 条目 {raw_n} / "
                f"merged 指针页 {dedup.get('merged_pages')}"),
    }
    steps["账本"] = {
        "rc": 0,
        "out": (f"总 {total} · " + " ".join(f"{k}={v}" for k, v in sorted(stages.items())) +
                f" · 有 kb_path {kv_n}"),
    }
    if drift:
        steps["漂移告警"] = {"rc": 0, "out": " ⚠ " + " ; ".join(drift)}
    else:
        steps["漂移告警"] = {"rc": 0, "out": "无（偏差在容忍范围内）"}

    # ---- 落盘对账产物 ----
    RECON_DIR.mkdir(parents=True, exist_ok=True)
    recon = {
        "at": now_iso(),
        "ledger": {"total": total, "stages": stages, "with_kb_path": kv_n},
        "dedup": {k: v for k, v in dedup.items() if k != "raw"},
        "ledger_vs_raw": cmp,
        "drift": drift,
    }
    (RECON_DIR / f"{today()}_recon.json").write_text(
        json.dumps(recon, ensure_ascii=False, indent=2), encoding="utf-8")

    return ("OK" if not drift else "WARN"), steps


STAGE_FN_FULL = {"A": stage_A, "B": stage_B, "C": stage_C, "R": stage_R, "E": stage_E}
STAGE_FN.update(STAGE_FN_FULL)
ALL_STAGE_KEYS = ["A", "B", "C", "R", "E"]


# --------------------------------------------------------- report

def write_report(results, cp, stages, mode):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = "_full" if mode == "full" else "_pipeline"
    p = REPORT_DIR / f"{today()}{suffix}.md"
    title = "全量对账" if mode == "full" else "日更"
    L = [f"# WKB-OB 知识管道{title} — {today()}", "",
         f"_生成于 {now_iso()} · 编排器 kb_daily_pipeline.py（模式 {mode}）_", ""]
    for st in stages:
        r = results.get(st)
        if not r:
            continue
        status, info = r
        L.append(f"## 阶段 {st}：{status}")
        if st == "A":
            L.append(f"- {info.get('stdout','')[:600]}")
            L.append(f"- 备注：{info.get('note','')}")
        else:
            for k, v in info.items():
                if v.get("skipped"):
                    L.append(f"- **{k}**：跳过（{v.get('reason')}）")
                else:
                    o = (v.get("out") or "").replace("\n", " / ")[:400]
                    L.append(f"- **{k}**：rc={v.get('rc')}  {o}")
        L.append("")
    L.append("## 结论")
    L.append("- 各阶段状态见上；PARTIAL 表示脚本侧已完成、Agent 侧抓取/提炼待会话执行。")
    if mode == "full":
        L.append("- 阶段 R 只读不改：对账仅列分歧与漂移，**不自动改写**账本或 WIKI。")
        L.append(f"- 对账产物：`.tools/kb_pipeline_recon/{today()}_recon.json`")
    L.append(f"- 检查点：`{CHECKPOINT.relative_to(ROOT)}`")
    p.write_text("\n".join(L), encoding="utf-8")
    return p


# --------------------------------------------------------- main

def cmd_run(args):
    mode = "full" if args.full else "incr"
    stages = [args.stage] if args.stage else (STAGES_FULL if args.full else STAGES)
    cp = load_cp()
    results = {}
    print("=" * 64)
    print(f"日更编排 {today()} · 模式 {mode} · 阶段 {','.join(stages)}")
    print("=" * 64)
    for st in stages:
        fn = STAGE_FN.get(st)
        if not fn:
            print(f"[{st}] 未知阶段，跳过")
            continue
        print(f"\n>>> 阶段 {st} ...")
        try:
            status, info = fn(cp)
        except Exception as e:  # noqa: BLE001
            status, info = "FAIL", {"error": f"{type(e).__name__}: {e}"}
        print(f"[{st}] -> {status}")
        results[st] = (status, info)
        cp["runs"].append({"at": now_iso(), "stage": st, "status": status, "mode": mode})
    save_cp(cp)
    rp = write_report(results, cp, stages, mode)
    print(f"\n报告已写：{rp.relative_to(ROOT)}")
    return 0


def cmd_status(args):
    print("=" * 64)
    print("日更管道状态")
    print("=" * 64)
    rc, out, _ = run_py("ima_sync_state.py", ["status"])
    print("\n[账本]\n" + out)
    for name, sub in (("阶段B", ["status"]), ("阶段C", ["status"])):
        rc, out, _ = run_py(f"kb_{'sync_handler' if name=='阶段B' else 'compiler'}.py", sub)
        print(f"\n[{name}]\n" + out)
    # 最近一次全量对账
    if RECON_DIR.exists():
        recons = sorted(RECON_DIR.glob("*_recon.json"))
        if recons:
            last = json.loads(recons[-1].read_text(encoding="utf-8"))
            print("\n[最近对账] " + recons[-1].name)
            print("  " + json.dumps(last.get("ledger", {}), ensure_ascii=False))
            print("  drift: " + ("无" if not last.get("drift") else "; ".join(last["drift"])))
    return 0


def main():
    ap = argparse.ArgumentParser(description="WKB-OB 日更编排器")
    sub = ap.add_subparsers(dest="cmd")
    p_run = sub.add_parser("run")
    p_run.add_argument("--stage", choices=ALL_STAGE_KEYS)
    p_run.add_argument("--full", action="store_true",
                       help="全量对账模式（A→B→C→R→E），周度校准用")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "run":
        return cmd_run(a)
    if a.cmd == "status":
        return cmd_status(a)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
