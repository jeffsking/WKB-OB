# -*- coding: utf-8 -*-
"""重构 concept 的 domain 分类（2026-10-12）。

问题：528 个 concept 分属 133 个 domain 变体（`hygiene-materials` 一档 261 页、大量一页一 domain）
      → 分类等于没做。

方案：**复用 MOC 的 11 域体系**（`.tools/_rebuild_moc.py` 的 DOMAINS 关键词表），
     把 domain 统一重写为 `[卫材研发, <MOC域>]`；未命中者归 `[卫材研发, 待归类]`。

幂等：第二次运行应无改动。
安全：--apply 前全量备份 WIKI/concepts。

用法：
  python .tools/_rebuild_concept_domains_20261012.py            # dry-run
  python .tools/_rebuild_concept_domains_20261012.py --apply
"""
import glob
import json
import os
import re
import shutil
import sys
from collections import Counter

TOOLS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
from _rebuild_moc import DOMAINS  # noqa: E402  复用域定义

CONC = os.path.join(VAULT, 'WIKI', 'concepts')
BACKUP = os.path.join(VAULT, '.tools', '_concept_domain_backup_20261012')
FM_RE = re.compile(r'^---[ \t]*\n(.*?)\n---[ \t]*\n?', re.S)
TODAY = '2026-10-12'

# 域归类顺序（MOC DOMAINS 的插入序即优先级）；排除「实体与供应链」（属实体页）
DOM_ORDER = [d for d in DOMAINS if d != '实体与供应链']

# 重构前的原始 domain（语义档案，2026-10-12 生成于重构之前）→ 保证分类确定性
ORIG = json.load(open(os.path.join(VAULT, '.tools', '_concept_index_20261012.json'),
                      encoding='utf-8'))

# 人工裁定覆盖表（114 页逐条细分结果）→ **优先级最高**，防自动归类覆盖人工结论
_ASSIGN = os.path.join(VAULT, '.tools', '_unclassified_assign_20261012.json')
ASSIGN = json.load(open(_ASSIGN, encoding='utf-8')) if os.path.exists(_ASSIGN) else {}

# 旧二级域名 → MOC 域（关键词 → 域），用于 MOC 关键词未命中时的兜底
LEGACY_MAP = [
    ('芯体结构', '芯体与吸收'), ('芯体工艺', '芯体与吸收'), ('面层结构', '芯体与吸收'),
    ('面层', '芯体与吸收'), ('结构设计', '芯体与吸收'), ('结构件', '芯体与吸收'),
    ('吸收机理', '芯体与吸收'), ('摄入系统', '芯体与吸收'), ('导流机理', '芯体与吸收'),
    ('回渗', '芯体与吸收'), ('加工与转换工程', '芯体与吸收'), ('舒适性', '芯体与吸收'),
    ('透气与热舒适', '芯体与吸收'),
    ('测试与验收', '测试与标准'), ('测试方法与表征', '测试与标准'), ('测试方法', '测试与标准'),
    ('测试方法与合规', '测试与标准'),
    ('纤维材料', 'REL增强层与纤维'), ('材料', 'REL增强层与纤维'),
    ('材料科学', '基础理论与模型'), ('聚合物加工', '基础理论与模型'), ('材料加工', '基础理论与模型'),
    ('生物基材料', '基础理论与模型'), ('生物材料', '基础理论与模型'), ('阻隔性能', '基础理论与模型'),
    ('统计力学', '基础理论与模型'), ('知识组织', '基础理论与模型'), ('仿真建模', '基础理论与模型'),
    ('吸收仿真', '基础理论与模型'), ('AI4Science', '基础理论与模型'),
    ('无纺布', '无纺布工艺'), ('无纺布结构', '无纺布工艺'), ('无纺布工艺', '无纺布工艺'),
    ('非织造与纳米纤维', '无纺布工艺'), ('设备工程', '无纺布工艺'), ('工艺', '无纺布工艺'),
    ('智能功能化', '变色与智能材料'), ('比色传感', '变色与智能材料'), ('涂层工艺', '表面处理与胶黏剂'),
    ('SAP 机理', 'SAP与流体'), ('SAP', 'SAP与流体'), ('高吸水树脂', 'SAP与流体'),
    ('胶黏剂', '表面处理与胶黏剂'),
    ('限用物质', '法规与合规'), ('中国标准体系', '法规与合规'), ('化妆品合规', '法规与合规'),
    ('原料标准', '法规与合规'), ('卫品', '法规与合规'), ('材料安全与法规', '法规与合规'),
    ('香精合规', '法规与合规'), ('知识产权', '法规与合规'), ('材料安全', '法规与合规'),
    ('市场洞察', '实体与供应链'), ('立项治理', '实体与供应链'), ('产品档位与材料策略', '实体与供应链'),
    ('消费者研究', '实体与供应链'), ('开放创新', '实体与供应链'),
    ('功能材料', '功能添加剂与整理'), ('气味控制', '功能添加剂与整理'),
    ('异味控制', '功能添加剂与整理'), ('消臭', '功能添加剂与整理'), ('载体技术', '功能添加剂与整理'),
]


