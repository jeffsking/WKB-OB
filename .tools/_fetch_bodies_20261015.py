#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 阶段 B 正文抓取（本地通道）：
  · 通道 A 笔记：REST openapi/note/v1/get_doc_content（经官方 ima_api.cjs，判据权威）
  · RAW 侧已有完整正文的条目：直接镜像（插件已落盘，省一次配额）
落盘 .tools/_kb_sync_bodies/<media_id>.md (+ .json meta)
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path('.')
TOOLS = ROOT / '.tools'
PLAN = TOOLS / '_kb_sync_plan.json'
BODIES = TOOLS / '_kb_sync_bodies'
CJS = Path(os.path.expanduser('~')) / '.workbuddy/skills/ima-skill/ima_api.cjs'
NODE = Path(os.path.expanduser('~')) / '.workbuddy/binaries/node/versions/22.22.2-6/node.exe'
if not NODE.exists():
    NODE = Path(r'C:\Program Files\nodejs\node.exe')

PLACEHOLDER_MARK = '暂不支持自动同步内容'
BODIES.mkdir(parents=True, exist_ok=True)


def rel(p):
    return str(Path(p).replace('\\', '/'))


def cjs(api_path, payload):
    r = subprocess.run([str(NODE), str(CJS), api_path, json.dumps(payload, ensure_ascii=False)],
                       capture_output=True, text=True, encoding='utf-8', timeout=120)
    try:
        return json.loads((r.stdout or '').strip())
    except Exception:
        return {'code': -1, 'msg': (r.stdout or '') + (r.stderr or '')}


def raw_body(raw_path):
    """取 RAW 正文（去 front matter）。"""
    t = (ROOT / raw_path).read_text(encoding='utf-8', errors='replace')
    parts = t.split('---', 2)
    return parts[2] if len(parts) > 2 else t


plan = json.loads(PLAN.read_text(encoding='utf-8'))
items = plan.get('items', [])
print(f'待抓 {len(items)} 条')

summary = []
quota_hit = False
for it in items:
    mid = it['media_id']
    raw = ROOT / it['raw_path']
    rt = raw.read_text(encoding='utf-8', errors='replace') if raw.exists() else ''
    prefix = it['prefix']
    src_chars = 0
    status = None
    method = None

    if PLACEHOLDER_MARK not in rt and len(rt) >= 600:
        # RAW 侧已有完整正文（插件落盘）→ 镜像
        body = raw_body(it['raw_path'])
        status = 'ok'
        method = 'RAW-side full body (IMA plugin synced)'
        src_chars = len(body)
    elif prefix == 'note':
        note_id = mid.split('_')[-1]
        resp = cjs('openapi/note/v1/get_doc_content',
                   {'note_id': note_id, 'target_content_format': 0})
        code = resp.get('code')
        if code == 0:
            body = (resp.get('data') or {}).get('content') or ''
            status = 'ok' if body.strip() else 'empty'
            method = f'REST openapi/note/v1/get_doc_content (target_content_format=0) — note_id={note_id}'
            src_chars = len(body)
        elif code == 200005:
            print(f'  [配额] {mid}: 200005 日配额耗尽 → 当日停止')
            quota_hit = True
            break
        else:
            print(f'  [FAIL] {mid}: code={code} msg={resp.get("msg")}')
            summary.append({'mid': mid, 'action': 'fail', 'code': code})
            continue
    else:
        print(f'  [SKIP] {mid} prefix={prefix}: 非笔记且 RAW 无正文 → 需原件通道')
        summary.append({'mid': mid, 'action': 'needs-original', 'prefix': prefix})
        continue

    (BODIES / f'{mid}.md').write_text(body, encoding='utf-8')
    (BODIES / f'{mid}.json').write_text(
        json.dumps({'extract_status': status,
                    'meta': {'extract_method': method, 'src_chars': src_chars}},
                   ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'  [OK] {mid} status={status} chars={src_chars}')
    summary.append({'mid': mid, 'action': 'ok', 'status': status, 'chars': src_chars})

print('\n汇总:', json.dumps(summary, ensure_ascii=False))
print('quota_hit:', quota_hit)
