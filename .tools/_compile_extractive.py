#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""阶段 C 批量「抽取式」编译器：为待编译条目生成合规的 WIKI source 页。

设计原则（诚实优先）：
- front matter 的 source_path 必须与 raw_path 逐字一致（apply 校验）。
- key_claims 留空（不臆造），正文用「原文抽取」而非编造摘要。
- 正文过长时截断到 MAX_BODY，并标注截断。
- 幂等：目标页已存在则跳过（apply 侧也会 skip-exists）。
"""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path('.')
PLAN = ROOT / '.tools/_kb_compile_plan.json'
PAGES_IN = ROOT / '.tools/_kb_compile_pages'
MAX_BODY = 6000

PAGE_HEAD = re.compile(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', re.S)


def strip_front_matter(text):
    m = PAGE_HEAD.match(text)
    return m.group(2) if m else text


def today():
    return date.today().isoformat()


def build_front_matter(it):
    return "\n".join([
        "---",
        "type: source",
        f'title: "{it["title"]}"',
        f"source_type: {it.get('source_type') or '行业新闻'}",
        f"source_path: {it['raw_path']}",
        'original_link: ""',
        f"date_published: {today()}",
        f"date_processed: {today()}",
        "credibility: 中",
        "knowledge_update_status: pending",
        "key_claims: []",
        "pages_linked: []",
        "compile_mode: extractive",
        "---",
    ])


def make_body(it, content):
    title = it["title"]
    truncated = False
    if len(content) > MAX_BODY:
        content = content[:MAX_BODY]
        truncated = True
    lines = [
        f"# {title}",
        "",
        "## Positioning 定位",
        "",
        f"本文为 IMA 知识库条目的抽取式源摘要页（`source_type: {it.get('source_type')}`）。",
        f"正文直接摘录自镜像层 `{it['full_path']}`，未做语义改写；",
        "待后续深度编译时补全 `key_claims` 与实体链接。",
        "",
        "## Extracted Content 原文摘录",
        "",
        content.strip(),
    ]
    if truncated:
        lines += ["", f"*（正文超过 {MAX_BODY} 字，此处截断；完整内容见镜像层）*"]
    lines += ["", "## Original 原文", "",
              f"- 本地路径：`{it['raw_path']}`",
              f"- 镜像正文：`{it['full_path']}`"]
    return "\n".join(lines)


def main():
    plan = json.loads(PLAN.read_text(encoding='utf-8'))
    PAGES_IN.mkdir(parents=True, exist_ok=True)
    written = skipped = failed = 0
    fails = []
    for it in plan["items"]:
        if it.get("stub_only"):
            continue  # stub 由 kb_compiler.py stub --write 负责
        mid = it["media_id"]
        dest = PAGES_IN / f"{mid}.md"
        if dest.exists():
            skipped += 1
            continue
        fp = ROOT / it["full_path"]
        if not fp.is_file():
            failed += 1
            fails.append((mid, "no-body"))
            continue
        raw = fp.read_text(encoding='utf-8', errors='replace')
        content = strip_front_matter(raw)
        page = build_front_matter(it) + "\n\n" + make_body(it, content)
        dest.write_text(page, encoding='utf-8')
        written += 1
    print(f"[gen] 写入 {written} · 跳过(已存在) {skipped} · 失败 {failed}")
    for mid, why in fails[:20]:
        print("   FAIL", mid, why)
    if fails:
        (ROOT / '.tools/_kb_compile_gen_failed.txt').write_text(
            "\n".join(f"{m}\t{w}" for m, w in fails), encoding='utf-8')


if __name__ == '__main__':
    main()
