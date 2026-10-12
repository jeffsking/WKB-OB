# -*- coding: utf-8 -*-
"""从保存的 MCP tool-result JSON 文件直接清洗成正文。
用法: python _clean_from_result.py <result_json_file> <out_md>
"""
import json
import sys
sys.path.insert(0, r'E:\WKB-OB\.tools')
from _clean_body import clean

raw = open(sys.argv[1], encoding='utf-8').read()
try:
    obj = json.loads(raw)
    content = obj.get('content', raw)
except Exception:
    content = raw
open(sys.argv[2], 'w', encoding='utf-8').write(clean(content))
print('OK', sys.argv[2])
