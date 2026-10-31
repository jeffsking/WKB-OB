#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-24 通道 B：markdown 原件直下（不吃配额）。

两个新 markdown 条目（金佰利×聚合芯能 功能性材料技术对接纪要 CN/EN）：
- get_media_info 取签名 URL → GET 原件 → 落暂存 .tools/_kb_sync_bodies/<media_id>.md
- 同时落 RAW_FULL 镜像（按「原题 + .md」的插件命名惯例推定期望 RAW 相对路径）
铁律：URL 必含本条目 media_id 片段（自证，防串号）；响应体先落盘再读。
"""
import json
import os
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
BODIES = os.path.join(ROOT, ".tools", "_kb_sync_bodies")
INFO = os.path.join(ROOT, ".tools", "_media_info_20261024")
os.makedirs(BODIES, exist_ok=True)
os.makedirs(INFO, exist_ok=True)

TARGETS = [
    "markdown_3867e2b60070d7dc3f413086d0b0036e_f5d67c32985d6dc7161e17124454d931001a693ee6c0644e",
    "markdown_3867e2b60070d7dc3f413086d0b0036e_256cbf2d99691b18c27f42b9085ee22b001a693ee6c0644e",
]


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()


def post(path, payload):
    req = urllib.request.Request(
        BASE + "/" + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                 "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    for mid in TARGETS:
        p = os.path.join(INFO, mid[-16:] + ".json")
        with open(p, "wb") as f:
            f.write(post("openapi/wiki/v1/get_media_info", {"media_id": mid}))
        d = json.load(open(p, encoding="utf-8"))
        info = (d.get("data") or {}).get("url_info") or {}
        url = info.get("url") or ""
        hdrs = info.get("headers") or {}
        if "media_id=" in url and mid not in url:
            print(f"[ABORT {mid[-10:]}] URL 串号: {url[:120]}")
            continue
        if not url:
            print(f"[FAIL {mid[-10:]}] no url: {json.dumps(d, ensure_ascii=False)[:200]}")
            continue
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=180) as r:
            body = r.read()
            ct = r.headers.get("Content-Type", "")
        out = os.path.join(BODIES, mid + ".md")
        with open(out, "wb") as f:
            f.write(body)
        txt = body.decode("utf-8", errors="ignore")
        print(f"[OK {mid[-10:]}] {len(body)} B ct={ct} chars={len(txt)} head={txt[:60]!r}")


if __name__ == "__main__":
    main()
