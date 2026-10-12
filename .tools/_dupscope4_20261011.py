# -*- coding: utf-8 -*-
import os,re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
built={};single={}
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    if not t.startswith('---'): continue
    fm=t.split('---',2)[1] if len(t.split('---',2))>2 else ''
    m=re.search(r'^source_path:[ \t]*(.+)$',fm,re.M)
    if not m: continue
    single[m.group(1).strip()]=p; built[m.group(1).strip()]=p
    ml=re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)',fm,re.M)
    if ml:
        for ln in ml.group(1).splitlines():
            v=ln.strip().lstrip('-').strip()
            if v: built.setdefault(v,p)
raws=[]
for r,d,fs in os.walk('RAW'):
    if 'attachments' in r or '\\.obsidian' in r: continue
    for f in fs:
        if f.endswith('.md'): raws.append(os.path.relpath(os.path.join(r,f),'.').replace('\\','/'))
print('RAW 条目(排除attachments):',len(raws))
old_unknown=[r for r in raws if r not in single]
newly=[r for r in old_unknown if r in built]
print('旧口径未登记:',len(old_unknown))
print('  其中其实已编译:',len(newly))
print('  真实未编译:',len(old_unknown)-len(newly))
print('\n重复登记样例(前20):')
for r in sorted(newly)[:20]: print('  ',r,'->',built[r])
