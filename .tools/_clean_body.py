# -*- coding: utf-8 -*-
"""把 MCP fetch_media_content 的 XML 原始返回清洗成纯 markdown 正文。
用法: python _clean_body.py <raw_file> <out_file>
"""
import html
import re
import sys


def strip_trailing_entity(s):
    s = html.unescape(html.unescape(s))
    for _ in range(3):
        s = s.replace('&#xA;', '\n').replace('&#x9;', '\t')
        s = html.unescape(s)
    s = re.sub(r'&amp;#x[0-9A-Fa-f]+;', '', s)
    return s


def parse_tags(s):
    """按引号感知方式扫描标签，返回 (tag, attrs, inner) 列表。"""
    out = []
    i = 0
    n = len(s)
    while i < n:
        lt = s.find('<', i)
        if lt < 0:
            break
        gt = s.find('>', lt)
        # 处理属性中含 '>' 的情况：扫描到引号闭合
        j = lt + 1
        in_q = None
        end = -1
        while j < n:
            c = s[j]
            if in_q:
                if c == in_q:
                    in_q = None
            elif c in '"\'':
                in_q = c
            elif c == '>':
                end = j
                break
            j += 1
        if end < 0:
            break
        tagtext = s[lt + 1:end]
        m = re.match(r'\s*([a-zA-Z0-9]+)', tagtext)
        if not m:
            i = end + 1
            continue
        tag = m.group(1).lower()
        attrs = tagtext[m.end():]
        # 找闭合标签
        close = '</%s>' % tag
        if tag in ('image', 'br', 'img'):
            out.append((tag, attrs, ''))
            i = end + 1
            continue
        cpos = s.find(close, end + 1)
        if cpos < 0:
            i = end + 1
            continue
        inner = s[end + 1:cpos]
        out.append((tag, attrs, inner))
        i = cpos + len(close)
    return out


IMG_HEADER_IDS = ('#activity-name', '#js_name', '#publish_time',
                  '#js_ip_wording', '#js_author_name')


def clean(raw: str) -> str:
    s = raw
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    m = re.search(r'<body[^>]*>(.*)</body>', s, re.S)
    if m:
        s = m.group(1)
    tags = parse_tags(s)
    lines = []
    for tag, attrs, inner in tags:
        if '#activity-name' in (attrs or ''):
            # 文章标题，apply 会自动加 # 标题，跳过避免重复
            continue
        if tag == 'image':
            am = re.search(r'alt="(.*?)"\s*$', attrs, re.S)
            alt = am.group(1) if am else ''
            alt = strip_trailing_entity(alt).strip()
            if alt:
                lines += ['', '> [图片] ' + alt, '']
            continue
        txt = strip_trailing_entity(inner).strip()
        if not txt:
            continue
        if tag == 'h':
            lines += ['', '## ' + txt, '']
        else:
            lines += [txt, '']
    out = '\n'.join(lines)
    out = strip_trailing_entity(out)
    # 丢弃"标题/作者/发布时间/发布地点"这类头部行
    drop_prefixes = ('作者:', '发布时间:', '发布地点:', '作者：', '发布时间：',
                     '发布地点：', '原文来源', '关注我们', '点击上方')
    kept = []
    for ln in out.split('\n'):
        st = ln.strip()
        if st.startswith('## ') and st[3:].strip() in ('',):
            continue
        if any(st.startswith(p) for p in drop_prefixes):
            continue
        if st == '%!s(MISSING)':
            continue
        kept.append(ln)
    out = '\n'.join(kept)
    out = re.sub(r'\n{3,}', '\n\n', out)
    return out.strip() + '\n'


def main():
    raw = open(sys.argv[1], encoding='utf-8').read()
    open(sys.argv[2], 'w', encoding='utf-8').write(clean(raw))


if __name__ == '__main__':
    main()
