# -*- coding: utf-8 -*-
import os,sys,re
sys.stdout.reconfigure(encoding='utf-8')
sets={
'RAW_FULL/ima_sync/个人知识库/WKB/Areas/IP':[
"01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md",
"09_包覆吸水性聚合物颗粒的方法 (EDANA ERT 完整引用).pdf.md",
"10_包覆吸水性聚合物颗粒的方法（含 SFC 详细计算）.pdf.md",
"16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物).pdf.md",
"18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤（ω型腿围橡筋）.pdf.md",
"CN102245218B.pdf.md","CN104004521B (1).pdf.md","JP5604444B2.pdf.md","US5389093.pdf.md","US9162007.pdf.md",
"五-1_一种便于识别吸湿状态的吸收性物品及其方法.pdf.md"],
'RAW_FULL/ima_sync/个人知识库/WKB/Areas/Supply Base':[
"BLOCLO盛色科技公司及产品介绍.pdf.md","Insilico_brochure_eng.pdf.md",
"Matsui 松井☆クロミ総合POP英語20260703.pdf.md","microcapsule_brochure_2019_chn.pdf.md"],
'RAW_FULL/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ':["JMP软件操作流程.docx.md"]}
for d,fs in sets.items():
    for f in fs:
        p=os.path.join(d,f)
        if not os.path.exists(p):
            print('MISSING',p);continue
        t=open(p,encoding='utf-8',errors='ignore').read()
        body=t.split('---',2)[-1]
        print('\n#####',f,'| body',len(body))
        lines=[l.strip() for l in body.splitlines() if l.strip()]
        for l in lines[:18]: print('  ',l[:180])
