# -*- coding: utf-8 -*-
"""归一化 WIKI front matter 的 title，使之与文件名一致（库内约定：文件名 = 页面标题 = wikilink 文本）。

原 title 的长写法（含英文扩展/括号说明）写入 `aliases:`，Obsidian 仍可用旧写法解析链接。

用法：python .tools/normalize_titles.py [--apply]
"""
import glob
import os
import re
import sys

VAULT = r'E:\WKB-OB'


def norm(s):
    s = re.sub(r'[（(][^）)]*[）)]', '', s)
    s = re.sub(r'[\s_\-–—×x·、，,。.:：;；"\'“”‘’]', '', s)
    return s.strip().lower()


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)
    fixed = []
    for f in glob.glob('WIKI/**/*.md', recursive=True):
        t = open(f, encoding='utf-8', errors='ignore').read()
        if not t.startswith('---'):
            continue
        head, sep, rest = t.partition('\n---\n')
        fm_lines = head.split('\n')[1:]
        title_i = next((i for i, l in enumerate(fm_lines)
                        if re.match(r'^title:', l)), None)
        if title_i is None:
            continue
        base = os.path.basename(f)[:-3]
        cur = fm_lines[title_i].split(':', 1)[1].strip().strip('"')
        if cur == base:
            continue
        fm_lines[title_i] = 'title: "%s"' % base
        if not any(l.startswith('aliases:') for l in fm_lines):
            fm_lines.append('aliases: ["%s"]' % cur.replace('"', "'"))
        fixed.append((base, cur))
        if apply:
            open(f, 'w', encoding='utf-8').write('---\n' + '\n'.join(fm_lines) + '\n---\n' + rest)

    print('title 与文件名不一致: %d 页' % len(fixed))
    for b, c in fixed[:10]:
        print('   %-42s  (原 title: %s)' % (b[:42], c[:52]))
    if len(fixed) > 10:
        print('   ...（其余 %d 页）' % (len(fixed) - 10))
    print('\n%s' % ('已归一化（原 title 存入 aliases）' if apply else '（dry-run，加 --apply 执行）'))


if __name__ == '__main__':
    main()
