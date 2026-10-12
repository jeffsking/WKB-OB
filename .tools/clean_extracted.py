# -*- coding: utf-8 -*-
"""
RAW_FULL 提取产物清洗 v2（幂等 / 信息零丢失）
规则：
  R1 图片死链降级   ![alt](非http路径) -> [图片: alt] / [图片]
  R2 重复数据串压缩  (数字串重复≥10次且总长≥40 token) -> [重复数据串: <seq> ×N]
原路径写入 .tools/_image_stripped.json，压缩串写入 .tools/_repeat_collapsed.json 供追溯。

不做：HTML 实体解码（渲染器兼容，解码有风险）、标题层级还原（属推断）。
幂等：front matter 的 clean_rules 含 'v2' 则跳过。
"""
import os, re, json, glob

CLEAN_VER = 'v2'
RULES_DESC = 'v2: dead-image-link->text(alt kept); repeat-digits->compressed'

IMG_RE = re.compile(r'!\[([\s\S]*?)\]\((?!https?://)([^)]*)\)')
REP_RE = re.compile(r'((?:\d{1,3})(?:\s+\d{1,3}){0,3})(?:\s+\1){9,}')

stripped, collapsed = [], []
n_files = n_img = n_rep = 0

for p in sorted(glob.glob('RAW_FULL/**/*.md', recursive=True)):
    t = open(p, encoding='utf-8', errors='replace').read()
    # 精确判幂等：只看 clean_rules 字段自身的值（避免正文里的 'v2' 误触发）
    cr = re.search(r'^clean_rules:\s*"?([^"\r\n]*)', t, re.M)
    if cr and CLEAN_VER in cr.group(1):
        continue                                    # 已是最新版本
    m = re.match(r'^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$', t)
    if not m:
        continue
    fm, body = m.group(1), m.group(2)

    def repl_img(mo):
        global n_img
        alt = mo.group(1).replace('\\n', ' ').replace('\\t', ' ')
        alt = ' '.join(alt.split())
        stripped.append({'file': p.replace('\\', '/'), 'path': mo.group(2), 'alt': alt})
        n_img += 1
        return ('[图片: %s]' % alt) if alt else '[图片]'

    def repl_rep(mo):
        global n_rep
        seq = ' '.join(mo.group(1).split())
        total = len(mo.group(0).split())
        if total < 40:
            return mo.group(0)                      # 太短，可能是真数据，保留
        n_rep += 1
        collapsed.append({'file': p.replace('\\', '/'), 'token': seq,
                          'count': total // max(1, len(seq.split()))})
        return '[重复数据串: %s ×%d]' % (seq, total // len(seq.split()))

    body = IMG_RE.sub(repl_img, body)
    body = REP_RE.sub(repl_rep, body)
    body = re.sub(r'\n{3,}', '\n\n', body)

    fm = re.sub(r'^(clean_rules|processed):.*\r?\n?', '', fm, flags=re.M).rstrip('\n')
    fm += '\nclean_rules: "%s"\nprocessed: "2026-09-27"' % RULES_DESC

    open(p, 'w', encoding='utf-8', newline='\n').write('---\n%s\n---\n%s' % (fm, body))
    n_files += 1

json.dump(stripped, open('.tools/_image_stripped.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(collapsed, open('.tools/_repeat_collapsed.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

print('=== 清洗 v2 完成 ===')
print('处理文件    :', n_files)
print('R1 降级死链 :', n_img)
print('R2 压缩重复 :', n_rep)
print()
if collapsed:
    print('=== 压缩明细 ===')
    for c in collapsed:
        print('  %-52s %s ×%d' % (os.path.basename(c['file'])[:50], c['token'], c['count']))
