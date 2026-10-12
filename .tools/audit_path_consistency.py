# -*- coding: utf-8 -*-
"""审计 RAW / RAW_FULL 两侧路径一致性，量化「路径非 1:1」的实际影响面。

用法：python .tools/audit_path_consistency.py
"""
import glob
import json
import os
import re

VAULT = r'E:\WKB-OB'


def fm_field(text, key):
    m = re.search(r'^' + key + r':\s*"?([^"\r\n]+)', text, re.M)
    return m.group(1).strip() if m else None


def main():
    os.chdir(VAULT)
    print('=' * 72)
    print('RAW / RAW_FULL 路径一致性审计')
    print('=' * 72)

    # ---------- 1. 两侧真实布局 ----------
    raw = glob.glob('RAW/**/*.md', recursive=True)
    rawa = [f for f in raw if os.sep + '个人知识库' + os.sep in f]
    rawb = [f for f in raw if os.sep + '个人知识库' + os.sep not in f]
    print('\n[1] 物理布局')
    print('  RAW      共 %d 份：含 `个人知识库` 段 %d 份 / 不含 %d 份' % (len(raw), len(rawa), len(rawb)))
    for d in os.listdir('RAW' + os.sep + 'ima_sync'):
        print('    RAW/ima_sync/ ->', d)
    for d in os.listdir('RAW_FULL' + os.sep + 'ima_sync'):
        print('    RAW_FULL/ima_sync/ ->', d)

    # ---------- 2. 台账 src 是否指向真实文件 ----------
    led = json.load(open('.tools/_extract_ledger.json', encoding='utf-8'))
    ok = bad = 0
    fixed = 0        # 插入 `个人知识库` 段后是否存在
    for e in led:
        p = e['src'].replace('/', os.sep)
        if os.path.exists(p):
            ok += 1
        else:
            bad += 1
            alt = e['src'].replace('ima_sync/', 'ima_sync/个人知识库/', 1).replace('/', os.sep)
            if os.path.exists(alt):
                fixed += 1
    print('\n[2] 台账 `src` 字段（编译判重与回溯的锚点）')
    print('  台账条目            : %d' % len(led))
    print('  src 指向真实文件    : %d' % ok)
    print('  src 指向不存在路径  : %d  ← 需插入 `个人知识库` 段的比例 %d/%d'
          % (bad, fixed, bad if bad else 1))

    # ---------- 3. RAW_FULL 的 original_path ----------
    files = glob.glob('RAW_FULL/**/*.md', recursive=True)
    n_ok = n_bad = n_none = 0
    ex_bad = []
    for f in files:
        t = open(f, encoding='utf-8', errors='ignore').read(1200)
        v = fm_field(t, 'original_path')
        if not v:
            n_none += 1
            continue
        if os.path.exists(v.replace('/', os.sep)):
            n_ok += 1
        else:
            n_bad += 1
            if len(ex_bad) < 3:
                ex_bad.append(v)
    print('\n[3] RAW_FULL 的 `original_path`')
    print('  共 %d 份：指向真实存在 %d / **指向不存在路径 %d** / 无该字段 %d'
          % (len(files), n_ok, n_bad, n_none))
    for v in ex_bad:
        alt = v.replace('ima_sync/', 'ima_sync/个人知识库/', 1)
        print('    坏例: %s' % v)
        print('          实际在: %s  (存在=%s)' % (alt, os.path.exists(alt.replace('/', os.sep))))

    # ---------- 4. WIKI source 页的 source_path ----------
    w = glob.glob('WIKI/sources/*.md')
    w_ok = w_bad = 0
    exw = []
    for f in w:
        t = open(f, encoding='utf-8', errors='ignore').read(1200)
        v = fm_field(t, 'source_path')
        if not v:
            continue
        if os.path.exists(v.replace('/', os.sep)):
            w_ok += 1
        else:
            w_bad += 1
            if len(exw) < 3:
                exw.append(v)
    print('\n[4] WIKI sources 的 `source_path`')
    print('  共 %d 页：指向真实存在 %d / **指向不存在路径 %d**' % (len(w), w_ok, w_bad))
    for v in exw:
        print('    坏例:', v)

    # ---------- 5. 重名冲突 ----------
    rawn = {}
    for f in raw:
        rawn.setdefault(os.path.basename(f), 0)
        rawn[os.path.basename(f)] += 1
    dup = [n for n, c in rawn.items() if c > 1]
    cross = 0
    full_names = {os.path.basename(f) for f in files}
    for n in full_names:
        if n in rawn:
            cross += 1
    print('\n[5] 重名')
    print('  RAW 内部同名文件名 : %d 个' % len(dup))
    print('  RAW 与 RAW_FULL 跨层同名 : %d 个（任何 [[该名]] 都无法唯一解析）' % cross)


if __name__ == '__main__':
    main()
