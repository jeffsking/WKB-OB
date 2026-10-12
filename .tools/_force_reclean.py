# -*- coding: utf-8 -*-
"""把 fix_raw_full_frontmatter.py 回填的文件 `clean_rules` 置空，让 clean_extracted.py 真正清洗一遍。

原因：回填脚本预写了 `clean_rules: "v2: ..."`，而 clean_extracted.py 的幂等判定是
「clean_rules 含 v2 则跳过」→ 这些文件被误判为已清洗，实际未跑 R1 死链降级 / R2 重复串压缩。
"""
import glob
import os
import re

VAULT = r'E:\WKB-OB'


def main():
    os.chdir(VAULT)
    n = 0
    for f in glob.glob('RAW_FULL/**/*.md', recursive=True):
        t = open(f, encoding='utf-8', errors='ignore').read()
        if 'fm_repaired' not in t[:800]:
            continue
        new, k = re.subn(r'^clean_rules:.*$', 'clean_rules: ""', t, count=1, flags=re.M)
        if k:
            open(f, 'w', encoding='utf-8').write(new)
            n += 1
    print('已置空 clean_rules 供清洗: %d 份' % n)


if __name__ == '__main__':
    main()
