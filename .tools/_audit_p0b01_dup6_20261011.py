# -*- coding: utf-8 -*-
"""P0-B01 近似副本回查（修正版：文件名补 .md 后缀）"""
import os,re,sys,io,difflib,itertools,collections
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D='RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/'
b01=set(l.split('|')[2].strip()+'.md' for l in io.open('.tools/compile_plan/P0-B01_Meeting_Minutes.md',encoding='utf-8') if re.match(r'^\| \d+ \|',l))
allf=sorted(f for f in os.listdir(D) if f.endswith('.md'))
def body(f):
    p=D+f
    return io.open(p,encoding='utf-8',errors='ignore').read().split('---',2)[-1] if os.path.exists(p) else None
T={f:body(f) for f in allf}; T={k:v for k,v in T.items() if v}
print('RAW_FULL 可读:',len(T),'/',len(allf))
missing=[f for f in b01 if f not in T]
print('P0-B01 中 RAW_FULL 缺失:',missing if missing else '无')
def toks(s): return set(re.findall(r'[A-Za-z]{4,}|[一-鿿]{2,}',s[:3000]))
print('\n=== P0-B01 26 条 vs 其余 %d 条：ratio>=0.55 ==='%(len(T)-len(b01)))
found=0
for f in sorted(b01):
    if f not in T: continue
    tf=toks(T[f]); best=[]
    for g in T:
        if g==f: continue
        tg=toks(T[g]); j=len(tf&tg)/max(1,len(tf|tg))
        if j<0.25: continue
        if difflib.SequenceMatcher(None,T[f],T[g]).quick_ratio()<0.45: continue
        r=difflib.SequenceMatcher(None,T[f],T[g]).ratio()
        if r>=0.55: best.append((r,j,g))
    if best:
        found+=1; print(f'  * {f}')
        for r,j,g in sorted(best,reverse=True): print(f'      {r:.4f} J={j:.2f} -> {g}')
print('  有近似副本的条目:',found)
print('\n=== 全目录 75 条两两ratio>=0.75（词元Jaccard>=0.35粗筛）===')
n=0
for a,b2 in itertools.combinations(sorted(T),2):
    ta,tb=toks(T[a]),toks(T[b2]); j=len(ta&tb)/max(1,len(ta|tb))
    if j<0.35: continue
    if difflib.SequenceMatcher(None,T[a],T[b2]).quick_ratio()<0.70: continue
    r=difflib.SequenceMatcher(None,T[a],T[b2]).ratio()
    if r>=0.75:
        n+=1
        ta_='B01' if a in b01 else '--'; tb_='B01' if b2 in b01 else '--'
        print(f'  {r:.4f} [{ta_}|{tb_}] {a[:46]:48s} <=> {b2[:46]}')
print('  高相似对数:',n)
