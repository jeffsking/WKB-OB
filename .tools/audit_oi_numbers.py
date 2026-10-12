# -*- coding: utf-8 -*-
"""审计 WIKI 中的 OI 编号引用口径（人工裁决：默认基准 = 重构版 E，09-18，19 项，OI-1~OI-19）。

判定规则（书面化，便于人工复核）：
  - **不补零** `OI-1` ~ `OI-19` → 符合默认基准（E 口径）
  - **补零** `OI-01` ~ `OI-25` → 旧口径（官方 v2 / 大纲 v7），**引用时必须注明出处与日期**，否则不可回溯
  - 同一页出现两种形式 → 标注为「混用」，列为清理待办（转写时逐条补注出处）

用法：python .tools/audit_oi_numbers.py [--list]
"""
import glob
import os
import re
import sys

VAULT = r'E:\WKB-OB'
# （无外部依赖）


def main():
    show = '--list' in sys.argv
    os.chdir(VAULT)
    padded, plain, mixed = [], [], []
    for f in glob.glob('WIKI/**/*.md', recursive=True):
        t = open(f, encoding='utf-8', errors='ignore').read()
        p = set(re.findall(r'OI-0\d+', t))
        q = set(re.findall(r'OI-[1-9]\d?(?!\d)', t)) - p
        name = os.path.basename(f)[:-3]
        if p and q:
            mixed.append((name, sorted(p), sorted(q)))
        elif p:
            padded.append((name, sorted(p)))
        elif q:
            plain.append((name, sorted(q)))

    print('=' * 74)
    print('OI 编号引用口径审计（默认基准 = 重构版 E · 09-18 · 19 项 · OI-1~OI-19）')
    print('=' * 74)
    print('  符合基准（仅不补零 OI-x）      : %d 页' % len(plain))
    print('  旧口径（仅补零 OI-0x，须注明）  : %d 页' % len(padded))
    print('  ⚠️ 两套混用（清理待办）        : %d 页' % len(mixed))
    print('  合计引用 OI 编号               : %d 页' % (len(plain) + len(padded) + len(mixed)))

    if show:
        print('\n--- 旧口径（补零）---')
        for n, p in padded:
            print('  %-52s %s' % (n[:52], ' '.join(p)))
        print('\n--- 混用 ---')
        for n, p, q in mixed:
            print('  %-52s 补零: %-26s 不补零: %s' % (n[:52], ' '.join(p), ' '.join(q)))

    print('\n处置口径：**不自动转换**（需逐条核对原文语义与 old→new 对照表）——')
    print('  下次编辑这些页面时，逐条为旧口径编号补注「(出自 X 清单 + 日期)」，或按 old→new 对照表换算为基准编号。')


if __name__ == '__main__':
    main()
