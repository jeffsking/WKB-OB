# -*- coding: utf-8 -*-
"""统一判重锚（2026-09-30 Reconciliation 第一步 #1）。

背景：index/源摘要页 front matter 的 source_path 双轨制——583 条指 RAW/、
269 条指 RAW_FULL/，违反 AGENTS §1「RAW 唯一事实锚点」。同资料双路径导致
判重漏判（已兑现：Absorbent Technology 4 项重同步重复件）。

动作：
  1) 备份 269 个待改写页 + index.md + AGENTS.md + _compile_backlog.json
     → .tools/_anchor_unify_backup_20260930/
  2) 269 页 front matter source_path：RAW_FULL/... → RAW/...（改前已 269/269 验证存在）
  3) 同页正文中的旧全路径引用一并替换
  4) 统一后做判重锚碰撞检查 → .tools/_anchor_collision_report.json
  5) 另把 raw/ 小写前缀归一为 RAW/

用法：python .tools/_unify_anchor_20260930.py          # dry-run
      python .tools/_unify_anchor_20260930.py --apply  # 实际执行
"""
import glob
import json
import os
import re
import shutil
import sys
from collections import Counter

VAULT = r'E:\WKB-OB'
BK = os.path.join(VAULT, '.tools', '_anchor_unify_backup_20260930')


def norm(p):
    """归一路径分隔符与前缀大小写。"""
    p = p.replace('\\', '/')
    if p.startswith('raw/'):
        p = 'RAW/' + p[4:]
    return p


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)
    print('=' * 72)
    print('判重锚统一 RAW_FULL → RAW  [%s]' % ('APPLY' if apply else 'DRY-RUN'))
    print('=' * 72)

    # 1. 收集待改写页
    pages = []
    for f in glob.glob('WIKI/sources/*.md'):
        t = open(f, encoding='utf-8', errors='ignore').read(4000)
        m = re.search(r'^source_path:\s*(.+)$', t, re.M)
        if m:
            p = m.group(1).strip().strip('"')
            if p.startswith('RAW_FULL') or p.startswith('raw/'):
                pages.append((f, p))
    rf = [x for x in pages if x[1].startswith('RAW_FULL')]
    lc = [x for x in pages if x[1].startswith('raw/')]
    print('待改写页: %d（RAW_FULL→RAW %d，raw 小写归一 %d）' % (len(pages), len(rf), len(lc)))

    # 映射可行性预检
    miss = [(f, p) for f, p in rf if not os.path.exists(p.replace('RAW_FULL', 'RAW', 1))]
    print('RAW 侧对应文件缺失: %d' % len(miss))
    if miss:
        for f, p in miss[:10]:
            print('  [缺] %s | %s' % (os.path.basename(f), p))
        print('中止：请先人工处理缺失项。')
        return

    if apply:
        os.makedirs(BK, exist_ok=True)
        for f, p in pages:
            shutil.copy2(f, os.path.join(BK, os.path.basename(f)))
        for extra in ('index.md', 'AGENTS.md', os.path.join('.tools', '_compile_backlog.json')):
            if os.path.exists(extra):
                shutil.copy2(extra, os.path.join(BK, os.path.basename(extra)))
        print('备份完成 → %s' % BK)

    # 2+3. 改写
    n_fm = n_body = 0
    rewrite_map = {}
    for f, old in pages:
        new = old.replace('RAW_FULL', 'RAW', 1) if old.startswith('RAW_FULL') else norm(old)
        t = open(f, encoding='utf-8').read()
        t2 = re.sub(r'^(source_path:\s*)"?' + re.escape(old) + r'"?\s*$',
                    lambda m: m.group(1) + new, t, count=1, flags=re.M)
        if t2 != t:
            n_fm += 1
        c = t2.count(old)
        if c:
            t2 = t2.replace(old, new)
            n_body += c
        if t2 != t:
            if apply:
                open(f, 'w', encoding='utf-8').write(t2)
            rewrite_map[os.path.basename(f)] = new
    print('front matter 改写: %d  正文路径引用改写: %d  %s'
          % (n_fm, n_body, '(已写盘)' if apply else '(dry-run)'))
    if apply and rewrite_map:
        json.dump(rewrite_map, open(os.path.join(BK, '_rewrite_map.json'), 'w',
                                    encoding='utf-8'), ensure_ascii=False, indent=1)

    # 4. 统一后碰撞检查
    allp = []
    for f in glob.glob('WIKI/sources/*.md'):
        t = open(f, encoding='utf-8', errors='ignore').read(4000)
        m = re.search(r'^source_path:\s*(.+)$', t, re.M)
        if m:
            allp.append((os.path.basename(f), norm(m.group(1).strip().strip('"'))))
    cnt = Counter(p for _, p in allp)
    dupes = {p: c for p, c in cnt.items() if c > 1}
    print('统一后判重锚碰撞组: %d（涉及 %d 页）'
          % (len(dupes), sum(dupes.values())))
    for p, c in list(dupes.items())[:20]:
        print('  x%d %s' % (c, p[:78]))
        for n, pp in allp:
            if pp == p:
                print('     - %s' % n)
    out = os.path.join(VAULT, '.tools', '_anchor_collision_report.json')
    json.dump(dupes, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('碰撞报告 → %s' % out)
    print('\n后续：python .tools/rebuild_index.py 重建索引；audit_path_consistency.py 复核。')


if __name__ == '__main__':
    main()
