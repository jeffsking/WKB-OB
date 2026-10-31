#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 通道 A：笔记正文抓取（走官方 ima_api.cjs，业务码为唯一判据）。

urllib 直调会返回 HTTP 403（假象），故一律经 cjs 取 code。
usage: python .tools/_fetch_notes_20261020.py
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJS_DIR = os.path.join(os.path.expanduser("~"), ".workbuddy", "skills", "ima-skill")
KB_REST = "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="
STAGE = os.path.join(ROOT, ".tools", "_kb_sync_bodies")

NOTES = [
    ("note_3867e2b60070d7dc3f413086d0b0036e_7517884351784262", "7517884351784262", "MEETING MINUTES"),
    ("note_3867e2b60070d7dc3f413086d0b0036e_7516355100157487", "7516355100157487",
     "三家技术档案都在知识库里，我重新调取本轮证据，把参数对齐后给"),
]


def fetch(note_id):
    payload = json.dumps({"note_id": note_id, "knowledge_base_id": KB_REST,
                          "content_format": 1, "target_content_format": 1})
    p = subprocess.run(["node", "ima_api.cjs", "openapi/note/v1/get_doc_content", payload],
                       cwd=CJS_DIR, capture_output=True, text=True, encoding="utf-8")
    out = (p.stdout or "").strip()
    try:
        return json.loads(out)
    except Exception:
        return {"code": -1, "msg": (out or p.stderr)[:300]}


def main():
    os.makedirs(STAGE, exist_ok=True)
    for media_id, note_id, title in NOTES:
        r = fetch(note_id)
        code = r.get("code")
        if code != 0:
            print(f"[FAIL] {title} -> code={code} msg={r.get('msg')}")
            continue
        content = (r.get("data") or {}).get("content") or ""
        print(f"[OK] {title} -> {len(content)} chars")
        if not content.strip():
            print("   (empty)")
            continue
        with open(os.path.join(STAGE, media_id + ".md"), "w", encoding="utf-8") as f:
            f.write(content)
        meta = {"extract_status": "ok", "channel": "A-mcp-note", "media_id": media_id,
                "note_id": note_id, "chars": len(content)}
        with open(os.path.join(STAGE, media_id + ".json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
