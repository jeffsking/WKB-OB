# -*- coding: utf-8 -*-
"""WIKI 层命名与路径一致性修复（2026-09-29）

1) 消除跨目录重名：源摘要页文件名与其 title 不一致、且与概念页同名
   → 重命名为 title（库内约定：文件名 = 页面标题 = wikilink 文本）
2) 修正 WIKI 正文里残留的旧短路径 `raw/ima_sync/WKB/` → `raw/ima_sync/个人知识库/WKB/`
   （此前 _align_rawfull_to_raw.py 只改了 front matter 的 source_path 字段）
"""
import glob
import os
import re

VAULT = r'E:\WKB-OB'
SEG = '个人知识库'

RENAME = [('WIKI/sources/聚酯水解与水分控制.md',
           'WIKI/sources/聚酯为什么要控制水分：水解机理、动力学与纺丝后果.md')]


def fix_body_paths(text):
    """把正文/字段里的旧短路径补上 个人知识库 段（不重复插入）。

    策略：文件里完全没有 `个人知识库` → 直接全局替换；已出现 → 用负向先行断言
    只替换后面没紧跟该段的那些（幂等）。
    """
    out = text
    for a, b in [('raw/ima_sync/WKB/', 'raw/ima_sync/%s/WKB/' % SEG),
                 ('RAW/ima_sync/WKB/', 'RAW/ima_sync/%s/WKB/' % SEG),
                 ('raw\\ima_sync\\WKB\\', 'raw\\ima_sync\\%s\\WKB\\' % SEG),
                 ('RAW\\ima_sync\\WKB\\', 'RAW\\ima_sync\\%s\\WKB\\' % SEG)]:
        if SEG not in out:
            out = out.replace(a, b)
        else:
            # 用 lambda 作替换，避免替换串里的反斜杠被 re 当转义解析
            out = re.sub(re.escape(a) + r'(?!%s)' % re.escape(SEG),
                         lambda m, _b=b: _b, out)
    return out


def main():
    os.chdir(VAULT)
    print('=== 1) 重命名消除跨目录重名 ===')
    for old, new in RENAME:
        if not os.path.exists(old):
            print('   [跳过] 已不存在:', old)
            continue
        if os.path.exists(new):
            print('   [跳过] 目标已存在:', new)
            continue
        os.rename(old, new)
        print('   %s\n     -> %s' % (old, new))

    print('\n=== 2) 修正 WIKI 正文旧短路径 ===')
    total = 0
    for f in glob.glob('WIKI/**/*.md', recursive=True):
        t = open(f, encoding='utf-8', errors='ignore').read()
        n = fix_body_paths(t)
        if n != t:
            cnt = t.count('raw/ima_sync/WKB/') + t.count('RAW/ima_sync/WKB/')
            open(f, 'w', encoding='utf-8').write(n)
            total += 1
            print('   %-52s %d 处' % (os.path.basename(f)[:52], cnt))
    print('   共修改 %d 个页面' % total)

    print('\n=== 3) index.md 同步更新 ===')
    p = 'index.md'
    t = open(p, encoding='utf-8').read()
    o = t.replace('[[聚酯水解与水分控制]]',
                  '[[聚酯为什么要控制水分：水解机理、动力学与纺丝后果]]')
    # index 列表里可能写作 `聚酯水解与水分控制` 纯文本
    o = o.replace('- 聚酯水解与水分控制\n',
                  '- 聚酯为什么要控制水分：水解机理、动力学与纺丝后果\n')
    if o != t:
        open(p, 'w', encoding='utf-8').write(o)
        print('   index.md 已更新')
    else:
        print('   index.md 无需改动')

    print('\n=== 4) 复检重名 ===')
    import collections
    names = collections.defaultdict(list)
    for f in glob.glob('WIKI/**/*.md', recursive=True):
        names[os.path.basename(f)].append(f)
    dup = {k: v for k, v in names.items() if len(v) > 1}
    print('   剩余重名:', len(dup), dup if dup else '（无）')


if __name__ == '__main__':
    main()
