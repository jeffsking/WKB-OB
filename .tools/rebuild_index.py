# -*- coding: utf-8 -*-
"""重建 index.md 的「一~四区」表格与头部统计（保留「五、六」原文）。

为什么需要：编译批次达 79 个、页面数上百，手写索引必然滞后/漏收。
本脚本以 WIKI 实际文件为唯一事实来源重生成索引，可反复运行（幂等）。

用法：python .tools/rebuild_index.py
"""
import glob
import os
import re
from collections import Counter

VAULT = r'E:\WKB-OB'
KEEP_FROM = '## 五、'


def parse_front_matter(t):
    """返回 (fm_dict, body)。只处理简单的 key: value / key: [..] / 多行列表。"""
    if not t.startswith('---'):
        return {}, t
    parts = t.split('\n---', 1)
    if len(parts) != 2:
        return {}, t
    raw, body = parts[0][3:], parts[1].lstrip('-\n')
    fm, cur = {}, None
    for line in raw.split('\n'):
        if not line.strip():
            continue
        m = re.match(r'^([A-Za-z_]+):\s*(.*)$', line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith('[') and v.endswith(']'):
                inner = v[1:-1]
                q = re.findall(r'"([^"]*)"', inner) or re.findall(r"'([^']*)'", inner)
                if q:   # 引号感知：引号内的逗号不是分隔符
                    fm[k] = [x.strip() for x in q if x.strip()]
                else:
                    fm[k] = [x.strip().strip('"\'') for x in inner.split(',') if x.strip()]
            elif v == '':
                fm[k] = []
                cur = k
            else:
                fm[k] = v.strip('"\'')
                cur = None
        elif line.strip().startswith('- ') and cur:
            fm[cur].append(line.strip()[2:].strip().strip('"\''))
    return fm, body


def summary(body, n=72):
    """取正文第一段可用文本作一句话概要。"""
    for line in body.split('\n'):
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('>') or s.startswith('|') or s.startswith('-'):
            continue
        s = re.sub(r'\[\[([^\]|]+)(\|[^\]]+)?\]\]', r'\1', s)
        s = re.sub(r'[*`]', '', s)
        return s[:n] + ('…' if len(s) > n else '')
    return ''


def cell(v, default='—'):
    if v is None or v == '':
        return default
    if isinstance(v, list):
        return '、'.join(v) if v else default
    return str(v)


def main():
    os.chdir(VAULT)
    pages = {'sources': [], 'concepts': [], 'entities': [], 'comparisons': [], 'MOC': []}
    for sub in pages:
        for f in glob.glob('WIKI/%s/*.md' % sub):
            t = open(f, encoding='utf-8', errors='ignore').read()
            fm, body = parse_front_matter(t)
            title = os.path.basename(f)[:-3]   # 链接文本一律用文件名（Obsidian 按 basename 解析）
            pages[sub].append({'file': os.path.basename(f), 'fm': fm, 'title': title,
                               'sum': summary(body)})
        pages[sub].sort(key=lambda x: x['title'])

    n = {k: len(v) for k, v in pages.items()}
    total = sum(n.values())

    out = []
    out.append('---')
    out.append('type: index')
    out.append('title: "WKB-OB 知识库目录索引"')
    out.append('updated: 2026-09-29')
    out.append('maintainer: AI（WorkBuddy，依 AGENTS.md 自动维护）')
    out.append('---')
    out.append('')
    out.append('# WKB-OB 知识库目录索引')
    out.append('')
    out.append('> 本文件由 AI 依《AGENTS.md》§3.5 自动维护（脚本 `.tools/rebuild_index.py`，可反复运行）。')
    out.append('> 查询时**先读本索引定位页面，再加载具体页面**，回答须附来源（页面名 + 其 source_path）。')
    out.append('> 本库结构：`raw/`（原始资料，AI 只读）→ `wiki/`（编译知识层，AI 读写）→ 本索引 + `log.md`（操作日志）。')
    out.append('')
    out.append('**当前规模：** %d 页 Wiki（源摘要 %d / 概念 %d / 实体 %d / 对比 %d / MOC %d）'
               % (total, n['sources'], n['concepts'], n['entities'], n['comparisons'], n['MOC']))
    out.append('**语言规范：** WIKI 页面自 2026-09-29 起为**英文为主 + 中文对照**（AGENTS.md §2.0）；'
               '此前产出的中文页不强制回溯，编辑时逐步补齐。')
    out.append('**raw 盘存：** `RAW/` 1718 份 .md（**唯一事实锚点与判重锚**，2026-09-30 起 source_path 全库统一指 RAW/）；'
               '`RAW_FULL/` 为已回填正文的镜像（与 RAW 路径 1:1，**仅作编译输入，不作判重锚**）。'
               '待编译积压见 `.tools/_compile_backlog.json`（2026-09-30 按统一锚重建）。')
    out.append('**最后编译：** 2026-09-30（P0 书目收官 + 判重锚统一，进度见 [[log]]）')
    out.append('')
    out.append('---')
    out.append('')

    # 一、源摘要页
    out.append('## 一、源摘要页 `WIKI/sources/`')
    out.append('')
    out.append('> 每份 raw 资料对应一页，是连接 Raw 层与 Wiki 层的桥（`source_path` 为唯一判重锚）。')
    out.append('')
    out.append('| 页面 | 类型 | 发布日期 | 可信度 | 源路径 | 状态 |')
    out.append('|---|---|---|---|---|---|')
    for p in pages['sources']:
        fm = p['fm']
        sp = cell(fm.get('source_path')).replace('\\', '/')
        out.append('| [[%s]] | %s | %s | %s | `%s` | %s |' % (
            p['title'], cell(fm.get('source_type')), cell(fm.get('date_published')),
            cell(fm.get('credibility')), sp, cell(fm.get('knowledge_update_status'))))
    out.append('')

    # 二、概念页
    out.append('## 二、概念页 `WIKI/concepts/`')
    out.append('')
    out.append('> 技术或商业的理论、方法、术语、机理。')
    out.append('')
    out.append('| 页面 | 领域 | 成熟度 | 一句话概要 |')
    out.append('|---|---|---|---|')
    for p in pages['concepts']:
        fm = p['fm']
        out.append('| [[%s]] | %s | %s | %s |' % (
            p['title'], cell(fm.get('domain')), cell(fm.get('status')), p['sum']))
    out.append('')

    # 三、实体页
    out.append('## 三、实体页 `WIKI/entities/`')
    out.append('')
    out.append('> 具体的人、公司、机构、产品、技术平台。')
    out.append('')
    out.append('| 页面 | 类别 | 关系 | 一句话概要 |')
    out.append('|---|---|---|---|')
    for p in pages['entities']:
        fm = p['fm']
        out.append('| [[%s]] | %s | %s | %s |' % (
            p['title'], cell(fm.get('category')), cell(fm.get('relationship')), p['sum']))
    out.append('')

    # 四、对比页
    out.append('## 四、对比页 `WIKI/comparisons/`')
    out.append('')
    out.append('> 两个及以上相似对象的系统性比较（表格必含「成本」「供应链风险」两列）。')
    out.append('')
    out.append('| 页面 | 维度 | 对象 | 一句话概要 |')
    out.append('|---|---|---|---|')
    for p in pages['comparisons']:
        fm = p['fm']
        out.append('| [[%s]] | %s | %s | %s |' % (
            p['title'], cell(fm.get('dimension')), cell(fm.get('subjects')), p['sum']))
    out.append('')
    # MOC 导航层（type: moc，不参与 status 治理）
    out.append('## 导航层 `WIKI/MOC/`')
    out.append('')
    out.append('> Map of Content 导航页（`type: moc`，不参与 status 治理；由 `.tools/_rebuild_moc.py` 幂等重建）。')
    out.append('')
    out.append('| 页面 | 域 | 更新时间 |')
    out.append('|---|---|---|')
    for p in pages['MOC']:
        fm = p['fm']
        out.append('| [[%s]] | %s | %s |' % (p['title'], cell(fm.get('domain')), cell(fm.get('updated'))))
    out.append('')
    out.append('---')
    out.append('')

    # 保留 五、六
    old = open('index.md', encoding='utf-8').read()
    idx = old.find(KEEP_FROM)
    if idx < 0:
        raise SystemExit('!! 未找到「%s」，中止以免丢失原内容' % KEEP_FROM)
    tail = old[idx:]
    # 刷新 五 里的 manual_review 积压提示（仅替换计数行）
    receipts = glob.glob('.tools/compile_batches/_done/*.json')
    mr_total = 0
    for r in receipts:
        try:
            import json
            mr_total += len(json.load(open(r, encoding='utf-8')).get('manual_review', []))
        except Exception:
            pass
    tail = re.sub(r'> 当前 manual_review 积压 \*\*\d+ 条\*\*[^\n]*',
                  '> 当前 manual_review 积压见本表（历史 9 条 + 本轮批次新增，'
                  '回执明细在 `.tools/compile_batches/_done/`）。依 AGENTS.md §5 已超 5 条阈值，**须集中处理**。',
                  tail)

    open('index.md', 'w', encoding='utf-8').write('\n'.join(out) + tail)
    print('index.md 已重建：%d 页（源摘要 %d / 概念 %d / 实体 %d / 对比 %d / MOC %d）'
          % (total, n['sources'], n['concepts'], n['entities'], n['comparisons'], n['MOC']))
    print('回执 manual_review 合计: %d 条' % mr_total)


if __name__ == '__main__':
    main()
