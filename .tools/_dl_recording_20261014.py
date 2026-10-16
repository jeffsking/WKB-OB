#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下载录音原件（media_type=15）到 RAW_FULL/.../attachments/<原名>。
规则：<50MB 双落（转写正文 + 原件）；>=50MB 只留转写正文（此处无转写 → 仍留原件但标注）。
"""
import json
import os
import urllib.request
from pathlib import Path

ROOT = Path('.')
CRED = Path(os.path.expanduser('~')) / '.config' / 'ima'
BASE = 'https://ima.qq.com'
KB_REST = 'F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI='
MID = 'soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a135d7ea36793b8813587843996532001a693ee6c0644e'
TITLE = '新生产线高速运行方案'


def rd(n):
    return (CRED / n).read_text(encoding='utf-8').strip()


CID, KEY = rd('client_id'), rd('api_key')


def post(path, payload):
    req = urllib.request.Request(
        BASE + '/' + path,
        data=json.dumps(payload).encode('utf-8'),
        headers={'ima-openapi-clientid': CID, 'ima-openapi-apikey': KEY,
                 'Content-Type': 'application/json'},
        method='POST')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode('utf-8'))


r = post('openapi/wiki/v1/get_media_info', {'knowledge_base_id': KB_REST, 'media_id': MID})
ui = (r.get('data') or {}).get('url_info') or {}
url = ui.get('url')
hdrs = ui.get('headers') or {}
print("url:", str(url)[:100])
print("headers keys:", list(hdrs.keys()) if isinstance(hdrs, dict) else type(hdrs))

out_dir = ROOT / 'RAW_FULL' / 'ima_sync' / '个人知识库' / 'WKB' / 'attachments'
out_dir.mkdir(parents=True, exist_ok=True)

# 探测 Content-Type / 大小
try:
    hreq = urllib.request.Request(url, headers=hdrs, method='GET')
    with urllib.request.urlopen(hreq, timeout=120) as resp:
        ct = resp.headers.get('Content-Type', '')
        clen = resp.headers.get('Content-Length')
        print(f"content-type={ct} length={clen}")
        ext = '.mp3'
        if 'mp4' in ct or 'm4a' in ct or 'aac' in ct:
            ext = '.m4a'
        elif 'wav' in ct:
            ext = '.wav'
        elif 'mpeg' in ct:
            ext = '.mp3'
        elif 'ogg' in ct:
            ext = '.ogg'
        dest = out_dir / f'{TITLE}{ext}'
        data = resp.read()
        dest.write_bytes(data)
        print(f"已下载 {len(data)}B -> {dest}")
except Exception as e:
    print("下载失败:", e)
