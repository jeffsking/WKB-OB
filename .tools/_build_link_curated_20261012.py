# -*- coding: utf-8 -*-
"""从三代断链修复脚本中「机械提取」白名单 → .tools/link_guard_curated.json

来源（用 ast 解析，禁止手工誊抄）：
  _fix_links_all.py  → CURATED / GROUPS / BLOCK
  final_link_fix.py  → REWRITE（value=None 者 = 占位符清理 → plain_text）
  _fixlinks_p0b02.py → FIX（键值带 [[ ]] 需剥离）

分类：
  redirects         同名变体改指（目标页须存在）
  groups            变体族 → canonical
  block             强制走 SEED（禁止自动改指，防上位→下位窄化）
  plain_text        占位符/行文链接 → 纯文本
  filename_sanitize 文件名安全化（含 / 的键或值）

用法：python .tools/_build_link_curated_20261012.py
"""
import ast
import json
import os
import re

TOOLS = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(TOOLS, 'link_guard_curated.json')


def load_assigns(fname, names):
    """用 ast 取模块级字面量赋值。"""
    src = open(os.path.join(TOOLS, fname), encoding='utf-8').read()
    tree = ast.parse(src)
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in names:
                    out[t.id] = ast.literal_eval(node.value)
    return out


def unwrap(s):
    """剥掉 [[ ]] 包裹。"""
    s = s.strip()
    if s.startswith('[[') and s.endswith(']]'):
        s = s[2:-2]
    return s


fa = load_assigns('_fix_links_all.py', {'CURATED', 'GROUPS', 'BLOCK'})
fl = load_assigns('final_link_fix.py', {'REWRITE'})
p0 = load_assigns('_fixlinks_p0b02.py', {'FIX'})

groups = fa.get('GROUPS', {})
block_lit = set(fa.get('BLOCK', set()))
# 复现行 90 的运算：group variants 从 BLOCK 移除（已由 GROUPS 处理）
vary = {v for vs in groups.values() for v in vs}
block = sorted(block_lit - vary)

redirects = {}
sanitize = {}
plain_text = {}

# 1) CURATED
for k, v in fa.get('CURATED', {}).items():
    redirects[k] = v
# 2) REWRITE
for k, v in fl.get('REWRITE', {}).items():
    if v is None:
        plain_text[k] = None
    else:
        redirects[k] = v
# 3) FIX（p0b02）
for k, v in p0.get('FIX', {}).items():
    redirects[unwrap(k)] = unwrap(v)

# 含 / 的键或值 → filename_sanitize
for k in list(redirects):
    if '/' in k or '/' in redirects[k]:
        sanitize[k] = redirects.pop(k)

# groups 的 canonical 若含 / 也归 sanitize（保守）
data = {
    '_warning': '本表非权威源，仅登记「同名变体」改指规则（同一对象的不同写法）；'
                '语义近似一律建 seed 页，禁止自动改指。目标页必须已存在才生效（guard 运行时会校验）。',
    'version': '2026-10-12',
    'extracted_from': ['_fix_links_all.py:CURATED/GROUPS/BLOCK',
                       'final_link_fix.py:REWRITE',
                       '_fixlinks_p0b02.py:FIX'],
    'redirects': dict(sorted(redirects.items())),
    'groups': {k: sorted(v) for k, v in sorted(groups.items())},
    'block': block,
    'plain_text': plain_text,
    'filename_sanitize': dict(sorted(sanitize.items())),
}

json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('提取完成 -> %s' % os.path.basename(OUT))
print('  redirects         : %d' % len(data['redirects']))
print('  groups            : %d 组（%d 变体）'
      % (len(data['groups']), sum(len(v) for v in data['groups'].values())))
print('  block             : %d' % len(data['block']))
print('  plain_text        : %d' % len(data['plain_text']))
print('  filename_sanitize : %d' % len(data['filename_sanitize']))
print('  —— 合计规则 %d 条' % (len(data['redirects']) + sum(len(v) for v in data['groups'].values())
                              + len(data['block']) + len(data['plain_text'])
                              + len(data['filename_sanitize'])))
