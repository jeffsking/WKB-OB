#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-21 通道 A：笔记正文抓取（走官方 ima_api.cjs，业务码为唯一判据）。

铁律：API 返回体先落盘再读，禁管道 head/tail 预览（10-20 教训）。
判据：code=0 成功；210001 = note_id 参数错；200005 = 日配额耗尽 → 立即停止不重试。
顺序：按「今日新增优先」排，因日配额实测约 1 次/日。
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
    ("note_3867e2b60070d7dc3f413086d0b0036e_7518291224433921", "7518291224433921", "聚合芯能拜访纪要"),
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
    got = 0
    for media_id, note_id, title in NOTES:
        r = fetch(note_id)
        code = r.get("code")
        if code != 0:
            print(f"[FAIL] {title} -> code={code} msg={r.get('msg')}")
            if code == 200005:
                print("       -> 日配额耗尽，按铁律当日停止，不再重试")
                break
            if code == 210001:
                print("       -> note_id 参数错，检查入参")
            continue
        data = r.get("data") or {}
        content = data.get("content") or ""
        print(f"[OK] {title} -> {len(content)} chars")
        # 先落盘（原始响应全文另存，便于事后复核，绝不预览丢弃）
        with open(os.path.join(STAGE, media_id + ".raw.json"), "w", encoding="utf-8") as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
        if not content.strip():
            print("   (empty) 空正文，不写 .md")
            continue
        with open(os.path.join(STAGE, media_id + ".md"), "w", encoding="utf-8") as f:
            f.write(content)
        meta = {"extract_status": "ok", "channel": "A-rest-note", "media_id": media_id,
                "note_id": note_id, "chars": len(content)}
        with open(os.path.join(STAGE, media_id + ".json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=1)
        got += 1
    print(f"落地暂存 {got} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
