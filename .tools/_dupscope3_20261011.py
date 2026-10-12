# -*- coding: utf-8 -*-
import os,re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
built={}
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    if not t.startswith('---'): continue
    fm=t.split('---',2)[1] if len(t.split('---',2))>2 else ''
    m=re.search(r'^source_path:[ \t]*(.+)$',fm,re.M)
    if not m: continue
    built[m.group(1).strip()]=p
    ml=re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)',fm,re.M)
    if ml:
        for ln in ml.group(1).splitlines():
            v=ln.strip().lstrip('-').strip()
            if v: built.setdefault(v,p)
raws=[]
for base in ('RAW/ima_sync/个人知识库/WKB',):
    for r,d,fs in os.walk(base):
        if 'attachments' in r: continue
        for f in fs:
            if f.endswith('.md'): raws.append(os.path.relpath(os.path.join(r,f),'RAW').replace('\\','/'))
print('RAW 条目(排除attachments):',len(raws))
known=[r for r in raws if r in built]
unknown=[r for r in raws if r not in built]
print('已登记 source_path:',len(known))
print('未登记:',len(unknown))
# 旧口径（只查单值 source_path）
single={}
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    if not t.startswith('---'): continue
    fm=t.split('---',2)[1] if len(t.split('---',2))>2 else ''
    m=re.search(r'^source_path:[ \t]*(.+)$',fm,re.M)
    if m: single[m.group(1).strip()]=p
old_unknown=[r for r in raws if r not in single]
print('\n旧口径(仅单值source_path)未登记:',len(old_unknown))
newly=[r for r in old_unknown if r in built]
print('其中其实已编译(被source_paths/合并页覆盖):',len(newly))
print('真实未编译:',len(old_unknown)-len(newly))
