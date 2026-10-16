# -*- coding: utf-8 -*-
"""P0-B02 批次 8 页 front matter 字段对齐 AGENTS §2.3（2026-10-12）。

问题（第三次「多源不一致」）：`_compile_p0b02_20261011.py` 生成时用了非标准字段名：
    source_credibility  ->  应为 credibility
    compiled_at         ->  应为 date_processed
    related             ->  应为 pages_linked
    （且缺 key_claims）

处置：**原地改名 + 补 key_claims: []**（不臆造内容）。
      `knowledge_area` / `compile_batch` / `subjects` 作为扩展元数据**保留不动**。

幂等：改完的页不再命中（无 source_credibility）。
安全：--apply 前全量备份受影响页。

用法：
  python .tools/_fix_p0b02_frontmatter_20261012.py            # dry-run
  python .tools/_fix_p0b02_frontmatter_20261012.py --apply
"""
import glob
import json
import os
import re
import shutil
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_SRC = os.path.join(VAULT, 'WIKI', 'sources')
BACKUP = os.path.join(VAULT, '.tools', '_p0b02_fm_backup_20261012')
FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)

RENAME = [('source_credibility', 'credibility'),
          ('compiled_at', 'date_processed'),
          ('related', 'pages_linked')]


def find_pages():
    """命中：P0-B02 批次页（含非标准字段名，或缺标准字段）。幂等。"""
    out = []
    for f in sorted(glob.glob(os.path.join(WIKI_SRC, '*.md'))):
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        if not m:
            continue
        fm = m.group(1)
        if not re.search(r'^type:[ \t]*source', fm, re.M):
            continue
        if (re.search(r'^source_credibility:', fm, re.M)
                or not re.search(r'^key_claims:', fm, re.M)
                or not re.search(r'^pages_linked:', fm, re.M)):
            out.append(f)
    return out


def fix(t):
    m = FM_RE.match(t)
    fm, body = m.group(1), t[m.end():]
    lines = fm.split('\n')
    out = []
    for l in lines:
        s = l
        for old, new in RENAME:
            if re.match(r'^%s:' % old, s):
                s = new + s[len(old):]
        out.append(s)
    # 补标准字段（若缺）：插在 knowledge_update_status 之后
    missing = [f for f in ('key_claims', 'pages_linked')
               if not any(re.match(r'^%s:' % f, l) for l in out)]
    if missing:
        ins = ['%s: []' % f for f in missing]
        for i, l in enumerate(out):
            if re.match(r'^knowledge_update_status:', l):
                out[i + 1:i + 1] = ins
                break
        else:
            out.extend(ins)
    return '---\n' + '\n'.join(out) + '\n---\n' + body


def main():
    apply = '--apply' in sys.argv
    pages = find_pages()
    print('命中（含 source_credibility 的页）: %d' % len(pages))
    if not apply:
        for f in pages:
            print('  ', os.path.basename(f))
        print('\n(dry-run; 加 --apply 执行)')
        return
    os.makedirs(BACKUP, exist_ok=True)
    for f in pages:
        dst = os.path.join(BACKUP, os.path.basename(f))
        if not os.path.exists(dst):        # 保留最早（最原始）备份，不被二次覆盖
            shutil.copy2(f, dst)
    print('备份: %d 页 -> %s' % (len(pages), os.path.relpath(BACKUP, VAULT)))
    n = 0
    for f in pages:
        t = open(f, encoding='utf-8', errors='ignore').read()
        nf = fix(t)
        if nf != t:
            open(f, 'w', encoding='utf-8', newline='\n').write(nf)
            n += 1
    print('已对齐: %d 页' % n)
    json.dump([os.path.relpath(f, VAULT).replace('\\', '/') for f in pages],
              open(os.path.join(VAULT, '.tools', '_p0b02_fm_fixed_20261012.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
