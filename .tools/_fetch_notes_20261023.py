#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 笔记正文 REST 兜底：逐条 get_doc_content，响应先落盘再读。

铁律：命中 200005（日配额耗尽）当日立即停止，禁止重试。
note_id = media_id 末段（形如 note_<hash>_<noteid> → <noteid>）。
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
OUT = os.path.join(ROOT, ".tools", "_doc_content_20261023")
os.makedirs(OUT, exist_ok=True)


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()
PLAN = os.path.join(ROOT, ".tools", "_kb_sync_plan.json")


def main():
    plan = json.load(open(PLAN, encoding="utf-8"))
    notes = [it for it in plan["items"] if it.get("media_type") == 11]
    print(f"待取笔记 {len(notes)} 条")
    for it in notes:
        mid = it["media_id"]
        note_id = mid.split("_")[-1]
        payload = {"note_id": note_id}
        req = urllib.request.Request(
            BASE + "/openapi/note/v1/get_doc_content",
            data=json.dumps(payload).encode("utf-8"),
            headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                     "Content-Type": "application/json"},
            method="POST")
        short = mid[-16:]
        p = os.path.join(OUT, short + ".json")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
        except Exception as e:  # noqa: BLE001
            print(f"  [{short}] HTTP EXC {e}")
            continue
        with open(p, "wb") as f:
            f.write(body)
        d = json.loads(body.decode("utf-8"))
        code = d.get("code")
        content = (d.get("data") or {}).get("content") or ""
        print(f"  [{short}] code={code} chars={len(content)} title={(d.get('data') or {}).get('title','')!r:.30}")
        if code == 200005:
            print("  → 200005 日配额耗尽，按铁律当日停止")
            break
        if code != 0:
            print("     msg:", d.get("msg") or d.get("message"))
        time.sleep(3)


if __name__ == "__main__":
    main()
