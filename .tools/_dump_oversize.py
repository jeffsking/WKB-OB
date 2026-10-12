#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解包 IMA 超限临时文件 → RAW_FULL 正文。

用法：
  python .tools/_dump_oversize.py <超限临时文件> <dst原始路径> <media_id> <name> <original_path>

背景：通道 A 单份正文超出工具返回上限时，系统会把结果**自动转存为临时文件**
（返回信息形如「result (N characters) exceeds maximum allowed tokens. Output has been saved to <路径>」）。
该临时文件可能是单行 JSON（含 `content` 字段），也可能是纯文本，本脚本两者兼容。
⚠️ 实测 11.1 万字符即可能触发（长专利 PDF 常见）。
"""
import json
import sys
import datetime

src, dst, media_id, name, orig = sys.argv[1:6]

with open(src, "r", encoding="utf-8") as f:
    raw = f.read()

try:
    obj = json.loads(raw)
    content = obj["content"] if isinstance(obj, dict) else obj
except Exception:
    content = raw

today = datetime.date.today().isoformat()
header = (
    "---\n"
    f'media_id: "{media_id}"\n'
    f'source_file: "{name}"\n'
    f'original_path: "{orig}"\n'
    f'extracted: "{today}"\n'
    'extract_method: "ima-mcp fetch_media_content"\n'
    'extract_status: "ok"\n'
    'clean_rules: ""\n'
    'processed: ""\n'
    "---\n\n"
    f"# {name}\n\n"
)

with open(dst, "w", encoding="utf-8", newline="\n") as f:
    f.write(header)
    f.write(content)

print("chars:", len(content))
