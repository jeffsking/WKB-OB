# -*- coding: utf-8 -*-
"""检查 RAW_FULL 中 original_path 未被迁移脚本命中的文件，定位漏网原因。"""
import glob
import os

VAULT = r'E:\WKB-OB'
os.chdir(VAULT)

files = glob.glob('RAW_FULL/**/*.md', recursive=True)
no_key = []
key_beyond = []
already = []
no_ima = []
for f in files:
    t = open(f, encoding='utf-8', errors='ignore').read()
    if 'original_path:' not in t[:1000]:
        no_key.append(f)
        continue
    lines = t.split('\n')
    idx = next((i for i, ln in enumerate(lines[:25]) if ln.startswith('original_path:')), -1)
    if idx < 0:
        key_beyond.append(f)
        continue
    v = lines[idx].split(':', 1)[1].strip().strip('"')
    if '个人知识库' in v:
        already.append(f)
    elif 'ima_sync' not in v:
        no_ima.append(f)

print('RAW_FULL 共 %d 份' % len(files))
print('  前1000字符无 original_path : %d' % len(no_key))
print('  有字段但不在前25行         : %d' % len(key_beyond))
print('  已含 个人知识库（无需改）   : %d' % len(already))
print('  值里不含 ima_sync          : %d' % len(no_ima))
for f in (no_key + key_beyond + no_ima)[:5]:
    t = open(f, encoding='utf-8', errors='ignore').read()
    print('\n  例:', f)
    print('    头 200 字:', repr(t[:200]))
