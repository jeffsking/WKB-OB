# -*- coding: utf-8 -*-
"""WKB-OB 编译层进度盘点：已编译源文件数 vs WIKI 页面数 vs 待编译积压量。

回答「为什么之前只编译了 62 份/页」这类口径问题，并为恢复编译提供准确的积压清单。
"""
import glob
import json
import os
import re
from collections import Counter

VAULT = r'E:\WKB-OB'


def strip_front_matter(t):
    if t.startswith('---'):
        parts = t.split('\n---', 1)
        if len(parts) == 2:
            t = parts[1].lstrip('-\n')
    return t


def net_len(path):
    """净正文长度：去 front matter、去标题、去自引用链接、去图片占位。"""
    t = open(path, encoding='utf-8', errors='ignore').read()
    t = strip_front_matter(t)
    t = re.sub(r'^\s*#.*$', '', t, flags=re.M)                 # 标题
    t = re.sub(r'\[\[[^\]]*\]\]', '', t)                       # wikilink
    t = re.sub(r'\[图片[^\]]*\]', '', t)                       # 图片降级占位
    t = re.sub(r'\|[-: ]+\|', '', t)                           # 表格分隔行
    return len(re.sub(r'\s', '', t))


def main():
    os.chdir(VAULT)
    print('=' * 74)
    print('编译层进度盘点')
    print('=' * 74)

    # ---------- 1. WIKI 页面构成 ----------
    print('\n[1] WIKI 目录实际页面数')
    total = 0
    for sub in ['sources', 'concepts', 'entities', 'comparisons']:
        n = len(glob.glob(os.path.join('WIKI', sub, '*.md')))
        total += n
        print('    %-12s %4d 页' % (sub, n))
    print('    %-12s %4d 页' % ('合计', total))

    # ---------- 2. 编译过的源文件（去重） ----------
    print('\n[2] 已编译的「源文件」数（按 sources 页的 source_path 去重）')
    srcs = []
    for f in glob.glob('WIKI/sources/*.md'):
        t = open(f, encoding='utf-8', errors='ignore').read(1500)
        m = re.search(r'^source_path:\s*"?([^"\r\n]+)', t, re.M)
        if m:
            srcs.append(m.group(1).strip())
    uniq = sorted(set(srcs))
    print('    sources 页 %d 个 → 去重后源文件 %d 份' % (len(srcs), len(uniq)))
    ex = 0
    for s in uniq:
        if os.path.exists(s.replace('/', os.sep)):
            ex += 1
    print('    其中指向真实存在的文件: %d / %d' % (ex, len(uniq)))
    # 按目录归类，看编译覆盖了哪几块
    c = Counter()
    for s in uniq:
        parts = s.replace('\\', '/').split('/')
        # 剥离 RAW/ima_sync/<库>/WKB/ 前缀
        if len(parts) >= 3 and 'ima_sync' in s:
            i = parts.index('ima_sync')
            tail = parts[i + 3:] if len(parts) > i + 3 else []
        else:
            tail = parts
        c['/'.join(tail[:2]) if tail else '(根)'] += 1
    print('    覆盖分布:')
    for k, v in c.most_common():
        print('       %-40s %d' % (k, v))

    # ---------- 3. 可编译积压量 ----------
    print('\n[3] 当前「可编译」存量（以 RAW_FULL 为准，净正文 ≥150 字）')
    led = json.load(open('.tools/_extract_ledger.json', encoding='utf-8'))
    done = [e for e in led if e['status'] == 'done']
    compilable = []
    for e in done:
        p = e['dst'].replace('/', os.sep)
        if os.path.isfile(p) and net_len(p) >= 150:
            compilable.append(e['dst'])
    compiled_set = set()
    for s in uniq:
        # 同一份 raw 的 RAW_FULL 对偶路径
        compiled_set.add(s.replace('RAW/', 'RAW_FULL/', 1).replace('\\', '/'))
    backlog = [d for d in compilable if d not in compiled_set]
    print('    台账 done          : %d 份' % len(done))
    print('    其中净正文 ≥150 字 : %d 份（真正可编译）' % len(compilable))
    print('    已被 sources 页覆盖: %d 份' % (len(compilable) - len(backlog)))
    print('    **待编译积压       : %d 份**' % len(backlog))

    # 积压按目录分布
    c2 = Counter()
    for d in backlog:
        parts = d.replace('\\', '/').split('/')
        if 'WKB' in parts:
            i = parts.index('WKB')
            tail = parts[i + 1:]
        else:
            tail = parts
        c2['/'.join(tail[:2]) if tail else '(根)'] += 1
    print('    积压目录分布 Top10:')
    for k, v in c2.most_common(10):
        print('       %-40s %d' % (k, v))

    # 未提取完的 pending 里还有多少
    pend = [e for e in led if e['status'] == 'pending']
    print('\n    （另有 pending %d 份尚未提取，W18 62 份已按用户指令暂停）' % len(pend))

    json.dump(backlog, open('.tools/_compile_backlog.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('\n    积压清单已写 .tools/_compile_backlog.json')


if __name__ == '__main__':
    main()
