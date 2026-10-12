# -*- coding: utf-8 -*-
"""MOC（Map of Content）导航层生成器 —— 幂等，可反复运行。

2026-09-30 v2（全量 9 域版）：
  域 MOC ×8（关键词/fm 归集）+ 书籍知识地图 ×1（按 book_title/parent_book/Ch 前缀归组）+ 00 总览。

规则（AGENTS §1 配套）：
- MOC 页是导航层，type: moc，不参与 status 治理；
- 全部由本脚本重建（覆盖式）；域成员按标题关键词或 frontmatter 归集，
  误收/漏收改 DOMAINS 表后重跑；
- 域成员只收知识页（concepts/entities/comparisons），仅书籍知识地图收 sources。

用法：python .tools/_rebuild_moc.py [--apply]   （默认 dry-run）
"""
import glob
import os
import re
import sys
from collections import Counter, defaultdict

VAULT = r'E:\WKB-OB'
MOC_DIR = os.path.join(VAULT, 'WIKI', 'MOC')
TODAY = '2026-09-30'
CORE_TOP_N = 15          # 域内核心页上限（按入链数）
ORPHAN_CAP = 120         # 孤儿列表上限，超出截断并注明

# ---- 域定义（命中顺序即优先级，先匹配的域收编） ----
DOMAINS = {
    'REL增强层与纤维': {
        'kw': ['rel', '增强层', '纤维', 'fiber', 'fibre', '皮芯', 'bicomponent',
               '双组分', '粘胶', 'viscose', 'rayon', 'lyocell', '纳米纤维素',
               'cellulose nan', '木浆', 'pulp', 'es纤维', '复合纤维', '短纤',
               'pp无纺布改性', '弹性纤维', 'elastane', 'spandex'],
        'adjacent': ['[[MOC - 无纺布工艺]]', '[[MOC - 芯体与吸收]]', '[[MOC - SAP与流体]]'],
    },
    '无纺布工艺': {
        'kw': ['无纺布', '非织造', 'nonwoven', '纺粘', 'spunbond', '熔喷', 'meltblown',
               'sms', '热风', 'through-air', '热轧', 'calender', '水刺', 'spunlace',
               '针刺', 'needle', '气铺', 'airlaid', '成网', 'web forming', '热粘合',
               'thermal bonding', '化学粘合', 'hydroentangl'],
        'adjacent': ['[[MOC - REL增强层与纤维]]', '[[MOC - 表面处理与胶黏剂]]'],
    },
    '变色与智能材料': {
        'kw': ['变色', 'chromic', 'chromism', 'pcm', '相变', 'phase change', '温敏',
               '湿敏', '光敏', 'thermochromic', 'photochromic', 'hydrochromic',
               'mechanochromic', 'stimuli', 'stimulus', 'smart polymer',
               'pnipaam', 'lcst', '形状记忆', '响应聚合物', '智能响应',
               '指示', 'indicator', '油墨', 'ink', '液晶', 'liquid crystal',
               '光子晶体', 'photonic', '结构色', 'structural color', '荧光',
               'fluoresc', '发光', 'luminesc', 'aie', '染料', 'dye', '颜料', 'pigment'],
        'adjacent': ['[[MOC - REL增强层与纤维]]', '[[MOC - SAP与流体]]', '[[MOC - 测试与标准]]'],
    },
    '法规与合规': {
        'kw': ['gb ', 'gb/', 'gb-t', 'gb‑t', '法规', 'regulation', '认证', 'certification',
               'reach', 'oeko', 'bluesign', 'ifra', 'codex', 'sccs', '合规', 'compliance',
               '限值', '宣称', 'claim', 'fda', '欧盟', '标签', 'label'],
        'adjacent': ['[[MOC - 测试与标准]]', '[[MOC - 实体与供应链]]'],
    },
    '功能添加剂与整理': {
        'kw': ['除臭', 'odor', 'odour', '抗菌', 'antibacterial', 'antimicrobial',
               '防腐', 'preservative', '保湿', 'humectant', '添加剂', 'additive',
               '母粒', 'masterbatch', '活性炭', 'zeolite', '沸石', '香精', 'fragrance',
               '壳聚糖', 'chitosan', '微胶囊', 'microencapsul', '表面活性剂', 'surfactant',
               '胶束', 'micelle', '乳化'],
        'adjacent': ['[[MOC - 表面处理与胶黏剂]]', '[[MOC - 法规与合规]]'],
    },
    '基础理论与模型': {
        'kw': ['定律', 'law\'', 'law ', 'equation', '方程', '理论', 'theory', '变换',
               'transform', '函数', 'function', '有限差分', '有限元', '有限体积',
               'cfd', '数值模拟', 'numerical', 'simulation', '仿真', '流变', 'rheolog',
               '力学', 'mechanics', '格林函数', 'green\'s', 'stokes', 'navier',
               'boltzmann', 'bessel', 'flory', 'donnan', 'wenzel', 'cassie',
               'washburn', 'young\'', 'wilhelmy', 'freundlich', 'stefan', 'marangoni',
               'poiseuille', 'laplace', 'fick', 'hagen'],
        'adjacent': ['[[MOC - SAP与流体]]', '[[MOC - 书籍知识地图]]'],
    },
    '测试与标准': {
        'kw': ['测试', 'test', 'astm', 'iso', '标准', 'standard', '模拟液',
               'simulant', '表征', 'characteriz', '可靠性', 'reliability', 'sop'],
        'adjacent': ['[[MOC - 书籍知识地图]]', '[[MOC - 芯体与吸收]]'],
    },
    '芯体与吸收': {
        'kw': ['芯体', 'core', 'coco', 'adl', '导流', 'acquisition', 'topsheet',
               'backsheet', '底膜', '面层', '回渗', 'rewet', '穿透', 'strikethrough',
               '吸收芯', '纸尿裤', '尿裤', 'diaper', 'pant', '渗漏', 'leak',
               '分区密度', 'zoning', '腰围', 'waist', '橡筋', 'elastic', '护挡',
               '阻漏', 'gasket', '层压', 'lamination', '防漏', '分布层',
               'retention', '保留层', 'pant'],
        'adjacent': ['[[MOC - REL增强层与纤维]]', '[[MOC - SAP与流体]]', '[[MOC - 无纺布工艺]]'],
    },
    'SAP与流体': {
        'kw': ['sap', '高吸水', 'superabsorb', '流动', 'flow', 'porous', '多孔',
               '毛细', 'capillar', 'wicking', '扩散', 'diffus', 'darcy',
               '渗透', 'permeab', 'permeat', 'hornification', '干燥', 'drying',
               '孔隙', 'porosity', '吸附', 'adsorption', '溶胀', 'swell', '凝胶', 'gel',
               '水凝胶', 'hydrogel'],
        'adjacent': ['[[MOC - 芯体与吸收]]', '[[MOC - 变色与智能材料]]', '[[MOC - 基础理论与模型]]'],
    },
    '表面处理与胶黏剂': {
        'kw': ['等离子', 'plasma', '电晕', 'corona', '亲水', 'hydrophilic', '润湿',
               'wetting', '表面能', 'surface energy', '接触角', 'contact angle',
               '胶黏', '胶粘', 'adhes', 'glue', '施胶', '上胶', 'coating', '涂层',
               '憎水', '疏水', 'hydrophob', 'latex', '胶乳', '压敏', 'psa',
               '聚氨酯', 'polyurethane', '水性 pu', '离型'],
        'adjacent': ['[[MOC - 无纺布工艺]]', '[[MOC - REL增强层与纤维]]', '[[MOC - 功能添加剂与整理]]'],
    },
    '实体与供应链': {
        'fm_cat': ['供应商', 'supplier', '浆厂', '竞品', '机构', '项目', '技术主体',
                   '待核', '大学', 'research'],   # 按 frontmatter category 归集（实体页）
        'kw': [],
        'adjacent': ['[[MOC - 书籍知识地图]]', '[[MOC - 法规与合规]]'],
    },
}


