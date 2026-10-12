# -*- coding: utf-8 -*-
"""把 RAW_FULL 物理布局对齐到 RAW 当前布局，并批量修正三处路径元数据。

背景（2026-09-29 实测）：
  2026-09-28 05:32:35，IMA 同步程序在 RAW 侧插入了一层 `个人知识库/`
  （RAW/ima_sync/WKB/ → RAW/ima_sync/个人知识库/WKB/）。
  此后台账 `src`、RAW_FULL 的 `original_path`、WIKI 的 `source_path`
  **100% 指向不存在的路径**，判重与回溯全部失效。

本脚本（= 用户拍板的 A + B）：
  B 物理对齐：RAW_FULL/ima_sync/WKB  →  RAW_FULL/ima_sync/个人知识库/WKB
  A 元数据  ：所有含 RAW / RAW_FULL 路径的 JSON 与 front matter 字段同步改写

用法：
  python .tools/_align_rawfull_to_raw.py          # dry-run，只报告
  python .tools/_align_rawfull_to_raw.py --apply  # 实际执行（自动全量备份）
"""
import glob
import json
import os
import shutil
import sys
from datetime import datetime

VAULT = r'E:\WKB-OB'
BACKUP = os.path.join(VAULT, '.tools', '_path_migration_backup')
SEG = '个人知识库'


def insert_seg(s):
    """在 ima_sync 之后插入 `个人知识库` 段；已含则原样返回。"""
    if not isinstance(s, str) or 'ima_sync' not in s:
        return s
    if SEG in s:
        return s
    if 'ima_sync/' in s:
        return s.replace('ima_sync/', 'ima_sync/%s/' % SEG, 1)
    if 'ima_sync\\' in s:
        return s.replace('ima_sync\\', 'ima_sync\\%s\\' % SEG, 1)
    return s


