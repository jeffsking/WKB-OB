# -*- coding: utf-8 -*-
"""合并重复 concept 页（2026-10-12）。

依据：AGENTS §1.1.4（以内容最全的页为主件；副件并登记；全库改写引用；删前备份）
模式：沿用 2026-09-30 既有治理做法 —— 副件改为 `status: merged` **指针页**（不物理删除，保留原文存档）。

拟合并 5 组（两页均 growing、此前未治）：

  主件（内容最全）                                  副件（并入）
  Core Channel Pattern（芯体通道花型设计）            芯体通道花型设计
  Changeover Four-Layer Architecture（…）        83 Changeover Four-Layer Architecture（…）
  刺激响应聚合物 Stimuli-Responsive Polymer         Stimuli-Responsive Polymers
  压敏胶 PSA                                      PSA
  摩擦电自供电 TENG                                 摩擦纳米发电机 TENG

幂等：副件已是 merged 则跳过。
安全：--apply 前全量备份 WIKI/concepts + index.md。

用法：
  python .tools/_merge_duplicate_concepts_20261012.py            # dry-run
  python .tools/_merge_duplicate_concepts_20261012.py --apply
"""
import glob
import json
import os
import re
import shutil
import sys
from datetime import datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONC = os.path.join(VAULT, 'WIKI', 'concepts')
BACKUP = os.path.join(VAULT, '.tools', '_concept_merge_backup_20261012')
TODAY = '2026-10-12'
FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)

PAIRS = [
    ('Core Channel Pattern（芯体通道花型设计）', '芯体通道花型设计'),
    ('Changeover Four-Layer Architecture（换型要素四层分层与变更控制）',
     '83 Changeover Four-Layer Architecture（换型要素四层分层与变更控制）'),
    ('刺激响应聚合物 Stimuli-Responsive Polymer', 'Stimuli-Responsive Polymers'),
    ('压敏胶 PSA', 'PSA'),
    ('摩擦电自供电 TENG', '摩擦纳米发电机 TENG'),
]


def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()


def write(p, t):
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(t)


def all_wiki_files():
    return (glob.glob(os.path.join(VAULT, 'WIKI', '**', '*.md'), recursive=True)
            + [os.path.join(VAULT, 'index.md')])


def main():
    apply = '--apply' in sys.argv
    # 校验主副件存在 + 副件未合并
    todo = []
    for main, sub in PAIRS:
        mp, sp = os.path.join(CONC, main + '.md'), os.path.join(CONC, sub + '.md')
        if not os.path.exists(mp):
            print('[跳过] 主件不存在:', main); continue
        if not os.path.exists(sp):
            print('[跳过] 副件不存在:', sub); continue
        if re.search(r'^status:[ \t]*merged', read(sp), re.M):
            print('[跳过] 副件已 merged:', sub); continue
        todo.append((main, sub, mp, sp))

    print('\n待合并: %d 组' % len(todo))
    if not todo:
        print('(无需处理)')
        return

    # 统计引用
    files = all_wiki_files()
    plan = []
    for main, sub, mp, sp in todo:
        n = 0
        for f in files:
            t = read(f)
            n += t.count('[[%s]]' % sub) + t.count('[[%s|' % sub)
        plan.append((main, sub, n))
        print('  [[%s]]  ->  [[%s]]   （%d 处引用待改写）' % (sub, main, n))

    if not apply:
        print('\n(dry-run; 加 --apply 执行)')
        return

    # ---- 备份 ----
    os.makedirs(BACKUP, exist_ok=True)
    for f in glob.glob(os.path.join(CONC, '*.md')):
        shutil.copy2(f, os.path.join(BACKUP, os.path.basename(f)))
    shutil.copy2(os.path.join(VAULT, 'index.md'), os.path.join(BACKUP, '_index.md'))
    print('\n备份: %d 文件 -> %s' % (len(glob.glob(os.path.join(CONC, '*.md'))),
                                     os.path.relpath(BACKUP, VAULT)))

    # ---- 1) 副件改 merged 指针页 ----
    for main, sub, mp, sp in todo:
        t = read(sp)
        m = FM_RE.match(t)
        fm, body = (m.group(1), t[m.end():]) if m else ('', t)
        dm = re.search(r'^domain:[ \t]*(.+)$', fm, re.M)
        tg = re.search(r'^tags:[ \t]*(.+)$', fm, re.M)
        new_fm = ('---\ntype: concept\ntitle: "%s"\ndomain: %s\nstatus: merged\nupdated: %s\ntags: %s\n---\n'
                  % (sub, (dm.group(1).strip() if dm else '[待补]'), TODAY,
                     (tg.group(1).strip() if tg else '[merged]')))
        new_body = ('\n> 🔴 **治理合并（%s）**：与 [[%s]] 同主题，已并入。\n'
                    '> 入链已全量改写；本页保留为**指针页**（未删除，原文存档于下方）。\n\n'
                    '本主题正文见：\n- [[%s]]\n\n\n---\n\n## 📦 原始内容存档（合并前，%s）\n\n%s'
                    % (TODAY, main, main, TODAY, body))
        write(sp, new_fm + new_body)

    # ---- 2) 全库改写引用 ----
    changed = 0
    for f in all_wiki_files():
        t0 = read(f)
        t = t0
        for main, sub, _, _ in todo:
            t = t.replace('[[%s]]' % sub, '[[%s]]' % main)
            t = t.replace('[[%s|' % sub, '[[%s|' % main)
        if t != t0:
            write(f, t)
            changed += 1
    print('全库改写: %d 文件' % changed)

    # ---- 3) 主件加合并记录 ----
    for main, sub, mp, sp in todo:
        t = read(mp)
        note = ('\n> 🔴 **治理合并（%s）**：[[%s]] 已并入本页（同主题重复），入链已改写。\n'
                % (TODAY, sub))
        m = FM_RE.match(t)
        if m:
            t = t[:m.end()] + note + t[m.end():]
            write(mp, t)

    json.dump([{'main': a, 'sub': b} for a, b, _ in plan],
              open(os.path.join(VAULT, '.tools', '_concept_merge_20261012.json'), 'w',
                   encoding='utf-8'), ensure_ascii=False, indent=1)
    print('合并完成: %d 组' % len(todo))


if __name__ == '__main__':
    main()
