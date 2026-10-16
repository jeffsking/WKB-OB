#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""阶段 B 正文准备（2026-10-13）：
  · NIFO visit 笔记 —— RAW 侧已有正文（插件今日同步成功）→ 抽取正文写入暂存
  · REL增强层（markdown）—— 走通道 B：get_media_info 签名 URL → GET 原件写入暂存
其余 3 条笔记（聚烯烃胶/益生菌/莱博药妆）REST get_doc_content 命中 200005 → 不写入，留账本 discovered。
"""
import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path('.')
TOOLS = ROOT / '.tools'
BODIES = TOOLS / '_kb_sync_bodies'
CRED = Path(os.path.expanduser('~')) / '.config' / 'ima'
KB_REST = 'F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI='

cid = (CRED / 'client_id').read_text(encoding='utf-8').strip()
key = (CRED / 'api_key').read_text(encoding='utf-8').strip()

BODIES.mkdir(parents=True, exist_ok=True)

plan = json.loads((TOOLS / '_kb_sync_plan.json').read_text(encoding='utf-8'))
by_mid = {x['media_id']: x for x in plan['items']}


def post(path, payload):
    req = urllib.request.Request(
        'https://ima.qq.com/' + path, data=json.dumps(payload).encode(),
        headers={'ima-openapi-clientid': cid, 'ima-openapi-apikey': key,
                 'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def strip_fm(t):
    if t.startswith('---'):
        parts = t.split('---', 2)
        return parts[2] if len(parts) >= 3 else t
    return t


def drop_leading_h1(t):
    lines = t.lstrip('\n').split('\n')
    out = []
    dropped = False
    for ln in lines:
        if not dropped and ln.strip().startswith('# '):
            dropped = True
            continue
        out.append(ln)
    return '\n'.join(out).strip()


written = []

# ---- 1) NIFO：RAW 已有正文 ----
for mid, it in by_mid.items():
    if 'NIFO' not in (it.get('title') or ''):
        continue
    raw = (ROOT / it['raw_path']).read_text(encoding='utf-8', errors='replace')
    body = drop_leading_h1(strip_fm(raw))
    (BODIES / f'{mid}.md').write_text(body, encoding='utf-8')
    (BODIES / f'{mid}.json').write_text(json.dumps(
        {'extract_status': 'ok',
         'meta': {'extract_method': 'raw-mirror (plugin synced body into RAW)',
                  'body_chars': len(body)}}, ensure_ascii=False, indent=1),
        encoding='utf-8')
    written.append((mid, 'raw-mirror', len(body)))

# ---- 2) REL增强层：通道 B 原件下载 ----
for mid, it in by_mid.items():
    if not mid.startswith('markdown_'):
        continue
    r = post('openapi/wiki/v1/get_media_info', {'media_id': mid})
    ui = (r.get('data') or {}).get('url_info', {})
    url = ui.get('url')
    if not url or not url.startswith('http'):
        print('[!] 无可用 URL:', mid, ui)
        continue
    req = urllib.request.Request(url, headers=ui.get('headers') or {}, method='GET')
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    try:
        body = data.decode('utf-8')
    except UnicodeDecodeError:
        body = data.decode('utf-8', errors='replace')
    (BODIES / f'{mid}.md').write_text(body, encoding='utf-8')
    (BODIES / f'{mid}.json').write_text(json.dumps(
        {'extract_status': 'ok',
         'meta': {'extract_method': 'channel-B get_media_info original',
                  'bytes': len(data), 'body_chars': len(body)}},
        ensure_ascii=False, indent=1), encoding='utf-8')
    written.append((mid, 'channel-B', len(body)))

print('写入暂存:', len(written))
for w in written:
    print('  ', w)
