# -*- coding: utf-8 -*-
"""重复页治理合并（2026-09-30 Reconciliation 第二步 #6，用户已授权）。

裁决结论（本次会话逐组核实）：
  合并（dup → canonical，dup 转指针页 status: merged，入链全量改写）：
    稀释便液 BM simulant A          → BM Simulant A（便液模拟液 A）
    粘胶 Rayon                      → 粘胶纤维 Viscose Fiber
    胶乳胶黏剂 Latex                → 胶乳 Latex
    角化 Hornification              → 干燥角质化 Hornification
    SMS 纺粘熔喷复合                → SMS复合结构
    SMS 复合无纺布                  → SMS复合结构
    热风无纺布                      → 热风粘合无纺布
    热风非织造 Hot-Air Bonded Nonwoven → 热风粘合无纺布
    热粘合热风无纺布 Airlaid        → （歧义页特殊处理：指向 [[热风粘合无纺布]] 与 [[气铺 Airlaid]] 双概念）
    Cross-linked Cellulose and Derivatives      → Cross-linked Cellulose and Its Derivatives（sources 同章双编译）
    Liquid Flow in Porous Structures            → Porous Structure and Liquid Flow Models（sources 同章双编译）
  保留不合并（裁决：非重复）：
    合金粘胶 Alloy Rayon（特种纤维，非普通粘胶）；纺粘熔喷 Spunbond-Meltblown（spunmelt 工艺家族页，SMS 仅为其标准型）；
    Composite Nonwoven Structures（comparison 页）。

动作：
  1) 备份全部受影响文件 → .tools/_merge_dupes_backup_20260930/
  2) dup 页：status→merged（无则加）、updated、tags 加 merged/指针页；正文顶部加指针横幅，
     原文全量存档于「📦 原始内容存档」节（不删不丢）
  3) 全库 WIKI 入链 [[dup]] / [[dup| / [[dup# → [[canon…
  4) canonical 页追加带日期合并注记
用法：--apply 执行；默认 dry-run。
"""
import glob
import os
import re
import shutil
import sys
from datetime import date

VAULT = r'E:\WKB-OB'
BK = os.path.join(VAULT, '.tools', '_merge_dupes_backup_20260930')
TODAY = '2026-09-30'

MERGES = [  # (dup, canonical, note)
    ('稀释便液 BM simulant A', 'BM Simulant A（便液模拟液 A）', '同名对象双页（命名变体），并入高入链页'),
    ('粘胶 Rayon', '粘胶纤维 Viscose Fiber', 'Rayon 与 Viscose Fiber 同物异名，并入主页面'),
    ('胶乳胶黏剂 Latex', '胶乳 Latex', '同物两角度（胶黏剂类别 vs 粘合介质），并入来源更全页'),
    ('角化 Hornification', '干燥角质化 Hornification', '同概念双页，并入高入链页'),
    ('SMS 纺粘熔喷复合', 'SMS复合结构', 'SMS 同主题三页收敛（本页自标重叠待裁定）'),
    ('SMS 复合无纺布', 'SMS复合结构', 'SMS 同主题三页收敛'),
    ('热风无纺布', '热风粘合无纺布', '热风（through-air）系 4 标题收敛'),
    ('热风非织造 Hot-Air Bonded Nonwoven', '热风粘合无纺布', '热风系 4 标题收敛（中英变体）'),
    ('Cross-linked Cellulose and Derivatives', 'Cross-linked Cellulose and Its Derivatives', 'Absorbent Technology 同章 IMA 重同步双编译'),
    ('Liquid Flow in Porous Structures', 'Porous Structure and Liquid Flow Models', 'Absorbent Technology 同章 IMA 重同步双编译'),
]
SPECIAL_AIRLAID = '热粘合热风无纺布 Airlaid'  # 歧义页：双指向，不并入单页


def find_page(name):
    for d in ('concepts', 'entities', 'comparisons', 'sources'):
        p = os.path.join(VAULT, 'WIKI', d, name + '.md')
        if os.path.exists(p):
            return p
    return None


def pointer_body(dup, canonical, reason, special=None):
    links = special if special else ['[[%s]]' % canonical]
    lst = '\n'.join('- %s' % x for x in links)
    return ('> 🔴 **治理合并（%s）**：%s。%s\n'
            '> 入链已全量改写；本页保留为**指针页**（未删除，原文存档于下方）。\n\n'
            '本主题正文见：\n%s\n'
            % (TODAY, reason,
               '本页标题混淆了两个概念，请分别查阅：' if special else '已并入：',
               lst))


