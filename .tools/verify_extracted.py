# -*- coding: utf-8 -*-
"""核验 RAW_FULL 提取产物：落盘完整性 / front matter / 正文规模 / 噪声模式"""
import os, re, json, glob

def scan(base='RAW_FULL'):
    files = sorted(glob.glob(base + '/**/*.md', recursive=True))
    print('提取产物文件数:', len(files))
    if not files:
        return
    total = 0
    noise = {'leading_num': [], 'dup_title': [], 'html_entity': [], 'ima_img': [], 'empty': [], 'repeat_digits': []}
    rows = []
    for p in files:
        t = open(p, encoding='utf-8', errors='replace').read()
        total += len(t)
        m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)$', t, re.S)
        fm = m.group(1) if m else ''
        body = m.group(2) if m else t
        net = len(re.sub(r'\s', '', body))
        title = ''
        tm = re.search(r'^source_file:\s*"?([^"\r\n]+)"?', fm, re.M)
        if tm:
            title = tm.group(1).strip()
        # 噪声检测
        first = next((l.strip() for l in body.splitlines() if l.strip()), '')
        if re.fullmatch(r'\d{1,3}', first):
            noise['leading_num'].append((p, first))
        # 重复标题：body 里 H1 与 source_file 同名出现（可能重复 2 次）
        h1s = re.findall(r'^#\s+(.+)$', body, re.M)
        rest = h1s[1:]          # 跳过本工具注入的文档标题，只看原文标题层
        if len(rest) != len(set(rest)):
            noise['dup_title'].append((p, rest[:4]))
        for ent in ['&lt;', '&gt;', '&amp;', '&quot;', '&#']:
            if ent in body:
                noise['html_entity'].append((p, ent)); break
        if re.search(r'!\[[^\]]*\]\([^)]*ima[^)]*\)', body) or re.search(r'!\[[^\]]*\]\((?!https?://)[^)]*\)', body):
            noise['ima_img'].append(p)
        if net < 60:
            noise['empty'].append((p, net))
        # 超长重复数字串（PPT 图表 alt 的 OCR 噪声）
        best, tok = 0, ''
        for mo in re.finditer(r'(\d{1,3})(?:\s+\1){39,}', body):
            n = len(mo.group(0).split())
            if n > best:
                best, tok = n, mo.group(1)
        if best:
            noise['repeat_digits'].append((p, tok, best))
        rows.append((p, len(t), net, title))

    rows.sort(key=lambda r: -r[1])
    print('产物总字符:', total)
    print()
    print('=== 规模 Top 10 ===')
    for p, n, net, ti in rows[:10]:
        print('  %7d B  %-60s %s' % (n, os.path.basename(p)[:58], ''))
    print()
    print('=== 规模 Bottom 6（需人工确认是否有效）===')
    for p, n, net, ti in rows[-6:]:
        print('  %7d B  net=%5d  %s' % (n, net, os.path.basename(p)[:60]))
    print()
    print('=== 噪声统计 ===')
    for k, v in noise.items():
        print('  %-14s %d' % (k, len(v)))
    print()
    for k in ['leading_num', 'dup_title', 'html_entity', 'empty', 'repeat_digits']:
        if noise[k]:
            print('--- %s 明细 ---' % k)
            for item in noise[k][:8]:
                print('   ', item)
            print()

if __name__ == '__main__':
    scan()
