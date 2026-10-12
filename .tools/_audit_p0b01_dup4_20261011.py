# -*- coding: utf-8 -*-
"""P0-B01 近似副本回查：26条 vs Meeting Minutes 全目录78条，两两 difflib"""
import os,re,sys,io,difflib,itertools
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAWREL='RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
FULLREL='RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
b01=set(l.split('|')[2].strip() for l in io.open('.tools/compile_plan/P0-B01_Meeting_Minutes.md',encoding='utf-8') if re.match(r'^\| \d+ \|',l))
allf=sorted(f for f in os.listdir(FULLREL) if f.endswith('.md'))
def body(f):
    p=os.path.join(FULLREL,f)
    if not os.path.exists(p): return None
    return io.open(p,encoding='utf-8',errors='ignore').read().split('---',2)[-1]
D={f:body(f) for f in allf}
D={k:v for k,v in D.items() if v}
print('RAW_FULL 可读条目:',len(D),'/',len(allf))
# 先用标题词/日期/参与方做粗筛，再 difflib，避免 78*77 全量比对
def toks(s):
    return set(re.findall(r'[A-Za-z]{4,}|[一-鿿]{2,}',s[:3000]))
keys=list(D)
print('\n=== P0-B01 26 条 vs 其余 %d 条：相似度 >= 0.55 ==='%(len(keys)-len(b01)))
found=0
for f in sorted(b01):
    if f not in D: print('  [RAW_FULL缺失]',f); continue
    tf=toks(D[f]); best=[]
    for g in keys:
        if g==f: continue
        tg=toks(D[g])
        j=len(tf&tg)/max(1,len(tf|tg))
        if j<0.30: continue
        r=difflib.SequenceMatcher(None,D[f],D[g]).quick_ratio()
        if r<0.45: continue
        r=difflib.SequenceMatcher(None,D[f],D[g]).ratio()
        if r>=0.55: best.append((r,j,g))
    if best:
        found+=1
        print(f'  * {f}')
        for r,j,g in sorted(best,reverse=True): print(f'      {r:.4f} (词元Jaccard {j:.2f}) -> {g}')
print('  存在近似副本的P0-B01条目:',found)

print('\n=== 目录内两两近似 >=0.80（跨P0-B01 边界）===')
n=0
for a,b in itertools.combinations(keys,2):
    ta,tb=toks(D[a]),toks(D[b])
    j=len(ta&tb)/max(1,len(ta|tb))
    if j<0.40: continue
    r=difflib.SequenceMatcher(None,D[a],D[b]).quick_ratio()
    if r<0.75: continue
    r=difflib.SequenceMatcher(None,D[a],D[b]).ratio()
    if r>=0.80:
        n+=1
        print(f'  {r:.4f}  {a[:52]:54s} <=> {b[:52]}')
print('  高相似对数:',n)
