#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 通道 B / 录音 暂存：
 - 2 份 Biocare markdown：正文取自已落地的 attachments/<同名>（插件已同步原件）
 - 录音 新生产线高速运行方案：尝试 get_media_info 下载原件；正文置 empty + 指针
"""
import json
import os
import urllib.request
from pathlib import Path

ROOT = Path('.')
CRED = Path(os.path.expanduser('~')) / '.config' / 'ima'
BASE = 'https://ima.qq.com'
BODIES = ROOT / '.tools' / '_kb_sync_bodies'
BODIES.mkdir(parents=True, exist_ok=True)
KB_REST = 'F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI='


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


PLAN = json.loads((ROOT / '.tools' / '_kb_sync_plan.json').read_text(encoding='utf-8'))

print("=== 通道 B：Biocare markdown ===")
for it in [x for x in PLAN['items'] if x['channel'] == 'B']:
    mid = it['media_id']
    raw = ROOT / it['raw_path']
    att = raw.parent / 'attachments' / raw.name[:-3]   # 去掉末尾 .md → 原件名
    if att.is_file():
        body = att.read_text(encoding='utf-8', errors='ignore')
        (BODIES / f'{mid}.md').write_text(body, encoding='utf-8')
        (BODIES / f'{mid}.json').write_text(json.dumps(
            {'extract_status': 'ok',
             'extract_method': 'local attachment (IMA plugin synced original)',
             'original_file': f'attachments/{att.name}'}, ensure_ascii=False), encoding='utf-8')
        print(f"[ok] {it['title'][:55]}  <- {att.name}  {len(body)}B")
    else:
        print(f"[!] 原件缺失: {att}")

print("\n=== 录音：新生产线高速运行方案 ===")
rec = [x for x in PLAN['items'] if x['type_label'] == '录音']
for it in rec:
    mid = it['media_id']
    try:
        r = post('openapi/wiki/v1/get_media_info',
                 {'knowledge_base_id': KB_REST, 'media_id': mid})
        info = r.get('data', {}).get('url_info', {})
        print(f"  get_media_info code={r.get('code')} url={str(info.get('url'))[:80]}")
    except Exception as e:
        print(f"  get_media_info 异常: {e}")
    body = ("（IMA 侧无可用转写正文：该录音条目 media_type=15，REST `note/get_doc_content` 当日配额 "
            "`200005` 未恢复；MCP `fetch_media_content` 本会话不可用。）\n\n"
            "> 该录音对应的会议纪要已由 IMA 侧生成并单独入库，见 "
            "[[Meeting Minutes: New Pilot Line High-Speed Running Solution]]。")
    (BODIES / f'{mid}.md').write_text(body, encoding='utf-8')
    (BODIES / f'{mid}.json').write_text(json.dumps(
        {'extract_status': 'empty',
         'extract_method': 'no transcript available (REST 200005 / MCP unavailable)'},
        ensure_ascii=False), encoding='utf-8')
    print(f"  [empty] 已暂存指针正文")

print("\n暂存目录:", len(list(BODIES.glob('*.md'))), "个 .md")
