# -*- coding: utf-8 -*-
import os,re,hashlib,difflib,io,sys
sys.stdout.reconfigure(encoding='utf-8')
B='RAW_FULL/ima_sync/个人知识库/WKB/Areas/IP'
files=["01_模块一：SMMS_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md",
"01_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_US20070203469A1_Disposable_garment_comprising_meltblown_.pdf.md",
"09_包覆吸水性聚合物颗粒的方法 (EDANA ERT 完整引用).pdf.md",
"10_Method for coating SAP particles (with EDANA ERT citations).pdf.md",
"10_包覆吸水性聚合物颗粒的方法（含 SFC 详细计算）.pdf.md",
"16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物).pdf.md",
"18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤（ω型腿围橡筋）.pdf.md",
"CN102245218B.pdf.md","CN104004521B (1).pdf.md","JP5604444B2.pdf.md","US5389093.pdf.md",
"US9162007 (1).pdf.md","US9162007.pdf.md",
"v3非传统资源_②OEM测试协议_9_Nippon_Shokubai_CN_101679760_B___EDANA_测试方法引用清单.pdf.md",
"五-1_一种便于识别吸湿状态的吸收性物品及其方法.pdf.md"]
PAT=re.compile(r'(US\s?\d{4}[/\d]*\s?[AB]\d?|CN\s?\d{6,}[A-Z]?\d?|EP\s?\d{7}[A-Z]\d?|JP\s?\d{7}[A-Z]\d?|WO\s?\d{10}[A-Z]\d?|KR\s?\d{9}[A-Z]\d?)')
for f in files:
    p=os.path.join(B,f)
    t=open(p,encoding='utf-8',errors='ignore').read()
    body=t.split('---',2)[-1]
    pats=PAT.findall(body[:20000])
    from collections import Counter
    c=Counter(x.replace(' ','') for x in pats).most_common(3)
    print('###',f)
    print('  len',len(body),'sha',hashlib.sha1(body.encode()).hexdigest()[:10],'pat',c)
# diff US9162007
a=open(os.path.join(B,'US9162007.pdf.md'),encoding='utf-8',errors='ignore').read()
b=open(os.path.join(B,'US9162007 (1).pdf.md'),encoding='utf-8',errors='ignore').read()
print('\n=== US9162007 diff ===')
print('front a==b:', a.split('---',2)[:2]==b.split('---',2)[:2])
print('body equal:', a.split('---',2)[-1]==b.split('---',2)[-1])
sm=difflib.SequenceMatcher(None,a,b)
print('ratio full',round(sm.ratio(),4))
if a!=b:
    for i,(x,y) in enumerate(zip(a.splitlines(),b.splitlines())):
        if x!=y:
            print('firstdiff line',i);print(' A:',x[:200]);print(' B:',y[:200]);break
