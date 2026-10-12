# -*- coding: utf-8 -*-
import os,re,sys
sys.stdout.reconfigure(encoding='utf-8')
T=[
('IP','RAW_FULL/ima_sync/个人知识库/WKB/Areas/IP/01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md'),
('IP','RAW_FULL/ima_sync/个人知识库/WKB/Areas/IP/16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物).pdf.md'),
('IP','RAW_FULL/ima_sync/个人知识库/WKB/Areas/IP/18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤（ω型腿围橡筋）.pdf.md'),
('SB','RAW_FULL/ima_sync/个人知识库/WKB/Areas/Supply Base/BLOCLO盛色科技公司及产品介绍.pdf.md'),
('SB','RAW_FULL/ima_sync/个人知识库/WKB/Areas/Supply Base/Insilico_brochure_eng.pdf.md'),
('SB','RAW_FULL/ima_sync/个人知识库/WKB/Areas/Supply Base/Matsui 松井☆クロミ総合POP英語20260703.pdf.md'),
('SB','RAW_FULL/ima_sync/个人知识库/WKB/Areas/Supply Base/microcapsule_brochure_2019_chn.pdf.md'),
('TM','RAW_FULL/ima_sync/个人知识库/WKB/Areas/Test Method/成品/TJ/JMP软件操作流程.docx.md'),
]
for tag,p in T:
    t=open(p,encoding='utf-8',errors='ignore').read()
    body=t.split('---',2)[-1]
    print('\n==========',tag,p.split('/')[-1],'len',len(body))
    for l in [x.strip() for x in body.splitlines() if x.strip()][:60]:
        print(' ',l[:170])
