#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""补齐最后 1 条 dedup 残余未编译。"""
import re
from datetime import date
from pathlib import Path

ROOT = Path('.')
WIKI_SRC = ROOT / 'WIKI/sources'
PAGE_HEAD = re.compile(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', re.S)
MAX_BODY = 6000

raw = "RAW/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/交互式机械变色电子织物传感器_拆解.md.md"
full = "RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook/Ebook Extract/Mechanochromic_Photonic_Sensors_拆解/交互式机械变色电子织物传感器_拆解.md.md"
page_name = "交互式机械变色电子织物传感器_拆解"
title = "交互式机械变色电子织物传感器（拆解）"
stype = "Smart-Materials"

content = (ROOT / full).read_text(encoding='utf-8', errors='replace')
m = PAGE_HEAD.match(content)
body = (m.group(2) if m else content).strip()
trunc = False
if len(body) > MAX_BODY:
    body = body[:MAX_BODY]
    trunc = True

fm = "\n".join([
    "---", "type: source", f'title: "{title}"', f"source_type: {stype}",
    f"source_path: {raw}", 'original_link: ""',
    f"date_published: {date.today().isoformat()}", f"date_processed: {date.today().isoformat()}",
    "credibility: 中", "key_claims: []", "pages_linked: []", "compile_mode: extractive", "---",
])
page = fm + "\n\n" + "\n".join([
    f"# {title}", "", "## Positioning 定位", "",
    f"抽取式源摘要页（`source_type: {stype}`）。正文摘录自镜像层，未做语义改写。", "",
    "## Extracted Content 原文摘录", "", body,
    *(["", f"*（正文超过 {MAX_BODY} 字，此处截断）*"] if trunc else []),
    "", "## Original 原文", "", f"- 本地路径：`{raw}`", f"- 镜像正文：`{full}`",
]) + "\n"
dest = WIKI_SRC / f"{page_name}.md"
dest.write_text(page, encoding='utf-8')
print("wrote", dest)