def walk_strings(obj):
    """递归遍历 JSON 结构，返回 (变换后对象, 命中的路径字符串数)。"""
    n = 0

    def rec(o):
        nonlocal n
        if isinstance(o, str):
            r = insert_seg(o)
            if r != o:
                n += 1
            return r
        if isinstance(o, list):
            return [rec(x) for x in o]
        if isinstance(o, dict):
            return {k: rec(v) for k, v in o.items()}
        return o

    return rec(obj), n


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)
    print('=' * 74)
    print('RAW_FULL → RAW 布局对齐 + 路径元数据修正  [%s]' % ('APPLY' if apply else 'DRY-RUN'))
    print('=' * 74)

    old_dir = os.path.join('RAW_FULL', 'ima_sync', 'WKB')
    new_parent = os.path.join('RAW_FULL', 'ima_sync', SEG)
    new_dir = os.path.join(new_parent, 'WKB')

    # ---------- 0. 预检 ----------
    assert os.path.isdir(old_dir), '源目录不存在: %s' % old_dir
    if os.path.exists(new_dir):
        print('!! 目标已存在，可能已迁移过：', new_dir)
        return
    nfiles = sum(len(f) for _, _, f in os.walk(old_dir))
    print('\n[0] 预检 OK')
    print('    待搬迁目录 : %s  (%d 个文件)' % (old_dir, nfiles))
    print('    目标位置   : %s' % new_dir)

    if apply:
        os.makedirs(BACKUP, exist_ok=True)

    # ---------- 1. 全量备份元数据文件 ----------
    targets = sorted(glob.glob('.tools/*.json')) + sorted(glob.glob('.tools/pilot/W*_batch_*.json'))
    targets = [t for t in targets if '_path_migration_backup' not in t]
    print('\n[1] 待改写元数据文件: %d 个' % len(targets))
    if apply:
        for t in targets:
            flat = t.replace('/', '__').replace('\\', '__')
            shutil.copy2(t, os.path.join(BACKUP, flat))
        print('    已备份到 %s' % BACKUP)

    # ---------- 2. 物理搬迁 ----------
    print('\n[2] 物理搬迁')
    if apply:
        os.makedirs(new_parent, exist_ok=True)
        shutil.move(old_dir, new_dir)
        print('    已移动 → %s' % new_dir)
    else:
        print('    [dry-run] 将执行: move %s → %s' % (old_dir, new_dir))

    # ---------- 3. JSON 元数据改写 ----------
    print('\n[3] JSON 路径字段改写（ima_sync/ → ima_sync/%s/）' % SEG)
    total_hits = 0
    for t in targets:
        try:
            d = json.load(open(t, encoding='utf-8'))
        except Exception as ex:
            print('    [跳过] %s (%s)' % (t, ex))
            continue
        nd, hits = walk_strings(d)
        if hits:
            total_hits += hits
            print('    %-52s %4d 处' % (t.replace('.tools/', '')[:52], hits))
            if apply:
                json.dump(nd, open(t, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('    JSON 合计命中 %d 处' % total_hits)

    # ---------- 4. RAW_FULL front matter 的 original_path ----------
    print('\n[4] RAW_FULL front matter 的 original_path')
    base = new_dir if apply else old_dir
    n_fm = n_fix_rel = n_broken = 0
    broken = []
    for f in glob.glob(os.path.join(base, '**', '*.md'), recursive=True):
        t = open(f, encoding='utf-8', errors='ignore').read()
        lines = t.split('\n')
        idx = next((i for i, ln in enumerate(lines[:25]) if ln.startswith('original_path:')), -1)
        if idx < 0:
            continue
        rel = os.path.relpath(f, base).replace(os.sep, '/')
        # 权威取值：从文件自身在 RAW_FULL 中的相对位置反推 RAW 侧真实路径
        cand = 'RAW/ima_sync/%s/WKB/%s' % (SEG, rel)
        if os.path.exists(cand.replace('/', os.sep)):
            nv = cand
        else:
            old = lines[idx].split(':', 1)[1].strip().strip('"')
            alt = insert_seg(old)
            if os.path.exists(alt.replace('/', os.sep)):
                nv = alt
            else:
                n_broken += 1
                broken.append((f, rel))
                continue
        old = lines[idx].split(':', 1)[1].strip().strip('"')
        if nv != old:
            lines[idx] = 'original_path: "%s"' % nv
            if 'ima_sync' not in old:
                n_fix_rel += 1
            n_fm += 1
            if apply:
                open(f, 'w', encoding='utf-8').write('\n'.join(lines))
    print('    改写 %d 份（其中 %d 份原为残缺相对路径）; 无法定位原件 %d 份'
          % (n_fm, n_fix_rel, n_broken))
    for f, rel in broken[:5]:
        print('      [需人工] %s' % rel)

    # ---------- 5. WIKI source 页的 source_path ----------
    print('\n[5] WIKI sources 的 source_path')
    n_w = 0
    for f in glob.glob(os.path.join('WIKI', 'sources', '*.md')):
        t = open(f, encoding='utf-8', errors='ignore').read()
        lines = t.split('\n')
        changed = False
        for i, ln in enumerate(lines[:20]):
            if ln.startswith('source_path:'):
                v = ln.split(':', 1)[1].strip().strip('"')
                nv = insert_seg(v)
                if nv.lower().startswith('raw/'):
                    nv = 'RAW/' + nv[4:]
                if nv != v:
                    lines[i] = 'source_path: %s' % nv
                    changed = True
                break
        if changed:
            n_w += 1
            if apply:
                open(f, 'w', encoding='utf-8').write('\n'.join(lines))
    print('    命中 %d 页（%s）' % (n_w, '已改写' if apply else 'dry-run'))

    print('\n' + '=' * 74)
    if apply:
        print('完成。备份：%s' % BACKUP)
        print('请随后运行：python .tools/audit_path_consistency.py 复核')
    else:
        print('DRY-RUN 结束。加 --apply 执行。')


if __name__ == '__main__':
    main()
