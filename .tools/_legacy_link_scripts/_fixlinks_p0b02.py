# -*- coding: utf-8 -*-
import io,os,sys,glob,re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIX={
 '[[松井色素（Chromicolor 温变油墨）]]':'[[松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型）]]',
 '[[拉力松紧可视化技术评估报告]]':'[[Elastic Tension Visualization Technology Assessment（拉力松紧可视化技术评估）]]',
 '[[水变油墨尿显暨松井技术交流纪要 2026-08-14]]':'[[Water-Activated Ink Wetness Indicator & Matsui Shikiso Technical Exchange（水变油墨尿显暨松井技术交流纪要 2026-08-14）]]',
 '[[盛色科技（广州盛色）光变/温变动态色彩材料产品册]]':'[[BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册]]',
 '[[Insilico 功能性微胶囊（英文公司手册）]]':'[[Insilico 功能性微胶囊产品手册（感温·感光·水致变色·香精·英文版）]]',
 '[[Insilico 功能性微胶囊（中文产品册）]]':'[[Insilico 功能性微胶囊（中文产品册·2019）]]',
}
files=['US 2007-0203469 A1 熔喷非织造背片（P&G SMMS 背片）',
'US 5266394 A SIS 嵌段共聚物热熔胶（Dow 与 Exxon·多线贴合用）',
'CN 111134966 A 防漏尿裤型纸尿裤（ω 型腿围橡筋·原件损坏）',
'BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册',
'Insilico 功能性微胶囊产品手册（感温·感光·水致变色·香精·英文版）',
'Insilico 功能性微胶囊（中文产品册·2019）',
'松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型）',
'JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版）',
'CN 101679760 B（包覆吸水性聚合物颗粒的方法·BASF）',
'CN 101641398 B（包覆吸水性聚合物颗粒的方法·BASF）',
'盛色科技官网关于我们（BLOCLO 温变与光变材料）']
for f in files:
    p='WIKI/sources/'+f+'.md'
    t=io.open(p,encoding='utf-8').read(); o=t
    for a,b in FIX.items(): t=t.replace(a,b)
    if t!=o: io.open(p,'w',encoding='utf-8',newline='\n').write(t); print('FIXED',f)
