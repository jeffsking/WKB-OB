# -*- coding: utf-8 -*-
"""完整枚举缺失链接目标 + 别名改指 + 近标题匹配报告。
用法: python .tools/seed_missing.py            (报告)
      python .tools/seed_missing.py --rewrite (执行别名改指)
"""
import re, glob, os, sys, collections

WIKI = 'WIKI'
LINK = re.compile(r'\[\[([^\]\|#]+)(?:[|#][^\]]*)?\]\]')

# 1) 收集所有页面
pages = glob.glob(WIKI + '/**/*.md', recursive=True)
basenames = {os.path.basename(f)[:-3]: f for f in pages}

# 2) 别名表
alias2canon = {}
for f in pages:
    t = open(f, encoding='utf-8', errors='ignore').read()
    fm = t.split('---')[1] if t.startswith('---') else ''
    m = re.search(r'^aliases:\s*\[(.*)\]\s*$', fm, re.M)
    if m:
        for a in re.findall(r'"([^"]+)"|\'([^\']+)\'|([^,\[\]]+)', m.group(1)):
            a = (a[0] or a[1] or a[2]).strip()
            if a:
                alias2canon.setdefault(a, os.path.basename(f)[:-3])

# 3) 统计缺失目标与引用者
refs = collections.defaultdict(list)
for f in pages:
    t = open(f, encoding='utf-8', errors='ignore').read()
    for m in LINK.finditer(t):
        tgt = m.group(1).strip()
        if tgt and tgt not in basenames:
            refs[tgt].append(os.path.basename(f)[:-3])

# 4) 近标题匹配（剥括号后的主干相同）
def stem(s):
    return re.sub(r'[（(].*$', '', s).strip().lower()

stem_map = collections.defaultdict(list)
for b in basenames:
    stem_map[stem(b)].append(b)

print('缺失目标总数: %d' % len(refs))
print('涉及引用总数: %d' % sum(len(v) for v in refs.values()))
print()
alias_fix, near, seed = [], [], []
for tgt, citing in sorted(refs.items(), key=lambda x: -len(x[1])):
    if tgt in alias2canon:
        alias_fix.append((tgt, alias2canon[tgt], len(citing)))
    elif stem(tgt) in stem_map and stem(tgt):
        near.append((tgt, stem_map[stem(tgt)][:3], len(citing)))
    else:
        seed.append((tgt, len(citing), citing[:3]))

print('=== A. 别名可改指（→ 既有页）: %d 个 ===' % len(alias_fix))
for t, c, n in alias_fix: print('   [%2d 处] %s  →  %s' % (n, t, c))
print()
print('=== B. 近标题（疑似同文档异名，人工定）: %d 个 ===' % len(near))
for t, cands, n in near: print('   [%2d 处] %s   ↹ 候选: %s' % (n, t, ' | '.join(cands)))
print()
print('=== C. 需补 seed 页: %d 个 ===' % len(seed))
for t, n, c in seed: print('   [%2d 处] %s' % (n, t))

if '--rewrite' in sys.argv:
    n_files = 0
    for tgt, canon, _ in alias_fix:
        for f in pages:
            t = open(f, encoding='utf-8', errors='ignore').read()
            o = t.replace('[[%s]]' % tgt, '[[%s]]' % canon)
            o = re.sub(r'\[\[%s\|' % re.escape(tgt), '[[%s|' % canon, o)
            if o != t:
                open(f, 'w', encoding='utf-8').write(o); n_files += 1
    print('\n别名改指完成: 修改 %d 个文件' % n_files)
