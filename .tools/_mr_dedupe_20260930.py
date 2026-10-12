# -*- coding: utf-8 -*-
"""manual_review 机械去重（2026-09-30 第二步 #8）。

裁决依据（本会话核验）：
  1) 变色油墨供应商综合技术联系表（1）——与主表同一 xlsx 的重传件（正文相似度 0.80，
     主表自标 duplicate/companion of '(1)'）→ 并入主表
  2) ASTM E2149-20（平行备份）——同一标准号的平行备份页（两页正文均缺失）→ 并入主 ASTM 页
两页均转 status: merged 指针页（原文存档保留，不删除）。
用法：python .tools/_mr_dedupe_20260930.py --apply
"""
import glob
import os
import re
import shutil
import sys

VAULT = r'E:\WKB-OB'
BK = os.path.join(VAULT, '.tools', '_manual_review_dedupe_backup_20260930')
TODAY = '2026-09-30'

PAIRS = [
    ('WIKI/sources/变色油墨供应商综合技术联系表（1）.md',
     '变色油墨供应商综合技术联系表'),
    ('WIKI/sources/ASTM E2149-20 Dynamic Contact Antimicrobial Activity（平行备份 · 正文同样缺失）.md',
     'ASTM E2149-20 Dynamic Contact Antimicrobial Activity（标准正文缺失 · 仅 ASTM 知识产权政策前置页）'),
]


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)
    if apply:
        os.makedirs(BK, exist_ok=True)
    for dup, canon in PAIRS:
        if not os.path.exists(dup):
            print('!! 缺文件:', dup)
            return
        if apply:
            shutil.copy2(dup, os.path.join(BK, os.path.basename(dup).replace('/', '__')))
        t = open(dup, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
        fm, body = m.group(1), m.group(2)
        if re.search(r'^status:', fm, re.M):
            fm = re.sub(r'^status:.*$', 'status: merged', fm, flags=re.M)
        else:
            fm += '\nstatus: merged'
        fm = re.sub(r'^.*manual_review.*\n?', '', fm, flags=re.M)
        fm = re.sub(r'^updated:.*$', 'updated: %s' % TODAY, fm, flags=re.M)
        seg = ('> 🔴 **治理合并（%s）**：与 [[%s]] 为同一对象（重复上传/平行备份）。'
               '本页保留为指针页，原文存档于下方。\n\n本页正文见：[[%s]]\n' % (TODAY, canon, canon))
        new = '---\n%s\n---\n\n%s\n\n---\n\n## 📦 原始内容存档（合并前，%s）\n\n%s\n' \
              % (fm, seg, TODAY, body.strip())
        if apply:
            open(dup, 'w', encoding='utf-8').write(new)
        print('指针化:', os.path.basename(dup)[:60])

    n = 0
    for f in glob.glob('WIKI/**/*.md', recursive=True):
        t = open(f, encoding='utf-8', errors='ignore').read()
        o = t
        for dup, canon in PAIRS:
            name = os.path.basename(dup)[:-3]
            t = t.replace('[[%s]]' % name, '[[%s]]' % canon)
            t = t.replace('[[%s|' % name, '[[%s|' % canon)
        if t != o:
            n += 1
            if apply:
                open(f, 'w', encoding='utf-8').write(t)
    print('入链改写文件: %d %s' % (n, '(已写盘)' if apply else '(dry-run)'))


if __name__ == '__main__':
    main()