def classify(title, odom):
    """odom = **重构前的原始 domain**（来自语义档案），保证确定性/幂等。"""
    hay = title.lower()
    for dom in DOM_ORDER:
        cfg = DOMAINS[dom]
        if any(k.lower() in hay for k in cfg.get('kw', [])):
            return dom
    # 兜底：旧二级域名 → MOC 域
    for kw, dom in LEGACY_MAP:
        if kw in odom:
            return dom
    return '待归类'


def main():
    apply = '--apply' in sys.argv
    changes, dist = {}, Counter()
    files = glob.glob(os.path.join(CONC, '*.md'))
    for f in files:
        name = os.path.basename(f)[:-3]
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        if not m:
            continue
        fm = m.group(1)
        if re.search(r'^status:[ \t]*merged', fm, re.M):
            dist['(merged 指针页·跳过)'] += 1
            continue
        # 人工裁定优先（防自动归类覆盖人工细分结论）
        dom = ASSIGN.get(name) or classify(name, ORIG.get(name, {}).get('domain', ''))
        dist[dom] += 1
        new_dom = '[卫材研发, %s]' % dom if dom != '待归类' else '[卫材研发, 待归类]'
        om = re.search(r'^domain:[ \t]*(.*)$', fm, re.M)
        old_dom = om.group(1).strip() if om else ''
        if old_dom != new_dom:
            changes[name] = (old_dom, new_dom)

    print('concept 总页数: %d' % len(files))
    print('需要改 domain: %d' % len(changes))
    print()
    print('=== 归类分布（新体系）===')
    for k, v in dist.most_common():
        print('  %-24s %d' % (k, v))
    print()

    if not apply:
        print('(dry-run; 加 --apply 执行)')
        for n in list(changes)[:8]:
            print('  %-46s %s -> %s' % (n[:46], changes[n][0][:28], changes[n][1]))
        return

    os.makedirs(BACKUP, exist_ok=True)
    for f in files:
        shutil.copy2(f, os.path.join(BACKUP, os.path.basename(f)))
    print('备份: %d 文件 -> %s' % (len(files), os.path.relpath(BACKUP, VAULT)))

    n = 0
    for f in files:
        name = os.path.basename(f)[:-3]
        if name not in changes:
            continue
        t = open(f, encoding='utf-8', errors='ignore').read()
        m = FM_RE.match(t)
        fm, body = m.group(1), t[m.end():]
        new_dom = changes[name][1]
        if re.search(r'^domain:', fm, re.M):
            fm2 = re.sub(r'^domain:[ \t]*.*$', 'domain: %s' % new_dom, fm, count=1, flags=re.M)
        else:
            fm2 = fm + '\ndomain: %s' % new_dom
        with open(f, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('---\n' + fm2 + '\n---\n' + body)
        n += 1
    print('已重写 domain: %d 页' % n)
    json.dump({k: list(v) for k, v in changes.items()},
              open(os.path.join(VAULT, '.tools', '_concept_domain_changes_20261012.json'),
                   'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
