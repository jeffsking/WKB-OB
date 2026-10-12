# -*- coding: utf-8 -*-
import os,re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
built={}   # raw_rel -> page
multi=0
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    if not t.startswith('---'): continue
    fm=t.split('---',2)[1] if len(t.split('---',2))>2 else ''
    m=re.search(r'^source_path:[ \t]*(.+)$',fm,re.M)
    if not m: continue
    built[m.group(1).strip()]=p
    ml=re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)',fm,re.M)
    if ml:
        multi+=1
        for ln in ml.group(1).splitlines():
            v=ln.strip().lstrip('-').strip()
            if v: built.setdefault(v,p)
print('WIKI 已登记 source_path 总数:',len(built),'| 含source_paths多值页:',multi)

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
print('\n=== 已登记（不需新建页）===')
hit=[]
for t in targets:
    if t in built: print('  HIT ',t.split('/')[-1][:65]);print('       ->',built[t]);hit.append(t)
print('  小计',len(hit))
print('\n=== 未登记（需编译）===')
miss=[t for t in targets if t not in built]
for t in miss: print('  MISS',t.split('/')[-1][:70])
print('  小计',len(miss))
