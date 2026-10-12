# -*- coding: utf-8 -*-
import os,re,sys,io,difflib
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D='RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/'
fs=['Daehyoon technical visit -sum.md','Daehyoon technical visit -1.md','Daehyoon technical visit -2.md','TJ visit and meeting.md']
def b(f): return io.open(D+f,encoding='utf-8',errors='ignore').read().split('---',2)[-1]
B={f:b(f) for f in fs}
for f in fs: print(f,'len',len(B[f]))
print('\n两两相似度:')
for i in range(len(fs)):
    for j in range(i+1,len(fs)):
        r=difflib.SequenceMatcher(None,B[fs[i]],B[fs[j]]).ratio()
        print(f'  {r:.4f}  {fs[i][:34]:36s} <=> {fs[j][:34]}')
print('\n--- 每件首段 ---')
for f in fs:
    ls=[x.strip() for x in B[f].splitlines() if x.strip()]
    print('\n###',f)
    for l in ls[:8]: print('  ',l[:150])
