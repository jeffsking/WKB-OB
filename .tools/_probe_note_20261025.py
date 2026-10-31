#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 笔记正文单条探测（官方 ima_api.cjs，业务码为唯一判据）。

urllib 直调实测 403（假象）。命中 200005 当日立即停止，禁止重试。
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJS_DIR = os.path.join(os.path.expanduser("~"), ".workbuddy", "skills", "ima-skill")
OUT = os.path.join(ROOT, ".tools", "_doc_content_20261025")
STAGE = os.path.join(ROOT, ".tools", "_kb_sync_bodies")
os.makedirs(OUT, exist_ok=True)

MID = sys.argv[1]
TITLE = sys.argv[2] if len(sys.argv) > 2 else MID
note_id = MID.split("_")[-1]


def fetch(nid):
    payload = json.dumps({"note_id": nid, "target_content_format": 0})
    p = subprocess.run(["node", "ima_api.cjs", "openapi/note/v1/get_doc_content", payload],
                       cwd=CJS_DIR, capture_output=True, text=True, encoding="utf-8")
    out = (p.stdout or "").strip()
    return out, p.stderr


raw, err = fetch(note_id)
with open(os.path.join(OUT, note_id + ".txt"), "w", encoding="utf-8") as f:
    f.write(raw if raw else ("STDERR:" + (err or "")))
try:
    r = json.loads(raw)
except Exception:
    print("[PARSE-FAIL]", (raw or err)[:400])
    sys.exit(1)

code = r.get("code")
print(f"code={code} msg={r.get('msg') or r.get('message')}")
if code != 0:
    sys.exit(0)

data = r.get("data") or {}
content = data.get("content") or ""
print(f"chars={len(content)} title={(data.get('title') or TITLE)!r}")
if content.strip():
    os.makedirs(STAGE, exist_ok=True)
    with open(os.path.join(STAGE, MID + ".md"), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(STAGE, MID + ".json"), "w", encoding="utf-8") as f:
        json.dump({"extract_status": "ok", "extract_method": "REST note get_doc_content (cjs)",
                   "media_id": MID, "note_id": note_id, "chars": len(content)},
                  f, ensure_ascii=False, indent=1)
    print("staged ->", MID + ".md")
else:
    print("(empty body)")