def load_pages():
    """返回 [(dir, title, fm_text, body)]，排除 merged 指针页。"""
    pages = []
    for d in ('concepts', 'entities', 'comparisons', 'sources'):
        for f in glob.glob(os.path.join(VAULT, 'WIKI', d, '*.md')):
            t = open(f, encoding='utf-8', errors='ignore').read()
            if re.search(r'^status:\s*merged', t[:600], re.M):
                continue
            parts = re.split(r'^---\s*$', t, maxsplit=2, flags=re.M)
            fm = parts[1] if len(parts) == 3 else ''
            body = parts[2] if len(parts) == 3 else t
            pages.append((d, os.path.basename(f)[:-3], fm, body))
    return pages


def link_graph(pages):
    names = {t for _, t, _, _ in pages}
    inlink = Counter()
    for _, title, _, body in pages:
        links = set()
        for x in re.findall(r'\[\[([^\]]+)\]\]', body):
            # Obsidian 解析：取 | 别名与 # 锚之前的部分；标题本身可含全角括号，勿截断
            l = x.split('|')[0].split('#')[0].strip()
            l = l[:-3] if l.endswith('.md') else l
            if l in names and l != title:
                links.add(l)
        for l in links:
            inlink[l] += 1
    return inlink


def classify(pages):
    """每页归入第一个命中的域。返回 {title: domain}。"""
    assign = {}
    for dom, cfg in DOMAINS.items():
        kws = cfg.get('kw', [])
        cats = cfg.get('fm_cat', [])
        for _, title, fm, _ in pages:
            if title in assign:
                continue
            hay = title.lower()
            hit = any(k.lower() in hay for k in kws)
            if not hit and cats:
                m = re.search(r'^category:\s*(.+)$', fm, re.M)
                cat = m.group(1).strip().lower() if m else ''
                hit = any(c.lower() in cat for c in cats)
            if not hit:
                m = re.search(r'^domain:\s*(.+)$', fm, re.M)
                dm = m.group(1).strip().lower() if m else ''
                hit = any(k.lower() in dm for k in kws)
            if hit:
                assign[title] = dom
    return assign


