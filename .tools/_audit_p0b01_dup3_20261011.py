# -*- coding: utf-8 -*-
import os,re,sys,glob,hashlib,difflib,collections,io
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAWREL='RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
FULLREL='RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
b01=[l.split('|')[2].strip() for l in io.open('.tools/compile_plan/P0-B01_Meeting_Minutes.md',encoding='utf-8') if re.match(r'^\| \d+ \|',l)]
print('P0-B01 清单条目:',len(b01))
def body(p): return io.open(p,encoding='utf-8',errors='ignore').read().split('---',2)[-1]
def nm(b): return re.sub(r'^media_id:.*$','',b,flags=re.M)

# 全库 RAW<->RAW_FULL 配对 + 指纹
FP={}
for r,d,fs in os.walk('RAW'):
    if 'attachments' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        rp=os.path.join(r,f); rel=os.path.relpath(rp,'.').replace('\\','/')
        fp=rel.replace('RAW/','RAW_FULL/',1)
        if not os.path.exists(fp): continue
        FP[rel]=hashlib.sha1(nm(body(fp)).encode()).hexdigest()[:12]
print('已建立指纹的 RAW 条目:',len(FP))

print('\n=== 维度2：P0-B01 每条在全库的同指纹副本 ===')
hit=0
for f in b01:
    rel=f'{RAWREL}/{f}.md'
    h=FP.get(rel)
    if h is None: print('  [RAW_FULL缺失]',f); continue
    sib=[k for k,v in FP.items() if v==h and k!=rel]
    if sib:
        hit+=1; print(f'  * {f}')
        for s in sib: print(f'      -> {s}')
print('  有同指纹副本的条目数:',hit)

# 维度3
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
print('\n=== 维度3：P0-B01 每条 RAW 被几个 WIKI 页登记 ===')
bad=0
for f in b01:
    ps=pages.get(f'{RAWREL}/{f}.md',[])
    if len(ps)!=1:
        bad+=1; print(f'  ! {len(ps)}页  {f}')
        for x in ps: print('       ',x)
print('  登记数!=1 的条目:',bad)

# 维度4：同指纹但被登记到不同页
print('\n=== 维度4：同正文指纹被拆到多个不同页（全库）===')
g=collections.defaultdict(list)
for rel,h in FP.items():
    ps=pages.get(rel,[])
    if ps: g[h].append((rel,ps[0]))
found=0
for h,v in g.items():
    pg=set(x[1] for x in v)
    if len(pg)>1:
        found+=1
        print('  指纹',h,'->',len(pg),'个不同页:')
        for rel,p in v: print(f'      {rel.split("/")[-1][:60]:62s} -> {p}')
print('  存在拆页的指纹组数:',found)
