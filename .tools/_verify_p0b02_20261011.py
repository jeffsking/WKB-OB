# -*- coding: utf-8 -*-
import os,re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
built={}
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    if not t.startswith('---'): continue
    fm=t.split('---',2)[1] if len(t.split('---',2))>2 else ''
    m=re.search(r'^source_path:[ \t]*(.+)$',fm,re.M)
    if not m: continue
    built[m.group(1).strip()]=p
    ml=re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)',fm,re.M)
    if ml:
        for ln in ml.group(1).splitlines():
            v=ln.strip().lstrip('-').strip()
            if v: built.setdefault(v,p)

targets=[
'RAW/ima_sync/个人知识库/WKB/Areas/IP/01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/01_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/09_包覆吸水性聚合物颗粒的方法 (EDANA ERT 完整引用).pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/10_Method for coating SAP particles (with EDANA ERT citations).pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/10_包覆吸水性聚合物颗粒的方法（含 SFC 详细计算）.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物).pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤（ω型腿围橡筋）.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/CN102245218B.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/CN104004521B (1).pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/JP5604444B2.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/US5389093.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/US9162007 (1).pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/US9162007.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/v3非传统资源_②OEM测试协议_9_Nippon_Shokubai_CN_101679760_B___EDANA_测试方法引用清单.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/IP/五-1_一种便于识别吸湿状态的吸收性物品及其方法.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/BLOCLO盛色科技公司及产品介绍.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/Insilico_brochure_eng.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/Matsui 松井☆クロミ総合POP英語20260703.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/Supply Base/microcapsule_brochure_2019_chn.pdf.md',
'RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/JMP软件操作流程.docx.md',
]
miss=[t for t in targets if t not in built]
print('P0-B02/03/04 共 20 条 -> 已登记 %d / 未登记 %d'%(len(targets)-len(miss),len(miss)))
for m in miss: print('  MISS',m)
# RAW 未被写入校验
print('\nRAW md 数(排除attachments):', sum(1 for r,d,fs in os.walk('RAW') if 'attachments' not in r for f in fs if f.endswith('.md')))
n=0
for r,d,fs in os.walk('RAW'):
    for f in fs:
        if f.endswith('.md'):
            t=open(os.path.join(r,f),encoding='utf-8',errors='ignore').read()
            if re.search(r'^(extract_status|date_processed|key_claims):',t,re.M): n+=1
print('RAW 侧被写入 AI 字段的文件数(应为0):',n)
# 新页 source_path 全部指向 RAW
newpages=['US 2007-0203469 A1 熔喷非织造背片（P&G SMMS 背片）.md',
'US 5266394 A SIS 嵌段共聚物热熔胶（Dow 与 Exxon·多线贴合用）.md',
'CN 111134966 A 防漏尿裤型纸尿裤（ω 型腿围橡筋·原件损坏）.md',
'BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册.md',
'Insilico 功能性微胶囊产品手册（感温·感光·水致变色·香精·英文版）.md',
'Insilico 功能性微胶囊（中文产品册·2019）.md',
'松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型）.md',
'JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版）.md']
print('\n=== 新页校验 ===')
for f in newpages:
    p='WIKI/sources/'+f
    if not os.path.exists(p): print('  MISSING',f);continue
    t=open(p,encoding='utf-8').read()
    fm=t.split('---',2)[1]
    sp=re.findall(r'^source_paths?:[ \t]*',fm,re.M)
    rawbad=[x for x in re.findall(r'(RAW_FULL/\S+)',fm)]
    f6=all(k in fm for k in ('type:','title:','source_type:','source_path:','subjects:','knowledge_update_status:'))
    st=re.search(r'^knowledge_update_status:[ \t]*(.+)$',fm,re.M)
    print(f'  OK {f[:44]:46s} 六字段={f6} RAW_FULL泄漏={len(rawbad)} status={st.group(1).strip()}')
# 全库source_path 指向 RAW_FULL 的页数
allbad=0
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    m=re.search(r'^source_path:[ \t]*(.+)$',t,re.M)
    if m and m.group(1).strip().startswith('RAW_FULL/'): allbad+=1
print('\n全库 source_path 误指向 RAW_FULL 的页数(应为0):',allbad)