def main():
    apply = '--apply' in sys.argv
    os.chdir(VAULT)
    print('=' * 72)
    print('重复页治理合并  [%s]' % ('APPLY' if apply else 'DRY-RUN'))
    print('=' * 72)

    # 1. 收集受影响文件
    affected = {}   # path -> 原文
    plans = []
    for dup, canon, reason in MERGES:
        pd, pc = find_page(dup), find_page(canon)
        if not pd or not pc:
            print('!! 找不到页：%s（dup=%s canon=%s）' % (dup, pd, pc))
            return
        plans.append((pd, pc, dup, canon, reason))
        affected[pd] = None
        affected[pc] = None
    # 歧义页单独处理
    p_air = find_page(SPECIAL_AIRLAID)
    if not p_air:
        print('!! 找不到歧义页', SPECIAL_AIRLAID)
        return
    affected[p_air] = None

    # 入链文件
    all_files = glob.glob('WIKI/**/*.md', recursive=True)
    for f in all_files:
        t = open(f, encoding='utf-8', errors='ignore').read()
        hit = False
        for _, _, dup, _, _ in plans:
            if ('[[%s]]' % dup) in t or ('[[%s|' % dup) in t or ('[[%s#' % dup) in t:
                hit = True
        if ('[[%s]]' % SPECIAL_AIRLAID) in t or ('[[%s|' % SPECIAL_AIRLAID) in t:
            hit = True
        if hit and f not in affected:
            affected[f] = None
    print('受影响文件: %d（dup/canonical %d + 入链页 %d）'
          % (len(affected), len(plans) * 2 + 1, len(affected) - len(plans) * 2 - 1))

    if apply:
        os.makedirs(BK, exist_ok=True)
        for f in affected:
            flat = f.replace('/', '__').replace('\\', '__')
            shutil.copy2(f, os.path.join(BK, flat))
        print('备份 → %s' % BK)

    # 2. dup 指针化
    for pd, pc, dup, canon, reason in plans:
        t = open(pd, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
        if not m:
            print('!! frontmatter 解析失败：%s' % pd)
            return
        fm, body = m.group(1), m.group(2)
        if re.search(r'^status:', fm, re.M):
            fm = re.sub(r'^status:.*$', 'status: merged', fm, flags=re.M)
        else:
            fm += '\nstatus: merged'
        fm = re.sub(r'^updated:.*$', 'updated: %s' % TODAY, fm, flags=re.M)
        if 'merged' not in fm:
            fm = re.sub(r'^tags:\s*\[(.*)\]$', lambda x: 'tags: [%s, merged, 指针页]' % x.group(1),
                        fm, flags=re.M)
        seg = pointer_body(dup, canon, reason)
        new = '---\n%s\n---\n\n%s\n\n---\n\n## 📦 原始内容存档（合并前，%s）\n\n%s\n' \
              % (fm, seg, TODAY, body.strip())
        if apply:
            open(pd, 'w', encoding='utf-8').write(new)
        print('指针化: %s → %s' % (dup[:40], canon[:40]))

    # 2b. 歧义页
    t = open(p_air, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    fm, body = m.group(1), m.group(2)
    if re.search(r'^status:', fm, re.M):
        fm = re.sub(r'^status:.*$', 'status: merged', fm, flags=re.M)
    else:
        fm += '\nstatus: merged'
    fm = re.sub(r'^updated:.*$', 'updated: %s' % TODAY, fm, flags=re.M)
    seg = pointer_body(SPECIAL_AIRLAID, None, '本页标题把两个不同概念压在一个标题下（页面正文自证此歧义）',
                       special=['[[热风粘合无纺布]]（through-air 热风粘合工艺）', '[[气铺 Airlaid]]（air-laid 气流成网工艺）'])
    new = '---\n%s\n---\n\n%s\n\n---\n\n## 📦 原始内容存档（合并前，%s）\n\n%s\n' \
          % (fm, seg, TODAY, body.strip())
    if apply:
        open(p_air, 'w', encoding='utf-8').write(new)
    print('歧义拆分: %s → 双指向' % SPECIAL_AIRLAID)

    # 3. 入链改写
    n_links = 0
    n_files = 0
    for f in all_files:
        t = open(f, encoding='utf-8', errors='ignore').read()
        orig = t
        for _, _, dup, canon, _ in plans:
            for a, b in (('[[%s]]' % dup, '[[%s]]' % canon),
                         ('[[%s|' % dup, '[[%s|' % canon),
                         ('[[%s#' % dup, '[[%s#' % canon)):
                c = t.count(a)
                if c:
                    t = t.replace(a, b)
                    n_links += c
        c = t.count('[[%s]]' % SPECIAL_AIRLAID) + t.count('[[%s|' % SPECIAL_AIRLAID)
        if c:
            t = t.replace('[[%s]]' % SPECIAL_AIRLAID, '[[热风粘合无纺布]]')
            t = t.replace('[[%s|' % SPECIAL_AIRLAID, '[[热风粘合无纺布|')
            n_links += c
        if t != orig:
            n_files += 1
            if apply:
                open(f, 'w', encoding='utf-8').write(t)
    print('入链改写: %d 处 / %d 文件 %s' % (n_links, n_files, '(已写盘)' if apply else '(dry-run)'))

    # 4. canonical 追加合并注记
    if apply:
        for _, pc, dup, _, reason in plans:
            t = open(pc, encoding='utf-8').read()
            note = '\n> 🔗 治理合并（%s）：[[%s]] 已并入本页（指针页保留，原文存档于指针页）。%s\n' % (TODAY, dup, reason)
            if '治理合并（%s）' % TODAY not in t or ('[[%s]]' % dup) not in t:
                t = t.rstrip('\n') + '\n' + note
                open(pc, 'w', encoding='utf-8').write(t)
        print('canonical 注记完成')
    print('\n后续：python .tools/rebuild_index.py；log.md 追加。')


if __name__ == '__main__':
    main()
