#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 通道 B/C 原件探测：对指定 media_id 调 get_media_info，响应全量落盘后再读。

铁律：API 返回体必须落盘后再读，禁管道预览。
"""
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
OUT = os.path.join(ROOT, ".tools", "_media_info_20261023")
os.makedirs(OUT, exist_ok=True)


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()

TARGETS = {
    "idx_IMA": "markdown_3867e2b60070d7dc3f413086d0b0036e_7424725e5aeb8eb37d0f7f6e71eff6d9001a693ee6c0644e",
    "jinbaili_zhongke": "markdown_e5656dbc3d0f2888096a8b56b414d9fc_5abe25ebc7e4724fa1c47c969f439460001a693ee6c0644e",
    "pcm_ntmt": "wechatarticle_3867e2b60070d7dc3f413086d0b0036e_1d9df36f0a1abbb60dfbf6341da17061",
    "xishi_fare": "wechatarticle_3867e2b60070d7dc3f413086d0b0036e_b1bd68417e4c5dd4d1eb21f5bd32d69f",
    "sensor_rec": "soundrecording_3867e2b60070d7dc3f413086d0b0036e_01a167615b427816ad84976174ccc20e001a693ee6c0644e",
}


def main():
    only = sys.argv[1:] or list(TARGETS)
    for name in only:
        mid = TARGETS.get(name)
        if not mid:
            print("?", name)
            continue
        payload = {"media_id": mid}
        req = urllib.request.Request(
            BASE + "/openapi/wiki/v1/get_media_info",
            data=json.dumps(payload).encode("utf-8"),
            headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                     "Content-Type": "application/json"},
            method="POST")
        p = os.path.join(OUT, name + ".json")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
            with open(p, "wb") as f:
                f.write(body)
            d = json.loads(body.decode("utf-8"))
            code = d.get("code")
            info = (d.get("data") or {}).get("media_info") or {}
            url = ((info.get("url_info") or {}).get("url") or "")
            print(f"{name}: code={code} title={info.get('title','')!r:.50} url={url[:70]}")
            if code != 0:
                print("   msg:", d.get("message"))
        except Exception as e:  # noqa: BLE001
            print(f"{name}: EXC {e}")


if __name__ == "__main__":
    main()
