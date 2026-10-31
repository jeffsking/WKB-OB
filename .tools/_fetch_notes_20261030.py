#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-29 通道 A · 笔记正文 REST 兜底（多条顺序探测）。

铁律：
  · 命中 200005（日配额耗尽）当日立即停止，禁止重试；
  · 响应体先落盘再解析（禁管道预览，2026-10-20 教训）；
  · note_id = media_id 末段；
  · 220030（条目级永久失败）标记后不重试。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
OUT = os.path.join(ROOT, ".tools", "_doc_content_20261030")
BODIES = os.path.join(ROOT, ".tools", "_kb_sync_bodies")
PLAN = ".tools/_kb_sync_plan.json"
os.makedirs(OUT, exist_ok=True)
os.makedirs(BODIES, exist_ok=True)

import urllib.request


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()


def main():
    plan = json.load(open(PLAN, encoding="utf-8"))
    notes = [x for x in plan["items"] if x["media_id"].startswith("note_")]
    print(f"待取笔记 {len(notes)} 条")
    stop = False
    rep = []
    for it in notes:
        mid = it["media_id"]
        note_id = mid.split("_")[-1]
        print(f"\n=== {it.get('title')}  note_id={note_id}")
        if stop:
            print("  已命中 200005，本条跳过（当日不再请求）")
            rep.append({"media_id": mid, "status": "skipped-quota"})
            continue
        req = urllib.request.Request(
            BASE + "/openapi/note/v1/get_doc_content",
            data=json.dumps({"note_id": note_id}).encode("utf-8"),
            headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                     "Content-Type": "application/json"},
            method="POST")
        p = os.path.join(OUT, note_id + ".json")
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read()
        except Exception as e:  # noqa: BLE001
            print(f"  ! 请求异常 {type(e).__name__} {e}")
            rep.append({"media_id": mid, "status": "error", "err": str(e)[:120]})
            continue
        with open(p, "wb") as f:      # 先落盘，后解析
            f.write(body)
        d = json.loads(body.decode("utf-8", errors="replace"))
        code = d.get("code")
        data = d.get("data") or {}
        content = data.get("content") or ""
        print(f"  code={code} chars={len(content)} msg={d.get('msg') or d.get('message')}")
        if code == 0 and content.strip():
            with open(os.path.join(BODIES, mid + ".md"), "w", encoding="utf-8") as f:
                f.write(content)
            with open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8") as f:
                json.dump({"media_id": mid, "extract_status": "ok", "channel": "A",
                           "chars": len(content), "title": it.get("title"),
                           "extract_method": "REST note/v1/get_doc_content"},
                          f, ensure_ascii=False, indent=1)
            rep.append({"media_id": mid, "status": "ok", "chars": len(content)})
        elif code == 200005:
            print("  → 日配额耗尽，当日停止（不重试）")
            stop = True
            rep.append({"media_id": mid, "status": "quota-exhausted"})
        elif code == 220030:
            rep.append({"media_id": mid, "status": "permanent-fail-220030"})
        else:
            rep.append({"media_id": mid, "status": f"code-{code}"})
    with open(".tools/_note_report_20261030.json", "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
    print("\n===== 汇总 =====")
    for r in rep:
        print(" ", r.get("status"), r["media_id"][-18:], r.get("chars", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
