# -*- coding: utf-8 -*-
"""只读：核实 RAW ↔ RAW_FULL 镜像完整性 + 三层职责边界"""
import os, re
from collections import Counter

ROOT = 'E:/WKB-OB'
def norm(p): return p.replace('\\', '/')

raw, full = set(), set()
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW')):
    for f in fn:
        if f.endswith('.md'):
            raw.add(norm(os.path.relpath(os.path.join(dp, f), ROOT)))
for dp, dn, fn in os.walk(os.path.join(ROOT, 'RAW_FULL')):
    for f in fn:
        if f.endswith('.md'):
            full.add(norm(os.path.relpath(os.path.join(dp, f), ROOT)))

def mirror(r): return 'RAW_FULL' + r[len('RAW'):]

paired     = [r for r in raw if mirror(r) in full]
fullmap    = {mirror(r): r for r in raw}
raw_only   = sorted(r for r in raw if mirror(r) not in full)      # RAW 有、镜像无
full_only  = sorted(f for f in full if f not in fullmap)          # 镜像有、RAW 无

print('=' * 74)
print('【镜像配对】')
print(f'  RAW md{len(raw):>6} 条')
print(f'  RAW_FULL      {len(full):>6} 条')
print(f'  一一配对       {len(paired):>6} 对  （RAW 相对路径 → RAW_FULL 同相对路径）')
print(f'  仅 RAW 无镜像   {len(raw_only):>6} 条   ← 尚未回填正文')
print(f'  仅 RAW_FULL 无源 {len(full_only):>6} 条   ← 违反 1:1，需查')

# 仅 RAW 侧排除 attachments
ra = [r for r in raw_only if '/attachments/' in r]
ro = [r for r in raw_only if '/attachments/' not in r]
print(f'    └ 其中 attachments（设计不回填）: {len(ra)}')
print(f'    └ 非附件真缺口                 : {len(ro)}')

# ---- 正文规模对比 ----
def sz(p):
    try: return os.path.getsize(os.path.join(ROOT, p))
    except OSError: return 0

UNSUP = '暂不支持自动同步内容'
STUB  = 500
raw_sz   = sum(sz(r) for r in raw)
full_sz  = sum(sz(f) for f in full)
print()
print('【正文规模】')
print(f'  RAW    总字节: {raw_sz/1024/1024:>8.2f} MB   平均 {raw_sz/max(len(raw),1):>7.0f} B/条')
print(f'  RAW_FULL 总字节: {full_sz/1024/1024:>8.2f} MB   平均 {full_sz/max(len(full),1):>7.0f} B/条')

# ---- RAW_FULL 侧状态 ----
st = Counter()
for f in full:
    t = open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read()
    m = re.search(r'extract_status:\s*"?(ok|empty|original-only)"?', t)
    st[m.group(1) if m else '(无标记)'] += 1
print()
print('【RAW_FULL 侧 extract_status 分布】')
for k, v in st.most_common():
    print(f'  {k:<16}{v:>6}')

# ---- 语义对比：RAW 侧是否也有正文 ----
unsup  = [r for r in raw if UNSUP in open(os.path.join(ROOT, r), encoding='utf-8', errors='replace').read()]
shell  = [r for r in raw if sz(r) < STUB]
print()
print('【RAW 侧语义状态】')
print(f'  含"暂不支持自动同步内容"  : {len(unsup)} 条  ← 插件占位符')
print(f'  <{STUB} B 的小文件        : {len(shell)} 条  ← 空壳')
print(f'  >={STUB} B 且非占位符     : {len(raw) - len(unsup) - len(shell)} 条  ← RAW 侧本身有内容（同步即带全文的源）')

# ---- WIKI source_path 指向哪一侧 ----
import glob
anch = Counter()
for p in glob.glob(os.path.join(ROOT, 'WIKI', 'sources', '*.md')):
    t = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'^source_path:\s*(.+)$', t, re.M)
    if not m: anch['(无 source_path)'] += 1; continue
    v = m.group(1).strip().strip('"').replace('\\', '/')
    if v.lower().startswith('raw_full/'): anch['RAW_FULL（异常·应指 RAW）'] += 1
    elif v.lower().startswith('raw/'):     anch['RAW（正确·判重锚）'] += 1
    else:                                  anch[f'其他: {v[:24]}'] += 1
print()
print('【WIKI source_path 指向侧】')
for k, v in anch.most_common(10):
    print(f'  {k:<34}{v:>6}')

# ---- 仅 RAW_FULL 无源的样本 ----
if full_only:
    print()
    print('【仅 RAW_FULL 无源 · 前 10 样本】')
    for f in full_only[:10]:
        print(f'  {f}')