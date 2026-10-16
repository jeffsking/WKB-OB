# -*- coding: utf-8 -*-
"""回填缺失的 knowledge_update_status 字段（2026-10-12）。

背景：AGENTS §2.3 示例漏列该字段 + 两个生成器（kb_compiler / _compile_extractive）
     漏写 → 483 页 source 页缺字段。本脚本按 TEMPLATES/source.md 顺序，
     在 `credibility:` 行后插入 `knowledge_update_status: pending`。

幂等：已有该字段的页跳过。
安全：--apply 时先全量备份受影响页到 .tools/_knowledge_status_backfill_backup_20261012/。

用法：
  python .tools/_backfill_knowledge_status_20261012.py            # dry-run
  python .tools/_backfill_knowledge_status_20261012.py --apply
"""
import glob
import json
import os
import re
import shutil
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_SRC = os.path.join(VAULT, 'WIKI', 'sources')
BACKUP = os.path.join(VAULT, '.tools', '_knowledge_status_backfill_backup_20261012')
STATUS = 'pending'
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)


def find_pages():
    out = []
    for f in sorted(glob.glob(os.path.join(WIKI_SRC, '*.md'))):
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        if not m:
            continue
        if re.search(r'^knowledge_update_status:', m.group(1), re.M):
            continue
        out.append(f)
    return out


def insert(t):
    """在 front matter 内 credibility: 后插入字段；退化到 date_processed: 后；再退化到末尾。"""
    m = FM_RE.match(t)
    fm, body = m.group(1), t[m.end():]
    lines = fm.split('\n')
    idx = None
    for i, l in enumerate(lines):
        if re.match(r'^credibility:', l):
            idx = i
            break
    if idx is None:
        for i, l in enumerate(lines):
            if re.match(r'^date_processed:', l):
                idx = i
                break
    if idx is None:
        lines.append('knowledge_update_status: %s' % STATUS)
    else:
        lines.insert(idx + 1, 'knowledge_update_status: %s' % STATUS)
    return '---\n' + '\n'.join(lines) + '\n---\n' + body


def main():
    apply = '--apply' in sys.argv
    total = len(glob.glob(os.path.join(WIKI_SRC, '*.md')))
    pages = find_pages()
    # 自证覆盖率（AGENTS §1.1.2-2）
    print('sources 总页数: %d' % total)
    print('已有字段: %d' % (total - len(pages)))
    print('缺字段  : %d' % len(pages))
    print('（匹配 %d / 缺失 %d，合计 %d）' % (total - len(pages), len(pages), total))

    if not apply:
        print('\n(dry-run; 加 --apply 执行)')
        for f in pages[:10]:
            print('  ', os.path.basename(f))
        print('  ...（共 %d 页）' % len(pages))
        return

    # ---- 备份（AGENTS §1.1.4：改动前必须备份）----
    dst = os.path.join(BACKUP, 'sources')
    os.makedirs(dst, exist_ok=True)
    for f in pages:
        shutil.copy2(f, os.path.join(dst, os.path.basename(f)))
    print('\n备份: %d 页 -> %s' % (len(pages), os.path.relpath(BACKUP, VAULT)))

    # ---- 回填 ----
    n = 0
    for f in pages:
        t = open(f, encoding='utf-8', errors='ignore').read()
        nf = insert(t)
        if nf != t:
            open(f, 'w', encoding='utf-8', newline='\n').write(nf)
            n += 1
    print('已回填: %d 页 (值=%s)' % (n, STATUS))

    json.dump(
        [os.path.relpath(f, VAULT).replace('\\', '/') for f in pages],
        open(os.path.join(VAULT, '.tools', '_knowledge_status_backfill_20261012.json'),
             'w', encoding='utf-8'),
        ensure_ascii=False, indent=1)
    print('受影响清单 -> .tools/_knowledge_status_backfill_20261012.json')


if __name__ == '__main__':
    main()
