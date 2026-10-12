#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""补齐 3 条 dedup 残余未编译：2 条抽取式编译 + 1 条 note stub。"""
import re
from datetime import date
from pathlib import Path

ROOT = Path('.')
WIKI_SRC = ROOT / 'WIKI/sources'
PAGE_HEAD = re.compile(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', re.S)
MAX_BODY = 6000

TARGETS = [
    # (raw_path, full_path, page_name, source_type, title)
    ("RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/README.md.md",
     "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Principles of Polymerization/README.md.md",
     "Principles of Polymerization README", "Book-Analysis", "Principles of Polymerization (README)"),
    ("RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Interactively mechanochromic electronic textile sensor.pdf.md",
     "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Interactively mechanochromic electronic textile sensor.pdf.md",
     "Interactively mechanochromic electronic textile sensor", "Smart-Materials",
     "Interactively mechanochromic electronic textile sensor"),
]


def today():
    return date.today().isoformat()


def fm(title, source_type, source_path):
    return "\n".join([
        "---", "type: source", f'title: "{title}"',
        f"source_type: {source_type}", f"source_path: {source_path}",
        'original_link: ""', f"date_published: {today()}",
        f"date_processed: {today()}", "credibility: 中",
        "key_claims: []", "pages_linked: []", "compile_mode: extractive", "---",
    ])


def main():
    WIKI_SRC.mkdir(parents=True, exist_ok=True)
    for raw, full, page_name, stype, title in TARGETS:
        fp = ROOT / full
        content = fp.read_text(encoding='utf-8', errors='replace')
        m = PAGE_HEAD.match(content)
        body_text = m.group(2) if m else content
        body_text = body_text.strip()
        trunc = False
        if len(body_text) > MAX_BODY:
            body_text = body_text[:MAX_BODY]
            trunc = True
        dest = WIKI_SRC / f"{page_name}.md"
        page = fm(title, stype, raw) + "\n\n" + "\n".join([
            f"# {title}", "", "## Positioning 定位", "",
            f"抽取式源摘要页（`source_type: {stype}`）。正文摘录自镜像层，未做语义改写。", "",
            "## Extracted Content 原文摘录", "", body_text,
            *(["", f"*（正文超过 {MAX_BODY} 字，此处截断）*"] if trunc else []),
            "", "## Original 原文", "",
            f"- 本地路径：`{raw}`", f"- 镜像正文：`{full}`",
        ]) + "\n"
        dest.write_text(page, encoding='utf-8')
        print("wrote", dest)

    # note stub
    note_raw = "RAW/ima_sync/notes/ima笔记使用指南.md"
    note_page = WIKI_SRC / "ima笔记使用指南.md"
    page = fm("ima笔记使用指南", "行业新闻", note_raw) + "\n\n" + "\n".join([
        "# ima笔记使用指南", "", "## Positioning 定位", "",
        "IMA 笔记类型条目的 minimal 源摘要页（MCP fetch 对该笔记返回 code:220030，正文不可自动获取）。", "",
        "## Original 原文", "", f"- 本地路径：`{note_raw}`", "- 状态：正文待人工补录（IMA 内查看）",
    ]) + "\n"
    note_page.write_text(page, encoding='utf-8')
    print("wrote", note_page)


if __name__ == '__main__':
    main()