def book_key(title, fm):
    """书籍源页归组键：book_title > parent_book > Ch 前缀 > 独立书名。"""
    m = re.search(r'^book_title:\s*"?(.+?)"?\s*$', fm, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r'^parent_book:\s*"?\[\[(.+?)\]\]"?', fm, re.M)
    if m:
        return m.group(1).strip()
    m = re.match(r'^(.*?)\s+Ch\s*\d+', title)
    if m and m.group(1):
        return m.group(1).strip()
    return title   # 独立书 / 无章号：以自身为组


def merge_book_keys(keys):
    """同书双名合并：键名互为包含时归入较长者（Industrial Drying → Handbook of Industrial Drying）。"""
    ks = sorted(keys, key=len, reverse=True)
    remap = {}
    for i, a in enumerate(ks):
        for b in ks[i + 1:]:
            if b.lower() in a.lower():
                remap[b] = a
    return {k: remap.get(k, k) for k in keys}


def chapter_sort_key(title):
    m = re.search(r'Ch\s*(\d+)', title)
    return int(m.group(1)) if m else 999


def book_moc_page(all_pages, inlink):
    """书籍知识地图：sources 中 source_type 含 book/book-index 的页按书归组。"""
    books = defaultdict(list)
    for d, title, fm, _ in all_pages:
        if d != 'sources':
            continue
        if not re.search(r'^source_type:\s*.*?(book|book-index)', fm, re.M):
            continue
        books[book_key(title, fm)].append(title)
    remap = merge_book_keys(list(books))
    merged = defaultdict(list)
    for k, v in books.items():
        merged[remap[k]].extend(v)
    lines = []
    lines.append('---')
    lines.append('type: moc')
    lines.append('domain: 书籍知识地图')
    lines.append('updated: %s' % TODAY)
    lines.append('maintainer: AI（.tools/_rebuild_moc.py 重建）')
    lines.append('---')
    lines.append('')
    lines.append('# MOC · 书籍知识地图')
    lines.append('')
    lines.append('> %d 本书的 %d 页源摘要/章节入口，按书归组'
                 '（组键优先级：book_title > parent_book > 标题 Ch 前缀 > 独立书名；'
                 '同书双名已按包含关系合并）。' % (len(merged), sum(len(v) for v in merged.values())))
    lines.append('')
    for bk in sorted(merged, key=lambda k: -len(merged[k])):
        chs = sorted(merged[bk], key=chapter_sort_key)
        lines.append('## %s（%d 页）' % (bk, len(chs)))
        lines.append('')
        for t in chs:
            mark = '（入链 %d）' % inlink[t] if inlink[t] >= 10 else ''
            lines.append('- [[%s]]%s' % (t, mark))
        lines.append('')
    return '\n'.join(lines)


def moc_page(dom, members, inlink, orphans_all):
    cfg = DOMAINS[dom]
    core = sorted([t for t in members if inlink[t] > 0],
                  key=lambda t: -inlink[t])[:CORE_TOP_N]
    orphans = sorted(orphans_all)
    trunc = ''
    if len(orphans) > ORPHAN_CAP:
        orphans = orphans[:ORPHAN_CAP]
        trunc = '\n\n> 截断：另有 %d 页孤儿未列出，扩容时调高 ORPHAN_CAP 或拆分本域。' % (
            len([t for t in members if inlink[t] == 0]) - ORPHAN_CAP)
    lines = []
    lines.append('---')
    lines.append('type: moc')
    lines.append('domain: %s' % dom)
    lines.append('updated: %s' % TODAY)
    lines.append('maintainer: AI（.tools/_rebuild_moc.py 重建，人工微调请先备份）')
    lines.append('---')
    lines.append('')
    lines.append('# MOC · %s' % dom)
    lines.append('')
    lines.append('> 导航页（2026-09-30 v2）。域成员按标题关键词/frontmatter 自动归集，'
                 '误收/漏收改 `_rebuild_moc.py` 的 DOMAINS 表后重跑即可。')
    lines.append('')
    lines.append('## 核心页（按入链数排序）')
    lines.append('')
    if core:
        for t in core:
            lines.append('- [[%s]]（入链 %d）' % (t, inlink[t]))
    else:
        lines.append('-（暂无有入链成员）')
    lines.append('')
    lines.append('## 孤儿页入口（零入链，共 %d 页）' % len([t for t in members if inlink[t] == 0]))
    lines.append('')
    for t in orphans:
        lines.append('- [[%s]]' % t)
    lines.append(trunc)
    lines.append('')
    lines.append('## 相邻 MOC')
    lines.append('')
    for a in cfg['adjacent']:
        lines.append('- %s' % a)
    lines.append('')
    return '\n'.join(lines)


