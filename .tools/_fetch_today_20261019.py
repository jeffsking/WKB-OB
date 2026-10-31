#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-19 单次抓取：html 型（type 20）原件 + note 正文（REST）。

用法：
  python _fetch_today_20261019.py media <media_id> [--out name]
  python _fetch_today_20261019.py note  <media_id>
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
KB_REST = "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="
STAGE = os.path.join(ROOT, ".tools", "_kb_sync_bodies")


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()
HDR = {"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY}


def post(path, payload, retries=3):
    body = json.dumps(payload).encode("utf-8")
    for a in range(retries):
        req = urllib.request.Request(BASE + "/" + path, data=body,
                                     headers={**HDR, "Content-Type": "application/json"},
                                     method="POST")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            print(f"  HTTP {e.code} (attempt {a+1})")
            if a < retries - 1:
                time.sleep(12)
        except Exception as e:  # noqa: BLE001
            print(f"  ERR {e} (attempt {a+1})")
            if a < retries - 1:
                time.sleep(12)
    return {"code": -1, "message": "request failed"}


def main():
    mode, mid = sys.argv[1], sys.argv[2]
    os.makedirs(STAGE, exist_ok=True)
    if mode == "media":
        r = post("openapi/wiki/v1/get_media_info",
                 {"knowledge_base_id": KB_REST, "media_id": mid})
        print("code", r.get("code"), r.get("message"))
        print(json.dumps(r.get("data", {}), ensure_ascii=False)[:1200])
    else:
        r = post("openapi/note/v1/get_doc_content",
                 {"knowledge_base_id": KB_REST, "media_id": mid, "target_content_format": 0})
        print("code", r.get("code"), r.get("message"))
        d = r.get("data") or {}
        txt = d.get("content") or ""
        print("len", len(txt))
        if txt:
            p = os.path.join(STAGE, mid + ".md")
            with open(p, "w", encoding="utf-8") as f:
                f.write(txt)
            print("saved", p)
            print(txt[:400].replace("\n", " "))


if __name__ == "__main__":
    main()
