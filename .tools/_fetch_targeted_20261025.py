#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 定向取件：给定 media_id 清单，逐条尝试 get_media_info 原件下载。

铁律（MEMORY §六）：API 返回体一律先落盘，禁止管道预览。
用法： python .tools/_fetch_targeted_20261025.py
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ima_fetch_originals as F  # noqa: E402

OUT = Path(__file__).resolve().parent / "_fetch_targeted_20261025"
OUT.mkdir(exist_ok=True)

TARGETS = json.loads((Path(__file__).resolve().parent / "_fetch_targets_20261025.json").read_text(encoding="utf-8"))

cid, key = F.load_creds()
log = []
for t in TARGETS:
    mid = t["media_id"]
    enc = mid.replace("/", "_")[:120]
    try:
        resp = F.post("openapi/wiki/v1/get_media_info", {"media_id": mid}, cid, key)
    except Exception as e:  # noqa: BLE001
        log.append({"media_id": mid, "ok": False, "err": f"call:{e}"})
        print(f"[FAIL-call] {t.get('title','')[:30]} :: {e}")
        continue
    (OUT / f"{enc}.info.json").write_text(json.dumps(resp, ensure_ascii=False, indent=1), encoding="utf-8")
    if resp.get("code") != 0:
        log.append({"media_id": mid, "ok": False, "code": resp.get("code"), "msg": resp.get("msg")})
        print(f"[FAIL-code] {t.get('title','')[:30]} :: code={resp.get('code')} {resp.get('msg')}")
        continue
    data = resp.get("data") or {}
    ui = data.get("url_info") or {}
    url = ui.get("url")
    if not url or url.startswith("chrome://"):
        log.append({"media_id": mid, "ok": False, "err": "no-url", "data_keys": list(data.keys())})
        print(f"[SKIP-url ] {t.get('title','')[:30]} :: url={str(url)[:60]}")
        continue
    try:
        blob, ct = F.fetch(url, ui.get("headers"))
    except Exception as e:  # noqa: BLE001
        log.append({"media_id": mid, "ok": False, "err": f"dl:{e}"})
        print(f"[FAIL-dl  ] {t.get('title','')[:30]} :: {e}")
        continue
    ext = F.CT_EXT.get(ct) or F.sniff_bytes(blob[:8192], "")
    dest = OUT / f"{enc}{ext or '.bin'}"
    dest.write_bytes(blob)
    log.append({"media_id": mid, "ok": True, "ct": ct, "bytes": len(blob), "file": str(dest), "ext": ext})
    print(f"[OK       ] {t.get('title','')[:30]} :: {len(blob)} B ({ct}) -> {dest.name}")

(OUT / "_log.json").write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
print("done", len(log))
