# -*- coding: utf-8 -*-
"""优先 SEED 的语义去重probe（2026-10-12）。

对引用≥2 的 SEED 目标，在 concepts+entities 库中做两路检索：
  ① 页名含关键词
  ② 正文命中关键词（计数）
输出候选 + 引用来源，供人工判断「改指到既有页」还是「建页」。

只读，不改任何文件。
"""
import glob
import json
import os
import re

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = (glob.glob(os.path.join(VAULT, 'WIKI', 'concepts', '*.md'))
         + glob.glob(os.path.join(VAULT, 'WIKI', 'entities', '*.md')))

KW = {
    'Pinhole 开孔': r'打孔|开孔|perforat|aperture|pinhole|网面|凹凸',
    '三叶草截面纤维': r'三叶|trilobal',
    'Daehyoon': r'Daehy|大炆',
    '微胶囊': r'微胶囊|microencapsul',
    '双组分纤维': r'双组分|bicomponent',
    '图片类条目': r'图片类',
    '温变材料': r'温变|热致变色|thermochrom|温度响应|温度敏感',
    '防漏结构': r'防漏|阻漏|gasket|leak|腿围|护挡',
    '绒毛浆': r'绒毛浆|fluff',
    '感光变色微胶囊': r'感光|光致变色|photochrom|光变',
    'Insilico': r'Insilico',
    '水致变色油墨': r'水致变色|hydrochrom|水变',
    '感温变色微胶囊': r'感温|温变微胶囊',
    'TBCW在线超声波复合工艺': r'超声波|ultrasonic|TBCW',
    '异形纤维': r'异形|截面纤维|profile fib|trilobal',
    '可弃式服装（P&G 专利族）': r'可弃式|disposabl|专利族',
    '热熔胶': r'热熔胶|hot ?melt',
    '底膜': r'底膜|backsheet',
    'ES纤维': r'ES ?纤维|ES ?fiber',
    '温变油墨': r'温变油墨|thermochromic ink|Chromicolor',
}


def main():
    d = json.load(open(os.path.join(VAULT, '.tools', 'link_guard_reports', '2026-10-12_plan.json'),
                       encoding='utf-8'))
    seed = d['seed']
    todo = [k for k, v in seed.items() if len(v) >= 2]
    cache = {}
    for f in FILES:
        cache[os.path.basename(f)[:-3]] = open(f, encoding='utf-8', errors='ignore').read()

    for key in sorted(todo, key=lambda k: -len(seed[k])):
        pat = KW.get(key)
        print('=' * 78)
        print('■ %s  (%d 处)' % (key, len(seed[key])))
        print('  引用自: %s' % '、'.join(sorted(seed[key])[:3]))
        if not pat:
            print('  (无关键词表，跳过)')
            continue
        by_name, by_body = [], []
        for name, body in cache.items():
            if re.search(pat, name, re.I):
                by_name.append(name)
            else:
                hits = len(re.findall(pat, body, re.I))
                if hits:
                    by_body.append((hits, name))
        by_body.sort(reverse=True)
        if by_name:
            print('  [页名命中]')
            for x in by_name[:10]:
                print('     ', x)
        for h, n in by_body[:6]:
            print('  [正文%s次] %s' % (h, n))


if __name__ == '__main__':
    main()
