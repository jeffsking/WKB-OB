# -*- coding: utf-8 -*-
"""回查P0-B01（Meeting Minutes 26条）是否存在同一文件多个 RAW 副本被重复编译。
三个维度：1) 26条之间正文互相重复 2) 26条是否被其他已编译页以其他副本登记 3) 同目录全量副本关系"""
import os,re,sys,glob,hashlib,difflib,collections,io
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE='RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
RAWD='RAW/ima_sync/个人知识库/WKB/Areas/Meeting Minutes'
print('RAW 目录条目数:',len([f for f in os.listdir(RAWD) if f.endswith('.md')]))
print('RAW_FULL 目录条目数:',len([f for f in os.listdir(BASE) if f.endswith('.md')]))
names=sorted(f for f in os.listdir(RAWD) if f.endswith('.md'))

def body(p):
    t=io.open(p,encoding='utf-8',errors='ignore').read()
    return t.split('---',2)[-1]
def strip_media(b):
    return re.sub(r'^media_id:.*$','',b,flags=re.M)

B={}
for f in names:
    p=os.path.join(BASE,f)
    if not os.path.exists(p): B[f]=None; continue
    b=body(p)
    B[f]=dict(len=len(b),sha=hashlib.sha1(b.encode()).hexdigest()[:10],
              sha_nm=hashlib.sha1(strip_media(b).encode()).hexdigest()[:10])
print('\n=== 维度1：正文完全相同（sha 忽略 media_id）===')
g=collections.defaultdict(list)
for f,v in B.items():
    if v: g[v['sha_nm']].append(f)
dup1={k:v for k,v in g.items() if len(v)>1}
if not dup1: print('  无')
for k,v in dup1.items():
    print('  组',k,'->')
    for f in v: print('     ',f,'| len',B[f]['len'],'| sha',B[f]['sha'])
print('\n=== 维度1b：media_id 也相同（即同一 media 完全重复落盘）===')
g2=collections.defaultdict(list)
for f,v in B.items():
    if v: g2[v['sha']].append(f)
for k,v in g2.items():
    if len(v)>1:
        print('  ',k)
        for f in v: print('     ',f)
