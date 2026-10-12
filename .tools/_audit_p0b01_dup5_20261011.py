# -*- coding: utf-8 -*-
import os,re,sys,glob,io,collections
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pages=collections.defaultdict(list)
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=io.open(p,encoding='utf-8',errors='ignore').read()
    if not t.startswith('---'): continue
    fm=t.split('---',2)[1] if len(t.split('---',2))>2 else ''
    m=re.search(r'^source_path:[ \t]*(.+)$',fm,re.M)
    if not m: continue
    lst=[m.group(1).strip()]
    ml=re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)',fm,re.M)
    if ml:
        for ln in ml.group(1).splitlines():
            v=ln.strip().lstrip('-').strip()
            if v: lst.append(v)
    for v in set(lst): pages[v].append(p)
PAIRS=[('TJ工厂访问会前简报_20260907_v3.1.docx','TJ工厂访问会前简报_20260907_v3.docx'),
       ('录音纪要_260829135725.md','录音纪要_260920002637.md'),
       ('STM-01078 OD产品折叠后长度、宽度测量方法.docx','STM-01078 OD产品折叠后长度、宽度测量方法.docx')]
BASE='RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
for a,b in PAIRS:
    print('\n===',a,'<=>',b)
    for f in (a,b):
        # 该文件可能不在MM 目录，用全库搜
        cands=[k for k in pages if k.endswith('/'+f)]
        if not cands: print('   ',f,'-> 无WIKI登记（未编译）'); continue
        for c in cands:
            print('   ',c.split('WKB/')[-1])
            for p in pages[c]: print('        ->',p)
