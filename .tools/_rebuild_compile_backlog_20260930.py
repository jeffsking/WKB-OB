# -*- coding: utf-8 -*-
"""重建编译积压账目（2026-09-30 Reconciliation 第一步 #2）。

背景：旧 `_compile_backlog.json`（1037 条）双轨锚 + 25% 已编译未出队，
876 done + 1037 backlog > 1718 raw md，账目失真。

本脚本以「RAW md 文件 ↔ WIKI source 页 source_path」双向对账重算真实积压：
  compiled : RAW 侧有文件 且 有源摘要页（source_path 指向它）
  stale    : 有源摘要页 但 RAW 侧无对应文件（锚失效，需人工核对）
  backlog  : RAW 侧有文件 但 无源摘要页（真实待编译）
  excluded : 已登记的无正文/空正文/跳过件（不计入 backlog）

输出：
  .tools/_compile_backlog.json          # 真实待编译清单（RAW/ 路径，排序）
  .tools/_compile_reconcile_20260930.json  # 对账全量明细

用法：python .tools/_rebuild_compile_backlog_20260930.py [--apply]
  默认 dry-run 只报告；--apply 写盘。
"""
import glob
import json
import os
import re
import sys

VAULT = r'E:\WKB-OB'


def norm(p):
    return p.replace('\\', '/').replace('RAW_FULL/', 'RAW/', 1) \
        if p.replace('\\', '/').startswith(('RAW_FULL/', 'raw/')) else p.replace('\\', '/')


def net_len(path):
    try:
        t = open(path, encoding='utf-8', errors='ignore').read()
    except Exception:
        return 0
    t = re.sub(r'^---\r?\n[\s\S]*?\r?\n---\r?\n', '', t)
    t = re.sub(r'^\s*#.*$', '', t, flags=re.M)
    return len(t.strip())


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)

    # 1. RAW 侧 md 全集（统一正斜杠口径）
    raw_files = sorted(p.replace('\\', '/') for p in glob.glob('RAW/**/*.md', recursive=True))
    raw_set = set(raw_files)
    print('RAW md 全集: %d' % len(raw_files))

    # 2. WIKI source 页锚集合
    anchor_owners = {}
    for f in glob.glob('WIKI/sources/*.md'):
        t = open(f, encoding='utf-8', errors='ignore').read(4000)
        m = re.search(r'^source_path:\s*(.+)$', t, re.M)
        if m:
            p = norm(m.group(1).strip().strip('"'))
            anchor_owners.setdefault(p, []).append(os.path.basename(f))
    print('源摘要页锚集合: %d 个唯一路径' % len(anchor_owners))

    # 3. 三向对账
    compiled = sorted(raw_set & set(anchor_owners))
    stale = sorted(p for p in anchor_owners if p not in raw_set)
    backlog = sorted(raw_set - set(anchor_owners))
    print('compiled（已编译）: %d' % len(compiled))
    print('stale（锚失效，页在文件不在）: %d' % len(stale))
    print('backlog（真实待编译）: %d' % len(backlog))

    # 4. 排除项（无正文/空正文登记件）
    excluded = set()
    for name in ('_extract_no_content.json', '_extract_source_empty.json'):
        fp = os.path.join('.tools', name)
        if os.path.exists(fp):
            d = json.load(open(fp, encoding='utf-8'))
            for x in d:
                s = x if isinstance(x, str) else (x.get('path') or x.get('src') or x.get('dst') or '')
                s = norm(s)
                if s:
                    excluded.add(s)
    # 排除件中确在 backlog 的（登记与盘存口径可能不同），从 backlog 摘出单独归类
    excl_hit = sorted(p for p in backlog if p in excluded
                      or os.path.basename(p) in {os.path.basename(x) for x in excluded})
    true_backlog = sorted(set(backlog) - set(excl_hit))
    print('排除件命中 backlog: %d（无正文/空正文登记）' % len(excl_hit))
    print('真实待编译（净）: %d' % len(true_backlog))

    # backlog 净正文体检（空壳件拦截，阈值沿用 build_ledger 的 50 字符）
    shells = [p for p in true_backlog if os.path.getsize(p) > 0 and net_len(p) < 50]
    print('其中空壳件（净正文<50 字符，建议不派发）: %d' % len(shells))

    # 5. 写盘
    detail = {
        'generated': '2026-09-30',
        'basis': 'RAW md 全集 1718 ↔ WIKI sources source_path（统一锚后）',
        'counts': {'raw_md': len(raw_files), 'compiled': len(compiled),
                   'stale_anchors': len(stale), 'backlog_gross': len(backlog),
                   'excluded_no_text': len(excl_hit), 'backlog_net': len(true_backlog),
                   'backlog_shells': len(shells)},
        'stale_anchors': {p: anchor_owners[p] for p in stale},
        'excluded_no_text': excl_hit,
        'backlog_shells': shells,
    }
    if apply:
        json.dump(true_backlog, open('.tools/_compile_backlog.json', 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        json.dump(detail, open('.tools/_compile_reconcile_20260930.json', 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        print('\n已写盘：.tools/_compile_backlog.json（%d 条）+ _compile_reconcile_20260930.json'
              % len(true_backlog))
    else:
        print('\n[dry-run] 加 --apply 写盘。')
        print('stale 锚样例:')
        for p in stale[:8]:
            print('  ', p[:80], '←', anchor_owners[p][:2])
        print('backlog 抽样:')
        for p in true_backlog[:8]:
            print('  ', p[:90])


if __name__ == '__main__':
    main()
