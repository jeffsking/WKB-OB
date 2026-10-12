# -*- coding: utf-8 -*-
import os,re,sys,glob
sys.stdout.reconfigure(encoding='utf-8')
# 1) 收集全部 WIKI sources 页的 source_path
built={}
for p in glob.glob('WIKI/**/*.md',recursive=True):
    t=open(p,encoding='utf-8',errors='ignore').read()
    m=re.search(r'^source_path:/s*(.+)$',t,re.M)
    if m: built[m.group(1).strip()]=p
print('WIKI 已编译 source_path 条数:',len(built))
# 2) 目标 20 条
targets={
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
}
print('\n=== 精确命中(source_path 直接已在WIKI) ===')
hit=0
for t in sorted(targets):
    if t in built: print('  HIT',t.split('/')[-1][:60],'->',built[t]);hit+=1
print('  小计',hit)
print('\n=== 未命中 ===')
for t in sorted(targets):
    if t not in built: print('  MISS',t.split('/')[-1][:70])
# 3) 全库尺度：RAW 侧未编译条目中，有多少能在已编译页正文里找到同名专利号
print('\n=== 全库尺度：RAW中专利类文件 vs WIKI已编译数===')
raw_ip=[p for p in glob.glob('RAW/ima_sync/个人知识库/WKB/Areas/IP/*.md')]
print('Areas/IP RAW条目数:',len(raw_ip))
PAT=re.compile(r'(?:US\s?\d{4}[/\d]*|CN\s?\d{6,}|EP\s?\d{7}|JP\s?\d{7}|WO\s?\d{10}|KR\s?\d{9})')
def norm(s): return re.sub(r'[^0-9A-Z]','',s.upper())
allpub=set()
for p in raw_ip:
    t=open(p,encoding='utf-8',errors='ignore').read()
    for x in PAT.findall(t[:8000]): allpub.add(norm(x))
print('Areas/IP 出现的专利公开号数(归一):',len(allpub))
