#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15：下载 5CB 贴身合规评估结论备忘录 word 原件 → RAW_FULL attachments，
并抽取正文写入 _kb_sync_bodies。"""
import json
import os
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path('.')
MID = 'word_3867e2b60070d7dc3f413086d0b0036e_01a13aff0bc2744e97852338ed77667d001a693ee6c0644e'
RAW_REL = 'RAW/ima_sync/个人知识库/WKB/5CB贴身合规评估结论备忘录_20261014.docx.md'
CJS = Path(os.path.expanduser('~')) / '.workbuddy/skills/ima-skill/ima_api.cjs'
NODE = Path(os.path.expanduser('~')) / '.workbuddy/binaries/node/versions/22.22.2-6/node.exe'
if not NODE.exists():
    NODE = Path(r'C:\Program Files\nodejs\node.exe')

r = subprocess.run([str(NODE), str(CJS), 'openapi/wiki/v1/get_media_info',
                    json.dumps({'media_id': MID}, ensure_ascii=False)],
                   capture_output=True, text=True, encoding='utf-8', timeout=120)
resp = json.loads(r.stdout.strip())
ui = (resp.get('data') or {}).get('url_info') or {}
url = ui.get('url')
headers = ui.get('headers') or {}
print('code', resp.get('code'), 'url?', bool(url))

req = urllib.request.Request(url, headers=headers, method='GET')
with urllib.request.urlopen(req, timeout=300) as rr:
    data = rr.read()
    ct = rr.headers.get('Content-Type')
print('downloaded', len(data), 'bytes', ct)

dest_dir = ROOT / 'RAW_FULL/ima_sync/个人知识库/WKB/attachments'
dest_dir.mkdir(parents=True, exist_ok=True)
dest = dest_dir / '5CB贴身合规评估结论备忘录_20261014.docx'
dest.write_bytes(data)
print('saved ->', dest)

# 抽取 docx 文本
import re
import zipfile
texts = []
with zipfile.ZipFile(dest) as z:
    xml = z.read('word/document.xml').decode('utf-8', 'ignore')
# 段落
for p in re.findall(r'<w:p[ >].*?</w:p>', xml, re.S):
    runs = re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S)
    line = ''.join(runs)
    line = re.sub(r'<[^>]+>', '', line)
    texts.append(line)
body = '\n'.join(texts).strip()
print('extracted chars:', len(body))
print('--- head ---')
print(body[:600])

out = ROOT / '.tools/_kb_sync_bodies'
out.mkdir(parents=True, exist_ok=True)
status = 'ok' if len(body) > 30 else 'original-only'
(out / f'{MID}.md').write_text(body, encoding='utf-8')
(out / f'{MID}.json').write_text(json.dumps({
    'extract_status': status,
    'meta': {'extract_method': 'REST get_media_info 原件下载 → docx 文本抽取',
             'original_attachment': str(dest).replace('\\', '/'),
             'audio_bytes': len(data)}}, ensure_ascii=False, indent=1), encoding='utf-8')
print('wrote bodies stub, status =', status)
