# -*- coding: utf-8 -*-
import os,re,sys,glob,collections,io
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pages={os.path.splitext(os.path.basename(p))[0]:p for p in glob.glob('WIKI/**/*.md',recursive=True)}
new=['US 2007-0203469 A1 熔喷非织造背片（P&G SMMS 背片）',
'US 5266394 A SIS 嵌段共聚物热熔胶（Dow 与 Exxon·多线贴合用）',
'CN 111134966 A 防漏尿裤型纸尿裤（ω 型腿围橡筋·原件损坏）',
'BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册',
'Insilico 功能性微胶囊产品手册（感温·感光·水致变色·香精·英文版）',
'Insilico 功能性微胶囊（中文产品册·2019）',
'松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型）',
'JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版）']
brk=collections.defaultdict(set)
for n in new:
    t=open('WIKI/sources/'+n+'.md',encoding='utf-8').read()
    for l in re.findall(r'\[\[([^\]|#]+)',t):
        if l.strip() not in pages: brk[l.strip()].add(n)
print('本批 8 页产生断链目标数:',len(brk))
lines=['# P0-B02/B03/B04 派生断链待建页清单','',
'**生成时间**：2026-10-11　**来源批次**：P0_Areas_IP_SupplyBase_TestMethod_01','',
'本批 8 个源摘要页共产生 %d 个 wikilink 目标在 WIKI 中尚不存在。'%len(brk),'',
'按库纪律，源摘要页编译与派生概念/实体页建 seed 是**两个独立批次**，此处只登记不建页。','',
'| # | 断链目标 | 出现次数 | 来源页 |',
'|---|---|---|---|']
for i,(k,v) in enumerate(sorted(brk.items(),key=lambda x:-len(x[1])),1):
    lines.append(f'| {i} | [[{k}]] | {len(v)} | {"、".join(sorted(v))} |')
io.open('.tools/compile_plan/_P0B02B03B04_断链待建页清单.md','w',encoding='utf-8',newline='\n').write('\n'.join(lines)+'\n')
for k,v in sorted(brk.items(),key=lambda x:-len(x[1])): print(f'  {len(v)}x  [[{k}]]')