def home_moc(domain_counts, total, orphan_total, unassigned):
    n_domains = len(domain_counts)
    lines = []
    lines.append('---')
    lines.append('type: moc')
    lines.append('domain: 总览')
    lines.append('updated: %s' % TODAY)
    lines.append('maintainer: AI（.tools/_rebuild_moc.py 重建）')
    lines.append('---')
    lines.append('')
    lines.append('# WKB-OB 总览 MOC（知识地图首页）')
    lines.append('')
    lines.append('> 全库 %d 页（孤儿 %d，%.0f%%）。本页是导航入口；'
                 '机械清单见 [[index]]，操作账目见 [[log]]。' % (
                     total, orphan_total, 100.0 * orphan_total / total if total else 0))
    lines.append('')
    lines.append('## 域 MOC（%d 域，2026-09-30 v2）' % n_domains)
    lines.append('')
    for dom, (n, o) in domain_counts.items():
        lines.append('- [[MOC - %s]]（成员 %d 页%s）' % (
            dom, n, '，含孤儿 %d' % o if o else ''))
    lines.append('')
    lines.append('## 使用说明')
    lines.append('')
    lines.append('- 找主题 → 先进对应域 MOC，再从核心页/成员链接进入')
    lines.append('- 域成员按标题关键词自动归集，误收/漏收改 `.tools/_rebuild_moc.py` DOMAINS 表重跑')
    lines.append('- 精确清单（全量平表）见 [[index]]；两页职责：MOC 管「怎么逛」，index 管「有没有」')
    lines.append('- 未归域知识页 %d 页（零散化学/物理/工程条目，不硬凑域，直接查 index）' % unassigned)
    lines.append('')
    return '\n'.join(lines)


def main(apply=False):
    os.chdir(VAULT)
    all_pages = load_pages()
    inlink = link_graph(all_pages)
    kpages = [p for p in all_pages if p[0] != 'sources']
    assign = classify(kpages)
    total = len(all_pages)
    orphan_total = sum(1 for _, t, _, _ in all_pages if inlink[t] == 0)

    domain_counts = {}
    outputs = {}
    for dom in DOMAINS:
        members = [t for _, t, _, _ in kpages if assign.get(t) == dom]
        orphans_all = [t for t in members if inlink[t] == 0]
        domain_counts[dom] = (len(members), len(orphans_all))
        outputs['MOC - %s.md' % dom] = moc_page(dom, members, inlink, orphans_all)
    # 书籍知识地图（唯一收 sources 的域）
    book_members = [t for d, t, fm, _ in all_pages
                    if d == 'sources' and re.search(r'^source_type:\s*.*?(book|book-index)', fm, re.M)]
    domain_counts['书籍知识地图'] = (len(book_members), 0)
    outputs['MOC - 书籍知识地图.md'] = book_moc_page(all_pages, inlink)
    # 未归域只按知识页计（书籍域是 sources，不能从知识页池里扣）
    kw_assigned = sum(n for d, (n, _) in domain_counts.items() if d != '书籍知识地图')
    outputs['00 总览 MOC.md'] = home_moc(domain_counts, total, orphan_total,
                                        len(kpages) - kw_assigned)

    print('非指针页 %d，孤儿 %d（%.0f%%）' % (total, orphan_total, 100.0 * orphan_total / total))
    for dom, (n, o) in domain_counts.items():
        print('  域 [%s]：成员 %d（孤儿 %d）' % (dom, n, o))
    print('  未归域知识页：%d' % (len(kpages) - kw_assigned))

    if not apply:
        print('[dry-run] 未写入。加 --apply 落盘。')
        return
    os.makedirs(MOC_DIR, exist_ok=True)
    for fn, content in outputs.items():
        open(os.path.join(MOC_DIR, fn), 'w', encoding='utf-8').write(content)
        print('写入:', fn, '(%d 行)' % content.count('\n'))
    # 清理改名前的旧域 MOC 文件（如 供应商与供应链 → 实体与供应链）
    for f in glob.glob(os.path.join(MOC_DIR, 'MOC - *.md')):
        if os.path.basename(f) not in outputs:
            os.remove(f)
            print('清理旧文件:', os.path.basename(f))


if __name__ == '__main__':
    main(apply='--apply' in sys.argv)
