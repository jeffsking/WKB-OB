# -*- coding: utf-8 -*-
"""只读：提取 P0-B01 各源文件的结构化要点（H2/H3 + 首段 + 数字行）"""
import os, re, sys

ROOT = 'E:/WKB-OB'
MD = os.path.join(ROOT, 'RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes')

TARGETS = [
 ('CO V6 新体机芯体验证实验方案评审.md', 'note_3867e2b6...'),
 ('Daehyoon technical visit - sum.md', ''),
 ('Daehyoon technical visit -1.md', ''),
 ('Daehyoon technical visit -2.md', ''),
 ('Huayi集团创新非织造布技术交流会.md', ''),
 ('KC 拜访供应商维盛（新维盛）——公司介绍、行业情况交流及合.md', ''),
 ('KC与福建兴泰SMS无纺布供应商技术交流会.md', ''),
 ('KC团队内部技术讨论会（TBCW在线超声波复合工艺）.md', ''),
 ('Liner trial request.md', ''),
 ('OI 会议纪要.md', ''),
 ('TJ visit and meeting.md', ''),
 ('与华峰集团研发及合作会议纪要.md', ''),
 ('会议纪要 山东希瑞新材.md', ''),
 ('会议纪要 松井油墨分享.md', ''),
 ('会议纪要FEI&OI 益生菌.md', ''),
 ('会议纪要：Bryan 1_1 纤维加工工艺验证及材料研发规划.md', ''),
 ('会议纪要：Q2 Mini BS - 创新功能开发脑暴会.md', ''),
 ('复合纤维生产工艺及性能探讨（KC 与闽瑞纤维技术交流）.md', ''),
 ('尿裤（卫生巾）弹性收紧力不足问题及Niso材料工艺改进方案探.md', ''),
 ('日本Nichdai 丝网工艺技术交流.md', ''),
 ('汉高亚太研发中心技术交流会会议纪要.md', ''),
 ('紫华公司与KC团队技术交流会议.md', ''),
 ('纸尿裤产品设计与材料开发评审会（涉及芯体结构、导流设计、SA.md', ''),
]

def digest(p):
    t = open(p, encoding='utf-8', errors='replace').read()
    # front matter
    fm = {}
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"')
    body = t[m.end():] if m else t
    # 标题层级
    heads = re.findall(r'^#{2,4}\s*(.+)$', body, re.M)
    # 含数字的正文行（潜在关键参数）
    nums = []
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith('#'): continue
        if re.search(r'\d+\s*(mm|gsm|G|克|%|度|MPa|kPa|m/min|片|公斤|kg|分钟|小时|个|级|档|元)', s):
            nums.append(re.sub(r'\s+', ' ', s)[:110])
    return fm, heads, nums, len(body)

for i, (fn, _) in enumerate(TARGETS, 1):
    p = os.path.join(MD, fn)
    if not os.path.isfile(p):
        print(f'[{i:02d}] ✗ 缺失: {fn}'); print(); continue
    fm, heads, nums, blen = digest(p)
    print('=' * 76)
    print(f'[{i:02d}] {fn}')
    print(f'  字数 {blen}  media_id={fm.get("media_id","?")[:40]}')
    print(f'  extracted={fm.get("extracted","?")}  method={fm.get("extract_method","?")}')
    if heads:
        print(f'  结构 ({len(heads)}): ' + ' | '.join(h.strip()[:26] for h in heads[:14]))
    if nums:
        print(f'  含参行 ({len(nums)}):')
        for x in nums[:10]:
            print(f'     · {x}')
    print()