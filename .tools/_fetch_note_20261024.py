#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-24 笔记正文 REST 兜底：单条探测（恒碳 ptt/pet 成本拆解）。

铁律：命中 200005（日配额耗尽）当日立即停止，禁止重试；响应体先落盘再读。
note_id = media_id 末段。
"""
import json
import os
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
OUT = os.path.join(ROOT, ".tools", "_doc_content_20261024")
BODIES = os.path.join(ROOT, ".tools", "_kb_sync_bodies")
os.makedirs(OUT, exist_ok=True)

MID = "note_3867e2b60070d7dc3f413086d0b0036e_7519362139311345"


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()
note_id = MID.split("_")[-1]
req = urllib.request.Request(
    BASE + "/openapi/note/v1/get_doc_content",
    data=json.dumps({"note_id": note_id}).encode("utf-8"),
    headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
             "Content-Type": "application/json"},
    method="POST")
p = os.path.join(OUT, note_id + ".json")
with urllib.request.urlopen(req, timeout=90) as r:
    body = r.read()
with open(p, "wb") as f:
    f.write(body)
d = json.loads(body.decode("utf-8"))
data = d.get("data") or {}
content = data.get("content") or ""
print(f"code={d.get('code')} chars={len(content)} title={data.get('title','')!r}")
if d.get("code") == 0 and content:
    with open(os.path.join(BODIES, MID + ".md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("已写暂存正文 →", os.path.join(BODIES, MID + ".md"))
else:
    print("msg:", d.get("msg") or d.get("message"))
