#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""连通性探针：验证 REST get_knowledge_list 用新 KB ID 是否可用 + 根层总数。
不落盘正文，只取根层第一页。"""
import json
import os
import urllib.request

CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"


def rd(n):
    with open(os.path.join(CRED, n), encoding="utf-8") as f:
        return f.read().strip()


CID, KEY = rd("client_id"), rd("api_key")

for kb in ["ima_kb_l24tiCGM", "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="]:
    payload = {"knowledge_base_id": kb, "limit": 50, "cursor": "",
               "sort_type": "MEDIA_DESC_SORT_TYPE"}
    req = urllib.request.Request(
        BASE + "/openapi/wiki/v1/get_knowledge_list",
        data=json.dumps(payload).encode("utf-8"),
        headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                 "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read().decode("utf-8"))
        data = d.get("data") or {}
        print(f"[{kb[:22]}] code={d.get('code')} msg={d.get('message')} "
              f"list={len(data.get('knowledge_list') or [])} "
              f"total={data.get('knowledge_total_size')} is_end={data.get('is_end')}")
    except Exception as e:  # noqa: BLE001
        print(f"[{kb[:22]}] EXC {type(e).__name__}: {e}")
