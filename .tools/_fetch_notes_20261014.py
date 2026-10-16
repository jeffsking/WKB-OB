#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 通道 A：REST get_doc_content 抓笔记/录音正文。
读 ~/.config/ima 凭证，urllib 直调（无需 Node）。
命中 200005 → 立即停止（日配额）；220030 → 标记永久失败不重试。
输出 .tools/_kb_sync_bodies/<media_id>.md + <media_id>.json
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path('.')
CRED = Path(os.path.expanduser('~')) / '.config' / 'ima'
BASE = 'https://ima.qq.com'
BODIES = ROOT / '.tools' / '_kb_sync_bodies'
BODIES.mkdir(parents=True, exist_ok=True)


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
targets = [i for i in PLAN['items'] if i['channel'] == 'A']

print(f"通道A 目标 {len(targets)} 条")
results = []
for it in targets:
    mid = it['media_id']
    title = it['title']
    # RAW 侧已有正文的（非占位壳）→ 直接镜像，无需 REST
    raw_txt = (ROOT / it['raw_path']).read_text(encoding='utf-8', errors='ignore')
    body_raw = raw_txt.split('---', 2)[-1].strip() if raw_txt.startswith('---') else raw_txt.strip()
    if len(body_raw) > 400 and '暂不支持自动同步' not in raw_txt and '此条目为' not in raw_txt:
        print(f"[mirror] {title[:40]}  RAW 已有正文 {len(body_raw)}B → 直接镜像")
        (BODIES / f'{mid}.md').write_text(body_raw, encoding='utf-8')
        (BODIES / f'{mid}.json').write_text(json.dumps(
            {'extract_status': 'ok', 'extract_method': 'RAW-side full body (IMA plugin synced)'},
            ensure_ascii=False), encoding='utf-8')
        results.append((title, 'mirror-ok', len(body_raw)))
        continue

    note_id = mid.split('_')[-1]
    try:
        r = post('openapi/note/v1/get_doc_content',
                 {'note_id': note_id, 'target_content_format': 0})
    except Exception as e:
        print(f"[!] {title[:40]} 请求异常: {e}")
        results.append((title, f'error:{e}', 0))
        continue
    code = r.get('code')
    if code == 0:
        content = (r.get('data') or {}).get('content') or ''
        if content.strip():
            (BODIES / f'{mid}.md').write_text(content, encoding='utf-8')
            (BODIES / f'{mid}.json').write_text(json.dumps(
                {'extract_status': 'ok', 'extract_method': 'REST note get_doc_content'},
                ensure_ascii=False), encoding='utf-8')
            print(f"[ok] {title[:40]}  {len(content)}B")
            results.append((title, 'ok', len(content)))
        else:
            (BODIES / f'{mid}.md').write_text('（IMA 侧无可用正文）', encoding='utf-8')
            (BODIES / f'{mid}.json').write_text(json.dumps(
                {'extract_status': 'empty', 'extract_method': 'REST note get_doc_content'},
                ensure_ascii=False), encoding='utf-8')
            print(f"[empty] {title[:40]}  code=0 但 content 空")
            results.append((title, 'empty', 0))
    elif code == 200005:
        print(f"[STOP] 命中日配额 200005 —— 立即停止，不重试。剩余 {len(targets) - len(results)} 条留待次日。")
        results.append((title, 'blocked-200005', 0))
        break
    elif code == 220030:
        print(f"[skip] {title[:40]}  220030 条目级永久失败（IMA 侧异常），留积压不重试")
        results.append((title, 'permfail-220030', 0))
    else:
        print(f"[!] {title[:40]}  code={code} msg={r.get('message')}")
        results.append((title, f'err-{code}', 0))
    time.sleep(1.5)

print("\n=== 通道A 汇总 ===")
for t, s, n in results:
    print(f"  {s:16s} {n:>7}  {t[:50]}")
