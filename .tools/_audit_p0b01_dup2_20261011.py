# -*- coding: utf-8 -*-
import os,re,sys,glob,hashlib,difflib,collections,io,json
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAWD='RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
b01=[l.split('|')[2].strip() for l in io.open('.tools/compile_plan/P0-B01_Meeting_Minutes.md',encoding='utf-8') if re.match(r'^\| \d+ \|',l)]
print('P0-B01 清单条目:',len(b01))

def body(p):
    return io.open(p,encoding='utf-8',errors='ignore').read().split('---',2)[-1]
def nm(b): return re.sub(r'^media_id:.*$','',b,flags=re.M)

# 全库正文指纹（忽略 media_id）
FP={}
for r,d,fs in os.walk('RAW'):
    if 'attachments' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        p=os.path.join(r,f)
        rel=os.path.relpath(p,'.').replace('\\','/')
        if not os.path.exists(p.replace('RAW'+os.sep,'RAW_FULL'+os.sep,1)): continue
        b=body(p.replace('RAW'+os.sep,'RAW_FULL'+os.sep,1))
        FP[rel]=hashlib.sha1(nm(b).encode()).hexdigest()[:12]

print('\n=== 维度2：P0-B01 每条在 RAW 全库中的同指纹副本 ===')
hit=0
for f in b01:
    rel=f'RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/{f}'
    h=FP.get(rel)
    if h is None: print('  [无RAW_FULL]',f);continue
    sib=[k for k,v in FP.items() if v==h and k!=rel]
    if sib:
        hit+=1
        print(f'  * {f}')
        for s in sib: print(f'      副本-> {s}')
print('  有副本的条目数:',hit)

# 维度3：P0-B01 的 26 条建了哪些页，页的 source_path 是否唯一
pages={}
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
    for v in lst: pages.setdefault(v,[]).append(p)
print('\n=== 维度3：P0-B01 每条 RAW 被几个 WIKI 页登记 ===')
bad=0
for f in b01:
    rel=f'RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/{f}'
    ps=pages.get(rel,[])
    if len(ps)!=1:
        bad+=1
        print(f'  ! {len(ps)}页  {f}')
        for x in ps: print('       ',x)
print('  登记数!=1 的条目:',bad)
# 维度4：反向——同一 WIKI 页是否登记了多个 MM 目录条目
print('\n=== 维度4：一个页登记多个 MM 条目（潜在合并）===')
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
    mm=[x for x in lst if 'Meeting Minutes/' in x]
    if len(set(mm))>1:
        print('  ',p)
        for x in sorted(set(mm)): print('      ',x.split('/')[-1])
